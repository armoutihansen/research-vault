---
citekey: Baker2023
title: Using bayesmixedlogit and bayesmixedlogitwtp in Stata
authors: ["Baker, Matthew J."]
year: 2023
type: preprint
doi: 10.48550/arXiv.2302.01775
zotero: "zotero://select/library/items/7AN9KJ34"
pdf: /Users/jesper/Zotero/storage/GSEVAY87/Baker2023.pdf
tags: [literature]
keywords: [mixed-logit, bayesian-mcmc, discrete-choice, willingness-to-pay, stata-package, random-coefficients]
topics: ["[[discrete-choice-econometrics]]"]
related: [Hole2007, Hole2012]
added: 2026-06-02
generated: 2026-06-02
---

> [!abstract] Abstract
> This document presents an overview of the bayesmixedlogit and bayesmixedlogitwtp Stata packages. It mirrors closely the helpfile obtainable in Stata (i.e., through help bayesmixedlogit or help bayesmixedlogitwtp). Further background for the packages can be found in Baker(2014).

## Summary

This is a **software tutorial / package documentation**, not an empirical study. It documents two user-written Stata commands authored by Matthew J. Baker: `bayesmixedlogit`, which fits the mixed logit (random-coefficients logit) discrete-choice model by Bayesian Markov chain Monte Carlo (MCMC), and its wrapper `bayesmixedlogitwtp`, which reparameterizes the model in willingness-to-pay (WTP) space. The text mirrors the in-Stata help files and supplies the command syntax, the full option set, five worked examples, and the stored `e()` results. The algorithm's derivation appears separately in Baker (2014); this document is the user-facing companion — a practical applied reference for estimating heterogeneous-preference choice models in a Bayesian framework, not a methodological contribution. Implementation follows Train (2009, ch. 12), with the sampler built on the author's adaptive-MCMC Mata routine `amcmc()`, and data-setup conventions and much of the syntax borrowed from Hole's (2007) frequentist `mixlogit`.

## Research question

Not a research paper with a hypothesis; it is software documentation. The implicit question it answers is practical: how can an applied researcher estimate a mixed logit model (and its WTP-space variant) in Stata using Bayesian methods, which options control the MCMC sampler, and how should the output be interpreted?

## Method / identification

No empirical identification strategy. The methodological content is the **estimation algorithm** the commands implement, summarized from Baker (2014) and Train (2009, ch. 12).

The target model is the mixed logit, the workhorse for discrete choice with heterogeneous preferences: each decision-maker draws a personal coefficient vector from a population distribution, generating realistic substitution patterns and accommodating panel choice data. Rather than maximizing a simulated likelihood, `bayesmixedlogit` draws from the posterior of the parameters. A diffuse prior is placed on the means of the random coefficients and an identity inverse-Wishart prior on their covariance matrix. The sampler draws individual-level coefficients and any fixed coefficients via **adaptive MCMC** (the Mata routine `amcmc()`, installed separately via `ssc install amcmc`).

The algorithm is structured as a Gibbs sampler in which each block of random coefficients, and the block of fixed coefficients, is a Gibbs step; `drawsrandom()` and `drawsfixed()` let each step run multiple sub-draws to improve mixing on hard, high-dimensional problems. Within a block the proposal can be sampled jointly (`samplerrandom(global)`, the default) or one parameter at a time as Metropolis-within-Gibbs (`mwg`), which the document notes is more robust when initial values are poorly scaled. Adaptation tunes the proposal scale toward a target acceptance rate (`araterandom()`, default $0.234$; `aratefixed()`), governed by damping parameters (`dampparmrandom()`, `dampparmfixed()`) that set how aggressively scales adjust early in the run.

Standard MCMC controls are exposed: `burn()` discards initial draws, `thin()` retains every #th draw, and `jumble` randomly permutes draws — both aimed at autocorrelation. Starting values default to a `clogit` (conditional logit) fit unless supplied via `from()` / `fromvariance()`. The `noisy` option prints a running joint log posterior-choice-probability value `ln_fc(p)`, whose drift the author treats as an informal non-convergence signal. Output reproduces Stata's coefficient-table layout, but the recurring "Attention!" note stresses the entries are posterior summary statistics of draws, not point estimates. Population draws can be saved (`saving()`) and individual-level posterior draws via `indsave()`/`indkeep()`/`indwide`, with explicit memory-cost warnings. The data layout matches `clogit`: `group()` indexes choice occasions and `identifier()` indexes the decision-maker, so a person observed over multiple occasions has many groups but one identifier; `rand()` lists random-coefficient variables and at least one is required.

The WTP variant `bayesmixedlogitwtp` normalizes coefficients by the (random) coefficient on a designated `price()` variable, following Train and Weeks (2005), Scarpa, Thiene, and Train (2008), and [[@Hole2012|Hole and Kolstad (2012)]]. The price coefficient is assumed to be the negative of a log-normal, so if the estimated parameter is $b$ the price coefficient is $-\exp(b)$. The document flags a subtlety: the reported transformed coefficient is the negative exponentiated mean of $b$, i.e. $-\exp(\bar b)$, not the posterior mean of $-\exp(b)$.

## Data

No original data. The examples use bundled Stata teaching datasets to demonstrate syntax: `choice.dta` (885 obs, car-nationality choices), `bangladesh.dta` (contraceptive choice, 3,868 obs across 60 districts, reshaped with `case2alt`), the NLS `union.dta` (52,400 obs, women's union membership), and Hole's `traindata.dta` (electricity-supplier choice, 4,780 obs, used for the WTP examples, with thanks to Arne Rise Hole). Data must be in long case-by-alternative format as for `clogit`; the helper `case2alt` from `spost9_ado` reshapes case-level data into the required form.

## Key findings

There are no empirical findings; the "results" are illustrative outputs demonstrating the commands run and recover sensible posteriors. Across examples the random coefficients show economically meaningful posterior dispersion — e.g., in the Bangladesh model the urban indicator has a large positive mean with substantial variance, consistent with preference heterogeneity. The WTP-space `traindata` example returns a transformed price coefficient of $-0.779$ (the all-random version: $-0.520$) and lets the user histogram the posterior draws of the price parameter directly. Practical workflow takeaways:
- Bayesian mixed logit posterior summaries are obtainable with `clogit`-style data and `mixlogit`-style syntax, sidestepping maximum simulated likelihood.
- Tuning levers (acceptance-rate targets, damping, thinning, jumbling, Gibbs sub-draws, global vs. MWG samplers) give direct control over mixing and convergence on difficult problems.
- Individual-level random coefficients are recoverable and savable (e.g., recovering per-group posterior means and kernel-density plotting an individual-level coefficient), subject to memory caveats and a two-pass warm-start workflow for large panels.
- WTP-space estimation is available as a wrapper with the log-normal price transformation handled and documented.

## Contribution

The contribution is **infrastructural**: a documented, openly available Bayesian estimator for mixed logit and WTP-space mixed logit inside Stata, complementing Hole's (2007) maximum-simulated-likelihood `mixlogit`/`mixlogitwtp`. It packages the adaptive MCMC of Baker (2014) behind a familiar `clogit`-style interface, exposes sampler tuning to the user, and stores both population- and individual-level draws for downstream analysis — lowering the barrier to Bayesian discrete-choice estimation for applied economists already working in Stata.

## Limitations & open questions

As documentation rather than research, it offers no validation, benchmarking, or simulation study of estimator performance — those live in Baker (2014). Convergence diagnosis is left largely to the user via an informal `ln_fc(p)` drift heuristic, with no built-in Gelman–Rubin, effective-sample-size, or trace tooling. Priors are fixed by design (diffuse on means, identity inverse-Wishart on the covariance) with no user control, so prior sensitivity is unexplored. Saving individual-level draws can exhaust memory in large panels. The WTP reporting convention ($-\exp(\bar b)$ rather than the posterior mean of $-\exp(b)$) is a known source of misinterpretation. Open practical questions include how to choose between the `global` and `mwg` samplers in general, and how to systematize convergence assessment for these models.

## Connections

The estimator is the Bayesian counterpart to the maximum-simulated-likelihood mixed logit of [[@Hole2007|Hole (2007)]], both descending from the canonical treatment in Train (2009, ch. 12) and sharing its `clogit`-style data setup and syntax conventions. The MCMC engine is the author's own Baker (2014), which derives the adaptive MCMC sampler in Mata. The WTP-space formulation traces to Train and Weeks (2005), with applications and comparisons in Scarpa, Thiene, and Train (2008) and [[@Hole2012|Hole and Kolstad (2012)]]; the Bayesian framework follows Gelman, Carlin, Stern, and Rubin (2009), and the data-handling examples lean on Long and Freese (2006). For the broader vault this is a methods/tooling note for random-coefficient discrete choice modeling under heterogeneous preferences, relevant wherever choice modeling, willingness-to-pay estimation, or Bayesian preference-heterogeneity recovery is used.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
