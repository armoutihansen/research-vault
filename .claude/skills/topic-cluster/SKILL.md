---
name: topic-cluster
description: Cluster the Layer-1 literature notes into emergent Layer-2 topic notes. Use when the user wants to build/refresh topic notes, cluster new papers into topics, run the topic bootstrap, re-balance topics (merge/split), or says "/topic-cluster". Bottom-up, LLM-thematic, human-gated (ADR-0007, ADR-0014).
---

# topic-cluster

Turn the literature notes into emergent **topic notes** (`topics/<slug>.md`) — bottom-up subject
clusters that surface cross-paper tensions and **candidate ideas** for Layer 3. Deterministic I/O
lives in `scripts/`; the clustering judgment is yours, under the discipline below. See
[`../../../CONTEXT.md`](../../../CONTEXT.md), [`../../../docs/adr/0007-topic-clustering.md`](../../../docs/adr/0007-topic-clustering.md),
and [`../../../docs/adr/0014-topic-cluster-operational-design.md`](../../../docs/adr/0014-topic-cluster-operational-design.md).

**Core principles (ADR-0014):**
- **You cluster; the graph is a prior.** Cluster by *research question*, using each note's keywords,
  Summary, `related:` edges, and Louvain `community` id as **hints** — never let citation cliques
  dictate topics.
- **Granularity = idea-generativity.** A topic is the smallest cluster that still carries internal
  tension worth a candidate idea — finer than a survey area, coarser than one paper. ~10–25 members,
  ~20–35 topics is the *expected outcome*, not a quota.
- **Multi-membership by centrality** (soft cap ~3): a note joins a topic only if *central to its core
  tension*, not merely relevant. Topic sizes don't sum to the corpus — that's honest.
- **Orphans, not junk drawers.** A note that fits nothing goes to `orphans` with a reason → `topics: []`.
- **Membership lives only in lit-note `topics:`.** Topic notes derive rosters via dataview. The writers
  are idempotent and touch only the AI region; re-running with no new/changed notes is a no-op.

## Prerequisites
- Run from the vault root. Layer 1 must exist (`literature/@*.md` with `keywords:` + `related:`).
- `uv` available (for the optional Louvain community prior — degrades gracefully if absent).
- **Bulk fan-out (Phase B, re-prose) uses the Workflow tool** — requires the user to opt into workflows.

## Scripts (deterministic — always use these)
- `scripts/make_input.py --mode bootstrap|incremental` — emit the clustering input JSON: a compact rep
  per note (citekey · title · year · keywords · related · `community` · Summary) + (incremental) the
  current taxonomy and only *pending* notes. `--out FILE`, `--summary-chars N`.
- `scripts/apply_taxonomy.py --taxonomy FILE` — the membership writer: rewrite each note's `topics:`
  (AI region, idempotent), update `.research/topic_state.json`, and **validate** (coverage, dangling
  members, empty topics, soft-cap, dangling links). `--require-full-coverage`, `--dry-run`,
  `--validate-only`.
- `scripts/write_topic.py --slug S --title T --scope … --members ck,… --body body.md` — write/refresh
  `topics/<slug>.md`: frontmatter + your prose + the derived `## Members` / `## Bordering work` /
  `## Promoted from this topic` blocks + the human fence. `created` is fixed at birth.
- `scripts/corpus.py` — shared readers (imported by the above); not a CLI.

## Procedure — first-run bootstrap (no anchors yet)

### Phase A — Taxonomy (one agent, one shot)
```
uv run python .claude/skills/topic-cluster/scripts/make_input.py --mode bootstrap --out .research/tmp/taxonomy_input.json
```
Hand the **whole** file to **one** agent (it fits one Opus 1M context, ~110k tokens for 469 notes).
Brief: *"Partition these literature notes into topics at the idea-generativity grain (above). Use
`community`/`related`/keywords as priors you may override on thematic grounds. Assign every note to ≥1
topic by centrality (cap ~3); send genuine misfits to `orphans` with a one-line reason."* Require this
**structured output**:
```json
{ "topics": [ {"slug": "kebab-slug", "title": "Human Title", "scope": "one line",
               "members": ["Citekey1", "..."], "rationale": "why this is one idea-generative topic"} ],
  "orphans": [ {"citekey": "X", "reason": "..."} ] }
```
(Slugs are kebab-case and become permanent identities — choose carefully.)

### Phase A′ — Critic / refine (1 agent, ≤2 rounds)
Give a second agent the proposed taxonomy + the input. It checks three failure modes — **grab-bag**
topics (no internal tension → split), **near-duplicate** topics (→ merge), **coverage** (every note
assigned or explicitly orphaned) — and the **graph cross-check** (flag topics that shred a tight
`community`, or a community scattered across many topics). It returns a revised taxonomy + notes.

### Human gate (required)
Present the refined taxonomy to the user as a **reviewable proposal**: topic count, each topic's
title · scope · size · a few member previews, the orphan list, and the critic's flags. The user
approves/edits before anything is written. This is the largest diff Layer 2 will ever produce.

### Phase C — Apply membership (deterministic)
Write the membership straight from the approved taxonomy (it accepts the `orphans` objects as-is):
```
uv run python .claude/skills/topic-cluster/scripts/apply_taxonomy.py --taxonomy .research/tmp/approved.json --require-full-coverage
```
This stamps `topics:` into every member note, records state, and validates. It will warn that each
slug still lacks a `topics/<slug>.md` — that's Phase B.

### Phase B — Topic prose (fan out, one agent per topic)
Use the **Workflow** tool (one agent/topic, parallel). Each agent reads the **full** summaries of its
members (the lit notes) and writes the thematic prose only — `## Scope`, `## Sub-themes`,
`## Cross-paper tensions`, `## Open questions`, `## Candidate ideas` (the Layer-3 hook: make ideas
specific, grounded in the members' open questions/tensions). Then it calls:
```
uv run python .claude/skills/topic-cluster/scripts/write_topic.py --slug <slug> --title "<title>" \
  --scope "<scope>" --members "<ck1,ck2,…>" --body /tmp/<slug>.md
```
The `## Members` / `## Bordering work` / `## Promoted from this topic` blocks are added by the script —
**do not** hand-write rosters or wikilink lists. Never write below the fence.

### Finalize
```
uv run python .claude/skills/topic-cluster/scripts/apply_taxonomy.py --validate-only
```
Expect a clean pass (no dangling membership links). Report: N topics, size distribution, N orphans,
and any graph-disagreement flags worth a human look.

## Procedure — incremental run (after the bootstrap)
For new notes from `lit-sync` or `changed` notes:
```
uv run python .claude/skills/topic-cluster/scripts/make_input.py --mode incremental --out .research/tmp/incr.json
```
This selects only **pending** notes (empty `topics:`, or manifest hash ≠ last-clustered) and includes
the current `taxonomy`. One agent assigns each pending note to best-fit topic(s) **or** flags
`needs_new_topic` (with a proposed name). **Pool** new-topic flags — one stray paper doesn't mint a
topic; a burst of related ones might — and run them through the same human gate. Then `apply_taxonomy`
(without `--require-full-coverage`, since only pending notes are in scope) and re-prose **only the
topics that gained/lost members** via Phase B. Anchors and untouched members are left alone.

## Procedure — re-balance (merge/split), explicit and gated
Run on request (`--rebalance` intent) or when a heuristic trips: a topic > ~40 members (split
candidate) or two topics with high member+citation overlap (merge candidate). Produce a **reviewable
diff** (proposed merges/splits + rationale + resulting rosters). On approval: apply membership changes
(`apply_taxonomy`), then for a **rename/merge/split**, move/remove the `topics/<slug>.md` file(s) and
re-run `apply_taxonomy` so member links are rewritten to surviving slugs; re-prose affected topics.
Slugs are identities — never silently rename; a rename is an explicit file move + membership rewrite.

## Sibling-skill contract
`/promote-idea` must stamp the source topic onto the new project note's **`topics:`** frontmatter
(`["[[<slug>]]"]`) — that back-link is what powers each topic note's *Promoted from this topic*
dataview and lets a promoted idea survive re-clustering (it lives in Layer 3, not pinned in the topic
note). The **orphan list** doubles as a Zotero data-cleanup signal (it surfaces mis-scanned/mismatched
PDFs).

## Notes
- Idempotent: re-running writers rewrites only the AI region; the user's `## My notes` is preserved.
- Clustering variance is bounded by persistence + pending-only re-clustering + the human gate; it is
  not eliminated (LLM-thematic), which is acceptable because every structural change is reviewed.
- New machine state: `.research/topic_state.json` (per-note last-clustered hash).
