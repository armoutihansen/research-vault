---
citekey: Sprumont2000
title: On the Testable Implications of Collective Choice Theories
authors: ["Sprumont, Yves"]
year: 2000
type: journalArticle
doi: 10.1006/jeth.2000.2657
zotero: "zotero://select/library/items/JFASC4KR"
pdf: /Users/jesper/Zotero/storage/D998CD9E/Sprumont2000.pdf
tags: [literature]
keywords: [revealed-preference, collective-choice, nash-rationalizability, pareto-efficiency, testable-implications, game-forms]
topics: ["[[incomplete-preferences-choice-deferral]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We analyze collective choices in game forms from a revealed preference viewpoint. We call the joint choice behavior of n agents Nash- (respectively, Pareto-) rationalizable if there exist n preferences over the conceivable joint actions such that the joint actions selected from each game form coincide with the Nash equilibria (respectively, the Pareto optima) of the corresponding game. In the two-agent case, we show that every deterministic joint behavior which is Nash-rationalizable is also Pareto-rationalizable. The converse is false. We further identify general necessary and sufficient conditions for Nash-rationalizability of an n-agent joint choice behavior. We also define and characterize partial versions of the Nash- and Pareto-rationalizability requirements. Journal of Economic Literature Classification Numbers: C72, C92.

## Summary

Sprumont extends the abstract revealed-preference program (Arrow, Sen, Chernoff) from individual choice to *collective* choice in game forms. He observes only a joint choice function $f$ that records, for each Cartesian-product set of feasible joint actions $B = B_1 \times \cdots \times B_n$, the joint actions the agents actually select. The question: which observed behaviors are consistent with the agents playing Nash equilibria (noncooperative) versus selecting Pareto optima (cooperative), for *some* fixed underlying preferences? The paper's headline results are (i) a surprising equivalence in the two-agent deterministic case — Nash-rationalizability implies Pareto-rationalizability but not conversely — and (ii) a clean axiomatic characterization of $n$-agent Nash-rationalizability via two persistence conditions, plus partial-rationalizability variants.

## Research question

What are the *testable implications* of the Nash-equilibrium and Pareto-optimality hypotheses for collective choice, when preferences are unobservable and only assumed complete and transitive (no further structure)? Equivalently: given observed joint choices across varying feasible sets, what observable conditions are necessary and sufficient for the existence of $n$ preferences rationalizing the data as Nash equilibria (or Pareto optima) of the induced game forms? And how do the noncooperative and cooperative restrictions compare?

## Method / identification

Pure theory / axiomatic characterization. The primitives: finite conceivable-action sets $A_i = \{1,\dots,m_i\}$, joint actions $a \in A = \prod_i A_i$, and the domain $\mathcal{A}$ of nonempty Cartesian-product subsets of $A$. A **joint choice function** $f$ assigns to each $B \in \mathcal{A}$ a nonempty $f(B) \subseteq B$; $f$ is *deterministic* if every $f(B)$ is a singleton.

- $f$ is **Nash-rationalizable** if there exist complete, transitive preferences $\succeq_1,\dots,\succeq_n$ on $A$ such that for every $B$, $f(B)$ equals the set of pure-strategy Nash equilibria of the game $(B,\succeq_1,\dots,\succeq_n)$.
- $f$ is **Pareto-rationalizable** if those preferences instead make $f(B)$ equal the set of Pareto-efficient joint actions of $(B,\succeq_1,\dots,\succeq_n)$.
- $f$ is **team-rationalizable** if a *single* preference $\succeq$ has $f(B) = \arg\max$ of $\succeq$ over $B$ for all $B$.

Key constructions: a "threatens" relation $\rhd$ where $a \rhd b$ iff $a,b$ lie in a common line (a row or column, i.e. all but one agent's action fixed) and the relevant agent strictly prefers $a$; acyclicity of $\rhd$ drives Theorem 1. The $n$-agent characterization rests on two axioms. Writing $B \vee B' = \prod_i (B_i \cup B_i')$ for the smallest Cartesian set containing $B \cup B'$:

- **Persistence under Expansion:** for all $B,B'$, $f(B) \cap f(B') \subseteq f(B \vee B')$.
- **Persistence under Contraction:** for $B' \subseteq B$, $f(B) \cap B' \subseteq f(B')$; and if $B$ lies in a line and $f(B) \cap B' \neq \varnothing$, then $f(B') \subseteq f(B)$.

Proof techniques are standard abstract-choice machinery: constructing incomplete preferences whose Nash equilibria match $f$, proving transitivity, then completing via Hansson's extension theorem. Lemma 2 (acyclicity of $\rhd$ when every subgame has a unique Nash equilibrium) is flagged as potentially of independent interest to game theorists.

## Data

None — this is a pure-theory paper. Motivation is empirical (household-behavior revealed preference à la Chiappori; general-equilibrium tests à la Brown–Matzkin), and the framework is built so that joint choice data *could* in principle be confronted with the conditions, but no data are analyzed.

## Key findings

- **Theorem 1 / 1′:** A deterministic two-agent joint choice function that is Nash-rationalizable is also Pareto-rationalizable (equivalently, team-rationalizable). So any deterministic two-agent behavior with no cooperative explanation has no noncooperative (Nash) explanation either. The converse is **false** (Fig. 2: Pareto-rationalizable but not Nash-rationalizable).
- **Lemma 1:** A deterministic two-agent $f$ is Pareto-rationalizable iff it is team-rationalizable (a single shared preference suffices).
- **Non-robustness:** Theorem 1 fails without determinism, and fails for $n \ge 3$ even with determinism — explicit three-agent counterexample with a Pareto-blocking cycle $\,(1,1,1)\rhd_2(1,2,1)\rhd_1(2,2,1)\rhd_3 \cdots$.
- **Theorem 2:** An $n$-agent $f$ is Nash-rationalizable iff it satisfies Persistence under Expansion *and* Persistence under Contraction. These two axioms are independent. This improves on Yanovskaya's earlier result by removing an auxiliary weak-rationalizability assumption.
- **Theorem 3:** $f$ is *partially* Nash-rationalizable in strict preferences iff for every $B$, every $b^* \in f(B)$, every agent $i$, and every $b_i \in B_i$: $f(\{b_i^*,b_i\} \times \prod_{j\neq i}\{b_j^*\}) = \{b^*\}$ — i.e. local two-action deviations confirm $b^*$.
- **Proposition 1:** Every joint choice function is partially Pareto-rationalizable in strict preferences (let agents 2,…,n be completely antagonistic to agent 1, making every action efficient). Cooperative behavior in this abstract sense thus has *no* testable content in the partial/strict form — sharply unlike structured models such as Chiappori's.

## Contribution

First general, structure-free characterization of the testable implications of Nash equilibrium for collective choice, isolating the empirical content of an equilibrium concept *separately* from preference assumptions (most experimental work tests joint hypotheses). It establishes that noncooperative and cooperative hypotheses impose *genuinely different* falsifiable restrictions, exhibits the unexpected Nash-implies-Pareto nesting in the deterministic two-agent case, and supplies a self-contained axiom system (two persistence conditions) usable as a basis for revealed-preference tests of game-theoretic behavior.

## Limitations & open questions

The paper explicitly lists several open problems (Section 4 and throughout):

- **Full Pareto-rationalizability is uncharacterized.** Necessary conditions (i)–(iii) are given, but they are insufficient because an $n$-agent Pareto relation is a quasi-ordering yet not every quasi-ordering is a Pareto relation. Characterizing the $n$-agent Pareto relations is the missing step.
- **Missing observations.** When $f$ is observed only on a strict subset $\mathcal{A}' \subset \mathcal{A}$ (incomplete joint choice function), the modified persistence conditions remain necessary but are no longer sufficient (explicit counterexample). No characterization is provided.
- **Mixed strategies.** Nash-rationalizability uses only pure strategies, so it is very strong (pure NE may not exist). The testable implications of *mixed*-strategy Nash equilibrium are open; Sprumont sketches three families of restrictions (product-of-marginals, support relations across subforms, and quantitative inequalities among distributions) but full necessary-and-sufficient conditions remain unknown.
- **Other solution concepts.** The core, subgame-perfect equilibrium (partly addressed by Zhou–Ray), and other cooperative/noncooperative concepts could be analyzed analogously.
- **Economic structure.** The model is fully abstract; embedding "economic flesh" (e.g. an outcome function with structural restrictions, varying across observations, as in oligopoly) is proposed as a richer alternative framework.

## Connections

The paper is the collective-choice analogue of Arrow–Sen–Chernoff abstract individual revealed preference; Arrow's choice axiom reappears restricted to "lines." It builds directly on **Yanovskaya** (Nash and strong-Nash rationalizability, source of Persistence under Expansion in "finite closure" form) and **Zhou and Ray** (subgame-perfect equilibrium; their sufficiency result for partial strict Nash-rationalizability in the deterministic case). The empirical motivation comes from the collective-household revealed-preference program of **Chiappori** and **Browning–Chiappori**, and from **Brown and Matzkin**'s revealed-preference tests of general equilibrium (extending **Afriat**). Schwartz's and Sen's theorems on quasi-transitive/weak rationalization of standard choice functions are invoked for the Pareto necessary conditions, and Hansson's extension theorem for the completeness step. The acyclicity lemma connects to the thin literature on pure-strategy Nash equilibria (Shapley; McLennan).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
