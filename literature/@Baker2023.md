---
citekey: Baker2023
title: Using bayesmixedlogit and bayesmixedlogitwtp in Stata
authors: ["Baker, Matthew J."]
year: 2023
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/8VMYYN4B"
pdf: /Users/jesper/Zotero/storage/5Z2TKNZJ/Baker - 2023 - Using bayesmixedlogit and bayesmixedlogitwtp in St.pdf
tags: [literature]
keywords: [discrete-choice, mixed-logit, bayesian-mcmc, random-coefficients, willingness-to-pay, stata-software]
topics: ["[[discrete-choice-econometrics]]"]
related: [Hole2007, Hole2012]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> _No abstract in source metadata; see Summary below._

## Summary

This is a software guide documenting two Stata commands authored by Matthew J. Baker: `bayesmixedlogit`, which fits the mixed logit (random-coefficients logit) discrete-choice model by Bayesian Markov chain Monte Carlo (MCMC), and its wrapper `bayesmixedlogitwtp`, which reparameterizes the model in willingness-to-pay (WTP) space. The document mirrors the in-Stata help files and gives the syntax, full option set, five worked examples, and stored results. The algorithm's derivation appears separately in Baker (2014); this paper is the user-facing companion — a practical applied-econometrics reference for estimating heterogeneous-preference choice models in a Bayesian framework, not a methodological contribution. Implementation follows Train (2009, ch. 12), with the sampler built on the author's adaptive-MCMC Mata routine `amcmc()`, and data-setup conventions and much syntax borrowed from Hole's (2007) frequentist `mixlogit`.

## Research question

Not a research paper with a hypothesis; it is software documentation. The implicit question it answers is practical: how can an applied researcher estimate a mixed logit model (and its WTP-space variant) in Stata using Bayesian methods, what options control the MCMC sampler, and how should the output be interpreted?

## Method / identification

The target model is the mixed logit. Individual $n$ choosing alternative $i$ on occasion $t$ has utility $U_{nit}=\beta_n' x_{nit}+\varepsilon_{nit}$ with i.i.d. type-1 extreme-value errors, so conditional on the individual-specific coefficient vector $\beta_n$ the choice probabilities are standard logit; heterogeneity enters through $\beta_n\sim N(b,\Sigma)$ (a subset of coefficients may be held fixed). Estimation is fully Bayesian: rather than maximizing a simulated likelihood, the command draws from the joint posterior of the population mean $b$, covariance $\Sigma$, and the individual-level $\{\beta_n\}$ via Gibbs sampling. Priors are deliberately diffuse — a flat (diffuse) prior on the means $b$ and an identity inverse-Wishart prior on $\Sigma$ — following the Gelman et al. (2009) Bayesian-data-analysis template.

The Gibbs blocks are the random coefficients, the fixed coefficients, and the hyperparameters $b,\Sigma$. Because the conditional posteriors of the logit-level coefficients are non-conjugate, the coefficient blocks are sampled by Metropolis steps embedded in the Gibbs scheme using the adaptive MCMC machinery of `amcmc()` (Baker 2014). Two samplers are offered: a `global` proposal updating all random parameters jointly, and a `mwg` ("Metropolis within Gibbs") proposal updating each random parameter separately in a nested step (more robust when starting values are poorly scaled). Adaptation tunes the proposal scale toward a target acceptance rate (default $0.234$, the diffusion-optimal rate), governed by a damping parameter. Standard MCMC controls are exposed — `draws()`, `burn()`, `thin()`, `jumble` (reshuffling) to attenuate autocorrelation, and `from()`/`fromvariance()` for warm starts (defaults come from a `clogit` conditional-logit fit). Convergence is monitored informally via a running log-posterior choice-probability statistic `ln_fc(p)`.

The WTP-space variant follows Train & Weeks (2005), Scarpa, Thiene & Train (2008), and [[@Hole2012|Hole & Kolstad (2012)]]. It normalizes coefficients by the (random) price coefficient so that estimates are read directly as money-metric marginal WTP. The price coefficient is modeled as the negative of a log-normal: if the sampled parameter is $b$, the implied price coefficient is $-\exp(b)$, guaranteeing the correct (negative) sign and a positive-support WTP distribution. A caution is flagged: the reported transformed coefficient is $-\exp(\bar b)$ (negative exponentiated mean), not the mean of $-\exp(b)$, so it is not the posterior mean of the price coefficient.

## Data

No original empirical data. The paper uses standard distributed teaching datasets to demonstrate syntax: Stata's `choice.dta` (885 obs, car-nationality choices), `bangladesh.dta` (contraceptive choice, 3,868 obs across 60 districts), the NLS `union.dta` (52,400 obs), and Hole's `traindata.dta` (electricity-supplier choice, 4,780 obs, used for the WTP examples, with thanks to Arne Rise Hole). Data must be in long/case-by-alternative format (as for `clogit`); the helper `case2alt` from `spost9_ado` reshapes case-level data into the required form.

## Key findings

There are no theorems; the "findings" are demonstrations that the estimator runs and recovers sensible posteriors. Across the examples the random coefficients show economically meaningful posterior dispersion: e.g., in the Bangladesh model the urban indicator has a large positive mean and substantial variance, confirming preference heterogeneity. The WTP-space `traindata` example returns a transformed price coefficient of $-0.779$ (all-random version: $-0.520$) and lets the user histogram the posterior draws of the price parameter directly. The examples also show practical workflow: saving population draws (`saving()`), saving individual-level random-parameter draws (`indsave()`, with `indkeep()`/`indwide` to manage memory and layout), recovering individual posterior means by group, and kernel-density plotting the empirical distribution of an individual-level coefficient. A recurring caveat is printed by the command itself: the regression-style table reports summary statistics of posterior draws conforming to Stata convention, not point estimates, and should be interpreted as such.

## Contribution

Provides a documented, openly available Bayesian estimator for mixed logit and WTP-space mixed logit inside Stata, complementing Hole's (2007) maximum-simulated-likelihood `mixlogit`/`mixlogitwtp`. The contribution is one of accessibility and reproducibility: it packages adaptive MCMC (Baker 2014) behind a familiar `clogit`-style interface, exposes sampler tuning to the user, and stores both population- and individual-level draws for downstream analysis.

## Limitations & open questions

The command leaves convergence diagnostics largely to the user — only an informal log-posterior drift indicator `ln_fc(p)` is provided, with no built-in Gelman–Rubin, effective-sample-size, or trace tooling. Priors are fixed (diffuse mean, identity inverse-Wishart on $\Sigma$) with no user control, so prior sensitivity is unexplored. Saving individual-level parameters can exhaust memory in large panels, forcing a two-pass warm-start workflow. The WTP reporting convention ($-\exp(\bar b)$ vs the posterior mean of $-\exp(b)$) is a known source of misinterpretation. Open practical questions: how to choose between the `global` and `mwg` samplers in general; how robust the inverse-Wishart prior is for high-dimensional covariance matrices; and how to systematize convergence assessment for these models.

## Connections

The estimator is the Bayesian counterpart to the maximum-simulated-likelihood mixed logit of [[@Hole2007|Hole (2007)]], both descending from the canonical treatment in Train (2009). The WTP-space formulation traces to Train & Weeks (2005), with applications and comparisons in Scarpa, Thiene & Train (2008) and [[@Hole2012|Hole & Kolstad (2012)]]. The MCMC engine is the author's own Baker (2014), and the Bayesian framework follows Gelman, Carlin, Stern & Rubin (2009); the data-handling examples lean on Long & Freese (2006). It connects to any analysis using random-coefficients logit to recover individual-level taste distributions, and to willingness-to-pay estimation in stated- and revealed-preference choice experiments.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
