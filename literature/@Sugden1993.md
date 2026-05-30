---
citekey: Sugden1993
title: An Axiomatic Foundation for Regret Theory
authors: ["Sugden, Robert"]
year: 1993
type: journalArticle
doi: 10.1006/jeth.1993.1039
zotero: "zotero://select/library/items/VW88YNMC"
pdf: /Users/jesper/Zotero/storage/QNGQDWVK/Sugden1993.pdf
tags: [literature]
keywords: [regret-theory, nontransitive-preferences, axiomatic-decision-theory, subjective-probability, menu-dependence, choice-under-uncertainty]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper, which extends previous work by Fishburn, presents a set of axioms which imply a form of regret theory. In the case of choice from two acts, these axioms are similar to those from which Savage derived expected utility theory, except that the transitivity axiom is dropped. Some of Savage′s other axioms are strengthened, and a new definition of "is as probable as" is used. These axioms are generalized to the case of choice from n acts by making preferences between any two acts contingent on the nature of the other acts in the choice problem. Journal of Economic Literature Classification Number: D81.

## Summary
Sugden gives regret theory a Savage-style axiomatic foundation. Where Bell and Loomes–Sugden took utility and probability as primitives, this paper derives both — a probability measure $\pi$ and a skew-symmetric "regret" function $\Psi$ — from axioms on preferences over acts. For pairwise choice the axioms mirror Savage's, but the general transitivity axiom is dropped and replaced by a strengthened "is as probable as" relation, recovering Fishburn's SSA/SAA representation. The decisive move is to generalize from binary preference to a *triadic* relation $f\succeq g/H$ ("choosing $f$ is at least as good as choosing $g$ from feasible set $H$"), making the ranking of any two acts contingent on the whole choice set. This yields a representation valid for feasible sets of any size and shows that regret-driven, non-transitive, menu-dependent choice can be axiomatized and is in principle recoverable from observed choices.

## Research question
Can regret theory — a theory of choice under uncertainty that does *not* require transitive preferences — be given an axiomatic foundation in the spirit of Savage, in which utility and subjective probability are *derived* from preferences over acts rather than assumed as primitives? And can this be extended beyond pairwise choice to feasible sets of arbitrary size, where the attractiveness of an act depends on the other acts available?

## Method / identification
The paper builds in three stages, all in a Savage state-space setup: $S$ is the universal event, acts $f$ are finite-valued functions from states to consequences $X$, and $xAy$ denotes the act yielding $x$ on event $A$ and $y$ otherwise.

1. **Restatement of Savage (P1–P6)** and of **Fishburn's SAA axioms** (P1*, P2, P3, P4, P5, P6*), which delete Savage's transitivity axiom P1(ii) and yield the skew-symmetric additive (SSA) representation
$$f\succeq g \Leftrightarrow \sum_E \pi(E)\,\Psi(f_E,g_E)\ge 0,\qquad \Psi(x,y)=-\Psi(y,x).$$
Under regret theory, $\Psi(f_E,g_E)=M(f_E,g_E)-M(g_E,f_E)$, where $M$ is the satisfaction from receiving $f_E$ having rejected $g_E$.

2. **Two-act regret theory.** Sugden replaces Savage's probability axiom P4 with a new axiom **P4\*** that defines "exactly as probable as", $=_R$, via *column transposition*: if disjoint events $A,B$ are equally probable, transposing their consequence columns across a pair of acts must not change the strict ranking, and must break indifference otherwise (Table I). This removes the residual transitivity axiom P1*(ii) entirely. **Theorem 1**: P1(i), P2, P2\*, P3, P4\*, P5, P6\* imply the SSA representation (2).

3. **General regret theory.** The binary relation is replaced by the triadic relation $f\succeq g/H$ over feasible sets $H$. Seven axioms **Q1–Q7** generalize the two-act axioms: Q1(i) completeness, Q1(ii) a *within-menu* transitivity ($f\succeq g/H,\ g\succeq h/H \Rightarrow f\succeq h/H$), Q2–Q5 sure-thing/probability analogues, Q6 nondegeneracy, Q7 continuity. **Theorem 2**: Q1(i), Q2–Q7 imply a unique probability measure $\pi(E)$ and a skew-symmetric $\Psi(x,y,Z)$ (unique up to a positive multiplicative constant) with
$$f\succeq g/H \Leftrightarrow \sum_E \pi(E)\,\Psi(f_E,g_E,H_E)\ge 0.$$
The choice link is **Choice Rule C3**: $f$ chosen from $H \Rightarrow f\succeq g/H$ for all $g\in H$. The probability-construction proof uses an ingenious *tiling-partition* argument (Definition 5, Lemmas 1.1–1.8): the number of equally-probable "tiles" needed to cover an event measures its probability.

## Data
None — this is a pure decision-theory paper. The only empirical object is an illustrative numerical example (Section 7, Table II) with three acts over events of probability $0.1, 0.4, 0.5$ and dollar consequences, used to demonstrate a predicted choice pattern, not to fit data.

## Key findings
- **Theorem 1:** the two-act axioms (with P4\* in place of P4) imply the SSA representation, deriving $\pi$ and skew-symmetric $\Psi$ *without any vestige of transitivity* — improving on Fishburn, who still needed P1*(ii).
- **Theorem 2:** general regret theory (Q1–Q7) yields the menu-dependent representation (4) with a unique probability measure and a skew-symmetric, context-dependent $\Psi(x,y,Z)$; here $\Psi(x,y,Z)=M(x,Z)-M(y,Z)$, with $M(x,Z)$ read as the Bernoullian utility of getting $x$ and missing out on the other consequences in $Z$.
- **Theorem 3 (observability):** despite the apparently unobservable triadic statements, if preferences satisfy Q1–Q7 and choices satisfy C3, then for each $f,g,H$ one can infer from sufficiently rich choice data whether $f\succ g/H$, $f\sim g/H$, or $g\succ f/H$. Thus the constructs are as observable as Savage's.
- **The worked example:** using Quiggin's form $\Psi(x,y,Z)=\Phi(x,y,\sup Z)$, adding an irrelevant-seeming act $h$ to $\{f,g\}$ *reverses* the choice between $f$ and $g$, violating Sen's Property $\alpha$ (the Chernoff condition). Sugden argues this is rational regret-avoidance: choosing $g$ insures against the large regret of getting nothing while $h$ would have paid $5000.

## Contribution
First fully axiomatic foundation for regret theory that (i) derives probability and the regret function from choice-based axioms rather than positing them, (ii) eliminates *all* transitivity from the pairwise theory, and (iii) extends regret theory from pairwise to arbitrary feasible sets via a triadic, menu-dependent preference relation. It thereby legitimizes systematic, regret-driven violations of transitivity and of choice-consistency (Property $\alpha$) as the output of a coherent, observable theory — a direct formal counterpart to Sugden's broader critique of consistency axioms.

## Limitations & open questions
- **Q1(ii) is not derived.** The within-menu transitivity axiom plays no role in Theorem 2 (the representation) and is only needed to link preference to choice; Sugden shows it is *consistent* with the other axioms but flags that justifying it on regret grounds is awkward, since regret was the reason for abandoning transitivity in the first place — an acknowledged tension.
- **Justifying P1\*(ii) / residual transitivity** in the two-act SAA system is similarly uncomfortable; the paper's P4\* route is offered precisely because invoking transitivity intuitions after rejecting transitivity is unattractive.
- **Continuity / infinite state space.** P6\*, Q7 force $S$ to be infinite to rule out the lexicographic case — an idealization, as in Savage.
- **Functional form of $\Psi(x,y,Z)$ left open.** The general representation pins down skew-symmetry but not how context $Z$ enters; the predictive example relies on extra "convexity"/regret-aversion assumptions (Quiggin's form) not implied by the axioms.
- **Testing menu-dependence.** Whether the predicted Property-$\alpha$ violations actually occur is posed as an empirical invitation ("I invite readers to try this problem"), not settled.

## Connections
Directly builds on **Bell (1982)** and **Loomes & Sugden (1982, 1987)** regret theory, and on **Fishburn's (1982, 1984, 1989)** nontransitive/SSA/SAA measurable utility — Sugden's two-act axioms are a refinement of Fishburn's SAA axioms with transitivity fully removed. The whole construction is a modification of **Savage (1954)**, inheriting the state–act–consequence framework and sure-thing reasoning. The menu-dependence and Property-$\alpha$ discussion connects to **Sen (1970, 1985)** on choice functions and rationalizability, and the example's functional form is from **Quiggin (1991)**. The companion theme — that consistency axioms are not constitutive of rationality — is developed in Sugden's "Why be consistent?" (Economica 1985). The empirical backdrop is the transitivity-violation and preference-reversal evidence in **Loomes, Starmer & Sugden (1989, 1991)**.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
