# research-vault — How it works

Status snapshot: **2026-06-01**. The operational guide — *what steps you can take and what each does*.
For the design rationale see [`architecture.md`](architecture.md); for vocabulary
[`../CONTEXT.md`](../CONTEXT.md); for decisions [`adr/`](adr/).

The vault is a three-layer pipeline that turns a Zotero library into research projects, plus a
cross-cutting open-access literature layer. Everything is **manual/prompted** (nothing runs on a
schedule); bulk work fans out via the **Workflow** tool (user opt-in); every generated note has an
**AI region** above a fence (regenerated freely) and a **human region** (`## My notes`) below it that
is never overwritten.

```
Zotero ──/lit-sync──► literature notes ──/topic-cluster──► topics ⊂ areas ──/idea-harvest──► idea dossier
          (Layer 1)                         (Layer 2)                       (Layer 2→3 bridge)
                                                                                  │ pick an idea
                                                                                  ▼ /promote-idea   ⟵ not built yet
                                                                            project notes ──/project-status──► execution repo
                                                                              (Layer 3)            ⟵ not built yet
```

---

## Steps you can take today (built)

### `/lit-sync` — build/refresh literature notes (Layer 1)
Turns in-scope Zotero items into `literature/@<citekey>.md`.
1. **Enumerate scope** (`scripts/enumerate.py`) — items with a PDF **or** tagged `#to-note`; pull
   metadata, PDF path, and your highlights from BetterBibTeX; **diff the content-hash manifest**
   (`.research/manifest.json`) to process only *new*/*changed* items.
2. **Read the PDF** (`scripts/extract_pdf.py`) — `pdftotext` + section segmentation; visual `Read`
   fallback for scanned PDFs; targeted/chapter reading for books.
3. **Map-reduce summarize** → a ~500–1000-word structured note (8 fixed analytical sections + a
   verbatim abstract callout + LaTeX math), with a coverage check.
4. **Write** (`scripts/write_note.py`) — frontmatter + AI body; **preserves `## My notes`**; updates
   the manifest. Notes are never hand-edited.
5. **Link pass** (`scripts/link_notes.py`) — resolve in-scope prose citations into `[[@citekey]]`
   wikilinks and rebuild the `related:` edge-list (the **citation graph**). Idempotent, re-runnable;
   links to not-yet-written in-scope notes are valid ghost links.

Bulk = a Workflow fan-out, one agent per paper, with one link pass per chunk. → `literature/`.

### `/topic-cluster` — cluster into topics & areas (Layer 2)
Groups the literature notes bottom-up into an emergent **two-level hierarchy** (areas ⊃ topics).
Granularity is set by *idea-generativity* (the smallest cluster with a tension worth a project idea).
- **Bootstrap (first run):** `make_input.py` emits a compact rep of every note (+ Louvain
  citation-community id as a prior) → one taxonomy agent proposes the whole topic set →
  `report_taxonomy.py` annotates it (sizes, coverage, graph-purity flags) → **human gate (you approve)**
  → `apply_taxonomy.py` stamps membership into each note's `topics:` → Workflow fan-out
  (`write_topic.py`) writes each topic note → topics grouped into areas (`apply_areas.py` stamps each
  topic's `area:`) → `write_area.py` writes each area note (field-level synthesis).
- **Incremental:** re-cluster only *pending* notes (empty `topics:` or changed hash, tracked in
  `.research/topic_state.json`) against existing anchors; new-topic proposals pooled + gated.
- **Rebalance:** gated merge/split as a reviewable diff.

Invariants: membership lives **only** in each lit note's `topics:`; topic/area notes list members via
live **dataview**; a paper can be a member of more than one topic (by centrality); genuine misfits are
orphaned (`topics: []`); all writers idempotent. → `topics/`, `areas/`.

### `/idea-harvest` — mine & vet project ideas (Layer 2→3 bridge)
A Workflow that reads the topic/area notes and produces a ranked idea dossier:
1. **Mine** (per area + cross-area hunters) — strongest existing + synthesized cross-cutting ideas,
   from the vault only.
2. **Consolidate** — dedup/merge into a numbered set.
3. **Vet** (adversarial, one per idea) — score novelty / feasibility / fit / grounding, with **grounded**
   novelty via `biblio` (`search` + `recent` for prior work; `verify` to existence-check every claim —
   no phantom citations).
4. **Synthesize** — ranked dossier → `ideas/idea-harvest-<date>.md`, plus an **acquire-list**
   (`acquire_list.py`) of relevant papers *not* in your library, deduped, with DOI + OA link.

---

## The open-access literature layer (cross-cutting, ADR-0015)
`.claude/scripts/biblio.py` is the **only** way the system touches external literature.
- **`search`** (OpenAlex) — recent/relevant work · **`recent --fields nep-…`** (RePEc/NEP) — newest econ
  working papers · **`verify`** (OpenAlex/Crossref) — confirm a citation is a real paper.
- **Metadata + abstracts only — never full-text.** Enforced structurally: the client only contacts an
  allowlist of open hosts (`api.openalex.org`, `api.crossref.org`, `nep.repec.org`) and refuses
  full-text URLs; a `PreToolUse` hook (`scripts/block_fulltext_fetch.py`, registered in
  `.claude/settings.json`) blocks any stray `WebFetch` of a PDF/publisher URL. Agents are not given raw
  web-fetch for papers.
- **Full-text only ever enters via your Zotero.** When something is needed, the system emits an
  **acquire-list** (DOI + OA link) for *you* to acquire and route back through `/lit-sync`.

This layer is consumed by `/idea-harvest` (and, in future, a `lit-sync` freshness pass) — **not** by
`/topic-cluster`, which works on the existing corpus only.

---

## Machine state & conventions
- `.research/manifest.json` — per-citekey content hash (lit-sync change detection).
- `.research/link_index.json` — citation-link candidate index.
- `.research/topic_state.json` — per-note last-clustered hash (topic-cluster pending detector).
- The repo is a **public git repo**; PDFs never live in it (notes carry a `pdf:` path into Zotero
  storage). All Python runs via `uv run` (`pyproject.toml` / `uv.lock`). Decisions are recorded as ADRs
  in `docs/adr/`; canonical terms in `CONTEXT.md`.

---

## Not built yet (designed / stubbed)
- **`/promote-idea`** (Layer 2→3) — turn a chosen candidate idea into `projects/<slug>.md` at
  `status: feasibility`, back-linked to its source topic (the project's `topics:` link powers the topic
  note's *Promoted from this topic* view).
- **`/project-status`** (Layer 3) — logged state transitions
  (`feasibility → planned → ongoing → finished`, with `on-hold` / `rejected`) + a Decision log.
- **feasibility** assessment process — deliberately deferred.
- **`lit-sync` freshness + citekey-migration** — a future ADR: detect a working paper that has since
  been published (via `biblio`), and migrate a note's citekey (rename + rewrite every inbound
  `related:` / `topics:` / `area:` / citation link + manifest/state).

---

## Current snapshot
literature **467** · topics **35** ⊂ areas **6** · idea dossiers **1** (`ideas/`) · projects **0** ·
ADRs **0001–0015**. Today you can go **Zotero → literature notes → topics/areas → a vetted idea
dossier**, with safe access to newer literature throughout. The open frontier is **Layer 3** (turning a
chosen idea into a tracked project) and the **lit-sync freshness loop**.
