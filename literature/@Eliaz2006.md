---
citekey: Eliaz2006
title: Indifference or indecisiveness? Choice-theoretic foundations of incomplete preferences
authors: ["Eliaz, Kfir", "Ok, Efe A."]
year: 2006
type: journalArticle
doi: 10.1016/j.geb.2005.06.007
zotero: "zotero://select/library/items/ECM52LMN"
pdf: /Users/jesper/Zotero/storage/R2DFYH8H/Eliaz2006.pdf
tags: [literature]
keywords: [incomplete-preferences, revealed-preference, indecisiveness, multi-utility, preference-reversal, choice-theory, warp]
topics: []
related: [Grether1979, Huber1982, Loomes1991, Samuelson1938, Sen1971, Shafir1993, Simonson1989, Tversky1990]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> A commonly held belief in economics is that an individual's preferences that are revealed by her choices must be complete. This paper takes issue with this position by showing that one may be able to distinguish between indifference and indecisiveness of an agent upon observing her choice behavior. We relax the standard Weak Axiom of Revealed Preferences (WARP) and show that a potent theory of individual choice (with and without risk) can be founded on this weaker axiom when it is coupled with some other standard postulates. The most notable features here are that an agent is allowed to be indifferent between certain alternatives and indecisive about others. Moreover, an outside observer can identify which of these actually occur upon examining the (observable) choice behavior of the decision maker. As an application, we also show how our theory may be able to cope with the classical preference reversal phenomenon.

## Summary
The paper gives choice-theoretic foundations for *incomplete* preferences. The standard view (after Samuelson) holds that choice—being observable—forces revealed preferences to be complete: if both $x$ and $y$ are chosen from a menu, the agent must be indifferent. Eliaz and Ok argue this is an artifact of WARP, not of revealed-preference reasoning itself. They reinterpret $x\in c(S)$ as "$x$ is not revealed strictly inferior to anything in $S$" (rather than "$x$ is at least as good as everything in $S$"), replace WARP with a weaker axiom (WARNI), and show this rationalizes choice by a transitive but possibly *incomplete* (regular) preference relation. Crucially, an outside observer can then tell indifference apart from indecisiveness from choice data alone. They extend the theory to risky choice, obtaining an expected multi-utility representation, and use it to recast the preference reversal phenomenon as rational.

## Research question
Can incomplete preferences be "revealed" from observable choice the same way complete preferences can? Specifically: which axiom of standard revealed-preference theory is responsible for forcing rationalizing preferences to be complete, how can it be weakened to retain maximizing behavior while permitting indecisiveness, and can an observer distinguish an agent who is *indifferent* between two options from one who is *indecisive* (finds them incomparable)?

## Method / identification
Purely axiomatic decision theory. The primitive is a choice correspondence $c:\Omega_X\rightrightarrows X$ on a choice space $(X,\Omega_X)$, with $\emptyset\neq c(S)\subseteq S$. Multiple choices $\{x,y\}=c\{x,y\}$ are interpreted as the agent subjectively randomizing ("I'd flip a coin"), so $x\in c(S)$ means $x$ is *non-inferior*, not best.

Key constructs:
- **WARP** (restated): for $S\in\Omega_X$, $y\in S$, if some $x\in c(S)$ has $y\in c(T)$ for some $T\ni x$, then $y\in c(S)$.
- **WARNI** (Weak Axiom of Revealed Non-Inferiority): if for *every* $x\in c(S)$ there is a $T\ni x$ with $y\in c(T)$, then $y\in c(S)$. This weakens the existential quantifier in WARP to a universal one—$y$ is chosen only if it is non-inferior to *all* selected alternatives, not merely to one.
- **Regularity**: a preference relation $\succeq$ is regular if, whenever $x\bowtie y$ (incomparable), there is a $z$ with $x\succ z$ or $z\succ x$ and the other pair strictly ordered—a mild richness condition on the strict part $\succ$, automatically satisfied by Pareto/multi-criteria orders (e.g. $u_i(x)\geq u_i(y)$ for all $i$).
- **$c$-incomparable pairs** $I(c)$: pairs $(x,y)$ with $\{x,y\}=c\{x,y\}$ whose roles are *not* interchangeable across menus (using the swap operation $S_{y,-x}=(S\cup\{y\})\setminus\{x\}$). This is an *observable* set.

For risk, $X=\mathcal{P}(Z)$ (Borel lotteries on a compact prize space $Z$), with mixing $p\oplus_\lambda q=\lambda p+(1-\lambda)q$. They add a continuity (C)-axiom, a best-prize (B)-axiom, and an independence (I)-axiom (an $x\in c(S)$ analogue of standard independence plus an incomparability-preservation clause), then invoke the expected multi-utility theorem of Dubra, Maccheroni & Ok (2004).

## Data
None—this is a theory paper. The only empirical material is discussion of existing experiments (the attraction/reason-based effect of [[@Huber1982|Huber et al. 1982]]; the preference-reversal data of [[@Tversky1990|Tversky et al. 1990]], who found over 65% of subjects overpriced the long-shot lottery).

## Key findings
- **Theorem 1** (benchmark): $c$ satisfies WARP iff there is a unique *complete* preference relation $\succeq$ with $c=\max(\cdot,\succeq)$.
- **Theorem 2 / Corollary 1**: WARNI is (essentially) necessary and sufficient for $c=\max(\cdot,\succeq)$ for a unique *regular, possibly incomplete* (but transitive) $\succeq$. Relaxing WARP to WARNI exactly relaxes completeness to regularity. WARNI also implies Sen's $\alpha$-axiom, so the dividing line between complete and incomplete rational preferences is the plausibility of Sen's $\beta$-axiom versus WARNI.
- **Propositions 1–3** (identification): if $c=\max(\cdot,\succeq)$ then $I(c)\subseteq\bowtie$; if $\succeq$ is additionally regular, $I(c)=\bowtie$ exactly. Hence the observable set $I(c)$ recovers precisely the indecisive pairs, separating indifference from incomparability. Proposition 3 gives an easy sufficient test: if $\{x,y\}=c\{x,y\}$ yet some menu $T\ni x,y$ has $|c(T)\cap\{x,y\}|=1$, then $(x,y)$ is incomparable.
- **Theorem 3**: on compact choice spaces, WARNI + (C) characterize maximization of a unique *continuous* regular incomplete preference relation.
- **Theorem 4** (expected multi-utility): WARNI + (C) + (B) + (I) hold iff there is a nonempty closed convex set $U\subseteq C(Z)$ of utility functions with $c(S)=\{p\in S: E_{q,U}>E_{p,U}\text{ for no }q\in S\}$—choice as undominated under a set of expected-utility criteria.
- **Application (preference reversal)**: a monotone agent maximizing an incomplete order (e.g. first-order stochastic dominance) can choose $h$ over $\ell$ while pricing $\ell$ above $h$, because $h$ and $\ell$ are FSD-incomparable. This rationalizes the *weak* form $\{h,\ell\}=c\{h,\ell\}$, $\{\delta_{\eta_c(\ell)}\}=c\{\delta_{\eta_c(h)},\delta_{\eta_c(\ell)}\}$. The *strong* form (with $\{h\}=c\{h,\ell\}$) remains inconsistent with the theory.

## Contribution
First revealed-preference characterization that derives genuinely *incomplete* yet transitive preferences from choice, and—uniquely—lets an observer separate indifference from indecisiveness in choice data. It identifies $\beta$ (not $\alpha$) as the axiom responsible for forced completeness, and delivers the first multi-utility (and the first risky-choice) representation obtained via a revealed-preference exercise, giving the multi-objective / multi-self paradigm a choice-theoretic foundation. The framework is universal (applies to all menus) rather than tailored to a single anomaly.

## Limitations & open questions
- The theory captures **dominance-based** choice but not **reason-based** choice (Example 3): the attraction-effect pattern $c\{x,y,z\}=\{y\}$ violates WARNI, requiring instead a theory of procedural choice (Ok 2005).
- It accounts only for the **weak** form of preference reversal; the **strong** form $\{h\}=c\{h,\ell\}$ is provably inconsistent with WARNI + (C). The authors note existing PR experiments do not distinguish the two forms—an explicit call for experiments that separate them.
- Upper hemicontinuity is too strong (Pareto correspondences fail it), motivating the weaker (C)-axiom; the (I)-axiom, like standard independence, is normatively appealing but descriptively demanding.
- The second part of Theorem 2 needs a countability requirement on $\Omega_X$; without it, regularity does not guarantee WARNI on arbitrary spaces.

## Connections
The two classical references for incomplete preferences are Aumann (1962) and Bewley (1986). The expected multi-utility representation builds directly on Dubra, Maccheroni & Ok (2004); related multi-objective foundations include Ok (2002), Seidenfeld, Schervish & Kadane (1995), and Sagi (2005). On choice-theoretic foundations of incompleteness, the closest predecessors are Danan (2003) and Mandler (2005), and Nehring (1997), who weakens WARP further to non-binary rationalization. [[@Sen1971|Sen]] (1971, 1993, 1997) supplies the $\alpha$/$\beta$ decomposition of WARP, with $\alpha$ originating in Chernoff (1954); Bandyopadhyay & Sengupta (1993) independently study an axiom coinciding with WARNI on finite spaces, and Schwartz (1976) characterizes binary rationalization with transitive strict part. The reason-based / attraction-effect evidence is from [[@Huber1982|Huber, Payne & Puto (1982)]], [[@Simonson1989|Simonson (1989)]], Tversky & Shafir (1992), and [[@Shafir1993|Shafir, Simonson & Tversky (1993)]]. Preference reversal traces to Slovic & Lichtenstein (1968) and [[@Grether1979|Grether & Plott (1979)]], with later work by Holt (1986), Karni & Safra (1987), Segal (1988), [[@Tversky1990|Tversky, Slovic & Kahneman (1990)]], and [[@Loomes1991|Loomes, Starmer & Sugden (1991)]]. Reference-dependence and the endowment effect via incompleteness appear in Mandler (2005), Masatlioglu & Ok (2005), and Sagi (2005); applications to voting in Roemer (1999) and Levy (2004), and to industrial organization in Bade (2005). Foundational revealed-preference theory is due to [[@Samuelson1938|Samuelson (1938)]], Arrow (1959), Richter (1966), and Hansson (1968).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
