---
citekey: Biglaiser1999
title: Adverse Selection with Competitive Inspection
authors: ["Biglaiser, Gary", "Friedman, James W."]
year: 1999
type: journalArticle
doi: 10.1111/j.1430-9134.1999.00001.x
zotero: "zotero://select/library/items/8NAN53E7"
pdf: /Users/jesper/Zotero/storage/Y6QRFZBD/Biglaiser1999.pdf
tags: [literature]
keywords: [adverse-selection, intermediation, certification, quality-inspection, market-design, search-costs]
topics: []
related: [Akerlof1970, Biglaiser1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We develop a model with heterogeneous buyers and sellers in which the sellers have private information about their goods' qualities. We show that efficient trading cannot occur without middlemen. Middlemen can provide two services: one is inspection, and the other is the sorting of buyers and sellers through the rationing of sellers and the provision of two different price schedules. The latter service permits the possibility of achieving the first best. When the first best is not attainable, there is a second best characterized by two intervals, one consisting of low-quality noninspected goods, and the other of high-quality inspected goods. We determine whether first and second best outcomes can be implemented in a market equilibrium with both zero and infinite buyer-seller search costs. First and second best outcomes are attainable under a larger set of parameter values when search costs are infinite; also, typically too much inspection occurs in a market equilibrium. Welfare may be either raised or lowered by the introduction of middlemen.

## Summary
Biglaiser and Friedman build a competitive intermediation model in which sellers privately know the vertical quality $q$ of their one-unit goods while buyers cannot observe quality before purchase. Infinitely-lived middlemen resolve the resulting adverse-selection problem through two distinct instruments: costly inspection (certification) and a sorting mechanism that rations sellers and posts separate bid and asked price schedules. Efficient (first-best) trade is shown to be impossible without middlemen; with them, the first best can be approached when buyers value goods strongly relative to sellers and search costs are high, while otherwise a three-interval second best obtains. A central comparative-statics result is that eliminating buyer-seller search costs can lower welfare, and that market equilibria typically involve too much inspection.

## Research question
Why is so much trade conducted through middlemen, and what are the welfare consequences of their presence, when sellers have private information about product quality and buyers cannot judge quality on their own? Specifically, can middlemen restore efficiency, and under what search-cost regimes and parameter configurations are first-best or second-best outcomes implementable as competitive market equilibria?

## Method / identification
A discrete-time competitive equilibrium model with three player types. Sellers and buyers live one period; middlemen are infinitely-lived (enabling reputation for honesty). Each seller owns one unit of a good with quality $q$, uniform on $[L,H]$ with $H>L\ge 0$; quality is also the seller's reservation value, so a seller's payoff is $q$ if unsold and $b(q)$ if sold for bid price $b(q)$. Buyers have type $\tau$ uniform on $[L+A,H+A]$ with $L+A>1$; a buyer of type $\tau$ buying good $q$ at asked price $a(q)$ earns $\tau q - a(q)$. Both sides are risk-neutral. Middlemen perfectly inspect quality at cost $k>0$ and enter freely at fixed cost $F$ (treated as a transfer through most of the paper, as a resource cost in Section 5).

The equilibrium objects are: a rationing function $\gamma(q)\in[0,1]$ (probability a type-$q$ seller trades in the noninspected segment), an assignment function $\theta$ matching buyers to sellers, the bid schedule $b$, the asked schedule $a$, and a cutoff $H_0$ splitting noninspected goods $[L,H_0)$ from inspected goods $[H_0,H]$. Incentive compatibility for sellers yields the differential equation
$$b'(q)=\frac{-\gamma'(q)}{\gamma(q)}\,[b(q)-q],$$
with solution $b(q)=q+\dfrac{C-\theta(q)}{\gamma(q)}$. Buyer incentive compatibility gives $\theta(q)=a'(q)$, so $a(q)=a(L)+\int_L^q \theta(x)\,dx$. Two regimes are analyzed: infinite search costs (trade only via middlemen) and zero search costs (a buyer-seller pair can contract directly and purchase inspection competitively at price $k$). A market equilibrium additionally requires no profitable middleman defection (supported by pessimistic off-path buyer beliefs and a reputation argument) and, under zero search costs, no profitable independent buyer-seller deviation.

## Data
None. This is a purely theoretical paper. The only empirical reference is motivating: middlemen account for over 25% of US GDP (citing Spulber 1996), with examples such as art, antiques, jewelry, used durables, and IPOs.

## Key findings
- **First-best impossible without middlemen.** Efficient sorting requires buyers face a convex asked schedule with slope $>1$ while sellers face a (near-)constant bid; with $a(q)=b(q)$ this cannot hold, so a single price schedule cannot simultaneously sort both sides.
- **Proposition 1.** Under infinite search costs, a first best is achievable in market equilibrium with nonnegative middleman profits if and only if $(L+A)L\ge H$ (the lowest buyer values the lowest good at least as much as the highest seller values his). Then $b(q)=a(q)=L(L+A)$.
- **Proposition 2.** Under zero search costs and $(L+A)L\ge H$: (i) if $k\ge k_0$ with $k_0=(H-L)A+(H^2-L^2)/2$, the first best is still attained; (ii) if $k<k_0$ some high-end pairs contract independently and the first best fails.
- **Welfare-reducing search.** Comparing Propositions 1 and 2, eliminating search costs can lower welfare: buyer welfare is unchanged, but for $k<k_0$ middlemen lose rents split between high-end sellers and wasted inspection, with aggregate welfare falling by $\Delta=k(H-H_0)$.
- **Proposition 3 / Proposition 4 (second best).** When $(L+A)L<H$, a second best exists (continuity of welfare on a compact feasible set) and is partitioned into three intervals: a low interval $[L,L_0)$ where the profit constraint $a(q)\ge b(q)$ binds ($b$ increasing, $\gamma$ decreasing); a middle interval $[L_0,H_0)$ with constant $\gamma$ (possibly a gap of untraded top-of-segment sellers, as in [[@Akerlof1970|Akerlof 1970]]); and a high interval $[H_0,H]$ where all goods are inspected and all sellers trade. $\gamma(L)=1$.
- **Too much inspection.** Market equilibria typically inspect more goods than the second best prescribes, and implementation is easier (holds for a larger parameter set) under infinite than under zero search costs.
- **Ambiguous middleman welfare.** If $F$ is a resource cost with free entry, middlemen can lower welfare (echoing the excess-entry logic of Mankiw and Whinston 1986); otherwise, and always under infinite search costs, middlemen are beneficial.

## Contribution
The paper unifies two roles of intermediaries — quality certification through inspection and information provision through price-schedule sorting plus rationing — within a single competitive model with two-sided heterogeneity and adverse selection. Unlike prior search-based middleman models (where goods are homogeneous) or certification models with identical buyers (so no buyer sorting), it delivers a continuum of prices and trade probabilities and isolates the wedge between bid and asked prices as the efficiency-restoring instrument (analogized to optimal warranties under double moral hazard). It also produces the counterintuitive result that lowering search frictions can reduce welfare.

## Limitations & open questions
- No closed-form solution for the second best is obtained; only a partial characterization (Proposition 4) is provided. A full analytical or numerical characterization is left open.
- Middleman honesty is supported by an unmodeled reputation argument with pessimistic off-path beliefs; an explicit dynamic reputation game is not solved.
- Analysis is confined to the two extreme search-cost regimes (zero and infinite); intermediate search costs are not treated.
- Distributions are assumed uniform and buyer/seller measures equal "for simplicity"; robustness to general distributions is asserted but not demonstrated.
- The treatment of the fixed entry cost $F$ as resource versus transfer drives the welfare sign; endogenizing entry and the number of differentiated middlemen is not pursued.
- The model restricts attention to pure-strategy equilibria (contrasting with the mixed-strategy equilibria of [[@Biglaiser1993|Biglaiser 1993]] when inspection is unobservable).

## Connections
The paper builds directly on [[@Biglaiser1993|Biglaiser (1993)]], which studies a dynamic correlated-value model where a reputation-valuing middleman reduces bargaining inefficiency, and on Biglaiser and Friedman (1994) on moral hazard in seller quality choice. It relates to certification and disclosure models, notably Lizzeri (1996) on optimal information revelation by a costless-inspection intermediary. The adverse-selection foundation is [[@Akerlof1970|Akerlof (1970)]], whose unraveling reappears as the untraded gap in the second best. Search-theoretic intermediation work includes Rubinstein and Wolinsky (1987), Gehrig (1993), Yavas (1996), and Spulber (1996a, 1996b). Expert/diagnosis models with credence-like quality include Wolinsky (1993) and Taylor (1995). Adverse selection with heterogeneous buyers and sellers connects to Wilson (1980) and Perktold (1996), while bilateral bargaining with correlated valuations relates to Samuelson (1984) and Bigelow (1990). The welfare-reducing free-entry result invokes Mankiw and Whinston (1986).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
