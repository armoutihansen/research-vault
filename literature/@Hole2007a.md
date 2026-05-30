---
citekey: Hole2007a
title: Fitting Mixed Logit Models by Using Maximum Simulated Likelihood
authors: ["Hole, Arne Risa"]
year: 2007
type: journalArticle
doi: 10.1177/1536867x0700700306
zotero: "zotero://select/library/items/QZEWP4C6"
pdf: /Users/jesper/Zotero/storage/5YMHMULG/Hole2007.pdf
tags: [literature]
keywords: [mixed-logit, random-parameters-logit, maximum-simulated-likelihood, discrete-choice, stata, halton-draws]
topics: []
related: [Drukker2006, Revelt1998]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This article describes the mixlogit Stata command for fitting mixed logit models by using maximum simulated likelihood.

## Summary
This is a Stata Journal software article introducing the `mixlogit` command (plus the companion `mixlpred` and `mixlcov` commands) for estimating mixed logit (random-parameters logit) models by maximum simulated likelihood. After a compact statement of the mixed logit model and its simulated likelihood, the bulk of the paper is a hands-on syntax reference and worked examples using Train's electricity-supplier choice data and Haan & Uhlendorff's pupil-behavior data. It became one of the most widely used tools for discrete-choice estimation in Stata.

## Research question
Not a research question in the scientific sense; the paper is a methods/software contribution. The practical question it answers is: how can applied researchers fit flexible mixed logit models - allowing random (normal or lognormal), possibly correlated, taste coefficients and panel choice data - within Stata using maximum simulated likelihood?

## Method / identification
The model follows [[@Revelt1998|Revelt & Train (1998)]]. For a sample of $N$ respondents each facing $J$ alternatives over $T$ choice occasions, individual $n$'s utility from alternative $j$ on occasion $t$ is
$$U_{njt} = \beta_n' x_{njt} + \varepsilon_{njt},$$
where $\beta_n$ is a vector of individual-specific coefficients, $x_{njt}$ are observed attributes, and $\varepsilon_{njt}$ is i.i.d. extreme value. Coefficients are distributed with density $f(\beta\mid\theta)$, where $\theta$ are the distributional parameters (means, standard deviations, and covariance terms). Conditional on $\beta_n$, the choice probability is the conditional logit (McFadden 1974):
$$L_{nit}(\beta_n) = \frac{\exp(\beta_n' x_{nit})}{\sum_{j=1}^{J}\exp(\beta_n' x_{njt})}.$$
The probability of an individual's observed choice sequence conditional on $\beta_n$ is $S_n(\beta_n) = \prod_{t=1}^{T} L_{ni(n,t)t}(\beta_n)$, and the unconditional probability integrates over the taste distribution:
$$P_n(\theta) = \int S_n(\beta) f(\beta\mid\theta)\, d\beta.$$
Because the log likelihood $LL(\theta) = \sum_{n=1}^{N}\ln P_n(\theta)$ has no closed form, it is approximated by the simulated log likelihood
$$SLL(\theta) = \sum_{n=1}^{N}\ln\left\{\frac{1}{R}\sum_{r=1}^{R} S_n(\beta_r)\right\},$$
where $R$ is the number of replications and $\beta_r$ is the $r$-th draw from $f(\beta\mid\theta)$. Implementation details: `mixlogit` is a `d0` `ml` evaluator; draws are Halton sequences (via Mata's `halton()`, per [[@Drukker2006|Drukker & Gates 2006]]), with the first $K$ primes used for $K$ random coefficients and an initial `burn()` to reduce cross-dimension correlation. Coefficients may be normal or lognormal (`ln()`); lognormal sign-restricts a coefficient (negative effects are accommodated by entering the attribute times $-1$). With the `corr` option, correlated coefficients are parameterized through the lower-triangular Cholesky factor $L$ of the covariance matrix $V = LL'$; `mixlcov` (a wrapper for `nlcom`) recovers $V$ and its standard errors postestimation. `mixlpred` produces in- and out-of-sample predicted probabilities. Default settings are `nrep(50)` and `burn(15)`.

## Data
No new data are collected. Illustrations use two existing datasets: (i) part of Huber & Train's (2001) residential electricity-supplier choice experiment (4,780 observations; four suppliers per choice; attributes price, contract length, local, well-known, time-of-day and seasonal rate dummies; unlabeled choice experiment with no alternative-specific constants); and (ii) Haan & Uhlendorff's (2006) data on teachers' ratings of pupil behavior (3,939 observations after expanding to three performance alternatives), used to show that `mixlogit` can fit a multinomial logit with unobserved heterogeneity.

## Key findings
There are no theorems; the "findings" are demonstrations of the command's capabilities and substantive illustrations. In the electricity example, consumers on average prefer lower price, shorter contracts, local and well-known providers, and fixed over variable rates, with significant taste heterogeneity for every attribute (the joint LR test on the standard deviations strongly rejects homogeneity). Using $100\times\Phi(-b_k/s_k)$, roughly 21% prefer longer contracts, 14% prefer a non-local provider, and 9% prefer a less-known provider. The lognormal-price specification yields a strictly negative price coefficient for all individuals, with median, mean, and standard deviation of the coefficient recovered as $\exp(b_p)$, $\exp(b_p + s_p^2/2)$, and $\exp(b_p + s_p^2/2)\sqrt{\exp(s_p^2)-1}$. The correlated-coefficients model improves fit substantially: an LR test of the off-diagonal $L$ elements ($\chi^2_{10} = 2\times(1137.7962-1060.8267)=153.94$) rejects uncorrelated tastes. The pupil-behavior example closely (not exactly) replicates Haan & Uhlendorff (2006); residual differences arise because the two implementations generate Halton draws from different primes.

## Contribution
Provides a flexible, freely distributed Stata estimator for mixed logit models supporting fixed and random coefficients, normal and lognormal distributions, correlated random coefficients via a Cholesky parameterization, panel (repeated-choice) data, and alternative-specific attributes - together with postestimation prediction (`mixlpred`) and covariance recovery (`mixlcov`). It lowered the barrier to applying random-parameters logit in applied microeconometrics, generalizing the earlier Haan & Uhlendorff (2006) routine.

## Limitations & open questions
The paper flags the accuracy-versus-speed tradeoff in choosing the number of Halton draws $R$: more draws raise accuracy but estimation time, and a suggested workflow is a small $R$ (e.g., 50) for specification search and a larger $R$ (e.g., 500) for the final model - referring to Train (2003), Cappellari & Jenkins (2006), and Haan & Uhlendorff (2006) for deeper treatment of simulation accuracy. Simulation-based estimators generally yield slightly different results unless draws are generated identically (prime selection matters). Distributional assumptions are restricted to normal and lognormal; richer mixing distributions are not supported. `technique(bhhh)` is not allowed. These are practical constraints rather than formally posed open problems.

## Connections
Built directly on [[@Revelt1998|Revelt & Train (1998)]] and Train (2003) for the mixed logit framework and simulation methods, and on McFadden (1974) for the underlying conditional logit. It extends Haan & Uhlendorff (2006), whose Stata routine for multinomial logit with unobserved heterogeneity it generalizes and replicates. The Halton-draw machinery relies on [[@Drukker2006|Drukker & Gates (2006)]], and the data-expansion approach parallels Long & Freese (2006). Illustrative data come from Huber & Train (2001). Simulation-accuracy discussion connects to Cappellari & Jenkins (2006). Substantively, the command is a workhorse for estimating heterogeneous preferences in discrete-choice and stated-preference work, complementing structural choice-modeling approaches used in social-preference and choice estimation.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
