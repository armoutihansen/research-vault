---
citekey: Barber2008
title: "All That Glitters: The Effect of Attention and News on the Buying Behavior of Individual and Institutional Investors"
authors: ["Barber, Brad M.", "Odean, Terrance"]
year: 2008
type: journalArticle
doi: 10.1093/rfs/hhm079
zotero: "zotero://select/library/items/FGHWLVX8"
pdf: /Users/jesper/Zotero/storage/9YNA7B27/Barber2008.pdf
tags: [literature]
keywords: [attention, behavioral-finance, individual-investors, buy-sell-imbalance, limited-attention, kyle-model, noise-trading]
topics: ["[[behavioral-io-naivete-attention]]"]
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We test and confirm the hypothesis that individual investors are net buyers of attention-grabbing stocks, e.g., stocks in the news, stocks experiencing high abnormal trading volume, and stocks with extreme one-day returns. Attention-driven buying results from the difficulty that investors have searching the thousands of stocks they can potentially buy. Individual investors do not face the same search problem when selling because they tend to sell only stocks they already own. We hypothesize that many investors consider purchasing only stocks that have first caught their attention. Thus, preferences determine choices after attention has determined the choice set.

## Summary
Buying and selling are not mirror images for individual investors. Because there are thousands of stocks to choose among but only a handful in a typical portfolio (and almost no short-selling), attention constrains the *buy* decision far more than the *sell* decision. The paper argues that investors first restrict the choice set to stocks that have caught their attention, and only then let preferences pick among them: "preferences determine choices *after* attention has determined the choice set." Using four trade-level datasets and three observable proxies for attention (abnormal trading volume, extreme prior-day returns, and same-day news), the authors show that individuals are net buyers on high-attention days, whereas professional money managers (especially value managers) are not. A Kyle (1985) extension in the appendix formalizes attention-driven noise trading and yields the testable prediction that attention-bought stocks subsequently underperform.

## Research question
Why do investors consider some stocks and not others when buying? Specifically, the paper tests two hypotheses: (i) the *buying* behavior of individual investors is more heavily influenced by attention than is their *selling* behavior; and (ii) the buying behavior of individual investors is more heavily influenced by attention than is the buying behavior of professional investors. The underlying claim is that attention, a scarce cognitive resource under bounded rationality, governs the composition of the consideration set when the option space is large.

## Method / identification
The empirical workhorse is a **buy-sell imbalance (BSI)** computed within attention partitions. Stocks are sorted each day into deciles (with the extreme deciles split into 5% vingtiles) on an attention proxy, and within each partition $p$ the imbalance is

$$BSI_{pt}=\frac{\sum_{i=1}^{n_{pt}} NB_{it}-\sum_{i=1}^{n_{pt}} NS_{it}}{\sum_{i=1}^{n_{pt}} NB_{it}+\sum_{i=1}^{n_{pt}} NS_{it}},$$

where $NB_{it}$ and $NS_{it}$ are the number of purchases and sales of stock $i$ on day $t$ (a value-weighted variant substitutes trade values). Inference uses the mean and Newey-West-corrected standard deviation of the daily BSI time series; partition-days with fewer than five trades are dropped. **Abnormal trading volume** for stock $i$ on day $t$ is the ratio of that day's dollar volume to its trailing one-year (252-day) average,

$$AV_{it}=\frac{V_{it}}{\bar V_{it}},\qquad \bar V_{it}=\frac{1}{252}\sum_{d=t-252}^{t-1} V_{id}.$$

Returns sorts use the *previous*-day return and BSI on day $t$, and news sorts split firms into news vs. no-news using the Dow Jones News Service feed. Lagging the return (and using $t{+}1$ volume in robustness) addresses the reverse-causality concern that buying pressure itself moves contemporaneous prices and volume. The appendix supplies a formal **Kyle (1985) market-microstructure model**: a risk-neutral informed insider and attention-driven noise traders submit market orders to a competitive risk-neutral market-maker over two rounds. Terminal value is $\tilde v=\tilde y_1+\tilde y_2$ with $\tilde y_t\sim N(0,\varphi^2)$; the public revelation of $\tilde y_1$ proxies for news, and period-2 attention is proportional to $\tilde y_1^2$. Expected noise-trader buying is $E[\tilde b_2\mid \tilde y_1]=m(A+\tilde y_1^2)$ while selling responds only partially, $E[\tilde s_2\mid \tilde y_1]=m(A+\kappa\tilde y_1^2+(1-\kappa)\varphi^2)$ with $0\le\kappa<1$, so unconditional net buying is zero but conditional net buying rises with attention. The insider conjectures a linear price rule $P_t=\mu+\lambda d_t$ on order flow $d_t=x_t+\tilde b_t-\tilde s_t$, the market-maker conjectures linear demand $x_t=\alpha+\beta\tilde y_t$, and Lemma 1 establishes the linear equilibrium (closed-form $\alpha,\beta,\mu,\lambda$). The model is calibrated and simulated 100,000 times ($\varphi=A=m=\psi=2$, $\kappa=0.5$) to reproduce the upward-sloping BSI-vs-volume pattern.

## Data
Four trade-level datasets. (1) A **large discount brokerage**: 78,000 households (66,465 with common-stock positions), Jan 1991–Nov/Dec 1996; 1,082,107 purchases vs. 887,594 sales. (2) A **small discount brokerage** marketing execution quality (more sophisticated traders): 14,667 accounts, Jan 1996–Jun 1999. (3) A **large retail brokerage**: 665,533 nondiscretionary accounts, 30 months ending Jun 1999, ~3.97M purchases / 3.22M sales. (4) **Plexus Group** institutional data: 43 professional money managers, Jan 1993–Mar 1996, classified as momentum (18), value (11), and diversified (14). Market data (volume, returns) are from CRSP NYSE/AMEX/NASDAQ files; news from the Dow Jones News Service (1994–1999), which records no news for ~91% of CRSP firms on an average day. The authors flag that individual data are broadly representative of U.S. retail investors but the institutional sample is "illustrative rather than representative."

## Key findings
Individual investors are strong net buyers on high-attention days. At the large discount brokerage, number-weighted BSI rises monotonically with abnormal volume from $-18.15\%$ (lowest decile) to $+29.5\%$ (highest vingtile); value-weighted, from $-16.28\%$ to $+17.67\%$. The retail and small discount brokerages behave similarly. On return sorts the relationship is **V-shaped**: individuals are net buyers after *both* extreme negative (≈$+29.4\%$ for the worst-return vingtile) and extreme positive prior-day returns. News stocks show higher buy-sell imbalances than no-news stocks across all size groups. Crucially, **institutional managers display the opposite pattern** — their imbalances are *higher* on low-attention days — with value managers the most aggressive low-volume buyers; their buying is least attention-driven. Results hold for large-cap stocks (ruling out the few-large-traders confound) and are similar across size terciles. Section 5 tests the rival **short-sale-constraints / heterogeneous-beliefs** explanation: restricting to stocks an investor *already owns* (so selling needs no short sale), the high-attention buy-sell tilt survives for volume and news sorts, and partitioning by exchange-traded-option availability (which relaxes short constraints) leaves patterns unchanged — so short-sale constraints do not fully explain the result; attention does. The appendix's **Proposition 1** proves the asset-pricing implication: expected noise-trader losses (equivalently insider profits) are strictly increasing in the attention level $\tilde y_1^2$,

$$\frac{\partial}{\partial \tilde y_1^2}\,E\big[x_2(\tilde v-P_2)\mid \tilde y_1\big]>0,$$

because higher attention raises the volatility of noise-trader demand, masking informed trading. Hence attention-bought stocks are predicted to subsequently underperform — "all that glitters is not gold."

## Contribution
The paper reframes investor choice as a two-stage process (attention forms the consideration set; preferences then select), breaking with standard models that treat buying and selling as symmetric ("differing only by a minus sign"). It introduces the buy-sell-imbalance methodology with cheap, observable attention proxies, documents the asymmetry between individual and institutional investors, and embeds the behavioral mechanism in a tractable Kyle-style equilibrium that delivers a falsifiable asset-pricing prediction. It is a foundational empirical anchor for the "limited attention" literature in behavioral finance and, more broadly, for consideration-set models of decision-making.

## Limitations & open questions
The authors are explicit that **none of the three attention proxies is perfect**: news data lack any measure of story salience or reach and are missing for parts of the sample; abnormal volume and large price moves can reflect a few institutions' liquidity trades rather than broad retail attention. The institutional sample is illustrative, not representative, and small (43 managers; only 159 professional traders in one dataset, with "no clear patterns"). The paper deliberately does *not* fully test the asset-pricing impact — Proposition 1's underperformance prediction is only checked in unreported auxiliary analysis, leaving the price-impact and return-predictability question open. Whether attention-driven buying generalizes beyond U.S. equities (and to other economic choices such as hiring or consumer purchases, as the conclusion speculates) is posed but untested here. The model takes the attention process ($\propto \tilde y_1^2$) as exogenous rather than deriving it.

## Connections
The framework builds directly on Odean (1999), which first proposed attention-limited search and documented that bought stocks underperform sold stocks, and on the disposition-effect work of Shefrin and Statman (1985) and Odean (1998a). The overconfidence and excessive-trading results of Odean (1998b) and Barber and Odean (2000, 2001, 2002) supply the welfare backdrop (attention-driven buying does not earn superior returns). The microstructure model extends Kyle (1985); the rival short-sale-constraints channel draws on Miller (1977) and Mayshar (1983). Empirically adjacent are Gervais, Kaniel, and Mingelgrin (2001) on the high-volume return premium, Grullon, Kanatas, and Weston (2004) on advertising and ownership breadth, Merton (1987) on investor recognition, and the out-of-sample replication on the Shanghai Stock Exchange by Seasholes and Wu (2004). Lee (1992) and Hirshleifer et al. (2003) provide earlier evidence of small-trader net buying around earnings news, and Huo, Peng, and Xiong (2006) link attention to overreaction.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
