# ADR-0002: Hybrid note I/O — file ops primary, Obsidian CLI for niceties

- Status: Accepted
- Date: 2026-05-29

## Context
Notes can be manipulated via Claude Code's native file tools or via the official Obsidian CLI. The
CLI offers link resolution/search/property handling but **requires the Obsidian app to be running**,
which breaks AFK/cron use and is slower over IPC. The vault is git-versioned and AFK-safe by design
(ADR-0001).

## Decision
**Direct file operations** (`Read`/`Write`/`Edit`/`Glob`/`Grep`) are the primary mechanism for all
bulk read/write. The **Obsidian CLI** is a thin optional layer for human-facing niceties only
(`obsidian open <note>`, interactive search). Note *format* follows kepano's `obsidian-markdown`
conventions regardless of mechanism.

## Consequences
- I/O never depends on the GUI being open; deterministic and testable.
- We implement Obsidian-Flavored-Markdown conventions ourselves (just markdown).
- CLI niceties available when a human is in the loop.

## Alternatives considered
- **Pure file ops** — simplest, but forgoes even `obsidian open`.
- **CLI primary** — built-in link/search/properties, but requires the app running; breaks automation.
