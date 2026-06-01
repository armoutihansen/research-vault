---
slug: choice-prediction-risky-choice
title: "Predicting Risky Choice: Competitions & Hybrid Models"
type: topic
scope: "Choice-prediction competitions and hybrid theory+ML models (BEAST, psychological forest, differentiable decision theory) for decisions under risk and from experience."
area: "[[econometrics-machine-learning]]"
tags: [topic]
created: 2026-05-31
generated: 2026-06-01
---

## Scope

This topic covers the program that judges descriptive theories of decisions under risk by their **out-of-sample predictive accuracy** rather than by axioms or in-sample fit — the choice-prediction-competition (CPC) tradition and the hybrid theory+ML models it spawned (BEAST, psychological forest, differentiable decision theory, BEAST-Net). The unit of study is choice between monetary lotteries, both from description and from experience/feedback, scored by mean squared deviation, the Equivalent Number of Observations (ENO), and — increasingly — a *completeness* score that benchmarks a model against a non-parametric estimate of the irreducible error. The boundary: it is about *predicting* aggregate or individual risky choice and the rival model classes that compete to do so, not about the axiomatic foundations of any single theory (those live in prospect-theory and non-EU topics) nor about the general completeness/restrictiveness machinery (that lives in the ML-for-evaluating-theories topic, here used only as a yardstick — though Fudenberg, Kleinberg, Liang & Mullainathan (2019) is now a multi-homed member because its lead application *is* certainty-equivalent prediction).

## Sub-themes

- **The competition infrastructure and the description–experience gap.** Erev et al. (2010) establish the generalization-criterion competition and ENO, documenting that rare events are overweighted from description but underweighted from experience — best predicted by different model classes. Erev et al. (2017) collapse 14 anomalies into one 11-dimensional task space and the BEAST process model, claiming the gap is quantitative, not qualitative.
- **Hybrid feature-engineering (theory → features → generic learner).** Noti et al. (2016) (SVM on PT/CPT features), Plonsky et al. (2017) (psychological forest), Plonsky et al. (2018) (CPC18 design), and Plonsky et al. (2019) (insight/foresight decomposition) all feed theory-derived features into random forests/XGBoost.
- **Differentiable / "white-box" theory.** Peterson et al. (2021) re-implement EV/EU/PT/CPT as constrained neural nets on a 9,831-problem dataset (Mixture-of-Theories); Shoshan et al. (2023) make BEAST itself differentiable (BEAST-Net) to recover interpretable parameters.
- **The completeness yardstick.** Fudenberg, Kleinberg, Liang & Mullainathan (2019) supply the scalar that several members now report: completeness $\kappa = (e^{\text{naive}} - e^{\text{model}})/(e^{\text{naive}} - e^{*})$, where the irreducible error $e^{*}$ is estimated by non-parametric Table Lookup. Their headline risk result — CPT is **95% complete** for certainty equivalents on the two-outcome Bruhin et al. (2010) lotteries — is the description-side counterpart of the CPC "theory is near-indispensable" finding, and the metric is exactly the "ML completeness score" used by Fudenberg & Puri (2021) and Fudenberg & Puri (2022).
- **Heterogeneous-agent structural prediction.** Bruhin et al. (2010) (finite-mixture EUT/CPT types) and Fudenberg & Puri (2021) / Fudenberg & Puri (2022) (CPT-simplicity mixtures) predict certainty equivalents out-of-sample, benchmarked against the ML/completeness ceiling of Fudenberg et al. (2019).
- **Process-level constraints on the prediction target.** Arieli, Ben-Ami & Rubinstein (2011) use eye-tracking to show choice deliberation is often componentwise, not holistic EU integration — challenging the valuation primitive every predictor assumes.

## Cross-paper tensions

The central fault line is **engineered behavioral structure vs. theory-free learning**. In CPC15, Plonsky et al. (2017) and Noti et al. (2016) show pure ML on raw parameters is badly beaten (the best feature-free learner is ~61% worse than the CPC winner), and Plonsky et al. (2019) report the only theory-free submission ranked 16th. Yet Peterson et al. (2021), with a dataset 30× larger, *reverse* the verdict: BEAST fails to beat plain PT and leads only in the small-data regime, and a near-unconstrained context-dependent net sets the predictive ceiling. The tension is thus not "theory vs. ML" but **data scale** — engineered features encode priors that substitute for data, so they win exactly where $N$ is small and lose as $N\to\infty$. Fudenberg et al. (2019) reframe this debate rather than resolve it: their completeness metric makes the "ceiling" explicit (Table Lookup approximates $e^{*}$), and the 95%-complete CPT result says that *on two-outcome description lotteries* there is almost no room left for any model — so the scale debate is really about whether richer problem spaces (more outcomes, experience, context) open up the incompleteness that the context-dependent net of Peterson et al. (2021) exploits. The two camps still use different datasets, elicitation (binary choice from experience vs. certainty equivalents from description), and targets (block-level B-rates vs. CEs), so the crossover is unadjudicated.

A second tension concerns **what completeness even measures, and against whose benchmark**. Fudenberg et al. (2019) estimate $e^{*}$ by Table Lookup, which needs discrete features and many observations per unique feature vector — a precondition the two-outcome Bruhin et al. (2010) data satisfy but which *fails* in the multi-outcome regime of Fudenberg & Puri (2021) (6 outcomes, few lotteries per cell). There, Fudenberg & Puri (2021) and Fudenberg & Puri (2022) substitute the *best ML algorithm* (k-means / gradient boosting) for $e^{*}$ in the same formula. So "93% complete" in Fudenberg & Puri (2021) and "95% complete" in Fudenberg et al. (2019) are not the same yardstick: one benchmarks against a consistent estimate of the conditional mean, the other against whatever ML happened to win on six test lotteries. The vault owner's critique of Fudenberg & Puri (2021) sharpens this: if the k-means "ML ceiling" computes a held-out subject's CE from the group mean of *other subjects in the same fold*, the benchmark is leaky and the gap is understated — putting the "near-ML completeness" claim directly at odds with the clean Table-Lookup benchmark Fudenberg et al. (2019) insist on.

A third tension is **what BEAST really is**. Erev et al. (2017) argue mental sampling needs no subjective weighting function and that the winning model is statistically indistinguishable from a dozen rivals — so the contribution is *common structure*, not a unique model. Plonsky et al. (2019) find what matters is a foresight's *resolution* (it helps even when its raw error is high; $\hat{y}$ and $1-\hat{y}$ are equally useful), implying BEAST is a good feature, not necessarily a correct process. Shoshan et al. (2023) then strip BEAST's "arbitrary auxiliary restrictions" and find its pessimism parameter is far too high for a no-loss dataset — i.e. BEAST's process commitments are partly mis-specified even where it predicts well. And the completeness lens deepens the puzzle: Fudenberg et al. (2019) show CPT is 95% complete on description CEs while Plonsky et al. (2019) show BEAST *out-predicts* (cumulative) PT on the description subset of CPC18 — two "near-complete/dominant" models with incompatible primitives winning on different datasets.

A fourth tension is **mechanism over-counting and the right notion of complexity**. Plonsky et al. (2017) show dropping BEAST's dominance treatment *improves* prediction and that only EV-sensitivity and regret matter — the six-mechanism theory reduces to two. Fudenberg & Puri (2022) go further on the description side, arguing the canonical certainty effect is confounded with **support size**: since classic experiments compare two-outcome lotteries to sure things, what looks like probability weighting may be a simplicity preference. CPT-simplicity beats CPT out-of-sample, directly contesting the weighting primitive shared by Noti et al. (2016), Peterson et al. (2021), and Bruhin et al. (2010). This collides with Fudenberg et al. (2019)'s own application: their 95%-complete CPT figure is computed on the *two-outcome* lotteries where Fudenberg & Puri (2022) say support size is held fixed and cannot be detected — so the very experiment that makes CPT look near-complete is the one that hides the simplicity confound. Fudenberg et al. (2019) anticipate this in their own language: completeness is feature-set-relative, and "support size" is exactly a *new feature* their framework says should raise the ceiling.

Finally, an **identification limit** and a **process challenge** run through the cluster. Bruhin et al. (2010) cannot identify loss aversion $\lambda$ (no mixed lotteries) and concede model size ($C=2$ vs. $3$) is genuinely indeterminate. Arieli et al. (2011) supply an orthogonal challenge: if deliberation is componentwise rather than holistic $g(p)v(x)$ integration, then *every* member's valuation primitive — including the differentiable EU/PT/CPT classes of Peterson et al. (2021) and the conditional-expectation target $f^{*}_P(x)=\mathbb{E}_P[y\mid x]$ that Fudenberg et al. (2019) treat as the prediction ideal — is a convenient fiction; yet gaze tendency does not even predict the realized choice.

## Open questions

- Does the theory-edge survive scale and richer domains? Plonsky et al. (2019) and Plonsky et al. (2018) explicitly leave open whether deep, theory-free models win once data are abundant — exactly the regime where Peterson et al. (2021) say they do, and exactly where Fudenberg et al. (2019) say the *feature set*, not the functional form, becomes the binding constraint.
- Is the "near-ML" / "95% complete" headline robust to the benchmark? Fudenberg et al. (2019) require a consistent Table-Lookup estimate of $e^{*}$; Fudenberg & Puri (2021) substitute a possibly-leaky ML ceiling on six test lotteries. The completeness denominator $e^{\text{naive}}-e^{*}$ is unmeasured in the multi-outcome regime, so it is open whether CPT-simplicity's "93%" is even on the same scale as CPT's "95%".
- What is the right notion of complexity, and is it a feature or a primitive? Fudenberg & Puri (2022) and Fudenberg & Puri (2021) note support size is one of several (irregularity, computability), and Fudenberg et al. (2019) frame "new features" as the lever once a functional form saturates — but no one has measured the completeness *gain* from adding a simplicity feature.
- Can a *simpler* model retain the ensemble/BEAST accuracy? Erev et al. (2010) and Erev et al. (2017) flag that no entrant found one and that BEAST contains post-hoc assumptions; Shoshan et al. (2023) show some of those assumptions are mis-fit.
- Individual-level prediction remains weak: CPC18's Track II is barely beaten by "predict the average DM" (Plonsky et al. (2018)), choice inertia is under-predicted by BEAST (Erev et al. (2017)), and Fudenberg et al. (2019) note their CEs are aggregate — the "what new feature raises completeness" question (subject type, response time) is their explicit open hook.
- How to fold discovered phenomena (outcome dropout, Shoshan et al. (2023)) and process evidence (Arieli et al. (2011)) back into a predictive model, and does doing so raise completeness or merely re-fit?

## Candidate ideas

- **One completeness yardstick across the whole cluster (theory / existing-data only).** Re-score every member that reports a "completeness" or "ENO" number — Fudenberg & Puri (2021), Fudenberg & Puri (2022), Plonsky et al. (2019), Peterson et al. (2021) — on a *single* benchmark, namely Fudenberg et al. (2019)'s Table-Lookup $e^{*}$ where feature vectors are discrete enough (the choices13k and CPC18 grids), and the best-ML ceiling where they are not, reporting both. This directly tests whether the "93%/95%/near-ML" claims survive a common denominator and quantifies how much of each headline is benchmark choice. Pure re-analysis of public data (Zenodo, choices13k, Bruhin CEs).
- **Settle the scale debate with completeness, not raw error (theory+simulation, existing data).** Re-run psychological forest / BEAST-Net vs. an unconstrained net on a single corpus across nested training-set sizes, but plot *completeness* $\kappa$ rather than MSE, using Fudenberg et al. (2019)'s $e^{*}$ as the fixed ceiling. The crossover $N^{*}$ where the theory-edge of Plonsky et al. (2019) flips to the ML-edge of Peterson et al. (2021) becomes the $N$ at which $\kappa_{\text{ML}}$ overtakes $\kappa_{\text{theory}}$ toward a *fixed* 100%, removing the moving-target problem of comparing two ML winners.
- **Does adding a simplicity feature raise completeness? (theory+simulation, existing data).** Fudenberg et al. (2019) say once a functional form saturates, gains require *new features*; Fudenberg & Puri (2022) propose support size as exactly such a feature. Add the Fudenberg & Puri (2021) support-size complexity cost as a foresight in the Plonsky et al. (2019) pipeline and as a Table-Lookup feature in Fudenberg et al. (2019)'s risk application, and measure the completeness increment on multi-outcome lotteries — testing where Shoshan et al. (2023) found EV-weight $w$ collapses.
- **Leakage-clean re-estimation of the structural ceiling (theory, existing data).** Redo the Fudenberg & Puri (2021) / Bruhin et al. (2010) mixture horse-race with a soft Gaussian mixture, subject-disjoint folds, and $C>3$, and recompute completeness against a *consistent* Table-Lookup $e^{*}$ in the spirit of Fudenberg et al. (2019). This tests directly whether the "near-ML" gap is real or the fold-leakage artifact flagged in the reader's critique.
- **Process-constrained predictor (theory+simulation; experiment optional).** Build a componentwise (similarity-based) valuation layer motivated by Arieli et al. (2011) and test whether it beats holistic BEAST-Net (Shoshan et al. (2023)) on the hard-to-multiply problems where componentwise gaze spikes — then ask, via Fudenberg et al. (2019)'s decomposition, whether "computational difficulty of $p\cdot x$" is a missing *feature* that raises the completeness ceiling rather than a better functional form.
- **Mechanism-pruning audit (theory+simulation, existing data).** Systematically leave-one-mechanism-out across BEAST.sd to confirm the Plonsky et al. (2017) "EV + regret suffices" reduction generalizes to CPC18 and to individual-level Track II, reporting each pruned model's completeness against the fixed Table-Lookup ceiling so a mechanism is kept only if it moves $\kappa$, not merely MSE.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Kahneman1979]] — cited by 10 members
- [[@Tversky1992]] — cited by 6 members
- [[@Fudenberg2022]] — cited by 3 members
- [[@Fudenberg2021]] — cited by 2 members
- [[@Peysakhovich2017]] — cited by 2 members
- [[@Chen2011]] — cited by 1 member
- [[@Fudenberg2020]] — cited by 1 member
- [[@Fudenberg2020a]] — cited by 1 member
- [[@Gneiting2007]] — cited by 1 member
- [[@Hartford2016]] — cited by 1 member
- [[@Kleinberg2018]] — cited by 1 member
- [[@Quiggin1982]] — cited by 1 member
- [[@Rendle2010]] — cited by 1 member
- [[@Selten1998]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
