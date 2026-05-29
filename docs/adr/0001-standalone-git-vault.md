# ADR-0001: Standalone git vault, separate from the Zettelkasten

- Status: Accepted
- Date: 2026-05-29

## Context
The user already runs a mature personal Obsidian vault (`Zettelkasten`, iCloud-synced, 695 notes)
with the exact plugins this project needs. The new research system could live as folders inside it,
or as a new vault. The system is agent-driven and generates potentially hundreds of notes.

## Decision
The research vault is a **standalone Obsidian vault = the `~/repos/research-vault` git repo**, opened
in Obsidian as a second vault.

## Consequences
- Git versioning: diffable, reviewable, AFK-safe agent writes; no iCloud sync conflicts.
- The curated Zettelkasten is not polluted by bulk AI-generated notes.
- One-time cost: re-point the citation plugin and re-install a few plugins in the new vault.
- No cross-vault wikilinks to Zettelkasten; agents may read it read-only for context.

## Alternatives considered
- **Folders inside Zettelkasten** — instant plugin/graph reuse, but iCloud (not git), pollution risk,
  unattended-write conflicts.
- **Standalone but iCloud-synced** — separation + mobile sync, but no version control.
