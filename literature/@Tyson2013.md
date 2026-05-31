---
citekey: Tyson2013
title: Behavioral implications of shortlisting procedures
authors: ["Tyson, Christopher J."]
year: 2013
type: journalArticle
doi: 10.1007/s00355-012-0704-0
zotero: "zotero://select/library/items/ZFBEDCEJ"
pdf: /Users/jesper/Zotero/storage/Y2Z8937P/Tyson2013.pdf
tags: [literature]
keywords: [revealed-preference, shortlisting-procedures, bounded-rationality, consideration-sets, choice-theory, lattice-theory, two-stage-choice]
topics: ["[[sequential-rationalizability-shortlists]]"]
related: [Cherepanov2013, Eliaz2011a, Manzini2007, Masatlioglu2012, Samuelson1938, Tyson2008]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We consider two-stage “shortlisting procedures” in which the menu of alternatives is first pruned by some process or criterion and then a binary relation is maximized. Given a particular first-stage process, our main result supplies a necessary and sufficient condition for choice data to be consistent with a procedure in the designated class. This result applies to any class of procedures with a certain lattice structure, including the cases of “consideration filters,” “satisficing with salience effects,” and “rational shortlist methods.” The theory avoids background assumptions made for mathematical convenience; in this and other respects following Richter’s classical analysis of preference-maximizing choice in the absence of shortlisting.

## Summary
Tyson develops an abstract, assumption-light theory that unifies the behavioral characterization of *two-stage shortlisting procedures* — models in which a menu is first pruned by an unobservable selection function $\sigma$ and a binary relation $R$ is then maximized over the survivors, so that $C=G(\sigma,R)$. The central device is a *revealed shortlisting map* $\hat{\sigma}_\Gamma$, the pointwise-smallest selection function that lies in the hypothesized class $\Gamma$ and contains the choice data. When $\langle\Gamma,\subset\rangle$ is a *complete lattice*, this minimal map exists and can serve as a surrogate menu generator, letting Richter's (1966) classical congruence analysis be transported wholesale. The result is a single "meta-characterization" (a $\Gamma$-Congruence axiom) that instantiates to consideration filters, satisficing-with-salience, rational shortlist methods, and more, with almost no per-case work beyond verifying lattice structure.

## Research question
For an unobservable two-stage choice procedure of a given structural class $\Gamma$, when is observed (possibly multi-valued) choice data consistent with *some* member of that class, and to what extent are the procedure's constituents revealed by behavior? The paper seeks one abstract necessary-and-sufficient condition covering many such classes simultaneously, free of the convenience assumptions (finiteness, full domain, single-valuedness) usual in the literature.

## Method / identification
Pure decision theory / revealed-preference axiomatics. Fix a universe $X$, menus $\mathbb{X}=\{A:A\subset X\}$, an arbitrary domain $D\subset\mathbb{X}\setminus\{\emptyset\}$, and the space $\Theta$ of *selection functions* $\xi$ with $\xi(A)\subset A$. Ordered by pointwise inclusion, $\langle\Theta,\subset\rangle$ is a complete lattice; the functions $\Theta_C=\{\xi:C\subset\xi\}$ containing the choice data $C$ form a complete sublattice. A class of procedures is identified with a subset $\Gamma\subset\Theta$ of admissible first-stage maps; $C$ is a *CP-shortlisting procedure of class $\Gamma$* if $C=G(\sigma,R)$ for some $\sigma\in\Gamma$ and complete preorder $R$ (CO- if $R$ is a complete order). The revealed shortlisting map is defined as the meet
$$\hat{\sigma}_\Gamma=\bigwedge[\Gamma\cap\Theta_C]=\bigcap_{C\subset\sigma\in\Gamma}\sigma,$$
an underestimate of the true $\sigma$. From it, $\Gamma$-revealed preference $\hat{R}_\Gamma$ is built: $x\hat{R}_\Gamma y$ iff some menu has $y\in\hat{\sigma}_\Gamma(A)$ and $x\in C(A)$ (comparisons among options *known* to be shortlisted). Identification turns on whether $\hat{\sigma}_\Gamma$ itself lies in $\Gamma$ — guaranteed (Proposition 2.3) exactly when $\langle\Gamma,\subset\rangle$ is a complete lattice. The proof of sufficiency mirrors Richter: it replaces the possibly-incomplete-intransitive $\hat{R}_\Gamma$ with a complete preorder via a Szpilrajn-embedding lemma (Lemma A.1) while preserving $C=G(\hat{\sigma}_\Gamma,R)$.

## Data
None — this is a theoretical paper. Worked numerical examples over small universes (e.g. $X=\{w,x,y,z\}$, Tables 1–3) illustrate construction of $\hat{\sigma}_\Gamma$, $\hat{R}_\Gamma$, and the failure of lattice structure for attention filters.

## Key findings
- **Proposition 2.3:** if $\langle\Gamma,\subset\rangle$ is a complete lattice then $\hat{\sigma}_\Gamma\in\Gamma$ — the existence guarantee for the revealed shortlisting map.
- **$\Gamma$-Congruence (Condition 2.12):** if $x\in C(A)$, $y\in\hat{\sigma}_\Gamma(A)$, and $y\hat{R}_\Gamma^{*}x$, then $y\in C(A)$; a natural weakening of Richter's Congruence (recovered at $\Gamma^{id}=\{\top\}$).
- **Theorem 2.13 (meta-characterization):** $\Gamma$-Congruence is *necessary* for any CP-shortlisting procedure of class $\Gamma$, and — when $\langle\Gamma,\subset\rangle$ is a complete lattice — *sufficient*.
- **Theorem 2.16 / Proposition 2.18:** the single-valued (complete-order) analogue, characterized by $\Gamma$-Congruence + Univalence, equivalently by *$\Gamma$-Anticyclicity* (all $\hat{R}_\Gamma$-cycles degenerate).
- **Applications.** Consideration/contraction filters $\Gamma^{cf}$ form a lattice with $\hat{\sigma}_{\Gamma^{cf}}(A)=\{x:\exists B\supset A,\,x\in C(B)\}$ (Props 3.2, 3.5). *Attention (Aizerman) filters* $\Gamma^{af}$ do **not** form a lattice (Example 3.7), so the meta-characterization fails — a sharp negative result. Strong- and weak-expansion filters $\Gamma^{se},\Gamma^{we}$ (satisficing with salience) are lattices with $\hat{\sigma}=G(\cdot,[R^\ell]^{*})$ and $G(\cdot,R^\ell)$ (Props 3.9–3.16). Extraction filters $\Gamma^{ef}$ (rational shortlist methods, $\sigma=G(\cdot,Q)$) are a lattice with $\hat{\sigma}_{\Gamma^{ef}}=G(\cdot,R^g)$; $\Gamma^{ef}$-Congruence implies Manzini–Mariotti's Generalized Weak WARP and Weak Expansion (Props 3.18–3.23). Justified shortlists (Mariotti) give weak-axiom filters $\Gamma^{wa}$ (Props 3.24–3.26). Strong-axiom filters $\Gamma^{sa}$ collapse behaviorally to the classical model (Prop 3.31).

## Contribution
Provides a *single* generalization of Richterian revealed-preference theory that simultaneously characterizes a whole family of bounded-rationality two-stage models, isolating **complete-lattice structure of the procedure class** as the precise condition under which such characterization is possible. It strictly generalizes prior case-by-case results (Lleras et al. 2010; Tyson 2011; [[@Manzini2007|Manzini & Mariotti 2007]]) by dropping finiteness, domain, and single-valuedness assumptions, and it yields the clean negative result that attention filters lack the structure the method requires.

## Limitations & open questions
- The framework only characterizes classes with *complete-lattice* structure; classes like attention filters fall outside it, leaving open how to characterize lattice-less procedures.
- Representations are generally **non-unique** (the shortlist-vs-second-stage ambiguity), so revelation is partial — the paper frames revelation as agreement across all valid representations rather than point identification.
- The "official" definition of $\hat{\sigma}_\Gamma$ as a greatest lower bound is unwieldy; finding explicit closed forms is left as per-application work (and for $\Gamma^{wa}$ only a sketched sequential construction is given).
- The strong-axiom case shows the model can have superfluous degrees of freedom that are behaviorally immaterial, raising the question of when added structure is genuinely identifying.

## Connections
Builds directly on Richter (1966, 1971) and the classical revealed-preference tradition of [[@Samuelson1938|Samuelson (1938)]], Houthakker (1950), Arrow (1959), Hansson (1968), and Suzumura (1976). The unified procedures are those of Lleras et al. (2010) (consideration filters), [[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay (2012)]] (attention filters), [[@Tyson2008|Tyson]] (2008, 2011) (satisficing with salience effects), [[@Manzini2007|Manzini & Mariotti (2007)]] (rational shortlist methods), and Mariotti (2008) / Clark (1988) (justified shortlists). The Aizerman/contraction conditions trace to Chernoff (1954), Sen (1969, 1971, 1977), Nash (1950), and Bordes (1976); related models appear in [[@Cherepanov2013|Cherepanov, Feddersen & Sandroni (2013)]] and [[@Eliaz2011a|Eliaz & Spiegler (2011)]]. The proof machinery rests on Szpilrajn's (1930) extension theorem.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
