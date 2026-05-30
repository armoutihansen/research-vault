---
citekey: Aggarwal2002
title: "The Other Side of the Tradeoff: The Impact of Risk on Executive Compensation - A Reply"
authors: ["Aggarwal, Rajesh K.", "Samwick, Andrew A."]
year: 2002
type: journalArticle
doi: 10.2139/ssrn.337301
zotero: "zotero://select/library/items/N8H8S644"
pdf: /Users/jesper/Zotero/storage/MINJP8CZ/Aggarwal2002.pdf
tags: [literature]
keywords: [executive-compensation, principal-agent, pay-performance-sensitivity, firm-risk, incentives, empirical-corporate-finance]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Core and Guay (2001) argue that there is an increasing relation between an executive's payperformance sensitivity (incentives) and firm risk, in contrast to the findings in Aggarwal and Samwick (1999) and the predictions of principal-agent models such as Holmstrom and Milgrom (1987). They claim that including a control variable for firm size in our regression specification reverses the sign of the coefficient on firm risk. We show that their conclusions are based on errors in their empirical work, not the validity of their claim. We re-examine both our original findings and Core and Guay's findings and show that our original findings are quite robust to changes in specification—the relation between payperformance sensitivity and firm risk is decreasing as predicted by principal-agent theory.

## Summary
This is a reply (Tuck Working Paper 02-19) defending the central empirical claim of Aggarwal & Samwick (1999, *JPE*): that the CEO pay-performance sensitivity (PPS) is *decreasing* in firm risk, as principal-agent theory predicts. Core & Guay (2001) had argued the relation reverses to positive once one controls for firm size (market value of equity). Aggarwal & Samwick reject this on two grounds: (i) in their original sample, adding market value as a control leaves the risk coefficient negative and significant; (ii) Core & Guay's positive result stems not from the size control but from two empirical errors — excluding the value of options exercised when computing the change in firm-specific wealth, and silently relaxing the sample restriction to 12 months of return data (vs. 48). Correcting both errors restores a negative, significant risk coefficient. They further show the "marginal-product-of-effort" rationale for size fails empirically, and that Core & Guay's percent-return-variance specification is a misspecified test of the Schaefer/Baker–Hall model.

## Research question
Does the documented negative relation between CEO incentives (pay-performance sensitivity) and firm risk survive once firm size is controlled for? Equivalently: is Core & Guay's (2001) claim — that incentives *rise* with risk after conditioning on size, contradicting agency theory — correct, or an artifact of empirical mistakes?

## Method / identification
The empirical object is a median (LAD) regression of the dollar change in a CEO's firm-specific wealth on the dollar firm return interacted with the empirical CDF of risk. The original Aggarwal–Samwick (1999) specification (their eq. 2) is
$$w_{ijt} = \gamma_0 + \gamma_1 \pi_{jt} + \gamma_2 F(\sigma_{jt}^2)\,\pi_{jt} + \gamma_3 F(\sigma_{jt}^2) + \mu_t + \varepsilon_{it},$$
where $w_{ijt}$ is the dollar increase in CEO wealth, $\pi_{jt}$ the dollar change in firm market value, $F(\sigma_{jt}^2)$ the CDF of the variance of dollar returns over the preceding five years, and $\mu_t$ year dummies. The PPS is $\gamma_1 + \gamma_2 F(\sigma_{jt}^2)$, so $\gamma_2 < 0$ means incentives decrease in risk. Core & Guay's specification (their eq. 5) augments this with the CDF of market value $F(V_{jt-1})$ interacted with the dollar return and on its own:
$$w_{ijt} = \beta_0 + \beta_1 \pi_{jt} + \beta_2 F(\sigma_{jt}^2)\,\pi_{jt} + \beta_3 F(\sigma_{jt}^2) + \beta_4 F(V_{jt-1})\,\pi_{jt} + \beta_5 F(V_{jt-1}) + \mu_t + \varepsilon_{it}.$$
Standard errors come from 20 bootstrap replications. To interrogate *why* size matters, the authors generalize Core & Guay's structural setup. Letting firm value follow $\Delta V = \lambda(s)\,x + \varepsilon$ with $\lambda'>0$ ($\lambda$ = marginal product of effort, $s$ = firm size), the optimal linear contract has slope
$$\alpha_1^* = \frac{\lambda(s)^2}{\lambda(s)^2 + \rho k \sigma^2},$$
with $\rho$ the coefficient of absolute risk aversion and $k$ the disutility of effort. This predicts PPS *increasing* in size (holding risk fixed) and *decreasing* in dollar return variance — a testable pair of signs. For the percent-variance debate they take Core & Guay's restriction $\lambda(s)=V_{t-1}^{\eta}$, giving
$$\alpha_1^* = \frac{V_{t-1}^{2-2\eta}}{V_{t-1}^{2-2\eta} + \rho k \sigma_r^2 V_{t-1}^{2-2\eta} \cdot V_{t-1}^{2\eta-2}} = \frac{1}{1 + \rho k\,(\sigma_r V_{t-1}^{1-\eta})^2},$$
showing the correct regressor is the *single* composite $\sigma_r V_{t-1}^{1-\eta}$, not separate percent-variance and market-value terms. Since $\eta$ is unknown, they estimate the coefficient on the CDF of $\sigma_r V_{t-1}^{1-\eta}$ across the full grid $\eta \in [0,1]$ (Figures 1–2), where $\eta=0$ recovers the dollar-variance case and $\eta=1$ the percent-variance case.

## Data
ExecuComp panel of executive-year observations merged with CRSP-based return variances. The original Aggarwal–Samwick sample (October 1997 ExecuComp release) has 4,506 CEO and 14,592 non-CEO observations. The Core & Guay sample uses the October 1999 release with a tighter CEO definition; after corrections it contains 4,162 CEO observations (Core & Guay's 4,812 = 4,162 + 624 IPO-tainted observations with 12–48 months of returns + 26 with missing compensation data). Alternative size proxies are log sales, book assets, capital stock (net PP&E), and number of employees; market-to-book and CEO tenure were supplied by Core & Guay.

## Key findings
- **Robustness in the original sample (Table 1):** controlling for market value, the coefficient on dollar-return $\times$ CDF of dollar-return variance is $-9.722$ (s.e. 4.702) for CEOs and negative/significant for non-CEOs — the negative risk–incentive relation holds.
- **The reversal is an artifact (Table 2):** Core & Guay's positive coefficient ($+7.37$) arises from two errors, not the size control. (1) They exclude the value of options *exercised* during the year (inconsistent with Jensen–Murphy 1990 and with their own treatment of stock); a worked example shows this wrongly records a zero-return executive as losing wealth. (2) They use a 12-month (not 48-month) return-history cutoff, admitting 624 recent-IPO firms whose owner-founders hold large, non-contractually-optimal positions amid high return variance — mechanically inducing a positive risk–incentive correlation. Correcting both yields $-9.291$ (significant), close to the original.
- **Size proxies (Table 3):** with sales, assets, capital, or labor as the size measure, the risk coefficient is negative and significant in every specification; moreover the dollar-return $\times$ size coefficient is *negative*, rejecting the generalized model's prediction (positive) that size proxies the marginal product of effort.
- **Direct ownership-share tests (Table 4):** regressing the executive's stock+option ownership share on risk, the risk coefficient is positive *only* when market value is the size control (the one case where size–risk correlation is 0.92); with sales/assets/capital/labor, and in fixed-effects (OLS) specifications, it is negative and significant.
- **Percent-variance specification (Figures 1–2):** estimating the coefficient on $\sigma_r V_{t-1}^{1-\eta}$, the median-regression slope is negative and significant for $\eta \in [0,0.69]$; the fixed-effects slope is negative across the entire $[0,1]$ range and significant up to $\eta \approx 0.95$. Baker & Hall's preferred $\eta=0.4$ (they reject 0 and 1) lies squarely in the negative region; Core & Guay implicitly impose $\eta=1$.

## Contribution
A methodological rejoinder that (a) defends the agency-theoretic risk–incentive tradeoff against a prominent published comment, (b) shows the apparent positive relation is driven by sample-construction and wealth-measurement errors plus the near-collinearity (0.92) of market value with dollar-return variance, and (c) reframes "why size matters": real operating proxies (sales, assets, capital, labor) for the marginal product of effort all carry negative risk coefficients, so size most plausibly captures further unmeasured risk rather than productivity. It clarifies that the percent-variance vs. dollar-variance debate hinges on the unidentified size-elasticity parameter $\eta$ in the Schaefer/Baker–Hall model.

## Limitations & open questions
- The authors concede market value of equity *is* correlated with incentives; their claim is only that it does not overturn the risk relation. The deeper structural reason size matters is left as interpretation ("most natural interpretation … is that they help capture the effect of risk") rather than identified.
- The percent-variance model "cannot be tested without knowing the value of $\eta$"; $\eta$ is not independently identified here — they sweep it rather than estimate it structurally as Schaefer (1998) does or infer it from optimality as Baker & Hall (2002) do. Pinning down $\eta$ with external information is an open empirical task.
- Whether large CEO equity stakes at recent IPOs reflect owner-founder liquidity dynamics rather than optimal contracting is asserted (via Field & Hanka 2001 on lockups) but not separately modeled — a hook for explicitly modeling the IPO/lockup contracting environment.
- The marginal product of effort is "a real, not financial, variable" but remains a latent construct proxied by accounting measures; no direct measure is offered.

## Connections
Directly rejoins Aggarwal & Samwick (1999, *JPE* 107:65–105) — the article being defended — and rebuts Core & Guay (2001), whose comment was distributed as JPE-forthcoming but ultimately rejected. The theoretical backbone is the linear-contract framework of Holmstrom & Milgrom (1987, *Econometrica*), with Holmstrom (1992) quoted endorsing the negative size–incentive correlation as agency-consistent. The percent-variance/size-elasticity machinery comes from Schaefer (1998, *REStat*) and Baker & Hall (2002, *JLE*, "CEO Incentives and Firm Size"). The empirical wealth-change definition follows Jensen & Murphy (1990, *JPE*). Corroborating subsequent evidence is marshaled from Himmelberg, Hubbard & Palia (1999) — whose fixed-effects/log-sales setting the authors adopt — Kraft & Niederprum (1999) on German data, Jin (2002) distinguishing idiosyncratic from systematic risk, Garvey & Milbourn (2002) on RPE and CEO age, and the authors' own Aggarwal & Samwick (2002, *JF*) on managerial responsibility. Berk (1995) supplies the argument that market value proxies unmeasured risk factors, motivating non-market-value size measures.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
