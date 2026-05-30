# CONTEXT — research-vault

The canonical domain language for this project. Agents and skills MUST use these terms
(not synonyms) in note titles, frontmatter, issue titles, and proposals. If a concept
you need isn't here, that's a signal to add it — don't invent drifting vocabulary.

> Full design, rationale, and build order: [`docs/architecture.md`](docs/architecture.md).
> Decision records: [`docs/adr/`](docs/adr/).

## What this is

A **human–AI collaborative research system**, built as a standalone Obsidian vault that is
also a git repo. It turns a Zotero library into structured knowledge and, ultimately, into
research projects, across **three layers**:

```
Zotero ─/lit-sync─►  literature notes  ─/topic-cluster─►  topic notes
                       (Layer 1)                            (Layer 2)
                                                               │ candidate ideas
                                                               ▼ /promote-idea (human gate)
                                                          project notes  ─/project-status─►  hand-off to project repo
                                                            (Layer 3)
```

## Glossary

### Vaults
- **Vault** — this repo (`~/repos/research-vault`), opened in Obsidian as a second vault,
  distinct from the personal **Zettelkasten** vault (iCloud). Git-versioned.
- **Zettelkasten** — the user's pre-existing personal Obsidian vault. Read-only context for
  agents; **no cross-vault wikilinks** (Obsidian links don't cross vaults).

### Layer 1 — Literature
- **Literature note** — one note per in-scope Zotero item, file `literature/@<citekey>.md`.
  A structured deep summary (~500–1000 words, LaTeX math) of a paper. See schema in `docs/architecture.md`.
- **Citekey** — the BetterBibTeX citation key (e.g. `Bruhin2019`). The stable join key and
  the literature-note filename stem (`@Bruhin2019`). Comes from BBT, **not** `zotero.sqlite`.
- **Obsidian scope** — the Layer-1 scope predicate: items with a PDF attachment **OR** tagged
  `to-note`. `lit-sync` enumerates this predicate directly (sqlite/bib for the list + BBT enrichment);
  optionally mirror it as a Zotero saved search of the same name to view/curate scope. The `to-note`
  tag is the opt-in lever for PDF-less items.
- **`to-note`** — Zotero tag that pulls a PDF-less item into the Obsidian scope.
- **Coverage check** — the verification step in `lit-sync` confirming every major section of a
  PDF was read (not skimmed) before a note is accepted.
- **Manifest** — `.research/manifest.json`: per-citekey content hash (metadata + PDF path/mtime)
  used to detect new/changed items. Machine state; hidden from Obsidian (dot-folder).
- **Citation link** — a `[[@citekey|display]]` wikilink in a note's prose pointing at another
  in-scope paper it cites. Written by the `link_notes.py` post-pass (ADR-0013), never by hand;
  the `related:` frontmatter mirrors them as a citekey edge-list. The citation graph is a primary
  Layer-2 clustering signal alongside `keywords:`.
- **Ghost link** — a citation link to an in-scope paper whose note doesn't exist **yet**. Valid in
  Obsidian; resolves automatically once the note lands. Lets linking run before backfill completes.
  Only in-scope citations are linked — out-of-scope mentions (Luce 1959) stay plain prose.

### Layer 2 — Topics
- **Topic note** — `topics/<topic>.md`. An emergent subject cluster discovered **bottom-up** from
  the literature notes. Contains: scope, sub-themes, cross-paper tensions, **open questions**, and
  **candidate ideas**, plus a live dataview list of member literature notes.
- **Anchor** — an existing topic note that persists across re-clustering. New/changed literature
  notes are clustered **incrementally** against anchors; merges/splits are proposed as a diff.

### Layer 2 → 3 — Ideas
- **Candidate idea** — a one-line research-project pitch in a topic note's *Candidate ideas*
  section, synthesized from the open questions/tensions of that topic's papers.
- **Promotion** — the human-gated act (`/promote-idea`) of turning a candidate idea into a
  project note at `status: feasibility`.

### Layer 3 — Projects
- **Project note** — `projects/<slug>.md`. A research project. Its lifecycle state is the
  `status:` frontmatter property (single folder; no per-state subfolders).
- **status** — one of: `feasibility` → `planned` → `ongoing` → `finished`, with `on-hold`
  (pausable from planned/ongoing) and `rejected` (terminal, reason required) as off-ramps.
  Entry state is always `feasibility`. There is no `idea` status — ideas live in topic notes.
- **Decision log** — a section in each project note holding dated transition lines
  (`2026-05-29 feasibility → planned: <reason>`). The audited home of every state change and the
  required **rejection reason**. Written only by `/project-status`.
- **Execution repo** — the dedicated git repo where a mature project's code/data/paper live
  (recorded in the project note's `repo:` property). The vault hands off to it; it is *not* the vault.

### Cross-cutting
- **AI region / human region** — every generated note splits at a fence marker; everything above
  is agent-owned and regenerable, everything below (`## My notes`) is the user's and never
  overwritten on regeneration.
- **Skill** — a Claude Code skill in `.claude/skills/`, the user-facing entry point (`/lit-sync`,
  `/topic-cluster`, `/promote-idea`, `/project-status`). Mechanical I/O lives in deterministic
  helper scripts; bulk LLM work fans out via the Workflow tool.
- **Cadence** — all skills are **manual/prompted**; nothing runs on a schedule (for now).
