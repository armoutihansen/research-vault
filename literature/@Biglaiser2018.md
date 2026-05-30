---
citekey: Biglaiser2018
title: "Middlemen: the good, the bad, and the ugly"
authors: ["Biglaiser, Gary", "Li, Fei"]
year: 2018
type: journalArticle
doi: 10.1111/1756-2171.12216
zotero: "zotero://select/library/items/L7DBCCZM"
pdf: /Users/jesper/Zotero/storage/74HWCJKG/Biglaiser2018.pdf
tags: [literature]
keywords: [middlemen, information-intermediary, adverse-selection, moral-hazard, hold-up-problem, certification, perfect-bayesian-equilibrium]
topics: []
related: [Biglaiser1993, Biglaiser1999]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We examine the role of a middleman as an expert in markets. A seller's effort determines the quality of the good. Buyers observe neither the seller's effort nor the good's quality. A middleman, after observing a signal about the good's quality, decides whether to purchase it and then to sell it. We show that the presence of a middleman may either reduce or exacerbate the seller's moral hazard problem. We also consider a model with multiple middlemen. We find that the seller's effort is minimized if either the middleman's signal is perfect or the number of middlemen is large.

## Summary

Biglaiser and Li study middlemen as *information intermediaries* (expert certifiers/dealers) in a market where a seller chooses unobservable, costly effort that stochastically determines a good's quality. An expert middleman with a more precise signal than ordinary buyers screens the good first and, because the seller's effort cost is already sunk, can hold him up. The paper shows the welfare effect of the middleman is ambiguous, decomposing it into a *misidentification effect* (always reduces effort) and a *market premium effect* (sign depends on the seller's cost). Strikingly, a perfectly informative middleman, or a large number of competing middlemen, drives the seller to minimum effort, so seemingly efficiency-improving intermediaries can degrade average product quality.

## Research question

When a seller's costly, hidden effort determines product quality and a better-informed middleman screens the good before it reaches buyers, does the presence of the middleman raise or lower equilibrium quality (and welfare)? How does the answer change with the precision of the middleman's signal and with competition among many middlemen?

## Method / identification

Pure game theory: a four-stage signaling/screening game solved for (pure-strategy) Perfect Bayesian Equilibrium (PBE, in the sense of Fudenberg and Tirole, 1991, def. 8.2). Agents: one seller, one middleman, two buyers.

- **Seller** chooses $q\in[\underline q,1]$, the probability the good is high quality $\theta\in\{L,H\}$, at convex cost $C(q)$ with $C'(\underline q)=0$, $C'''\ge 0$; payoff $p-C(q)$. Quality is privately observed by the seller.
- **Buyers** see a common binary public signal with precision $\phi_b\in(0.5,1)$; values $v_H=1$, $v_L=0$, so there is no gain from trade on a low-quality good. Bertrand bidding yields the posterior expected value.
- **Middleman** sees a more precise binary signal $\phi_m\in[\phi_b,1]$, sells via a quality-contingent warranty (pays $p=1$ iff $\theta=H$), and incurs operation cost $\delta>0$ per trade (making low-quality trade socially negative). He makes a take-it-or-leave-it offer $w$.
- **Timing:** (1) seller chooses $q$, learns $\theta$; (2) middleman observes signal, offers $w$, seller accepts/rejects; (3) if no trade, seller goes to market where two buyers bid; (4) buyer learns quality and exercises the contingent contract.

The key construct is the posterior-updating map $f_s(\tilde q;\phi)$ from Bayes' rule and the high-type **premium** $\Delta U(q)\equiv U_H(q)-U_L(q)=(2\phi_b-1)[f_G(q;\phi_b)-f_B(q;\phi_b)]$, which is strictly concave, zero at $q\in\{0,1\}$, and maximized at $q=0.5$ (nonmonotonicity drives the ambiguity). The benchmark (no middleman) equilibrium effort $q_N$ solves $\Delta U(q_N)=C'(q_N)$. With a middleman, attention restricts (w.l.o.g., under Assumption 1: $\underline q<\delta<\bar\delta$) to *informative equilibria* where trade occurs iff the middleman's signal is $G$, and the seller's effort $q_M$ solves $\phi_m\,\Delta U(f_B(q_M;\phi_m))=C'(q_M)$.

The welfare comparison comes from a Slutsky-like decomposition of $C'(q_N)-C'(q_M)$ into the misidentification and market-premium terms. The competitive extension has $K$ anonymous middlemen visited sequentially in random order, no recall, private signals (Diamond-paradox logic makes each behave as a monopolist); effort $q_K$ solves $\phi_m^K\,\Delta U(f_K^B(q_K;\phi_m))=C'(q_K)$.

## Data

None - this is a purely theoretical paper. Motivating applications (used cars/homes/boats, mortgage-loan securitization through core dealers) are discussed narratively, and the authors note an empirical companion (Biglaiser, Li, Murry, and Zhou, 2017) finding higher dealer prices for observationally identical used cars.

## Key findings

- **Lemma 1 (benchmark):** Without a middleman there is a unique, inefficiently low effort $q_N\in(\underline q,1)$, with $q_N<q_E$ (the efficient level $C'(q_E)=1$) whenever $\phi_b<1$.
- **Lemma 2:** Under Assumption 1 any equilibrium is informative; trade occurs iff signal $G$, at price $w=U_H(f_B(q_M;\phi_m))$, and $q_M<1$. The middleman makes either a "winning" offer (accepted by both types) or a "losing" one (rejected by both).
- **Proposition 1 (perfect signal, $\phi_m=1$):** Unique equilibrium with *minimum effort* $q_M=\underline q$, price $w=0$, market bids $0$. Extreme adverse selection destroys the seller's outside option; the middleman extracts all surplus yet earns almost nothing ($\underline q(1-\delta)$) - giving the middleman perfect technology and all bargaining power paradoxically minimizes his profit.
- **Proposition 2:** For small $\delta$ an informative equilibrium with $q_M\in(\underline q,1)$ exists.
- **Proposition 3 (decomposition):** For $\phi_m\in(\phi^*,1)$ (with $\phi^*\approx 0.62$, root of $\phi^2+\phi-1=0$): if marginal cost is high then $q_M<q_N$ (middleman lowers quality); if marginal cost is low then $q_M>q_N$ (middleman raises quality). The **misidentification effect** always lowers effort; the **market premium effect** can go either way, and at intermediate costs $C'(q)\in[\underline c,\bar c]$ multiple equilibria can arise.
- **Comparative statics:** $dq_M/d\phi_m$ has ambiguous sign; a costless choice of precision is *not* maximized by the middleman - more precision can lower seller effort and the middleman's own profit (when $\phi_m$ is publicly observable).
- **Proposition 4 (competition):** Fixing $\phi_m<1$, for any $\hat q>\underline q$ there is $\hat K$ such that $q_K<\hat q$ for all $K>\hat K$; as $K\to\infty$, $q_K\to\underline q$. With many imperfect middlemen the premium of being a high type vanishes and effort collapses - competition can lower quality *below* the monopoly-middleman case.

## Contribution

Provides a new welfare channel for middlemen: an *information externality* on the pool of sellers who reach the open market, interacting with a *hold-up* problem on sunk quality investment. Unlike prior certification work where quality is exogenous, here quality is the seller's endogenous, unobservable choice, and the middleman cannot commit to a price. The framework rationalizes (i) why securitization through a few core dealers may have weakened mortgage originators' screening incentives before 2008, and (ii) why dealers obtain higher prices than direct sellers for identical used goods. Partial-commitment and seller-bargaining extensions show the seller strictly prefers visiting the middleman, so bypassing is not a credible escape.

## Limitations & open questions

- The negative competition result hinges on **no free recall** of rejected offers; a web-appendix two-middleman model with recall reverses Proposition 3 (competition raises price and, at $\phi_m=1$, near-efficient effort) - the recall assumption is an explicit open modeling choice.
- The **binary signal** is for tractability; the authors only *conjecture* that misidentification and market-premium effects survive under a general continuous signal space with the monotone likelihood ratio property.
- **Warranties** are assumed to abstract from reputation; absent warranties, one must model dynamic games with imperfect public monitoring so the middleman does not cheat.
- The seller-makes-offers case admits **multiple equilibria**, which the paper sidesteps by letting the uninformed parties make offers.
- The ordering assumption (seller meets middleman before the market) and the normalization of search costs to zero are defended but not endogenized.

## Connections

The paper builds directly on [[@Biglaiser1993|Biglaiser (1993)]], which initiated the view of the middleman as an information intermediary, and on [[@Biglaiser1999|Biglaiser and Friedman (1999)]] for warranty/reputation foundations. It contrasts with the certification design literature where quality is exogenous: Lizzeri (1999) (monopoly certifier discloses minimally, competition yields full disclosure), Albano and Lizzeri (2001) (endogenous seller quality with committed disclosure), and rating-inflation models such as Skreta and Veldkamp (2009) and Bolton, Freixas, and Shapiro (2012), as well as Faure-Grimaud, Peyrache, and Quesada (2009) and Farhi, Lerner, and Tirole (2013). The hold-up literature it extends includes Gul (2001), Hermalin (2013), and Halac (2015), while Kawai (2014, 2015) studies a related buyer-screening hold-up; Marinovic, Skrzypacz, and Varas (2017) and Board and Meyer-ter-Vehn (2013) treat dynamic reputation for quality. A complementary strand views middlemen as overcoming search frictions: Rubinstein and Wolinsky (1987), Gehrig (1993), Wright and Wong (2014), and Nosal, Wong, and Wright (2015). The empirical motivation draws on Mian and Sufi (2009) and Keys et al. (2010) for securitization and on the authors' own Biglaiser et al. (2017) for used cars; the Diamond-paradox logic underpins the competitive case, and equilibrium follows Fudenberg and Tirole (1991), with repeated-game foundations referencing Fudenberg, Levine, and Maskin (1994) and Mailath and Samuelson (2006).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
