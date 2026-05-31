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
- **Two levels.** Topics are grouped into broad **areas** (`areas/<slug>.md`, ADR-0014): each topic
  links up via a single `area:`; area notes carry field-level synthesis + a dataview child list. Areas
  are grouped from the topics, human-gated, the same way topics are clustered from papers.

## Prerequisites
- Run from the vault root. Layer 1 must exist (`literature/@*.md` with `keywords:` + `related:`).
- `uv` available (for the optional Louvain community prior — degrades gracefully if absent).
- **Bulk fan-out (Phase C, topic prose) uses the Workflow tool** — requires the user to opt into workflows.

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
  `## Promoted from this topic` blocks + the human fence. `created` is fixed at birth; `area:` preserved.
- `scripts/apply_areas.py --areas FILE` — stamp each topic's parent `area:` link (idempotent, single
  source of truth) + validate (single-parent, no dangling area). `--validate-only`, `--dry-run`.
- `scripts/write_area.py --slug S --title T --scope … --body body.md` — write/refresh `areas/<slug>.md`:
  frontmatter + your synthesis prose + the derived `## Topics` dataview child-list + the human fence.
- `scripts/corpus.py` — shared readers (imported by the above); not a CLI.

## Procedure — first-run bootstrap (no anchors yet)

### Phase A — Taxonomy (one agent, one shot)
```
uv run python .claude/skills/topic-cluster/scripts/make_input.py --mode bootstrap --out .research/tmp/taxonomy_input.json
```
Hand the **whole** file to **one** agent (it fits one Opus 1M context, ~110k tokens for 469 notes).
Brief: *"Partition these literature notes into topics at the idea-generativity grain (above). Use
`community`/`related`/keywords as priors you may override on thematic grounds. Assign every note to ≥1
topic by centrality (cap ~3); send genuine misfits to `orphans` with a one-line reason. Before
returning, self-check: no grab-bag topics, no near-duplicate topics, full coverage."* Require this
**structured output**:
```json
{ "topics": [ {"slug": "kebab-slug", "title": "Human Title", "scope": "one line",
               "members": ["Citekey1", "..."], "rationale": "why this is one idea-generative topic"} ],
  "orphans": [ {"citekey": "X", "reason": "..."} ] }
```
(Slugs are kebab-case and become permanent identities — choose carefully.) There is **no separate LLM
"critic" pass**: a second agent re-running the same thematic judgment adds nothing the human gate
doesn't, and has no fitness signal to iterate against. The cold-eyes review is the **human's**, informed
by the deterministic annotation below.

### Human gate (required)
Annotate the proposal deterministically, then hand it to the user:
```
uv run python .claude/skills/topic-cluster/scripts/report_taxonomy.py --taxonomy .research/tmp/proposed_taxonomy.json
```
This prints the gate summary — topic count + size distribution, coverage/orphans, multi-membership and
cap/singleton flags, and the **graph cross-check**: each topic's agreement (purity) with the Louvain
citation communities, flagging topics that span many communities and communities scattered across many
topics. Present to the user: topics (title · scope · size · member previews), the orphan list, and
these flags. The user approves/edits **before anything is written** — the largest diff Layer 2 will
ever produce. **Refinement is iteration here**, driven by the user's calls ("split 7", "merge 3 and
12"): re-run the taxonomy agent with that feedback or hand-edit, re-annotate, re-gate. Save the
approved result to `.research/tmp/approved.json`.

### Phase B — Apply membership (deterministic)
Write the membership straight from the approved taxonomy (it accepts the `orphans` objects as-is):
```
uv run python .claude/skills/topic-cluster/scripts/apply_taxonomy.py --taxonomy .research/tmp/approved.json --require-full-coverage
```
This stamps `topics:` into every member note, records state, and validates. It will warn that each
slug still lacks a `topics/<slug>.md` — that's Phase C.

### Phase C — Topic prose (fan out, one agent per topic)
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

### Phase D — Group topics into areas (the upper level)
Group the topics into ~6–8 broad **areas**: one cheap LLM pass over the topic titles/scopes (the
Louvain communities are a prior — community ≈ area), each topic to **exactly one** area, human-gated
like the taxonomy. Save the approved map to `.research/tmp/area_map.json`
(`{"areas":[{"slug","title","scope","topics":[...]}]}`), then stamp the parent links:
```
uv run python .claude/skills/topic-cluster/scripts/apply_areas.py --areas .research/tmp/area_map.json
```
Then fan out **one agent per area** (Workflow): each reads its child *topic notes* and writes the
area's field-level synthesis prose — `## Scope`, `## Sub-areas / themes`, `## Cross-topic tensions`,
`## Open questions` — then calls `write_area.py`. The `## Topics` child-list is added by the script.
(Area synthesis reads topic notes, so run this after Phase C.)

### Finalize
```
uv run python .claude/skills/topic-cluster/scripts/apply_taxonomy.py --validate-only
uv run python .claude/skills/topic-cluster/scripts/apply_areas.py --validate-only
```
Expect clean passes (no dangling membership/area links). Report: N areas, N topics + size
distribution, N orphans, and any graph-disagreement flags worth a human look.

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
topics that gained/lost members** via Phase C. Anchors and untouched members are left alone. A
genuinely **new topic** also gets an area (assign it in `area_map.json`, run `apply_areas`, and refresh
that area note); a new note rarely shifts an existing topic's area.

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
