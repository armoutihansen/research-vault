---
citekey: Manzini2016
title: Partial knowledge restrictions on the two-stage threshold model of choice
authors: ["Manzini, Paola", "Mariotti, Marco", "Tyson, Christopher J."]
year: 2016
type: journalArticle
doi: 10.1016/j.jmateco.2016.03.003
zotero: "zotero://select/library/items/WBG29KE4"
pdf: /Users/jesper/Zotero/storage/2YPPWWTZ/Manzini2016.pdf
tags: [literature]
keywords: [choice-theory, revealed-preference, bounded-rationality, two-stage-threshold-model, partial-knowledge, axiomatization, satisficing]
topics: ["[[limited-attention-consideration-sets]]"]
related: [Kalai2002, Manzini2007, Manzini2013, Masatlioglu2012, Salant2008, Tyson2008]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> In the context of the two-stage threshold model of decision making, with the agent's choices determined by the interaction of three "structural variables," we study the restrictions on behavior that arise when one or more variables are exogenously known. Our results supply necessary and sufficient conditions for consistency with the model for all possible states of partial knowledge, and for both single- and multi-valued choice functions.

## Summary
A short, dense revealed-preference paper. It takes the general two-stage threshold (TST) model of choice — choose $\arg\max_{x} g(x)$ among the alternatives that clear a menu-dependent threshold, $f(x)\ge\theta(A)$ — and asks a question apparently new to axiomatic choice theory: *what behavioral restrictions emerge when an observer treats one or two of the three structural variables $\langle f,\theta,g\rangle$ as known (measured, assumed, or estimated externally)?* For every strict subset of the three variables, and for both multi- and single-valued choice functions, the authors provide necessary-and-sufficient axioms. The general unconstrained model is essentially unfalsifiable, so all the empirical bite comes from combining choice data with known components. The full grid of seven characterizations is summarized in two figures (Fig. 1 multi-valued, Fig. 2 single-valued).

## Research question
Given a multiple-component model of choice, how does the testable content change when an outside observer can treat some components as exogenously known? Concretely, for each strict subset $S\subsetneq\{f,\theta,g\}$ of the TST structural variables: what are the necessary and sufficient conditions on observed choice data $C$ for the existence of a TST representation that agrees with the prescribed values of the variables in $S$ while leaving the others free?

## Method / identification
The object is a choice function $C:\mathcal{D}\to\mathcal{A}$ on a finite alternative set $X$, with menus $\mathcal{D}\subseteq\mathcal{A}=2^X\setminus\{\emptyset\}$ and $C(A)\subseteq A$. The TST representation is a profile $\langle f,\theta,g\rangle$ with primary criterion $f:X\to\Re$, threshold map $\theta:\mathcal{D}\to\Re$, secondary criterion $g:X\to\Re$, such that for the first-stage survivor set $\Gamma(A\mid f,\theta)=\{x\in A:f(x)\ge\theta(A)\}$ one has
$$C(A)=\arg\max_{x\in\Gamma(A\mid f,\theta)} g(x).$$
The identification engine is a family of revealed binary relations built from $C$ and the known variables, plus the requirement that these relations contain no self-contradiction. The base relations (from [[@Manzini2013|Manzini–Mariotti–Tyson 2013]]) are: separation $xSy$ (some menu has $x$ chosen, $y$ available-but-rejected); togetherness $xTy$ (both chosen from some menu); extended togetherness $xEy$ (transitive closure of $T$, which under the model forces $g(x)=g(y)$); and first-stage separation $xFy$ iff $xEy$ and $xSy$.

The method, stated explicitly by the authors, is: use the data plus the known variable(s) to infer second-stage (or first-stage) superiority, find every way that inference could be self-contradictory, and write axioms ruling those out — necessary by construction, and sufficient once the search for contradictions is exhaustive (sufficiency proofs are the work). The recurring device is a *known-variable-indexed strict superiority relation* $H_\bullet$ and its weak chain-closure $W_\bullet$ (links via $H_\bullet$ or $E$), with the characterization typically a Richter-style congruence axiom $xW_\bullet y\Rightarrow\neg[yH_\bullet x]$. Sufficiency proofs build an explicit representation: collapse to $E$-equivalence classes $K(x)$, define an acyclic order $\gg$ on classes, extend to a linear order via Szpilrajn's Theorem, and read off $g$ (or $f$); proofs are chained non-consecutively (3.18 first, then 3.5 and 3.12, then 3.16, 3.9, 3.19), with "more known" results bootstrapping "less known" ones.

## Data
None — this is pure axiomatic decision theory. "Data" appears only as abstract choice functions $C$ and small finite counterexamples (e.g., $f(x)=1,f(y)=2,f(z)=0$, $C(xy)=x$, $C(xz)=z$, $C(yz)=yz$ in Example 3.3) used to show a relation must be ruled out.

## Key findings
Baseline (no known variable, from prior work): **Theorem 2.5** — $C$ has a TST representation iff $F$ is acyclic; and **Proposition 2.6** — every single-valued $C$ has a TST representation (the model is vacuous on single-valued data). So all testable content requires partial knowledge.

One known variable (multi-valued):
- **Theorem 3.5** (known $f$): with $xH_f y$ iff $f(y)\ge f(x)$ and $xSy$, representation exists iff $xW_f y\Rightarrow\neg[yH_f x]$.
- **Theorem 3.9** (known $\theta$): with critical threshold $M(y\mid\theta)=\max\{\theta(A):y\in C(A)\}$ and $xH_\theta y$ iff some $A$ has $M(y\mid\theta)\ge\theta(A)$, $x\in C(A)$, $y\in A\setminus C(A)$, representation exists iff $xW_\theta y\Rightarrow\neg[yH_\theta x]$.
- **Theorem 3.12** (known $g$): with $xH_g y$ iff $g(y)\ge g(x)$ and $xSy$, representation exists iff $H_g$ is acyclic *and* $xEy\Rightarrow g(x)=g(y)$.

Two known variables (multi-valued):
- **Theorem 3.16** (known primary profile $\langle f,\theta\rangle$): with $xH_{f\theta}y$ iff some $A$ has $f(y)\ge\theta(A)$, $x\in C(A)$, $y\in A\setminus C(A)$, representation exists iff $xW_{f\theta}y\Rightarrow\neg[yH_{f\theta}x]$ *and* $f[C(A)]\ge\theta(A)$. (Notably this reduces to Richter's classical revealed-preference exercise, since the survivor sets $\Gamma(A\mid f,\theta)$ are then observable surrogate menus.)
- **Theorem 3.18** (known $f,g$): representation exists iff $xH_f y\Rightarrow g(x)>g(y)$ *and* $xEy\Rightarrow g(x)=g(y)$.
- **Theorem 3.19** (known $\theta,g$): representation exists iff $xH_\theta y\Rightarrow g(x)>g(y)$ *and* $xEy\Rightarrow g(x)=g(y)$.

Single-valued specialization (Section 4): since $T,E,F$ are empty for single-valued $C$, the $xEy\Rightarrow g(x)=g(y)$ clauses vanish and congruence collapses to plain acyclicity. **Propositions 4.1–4.6**: one known variable each gives a single acyclicity condition ($H_g$, $H_f$, $H_\theta$ acyclic respectively, 4.1/4.4/4.5); $\langle\cdot,\cdot,g\rangle$ adds nothing beyond acyclicity, while known $\langle f,g\rangle$ or $\langle\theta,g\rangle$ become consistency tests $xH_f y\Rightarrow g(x)>g(y)$ / $xH_\theta y\Rightarrow g(x)>g(y)$ (4.2/4.3), and known $\langle f,\theta\rangle$ requires $H_{f\theta}$ acyclic plus $f[C(A)]\ge\theta(A)$ (4.6). The figures also display the logical entailments: discarding knowledge of a variable maps a stronger characterization to a weaker one (e.g., 3.18 → 3.5 by dropping $g$, or → 3.12 by dropping $f$).

## Contribution
Two things. First, methodologically, the paper *introduces the partial-knowledge testing question itself* for multiple-component choice models — distinct from the usual "is $C$ consistent with the model" question, it asks consistency conditional on externally fixing components. Second, it delivers the complete, interpretation-free grid of necessary-and-sufficient axioms for the TST model across all states of partial knowledge and both choice-function types, deliberately favoring no single interpretation (the TST framework nests limited-attention/consideration-set models à la Lleras et al. and Masatlioglu et al., and satisficing à la Tyson/Simon depending on how $f,\theta,g$ are read).

## Limitations & open questions
- The framework assumes **independence of components**: knowing one structural variable places no constraint on the others (Footnote 8). The authors flag that interpretations imposing joint restrictions break this — e.g., Tyson's (2015) "expansiveness" links $f$ and $\theta$, or $\theta(A)$ could be the mean $|A|^{-1}\sum_{x\in A}f(x)$ of available $f$-values, in which case one variable determines another. Incorporating such dependences is left open.
- Single-valuedness buys simplicity "at the cost of substantial generality" — an explicit tradeoff rather than a result.
- The discussion (Section 5.2) poses partial-knowledge questions for **other models** as project hooks: (i) a variant of the rational shortlist method (RSM, Manzini–Mariotti 2007) where stage one removes non-$\succ$-maximal alternatives and stage two optimizes $g$ — known $\succ$ resembles Theorem 3.16, but known $g$ "poses more of a challenge," requiring axioms that infer the unknown $\succ$ from $C$ and $g$ (a first step is given in Footnote 16); (ii) [[@Salant2008|Salant–Rubinstein (2008)]] salient consideration functions $C(A)=\bigcup_{i=1}^{n}\{x\in A:\forall y\in A\,\neg[yP_i x]\}$ — restrictions from knowing $n$ or some $P_i$; (iii) [[@Kalai2002|Kalai–Rubinstein–Spiegler (2002)]] rationalization by multiple rationales. Whether the $H_\bullet/W_\bullet$-and-congruence technique transfers is conjectural.

## Connections
Directly builds on [[@Manzini2013|Manzini, Mariotti & Tyson]] (2013, *Theoretical Economics*), which introduced and characterized the unconstrained TST model (Theorem 2.5 / Prop 2.6 are theirs). The proof machinery is classical revealed-preference theory: Richter (1966) congruence/revealed-preference, with Theorem 3.16 an explicit corollary of Richter when the whole primary profile is observed; Szpilrajn (1930) order-extension is the workhorse for every sufficiency proof. The TST model's interpretations connect it to the limited-consideration literature (Lleras, Masatlioglu, Nakajima, Ozbay 2010; [[@Masatlioglu2012|Masatlioglu, Nakajima, Ozbay 2012]] "Revealed attention") and to satisficing (Simon 1955; [[@Tyson2008|Tyson 2008]], 2015). The open-problem models cited are [[@Manzini2007|Manzini & Mariotti (2007)]] sequentially rationalizable / rational shortlist methods, [[@Salant2008|Salant & Rubinstein (2008)]] choice with frames, and [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]] multiple rationales — all multiple-component models to which the partial-knowledge program might extend.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
