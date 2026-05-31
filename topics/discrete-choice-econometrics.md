---
slug: discrete-choice-econometrics
title: "Discrete-Choice Econometrics & Mixed Logit"
type: topic
scope: "Random-utility discrete-choice estimation: multinomial/nested/mixed logit, maximum simulated likelihood, WTP, and software."
area: "[[econometrics-machine-learning]]"
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This topic covers the random-utility-maximization (RUM) toolkit for estimating discrete choice from observed selections: the multinomial, nested, and mixed (random-parameters) logit families, their identification, the maximum-simulated-likelihood (MSL) and Bayesian-MCMC machinery that makes them estimable, and the willingness-to-pay (WTP) and individual-prediction quantities they deliver. Its boundary is *parametric, choice-data-driven* estimation of taste parameters and substitution patterns; it abuts but excludes the axiomatic foundations of stochastic choice (limited to the identification debate here) and pure prediction-competition work, which live in neighboring topics.

## Sub-themes

- **RUM foundations and the GEV/nested-logit construction** — [[@McFadden1981|McFadden (1981)]] and [[@McFadden1979|McFadden (1979)]] build discrete choice from a probabilistic choice system, the strong axiom of revealed stochastic preference, the Williams–Daly–Zachary social-surplus theorem, and the GEV family that relaxes IIA while keeping a closed form. [[@McFadden2000|McFadden (2000)]] interrogates how much of the RUM rationality assumption survives the behavioral evidence.
- **Mixed logit / random coefficients** — [[@Revelt1998|Revelt & Train (1998)]] establish the panel/repeated-choices likelihood; [[@Andersen2012|Andersen et al. (2012)]] push the latent index from linear to a non-linear structural function (CRRA, discounting); [[@Hole2007|Hole (2007)]] and [[@Croissant2020|Croissant (2020)]] document the workhorse estimators.
- **Individual-level recovery and WTP** — [[@Revelt2000|Revelt & Train (2000)]] condition population draws on a person's history to recover individual tastes; [[@Hole2012|Hole & Kolstad (2012)]] and [[@Baker2023|Baker (2023)]] contrast preference-space vs. WTP-space parameterizations.
- **Simulation and computation** — [[@Drukker2006|Drukker & Gates (2006)]] on Halton/Hammersley low-discrepancy draws; [[@Arteaga2022|Arteaga et al. (2022)]] on GPU-accelerated MSL; [[@Baker2023|Baker (2023)]] on Bayesian MCMC as the alternative estimator.
- **Heterogeneity vs. prediction, and identification under noise** — [[@Krueger2021|Krueger et al. (2021)]] and [[@Zhao2020|Zhao et al. (2020)]] ask whether richer heterogeneity or flexible ML actually improves out-of-sample choice; [[@Alos-Ferrer2021|Alós-Ferrer, Fehr & Netzer (2021)]] confront the non-identification of preferences from stochastic choice alone.

## Cross-paper tensions

The defining tension is **flexible taste heterogeneity vs. interpretable structural recovery**. [[@Revelt1998|Revelt & Train (1998)]] and [[@Hole2007|Hole (2007)]] recover only *reduced-form* random coefficients; [[@Andersen2012|Andersen et al. (2012)]] show the McFadden–Train approximation theorem runs one way only — any RUM is approximable by a *linear* mixed logit, but that linear model does not recover deep parameters (a CRRA $r$ or discount rate $\delta$), which require an explicit non-linear index $U_{njt}=G(\beta_n,x_{njt})+\varepsilon_{njt}$. So "fits the data" and "recovers the economics" are not the same claim.

A sharper, *empirical* tension: **does heterogeneity earn its keep in prediction?** [[@Revelt2000|Revelt & Train (2000)]] argue conditioning on individual histories roughly halves prediction error; but [[@Krueger2021|Krueger et al. (2021)]] show — with a strictly proper Brier score and a correct conditional-vs-conditional comparison — that adding an *intra*-individual heterogeneity level buys at most $0.003$ in Brier score at $\geq 7\times$ the compute, and [[@Zhao2020|Zhao et al. (2020)]] find mixed logit actually predicts *worse out of sample than plain MNL* (0.631 vs 0.647 accuracy) despite a far higher pseudo-$R^2$ — overfitting from the random parameters. Flexibility that raises in-sample likelihood can degrade genuine prediction.

A **parameterization tension**: [[@Hole2012|Hole & Kolstad (2012)]] show preference-space models fit slightly better yet manufacture implausible, heavy-tailed WTP (a ratio-of-normals with no moments), while WTP-space estimation yields moderate WTP at negligible fit cost — so the "better-fitting" model gives worse economics, echoing the Andersen tension at the level of derived quantities. [[@Baker2023|Baker (2023)]] adds that even reporting WTP is ambiguous: $-\exp(\bar b)$ is not the posterior mean of $-\exp(b)$.

An **identification tension** sits beneath all of it: [[@McFadden1981|McFadden (1981)]] already flagged that no general *sufficiency* (integrability) conditions exist for population RUM consistency, and [[@Alos-Ferrer2021|Alós-Ferrer, Fehr & Netzer (2021)]] make it bite — within the class of all RUMs, choice frequencies reveal *nothing* about preference order without untestable noise-distribution assumptions ($p(x,y)>1/2$ is consistent with $u(x)<u(y)$). Their response-time remedy implies the entire mixed-logit edifice rests on an identifying symmetry/Fechnerian assumption that is, in 39% of their problems, *falsified*. Finally, [[@McFadden2000|McFadden (2000)]] questions whether the stable preferences the whole program estimates even exist, while a computational tension ([[@Drukker2006|Drukker & Gates (2006)]] vs [[@Arteaga2022|Arteaga et al. (2022)]]) pits draw *quality* (Halton breaks down past ~10 dimensions) against draw *quantity* (GPU MSL at 500,000 draws).

## Open questions

- **Sufficiency conditions for population RUM.** [[@McFadden1981|McFadden (1981)]] has no practical sufficient condition for an observed choice distribution to be RUM-consistent; [[@Alos-Ferrer2021|Alós-Ferrer, Fehr & Netzer (2021)]] characterize rationalizability only for special model classes, leaving the general $>2$-option case open.
- **Which mixing distribution?** Normality forces wrong-sign coefficients and non-satiating tails; the bounded Beta4 ([[@Andersen2012|Andersen et al. 2012]]) and lognormal ([[@Hole2007|Hole 2007]]) are partial fixes. No decision rule exists for the "true" distribution ([[@Hole2012|Hole & Kolstad 2012]]).
- **When does conditioning help?** [[@Revelt2000|Revelt & Train (2000)]] note it fails on new tradeoffs or omitted attributes; [[@Krueger2021|Krueger et al. (2021)]] ask whether the null heterogeneity result survives *external* (cross-time/region) validation.
- **Behavioral soundness of ML choice models.** [[@Zhao2020|Zhao et al. (2020)]] leave open how to impose behavioral constraints so flexible learners yield credible elasticities/VOT, and whether their divergent estimates are noise or ground truth.
- **High-dimensional simulation.** [[@Drukker2006|Drukker & Gates (2006)]] leave the $d>10$ Halton crossover a conjecture and call for better low-discrepancy sequences; [[@Arteaga2022|Arteaga et al. (2022)]] note Probit/nested/latent-class coverage and the RAM ceiling remain unsolved.

## Candidate ideas

- **Structured beats unstructured heterogeneity, tested properly.** Pit matrix-factorization / embedding utilities against intra-individual mixed logit on the Brier-score, conditional-prediction protocol of [[@Krueger2021|Krueger et al. (2021)]] — does *structured* dependence succeed where the variance-only level failed?
- **Response-time-augmented mixed logit.** Fold the chronometric identification of [[@Alos-Ferrer2021|Alós-Ferrer, Fehr & Netzer (2021)]] into the MSL estimator of [[@Hole2007|Hole (2007)]]/[[@Revelt1998|Revelt & Train (1998)]] to relax the symmetry assumption their noise distribution silently imposes.
- **Non-linear structural mixed logit for social preferences.** Apply the [[@Andersen2012|Andersen et al. (2012)]] non-linear-index approach to recover deep distributional/reciprocity parameters with bounded heterogeneity, ported to GPU MSL ([[@Arteaga2022|Arteaga et al. 2022]]) for routine estimation.
- **Prediction–interpretability frontier audit.** Systematize the [[@Zhao2020|Zhao et al. (2020)]] tradeoff: across datasets, map where mixed logit's overfitting ([[@Zhao2020|Zhao et al. 2020]]; [[@Krueger2021|Krueger et al. 2021]]) costs out-of-sample accuracy vs. its WTP/elasticity advantage over ML.
- **WTP-space as default.** Build the [[@Hole2012|Hole & Kolstad (2012)]] preference- vs. WTP-space comparison and the [[@Baker2023|Baker (2023)]] $-\exp(\bar b)$ caveat into an automated sensitivity-test wrapper that flags ratio-of-randoms pathologies.
- **Better high-dimensional draws.** Benchmark scrambled/randomized-QMC and lattice sequences against the large-prime-correlated Halton failure ([[@Drukker2006|Drukker & Gates 2006]]) inside GPU MSL ([[@Arteaga2022|Arteaga et al. 2022]]) for many-alternative models.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Bernheim2009]] — cited by 1 member
- [[@Bruhin2019]] — cited by 1 member
- [[@Hastie2001]] — cited by 1 member
- [[@Manzini2007]] — cited by 1 member
- [[@Manzini2014]] — cited by 1 member
- [[@Tversky1972]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
