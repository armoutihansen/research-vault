---
citekey: Manzini2013
title: Two-stage threshold representations
authors: ["Manzini, Paola", "Mariotti, Marco", "Tyson, Christopher J."]
year: 2013
type: journalArticle
doi: 10.3982/TE1048
zotero: "zotero://select/library/items/AL8E77L6"
pdf: /Users/jesper/Zotero/storage/Q2YWHP4H/Manzini2013.pdf
tags: [literature]
keywords: [revealed-preference, choice-theory, threshold-representation, limited-consideration, satisficing, bounded-rationality, axiomatic-choice]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We study two-stage choice procedures in which the decision maker first preselects the alternatives whose values according to a criterion pass a menu-dependent threshold and then maximizes a second criterion to narrow the selection further. This framework overlaps with several existing models that have various interpretations and impose various additional restrictions on behavior. We show that the general class of procedures is characterized by acyclicity of the revealed "first-stage separation relation."

## Summary
This short theory paper isolates the behavioral content of a broad class of two-stage choice procedures. A decision maker first preselects every alternative whose *primary criterion* value clears a *menu-dependent threshold*, then maximizes a *secondary criterion* over the survivors. Manzini, Mariotti, and Tyson show that a choice function admits such a "two-stage threshold" (TST) representation if and only if a single behavioral relation, the *first-stage separation relation* $F$, is acyclic. The headline message is deflationary: the TST structure has surprisingly little empirical content on its own. For single-valued choice functions it imposes no restriction whatsoever, so the more specialized consideration/awareness/satisficing models that nest within it derive their predictive force from their *extra* axioms, not from the threshold architecture itself.

## Research question
What behavioral restrictions on a choice function $C$ are implied by the assumption that choices arise from a two-stage threshold procedure, *independently* of any additional structure imposed by more specific models (limited consideration, revealed attention, satisficing)? Equivalently: what is the exact empirical content of the TST representation, and how much of the bite of nested models comes from the representation versus from their supplementary axioms?

## Method / identification
Pure axiomatic revealed-preference theory; no data, no estimation. Fix a nonempty finite set of alternatives $X$ and a domain of menus $D \subseteq 2^X \setminus \{\emptyset\}$ (with all singletons in $D$). A choice function $C : D \to 2^X$ satisfies $C(A) \subseteq A$ and is possibly multi-valued.

A **TST representation** is a profile $\langle f, \theta, g\rangle$ with primary criterion $f : X \to \mathbb{R}$, threshold map $\theta : D \to \mathbb{R}$, and secondary criterion $g : X \to \mathbb{R}$ such that, defining the threshold set $\Gamma(A\mid f,\theta) = \{x \in A : f(x) \ge \theta(A)\}$,
$$C(A) = \arg\max_{x \in \Gamma(A\mid f,\theta)} g(x) \quad \text{for all } A \in D.$$
So stage one keeps alternatives above the (choice-problem-specific) bar; stage two maximizes $g$ over them.

Identification proceeds through behavioral relations derived from $C$:
- **Separation** $x\, S\, y$: some menu $A$ has $x \in C(A)$ and $y \in A \setminus C(A)$. Under a TST representation $x\, S\, y$ implies $f(x) > f(y)$ **or** $g(x) > g(y)$ (the split happens at *some* stage).
- **Togetherness** $x\, T\, y$: some menu has $x, y \in C(A)$ jointly chosen; this forces $g(x) = g(y)$.
- **Extended togetherness** $E$: the transitive closure of $T$; since $T$ is reflexive and symmetric, $E$ is an equivalence relation whose classes act like revealed indifference sets and on which $g$ is constant.
- **First-stage separation** $x\, F\, y$ iff $x\, E\, y$ **and** $x\, S\, y$: a separation between two alternatives in the same $g$-indifference class, which therefore *must* be attributed to stage one ($f(x) > f(y)$).

The sufficiency proof is constructive plus Szpilrajn. Given $F$-acyclicity: set $g$ constant on each $E$-class (ordering classes arbitrarily via a linear order on the quotient); define $x\, Q\, y$ iff $x\, F\, y$ or $g(x) < g(y)$; show (Lemma 1) that $Q$ is acyclic; invoke **Szpilrajn's Theorem** to extend its transitive closure to a linear order $P$, and let $f$ represent $P$; finally set $\theta(A) = \min_{x \in C(A)} f(x)$. A short argument verifies that any $y \in \Gamma(A\mid f,\theta) \setminus C(A)$ must have strictly lower $g$, so the constructed profile reproduces $C$.

## Data
None - this is a theoretical contribution. Behavioral content is examined via worked examples on three-element menus ($x,y,z$) rather than empirical observations.

## Key findings
- **Theorem (main result).** A choice function has a two-stage threshold representation if and only if the relation $F$ is acyclic (no $S$-cycle within any single $E$-equivalence class). Notably, this involves no contraction/expansion consistency, no congruence axiom, and no condition linking pairwise choices to choices from larger menus.
- **Proposition (one-stage benchmark, due to Aleskerov–Monjardet 2002).** When $g$ is constant the second stage collapses ($C(A) = \Gamma(A\mid f,\theta)$), and $C$ has a one-stage threshold representation iff the *entire* relation $S$ is acyclic. Since $F \subseteq S$, the two-stage condition is strictly weaker, quantifying how much adding a second stage relaxes the model.
- **Corollary (the deflationary punchline).** Any single-valued choice function has a TST representation. With singleton choice sets $T$, $E$, and hence $F$ are empty, so $F$-acyclicity holds trivially; one can take $g$ one-to-one and $f = -g$.
- **Illustrative examples.** Example 1 shows TST can rationalize *cyclical* binary choices ($C(xy)=x$, $C(xz)=z$, $C(yz)=y$). Example 2 shows the limit: changing $C(xyz)$ to $\{x,y,z\}$ forces $g(x)=g(y)=g(z)$, turning all separations into first-stage ones and producing the impossible chain $f(x) > f(y) > f(z) > f(x)$.

## Contribution
The paper is the first to study the two-stage threshold class *in isolation* and to pin down its exact empirical content with one transparent axiom. Its broader payoff is diagnostic: several prominent bounded-rationality models are TST special cases under specific readings of $\langle f, \theta, g\rangle$, and the result lets one locate where each model's predictive power actually resides. (i) **Lleras–Masatlioglu–Nakajima–Ozbay (2010)** limited consideration: $f$ is consideration propensity, $g$ is utility, and the extra force comes from a *monotone* threshold ($A \subseteq B \Rightarrow \theta(A) \le \theta(B)$). (ii) **Masatlioglu–Nakajima–Ozbay (2012)** revealed attention: $f,\theta$ govern awareness, $g$ is utility, with an "attention filter" condition. (iii) **Tyson (2011)** salience/satisficing: here $f$ is *utility* and $\theta$ returns satisfaction levels while $g$ encodes salience, plus an "expansiveness" restriction. The interpretive contrast is sharp - in (i)-(ii) the *secondary* criterion is the welfare-relevant object, whereas in (iii) it is the *primary* criterion. Because the bare TST structure is so permissive (vacuous in the single-valued case), the authors conclude these models get "most of their logical strength not from the representation itself, but rather from the additional restrictions they impose."

## Limitations & open questions
- **Vacuity under single-valuedness.** The corollary means the framework predicts nothing for deterministic choice; any single-valued $C$ fits. Useful empirical content requires either multi-valued choice data or supplementary axioms - a built-in caveat for anyone hoping to test "threshold/satisficing" behavior directly.
- **Non-uniqueness of the representation.** The constructive proof's profile need not match a given target profile even ordinally (footnote 4), so the components $f$, $\theta$, $g$ are not identified; welfare and attention interpretations are underdetermined by behavior alone.
- **Mapping additional content.** The authors frame the incremental content of richer models as "the logical gap" between $F$-acyclicity and each model's axioms (e.g., in Tyson 2011 "Weak Congruence" + "Base Transitivity" exceeds $F$-acyclicity and yields expansiveness). They do not give a general characterization of *which* extra axioms generate *which* threshold properties - an open program.
- **Scope assumptions.** Results assume a finite $X$ and a domain containing all singletons; extensions to infinite alternative spaces or restricted/limited domains are left open.

## Connections
Directly extends the threshold-choice tradition of **Aleskerov & Monjardet (2002)** and **Tyson (2008)** (cognitive constraints and the satisficing criterion), reproducing the one-stage characterization as the constant-$g$ benchmark. It provides an organizing umbrella over the limited-consideration and attention literature - **Lleras et al. (2010)**, **Masatlioglu, Nakajima & Ozbay (2012)** ("Revealed attention"), **Cherepanov, Feddersen & Sandroni (2013)** ("Rationalization"), and the "choice with frames" approach of **Salant & Rubinstein (2008)** - as well as **Tyson (2011)** on salience/satisficing. The two-stage logic connects to the authors' own **Manzini & Mariotti (2007)** "Sequentially rationalizable choice" and its noncompensatory heuristics. Methodologically it rests on classical revealed-preference machinery: **Richter (1966)** congruence (cited to note that lexicographic two-criterion maximization collapses to single-utility maximization, sharpening why thresholds behave differently) and **Szpilrajn (1930)** linear-extension theorem for the sufficiency construction.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
