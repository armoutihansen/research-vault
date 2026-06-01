---
slug: discrete-choice-econometrics
title: "Discrete-Choice Econometrics & Mixed Logit"
type: topic
scope: "Random-utility discrete-choice estimation: multinomial/nested/mixed logit, maximum simulated likelihood, WTP, and software."
area: "[[econometrics-machine-learning]]"
tags: [topic]
created: 2026-05-31
generated: 2026-06-01
---

## Scope

This topic covers the random-utility-maximization (RUM) toolkit for estimating discrete choice from observed selections: the conditional/multinomial, nested, and mixed (random-parameters) logit families, their identification, the maximum-simulated-likelihood (MSL) and Bayesian-MCMC machinery that makes them estimable, and the willingness-to-pay (WTP) and individual-prediction quantities they deliver. The unifying research question is how to recover a *population* distribution of tastes — and the substitution patterns it implies — from discrete selections among finite alternative sets, when the analyst observes only some attributes and idiosyncratic tastes vary. Its boundary is *parametric, choice-data-driven* estimation of taste parameters and substitution patterns; it abuts but excludes the axiomatic foundations of stochastic choice (limited to the identification debate here) and pure prediction-competition work, which live in neighboring topics.

## Sub-themes

- **The conditional-logit root and RUM foundations** — McFadden (1972) is the historical seed of the whole topic: it derives the conditional (multinomial) logit form $P(x\mid s,B)=e^{v(s,x)}/\sum_{y\in B}e^{v(s,y)}$ from behavioral axioms (IIA, positivity), proves it is exactly the population choice probability when idiosyncratic taste shocks are i.i.d. type-I extreme value (essentially the *only* such error law), establishes a globally concave log-likelihood with ML existence/uniqueness/efficiency results, and already flags the IIA red-bus/blue-bus failure and the nested "inclusive-price" idea. McFadden (1981) and McFadden (1979) then build discrete choice up from a probabilistic choice system, the strong axiom of revealed stochastic preference, the Williams–Daly–Zachary social-surplus theorem, and the GEV/nested-logit family that relaxes IIA while keeping a closed form. McFadden (2000) interrogates how much of the RUM rationality assumption survives the behavioral evidence.
- **Mixed logit / random coefficients** — Revelt & Train (1998) establish the panel/repeated-choices likelihood; Andersen et al. (2012) push the latent index from linear to a non-linear structural function (CRRA, discounting); Hole (2007) and Croissant (2020) document the workhorse estimators.
- **Individual-level recovery and WTP** — Revelt & Train (2000) condition population draws on a person's history to recover individual tastes; Hole & Kolstad (2012) and Baker (2023) contrast preference-space vs. WTP-space parameterizations.
- **Simulation and computation** — Drukker & Gates (2006) on Halton/Hammersley low-discrepancy draws; Arteaga et al. (2022) on GPU-accelerated MSL; Baker (2023) on Bayesian adaptive-MCMC as the alternative to maximum simulated likelihood.
- **Heterogeneity vs. prediction, and identification under noise** — Krueger et al. (2021) and Zhao et al. (2020) ask whether richer heterogeneity or flexible ML actually improves out-of-sample choice; Alós-Ferrer, Fehr & Netzer (2021) confront the non-identification of preferences from stochastic choice alone.

## Cross-paper tensions

The deepest tension is present at the **birth** of the topic and never resolved. McFadden (1972) buys tractability and a clean structural utility interpretation by imposing IIA — and immediately exhibits its failure (red-bus/blue-bus: adding an identical bus wrongly steals share from auto). Every later member is, in effect, a different bargain against that founding restriction: McFadden (1981)/McFadden (1979) relax IIA *parametrically* via GEV/nested logit (closed form, but the analyst must pre-specify the nesting tree); Revelt & Train (1998) and Hole (2007) relax it via *random coefficients* (no tree, but an intractable integral and an assumed mixing distribution); Alós-Ferrer, Fehr & Netzer (2021) show that relaxing it at all reopens an identification hole McFadden (1972) closed only by assuming a *single, symmetric* extreme-value error law. The topic is the history of trading McFadden's IIA away and paying for it elsewhere.

The defining methodological tension is **flexible taste heterogeneity vs. interpretable structural recovery**. Revelt & Train (1998) and Hole (2007) recover only *reduced-form* random coefficients; Andersen et al. (2012) show the McFadden–Train approximation theorem runs one way only — any RUM is approximable by a *linear* mixed logit, but that linear model does not recover deep parameters (a CRRA $r$ or discount rate $\delta$), which require an explicit non-linear index $U_{njt}=G(\beta_n,x_{njt})+\varepsilon_{njt}$. So "fits the data" and "recovers the economics" are not the same claim — a distinction already latent in McFadden (1972)'s insistence that logit coefficients carry a *structural* utility reading.

A sharper, *empirical* tension: **does heterogeneity earn its keep in prediction?** Revelt & Train (2000) argue conditioning on individual histories roughly halves prediction error; but Krueger et al. (2021) show — with a strictly proper Brier score and a correct conditional-vs-conditional comparison — that adding an *intra*-individual heterogeneity level buys at most $0.003$ in Brier score at $\geq 7\times$ the compute, and Zhao et al. (2020) find mixed logit actually predicts *worse out of sample than plain MNL* (0.631 vs 0.647 accuracy) despite a far higher pseudo-$R^2$ — overfitting from the random parameters. Flexibility that raises in-sample likelihood, or relaxes the parsimonious McFadden (1972) baseline, can degrade genuine prediction.

A **parameterization tension**: Hole & Kolstad (2012) show preference-space models fit slightly better yet manufacture implausible, heavy-tailed WTP (a ratio-of-normals with no moments), while WTP-space estimation yields moderate WTP at negligible fit cost — so the "better-fitting" model gives worse economics, echoing the Andersen tension at the level of derived quantities. Baker (2023) adds that even *reporting* WTP is ambiguous: its transformed price coefficient $-\exp(\bar b)$ is not the posterior mean of $-\exp(b)$, so the headline number is not the posterior mean it looks like.

An **identification tension** sits beneath all of it, and it now reaches all the way back to the founder. McFadden (1972) closed the gap by *assuming* i.i.d. extreme-value errors (and proving them essentially unique given IIA); McFadden (1981) then flagged that no general *sufficiency* (integrability) conditions exist for population RUM consistency, and Alós-Ferrer, Fehr & Netzer (2021) make it bite — within the class of all RUMs, choice frequencies reveal *nothing* about preference order without untestable noise-distribution assumptions ($p(x,y)>1/2$ is consistent with $u(x)<u(y)$). Their response-time remedy implies the entire mixed-logit edifice rests on an identifying symmetry/Fechnerian assumption that is, in 39% of their problems, *falsified*. Finally, McFadden (2000) questions whether the stable preferences the whole program estimates even exist, while a computational tension (Drukker & Gates (2006) vs Arteaga et al. (2022)) pits draw *quality* (Halton breaks down past ~10 dimensions) against draw *quantity* (GPU MSL at 500,000 draws).

## Open questions

- **Sufficiency conditions for population RUM.** McFadden (1981) has no practical sufficient condition for an observed choice distribution to be RUM-consistent — a gap McFadden (1972) sidestepped only by assuming a specific (extreme-value) error law; Alós-Ferrer, Fehr & Netzer (2021) characterize rationalizability only for special model classes, leaving the general $>2$-option case open.
- **How much does relaxing IIA actually cost, and is the bargain worth it?** McFadden (1972) makes IIA explicit and falsifiable (the red-bus/blue-bus diagnostic); McFadden (1979) sketches but does not fully develop the McFadden–Tye–Train tests of IIA validity. When does the heterogeneity or nesting that relaxes IIA help enough to justify the lost concavity, identification, and out-of-sample stability documented by Krueger et al. (2021) and Zhao et al. (2020)?
- **Which mixing distribution?** Normality forces wrong-sign coefficients and non-satiating tails; the bounded Beta4 (Andersen et al. 2012) and lognormal (Hole 2007) are partial fixes. No decision rule exists for the "true" distribution (Hole & Kolstad 2012).
- **When does conditioning help?** Revelt & Train (2000) note it fails on new tradeoffs or omitted attributes; Krueger et al. (2021) ask whether the null heterogeneity result survives *external* (cross-time/region) validation.
- **Behavioral soundness of ML choice models.** Zhao et al. (2020) leave open how to impose behavioral constraints so flexible learners yield credible elasticities/VOT, and whether their divergent estimates are noise or ground truth.
- **High-dimensional simulation.** Drukker & Gates (2006) leave the $d>10$ Halton crossover a conjecture and call for better low-discrepancy sequences; Arteaga et al. (2022) note Probit/nested/latent-class coverage and the RAM ceiling remain unsolved.
- **Bayesian convergence and priors.** Baker (2023) supplies only an informal log-posterior drift indicator, no Gelman–Rubin/ESS tooling, and a fixed diffuse mean / identity inverse-Wishart prior whose sensitivity in high-dimensional covariance is unexplored.

## Candidate ideas

- **A unified IIA-relaxation cost ledger.** McFadden (1972) makes IIA explicit and falsifiable but every relaxation pays a price; assemble (theory + existing-data) a single benchmark that, on the shared datasets bundled with Croissant (2020), Hole (2007), and Arteaga et al. (2022), maps for each IIA-relaxation route — nested/GEV (McFadden 1981/1979), random coefficients (Revelt & Train 1998), intra-individual heterogeneity (Krueger et al. 2021) — the gain on a proper scoring rule against the cost in concavity loss, compute, and out-of-sample stability. Feasible with existing data; the contribution is the like-for-like ledger nobody has built.
- **Response-time-augmented mixed logit.** Fold the chronometric identification of Alós-Ferrer, Fehr & Netzer (2021) into the MSL estimator of Hole (2007)/Revelt & Train (1998) to relax the symmetry/extreme-value assumption that McFadden (1972) proved unique *only given IIA* — turning the silently-imposed noise law into something testable. Theory + simulation, then existing RT-choice datasets.
- **Structured beats unstructured heterogeneity, tested properly.** Pit matrix-factorization / embedding utilities against intra-individual mixed logit on the Brier-score, conditional-prediction protocol of Krueger et al. (2021) — does *structured* dependence succeed where the variance-only level failed? Existing-data only.
- **Non-linear structural mixed logit for social preferences.** Apply the Andersen et al. (2012) non-linear-index approach to recover deep distributional/reciprocity parameters with bounded (Beta4) heterogeneity, ported to GPU MSL (Arteaga et al. 2022) for routine estimation — bridging the founding structural reading of McFadden (1972) to modern social-preference data. Theory + simulation + existing experimental data.
- **WTP-space as default, with a Bayesian honesty check.** Build the Hole & Kolstad (2012) preference- vs. WTP-space comparison and the Baker (2023) $-\exp(\bar b)$-vs-posterior-mean caveat into one automated sensitivity wrapper that flags ratio-of-randoms pathologies and reports the *correct* posterior WTP moment. Existing-data / software; low-hanging fruit with immediate applied value.
- **Better high-dimensional draws inside GPU MSL.** Benchmark scrambled/randomized-QMC and lattice sequences against the large-prime-correlated Halton failure (Drukker & Gates 2006) inside the GPU estimator of Arteaga et al. (2022) for many-alternative models, closing the draw-quality-vs-quantity gap. Theory + simulation.

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
