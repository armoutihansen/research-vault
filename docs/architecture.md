# research-vault — Architecture & Design

Status: **Accepted** (design phase) · Date: 2026-05-29

A human–AI collaborative research system: a standalone, git-versioned Obsidian vault that turns a
Zotero library into literature notes → emergent topic notes → research projects with a tracked
lifecycle. Vocabulary is defined in [`CONTEXT.md`](../CONTEXT.md); each decision below has an ADR in
[`adr/`](adr/).

## Design decisions (summary)

| # | Decision | Choice | ADR |
|---|----------|--------|-----|
| 1 | Vault home | Standalone git vault, opened in Obsidian as a 2nd vault | [0001](adr/0001-standalone-git-vault.md) |
| 2 | Note I/O | Hybrid: file ops primary, Obsidian CLI for niceties | [0002](adr/0002-hybrid-note-io.md) |
| 3 | Lit-note scope | PDF-bearing items (~481) + `to-note` tag, via a Zotero saved search | [0003](adr/0003-literature-scope.md) |
| 4 | Note depth | Structured deep note (~300–600 w), fixed analytical sections | [0004](adr/0004-literature-note-schema.md) |
| 5 | Project state | `status:` frontmatter property, single folder, dataview/kanban | [0009](adr/0009-project-state-machine.md) |
| 6 | AI/human split | Managed AI region + protected human region in one note | [0005](adr/0005-ai-human-regions.md) |
| 7 | Sync source | Zotero saved search + live BBT pull + content-hash manifest | [0006](adr/0006-zotero-sync.md) |
| 8 | Topic derivation | Pure bottom-up (emergent, no seeding) | [0007](adr/0007-topic-clustering.md) |
| 9 | Re-cluster model | Incremental — anchors persist, merge/split diffs | [0007](adr/0007-topic-clustering.md) |
| 10 | Cluster method | LLM-thematic (no embedding infra) | [0007](adr/0007-topic-clustering.md) |
| 11 | Idea generation | Topic-note ideas → human-gated promotion | [0008](adr/0008-idea-generation.md) |
| 12 | Transitions | Logged `project-status` skill + mandatory reasons | [0009](adr/0009-project-state-machine.md) |
| 13 | Execution boundary | Hand off to per-project repos; vault issues = vault dev | [0010](adr/0010-execution-boundary.md) |
| 14 | Skill form | Skills + deterministic scripts + Workflow fan-out | [0011](adr/0011-skill-architecture.md) |
| 15 | Cadence | All manual / prompted | [0012](adr/0012-manual-cadence.md) |
| 16 | Reading | Section map-reduce + coverage check, length-adaptive | [0004](adr/0004-literature-note-schema.md) |

## Data flow

```
Zotero ── saved search "Obsidian scope" (PDF ∪ #to-note)
   │
   ▼  /lit-sync   ─ enumerate (PDF ∪ #to-note) via sqlite/bib · enrich via BBT (abstract · path · highlights) · diff manifest
   │              ─ per new/changed item: segment PDF → map-reduce summarize → coverage check
literature/@<citekey>.md       Layer 1  (AI region ⌐ + human region)
   │
   ▼  /topic-cluster  ─ incremental LLM-thematic; assign new notes to anchor or new topic
   │                  ─ refresh topic prose; propose merges/splits as a diff
topics/<topic>.md              Layer 2  (scope · tensions · open questions · candidate ideas · dataview list)
   │
   ▼  /promote-idea   ─ human picks a candidate idea (the gate)
projects/<slug>.md             Layer 3  status: feasibility → planned → ongoing → finished
   │                                                  ↘ on-hold ↗      ↘ rejected (reason required)
   ▼  /project-status (logged: status + Decision log)
hand off → per-project execution repo (repo: property)
```

## Repository layout

```
research-vault/
├── CLAUDE.md, docs/agents/        # skill config + GitHub issue tracker (Matt Pocock setup)
├── CONTEXT.md                     # canonical vocabulary
├── docs/architecture.md, docs/adr/
├── .claude/skills/                # lit-sync, topic-cluster, promote-idea, project-status, feasibility
├── literature/                    # Layer 1: @<citekey>.md
├── topics/                        # Layer 2: <topic>.md
├── projects/                      # Layer 3: <slug>.md
└── .research/                     # machine state: manifest.json, sync logs (hidden from Obsidian)
```

## Literature-note schema

```markdown
---
citekey: hansen2024predictive
title: "..."
authors: [Hansen, J., ...]
year: 2024
type: journalArticle
doi: 10.xxxx/...
zotero: "zotero://select/..."         # click → open in Zotero
pdf: "/Users/.../storage/.../x.pdf"
tags: [literature]
keywords: [predictive-completeness, social-preferences]   # extracted → fuels clustering
topics: []        # [[wikilinks]] to topic notes — filled by /topic-cluster
related: []       # [[@othercitekey]] — filled during synthesis
added: 2026-05-29
generated: 2026-05-29                  # AI provenance
---

> [!abstract] Abstract
> {verbatim from Zotero}

## Summary
## Research question
## Method / identification
## Data
## Key findings
## Contribution
## Limitations & open questions     ← the project-idea hook
## Connections

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
```

## Reading mechanism (map-reduce)

1. **Extract & segment** — `pdftotext`; detect section headings (or PDF TOC via `pdfinfo`). Fallback
   to Claude visual `Read` (≤20 pp/request) for scanned/image/math-heavy PDFs.
2. **Map** — summarize each section into the schema slot it feeds (methods→Method/Data,
   results→Key findings, discussion→Limitations/Contribution).
3. **Reduce** — synthesize section summaries into the ~300–600-word note.
4. **Coverage check** — verify every major section was captured; flag any that yielded nothing.
5. **Length-adaptive** — articles (≤~50 pp) fully mapped; books/theses → chapter-level + targeted.

No OCR is installed (`tesseract`/`mutool` absent); the visual `Read` fallback covers scanned PDFs.

## Skill inventory (`.claude/skills/`)

| Skill | Layer | Responsibility |
|-------|-------|----------------|
| `lit-sync` | 1 | Enumerate scope (PDF ∪ #to-note) via sqlite/bib → enrich via BBT (abstract, path, highlights) → diff manifest → map-reduce read → write/refresh `literature/@<citekey>.md` (AI region only) → update manifest. Bulk = Workflow fan-out (one agent/paper). |
| `topic-cluster` | 2 | Incremental LLM-thematic clustering of new/changed lit notes; refresh topic notes (themes, tensions, open questions, candidate ideas); propose merges/splits as a diff. |
| `promote-idea` | 2→3 | Turn a chosen candidate idea into `projects/<slug>.md` at `status: feasibility`, linked to topic + source lit notes. |
| `project-status` | 3 | Logged state transition: set `status`, stamp `updated`, append a Decision-log line; require a reason for `rejected`/`on-hold`. |
| `feasibility` | 3 | **Deferred stub.** The real feasibility-assessment process is built later. |

Reuse: Matt Pocock skills (`to-prd`/`to-issues`/`triage` for vault development; `tdd`/`diagnose`).
Format reference: kepano's `obsidian-markdown` skill (Obsidian-Flavored-Markdown conventions).

Mechanical I/O (BBT pull, manifest diff, PDF segment/extract) lives in **deterministic helper
scripts** the skills call; only judgment steps (summarize, cluster, synthesize) use the LLM.

## Build order

1. **Prereqs** (some require the user): register `research-vault` as an Obsidian vault; install
   dataview + kanban + citation-plugin + linter; create the Zotero saved search `Obsidian scope`.
2. **`lit-sync`** — helper scripts + map-reduce note writer.
3. **Pilot** ~15 papers → review → tune schema/prompt.
4. **Backfill** ~481 via Workflow fan-out.
5. **`topic-cluster`** over the backfill.
6. **`promote-idea`** + **`project-status`**.
7. *(later)* the real **feasibility** process.

## Deferred / open

- **Feasibility process** — deliberately deferred.
- **The ~11.7k Zotero firehose** (May-2026 bulk import, no PDFs) — walled off; long-term triage TBD.
- **Keyword vocabulary** — free LLM-extracted by default; controlled vocab + tag-wrangler later.
- **Zettelkasten cross-pollination** — readable for context, but no cross-vault links; mining it is open.
- **Topic granularity & merge/split cadence** — tune once real clusters exist.

## Appendix — environment facts (discovered 2026-05-29)

- **Zotero**: 12,224 bibliographic items (12,130 journal articles); **481 PDFs**; abstracts on 12,061;
  only 91 items filed in collections. Split: ~536 curated (2022–early 2026) vs **11,227 bulk-imported
  May 2026** (no PDFs). The 481 PDFs are all on the curated set → Layer-1 scope.
- **BetterBibTeX**: live JSON-RPC at `http://127.0.0.1:23119/better-bibtex/json-rpc` (verified).
  `item.search` returns CSL-JSON incl. `citekey`, `abstract`, `author`, `DOI`, `issued`, `type`;
  `item.attachments(citekey)` resolves PDF paths **and the user's highlight annotations**. The biblatex
  auto-export `~/Documents/Academics/library.bib` (509 entries) omits the 11.7k firehose — fine, since
  509 ≈ the in-scope curated PDF set; usable for enumeration when refreshed.
- **Obsidian**: app installed; official CLI available (`/usr/local/bin/obsidian`, requires the app
  running). Mature personal vault `Zettelkasten` (695 notes) with citation-plugin, dataview, kanban,
  pandoc-reference-list, omnisearch already configured.
- **Tooling**: `pdftotext` ✓, `sqlite3` ✓; `tesseract`/`mutool`/`ollama`/`llm` ✗; no embedding API keys.
