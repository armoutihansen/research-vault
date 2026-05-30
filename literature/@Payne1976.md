---
citekey: Payne1976
title: "Task complexity and contingent processing in decision making: An information search and protocol analysis"
authors: ["Payne, John W."]
year: 1976
type: journalArticle
doi: 10.1016/0030-5073(76)90022-2
zotero: "zotero://select/library/items/2QFARVN4"
pdf: /Users/jesper/Zotero/storage/XRU7LBMJ/Payne1976.pdf
tags: [literature]
keywords: [contingent-decision-making, process-tracing, elimination-by-aspects, compensatory-vs-noncompensatory, task-complexity, heuristics]
topics: []
related: [Manzini2007, Tversky1972]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Two process tracing techniques, explicit information search and verbal protocols, were used to examine the information processing strategies subjects use in reaching a decision. Subjects indicated preferences among apartments. The number of alternatives available and number of dimensions of information available was varied across sets of apartments. When faced with a two alternative situation, the subjects employed search strategies consistent with a compensatory decision process. In contrast, when faced with a more complex (multialternative) decision task, the subjects employed decision strategies designed to eliminate some of the available alternatives as quickly as possible and on the basis of a limited amount of information search and evaluation. The results demonstrate that the information processing leading to choice will vary as a function of task complexity. An integration of research in decision behavior with the methodology and theory of more established areas of cognitive psychology, such as human problem solving, is advocated.

## Summary
A foundational process-tracing study showing that decision makers do not apply a single fixed choice rule but switch strategies *contingent on task complexity*. Using information-board search records and concurrent "think-aloud" verbal protocols over apartment-choice tasks, Payne finds that with two alternatives subjects search exhaustively and symmetrically (a compensatory, trade-off-based process), whereas with many alternatives they search variably and selectively, eliminating options early on a few dimensions (a noncompensatory, heuristic process). Choice procedure is thus an adaptive response to cognitive load, not a stable property of the agent.

## Research question
Which characteristics of a decision task push an individual toward different information-processing (choice) strategies? Specifically, how do (a) the number of alternatives and (b) the number of dimensions per alternative affect whether a decision maker uses a compensatory rule (additive, additive-difference) versus a noncompensatory rule (conjunctive, elimination-by-aspects)?

## Method / identification
Two process-tracing techniques applied to multidimensional preferential choice over hypothetical one-bedroom apartments, presented as "information boards" (Wilkins, 1967): a grid of envelopes whose hidden cards reveal a dimension's value (e.g., "noise level: low") only when deliberately pulled. This externalizes acquisition: the experimenter records the exact order in which cells are opened.

Payne frames four candidate models by the search signature each implies, along two axes — amount of search per alternative (constant vs. variable) and search direction (interdimensional, i.e., within an alternative across dimensions; vs. intradimensional, i.e., within a dimension across alternatives):
- Additive (compensatory): constant + interdimensional.
- Additive-difference (Tversky, 1969; compensatory): constant + intradimensional.
- Conjunctive (Simon's satisficing / aspiration cutoffs): variable + interdimensional.
- Elimination-by-aspects (Tversky, 1972): variable + intradimensional.

Direction is quantified from single-step transitions: a transition is interdimensional if cell $n{+}1$ shares the alternative of cell $n$ but a new dimension, intradimensional if it shares the dimension but a new alternative, otherwise a shift. The summary index is

$$\frac{(\text{inter}) - (\text{intra})}{(\text{inter}) + (\text{intra})},$$

ranging from $-1$ (pure intradimensional) to $+1$ (pure interdimensional). Verbal protocols are segmented into short phrases (Newell & Simon, 1972) to corroborate the search-pattern inference. Design: number of alternatives $\in\{2,6,12\}$ (Exp. 1) or $\{2,4,8,12\}$ (Exp. 2), dimensions per alternative $\in\{4,8,12\}$, with values set so no alternative dominates. Exp. 1 ($n=6$, partial design) is replicated by Exp. 2 ($n=12$, full within-subjects design); Exp. 2's dispersion test uses Levene's test within a three-way ANOVA (alternatives $\times$ dimensions $\times$ subject).

## Data
None external — original lab data. Exp. 1: 6 paid college-age subjects, 3 task cells each. Exp. 2: 12 paid subjects, all 12 cells across three 1-hour sessions within a week. Stimuli are constructed apartment profiles on dimensions such as rent, noise level, cleanliness, distance from campus, landlord attitude.

## Key findings
- **Mean percentage of available information searched falls as complexity rises** — both with more alternatives (Exp. 2 means: .702, .590, .488, .480 for 2/4/8/12 alternatives) and more dimensions (.732, .551, .413 for 4/8/12 dimensions), even though absolute information acquired increases.
- **Two alternatives → compensatory, constant search.** Every subject searched the same amount on each of the two options; protocols show explicit trade-off reasoning ("is it worth spending that extra \$30 a month..."). Subjects split between interdimensional (additive) and intradimensional (additive-difference) styles.
- **Many alternatives → variable, selective search consistent with noncompensatory rules.** The amount searched varied across alternatives (Levene/ANOVA main effect of number of alternatives $F(3,33)=12.36$, $p<.01$; dimension effect and interaction n.s.). Protocols reveal early elimination on single dimensions (e.g., reject any apartment with high noise, or with poor landlord attitude).
- **Chosen alternative is the most-searched.** In 11/12 (Exp. 1) and 99/108 (Exp. 2) multialternative cells, the selected option had the maximum (or next-to-maximum) information searched — consistent with surviving an elimination process.
- **Evidence of strict elimination-by-aspects** (all remaining options scanned on one dimension before moving on) in 33 of 108 multialternative patterns, plus a documented *phased* strategy: EBA to prune the set, then a compensatory additive-difference comparison between the final two.
- **Robust individual differences** in inter- vs. intradimensional style; differences persisted across sessions.

## Contribution
Provides early, direct behavioral evidence for *contingent / adaptive decision making*: the four classic choice models are reframed not as competing universal theories but as complementary "subroutines" of a general choice program, called under control conditions set by task structure. Methodologically, it imports process-tracing (information search + verbal protocols) from cognitive psychology and human problem solving (Newell & Simon, 1972) into preferential choice, demonstrating that observable choice outcomes underdetermine the underlying process — the same choice can arise from different mechanisms, so algebraic models capture only "surface form."

## Limitations & open questions
- **Tiny samples** (6 and 12 subjects), hypothetical apartments, no real stakes; generality of the strategy-switching threshold is untested.
- **Search direction explanation is speculative**: Payne conjectures inter- vs. intradimensional preference reflects how a person *encodes* attribute knowledge — object-keyed "Apartment A (rent, \$140)" vs. property-keyed "rent (Apartment A, \$140)" — but calls for research on the heuristics by which people set up a storage format for a decision problem.
- **Process inference is indirect**: search patterns are consistent with, but do not uniquely identify, a given model (conjunctive vs. EBA both imply variable search).
- **Explicit next step**: build a computer program to *simulate* the observed phased, complexity-contingent behavior (work the author reports as underway).
- Verbal reports may mislead, though concurrent ones less so than retrospective ones.

## Connections
The four models anchor much of choice theory: Tversky (1969) on the additive-difference model and intransitivity, [[@Tversky1972|Tversky (1972)]] on elimination-by-aspects, Simon (1957) on satisficing, and the conjunctive/noncompensatory tradition (Coombs, 1964; Dawes, 1964; Einhorn, 1970, 1971). The method extends Newell & Simon (1972) on human problem solving and verbal protocols, and the eye-fixation process tracing of Russo & Rosen (1975). It sits alongside Slovic & Lichtenstein (1971) and Lichtenstein & Slovic (1973) on preference reversals and the limits of algebraic judgment models, and Wright (1975) on simplifying-vs-optimizing consumer strategies. This paper is the empirical seed of Payne, Bettman & Johnson's later "adaptive decision maker" program, and connects to modern economic work on stochastic/heuristic choice and bounded rationality — e.g., [[@Manzini2007|Manzini & Mariotti (2007)]] on sequentially rationalizable choice and rationalization by multiple criteria, and the information-search / attention literature on costly information acquisition.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
