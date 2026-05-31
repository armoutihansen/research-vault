---
name: idea-harvest
description: Harvest research-project ideas from the Layer-2 topic/area notes, adversarially vet them with grounded (real, existence-checked) novelty, and emit a ranked dossier + a verified acquire-list. Use when the user wants to mine candidate ideas, find what's promising/novel across topics, or says "/idea-harvest". The Layer 2 -> 3 bridge.
---

# idea-harvest

Turn the Layer-2 topic/area notes into a ranked, adversarially-vetted **dossier of research-project
ideas** (`ideas/idea-harvest-<date>.md`) plus an **acquire-list** of relevant papers you don't yet hold.
The bridge from topics (ADR-0007/0014) to projects (`/promote-idea`). External literature is touched
**only** through the open-only `biblio` client (ADR-0015). See [`../../../CONTEXT.md`](../../../CONTEXT.md)
and [`../../../docs/adr/0015-open-access-biblio-lookup.md`](../../../docs/adr/0015-open-access-biblio-lookup.md).

**Core principles:**
- **Generate from the vault; vet against reality.** Ideas are mined from your topic/area notes; their
  *novelty* is checked against the live literature — but only via open metadata.
- **Grounded, not recalled.** Every external "prior work" claim and every acquire-list entry is
  **existence-verified** with `biblio verify` before it is surfaced — no LLM-recalled phantom citations.
- **Open-access only, by construction (ADR-0015).** Agents use the `biblio` client (OpenAlex/Crossref —
  metadata + abstracts), **never raw `WebFetch`/`WebSearch` for papers**. The system never fetches
  full-text; the backstop hook denies any stray full-text fetch. Full-text you want enters via Zotero.

## Prerequisites
- Run from the vault root. **Layer 2 must exist** (`topics/` + `areas/` populated).
- The `biblio` client (`.claude/scripts/biblio.py`) and the full-text-fetch hook (ADR-0015) in place.
- **Bulk fan-out uses the Workflow tool** — requires the user to opt into workflows.

## Scripts (deterministic)
- `.claude/scripts/biblio.py search|verify` — the ONLY external-literature path: `search` for recent
  relevant work, `verify` to resolve a citation to a real OpenAlex/Crossref record. Metadata only.
- `.claude/scripts/acquire_list.py --records FILE` — turn verified biblio records into the acquire-list,
  deduped against the vault (by DOI + title). Only `found:true` records are kept.
- `.claude/skills/topic-cluster/scripts/corpus.py` — read topic/area/lit notes (reused).

## Procedure (Workflow, four phases)

### Phase 1 — Mine (parallel: per area + cross-area hunters)
Read the area notes + their child topic notes (their *Candidate ideas*, *Open questions*, *Cross-paper
/ Cross-topic tensions*). Emit the strongest **existing** ideas + **synthesized** ideas at topic/area
intersections. Vault-only — no external access here. Structured output per idea: title, pitch,
source_topics, key_papers (vault citekeys), kind, why_promising.

### Phase 2 — Consolidate (1 agent, barrier)
Merge near-duplicates, drop the vague, number the distinct set.

### Phase 3 — Vet (parallel, one per idea) — **biblio-grounded**
Each idea is scored adversarially (novelty / feasibility / fit / grounding). The novelty check is
**grounded**, not recalled:
- Run `uv run python .claude/scripts/biblio.py search --query "<idea's core claim>" --from-year <recent>`
  to surface genuinely-recent related work the idea must beat.
- For every paper the agent names as "closest prior work," run
  `uv run python .claude/scripts/biblio.py verify --doi <doi>` (or `--title "..." --year Y`). If a claim
  does **not** resolve to a real record, it is dropped or marked **"⚠ unverified — may not exist."**
- Agents must use `biblio` only — **never** `WebFetch`/`WebSearch` a paper (the hook will block it).
Collect, per idea, the verified external records found (their JSON), for the acquire-list.

### Phase 4 — Synthesize (1 agent) + acquire-list
Rank by composite score; write the dossier to `ideas/idea-harvest-<date>.md` (top tier → promising →
also-surfaced; each idea with refined pitch, source topics, grounding papers, scores, **verified**
prior work, first step, risks). Then build the acquire-list from the verified external records gathered
in Phase 3:
```
uv run python .claude/scripts/acquire_list.py --records .research/tmp/vetting_records.json >> ideas/idea-harvest-<date>.md
```
This appends a `## Acquire-list` of relevant papers **not already in your library** (DOI + OA link when
open) — the papers to add to Zotero (via your own access) and ingest with `lit-sync` before a feasibility
deep-read. Frontmatter (`type: idea-harvest`) + a `## My notes` human region (ADR-0005), as for the
persisted dossier.

## Notes
- Re-runnable as the corpus grows; dossiers are dated snapshots in `ideas/`.
- Scale to the ask: a quick harvest = a few miners + single-vote vetting; "max effort" = full area +
  cross-area mining, ~20-30 ideas, adversarial multi-signal vetting (this is token-heavy — mind session
  limits; the workflow is resumable via `resumeFromRunId`).
- The dossier is the input to `/promote-idea` (Layer 3): a chosen idea becomes `projects/<slug>.md` at
  `status: feasibility`, back-linked to its source topic.
