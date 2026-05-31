#!/usr/bin/env python3
"""Deterministic annotation of a proposed taxonomy for the human gate (ADR-0014).

Replaces the old LLM "critic" phase. The judgment calls (grab-bag? duplicate?) are the human's; this
just lays out the facts they need to make them: size distribution, coverage/orphans, multi-membership
and cap/singleton flags, and the **graph cross-check** — how well the proposed thematic partition
agrees with the Louvain citation communities (a topic that scatters a tight community, or a community
shredded across many topics, is worth a human look; it may be a real cross-cutting theme or an error).

Reads a proposed taxonomy JSON ({"topics":[{slug,title,scope,members[]}], "orphans":[...]}); writes
nothing. Run via `uv run` so the networkx prior is present. Standard library + networkx.

Usage (from vault root):
  report_taxonomy.py --taxonomy .research/tmp/proposed_taxonomy.json [--cap 3]
"""
import argparse
import collections
import json
import statistics
from pathlib import Path

import corpus


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--taxonomy", required=True)
    ap.add_argument("--cap", type=int, default=3)
    ap.add_argument("--vault", default=None)
    args = ap.parse_args()

    vault = Path(args.vault).resolve() if args.vault else corpus.find_vault(Path.cwd())
    notes = corpus.iter_notes(vault)
    present = {n["citekey"] for n in notes}
    tax = json.loads(Path(args.taxonomy).read_text())
    topics = tax.get("topics", [])
    orphans = {o["citekey"] if isinstance(o, dict) else o for o in tax.get("orphans", [])}
    community = corpus.communities(notes)  # ck -> Louvain id ({} if networkx missing)

    membership = collections.defaultdict(set)  # ck -> {slug}
    for t in topics:
        for ck in t.get("members", []):
            membership[ck].add(t["slug"])

    sizes = sorted(len(t.get("members", [])) for t in topics)
    member_notes = set(membership)
    mentioned = member_notes | orphans
    uncovered = sorted(present - mentioned)
    unknown = sorted(member_notes - present)  # members not in the corpus

    print(f"\n=== Taxonomy proposal: {len(topics)} topics ===")
    if sizes:
        print(f"  sizes: min {sizes[0]} · median {int(statistics.median(sizes))} · "
              f"mean {statistics.mean(sizes):.1f} · max {sizes[-1]}  (total memberships {sum(sizes)})")
    print(f"  coverage: {len(present)} corpus notes — {len(member_notes)} placed, "
          f"{len(orphans)} orphaned, {len(uncovered)} UNCOVERED")
    multi = {ck: s for ck, s in membership.items() if len(s) > 1}
    over = {ck: s for ck, s in membership.items() if len(s) > args.cap}
    print(f"  multi-membership: {len(multi)} notes in >1 topic; {len(over)} over cap {args.cap}")

    print("\n--- per topic (size · graph purity) ---")
    for t in sorted(topics, key=lambda x: -len(x.get("members", []))):
        mem = t.get("members", [])
        cids = [community[ck] for ck in mem if ck in community]
        if cids:
            dom, dom_n = collections.Counter(cids).most_common(1)[0]
            purity = dom_n / len(cids)
            ncomm = len(set(cids))
            graph = f"purity {purity:.0%} (dom comm {dom}; spans {ncomm} comm)"
        else:
            graph = "no community prior"
        print(f"  {len(mem):>3}  {t['slug']:<34} {graph}")

    # flags for the human
    flags = []
    singles = [t["slug"] for t in topics if len(t.get("members", [])) <= 1]
    if singles:
        flags.append(f"singleton/empty topics (size ≤1): {', '.join(singles)}")
    if over:
        flags.append("over-cap notes: " + ", ".join(f"{ck}({len(s)})" for ck, s in sorted(over.items())))
    if unknown:
        flags.append(f"members not in corpus: {', '.join(unknown[:10])}")
    if uncovered:
        flags.append(f"{len(uncovered)} uncovered notes: {', '.join(uncovered[:10])}"
                     + ("…" if len(uncovered) > 10 else ""))
    if community:
        # heterogeneous topics: many member-communities, low dominant share
        for t in topics:
            cids = [community[ck] for ck in t.get("members", []) if ck in community]
            if len(cids) >= 5:
                dom_n = collections.Counter(cids).most_common(1)[0][1]
                if dom_n / len(cids) < 0.5 and len(set(cids)) >= 4:
                    flags.append(f"heterogeneous: '{t['slug']}' spans {len(set(cids))} citation "
                                 f"communities (dom {dom_n}/{len(cids)}) — real cross-cut or grab-bag?")
        # fragmented communities: one community scattered across many topics
        comm_topics = collections.defaultdict(set)
        for ck, slugs in membership.items():
            if ck in community:
                comm_topics[community[ck]].update(slugs)
        for cid, slugs in sorted(comm_topics.items()):
            if len(slugs) >= 5:
                flags.append(f"fragmented: citation community {cid} is split across {len(slugs)} topics")

    print("\n--- flags for review ---")
    print("\n".join(f"  ⚠ {f}" for f in flags) if flags else "  (none)")
    print()


if __name__ == "__main__":
    main()
