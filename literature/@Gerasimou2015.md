---
citekey: Gerasimou2015
title: (Hemi)continuity of additive preference preorders
authors: ["Gerasimou, Georgios"]
year: 2015
type: journalArticle
doi: 10.1016/j.jmateco.2015.03.009
zotero: "zotero://select/library/items/E298IHF4"
pdf: /Users/jesper/Zotero/storage/B39UVXN2/Gerasimou2015.pdf
tags: [literature]
keywords: [incomplete-preferences, continuity, hemicontinuity, additivity, decision-theory, order-topology, independence-axiom]
topics: []
related: [Gerasimou2013]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> It is shown that the two common notions of topological continuity for preference preorders, which require closed contour sets and a closed graph respectively, are equivalent even when completeness is not assumed, provided that the domain is a normed linear space or a topological group and the preorder is additive.

## Summary
This short note in mathematical economics reconciles two distinct topological-continuity notions for (possibly incomplete) preference preorders. A preorder is *continuous* if it is closed as a subset of the product space $X\times X$, and *hemicontinuous* if every upper and lower contour set is closed. For complete preorders these coincide (Ward 1954); for incomplete ones, continuity is strictly stronger in general. Gerasimou proves that the two coincide again once the domain carries algebraic structure (a normed vector space or a topological group) and the preorder is *additive* ($x\succeq y \Rightarrow x+z\succeq y+z$). The result is sharp: two counterexamples show hemicontinuity without continuity when additivity fails, and a companion claim ties additivity to the more familiar independence/affinity and homotheticity axioms. The motivating application is incomplete subjective-expected-value preferences à la de Finetti / Bewley / Ghirardato–Maccheroni–Marinacci.

## Research question
When completeness is *not* assumed, do mild conditions on a preference relation and/or its domain restore the equivalence between the two standard notions of continuity (closed graph vs. closed contour sets)? Equivalently: what algebraic-topological structure makes hemicontinuity suffice for full continuity of an incomplete preorder?

## Method / identification
Pure axiomatic order theory; no data or estimation. A *preordered topological space* $(X,\tau,\succeq)$ has a reflexive, transitive $\succeq$. Define upper/lower contour sets $U(x):=\{y\in X: y\succeq x\}$ and $L(x):=\{y\in X: x\succeq y\}$. The preorder is hemicontinuous if $U(x),L(x)$ are closed for all $x$; continuous if $\succeq$ is closed in $X\times X$ (equivalently its complement $\not\succeq$ has open graph). On a vector space, $\succeq$ is *additive* if $x\succeq y \Rightarrow x+z\succeq y+z$ for all $z$. The proofs proceed by elementary topology. The $(b)\Rightarrow(c)$ step is the substantive one: assuming $x\not\succeq y$, hemicontinuity gives open balls of radius $\epsilon$ around $x$ and $y$ on which non-preference persists; then for any candidate $x'\succeq y'$ inside the half-radius balls, additivity translates the pair by $v:=x-x'$ to yield $x\succeq y'+x-x'$, while the triangle inequality places $y'+x-x'$ within $B_\epsilon(y)$, contradicting $x\not\succeq y'+x-x'$. Hence $\not\succeq$ is open and $\succeq$ is continuous. The topological-group extension replaces sequences with nets and additive translation by group multiplication $x_d y_d^{-1}\succeq 1$, using only the group operation (not scalar multiplication).

## Data
None — this is a theoretical note in order topology / decision theory.

## Key findings
- **Theorem 1** (normed vector space, additive $\succeq$): the following are equivalent — (a) $\succeq$ is upper- *or* lower-hemicontinuous at $0$; (b) $\succeq$ is hemicontinuous; (c) $\succeq$ is continuous. Strikingly, hemicontinuity at the single point $0$ (in one direction) propagates to global continuity, via additive translation $y_n\succeq x \Leftrightarrow y_n - x\succeq 0$.
- **Theorem 3** (topological group $(G,\succeq)$, additive $\succeq$ with $xz\succeq yz$): same three-way equivalence, with hemicontinuity at the identity $1$ sufficing. Proved with nets, since groups need not be metrizable.
- **Claim 2**: a *lower-homothetic* preorder ($x\succeq y\Rightarrow \alpha x\succeq\alpha y$ for $\alpha\in(0,1)$) on a vector space is *affine* (independence) if and only if it is *additive*. Thus additivity is essentially independence under weak homotheticity.
- **Examples 1 and 2** establish sharpness: a partial order on $\mathbb{R}$ (where $x\succeq y \Leftrightarrow x=y$ or $y<-1, x=-y$) and a partial order on the 2-simplex are hemicontinuous but not continuous — and both violate additivity, confirming additivity is doing real work.
- **Remark 2** shows Theorem 1 strictly generalizes the classical Wong–Ng result (a cone-induced preorder is continuous iff the cone $C=U(0)$ is closed): additivity is retained but $U(0)$ need not be a convex cone, so $\succeq$ need not be convex/homothetic/affine.

## Contribution
Identifies a clean, minimal structural condition — additivity on a normed space or topological group — under which the two textbook continuity notions for *incomplete* preorders coincide. This lets applied decision-theory results that assume full continuity (e.g. the incomplete subjective-expected-value representation of Ghirardato–Maccheroni–Marinacci 2004, Prop. A.2) weaken their hypothesis to mere hemicontinuity, or even one-sided hemicontinuity at the origin. It also clarifies that additivity + (hemi)continuity does *not* force completeness, unlike the strong-continuity completeness results of Schmeidler (1971) and Dubra (2011) — the usual order $\geq$ on $\mathbb{R}^n$ being additive, convex, homothetic, continuous, yet incomplete.

## Limitations & open questions
- The axioms (additivity, independence, homotheticity) are acknowledged to have well-known *descriptive shortcomings*; the result is justified instrumentally via subjective-expected-value modelling rather than behavioral realism.
- The vector-space proof of $(b)\Rightarrow(c)$ uses the metric induced by the norm; the group version needs nets. An open direction (implicit) is how far beyond normed/metrizable structure the equivalence extends — e.g. general topological vector spaces or non-metrizable ordered spaces.
- The paper does not characterize the *gap* between continuity and hemicontinuity when additivity fails (that is treated in the author's companion [[@Gerasimou2013|Gerasimou 2013)]]; a unified characterization across structured and unstructured domains remains open.
- Whether analogous equivalences hold for strict-preference relations $\succ$ or for multi-utility representations under additivity is not addressed.

## Connections
The note sits in the incomplete-preferences literature stemming from Bewley (2002) "Knightian decision theory" and Schmeidler (1971), and is a direct companion to [[@Gerasimou2013|Gerasimou (2013]], *Soc. Choice Welf.*) on continuity of incomplete preferences. The equivalence-under-completeness baseline is Ward (1954) and the survey of Bridges & Mehta (1995). Methodologically it parallels Karni (2007), who related Archimedean and mixture continuity via "local mixture dominance," and Gilboa, Maccheroni, Marinacci & Schmeidler (2010, Lemma 3), who linked closed-graph and mixture continuity for incomplete monotone-independent preorders. The cone/representation backdrop is Wong & Ng (1973) and Candeal-Haro & Indurain-Eraso (1992) (weak-utility representations on ordered topological groups). The applied target is Ghirardato, Maccheroni & Marinacci (2004) on differentiating ambiguity from ambiguity attitude, and de Finetti (1937) / Gilboa (2009) on subjective expected value. Examples 1 and 3's group extension are credited to E. Minguzzi and H.-P. Künzi respectively.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
