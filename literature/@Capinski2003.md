---
citekey: Capinski2003
title: Mathematics for Finance
authors: ["Capinski, M", "Zaszawniak, T"]
year: 2003
type: book
doi: 10.1007/b97511
zotero: "zotero://select/library/items/YQ5R8EH9"
pdf: /Users/jesper/Zotero/storage/ZIANYSAW/Capinski2003.pdf
tags: [literature]
keywords: [mathematical-finance, no-arbitrage-pricing, binomial-model, black-scholes, portfolio-theory, capm, term-structure, textbook]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero) — Undergraduate textbook (Springer Undergraduate Mathematics Series, 2003) introducing the core mathematics of financial engineering: no-arbitrage pricing of derivatives (Black–Scholes) and mean–variance portfolio theory (Markowitz, CAPM), plus interest-rate models. Aimed at second/third-year undergraduates in mathematics, business, finance or economics, assuming only elementary calculus, probability and linear algebra.

## Summary
This is a self-contained undergraduate textbook by Capiński and Zastawniak that builds the two Nobel-Prize-winning pillars of mathematical finance from a common no-arbitrage foundation: Black–Scholes arbitrage pricing of options and other derivatives, and Markowitz mean–variance portfolio optimisation together with the Capital Asset Pricing Model. It develops the discrete-time machinery (binomial tree, risk-neutral / martingale pricing, the Fundamental Theorem of Asset Pricing) first, then passes to the continuous-time limit and the Black–Scholes formula, and finally extends the no-arbitrage logic to deterministic and stochastic interest-rate / term-structure models. It is a reference and teaching text rather than a research contribution. (Targeted read: front matter, preface, full table of contents, and sampled core chapters on no-arbitrage and risk-free assets; the ~320-page body of worked examples, exercises and solutions was not ingested in full.)

## Research question
Not a research paper. The pedagogical aim is: starting from the single economic principle of no arbitrage and elementary probability, how does one rigorously derive the pricing of derivative securities and the construction of optimal portfolios, at a level accessible to undergraduates? It answers how the binomial-tree, risk-neutral, and Black–Scholes frameworks fit together and how the same arbitrage reasoning governs forwards, futures, options, bonds and interest-rate derivatives.

## Method / identification
The book is organised as a sequence of formal models layered by increasing complexity:
- **Simple one-period market model** (Ch. 1): two assets — a risk-free bond and a risky stock — with the no-arbitrage principle stated as the impossibility of a self-financing strategy that turns zero initial wealth into a non-negative, sometimes-positive terminal payoff.
- **Risk-free assets** (Ch. 2): time value of money under simple, periodic and continuous compounding, with the discount factor $(1+\tfrac{r}{m})^{-tm}$ and its continuous limit $e^{-rt}$; zero-coupon and coupon bonds, money-market account.
- **Risky assets** (Ch. 3): stock-price dynamics, returns, the **binomial tree model**, derivation of the **risk-neutral probability** and the **martingale property** of discounted prices, plus the trinomial model and the continuous-time limit.
- **Discrete-time market models** (Ch. 4): multi-step self-financing strategies and the **Fundamental Theorem of Asset Pricing** linking absence of arbitrage to existence of a risk-neutral (equivalent martingale) measure.
- **Portfolio management** (Ch. 5): mean–variance analysis of two and several securities, the **efficient frontier**, and the **Capital Asset Pricing Model** (capital market line, beta factor, security market line).
- **Derivatives** (Chs. 6–9): forward and futures pricing/hedging, model-free option bounds and put–call parity, binomial option pricing, the **Cox–Ross–Rubinstein formula**, the **Black–Scholes formula**, delta hedging and the Greeks, Value at Risk.
- **Interest rates** (Chs. 10–11): deterministic term structure (yields, duration, forward rates) and stochastic interest rates via a binomial tree, arbitrage pricing of bonds, and interest-rate derivatives (options, swaps, caps and floors).
Each result is proved at undergraduate rigour, interspersed with worked examples and exercises with full solutions.

## Data
None — this is a theoretical/pedagogical text. It uses stylised numerical examples and spreadsheet exercises (Excel files provided by the authors) rather than empirical datasets.

## Key findings
As a textbook the "findings" are the standard theorems it derives and presents:
- **No-Arbitrage Principle** and its consequences (e.g. the law of one price, monotonicity of present value in $r$, $t$, $m$).
- **Risk-neutral valuation / martingale property**: discounted asset prices are martingales under the risk-neutral measure, so derivative prices are discounted risk-neutral expectations of payoffs.
- **Fundamental Theorem of Asset Pricing**: no arbitrage $\iff$ existence of an equivalent risk-neutral probability measure.
- **Cox–Ross–Rubinstein binomial option-pricing formula** and its convergence to the **Black–Scholes formula** in the continuous-time limit.
- **Put–call parity** and model-free bounds on European and American option prices.
- **Markowitz efficient frontier** and the **CAPM** relation (security market line, beta).
- Arbitrage pricing of bonds and interest-rate derivatives under deterministic and stochastic term-structure models.

## Contribution
The contribution is pedagogical and synthetic: it presents arbitrage pricing and portfolio theory together, from a unified no-arbitrage / risk-neutral viewpoint, at a genuinely introductory mathematical level (prerequisites: elementary calculus, probability, linear algebra). Its value as a citation is as a standard, rigorous reference for the binomial model, risk-neutral pricing, the FTAP, Black–Scholes, mean–variance/CAPM, and basic term-structure modelling — useful background for any economic or ML work that touches asset pricing, discounting, or financial risk.

## Limitations & open questions
The book makes no research claims and lists no open problems; its scope is deliberately bounded to undergraduate material. Implicit boundaries that a reader should note: it stays largely in discrete time, treating continuous-time Black–Scholes as a limit rather than developing full stochastic calculus (Itô, measure-theoretic martingale theory); it does not cover incomplete markets, transaction costs, stochastic volatility, jump processes, or modern term-structure models (Heath–Jarrow–Morton, affine models) in depth. The authors point readers to their companion measure-theoretic texts for the probabilistic foundations.

## Connections
The treatment of binomial option pricing follows Cox, Ross & Rubinstein (1979), and the continuous-time limit yields the Black & Scholes (1973) and Merton (1973) formula. The portfolio chapter develops Markowitz (1952) mean–variance optimisation and the Sharpe–Lintner Capital Asset Pricing Model. The risk-neutral/martingale and Fundamental-Theorem-of-Asset-Pricing material descends from Harrison & Kreps (1979) and Harrison & Pliska (1981). For the probabilistic prerequisites the authors cite their own Capiński & Zastawniak, Probability Through Problems (2001), and the measure-theoretic companion Capiński & Zastawniak, Measure, Integral and Probability. The interest-rate chapters connect to the term-structure and short-rate modelling literature (e.g. Vasicek, Ho–Lee, and the forward-rate framework of Heath, Jarrow & Morton). Within mathematical-finance pedagogy it sits alongside Hull's Options, Futures, and Other Derivatives and Shreve's Stochastic Calculus for Finance as a more elementary, mathematically explicit entry point.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
