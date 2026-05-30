---
citekey: Baigent1996
title: Never choose the uniquely largest a characterization
authors: ["Baigent, Nick", "Gaertner, Wulf"]
year: 1996
type: journalArticle
doi: 10.1007/BF01211816
zotero: "zotero://select/library/items/3T8X2FNH"
pdf: /Users/jesper/Zotero/storage/XSQPAL4E/Baigent1996.pdf
tags: [literature]
keywords: [choice-theory, revealed-preference, social-norms, rationalizability, axiomatization, choice-function-consistency]
topics: []
related: [Sen1993]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> In this paper we characterize choice behaviour that picks the second largest element if there is a uniquely largest; otherwise, the largest elements are picked. Having defined our choice function, we offer a complete characterization of the latter in terms of pure choice function conditions. Similarities to and divergences from conventional choice theory are explained. We discuss the motivations underlying our exercise and provide several examples for the axiomatized choice behaviour.

## Summary
Baigent and Gaertner axiomatize a deliberately "badly behaved" choice rule: given a quality ordering $q$ over alternatives, an agent picks the second-largest element whenever there is a unique largest, and otherwise picks the (tied) largest elements. The motivating story is an internalized social norm — modesty, politeness, a rule of thumb ("never take the biggest piece of cake") — that supervenes on ordinary preference optimization. Although the rule violates almost all standard consistency conditions (including those, like $\alpha$ and $\gamma$, that are necessary and sufficient for rationalizability by a transitive preference), the authors show it admits a complete characterization in terms of four pure choice-function axioms, and that its induced revealed-preference relation is nonetheless transitive. The result demonstrates that "non-standard rationality" anchored in an explicit external reference can be just as fully axiomatized as conventional rational choice.

## Research question
Can choice behaviour that systematically refuses the best available option — selecting instead the next-best, except under ties — be given a complete axiomatic characterization in terms of conditions stated purely on the choice function, despite violating the classical consistency axioms that define preference-rationalizable choice? And what minimal set of such conditions exactly pins down this rule?

## Method / identification
The paper is pure axiomatic choice theory; there is no estimation or experiment. Let $X$ be a finite set of alternatives, $K$ the set of nonempty subsets, and $C$ a choice function with $C(A)\subseteq A$ and $C(A)\neq\varnothing$ for all $A\in K$. A weak order $q$ on $X$ (the "quality ordering," e.g. size, speed, brightness) has strict and indifferent parts $P_q$ and $I_q$. Writing $M(A,q)$ for the set of $q$-maximal elements of $A$, and $M^*(A,q)$ for that set when it is a singleton (the *uniquely* largest element), the central object is the choice function defined by
$$C(A) = M\bigl(A \setminus M^*(A,q),\, q\bigr) \quad \text{for all } A\in K.$$
That is: delete the unique maximum (if one exists) and choose the maximal elements of what remains; if the top is a tie, $M^*$ is empty and the rule returns the tied maxima themselves.

The authors first catalogue standard conditions — contraction property $\alpha$ (if $x\in C(T)$ and $x\in S\subseteq T$ then $x\in C(S)$), expansion property $\gamma$ (anything chosen from every set in a family is chosen from their union), property $\beta$, $\beta(+)$, $\epsilon$, and path independence $C(S\cup T)=C(C(S)\cup C(T))$ — and show the rule violates $\alpha$, $\alpha_2$, $\alpha(-)$, $\gamma$, $\beta(+)$, path independence, weak path independence, and acyclic path independence, while satisfying $\beta$ and $\epsilon$. A worked example with $x\succ y\succ z\succ w\succ v$, $S_1=\{x,y,z\}$, $S_2=\{z,w,v\}$ gives $C(S_1)=\{y\}$, $C(S_2)=\{w\}$, $C(S_1\cup S_2)=\{y\}$ but $C(C(S_1)\cup C(S_2))=C(\{y,w\})=\{w\}$, demonstrating the failure of path independence.

The identification strategy is to define a new notion: $C$ is **Non-Standard (NS) Rationalizable** iff there exists an order $q$ satisfying the displayed equation. The revealed relation is $x\,q_C\,y \iff y\in C(\{x,y\})$. Four axioms are then introduced (for $S\subseteq T$): **Axiom 3.1** (a restricted Arrow-style consistency: if $S\cap C(T)$ has at least two elements, then $C(S)=S\cap C(T)$); **Axiom 3.2** (part (i), a pairwise condition whose implication is the *reverse* of $\gamma$ — if $\{x\}=C(\{x,y\})$ and $\{x\}=C(\{x,z\})$ then $x\notin C(S)$; part (ii), the standard condition $\beta$); **Axiom 3.3** (if $C(T)=\{x\}$ is a singleton, some other $y$ is rejected in every pairwise comparison in $T$); and **Axiom 3.4** (an "equal-treatment" condition forcing acceptance-symmetry or rejection-symmetry, used solely to obtain transitivity of $q_C$).

## Data
None — this is a theoretical, axiomatic paper. The only empirical content is illustrative examples (pieces of cake in ascending size; pupils reluctant to answer first; party-goers avoiding being the most elegantly dressed or bringing the most expensive wine; residents avoiding the most luxurious car; the 1960s Volkswagen "Drive below your means" campaign).

## Key findings
- **Proposition 3.1 (uniqueness of rationalization):** If $q$ NS-Rationalizes $C$, then $q=q_C$. NS-Rationalizations are unique, and no axioms on $C$ are needed for this.
- **Proposition 3.2 (transitivity):** If $C$ satisfies Axioms 3.1, 3.2(ii), 3.3 and 3.4, then the revealed relation $q_C$ is transitive (shown by proving $xP_q^c y \,\&\, yP_q^c z \Rightarrow xP_q^c z$ and $xP_q^c y \,\&\, yI_q^c z \Rightarrow xP_q^c z$, which per Sen suffices for full transitivity).
- **Propositions 3.3 and 3.4 (representation):** Under the relevant axioms, $C(A)\setminus M(A\setminus M^*(A,q_C),q_C)=\varnothing$ and $M(A\setminus M^*(A,q_C),q_C)\setminus C(A)=\varnothing$; i.e. the axioms force $C$ to coincide with the "second-largest" rule generated by $q_C$.
- **Theorem 3.5 (main characterization):** A choice function is NS-Rationalizable if and only if it satisfies Axioms 3.1, 3.2, 3.3, and 3.4. This is a complete axiomatization of the "never choose the uniquely largest" rule in pure choice-function terms.
- A structural observation: when the maximal set is non-unique the rule actually *does* select largest (maximal) elements, so it is a "preference optimizing principle of a richer type," not a satisficing rule.

## Contribution
The paper extends a choice function mentioned by [[@Sen1993|Sen (1993)]] into a fully axiomatized object and shows, against the usual presumption, that choices violating the canonical rationalizability conditions ($\alpha$ and $\gamma$) are not beyond analysis. It operationalizes Sen's argument that the consistency of choices across subsets cannot be judged without an *external reference*: here the reference is the explicit norm/quality structure encoded in $C(A)=M(A\setminus M^*(A,q),q)$. The authors stress they study *internalized* norms (where violation costs integrity and self-respect), sharply distinguishing this from game-theoretic accounts where norm-conforming behaviour is merely strategic equilibrium play. They also argue that working with *incompletely described* alternatives (commodity bundles, tax schedules, pieces of cake) is the empirically relevant case, rather than refusing the puzzle by appeal to fully specified states of the world. Methodologically, the axioms are characterized as "anatomic" — dissecting an existing phenomenon into components — and several are shown to be close relatives of standard axioms (3.1 weakens Arrow 1959; 3.2(i) mirrors $\gamma$ in structure but reverses its implication; 3.2(ii) is $\beta$).

## Limitations & open questions
- **The $k$-th largest generalization:** the authors note it would be "mathematically tempting to axiomatize the choice of the $k$-th largest element," but they explicitly decline because they cannot formulate a *norm* that would motivate this extension.
- **The "Mother Theresa" rule** (always choose the *smallest* piece / shabbiest clothes) is dismissed as already a conventional choice function satisfying $\alpha$ and $\beta$, so it needs no new theory; for general intermediate cases the specification of motivating norms "appears rather doubtful."
- **The median element** is flagged as "really worth looking into" — its axiomatization is explicitly left to a future paper, making it the paper's clearest open project hook.
- **Single-element / empty choice sets:** the framework requires nonempty choices and side-steps the "no piece of cake chosen" case (including singleton menus $\{x\}$); they sketch but decline to pursue a fix using a dummy "don't choose" state $\bar{x}$.

## Connections
The paper sits squarely in the Sen tradition of revealed-preference and choice-consistency theory: Sen (1970, 1977, 1986) supply the standard axioms and the rationalizability result that $C$ is rationalizable by a weak order iff it satisfies $\alpha$ and $\gamma$, while Sen (1993), "Internal consistency of choice," provides both the seed choice function and the central methodological claim that consistency requires an external reference. Arrow (1959) supplies the consistency condition that Axiom 3.1 weakens. The path-independence apparatus draws on Plott (1973) and Parks (1971) (acyclic path independence and property $\epsilon$), and Bordes (1976) for the $\beta(+)$/transitive-revealed-preference link. The motivational discussion of norms and non-instrumental rationality connects to Hargreaves Heap et al. (1992) ("expressive rationality," Sugden's chapter), Sugden (1985) on why one should be consistent, and Dasgupta (1993) on norms in repeated games. The argument for treating alternatives as nonseparable incomplete descriptions invokes Machina (1991) and Malishevski (1993); Saari (1992) is contrasted on "inner" versus "internal" consistency. For a research vault on social preferences and choice, this is a foundational reference for norm-driven, non-optimizing-yet-rationalizable choice behaviour and for the technique of characterizing "anomalous" rules via an explicit external reference.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
