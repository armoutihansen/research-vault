---
citekey: Benartzi1995
title: Myopic Loss Aversion and the Equity Premium Puzzle
authors: ["Benartzi, Shlomo", "Thaler, Richard H."]
year: 1995
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/U7BXCMWX"
pdf: /Users/jesper/Zotero/storage/3S9D3GCH/Benartzi1995.pdf
tags: [literature]
keywords: [behavioral-finance, myopic-loss-aversion, equity-premium-puzzle, prospect-theory, mental-accounting, loss-aversion, asset-allocation]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> (no abstract in Zotero) — The published abstract (recovered from the PDF) reads: The equity premium puzzle refers to the empirical fact that stocks have outperformed bonds over the last century by a surprisingly large margin. We offer a new explanation based on two behavioral concepts. First, investors are assumed to be "loss averse," meaning that they are distinctly more sensitive to losses than to gains. Second, even long-term investors are assumed to evaluate their portfolios frequently. We dub this combination "myopic loss aversion." Using simulations, we find that the size of the equity premium is consistent with the previously estimated parameters of prospect theory if investors evaluate their portfolios annually.

## Summary
Benartzi and Thaler propose a behavioral resolution of the Mehra-Prescott equity premium puzzle by combining two ingredients from the psychology of decision-making: **loss aversion** (investors weigh losses roughly $2.25\times$ as heavily as equal-sized gains) and **mental accounting** with short evaluation periods (even investors with long planning horizons re-evaluate their portfolios often). The combination — dubbed *myopic loss aversion* — makes risky equities look unattractive because frequent evaluation exposes the investor to more frequent paper losses. Feeding the experimentally estimated parameters of cumulative prospect theory into simulations of historical CRSP returns, the authors find that the observed equity premium is exactly what one would expect if the representative investor evaluates returns about **once a year**. The same one-year evaluation period also rationalizes the observed near 50-50 stock/bond split of large institutional and individual portfolios.

## Research question
Why is the equity premium so large (≈6.5% per year over 1926-1990) — equivalently, why is anyone willing to hold bonds — given that standard expected-utility models require implausible relative-risk-aversion coefficients (Mehra-Prescott estimate >30, versus a plausible value near 1.0) to reconcile it? Reframed in the authors' own terms: if investors have prospect-theory preferences, **how frequently would they have to evaluate their portfolios** for the historical premium to be an equilibrium? And given that evaluation period, what asset allocation is optimal?

## Method / identification
The model of the individual is **cumulative prospect theory** [Tversky and Kahneman 1992], used with the authors' published representative-agent parameters rather than parameters fit to the asset-return data (a deliberate discipline). Utility is defined over gains/losses (returns) relative to a moving status-quo reference point, via the value function
$$v(x) = \begin{cases} x^{\alpha} & x \ge 0 \\ -\lambda(-x)^{\beta} & x < 0, \end{cases}$$
with estimated $\alpha=\beta=0.88$ and loss-aversion coefficient $\lambda=2.25$. The prospective utility of a gamble $G$ paying $x_i$ with probability $p_i$ is
$$V(G) = \sum_i \pi_i\, v(x_i),$$
where the decision weights $\pi_i$ are derived from a *rank-dependent* nonlinear transform $w(\cdot)$ of the cumulative distribution: with $P_i$ the probability of an outcome at least as good as $x_i$ and $P_i^{*}$ the probability of one strictly better, $\pi_i = w(P_i) - w(P_i^{*})$ (applied separately over gains and losses). They use the one-parameter weighting form
$$w(p) = \frac{p^{\gamma}}{\left(p^{\gamma} + (1-p)^{\gamma}\right)^{1/\gamma}},$$
with $\gamma = 0.61$ for gains and $0.69$ for losses.

The key conceptual move is separating the **evaluation period** (how often returns enter the value function as realized gains/losses) from the **planning horizon**. Because prospect-theory utility is carried by changes in wealth and is approximately wealth-independent, an investor who evaluates annually behaves like one with a one-year horizon regardless of the true horizon.

**Identification is via simulation.** For each candidate $n$-month evaluation period, they draw 100,000 $n$-month returns with replacement from the 1926-1990 CRSP monthly series for stocks, five-year bonds, and T-bills (sampling with replacement removes serial correlation; they argue mean reversion is trivial at these short horizons and would only deepen the puzzle). Returns are ranked and discretized into 20 cumulative intervals to feed the rank-dependent weights, and the prospective utility $V$ of each asset is computed. (1) The **equilibrium evaluation period** is the $n$ at which the prospective utilities of stocks and bonds cross. (2) As a reliability check grounded in optimization, they fix a one-year horizon and compute $V$ for every stock/bond mix in 10% increments to find the optimal allocation. (3) They invert the exercise to trace the implied equity premium as a function of the evaluation period.

## Data
Historical monthly real and nominal returns on the CRSP value-weighted stock index, five-year government bonds, and Treasury bills, 1926-1990. The empirical equity premium in their sample is ≈6.5% per year. External corroborating figures: Siegel's 1802-1990 return series; MaCurdy-Shoven retirement-saving simulations; and observed institutional allocations (Greenwich Associates ≈47% bonds / 53% stocks; TIAA-CREF modal allocation of 50-50).

## Key findings
- **Equilibrium evaluation period ≈ one year.** For nominal stock-versus-bond returns the prospective-utility curves cross at about **13 months**; for real returns at **10-11 months**. Across all four specifications (stocks vs. bonds and vs. T-bills, real and nominal) the crossing is "in the neighborhood of one year" — a strikingly plausible figure, matching tax years and annual reporting cycles.
- **Loss aversion, not probability weighting, drives the result.** Replacing the weighting function with actual probabilities moves the crossing only modestly; with a piecewise-linear value function ($v(x)=x$ for $x\ge0$, $v(x)=2.25x$ for $x<0$) and linear probabilities the crossing is 8 months, and a 12-month evaluation period corresponds to a loss-aversion factor of 2.77. The specific functional forms are not critical.
- **Optimal allocation ≈ 50-50.** Under a one-year evaluation period, portfolios with roughly **30-55% in stocks** yield approximately equal (near-maximal) prospective utility, matching observed individual and institutional behavior.
- **The premium is decreasing in the evaluation period.** With their parameters the 6.5% premium maps to a one-year period; the implied premium falls to 4.65% at two years, 3.0% at five, 2.0% at ten, and 1.4% at twenty years. Hence an investor with a 20-year horizon who nonetheless evaluates annually pays a "psychic cost" of ≈5.1% per year — "the price of excessive vigilance."
- **Organizations also exhibit myopic loss aversion, via agency.** Defined-benefit pension funds and university/foundation endowments have effectively infinite horizons yet hold ≈40-60% bonds. The authors argue short managerial horizons (a manager/CFO who must report funding levels regularly) and binding spending rules (spend $x\%$ of an $n\le5$-year moving average of endowment value) reproduce myopic loss aversion as an *agency* phenomenon — for foundations, "an agency problem without a principal."

## Contribution
Introduces the concept of **myopic loss aversion** and demonstrates that it quantitatively reconciles the equity premium puzzle without invoking implausible risk aversion. The paper is foundational in behavioral finance: it shifts the carrier of utility from the consumption stream to returns themselves, shows that the puzzle is sensitive to the *frequency of evaluation* (a manipulable policy variable, not just a fixed preference), and connects laboratory prospect-theory parameters to a major asset-pricing anomaly. It also reframes the magnitude of the premium as a quantity that would shrink if investors lengthened their evaluation horizon, and extends the explanation from individuals to institutions through agency costs.

## Limitations & open questions
- The mechanism shifts utility onto returns even when "short-run returns have no effect on consumption"; whether this is a genuine preference or a framing artifact is acknowledged but not resolved.
- **House-money / path dependence:** the model assumes a fresh reference point each period, but Thaler-Johnson's house-money effect (prior gains reduce subsequent loss aversion) could qualify the annual-reset assumption.
- The institutional story is an explicit *agency* conjecture rather than a tested structural model; the authors suggest pension asset allocation could be "a useful domain for measuring firms' horizons" — an empirical program left open.
- They explicitly take up Mehra and Prescott's challenge that any alternative preference structure must also organize observations in growth theory, business-cycle theory, and labor markets; they concede prospect theory "has not yet been applied in all the contexts Mehra and Prescott cite," leaving cross-domain validation open.
- A connected **risk-free-rate puzzle** is flagged: a framing-plus-money-illusion story (nominal T-bills as an illusory sure gain) is sketched but not modeled.
- Simulation removes serial correlation by construction; reconciling the explanation with documented long-horizon mean reversion is noted as a concern (argued away at short horizons) rather than fully integrated.
- No single evaluation period fits all investors; the one-year figure is a plausible central case, not an estimated population parameter.

## Connections
The paper sits directly against **Mehra and Prescott [1985, 1988]**, whose puzzle it answers, and the rational-resolution literature it argues is incomplete: **Reitz [1988]** (catastrophe risk), **Weil [1989]** and **Epstein-Zin [1990]** (Kreps-Porteus / Yaari non-expected-utility, which Weil shows merely transmutes the puzzle into the risk-free-rate puzzle), **Mankiw-Zeldes [1991]** (limited stock-market participation), and especially **Constantinides [1990]** habit formation — whose gain/loss asymmetry the authors endorse but relocate from consumption to returns. The preference model is **Kahneman-Tversky prospect theory [1979]** and its **cumulative** form [Tversky-Kahneman 1992], with loss aversion calibrated against the endowment-effect experiments of **Kahneman, Knetsch, and Thaler [1990]** and **Tversky-Kahneman [1991]**, and mental accounting from **Thaler [1985]**. The horizon result deliberately contrasts with the classic **Merton [1969]/Samuelson [1969]** constant-allocation theorem and with **Samuelson's [1963]** repeated-bet fallacy. The agency extension draws on **Shleifer-Vishny [1990]** and **Lakonishok-Shleifer-Vishny [1992]** on short investor horizons. This work is itself the seed of a large myopic-loss-aversion experimental literature (e.g., Thaler-Tversky-Kahneman-Schwartz 1997 and Gneezy-Potters 1997).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
