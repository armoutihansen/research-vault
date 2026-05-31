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
keywords: [mixed-logit, bayesian-estimation, discrete-choice, mcmc, willingness-to-pay, stata]
topics: ["[[discrete-choice-econometrics]]"]
related: [Hole2007, Hole2012]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> This document presents an overview of the bayesmixedlogit and bayesmixedlogitwtp Stata packages. It mirrors closely the helpfile obtainable in Stata (i.e., through help bayesmixedlogit or help bayesmixedlogitwtp). Further background for the packages can be found in Baker (2014).

## Summary
This is a software-documentation preprint (an arXiv mirror of the Stata helpfiles) for two user-written Stata commands, `bayesmixedlogit` and its wrapper `bayesmixedlogitwtp`. The commands fit mixed (random-coefficients) logit discrete-choice models by Bayesian MCMC rather than by maximum simulated likelihood. The document explains the estimation approach (drawing from the posterior over individual-level and population parameters via adaptive Metropolis-Hastings and Gibbs steps), enumerates every command option, and walks through five worked examples on standard Stata datasets, including a willingness-to-pay (WTP) space variant. It is a usage reference, not a research contribution; methodological derivations live in Baker (2014, *Stata Journal*) and Train (2009, ch. 12).

## Research question
Not a hypothesis-driven paper. The practical question it answers is: how can an applied researcher estimate a mixed logit model in Stata using Bayesian (posterior-simulation) methods, recover both population-level moments of the random coefficients and individual-level coefficient draws, and optionally express results in WTP space rather than preference space?

## Method / identification
The underlying model is the mixed (random-parameters) logit. Each decision maker $i$ on choice occasion $t$ picks alternative $j$ to maximise utility $U_{ijt}=\beta_i' x_{ijt}+\varepsilon_{ijt}$, with $\varepsilon_{ijt}$ i.i.d. extreme value, giving the conditional logit choice probability
$$ p(j\mid i,t)=\frac{\exp(\beta_i' x_{ijt})}{\sum_{k}\exp(\beta_i' x_{ikt})}. $$
The individual coefficient vector is heterogeneous, $\beta_i\sim N(b,\Sigma)$, where some elements may instead be fixed (common) across people. Estimation follows the hierarchical-Bayes scheme in Train (2009, ch. 12). A diffuse (flat) prior is placed on the population mean $b$ of the random coefficients, and an inverse-Wishart prior with an identity scale is placed on the covariance $\Sigma$. The posterior is sampled by alternating Gibbs-type steps: draws of the population mean and covariance conditional on the individual $\beta_i$, draws of the individual-level $\beta_i$ via Metropolis-Hastings (the choice-probability likelihood has no conjugate form), and a separate step for any fixed coefficients. Sampling of individual-level and fixed coefficients uses adaptive MCMC via the companion Mata routine `amcmc()` (Baker 2014): the proposal scale is tuned online toward a target acceptance rate (default $0.234$), governed by a damping parameter that controls how aggressively early proposals adapt. The proposal for the random block can be drawn jointly (`samplerrandom(global)`) or one parameter at a time as nested Metropolis-within-Gibbs (`mwg`), which helps when starting values are poorly scaled. Standard MCMC controls are exposed: number of draws (default 1000), burn-in, thinning (keep every $k$th draw), and `jumble` (random reordering) to mitigate autocorrelation. Default starting values come from a `clogit` (conditional logit) fit; users may pass their own mean vector and covariance. Output is reported in Stata coefficient-table format, but the displayed numbers are posterior summary statistics of the draws, not point estimates — the paper repeatedly flags this. The WTP variant `bayesmixedlogitwtp` is a thin wrapper that normalises coefficients by a designated (random) price coefficient, following Train and Weeks (2005), Scarpa, Thiene and Train (2008), and [[@Hole2012|Hole and Kolstad (2012)]]. The price coefficient is parameterised as the negative of a log-normal: if the sampled parameter is $b$, the price coefficient is $-\exp(b)$, so the remaining coefficients are interpreted directly as willingness-to-pay amounts.

## Data
None of the author's own. The five examples run on shipped/teaching datasets: Stata's `choice.dta` (car-nationality choice, 885 obs / 295 groups), the Bangladesh Fertility Survey contraceptive-choice data (`bangladesh.dta`, with `case2alt` reshaping), the NLS `union.dta` panel (52,400 obs / 4,434 women), and Hole's `traindata.dta` electricity-supplier WTP example (4,780 obs / 100 groups). Data layout mirrors `clogit`/`mixlogit` ([[@Hole2007|Hole 2007]]): `group()` marks choice occasions and `identifier()` marks the person whose coefficients are shared across occasions.

## Key findings
There are no theorems or empirical results in the scientific sense — this is documentation. The substantive content is the command's capabilities and behaviour. Notable points an applied user should take away: (i) the estimator produces full posterior draws, so the user, not the command, performs detailed inference (e.g. kernel-density plots of individual-level coefficient means by group); (ii) individual-level draws can be saved (`indsave`, `indkeep`, `indwide`), but the documentation explicitly warns this is memory-intensive for large panels and many draws, recommending a long unsaved first run followed by a short second run seeded with `from()`/`fromvariance()` to harvest individual parameters; (iii) convergence has no formal objective function, but the author notes drift in the joint log posterior-probability value `ln_fc(p)` signals non-convergence; (iv) the WTP-space output displays the transformed price coefficient as $-\exp(\bar b)$ (the negative exponentiated mean of $b$), which is deliberately distinct from the mean of $-\exp(b)$ — a subtle but important caveat for interpretation. The worked WTP example recovers a transformed price coefficient of about $-0.78$ in one specification and $-0.52$ in another.

## Contribution
Provides accessible, citable documentation for Bayesian estimation of mixed logit models within Stata, lowering the barrier for applied choice modellers who want a hierarchical-Bayes alternative to maximum simulated likelihood (`mixlogit`). It packages adaptive MCMC (`amcmc`), individual-level posterior recovery, and a WTP-space reparameterisation behind a `clogit`-compatible syntax.

## Limitations & open questions
The document is explicit on several practical limitations that double as caveats / extension hooks: (a) no built-in convergence diagnostic beyond watching `ln_fc(p)` drift — formal diagnostics (e.g. Gelman-Rubin, effective sample size) are left to the user; (b) memory pressure when saving individual-level parameters for large $N$ or long chains, with a manual two-run workaround rather than an automated solution; (c) priors are fixed by design — a diffuse prior on means and an identity inverse-Wishart on the covariance — with no user-facing hyperparameters to override them; (d) all random coefficients are normal (the WTP price coefficient is the only non-normal, log-normal, case), so richer mixing distributions are not supported; (e) the WTP transformed coefficient reports $-\exp(\bar b)$ rather than the posterior mean of $-\exp(b)$, leaving correct WTP-distribution summarisation to post-processing of the saved draws. These point toward extensions: flexible priors, alternative coefficient distributions, automated convergence checks, and built-in WTP-distribution summaries.

## Connections
The methodological backbone is Train (2009, *Discrete Choice Methods with Simulation*, ch. 12) for hierarchical Bayes mixed logit and Baker (2014, *Stata Journal*) for the adaptive-MCMC `amcmc` engine and algorithmic details. Syntax and data setup follow [[@Hole2007|Hole (2007)]], whose `mixlogit` fits the same model by maximum simulated likelihood — `bayesmixedlogit` is the Bayesian sibling. The WTP-space formulation draws on Train and Weeks (2005) and Scarpa, Thiene and Train (2008) on preference- versus WTP-space parameterisation, and on [[@Hole2012|Hole and Kolstad (2012)]], who compare preference- and WTP-space models in a health choice experiment. Gelman et al. (2009, *Bayesian Data Analysis*) supplies the inverse-Wishart prior conventions, and Long and Freese (2006) the `case2alt` data-reshaping used in the examples. In a research-vault context this note is primarily a methods/tooling reference for discrete-choice and stated-preference work rather than a substantive empirical source.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
