#!/usr/bin/env python3
"""Shared readers for the topic-cluster skill (ADR-0014).

The literature notes are the single source of truth for Layer-2 clustering. This module reads them
the way `lit-sync` writes them — frontmatter is plain `key: [a, b]` lines (write_note.py's yaml_list),
the AI body is `## Section` blocks above the FENCE, the human region is below it. We never parse below
the fence and never write here (the write side lives in apply_taxonomy.py / write_topic.py).

Also builds the citation graph from `related:` and a Louvain community id per note — a *prior* the
taxonomy agent may follow or override (ADR-0014), never the partitioner. Graceful no-op (empty
community map) if networkx isn't importable.

Standard library + networkx (the only third-party dep). Run the skill scripts via `uv run` so the
pinned environment (pyproject.toml / uv.lock) provides networkx; bare `python3` still works but skips
the community prior.
"""
import re
import sys
from pathlib import Path

FENCE = "%% ─── below is yours; regeneration never touches it ─── %%"


def find_vault(start):
    p = Path(start).resolve()
    for cand in [p, *p.parents]:
        if (cand / ".research").exists() or (cand / "CONTEXT.md").exists():
            return cand
    return p


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


def _scalar(fm, key):
    m = re.search(rf"^{key}:\s*(.*)$", fm, flags=re.M)
    if not m:
        return ""
    v = m.group(1).strip()
    if v.startswith('"') and v.endswith('"') and len(v) >= 2:
        v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return v


def _list(fm, key):
    """Parse a `key: [a, b, c]` inline list. Used only for comma-free tokens (keywords, related,
    topics) — NOT authors, whose 'Last, First' commas would break a naive split."""
    m = re.search(rf"^{key}:\s*\[(.*)\]\s*$", fm, flags=re.M)
    if not m or not m.group(1).strip():
        return []
    return [t.strip() for t in m.group(1).split(",") if t.strip()]


WIKILINK = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")


def topic_slugs(fm):
    """Slugs from a lit note's `topics:` field. Tolerates both the wikilink form we write
    (`["[[slug]]", ...]`) and a bare-slug fallback."""
    out = []
    for tok in _list(fm, "topics"):
        tok = tok.strip().strip('"').strip("'")
        m = WIKILINK.fullmatch(tok)
        slug = m.group(1) if m else tok
        slug = slug.split("/")[-1]  # tolerate a path-qualified link
        if slug:
            out.append(slug)
    return out


def section(body, name):
    """Text of the `## <name>` section (up to the next `## ` heading), stripped."""
    m = re.search(rf"^##\s+{re.escape(name)}\s*\n(.*?)(?=^##\s+|\Z)", body, flags=re.M | re.S)
    return m.group(1).strip() if m else ""


def summary_para(body):
    """The Summary section's first paragraph; falls back to the abstract callout."""
    s = section(body, "Summary")
    if s:
        return s.split("\n\n")[0].strip()
    m = re.search(r"^>\s*\[!abstract\][^\n]*\n((?:^>.*\n?)*)", body, flags=re.M)
    if m:
        return re.sub(r"^>\s?", "", m.group(1), flags=re.M).strip().split("\n\n")[0]
    return ""


def read_note(path):
    """Compact, clustering-relevant view of one literature note."""
    fm, body, _human = split_regions(path.read_text())
    ck = path.stem[1:] if path.stem.startswith("@") else path.stem
    return {
        "citekey": ck,
        "title": _scalar(fm, "title"),
        "year": _scalar(fm, "year"),
        "keywords": _list(fm, "keywords"),
        "related": _list(fm, "related"),
        "topics": topic_slugs(fm),
        "summary": summary_para(body),
    }


def iter_notes(vault):
    return [read_note(p) for p in sorted((vault / "literature").glob("@*.md"))]


def iter_topic_paths(vault):
    """Topic-note files in topics/ — those with `type: topic` frontmatter. Skips README.md and any
    other stray markdown so it never gets mistaken for a topic (ADR-0014)."""
    out = []
    d = vault / "topics"
    if not d.exists():
        return out
    for p in sorted(d.glob("*.md")):
        if re.search(r"^type:\s*topic\s*$", p.read_text()[:400], flags=re.M):
            out.append(p)
    return out


def citation_edges(notes):
    """Undirected edges among in-corpus citekeys, derived from `related:` (symmetric, deduped)."""
    present = {n["citekey"] for n in notes}
    edges = set()
    for n in notes:
        a = n["citekey"]
        for b in n["related"]:
            if b in present and b != a:
                edges.add((a, b) if a < b else (b, a))
    return sorted(edges)


def communities(notes):
    """citekey -> Louvain community id (a clustering *prior*). {} if networkx is unavailable — the
    prior is simply absent and the LLM clusters without it (ADR-0014). Deterministic via a fixed seed."""
    edges = citation_edges(notes)
    if not edges:
        return {}
    try:
        import networkx as nx
        from networkx.algorithms.community import louvain_communities
    except ImportError as e:
        print(f"[topic-cluster] community prior skipped (networkx unavailable: {e}); "
              f"run via `uv run` to enable it", file=sys.stderr)
        return {}
    g = nx.Graph()
    g.add_edges_from(edges)
    out = {}
    for i, comm in enumerate(sorted(louvain_communities(g, seed=0, resolution=1.0),
                                    key=len, reverse=True)):
        for node in comm:
            out[node] = i
    return out


def bordering_work(slug, members_by_slug, notes_by_ck):
    """Citation-derived 'bordering work' for a topic: in-corpus papers cited by this topic's members
    (via `related:`) that are NOT themselves members of it, with the count of member citations.
    This is how merely-related papers surface without diluting the membership roster (ADR-0014)."""
    members = members_by_slug.get(slug, set())
    counts = {}
    for ck in members:
        for b in notes_by_ck.get(ck, {}).get("related", []):
            if b in notes_by_ck and b not in members:
                counts[b] = counts.get(b, 0) + 1
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
