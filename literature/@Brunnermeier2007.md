---
citekey: Brunnermeier2007
title: "Optimal Beliefs, Asset Prices, and the Preference for Skewed Returns"
authors: ["Brunnermeier, Markus K.", "Gollier, Christian", "Parker, Jonathan A."]
year: 2007
type: journalArticle
doi: 10.1257/aer.97.2.159
zotero: "zotero://select/library/items/W6CGCNV5"
pdf: /Users/jesper/Zotero/storage/3UBBXT9D/Brunnermeier2007.pdf
tags: [literature]
keywords: [optimal-expectations, anticipatory-utility, skewness-preference, portfolio-choice, asset-pricing, motivated-beliefs, under-diversification]
topics: []
related: [Brunnermeier2005]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper studies portfolio holdings and asset prices in an economy in which people's natural tendency to be optimistic about the payout from their investments is tempered by the ex post costs of basing their portfolio decisions on incorrect beliefs. We show that this model can generate the following three stylized facts. First, households' portfolios are not optimally diversified. Second, household portfolios are tilted toward stocks with positive skewness, and undiversified households hold individual stocks with relatively high idiosyncratically skewed returns. Finally, positively skewed assets tend to have lower returns.

## Summary
Brunnermeier, Gollier, and Parker embed the *optimal expectations* framework of [[@Brunnermeier2005|Brunnermeier and Parker (2005)]] into a complete-markets exchange economy to explain three puzzles in household finance: under-diversification, a tilt toward positively skewed (lottery-like) stocks, and the low average returns of skewed assets. Investors derive anticipatory utility from being optimistic, but optimism distorts portfolio choice and lowers ex post realized utility. Optimal beliefs trade these off, and the resulting equilibrium endogenously generates a *preference for skewness*: each investor biases up the probability of exactly one cheap, unlikely state, over-invests in the corresponding skewed Arrow-Debreu security, and this demand depresses the equilibrium returns of skewed assets.

## Research question
Can a single, disciplined model of belief distortion simultaneously explain (a) why household portfolios are under-diversified, (b) why undiversified households over-weight individual stocks with positively, idiosyncratically skewed returns, and (c) why positively skewed assets earn lower average returns?

## Method / identification
A two-period exchange economy with $S$ states, complete markets in Arrow-Debreu securities, and log (CRRA-1) utility. State $s$ has objective probability $p_s>0$ and Arrow-Debreu price $\pi_s$; wealth is normalized to one. Given *subjective* beliefs $\hat{p}=\{\hat{p}_s\}$, the investor solves
$$V_1=\max_{c}\sum_{s=1}^{S}\hat{p}_s\ln(c_s)\quad\text{s.t.}\quad\sum_{s=1}^{S}\pi_s c_s=1,\ c_s\ge 0,$$
yielding the unique optimal demand $c_s^*(\hat{p})=\hat{p}_s/\pi_s$. Beliefs are then chosen to maximize *well-being*, the average of anticipated (period-1) and realized (period-2) expected utility, $\tfrac{1}{2}E[V_1+V_2]$ with $V_2=\ln c$, taking portfolio optimality as a constraint. This well-being objective follows Caplin and Leahy (2000). Formally $\hat{p}$ maximizes the Lagrangian
$$L=\sum_{s}\hat{p}_s\ln c_s^*(\hat{p})+\sum_{s}p_s\ln c_s^*(\hat{p})-\mu\Big(\sum_{s}\hat{p}_s-1\Big),$$
delivering first-order conditions that are Lambert-$W$ equations in $\pi_s/\hat{p}_s$ with generically no closed form. Section II closes the model as an *optimal expectations equilibrium*: each agent's portfolio is optimal given beliefs, each agent's beliefs maximize well-being, and all asset markets clear; prices $\pi_s$ are endogenized.

## Data
None — this is a pure theory paper. It is motivated by, but does not estimate, empirical regularities documented elsewhere (Blume, Crockett & Friend 1974; Goetzmann & Kumar 2001; Calvet, Campbell & Sodini 2006; Mitton & Vorkink, forthcoming; Zhang 2005) on household under-diversification, skewness-tilted holdings, and skewness-return relationships, plus complementary evidence from gambling/parimutuel betting.

## Key findings
- **Proposition 1 (existence):** Optimal interior beliefs exist with $0<\hat{p}_s^*<1$ for all $s$ (zero subjective probability is ruled out because it implies $-\infty$ utility if that state occurs).
- **Proposition 2 (one-state optimism):** Except in the knife-edge $S=2,\ p_1=p_2,\ \pi_1=\pi_2$ where rational beliefs are optimal, exactly one state is biased *upward* and all others *downward*; among under-weighted states, those with larger price-probability ratios (stochastic discount factors) are biased down more. This follows from a complementarity between believing a state likely and consuming more in it.
- **Proposition 3 (which state):** Investors are optimistic about the "cheapest" state — the lowest-probability state when price-probability ratios are equal, or the lowest price-probability-ratio state when probabilities are equal, or both when they coincide.
- **Corollaries 1–2 (skewness preference & two-fund separation):** Under fair prices the investor holds a risk-free position plus an extra amount of one most-skewed security, generating positively skewed portfolio returns and matching under-diversification.
- **Proposition 4 (heterogeneous portfolios):** With fair prices and limited aggregate risk, different fractions $\lambda_s$ of investors are optimistic about different states, so portfolios are heterogeneous, idiosyncratically skewed, and consumption insurance *appears* incomplete despite complete markets.
- **Proposition 5 (underperformance of skewed assets):** As endowment dispersion shrinks, prices of skewed (low-probability) securities rise, so the most skewed assets earn lower expected returns than under rational expectations and lower than less-skewed assets.

## Contribution
The paper provides a general, complete-markets characterization of portfolio choice and asset pricing under optimal expectations, going beyond the incomplete-markets and two-state cases in Gollier (2005) and [[@Brunnermeier2005|Brunnermeier & Parker (2005)]]. It unifies three household-finance puzzles under one endogenous, disciplined belief-distortion mechanism, and shows that apparent incomplete consumption insurance can arise from optimal risk-taking rather than missing markets or moral hazard. It connects to co-skewness pricing and offers a belief-based microfoundation distinct from probability-weighting/Prospect-Theory accounts (Barberis & Huang 2007).

## Limitations & open questions
- The model is a "frictionless extreme" in which *only* ex post costs discipline belief distortion; the authors note additional factors could further constrain biases.
- Log utility and the two-period structure are special; richer preferences and dynamics are left open.
- Results depend on assumptions about aggregate endowment across states — e.g., if low-probability states have much larger endowments, the sign of the return effect can reverse (though skewed assets still under-perform relative to the rational benchmark).
- The relative weight of idiosyncratic versus aggregate (co-)skewness in pricing varies with the environment and is not fully characterized.
- If bad aggregate states are unlikely (disasters/peso problems), skewness preference may *raise* the equity premium — an interaction the paper flags but does not develop.

## Connections
The belief model is the *optimal expectations* framework of [[@Brunnermeier2005|Brunnermeier and Parker (2005)]], with the well-being objective borrowed from Caplin and Leahy (2000); the working-paper companion is Brunnermeier, Gollier and Parker (2007, NBER 12940). Gollier (2005) studies optimal illusions under risk and in incomplete markets. The skewness-preference result parallels the Prospect-Theory / probability-weighting account of Barberis and Huang (2007), "Stocks as Lotteries," and the equilibrium under-diversification model of Mitton and Vorkink (forthcoming). Empirical motivation comes from Blume, Crockett and Friend (1974), Goetzmann and Kumar (2001), Calvet, Campbell and Sodini (2006) on diversification, and Zhang (2005) on individual skewness and the cross-section of returns. The incomplete-insurance evidence is from Attanasio and Davis (1996), and self-reported-belief/portfolio correlations from Vissing-Jorgensen (2003). The work sits within the broader anticipatory-utility and motivated-beliefs literature and has been linked to later experimental tests of skewness expectations and portfolio choice (Drerup, Wibral and Zimpelmann 2023).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
