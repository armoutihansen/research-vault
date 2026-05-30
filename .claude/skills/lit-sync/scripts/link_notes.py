#!/usr/bin/env python3
"""Resolve in-scope citations in literature notes into Obsidian wikilinks (ADR: citation linking).

A literature note's `## Connections` (and the rest of its AI region) names related work in prose
("Manzini & Mariotti (2007)", "Tversky–Kahneman 1974"). This pass turns each mention of an
*in-scope* paper — one that has, or will have, a note — into a piped wikilink
`[[@citekey|Manzini & Mariotti (2007)]]`, and rebuilds the `related:` frontmatter as the citekey
edge-list. Out-of-scope citations (Luce 1959, Savage 1954) stay plain prose. Obsidian's backlinks
make the graph symmetric for free, and unresolved links to not-yet-written notes resolve the moment
those notes land — so this can run before the backfill is complete.

The writer is *validate-and-augment*, not strip-and-replace: it keeps any existing valid wikilink,
adds freshly resolved ones, drops links whose citekey is no longer in scope, and rebuilds `related:`
from the union. That makes it idempotent and safe to layer an LLM enrichment pass on top of the
deterministic matches. Everything below the human fence is never touched.

Index: `.research/link_index.json` (committed, regenerable) maps every in-scope citekey to its
authors/year/title. Build/refresh it with --rebuild-index (needs Zotero running, via enumerate.py).

Usage (from the vault root):
  link_notes.py --all                      # link every literature/@*.md
  link_notes.py --citekey Manzini2014      # one note
  link_notes.py --citekey X --add-links links.json   # apply an LLM enrichment's resolved links
  link_notes.py --rebuild-index            # refresh the candidate index from Zotero
  link_notes.py --all --dry-run            # report, write nothing

Standard library only.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

FENCE = "%% ─── below is yours; regeneration never touches it ─── %%"
HERE = Path(__file__).resolve().parent

# A surname cluster (Caps words joined by & / and / , / en- or em-dash) followed by a nearby year.
_NAME = r"[A-Z][A-Za-z'’]+(?:[-–][A-Z][A-Za-z'’]+)?"
SPAN_RE = re.compile(
    rf"({_NAME}(?:\s*(?:&|and|,|–|—|-)\s*(?:and\s+)?{_NAME}){{0,3}})\s*\(?(?:\w+\.\s*)?(\d{{4}})[a-z]?\)?"
)
# An already-present piped wikilink: [[@citekey|display]]  (display is what the reader sees).
LINK_RE = re.compile(r"\[\[@([^\]|]+)\|([^\]]+)\]\]")


def find_vault(start):
    p = Path(start).resolve()
    for cand in [p, *p.parents]:
        if (cand / ".research").exists() or (cand / "CONTEXT.md").exists():
            return cand
    return p


def rebuild_index(vault, index_path):
    """Run enumerate.py over the full in-scope set and cache citekey -> {surnames, year, title}."""
    tmp = vault / ".research" / "tmp" / "scope_index.json"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [sys.executable, str(HERE / "enumerate.py"),
         "--status", "new,changed,unchanged", "--vault", str(vault), "--out", str(tmp)],
        check=True, capture_output=True, text=True,
    )
    payload = json.loads(tmp.read_text())
    tmp.unlink(missing_ok=True)
    index = {}
    for it in payload["items"]:
        surnames = [a.split(",")[0].strip() for a in it.get("authors", []) if a.split(",")[0].strip()]
        index[it["citekey"]] = {
            "surnames": surnames,
            "year": str(it.get("year", "")),
            "title": it.get("title", ""),
        }
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2, sort_keys=True))
    return index


def load_index(vault, rebuild=False):
    index_path = vault / ".research" / "link_index.json"
    if rebuild or not index_path.exists():
        return rebuild_index(vault, index_path)
    return json.loads(index_path.read_text())


def title_tokens(title):
    return set(re.findall(r"[a-z]{4,}", (title or "").lower()))


def resolve_span(names, year, context, index):
    """Map a (surname-cluster, year) citation span to a unique in-scope citekey, or None.

    Ambiguity is common — e.g. "Tversky–Kahneman (1992)" matches both Tversky1992 (Tversky, Kahneman)
    and Simonson1992 (Simonson, Tversky) on surname+year. Rank candidates by, in order: leading-surname
    match (the span's first author == the candidate's first author), how many of the span's surnames
    the candidate covers, then title-token overlap with the surrounding paragraph. Ties break on citekey
    so the result is deterministic across processes (independent of dict/hash order).
    """
    span_surn = [t.split("-")[0].split("–")[0] for t in re.findall(r"[A-Z][A-Za-z'’\-–]+", names)]
    span_set = set(span_surn)
    cands = [ck for ck, m in index.items()
             if m["year"] == year and (set(m["surnames"]) & span_set
                                       or any(s in names for s in m["surnames"]))]
    if len(cands) <= 1:
        return cands[0] if cands else None
    ctx = set(re.findall(r"[a-z]{4,}", context.lower()))

    def score(ck):
        m = index[ck]
        cand_surn = [s.split("-")[0].split("–")[0] for s in m["surnames"]]
        lead = 1 if (cand_surn and span_surn and cand_surn[0] == span_surn[0]) else 0
        n_match = len(set(cand_surn) & span_set)
        t_overlap = len(title_tokens(m["title"]) & ctx)
        return (lead, n_match, t_overlap)

    return max(sorted(cands), key=score)  # sorted() → deterministic tie-break by citekey


def split_regions(text):
    """Return (frontmatter, ai_body, human_region). ai_body is between frontmatter and the fence."""
    fm = ""
    rest = text
    if text.startswith("---\n"):
        end = text.index("\n---\n", 4) + len("\n---\n")
        fm, rest = text[:end], text[end:]
    if FENCE in rest:
        i = rest.index(FENCE)
        return fm, rest[:i], rest[i:]
    return fm, rest, ""


def unwrap_links(body):
    """Normalize existing [[@ck|display]] back to plain display so we can re-resolve idempotently.

    Returns (plain_body, {display_text: citekey}) so previously-resolved links can be re-validated.
    """
    prior = {}

    def repl(m):
        prior[m.group(2)] = m.group(1)
        return m.group(2)

    return LINK_RE.sub(repl, body), prior


def paragraph_around(text, pos):
    """The blank-line-delimited paragraph containing offset `pos` — disambiguation context that
    survives intervening math/markup (a fixed char window can miss the topical words)."""
    start = text.rfind("\n\n", 0, pos)
    end = text.find("\n\n", pos)
    return text[(start + 2 if start != -1 else 0):(end if end != -1 else len(text))]


def link_body(self_ck, body, index, extra=None):
    """Wrap in-scope citation spans in `body` as wikilinks. Returns (new_body, citekeys_set).

    Pure function of (plain prose, index, extra): unwrap → resolve → wrap is its own fixed point, so a
    re-run is a no-op. We do NOT carry prior in-prose links forward (that made the result path-dependent
    and let ambiguous spans oscillate); durable LLM-enrichment links arrive via `extra` instead.
    """
    plain, _prior = unwrap_links(body)
    resolved = {}  # display span -> citekey  (first occurrence wins for replacement)

    # 1) deterministic span matches, disambiguated against the enclosing paragraph
    for m in SPAN_RE.finditer(plain):
        names, year = m.group(1), m.group(2)
        ck = resolve_span(names, year, paragraph_around(plain, m.start()), index)
        if ck and ck != self_ck:
            resolved.setdefault(m.group(0), ck)

    # 2) explicit enrichment links (LLM pass / sidecar): {display span -> citekey}
    for disp, ck in (extra or {}).items():
        if ck in index and ck != self_ck and disp in plain:
            resolved.setdefault(disp, ck)

    # apply: wrap the first occurrence of each display span, longest spans first to avoid nesting
    new_body = plain
    for disp in sorted(resolved, key=len, reverse=True):
        ck = resolved[disp]
        wrapped = f"[[@{ck}|{disp}]]"
        # only wrap an occurrence that is not already inside a wikilink
        idx = new_body.find(disp)
        while idx != -1:
            if new_body.count("[[", 0, idx) == new_body.count("]]", 0, idx):  # not already linked
                new_body = new_body[:idx] + wrapped + new_body[idx + len(disp):]
                break
            idx = new_body.find(disp, idx + 1)
    return new_body, set(resolved.values())


def set_related(fm, citekeys):
    related = "[" + ", ".join(sorted(citekeys)) + "]"
    line = f"related: {related}\n"
    if re.search(r"^related:.*$", fm, flags=re.M):
        return re.sub(r"^related:.*$", line.rstrip("\n"), fm, flags=re.M)
    # insert before closing ---
    return fm.rstrip("\n")[:-3] + line + "---\n" if fm.endswith("---\n") else fm


def load_enrichment(vault):
    """Durable LLM-enrichment links: {note_citekey: {display_span: target_citekey}}.

    Because prose links are no longer carried forward, enrichment that the regex can't re-derive lives
    here and is re-applied on every run. Empty until the deferred enrichment pass writes it (ADR-0013)."""
    p = vault / ".research" / "link_enrichment.json"
    return json.loads(p.read_text()) if p.exists() else {}


def process_note(path, index, enrich=None, dry_run=False):
    self_ck = path.stem[1:] if path.stem.startswith("@") else path.stem
    extra = (enrich or {}).get(self_ck)
    text = path.read_text()
    fm, body, human = split_regions(text)
    new_body, citekeys = link_body(self_ck, body, index, extra)
    new_fm = set_related(fm, citekeys)
    changed = (new_body != body) or (new_fm != fm)
    if changed and not dry_run:
        path.write_text(new_fm + new_body + human)
    return self_ck, sorted(citekeys), changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--all", action="store_true", help="process every literature/@*.md")
    ap.add_argument("--citekey", help="process a single note by citekey")
    ap.add_argument("--add-links", help="JSON [{citekey, span}] of LLM-resolved links for --citekey")
    ap.add_argument("--rebuild-index", action="store_true", help="refresh the candidate index from Zotero")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    vault = Path(args.vault).resolve() if args.vault else find_vault(os.getcwd())
    index = load_index(vault, rebuild=args.rebuild_index)
    enrich = load_enrichment(vault)

    # --add-links (for --citekey) is persisted into the enrichment sidecar, then applied like any run.
    if args.add_links:
        if not args.citekey:
            ap.error("--add-links requires --citekey")
        rows = json.loads(Path(args.add_links).read_text())
        merged = dict(enrich.get(args.citekey, {}))
        merged.update({r["span"]: r["citekey"] for r in rows if r.get("span") and r.get("citekey")})
        enrich[args.citekey] = merged
        if not args.dry_run:
            (vault / ".research" / "link_enrichment.json").write_text(
                json.dumps(enrich, ensure_ascii=False, indent=2, sort_keys=True))

    if args.citekey:
        notes = [vault / "literature" / f"@{args.citekey}.md"]
    elif args.all:
        notes = sorted((vault / "literature").glob("@*.md"))
    else:
        ap.error("pass --all or --citekey")

    total_links = changed_n = 0
    for path in notes:
        if not path.exists():
            print(f"  ! missing {path.name}", file=sys.stderr)
            continue
        ck, links, changed = process_note(path, index, enrich=enrich, dry_run=args.dry_run)
        total_links += len(links)
        changed_n += int(changed)
        if links:
            print(f"  {ck}: {len(links)} -> {', '.join(links)}")
    verb = "would link" if args.dry_run else "linked"
    print(f"[link] {verb} {total_links} edges across {changed_n}/{len(notes)} notes "
          f"({len(index)} in-scope candidates)")


if __name__ == "__main__":
    main()
