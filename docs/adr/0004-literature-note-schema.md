# ADR-0004: Literature notes — structured deep notes via section map-reduce

- Status: Accepted
- Date: 2026-05-29
- Covers decisions: note depth (#4) and reading strategy (#16)

## Context
Literature notes are not only for re-reading — they are fuel for topic synthesis and project
ideation, so they must be structured enough to mine across, especially limitations/open questions.
Every in-scope item has a PDF, so full-text reading is possible. A single-pass summary of a long
paper over-weights the abstract/intro and skims methods/results; the user explicitly wants certainty
that the whole paper is read.

## Decision
Each note is a **structured, comprehensive note (~500–1000 words)** with fixed sections: Summary ·
Research question · Method/identification · Data · Key findings · Contribution · **Limitations & open
questions** · Connections, plus keyword frontmatter (full schema in `docs/architecture.md`). Formulas
are written in **Obsidian MathJax** (`$...$` inline, `$$...$$` block) so they render in the vault.

> Revision (2026-05-29, after the pilot): depth raised from the initial ~300–600 to ~500–1000 words —
> favoring detail in *Method* and *Key findings* — and LaTeX math made mandatory.

Reading uses **section-based map-reduce + a coverage check**:
1. Extract (`pdftotext`) and segment by section (or PDF TOC); visual `Read` fallback for scanned PDFs.
2. Map: summarize each section into the schema slot it feeds.
3. Reduce: synthesize into the final note.
4. Coverage check: confirm every major section was captured; flag empties.
5. Length-adaptive: articles fully mapped; books/theses → chapter-level + targeted.

## Consequences
- Whole-paper coverage with provenance, not skimmed abstracts.
- Chunk by *structure*, never arbitrary token windows (preserves tables/equations/cross-refs).
- Higher per-paper cost than single-pass; mitigated by the pilot-then-backfill rollout.

## Alternatives considered
- **Lean ~150-word summary** — cheaper, thinner fuel for Layers 2–3.
- **Exhaustive section-by-section summary** — thorough but verbose and not "concise".
- **Single-pass full text** — simpler, but weaker completeness and can't do >20pp visual reads.
- **Targeted sections only** — cheapest, but not whole-paper (contradicts the requirement).
