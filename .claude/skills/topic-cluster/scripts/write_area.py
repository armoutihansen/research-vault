#!/usr/bin/env python3
"""Write or refresh an area note (areas/<slug>.md), preserving the human region (ADR-0014, ADR-0005).

The upper level of the Layer-2 hierarchy. Like write_topic.py: the *agent* writes the field-level
synthesis prose — Scope, Sub-areas / themes, Cross-topic tensions, Open questions — and passes it as
--body; this script owns the frontmatter, the stable slug identity, and the derived `## Topics` block
(a dataview over child topics whose `area:` links here — the single source of truth being each topic's
`area:`). `created` is fixed at birth; title/scope/body refresh in place.

Usage (from vault root, via `uv run`):
  write_area.py --slug social-other-regarding-preferences --title "Social & Other-Regarding Preferences" \
    --scope "one-line scope" --body body.md [--generated YYYY-MM-DD]
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

import corpus


def yaml_scalar(v):
    s = str(v)
    if s == "":
        return '""'
    if any(c in s for c in ':#[]{}",&*!|>%@`') or s[0] in "-? " or s != s.strip():
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


TOPICS_BLOCK = (
    "## Topics\n"
    "```dataview\n"
    "TABLE scope AS Scope\n"
    'FROM "topics"\n'
    "WHERE area = this.file.link\n"
    "SORT file.name ASC\n"
    "```\n"
)


def build_frontmatter(slug, title, scope, created, generated):
    rows = [
        ("slug", yaml_scalar(slug)),
        ("title", yaml_scalar(title)),
        ("type", "area"),
        ("scope", yaml_scalar(scope)),
        ("tags", "[area]"),
        ("created", yaml_scalar(created)),
        ("generated", yaml_scalar(generated)),
    ]
    return "---\n" + "".join(f"{k}: {v}\n" for k, v in rows) + "---\n"


def existing_created(text, fallback):
    m = re.search(r"^created:\s*(.*)$", text, flags=re.M)
    return (m.group(1).strip().strip('"') if m else None) or fallback


def split_human(existing):
    if existing and corpus.FENCE in existing:
        return existing[existing.index(corpus.FENCE):]
    return corpus.FENCE + "\n## My notes\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--scope", default="")
    ap.add_argument("--body", required=True, help="agent prose markdown (path or '-')")
    ap.add_argument("--generated", default=date.today().isoformat())
    ap.add_argument("--vault", default=None)
    args = ap.parse_args()

    vault = Path(args.vault).resolve() if args.vault else corpus.find_vault(Path.cwd())
    body = sys.stdin.read() if args.body == "-" else Path(args.body).read_text()

    path = vault / "areas" / f"{args.slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    prior = path.read_text() if path.exists() else None
    created = existing_created(prior, args.generated) if prior else args.generated

    fm = build_frontmatter(args.slug, args.title, args.scope, created, args.generated)
    ai_region = fm + "\n" + body.strip() + "\n\n" + TOPICS_BLOCK.rstrip() + "\n\n"
    path.write_text(ai_region + split_human(prior))
    print(f"wrote {path.relative_to(vault)}")


if __name__ == "__main__":
    main()
