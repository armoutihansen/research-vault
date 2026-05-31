#!/usr/bin/env python3
"""Apply an approved area grouping: stamp each topic's parent `area:` link + validate (ADR-0014).

The upper level of the Layer-2 hierarchy. A topic's single source of truth for its parent is the
`area:` link in its own frontmatter (area notes derive their child roster via dataview). This is the
idempotent writer for it — the analog of apply_taxonomy.py one level up. The area map (the human-gated
grouping) comes in as JSON; this script:

  1. derives topic-slug -> area-slug (single parent — errors if a topic is in >1 area),
  2. rewrites each existing topic note's `area:` line (AI region only, idempotent),
  3. validates: every topic note has exactly one area; every mapped topic has a topic note (else it's
     not written yet); no topic note left without an area.

Re-running with the same map is a true no-op.

Area map JSON: {"areas": [{"slug","title","scope","topics":[topic-slug,...]}, ...]}

Usage (from vault root, via `uv run`):
  apply_areas.py --areas .research/tmp/area_map.json [--dry-run]
  apply_areas.py --validate-only
"""
import argparse
import json
import re
import sys
from pathlib import Path

import corpus


def set_area(fm, area_slug):
    line = f'area: "[[{area_slug}]]"'
    if re.search(r"^area:.*$", fm, flags=re.M):
        return re.sub(r"^area:.*$", line, fm, flags=re.M)
    return fm.rstrip("\n")[:-3] + line + "\n---\n" if fm.endswith("---\n") else fm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--areas", help="approved area-map JSON")
    ap.add_argument("--validate-only", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--vault", default=None)
    args = ap.parse_args()

    vault = Path(args.vault).resolve() if args.vault else corpus.find_vault(Path.cwd())
    topic_paths = {p.stem: p for p in corpus.iter_topic_paths(vault)}  # existing topic notes
    area_paths = {p.stem for p in (vault / "areas").glob("*.md")
                  if re.search(r"^type:\s*area\s*$", p.read_text()[:400], flags=re.M)} \
        if (vault / "areas").exists() else set()
    problems, warnings = [], []

    if args.validate_only:
        # check on-disk topic notes' area links
        missing_area, dangling = [], []
        for slug, p in topic_paths.items():
            fm, _b, _h = corpus.split_regions(p.read_text())
            links = corpus.WIKILINK.findall(corpus._scalar(fm, "area"))
            if not links:
                missing_area.append(slug)
            elif links[0].split("/")[-1] not in area_paths:
                dangling.append(f"{slug}->{links[0]}")
        if missing_area:
            warnings.append(f"{len(missing_area)} topic notes have no area: {', '.join(missing_area[:10])}")
        if dangling:
            warnings.append(f"{len(dangling)} topic notes point at a missing area note: {', '.join(dangling[:10])}")
    else:
        if not args.areas:
            ap.error("pass --areas or --validate-only")
        amap = json.loads(Path(args.areas).read_text())
        areas = amap.get("areas", [])

        topic_to_area = {}
        for a in areas:
            if not a.get("topics"):
                problems.append(f"area '{a['slug']}' has no topics")
            for ts in a.get("topics", []):
                if ts in topic_to_area:
                    problems.append(f"topic '{ts}' is in >1 area ({topic_to_area[ts]} and {a['slug']}) "
                                    f"— single-parent violated")
                topic_to_area[ts] = a["slug"]
        if problems:
            for p in problems:
                print(f"  ✗ {p}", file=sys.stderr)
            print("[apply_areas] refusing to write.", file=sys.stderr)
            sys.exit(1)

        changed = written = 0
        for ts, area_slug in sorted(topic_to_area.items()):
            p = topic_paths.get(ts)
            if not p:
                warnings.append(f"mapped topic '{ts}' has no topic note yet (write it, then re-run)")
                continue
            written += 1
            text = p.read_text()
            fm, body, human = corpus.split_regions(text)
            new_fm = set_area(fm, area_slug)
            if new_fm != fm and not args.dry_run:
                p.write_text(new_fm + body + human)
            changed += int(new_fm != fm)
        # topic notes that exist but aren't in the map
        for slug in sorted(set(topic_paths) - set(topic_to_area)):
            warnings.append(f"topic note '{slug}' is in no area")
        verb = "would stamp" if args.dry_run else "stamped"
        print(f"[apply_areas] {verb} area: on {changed} of {written} present topic notes "
              f"({len(areas)} areas, {len(topic_to_area)} topics mapped)")

    for w in warnings:
        print(f"  ⚠ {w}", file=sys.stderr)
    if not warnings and not args.dry_run:
        print("[apply_areas] validation clean.", file=sys.stderr)


if __name__ == "__main__":
    main()
