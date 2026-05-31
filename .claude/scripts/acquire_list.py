#!/usr/bin/env python3
"""acquire_list — turn verified biblio records into an acquire-list (ADR-0015).

The acquire-list is how the system says *"here is what you need and where to get it"*: papers a skill
found relevant that are **not yet in your library**, each with its DOI and (when open) a direct link,
for you to acquire and route back via Zotero → lit-sync. This helper takes biblio records (already
existence-verified — only `found:true` records belong here) and **dedups them against the vault** (by
DOI, with a normalized-title fallback), emitting the papers you don't already have.

It never fetches anything — it only reads your local literature notes' `doi:`/`title:` and the records
you pass in. Run via `uv run`. Standard library only.

Usage (from vault root):
  uv run python .claude/scripts/acquire_list.py --records records.json [--format md|json]
    records.json: a biblio `search`/`verify` payload — a list of records, or {"results":[...]}.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path


def find_vault(start):
    p = Path(start).resolve()
    for c in [p, *p.parents]:
        if (c / ".research").exists() or (c / "CONTEXT.md").exists():
            return c
    return p


def norm_doi(d):
    return (d or "").strip().strip('"').lower().replace("https://doi.org/", "").replace("doi.org/", "")


def norm_title(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return " ".join(re.findall(r"[a-z0-9]+", t))


def vault_index(vault):
    dois, titles = set(), set()
    for p in (vault / "literature").glob("@*.md"):
        head = p.read_text()[:1200]
        m = re.search(r"^doi:\s*(.*)$", head, re.M)
        if m and norm_doi(m.group(1)):
            dois.add(norm_doi(m.group(1)))
        m = re.search(r'^title:\s*"?(.*?)"?\s*$', head, re.M)
        if m and norm_title(m.group(1)):
            titles.add(norm_title(m.group(1)))
    return dois, titles


def load_records(path):
    data = json.loads(Path(path).read_text())
    if isinstance(data, dict):
        data = data.get("results") or data.get("records") or data.get("ideas") or []
    return [r for r in data if isinstance(r, dict)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--records", required=True, help="biblio search/verify JSON (list or {results:[...]})")
    ap.add_argument("--format", choices=["md", "json"], default="md")
    ap.add_argument("--vault", default=None)
    args = ap.parse_args()

    vault = Path(args.vault).resolve() if args.vault else find_vault(Path.cwd())
    dois, titles = vault_index(vault)
    records = load_records(args.records)

    need, have, unverified = [], 0, 0
    for r in records:
        if not r.get("found", True):  # only existence-verified records belong on an acquire-list
            unverified += 1
            continue
        d, t = norm_doi(r.get("doi")), norm_title(r.get("title"))
        if (d and d in dois) or (t and t in titles):
            have += 1
        else:
            need.append(r)

    if args.format == "json":
        print(json.dumps({"acquire": need, "already_in_vault": have, "skipped_unverified": unverified},
                         ensure_ascii=False, indent=2))
        return

    print(f"## Acquire-list — {len(need)} paper(s) not in your library")
    if have or unverified:
        print(f"<!-- {have} already in vault (skipped); {unverified} unverified (skipped — not real records) -->")
    for r in need:
        au = r.get("authors") or []
        who = au[0].split(",")[0] if au else "?"
        who = f"{who} et al." if len(au) > 2 else " & ".join(a.split(",")[0] for a in au) if au else "?"
        doi = norm_doi(r.get("doi"))
        link = f"[open access]({r['oa_url']})" if r.get("is_oa") and r.get("oa_url") else "via library/DOI"
        doi_s = f"https://doi.org/{doi}" if doi else "(no DOI)"
        print(f"- **{r.get('title','(untitled)')}** — {who} ({r.get('year','?')}), "
              f"{r.get('venue') or '?'}. {doi_s} · {link}")
    if not need:
        print("_Nothing to acquire — every verified record is already in your library._")


if __name__ == "__main__":
    main()
