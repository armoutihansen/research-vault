---
citekey: Andreoni2002
title: "Giving According to GARP: An Experimental Test of the Consistency of Preferences for Altruism"
authors: ["Andreoni, James", "Miller, John"]
year: 2002
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/H3JAG845"
pdf: /Users/jesper/Zotero/storage/Q6HRUDW5/Andreoni2002.pdf
tags: [literature]
keywords: [revealed-preference, garp, altruism, social-preferences, dictator-game, ces-utility, preference-heterogeneity]
topics: ["[[inequity-aversion-distributional-preferences]]"]
related: [Bolton2000, Charness2002, Fehr1999, Fisman2007, Samuelson1938]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Andreoni and Miller embed altruistic giving in a modified dictator game where the price of giving and the size of the pie vary across decisions, generating crossing linear budget sets over the payoffs of self and other. This lets them apply revealed-preference theory (GARP) to other-regarding choice. Over 98% of subjects choose consistently with utility maximization, so altruism is "rational" in the sense of being rationalizable by a well-behaved (continuous, convex, monotonic) utility function. Preferences are highly heterogeneous: roughly a quarter are purely selfish, others span Leontief (Rawlsian, equal-split) to perfect-substitutes (utilitarian) types. Estimated CES utility functions, weighted by type frequencies, successfully predict aggregate giving in independent dictator, public-goods, and prisoner's-dilemma studies. A sizable minority (23%) exhibit convex but nonmonotonic ("jealous") preferences.

## Research question
Can subjects' concern for altruism or fairness be expressed as a well-behaved preference ordering — i.e., is observed unselfish behavior consistent with the axioms of revealed preference, and hence rationalizable by a quasiconcave utility function? Secondarily: are altruistic preferences monotonic, or do some subjects display jealousy/spite?

## Method / identification
The setting is nonstrategic. Person $s$ chooses an allocation $(\pi_s,\pi_o)$ of own and other's payoff to maximize $U_s=u_s(\pi_s,\pi_o)$. A modified dictator game (extending Forsythe et al. 1994) gives each subject a menu of budgets $\pi_s+p\,\pi_o=m$, where the inverse of the "hold" value is the price of self-payoff and the inverse of the "pass" value is the price of other-payoff $p$. Varying token endowments (income) and token redemption values (prices) produces budget lines that cross, the variation needed to test for an underlying ordering.

Consistency is assessed with the revealed-preference hierarchy WARP $\subset$ SARP, and GARP: GARP states that if $A$ is indirectly revealed preferred to $B$, then $B$ is not strictly directly revealed preferred to $A$. Following Afriat (1967) and Varian (1982), satisfying GARP is necessary and sufficient for the existence of a well-behaved (nonsatiated, continuous, concave, monotonic) utility function rationalizing the data under linear budgets. Severity of violations is measured by Afriat's (1972) Critical Cost Efficiency Index (CCEI) — the fraction by which budgets must be shrunk to remove all violations — with Varian's (1991) 0.95 threshold. Statistical power is assessed two ways: Bronars' (1987) test (probability a uniformly-random chooser violates GARP) and an ex-post bootstrap drawing each budget's choice from the empirical pool.

For the 57% of subjects not fitting an exact type, CES utility $U_s=(a\pi_s^{\rho}+(1-a)\pi_o^{\rho})^{1/\rho}$ is estimated, where $a$ indexes selfishness and the elasticity of substitution is $\sigma=1/(\rho-1)$. With self-payoff as numeraire and $r=-\rho/(1-\rho)$, $A=[a/(1-a)]^{1/(1-\rho)}$, the demand share is estimated by two-limit tobit maximum likelihood (choices censored at both budget ends), specified in budget shares to ensure homoskedasticity.

Monotonicity is tested via five upward-sloping (but finite) budgets in which subjects fix the cents-per-token value (0–10) on assigned allocations; two are advantageous, two disadvantageous, letting "rational jealousy" reduce own and other payoff to shrink inequality.

## Data
176 subjects from intermediate/upper-level economics courses across 5 sessions (34–38 each). Sessions 1–4 had 8 budgets; session 5 added 3 more downward-sloping budgets (11 total) plus a part-2 set of 5 upward-sloping budgets. Tokens worth 1–4 points; total tokens 40/60/75/80/100; points worth $0.10. Sessions 1–4 averaged $9.60 in ~1 hour; session 5 averaged $19.74 in ~70 minutes. Anonymous random matching; one decision per subject chosen and paid.

## Key findings
- Consistency: only 3 subjects (1.7%) cannot be rationalized by a quasiconcave utility function; over 98% are consistent. Of those with any violation, only 3 fall below the 0.95 CCEI threshold. The test has real power: Bronars power 78.1% (8 budgets) rising to 94.7% (11 budgets); bootstrap power 76.4% and 85.7%.
- Representativeness: at price one (budgets 7–9), subjects give away ~23% of the pie, closely matching Forsythe et al. (1994) (22.2–23.3%).
- Heterogeneous types: 43% fit a standard utility function exactly — 22.7% perfectly selfish $U=\pi_s$, 14.2% Leontief $U=\min\{\pi_s,\pi_o\}$ (always equal split, Rawlsian), 6.2% perfect substitutes $U=\pi_s+\pi_o$ (give all to the cheaper recipient, utilitarian). The remaining 57% cluster into "weak" versions of these three.
- CES estimates (Table IV) are all significant beyond 0.001: weak-Leontief $\sigma\approx-0.74$ (strong complementarity), weak-selfish $\sigma\approx-2$, weak-perfect-substitutes $\sigma\approx-3.02$ (flat indifference curves).
- Out-of-sample prediction: the frequency-weighted mix of six types reproduces giving curves in independent dictator games, first-round/average linear public-goods contributions (recast as multi-person dictator games with price $p=(1-a)/a$), and cooperation rates in 200-round PD (predicted 6.25–22.4% vs. observed ~20%).
- Jealousy: 23% (8 of 34) make convex but nonmonotonic choices, shrinking token values on disadvantageous budgets (71% of nonmonotonic choices there); average valuation falls from 9.94 to 8.97 cents as budgets become less advantageous. Distaste for advantageous inequality is far weaker. Four of the eight jealous subjects remain consistent with convexity, four do not.

## Contribution
First application of nonparametric revealed-preference analysis (GARP, CCEI) to other-regarding/altruistic choice, establishing that altruism is rational and rationalizable rather than noise or irrationality. Provides a portable, individual-level CES "menu" of social-preference types whose aggregation predicts behavior across distinct experimental paradigms, and documents the centrality of preference heterogeneity (selfish, Rawlsian, utilitarian) for any theory of fairness. Introduces a clean within-subject budget design that became a template for later modular dictator/social-allocation experiments.

## Limitations & open questions
- The strong-type subjects are treated as choosing without measurement error, a simplifying assumption; a "perfectly selfish" subject might show price elasticity over a wider price range, weakening prediction outside the experimental price range.
- The analysis is deliberately nonstrategic; the authors flag as future work the more general program in which preferences $u_s(\pi_s,\pi_o;\gamma)$ depend on a vector $\gamma$ of game attributes (rules, anonymity, sex of opponent, framing) and shift systematically with $\gamma$.
- Public-goods comparisons are only "suggestive" given repetition/learning, strategic play, and group-size differences from the two-person game.
- Nonmonotonicity (jealousy) coexists with convexity for some subjects but not others; reconciling spite with well-behaved preferences is left open.
- The authors argue fairness must be modeled at the individual level because aggregate-fitting models may misdescribe individuals — an open modeling challenge.

## Connections
Builds directly on the dictator game of Forsythe, Horowitz, Savin & Sefton (1994) and the revealed-preference machinery of [[@Samuelson1938|Samuelson (1938)]], Houthakker (1950), Afriat (1967, 1972), and Varian (1982, 1991, 1993); Bronars (1987) supplies the power test. Related individual-rationality GARP experiments include Cox (1997), Sippel (1997), Mattei (2000), and Harbaugh, Krause & Berry (2001) ("GARP for kids"). The estimated social-preference types anticipate and complement structural inequity-aversion and reciprocity models such as [[@Fehr1999|Fehr & Schmidt (1999)]], [[@Bolton2000|Bolton & Ockenfels (2000)]], and [[@Charness2002|Charness & Rabin (2002)]], and connect to warm-glow giving (Andreoni 1988, 1990). The prediction exercises draw on public-goods data from Isaac & Walker (1988), Andreoni (1995a, 1995b), and others, and the PD evidence from Andreoni & Miller (1993). Nonmonotonicity links to Ochs & Roth's (1989) disadvantageous counter-proposals and Palfrey & Prisbrey (1996, 1997). The crossing-budget design later underpins large-scale social-preference estimation, e.g. [[@Fisman2007|Fisman, Kariv & Markovits (2007)]] and Bruhin, Fehr & Schmidt (2019).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
