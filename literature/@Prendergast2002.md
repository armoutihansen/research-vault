---
citekey: Prendergast2002
title: Uncertainty and Incentives
authors: ["Prendergast, Canice"]
year: 2002
type: journalArticle
doi: 10.1086/338676
zotero: "zotero://select/library/items/YZHS94TQ"
pdf: /Users/jesper/Zotero/storage/8WGL77FI/Prendergast - 2002 - Uncertainty and Incentives.pdf
tags: [literature]
keywords: [agency-theory, incentive-contracts, risk-incentive-tradeoff, subjective-performance-evaluation, favoritism, endogenous-monitoring]
topics: ["[[risk-incentive-tradeoff]]"]
related: [Holmstrom1982, Prendergast1996]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Empirical work testing for a trade‐off between risk and incentives has had, at best, mixed success. This article provides two simple reasons, associated with subjectivity of performance appraisals, why we might not expect to see any negative relationship. Both reasons relate to empirically observed problems associated with monitoring: (i) supervisors sometimes bias their evaluations based on their personal feelings toward their subordinates, and (ii) supervisors will sometimes offer evaluations that reduce their costs. These aspects of monitoring are ignored in the standard model and can reverse the usual negative trade‐off between risk and incentives.

## Summary
Standard agency theory predicts a negative trade-off between risk (environmental uncertainty) and incentive intensity: noisier performance measures impose more risk on agents, so optimal pay-for-performance should fall as uncertainty rises. Yet the empirical record is at best mixed and often shows a positive relationship. Prendergast offers two theoretical mechanisms, both rooted in the subjectivity of performance appraisals, under which incentives optimally *increase* with uncertainty even for risk-neutral agents. The first turns on supervisor favoritism interacting with a sorting motive; the second turns on endogenous, supervisor-chosen investigations. In both, the marginal cost of high-powered incentives falls as the environment gets noisier, so firms respond to uncertainty with stronger pay-for-performance.

## Research question
Why does the empirical literature fail to find the negative risk–incentive trade-off that is the workhorse prediction of agency theory, and can plausible features of subjective performance appraisal generate a *positive* relationship between environmental uncertainty and incentive intensity?

## Method / identification
Two complementary principal–agent models, both deliberately assuming a risk-neutral agent so as to shut down the standard risk-bearing channel and isolate the new mechanisms.

A baseline subjective-appraisal model is shared: a risk-neutral agent exerts effort $e$ at convex cost $C(e)$ with $C'(e)>0$, $C''(e)>0$, $C'(0)=0$. Output is unobservable/uncontractible; the supervisor sees a noisy signal $y=e+a+\varepsilon$ with $\varepsilon\sim N(0,\sigma^2)$, ability $a\sim N(0,1)$, and reports $y_s=y+b(y)$, where $b$ is the distortion.

**Model 1 — Favoritism and the incentives–sorting trade-off (Section III).** The supervisor's utility is
$$v_s = w_s + \mu w - \frac{b^2}{2},$$
where $\mu\sim N(0,\sigma_\mu^2)$ is the supervisor's (privately known) taste for the worker and $b^2/2$ is the cost of distortion. Workers get a linear contract $w=\beta_0+\beta_1 y_s$. Appraisals serve two purposes: rewarding effort and *sorting* workers to tasks (comparative advantage $a$; retain if estimated $\hat a\ge 0$, reassign otherwise). Maximizing $v_s$ gives distortion $b(\mu,\beta_1)=\mu\beta_1$, so distortion scales with incentive intensity. The posterior variance of ability rises in $\beta_1$:
$$\tilde\sigma^2=\frac{\sigma^2+\beta_1^2\sigma_\mu^2}{1+\sigma^2+\beta_1^2\sigma_\mu^2}.$$
Sorting surplus is $S(\beta_1)=k/(1+\sigma^2+\beta_1^2\sigma_\mu^2)$ with $k=0.7898$ (mean deviation of the standard normal). The optimal piece rate solves a first-order condition trading effort against sorting.

**Model 2 — Endogenous investigations (Section IV).** The supervisor is residual claimant and always under-reports, so subjective reports cannot reward effort. Verifiable incentives come only from a costly investigation yielding $y_I=e+a$ (eliminating measurement error). Investigation cost is $0$ with probability $p$, $\infty$ otherwise; the supervisor privately learns the cost and decides whether to investigate. The contract pays $\beta_0$ if no investigation and $\beta_0+\beta_1[y_I-Ey]$ if investigated. The key behavioral assumption is *endogenous* monitoring: the supervisor investigates only when he expects the outcome to favor him, i.e. when $E[a\mid y]<0$ (when $y-e^*<0$).

## Data
None — this is a pure theory paper. It is explicitly motivated by the author's earlier empirical survey (Prendergast 1999) summarizing mixed/positive risk–incentive evidence across executives, sharecropping, franchising, and salesforce compensation, and draws qualitative facts on favoritism and appraisal multiplicity from the HR-management literature, but estimates no model.

## Key findings
1. **No-sorting benchmark (eq. 6):** with favoritism but no sorting, the optimal piece rate $\tilde\beta_1=1/(1-2C''\sigma_\mu^2)>1$ exceeds unity and is *independent* of environmental risk $\sigma^2$. The piece rate exceeds one because the right to exercise favoritism is bundled with the incentive contract.
2. **Incentives–sorting trade-off (eq. 9):** adding the sorting motive lowers the optimal rate, $\beta_1^*<\tilde\beta_1$, since $\partial S/\partial\beta_1<0$: stronger incentives induce more distortion and worse task assignment.
3. **Positive risk–incentive relation via sorting (eq. 10):** $\partial^2 S/(\partial\beta_1\,\partial\sigma^2)>0$, so the marginal cost of incentives falls in $\sigma^2$ and $\beta_1^*$ is increasing in $\sigma^2$. In very noisy environments the supervisor's report is useless for sorting anyway, so distorting it is cheap; as $\sigma^2\to\infty$, $\beta_1^*\to 1/(1-2C''\sigma_\mu^2)$.
4. **Independence result (Section IV.B):** if monitoring were exogenous/random (Becker 1968 style), setting $\beta_1=1/p$ attains first-best effort independent of noise — but this is not credible.
5. **Endogenous-monitoring result (eqs. 13–15):** since investigations occur only when bad performance is suspected, the expected penalty conditional on investigation is $\beta_1 E(a\mid a+\varepsilon<0)=k\beta_1/(2+\sigma^2)$. To restore first-best effort the firm sets
$$\beta_1^*=\frac{4+2\sigma^2}{pk},\qquad \frac{d\beta_1^*}{d\sigma^2}=\frac{2}{pk}>0.$$
In noisier settings investigations are more often erroneous, so agents partly "get away with it," weakening incentives — the firm offsets with higher pay-for-performance.

## Contribution
Provides a theoretical resolution to the empirical puzzle that the canonical negative risk–incentive trade-off is poorly supported. By embedding two empirically grounded features of subjective appraisal — favoritism and cost-saving/endogenous monitoring — into otherwise standard agency models, it shows the trade-off can reverse sign for entirely incentive-related (not risk-bearing) reasons. It reframes the design problem as a trade-off between *sorting* (information value of evaluations) and *incentives*, and identifies a class of "guardian jobs" (per Baron & Kreps 1999) where investigation-based monitoring applies.

## Limitations & open questions
- Both results are obtained under *risk neutrality* to shut down the standard channel; the paper does not characterize how the new positive effects net against the classical negative trade-off when agents are risk averse — an explicit open integration problem.
- The investigation model assumes a stark cost structure ($0$ or $\infty$ with prob. $p$) and small $p$; generality beyond this is asserted (footnotes) but not fully developed.
- The supervisor is assumed paid a fixed salary independent of his report in Model 1; relaxing this is deferred to [[@Prendergast1996|Prendergast & Topel (1996)]].
- The future task-assignment period is unmodeled (reduced-form surplus $S$); the dynamics of sorting are not endogenized.
- The author lists (Section V, citing Prendergast 2000) three further, unmodeled channels for a positive relation — weaker career-concern inferences in noisy settings, delegation of decision rights, and selection of high-ability workers — each a candidate for separate formalization.

## Connections
Builds directly on the author's own empirical survey "The Provision of Incentives in Firms" (Prendergast 1999) and the companion piece "What Trade-Off of Risk and Incentives?" (Prendergast 2000), and adapts the favoritism-and-sorting machinery of [[@Prendergast1996|Prendergast & Topel (1996)]], "Favoritism in Organizations." The classical negative trade-off it pushes against originates with Holmstrom (1979); the sorting/selection technology follows Prescott & Visscher (1980). The investigation model contrasts with Becker (1968) on costly random monitoring, replacing exogenous with endogenous (supervisor-chosen) audits. Subjective performance measurement and the non-credibility of supervisor reports connect to Baker, Gibbons & Murphy (1994), Bull (1987), and Kahn & Huberman (1988), with the underlying hold-up to Prendergast (1993). The favoritism-as-influence interpretation parallels the influence-cost literature of Milgrom & Roberts (1988). Career-concern inference channels invoke [[@Holmstrom1982|Holmstrom (1982)]]. The "guardian jobs" typology is from Baron & Kreps (1999), and the empirical favoritism evidence draws on Cardy & Dobbins (1986) and Varma, Denisi & Peters (1996).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
