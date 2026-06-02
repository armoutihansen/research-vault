#!/usr/bin/env python3
"""Enumerate in-scope Zotero items and diff them against the lit-sync manifest.

Scope (ADR-0003) = items with a PDF attachment  OR  items tagged `to-note`.
Pipeline (ADR-0006): read zotero.sqlite (a copy, read-only) for the item list + metadata;
resolve BBT citekeys via item.citationkey. Emit a JSON work-list of items whose note must be
created (new) or refreshed (changed); skip unchanged ones.

Change detection: a content hash per citekey over title/abstract/authors/year/doi + PDF
path/size/mtime, compared against `.research/manifest.json`.

Usage (run from the vault root):
  enumerate.py [--vault DIR] [--zotero-dir ~/Zotero] [--tag to-note]
               [--status new,changed] [--limit N] [--out FILE] [--no-bbt]

Standard library only. Requires Zotero running (for citekeys) unless --no-bbt.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sqlite3
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bbt  # noqa: E402

YEAR_RE = re.compile(r"(\d{4})")


def find_vault(start):
    p = Path(start).resolve()
    for cand in [p, *p.parents]:
        if (cand / ".research").exists() or (cand / "CONTEXT.md").exists():
            return cand
    return p


def snapshot_db(zotero_dir):
    """Copy zotero.sqlite (+ -wal/-shm) to a temp dir for a safe, lock-free read."""
    src = Path(zotero_dir).expanduser() / "zotero.sqlite"
    if not src.exists():
        raise SystemExit(f"zotero.sqlite not found at {src} (use --zotero-dir)")
    tmp = Path(tempfile.mkdtemp(prefix="litsync-"))
    dst = tmp / "zotero.sqlite"
    shutil.copy2(src, dst)
    for suff in ("-wal", "-shm"):
        w = Path(str(src) + suff)
        if w.exists():
            shutil.copy2(w, Path(str(dst) + suff))
    return tmp, dst


def query_scope(con, tag):
    cur = con.execute(
        """
        SELECT i.itemID, i.libraryID, i.key, it.typeName
        FROM items i
        JOIN itemTypes it ON it.itemTypeID = i.itemTypeID
        WHERE it.typeName NOT IN ('attachment','note','annotation')
          AND i.itemID NOT IN (SELECT itemID FROM deletedItems)
          AND (
            i.itemID IN (
              SELECT parentItemID FROM itemAttachments
              WHERE contentType='application/pdf' AND parentItemID IS NOT NULL
            )
            OR i.itemID IN (
              SELECT itx.itemID FROM itemTags itx
              JOIN tags t ON t.tagID = itx.tagID WHERE t.name = ?
            )
          )
        ORDER BY i.itemID
        """,
        (tag,),
    )
    return cur.fetchall()


def fields_for(con, item_id):
    out = {}
    for name, value in con.execute(
        """
        SELECT f.fieldName, idv.value
        FROM itemData id
        JOIN fields f ON f.fieldID = id.fieldID
        JOIN itemDataValues idv ON idv.valueID = id.valueID
        WHERE id.itemID = ?
        """,
        (item_id,),
    ):
        out[name] = value
    return out


def authors_for(con, item_id):
    rows = con.execute(
        """
        SELECT c.lastName, c.firstName, c.fieldMode, ct.creatorType
        FROM itemCreators ic
        JOIN creators c ON c.creatorID = ic.creatorID
        JOIN creatorTypes ct ON ct.creatorTypeID = ic.creatorTypeID
        WHERE ic.itemID = ?
        ORDER BY ic.orderIndex
        """,
        (item_id,),
    ).fetchall()
    authors = []
    for last, first, field_mode, ctype in rows:
        if ctype not in ("author", "editor", None):
            continue
        if field_mode == 1 or not first:  # institutional / single-field name
            authors.append(last or "")
        else:
            authors.append(f"{last}, {first}")
    return [a for a in authors if a]


def pdfs_for(con, item_id, zotero_dir):
    rows = con.execute(
        """
        SELECT att.key, ia.path, ia.linkMode
        FROM itemAttachments ia
        JOIN items att ON att.itemID = ia.itemID
        WHERE ia.parentItemID = ? AND ia.contentType = 'application/pdf'
              AND att.itemID NOT IN (SELECT itemID FROM deletedItems)
        """,
        (item_id,),
    ).fetchall()
    resolved = []
    for att_key, path, _mode in rows:
        ap = resolve_pdf(zotero_dir, att_key, path)
        if ap:
            resolved.append(ap)
    # prefer an existing file
    resolved.sort(key=lambda p: (not os.path.exists(p), p))
    return resolved


def resolve_pdf(zotero_dir, att_key, path):
    if not path:
        return None
    if path.startswith("storage:"):
        fname = path[len("storage:"):]
        return str(Path(zotero_dir).expanduser() / "storage" / att_key / fname)
    if path.startswith("attachments:"):
        return None  # linked base-dir; resolve via BBT item.attachments if needed
    return path  # absolute linked file


def year_of(fields):
    d = fields.get("date", "")
    m = YEAR_RE.search(d or "")
    return m.group(1) if m else ""


def content_hash(meta):
    h = hashlib.sha256()
    parts = [
        meta.get("title", ""),
        meta.get("abstract", ""),
        "; ".join(meta.get("authors", [])),
        str(meta.get("year", "")),
        meta.get("doi", ""),
    ]
    pdf = meta.get("pdf_path")
    if pdf and os.path.exists(pdf):
        st = os.stat(pdf)
        parts += [pdf, str(st.st_size), str(int(st.st_mtime))]
    h.update("|".join(p or "" for p in parts).encode("utf-8", "replace"))
    return h.hexdigest()[:16]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--zotero-dir", default="~/Zotero")
    ap.add_argument("--tag", default="to-note", help="opt-in tag for PDF-less items")
    ap.add_argument("--status", default="new,changed",
                    help="comma list of statuses to emit: new,changed,unchanged")
    ap.add_argument("--limit", type=int, default=0, help="cap emitted items (0 = all); for the pilot")
    ap.add_argument("--out", default=None, help="write JSON work-list here (default stdout)")
    ap.add_argument("--no-bbt", action="store_true", help="skip citekey resolution (debug)")
    args = ap.parse_args()

    vault = Path(args.vault).resolve() if args.vault else find_vault(os.getcwd())
    manifest_path = vault / ".research" / "manifest.json"
    manifest = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
    want = {s.strip() for s in args.status.split(",") if s.strip()}

    tmp, dbpath = snapshot_db(args.zotero_dir)
    try:
        con = sqlite3.connect(f"file:{dbpath}?mode=ro", uri=True)
        scope = query_scope(con, args.tag)
        items = []
        keymap_in = []  # "LIB:KEY"
        for item_id, library_id, key, type_name in scope:
            fields = fields_for(con, item_id)
            pdfs = pdfs_for(con, item_id, args.zotero_dir)
            pdf_path = pdfs[0] if pdfs else None
            meta = {
                "item_key": key,
                "library_id": library_id,
                "type": type_name,
                "title": fields.get("title", "").strip(),
                "authors": authors_for(con, item_id),
                "year": year_of(fields),
                "doi": fields.get("DOI", ""),
                "abstract": fields.get("abstractNote", ""),
                "pdf_path": pdf_path,
                "pdf_exists": bool(pdf_path and os.path.exists(pdf_path)),
            }
            items.append(meta)
            keymap_in.append(f"{library_id}:{key}")
        con.close()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # Resolve citekeys via BBT (batched).
    citekeys = {}
    if not args.no_bbt:
        citekeys = bbt.citationkeys(keymap_in)

    worklist = []
    counts = {"new": 0, "changed": 0, "unchanged": 0, "no_citekey": 0}
    for meta, k in zip(items, keymap_in):
        ck = citekeys.get(k) or citekeys.get(meta["item_key"]) if not args.no_bbt else None
        if not args.no_bbt and not ck:
            counts["no_citekey"] += 1
            continue
        meta["citekey"] = ck or meta["item_key"]
        h = content_hash(meta)
        meta["hash"] = h
        prev = manifest.get(meta["citekey"])
        if prev is None:
            status = "new"
        elif prev.get("hash") != h:
            status = "changed"
        else:
            status = "unchanged"
        counts[status] += 1
        meta["status"] = status
        if status in want:
            worklist.append(meta)

    if args.limit and len(worklist) > args.limit:
        worklist = worklist[: args.limit]

    payload = {"counts": counts, "emitted": len(worklist), "items": worklist}
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_text(text)
        print(f"scope={sum(counts.values())} {counts} → emitted {len(worklist)} to {args.out}",
              file=sys.stderr)
    else:
        print(text)
    print(f"[enumerate] {counts}, emitted {len(worklist)}", file=sys.stderr)


if __name__ == "__main__":
    main()
