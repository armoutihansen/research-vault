# ADR-0014: Topic-cluster — operational design (extends ADR-0007)

- Status: Accepted
- Date: 2026-05-31
- Extends: [ADR-0007](0007-topic-clustering.md) (bottom-up · incremental · LLM-thematic)

## Context
ADR-0007 set the *stance* for Layer 2 — topics emerge bottom-up, persist as anchors, and are assigned
by LLM theme — but left the build open ("granularity tunable once real clusters exist"). Layer 1 is now
complete: **469 literature notes** with `keywords:` and a materialized citation graph (**1470 edges** in
`related:`, ADR-0013). Designing the `topic-cluster` skill against that real corpus surfaced facts that
force concrete decisions ADR-0007 didn't make:

- The citation graph is **one giant component** (381 of 469 notes; next largest is 6), so topics cannot
  be read off graph components — the whole corpus is one blob.
- `keywords:` is a **sparse long tail** (1527 distinct keywords / 3140 uses, ~2 uses each): the head is a
  good thematic signal, the tail is single-use noise.
- 67 notes have **no citation edges** at all.
- A **compact representation** of a note (citekey · title · year · keywords · `related:` · Summary
  paragraph) is ~130 tokens, so all 469 fit in **one ~70k-token context** — the old "469 notes don't fit
  in one judgment" assumption is false on a 1M-context model.
- The first run has **no anchors**, so "incremental against anchors" is undefined for the bootstrap.

## Decision

### Granularity — idea-generativity, not a fixed count
A topic is the **smallest cluster that still carries internal tension worth a candidate idea** — finer
than a survey area ("social preferences"), coarser than a single paper. Operationally this lands ~20–35
topics of ~10–25 members over the 469 notes, but the *count is an outcome of the principle*, not a target.

### Areas over topics — a two-level emergent hierarchy (amended 2026-05-31)
The idea-generative topics have a parent structure a flat list loses: inequity aversion / reciprocity
are *social preferences*; satisficing / shortlist methods are *bounded rationality*. That structure is
already latent — the Louvain communities are essentially these fields, and the bootstrap's own gate
grouped the 35 topics under exactly such headers. So Layer 2 is a **two-level hierarchy**: a broad
**area** (`areas/<slug>.md`, ~6–8 fields) over the fine **topics**. Decisions: **two levels only** (area
⊃ topic; no deeper tree); each topic in **exactly one area** (a clean navigational tree — genuine
cross-field bridges surface via the citation graph / shared papers, not multi-parenting); area notes are
**synthesis-bearing** (field-level cross-topic tensions + major open questions + a dataview child list),
not mere indexes; the grouping is **emergent + human-gated** like topics (group the existing topics, with
communities as a prior). Single source of truth: a topic's `area:` frontmatter link; area notes derive
their child roster via dataview. The level is **additive** — paper→topic memberships are unchanged.

### The LLM clusters; the citation graph is a prior and a cross-check
Clustering is **LLM-thematic** (ADR-0007), not graph community detection. Even with `networkx` now
installable via `uv`, modularity partitions by *who-cites-whom* (methodological schools, author cliques,
era), which only correlates with research question, and it strands the 67 edge-less notes. For an
idea-generativity target, theme must drive the partition. The graph still earns its keep two ways:
a Louvain community id per note is fed into the compact representation as a **prior** the taxonomy agent
may follow or override on thematic grounds; and after the LLM proposes topics, the thematic partition is
compared to the citation-modularity partition and **large disagreements are flagged for human review**
(a topic that shreds a tight citation community, or a community split across many topics). The graph
informs and audits; the LLM decides. Promoting graph community detection to the partitioner is a possible
future refinement, not v1.

### First-run bootstrap — four phases, single-context taxonomy, human-gated
1. **Taxonomy (one agent, one shot).** A deterministic script emits the compact representation of all 469
   notes (~110k tokens); one Opus 1M-context agent proposes the whole topic set — `{topic, slug, scope,
   members[]}` — as **one globally consistent partition**, self-checking for grab-bags, near-duplicates,
   and coverage before returning. Single-context is deliberate: it avoids the cross-batch topic-merge
   problem a map-reduce or competing-panel approach would create.
2. **Human gate, with deterministic annotation.** There is **no separate LLM "critic" phase.** With a
   single taxonomy agent (not a competing panel), a second agent re-running the same thematic judgment is
   just that judgment done twice, with no fitness signal to iterate against — and the genuine cold-eyes
   review is the *human's*. What the critic was really doing splits in two: the **mechanical** checks
   (coverage, cap/singletons, empty topics, and the **graph cross-check** — agreement of the thematic
   partition with the Louvain citation communities) are deterministic and move into a script
   (`report_taxonomy.py`); the **judgment** calls (grab-bag? duplicate?) are the human's, made far better
   with those stats in front of them. So: annotate the proposal, present it (topics · sizes · member
   previews · orphans · flags), and the user approves/edits before anything is written. Refinement is
   *iteration here*, driven by the user's calls — which is where revision finally has a signal. The
   bootstrap is the largest "diff" Layer 2 will ever produce, so it is gated like every later merge/split
   (ADR-0007).
3. **Apply membership (deterministic write-back).** Stamps `topics:` into member frontmatter (idempotent,
   AI region only) and records state.
4. **Topic prose (fan-out, one agent/topic).** Each agent reads the **full summaries** of its members and
   writes the topic note: scope · sub-themes · cross-paper tensions · open questions · candidate ideas;
   the script adds the derived Members/Bordering-work/Promoted blocks and writes `topics/<slug>.md`.

### Membership — multi, by centrality, not a partition
A literature note is a full **member of one *or more* topics** (overriding ADR-0007's singular "a topic"),
but only when it is *central to that topic's core tension*, not merely relevant — with a **soft cap of ~3**
the critic enforces. The foundational hubs (Fehr & Schmidt 1999; Kahneman & Tversky 1979) are genuinely
co-central to several topics, and those boundary-spanning notes are the richest candidate-idea sources, so
forcing a single home would discard the most valuable structure. Topic sizes therefore **do not sum to
469**, which is honest, not a bug. Merely-related papers are *not* members; they surface as **citation-
derived bordering work** (from `related:` edges that cross topics), so multi-membership never dilutes a
topic's roster.

### Coverage — full coverage attempted, orphans allowed, no junk drawer
Every note should land in a topic, but the agent assigns `topics: []` when nothing fits rather than forcing
a misfit (one off-topic paper pollutes the very tension that makes a topic idea-generative). Orphans go
into the review report with a reason — **never into a manufactured "misc" topic** (a junk drawer that
never gets cleaned and pollutes the Obsidian graph). Most orphans are expected to *be* the known Zotero
data-quality casualties (mis-scanned/mismatched PDFs), so the orphan list doubles as a data-cleanup signal.

### Topic identity & what survives a re-cluster
- **Stable slug = anchor identity.** `topics/<slug>.md`; the kebab slug is fixed at birth and is the
  anchor's permanent identity (members link `topics: [[<slug>]]`). The human-readable **title** can be
  refined in place across runs; **renames/merges/splits are explicit scripted diff operations** (move file
  + rewrite every member link), never silent drift — mirroring `citekey` as the immutable lit-note key.
- **Same AI/human fence as lit notes (ADR-0005).** Scope/sub-themes/tensions/open-questions/candidate-
  ideas/dataview are regenerable; `## My notes` below the fence is never touched.
- **Candidate ideas are regenerable; promotion extracts them to Layer 3.** Rather than pinning a promoted
  idea inside the topic note (fragile carry-forward state), `/promote-idea` makes the **project note the
  source of truth** and stamps a back-link to its source topic; the topic note shows a dataview "Promoted
  from this topic" list (derived, not stored). So regeneration may freely churn *un*-promoted ideas and can
  never destroy a promoted one. This is the answer to ADR-0007's "re-clustering orphans promoted ideas".

### Incremental runs (the everyday path after bootstrap)
- **Only pending notes re-cluster:** a note is pending if `topics:` is empty (new from `lit-sync`) or its
  manifest content-hash changed since last clustered (tracked in `.research/topic_state.json`). Anchors and
  settled members are untouched.
- **Default run = assignment only.** Each pending note is assigned to best-fit topic(s) (capped multi) or
  flagged "needs new topic." New-topic flags are *pooled* (one stray paper doesn't mint a topic; a burst of
  related ones might) and pass the same human gate. Only topics that gained/lost members are re-prosed.
- **Merge/split = a separate, explicit re-balance pass** (`--rebalance`), not run every time (it is
  expensive and churny). Auto-*suggested* when a heuristic trips (topic > ~40 members → split candidate;
  two topics' member+citation overlap over threshold → merge candidate). Emits a reviewable diff; on
  approval a script applies it. A deliberate, rare, human-invoked **full re-bootstrap** is the escape hatch
  for large drift (re-mints slugs; human-region migration deferred until needed).

### Write contract — single source of truth, idempotent writer, validation
- **Membership lives only in the lit note's `topics:` frontmatter.** Topic notes store *no* roster; members
  render via a live dataview query (`WHERE contains(topics, this.file.link)`) — like `related:`/backlinks.
  One write site, no sync drift; orphans = `topics: []`, topic size = dataview count.
- **LLM judgment is gated and persisted; a deterministic script does the write-back** (AI region only), so
  re-running with no new/changed notes is a **true no-op**. Non-determinism is contained to pending notes
  and explicit re-balances.
- **A validation pass** ends every invocation: every pending note resolved, no `topics:` link to a missing
  slug, every topic note has ≥1 member, no membership over the soft cap without a critic note. Failures
  block the write and surface for review. New machine state: `.research/topic_state.json` only.

## Consequences
- A concrete, buildable `topic-cluster` skill that reuses the `lit-sync` pattern (deterministic scripts +
  gated LLM fan-out) and the ADR-0013 idempotency discipline.
- Topics are thematic and idea-oriented, not citation-clique artifacts; the 67 edge-less notes cluster
  normally on their text.
- Topic sizes overlap (no clean partition) and rosters are dataview-derived (no stored membership) — a
  deliberate trade of "tidy partition" for "honest overlap + zero sync drift."
- The bootstrap is one big human-gated decision; everyday runs are cheap, no-op-clean, and low-churn.
- LLM clustering variance is bounded by persistence + the pending-only re-cluster rule + the human gate;
  it is not eliminated, which is acceptable because every structural change is reviewed.

## Alternatives considered
- **Graph community detection as the partitioner** (now dependency-free via `uv`) — reproducible, but
  clusters by citation clique not research question and strands edge-less notes. Kept as prior + cross-check
  only.
- **Map-reduce / competing-panel taxonomy** (cluster batches, then merge) — needed when notes don't fit one
  context; they do (~70k tokens), and merging near-duplicate cross-batch topics is the hard, churny part.
  Rejected in favor of a single-context taxonomy + human gate.
- **Strict single membership** — clean partition and trivially-defined incremental ownership, but
  mis-describes the foundational hubs and discards the boundary-spanning notes that generate the best
  ideas. Rejected.
- **Stored member roster in the topic note** — lets a topic note stand alone, but duplicates membership and
  invites drift between the two copies. Rejected for dataview-derived rosters.
- **Pinning promoted ideas inside the topic note** — keeps the idea visible in place, but forces the
  regenerator to carry fragile state and risks dropping a promoted idea on churn. Rejected for Layer-3
  extraction + dataview back-link.
- **A "misc/unsorted" topic for non-fitters** — guarantees full coverage, but becomes an uncleaned junk
  drawer and a fake node in the graph. Rejected for explicit `topics: []` orphans + review report.
