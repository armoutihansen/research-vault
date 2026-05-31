---
slug: contracts-incentives-personnel
title: "Contracts, Incentives & Personnel Economics"
type: area
scope: "Moral hazard, incentive design, and the organization of work and firm objectives."
tags: [area]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This area studies how organizations motivate and structure work when effort is hidden and output is a noisy, manipulable signal of it — the moral-hazard core of personnel economics and the theory of the firm's objective function. Its child topics fan out along two axes: the *instrument* used to provide incentives (a piece rate's slope, a rank-order prize, an implicit reputational stake, a distorted managerial mandate) and the *primitive* assumed about the agent (risk-averse and selfish, other-regarding, or merely a follower responding to leadership). Together they trace one question — how high-powered should incentives be, and on what should they be conditioned — from the Holmström–Milgrom benchmark out to its empirical, behavioral, and organizational frontiers.

## Sub-areas / themes

The classical agency core sets the benchmark and tests it. [[risk-incentive-tradeoff|The Risk-Incentive Tradeoff (Theory & Evidence)]] anchors the field on the canonical prediction $\alpha_1^\*=1/(1+rk\sigma^2)$ and its tenuous empirical record — the "is the slope falling in noise?" question every other topic inherits. [[tournaments-relative-performance|Tournaments & Relative Performance Pay]] swaps the absolute piece rate for ordinal rank and relative-performance evaluation, asking when conditioning on peers filters common shocks versus when it merely invites sabotage and doping. [[career-concerns-subjective-evaluation|Career Concerns & Subjective Evaluation]] endogenizes the signal itself — reputational incentives and the agency of a biased or colluding evaluator — closing the loop on what "performance" even measures.

The frontier topics relax the benchmark's behavioral and organizational assumptions. [[social-preferences-contract-theory|Social Preferences in Contract Theory]] embeds inequity aversion, reciprocity, and spite into the wage schedule $w(\cdot)$, supplying the non-standard agent the core treats as selfish. [[strategic-delegation-firm-objectives|Strategic Delegation & Firm Objectives]] turns the lens on the principal: why an owner deliberately hands a manager a non-profit objective, for oligopoly commitment or internal empowerment. [[transformational-leadership|Transformational Leadership]] is the area's empirical-organizational outlier, asking whether non-contractual leadership behaviors add explanatory power beyond contingent reward.

## Cross-topic tensions

The field-level fault line is **whether the optimal slope of pay rises or falls with the environment, and whether any of its signature comparative statics survive identification.** The core [[risk-incentive-tradeoff|risk-incentive]] prediction (steeper pay only in quiet environments) is contradicted from three directions: [[strategic-delegation-firm-objectives|delegation]] makes incentives and discretion *rise together* with uncertainty; [[social-preferences-contract-theory|social preferences]] make a horizontal comparison (agent-vs-agent) a *free* incentive lever even as the same vertical comparison (agent-vs-principal) is pure cost; and [[career-concerns-subjective-evaluation|subjective evaluation]] shows a steeper explicit slope *manufactures* the very bias variance it fights, so steepening is self-defeating. No topic agrees on the sign of $\partial(\text{power})/\partial\sigma^2$.

A second, methodological tension cuts across all of them: **endogenous selection and method artifact swamp the structural object.** [[risk-incentive-tradeoff|Sorting]] inflates measured incentive effects ~2:1; [[transformational-leadership|common-method variance]] inflates leadership's $\Delta R^2$ until it collapses for hard outcomes; [[tournaments-relative-performance|Holmström's]] sufficient-statistic logic says ordinal rank is informationally wasteful, yet rank persists. The recurring worry is that the reduced-form correlations on which the field rests are nearly uninterpretable until the confounds are signed.

Third, **is a deviation from the selfish-profit benchmark a friction or an instrument?** [[social-preferences-contract-theory|Other-regard]], [[strategic-delegation-firm-objectives|distorted firm objectives]], and [[tournaments-relative-performance|inequity in contests]] all show the same departure can raise *or* destroy welfare depending on configuration (horizontal vs. vertical comparison; Cournot vs. Bertrand; fixed vs. optimized prizes) — the field has no unified welfare statement.

## Open questions

- **Joint identification of the primitives.** No design across [[risk-incentive-tradeoff|risk]], [[career-concerns-subjective-evaluation|career concerns]], and [[social-preferences-contract-theory|social-preference]] models separately recovers signal noise $\sigma^2$, risk aversion $r$, the responsibility/delegation margin, and the fairness intensities $(\alpha,\beta,\eta)$ in the same data.
- **Endogenous reference groups and signals.** Whom an agent compares to ([[social-preferences-contract-theory|social preferences]]) and how informative the evaluator's report is ([[career-concerns-subjective-evaluation|subjective evaluation]]) are treated as exogenous; no model lets the firm's information policy set them.
- **Unifying the instruments.** Can one firm facing both product-market rivals and a subordinate ([[strategic-delegation-firm-objectives|delegation]]) choose objectives compatible with the slope, rank, and reputational devices the other topics study?
- **Behavioral residual vs. structure.** How much observed effort — in tournaments, under leadership, under fairness — escapes the standard model, and is it construct or method?

## Topics
```dataview
TABLE scope AS Scope
FROM "topics"
WHERE area = this.file.link
SORT file.name ASC
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
