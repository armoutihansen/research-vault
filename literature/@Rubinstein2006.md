---
citekey: Rubinstein2006
title: A model of choice from lists
authors: ["Rubinstein, Ariel", "Salant, Yuval"]
year: 2006
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/LFMXG55W"
pdf: /Users/jesper/Zotero/storage/QYC7D5V8/Rubinstein2006.pdf
tags: [literature]
keywords: [choice-from-lists, rational-choice, revealed-preference, bounded-rationality, random-choice, order-effects, satisficing]
topics: []
related: [Simonson1992, Tversky1972]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The standard economic choice model assumes that the decision maker chooses from sets of alternatives. In contrast, we analyze a choice model in which the decision maker encounters the alternatives in the form of a list. We present two axioms similar in nature to the classical axioms of choice from sets. We show that they characterize all the choice functions from lists that involve the choice of either the first or the last optimal alternative in the list according to some preference relation. We then relate choice functions from lists to the classical notions of choice correspondences and random choice functions. (Abstract empty in Zotero; reproduced verbatim from the journal front matter.)

## Summary
Rubinstein and Salant replace the standard primitive — choice from *sets* — with choice from *lists* (ordered sequences of distinct alternatives). A single procedural axiom, Partition Independence, pins down exactly the class of "preference-maximizing with a fixed tie-breaking rule" procedures: maximize a weak preference relation and, among the maximizers, always take either the first or the last in list order. The paper then shows how this list-based primitive recovers and reinterprets the classical objects of choice theory — choice correspondences satisfying WARP and monotone random choice functions — giving an order-based microfoundation for them. A small survey closes the paper with evidence that real "sampling-then-choosing" behavior can violate monotonicity.

## Research question
When alternatives are encountered sequentially (a list) rather than simultaneously (a set), order of presentation can be a substantive determinant of choice (primacy, recency, reference-point, contrast effects). What discipline must an order-dependent choice procedure satisfy to remain "rational-like," and which procedures exactly are picked out? How do such list-based procedures map back onto the classical set-based notions of choice correspondence and random choice function?

## Method / identification
The framework is axiomatic decision theory, not estimation. Let $X$ be a finite grand set of $N$ elements. A *list* is a non-empty finite sequence of distinct elements; $L$ is the set of all lists. A *choice function from lists* is $D:L\to X$ with $D(a_1,\dots,a_K)\in\{a_1,\dots,a_K\}$. Section 2 motivates the breadth of the object with nine example families (rational choice, satisficing, place-dependent rationality, first-element-as-reference, successive/register choice, "stop when value declines," contrast effect, knockout tournament, a pseudo-random rule).

Two axioms are central.
- **Partition Independence (PI):** for disjoint lists $L_1,L_2$, $D(\langle L_1,L_2\rangle)=D(D(L_1),D(L_2))$. Equivalently, $D$ can be computed by $K-1$ pairwise applications, so every PI function is a *successive* (register-based) choice function — though not conversely.
- **List IIA (LIIA):** deleting a non-chosen element never changes the choice.

The characterization object is $D_{\succeq,\delta}$: given a weak preference $\succeq$ over $X$ and a *priority indicator* $\delta:X\to\{1,2\}$ constant on $\succeq$-indifference sets, $D_{\succeq,\delta}$ selects the set of $\succeq$-maximal elements in the list and returns the *first* of them if their $\delta$-label is $1$, the *last* if $2$. The proofs construct $\succeq$ directly from binary choices: $a\succ b$ iff $D(a,b)=D(b,a)=a$; $a\sim_1 b$ iff $D(a,b)=a, D(b,a)=b$ (first-tie); $a\sim_2 b$ iff $D(a,b)=b, D(b,a)=a$ (last-tie). A sequence of claims establishes transitivity of $\succ$, $\sim_1$, $\sim_2$, and that $\sim_1$ and $\sim_2$ cannot chain together (Claim 4), so each indifference set is uniformly first- or last-breaking.

Two bridges to classical objects: the induced choice correspondence $C_D(A)=\{a\mid \exists\text{ ordering }O,\ D(L(A,O))=a\}$ (all elements selected under some order), and, given a measure $\mu$ over orderings, the induced random choice function $C_D^{\mu}(A)(a)=\mu(\{O\mid D(L(A,O))=a\})$.

## Data
None for the theory. A small survey provides illustrative evidence: 131 Tel Aviv University students chose which 3 of 7 arbitrarily-numbered journal papers to read before committing to publish one. Sampling frequencies were heavily front-loaded (paper 1: 79%, paper 2: 61%, ... paper 5: 14%, paper 7: 34%), and ~83% picked one of just eight triplets — about 40% chose $\{1,2,3\}$ and ~20% chose the first/middle/last triplet $\{1,4,7\}$.

## Key findings
- **Proposition 1:** LIIA $\iff$ PI.
- **Proposition 2 (main characterization):** $D$ satisfies PI iff there exist a *unique* $\succeq$ and a *unique* priority indicator $\delta$ with $D=D_{\succeq,\delta}$. Rational choice and satisficing are special cases; satisficing arises from two indifference classes (satisfactory $\delta=1$, unsatisfactory $\delta=2$). A function is fully *rationalizable* (order-invariant, picking the same $\succ$-best regardless of order) exactly when it additionally satisfies Order Invariance.
- **Proposition 3:** If $D$ satisfies PI then $C_D$ satisfies WARP; conversely any WARP-satisfying choice correspondence is generated by some PI list-choice function. Choice correspondences thus get an order-based interpretation: they summarize what a list-chooser would pick under unknown orderings.
- **Proposition 4:** $D$ satisfies PI iff for *every* $\mu$ the induced $C_D^{\mu}$ is monotone (probability of choosing $a$ weakly rises as the available set shrinks, $A'\subseteq A\Rightarrow C(A)(a)\le C(A')(a)$).
- **Proposition 5:** $C_D^{\mu}$ preserves inequalities for all $\mu$ iff $D=D_{\succeq,\delta}$ with at most two elements per $\succeq$-indifference set — connecting to Luce's family and Tversky's critiques.
- **Section 6 (duplication):** allowing repeated elements, PI* and LIIA* are *no longer equivalent* (PI* implies LIIA*, not conversely; the "most-frequent-element" rule satisfies LIIA* but violates PI*). Proposition 2* nevertheless extends the $D_{\succeq,\delta}$ characterization to lists with duplicates via induction on the duplication count.

## Contribution
The paper installs the *list* as an alternative primitive for choice theory and shows it is not merely a behavioral curiosity but a unifying lens: a single intuitive axiom (PI) recovers preference maximization with a disciplined tie-break, and the same primitive supplies fresh microfoundations for WARP-satisfying choice correspondences and for monotone/inequality-preserving random choice functions. It clarifies precisely *how much* order may matter while still leaving behavior "rationalizable" — order may only break indifferences, uniformly first or last. It is a foundational entry in the bounded-rationality / choice-procedures literature (alongside satisficing and successive choice).

## Limitations & open questions
- The authors flag that **monotonicity, though seemingly robust, can be violated** in plausible sampling settings: when a decision maker samples a few positions of a list and then maximizes, adding alternatives can *raise* a fixed alternative's selection probability by moving it toward favored (e.g. middle) sample positions. This sampling-based choice model is gestured at via the survey but not formalized — an explicit project hook.
- The survey is described as a "modest contribution," underpowered and not incentivized; the regularities in *which* positions get sampled (front-loading plus first/middle/last) are documented but not modeled.
- The tie-breaking is restricted to two labels (first/last) per indifference set; richer position-dependent selection (the place-dependent and contrast examples in Section 2) falls outside PI and is left uncharacterized.
- The duplication extension establishes that PI*/LIIA* diverge but does not fully characterize the weaker LIIA* class.

## Connections
The procedural primitive (successive register-based choice) draws on Salant (2003) on limited computational resources favoring rationality, and the satisficing example is Simon (1955). The set-based partition condition mirrors Plott (1973) on path independence, and the correspondence results lean on the standard WARP $\Rightarrow$ rationalization result in Mas-Colell, Whinston, and Green (1995). The random-choice connections engage Luce (1959) and Luce–Suppes (1965) on monotone/Luce-form choice and [[@Tversky1972|Tversky (1972)]] "elimination by aspects," plus [[@Simonson1992|Simonson and Tversky (1992)]] on context effects; the reference-point example cites Tversky and Kahneman (1991). Empirical order effects are surveyed via panel-judging studies (Bruine de Bruin 2005; Glejser and Heyndels 2001; Wilson 1977), the hide-and-seek games of Rubinstein, Tversky, and Heller (1996), Attali and Bar-Hillel (2003) on multiple-choice answer placement, Christenfeld (1995) on choices from identical options, and Liu and Simonson (2005), whose ten-product keep-or-replace task instantiates Example 5. The paper is a touchstone for later work formalizing choice with frames, attention, and consideration sets.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
