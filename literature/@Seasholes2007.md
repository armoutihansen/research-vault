---
citekey: Seasholes2007
title: "Predictable behavior, profits, and attention"
authors: ["Seasholes, Mark S.", "Wu, Guojun"]
year: 2007
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/DPCFZ7WU"
pdf: /Users/jesper/Zotero/storage/P54DPTX9/Seasholes2007.pdf
tags: [literature]
keywords: [attention, individual-investors, statistical-arbitrage, behavioral-finance, disposition-effect, consideration-set, price-limits]
topics: ["[[behavioral-io-naivete-attention]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Stocks in the Shanghai market that hit upper price limits typically exhibit three characteristics: high returns, high volumes, and news coverage. We show that these price limit events attract investors' attention. Attention-grabbing events lead active individual investors to buy stocks they have not previously owned. Consistent with lowering investor search costs, events that affect a few (many) stocks lead to increased (decreased) buying. Upper price limit events coincide with initial price increases followed by statistically significant price mean reversion over the following week. Rational traders (statistical arbitrageurs) profit in response to attention-based buying. Smart traders accumulate shares on date t, sell shares on date t + 1, and earn a daily average profit of 1.16%. We show the amount they invest predicts the degree of attention-based buying by individual investors. We end by decomposing individual investor trades in order to estimate losses attributable to behavioral biases.

## Summary
Using account-level transaction data from the Shanghai Stock Exchange, the paper shows that "upper price limit events" (a stock hitting its $+10\%$ daily limit, bundling high return, high volume, and news) are attention-grabbing events that drive predictable individual-investor behavior: on the following day individuals are net buyers, especially of stocks they have never owned. The buying is stronger when few stocks simultaneously hit limits (lower search cost). This demand temporarily pushes prices up before they mean-revert within a week. A group of "smart traders" (statistical arbitrageurs) systematically buys on date $t$ and sells on date $t+1$, earning $1.16\%$ per day; their investment predicts next-day individual buying. The paper closes by decomposing individual losses into a disposition-effect component and an attention-buying component.

## Research question
Do attention-grabbing events cause predictable, biased trading by individual investors, and—crucially—can rational arbitrageurs profitably trade against that bias? The paper asks (i) whether such events generate next-day net buying by individuals, (ii) whether the effect depends on search costs (number of simultaneous events), (iii) whether events induce first-time purchases of previously-unowned stocks, (iv) whether events produce transitory price pressure (mean reversion), and (v) whether identifiable "smart traders" exploit the bias and how costly the bias is to individuals.

## Method / identification
The unit of analysis is a stock-day. An **upper price limit event** is a date $t$ on which stock $k$ hits its daily upper limit ($\pm 10\%$ for Normal stocks, $\pm 5\%$ for "ST" special-treatment stocks). The empirical design has four pieces:

1. **Attention-based buying.** For each event, a net buy–sell imbalance is computed on date $t$ and date $t+1$:
$$\text{Imbalance}^{Indiv}_{k,t}=\frac{\text{Buys}^{Indiv}_{k,t}-\text{Sells}^{Indiv}_{k,t}}{\text{Buys}^{Indiv}_{k,t}+\text{Sells}^{Indiv}_{k,t}}$$
(the same measure as Barber and Odean 2005, so date-$t+1$ results are an out-of-sample replication). Hypothesis $H_A$: imbalance on $t+1$ is positive. $H_B$: the imbalance is decreasing in the size of the consideration set, tested by sorting events into bins by the number of contemporaneous events. Turnover is $\text{Turn}_{k,t}=\text{Volume(RMB)}_{k,t}/\text{MktCap(FreeFloat)}_{k,t}$, scaled to relative turnover.
2. **First-time buys ($H_C$).** Buy transactions are aggregated into account-stock-date combinations; the fraction that are first-time purchases of a stock by an account following events is compared to baseline via a Kolmogorov–Smirnov test on the discrete distributions.
3. **Price reaction.** Calendar-time portfolios buy \$1 at the close on a reference date and hold $h$ days; the return series is regressed on a constant and market return to recover a daily risk-adjusted alpha (controlling cross-sectional correlation and heteroscedasticity).
4. **Smart-trader profits and individual losses.** "Smart traders" are defined empirically: accounts that on $\ge 5$ occasions buy on date $t$ and sell the same share count on $t+1$, committing $\ge$ RMB 100,000 overnight (7878 accounts). Gross one-day profit uses volume-weighted average prices: $\text{GrossProfit}^{Smart}_{k,t+1}=\text{VWAP}^{Smart}_{k,t+1}/\text{VWAP}^{Smart}_{k,t}-1$. Determinants of smart-trader net investment are estimated by regressions on event-count indicators, an ST dummy, relative turnover, and individual imbalances (date $t$ and $t+1$). Individual losses are decomposed into a **disposition** piece $1-\text{VWAP}^{Indiv}_{k,t+1}/\text{VWAP}^{Indiv}_{k,t}$ and an **attention** piece $\text{Close}_{k,t+6}/\text{VWAP}^{Indiv}_{k,t+1}-1$. All t-statistics use robust (Rogers) standard errors clustering contemporaneous events.

## Data
Proprietary Shanghai Stock Exchange records, Jan 2, 2001 – Jul 25, 2003 (610 trading days). The exchange is an electronic limit-order book disclosing trade time, price, size, buyer and seller account numbers, and account location. Three datasets: (i) a **main** dataset of all transactions for each of the 2442 upper-price-limit-event stocks on dates $t$ and $t+1$ — 21,567,617 matched transactions across 6,459,723 accounts; (ii) an **auxiliary** dataset of all trades where one side originates in the city of Ningbo (2,989,462 matched transactions; chosen because the original smart traders were there; correlation 0.72 with market-wide value traded); (iii) daily price data for all 743 listed stocks (657, or 88.4%, experience an event). Short selling is prohibited; lower-limit events could not be obtained.

## Key findings
- **Attention-based buying ($H_A$).** Individuals are net *sellers* on event day $t$ (mean imbalance $-0.0863$, $t=-8.31$, consistent with the disposition effect) but net *buyers* on $t+1$ (mean $+0.0254$, $t=2.43$), replicating Barber–Odean out of sample.
- **Search-cost channel ($H_B$).** Next-day buying is monotonically decreasing in the number of simultaneous events: imbalance is $+0.0616$ ($t=14.06$) for 1–5 events but $-0.0083$ ($t=-0.46$) for >100 events. Fewer events = narrower consideration set = stronger attention buying.
- **First-time buys ($H_C$).** First-time purchases jump from a 47.84% baseline to 66.49% after events (73.35% for 1–5-event days); KS test significant at all levels.
- **Transitory price pressure.** Risk-adjusted return is $+0.61\%$ daily from $t$ to $t+1$ ($t=5.47$), then $-0.13\%$/day ($-0.89\%$ total over $t+1$ to $t+6$, $t=-2.41$): an upward spike followed by mean reversion within a week.
- **Smart-trader profits.** Smart traders are heavy net buyers on $t$ (imbalance $+0.4772$) and net sellers on $t+1$ ($-0.3889$), earning a gross daily profit of $1.16\%$ ($t=7.72$; $\approx 0.71\%$ net of costs). Their date-$t$ investment predicts date-$t+1$ individual buying (regression coefficient $0.3025$, $t=4.10$; $R^2=0.4483$), confirming they anticipate the bias. They place orders fast—58% of buy orders within five minutes of a stock first hitting its limit.
- **Individual losses.** Decomposition: $\approx 1.46\%$ lost over one day to selling too early (disposition) and $\approx 0.88\%$ over five days to attention-based buying at inflated prices.

## Contribution
The paper makes a tight, identified link between a behavioral bias and the rational agents who profit from it—something most behavioral-finance studies cannot do because they lack counterparty-identified data. It extends Barber and Odean (2005) by (a) using a single event type that simultaneously embodies high return, high volume, and news; (b) providing an out-of-sample replication of attention-based buying in a non-U.S. market; (c) introducing the search-cost (consideration-set) test via contemporaneous-event counts; (d) directly identifying statistical arbitrageurs and measuring their profits at the account level; and (e) decomposing individual investor losses into disposition and attention components.

## Limitations & open questions
- **No formal imbalance→mean-reversion regression.** The authors explicitly state the data "do not have enough power" to regress mean reversion on imbalance (only three days have $\ge 100$ simultaneous events). They flag as future work showing that a significant *degree* of attention buying causes a significant *degree* of mean reversion.
- **Censored prices.** Once a stock hits the limit, transaction prices are censored, complicating loss estimation; the "rough decomposition" of losses is therefore approximate.
- **No lower-limit events.** The exchange declined data on lower price limits, so the analysis is one-sided (buying, not panic selling) and short selling is banned, limiting external validity to no-short markets.
- **First-time-buy confound.** Part of the first-time-buy surge reflects investors opening new accounts during large market moves; disentangling new-account entry is left for "future research."
- **Smart-trader classification noise.** The empirical 7878-account definition may misclassify traders, biasing results toward conservatism but not cleanly identified.

## Connections
The paper is an extension of and out-of-sample test for **Barber and Odean (2005, 2008)** on attention and individual investor net buying, importing their imbalance measure directly. The disposition-effect interpretation of date-$t$ selling links to **Shefrin and Statman** and **Odean (1998)**. The limited-attention foundation draws on **Hirshleifer and Teoh (2003)**, **Peng (2005)**, **Peng and Xiong (2006)**, and rational-inattention work (**Sims 2003**, **Mankiw and Reis 2002**, **Gabaix et al. 2003**). The "consideration set" framing connects to search-cost models of choice. The calendar-time-portfolio methodology follows **Barber and Lyon (1997)** and **Lyon and Barber (1999)**. Anecdotal precursors on attention and buying include **Lee (1992)**, **Graham and Kumar (2004)**, **Gervais et al. (2001)**, **Huberman and Regev (2001)**, and **Grinblatt and Keloharju (2001)**. For the choice-modeling reader, the consideration-set/search-cost mechanism is a natural bridge to limited-attention and consideration-set models of discrete choice.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
