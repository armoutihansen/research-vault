---
citekey: Shalev2000
title: Loss aversion equilibrium
authors: ["Shalev, Jonathan"]
year: 2000
type: journalArticle
doi: 10.1007/s001820000038
zotero: "zotero://select/library/items/EY5BL7TB"
pdf: /Users/jesper/Zotero/storage/CJYD6MJY/Shalev2000.pdf
tags: [literature]
keywords: [loss-aversion, reference-dependence, equilibrium-refinement, prospect-theory, game-theory, endogenous-reference-points]
topics: ["[[expectations-based-reference-dependence]]"]
related: [Gul1991, Kahneman1979, Koszegi2006b, Tversky1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The Nash equilibrium solution concept for games is based on the assumption of expected utility maximization. Reference dependent utility functions (in which utility is determined not only by an outcome, but also by the relationship of the outcome to a reference point) are a better predictor of behavior than expected utility. In particular, loss aversion is an important element of such utility functions.

## Summary
Shalev embeds prospect-theoretic loss aversion into non-cooperative game theory by extending each game with a per-player loss-aversion coefficient and endogenizing reference points: in equilibrium each player's reference point equals the loss-aversion-weighted expectation of her own payoff (a "consistent" reference point), and no unilateral deviation pays. Two variants are defined—myopic and non-myopic loss-aversion equilibrium—differing in when reference points are updated as an extensive game unfolds. Myopic equilibria always exist (via Kakutani); non-myopic ones may not. The framework nests Nash equilibrium (recovered when all $\lambda_i=0$) and yields counterintuitive comparative statics: becoming more loss averse can raise or lower one's own payoff and others' payoffs.

## Research question
How can loss aversion and reference dependence be incorporated into the solution concept for strategic games, given that reference-dependent utility cannot be folded into a single fixed payoff number (the value of an outcome depends on the whole lottery it sits in)? Where do reference points come from when they are not exogenously framed by an experimenter, and what equilibrium predictions follow?

## Method / identification
The paper is purely theoretical. A standard extensive-form game $G$ with player set $I$, strategy spaces $S_i$, and von Neumann–Morgenstern payoffs $u_i(s)$ is augmented to an **extended game** $(G,(\lambda_i)_{i\in I})$, where $\lambda_i\in\mathbb{R}$ is player $i$'s loss-aversion coefficient ($\lambda_i=0$ is an expected-utility maximizer). Given a basic value $x_i$ and reference point $r_i$, the final (loss-aversion) utility is the kinked function
$$v_i(x_i,r_i)=\begin{cases} x_i & \text{if } x_i\ge r_i\\ x_i-\lambda_i\,(r_i-x_i) & \text{if } x_i< r_i\end{cases}$$
modeled on Tversky & Kahneman's (1992) value function (slope steeper for losses), but applied to vNM utilities rather than money, so it keeps the loss-aversion kink without the S-shaped curvature. For a mixed profile $\sigma$ giving outcome $s$ probability $p_\sigma(s)$, the player's payoff is $w_i(\sigma,r_i)=\sum_{s}p_\sigma(s)\,v_i(u_i(s),r_i)$.

A reference point is **consistent** with a lottery if it equals the lottery's own loss-aversion evaluation: $r_i=\sum_j p^j\,v_i(u_i(x^j),r_i)$. **Lemma 1** shows that for each player and each profile $\sigma$ this fixed point is unique (since $w_i(\sigma,\cdot)$ is continuous and non-increasing in $r_i$), defining a single-valued function $r_i(\sigma)$ lying in a bounded interval $[\underline{r},\bar{r}]$. This consistent reference point coincides with the local utility of Gul's (1991) disappointment-aversion functional, itself a special case of Dekel's (1986) weakening of independence.

A **myopic loss-aversion equilibrium** is a profile $\sigma$ for which there exists $r$ such that $\sigma$ is a Nash equilibrium of the transformed standard game $L(G,\lambda,r)$ and the resulting payoffs equal $r$. Here all evaluation is done at the root and the reference point is held fixed even when contemplating deviations. A **non-myopic loss-aversion equilibrium** requires, at every information set $m$ of player $i$ reached with positive probability, that $r_i(\sigma)\ge r_i(\sigma_{-i},\sigma_i')$ for all deviations $\sigma_i'$—i.e. the player re-evaluates her reference point at each node and consistently with each contemplated deviation.

## Data
None — this is a theoretical contribution. The only empirical inputs are calibration anchors borrowed from the literature (e.g. Tversky & Kahneman's median estimates $\alpha\approx0.88$, $\lambda\approx2.25$; Fishburn & Kochenberger's finding that the loss slope is roughly five times the gain slope). Section 6 sketches, but does not run, experimental tests.

## Key findings
- **Proposition 1:** For simultaneous games (each player one always-reached information set), the sets of myopic and non-myopic loss-aversion equilibria coincide—the two notions differ only through the timing of reference-point updating, not through re-evaluation under deviations.
- **Proposition 2:** Any pure-strategy Nash equilibrium of a perfect-information game is both a myopic and a non-myopic loss-aversion equilibrium of every extension $(G,\lambda)$.
- **Proposition 3 (existence):** Every extended game has a myopic loss-aversion equilibrium (Kakutani fixed-point argument over strategies $\times$ reference points, due to Mertens). Non-myopic equilibria need **not** exist (Example 7).
- **Nesting remark:** If $\lambda_i=0$ for all $i$, the loss-aversion equilibria coincide exactly with the Nash equilibria of $G$.
- **Indeterminacy in equilibrium count:** The number of loss-aversion equilibria can exceed, equal, or fall short of the number of Nash equilibria (Example 4: continuum of Nash, unique LAE; Example 5: unique Nash, continuum of LAE).
- **Allais paradox (Example 1):** Consistent reference points rationalize the modal A-and-D choices for $\lambda\in(\tfrac{1}{9},10)$; the same example shows non-myopic LAE can fail to exist in the two-stage tree representation.
- **Comparative statics (Section 5, Examples 2,3,8):** In matching pennies and the mixed equilibrium of Battle of the Sexes, raising one's $\lambda$ lowers one's own payoff and leaves the other's unchanged; but in a three-player game (Example 8) raising player 1's loss aversion *raises* her payoff and *lowers* player 3's—so loss aversion has no fixed-sign welfare effect.

## Contribution
This is the first solution concept to endogenize reference points inside equilibrium for general (including extensive-form) games rather than treating them as exogenous experimental frames. Reference points acquire a dual role—both the comparison level for gains/losses and a rational anticipation fulfilled in equilibrium—linking game theory to the prospect-theory and disappointment-aversion ([[@Gul1991|Gul 1991]]) traditions while preserving Nash equilibrium as the loss-neutral limit. The myopic/non-myopic distinction cleanly isolates the role of temporal updating of reference points in dynamic strategic settings.

## Limitations & open questions
- **Non-existence of non-myopic equilibrium** is a structural defect: without a built-in notion of timing it is unclear how to balance conflicting reference-point evaluations at different nodes (the author contrasts Ferreira, Gilboa & Maschler's 1995 credible-equilibrium approach, which always exists but assumes preference updating unsuited to this functional).
- **Common knowledge of loss-aversion coefficients** is assumed; learning about others' $\lambda_i$ is left for future work.
- **Measuring loss aversion at the individual level**: virtually all evidence is about averages, not heterogeneity; correlating $\lambda$ with age, gender, status, culture is proposed (with the hypothesis that women are more loss averse than men).
- **Multiple reference points**: how competing reference points combine ([[@Tversky1992|Kahneman 1992]]) is flagged as open.
- **Experimental tests**: designing games where differing $\lambda$ yield different equilibrium strategies, after first eliciting individual loss aversion.
- The functional retains the loss-aversion kink but **cannot reproduce the S-shaped curvature** of prospect theory's value function; risk attitudes are not reference-dependent in this model.

## Connections
The kinked value function and calibration come directly from [[@Kahneman1979|Kahneman & Tversky (1979)]] and [[@Tversky1992|Tversky & Kahneman (1992)]]; the consistent reference point is the fixed-point construction underlying Gul's (1991) disappointment aversion, itself nested in Dekel's (1986) betweenness-style weakening of the independence axiom. Fishburn & Kochenberger (1979) supply the empirical loss-slope estimate. Endowment-effect and status-quo evidence motivating loss aversion is drawn from Kahneman, Knetsch & Thaler (1990, 1991). The dynamic existence problem is contrasted with Ferreira, Gilboa & Maschler (1995) on credible equilibria under preferences that change during play. Rabin (1996) frames reference dependence as core to economic modeling. The broader programme of embedding non-standard preferences into equilibrium connects to later reference-dependent equilibrium work, notably the personal-equilibrium framework of Köszegi & [[@Koszegi2006b|Rabin (2006)]], which similarly endogenizes reference points as rational expectations.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
