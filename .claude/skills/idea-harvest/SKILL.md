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
- `.claude/scripts/biblio.py search|recent|verify` — the ONLY external-literature path: `search`
  (OpenAlex) + `recent` (RePEc/NEP) for relevant/new work, `verify` to resolve a citation to a real
  record. Metadata only.
- `.claude/scripts/score_ideas.py --vetted FILE` — deterministic **project-potential** scoring (ADR-0016):
  admissibility filter (drop + record failures) + `Potential = w·(Significance, Novelty, Feasibility)`
  normalized 0–100, ranked. Weights tunable; re-run to re-rank without re-vetting.
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
Each idea is assessed on the **project-potential** model (ADR-0016). The agent emits only the *inputs*,
each with cited evidence — a script computes the score in Phase 4 (the agent does **not** emit a
composite or verdict):
- **Admissibility** (pass/fail + evidence): *sound & grounded* (premise supported by **≥2 verified
  corpus papers**, not hallucinated) and *not-already-done* (`biblio` finds nothing that *fully* does it).
- **Three 1–5 dimensions** (rubric-anchored; a dimension **may not exceed 3 without cited evidence**):
  *Significance* (how much it matters — corroborate with a coarse target-venue band), *Novelty* (how new,
  above the floor), *Feasibility* (ease / inverse effort — low is fine; moonshots survive, never gated).
- **Fit** (1–5; relevance to the user's research programme — a filter, *not* part of the score).

The novelty + admissibility checks are **grounded**, not recalled:
- Run `uv run python .claude/scripts/biblio.py search --query "<idea's core claim>" --from-year <recent>`
  to surface genuinely-recent related work the idea must beat. For economics ideas, also run
  `biblio.py recent --fields nep-dcm,nep-exp,nep-upt,nep-cbe,nep-mic` to catch the newest working papers
  (RePEc/NEP feeds) that OpenAlex may not have indexed yet.
- For every paper the agent names as "closest prior work," run
  `uv run python .claude/scripts/biblio.py verify --doi <doi>` (or `--title "..." --year Y`). If a claim
  does **not** resolve to a real record, it is dropped or marked **"⚠ unverified — may not exist."**
- Agents must use `biblio` only — **never** `WebFetch`/`WebSearch` a paper (the hook will block it).
Collect, per idea, the verified external records found (their JSON), for the acquire-list.

### Phase 4 — Score, synthesize, acquire-list
**Compute project potential deterministically** (ADR-0016) from the Phase-3 inputs:
`uv run python .claude/scripts/score_ideas.py --vetted <vetting.json>` — applies the admissibility filter
(drops + records failures), computes `Potential = w·(Significance, Novelty, Feasibility)` normalized
0–100 (equal weights default, tunable), and ranks. Then write the dossier to `ideas/idea-harvest-<date>.md`:
- **Inadmissible ideas** listed separately, each with the failed gate + reason (nothing vanishes silently).
- **Admissible ideas** ranked by **Potential (0–100)**, each showing the three dimension scores **+ their
  evidence** (biblio records, corpus citekeys, venue band), the Fit tag, the admissibility evidence, and
  the refined pitch / first step / risks.
The score is reproducible — re-run `score_ideas.py` (e.g. with new weights) to re-rank *without* re-vetting.
Then build the acquire-list from the verified external records gathered in Phase 3:
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
