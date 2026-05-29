---
name: lit-sync
description: Sync the Zotero library into Layer-1 literature notes. Use when the user wants to create/refresh literature notes, ingest new papers from Zotero, run the literature backfill, or says "/lit-sync". Reads PDFs via map-reduce and writes structured deep notes to literature/@<citekey>.md.
---

# lit-sync

Turn in-scope Zotero items into structured **literature notes** (`literature/@<citekey>.md`).
Deterministic I/O lives in `scripts/`; the reading/summarizing is your job, done with the
map-reduce discipline below. See [`../../../CONTEXT.md`](../../../CONTEXT.md) and
[`../../../docs/adr/0004-literature-note-schema.md`](../../../docs/adr/0004-literature-note-schema.md).

## Prerequisites
- **Zotero must be running** (BBT serves citekeys/attachments on :23119).
- Run from the vault root.

## Scripts (deterministic — always use these, don't hand-roll the I/O)
- `scripts/enumerate.py` — list in-scope items (PDF ∪ `#to-note`) + metadata, resolve citekeys,
  diff the manifest. Emits a JSON work-list. Flags: `--limit N` (pilot), `--status new,changed`,
  `--out FILE`.
- `scripts/extract_pdf.py PATH` — `pdftotext` + section segmentation → `{pages, n_chars,
  needs_visual, truncated, sections:[{heading,text}]}`.
- `scripts/bbt.py attachments <citekey>` — PDF path **and the user's highlight annotations**.
- `scripts/write_note.py --item item.json --body body.md --keywords a,b` — write/refresh the note
  (preserving the human region) and update the manifest. Never write `literature/*.md` by hand.

## Procedure

### 1. Enumerate
```
python3 .claude/skills/lit-sync/scripts/enumerate.py --status new,changed --out .research/work.json
```
For a **pilot**, add `--limit 15`. The work-list `.items[]` each have: citekey, title, authors,
year, type, doi, abstract, pdf_path, hash, status.

### 2. For each work item — read, summarize, write
Per paper (fan out for bulk — see §4):

1. **Read the PDF** — `extract_pdf.py <pdf_path>`.
   - `needs_visual: true` (scanned/image) → read the PDF with the **`Read` tool** (visual, ≤20
     pages/request) instead of the extracted text.
   - `pages > 50` (book/thesis) → **targeted/chapter-level**: read front matter + intro + a TOC-led
     sample + conclusion; do NOT ingest the whole thing. Note in the summary that coverage was targeted.
   - otherwise → use the segmented `sections`.
2. **Fetch highlights** (optional signal) — `bbt.py attachments <citekey>`; if the user has
   annotations, weight the summary toward what they highlighted and you may seed a line in
   *Connections*. Never put highlights below the fence (that's the user's region).
3. **Map** — summarize each section into the schema slot it feeds (methods→Method/Data,
   results→Key findings, discussion→Limitations/Contribution).
4. **Reduce** — synthesize a **~300–600 word** note body with these exact sections (the abstract
   callout is prepended automatically? no — include it):

   ```markdown
   > [!abstract] Abstract
   > <verbatim abstract from the work item>

   ## Summary
   <1 short paragraph TL;DR>
   ## Research question
   ## Method / identification
   ## Data
   ## Key findings
   ## Contribution
   ## Limitations & open questions
   ## Connections
   ```
   Use the project's vocabulary (CONTEXT.md). *Limitations & open questions* is the project-idea
   hook — make it substantive. Leave *Connections* light for now (Layer 2 fills links).
5. **Coverage check** — confirm every major section of the paper is represented. If a section
   produced nothing (e.g. no Data section in a theory paper), say so explicitly rather than padding.
6. **Extract keywords** — 3–8 lowercase-kebab concepts for clustering (e.g. `stochastic-choice`,
   `limited-attention`).
7. **Write** — pass the work item and your body to `write_note.py`:
   ```
   python3 .claude/skills/lit-sync/scripts/write_note.py \
     --item <(jq '.items[i]' .research/work.json) --body /tmp/body.md --keywords "k1,k2,k3"
   ```

### 3. Report
Summarize: N created, N refreshed, N skipped, any `needs_visual`/targeted cases, any coverage gaps.

### 4. Bulk backfill (the ~471 set)
Use the **Workflow** tool to fan out one agent per paper (requires the user to opt into workflows).
Each agent does §2 for one work item and returns a status line. Pilot first (`--limit 15`), let the
user review and tune this SKILL's template/prompt, *then* backfill the rest.

## Notes
- Idempotent: re-running only rewrites the AI region; the user's `## My notes` is preserved.
- Change detection is by content hash (metadata + PDF path/mtime); unchanged items are skipped.
- No OCR is installed — the visual `Read` fallback covers scanned PDFs.
