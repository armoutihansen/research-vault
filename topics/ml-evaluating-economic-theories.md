---
slug: ml-evaluating-economic-theories
title: Machine Learning for Evaluating Economic Theories
type: topic
scope: "Completeness/restrictiveness diagnostics, anomaly generation, and using black-box predictors to benchmark and improve behavioral models."
area: "[[econometrics-machine-learning]]"
tags: [topic]
created: 2026-05-31
generated: 2026-06-01
---

## Scope

This topic covers using flexible machine-learning predictors as *yardsticks* for interpretable economic theories — not as substitutes. The defining move is to treat a behavioral model as a point in a prediction problem and ask how far it sits from a black-box ceiling (*completeness*), how much arbitrary behavior its functional form rules out (*restrictiveness*), how it transfers across domains, and where it can be made to fail (*anomaly generation*). The target of evaluation is a structural/behavioral theory; ML is the diagnostic instrument. The applied predictive horse-races at the topic's edge — flexible learners against a discrete-choice baseline — belong here not as contests for their own sake but because the *gap* they expose is itself a verdict on the parametric model.

## Sub-themes

- **Completeness — the predictable-variation benchmark.** Fudenberg, Kleinberg, Liang & Mullainathan (2019) introduce completeness as the fraction of *achievable* error reduction a model captures, estimating the irreducible-error floor with a Table-Lookup conditional-expectation rule and finding CPT 95% complete, the Poisson Cognitive Hierarchy Model ~67–68% complete, and models of human randomness only ~24% complete; the published Fudenberg, Kleinberg, Liang & Mullainathan (2022) refines the estimator (cross-validation, bootstrap standard errors, the 97% PCHM result on dominance-solvable games). Peysakhovich & Naecker (2017) is the precursor, using a heavily-parameterized regression as an explainable-variance ceiling; Armouti-Hansen (2022) ports completeness to social-preference data (binary dictator and reciprocity games) with within-type and unrestricted variants.
- **Restrictiveness — empirical content from synthetic data.** Fudenberg, Gao & Liang (2020) and its published version Fudenberg, Gao & Liang (2025) measure how well a model fits *random* permissible behaviors drawn from an eligible set, normalize against a baseline, and pair restrictiveness with completeness on a Pareto frontier; Fudenberg, Gao & Liang (2025) adds the axiomatization, asymptotic inference, and a field application (microfinance diffusion in Indian villages) where a simple OLS centrality model dominates a structural gossip model on *both* axes. Fudenberg & Liang (2020) surveys completeness + restrictiveness + algorithmic experimental design as one program.
- **ML vs. structural choice models — out-of-sample predictive benchmarking.** The applied wing supplies the raw evidence the diagnostic program presupposes: that flexible learners out-predict a parametric discrete-choice model on real data. Gan, Limsombunchai, Clemes & Weng (2005) races a binary logit against feed-forward and probabilistic neural networks on banking-channel choice, both nets beating the logit out-of-sample; van Wezel & Potharst (2007) generalizes to multi-class brand choice, showing bagged/boosted CART ensembles beat a single tree *and* multinomial logit, and reads the gap through James's bias/variance split $PE = \text{irreducible} + SE + VE$ — logit is high-bias/low-variance, so a persistent systematic-effect gap signals the theory-derived form misrepresents the choice process.
- **Feature-free predictors as the ceiling in strategic settings.** Hartford, Wright & Leyton-Brown (2016) — both the conference paper and the journal version — build a size- and permutation-invariant deep net (matrix units + pooling + action-response layers) that *subsumes* quantal cognitive hierarchy and level-$k$ yet beats the hand-engineered behavioral-game-theory state of the art on pooled human play, with the gain from learning exceeding the gain from expert features. This is the strategic-domain analogue of the black-box ceiling that Fudenberg et al. (2022) measures completeness against.
- **Transfer and out-of-domain generalization.** Andrews, Fudenberg, Liang & Wu (2022) formalizes transfer error with domain-level conformal intervals; Fudenberg & Karreskog (2020) shows a 6-parameter learning model extrapolates better than ML across PD treatments and horizons.
- **Generative theory criticism.** Mullainathan & Rambachan (2023) automates anomaly discovery via an adversarial max-min game and gradient-based dataset morphing, axiomatizing theories as allowable function classes that always admit minimal anomalies, and recovering a novel independence-axiom anomaly on simulated CPT data.
- **Modeling the learner / choosing the loss.** Caplin, Martin & Marx (2022) treats a CNN as a rationally-inattentive agent and recovers its learning costs; d'Eon, Greenwood, Leyton-Brown & Wright (2024) axiomatizes which loss to *report* (squared $L_2$, a diagonal bounded Bregman divergence).
- **Diagnosing and improving human decisions.** Kleinberg et al. (2018) and Bastani, Bastani & Sinchaisri (2022) use ML to diagnose and improve *human* decisions under selective labels and unknown payoffs; Zrill (2021) benchmarks a parametric discounting model against non-parametric Varian bounds as an upper bound, the revealed-preference counterpart to completeness. The ML-for-causal-inference toolkit (Athey & Imbens 2019) enters only as imported machinery.

## Cross-paper tensions

The sharpest fault line runs **between within-domain completeness and out-of-domain transfer**. Fudenberg et al. (2019, 2022) and Peysakhovich & Naecker (2017) crown the black box as the *ceiling* a theory should approach; Andrews et al. (2022) then shows that on the same certainty-equivalent task the ceiling-setter (random forest, kernel ridge) **transfers worse than CPT/EU** once the lottery marginal shifts, reinforced by Fudenberg & Karreskog (2020) beating ML out-of-treatment. Hartford et al. (2016) sharpens the stakes: its feature-free net is *only* validated within a pooled corpus, and the authors flag that out-of-distribution generalization to genuinely new game families is untested — so its dethroning of behavioral game theory is exactly the within-domain verdict Andrews et al. (2022) warns may reverse. The new applied benchmarks sit on the same within-domain side: Gan et al. (2005) and van Wezel & Potharst (2007) report only same-population held-out accuracy.

A genuinely new tension arrives with **restrictiveness as a confound for completeness**. Fudenberg et al. (2025) shows that CPT's headline 95% completeness on binary lotteries is *flattered by flexibility*: much of CPT's empirical content there is just first-order stochastic dominance, so a near-complete fit need not mean the theory has identified deep structure. This cuts against the framing in Fudenberg et al. (2019, 2022) and Armouti-Hansen (2022), where high completeness reads as a near-optimal model. The two diagnostics can disagree about which model to prefer: Disappointment Aversion is only 27% complete yet *more* restrictive than CPT, so on a pure restrictiveness criterion it carries more empirical content per unit of fit. Worse, the Pareto frontier is **non-concave** (explicitly in both Fudenberg et al. 2020 and 2025), so no principled scalar reconciles the two axes — completeness and restrictiveness are *competing virtues*, and the topic now contains the paper that says so and the papers that quietly assume completeness alone suffices.

A third tension: **does the black box really beat the structural model, and what does the margin mean?** van Wezel & Potharst (2007) finds the logit only ~4.5% worse than the best ensemble on one product yet ~16% worse on another, and proves *ensembling never improves the logit itself* — the gain is pure variance reduction, so where the logit's bias is small the structural form is nearly optimal. This mirrors Zrill (2021)'s small loss of a restrictive discounting form to non-parametric bounds and the 95%-complete CPT of Fudenberg et al. (2019, 2022): across lab and field the parametric gap is often *small* — restrictiveness is nearly free — even as the headline "neural net wins" (Gan et al. 2005, Hartford et al. 2016) invites the opposite reading. The microfinance application of Fudenberg et al. (2025), where plain OLS dominates the structural gossip model, is the inverse case: structure that buys *neither* completeness nor restrictiveness.

Fourth, **the benchmark itself is contested**. Fudenberg et al. (2019, 2022) estimate irreducible error directly via Table Lookup; Peysakhovich & Naecker (2017), Zrill (2021), and the applied pair offer only an *approximate* ceiling — van Wezel & Potharst (2007) candidly *sets intrinsic noise to zero*, so its "logit is biased" diagnosis is itself a bound. d'Eon et al. (2024) adds that the loss is not innocent — van Wezel scores under zero–one *and* cross-entropy and gets different winners, the cross-loss incomparability d'Eon predicts. And whose decision is modeled splits the topic: Caplin et al. (2022) models the *algorithm* as agent, Hartford et al. (2016) treats the net as a black-box predictor of humans, while Kleinberg et al. (2018) and Bastani et al. (2022) use ML to expose human *suboptimality* — implying the completeness floor may be partly removable inconsistency rather than genuine noise.

## Open questions

- Does Hartford et al. (2016)'s feature-free deep net retain its lead **out of domain** — on game families absent from the pooled training corpus — or does it, like the black boxes in Andrews et al. (2022) and Fudenberg & Karreskog (2020), cede ground to structured behavioral game-theory models once the distribution shifts?
- How much of a model's measured completeness is **restrictiveness-adjusted signal** versus FOSD-or-baseline flexibility? Fudenberg et al. (2025) shows the two can diverge, but offers no joint statistic that nets one out of the other.
- How should completeness and restrictiveness be *aggregated* on a **non-concave frontier** (Fudenberg et al. 2020, 2025)? No principled scalar exists; the choice is left to "the analyst's taste."
- How much measured irreducible error is genuine noise vs. recoverable with richer features or better subject grouping? Explicitly open in Fudenberg et al. (2022), van Wezel & Potharst (2007) (which assumes it away), and Armouti-Hansen (2022).
- Can anomaly generation move from *simulated* to *real* choice data (Mullainathan & Rambachan 2023)? And can the eligible set / discrepancy in Fudenberg et al. (2025) be chosen by a disciplined principle rather than intuition?
- Is there a *single* defensible reporting loss, or only the DBBD family (d'Eon et al. 2024), and do completeness/restrictiveness rankings survive a change of loss?

## Candidate ideas

- **Transfer-restrictiveness of the strategic black box.** Re-estimate Hartford et al. (2016)'s deep net and a panel of behavioral-game-theory models, then evaluate both under Andrews et al. (2022)'s domain-level conformal transfer intervals across held-out game families (and, separately, compute the net's restrictiveness à la Fudenberg et al. 2025). The hypothesis: the net wins within-domain but the level-$k$/QCH models transfer better and are far more restrictive, reproducing the certainty-equivalent reversal in the strategic domain. Feasible on existing data — the pooled normal-form corpus and the trained-architecture code are public — no new experiments required (theory + simulation + existing-data).
- **Restrictiveness-adjusted completeness.** Construct a joint statistic that nets a model's FOSD/baseline flexibility (its restrictiveness, Fudenberg et al. 2025) out of its raw completeness, so "95% complete because CPT is flexible" and "95% complete because CPT identifies structure" become distinguishable scalars. Validate by recomputing the CPT-vs-DA frontier and asking whether the adjusted ranking flips. Pure theory + simulation on the public Bruhin et al. lottery data.
- **Bias/variance to completeness/restrictiveness bridge.** Map van Wezel & Potharst (2007)'s $SE/VE$ decomposition onto the completeness/restrictiveness pair, testing whether a high-bias parametric choice model is *necessarily* low-completeness once intrinsic noise is estimated rather than zeroed, and whether $VE$ corresponds to the model's flexibility. Existing-data only.
- **Anomaly generation on real social-preference data.** Apply Mullainathan & Rambachan (2023)'s dataset-morphing to the dictator/reciprocity data of Armouti-Hansen (2022) to construct minimal *real-data* anomalies for Fehr–Schmidt-style models — the first move of anomaly generation off simulated data, directly answering both papers' open question. Existing-data only.
- **Loss-robust frontier.** Recompute completeness and restrictiveness under every diagonal bounded Bregman divergence (d'Eon et al. 2024) and test whether the rankings in Fudenberg et al. (2020, 2025) — and the cross-loss winner flip in van Wezel & Potharst (2007) — are loss-invariant. If the frontier reshuffles under an admissible loss, the "matter of taste" aggregation problem is even worse than stated. Theory + simulation on existing data.
- **Restrictiveness of structure in the field.** Generalize the microfinance finding of Fudenberg et al. (2025) — that structure can buy *neither* completeness nor restrictiveness over plain OLS — into a diagnostic for when a field structural model is worth its assumptions, applied to a second field setting with a published structural-vs-reduced-form contest. Existing-data only.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Gul1991]] — cited by 4 members
- [[@Tversky1992]] — cited by 4 members
- [[@Bruhin2010]] — cited by 3 members
- [[@Kahneman1979]] — cited by 3 members
- [[@Plonsky2019]] — cited by 3 members
- [[@Charness2002]] — cited by 2 members
- [[@Gneiting2007]] — cited by 2 members
- [[@Goeree2001]] — cited by 2 members
- [[@Noti2016]] — cited by 2 members
- [[@Plonsky2017]] — cited by 2 members
- [[@deClippel2022]] — cited by 2 members
- [[@Abeler2011]] — cited by 1 member
- [[@Andreoni2002]] — cited by 1 member
- [[@Baillon2020]] — cited by 1 member
- [[@Benjamin2010]] — cited by 1 member
- [[@Berns2006]] — cited by 1 member
- [[@Dekel2010]] — cited by 1 member
- [[@DellaVigna2018]] — cited by 1 member
- [[@Erev2010]] — cited by 1 member
- [[@Fehr1999]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
