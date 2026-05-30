---
citekey: Kolay2013
title: Contract Design with a Dominant Retailer and a Competitive Fringe
authors: ["Kolay, Sreya", "Shaffer, Greg"]
year: 2013
type: journalArticle
doi: 10.1287/mnsc.1120.1677
zotero: "zotero://select/library/items/FK8MU97Q"
pdf: /Users/jesper/Zotero/storage/SYZ7PL87/Kolay2013.pdf
tags: [literature]
keywords: [channel-coordination, vertical-contracting, two-part-tariffs, quantity-discounts, dominant-retailer, competitive-fringe, mechanism-design]
topics: []
related: [Jeuland1983, Kolay2004, Moorthy1987]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We show that under some conditions, quantity discounts and two-part tariffs are equivalent as mechanisms for channel coordination when an upstream firm sells its product in a downstream market that is characterized by a dominant retailer and a competitive fringe. We consider a setting in which discriminatory offers are feasible and a setting in which the same menu of options must be offered to all retailers. We find that the upstream firm's profit in both settings is independent of whether quantity discounts or two-part tariffs are used. The implication of this finding is that the firm's choice of contract design may turn on which one is easier to implement. This paper was accepted by J. Miguel Villas-Boas, marketing.

## Summary
Kolay and Shaffer study how an upstream manufacturer can coordinate a vertical channel when the downstream market consists of one dominant retailer (who sets the market price and decides whether to provide a demand-enhancing service) plus a competitive fringe of price-taking firms. Extending the setting of Raju and Zhang (2005), they show that the channel can always be fully coordinated, and—contrary to Raju and Zhang—that the manufacturer's profit is *independent* of whether it uses Jeuland–Shugan quantity-discount schedules or two-part tariffs. This isomorphism holds both when discriminatory contracts are allowed and when the same menu must be offered to all retailers. The practical upshot is that contract choice should turn on implementation ease rather than profitability.

## Research question
In a downstream market with a dominant retailer and a competitive fringe: (i) Can the manufacturer fully coordinate the channel (replicate the vertically integrated outcome) through arm's-length contracting? (ii) Does its profit differ depending on whether it uses quantity-discount schedules or two-part tariffs, both when overt price discrimination across retailers is feasible and when it is not?

## Method / identification
A three-stage game-theoretic model. The dominant retailer faces demand $Q_d(p,s)=\gamma(\alpha-p+s)$, where $\gamma\in(0,1]$ is its market share, $p$ the price it sets, and $s\in\{0,\bar s\}$ a demand-enhancing service costing $f>0$. Residual fringe demand is $Q_f(p,s)=(1-\gamma)(\alpha-p+s)$, split over $N$ price-taking firms. Parameters obey bounds in (1): $\alpha\ge 7\bar s$, $\gamma\ge\frac{(\alpha+\bar s)}{(\alpha+\bar s+N\bar s)}$, and $f\le\frac{\gamma\bar s(2\alpha+\bar s)}{4}$, guaranteeing the integrated firm provides service and chooses the channel-optimal price.

Timing: (1) the manufacturer offers contracts; (2) retailers accept/reject; (3) the dominant retailer chooses $p$ and whether to provide $\bar s$. Full coordination means achieving the integrated benchmark $\max_{p,s}\,\gamma p(\alpha-p+\bar s)-f$, with optimal price $p^*(\bar s)\equiv(\alpha+\bar s)/2$ and channel profit $\Pi_I\equiv\gamma(\alpha+\bar s)^2/4-f$.

The analysis proceeds in two regimes. In the **discriminatory** regime the manufacturer may offer the dominant retailer and fringe different contracts. A Jeuland–Shugan schedule takes the form $t_d(q;\bar s,f)\equiv\frac{\gamma-k_1\alpha+s̄}{\gamma}-\frac{(1-k_2)f}{q}-\dots$, parameterized by $k_1\in[0,\gamma]$ and $k_2\ge 0$; $k_1$ aligns the marginal incentive (service provision) and $k_2$ acts as a fixed fee extracting surplus. A two-part tariff is $(w_d,F_d)$ with $w_d\ge 0$, $F_d\ge 0$. In the **non-discriminatory** regime the manufacturer offers a single menu (at most two options, one per retailer type) and lets retailers self-select, subject to incentive-compatibility constraints. The author solves for the optimal menu of quantity discounts and the optimal menu of two-part tariffs and compares manufacturer profit.

## Data
None — this is a purely theoretical contract-design / mechanism-design paper. The model is solved analytically.

## Key findings
- **Proposition 1:** Discriminatory quantity-discount schedules exist that align channel incentives and let the manufacturer extract all surplus; the fringe is offered a constant per-unit price $t_f(q)\equiv p^*(\bar s)$ and the dominant retailer a Jeuland–Shugan schedule with $(\tilde k_1,\tilde k_2)$ driving its profit to zero while still inducing service.
- **Proposition 2:** Discriminatory two-part tariffs also coordinate and extract all surplus; the dominant retailer is offered $(w_d=0,\,F_d=p^*(\bar s)(\gamma\alpha-\gamma p^*(\bar s)+\gamma\bar s)-f)$. Setting $w_d=0$ solves double marginalization; $F_d$ extracts surplus. Both Props 1 and 2 hold whether or not service can be separately contracted.
- **Discriminatory equivalence:** Since the manufacturer extracts all surplus under both contract forms, it is indifferent between them.
- **Proposition 3:** A non-discriminatory *menu* of quantity discounts exists that coordinates the channel; $(\hat k_1,\hat k_2)$ make the dominant retailer indifferent between its option and the fringe option $t_2(q)=p^*(\bar s)$.
- **Proposition 4:** The optimal non-discriminatory menu of two-part tariffs is $(w_d^*,F_d^*)=(0,\,\Pi_d(0)-\Pi_d(p^*(\bar s)))$ for the dominant retailer and $(w_f^*,F_f^*)=(p^*(\bar s),0)$ for the fringe, where $\Pi_d(w)\equiv\max_{p,s}(p-w)\gamma(\alpha-p+\bar s)-f$. Optimality of $w_f=p^*(\bar s)$ follows from differentiating $-\Pi_d(w_f)+(p^*(\bar s)-w_f)q_f(p^*(\bar s),\bar s)$.
- **Proposition 5 (central result):** When the same menu must be offered to all, the manufacturer is *indifferent* between the optimal menu of two-part tariffs and the optimal menu of quantity discounts—both coordinate the channel and yield the same surplus division. The intuition: in both menus the dominant retailer's information rent equals the profit it could earn by taking the fringe option, which sells at $p^*(\bar s)$ in both cases, so its rent (and hence the manufacturer's residual profit) is identical.

## Contribution
The paper extends Raju and Zhang (2005) by enlarging the contract space to include *customized* two-part tariffs and *menus* of quantity discounts, and by separating the discriminatory and non-discriminatory regimes. It overturns Raju and Zhang's conclusion that the manufacturer may strictly prefer one contract form: the surprising result is that the added flexibility of quantity discounts (different per-unit prices on and off the equilibrium path) is *unneeded* in this market structure. Contract choice is therefore driven by implementation cost, not profit—relevant to policy debates on dominant retailers and price discrimination (e.g., the Robinson–Patman Act).

## Limitations & open questions
- The equivalence relies on the manufacturer being able to *fully extract* surplus; the authors note it may break under market imperfections that prevent full extraction.
- Future work should compare *other* contract classes in this setting—e.g., all-units discounts (discounts applying to all units once a threshold is reached), revenue-sharing contracts, or minimum market-share requirements—which may yield strictly higher manufacturer profit when full extraction fails.
- The fringe makes no demand-related decisions; richer fringe behavior is unexplored.
- Demand is deterministic and actions observable; relaxing these (as in Iyer and Villas-Boas 2003) could break the isomorphism.

## Connections
The paper builds most directly on Raju and Zhang (2005), the only prior work analyzing channel coordination with a dominant retailer and competitive fringe. The equivalence-of-contracts tradition originates with [[@Jeuland1983|Jeuland and Shugan]] (1983, 1988) and [[@Moorthy1987|Moorthy (1987)]], who established quantity-discount/two-part-tariff equivalence in bilateral monopoly. Work showing equivalence can fail under downstream competition includes Mathewson and Winter (1984), Ingene and Parry (1995, 2000), and Iyer (1998). Iyer and Villas-Boas (2003) show linear contracts can dominate two-part tariffs under demand uncertainty and unobservable actions. The suggested extensions connect to the authors' related work on all-units discounts ([[@Kolay2004|Kolay, Shaffer, and Ordover 2004]]) and market-share contracts under asymmetric information (Majumdar and Shaffer 2009).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
