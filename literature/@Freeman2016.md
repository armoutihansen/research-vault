---
citekey: Freeman2016
title: Preferred Personal Equilibrium and Choice under Risk
authors: ["Freeman, David"]
year: 2016
type: report
doi: ""
zotero: "zotero://select/library/items/HEXZCXPC"
pdf: /Users/jesper/Zotero/storage/UNSZMBI4/Freeman2016.pdf
tags: [literature]
keywords: [reference-dependent-preferences, expectations-based-reference-points, personal-equilibrium, choice-under-risk, revealed-preference, axiomatization, independence-axiom]
topics: ["[[expectations-based-reference-dependence]]"]
related: [Abeler2011, Crawford2011, Gul1991, Koszegi2006b, Loomes1986, Ok2015]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper studies the choice behavior of Kőszegi and Rabin's (2006) Preferred Personal Equilibrium (PPE) model of choice with reference-dependent preferences and expectations-based reference points. The choices under risk of leading cases of their model fail to satisfy both the Independence Axiom and the Weak Axiom of Revealed Preference (WARP). I introduce the EU-PPE model as a restriction of the PPE model in which reference-dependent preferences take an expected utility form conditional on the reference point. In a two-period choice setting, I provide a set of necessary and sufficient conditions for behavior to have an EU-PPE representation. I provide a definition of exhibiting expectations-based reference-dependence in choice, and show that in this representation such behavior is tightly tied to violations of the Independence Axiom, while a failure of WARP is sufficient but not necessary to display expectations-based reference-dependence.

## Summary
Freeman gives a revealed-preference (axiomatic) foundation for the choice content of Kőszegi and Rabin's Preferred Personal Equilibrium under risk. He defines a non-parametric EU-PPE model in which the decision-maker holds a family of reference-dependent expected-utility functions $v(\cdot\mid p)$ indexed by the reference lottery $p$, and chooses a fixed point of expectations: a lottery that is self-confirming as a reference point. Using two kinds of choice data — a commitment (CPE) ranking and ordinary non-committed menu choices — he provides necessary and sufficient axioms for an EU-PPE representation, characterizes a strengthening motivated by experiments, and shows that Independence violations, not WARP violations, are the essential behavioral signature of expectations-based reference-dependence.

## Research question
What is the behavioral (revealed-preference) content of the PPE model when applied to choice under risk, once one abstracts away from specific parametric functional forms for reference-dependent utility? Concretely: which observable patterns of choice between lotteries are equivalent to having an expectations-based, reference-dependent representation in which the reference point is determined endogenously by rational expectations about one's own choice?

## Method / identification
The paper is pure decision theory: an axiomatic representation result, not estimation or experiment. The primitive is a pair $(\succeq^?, c)$, where $\succeq^?$ is a commitment (CPE) ranking of lotteries and $c$ is a choice correspondence over menus of lotteries in a two-period setting. The DM holds reference-dependent utilities $v(\cdot\mid p)$, each taking an expected-utility (affine) form given the reference lottery $p$ and jointly continuous in $p$. Choice from a menu $D$ is the set of personal equilibria:
$$PPE_v(D)=\arg\max_{p\in D}\{v(p\mid p): v(p\mid p)\ge v(q\mid p)\ \forall q\in D\}.$$
A lottery is selected only if it is a fixed point — best against itself as reference point — and among such fixed points the CPE criterion $v(p\mid p)$ breaks ties. Because mixing a menu with a fixed lottery shifts the reference point, the model can violate the Independence Axiom; because choice is a lexicographic composition of a (possibly incomplete, intransitive) PE criterion and the CPE ranking, it can also violate WARP.

The characterization rests on axioms exploiting the interpretation of mixtures $(1-\alpha)p+\alpha q$ versus $(1-\alpha)p+\alpha r$ as a conditional choice between $q$ and $r$ when expectations are partly pinned to $p$. The four main axioms: (i) **Non-Intrinsic Preference for Commitment** — if $p$ is chosen in a small menu but dropped in a larger one for a CPE-worse lottery, then $p\succ^? q$ in the CPE ranking; (ii) **Conditional Exclusion Consistency**, a weakening of Independence; (iii) **Weak Reference Bias** — if $p$ is chosen when $q$ is available, $p$ is (approximately) chosen against $(1-\alpha)p+\alpha q$ for small $\alpha$, i.e. when the reference point is moved toward $p$; (iv) **Transitive Limit** — as $\alpha\to0$ conditional choices between $(1-\alpha)p+\alpha q$ and $(1-\alpha)p+\alpha r$ obey a transitive relation, recovering the preference between $q$ and $r$ at reference point $p$. The proof constructs, via continuity axioms, a family of EU vectors $\hat u_p$ (one per reference point) and assembles a jointly continuous $v$ consistent with $\succeq^?$.

## Data
None — this is a theoretical paper. The only "empirical" inputs are stylized two-stage choice tables (e.g. mug/pen exchange examples in the spirit of Ericson and Fuster 2011) used to illustrate the approximate testability of the axioms; no dataset is analyzed.

## Key findings
- **Theorem 1.** $(\succeq^?, c)$ satisfies axioms A1–A7 if and only if it has an EU-PPE representation consistent with $\succeq^?$ and increasing in the riskless dimension $x^?$. **Corollary 1** establishes essential uniqueness: any two continuous EU-PPE representations of the same $c$ induce the same reference-dependent preferences and the same CPE ranking.
- **Limited cycle inequalities.** Non-emptiness of the PE set for every menu ($PPE_v(D)\ne\varnothing$) holds iff $v$ satisfies the limited cycle inequalities: if $v(p_i\mid p_{i-1})>v(p_{i-1}\mid p_{i-1})$ for $i=1,\dots,n$ then $v(p_n\mid p_n)\ge v(p_0\mid p_n)$. **Proposition 1** shows the Kőszegi–Rabin linear loss-averse form satisfies them, but not all KR preferences do (e.g. $\lambda=-1$ violates loss aversion and leaves some menus with no PE).
- **Theorem 2.** Replacing Weak Reference Bias (A6) with **Strong Reference Bias** (A6': $p\in c(\{p,q\})\Rightarrow p\in c(\{p\}_\alpha\{p,q\})$), motivated by Ericson and Fuster (2011), yields an EU-PPE representation that additionally "PPE-dislikes mixtures."
- **Behavioral signature.** Expectations-based reference-dependence is defined through Independence violations; WARP violations are sufficient but not necessary for it. Independence failure is thus more fundamental than WARP failure.

## Contribution
First revealed-preference axiomatization of the PPE/EU-PPE model that treats reference points as unobserved and infers them from choice, departing from prior reference-dependence axiomatics (Sugden 2003; Masatlioglu and Ok 2005; Sagi 2006; Apesteguia and Ballester 2009) that take the reference point as observed. It clarifies the empirical content of a model used pervasively in applied work, separates Independence from WARP violations as diagnostics, and identifies the limited cycle inequalities as the condition guaranteeing well-defined equilibrium choice.

## Limitations & open questions
- The model permits WARP violations, but Freeman notes "no direct empirical test of this aspect of the model exists" — experiments are needed to learn whether a descriptive theory should allow WARP violations and whether they take the permitted forms.
- Continuity axioms (notably A7) are not exactly testable, only approximately; designing sharp experimental tests of the conditional-choice axioms is open.
- The analysis is confined to a two-period setting with a single resolution stage; extension to richer dynamic environments is left open.
- The relationship between the limited cycle inequalities and the boundaries of admissible Kőszegi–Rabin parameterizations (when PE existence fails) invites further structural work.

## Connections
Builds directly on Kőszegi and [[@Koszegi2006b|Rabin]] (2006, 2007) (PPE, CPE, reference-dependent risk attitudes) and Kőszegi (2010) (the broader PE model, of which PPE is a refinement). The author's own working paper, Freeman (2013), studies revealed-preference implications of expectations-based reference-dependence. The axiomatic comparison set includes Sugden (2003), Munro and Sugden (2003), Masatlioglu and Ok (2005, 2014), Sagi (2006), Apesteguia and Ballester (2009), and [[@Ok2015|Ok, Ortoleva and Riella (2015)]] on revealed (p)reference theory. Strong Reference Bias is grounded in the experimental evidence of Ericson and Fuster (2011). Related models of disappointment and anticipation include [[@Gul1991|Gul (1991)]], [[@Loomes1986|Loomes and Sugden (1986)]], and Delquié and Cillo (2006). Applications motivating the exercise span Heidhues and Kőszegi (2008, 2014), Herweg and Mierendorff (2013), Karle, Kirchsteiger and Peitz (2015), Pagel (2016), and the labor-supply debate of Camerer, Babcock, Loewenstein and Thaler (1997) and [[@Crawford2011|Crawford and Meng (2011)]], as well as Abeler, Falk, Götte and [[@Abeler2011|Huffman (2011)]] and Gill and Prowse (2012).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
