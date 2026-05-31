#!/usr/bin/env python3
"""biblio — the ONLY path the system uses to touch external literature (ADR-0015).

Open-access by construction: it queries open, storable bibliographic APIs (OpenAlex, Crossref) for
**metadata + abstracts only**, and **never fetches full-text**. The safety guarantee is structural —
every network call goes through `_get`, which refuses any host not on `ALLOWED_HOSTS`. There is no
method that downloads a PDF; `oa_url` is returned as a *pointer* for the acquire-list, never fetched.

Two jobs:
  - discovery   `search --query "..."`         find recent/relevant work
  - verification `verify --doi ...` / `--title` resolve a citation to a REAL record (anti-hallucination)

Full-text never comes from here — it enters only through the user's Zotero (ADR-0015). Run via `uv run`.
Standard library only. Optional polite-pool email via env BIBLIO_MAILTO.

Usage (from vault root):
  uv run python .claude/scripts/biblio.py verify --doi 10.1086/262063
  uv run python .claude/scripts/biblio.py verify --title "Formal and Real Authority in Organizations" --year 1997
  uv run python .claude/scripts/biblio.py search --query "predictive completeness" --from-year 2023 --limit 10 --sort recency
  uv run python .claude/scripts/biblio.py --self-test     # verify the open-only guard
"""
import argparse
import difflib
import json
import os
import re
import sys
import unicodedata
import urllib.parse
import urllib.request

# The open-only guarantee: these are the ONLY hosts this client may ever contact. Both serve open,
# storable metadata (OpenAlex = CC0; Crossref = open). No publisher / PDF / full-text host is here.
ALLOWED_HOSTS = {"api.openalex.org", "api.crossref.org"}
MAILTO = os.environ.get("BIBLIO_MAILTO", "").strip()
UA = f"research-vault-biblio/0.1 (https://github.com/armoutihansen/research-vault{'; mailto:' + MAILTO if MAILTO else ''})"


class FullTextRefused(Exception):
    """Raised if anything ever tries to fetch a non-allowlisted (e.g. full-text/publisher) host."""


def _get(url, timeout=30):
    host = urllib.parse.urlsplit(url).hostname or ""
    if host not in ALLOWED_HOSTS:
        raise FullTextRefused(
            f"biblio refuses to fetch host {host!r}: only open-metadata APIs {sorted(ALLOWED_HOSTS)} "
            f"are allowed; full-text/other hosts are never fetched (ADR-0015).")
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def fold(s):
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().strip()


def title_sim(a, b):
    return difflib.SequenceMatcher(None, " ".join(re.findall(r"[a-z0-9]+", fold(a))),
                                   " ".join(re.findall(r"[a-z0-9]+", fold(b)))).ratio()


# ---------- OpenAlex ----------
def _oa_abstract(inv):
    if not inv:
        return ""
    pos = [(i, w) for w, idxs in inv.items() for i in idxs]
    pos.sort()
    return " ".join(w for _, w in pos)


def _oa_record(work):
    if not work:
        return None
    oa = work.get("open_access") or {}
    loc = work.get("best_oa_location") or {}
    src = (work.get("primary_location") or {}).get("source") or {}
    return {
        "found": True,
        "source": "openalex",
        "id": work.get("id"),
        "doi": (work.get("doi") or "").replace("https://doi.org/", "") or None,
        "title": work.get("display_name") or work.get("title"),
        "authors": [a.get("author", {}).get("display_name") for a in (work.get("authorships") or [])],
        "year": work.get("publication_year"),
        "venue": src.get("display_name"),
        "type": work.get("type"),
        "is_oa": bool(oa.get("is_oa")),
        # POINTER ONLY — surfaced for the acquire-list; this client never fetches it.
        "oa_url": oa.get("oa_url") or loc.get("landing_page_url"),
        "cited_by_count": work.get("cited_by_count"),
        "abstract": _oa_abstract(work.get("abstract_inverted_index")),
    }


def oa_by_doi(doi):
    doi = doi.replace("https://doi.org/", "").strip()
    try:
        return _oa_record(_get(f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def oa_search(query, from_year=None, limit=10, sort="relevance"):
    params = {"search": query, "per-page": min(limit, 50)}
    if from_year:
        params["filter"] = f"from_publication_date:{from_year}-01-01"
    if sort == "recency":
        params["sort"] = "publication_date:desc"
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    return [_oa_record(w) for w in (_get(url).get("results") or [])]


def oa_by_title(title, year=None):
    params = {"filter": f"title.search:{title}", "per-page": 10}
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    cands = [_oa_record(w) for w in (_get(url).get("results") or [])]
    return _best_title_match(cands, title, year)


# ---------- Crossref (verify fallback + preprint↔published relations) ----------
def _cr_record(msg):
    if not msg:
        return None
    rel = {}
    for k, v in (msg.get("relation") or {}).items():
        if "preprint" in k or "version" in k:
            rel[k] = [d.get("id") for d in (v if isinstance(v, list) else [v])]
    issued = (msg.get("issued") or {}).get("date-parts") or [[None]]
    return {
        "found": True,
        "source": "crossref",
        "id": msg.get("DOI"),
        "doi": msg.get("DOI"),
        "title": (msg.get("title") or [None])[0],
        "authors": [f"{a.get('family','')}, {a.get('given','')}".strip(", ") for a in (msg.get("author") or [])],
        "year": issued[0][0],
        "venue": (msg.get("container-title") or [None])[0],
        "type": msg.get("type"),
        "is_oa": None,
        "oa_url": None,
        "cited_by_count": msg.get("is-referenced-by-count"),
        "relations": rel,  # e.g. {"is-preprint-of": [doi]} — powers working-paper→published detection
        "abstract": re.sub(r"<[^>]+>", "", msg.get("abstract", "") or "").strip(),
    }


def cr_by_doi(doi):
    doi = doi.replace("https://doi.org/", "").strip()
    try:
        return _cr_record(_get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}").get("message"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


# ---------- shared ----------
def _best_title_match(cands, title, year):
    best, best_score = None, 0.0
    for c in cands:
        if not c:
            continue
        sim = title_sim(title, c.get("title") or "")
        if year and c.get("year"):
            sim *= 1.0 if abs(int(c["year"]) - int(year)) <= 1 else 0.7
        if sim > best_score:
            best, best_score = c, sim
    if best and best_score >= 0.8:
        return {**best, "confidence": round(best_score, 3)}
    return {"found": False, "confidence": round(best_score, 3),
            "note": "no confident match (>=0.80) — treat as UNVERIFIED"}


def verify(doi=None, title=None, authors=None, year=None):
    """Resolve a citation to a REAL record. OpenAlex first, Crossref fallback. {found:false} if neither."""
    if doi:
        rec = oa_by_doi(doi) or cr_by_doi(doi)
        return rec or {"found": False, "note": f"DOI {doi} not found in OpenAlex or Crossref — UNVERIFIED"}
    if title:
        rec = oa_by_title(title, year)
        if rec.get("found"):
            return rec
        # Crossref bibliographic-query fallback
        params = {"query.bibliographic": title, "rows": 5}
        if authors:
            params["query.author"] = authors
        msg = _get("https://api.crossref.org/works?" + urllib.parse.urlencode(params)).get("message", {})
        cands = [_cr_record(m) for m in (msg.get("items") or [])]
        return _best_title_match(cands, title, year)
    raise SystemExit("verify needs --doi or --title")


def main():
    ap = argparse.ArgumentParser(description="Open-only bibliographic lookup (ADR-0015).")
    sub = ap.add_subparsers(dest="cmd")
    v = sub.add_parser("verify", help="resolve a citation to a real record")
    v.add_argument("--doi"); v.add_argument("--title"); v.add_argument("--authors"); v.add_argument("--year")
    s = sub.add_parser("search", help="discover recent/relevant work")
    s.add_argument("--query", required=True); s.add_argument("--from-year")
    s.add_argument("--limit", type=int, default=10); s.add_argument("--sort", choices=["relevance", "recency"], default="relevance")
    ap.add_argument("--self-test", action="store_true", help="verify the open-only host guard")
    args = ap.parse_args()

    if args.self_test:
        for bad in ["https://www.sciencedirect.com/science/article/pii/x.pdf",
                    "https://arxiv.org/pdf/2404.10111.pdf", "http://sci-hub.se/10.1/x"]:
            try:
                _get(bad); print(f"  FAIL: fetched {bad}"); sys.exit(1)
            except FullTextRefused:
                print(f"  ✓ refused {urllib.parse.urlsplit(bad).hostname}")
        print("[biblio] open-only guard OK — only", sorted(ALLOWED_HOSTS), "are fetchable.")
        return

    if args.cmd == "verify":
        print(json.dumps(verify(args.doi, args.title, args.authors, args.year), ensure_ascii=False, indent=2))
    elif args.cmd == "search":
        recs = oa_search(args.query, args.from_year, args.limit, args.sort)
        print(json.dumps({"query": args.query, "n": len(recs), "results": recs}, ensure_ascii=False, indent=2))
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
