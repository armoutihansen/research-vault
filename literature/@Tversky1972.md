---
citekey: Tversky1972
title: "Elimination by aspects: A theory of choice."
authors: ["Tversky, Amos"]
year: 1972
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/VKJDM8B4"
pdf: /Users/jesper/Zotero/storage/HKCGBMI6/Tversky1972.pdf
tags: [literature]
keywords: [elimination-by-aspects, stochastic-choice, similarity-effect, independence-of-irrelevant-alternatives, context-dependent-choice, random-utility, luce-choice-model]
topics: ["[[context-effects-attraction-compromise]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Tversky proposes **elimination by aspects (EBA)**, a probabilistic theory in which choice is a covert sequential elimination process: each alternative is a set of *aspects*; at each stage an aspect is drawn with probability proportional to its utility weight, and every alternative lacking that aspect is removed, until one survives. EBA is the first major choice model to make the probability of choosing an option depend not just on its own value but on its similarity relations to the rival options, thereby breaking Luce's constant-ratio rule (IIA) while still implying weaker, testable regularities. It generalizes the choice models of Luce and Restle and gives a process-level account of the similarity/substitution effect later canonized as a violation of independence of irrelevant alternatives.

## Research question
What kind of probabilistic choice theory can describe choice among multidimensional alternatives while accommodating the empirical failure of *simple scalability* and *independence from irrelevant alternatives* — i.e., the fact that adding a similar alternative draws share disproportionately from its near-neighbors rather than uniformly?

## Method / identification
The paper is theoretical, building a stochastic-choice model and deriving its falsifiable consequences. Let $T$ be a finite alternative set; associate with each $x\in T$ a nonempty set $x'=\{a,b,\dots\}$ of *aspects*, with a positive scale $u$ assigning each aspect a utility weight. For $A\subseteq T$ let $A_0=\{a\mid a\in x' \text{ for some } x\in A\}$ (aspects of *some* member) and $A^0=\{a\mid a\in x' \text{ for all } x\in A\}$ (aspects shared by *all*, which never affect choice). The model's recursive (aspect-based) form is
$$P(x,A)=\frac{\sum_{a\in x'\setminus A^0} u(a)\,P(x,A_a)}{\sum_{b\in A_0\setminus A^0} u(b)},$$
where $A_a=\{x\in A\mid a\in x'\}$ are the alternatives surviving selection of aspect $a$. This expresses $P(x,A)$ as a weighted sum of the probabilities of choosing $x$ from the subsets reachable by eliminating on each of $x$'s aspects, with weights equal to the aspect-selection probabilities $u(a)/\sum u(b)$.

A central technical result is that the model need **not** presuppose a known aspect representation: Tversky gives an equivalent set-based formulation (equation 9) defined purely on subsets $A_i\subseteq T$ via a scale $U(A)=\sum_{a\in A}u(a)$, and an appendix proves equation 6 and equation 9 are equivalent (the $\{A_i\}$ partition $T_0\setminus T^0$). Hence the model's validity can be tested without knowing the underlying aspects. The empirical sections (a companion line of work) test the derived inequalities against pair- and triple-choice data from three tasks — dot patterns, applicant profiles, and gambles.

## Data
None central to the theory. The model is tested on small controlled paired/trinary-comparison experiments (Task A: dot-density patterns; Task B: applicant intelligence/motivation profiles; Task C: two-outcome gambles), with per-subject likelihood-ratio statistics and estimated overlap parameters $d$, but the contribution is the model and its representation theorems, not a dataset.

## Key findings
EBA yields several named, testable consequences (full derivations in the companion paper Tversky 1972, *J. Math. Psych.*):
- **Reduction to known models.** When aspects are pairwise disjoint, EBA collapses to **Luce's strict-utility (BTL) model**, $P(x,A)=u(x)/\sum_{y\in A}u(y)$; restricted to binary choices it coincides with **Restle's** model, $P(x,y)=u(x'\setminus y')/[u(x'\setminus y')+u(y'\setminus x')]$. EBA thus *generalizes* both.
- **Regularity.** For $x\in A\subseteq B$, $P(x,A)\ge P(x,B)$: enlarging the offered set cannot raise an option's choice probability. (Strict inequality would be violated by the similarity/record-selection example.)
- **Moderate stochastic transitivity (MST).** If $P(x,y)\ge\frac12$ and $P(y,z)\ge\frac12$ then $P(x,z)\ge\min[P(x,y),P(y,z)]$. EBA implies MST but *not* strong stochastic transitivity (the latter is essentially equivalent to simple scalability and is rejected).
- **Multiplicative inequality.** $P(x,\{y,z\})\ge P(x,y)\,P(x,z)$ (a previously unstudied property). Combined with regularity it bounds trinary probabilities: $\min[P(x,y),P(x,z)]\ge P(x,\{y,z\})\ge P(x,y)P(x,z)$.
- **Similarity effect / IIA failure.** Because shared aspects are eliminated jointly, an added alternative "hurts" similar options more than dissimilar ones, so the ratio $P(x,A)/P(y,A)$ depends on the whole set $A$ — unlike Luce's constant-ratio rule, under which it equals $P(x,y)/P(y,x)$ regardless of context. EBA also shows independent random-utility (Thurstonian) representations are too restrictive: some reasonable preference patterns are incompatible with any independent random utility model.
- **Strategic implications.** The set-dependence makes choice shares manipulable through product/menu design: a favored alternative benefits from being made easy to compare (maximize aspect overlap), a disfavored one from being made hard to compare — Tversky's "all aspirins are the same" vs. "this car is completely different" advertising contrast.

## Contribution
EBA is a landmark stochastic-choice model that reconciles a process account of deliberation with a probabilistic representation, and it is the canonical theoretical source for context-/menu-dependent choice and similarity effects in both psychology and economics. It nests Luce (BTL) and Restle as special cases, delivers an explicit hierarchy of testable axioms (regularity $\supset$ MST $\supset$ multiplicative inequality) weaker than IIA, and shows these can be checked without specifying aspects — making it empirically operational. It anticipates modern work on attribute-based, heuristic, and consideration-set choice and on the asymmetric-dominance/decoy and attraction effects.

## Limitations & open questions
Tversky is explicit that EBA "cannot be defended as a rational procedure of choice": using an aspect as an elimination criterion can discard an option whose overall (compensatory) value is higher, because elimination is noncompensatory and order-dependent on the random aspect sequence. He flags as open: (i) **conditions under which EBA well-approximates a compensatory model** and how to exploit it as a simplification/decision aid — "subjects for future investigations"; (ii) the conjectured **strong multiplicative inequality** $P(x,A\cup B)\ge P(x,A)P(x,B)$ for all $A,B\subseteq T$, left unproven; (iii) the model says nothing about *where aspect weights come from* or how aspect representations are formed, treating them as primitives; (iv) the empirical significance levels are caveated by within-subject dependence. These hooks — approximation bounds, the strong inequality, and endogenizing aspects — are natural project ideas.

## Connections
EBA extends **Luce (1959)** strict utility / BTL and **Restle (1961)** set-theoretic similarity, and responds to the critique of probabilistic-choice theories by **Luce & Suppes (1965)** that outcome structure must be modeled. It is tied to **Lancaster's (1966)** characteristics approach to demand (goods as bundles of attributes), though Lancaster is nonprobabilistic, and to lexicographic/noncompensatory rules (**Coombs 1964**, **Fishburn 1968**). It builds directly on Tversky's own **Intransitivity of Preferences (1969)** and the **lexicographic semiorder**, and is the companion of **Choice by Elimination (Tversky 1972, J. Math. Psych.)** which proves the representation results. The aspect/similarity machinery feeds Tversky's later **Features of Similarity (1977)** and the **Preference Trees / elimination-by-tree** model (Tversky & Sattath 1979). Within economics it underpins later treatments of context-dependent and menu-dependent choice, attraction/decoy effects, and consideration sets.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
