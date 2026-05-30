#!/usr/bin/env python3
"""Print the in-scope citekeys a note *might* reference, to shortlist an LLM linking pass.

Given a note, returns every in-scope candidate whose surname (or a distinctive title token) appears
in the note's AI region — narrowing 469 candidates to the few dozen worth showing an agent. The
agent then decides which the note genuinely cites and supplies the exact display span to wrap.

Usage:  link_candidates.py --citekey Samuelson1988
Output: one `citekey<TAB>Year<TAB>Authors — Title` line per candidate (already-linked ones excluded).
"""
import argparse
import json
import os
import re
from pathlib import Path

FENCE = "%% ─── below is yours; regeneration never touches it ─── %%"


def find_vault(start):
    p = Path(start).resolve()
    for cand in [p, *p.parents]:
        if (cand / ".research").exists() or (cand / "CONTEXT.md").exists():
            return cand
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--citekey", required=True)
    ap.add_argument("--vault", default=None)
    args = ap.parse_args()
    vault = Path(args.vault).resolve() if args.vault else find_vault(os.getcwd())
    index = json.loads((vault / ".research" / "link_index.json").read_text())
    note = (vault / "literature" / f"@{args.citekey}.md").read_text()
    ai = note.split(FENCE)[0]
    already = set(re.findall(r"\[\[@([^\]|]+)\|", ai))
    words = set(re.findall(r"[A-Za-z'’\-]{3,}", ai))
    title_words = set(re.findall(r"[a-z]{5,}", ai.lower()))

    rows = []
    for ck, m in index.items():
        if ck == args.citekey or ck in already:
            continue
        year = str(m.get("year") or "")
        # a surname hit only counts if the candidate's year also appears in the note (kills
        # coincidental common-surname matches); title overlap is the year-less fallback.
        surn_hit = bool(year) and year in ai and any(s in words for s in m["surnames"] if len(s) >= 3)
        tt = set(re.findall(r"[a-z]{5,}", (m["title"] or "").lower()))
        title_hit = len(tt & title_words) >= 2
        if surn_hit or title_hit:
            authors = ", ".join(m["surnames"][:3]) + (" et al." if len(m["surnames"]) > 3 else "")
            rows.append((ck, m["year"], authors, m["title"]))
    rows.sort(key=lambda r: (r[1], r[0]))
    for ck, year, authors, title in rows:
        print(f"{ck}\t{year}\t{authors} — {title}")


if __name__ == "__main__":
    main()
