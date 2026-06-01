---
citekey: Lambert2008
title: Eliciting properties of probability distributions
authors: ["Lambert, Nicolas S.", "Pennock, David M.", "Shoham, Yoav"]
year: 2008
type: conferencePaper
doi: 10.1145/1386790.1386813
zotero: "zotero://select/library/items/8KQ6UUM7"
pdf: /Users/jesper/Zotero/storage/RTGQUDYE/Lambert et al. - 2008 - Eliciting properties of probability distributions.pdf
tags: [literature]
keywords: [proper-scoring-rules, belief-elicitation, elicitability, prediction-markets, elicitation-complexity, mechanism-design]
topics: []
related: [Gneiting2007, Savage1971]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> _No abstract in source metadata; see Summary below._

## Summary

This paper asks a foundational question in the theory of belief elicitation: when can a single *property* of a probability distribution — a real-valued summary such as the mean, a quantile, or the probability of an event — be elicited truthfully from a forecaster, and which payment rules achieve this? Classical proper scoring rules elicit the *entire* distribution, which is often infeasible (the expert may not know the full distribution, it may be too costly to communicate, or the experimenter may care only about one statistic). Lambert, Pennock, and Shoham (an EC'08 extended abstract) generalize the proper-scoring-rule machinery from full distributions to arbitrary properties. Their central result is a clean geometric characterization: a property is (directly) elicitable if and only if its level sets are convex — equivalently, the property is expressible as a linear constraint on the distribution. They then characterize *all* truth-inducing payment rules, generalize to vectors of properties, define an *elicitation complexity* for properties that are not directly elicitable, and connect the whole apparatus to prediction-market security design.

## Research question

Given a finite outcome space $\Omega=\{\omega_1,\dots,\omega_n\}$, a convex domain $D\subseteq\Delta(\Omega)$ of admissible beliefs, and a property $\Gamma:D\to\mathbb{R}$ (continuous, not locally constant), (1) for which $\Gamma$ does there exist a payment scheme that makes truthful reporting of $\Gamma(P)$ optimal for an expected-utility forecaster, and (2) what is the full class of such schemes? Subsequent questions: how to elicit non-elicitable properties via sets/vectors, how to quantify a property's intrinsic difficulty, and how these map onto market mechanisms.

## Method / identification

This is pure decision/contract theory. A *score function* is a map $s:\mathrm{Int}(\Gamma(D))\to\mathbb{R}^{\Omega}$ assigning to each admissible report $r$ a contract paying $s(r)(\omega^*)$ at realized outcome $\omega^*$. A forecaster with belief $P$ solves $\max_r E_P[s(r)]=\max_r\langle P,s(r)\rangle$. The score is *strictly proper* (incentive compatible) for $\Gamma$ if $E_P[s(r)]<E_P[s(\Gamma(P))]$ for all admissible $P$ and $r\neq\Gamma(P)$. Two strengthenings are introduced: *accuracy-rewarding* (expected score rises monotonically as the report approaches the truth) and *first-order* (the optimum is pinned by the first-order condition).

The identification of elicitable properties is geometric. Lemma 1 shows strict propriety forces each level set $\Gamma^{-1}(r)$ to be convex; Lemmas 2-3 show such level sets are *convex maximal* and have dimension $\dim D - 1$, i.e. they are hyperplanes of $D$. The constructive converse (Theorem 1) builds, from a property with convex level sets, a normal-vector field $v(r)$ — unit-norm, continuous, oriented toward the positive half-space — and sets $s(r)=\int_{r_0}^{r}v(t)\,dt$, verifying strict propriety via $dE_P[s(r)]/dr=\langle v(r),P\rangle$. The full representation (Theorem 3) shows every continuously differentiable strictly proper score has the form

$$s(r)=s_0+\int_{r_0}^{r}\lambda(t)\,v(t)\,dt,$$

where $v$ — the property's *signature* — is uniquely determined by $\Gamma$, and $\lambda(t)\ge 0$ is a free, not-locally-null *weight function* (never null for first-order scores). This is a strict generalization of Schervish's (1989) integral representation for binary-event probability scores.

## Data

None. This is a theory paper: all results are theorems and constructions over abstract probability simplices. The only "data" are worked examples (the binary-event signature, and the logarithmic and quadratic scores recovered as specific weight functions $\lambda$).

## Key findings

- **Theorem 1 / Corollary 1 / Theorem 2:** $\Gamma$ is elicitable iff every level set $\Gamma^{-1}(r)$ is convex, iff convex maximal, iff $\Gamma(P)=r$ is a linear constraint on $P$. Consequence: probabilities, expectations, and (raw) moments are elicitable; variance, skewness, kurtosis, and centered moments are *not* directly elicitable whenever $|\Omega|>2$.
- **Theorem 3 (signature/weight representation):** incentive-compatible payments are exactly positively weighted mixtures of the property's signature; the property fixes the gradient *direction* $v(r)$, while the gradient *norm* $\lambda(r)$ is free (allocate more amplitude where accuracy matters most). **Corollary 2:** a $C^1$ score is strictly proper iff accuracy-rewarding.
- **Vectors of properties (Theorems 4-5):** elicitability of a vector requires convex level sets (necessity only; sufficiency for vectors is left *open*). Crucially, $\{\text{mean},\text{variance}\}$ is elicitable even though variance alone is not. An accuracy-rewarding score for a vector exists iff it is *additively separable* into strictly proper one-dimensional scores — so no accuracy-rewarding score exists for any vector containing an unelicitable component (e.g. the (expectation, variance) pair admits none).
- **Elicitation complexity (Theorems 6):** a property is $k$-elicitable if inferable from $k$ elicitable properties; complexity $C^k$ is the minimal such $k$. Variance is $C^2$, skewness $C^3$, kurtosis $C^3$ or $C^4$ (conjectured $C^4$). With $|\Omega|=n$ every property lies in $C^1,\dots,C^{n-1}$ and no class is empty; some properties (e.g. $\max_\omega P(\{\omega\})$ at $C^{n-1}$) are as hard to elicit as the full distribution.
- **Prediction markets (Theorems 7-9):** under consensus-belief assumptions, markets reveal exactly the same properties as one-dimensional score functions, so $C^k$ properties need $\ge k$ parallel markets. For both continuous double auctions and automated market makers (Hanson's LMSR), the traded securities satisfy $q_r-p_r=ds(r)/dr$ for a first-order score $s$ — a one-to-one map between securities and scores, recovering Hanson's $g(Q)=1/(1+e^{-Q/b})$.

## Contribution

The paper unifies and generalizes the proper-scoring-rule literature ([[@Savage1971|Savage 1971]]; Schervish 1989; [[@Gneiting2007|Gneiting & Raftery 2007]]) from eliciting whole distributions to eliciting arbitrary statistics, giving (a) a sharp convexity/linearity characterization of *what* is elicitable, (b) a complete signature-plus-weight representation of *all* truthful contracts, (c) the new and durable notion of elicitation complexity, and (d) a structural equivalence between elicitation and prediction-market design. These results became a cornerstone of later work on elicitability in statistics and machine learning.

## Limitations & open questions

- **Continuity is assumed throughout.** For properties with *discrete* range, convex level sets remain necessary but are no longer sufficient — characterizing elicitable discrete properties is left open.
- **Finite outcome space.** The authors conjecture results fail on continuous outcome spaces (proofs lean on topological completeness of the domain); whether stronger continuity conditions or generalized-function scores rescue them is open.
- **Vectors/sets of properties:** convexity of level sets is sufficient but its *necessity* for set-elicitability is unresolved; a Schervish-style integral representation for sets is not yet known; and the complexity of most common properties is not pinned down (kurtosis $C^3$ vs $C^4$).

## Connections

This is the canonical generalization of proper scoring rules surveyed by [[@Gneiting2007|Gneiting & Raftery (2007)]], building directly on [[@Savage1971|Savage (1971)]] for expectation elicitation, Cervera & Munoz (1996) for quantile/fractile scores, and Schervish (1989) for the integral representation of binary-event scores (with Buja, Stuetzle & Shen 2005 on the same Schervish-measure taxonomy in statistical learning). The market half connects to Hanson (2003) on the logarithmic market scoring rule and to Feigenbaum, Fortnow, Pennock & Sami (2005) on which statistics distributed markets can compute (linear functions of signals). The elicitability characterization and complexity notion are foundational for choice modeling and the broader proper-scoring-rule / belief-elicitation toolkit used to incentivize truthful probabilistic forecasts.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
