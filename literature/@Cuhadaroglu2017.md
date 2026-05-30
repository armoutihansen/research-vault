---
citekey: Cuhadaroglu2017
title: Choosing on influence
authors: ["Cuhadaroglu, Tugce"]
year: 2017
type: journalArticle
doi: 10.3982/TE2170
zotero: "zotero://select/library/items/FFAXK7VY"
pdf: /Users/jesper/Zotero/storage/KWI6TBX5/Cuhadaroglu2017.pdf
tags: [literature]
keywords: [revealed-preference, social-influence, bounded-rationality, incomplete-preferences, two-stage-maximization, choice-correspondences, axiomatization]
topics: []
related: [Apesteguia2013, Au2011, Horan2016, Mas2009, Masatlioglu2012, Salant2008, Sen1993, Zimmerman2003]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Interaction, the act of mutual influence, is an essential part of daily life and economic decisions. This paper presents an individual decision procedure for interacting individuals. According to our model, individuals seek influence from each other for those issues that they cannot solve on their own. Following a choice-theoretic approach, we provide simple properties that aid us to detect interacting individuals. Revealed preference analysis not only grants underlying preferences, but also the influence acquired.

## Summary

The paper imports the revealed-preference / bounded-rationality toolkit into the study of social interaction. It models two (or more) agents with transitive but incomplete preferences who, when their own preferences fail to single out a unique alternative, appeal to each other's preferences in a second stage to refine their choices. This "Choice on Mutual Influence" (CMI) procedure is characterized by three falsifiable axioms on the pair of choice correspondences, and revealed-preference analysis recovers both the underlying (unobservable) preferences and the influence each agent exerts on the other. The model extends to $n$-agent settings, with an explicit characterization of expert influence, and offers a fresh, non-econometric angle on the classic homophily-versus-influence identification problem.

## Research question

Can social interaction be given choice-theoretic microfoundations? Specifically: given only observed choice behavior of socially related individuals, (i) what testable properties detect that they are interacting; (ii) can revealed-preference analysis recover their underlying preferences; and (iii) can it recover the influence they acquire from one another? The paper frames this as addressing the gap flagged by Blume et al. (2010) that the micro-foundations of social interactions remain unexplored, since the econometrics literature defines interactions via variable types rather than via mechanisms.

## Method / identification

Pure choice-theoretic axiomatization. Let $X$ be a finite set of alternatives and $\Gamma X$ the nonempty subsets. Each individual $i\in\{1,2\}$ is described by a choice correspondence $C_i:\Gamma X\rightrightarrows X$ with $\emptyset\neq C_i(S)\subseteq S$, and (latently) by an asymmetric, transitive but possibly incomplete strict preference $\succ_i$. The CMI mechanism is the two-stage nested maximization

$$C_1(S)=\mathrm{Max}\big(\mathrm{Max}(S,\succ_1),\succ_2\big),\qquad C_2(S)=\mathrm{Max}\big(\mathrm{Max}(S,\succ_2),\succ_1\big).$$

Because incompleteness means stage one need not yield a singleton, choice is allowed to be set-valued (following [[@Sen1993|Sen 1993]]'s "choosable elements"). Three axioms characterize CMI:

- **Expansion (EXP / Sen's $\gamma$):** if $x\in C_i(S)\cap C_i(T)$ then $x\in C_i(S\cup T)$ — standard individual rationality.
- **Nullipotency (NULL):** $C_j(C_i(S))=C_i(S)$ for $i\neq j$ — all attainable influence is already inherent in $i$'s behavior; $j$ cannot refine it further.
- **Consistency of Influence (CoI):** the key property. Define a *weak $(x,y)$ reversal* (after [[@Horan2016|Horan 2016]]) when $x=C_i(xy)$ yet $C_i(S)\neq C_i(S\setminus y)$; such reversals are evidence of influence. Say $x$ *shadows* $y$ for $i$ ($x\succ^s_i y$) if $C_i(S)=C_i(S\setminus y)$ for all $S\ni x$. CoI requires: if $x=C_i(xy)$, then $x$ shadows $y$ for at least one of the two individuals.

Identification proceeds by setting $\succ_i=\succ^s_i$ (the shadows relation), proven asymmetric and transitive, and partitioning binary comparisons into **disagreements** $D_i$, **influences** $I_i$, and **agreements** $A$. The uniquely identified part of preferences is the transitive closure $(\mathrm{tr}(D_1\cup I_1),\mathrm{tr}(D_2\cup I_2))$, with residual indeterminacy located entirely in $A$.

## Data

None — this is a pure theory / axiomatic paper. No empirical dataset or experiment; all "data" are abstract choice correspondences. The author repeatedly notes the properties are falsifiable and could be brought to observed choice data, but performs no estimation.

## Key findings

- **Theorem 1 (characterization of CMI):** A pair $(C_1,C_2)$ satisfies EXP, NULL, and CoI if and only if it is a CMI mechanism. Necessity is straightforward; sufficiency constructs the rationalizing preferences from the shadows relations. Corollaries: for identical behavior $C_1=C_2=C$, $(C,C)$ has a CMI representation iff $C$ is quasi-rational (no inconsistencies); if additionally single-valued, iff $C$ is rational. When choice is single-valued, NULL becomes redundant and EXP + CoI suffice.
- **Theorem 2 (identification):** Any preference pair explaining a CMI mechanism is identified uniquely up to *A-completions* of $(\mathrm{tr}(D_1\cup I_1),\mathrm{tr}(D_2\cup I_2))$. The pair $(\succ^s_1,\succ^s_2)$ is the largest rationalizing pair; the overidentification problem lives in $A$. Extremes: identical overall behavior ($D_i=I_i=\emptyset$) cannot distinguish shared preferences from one agent being null and fully influenced; an empty $A$ delivers full identification of preferences and influence.
- **Theorem 3 (Choice on Expert Influence, CEI):** For $n$ agents with disjoint areas of expertise $E_i$ and society-wide expert rationale $\succ^E=\bigcup_j(\succ_j|E_j)$, the mechanism $C_i(S)=\mathrm{Max}(\mathrm{Max}(S,\succ_i),\succ^E)$ is characterized by EXP, a weakened weak WARP for correspondences (WWARP\*), Consistency of Expert Influence (CoEI), and Binding Influence (BI).
- Multi-agent variants (unanimous influence, directed influence forming a network) are sketched as modifications of CoI and NULL.

## Contribution

Two-fold, per the author. First, it is, to the author's knowledge, the first paper to deploy choice theory to study social interaction, replacing the dominant econometric framing with falsifiable axioms that detect interacting agents and reveal both their latent preferences and the influence acquired — notably without strategic/payoff-relevant intentions (unlike persuasion or compliance models). Second, it adds a simple, natural two-stage maximization procedure to the bounded-rationality literature, distinguished from prior two-stage models because the second stage is *another agent* with its own choice structure rather than a second internal criterion, and because it handles set-valued choice. Section 3.1 reframes the homophily-versus-influence identification problem: once CMI's testable properties hold, revealed preference recovers influence, and homophily can be measured by similarity of recovered individual preferences.

## Limitations & open questions

- **Overidentification via agreements $A$:** preferences are only pinned down up to A-completions; when two agents behave identically, shared preferences cannot be distinguished from full influence over a null-preference agent. The author notes a *richness* condition on preferences restores unique identification but concedes "whether richness is a reasonable assumption is open to discussion" (result available on request).
- **No strategic intentions:** influence is not payoff-relevant for the influencer; integrating strategic motives (the author notes a Stackelberg-game construction is observationally equivalent, after Yildiz 2017) is left open.
- **Inference is permissive:** sharing an environment plus satisfying EXP/NULL/CoI is taken as evidence of mutual influence, but alternative explanations (e.g., each agent independently running a rational shortlist method) can generate the same data — a genuine challenge to the interaction interpretation.
- **Multi-agent characterizations** for unanimous and directed influence (with set-valued outcomes) are only sketched; full results are deferred ("available upon request").
- The closing remark — "there is still a lot to explore once we go beyond more than one individual's behavior" — is an explicit invitation to expand the choice-data-on-groups research program.

## Connections

The baseline two-stage architecture is Manzini & Mariotti's (2007) rational shortlist methods (RSM), characterized by EXP and weak WARP; [[@Salant2008|Rubinstein & Salant (2008)]] give an alternative axiomatization via exclusion consistency. RSM with transitive rationales is axiomatized independently by [[@Au2011|Au & Kawai (2011)]], Yildiz (2017), and [[@Horan2016|Horan (2016)]]; the present paper borrows Horan's (2016) inconsistency-based approach and his weak $(x,y)$ reversal device. The only prior set-valued RSM treatment is Garcia-Sanz & Alcantud (2015). Related bounded-rationality procedures include [[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay (2012)]] on limited attention, Masatlioglu & Ok (2005) and [[@Apesteguia2013|Apesteguia & Ballester (2013)]] on status-quo bias, and [[@Salant2008|Salant & Rubinstein (2008)]] on framing. The set-valued "choosable elements" interpretation follows [[@Sen1993|Sen (1993)]], and the characterization of transitive asymmetric relations uses Plott (1973). On the empirical side it engages the social-interactions literature — Manski (1993, 2000) on the reflection problem and identification, Blume et al. (2010), Calvo-Armengol et al. (2009) and Bramoullé et al. (2009) on network peer effects, [[@Mas2009|Mas & Moretti (2009)]] on peers at work, [[@Zimmerman2003|Zimmerman (2003)]] on education — and the homophily literature, McPherson, Smith-Lovin & Cook (2001) and Currarini et al. (2009).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
