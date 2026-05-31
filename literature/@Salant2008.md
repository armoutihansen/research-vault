---
citekey: Salant2008
title: "(A, f): Choice with Frames"
authors: ["Salant, Yuval", "Rubinstein, Ariel"]
year: 2008
type: journalArticle
doi: 10.1111/j.1467-937X.2008.00510.x
zotero: "zotero://select/library/items/BW33C4PE"
pdf: /Users/jesper/Zotero/storage/MUUJATYV/Salant2008.pdf
tags: [literature]
keywords: [bounded-rationality, framing-effects, revealed-preference, choice-theory, limited-attention, reference-dependence]
topics: ["[[behavioral-welfare-nudge]]"]
related: [Manzini2007, Rubinstein2006, Sen1971]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We develop a framework for modelling choice in the presence of framing effects. An extended choice function assigns a chosen element to every pair (A, f) where A is a set of alternatives, and f is a frame. A frame includes observable information that is irrelevant in the rational assessment of the alternatives, but nonetheless affects choice. We relate the new framework to the classical model of choice correspondence. Conditions are identified under which there exists either a transitive or a transitive and complete binary relation R such that an alternative x is chosen in some (A, f) iff x is R-maximal in the set A. We then demonstrate that the framework of choice correspondence misses information, which is essential to economic modelling, and which is incorporated in the extended choice function.

## Summary

Salant and Rubinstein propose modelling boundedly rational, frame-sensitive behaviour by enriching the standard choice problem with a *frame*: observable but normatively irrelevant information (ballot order, default, attention budget, advertising intensity, deadline) that nonetheless moves choice. An *extended choice function* $c(A,f)$ picks a single element from each pair of a menu $A$ and a frame $f$. The paper's core contribution is to map this richer object onto the classical theory: it characterizes exactly when the induced choice *correspondence* is observationally equivalent to maximizing a (possibly complete) transitive binary relation, and then argues that even when such a relation exists, the correspondence throws away information essential to economics. The take-away: a rationalizing relation can exist yet be a poor guide to welfare or behaviour, so the frame-sensitive procedure itself must be modelled.

## Research question

How should economists model choice when behaviour systematically depends on observable information that is irrelevant to the rational assessment of the alternatives? Specifically, (i) what is the formal relationship between this enriched "choice with frames" model and the classical choice-correspondence/preference-maximization model, and (ii) under what conditions does the classical apparatus suffice — and when does it lose economically essential information?

## Method / identification

Pure decision theory; no data. Let $X$ be a finite set of alternatives and $F$ a set of frames. An *extended choice problem* is a pair $(A,f)$ with $A\subseteq X$ and $f\in F$; an *extended choice function* assigns $c(A,f)\in A$. It induces a choice correspondence
$$C_c(A)=\{x \mid c(A,f)=x \text{ for some } f\in F\},$$
the data seen by an observer who knows choice is frame-sensitive but cannot observe $f$.

The central class is the **Salient Consideration function**: for every frame $f$ there is an ordering $\succ_f$ such that $c(A,f)$ is the $\succ_f$-maximal element of $A$ (each frame triggers a "rationale"). The analysis uses Sen-style consistency axioms on the induced correspondence — property $\alpha$ (contraction consistency), $\alpha^+$ (a singleton choice survives in subsets), $\gamma$ (expansion consistency) — together with frame-level analogues:

- **Property $\gamma$-extended:** if $c(A,f)=x$ and $c(B,g)=x$, then some frame $h$ gives $c(A\cup B,h)=x$.
- **Property $\gamma^+$-extended:** if $c(A,f)=x$, $c(B,g)=y$ and $y\in A$, then some $h$ gives $c(A\cup B,h)=x$.

The identification strategy is *behavioural equivalence*: two models are "indistinguishable" when their induced correspondences coincide for all menus. The constructed relation is $x\succ y$ iff $c(\{x,y\},f)=x$ for every frame $f$ — i.e. $x$ beats $y$ under every framing.

## Data

None — this is a theoretical paper. Six illustrative extended-choice models are developed (default alternative / status-quo bias, choice from a list with satisficing, limited attention, advertisement weighting, gradual accessibility, deadline with processing times), each instantiated by a worked example rather than estimated.

## Key findings

- **Observation 1.** Without structure the two models are indistinguishable: every choice correspondence $C$ equals $C_c$ for some extended choice function $c$ when frames are unobserved (proved by a direct construction). So frames add nothing unless one restricts the class.
- **Proposition 1.** A correspondence $C$ equals $C_\succ$ for some asymmetric, transitive (possibly incomplete) $\succ$ **iff** there is a Salient Consideration function satisfying $\gamma$-extended with $C=C_c$. The proof routes through **Lemma 1**: $C$ satisfies $\alpha$, $\alpha^+$, $\gamma$ iff it maximizes an asymmetric transitive relation (building on [[@Sen1971|Sen 1971]], with $\alpha^+$ supplying transitivity beyond acyclicity).
- **Proposition 2.** $C=C_{\succeq}$ for a *complete* and transitive $\succeq$ **iff** there is a Salient Consideration function satisfying the stronger $\gamma^+$-extended. **Lemma 2** establishes that $\alpha$, $\alpha^+$, $\gamma^+$ jointly characterize complete-transitive maximization.
- **Limits of the correspondence view (Section 4).** Three negative results: (a) the induced correspondence may carry *no* information — e.g. the advertisement model gives $C_c(A)=A$ for every menu; (b) reasonable extended choice functions (e.g. good-mood maximize / bad-mood minimize an ordering) induce correspondences that *cannot* be rationalized by any transitive relation; (c) even when a transitive relation exists, it conflates preference with procedure (in the limited-attention model $\succ$ treats the attention ordering $O$ and the preference ordering $P$ symmetrically), and its symmetric component need not mean indifference.
- **Limited-attention characterization (Section 5).** The class $c^{O,P}(A,n)$ — pick the $P$-best among the first $\min\{n,|A|\}$ elements under attention ordering $O$ — is characterized by three "Attention" axioms (Attention 1–3) relating one-element vs full-attention binary choices and accessibility-monotone menu expansion.

## Contribution

Provides a clean, classical-theory-compatible language for framing/bounded-rationality phenomena, unifying the authors' earlier work on choice from lists and choice with defaults. It pins down precisely when the familiar revealed-preference toolkit survives the introduction of frames (Propositions 1–2) and, crucially, demonstrates by counterexample that the existence of a rationalizing relation does *not* justify ignoring the choice procedure. The constructed relation $x\succ y \iff c(\{x,y\},f)=x\ \forall f$ becomes a template for revealed-preference exercises under framing, closely related to Bernheim and Rangel's contemporaneous $P^*$ relation.

## Limitations & open questions

- The paper deliberately brackets **welfare**: it constructs rationalizing relations but argues (citing [[@Rubinstein2006|Rubinstein 2006]]; Rubinstein and Salant 2008) that identifying choice with well-being is a strong, separate assumption. How to extract welfare from frame-sensitive data is left open — exactly the gap Bernheim and Rangel pursue.
- It flags but does not resolve the **identification problem** that the rationalizing relation entangles preference and procedure (e.g. $O$ vs $P$ in limited attention); disentangling them requires richer, frame-level data.
- The authors caution that the framework should *not* be applied when the "frame" is in fact payoff-relevant (their matchmaking example $(A,f)$), but give no formal test to distinguish genuine frames from relevant covariates.
- Domain restrictions and invariance requirements (e.g. list invariance) are noted as modelling choices to be made case by case rather than derived.
- Beyond the limited-attention class, **axiomatic characterizations of specific extended-choice families** (advertisement, deadline, gradual accessibility) are left as open exercises.

## Connections

This is a foundational entry in the "choice with frames / bounded rationality" literature. It is developed in parallel with Bernheim and Rangel (2007)'s "choice with ancillary conditions," which shares the $(A,f)$ structure but targets behavioural welfare economics. It consolidates [[@Rubinstein2006|Rubinstein and Salant]] (2006a, "A Model of Choice from Lists") and (2006b, "Two Comments on the Principle of Revealed Preference"). The limited-attention example connects to two-stage / consideration-set procedures: [[@Manzini2007|Manzini and Mariotti (2007)]]'s Rational Shortlist Method and Eliaz and Spiegler (2007)'s consideration sets. The default/status-quo model links to Zhou (1997), Masatlioglu and Ok (2005, 2006), and Sagi (2006). The list/satisficing example operationalizes Simon (1955). The technical backbone is [[@Sen1971|Sen (1971)]] on consistency conditions ($\alpha$, $\gamma$) and revealed preference. Together these works seed the modern literature on limited attention and reference-dependent, procedurally rational choice.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
