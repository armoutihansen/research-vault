---
citekey: Sydnor2010
title: (Over)insuring Modest Risks
authors: ["Sydnor, Justin"]
year: 2010
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/M3JAV5VJ"
pdf: /Users/jesper/Zotero/storage/BF2ZMK95/Sydnor2010.pdf
tags: [literature]
keywords: [risk-aversion, insurance-deductibles, rabin-critique, reference-dependent-preferences, modest-stakes, field-evidence]
topics: []
related: [Kahneman1979, Kamenica2008, Koszegi2006b, Tversky1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Despite the large literature on anomalies in risky choice, very little research has explored the relevance of these insights in real insurance markets. This paper uses new data on consumers' choices of deductibles for home insurance to provide evidence that a surprising level of risk aversion over modest stakes is a reality in the market. Most customers purchase low deductibles despite costs significantly above the expected value. Fitting these choices to a standard model of risk aversion yields implausibly large measures of risk parameters. Potential explanations and the implications of these results for understanding the market for insurance are discussed.

## Summary
Using a random sample of 50,000 US home-insurance policies, Sydnor shows that the vast majority of homeowners buy low deductibles at prices far above the expected value of the extra coverage — paying on average roughly five times what that coverage is worth. Rationalizing these choices inside a standard expected-utility-of-wealth model requires coefficients of relative risk aversion in the thousands, hundreds to thousands of times larger than estimates from labor-supply and lifecycle-consumption studies. This is the first micro-level field evidence that the "Rabin critique" bites in a real, important insurance market, and the paper argues that reference-dependent preferences (Kőszegi–Rabin), not the diminishing marginal utility of wealth, are the more plausible driver of aversion to modest stakes.

## Research question
Do people exhibit economically significant risk aversion over *modest* financial stakes in a real market, and if so, can the standard expected-utility-of-wealth model accommodate that behavior with plausible preference parameters? The paper operationalizes this through the choice of home-insurance deductibles, where opting below the maximum deductible is exactly a purchase of a small amount of extra insurance ($500–$900 of downside protection).

## Method / identification
The empirical object is a discrete choice from a menu of four deductibles ($1,000, $500, $250, $100). The company prices deductibles via a standard actuarial scheme: for customer $i$, the premium for deductible $D_j$ is $\text{Premium}_i = \delta_j f(X_i) + g(X_i)$, where $f(X_i)$ is a proprietary base price (roughly linear in insured home value), $\delta_j$ is a deductible-specific multiplicative factor, and $g(X_i)$ an additive adjustment. Because the multiplier scales the base premium, customers with higher home values face higher *marginal* costs for lower deductibles — generating cross-sectional variation in price exploited descriptively.

For the structural piece, Sydnor follows Chetty (2006) and treats choices as maximizing an indirect utility-of-wealth function over lifetime (permanent-income) wealth. With at most one loss of probability $\pi$, the value of contract $(P,D)$ is
$$V(P,D,\pi) = \pi\,u(w - P - D) + (1-\pi)\,u(w - P),$$
and allowing multiple per-claim losses the customer solves $\max_j \sum_n \pi_n\, u(w - P_j - nD_j)$. The key identification device: observing a choice from the menu places **bounds** on the curvature parameter. A $1,000-deductible buyer reveals an upper bound on risk aversion; a $500 buyer reveals both a lower and upper bound (she preferred $500 to both $250 and $1,000). Bounds are computed individually via a numerical search for the indifference cutoff under CRRA, $u(x)=x^{1-\rho}/(1-\rho)$, and CARA, $u(x)=-(1/r)e^{-rx}$. Robustness varies lifetime wealth ($1M down to $5k, and insured home value) and subjective claim rates (deductible-level averages vs. Poisson-regression individual predictions). Analysis focuses on *new* customers to purge consumer inertia, since longer-tenured customers hold lower deductibles largely because deductibles were historically cheaper relative to rising home values (and renewal notices omit the current menu).

## Data
A random sample of 50,000 standard home-insurance policies from one large company in a single western US state, for one post-2000 year. Includes policy parameters, all rating variables, the full available deductible–premium menu per customer, and individual claims data (number of paid claims and payouts). Excludes renters, commercial, and condo policies; flood and earthquake are excluded as usual.

## Key findings
- **Over-insurance is pervasive and costly.** 82.7% of customers held a middle deductible (48% at $500, 35% at $250); only 17% held the $1,000 deductible. The average $500-deductible buyer paid about $100 for coverage worth under $25 in expectation (claim rate ≈ 4.3%, ex-post value ≈ $19.93) — roughly five times its actuarial value. A risk-neutral buyer would need a subjective claim rate above 20% to justify the $500 deductible.
- **Implied risk aversion is implausible.** Under CRRA with $1M lifetime wealth, the median $500 buyer's choice implies relative risk aversion bounded between 1,839 and 5,064; $250 buyers between 4,337 and 14,032. These are ~1,000× the single-digit estimates of Chetty (2006) and Gourinchas–Parker (2002). Results are robust to CARA and to drastically lower wealth: even at $100k wealth the lower bounds exceed 100× standard estimates.
- **Rabin critique made concrete.** Under the baseline preferences, 99.95% of new low-deductible customers would reject *any* 50/50 gamble with a $1,000 downside, regardless of the upside.
- **Explanations assessed.** Risk misperception would require subjective claim rates ~18% (5× actual); consumption commitments (Chetty–Szeidl) raise local CRRA only to ~7.4 — orders of magnitude short; borrowing constraints, sales-agent pressure, and menu effects each fail as a full account. Standard prospect theory cannot explain it (insurance is entirely in the loss domain, away from the kink, and probability weighting alone covers only ~half the willingness to pay, ≈$45). Kőszegi–[[@Koszegi2006b|Rabin (2006]], 2007) reference-dependence, where money paid up front is a "cost" not a "loss" (the Novemsky–Kahneman "no loss in buying" idea), yields $\Delta P = \lambda\, w(\pi)\,\Delta D$; with $\lambda = 2.25$ this predicts a willingness to pay just over $100 — matching the data with off-the-shelf parameters.
- **Supply side.** The firm does not earn excess profits on low-deductible customers because they have higher claim rates (consistent with adverse selection); marginal cost is not actuarially fair, but average cost is justified, so the $4.8B/year aggregate "savings" is only a partial-equilibrium figure.

## Contribution
First micro-level field evidence that significant aversion to modest-scale risk is real in a major insurance market, directly validating Rabin's (2000) calibration critique with market (not lab) data. It shows the diminishing marginal utility of wealth cannot explain attitudes toward moderate stakes, and demonstrates that the newer Kőszegi–Rabin reference-dependent framework can rationalize the demand for low deductibles with existing parameter estimates — motivating the use of behavioral preference models in applied insurance economics.

## Limitations & open questions
- Subjective beliefs are unobserved, so risk misperception cannot be ruled out conclusively (though it would require implausibly large, widespread bias).
- Data cannot decisively discriminate among the candidate explanations; the reference-dependence account is suggestive, not tested.
- **Reconciling cross-study heterogeneity:** Cohen–Einav (2007) find much lower risk aversion for Israeli auto deductibles. Is the gap population heterogeneity, or does probability weighting (much steeper overweighting at the ~4–5% home-loss probability than at the 20–30% auto range) drive it? Sydnor flags this as an explicit direction for future work.
- Welfare and policy implications of systematic over-insurance (for health insurance, annuities) are raised but not worked out.
- General-equilibrium supply-side response — how prices and contract menus adjust if consumers stopped over-insuring — is only sketched.

## Connections
The theoretical anchor is Rabin (2000) and Rabin–Thaler (2001) on the impossibility of explaining modest-stakes risk aversion via expected-utility curvature; the wealth/permanent-income modeling follows Chetty (2006) and Chetty–Szeidl (2007). It contrasts with field studies reporting low modest-stakes risk aversion — Cicchetti–Dubin (1994) and Cohen–Einav (2007) — and complements lab evidence (Holt–Laury 2002; Harrison–Rutström 2008). The favored explanation builds on prospect theory ([[@Kahneman1979|Kahneman–Tversky 1979]]; [[@Tversky1992|Tversky–Kahneman 1992)]], Kőszegi–Rabin (2006, 2007) reference-dependent preferences, and Novemsky–Kahneman (2005) "no loss in buying." Inertia connections draw on Madrian–Shea (2001), Carroll et al. (2009), and DellaVigna–Malmendier (2006); menu effects relate to [[@Kamenica2008|Kamenica (2008)]]. The paper sits in the broader insurance-anomalies literature (Kunreuther–Pauly 2006; Cutler–Zeckhauser 2004).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
