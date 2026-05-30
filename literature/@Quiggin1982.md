---
citekey: Quiggin1982
title: A theory of anticipated utility
authors: ["Quiggin, John"]
year: 1982
type: journalArticle
doi: 10.1016/0167-2681(82)90008-7
zotero: "zotero://select/library/items/78DK35RB"
pdf: /Users/jesper/Zotero/storage/5X3NDXHJ/Quiggin1982.pdf
tags: [literature]
keywords: [rank-dependent-utility, anticipated-utility, expected-utility-generalization, decision-weights, probability-weighting, stochastic-dominance, non-expected-utility, allais-paradox]
topics: []
related: [Kahneman1979, Tversky1974, Tversky1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> A new theory of cardinal utility, with an associated set of axioms, is presented. It is a generalization of the von Neumann-Morgenstern expected utility theory, which permits the analysis of phenomena associated with the distortion of subjective probability.

## Summary
This is the founding paper of **rank-dependent expected utility** (here called "anticipated utility", AU). Quiggin generalizes von Neumann-Morgenstern (NM) expected utility by replacing the mathematical expectation with a weighted sum in which the **decision weight attached to an outcome depends on the entire probability distribution and on the outcome's rank**, not on its individual probability alone. The crucial innovation that distinguishes AU from earlier decision-weight schemes (Handa, Kahneman-Tversky's original prospect theory, Karmarkar) is that this rank-dependent transformation of the *cumulative* distribution **automatically preserves first-order stochastic dominance**, curing the dominance violations that plagued those models. The theory is axiomatized via a weakened independence axiom restricted to 50-50 bets, and is shown to extend cleanly to continuous distributions and to support partial stochastic-dominance and mean-variance results.

## Research question
Can one build an axiomatic cardinal utility theory that (i) accommodates the systematic, non-random violations of the NM independence axiom documented by Allais, MacCrimmon, Kahneman-Tversky, etc., while (ii) retaining transitivity and dominance, the properties that even violators of independence assent to and that the rest of economic theory relies on? Earlier "decision weight" theories (Handa 1977, Karmarkar 1978/79, original prospect theory) fail because weighting individual probabilities $w(p_i)$ generates dominance violations.

## Method / identification
The object is a **utility functional** $V$ on the set $Y$ of prospects $y=\{(x_1,\dots,x_n);(p_1,\dots,p_n)\}$, representing a complete, transitive preference $P$. Outcomes are first **ordered worst-to-best**, $x_n P x_{n-1} P \cdots P x_1$. AU is defined as
$$V = h(p)\cdot U(x) = \sum_i h_i(p)\,U(x_i),$$
where $U$ is an NM-like cardinal utility and $h_i(p)$ is a **rank-dependent decision weight** that depends on the whole vector $p$ (not just $p_i$), with $\sum_i h_i(p)=1$, $h(1)=1$, and the normalization $h(\tfrac12,\tfrac12)=(\tfrac12,\tfrac12)$ (50-50 bets are undistorted).

The key structural result is that $h$ is fully pinned down by a single **probability transformation** $f:[0,1]\to[0,1]$ acting on the cumulative probability. Writing $f(p)=h_1(p,1-p)$, an induction (eqs. 7-10) yields
$$h_i(p)=f\!\Big(\sum_{j=1}^{i} p_j\Big)-f\!\Big(\sum_{j=1}^{i-1} p_j\Big),$$
so the weight on an outcome is the $f$-transformed increment of the cumulative distribution at that outcome's rank. For continuous distributions with objective CDF $D$, one defines a transformed "decision CDF" $G(x_0)=f(D(x_0))$ with density $g$, giving
$$V=\int U(x)\,g(x)\,dx=\int U(x)\,dG(x).$$

**Axioms.** Axiom 1 (completeness: $P$ complete, reflexive, transitive). Axiom 2 (dominance, on outcomes). Axiom 3 (continuity, on outcomes). Axiom 4 (**weak independence**): if every component of two prospects, paired and reduced to certainty equivalents of 50-50 bets, is matched, the resulting 50-50 combinations are indifferent — this restricts the controversial independence axiom to fifty-fifty gambles, where empirically distortion is minimal. Two richness conditions (R.1, R.2) on $X$ and $Y$ guarantee enough prospects for uniqueness. The proof (in the appendix) constructs $U$ on a binary-rational dense subset via 50-50 certainty equivalents, then extends to all $Y$ by induction.

## Data
None — this is a pure axiomatic / decision-theoretic contribution. It is motivated by, and reinterprets, prior experimental evidence (Allais 1953, MacCrimmon 1968, [[@Tversky1974|Slovic-Tversky 1974]], [[@Kahneman1979|Kahneman-Tversky 1979]], Kunreuther et al. 1978 on under/over-insurance), but contains no new data or estimation.

## Key findings
- **Proposition 1 (representation & uniqueness):** Under R.1, R.2 and Axioms 1-4 there exists $V:Y\to\mathbb{R}$ with $V(y)\ge V(y')\iff yPy'$ and $V(x;p)=\sum_i h_i(p)U(x_i)$, with $h(1)=1$, $h(\tfrac12,\tfrac12)=(\tfrac12,\tfrac12)$; $U$ is unique up to a positive affine transformation $V'=aV+b$, $a>0$. This is the headline rank-dependent representation theorem.
- **Dominance preservation (eq. 5):** Any decision-weight scheme depending only on individual $p_i$ must collapse to $w(p_i)/\sum_j w(p_j)=p_i$ — i.e. to NM — to avoid dominance violations; AU escapes this trap precisely by using the rank/cumulative transformation $f$.
- **Conditions on $f$ (Section 4):** overweighting of extreme events corresponds to $f(p)\ge p$ for $p\le\tfrac12$ and $f(p)\le p$ for $p\ge\tfrac12$ (condition A); the converse is underweighting (B). Single inflexion is guaranteed by $f$ concave on $[0,\tfrac12]$ and convex on $[\tfrac12,1]$ (A*). **Optimism vs. pessimism** is captured by $f(p)$ vs. $1-f(1-p)$; a symmetric $f$ is "neutral". Overweighting extreme events explains both the Friedman-Savage/Allais paradoxes and the "editing"/ignoring of tiny probabilities (reinterpreted as a fixed cost-of-calculation), without requiring $f$ to be discontinuous.
- **Proposition 3 (FSD):** $y_1$ FSD $y_0$ iff $V(y_1)\ge V(y_0)$ for *all* AU functions $V$ — AU fully respects first-order stochastic dominance.
- **Proposition 4 (SSD, partial):** SSD cannot be fully extended (and shouldn't be — over-insurance is the point), but for $y_0,y_1$ with equal medians and symmetric distributions intersecting finitely often, $y_1$ SSD $y_0$ iff $V(y_1)\ge V(y_0)$ for every $V$ built from concave $U$ and symmetric $f$ satisfying A*. A corollary: **mean-variance analysis remains valid** for normally distributed variables, and the symmetry condition can be relaxed to right-skewness (eq. 34).

## Contribution
Quiggin founds **rank-dependent expected utility**, one of the most influential non-expected-utility models in economics. The decisive conceptual move — distorting the *cumulative* probability via $f$ and assigning rank-dependent weights rather than transforming individual probabilities — is what makes a decision-weight theory simultaneously *descriptively flexible* (it accommodates Allais, over-insurance, gambling, overweighted catastrophes) and *normatively disciplined* (transitive, dominance-respecting). This directly fixed the fatal flaw of original prospect theory and Handa's/Karmarkar's models, and seeded cumulative prospect theory ([[@Tversky1992|Tversky-Kahneman 1992]]) and the entire rank-dependent literature.

## Limitations & open questions
- The author flags that adopting a more general theory **makes useful predictions harder to obtain**; "further work is needed in developing conditions under which other results [beyond dominance] can be extended" to AU.
- **SSD has no full analogue** under AU (Proposition 2(ii) does not extend); only partial extensions (equal-median symmetric, or right-skewed) are obtained. Characterizing the broadest class of distributions/$V$ for which second-order results hold is left open.
- The "editing"/ignoring of extremely small probabilities is given an informal cost-of-calculation reinterpretation rather than an axiomatic treatment.
- Quiggin notes AU is "one of a number of possibilities considered (but not developed or axiomatized) by Allais (1952)"; more general transformations (relaxing transitivity/dominance) are mentioned but deliberately not pursued.
- Suggested application domains explicitly named as open: the apparent propensity to **over-insure**, the **economic analysis of gambling**, and decisions involving **catastrophic or extremely favourable low-probability outcomes**.

## Connections
Generalizes **von Neumann-Morgenstern (1944)** expected utility, weakening its independence axiom (the version directly contradicted by **Allais 1953**). It is explicitly positioned against the earlier individual-probability decision-weight theories of **Handa (1977)** (shown by Fishburn 1978 to reduce to expected-return maximization and to violate dominance), **Karmarkar (1978, 1979)** subjectively weighted utility, and **[[@Kahneman1979|Kahneman-Tversky (1979)]]** original prospect theory (whose "editing" of dominated prospects produces intransitivity). The stochastic-dominance machinery builds on **Hadar-Russell (1969)** and **Fishburn (1964)**, with technical corrections from **Tesfatsion (1976)**. Empirical motivation draws on **MacCrimmon (1968)**, **[[@Tversky1974|Slovic-Tversky (1974)]]**, and **Kunreuther et al. (1978)**. Forward in time, this paper is the direct ancestor of cumulative prospect theory and rank-dependent utility as standard tools in choice modeling under risk.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
