---
citekey: Shreve2005
title: "Stochastic calculus for finance I: the binomial asset pricing model"
authors: ["Shreve, Steven"]
year: 2005
type: book
doi: ""
zotero: "zotero://select/library/items/BKCQX24U"
pdf: /Users/jesper/Zotero/storage/28KCQFU4/Shreve2005.pdf
tags: [literature]
keywords: [binomial-model, no-arbitrage-pricing, risk-neutral-measure, replication, martingales, optimal-stopping, derivative-pricing]
topics: []
related: [Shreve2004]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary

Volume I of Shreve's two-part graduate text develops the full machinery of arbitrage-free derivative pricing inside the discrete-time *binomial asset pricing model*, deliberately avoiding measure-theoretic stochastic calculus so that every central idea of mathematical finance — replication, risk-neutral pricing, martingales, change of measure, optimal stopping — can be seen concretely on a finite coin-toss space before Volume II reintroduces them in continuous time. The unifying message is that the no-arbitrage price of a derivative equals the initial capital of a self-financing portfolio that replicates its payoff, and that this price can equivalently be computed as a discounted expectation under a *risk-neutral* (martingale) probability measure. Because it builds the entire conceptual scaffold of modern asset pricing from elementary probability, it is a standard methodological reference rather than a research contribution.

## Research question

How can one price and hedge derivative securities (European and American options, exotic and path-dependent claims, interest-rate products) without assuming any arbitrage opportunities, using only finite, calculus-free probability, while exposing the structural ideas (replication, equivalent martingale measures, the fundamental theorems of asset pricing) that carry over to continuous-time models?

## Method / identification

The formal object is the *binomial tree*: a single risky asset whose price $S_n$ at each step is multiplied by an up factor $u$ or a down factor $d$ ($0 < d < u$) according to a coin toss, alongside a money-market account paying constant interest $r$. The state space is coin-toss space $\Omega = \{H,T\}^N$.

- **One-period replication.** For a claim with payoff $V_1$, one chooses a stock position $\Delta_0$ and money-market position so the portfolio value $X_1 = \Delta_0 S_1 + (1+r)(X_0 - \Delta_0 S_0)$ matches $V_1$ in both states. Solving gives the *delta-hedging* rule $\Delta_0 = \frac{V_1(H) - V_1(T)}{S_1(H) - S_1(T)}$ and the no-arbitrage price $X_0$.
- **Risk-neutral probabilities.** Absence of arbitrage requires $d < 1+r < u$; the risk-neutral measure is defined by $\tilde p = \frac{1+r-d}{u-d}$, $\tilde q = 1-\tilde p$, under which the price is the discounted expected payoff $V_0 = \frac{1}{1+r}\big(\tilde p\, V_1(H) + \tilde q\, V_1(T)\big)$.
- **Multiperiod backward induction.** Iterating the one-period argument yields the recursive pricing algorithm and the *risk-neutral pricing formula* $V_n = \frac{1}{(1+r)^{N-n}}\,\widetilde{\mathbb E}_n[V_N]$, with the discounted portfolio and discounted stock price both martingales under $\widetilde{\mathbb P}$.
- **Probability foundations (Ch. 2).** Random variables, distributions, expectations, conditional expectation, the *martingale* property, and *Markov processes* are all developed on the finite space, culminating in the result that the discounted asset price is a martingale exactly under the risk-neutral measure.
- **State prices and change of measure (Ch. 3).** The *Radon–Nikodym derivative process* $Z_n = \widetilde{\mathbb E}_n\big[\frac{d\widetilde{\mathbb P}}{d\mathbb P}\big]$ links the actual and risk-neutral measures; state prices and a discrete *Capital Asset Pricing Model* are derived.
- **American derivatives (Ch. 4)** are priced by *optimal stopping*: the price is the supremum over stopping times of discounted expected payoff, equivalently the smallest supermartingale dominating the intrinsic value (the Snell envelope), yielding the stopped-process / early-exercise characterization.
- **Random walk (Ch. 5)** and **interest-rate models (Ch. 6)** extend the apparatus to reflection principles, perpetuities, and a binomial term-structure model with a stochastic short rate.

## Data

None — this is a pedagogical mathematics textbook. Examples use small numeric trees (e.g., $S_0=4$, $u=2$, $d=\tfrac12$, $r=\tfrac14$) for illustration, not empirical datasets.

## Key findings

- **No-arbitrage = replication price.** A derivative's fair time-zero price is the initial wealth of the replicating self-financing portfolio; any other price admits arbitrage (worked through the canonical $X_0 = 1.20$ call example).
- **Risk-neutral pricing formula.** Prices equal discounted expectations under the unique equivalent martingale measure $\widetilde{\mathbb P}$ with up-probability $\tilde p = \frac{1+r-d}{u-d}$; this is the discrete *first/second fundamental theorem of asset pricing* (no arbitrage $\Leftrightarrow$ existence of a martingale measure; completeness $\Leftrightarrow$ uniqueness).
- **Martingale characterization.** Discounted stock prices and discounted self-financing portfolio values are martingales under $\widetilde{\mathbb P}$.
- **Change of measure.** The Radon–Nikodym derivative process implements the discrete analogue of Girsanov's theorem and underpins state-price deflators and a discrete CAPM.
- **American options via optimal stopping.** The price is the value of an optimal-stopping problem and is the smallest supermartingale dominating the payoff, giving the optimal early-exercise rule.

## Contribution

The book's contribution is expository and methodological: it isolates the *algebraic and probabilistic core* of arbitrage pricing in a setting requiring only calculus-based probability, so that replication, martingale measures, change of measure, and optimal stopping are fully transparent before being re-derived with Itô calculus in Volume II. It has become a standard graduate and quantitative-finance reference for the conceptual foundations of derivative pricing.

## Limitations & open questions

The text is explicit about where the binomial model departs from reality, framing these as the bridges to later theory rather than unsolved research problems: the assumptions of infinitely divisible shares, equal borrowing/lending rates, zero bid–ask spread, and — most consequentially — that the stock takes only two values per period. The author notes empirical stock returns are not geometric Brownian motion (the continuous-time limit of the binomial tree), flagging model misspecification. Market *incompleteness*, transaction costs, and stochastic volatility are signposted as situations where the idealized model "becomes a serious issue," motivating the continuous-time and more general frameworks of Volume II.

## Connections

The model is the discrete-time Cox–Ross–Rubinstein (1979) binomial tree, whose continuous-time limit is the Black–Scholes–Merton (1973) framework cited throughout. The risk-neutral pricing and fundamental-theorem material formalizes Harrison & Kreps (1979) and Harrison & Pliska (1981). The optimal-stopping treatment of American options draws on Snell-envelope theory. The probabilistic foundations (martingales, Markov chains, change of measure) anticipate the Girsanov theorem and stochastic-calculus tools of the companion [[@Shreve2004|Shreve (2004)]] *Volume II: Continuous-Time Models*. The economic background situates the work relative to Markowitz (1952) portfolio theory, Sharpe's CAPM, and Merton's (1969) introduction of stochastic calculus to finance.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
