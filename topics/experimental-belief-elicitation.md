---
slug: experimental-belief-elicitation
title: Incentivized Belief Elicitation in Experiments
type: topic
scope: "Mechanisms for eliciting subjective beliefs from experimental subjects and their (behavioral) incentive compatibility under risk, ambiguity, and non-EU preferences: risk-correction, binarization, binary lotteries, frequency reports, and partial identification."
area: "[[beliefs-forecasting-elicitation]]"
tags: [topic]
created: 2026-06-01
generated: 2026-06-01
---

## Scope

This topic gathers the mechanisms that pay experimental subjects to reveal their subjective beliefs, and the long argument over when a report can actually be read as a belief. The unifying question is *incentive compatibility under realistic preferences*: a proper scoring rule recovers the truth only under risk neutrality and expected-value maximization, so the literature has built progressively more robust instruments — risk-correction curves, binary-lottery / binarized payment, BDM-style probability matching, and fixed-prize frequency reports — only to discover that each robustness gain trades against subject comprehension, point identification, or freedom from ambiguity. The members span the full arc from the foundational theory (which functionals are even elicitable) through the mechanism-design fixes to the experimental horse-races that ask, deflatingly, whether any of it beats just asking.

## Sub-themes

- **Foundations: which functionals are elicitable, and what propriety costs.** Savage (1971) frames a probability as a marginal rate of substitution and characterizes the entire proper-rule class as supports of a strictly convex expected-score function $J$, isolating the quadratic and logarithmic rules; Gneiting & Raftery (2007) generalize this to arbitrary probability spaces (the Bregman/entropy backbone, CRPS, energy and quantile/interval scores) and supply the elicitability taxonomy — squared-error elicits the mean, absolute-error the median, the tick loss a quantile. Both flag that propriety alone says nothing about *behavioral* robustness, and that selecting *which* proper rule to use is undertheorized.
- **The risk-neutrality problem and ex-post correction.** Offerman et al. (2009) make the distortion observable: estimate each subject's reporting map $R(p)$ on objective-probability calibration events, then invert it to recover beliefs and, residually, ambiguity attitudes. Armantier & Treich (2013) generalize the bias to *all* proper rules and *all* risk-averse EU agents, and show it interacts with payment scale, exogenous stakes, and hedging in ways no single correction can undo (and that paying *less* can worsen the bias under DRRA). Karni (2009) diagnoses the same scoring-rule bias as a marginal-utility ratio $K(r)\ne 1$.
- **Ex-ante robustness: binary lotteries and binarization.** The alternative is to design the distortion away. Berg et al. (1986) give the induced-preference foundation — paying in win-probability of a two-prize gamble makes the agent behave as an EU maximizer with a decreed utility, because EU is linear in that probability. Karni (2009) builds a BDM-style direct-revelation mechanism with a dominant truth-telling strategy under probabilistic sophistication. Hossain & Okui (2013) fold any proper rule into this binary-lottery wrapper (the BSR), extending robustness to non-EU/stochastic-dominance-monotone preferences and to means/medians/quantiles. Harrison et al. (2014) supply the cleanest test on a *genuinely subjective* event and extend validity to rank-dependent utility.
- **Frequency reports and partial identification.** Schlag & Tremewan (2021) exploit multiple realizations: guess the realized count, win a fixed prize on an exact match. Incentive compatibility then holds for *any* monotone utility (no scoring curve, no intermediate payoffs), but the rule identifies a belief *interval*, not a point — partial identification of the latent belief, provably the tightest any single binary-event report can be. Armouti-Hansen2026b recasts this whole class as a partial-identification problem (Manski-style), characterizing the identified set $P_S(r)$ and coordinate/linear-functional bounds for squared-distance, frequency-guessing, and Manhattan count losses under a single discrete-convexity condition.
- **Behavioral incentive compatibility and the horse-races.** Danz et al. (2022) show the theoretically-clean BSR fails *de facto*: giving subjects more information about its (flat) incentives increases center-biased misreporting, distorting downstream inference. Schlag & Tremewan (2021) document an analogous focal-$0.5$ collapse under the cognitively heavier Karni mechanism. Trautmann & van de Kuilen (2015) and the survey of Charness et al. (2021) run the broad comparison and find non-incentivized introspection roughly ties the truth serums on accuracy and additivity, beaten only on predicting own behavior — reframing the field around comprehension/complexity rather than theoretical propriety.

## Cross-paper tensions

The defining fault line is **correct-but-fragile vs. robust-but-coarse-or-confusing**. Gneiting & Raftery (2007) and Savage (1971) deliver point identification and a rich elicitability calculus, but only under risk neutrality. The risk-neutrality fixes then split into two camps that disagree on *what* to robustify against and at what cost. Offerman et al. (2009) keep the point estimate and add an ex-post correction curve; Armantier & Treich (2013) pull hard against that program, proving the bias depends on *unobserved* stakes and hedging so that "no general payment-scaling fix" exists and Karni & Safra-style impossibility bites — a correction that fixes risk aversion need not survive a financial stake. The binary-lottery camp (Berg et al. 1986; Karni 2009; Hossain & Okui 2013; Harrison et al. 2014) instead removes risk attitude ex ante, but buys it with an extra randomization layer that *itself* assumes reduction of compound lotteries and probabilistic sophistication — assumptions Charness et al. (2021) note may be exactly what fails.

The sharpest empirical collision is **Hossain & Okui (2013) vs. Danz et al. (2022)** over the very same mechanism: Hossain & Okui validate the BSR as risk-robust and truth-revealing, while Danz, Vesterlund & Wilson show that *explaining its incentives* raises false-report rates and pulls reports to center, with subjects failing even a stripped-down direct choice over the BSR lottery pairs. Theoretical incentive compatibility and behavioral incentive compatibility point in opposite directions for the field's workhorse. A parallel tension runs along the **point vs. interval** axis: Schlag & Tremewan (2021) and Armouti-Hansen2026b deliberately abandon point identification for distribution-free robustness and report a set, whereas Offerman et al. (2009), Hossain & Okui (2013), and Harrison et al. (2014) fight to preserve a point estimate; the frequency camp would say the point estimates are spuriously precise, the point camp that intervals discard usable information.

A third, quieter tension is **whether incentivization helps at all**. Charness et al. (2021) and Trautmann & van de Kuilen (2015) find introspection matches the elaborate truth serums on accuracy and additivity — implying the entire mechanism-design enterprise (Savage 1971 → Karni 2009 → Hossain & Okui 2013 → Armouti-Hansen2026b) may be optimizing a margin that the data cannot see, except for predicting own behavior. Finally there is a **comprehension–robustness inversion**: the most theoretically robust mechanisms (Karni 2009; the BSR) are the ones Schlag & Tremewan (2021) and Danz et al. (2022) find subjects understand *worst*, while the assumption-light frequency report is understood best — so robustness in theory and robustness in the lab are anticorrelated.

## Open questions

- **Can a mechanism be simultaneously informative and behaviorally incentive compatible?** Danz et al. (2022) leave open what an elicitation that is both transparent about incentives *and* truth-revealing would look like, and give no characterization of which preference/cognitive types satisfy behavioral incentive compatibility, nor a constructive mechanism delivering it.
- **Is the optimal-reporting premise true?** Armouti-Hansen2026b's whole informativeness ranking is conditional on subjects reporting optimally — an upper bound, not a behavioral prediction — and the cognitive-ease claim for frequency formats is inherited, not established. Whether real subjects play the dominant strategy is likewise untested in Karni (2009).
- **Robustness under joint stakes, hedging, and non-EU.** Armantier & Treich (2013) leave open any mechanism robust to *both* unobserved stakes/hedging *and* risk attitude; the non-EU × stakes interaction is unexplored. Harrison et al. (2014) extend robustness only to rank-dependent utility, not to disappointment aversion or reference-dependence.
- **Frequency/interval methods beyond binary events.** Schlag & Tremewan (2021) prove optimality of the frequency interval only for $k=2$; extension to $k>2$ is open, and Armouti-Hansen2026b shows two natural count losses (Hamming, Chebyshev) resist tractable bounds and that no rule dominates across belief regimes. A usable simple *quantile/distribution* analogue is still missing.
- **Disentangling genuine non-additivity from measurement artifact.** Offerman et al. (2009) and Trautmann & van de Kuilen (2015) both reduce but cannot eliminate additivity violations, leaving the split between true ambiguity attitude and residual elicitation bias open; ambiguity-robust elicitation is unsolved.
- **Sequence/portfolio validity.** Hossain & Okui (2013) establish incentive compatibility for a single report; running multiple elicitations together (hedging across decisions) is flagged but unsolved — as is the stability of a risk-correction curve across domains/time (Offerman et al. 2009).

## Candidate ideas

- **Coverage of identified sets under non-optimal reporting (theory + simulation).** Armouti-Hansen2026b's bounds presume optimal reports; Danz et al. (2022) document systematic center bias. Build a behavioral reporting model (center-bias mixture $q=c$ w.p. $\alpha$, optimal w.p. $1-\alpha$, à la Danz et al.) on top of the frequency-report rules and ask, by simulation, whether the identified set $P_S(r)$ still *covers* the true belief and how its informativeness ranking across squared-distance / frequency-guessing / Manhattan reorders once misreporting is priced in. Feasible with no new experiment — pure theory + Monte Carlo on the existing `design_efficiency` machinery.
- **A partial-identification reading of binarized and Karni reports (theory).** Schlag & Tremewan (2021) and Armouti-Hansen2026b deliver sharp identified sets for count rules; the BSR (Hossain & Okui 2013) and the Karni (2009) mechanism are studied only as point-identifying under their maintained assumptions. Derive the *identified set* a BSR or Karni report implies once risk neutrality / probabilistic sophistication is relaxed to stochastic-dominance monotonicity — turning the Armantier & Treich (2013) "the report is not the belief" critique into explicit Manski-style bounds rather than a correction curve. Theory-only.
- **Behaviorally incentive-compatible by construction: a frequency-report diagnostic.** Danz et al. (2022) show information about flat incentives breaks the BSR but never tested whether a fixed-prize frequency report — whose incentives are *not* flat near the optimum and require no compound-lottery reduction — passes their two weak conditions (more information should raise truth-telling; a direct choice should pick the maximizer). Design (or, existing-data-only, re-analyze Schlag & Tremewan's 2021 comprehension/response-time data through the Danz et al. center-bias measurement model) to test whether the frequency format is the behaviorally incentive-compatible mechanism Danz et al. leave open.
- **Multi-outcome frequency optimality and the regime-robust rule (theory).** Schlag & Tremewan (2021) prove minimal-precision optimality only for $k=2$; Armouti-Hansen2026b shows the closed-form rules' coordinate widths cross in report concentration and that Manhattan is the minimax-regret hedge. Pin down whether *any* single-report count rule is uniformly most informative for $k>2$, or prove an impossibility, and characterize the sharp bounds for the open Hamming/Chebyshev cases (non-convex semialgebraic identified sets) — directly closing Armouti-Hansen2026b's two boundary-rule gaps. Theory; simulation for the empirical regime map.
- **The induced-beliefs coverage experiment (Armouti-Hansen2026b Section 5.3, design + data).** Induce $p$ via a known urn/signal structure so the true multinomial belief is known, then measure empirical coverage of $p$ by $P_S(r)$ across rules, crossing frequency-report vs. standard probability scoring and direct vs. binary-lottery payment (Berg et al. 1986; Hossain & Okui 2013), logging response times and dominated-report rates as in Schlag & Tremewan (2021) and Harrison et al. (2014). This is the explicit project hook; if new experiments are infeasible, the comprehension/accuracy comparison can be partially assembled from the archived Trautmann & van de Kuilen (2015) and Schlag & Tremewan (2021) replication data.
- **Joint identification of belief, risk, and ambiguity from one frequency report (theory + existing data).** Offerman et al. (2009) recover beliefs *and* residual ambiguity attitudes from one risk-corrected report; the frequency method drops the risk channel entirely but says nothing about ambiguity. Ask whether crossing a frequency report with a small objective-probability calibration (Offerman et al. 2009 style) lets one separate the identified belief set from an ambiguity index without a parametric risk model — combining the partial-identification machinery of Armouti-Hansen2026b with the calibration logic of Offerman et al., re-using their archived calibration data.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Roth1979]] — cited by 5 members
- [[@Gigerenzer1995]] — cited by 2 members
- [[@Manski2004]] — cited by 2 members
- [[@Bellemare2008]] — cited by 1 member
- [[@Delavande2011]] — cited by 1 member
- [[@Federgruen1986]] — cited by 1 member
- [[@Fehr1999]] — cited by 1 member
- [[@Fox1966]] — cited by 1 member
- [[@Gneiting2011]] — cited by 1 member
- [[@Heinrich2014]] — cited by 1 member
- [[@Hogarth1975]] — cited by 1 member
- [[@Lambert2008]] — cited by 1 member
- [[@Quiggin1982]] — cited by 1 member
- [[@Selten1998]] — cited by 1 member
- [[@Tversky1992]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
