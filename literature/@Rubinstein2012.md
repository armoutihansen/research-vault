---
citekey: Rubinstein2012
title: Eliciting Welfare Preferences from Behavioural Data Sets
authors: ["Rubinstein, Ariel", "Salant, Yuval"]
year: 2012
type: journalArticle
doi: 10.1093/restud/rdr024
zotero: "zotero://select/library/items/CGUZ36TV"
pdf: /Users/jesper/Zotero/storage/BLFLFD5D/Rubinstein2012.pdf
tags: [literature]
keywords: [behavioural-welfare, preference-elicitation, distortion-function, satisficing, bounded-rationality, revealed-preference, social-choice]
topics: []
related: [Manzini2007, Mas2009, Rubinstein2006, Salant2008, Tyson2008]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> An individual displays various preference orderings in different payoff-irrelevant circumstances. It is assumed that the variation in the observed preference orderings is the outcome of some cognitive process that distorts the underlying preferences of the individual. We introduce a framework for eliciting the individual's underlying preferences in such cases and then demonstrate it for two cognitive processes—satisficing and small assessment errors.

## Summary

Rubinstein and Salant tackle behavioural welfare analysis when an individual's choices are inconsistent across payoff-irrelevant circumstances (days, frames, occasions). Rather than retreat to the coarse Pareto criterion, they posit that there is a single unobservable welfare ordering and a *distortion function* $D$ that maps each welfare ordering to the set of orderings the individual might display. Given a *behavioural data set* (a set of observed orderings), the task is to test whether the data are consistent with the conjectured cognitive process and, if so, to recover the set of welfare orderings compatible with it. They work out the machinery in full for two processes—satisficing (perfect-recall and no-recall) and small assessment errors—and sketch extensions to framed data sets (highlighting, advertising).

## Research question

When the same individual reveals different preference orderings in circumstances that an observer deems payoff-irrelevant, which ordering reflects the individual's *welfare*? More precisely: given a conjecture about the cognitive process that distorts the underlying preferences, (i) under what conditions is a behavioural data set consistent with that process, and (ii) what is the set of welfare orderings that could have generated it?

## Method / identification

The framework is purely choice-theoretic, no estimation. The welfare of the individual is an unobservable strict ordering (asymmetric, transitive binary relation) $\succ$ over a finite set $X$. The observable is a *behavioural data set* $\Lambda$, i.e. a *set* (not a vector) of orderings — anonymity over frames plus invariance to the frequency with which each ordering appears.

A *distortion function* $D$ attaches to every ordering $\succ$ the set $D(\succ)$ of orderings an individual with welfare $\succ$ might display. An ordering $\succ$ is **$D$-consistent** with $\Lambda$ if $\Lambda\subseteq D(\succ)$; the data set is $D$-consistent if some such $\succ$ exists. Rational choice is the degenerate case $D_R(\succ)=\{\succ\}$, consistent only with a singleton data set.

The identification strategy in each model is to construct an auxiliary binary relation that captures the welfare inferences the data force, then show the candidate welfare orderings are exactly its order-extensions:

- **Perfect-recall satisficing** ($D_{PR}$): alternatives are considered in a fixed order $O$; the first satisfactory one is chosen, else the welfare-best. Define the Upper Tail $UT(\succ_f)$ as the largest top segment of $\succ_f$ ordered by $O$, and Lower Tail $LT(\succ_f)=X\setminus UT(\succ_f)$. Then $a\succ_{PR}b$ if some $\succ_f\in\Lambda$ has $a\succ_f b$ and $b\in LT(\succ_f)$.
- **No-recall satisficing** ($D_{NR}$): if nothing is satisfactory, the last-considered alternative is chosen; non-satisfactory elements end up reverse-$O$ ranked. With $Z$ the $O$-minimal element, $a\succ_{NR}b$ if some $\succ_f$ has $a\succ_f Z\succ_f b$.
- **Small assessment errors** ($D_E$): $D_E(\succ)=\{\succ_f\mid a\succ b\succ c \Rightarrow a\succ_f c\}$ — only $\succ$-adjacent alternatives may swap. Define $a\succ_E b$ if some $\succ_f$ and element $x$ have $a\succ_f x\succ_f b$.

Extensions in Section 4 enrich the data to *extended* behavioural data sets $\{(\succ_f,f)\}$ pairing each ordering with a frame $f$: a highlighting distortion $D_H(\succ,f)=\{\succ_f\mid [b\succ a \text{ and } a\succ_f b]\Rightarrow a\in f\}$, and a cardinal advertising model where the agent maximizes $i(x)u(x)$ under frame $i$, reducing identification to the solvability of a system of inequalities $i(x)u(x)>i(y)u(y)$ in $|X|$ unknowns.

## Data

None — this is a theory paper. "Data" are stylized behavioural data sets (sets of orderings) in illustrative scenarios (weekday choices over $\{a,b,c\}$, ranking of political parties L/C/R, advertising/highlighting examples).

## Key findings

- **Proposition 1 (perfect recall):** if $\succ_{PR}$ is cyclic, $\Lambda$ is not $D_{PR}$-consistent; if $\succ_{PR}$ is asymmetric, $\Lambda$ is $D_{PR}$-consistent. An ordering is $D_{PR}$-consistent with $\Lambda$ iff it *extends* $\succ_{PR}$. Thus $\succ_{PR}$ is the maximal relation nested in every candidate welfare ordering. **Corollary 1** gives the uniqueness condition.
- **Proposition 2 (no recall):** $\Lambda$ is $D_{NR}$-consistent iff $\succ_{NR}$ is acyclic *and* $Z$ is the "$O$-single trough" of every ordering in $\Lambda$; the consistent orderings are exactly the extensions of $\succ_{NR}$. The welfare rank of $Z$ is never identified. The set of perfect-recall welfare orderings is a subset of the no-recall set (perfect recall imposes more restrictions).
- **Propositions 3 & 4 (small errors):** an ordering is $D_E$-consistent iff it extends $\succ_E$; consistency holds when $\succ_E$ is $\Lambda$-acyclic (no cycles of three or fewer). Proposition 4 characterizes when a *unique* welfare ordering exists.
- **Finer-than-Pareto, even reversing it:** the framework can rank alternatives the Pareto relation leaves incomparable, and (Scenario III, the $D_M$ "monotone mistakes" example) can yield welfare judgements *opposite* to Pareto — $a$ is welfare-superior to $b$ even though $b$ Pareto-dominates $a$.

## Contribution

Provides a unifying, "testable" framework for behavioural welfare analysis that sits between two extremes: the model-free Pareto/unambiguous-choice approach of Bernheim and Rangel (coarse, gets coarser with more data) and procedural-choice models that recover only fragments of preferences. By making explicit, refutable assumptions on the preference-to-behaviour map (the distortion function), the paper shows one can make *finer* welfare inferences and still characterize the full identified set tractably. It reframes individual behavioural welfare as a single-profile social-choice problem where the distortion function plays the role of the axioms, with inconsistency arising from systematic mistakes rather than aggregation of distinct individuals.

## Limitations & open questions

- The distortion function is **deterministic**: it says which orderings are *possible*, not how *likely*. The authors flag the natural extension where $D$ assigns a probability measure over orderings, enabling maximum-likelihood selection of the welfare ordering and model-fit comparison across competing cognitive processes (the Condorcet/Young/Nitzan-Paroush lineage).
- Welfare is treated as **ordinal**; some cognitive processes (e.g. advertising, Scenario V) intrinsically require **cardinal** utility, which the basic framework cannot accommodate without modification.
- Identification is often **partial** — many processes leave a set of candidate orderings rather than a unique one (e.g. $Z$ unranked under no-recall), and the paper does not give a general theory of when point identification obtains across arbitrary distortion functions.
- The framework presumes the *correct* distortion function is among the observer's conjectures; selecting/validating the conjecture itself is left open (only consistency-based refutation is offered).

## Connections

The paper is the welfare-analysis companion to [[@Salant2008|Salant and Rubinstein (2008)]] "$(A,f)$: Choice with Frames," which supplies the frame/extended-choice-function foundation, and to [[@Rubinstein2006|Rubinstein and Salant (2006)]] "A Model of Choice from Lists." It contrasts sharply with the model-free Pareto approach of Bernheim and Rangel (2007, 2009) and the rationality-distance index of Apesteguia and Ballester (2010). It is allied with the procedural bounded-rationality literature that recovers preferences from a decision procedure — [[@Manzini2007|Manzini and Mariotti (2007]]; categorize-then-choose), Cherepanov, Feddersen and Sandroni (2008, rationalization), [[@Mas2009|Masatlioglu, Nakajima and Ozbay (2009]], revealed attention), and Green and Hojman (2007). The satisficing model formalizes Simon (1955); see also [[@Tyson2008|Tyson (2008)]] and Salant (2011). The single-profile social-choice analogy draws on Roberts (1980) and Rubinstein (1984), and the suggested stochastic extension connects to Condorcet (1785), Young (1988), and Baldiga and Green (2009).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
