---
citekey: Harless1994
title: The Predictive Utility of Generalized Expected Utility Theories
authors: ["Harless, David W.", "Camerer, Colin F."]
year: 1994
type: journalArticle
doi: 10.2307/2951749
zotero: "zotero://select/library/items/S33ZI72Z"
pdf: /Users/jesper/Zotero/storage/IETYAWM3/Harless1994.pdf
tags: [literature]
keywords: [expected-utility, generalized-eu, prospect-theory, rank-dependent-utility, maximum-likelihood, risk-preferences, model-selection, choice-under-risk]
topics: []
related: [Gul1991, Kahneman1979, Quiggin1982, Tversky1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Many alternative theories have been proposed to explain violations of expected utility (EU) theory observed in experiments. Several recent studies test some of these alternative theories against each other. Formal tests used to judge the theories usually count the number of responses consistent with the theory, ignoring systematic variation in responses that are inconsistent. We develop a maximum-likelihood estimation method which uses all the information in the data, creates test statistics that can be aggregated across studies, and enables one to judge the predictive utility--the fit and parsimony--of utility theories. Analyses of 23 data sets, using several thousand choices, suggest a menu of theories which sacrifice the least parsimony for the biggest improvement in fit. The menu is: mixed fanning, prospect theory, EU, and expected value. Which theories are best is highly sensitive to whether gambles in a pair have the same support (EU fits better) or not (EU fits poorly). Our method may have application to other domains in which various theories predict different subsets of choices (e.g., refinements of Nash equilibrium in noncooperative games).

## Summary
Harless and Camerer reanalyze 23 experimental data sets of risky pairwise choice (~8,000 choices, ~2,000 choice patterns) with a unified maximum-likelihood error-rate model that treats each theory of choice under risk as a restriction on the proportions of subjects holding each possible *pattern* of preferences. Because the method scores theories on the entire distribution of observed patterns rather than just the count of consistent choices, and because its test statistics are additive across studies, it can rank theories by a fit-vs-parsimony tradeoff. The headline output is a "menu" of undominated theories—mixed fanning, prospect theory, EU, and expected value—from which a researcher selects according to the price they are willing to pay in fit for added parsimony. A central empirical finding is that EU's accuracy depends sharply on whether the two gambles in a pair share the same support (interior of the probability triangle, where EU fits well) or not (boundary, where EU fits poorly).

## Research question
How can competing generalized expected-utility theories be compared on equal statistical footing, using all the information in observed choice patterns, so as to judge each theory's *predictive utility*—the joint tradeoff of goodness-of-fit and parsimony—and which theories survive such a comparison?

## Method / identification
The central object is the unit (Marschak–Machina) probability triangle, in which three-outcome lotteries are plotted and theories are expressed as restrictions on the *patterns* of S ("safer") vs R ("riskier") choices a subject can hold across several related pairs. With three pairs there are $2^3=8$ possible patterns; EU permits only the two consistent patterns SSS and RRR (parallel linear indifference curves), fanning out additionally permits RSS and RRS, fanning in permits SSR and SRR, mixed fanning excludes only SRS, and so on for rank-dependent variants (RD-cave/RD-vex under elasticity conditions on the weighting function $g(p)$) and a simplified prospect theory.

The estimator characterizes each theory as a restriction on the population proportions $p(\cdot)$ of subjects whose *true* preferences correspond to each allowed pattern, plus a single error rate $\varepsilon$ governing independent, equally-likely mistakes on each binary choice. A subject of true type can produce an observed pattern through errors: e.g. for fanning out the probability of observing RRR is
$$p(\text{SSS})\varepsilon^3 + p(\text{RSS})\varepsilon^2(1-\varepsilon) + p(\text{RRS})\varepsilon(1-\varepsilon)^2 + p(\text{RRR})(1-\varepsilon)^3.$$
For each theory one maximizes the multinomial likelihood of the observed pattern frequencies over the allowed type proportions and over $\varepsilon\in[0,0.5]$. The maximized log-likelihood yields chi-squared statistics that test a theory against the saturated model and—being additive—can be summed across the 23 studies. Theories are then ranked by trading the chi-squared cost of misfit against the number of free pattern-parameters (parsimony, defined here as the number of patterns a theory allows, not its count of free functions). A graphical device plots proportion-consistent against number-of-patterns-allowed relative to a concave "data frontier" and a "random-choice line," screening out *dominated* theories.

## Data
None original. The paper is a meta-analysis / reanalysis of 23 published data sets of multiple pairwise lottery choices (3, 4, or 5 pairs each), totaling nearly 8,000 individual choices and about 2,000 choice patterns, drawn from studies such as Battalio, Kagel and Jiranyakul (1990), Camerer (1989, 1992), Chew and Waller (1986), Conlisk (1989), Harless (1992), Prelec (1990), Sopher and Gigliotti (1990), and Starmer and Sugden (1989).

## Key findings
(1) Every theory is rejected by a chi-squared test against the saturated model: for each there is systematic variation in excluded patterns a more refined theory could capture. (2) Theories err in two opposite ways—EU and weighted utility (WEU) are "too lean" (they should admit a few more common patterns), while mixed fanning and rank-dependent EU are "too fat" (they admit many rarely-chosen patterns). (3) EU's fit depends dramatically on support: it predicts poorly when the paired gambles have *different* support (triangle boundary) and well when they have the *same* support (interior), implying that nonlinear weighting of small probabilities is the empirically important departure from EU. (4) Aggregating all studies, the undominated menu (by ascending parsimony) is mixed fanning, prospect theory, EU, and expected value; for gambles with different support there is *no* price-of-precision at which EU beats EV. Losers—dominated by more accurate, more parsimonious rivals—are betweenness-based theories (implicit/weighted EU) and pure fanning-in. Notably, the method rejects several theories (mixed fan, linear mixed fan / Gul's disappointment aversion) using the very data that inspired them.

## Contribution
Replaces the prevailing "count the consistent choices" test—which mechanically rewards theories that permit more patterns and discards information in the unpredicted responses—with a likelihood-based, error-augmented framework that (i) uses the full pattern distribution, (ii) produces additive, poolable test statistics, and (iii) operationalizes a transparent fit-vs-parsimony menu. It thereby resolves prior interpretive disputes (e.g. conflicting readings of Chew–Waller) and delivers a cumulative empirical verdict on generalized EU theories.

## Limitations & open questions
The authors flag several explicit hooks: (a) the cross-study aggregation assumes studies are *independent*; if they are dependent, the pooled conclusions are overstated and new domains may still add value. (b) The error model is deliberately simple (constant, independent error rate $\varepsilon$); they call for "combining structural explanations of choice problems with more sophisticated theories of errors." (c) Generalizability is limited to lotteries with well-specified probabilities and monetary outcomes; behavior in naturally-occurring choices may differ. (d) Promising untested domains include gambles over losses, many-outcome gambles, and very-low-probability gambles. (e) Individual function-fitting (heterogeneous parameters) versus representative-agent homogeneity is left open. (f) The method is proposed for transfer to other domains—ranking Nash equilibrium refinements/coarsenings in noncooperative games and solution concepts in cooperative games—where theories predict different subsets of choices.

## Connections
The exercise sits atop the Marschak (1950) and Machina (1982, 1987) triangle geometry and tests generalizations of EU including [[@Quiggin1982|Quiggin (1982)]] and Yaari (1987) rank-dependent / anticipated utility, Chew, Karni and Safra (1987) and Segal (1987, 1989) rank-dependent forms, Chew and MacCrimmon (1979) / Chew (1983) / Fishburn (1982, 1983) weighted utility, Dekel (1986) and Chew (1989) implicit EU (betweenness), [[@Gul1991|Gul (1991)]] disappointment aversion, Neilson (1992a) mixed/linear mixed fanning, and [[@Kahneman1979|Kahneman and Tversky (1979)]] prospect theory (with the cumulative extension of [[@Tversky1992|Tversky and Kahneman (1992)]]). The error-rate philosophy parallels McKelvey and Palfrey (1992) on the centipede game and anticipates quantal-response approaches, and El-Gamal and Grether (1993) on probability judgments; Selten (1991) supplies an alternative measure-of-predictive-success the paper compares against. The fit-vs-parsimony framing echoes Stigler (1950) on generality, congruence, and manageability of utility theories. The follow-on representative-agent estimation is Camerer and Ho (1994).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
