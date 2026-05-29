#!/usr/bin/env python3
"""Extract and section-segment a PDF for the lit-sync map-reduce reader.

Runs `pdftotext` and splits the text on detected section headings so the skill can summarize
each section (the "map" step) and verify coverage. If extraction yields too little text
(scanned/image PDF), sets needs_visual=True and the skill falls back to Claude's visual `Read`.

Output (JSON to stdout): {path, pages, n_chars, needs_visual, truncated, n_sections,
sections:[{heading, char_len, text?}]}. Section text is included unless --headings.

Standard library only; uses `pdftotext`/`pdfinfo` (poppler) if present.
"""
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path

# Headings common in economics / ML / general academic papers. Matched on short lines,
# optionally numbered ("3", "3.", "3.1 Results").
SECTION_RE = re.compile(
    r"^\s*(\d+(\.\d+)*\.?\s+)?"
    r"(abstract|introduction|background|related work|literature review|motivation|"
    r"model|theory|theoretical framework|setup|set-up|methods?|methodology|"
    r"materials and methods|empirical strategy|identification|estimation|data|"
    r"experimental design|experiment|results|findings|analysis|discussion|"
    r"robustness|robustness checks|limitations|conclusions?|concluding remarks|"
    r"references|bibliography|appendix|supplementary)\b.*$",
    re.I,
)


def pdfinfo_pages(path):
    if not shutil.which("pdfinfo"):
        return None
    try:
        out = subprocess.run(["pdfinfo", path], capture_output=True, text=True, timeout=30).stdout
        m = re.search(r"^Pages:\s+(\d+)", out, re.M)
        return int(m.group(1)) if m else None
    except Exception:
        return None


def extract_text(path):
    if not shutil.which("pdftotext"):
        return ""
    try:
        r = subprocess.run(["pdftotext", "-q", path, "-"], capture_output=True, text=True, timeout=180)
        return r.stdout or ""
    except Exception:
        return ""


def segment(text):
    sections, cur = [], {"heading": "(front matter)", "lines": []}
    for ln in text.splitlines():
        h = ln.strip()
        # A real heading is short (or ALL-CAPS), not a sentence that merely starts with a
        # section keyword (e.g. "data. A Luce-like model that ...").
        is_heading = bool(SECTION_RE.match(ln)) and (len(h) <= 50 or (h.isupper() and len(h) <= 72))
        if is_heading:
            sections.append(cur)
            cur = {"heading": h, "lines": [ln]}
        else:
            cur["lines"].append(ln)
    sections.append(cur)
    out = []
    for s in sections:
        body = "\n".join(s["lines"]).strip()
        if body:
            out.append({"heading": s["heading"], "char_len": len(body), "text": body})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--max-chars", type=int, default=140000,
                    help="truncate total text beyond this (very long docs / books)")
    ap.add_argument("--headings", action="store_true", help="omit section text (overview only)")
    args = ap.parse_args()

    p = args.path
    if not Path(p).exists():
        print(json.dumps({"error": "not found", "path": p}))
        return

    pages = pdfinfo_pages(p)
    text = extract_text(p)
    n = len(text)
    truncated = n > args.max_chars
    if truncated:
        text = text[: args.max_chars]
    # Heuristic: scanned/image PDF if almost no text, or far less than expected for the page count.
    expected = (pages or 1) * 200
    needs_visual = n < 500 or n < 0.25 * expected

    sections = segment(text) if text else []
    result = {
        "path": p,
        "pages": pages,
        "n_chars": n,
        "needs_visual": needs_visual,
        "truncated": truncated,
        "n_sections": len(sections),
        "sections": [
            {"heading": s["heading"], "char_len": s["char_len"]}
            if args.headings else s
            for s in sections
        ],
    }
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
