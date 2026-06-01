#!/usr/bin/env python3
"""score_ideas — deterministic project-potential scoring (ADR-0016).

The vetting agents emit only *inputs* — per-idea admissibility verdicts and four 1–5 dimension scores,
each with evidence. This script does the *calculation*, so "how potential is computed" is a documented,
re-runnable formula rather than an agent's gut:

  Potential = 𝟙{admissible} · ( w_S·Significance + w_N·Novelty + w_F·Feasibility + w_Fit·Fit )

  - Admissibility (gate): an idea is kept only if BOTH `sound_grounded` AND `not_already_done` pass.
    Failures are reported separately (never silently dropped), not scored.
  - Reward (Significance, Novelty) and cost/ease (Feasibility) COMPENSATE additively — a low-effort
    "low-hanging fruit" and a high-reward "moonshot" both score high; only expensive-and-unimportant
    scores low. Fit is a modest additive tilt (default weight 0.5), never a gate.
  - Evidence cap (anti-inflation): a dimension may NOT exceed 3 without its evidence present — enforced
    here, deterministically.
  - Score is normalized to 0–100 (raw / (Σweights · 5) · 100) and admissibles are ranked.

Re-run with different --weights to re-rank WITHOUT re-vetting. Standard library only; run via `uv run`.

Input `--vetted FILE`: JSON list (or {"ideas":[...]}) of vetted ideas; tolerant of nesting, e.g.
  {"id":1,"title":"...","admissible":{"sound_grounded":true,"not_already_done":true},
   "scores":{"significance":2,"novelty":2,"feasibility":5,"fit":4},
   "evidence":{"significance":"…","novelty":"…","feasibility":"…","fit":"…"}}

Usage:
  uv run python .claude/scripts/score_ideas.py --vetted vetting.json [--weights 1,1,1,0.5] [--format md|json]
"""
import argparse
import json
from pathlib import Path

DIMS = ["significance", "novelty", "feasibility", "fit"]
GATES = ["sound_grounded", "not_already_done"]


def _scores(idea):
    s = idea.get("scores") or {k: idea.get(k) for k in DIMS}
    return {d: s.get(d) for d in DIMS}


def _evidence(idea):
    e = idea.get("evidence") or {}
    return {d: (e.get(d) if isinstance(e, dict) else None) or idea.get(d + "_evidence") for d in DIMS}


def _admissibility(idea):
    a = idea.get("admissible") or idea.get("admissibility") or {}
    return {g: bool(a.get(g)) for g in GATES}


def _has(ev):
    return bool(ev) and (str(ev).strip() if not isinstance(ev, (list, dict)) else len(ev)) not in ("", 0)


def effective(idea):
    """Per-dimension effective scores with the evidence cap applied. Returns (scores, capped_flags)."""
    raw, ev = _scores(idea), _evidence(idea)
    out, capped = {}, []
    for d in DIMS:
        try:
            v = int(raw[d])
        except (TypeError, ValueError):
            v = 1
        v = max(1, min(5, v))
        if v > 3 and not _has(ev.get(d)):
            v, _ = 3, capped.append(d)   # cap, record
        out[d] = v
    return out, capped


def potential(scores, w):
    raw = sum(w[d] * scores[d] for d in DIMS)
    return round(raw / (sum(w.values()) * 5) * 100)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vetted", required=True)
    ap.add_argument("--weights", default="1,1,1,0.5", help="S,N,F,Fit (default 1,1,1,0.5 — Fit modest)")
    ap.add_argument("--format", choices=["json", "md"], default="json")
    args = ap.parse_args()

    parts = [float(x) for x in args.weights.split(",")]
    w = dict(zip(DIMS, parts))
    data = json.loads(Path(args.vetted).read_text())
    ideas = data.get("ideas", data) if isinstance(data, dict) else data

    admissible, inadmissible = [], []
    for idea in ideas:
        adm = _admissibility(idea)
        failed = [g for g in GATES if not adm[g]]
        base = {"id": idea.get("id"), "title": idea.get("title", "(untitled)")}
        if failed:
            inadmissible.append({**base, "failed_gates": failed})
            continue
        scores, capped = effective(idea)
        admissible.append({**base, "potential": potential(scores, w), "scores": scores,
                           "capped": capped, "source_topics": idea.get("source_topics", []),
                           "pitch": idea.get("refined_pitch") or idea.get("pitch", "")})
    admissible.sort(key=lambda r: r["potential"], reverse=True)

    if args.format == "json":
        print(json.dumps({"weights": w, "admissible": admissible, "inadmissible": inadmissible},
                         ensure_ascii=False, indent=2))
        return
    print(f"## Potential — {len(admissible)} admissible, {len(inadmissible)} dropped "
          f"(weights S,N,F,Fit = {args.weights})\n")
    print("| # | Potential | S | N | F | Fit | Title |")
    print("|---|---|---|---|---|---|---|")
    for r in admissible:
        s = r["scores"]
        cap = "*" if r["capped"] else ""
        print(f"| {r['id']} | **{r['potential']}** | {s['significance']} | {s['novelty']} | "
              f"{s['feasibility']} | {s['fit']} | {r['title']}{(' '+cap) if cap else ''} |")
    if any(r["capped"] for r in admissible):
        print("\n_\\* = a dimension was capped at 3 for missing evidence._")
    if inadmissible:
        print("\n### Dropped (inadmissible)")
        for r in inadmissible:
            print(f"- **{r['title']}** — failed: {', '.join(r['failed_gates'])}")


if __name__ == "__main__":
    main()
