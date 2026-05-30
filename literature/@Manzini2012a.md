---
citekey: Manzini2012a
title: "Categorize Then Choose: Boundedly Rational Choice and Welfare"
authors: ["Manzini, Paola", "Mariotti, Marco"]
year: 2012
type: journalArticle
doi: 10.1111/j.1542-4774.2012.01078.x
zotero: "zotero://select/library/items/MA5HWZYM"
pdf: /Users/jesper/Zotero/storage/8N85TY8N/Manzini2012.pdf
tags: [literature]
keywords: [categorization, bounded-rationality, revealed-preference, menu-effects, choice-theory, welfare-analysis, wwarp]
topics: []
related: [Bernheim2009, Chambers2012, Eliaz2011a, Mandler2012, Manzini2007, Samuelson1938, Tyson2008]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We propose a boundedly rational model of choice where agents categorize alternatives before choosing. The model explains some behavioral anomalies, and it is fully characterized by a property of choice data: a categorizer can never exhibit certain patterns of “revealed preference reversals”. This model offers clues on the problem of making welfare judgements in the presence of boundedly rational agents.

## Summary
Manzini and Mariotti model a decision maker who, facing a complex menu, first eliminates alternatives belonging to "shaded" (psychologically dominated) categories and then maximizes a preference over the survivors — Categorize Then Choose (CTC). The procedure uses just two binary relations (a shading relation on sets of alternatives and a preference on alternatives), yet it rationalizes both elementary failures of rationality — pairwise cycles and menu dependence — that richer sequential-rationalizability models cannot jointly handle. CTC choice is exactly characterized by Weak WARP (WWARP), giving a single nonparametric test. The paper closes with a careful discussion of how categorization complicates, but also partly illuminates, welfare analysis for boundedly rational agents.

## Research question
Can a tractable two-relation model grounded in the cognitive operation of categorization explain the main observable violations of rational choice (both pairwise cycles and menu effects), be sharply characterized by a falsifiable axiom on choice data, and yield disciplined welfare judgments when the standard revealed-preference relation is inconsistent?

## Method / identification
Pure axiomatic choice theory. The primitive is a single-valued choice function $\gamma:\Sigma\to X$ on a domain $\Sigma\subseteq 2^{X}\setminus\emptyset$ that contains all pairs and all triples, with $\gamma(S)\in S$. Full rationality $=$ existence of a complete order $\succeq$ with $\{\gamma(S)\}=\max(S,\succeq)$, equivalent to WARP.

The authors first decompose irrationality. The base relation is $x\succeq_\gamma y\iff x=\gamma(\{x,y\})$. **Pairwise consistency** forbids base cycles; **Condorcet consistency** says an alternative that beats every other pairwise is chosen from the whole menu. Proposition 1 shows WARP $=$ Condorcet consistency $+$ pairwise consistency — cleanly separating menu dependence from pairwise cycles.

The core model. A **shading relation** $\succ$ is an asymmetric (possibly incomplete) relation on $2^{X}\setminus\emptyset$; $R\succ S$ means category $R$ shades (eliminates) category $S$. The shaded-survivor set is
$$\max(S,\succ)=\{x\in S \mid \text{for no } R',R\subseteq S \text{ is } R\succ R' \text{ with } x\in R'\}.$$
A **preference** $\succ^{*}$ is asymmetric and complete on $X$. A choice function is **CTC** if there exist $\succ,\succ^{*}$ such that for all $S$, $\gamma(S)\in\max(S,\succ)$ and $\gamma(S)\succ^{*}y$ for every other surviving $y$. Categories may overlap (multiple criteria) and need not be disjoint or non-singleton; the baseline takes a "negative" view — the agent ignores losers.

Variants studied: (i) **salience CTC**, where the agent picks from a uniquely maximally salient category (a "positive" view, focusing on winners); (ii) **restricted CTC**, requiring shaded categories be disjoint ($R\cap S=\emptyset$) and non-degenerate ($|R\cup S|>2$); (iii) **consistent CTC** / **consistent salience CTC**, where the categorization map is stable across subsets (intersection-consistency). Welfare analysis applies the Bernheim–Rangel strict-dominance relation $xP^{*}y$ (no relevant $S$ with $x\in S$, $y=\gamma(S)$) to CTC data.

## Data
None — this is a theory paper. The empirical content is the falsifiable test (WWARP) whose effectiveness the authors validate elsewhere using experimental data from Manzini and Mariotti (2009); motivating anomalies are drawn from published findings (Redelmeier–Shafir doctors' prescriptions, Iyengar–Lepper jam choices).

## Key findings
- **Proposition 1**: WARP $\iff$ Condorcet consistency and pairwise consistency — a behavioral taxonomy of irrationality into menu dependence vs. pairwise cycles.
- **Theorem 1 (main characterization)**: $\gamma$ is CTC $\iff$ it satisfies **WWARP** — if $\{x,y\}\subseteq R\subseteq S$ and $x=\gamma(\{x,y\})=\gamma(S)\neq y$, then $y\neq\gamma(R)$. CTC accommodates both pairwise cycles and menu dependence using only two relations, exceeding the reach of the sequentially-rationalizable (RSM) model of [[@Manzini2007|Manzini and Mariotti (2007)]], which cannot generate menu effects despite arbitrarily many relations.
- **Remark 1**: WWARP is equivalent to a seemingly stronger "non-binary small set" version on this domain.
- **Proposition 2**: restricted CTC is also characterized by WWARP, and crucially its rationalizing preference $\succ^{*}$ is **unique** (pinned to the base relation), so the chosen alternative is always strictly preferred to all surviving rejected ones.
- **Salience CTC** is *not* a strengthening of CTC: Examples 1–2 show it can violate both Condorcet consistency and WWARP; its full characterization is left open.
- **Proposition 3**: a consistent CTC satisfies Expansion, hence forbids all menu dependence — collapsing to RSM-level (sequentially rational) behavior.
- **Proposition 4 / Lemma 1**: a consistent *salience* CTC satisfies IIA and is therefore **fully rational** — transitivity emerges purely from consistent category formation, with no transitivity assumed on either relation.
- **Proposition 5 (welfare comparative statics)**: when $\succ^{*}$ is welfare-relevant, enlarging a menu can lower welfare (manipulation by menu inflation), while deleting rejected alternatives never lowers welfare. A standing welfare lesson: whenever a binary choice conflicts with a choice from a larger set, the *binary* choice reveals true preference (not categorization).

## Contribution
Introduces categorization as a primitive cognitive mechanism in revealed-preference theory and delivers a parsimonious, falsifiable model (two relations, one axiom) that subsumes both canonical anomalies. It clarifies the boundary between cognition and observable behavior: consistent categorizers, checklist users, RSM users, and the rationalization model of Cherepanov, Feddersen, and Sandroni are shown to be observationally equivalent to (or indistinguishable from) preference maximization or each other. The paper reframes the "identification problem" in boundedly rational welfare analysis as a potential *strength*: when several distinct two-stage models (CTC, rationalization, limited consideration) all converge — and are jointly rejectable by the single axiom WWARP — on identifying a preference-revelation mechanism, that convergence licenses treating the revealed relation as welfare-relevant.

## Limitations & open questions
- **Category formation is exogenous**: the model deliberately abstracts from *how* categories are formed and *why* one category shades another; endogenizing the shading relation is left open.
- **Salience CTC lacks a characterization** — an explicit open problem.
- **Welfare identification is unresolved**: there is no systematic procedure for deciding whether $\succ^{*}$ is a genuine preference or merely a salience ordering, nor for when the shading relation $\succ$ itself carries welfare content (the three "varieties": clear welfare component, expected/average welfare, pure attention as in Google-search ordering).
- **No systematic framework** exists for gathering and processing the extra-choice / contextual evidence needed to break observational equivalence, nor for the principled pruning of the choice domain in the Bernheim–Rangel approach.
- [[@Bernheim2009|Bernheim's (2009)]] finding that preference tests can have zero power against plausible alternatives is acknowledged to retain full force.

## Connections
Directly builds on and extends [[@Manzini2007|Manzini & Mariotti (2007)]], whose Rational Shortlist Method (RSM) and WWARP axiom are reused; CTC strictly enlarges what RSM can explain by admitting menu effects. The decomposition relates to [[@Samuelson1938|Samuelson (1938)]] WARP and the classic rationality treatments of Moulin (1985) and Suzumura (1983). It sits in the two-stage "focus and choose" literature alongside the rationalization model of Cherepanov, Feddersen, and Sandroni (2008), the revealed-attention / limited-attention model of Masatlioglu, Nakajima & Ozbay, and the limited-consideration model of Lleras et al. (2010), with which choice-by-limited-consideration is shown to be nested in CTC; [[@Eliaz2011a|Eliaz & Spiegler (2011)]] give an economic application. Sequential rationalizability extensions by Apesteguia & Ballester (2009) and the checklist procedure of [[@Mandler2012|Mandler, Manzini & Mariotti (2012)]] are contrasted. Categorization-in-economics antecedents include Rubinstein (1988) and Leland (1994) on similarity; Arad & Rubinstein (2010) on categorizing strategies. The welfare discussion engages [[@Bernheim2009|Bernheim & Rangel (2009)]], [[@Bernheim2009|Bernheim (2009)]], Green & Hojman (2008), [[@Chambers2012|Chambers & Hayashi, Rubinstein & Salant (2012)]], Sugden (2004), [[@Tyson2008|Tyson (2008)]] on salience, and Tversky (1969) on pairwise cycles.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
