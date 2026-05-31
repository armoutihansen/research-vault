#!/usr/bin/env python3
"""Emit the LLM clustering input for topic-cluster (ADR-0014).

Bootstrap mode: a compact representation of *every* literature note — citekey, title, year,
keywords, related[] edges, Louvain community id (prior), and the Summary paragraph — small enough
(~130 tokens/note) that all ~469 fit one Opus 1M-context taxonomy agent, so the partition is one
globally consistent decision (no cross-batch merge).

Incremental mode: only *pending* notes (topics empty, or manifest content-hash changed since last
clustered — tracked in .research/topic_state.json), plus the current taxonomy (slug/title/scope +
member rosters) so the agent assigns each pending note to an anchor or flags a new topic.

Usage (from vault root):
  make_input.py --mode bootstrap   [--out .research/tmp/taxonomy_input.json] [--summary-chars 600]
  make_input.py --mode incremental [--out ...]
Prints a one-line summary to stderr; the JSON goes to --out (or stdout). Standard library only.
"""
import argparse
import json
import sys
from pathlib import Path

import corpus


def read_manifest(vault):
    p = vault / ".research" / "manifest.json"
    return json.loads(p.read_text()) if p.exists() else {}


def read_state(vault):
    p = vault / ".research" / "topic_state.json"
    return json.loads(p.read_text()) if p.exists() else {}


def read_topics(vault, notes):
    """Current taxonomy from topics/<slug>.md frontmatter + dataview-equivalent member rosters
    (membership lives in lit notes' topics:, so we derive rosters from `notes`)."""
    members = {}
    for n in notes:
        for slug in n["topics"]:
            members.setdefault(slug, []).append(n["citekey"])
    tax = []
    for p in corpus.iter_topic_paths(vault):
        fm, _body, _human = corpus.split_regions(p.read_text())
        slug = corpus._scalar(fm, "slug") or p.stem
        tax.append({
            "slug": slug,
            "title": corpus._scalar(fm, "title"),
            "scope": corpus._scalar(fm, "scope"),
            "members": sorted(members.get(slug, [])),
        })
    return tax


def is_pending(note, manifest, state):
    if not note["topics"]:
        return True
    cur = manifest.get(note["citekey"], {}).get("hash")
    return cur is not None and cur != state.get(note["citekey"])


def rep(note, community, summary_chars):
    s = note["summary"]
    if len(s) > summary_chars:
        s = s[:summary_chars].rsplit(" ", 1)[0] + "…"
    r = {
        "citekey": note["citekey"],
        "title": note["title"],
        "year": note["year"],
        "keywords": note["keywords"],
        "related": note["related"],
        "community": community.get(note["citekey"]),
        "summary": s,
    }
    if note["topics"]:
        r["current_topics"] = note["topics"]
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["bootstrap", "incremental"], required=True)
    ap.add_argument("--out", default=None)
    ap.add_argument("--summary-chars", type=int, default=600)
    ap.add_argument("--vault", default=None)
    args = ap.parse_args()

    vault = Path(args.vault).resolve() if args.vault else corpus.find_vault(Path.cwd())
    notes = corpus.iter_notes(vault)
    community = corpus.communities(notes)

    if args.mode == "bootstrap":
        selected = notes
        taxonomy = []
    else:
        manifest, state = read_manifest(vault), read_state(vault)
        selected = [n for n in notes if is_pending(n, manifest, state)]
        taxonomy = read_topics(vault, notes)

    payload = {
        "mode": args.mode,
        "granularity": "idea-generativity: smallest cluster with internal tension worth a "
                       "candidate idea (~10-25 members, ~20-35 topics; an outcome, not a target)",
        "n_corpus": len(notes),
        "n_selected": len(selected),
        "community_prior": bool(community),
        "notes": [rep(n, community, args.summary_chars) for n in selected],
    }
    if args.mode == "incremental":
        payload["taxonomy"] = taxonomy

    out = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(out)
    else:
        print(out)
    n_comm = len(set(community.values())) if community else 0
    print(f"[make_input] mode={args.mode} corpus={len(notes)} selected={len(selected)} "
          f"communities={n_comm}", file=sys.stderr)


if __name__ == "__main__":
    main()
