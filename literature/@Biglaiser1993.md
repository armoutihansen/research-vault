---
citekey: Biglaiser1993
title: Middlemen as experts
authors: ["Biglaiser, Gary"]
year: 1993
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/PT9H77RB"
pdf: /Users/jesper/Zotero/storage/3AYSM2E9/Biglaiser1993.pdf
tags: [literature]
keywords: [middlemen, adverse-selection, quality-certification, reputation, bargaining, market-microstructure]
topics: []
related: [Akerlof1970]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Biglaiser builds a steady-state bargaining model of a used-durable-goods market with adverse selection (two-sided gains from trade, correlated valuations) and shows that introducing a single middleman who can become an *expert* — sinking an investment to detect quality and inspect goods — is welfare-improving in *all* equilibria when transaction costs are low and the quality gap is large. The middleman resolves the lemons problem because (i) he buys many goods, so it pays to invest in inspection technology, and (ii) he stays in the market forever, so his reputation/warranty is credible. The result is deliberately extensive-form-free, which is the paper's main methodological selling point.

## Research question
Why do middlemen — agents who neither produce, alter, nor consume a good — exist in markets such as used cars, jewelry, coins, stamps, and fine art? Specifically, can a middleman acting as a *quality-validating expert* (as opposed to a search/matching facilitator) raise welfare in a market crippled by adverse selection, and under what market conditions is such a middleman most likely to appear?

## Method / identification
A continuous-population, infinite-horizon steady-state matching-and-bargaining model. Goods are high ($H$) or low ($L$) quality; sellers know their type, value an $H$ good at $(1-\delta)U_H$ per period (present value $U_H$) and an $L$ good at zero. Buyers value quality $i$ at $V_i$, with $VH>VL>0$ and $VH>U_H$, paying $D(V_i,P)=V_i-P$. A measure-1 flow of buyers and sellers is born each period; proportion $\lambda$ of sellers are $H$. Matching costs $C_B,C_S>0$ are paid on meeting; players share discount factor $\delta\in(0,1)$ with rate $r$.

The model is made *extensive-form-independent*: rather than specifying an alternating-offer protocol, the bargaining outcome is summarized by a trading density $g(t,p\mid\mu,s)$ over time $t$ and price $p$ given buyer beliefs $\mu$ and seller type $s$. Only mild restrictions are imposed — Restriction 1 (a buyer certain she faces an $L$ trades immediately), plus steady-state consistency, individual optimization, and symmetric strategies. The driving assumption is Condition 1, the Akerlof-style inequality
$$(1-\lambda)V_L+\lambda V_H < U_H,$$
i.e. a buyer values an average good less than an $H$ seller values his own — a large quality gap.

A middleman is then added. On entry he can sink $X$ dollars in a technology giving per-inspection cost $\tau(X)$, strictly decreasing in $X$, with the investment sunk and non-transferable. He pays sellers the private-market expected price $P_i(\mu)$, may inspect or not, then quotes resale price $P_{M,i}$, and offers a non-court-enforceable but reputation-backed warranty (cheating is observed by all current and future players; another middleman can replace a cheater). The equilibrium with a middleman is constructed in seven steps that pin down the middleman's inspection probability, the share of $L$ sellers approaching him, the no-cheat price floor, $P_{MH}$, his profit, and the resulting welfare.

## Data
None — this is a pure theory paper. Empirical content is illustrative: dealers in jewelry (graduate-gemologist certification), coins/stamps (numismatist/philatelist societies), art (auction-house experts at Christie's/Sotheby's), used cars (ASE-certified mechanics), and two Los Angeles auto-repair *referral* firms (FIX-A-CAR, GOOD-TEC) are offered as anecdotal support for the displayed-sunk-investment prediction.

## Key findings
- **Proposition 1 (welfare ceiling without a middleman).** Under Condition 1 and Restriction 1, the highest attainable welfare equals the max of expression (1) (only $L$ types enter) and expression (2), where the $H$-buyer surplus is bounded by $U_H(1-K)+V_H K$ with $K=\delta^{-\log K/r}$ derived from the incentive constraint $t_H-t_L\ge -\log K/r$. The key consequence: signalling quality is only possible through *costly delay*, so there must be significant delay before an $H$ trades, and welfare lies strictly below the first-best $W^*=[(1-\lambda)V_L+\lambda V_H-C_S-C_B]/(1-\delta)$. Alternative signals (burning money, extra entry fees, history, product destruction) all fail because the single-crossing (Spence–Mirrlees) condition does not hold.
- **Proposition 2 (welfare gain with a middleman).** Under Restrictions 1–3 and Condition 1, there exist thresholds $C_B^*,C_S^*>0$ and $\delta^*<1$ such that if $C_B<C_B^*$, $C_S<C_S^*$, and $\delta>\delta^*$, an equilibrium exists with strictly higher welfare than the best middleman-free outcome. As entry/inspection costs vanish and $\delta\to1$, the welfare gains over expressions (1) and (2) converge to $\lambda(V_H-U_H)-X$ and $\lambda(1-K)(V_H-U_H)-X$ respectively, both positive for finite $X$.
- **Equilibrium properties:** the market segments — all $H$ sellers sell to the middleman, most $L$ sellers sell privately; the no-cheat resale price keeps the middleman honest (an idea paralleling Klein–Leffler and Shapiro); and the inspection investment $X$ can be large without overturning the result.
- **Empirical predictions:** middlemen are more likely where there are many low-quality goods, a large quality gap, high buyer inspection cost, low transaction costs, and effective human-capital investment; and middleman-sold goods carry *higher average price and quality* than directly sold goods.

## Contribution
Two main contributions. First, the welfare-improving role of an expert middleman is shown in a *relatively unstructured* bargaining model with asymmetric information and correlated valuations — robust to the extensive form, addressing the standard critique (Banks–Sobel, Cho–Kreps) that signalling results hinge on the precise game. Second, it isolates the *quality-guarantor* rationale for middlemen (distinct from the search/matching rationale of Rubinstein–Wolinsky) and delivers a rich set of testable predictions, while also rationalizing professional appraisers and referral organizations as middlemen who never take possession of the good.

## Limitations & open questions
- The analysis restricts attention to a *single* middleman; the free-entry case (multiple middlemen entering until profits are exhausted) is relegated to the working paper Biglaiser (1991), with only a claim that the same market features apply.
- Several simplifying assumptions are flagged as non-essential but unrelaxed here: information about cheating is transmitted instantaneously and perfectly to all newborns (an information lag is claimed not to matter qualitatively); entry costs are independent of the measure of searchers; only two quality levels are modelled.
- Equilibrium *existence* hinges on Restriction 3 (a buyer's outside option pins down the private $L$ price), which is assumed rather than derived from primitives.
- Signalling through delay is the only mechanism allowed; richer signalling spaces and non-steady-state dynamics are noted as possibly lowering welfare further but not analyzed.

## Connections
The adverse-selection backbone and Condition 1 are explicitly [[@Akerlof1970|Akerlof (1970)]]'s lemons logic. The paper positions itself against Rubinstein & Wolinsky (1987), whose middlemen reduce *search* costs rather than validate quality. The reputation-as-bond mechanism keeping the middleman honest echoes Klein & Leffler (1981) and Shapiro (1983) on reputation premia. Closely related are the author's own Biglaiser (1991) (the lemons market with bargaining and middlemen) and Biglaiser & Friedman (1992) (middlemen as guarantors of quality under moral hazard rather than adverse selection). Admati & Pfleiderer (1990) treat an information-selling middleman in finance; Davis (1991) and Chu & Chu (1990) study quality signalling through retailers/dealers, the latter being the closest precursor but far less general. The delay/correlated-values bargaining results draw on Evans (1989) and Vincent (1989), and the equilibrium-selection critique cites Banks & Sobel (1987) and Cho & Kreps (1987).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
