# ADR-0007: Topic notes — bottom-up, incremental, LLM-thematic clustering

- Status: Accepted
- Date: 2026-05-29
- Covers decisions: derivation (#8), re-cluster model (#9), method (#10)

## Context
Layer 2 turns literature notes into emergent subject clusters that surface cross-paper tensions and
candidate project ideas. Topics could be seeded top-down or discovered bottom-up; re-clustering can
churn names/memberships and orphan annotations and promoted ideas. No embedding infrastructure exists
locally (no sentence-transformers/Ollama/embedding API keys).

## Decision
- **Bottom-up**: topics emerge purely from clustering the literature notes — no seeding.
- **Incremental**: existing topic notes persist as **anchors**; each run clusters only new/changed
  literature notes into the best-fit anchor or a new topic. Merges/splits are proposed periodically
  as a **reviewable diff**, not applied silently.
- **LLM-thematic**: an agent reads the structured summaries + `keywords:` and assigns each note to a
  topic with a written justification. Membership is recorded in each lit note's `topics:` frontmatter;
  topic notes show members via a live dataview query.

## Consequences
- Emergence + stability: new topics arise from data, but anchors/annotations/ideas survive.
- Explainable assignments; no infra to stand up; ample at ~481 notes / a few dozen topics.
- Topic granularity and merge/split cadence are tunable once real clusters exist (open).

## Alternatives considered
- **Hybrid seed+maintain** — coherent but predefines topics (rejected: user wants pure emergence).
- **Full re-cluster each run** (+diff, or disposable topics) — most faithful to "emergent," but
  heavier and risks stranding protected human regions.
- **Embeddings / hybrid embed+LLM** — more principled and scalable, but needs infra to maintain.
