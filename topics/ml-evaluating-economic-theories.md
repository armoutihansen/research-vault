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

This topic covers the methodology of using flexible machine-learning predictors as *yardsticks* for interpretable economic theories — not as substitutes for them. The defining move is to treat a behavioral model as a point in a prediction problem and ask how far it sits from a black-box ceiling (completeness), how much arbitrary behavior its functional form rules out (restrictiveness), how it transfers across domains, and where it can be made to fail (anomaly generation). The boundary: the *target* of evaluation is a structural/behavioral theory, and ML is the diagnostic instrument. Papers about prediction competitions for their own sake, or ML methods with no theory-evaluation payoff, live in neighboring topics; the ML-for-causal-inference toolkit ([[@Athey2019|Athey & Imbens (2019)]]) enters only as imported machinery.

## Sub-themes

- **Completeness — the predictable-variation benchmark.** [[@Fudenberg2022|Fudenberg, Kleinberg, Liang & Mullainathan (2022)]] defines completeness as the fraction of *achievable* error reduction a model captures, with irreducible error estimated cheaply by lookup tables; [[@Fudenberg2019a|Fudenberg & Liang (2019)]] supplies the initial-play data and the "ML-as-microscope" diagnostic loop. [[@Peysakhovich2017|Peysakhovich & Naecker (2017)]] is the precursor, using a 55k-parameter regression as an explainable-variance ceiling for risk/ambiguity preferences. [[@Armouti-Hansen2022|Armouti-Hansen (2022)]] ports completeness to social-preference data and adds within-type and unrestricted completeness for mixtures.
- **Restrictiveness — empirical content from synthetic data.** [[@Fudenberg2020|Fudenberg, Gao & Liang (2020)]] and its conference twin [[@Fudenberg2021|Fudenberg, Gao & Liang (2021)]] measure how well a model fits *random* permissible behaviors, axiomatizing a uniform-prior measure; [[@Fudenberg2020b|Fudenberg & Liang (2020)]] surveys completeness + restrictiveness + algorithmic experimental design as one program.
- **Transfer and out-of-domain generalization.** [[@Andrews2022|Andrews, Fudenberg, Liang & Wu (2022)]] formalizes transfer error with domain-level conformal intervals; [[@Fudenberg2020a|Fudenberg & Karreskog (2020)]] shows a 6-parameter learning model extrapolates better than ML across PD treatments and horizons.
- **Generative theory criticism.** [[@Mullainathan2023|Mullainathan & Rambachan (2023)]] automates anomaly discovery via adversarial and morphing procedures, generalizing restrictiveness into an existence theorem.
- **Modeling the learner / choosing the loss.** [[@Caplin2022|Caplin, Martin & Marx (2022)]] treats a CNN as a rationally-inattentive decision maker and recovers its learning costs; [[@dEon2024|d'Eon, Greenwood, Leyton-Brown & Wright (2024)]] axiomatizes which loss to *report* (squared $L_2$, a diagonal bounded Bregman divergence).
- **Feature-free predictors as the ceiling.** [[@Hartford2016|Hartford, Wright & Leyton-Brown (2016)]] builds a deep, size-invariant net that beats hand-engineered behavioral game theory; [[@Kleinberg2018|Kleinberg et al. (2018)]] and [[@Bastani2022|Bastani, Bastani & Sinchaisri (2022)]] use ML to diagnose and improve *human* decisions under selective labels and unknown payoffs.
- **Revealed-preference recoverability.** [[@Zrill2021|Zrill (2021)]] benchmarks a parametric DA model against non-parametric Varian bounds as an upper bound; [[@Athey2019|Athey & Imbens (2019)]] supplies the orthogonalization/policy-learning toolkit the program borrows.

## Cross-paper tensions

The sharpest fault line runs **between within-domain completeness and out-of-domain transfer**. [[@Fudenberg2022|Fudenberg et al. (2022)]] and [[@Peysakhovich2017|Peysakhovich & Naecker (2017)]] crown the black box as the *ceiling* a theory should approach; [[@Andrews2022|Andrews et al. (2022)]] then shows that on the *same* certainty-equivalent task the ceiling-setter (random forest, kernel ridge) **transfers worse than CPT/EU** once the lottery marginal shifts — black boxes interpolate but do not extrapolate. So the very object used to *score* completeness is the object that *fails* the generalization test, and [[@Fudenberg2020a|Fudenberg & Karreskog (2020)]] reinforces this by beating ML out-of-treatment with a spare learning model. A theory at 95% completeness in-domain may be the *more* portable model — completeness and transferability can point opposite ways.

A second tension is **completeness vs. restrictiveness as competing virtues**. [[@Fudenberg2020|Fudenberg et al. (2020)]] shows CPT is 95% complete yet flexible ($r\approx0.28$), while Disappointment Aversion is restrictive but only 27% complete — and a *structural* network-diffusion model is Pareto-dominated by one-regressor OLS. Parameter count tracks neither axis. But the frontier need not be concave, so the two scores cannot be collapsed into one criterion; which model "wins" is, by the authors' own admission, a matter of taste. [[@Zrill2021|Zrill (2021)]] sharpens the same trade-off from the revealed-preference side: a restrictive CRRA-DA form loses only ~6% predictive accuracy to non-parametric bounds — restrictiveness is nearly free, contradicting the worry that simple forms sacrifice fit.

Third, **what counts as the benchmark is contested**. [[@Fudenberg2022|Fudenberg et al. (2022)]] insists irreducible error is directly estimable via lookup tables; [[@Peysakhovich2017|Peysakhovich & Naecker (2017)]] and [[@Zrill2021|Zrill (2021)]] can only offer an *approximate* upper bound (a regularized regression, non-parametric bounds that need not nest the parametric model). [[@dEon2024|d'Eon et al. (2024)]] adds that the loss function itself is not innocent — NLL, Brier, and KL all violate its reporting axioms, so completeness numbers computed under a "wrong" loss are not comparable across papers. And whereas the Fudenberg program asks *how much* of behavior a theory misses, [[@Mullainathan2023|Mullainathan & Rambachan (2023)]] argues every non-trivial theory *necessarily* admits anomalies, shifting the question from measurement to *construction* of the minimal falsifying dataset.

Finally, **whose decision is being modeled** splits the topic: most members evaluate human behavioral theories, but [[@Caplin2022|Caplin et al. (2022)]] turns the lens around and asks whether the *algorithm* is the rational-inattention agent, while [[@Kleinberg2018|Kleinberg et al. (2018)]] and [[@Bastani2022|Bastani et al. (2022)]] use ML to expose human *noise/suboptimality* — implying the "irreducible error" the completeness program treats as a floor may partly be human inconsistency that better grouping ([[@Fudenberg2022|Fudenberg et al. 2022]]'s own open hook) could shrink.

## Open questions

- How should completeness and restrictiveness be *aggregated* when the frontier is non-concave ([[@Fudenberg2020|Fudenberg et al. 2020]]; [[@Fudenberg2021|Fudenberg et al. 2021]])? No principled scalar criterion exists.
- Is within-domain completeness the wrong target? [[@Andrews2022|Andrews et al. (2022)]] and [[@Fudenberg2022|Fudenberg et al. (2022)]] both flag "overall/transfer completeness" as undefined, and finding a *best* transfer decision rule (cross-domain CV, hierarchical Bayes, DRO) is open.
- How much of measured irreducible error is genuine noise vs. recoverable with better subject grouping or richer features (response times, demographics)? Left open by [[@Fudenberg2022|Fudenberg et al. (2022)]], [[@Fudenberg2020a|Fudenberg & Karreskog (2020)]], and [[@Armouti-Hansen2022|Armouti-Hansen (2022)]] (the 60–65%-complete second latent type).
- Can anomaly generation move from *simulated* to *real* choice data, and is the "dominated consequence effect" a real human anomaly ([[@Mullainathan2023|Mullainathan & Rambachan 2023]])?
- Does the completeness/restrictiveness framework survive outside low-dimensional finite-feature lab settings ([[@Fudenberg2020b|Fudenberg & Liang 2020]]; [[@Peysakhovich2017|Peysakhovich & Naecker 2017]])?
- Is there a *single* defensible reporting loss, or only the DBBD family ([[@dEon2024|d'Eon et al. 2024]])? And does ambiguity aversion admit a portable parsimonious form whose penalty is convex ([[@Peysakhovich2017|Peysakhovich & Naecker 2017]])?

## Candidate ideas

- **Transfer-completeness measure.** Define and estimate an out-of-domain analogue of completeness that benchmarks a theory's transfer error against the best *transferable* predictor, reconciling [[@Fudenberg2022|Fudenberg et al. (2022)]] with the black-box transfer failure in [[@Andrews2022|Andrews et al. (2022)]].
- **Loss-robust completeness.** Recompute completeness/restrictiveness for CPT, DA, and PCHM under every DBBD ([[@dEon2024|d'Eon et al. 2024]]) and test whether the model rankings in [[@Fudenberg2020|Fudenberg et al. (2020)]] are loss-invariant or artifacts of squared error vs. log-loss.
- **Anomaly generation on real social-preference data.** Apply [[@Mullainathan2023|Mullainathan & Rambachan (2023)]]'s morphing to the dictator/reciprocity data of [[@Armouti-Hansen2022|Armouti-Hansen (2022)]] to construct minimal anomalies for [[@Fehr1999|Fehr–Schmidt]]-style models in the 60–65%-incomplete latent type.
- **Noise-vs-structure decomposition.** Combine [[@Kleinberg2018|Kleinberg et al. (2018)]]'s "predict the human" diagnostic with [[@Fudenberg2022|Fudenberg et al. (2022)]]'s lookup tables to estimate how much "irreducible" error in lab choice is human inconsistency a better grouping could remove.
- **Convex portable ambiguity model + completeness audit.** Build the parsimonious convex-penalty ambiguity model [[@Peysakhovich2017|Peysakhovich & Naecker (2017)]] call for and certify it via restrictiveness ([[@Fudenberg2021|Fudenberg et al. 2021]]) so its fit reflects structure, not flexibility.
- **Algorithm-as-DM diagnostics for behavioral predictors.** Extend [[@Caplin2022|Caplin et al. (2022)]]'s cost-recovery to the deep behavioral-game net of [[@Hartford2016|Hartford et al. (2016)]], asking whether a learned payoff-to-play map is loss-calibrated and what "learning cost" rationalizes its departures from level-$k$.

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
