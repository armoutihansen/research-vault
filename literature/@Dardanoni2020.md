---
citekey: Dardanoni2020
title: Inferring Cognitive Heterogeneity From Aggregate Choices
authors: ["Dardanoni, Valentino", "Manzini, Paola", "Mariotti, Marco", "Tyson, Christopher J."]
year: 2020
type: journalArticle
doi: 10.3982/ECTA16382
zotero: "zotero://select/library/items/TQ7ADYSP"
pdf: /Users/jesper/Zotero/storage/X3KGV5RH/Dardanoni2020.pdf
tags: [literature]
keywords: [bounded-rationality, limited-attention, consideration-set, stochastic-choice, identification, tensor-decomposition, aggregate-choice-shares]
topics: []
related: [Lleras2017, Manzini2014, Masatlioglu2012]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Theories of bounded rationality often assume a rich dataset of choices from many overlapping menus, limiting their practical applicability. In contrast, we study the problem of identifying the distribution of cognitive characteristics in a population of agents from a minimal dataset that consists of aggregate choice shares from a single menu, and includes no observable covariates of any kind. With homogeneous preferences, we find that "consideration capacity" and "consideration probability" distributions can both be recovered effectively if the menu is sufficiently large. This remains true generically when tastes are heterogeneous with a known distribution. When the taste distribution is unknown, we show that joint choice share data from three "occasions" are generically sufficient for full identification of the cognitive distribution, and also provide substantial information about tastes.

## Summary

The paper asks how much can be learned about the *distribution of cognitive types* in a population of limited-attention decision makers when the analyst sees only aggregate choice shares from a single fixed menu — no individual-level data, no menu variation, no covariates. The central insight is that suboptimal choices (caused by limited attention) leave an algebraically tractable fingerprint in the choice shares: the system mapping the latent cognitive distribution to observed shares is *recursive, linear and (anti)triangular*, hence invertible in closed form. Under homogeneous tastes a single large menu recovers the consideration-capacity distribution (and, in the consideration-probability special case, the first $n$ raw moments of $F$); with heterogeneous, unknown tastes, joint choice shares from just three "occasions" generically identify the cognitive distribution via a tensor-decomposition uniqueness theorem (Kruskal/Rhodes).

## Research question

Can the distribution $F$ of unobserved cognitive characteristics (how much attention agents pay) be identified from a *minimal* dataset — aggregate choice shares on one menu — once a bounded-rationality model is stripped of the rich menu variation typically assumed in revealed-preference theory, and prior to any econometric covariate specification?

## Method / identification

The setup is abstract choice theory plus a population distribution over cognitive types. Each agent has cognitive type $\theta\in\Theta\subset\mathbb{R}$ drawn from cdf $F$; given a menu, type $\theta$ chooses alternative $x$ with probability $p_\theta(x)$, and the observed aggregate share is $p(x)=\int_\Theta p_\theta(x)\,dF$. Agents consider only a subset (the *consideration set*) and maximize a common linear preference order over it; the default $d$ is chosen if nothing is considered. Two attention models are studied:

- **Consideration capacity model.** Type $\gamma\in\{0,1,2,\dots\}$ caps the cardinality of the consideration set; for $1\le\gamma<n$ all $\binom{n}{\gamma}$ subsets of that size are equally likely. Writing the kth-best option as $k$, the type-conditional share is $p_\gamma(k)=\binom{n-k}{\gamma-1}/\binom{n}{\gamma}$, and aggregate shares are $p(k)=\sum_{\gamma}p_\gamma(k)\pi(\gamma)$ where $\pi(\gamma)$ are the capacity probability masses.
- **Consideration probability model** (special case, after [[@Manzini2014|Manzini-Mariotti 2014]]): each option is considered independently with probability $\rho\in[0,1]$, so $\pi(\gamma)=\binom{n}{\gamma}\int_0^1\rho^\gamma(1-\rho)^{n-\gamma}\,dF$ and $p(k)=\int_0^1 \rho(1-\rho)^{k-1}\,dF$.

The identification engine is linear algebra. Stacking shares gives $p=C\pi$ with $C$ an upper-antitriangular, left-stochastic matrix; its lower-antitriangular inverse yields $\pi=C^{-1}p$ in closed form. For the probability model a second upper-triangular matrix $Q$ links capacity masses to raw moments $m_j=\int_0^1\rho^j\,dF$, so $m=[CQ]^{-1}p$. To go *from moments to the distribution*, two routes: (i) for discrete $F$ on $L$ types over a known grid, the Vandermonde system is uniquely solvable when $n\ge 2L$ (Cohen-Yeredor 2011); (ii) for $F$ with a density, a *maximum-entropy* reconstruction on the Hausdorff moment problem, $\max -\int f_n\log f_n$ subject to the moment constraints, gives a sequence $\hat F_n$ converging weakly to $F$ (Mead-Papanicolaou 1984).

For **heterogeneous, unknown tastes** the dataset is enriched to joint choice shares across $I$ "occasions" (panel or repeated experiments) with stable $F$ but possibly changing taste distributions $\tau^i$. The joint-share tensor factorizes as $S=\sum_{\gamma=1}^{n}\pi(\gamma)\bigotimes_{i=1}^{I}[B_iC]\mathbf{1}_\gamma$, a sum of $n$ rank-1 tensors, where $B_i$ is the average preference-permutation matrix on occasion $i$. The Kruskal (1977) uniqueness theorem for tensor decompositions, in the Rhodes (2010) corollary form (Lemma 1), guarantees that for $I=3$ the triad of invertible matrices is determined up to column rescaling and permutation; bistochasticity of the $B_i$ and left-stochasticity of $C$ kill the rescaling, leaving only a relabeling that is undone by correct label assignment.

## Data

None — the paper is purely theoretical. Its entire point is to characterize what is identified by the *model itself* from a deliberately impoverished dataset (aggregate or joint choice shares with no covariates), before any empirical implementation. The authors repeatedly note where additional data (covariates, menu subsets, a RUM error distribution) would sharpen identification, but leave estimation and application to future work.

## Key findings

- **Proposition 1 (+ Corollary 1):** Under homogeneous tastes, common preferences are essentially fully revealed by the shares: $p(k)\ge p(k+1)$ always, and strict positivity of the single mass $\pi(2)$ suffices for $p(1)>p(2)>\dots>p(n)$, faithfully recovering the order.
- **Proposition 2:** In the capacity model the probability masses $\pi$ are uniquely determined by aggregate shares $p$ (via inverting $C$); capacities $\gamma\ge n$ are behaviorally indistinguishable, so a larger menu reveals one more mass.
- **Proposition 3:** In the probability model the first $n$ raw moments $m$ of $F$ are uniquely determined by $p$.
- **Propositions 4-5:** From those moments, $F$ is *uniquely* recovered if discrete with $n\ge 2L$ (Prop 4), or *approximated with weak convergence* as $n\to\infty$ via maximum entropy if $F$ has a density (Prop 5), with each $\hat F_n$ matching true shares on the $n$ best options of any menu.
- **Propositions 6-7:** Identification survives generically when tastes are heterogeneous but with a *known* distribution.
- **Proposition 8 (main result):** In the capacity model with *unknown* taste heterogeneity and three occasions, if $\pi\gg 0$ then for almost all taste distributions $\tau^1,\tau^2,\tau^3$ the masses $\pi$ and the average preference-permutation matrices $B_1,B_2,B_3$ are uniquely determined by the joint choice shares. Tastes are only *partially* recovered (the $B_i$ record rank-position probabilities; full taste distributions cannot be pinned down due to factorial explosion of rankings).

## Contribution

The paper severs cognitive identification from the data-hungry "rich menu variation" assumption pervasive in bounded-rationality theory (e.g. Aguiar et al. 2018, Cattaneo et al. 2017, Masatlioglu et al. 2012, Caplin-Dean 2015), and simultaneously from the covariate-driven identification of the applied/econometric literature (Abaluck-Adams 2017, Barseghyan-Molinari-Thirkettle 2019). It shows a minimal aggregate dataset already pins down the *cognitive* distribution, separating attention from tastes. Methodologically it is, to the authors' knowledge, the first use of *tensor-decomposition uniqueness* (Kruskal/Rhodes) in the bounded-rationality literature — a tool they flag as having independent interest beyond these specific models.

## Limitations & open questions

The authors are explicit about extension hooks: (1) *tighten preference identification* in the multioccasion environment by postulating additional data (e.g. choices from multiple menu subsets with stable tastes, or supplementing with covariates and a random utility model of preference formation); (2) bring *other forms of bounded rationality* — framing effects, satisficing — into the same minimal-data setting; (3) *weaken the assumptions*, e.g. relax conditionally uniform consideration sets (the salience-weight generalization of Example 1, shown to remain identified, even with occasion-dependent weights) and relax constant menu cardinality across occasions (within scope via Rhodes' more general Kruskal-rank condition, but not pursued). They note three occasions are both necessary (two are non-identifiable, tied to non-uniqueness of matrix factorizations) and sufficient (higher-order tensors add nothing). Full empirical implementation, estimation, inference, and refining tastes beyond rank-position probabilities (e.g. via a single-crossing RUM, Apesteguia-Ballester-Lu 2017) are left for future work.

## Connections

The consideration-probability model is the one sketched in [[@Manzini2014|Manzini and Mariotti]] (2014, Sec 7.2); the capacity model connects to Barseghyan, Molinari and Thirkettle (2019) and de Clippel, Eliaz and Rozen (2014). The paper positions itself against covariate-based identification (Abaluck-Adams 2017; Barseghyan, Coughlin, Molinari, Teitelbaum 2019) and against richness-demanding revealed-preference results (Aguiar, Boccardi, Kashaev, Kim 2018; [[@Lleras2017|Cattaneo, Ma, Masatlioglu, Suleymanov 2017]]; Caplin-Dean 2015; [[@Masatlioglu2012|Masatlioglu, Nakajima, Ozbay 2012]]). The framework parallels mixed/random-coefficient discrete-choice models (Train 2009; McFadden 2001) but uses the type $\theta$ to vary *cognition* rather than tastes, so the conditional choice probabilities are explicitly *non*-logit. Mathematically it draws on tensor algebra (Kruskal 1977; Sidiropoulos-Bro 2000; Allman-Matias-Rhodes 2009; Rhodes 2010), Vandermonde/sparsity theory (Cohen-Yeredor 2011), and the Hausdorff moment problem with maximum entropy (Mead-Papanicolaou 1984). The "consideration set" terminology is borrowed from marketing (Roberts-Lattin 1997; Shocker et al. 1991).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
