---
slug: revealed-preference-foundations
title: "Revealed-Preference & Rationalizability Foundations"
type: topic
scope: "Classical axiomatic theory of choice functions, WARP/SARP, congruence, and the empirical content of utility analysis."
area: "[[bounded-rationality-choice]]"
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This topic holds the classical axiomatic bedrock of choice theory: when does observed behavior reveal an underlying preference, what consistency conditions ($WARP$, $SARP$, congruence, Properties $\alpha/\beta/\gamma/\delta$) are equivalent, and how much empirical content does utility maximization carry? It runs from Samuelson's operational reconstruction of demand through Sen's deconstruction of "internal consistency," and out to two frontier moves: weakening $WARP$ to admit endogenous reference points, and making *preference itself* socially endogenous. The boundary: members supply the axioms and identification logic *against which* the bounded-rationality, menu-dependence, and social-preference topics are tested — they set the rules, the other topics break them.

## Sub-themes

- **Operational content of utility analysis.** [[@Samuelson1938|Samuelson (1938)]] alone: deriving refutable Slutsky symmetry/negativity restrictions on price–quantity data from a single stability postulate, with the law of demand and aggregate-income aggregation flagged as non-implications.
- **The axiomatic hierarchy and its collapse.** [[@Sen1971|Sen (1971)]] proves $WARP$, $SARP$, congruence, and normality coincide on the full finite domain and factorizes rationality into $\alpha+\beta$ (full), $\alpha+\gamma$ (normality), $\delta$ (quasi-transitivity); [[@Sen1977|Sen (1977)]] ports this to social choice, isolating contraction-consistency as the impossibility engine.
- **The critique of consistency itself.** [[@Sen1993|Sen (1993)]] argues "internal consistency" is undecidable without an external reference (objectives, norms, menu-dependent rationales), re-deriving Arrow with no imposed consistency axiom.
- **Empirical fragility of the foundations.** [[@Grether1979|Grether and Plott (1979)]] shows procedure invariance — that choice and valuation must agree — fails systematically under incentivized lab conditions (preference reversals as transitivity violations).
- **Endogenous references inside revealed preference.** [[@Ok2015|Ok, Ortoleva, and Riella (2015)]] weakens $WARP$ into four axioms so that reference points and subjective attributes are *inferred from* choice rather than labeled, rationalizing the attraction effect.
- **Endogenous, socially-determined preference.** [[@Cuhadaroglu2017|Cuhadaroglu (2017)]] and [[@Fershtman2018|Fershtman and Segal (2018)]] both let others' choices reshape what is maximized — Cuhadaroglu via two-stage influence on incomplete preferences, Fershtman–Segal via core-vs-behavioral utilities in fixed-point equilibrium.

## Cross-paper tensions

The sharpest fault line is **whether "consistency" is a discoverable property of behavior or a category error.** [[@Samuelson1938|Samuelson (1938)]] founds the whole program on "explaining behavior without reference to anything other than behavior," and [[@Sen1971|Sen (1971)]] hands it a clean internal hierarchy. [[@Sen1993|Sen (1993)]] then turns directly on Samuelson: acts of choice, unlike statements, *cannot contradict each other*, so picking $x$ from $\{x,y\}$ and $y$ from $\{x,y,z\}$ — a flat $WARP$ violation for Sen-1971 — is fully rational once a menu-dependent rationale (positional, epistemic, freedom-to-reject) is admitted. The same author thus supplies both the consistency apparatus and its dissolution.

A second tension is **how to absorb $WARP$ violations.** [[@Sen1993|Sen (1993)]] makes them *external/interpretive* — the analyst must import objectives. [[@Ok2015|Ok et al. (2015)]] make them *internal and structural*: an explicit weakening of $WARP$ that endogenizes a reference $r(S)$ and an attribute set $\mathcal{U}$, keeping testable discipline (their reference is feasible-but-unchosen, deliberately unlike Köszegi–Rabin's belief-based reference). [[@Grether1979|Grether and Plott (1979)]] threaten both: reversals are not menu effects but a clash between choice-revealed and valuation-revealed preference under *procedure* variation, an axis neither the $\alpha/\beta/\gamma$ machinery nor the single-menu reference model addresses. Their surviving explanation (response-mode/easy-justification) leaves "no apparent route to repair the theory."

Third, **what is the carrier of preference — fixed and individual, or endogenous and social?** [[@Cuhadaroglu2017|Cuhadaroglu (2017)]] and [[@Fershtman2018|Fershtman and Segal (2018)]] both socialize preference but disagree at the root. Cuhadaroglu keeps a single latent (incomplete, transitive) preference and lets influence operate as a *second-stage tie-breaker* (Max of Max), recovering influence by revealed preference. Fershtman–Segal posit *two* preference relations and let influence transform the maximand itself via a social influence function $v_i=h^i_{\bar v_{-i}}\circ u_i$, solved as a Schauder–Tychonoff fixed point. The first is identification-driven and falsifiable on choice data; the second is existence/structure-driven and (by its own admission) has no observable footprint absent the core utilities. Cuhadaroglu even concedes her own identification is *permissive*: independent rational shortlisting can mimic mutual influence — the reflection problem ([[@Sen1977|Sen (1977)]]'s aggregation worry resurfacing as Manski's).

## Open questions

- **Intermediate domains.** [[@Sen1971|Sen (1971)]]'s collapse of $WARP/SARP$ holds only on the *full* finite domain; whether the equivalences degrade gracefully on domains richer than budget sets but poorer than all finite subsets is left open — directly relevant since real data live on sparse domains ([[@Samuelson1938|Samuelson (1938)]]).
- **Aggregation.** [[@Samuelson1938|Samuelson (1938)]] explicitly defers market-demand restrictions on *total* income (the SMD kernel); [[@Sen1977|Sen (1977)]] leaves the $JD$ verdict turning on "how much contraction-consistency we demand."
- **Repairing theory after reversals.** [[@Grether1979|Grether and Plott (1979)]] issue the standing challenge: modify choice theory to accommodate procedure-dependence *without rendering it vacuous*.
- **Graded vs. all-or-nothing references.** [[@Ok2015|Ok et al. (2015)]] model "being a reference" as binary and leave graded references and the non-unique reference *map* (vs. correspondence) open.
- **Disentangling influence from homophily/independent rationality.** Both [[@Cuhadaroglu2017|Cuhadaroglu (2017)]] and [[@Fershtman2018|Fershtman and Segal (2018)]] leave network structure, partial observability (beliefs), and dynamics as flagged extensions, and neither separates influence from sorting on choice data alone.

## Candidate ideas

- **An experimental test of Ok–Ortoleva–Riella's RCon.** [[@Ok2015|Ok et al. (2015)]] note their finite three-set-cover restatement is "easy to test"; design an incentivized attraction-effect experiment that directly checks RCon and recovers the subjective attribute set $\mathcal{U}$, benchmarking against [[@Grether1979|Grether and Plott (1979)]]-style procedure controls.
- **Are preference reversals a reference effect?** Formally ask whether [[@Grether1979|Grether and Plott (1979)]] reversals fit the endogenous-reference representation of [[@Ok2015|Ok et al. (2015)]], or whether procedure-variance is a genuinely orthogonal violation axis — a falsifiable nesting test.
- **Identifying influence vs. independent shortlisting.** Build an experiment (or estimator) that separates [[@Cuhadaroglu2017|Cuhadaroglu (2017)]]'s mutual-influence CMI from two agents independently running rational shortlist methods, resolving the permissiveness she concedes.
- **Observable footprint of behavioral preferences.** Derive the comparative statics ([[@Fershtman2018|Fershtman and Segal (2018)]] Claims 6–8: no divergence, comonotonicity) into refutable predictions on group risk-taking data, turning a pure existence result into a [[@Samuelson1938|Samuelson (1938)]]-style empirical-content claim.
- **Contraction-consistency on sparse domains.** Using [[@Sen1977|Sen (1977)]]'s diagnosis that $\alpha$ drives impossibility, study which Afriat-style nonparametric tests of [[@Sen1971|Sen (1971)]]'s equivalences retain power on the limited domains [[@Samuelson1938|Samuelson (1938)]] worried about.
- **Menu-dependent rationales as estimable structure.** Operationalize [[@Sen1993|Sen (1993)]]'s positional/epistemic/freedom rationales as competing external references and test which best fits attraction- and reversal-type data, bridging his critique to [[@Ok2015|Ok et al. (2015)]]'s constructive model.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Manzini2007]] — cited by 2 members
- [[@Masatlioglu2012]] — cited by 2 members
- [[@Apesteguia2013]] — cited by 1 member
- [[@Ariely2000]] — cited by 1 member
- [[@Au2011]] — cited by 1 member
- [[@Chen2009]] — cited by 1 member
- [[@Cherepanov2013]] — cited by 1 member
- [[@Fehr1999]] — cited by 1 member
- [[@Horan2016]] — cited by 1 member
- [[@Huber1982]] — cited by 1 member
- [[@Kamenica2008]] — cited by 1 member
- [[@Koszegi2006b]] — cited by 1 member
- [[@Lombardi2009]] — cited by 1 member
- [[@Mas2009]] — cited by 1 member
- [[@Rubinstein2006]] — cited by 1 member
- [[@Salant2008]] — cited by 1 member
- [[@Simonson1992]] — cited by 1 member
- [[@Tversky1972]] — cited by 1 member
- [[@Zimmerman2003]] — cited by 1 member
- [[@deClippel2012]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
