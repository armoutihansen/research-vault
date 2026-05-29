#!/usr/bin/env python3
"""Write or refresh a literature note, preserving the human region, and update the manifest.

The note splits at FENCE: everything ABOVE is AI-owned and rewritten on every run; everything
BELOW (the user's `## My notes`) is preserved verbatim (ADR-0005). Frontmatter + AI body come
from the model; this script handles the safe merge, the schema, and the manifest bookkeeping so
those stay deterministic.

Usage:
  write_note.py --item item.json --body body.md [--keywords a,b,c]
                [--vault DIR] [--generated YYYY-MM-DD]

`item.json` is one element of enumerate.py's work-list (citekey, title, authors, year, type,
doi, item_key, library_id, pdf_path, hash). `body.md` is the AI-written markdown (the sections
below the abstract). Standard library only.
"""
import argparse
import fcntl
import json
import os
import sys
from datetime import date
from pathlib import Path

FENCE = "%% ─── below is yours; regeneration never touches it ─── %%"
DEFAULT_HUMAN = FENCE + "\n## My notes\n"


def find_vault(start):
    p = Path(start).resolve()
    for cand in [p, *p.parents]:
        if (cand / ".research").exists() or (cand / "CONTEXT.md").exists():
            return cand
    return p


def yaml_scalar(v):
    s = str(v)
    if s == "":
        return '""'
    # Quote when YAML could misread it.
    if any(c in s for c in ':#[]{}",&*!|>%@`') or s[0] in "-? " or s != s.strip():
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def yaml_list(items):
    return "[" + ", ".join(yaml_scalar(x) for x in items) + "]"


def build_frontmatter(item, keywords, generated):
    lib = item.get("library_id", 1)
    key = item.get("item_key", "")
    zotero = f"zotero://select/library/items/{key}" if lib == 1 else \
        f"zotero://select/groups/{lib}/items/{key}"
    rows = [
        ("citekey", yaml_scalar(item["citekey"])),
        ("title", yaml_scalar(item.get("title", ""))),
        ("authors", yaml_list(item.get("authors", []))),
        ("year", yaml_scalar(item.get("year", ""))),
        ("type", yaml_scalar(item.get("type", ""))),
        ("doi", yaml_scalar(item.get("doi", ""))),
        ("zotero", yaml_scalar(zotero)),
        ("pdf", yaml_scalar(item.get("pdf_path", "") or "")),
        ("tags", yaml_list(["literature"])),
        ("keywords", yaml_list(keywords)),
        ("topics", "[]"),
        ("related", "[]"),
        ("added", yaml_scalar(generated)),
        ("generated", yaml_scalar(generated)),
    ]
    return "---\n" + "".join(f"{k}: {v}\n" for k, v in rows) + "---\n"


def split_human(existing):
    """Return the human region (fence + below) of an existing note, or the default."""
    if existing and FENCE in existing:
        idx = existing.index(FENCE)
        return existing[idx:]
    return DEFAULT_HUMAN


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--item", required=True, help="work-item JSON (path or '-')")
    ap.add_argument("--body", required=True, help="AI body markdown (path or '-')")
    ap.add_argument("--keywords", default="", help="comma-separated keywords")
    ap.add_argument("--vault", default=None)
    ap.add_argument("--generated", default=date.today().isoformat())
    args = ap.parse_args()

    item = json.load(sys.stdin) if args.item == "-" else json.loads(Path(args.item).read_text())
    body = sys.stdin.read() if args.body == "-" else Path(args.body).read_text()
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]

    vault = Path(args.vault).resolve() if args.vault else find_vault(os.getcwd())
    citekey = item["citekey"]
    note_path = vault / "literature" / f"@{citekey}.md"
    note_path.parent.mkdir(parents=True, exist_ok=True)

    fm = build_frontmatter(item, keywords, args.generated)
    ai_region = fm + "\n" + body.strip() + "\n\n"
    human_region = split_human(note_path.read_text() if note_path.exists() else None)
    note_path.write_text(ai_region + human_region)

    # Update the manifest (change-detection state). Guarded by an exclusive file lock so that
    # parallel write_note.py processes (e.g. a Workflow fan-out) don't clobber each other's entries.
    manifest_path = vault / ".research" / "manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = manifest_path.parent / "manifest.lock"
    entry = {
        "hash": item.get("hash", ""),
        "generated": args.generated,
        "pdf": item.get("pdf_path", ""),
        "title": item.get("title", ""),
    }
    with open(lock_path, "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
        manifest[citekey] = entry
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True))
        fcntl.flock(lock, fcntl.LOCK_UN)

    print(f"wrote {note_path.relative_to(vault)} (manifest: {len(manifest)} entries)")


if __name__ == "__main__":
    main()
