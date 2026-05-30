---
citekey: Tyson2015
title: Satisficing behavior with a secondary criterion
authors: ["Tyson, Christopher J."]
year: 2015
type: journalArticle
doi: 10.1007/s00355-014-0850-7
zotero: "zotero://select/library/items/7DCDNPQ2"
pdf: /Users/jesper/Zotero/storage/P7IXY383/Tyson2015.pdf
tags: [literature]
keywords: [satisficing, revealed-preference, bounded-rationality, secondary-criterion, consideration-set, behavioral-welfare, lexicographic-choice]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Using the techniques of revealed preference analysis, we study a two-stage model of choice behavior. In the first stage, the decision maker maximizes a menu-dependent binary relation encoding preferences that are imperfectly perceived. In the second, a menu-independent binary relation is maximized over the subset of alternatives that survive the first stage. This structure can support various interpretations, including those of salience effects, positive action, and surface characteristics. We characterize the model behaviorally both in ordinal form and in terms of the corresponding numerical representations.

## Summary
Tyson extends his earlier (2008) revealed-preference theory of satisficing by appending a *secondary criterion*. A decision maker (DM) first satisfices on a primary relation whose perception degrades as menus grow more complex, leaving a "pseudo-indifference" class of good-enough options; he then maximizes a fixed secondary relation over the survivors. The composite choice rule $C(A)=G(G(A,\mathbf{R}^1),R^2)$ is characterized behaviorally by exactly two axioms — *Weak Congruence* and *Base Transitivity* — and is given an equivalent numerical (satisficing-plus-threshold) representation. The same secondary criterion can be read as salience, legal positive action, or a surface characteristic, and the paper argues that *binary* choices are the reliable arbiter of welfare.

## Research question
What behavioral (revealed-preference) restrictions are implied when a boundedly rational DM first satisfices on an imperfectly perceived primary preference and then breaks the residual pseudo-indifference by lexicographically applying a second, menu-independent criterion? And how should welfare be inferred when behavior diverges from the underlying primary preference?

## Method / identification
Pure axiomatic choice theory; no data. The primitive is a choice function $C:\mathcal{D}\to\mathcal{F}$ on a domain $\mathcal{D}$ that must contain all unary/binary menus (and $X$) but is otherwise unrestricted. The model has three layers:

- **Conceptual primitive (ordinal model).** A *primary preference system* $\mathbf{R}^1=\langle R^1_A\rangle_{A\in\mathcal{D}}$ of menu-dependent complete preorders, plus a menu-independent complete-preorder *secondary relation* $R^2$. Perceived strict preference $xP^1_A y$ encodes that the DM resolves $x\succ y$ when facing menu $A$; the default relation is pseudo-indifference $xI^1_A y$. The system must be **nested** ($A\subseteq B$ and $xP^1_B y \Rightarrow xP^1_A y$ — finer discrimination on smaller menus) and **binary transitive** (true preferences, which coincide with binary perceived ones, are transitive). Choice is the two-stage operator
$$C(A)=G\big(G(A,\mathbf{R}^1),R^2\big),\qquad G(A,R):=\{x\in A:\forall y\in A,\ xRy\}.$$
- **Revealed constructs.** Since $\mathbf{R}^1,R^2$ are unobserved, Tyson defines directly/indirectly revealed primary pseudo-preferences $\hat R^{1d},\hat R^{1i}$ (a *local*, $\subseteq B$ search: $x\hat R^{1d}_B y$ if $x\in C(A)$ for some $y\in A\subseteq B$) and revealed secondary preferences $\hat R^{2d},\hat R^{2i}$ (a *global* search). Each is shown to be valid evidence of the corresponding latent preference.
- **Axioms.** *Weak Congruence* (Cond. 2.7): if $x\in C(A)$, $y\hat R^{1i}_A x$ and $y\hat R^{2i} x$, then $y\in C(A)$ — a two-stage strengthening of Richter's Congruence (it implies Sen's $\beta$). *Base Transitivity* (Cond. 2.8): $x\in C(xy)$ and $y\in C(yz)\Rightarrow x\in C(xz)$.

The sufficiency proof shows the revealed systems can substitute for the latent ones, $C=G(G(\cdot,\hat R^{1i}),\hat R^{2i})$, using Szpilrajn's extension theorem to complete $\hat R^{2i}$.

## Data
None — this is a theoretical/axiomatic paper. Worked examples on $\{w,x,y,z\}$ (Fig. 1) illustrate satisfaction and a manufactured violation of Weak Congruence.

## Key findings
- **Theorem 2.9 (ordinal characterization).** A nested, binary-transitive system of complete preorders $\mathbf{R}^1$ and a complete preorder $R^2$ with $C=G(G(\cdot,\mathbf{R}^1),R^2)$ exist **iff** Weak Congruence and Base Transitivity hold.
- **Theorem 2.11 (numerical representation).** For finite $X$, the model holds iff there is an *expansive* threshold structure $\langle f_1,\theta_1\rangle$ and $f_2:X\to\mathbb{R}$ with
$$C(A)=\operatorname*{argmax}_{x\in A\,\wedge\, f_1(x)\ge\theta_1(A)} f_2(x).$$
Expansiveness ($A\subseteq B$, $\max f_1[A]\ge\theta_1(B)\Rightarrow\theta_1(A)\ge\theta_1(B)$) is the numerical face of nestedness — larger menus carry (weakly) lower thresholds.
- **Welfare (Props. 3.2–3.7).** If the welfare order is the lexicographic composition $L^{12}$ (Def. 3.1), then $xL^{12}y\iff x\in C(xy)$ — welfare is read off binary choices (Prop. 3.2). If instead the primary criterion $R^1$ is the standard, binary data identify it only partially: $x\in C(xy)\Rightarrow xR^1_{xy}y$, and a strict base preference is genuine only when it opposes a $\hat R^{1d}_X$-ranking (Prop. 3.3). Adding *Base Univalence* ($|C(xy)|=1$, Prop. 3.6) forces $R^1$ to be a complete order so that $R^1=L^{12}$ and binary data are fully reliable (Prop. 3.7); full *Univalence* additionally makes $R^2$ a complete order (Thm. 3.9).
- **The primacy of binary problems.** When classical revealed preferences conflict across menu sizes, the model justifies favoring the smaller menu, where welfare-significant preferences are perceived at higher resolution — operationalizing Bernheim–Rangel behavioral welfare economics.

## Contribution
Adds a second, fully-perceived criterion to the one-stage satisficing model of Tyson (2008), turning residual pseudo-indifference into determinate choice and yielding a clean two-axiom characterization plus a satisficing-with-threshold numerical representation. The single formal structure unifies three interpretations — involuntary salience effects, legally mandated positive/affirmative action (tie-breaking only among "as qualified as" candidates), and lexicographic hidden-then-surface characteristics. It also supplies a principled, model-based welfare criterion grounded in binary choice.

## Limitations & open questions
- The complete-preorder assumption on perceived preferences $R^1_A$ is, by the author's own admission, debatable for a cognitively limited DM; relaxing it to allow **incompleteness of $R^1_A$ or intransitivity of $I^1_A$** (handled for one stage in Tyson 2008) and asking which results survive in two stages is "beyond the scope of the present paper."
- The numerical analysis assumes **finite $X$**; relating threshold structures to relation systems in the general (infinite) case is flagged as an open technical issue.
- **Identification gap:** when $y$ is never chosen in the presence of $x$ and no $\hat R^{1d}_X$ ranking opposes it, the model cannot attribute the non-choice to primary vs. secondary preference — full identification requires violations of classical rationality axioms.
- The proposed **extended-choice-function refinements** (conditioning $R^1(\rho)$ on a cognitive-resource endowment $\rho$, with extended nestedness in $\rho$) are sketched as opening the door to cross-resource revealed-preference deductions and comparative statics, but are not developed.

## Connections
Builds directly on Tyson (2008) one-stage satisficing and on Simon (1955). The composite operator places the model inside the **consideration-set** framework $C(A)=G(\sigma(A),R^2)$ with $\sigma=G(\cdot,\mathbf{R}^1)$, and the paper carefully shows it is *structurally unrelated* to the attention-filter model of Masatlioglu, Nakajima & Ozbay (2012), the consideration filters of Lleras et al. (2010) and Cherepanov, Feinberg & Sandbu (2013), the rational shortlist methods / categorize-then-choose of Manzini & Mariotti (2007, 2012), and Spears (2011). Lexicographic, noncompensatory structure connects to Manzini & Mariotti's sequential heuristics. The framing connection runs through Salant & Rubinstein (2008): with $R^2$ as payoff-irrelevant framing information, aggregating over frames collapses to satisficing without a secondary criterion, and their choice-from-lists satisficing is a special case of Eq. 2. Welfare methodology follows Bernheim (2009) and Bernheim & Rangel (2009), with revealed-preference roots in Richter (1966), Sen (1969, 1993), Samuelson (1938), Arrow (1959), and Rubinstein & Salant (2008); Szpilrajn (1930) supplies the extension lemma.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
