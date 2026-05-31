#!/usr/bin/env python3
"""Write or refresh a topic note (topics/<slug>.md), preserving the human region (ADR-0014, ADR-0005).

Split of labor (like lit-sync's write_note.py): the *agent* writes the thematic prose — Scope,
Sub-themes, Cross-paper tensions, Open questions, Candidate ideas — and passes it as --body. This
script owns the deterministic parts: frontmatter, the stable slug identity, and the three derived
blocks that must not drift:

  ## Members            — dataview over lit-note `topics:` (single source of truth; live roster)
  ## Bordering work     — citation-derived: in-corpus papers cited by members but not members here
  ## Promoted from this topic — dataview over projects whose `topics:` link back here

`created` is fixed at birth; `title`/`scope`/body are refreshable in place. Renames are a separate
explicit op (move file + rewrite member links), never done here. Standard library only.

Usage (from vault root):
  write_topic.py --slug inequity-aversion --title "Inequity-averse models & their tests" \
    --scope "one-line scope" --members ck1,ck2,ck3 --body body.md [--generated YYYY-MM-DD]
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


MEMBERS_BLOCK = (
    "## Members\n"
    "```dataview\n"
    "LIST\n"
    'FROM "literature"\n'
    "WHERE contains(topics, this.file.link)\n"
    "SORT file.name ASC\n"
    "```\n"
)

PROMOTED_BLOCK = (
    "## Promoted from this topic\n"
    "```dataview\n"
    "LIST\n"
    'FROM "projects"\n'
    "WHERE contains(topics, this.file.link)\n"
    "```\n"
)


def bordering_block(slug, members, notes):
    notes_by_ck = {n["citekey"]: n for n in notes}
    rows = corpus.bordering_work(slug, {slug: set(members)}, notes_by_ck)
    lines = ["## Bordering work",
             "<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->"]
    if not rows:
        lines.append("_None — no member cites an in-corpus paper outside this topic._")
    else:
        for ck, n in rows[:20]:
            lines.append(f"- [[@{ck}]] — cited by {n} member{'s' if n > 1 else ''}")
    return "\n".join(lines) + "\n"


def build_frontmatter(slug, title, scope, area_raw, created, generated):
    rows = [
        ("slug", yaml_scalar(slug)),
        ("title", yaml_scalar(title)),
        ("type", "topic"),
        ("scope", yaml_scalar(scope)),
        ("area", area_raw or '""'),  # "[[area-slug]]" link, set by apply_areas.py; preserved on re-prose
        ("tags", "[topic]"),
        ("created", yaml_scalar(created)),
        ("generated", yaml_scalar(generated)),
    ]
    return "---\n" + "".join(f"{k}: {v}\n" for k, v in rows) + "---\n"


def existing_field(text, key, fallback=""):
    """Raw value of a frontmatter line in an existing note (verbatim, so an `area: "[[x]]"` link is
    preserved exactly when re-prosing)."""
    m = re.search(rf"^{key}:\s*(.*)$", text, flags=re.M)
    return (m.group(1).strip() if m else "") or fallback


def split_human(existing):
    if existing and corpus.FENCE in existing:
        return existing[existing.index(corpus.FENCE):]
    return corpus.FENCE + "\n## My notes\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--scope", default="")
    ap.add_argument("--members", default="", help="comma-separated member citekeys")
    ap.add_argument("--area", default="", help="parent area slug (else preserved from existing note)")
    ap.add_argument("--body", required=True, help="agent prose markdown (path or '-')")
    ap.add_argument("--generated", default=date.today().isoformat())
    ap.add_argument("--vault", default=None)
    args = ap.parse_args()

    vault = Path(args.vault).resolve() if args.vault else corpus.find_vault(Path.cwd())
    members = [c.strip() for c in args.members.split(",") if c.strip()]
    body = sys.stdin.read() if args.body == "-" else Path(args.body).read_text()
    notes = corpus.iter_notes(vault)

    path = vault / "topics" / f"{args.slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    prior = path.read_text() if path.exists() else None
    created = existing_field(prior, "created", args.generated) if prior else args.generated
    # area: from --area, else preserve the existing link (apply_areas.py is the usual setter)
    area_raw = f'"[[{args.area}]]"' if args.area else (existing_field(prior, "area") if prior else "")

    fm = build_frontmatter(args.slug, args.title, args.scope, area_raw, created, args.generated)
    derived = "\n".join([MEMBERS_BLOCK.rstrip(), "", bordering_block(args.slug, members, notes).rstrip(),
                         "", PROMOTED_BLOCK.rstrip()])
    ai_region = fm + "\n" + body.strip() + "\n\n" + derived + "\n\n"
    path.write_text(ai_region + split_human(prior))
    print(f"wrote {path.relative_to(vault)} ({len(members)} members)")


if __name__ == "__main__":
    main()
