---
citekey: Prendergast1996
title: Favoritism in Organizations
authors: ["Prendergast, Canice", "Topel, Robert H."]
year: 1996
type: journalArticle
doi: 10.1086/262048
zotero: "zotero://select/library/items/5IEGVIP8"
pdf: /Users/jesper/Zotero/storage/53XRPTGY/Prendergast1996.pdf
tags: [literature]
keywords: [favoritism, subjective-performance-evaluation, principal-agent, incentive-compensation, bureaucracy, promotion, personnel-economics]
topics: ["[[career-concerns-subjective-evaluation]]"]
related: [Holmstrom1982]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Objective measures of employee performance are rarely available. Instead, firms rely on subjective judgments by supervisors. Subjectivity opens the door to favoritism, where evaluators act on personal preferences toward subordinates to favor some employees over others. Firms must balance the costs of favoritism--arbitrary rewards and less productive job assignments--against supervisors' demands for authority over subordinates. We analyze the conditions under which favoritism is costly to organizations and the effects of favoritism on compensation, the optimal extent of authority, and the use of bureaucratic rules.

## Summary
Because performance appraisals are subjective and noncontractible, supervisors can exercise personal preferences ("favoritism") when reporting on subordinates. Prendergast and Topel embed this in a standard Holmstrom–Milgrom linear-contract agency model and show that the firm rationally responds by distorting its own institutions: it flattens pay-for-performance (more equality), adopts ex-post-inefficient bureaucratic rules, under-uses the supervisor's report, and ties wages to jobs rather than individuals. The central mechanism is that the compensation scheme itself *generates* the noise it must combat—steeper incentives put more "money on the line," which induces supervisors to distort more.

## Research question
How do organizations optimally respond when performance evaluation is subjective and therefore vulnerable to supervisor favoritism? Specifically, what do the costs of favoritism imply for the slope of compensation, the optimal scope of supervisory authority, the use of bureaucratic rules, the monitoring of supervisors, and the linkage of wages to jobs?

## Method / identification
A theoretical principal–agent model. Two workers $i\in\{1,2\}$ exert effort $e^i$ producing output observed only by the supervisor:
$$y^i = e^i + \alpha^i + \epsilon^i,$$
where $\alpha^i\sim N(0,\sigma_0^2)$ is unknown ability and $\epsilon^i\sim N(0,\sigma_\epsilon^2)$. Workers have CARA utility $v^i=-\exp(-r(w^i-c(e^i)))$ with $c'>0,c''>0$. The supervisor has preferences $v_s=w_s+\eta^1 w^1+\eta^2 w^2$, where $\eta^i\sim N(0,\sigma_\eta^2)$ is privately known altruism/spite toward worker $i$ (favoritism = nonzero altruism). Rather than reporting $y^i$, the supervisor reports $\hat y^i=y^i+b^i$, where bias $b^i$ carries a quadratic distortion cost $D(b^i)=\tfrac12(b^i)^2$ (a transfer to the firm, welfare-neutral).

By Holmstrom–Milgrom, with normal errors the optimal contract is linear, $w^i=\delta+\tau\hat y^i$. The supervisor maximizes $w_s+\eta^1 w^1+\eta^2 w^2-\tfrac12(b^i)^2$, giving $b^i=\tau\eta^i$, so ex ante $b^i\sim N(0,\tau^2\sigma_\eta^2)$. The key comparative static is $\partial^2 b^i/\partial\eta\,\partial\tau=1$: steeper incentives raise distortion. Sorting is modeled by promoting the higher-evaluated worker to job B with marginal product of ability $\gamma>1$; promoting the wrong worker costs $(\gamma-1)(\alpha^j-\alpha^i)$. The firm maximizes ex ante surplus
$$\max_{\delta,\tau}\sum_{i=1}^2\Big[y^i-c(e^i)-\frac{r}{2}\tau^2(\sigma_s^2+\sigma_b^2)\Big]+2\sigma_b^2-(\gamma-1)(E\alpha\mid\alpha>0)\,\mathrm{prob}(\alpha<0\mid\hat y^1>\hat y^2),$$
with $\sigma_s^2=\sigma_\epsilon^2+\sigma_0^2$. Section 2 adds an independent firm signal $y_f=e+\epsilon_f+\alpha$ to study bureaucratic aggregation; Section 3 studies monitoring the supervisor via that signal; Section 4 is a two-period model with the supervisor as residual claimant and no reputation formation.

## Data
None—this is a pure theory paper. It motivates assumptions with the personnel/HR appraisal literature (leniency bias; ratings inflated when used for pay or promotion; same-race rater–ratee effects from Kraiger and Ford 1985) but estimates nothing.

## Key findings
- **Tendency toward equality (Section 1).** The optimal piece rate is $\tau^*=\dfrac{1-L'(\tau)}{1+rc''[\sigma_s^2+\sigma_b^2]+2(r\tau^2-2)c''\sigma_\eta^2}<\hat\tau$, where $\hat\tau=1/(1+rc''[\sigma_s^2+\sigma_b^2])$ is the optimum with exogenous bias variance. Under Assumption 1 ($r\hat\tau>2$, ensuring favoritism is net harmful), the firm flattens incentives *below* even the noisy benchmark—because the compensation scheme endogenously generates the distortion. Lemma 1 ($L'(\tau)>0$): a higher piece rate worsens job allocation.
- **Bureaucratic rules (Section 2).** When the firm has a second signal, it optimally commits to a rule that places "too little" weight on the supervisor's report relative to ex-post-efficient Bayesian aggregation. Paradoxically, committing to under-utilize the supervisor's information makes that information better (less distorted).
- **Monitoring the supervisor and "yes men" (Section 3).** Comparing the firm's signal to the supervisor's report can achieve first best with a risk-neutral supervisor, but punishing bias gives supervisors an incentive to avoid detection by making uncontroversial recommendations—creating "yes men" who second-guess the manager rather than report honestly. Distortion on appraisals and distortion of training are substitutes (via Holmstrom–Milgrom 1992), so the firm should not punish appraisal bias too harshly.
- **Tying wages to jobs (Section 4).** With the supervisor as residual claimant but no reputation, separating sorting from incentives yields zero effort (backward induction: whim-based recommendations). Attaching wages to jobs ($W>L$ for job B vs A) makes promoting an undeserving favorite costly because productivity falls; a job-B assignment occurs iff $\eta>(1-\gamma)\alpha_1/(W-L)$, so capable workers are promoted with positive probability even if disliked, restoring effort incentives—at the cost of occasional misallocation.

## Contribution
First systematic treatment of favoritism arising from *subjective, noncontractible* performance evaluation within a standard agency framework, rather than appealing to fairness or reputation. It rationalizes several pervasive but puzzling organizational practices—pay compression, decoupling appraisal from merit pay, bureaucratic seniority rules, limited supervisory discretion, and job-based (promotion-based) pay—as optimal second-best responses to supervisor bias. The deeper insight is that the inefficiency is not exogenous monitoring noise but is *caused* by the incentive scheme itself, making favoritism a theoretically distinct construct.

## Limitations & open questions
- The authors assume workers neither know nor act on supervisors' preferences (footnote 5 conjectures the quit-distortion would give similar responses) and that ability is unknown to all parties—robustness is argued, not proven.
- Favoritism via *productivity-enhancing* personal relationships is excluded; the authors note this would make monitoring (Section 3) far more problematic and is left open.
- Reputation formation is assumed prohibitively costly. They explicitly ask: is the incentive for reputation-building (fairness concerns, especially regarding discrimination against women or minorities) enough to eliminate favoritism, or could it lead to *positive* discrimination toward an otherwise unfavored group?
- The optimal tying of wages to jobs depends on parameter values trading incentive provision against misallocation; characterizing this boundary more generally is left informal.

## Connections
Built directly on Holmstrom and Milgrom (1987) linear-contract / CARA-normal foundations and extends Prendergast (1993) on subjective evaluation; the "yes men" and training-substitution results draw on Holmstrom and Milgrom (1992) and Prendergast (1993). It is positioned as complementary to but distinct from Milgrom (1988) and Milgrom and Roberts (1988, 1990) on influence costs—here the firm bears the distortion, not wasteful influence activities. [[@Holmstrom1982|Holmstrom (1982)]] career-concerns reputation effects are deliberately shut down by the assumption that promotion carries no return in the base model. The bureaucracy result connects to Milkovich and Wigdor (1991) on decoupling appraisal from merit pay. The paper anticipates later work on subjective performance evaluation, relational contracts, and the design of discretion in organizations.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
