---
citekey: Prendergast2002a
title: The Tenuous Trade‐off between Risk and Incentives
authors: ["Prendergast, Canice"]
year: 2002
type: journalArticle
doi: 10.1086/341874
zotero: "zotero://select/library/items/5G2MMX5A"
pdf: /Users/jesper/Zotero/storage/T9WTM8IG/Prendergast - 2002 - The Tenuous Trade‐off between Risk and Incentives.pdf
tags: [literature]
keywords: [principal-agent, incentive-contracts, risk-incentive-tradeoff, delegation, uncertainty, output-monitoring]
topics: []
related: [Ackerberg2002, Aggarwal1999, Aghion1997, Lazear2000, Prendergast1996]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Empirical work testing for a negative trade‐off between risk and incentives has not had much success: the data suggest a positive relationship between measures of uncertainty and incentives rather than the posited negative trade‐off. I argue that the existing literature fails to account for an important effect of uncertainty on incentives through the allocation of responsibility to employees. When workers operate in certain settings, firms are content to assign tasks to workers and monitor their inputs. By contrast, when the situation is more uncertain, they delegate responsibility to workers but, to constrain their discretion, base compensation on observed output.

## Summary
The canonical principal-agent prediction is that incentive pay should fall as the environment grows noisier, because output-based contracts impose costly risk on risk-averse agents. The data refuse to cooperate: across sharecropping and franchising, and ambiguously across executives, incentive pay is often *positively* correlated with uncertainty. Prendergast argues the literature has omitted a second channel through which uncertainty operates: the *allocation of responsibility*. In stable settings the principal knows what the agent should do, so she assigns tasks and monitors inputs cheaply. In uncertain settings she does not know the right action, so she delegates discretion to the better-informed agent and uses output-based pay to align his choice. Delegation and incentive pay therefore travel together with uncertainty, reversing the textbook sign. The reversal is itself fragile: it depends on having reliable output measures, and can flip back if measurement distortion (multitasking) worsens with uncertainty.

## Research question
Why does empirical work fail to find the predicted negative relationship between environmental uncertainty (risk) and the strength of pay-for-performance incentives, and under what conditions should we instead expect a *positive* relationship?

## Method / identification
A theoretical agency model with a deliberately stripped-down information structure. A principal hires an agent who can exert effort on one of $n$ tasks. Output on task $i$ is $y_i = r_i + e_i$, with effort cost $C(e_i)$ satisfying $C'>0$, $C''>0$, $C'(0)=0$. The $r_i$ are drawn from a common distribution with mean $\bar r_i$ and variance $\sigma^2$; raising $\sigma^2$ is the operational definition of a more uncertain environment. All parties are *risk-neutral* — a modeling choice that deliberately shuts off the standard risk-sharing channel so the delegation channel can be isolated. The agent privately knows the realized $r_i$ and his own small private benefits $B_i$; the principal knows only the distribution.

The principal can monitor inputs at cost $m_e$ or output at cost $m_y$, with $m_y > m_e$ (output monitoring is a metaphor for any deadweight cost of incentive pay). Two strategies are compared: (i) **assign a task + input contract** $w(e_i)=C(e_i)$, which yields the assigned mean $\bar r_k$; (ii) **delegate + output contract**, under which the agent selects the highest realized $r_i$, i.e. the first-order statistic $r_{1\{n\}}^{*}$. The key comparative static is that the value of sampling the first-order statistic rises with $\sigma$ while the value of assignment does not. For a distribution with mean $\bar r$ and variance $\sigma^2$, $E[r_{1\{n\}}^{*}] = \bar r + \sigma H_n$, where $H_n$ depends only on $n$ — linear in $\sigma$. Closed forms are derived for the normal ($n=2$, $E[r_{1\{2\}}^{*}]=\sigma/\sqrt{\pi}$) and uniform cases. Extensions add partial delegation ($n=3$), cheap-talk communication, recontracting costs under symmetric uncertainty, correlated principal-agent preferences, complexity (more tasks $n$), and a rent-seeking/Baker (1992)-style distorted measure $\hat y_i = r_i + m e_i$.

## Data
None as primary data — this is a theory paper. It does, however, marshal an extensive *survey* of prior empirical findings as motivating and corroborating evidence, tabulated by sign of the risk-incentive relationship: executives (Table 1, mixed: three negative, three positive, five null), sharecroppers (Table 2, all positive), the franchise decision (Table 3, positive), other industries (Table 4, no pattern), and direct monitoring costs and franchising (Table 5, uniformly positive). Specific studies (Lafontaine 1992; Rao 1971; Lafontaine & Slade 2001) are reread as supportive.

## Key findings
- **Positive risk-incentive relationship via delegation.** In the normal case, output contracting is preferred iff $\sigma/\sqrt{\pi} \ge m_y - m_e + B(n-1)/n$, giving a critical variance $\sigma^{2*} = [m_y - m_e + B(n-1)/n]^2 \pi$ above which the firm delegates and pays on output. So incentive pay *rises* with uncertainty.
- **General distributions.** Because $E[r_{1\{n\}}^{*}] = \bar r + \sigma H_n$ is linear in $\sigma$ while input-contract value is not, a single critical $\sigma$ threshold exists for any common distribution.
- **Complexity.** More tasks $n$ widens the region where output pay is optimal (e.g. $\tilde\sigma^{2*}$ for $n=3$ exceeds $\sigma^{2*}$ for $n=2$): incentive pay is *more* likely in complex jobs, contra naive multitasking intuition.
- **Robustness.** Partial delegation makes contract choice vary continuously with $\sigma$; communication and correlated preferences raise the threshold but preserve the qualitative result; recontracting costs under symmetric uncertainty deliver the same prediction.
- **The reversal (Section V).** With a corrupted measure $\hat y_i = r_i + m e_i$, $m\sim N(0,\sigma_m^2)$: if $\sigma_m^2$ is uncorrelated with $\sigma^2$, distortion acts like a fixed cost and the positive relation survives. But under $\sigma_m^2 = \tilde\sigma_m^2 + k\sigma^2$, for $k$ large enough the value of output contracting *decreases* in $\sigma^2$ and the standard negative trade-off re-emerges. Positive correlations should thus appear only where good output measures exist (franchising, sharecropping), not where measurement is poor (e.g. experimental surgery).
- **Omitted-variable interpretation.** Discretion/responsibility is rarely observed by the econometrician, so regressions of incentives on uncertainty suffer omitted-variable bias; controlling for task assignment should kill the positive relationship (consistent with Lafontaine's franchise-vs-royalty split).

## Contribution
Provides a coherent agency-theoretic explanation for a persistent empirical anomaly, by adding an endogenous *allocation-of-responsibility* margin to the standard Holmström-Milgrom (1991) linear-contract benchmark. It reframes output-based pay not merely as an effort-inducing device but as a substitute for the principal's lost ability to direct actions when she does not know the right action. It also delimits precisely when the result holds (reliable, uncertainty-invariant output measures) and reinterprets the executive/sharecropping/franchising evidence through that lens.

## Limitations & open questions
- With risk-neutral agents the strict model predicts *no* relationship between uncertainty and incentive *intensity* conditional on franchising; recovering the conventional negative slope requires re-introducing risk aversion — the two channels are not jointly modeled.
- Effort is "not clear why ... in the model at all" given first-best effort under both regimes; the role of $m_y$ as deadweight cost is a metaphor rather than a microfounded distortion (the rent-seeking example is offered to patch this).
- The reversal hinges on the sign and magnitude of $k$ (how multitasking opportunities scale with uncertainty), which is unmeasured.
- Discretion/responsibility is essentially unobserved in existing data; the central omitted variable remains empirically elusive, leaving the theory under-tested outside franchising.
- Intermediate uncertainty levels are analytically intractable ($\tilde S$ need not be monotone in $\sigma^2$).

## Connections
The benchmark is Holmström & Milgrom (1991) on multitask linear contracts and the optimal piece rate $1/[1+rC''(e)\sigma^2]$; the general agency framework traces to Grossman & Hart (1983). The delegation/authority machinery draws on [[@Aghion1997|Aghion & Tirole (1997)]] on formal and real authority and on [[@Prendergast1996|Prendergast & Topel (1996)]] on favoritism. The distorted-measure analysis follows Baker (1992) on performance-measurement and Milgrom & Roberts (1988) on influence activities, with random-monitoring logic from Becker (1968). The empirical survey leans on Lafontaine (1992), Lafontaine & Bhattacharyya (1995), and Lafontaine & Slade (2001) for franchising; Rao (1971) and [[@Ackerberg2002|Ackerberg & Botticini (2002)]] for sharecropping and endogenous matching; [[@Aggarwal1999|Aggarwal & Samwick (1999)]], Core & Guay (1999), Garen (1994), and Yermack (1995) for executive compensation; and [[@Lazear2000|Lazear (2000)]] on the monitor-versus-delegate dichotomy. It is a companion to Prendergast (2000, 2002 "Incentives and Uncertainty") and to the survey Prendergast (1999).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
