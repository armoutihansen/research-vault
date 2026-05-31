---
slug: choice-prediction-risky-choice
title: "Predicting Risky Choice: Competitions & Hybrid Models"
type: topic
scope: "Choice-prediction competitions and hybrid theory+ML models (BEAST, psychological forest, differentiable decision theory) for decisions under risk and from experience."
area: "[[econometrics-machine-learning]]"
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This topic covers the program that judges descriptive theories of decisions under risk by their **out-of-sample predictive accuracy** rather than by axioms or in-sample fit — the choice-prediction-competition (CPC) tradition and the hybrid theory+ML models it spawned (BEAST, psychological forest, differentiable decision theory, BEAST-Net). The unit of study is choice between monetary lotteries, both from description and from experience/feedback, scored by mean squared deviation and the Equivalent Number of Observations (ENO). The boundary: it is about *predicting* aggregate or individual risky choice and the rival model classes that compete to do so, not about the axiomatic foundations of any single theory (those live in prospect-theory and non-EU topics) nor about the general completeness/restrictiveness machinery (that lives in the ML-for-evaluating-theories topic, here used only as a yardstick).

## Sub-themes

- **The competition infrastructure and the description–experience gap.** [[@Erev2010|Erev et al. (2010)]] establish the generalization-criterion competition and ENO, documenting that rare events are overweighted from description but underweighted from experience — best predicted by different model classes. [[@Erev2017|Erev et al. (2017)]] collapse 14 anomalies into one 11-dimensional task space and the BEAST process model, claiming the gap is quantitative, not qualitative.
- **Hybrid feature-engineering (theory → features → generic learner).** [[@Noti2016|Noti et al. (2016)]] (SVM on PT/CPT features), [[@Plonsky2017|Plonsky et al. (2017)]] (psychological forest), [[@Plonsky2018|Plonsky et al. (2018)]] (CPC18 design), and [[@Plonsky2019|Plonsky et al. (2019)]] (insight/foresight decomposition) all feed theory-derived features into random forests/XGBoost.
- **Differentiable / "white-box" theory.** [[@Peterson2021|Peterson et al. (2021)]] re-implement EV/EU/PT/CPT as constrained neural nets on a 9,831-problem dataset (Mixture-of-Theories); [[@Shoshan2023|Shoshan et al. (2023)]] make BEAST itself differentiable (BEAST-Net) to recover interpretable parameters.
- **Heterogeneous-agent structural prediction.** [[@Bruhin2010|Bruhin et al. (2010)]] (finite-mixture EUT/CPT types) and [[@Fudenberg2021a|Fudenberg & Puri (2021)]] / [[@Fudenberg2022a|Fudenberg & Puri (2022)]] / [[@Fudenberg2022b|Fudenberg & Puri (2022)]] (CPT-simplicity mixtures) predict certainty equivalents out-of-sample, benchmarked against an ML ceiling.
- **Process-level constraints on the prediction target.** [[@Arieli2011|Arieli, Ben-Ami & Rubinstein (2011)]] use eye-tracking to show choice deliberation is often componentwise, not holistic EU integration — challenging the valuation primitive every predictor assumes.

## Cross-paper tensions

The central fault line is **engineered behavioral structure vs. theory-free learning**. In CPC15, [[@Plonsky2017|Plonsky et al. (2017)]] and [[@Noti2016|Noti et al. (2016)]] show pure ML on raw parameters is badly beaten (the best feature-free learner is ~61% worse than the CPC winner), and [[@Plonsky2019|Plonsky et al. (2019)]] report the only theory-free submission ranked 16th. Yet [[@Peterson2021|Peterson et al. (2021)]], with a dataset 30× larger, *reverse* the verdict: BEAST fails to beat plain PT and leads only in the small-data regime, and a near-unconstrained context-dependent net sets the predictive ceiling. The tension is thus not "theory vs. ML" but **data scale** — engineered features encode priors that substitute for data, so they win exactly where $N$ is small and lose as $N\to\infty$. This is the sharpest disagreement in the cluster, and it is not yet adjudicated because the two camps use different datasets, elicitation (binary choice from experience vs. certainty equivalents from description), and targets (block-level B-rates vs. CEs).

A second tension concerns **what BEAST really is**. [[@Erev2017|Erev et al. (2017)]] argue mental sampling needs no subjective weighting function and that the winning model is statistically indistinguishable from a dozen rivals — so the contribution is *common structure*, not a unique model. [[@Plonsky2019|Plonsky et al. (2019)]] find what matters is a foresight's *resolution* (it helps even when its raw error is high; $\hat{y}$ and $1-\hat{y}$ are equally useful), implying BEAST is a good feature, not necessarily a correct process. [[@Shoshan2023|Shoshan et al. (2023)]] then strip BEAST's "arbitrary auxiliary restrictions" and find its pessimism parameter is far too high for a no-loss dataset — i.e. BEAST's process commitments are partly mis-specified even where it predicts well.

A third tension is **mechanism over-counting**. [[@Plonsky2017|Plonsky et al. (2017)]] show dropping BEAST's dominance treatment *improves* prediction and that only EV-sensitivity and regret matter — the six-mechanism theory reduces to two. [[@Fudenberg2022a|Fudenberg & Puri (2022)]] go further on the description side, arguing the canonical certainty effect is confounded with **support size**: since classic experiments compare two-outcome lotteries to sure things, what looks like probability weighting may be a simplicity preference. CPT-simplicity beats CPT out-of-sample, directly contesting the weighting primitive shared by [[@Noti2016|Noti et al. (2016)]], [[@Peterson2021|Peterson et al. (2021)]], and [[@Bruhin2010|Bruhin et al. (2010)]].

Fourth, an **identification limit** runs through the structural members. [[@Bruhin2010|Bruhin et al. (2010)]] cannot identify loss aversion $\lambda$ (no mixed lotteries) and concede model size ($C=2$ vs. $3$) is genuinely indeterminate; the vault owner's critique of [[@Fudenberg2021a|Fudenberg & Puri (2021)]] flags possible test-set leakage when group means are computed over other subjects in the same fold — putting the "near-ML completeness" claim at risk. Finally, [[@Arieli2011|Arieli et al. (2011)]] supply an orthogonal challenge: if deliberation is componentwise rather than holistic $g(p)v(x)$ integration, then *every* member's valuation primitive is a convenient fiction, yet gaze tendency does not even predict the realized choice.

## Open questions

- Does the theory-edge survive scale and richer domains? [[@Plonsky2019|Plonsky et al. (2019)]] and [[@Plonsky2018|Plonsky et al. (2018)]] explicitly leave open whether deep, theory-free models win once data are abundant — exactly the regime where [[@Peterson2021|Peterson et al. (2021)]] say they do.
- Can a *simpler* model retain the ensemble/BEAST accuracy? [[@Erev2010|Erev et al. (2010)]] and [[@Erev2017|Erev et al. (2017)]] flag that no entrant found one and that BEAST contains post-hoc assumptions.
- What is the right notion of complexity? [[@Fudenberg2022a|Fudenberg & Puri (2022)]] and [[@Fudenberg2022b|Fudenberg & Puri (2022)]] note support size is one of several (irregularity, computability), and the cognition–complexity-aversion link is unsettled.
- Individual-level prediction remains weak: CPC18's Track II is barely beaten by "predict the average DM" ([[@Plonsky2018|Plonsky et al. (2018)]]), and choice inertia is under-predicted by BEAST ([[@Erev2017|Erev et al. (2017)]]).
- How to fold discovered phenomena (outcome dropout, [[@Shoshan2023|Shoshan et al. (2023)]]) and process evidence ([[@Arieli2011|Arieli et al. (2011)]]) back into a predictive model?

## Candidate ideas

- **Settle the scale debate head-on:** re-run psychological forest / BEAST-Net vs. an unconstrained net on a single corpus across nested training-set sizes, mapping the crossover $N^\*$ where the theory-edge of [[@Plonsky2019|Plonsky et al. (2019)]] flips to the ML-edge of [[@Peterson2021|Peterson et al. (2021)]].
- **Simplicity as a CPC feature:** add the [[@Fudenberg2022a|Fudenberg & Puri (2022)]] support-size complexity cost as a foresight in the [[@Plonsky2019|Plonsky et al. (2019)]] pipeline and test whether it improves multi-outcome (LotNum > 2) prediction where [[@Shoshan2023|Shoshan et al. (2023)]] found EV-weight $w$ collapses.
- **Leakage-clean re-estimation:** redo the [[@Fudenberg2021a|Fudenberg & Puri (2021)]] / [[@Bruhin2010|Bruhin et al. (2010)]] mixture horse-race with a soft Gaussian mixture, subject-disjoint folds, and $C>3$ to test whether the "near-ML" gap is real or a fold-leakage artifact.
- **Process-constrained predictor:** build a componentwise (similarity-based) valuation layer motivated by [[@Arieli2011|Arieli et al. (2011)]] and test whether it beats holistic BEAST-Net ([[@Shoshan2023|Shoshan et al. (2023)]]) on the hard-to-multiply problems where componentwise gaze spikes.
- **Mechanism-pruning audit:** systematically leave-one-mechanism-out across BEAST.sd to confirm the [[@Plonsky2017|Plonsky et al. (2017)]] "EV + regret suffices" reduction generalizes to CPC18 and to individual-level Track II.
- **Inertia module:** add a learned choice-inertia/recency term to BEAST-Net to close the under-predicted inertia gap noted by [[@Erev2017|Erev et al. (2017)]], scored by ENO on the experience subset.

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
- [[@Chen2011]] — cited by 1 member
- [[@Fudenberg2019a]] — cited by 1 member
- [[@Fudenberg2020]] — cited by 1 member
- [[@Fudenberg2020a]] — cited by 1 member
- [[@Hartford2016]] — cited by 1 member
- [[@Kleinberg2018]] — cited by 1 member
- [[@Peysakhovich2017]] — cited by 1 member
- [[@Quiggin1982]] — cited by 1 member
- [[@Rendle2010]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
