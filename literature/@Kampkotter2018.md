---
citekey: Kampkotter2018
title: "More Dispersion, Higher Bonuses? On Differentiation in Subjective Performance Evaluations"
authors: ["Kampkötter, Patrick", "Sliwka, Dirk"]
year: 2018
type: journalArticle
doi: 10.1086/694588
zotero: "zotero://select/library/items/MAXCHUKF"
pdf: /Users/jesper/Zotero/storage/ID2P3LQV/Kampkotter2018.pdf
tags: [literature]
keywords: [subjective-performance-evaluation, bonus-pools, rating-compression, differentiation, personnel-economics, inequity-aversion]
topics: []
related: [Bolton2000, Fehr1999, Gibbons1992, Lazear1981, Ockenfels2015, Prendergast1996, Prendergast2002]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We investigate the claim that supervisors do not differentiate enough between high- and low-performing employees when evaluating performance. In a first step, this claim is illustrated in a formal model showing that rating compression reduces performance and subsequent bonus payments. The effect depends on the precision of performance information and may be reversed when cooperation is important. We then investigate panel data spanning different banks and find that stronger differentiation indeed increases subsequent bonus payments. The effect tends to be larger for larger spans of control and at higher hierarchical levels but is reversed at the lowest levels.

## Summary
Most employee bonuses are based on a supervisor's subjective appraisal, and a recurring complaint is that supervisors "compress" ratings — failing to separate high from low performers. Kampkötter and Sliwka formalize why such compression dampens effort incentives and shrinks the bonus pool, then test the implications on a large panel of German banks. They find that greater within-unit differentiation in bonuses in one year predicts substantially higher individual bonuses the next year (about a 31% rise from the lowest to highest quintile of differentiation), with effects strongest where the span of control is large and at higher hierarchical levels, but reversed at the bottom level — consistent with the model's prediction that differentiation can backfire when cooperation matters or career concerns dominate.

## Research question
To what extent, and under which organizational circumstances, does the degree of differentiation in bonus payments within a work unit affect employees' subsequent bonus payments? Equivalently: does rating compression by supervisors lower performance incentives, and how is this moderated by span of control, measurement precision, hierarchical level, and task interdependence?

## Method / identification
The paper combines an illustrative principal–multi-agent model with a fixed-effects panel analysis.

**Model.** $n$ risk-neutral agents have unknown ability $a_i\sim N(\mu_i,\sigma_a^2)$, choose effort $e_i$ at cost $c(e_i)$, and produce $y_i=e_i+a_i$. A supervisor observes noisy signals $s_i=y_i+\eta_i$ with $\eta_i\sim N(0,\sigma_\eta^2)$ and a verifiable revenue signal $P=p\sum_i s_i$. Wages are linear in the reported rating, $w_i=\alpha+\beta r_i$, paid out of a bonus pool $B=k\,P$ subject to the budget constraint $\beta\sum_i r_i = B$. The supervisor's utility trades off **accuracy** (weight $\nu_A$, penalizing $E[(r_i-y_i)^2\mid s_i]$) against **equity** (weight $\nu_E$, penalizing deviations of $\beta r_i$ from the equal share $B/n$). The key composite parameter is the **preference for differentiation** $\nu_D=\nu_A/\nu_E$. Solving the supervisor's constrained problem yields optimal reports (Proposition 1); substituting these into the agents' first-order conditions yields equilibrium effort (Proposition 2). Comparative statics in span of control, precision, and interdependence give Propositions 3–6.

**Empirics.** A balanced employee panel is constructed and organizational "cells" are defined by year × company × functional area × detailed function × career ladder × hierarchical level. Within-cell bonus dispersion is measured three ways — coefficient of variation, P90/P10 ratio, and standard deviation of logs. The core specification regresses the log subsequent individual bonus on lagged cell dispersion with **employee fixed effects** and year dummies:
$$\ln b_{it}=\beta\,\sigma_{c_i,t-1}+X_{it}'\gamma+a_i+\lambda_t+\varepsilon_{it},$$
identifying off within-employee, over-time variation in the dispersion of their unit. The identifying assumption is that omitted determinants of bonuses are time-invariant; to support it, the baseline sample excludes movers (employees who changed level, function, area, or career ladder), and robustness checks add lagged-dependent-variable and instrumental-variable specifications. Standard errors are clustered at the cell level.

## Data
A panel of compensation data on the German banking and financial-services sector for 2005–2007, owned by the consultancy Towers Watson and used for wage benchmarking. It covers more than 50 banks; for a subset of 18 banks employees can be tracked over time (~12,000 individuals). It records base salary, bonus, age, tenure, six hierarchical levels, functional area, and ~60 specific functions, with standardized cross-firm job evaluation. The model section is also informed by a 2013 Towers Watson survey of 36 bonus plans at 25 banks in Germany, Austria, and Switzerland.

## Key findings
- **Proposition 1 (reporting).** Ratings increase in absolute team performance $\sum_j s_j$ and in the agent's relative performance $s_i-\tfrac1n\sum_j s_j$. For given signals, the within-team SD of ratings falls with equity weight $\nu_E$ and rises with accuracy weight $\nu_A$. Less precise signals (higher $\sigma_\eta^2$) pull ratings toward priors, a second source of compression.
- **Proposition 2 (incentives).** Effort and the expected bonus pool rise with the preference for differentiation $\nu_D$ and with signal precision $1/\sigma_\eta^2$. Hence higher past differentiation should raise subsequent average bonuses — the central testable hypothesis.
- **Proposition 3 (span of control).** The incentive gain from greater differentiation is larger when the span of control $n$ is larger: small teams make differentiation costly under the budget constraint.
- **Proposition 4 (precision).** The benefit of differentiation is larger when performance measures are more precise.
- **Proposition 5 (endogenous precision).** When the firm chooses precision, optimal precision rises with task profitability $p$ — implying more precision (and bigger differentiation effects) at higher levels.
- **Proposition 6 (interdependence).** With helping/cooperation effort, a higher $\nu_D$ reduces helping; when spillovers are large, differentiation's net effect can turn negative.
- **Empirical core.** Differentiation significantly raises future bonuses for all three measures; moving from the lowest to highest dispersion quintile raises bonuses by roughly 31–36%.
- **Heterogeneity.** Effects are stronger with larger span of control (weakly significant interaction), strongest at intermediate and high hierarchical levels, but **reversed (negative) at level 1**. Differentiation and promotion probability are complements, not substitutes. Effects are largest in retail banking and capital-market functions, where performance is more objectively measurable.

## Contribution
The paper supplies a tractable model linking equity-versus-accuracy preferences in subjective evaluation to rating compression, effort, and bonus-pool size, generating sharp, sign-identified moderators (span of control, precision, interdependence). It then provides large-scale field evidence — across many firms in one industry, with employee fixed effects — that compression depresses, and differentiation raises, subsequent pay, while documenting the boundary case (lowest levels) where more differentiation is harmful. It thereby bridges the management debate over forced ranking with personnel-economics theory and credible identification.

## Limitations & open questions
- Subsequent bonus payments are used as a **proxy for performance**; the authors note this rests on bonus pools scaling with unit financial success and do not observe output directly.
- The hierarchical-level analysis is described as **exploratory**, since level differences confound several model parameters (precision, interdependence, career concerns); the reversal at the lowest level admits multiple explanations (cooperation, career concerns à la Gibbons–Murphy) that the data cannot fully separate.
- Identification relies on the assumption that omitted bonus determinants are time-invariant; despite mover exclusions and IV/LDV checks, residual endogeneity of differentiation (firms placing strong differentiators where effort is profitable) cannot be wholly ruled out.
- Span-of-control is a constructed average measure; interdependence is inferred indirectly rather than observed, leaving the cooperation channel only suggestively tested.
- Top executives and stock-option compensation are outside the sample, and the window (2005–07) predates the financial crisis, bounding external validity.

## Connections
The accuracy-versus-distortion framing of subjective evaluation builds directly on [[@Prendergast1996|Prendergast and Topel (1996)]] and [[@Prendergast2002|Prendergast (2002)]]; the equity/centrality-bias channel draws on inequity-aversion models of [[@Fehr1999|Fehr and Schmidt (1999)]] and [[@Bolton2000|Bolton and Ockenfels (2000)]], and on field evidence in [[@Ockenfels2015|Ockenfels, Sliwka, and Werner (2015)]]. The complementarity of subjective and objective signals connects to Ittner, Larcker, and Meyer (2003), Gibbs and Hendricks (2004), Bol and Smith (2011), and Manthei and Sliwka (2015). The cooperation cost of differentiation echoes Lazear (1989), while the experimental counterpart on forced distribution is Berger, Harbring, and Sliwka (2013). The career-concerns interpretation of the lowest-level reversal invokes [[@Lazear1981|Lazear and Rosen (1981)]], Holmström (1982), [[@Gibbons1992|Gibbons and Murphy (1992)]], and Waldman (2013). The span-of-control "scale of operations" logic follows Smeets, Waldman, and Warzynski (2015), and bonus-pool theory rests on Baiman and Rajan (1995) and Rajan and Reichelstein (2006, 2009).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
