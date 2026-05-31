---
slug: econometrics-machine-learning
title: "Econometrics & Machine Learning"
type: area
scope: "Structural choice estimation, latent heterogeneity, and ML for prediction and theory evaluation."
tags: [area]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This area collects the quantitative machinery economists use to turn observed choices into estimated preferences and out-of-sample predictions — and the meta-methodology for judging when a model has earned its complexity. It spans the parametric random-utility toolkit ([[discrete-choice-econometrics|Discrete-Choice Econometrics & Mixed Logit]]), the latent-structure estimators that sit beneath it ([[finite-mixture-models|Finite Mixture Models & Latent Heterogeneity]]), two prediction-first programs that pit theory against flexible learners ([[ml-evaluating-economic-theories|ML for Evaluating Economic Theories]], [[choice-prediction-risky-choice|Predicting Risky Choice]]), and the pure-ML latent-factor apparatus imported from recommendation ([[recommender-systems-matrix-factorization|Recommender Systems & Matrix Factorization]]). Together they form a single pipeline — specify a utility/likelihood, recover heterogeneity, predict held-out choice, and benchmark the result against a black-box ceiling — repeatedly cut by the same trade-off between fit and interpretable, identified structure.

## Sub-areas / themes

**Estimation core — recovering structured preferences.**
- [[discrete-choice-econometrics|Discrete-Choice Econometrics & Mixed Logit]] — the RUM workhorse: multinomial/nested/mixed logit, MSL/MCMC, WTP, and substitution patterns from observed selections.
- [[finite-mixture-models|Finite Mixture Models & Latent Heterogeneity]] — the EM/model-based-clustering layer that supplies discrete latent types (preference classes) and the unsolved problem of choosing how many.

**Prediction-as-yardstick — theory vs. the black box.**
- [[ml-evaluating-economic-theories|ML for Evaluating Economic Theories]] — uses flexible predictors as diagnostic instruments (completeness, restrictiveness, anomaly generation) to score how much of behavior a structural model misses.
- [[choice-prediction-risky-choice|Predicting Risky Choice]] — the choice-prediction-competition tradition and hybrid theory+ML models (BEAST, psychological forest, differentiable decision theory) judged on out-of-sample MSD/ENO.

**Imported machinery — latent factors at scale.**
- [[recommender-systems-matrix-factorization|Recommender Systems & Matrix Factorization]] — collaborative filtering, matrix completion, and factorization machines: the low-rank, large-$N$ prediction technology economists are beginning to borrow for sparse choice panels.

## Cross-topic tensions

**The field-defining tension is fit versus identified structure — "predicts well" and "recovers the economics" are not the same claim, and the gap recurs in every topic.** Mixed logit can approximate any RUM yet fail to recover a deep CRRA $r$ or discount $\delta$ ([[discrete-choice-econometrics|discrete-choice]]); matrix factorization scales linearly but minimizes a non-convex objective with no recovery guarantee, while the convex estimator that *is* guaranteed ([[recommender-systems-matrix-factorization|Candès–Recht]]) does not scale ([[recommender-systems-matrix-factorization|recommender systems]]); and the completeness program ([[ml-evaluating-economic-theories|ML-for-theories]]) measures fit-to-ceiling while restrictiveness measures empirical content — two virtues that, on a non-concave frontier, cannot be collapsed into one criterion.

**Does out-of-sample prediction even adjudicate?** The two prediction programs disagree with the estimation core on whether held-out accuracy is the right loss. [[choice-prediction-risky-choice|Choice-prediction]] makes predictive MSD the verdict — yet [[discrete-choice-econometrics|discrete-choice]] finds richer heterogeneity can *lower* out-of-sample accuracy (mixed logit beaten by plain MNL), and [[ml-evaluating-economic-theories|ML-for-theories]] shows the black box that *sets* the in-domain ceiling **transfers worse** than CPT/EU once the domain shifts — so the object used to score completeness is the one that fails generalization.

**When does latent heterogeneity earn its keep, and how much is there?** [[finite-mixture-models|Finite mixtures]] concede there is no agreed method for choosing the number of components $g$ — the LRT loses its $\chi^2$ asymptotics, BIC over-splits, ICL and CV can disagree — and that indeterminacy propagates directly into [[discrete-choice-econometrics|latent-class logit]] and the type-mixtures used to predict risky choice ([[choice-prediction-risky-choice|Bruhin-style $C=2$ vs $3$]]).

**Data scale governs who wins.** Engineered behavioral features encode priors that substitute for data: they dominate at small $N$ in [[choice-prediction-risky-choice|CPC]] but lose to near-unconstrained nets as $N\to\infty$ ([[ml-evaluating-economic-theories|black-box ceiling]], [[recommender-systems-matrix-factorization|FM scaling]]) — the same Bayesian-vs-point-estimate, regularization-tuning story that makes published leaderboards unreliable ([[recommender-systems-matrix-factorization|Rendle et al.]]).

## Open questions

- Is there a principled **identification floor** — sufficiency conditions for population RUM consistency, an information-theoretic completion bound, a calibrated rule for $g$ — that the whole estimation core currently lacks?
- How much measured **irreducible error** is genuine noise versus recoverable structure (better grouping, response times, latent types) — the floor in completeness, the indeterminate $g$ in mixtures, and the "predict the average DM" ceiling in CPC all turn on the same unknown?
- Can prediction be scored on a **single defensible loss** (the DBBD family, strictly-proper Brier, transfer-completeness) so that completeness numbers and competition rankings are comparable across papers and domains?
- Does the **scale crossover** $N^\*$ where theory's edge flips to ML's exist universally, and can structured (factorization/embedding) heterogeneity succeed in prediction where the variance-only mixed-logit level failed?
- Can **latent-factor and process-level evidence** (eye-tracking, response times, side information) be folded into identified structural estimators rather than bolted on as features?

## Topics
```dataview
TABLE scope AS Scope
FROM "topics"
WHERE area = this.file.link
SORT file.name ASC
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
