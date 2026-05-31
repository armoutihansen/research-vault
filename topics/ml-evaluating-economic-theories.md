---
slug: ml-evaluating-economic-theories
title: Machine Learning for Evaluating Economic Theories
type: topic
scope: "Completeness/restrictiveness diagnostics, anomaly generation, and using black-box predictors to benchmark and improve behavioral models."
area: "[[econometrics-machine-learning]]"
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This topic covers using flexible machine-learning predictors as *yardsticks* for interpretable economic theories — not as substitutes. The defining move is to treat a behavioral model as a point in a prediction problem and ask how far it sits from a black-box ceiling (completeness), how much arbitrary behavior its form rules out (restrictiveness), how it transfers across domains, and where it can be made to fail (anomaly generation). The *target* of evaluation is a structural/behavioral theory; ML is the diagnostic instrument. The applied predictive horse-races at the topic's edge — flexible learners against a discrete-choice baseline — belong here not as contests for their own sake but because the *gap* they expose is itself a verdict on the parametric model. The ML-for-causal-inference toolkit ([[@Athey2019|Athey & Imbens (2019)]]) enters only as imported machinery.

## Sub-themes

- **Completeness — the predictable-variation benchmark.** [[@Fudenberg2022|Fudenberg, Kleinberg, Liang & Mullainathan (2022)]] defines completeness as the fraction of *achievable* error reduction a model captures, with irreducible error estimated via lookup tables; [[@Fudenberg2019a|Fudenberg & Liang (2019)]] supplies the initial-play data and "ML-as-microscope" loop. [[@Peysakhovich2017|Peysakhovich & Naecker (2017)]] is the precursor, using a 55k-parameter regression as an explainable-variance ceiling; [[@Armouti-Hansen2022|Armouti-Hansen (2022)]] ports completeness to social-preference data with within-type and unrestricted variants.
- **Restrictiveness — empirical content from synthetic data.** [[@Fudenberg2020|Fudenberg, Gao & Liang (2020)]] and its twin [[@Fudenberg2021|Fudenberg, Gao & Liang (2021)]] measure how well a model fits *random* permissible behaviors; [[@Fudenberg2020b|Fudenberg & Liang (2020)]] surveys completeness + restrictiveness + algorithmic experimental design as one program.
- **ML vs. structural choice models — out-of-sample predictive benchmarking.** The applied wing supplies the raw evidence the diagnostic program presupposes: that flexible learners out-predict a parametric discrete-choice model on real data. [[@Gan2005|Gan, Limsombunchai, Clemes & Weng (2005)]] races a binary logit against a feed-forward and a probabilistic neural network on banking-channel choice; both nets beat the logit out-of-sample (91.4% vs. 99.05%). [[@vanWezel2007|van Wezel & Potharst (2007)]] generalizes to multi-class brand choice, showing bagged/boosted CART ensembles beat a single tree *and* multinomial logit, and reads the gap through James's bias/variance split $PE = \text{irreducible} + SE + VE$: logit is high-bias/low-variance, so a persistent systematic-effect gap signals the theory-derived form misrepresents the choice process — turning an accuracy contest into a completeness-style diagnostic.
- **Transfer and out-of-domain generalization.** [[@Andrews2022|Andrews, Fudenberg, Liang & Wu (2022)]] formalizes transfer error with domain-level conformal intervals; [[@Fudenberg2020a|Fudenberg & Karreskog (2020)]] shows a 6-parameter learning model extrapolates better than ML across PD treatments and horizons.
- **Generative theory criticism.** [[@Mullainathan2023|Mullainathan & Rambachan (2023)]] automates anomaly discovery via adversarial/morphing procedures, generalizing restrictiveness into an existence theorem.
- **Modeling the learner / choosing the loss.** [[@Caplin2022|Caplin, Martin & Marx (2022)]] treats a CNN as a rationally-inattentive agent and recovers its learning costs; [[@dEon2024|d'Eon, Greenwood, Leyton-Brown & Wright (2024)]] axiomatizes which loss to *report* (squared $L_2$, a diagonal bounded Bregman divergence).
- **Feature-free predictors as the ceiling.** [[@Hartford2016|Hartford, Wright & Leyton-Brown (2016)]] builds a size-invariant net beating hand-engineered behavioral game theory; [[@Kleinberg2018|Kleinberg et al. (2018)]] and [[@Bastani2022|Bastani, Bastani & Sinchaisri (2022)]] use ML to diagnose and improve *human* decisions under selective labels and unknown payoffs.
- **Revealed-preference recoverability.** [[@Zrill2021|Zrill (2021)]] benchmarks a parametric DA model against non-parametric Varian bounds as an upper bound.

## Cross-paper tensions

The sharpest fault line runs **between within-domain completeness and out-of-domain transfer**. [[@Fudenberg2022|Fudenberg et al. (2022)]] and [[@Peysakhovich2017|Peysakhovich & Naecker (2017)]] crown the black box as the *ceiling* a theory should approach; [[@Andrews2022|Andrews et al. (2022)]] then shows that on the same certainty-equivalent task the ceiling-setter (random forest, kernel ridge) **transfers worse than CPT/EU** once the lottery marginal shifts, reinforced by [[@Fudenberg2020a|Fudenberg & Karreskog (2020)]] beating ML out-of-treatment. The new applied benchmarks sit entirely on the *within-domain* side: [[@Gan2005|Gan et al. (2005)]] and [[@vanWezel2007|van Wezel & Potharst (2007)]] report only same-population held-out accuracy, so their flattering verdicts on the black box are exactly the ones [[@Andrews2022|Andrews et al. (2022)]] warns may reverse under a change of city, product, or panel.

A second tension: **does the black box really beat the structural model, and what does the margin mean?** [[@vanWezel2007|van Wezel & Potharst (2007)]] finds the logit only $\sim$4.5% worse than the best ensemble on peanut butter yet $\sim$16% worse on ketchup, and proves *ensembling never improves the logit itself* (a linear combination of linear models stays linear) — the gain is pure variance reduction, so where the logit's bias is small the structural form is nearly optimal. This mirrors [[@Zrill2021|Zrill (2021)]]'s $\sim$6% loss of a restrictive CRRA-DA form to non-parametric bounds and [[@Fudenberg2020|Fudenberg et al. (2020)]]'s 95%-complete CPT: across lab and field the parametric gap is *small* — restrictiveness is nearly free — even as the headline "neural net wins" ([[@Gan2005|Gan et al. 2005]]) invites the opposite reading.

Third, **completeness and restrictiveness are competing virtues**. [[@Fudenberg2020|Fudenberg et al. (2020)]] shows CPT is flexible ($r\approx0.28$) while Disappointment Aversion is restrictive but only 27% complete; parameter count tracks neither, and a non-concave frontier blocks any scalar criterion.

Fourth, **the benchmark itself is contested**. [[@Fudenberg2022|Fudenberg et al. (2022)]] estimates irreducible error directly; [[@Peysakhovich2017|Peysakhovich & Naecker (2017)]], [[@Zrill2021|Zrill (2021)]], and the applied pair offer only an *approximate* ceiling — [[@vanWezel2007|van Wezel & Potharst (2007)]] candidly *sets intrinsic noise to zero*, so its "logit is biased" diagnosis is itself a bound. [[@dEon2024|d'Eon et al. (2024)]] adds that the loss is not innocent: van Wezel scores under zero–one *and* cross-entropy and gets different winners, the cross-loss incomparability d'Eon predicts. And whose decision is modeled splits the topic — [[@Caplin2022|Caplin et al. (2022)]] models the *algorithm* as agent, while [[@Kleinberg2018|Kleinberg et al. (2018)]] and [[@Bastani2022|Bastani et al. (2022)]] use ML to expose human *suboptimality*, implying the completeness floor may be partly removable inconsistency.

## Open questions

- Do the within-domain ML-beats-logit verdicts of [[@Gan2005|Gan et al. (2005)]] and [[@vanWezel2007|van Wezel & Potharst (2007)]] survive [[@Andrews2022|Andrews et al. (2022)]]'s transfer test — does the structural model claw the gap back out of domain?
- Can [[@vanWezel2007|van Wezel & Potharst (2007)]]'s bias/variance gap be promoted to a proper *completeness* statistic — is $SE(\text{logit})$ relative to irreducible error the same object as Fudenberg-style incompleteness?
- How should completeness and restrictiveness be *aggregated* on a non-concave frontier ([[@Fudenberg2020|Fudenberg et al. 2020]])? No principled scalar exists.
- How much measured irreducible error is genuine noise vs. recoverable with richer features? Open in [[@Fudenberg2022|Fudenberg et al. (2022)]], [[@vanWezel2007|van Wezel & Potharst (2007)]] (which assumes it away), and [[@Armouti-Hansen2022|Armouti-Hansen (2022)]].
- Can anomaly generation move from *simulated* to *real* choice data ([[@Mullainathan2023|Mullainathan & Rambachan 2023]])?
- Is there a *single* defensible reporting loss, or only the DBBD family ([[@dEon2024|d'Eon et al. 2024]])?

## Candidate ideas

- **Transfer-completeness measure.** Benchmark a theory's transfer error against the best *transferable* predictor, reconciling [[@Fudenberg2022|Fudenberg et al. (2022)]] with the transfer failure in [[@Andrews2022|Andrews et al. (2022)]] — then re-run it on the consumer/brand-choice data of [[@Gan2005|Gan et al. (2005)]] and [[@vanWezel2007|van Wezel & Potharst (2007)]] to test whether the logit's deficit is portable.
- **Bias/variance completeness bridge.** Map [[@vanWezel2007|van Wezel & Potharst (2007)]]'s $SE/VE$ split onto completeness/restrictiveness, testing whether a high-bias parametric choice model is *necessarily* low-completeness once intrinsic noise is estimated rather than zeroed.
- **Loss-robust completeness.** Recompute the scores under every DBBD ([[@dEon2024|d'Eon et al. 2024]]) and test whether the rankings in [[@Fudenberg2020|Fudenberg et al. (2020)]] — and the cross-loss winner flip in [[@vanWezel2007|van Wezel & Potharst (2007)]] — are loss-invariant.
- **Anomaly generation on real social-preference data.** Apply [[@Mullainathan2023|Mullainathan & Rambachan (2023)]]'s morphing to the dictator/reciprocity data of [[@Armouti-Hansen2022|Armouti-Hansen (2022)]] to build minimal anomalies for Fehr–Schmidt-style models.
- **Algorithm-as-DM diagnostics.** Extend [[@Caplin2022|Caplin et al. (2022)]]'s cost-recovery to the behavioral-game net of [[@Hartford2016|Hartford et al. (2016)]], asking whether a learned payoff-to-play map is loss-calibrated and what learning cost rationalizes its departures from level-$k$.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Gul1991]] — cited by 3 members
- [[@Kahneman1979]] — cited by 3 members
- [[@Tversky1992]] — cited by 3 members
- [[@Bruhin2010]] — cited by 2 members
- [[@Charness2002]] — cited by 2 members
- [[@Goeree2001]] — cited by 2 members
- [[@Plonsky2017]] — cited by 2 members
- [[@Plonsky2019]] — cited by 2 members
- [[@Abeler2011]] — cited by 1 member
- [[@Andreoni2002]] — cited by 1 member
- [[@Baillon2020]] — cited by 1 member
- [[@Benjamin2010]] — cited by 1 member
- [[@Berns2006]] — cited by 1 member
- [[@Dekel2010]] — cited by 1 member
- [[@DellaVigna2018]] — cited by 1 member
- [[@Erev2010]] — cited by 1 member
- [[@Fehr1999]] — cited by 1 member
- [[@Fisman2007]] — cited by 1 member
- [[@Fudenberg2021a]] — cited by 1 member
- [[@Fudenberg2022a]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
