#!/usr/bin/env python3
"""PreToolUse backstop hook (ADR-0015): block WebFetch of paper full-text.

The `biblio` client is the only sanctioned path to external literature and it fetches metadata only.
This hook is the belt-and-suspenders against a *rogue* agent calling WebFetch on a paper directly: it
denies WebFetch to PDF / known-publisher-full-text URLs, so the system can never pull paper full-text
off the web (open-access or not — full-text always enters via the user's Zotero). It is **scoped** —
ordinary non-paper fetches (docs, general web, abstract/landing pages, the open metadata APIs) pass.

Reads the PreToolUse JSON payload on stdin; emits a deny decision on a match, otherwise allows.
Standard library only (so it runs fast on every WebFetch, no uv needed).
"""
import json
import sys
import urllib.parse

# Hosts where paywalled/licensed full-text lives, plus shadow-library hosts.
PUBLISHER_HOSTS = {
    "sciencedirect.com", "link.springer.com", "springer.com", "onlinelibrary.wiley.com",
    "tandfonline.com", "jstor.org", "academic.oup.com", "journals.sagepub.com", "dl.acm.org",
    "ieeexplore.ieee.org", "nature.com", "science.org", "cambridge.org", "degruyter.com",
    "emerald.com", "muse.jhu.edu", "journals.uchicago.edu", "aeaweb.org",
    "sci-hub.se", "sci-hub.st", "sci-hub.ru", "libgen.is", "libgen.rs", "annas-archive.org",
}


def is_fulltext(url):
    try:
        u = urllib.parse.urlsplit(url)
    except Exception:
        return False
    host = (u.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = (u.path or "").lower()
    # The full-text artifact itself, on any host (covers arxiv.org/pdf/..., publisher PDFs, etc.).
    if path.endswith(".pdf") or path.endswith("/pdf") or "/pdf/" in path:
        return True
    # Known full-text / shadow-library hosts (suffix match so subdomains count).
    if any(host == h or host.endswith("." + h) for h in PUBLISHER_HOSTS):
        return True
    return False


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # malformed payload → never block
    if payload.get("tool_name") != "WebFetch":
        sys.exit(0)
    url = (payload.get("tool_input") or {}).get("url", "") or ""
    if is_fulltext(url):
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                f"Blocked WebFetch of probable paper full-text: {url}\n"
                "Per ADR-0015 the system never fetches paper full-text from the web (open-access or not). "
                "Use the biblio client (.claude/scripts/biblio.py) for metadata/abstracts, surface the DOI "
                "+ OA link on the acquire-list, and add full-text to Zotero yourself."),
        }}))
    sys.exit(0)


if __name__ == "__main__":
    main()
