---
citekey: Heinrich2014
title: The mode functional is not elicitable
authors: ["Heinrich, Claudio"]
year: 2014
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/IJ4HAF8Z"
pdf: /Users/jesper/Zotero/storage/N7QW3F3Q/Heinrich - 2014 - The mode functional is not elicitable.pdf
tags: [literature]
keywords: [elicitability, proper-scoring-rules, point-forecasting, mode-functional, decision-theory, consistent-scoring-functions]
topics: ["[[scoring-rules-elicitability]]"]
related: [Gneiting2011, Lambert2008, Savage1971]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> This article is concerned with point forecasting of a real-valued random variable with a general Lebesgue density. Answering a question of [[@Gneiting2011|Gneiting (2011)]], it is shown that the mode is not elicitable, or, in other words, that it is impossible to find a loss or scoring function under which the mode is the Bayes predictor.

## Summary

This short Biometrika paper answers an open question posed by [[@Gneiting2011|Gneiting (2011)]]: is the mode of a probability distribution an elicitable functional? The answer is no. A statistical functional is *elicitable* if there exists a scoring function under which reporting the functional's value is the (uniquely) loss-minimizing point forecast — the property that licenses comparative forecast evaluation and regression-style estimation. The mean, quantiles, expectiles, and the midpoint of a modal interval are all elicitable; conditional value-at-risk is not. Heinrich shows the mode joins the non-elicitable camp, and does so via a mechanism distinct from any prior example. The paper proves three increasingly tight non-elicitability theorems, supplies the locally-integrable scoring-function machinery behind them, and runs a small simulation showing that the standard practical workaround — minimizing the zero-one ("$0$–$1$") score over a small modal interval — cannot reliably recover the mode of a bimodal density. Coverage here is full: the extracted PDF includes the abstract, all results, the simulation, the discussion, and the appendix proofs.

## Research question

Can the mode functional $T_0$, mapping a distribution to its mode(s), be elicited by some strictly consistent scoring function $S(x,y)$? Equivalently: does there exist a loss function under which the Bayes-optimal point forecast equals the mode for every distribution in a reasonably rich class? The motivation is the widespread informal claim that the mode minimizes expected zero-one loss $S_c(x,y)=\mathbf{1}(|x-y|>c)$ "in the limit" as $c\to 0$, a heuristic the paper sets out to test.

## Method / identification

This is a pure decision-theory / mathematical-statistics paper. A scoring function is $S:\mathbb{R}\times\mathbb{R}\to[0,\infty)$; $S(x,y)$ is the penalty for forecasting $x$ when $y$ realizes. $S$ is *consistent* for a set-valued functional $T:\mathcal{F}\to 2^{\mathbb{R}}$ relative to a class $\mathcal{F}$ if $E_F\{S(t,Y)\}\le E_F\{S(x,Y)\}$ for all $F\in\mathcal{F}$, $t\in T(F)$, $x\in\mathbb{R}$; *strictly* consistent if equality forces $x\in T(F)$. $T$ is elicitable relative to $\mathcal{F}$ iff some strictly consistent $S$ exists. The mode $T_0$ is defined as a limit of midpoints $\hat{x}_c=\arg\max_x F([x-c,x+c])$ of modal intervals of length $2c$ as $c\to 0$.

The core proof device is the set
$$M_\varepsilon(x_0,x_1)=\{y\in\mathbb{R}:\varepsilon<S(x_0,y)-S(x_1,y)\},$$
the region where the score prefers forecast $x_1$ to $x_0$ by more than $\varepsilon$. The strategy (reminiscent of Thomson's 1979 characterization of quantile-consistent scores, reviewed by Grant & Gneiting, 2013): assume a strictly consistent $S$ exists, then show $\lambda\{M_\varepsilon(x_0,x_1)\}=0$ for all $\varepsilon>0$ (else one could build a density with mode $x_0$ but most mass in $M_\varepsilon$, contradicting consistency). But then $M_0(x_0,x_1)=\bigcup_n M_{1/n}(x_0,x_1)$ is also null, which contradicts consistency once a distribution with mode $x_1$ is chosen. The technical engine is that distributions with a tall, thin modal peak at $x_0$ carrying negligible probability mass are admissible — Lemma A1 establishes that any strictly consistent $S$ must have $S(x_0,\cdot)$ locally integrable; the dominated-convergence argument then drives the contradiction. For the Gaussian-mixture case, Lemma 1 constructs mixtures $h=pf+(1-p)g$ with unique mode $x_0$ yet arbitrarily little mass outside any target interval $I$.

## Data

No empirical data. The only "data" is a Monte Carlo simulation study (§4): $n=10{,}000$ draws from a bimodal mixture $0.75f+0.25g$ ($f\sim\mathcal{N}(2,1.5^2)$, $g\sim\mathcal{N}(-2,0.5^2)$), repeated over 1000 runs, used to estimate the modal-interval midpoint $\hat{x}_c$ for several $c$.

## Key findings

- **Proposition 1** (positive result): For classes containing only unimodal *discrete* measures, $T_0$ *is* elicitable, with strictly consistent score $S(x,y)=\mathbf{1}(x\neq y)$.
- **Theorem 1** (main result): $T_0$ is *not* elicitable relative to the class $\mathcal{F}$ of unimodal probability measures on $\mathbb{R}$ with Lebesgue densities.
- **Theorem 2** (strengthening): Non-elicitability persists even when densities are uniformly bounded by any $B>0$ (class $\mathcal{F}_B$). The proof splits into three cases on whether $\lambda\{M_\varepsilon\}$ is infinite, finite-positive, or zero, deriving a contradiction in each.
- **Theorem 3** (restricted, applied class): Even for unimodal *Gaussian mixtures* $\mathcal{F}_{GM}$, no strictly consistent $S$ exists whose discontinuity sets are Lebesgue-null — i.e., any putative mode-eliciting score would have to be wildly (more than null-set) discontinuous.
- **Structural insight**: The mode has *convex level sets* (a mixture of two distributions sharing unique mode $x_0$ still has mode $x_0$), yet is not elicitable. This is, to the author's knowledge, the first non-elicitability example *not* obtained by violating Osband's convex-level-set condition — proving convex level sets are necessary but **not sufficient** for elicitability (cf. [[@Gneiting2011|Gneiting 2011]], Thm 6).
- **Simulation**: The zero-one score with small $c$ fails to discriminate the two near-equal peaks; MSE relative to the true mode bottoms out around $c=0.1$ and does *not* improve for smaller $c$, because too few sampled points fall in $[x-c,x+c]$.

## Contribution

It settles Gneiting's (2011) open question negatively and corrects a folklore claim that the mode is the Bayes forecast under zero-one loss. Methodologically, it severs the link between convex level sets and elicitability — previously the main known route to non-elicitability — supplying a qualitatively new counterexample. Practically, it warns that mode forecasts cannot be honestly elicited or compared via any scoring rule, and that small modal intervals are an unreliable substitute.

## Limitations & open questions

The non-elicitability results require *rich* distribution classes admitting tall thin peaks; the discrete case (Prop. 1) is elicitable, so the boundary between elicitable and non-elicitable mode-classes is not fully mapped. The author conjectures Theorem 3's argument extends beyond Gaussian mixtures — explicitly naming Cauchy and Student-$t$ mixtures (any convex combination of suitable classes) as candidate generalizations, but leaves these unproven. Open hooks: (i) characterize exactly which restricted/parametric classes make the mode elicitable; (ii) whether a useful *weakly* consistent or order-sensitive surrogate exists; (iii) the connection to higher-order elicitability (jointly eliciting the mode with an auxiliary functional), which the paper does not address.

## Connections

The paper directly answers and builds on [[@Gneiting2011|Gneiting (2011)]], "Making and evaluating point forecasts," the canonical reference framing elicitability for point forecasting. The elicitability concept traces to [[@Lambert2008|Lambert, Pennock & Shoham (2008)]] on eliciting properties of distributions over finite outcome spaces, and further back to [[@Savage1971|Savage (1971)]] on eliciting personal probabilities. The proof technique adapts Thomson (1979)'s characterization of quantile-consistent scoring functions, as reviewed in the decision-theoretic setting by Grant & Gneiting (2013). The convex-level-set necessary condition is Osband's (1985 PhD thesis), restated in [[@Gneiting2011|Gneiting]] (2011, Theorem 6). Elicitability of the midpoint functional uses Lehmann & Casella (1998). The work sits adjacent to the broader proper-scoring-rules literature (e.g., Gneiting & Raftery, 2007) and to later joint-elicitability work by Fissler & Ziegel (both acknowledged) on the systemic risk measures Value-at-Risk and Expected Shortfall.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
