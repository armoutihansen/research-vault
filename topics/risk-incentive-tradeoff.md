---
slug: risk-incentive-tradeoff
title: "The Risk-Incentive Tradeoff (Theory & Evidence)"
type: topic
scope: "The canonical agency prediction that incentive intensity falls with environmental noise, and the tenuous empirical record."
area: "[[contracts-incentives-personnel]]"
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This topic covers the canonical moral-hazard prediction that incentive intensity should *fall* as the environment grows noisier — formally, the Holmström–Milgrom optimal piece rate $\alpha_1^\*=1/(1+r k\sigma^2)$ with $\partial\alpha_1^\*/\partial\sigma^2<0$ — and the stubborn empirical record that mostly fails to confirm it. Members span the theory of the tradeoff, the proposed reasons it reverses sign (favoritism, endogenous monitoring, allocation of responsibility), and the field/quasi-experimental evidence on executives, sharecroppers, whalers, and piece-rate workers. The boundary excludes the broader contract-theory and tournament literatures except where they bear directly on the risk-noise–incentive-intensity link; pure performance-pay-and-productivity work enters only via the selection/sorting confounds it exposes.

## Sub-themes

- **Theory of why the negative tradeoff reverses.** [[@Prendergast2002|Prendergast (2002)]] derives a *positive* relation from favoritism-plus-sorting and from endogenous (supervisor-chosen) investigations; [[@Prendergast2002a|Prendergast (2002a)]] adds the allocation-of-responsibility channel — uncertain settings force delegation, and output pay disciplines delegated discretion. [[@Schmitz2005|Schmitz (2005)]] is the formal outlier: a limited-liability, complete-contracting model where control allocation, not risk, drives incentive structure.
- **Executive-compensation evidence (the showcase test).** [[@Aggarwal1999|Aggarwal & Samwick (1999)]] reframe the test from PPS *level* to its comparative static and find PPS strongly decreasing in return variance; [[@Aggarwal2002|Aggarwal & Samwick (2002)]] defends this against Core & Guay's size-control reversal.
- **Quasi-experimental and structural field evidence.** [[@Hilt2008|Hilt (2008)]] uses Confederate commerce-raiders as a risk shock to whaling shares and recovers the negative tradeoff; [[@Ackerberg2002|Ackerberg & Botticini (2002)]] show endogenous matching contaminates Tuscan sharecropping regressions; [[@Grund2010|Grund & Sliwka (2010)]] measure *agent* risk aversion directly in the GSOEP.
- **Selection/sorting as the master confound.** [[@Lazear2000|Lazear (2000)]] (Safelite) and [[@Bloom2015|Bloom et al. (2015)]] (Ctrip WFH) decompose incentive effects from sorting with a recurring ~2:1 selection-to-treatment ratio; [[@Lazear2007|Lazear & Oyer (2007)]] surveys why the tradeoff is "empirically elusive."

## Cross-paper tensions

The sharpest tension is **whether the negative tradeoff exists at all in the data, and if not, why.** [[@Aggarwal1999|Aggarwal & Samwick (1999)]] and [[@Hilt2008|Hilt (2008)]] claim it does — once you test the right object (the PPS comparative static, not its level) or find a clean exogenous risk shock. The Prendergast pair claims the *opposite sign* is the rational equilibrium: in [[@Prendergast2002a|Prendergast (2002a)]] incentives and delegation rise together with $\sigma^2$, so a positive correlation is not a refutation of agency theory but a prediction of it. These cannot both be the default reading of the same cross-sectional regressions.

A second tension is **what "risk" means.** The theory's $\sigma^2$ is *environmental noise in the signal*, but [[@Grund2010|Grund & Sliwka (2010)]] move the test to *agent risk aversion* $r$ — a logically distinct primitive in the same formula — and find clean confirmation precisely because they measure $r$ directly rather than proxying it. [[@Aggarwal2002|Aggarwal & Samwick (2002)]] in turn show the executive debate hinges on an *unidentified* parameter, the size-elasticity $\eta$ in $\sigma_r V^{1-\eta}$: Core & Guay implicitly impose $\eta=1$ (percent variance), Aggarwal–Samwick $\eta=0$ (dollar variance), and Baker–Hall's preferred $\eta=0.4$ lands in the negative region. The "tradeoff" is sign-indeterminate until someone pins down $\eta$.

A third, methodological tension is **endogenous selection and matching.** [[@Ackerberg2002|Ackerberg & Botticini (2002)]] show that when risk-averse agents *match* to particular principals/tasks, OLS coefficients on observed traits are biased in unsigned directions — exactly the confound [[@Hilt2008|Hilt (2008)]] signs explicitly (less-risk-averse sailors sorting into Atlantic voyages *masks* the tradeoff; risk-averse principals exiting *overstates* it). [[@Lazear2000|Lazear (2000)]] and [[@Bloom2015|Bloom et al. (2015)]] show the same sorting force inflating measured "incentive" effects by roughly 2:1. If selection is this large and bidirectional, the reduced-form risk–incentive correlation is nearly uninterpretable — which undercuts *both* the confirming ([[@Aggarwal1999|Aggarwal & Samwick]]) and the reversing ([[@Prendergast2002a|Prendergast]]) camps.

Finally, [[@Prendergast2002|Prendergast (2002)]] and [[@Prendergast2002a|Prendergast (2002a)]] both shut down risk aversion (risk-neutral agents) to isolate their new channels — so by construction they cannot say how favoritism/delegation effects *net against* the classical negative channel when agents are genuinely risk-averse. [[@Grund2010|Grund & Sliwka (2010)]] and [[@Hilt2008|Hilt (2008)]] supply the missing risk-averse agents but in models without the responsibility channel. No member jointly models $\sigma^2$, $r$, and delegation.

## Open questions

- **Joint identification of the three primitives.** Multiple members ([[@Grund2010|Grund & Sliwka]], [[@Hilt2008|Hilt]], [[@Prendergast2002|Prendergast]]) flag that no design separately recovers signal noise $\sigma^2$, agent risk aversion $r$, and the marginal product/responsibility margin in the same data — the central open empirical task.
- **Pinning down $\eta$.** [[@Aggarwal2002|Aggarwal & Samwick (2002)]] leave the size-elasticity unidentified, sweeping rather than estimating it; the executive debate cannot resolve without it.
- **When does the reversal itself reverse?** [[@Prendergast2002a|Prendergast (2002a)]]'s positive relation re-flips to negative if measurement distortion scales with uncertainty ($\sigma_m^2=\tilde\sigma_m^2+k\sigma^2$), but $k$ is unmeasured.
- **Responsibility/delegation is unobserved.** [[@Prendergast2002a|Prendergast]] notes discretion is the elusive omitted variable; controlling for it should kill the positive relation, but data rarely record it.
- **Structural separation of selection.** [[@Lazear2000|Lazear]], [[@Bloom2015|Bloom et al.]], and [[@Lazear2007|Lazear & Oyer]] all leave the equilibrium question — *why some firms optimally keep fixed pay/low-powered incentives given who sorts in* — open.

## Candidate ideas

- **Structurally estimate the full $(\sigma^2, r, \text{responsibility})$ system** in matched employer–employee data, resolving the [[@Prendergast2002a|Prendergast (2002a)]] vs. [[@Aggarwal1999|Aggarwal & Samwick (1999)]] sign dispute by jointly identifying the channels neither isolates.
- **Re-run the executive test as a Bayesian estimation of $\eta$** rather than a grid sweep, settling the [[@Aggarwal2002|Aggarwal & Samwick (2002)]]–Core/Guay debate with an external prior on the size-elasticity.
- **A lab/online experiment manipulating signal noise and delegation orthogonally**, holding measured risk aversion fixed, to test whether the [[@Prendergast2002a|Prendergast]] delegation channel actually generates positive risk–incentive comovement among risk-averse agents.
- **Measure how multitasking distortion $k$ scales with uncertainty** across franchising vs. poorly-measured sectors, testing [[@Prendergast2002a|Prendergast (2002a)]]'s prediction that positive correlations appear only where output measures are reliable.
- **Use a matching-correction design à la [[@Ackerberg2002|Ackerberg & Botticini (2002)]] on a modern risk shock** (e.g., demand-volatility shocks à la [[@Hilt2008|Hilt (2008)]]) to sign the selection bias and recover the structural tradeoff in contemporary contracts.
- **Embed the [[@Lazear2000|Lazear (2000)]]/[[@Bloom2015|Bloom et al. (2015)]] sorting decomposition into the risk-incentive regression directly**, estimating how much of the measured risk–PPS relation is contract design vs. who selects into noisy jobs.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Prendergast1996]] — cited by 3 members
- [[@Lazear1981]] — cited by 2 members
- [[@Aghion1997]] — cited by 1 member
- [[@Akerlof1970]] — cited by 1 member
- [[@Gibbons1992]] — cited by 1 member
- [[@Gneezy2000]] — cited by 1 member
- [[@Holmstrom1982]] — cited by 1 member
- [[@Holmstrom1999]] — cited by 1 member
- [[@Nalebuff1983]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
