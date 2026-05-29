#!/usr/bin/env python3
"""Minimal BetterBibTeX JSON-RPC client for lit-sync.

Endpoints used (verified against the running BBT, 2026-05-29):
  item.citationkey(["<key>" | "<lib>:<key>", ...]) -> {passed_key: citekey}
  item.attachments("<citekey>")                     -> [{path, open, annotations:[...]}]
  item.search("<terms>")                            -> [CSL-JSON items incl. citekey, abstract]

Requires Zotero to be running (BBT serves on 127.0.0.1:23119).
Standard library only.
"""
import argparse
import json
import sys
import urllib.request

ENDPOINT = "http://127.0.0.1:23119/better-bibtex/json-rpc"


def rpc(method, params, endpoint=ENDPOINT, timeout=60):
    payload = json.dumps({"jsonrpc": "2.0", "method": method, "params": params, "id": 1}).encode()
    req = urllib.request.Request(
        endpoint, data=payload, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.load(r)
    except urllib.error.URLError as e:
        raise SystemExit(
            f"Could not reach BetterBibTeX at {endpoint} ({e}). Is Zotero running?"
        )
    if "error" in data and data["error"] is not None:
        raise RuntimeError(f"BBT {method} error: {data['error']}")
    return data["result"]


def citationkeys(item_keys, endpoint=ENDPOINT):
    """Map Zotero item keys -> BBT citekeys. Accepts ['KEY'] or ['LIB:KEY']. Batched."""
    keys = list(item_keys)
    if not keys:
        return {}
    return rpc("item.citationkey", [keys], endpoint)


def attachments(citekey, endpoint=ENDPOINT):
    """Return attachments for a citekey: [{path, open, annotations:[{annotationText,...}]}]."""
    return rpc("item.attachments", [citekey], endpoint)


def search(terms, endpoint=ENDPOINT):
    return rpc("item.search", [terms], endpoint)


def main():
    ap = argparse.ArgumentParser(description="BetterBibTeX JSON-RPC client")
    ap.add_argument("--endpoint", default=ENDPOINT)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("citationkey", help="map Zotero item keys -> citekeys")
    c.add_argument("keys", nargs="+")
    a = sub.add_parser("attachments", help="list attachments (path + highlights) for a citekey")
    a.add_argument("citekey")
    s = sub.add_parser("search", help="full-text-ish item search -> CSL-JSON")
    s.add_argument("terms")
    args = ap.parse_args()

    if args.cmd == "citationkey":
        out = citationkeys(args.keys, args.endpoint)
    elif args.cmd == "attachments":
        out = attachments(args.citekey, args.endpoint)
    elif args.cmd == "search":
        out = search(args.terms, args.endpoint)
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
