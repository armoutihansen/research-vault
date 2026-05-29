---
citekey: McFadden2000
title: Rationality for Economists?
authors: ["McFadden, Daniel", "Machina, Mark J.", "Baron, Jonathan", "Fischhoff, Baruch", "Manski, Charles F."]
year: 2000
type: bookSection
doi: 10.1007/978-94-017-1406-8_4
zotero: "zotero://select/library/items/I78HBA42"
pdf: /Users/jesper/Zotero/storage/Z9US6AXR/McFadden2000.pdf
tags: [literature]
keywords: [behavioral-decision-theory, rationality, prospect-theory, cognitive-anomalies, stochastic-rationality, survey-measurement, contingent-valuation]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Rationality is a complex behavioral theory that can be parsed into statements about preferences, perceptions, and process. This paper looks at the evidence on rationality that is provided by behavioral experiments, and argues that most cognitive anomalies operate through errors in perception that arise from the way information is stored, retrieved, and processed, or through errors in process that lead to formulation of choice problems as cognitive tasks that are inconsistent at least with rationality narrowly defined. The paper discusses how these cognitive anomalies influence economic behavior and measurement, and their implications for economic analysis.

## Summary
McFadden's Fisher-Schultz-style essay (the 1999 *Journal of Risk and Uncertainty* paper, here reprinted as a book chapter alongside discussant commentaries by Machina, Baron, Fischhoff, and Manski) decomposes economic "rationality" into three separable claims and asks the survey-design economist's practical question: which parts of the neoclassical choice model survive the behavioral-decision-theory evidence, and what does that mean for using non-market survey and experimental data? His verdict: perception-rationality and process-rationality fail systematically and pervasively, the case against preference-rationality is mostly circumstantial, and the productive response is to evolve "Chicago man" toward "K-T man" while salvaging the economic results that hold under weaker rationality.

## Research question
How deeply do documented cognitive anomalies (framing, anchoring, loss aversion, endowment effects, availability/representativeness, superstition, rule-driven choice, temporal inconsistency, projection) infect *economic* market behavior and economic *measurement*, and how much of the apparatus of demand analysis, benefit-cost analysis, and especially non-market (survey, contingent-valuation) data can be preserved once one takes that evidence seriously?

## Method / identification
This is a conceptual survey and synthesis, not an empirical estimation paper. Its core analytic move is to parse rationality (the "standard model," embodied in *Chicago man*) into three independent components, so that anomalies can be attributed to whichever component fails:
- **Perception-rationality**: beliefs are formed from information by strict Bayesian updating.
- **Preference-rationality**: preferences are primitive, complete, transitive, and immutable (representable by a utility index; under completeness + transitivity preferences yield a numerical scale).
- **Process-rationality**: the cognitive process is simply preference maximization given constraints.

He situates two historical templates: a broad *19th-century* view in which "preference maximization is a synonym for choice" (volatile, context-dependent), and the *20th-century Debreu-Deaton-Muellbauer* view where the consumer chooses a complete life-course plan over fully specified contingent commodities. He proposes **stochastic rationality** as the minimal structure that rescues most economic objectives: assume only that the *population distribution* of preferences is stationary even if individual preferences are volatile, so social-choice analysis treats individual volatility exactly as it treats cross-individual heterogeneity (citing McFadden 1981, 1997). The key refutable implication retained is the **regularity property**: a choice probability for an alternative cannot rise when the choice set is enlarged.

The opposing pole, *K-T man* (Kahneman-Tversky), is characterized via prospect theory and the rule-driven / problem-solving view of cognition. The paper formalizes prospect theory's mechanics: choice maximizes a weighted value function over gains/losses relative to an edited reference point, with value function $v(x)$ ($v(0)=0$) capturing the gain/loss asymmetry and probability weight $\pi(p)$ overweighting improbable and underweighting probable events. A worked Tversky-Fox (1995) example uses segregation — paying net $W$ for ticket $(x,p)$ is *not* evaluated as the merged lottery $(x-W, p;\, -W, 1-p)$ — so the median willingness-to-pay $w(100,0.05)=14$ satisfies $\pi(0.05)\cdot v(100)+v(-14)=0$, fit by $\pi(0.05)=0.2$, $\pi(0.95)=0.9$ and a piecewise-linear $v$. Machina's caveat is noted: if $W$ and $(x,p)$ *were* evaluated as the merged lottery (as EU requires), the data are inconsistent with any monotone increasing value function even allowing biased probability weights.

## Data
None original. The paper marshals secondary experimental evidence (Kahneman-Tversky framing, Allais, Simonson-Tversky context, Tversky-Kahneman anchoring, Thaler endowment, Shafir-Tversky disjunctive/prisoner's-dilemma) and references applied survey work the author is connected to — the AHEAD panel "unfolding bracket" anchoring studies (Hurd et al. 1997; Hurd 1999), where estimated mean household consumption varies by up to a factor of two with prompt sequence, and Green et al. (1996) on referendum-cue anchoring shifting apparent response distributions — plus the contingent-valuation / non-use-good literature.

## Key findings
- **A taxonomy of ~25 cognitive anomalies** (Table 1) grouped under four perception/belief headings (Context, Reference Point, Availability, Superstition) and two process-of-task headings (Process, Projection) — anchoring, framing, prominence, asymmetry/loss aversion, status-quo/endowment, certainty, focal, isolation/segregation, representativeness, regression, credulity, disjunctive, suspicion, rule-driven, temporal, misrepresentation, projection.
- **The Allais paradox** is presented as a clean violation of the von Neumann-Morgenstern substitution axiom: majority choices imply both $v(3000)/v(4000)>0.8$ and its reverse.
- **Endowment / reference-point effects** are pervasive, large, and near-instantaneous (so not sentimental attachment), producing a WTA-WTP gap and a reluctance to trade. The voting WTA $\gg$ WTP example is read as rule-driven ("voting is an entitlement; it is immoral to sell it"), not a kinked indifference curve.
- **Superstition and suspicion**: the Shafir-Tversky "quasi-magical" effect — 97% compete when told the opponent competes, 84% when told the opponent cooperates, yet only 63% compete when the opponent's move is hidden — violates the sure-thing principle; superstition can be quasi-Bayesian in a non-ergodic world where data never refute a conspiratorial Nature, and suspicion can be a *rational defensive rule* against sharp traders.
- **Headline conclusion**: perception-rationality fails — failures are "systematic, persistent, pervasive, and large in magnitude"; process-rationality also fails; preference-rationality is unrefuted by direct evidence but undercut circumstantially. Moreover, perception/process failures may be so large that "even if they exist, preferences are largely irrelevant to the explanation of observed behavior."
- **Market discipline is limited**: arbitrage only polices a few organized markets, and reluctance to trade *shelters* irrationalities from arbitrage ("There is a fool reborn every minute").

## Contribution
It reframes the economics-versus-psychology debate as a question of *which* rationality assumption fails and *where*, giving economists a defensible middle position: keep the predictive convenience of the standard model where it works, but treat survey and contingent-valuation responses as psychometric measurements requiring correction (e.g., randomizing anchors by design to identify and net out anchoring). The parse into perception/preference/process, and the claim that anomalies are mostly *perceptual* rather than *preference* failures, is the load-bearing idea: if true, conventional demand and welfare analysis survives in a form where history and path-dependence matter, and even social-choice/welfare comparisons remain workable albeit relative and path-dependent.

## Limitations & open questions
McFadden is explicit about what remains unresolved — these are direct project hooks:
- **Is there a "there" there in preferences?** Whether stable, deep preferences exist or are "illusionary, the temporary product of rule-driven processes" is the central open empirical question; if the latter, richer surveys yield only more elaborate constructed preferences, never fundamentals.
- **Perception vs. preference attribution is unsettled.** "This coffin has not yet been nailed shut" — the evidence cannot cleanly exclude perception failures (vs. genuine preference failures) as the source of most anomalies, partly because experiments do not control for the unrecognized aspects of commodities that an abstractly preference-rational agent could care about.
- **Prospect theory is admittedly partial**: it does not specify the editing/reference-point-formation process except by anecdote, especially for complex or multi-stage lotteries.
- **Stochastic rationality is no panacea**: it cannot explain anomalies that shift the *distribution* of preferences and is itself refutable via the regularity property.
- **Survey design**: good design can *identify and reduce* anomaly-driven response error (anchoring, focal effects, rule-driven and "warm glow" misrepresentation, projection) but "it is less clear that it can eliminate them."
- Discussant **Machina** issues a sharper methodological challenge ("Don't study the epicycles — piece together the ellipse"): describe anomalies on their own terms rather than as deviations from the classical model, and search for simpler unifying regularities. **Baron** argues the most consequential deviations are in survey responses and *political* behavior (status-quo/loss aversion blocking welfare-improving reforms), where feedback is weakest.

## Connections
The intellectual lineage runs from von Neumann-Morgenstern (1947) and the Allais (1953) paradox through the Kahneman-Tversky program (prospect theory 1979/1992; framing 1984; anchoring 1974; representativeness/availability) and Thaler's endowment effect, with Simon's bounded rationality, Prelec's rule-governed action, and Loewenstein's affect-in-decision work as the process-side anchors. The neoclassical pole is Hicks-Samuelson-Debreu, extended by Deaton-Muellbauer and the Becker/Lucas "Chicago" reading. Most directly for the present project, McFadden ties the discussion to his own random-utility / stochastic-choice and social-choice work (McFadden 1974, 1981, 1997) — stochastic rationality and the regularity property are the bridge between population-level demand prediction and individual preference volatility, which is the natural connection point for any project predicting or aggregating heterogeneous (and possibly unstable) preferences.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
