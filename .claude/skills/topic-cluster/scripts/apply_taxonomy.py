#!/usr/bin/env python3
"""Apply an approved taxonomy to the corpus: write membership, update state, validate (ADR-0014).

Membership's single source of truth is each literature note's `topics:` frontmatter. This is the
deterministic, idempotent writer for it — the analog of link_notes.py's `set_related`. The taxonomy
(the human-gated decision) comes in as JSON; this script:

  1. derives citekey -> [slugs] (a note may be a member of several topics — multi-membership),
  2. rewrites each mentioned note's `topics:` line (AI region only) to the quoted-wikilink form
     `["[[slug]]", ...]` so dataview rosters resolve; notes not mentioned are left untouched,
  3. records each mentioned note's current manifest hash in .research/topic_state.json (the
     pending-detector for incremental runs), and
  4. runs the validation pass: coverage, dangling members, empty topics, soft-cap, dangling links.

Re-running with the same taxonomy is a true no-op.

Taxonomy JSON: {"topics": [{"slug","title","scope","members":[ck...]}, ...], "orphans":[ck...]}

Usage (from vault root):
  apply_taxonomy.py --taxonomy taxonomy.json [--cap 3] [--require-full-coverage] [--dry-run]
  apply_taxonomy.py --validate-only           # validate current on-disk state, write nothing
"""
import argparse
import json
import re
import sys
from pathlib import Path

import corpus


def set_topics(fm, slugs):
    val = "[" + ", ".join(f'"[[{s}]]"' for s in sorted(set(slugs))) + "]"
    line = f"topics: {val}"
    if re.search(r"^topics:.*$", fm, flags=re.M):
        return re.sub(r"^topics:.*$", line, fm, flags=re.M)
    return fm.rstrip("\n")[:-3] + line + "\n---\n" if fm.endswith("---\n") else fm  # insert before ---


def read_json(p, default):
    p = Path(p)
    return json.loads(p.read_text()) if p.exists() else default


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--taxonomy", help="approved taxonomy JSON")
    ap.add_argument("--cap", type=int, default=3, help="soft cap on memberships per note")
    ap.add_argument("--require-full-coverage", action="store_true",
                    help="error if any corpus note is neither a member nor an explicit orphan")
    ap.add_argument("--validate-only", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--vault", default=None)
    args = ap.parse_args()

    vault = Path(args.vault).resolve() if args.vault else corpus.find_vault(Path.cwd())
    notes = corpus.iter_notes(vault)
    by_ck = {n["citekey"]: n for n in notes}
    present = set(by_ck)
    slugs_on_disk = {p.stem for p in corpus.iter_topic_paths(vault)}
    problems, warnings = [], []

    if args.validate_only:
        membership = {ck: set(n["topics"]) for ck, n in by_ck.items() if n["topics"]}
    else:
        if not args.taxonomy:
            ap.error("pass --taxonomy or --validate-only")
        tax = read_json(args.taxonomy, {})
        topics = tax.get("topics", [])
        # orphans may be bare citekeys or {"citekey","reason"} objects (the Phase-A schema) — accept both
        orphans = {o["citekey"] if isinstance(o, dict) else o for o in tax.get("orphans", [])}

        # 1) derive citekey -> {slugs}
        membership = {}
        for t in topics:
            for ck in t.get("members", []):
                membership.setdefault(ck, set()).add(t["slug"])

        # structural validation (before any write)
        for t in topics:
            if not t.get("members"):
                problems.append(f"topic '{t['slug']}' has no members")
            for ck in t.get("members", []):
                if ck not in present:
                    problems.append(f"topic '{t['slug']}' lists non-existent member {ck}")
        for ck, slugs in membership.items():
            if len(slugs) > args.cap:
                warnings.append(f"{ck} is in {len(slugs)} topics (> cap {args.cap}): {sorted(slugs)}")
        mentioned = set(membership) | orphans
        uncovered = present - mentioned
        if uncovered:
            msg = f"{len(uncovered)} corpus notes not covered by taxonomy (would stay pending)"
            (problems if args.require_full_coverage else warnings).append(
                msg + ": " + ", ".join(sorted(uncovered)[:10]) + ("…" if len(uncovered) > 10 else ""))

        if problems:
            for p in problems:
                print(f"  ✗ {p}", file=sys.stderr)
            print(f"[apply_taxonomy] {len(problems)} problem(s) — refusing to write.", file=sys.stderr)
            sys.exit(1)

        # 2) write membership (idempotent, AI region only) + 3) update state
        manifest = read_json(vault / ".research" / "manifest.json", {})
        state = read_json(vault / ".research" / "topic_state.json", {})
        changed = 0
        for ck in sorted(mentioned):
            path = vault / "literature" / f"@{ck}.md"
            if not path.exists():
                continue
            text = path.read_text()
            fm, body, human = corpus.split_regions(text)
            new_fm = set_topics(fm, membership.get(ck, set()))
            if new_fm != fm and not args.dry_run:
                path.write_text(new_fm + body + human)
            changed += int(new_fm != fm)
            h = manifest.get(ck, {}).get("hash")
            if h is not None:
                state[ck] = h
        if not args.dry_run:
            (vault / ".research" / "topic_state.json").write_text(
                json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True))
        verb = "would update" if args.dry_run else "updated"
        print(f"[apply_taxonomy] {verb} {changed} notes' topics:; "
              f"{len(topics)} topics, {len(orphans)} orphans, {len(mentioned)} covered")

    # 4) post-write validation: every membership slug must have a topic note
    dangling = sorted({s for slugs in membership.values() for s in slugs} - slugs_on_disk)
    if dangling:
        warnings.append(f"{len(dangling)} membership link(s) point at a missing topics/<slug>.md "
                        f"(write the topic note): {', '.join(dangling[:10])}")
    for w in warnings:
        print(f"  ⚠ {w}", file=sys.stderr)
    if not warnings and not args.dry_run:
        print("[apply_taxonomy] validation clean.", file=sys.stderr)


if __name__ == "__main__":
    main()
