# ADR-0013: Citation linking — resolve in-scope citations to wikilinks via a re-runnable post-pass

- Status: Accepted
- Date: 2026-05-30

## Context
Literature notes name related work in prose `## Connections` ("Manzini & Mariotti (2007)",
"Tversky–Kahneman 1974"). That signal is human-readable but not navigable and not machine-readable:
Obsidian's graph/backlinks see nothing, and the `related:` frontmatter sits empty. The inter-note
citation graph is the cheapest, highest-quality edge set for Layer-2 bottom-up clustering (ADR-0007),
so it is worth materializing — but only for papers that are **in scope** (ADR-0003), i.e. that have
or will have a note. Linking out-of-scope citations (Luce 1959, Savage 1954) would create permanent
dangling links. Generating notes is expensive (PDF map-reduce); we do not want linking to require
re-reading PDFs, and the corpus grows in chunks, so linking must be cheaply re-runnable as scope and
note count change.

## Decision
- **Linking is a distinct corpus-level post-pass**, not baked into note generation. Generation writes
  prose citations in normal form; `scripts/link_notes.py` decorates them afterward. PDF-free.
- **A wikilink is a promise a note exists or will.** Only the ~471 in-scope citekeys are link targets;
  out-of-scope mentions stay plain prose. Links to not-yet-written in-scope notes are valid Obsidian
  **ghost links** that resolve automatically when those notes land — so the pass runs before backfill
  completes, and backlinks make the graph symmetric for free (only outgoing links are written).
- **Validate-and-augment writer, idempotent.** Each run normalizes existing `[[@ck|disp]]` back to
  text, re-resolves, keeps valid prior links, drops links whose citekey left scope, and rebuilds
  `related:` from the union. Never touches below the human fence (ADR-0005). Re-runs are free, so the
  update path on corpus/scope growth is a single `link_notes.py --rebuild-index --all`.
- **Resolution is deterministic (span-first) for v1.** A regenerable candidate index
  (`.research/link_index.json`, citekey → surnames/year/title, built from `enumerate.py`) backs a
  matcher that finds `Surname (Year)` citation spans and resolves each to a unique in-scope citekey
  (suffix collisions like `Manzini2012`/`Manzini2012a` broken by title-token overlap with context).
- **LLM enrichment is deferred, not designed out.** Detached-year ("…prospect theory (1979)"),
  year-less ("Tversky's Elimination-by-Aspects"), and acronym references are missed by the regex. A
  candidate-shortlisted LLM pass (`scripts/link_candidates.py` + `link_notes.py --add-links`) recovers
  them; it is deferred until Layer-2 clustering demonstrates it needs denser edges, since the hub
  structure is already well-connected without it.

## Consequences
- Navigable citation graph + populated `related:` now, at ~zero ongoing cost; 520 edges across 134 of
  the first 165 notes. Clustering gets real edges before Layer 2 is built.
- Citation-grounded only: no thematic/invented edges, so the graph is fully explainable but sparser
  than a semantic-similarity graph would be (acceptable; ADR-0007 already carries thematic signal via
  `keywords:`/LLM assignment).
- Deterministic recall is partial; the most foundational hubs are nonetheless richly linked
  (Kahneman1979 in-degree 25, Manzini2007 19). Long-tail edges await the deferred enrichment.
- Linking re-runs after every backfill chunk; ghost links mean no re-link is needed when sibling
  notes appear, only when prose or scope changes.

## Alternatives considered
- **Link at generation time (writer emits `[[...]]`)** — highest recall (the writer knows what it
  cited), but couples linking to expensive regeneration and to per-run LLM variance, and complicates
  idempotent re-linking. Rejected in favor of a separable, deterministic, free-to-re-run pass.
- **Pure regex over prose** — cheapest, but brittle on citation-format variety; kept as the v1 core
  but explicitly backstopped by deferred LLM enrichment rather than treated as sufficient.
- **Semantic-similarity edges (embeddings)** — denser, captures uncited affinities, but needs
  embedding infra the project deliberately avoids (ADR-0007) and yields unexplainable edges.
- **Link all cited works, in scope or not** — richer prose links, but creates permanent dangling
  links to papers that will never have a note, eroding the "ghost link = forthcoming note" invariant.
