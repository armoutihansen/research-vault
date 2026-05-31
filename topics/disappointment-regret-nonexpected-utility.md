---
slug: disappointment-regret-nonexpected-utility
title: "Disappointment, Regret & Non-Expected Utility"
type: topic
scope: "Transitive and non-transitive generalizations of EU (disappointment, regret, rank-dependent/anticipated utility) resolving Allais-type anomalies."
area: "[[decision-under-risk-time]]"
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This topic collects the families of non-expected-utility (non-EU) theory built to rationalize systematic risk anomalies — the Allais common-ratio and common-consequence effects, the certainty effect, simultaneous gambling-and-insurance — by adding a *single* psychological or structural ingredient to von Neumann–Morgenstern (vNM) expected utility. The members split along a fault line: *transitive* models that distort how outcomes or probabilities are weighted (disappointment, rank-dependent/anticipated utility, mixture aversion) versus *non-transitive* regret models built on pairwise comparison across foregone acts. The boundary is methodological: these papers depart from EU *minimally* and remain choice-theoretic. Cumulative prospect theory's full reference-dependent value function (gain-loss kink, separate loss aversion) lives in the prospect-theory topic; expectation-as-reference-point machinery lives in the Kőszegi–Rabin topic.

## Sub-themes

- **Disappointment as a reference comparison within an act.** [[@Bell1985|Bell (1985)]] introduces the elation/disappointment premium against one's prior expectation, holding marginal value of money constant; [[@Loomes1986|Loomes & Sugden (1986)]] generalize it to a transitive, dynamically consistent model with a nonlinear disappointment-elation function $D(\cdot)$; [[@Gul1991|Gul (1991)]] axiomatizes the one-parameter $\beta$ disappointment-aversion representation nesting EU at $\beta=0$.
- **Rank-dependent / anticipated utility.** [[@Quiggin1982|Quiggin (1982)]] founds rank-dependent EU by transforming the *cumulative* distribution via $f$, preserving first-order stochastic dominance where individual-probability weighting fails.
- **Regret as a comparison across foregone acts.** [[@Sugden1993|Sugden (1993)]] gives regret theory a Savage-style axiomatic foundation, dropping transitivity entirely via a triadic, menu-dependent preference; [[@Sarver2008|Sarver (2008)]] recasts anticipated regret as a preference-over-menus representation explaining why fewer options can be better.
- **Recursive / dynamic non-EU.** [[@Sarver2018|Sarver (2018)]] embeds mixture-averse "optimal risk attitude" preferences in Epstein–Zin; [[@DeJarnette2020|DeJarnette et al. (2020)]] extend non-EU to lotteries over payment *dates* (time lotteries).
- **Discriminating among the models.** [[@Loomes1987|Loomes & Sugden (1987)]] design an experiment to separate regret from disappointment; [[@Harless1994|Harless & Camerer (1994)]] run a fit-vs-parsimony horse race across 23 datasets.

## Cross-paper tensions

The defining clash is **transitivity vs. non-transitivity as the locus of EU's failure.** [[@Loomes1986|Loomes & Sugden (1986)]] and [[@Gul1991|Gul (1991)]] keep a real-valued index, so $\succeq$ is necessarily complete and transitive; the anomaly is forced entirely into nonlinear weighting. [[@Sugden1993|Sugden (1993)]] argues the opposite — that regret *requires* intransitivity and menu-dependence (violations of Sen's Property $\alpha$) — and treats consistency axioms as non-constitutive of rationality. These are not nested: a single dataset cannot be simultaneously the transitive disappointment world and the intransitive regret world.

A sharper, *empirical* version of this tension is [[@Loomes1987|Loomes & Sugden (1987)]]'s identification design. Regret depends on the state-overlap $\omega$ between two acts; disappointment depends only on the win-probability $p$; under independence $\omega=p$, so ordinary common-ratio experiments *confound them*. Decoupling $\omega$ from $p$, they find a strong $p$-driven disappointment effect but a weak, sometimes *reversed* regret effect — directly undercutting Sugden's regret program with the authors' own data, and leaving the perverse Type-3 reversal unexplained.

A second axis is **how minimal the departure can be while still fitting.** Gul's $\beta$ is the most parsimonious story, but [[@Harless1994|Harless & Camerer (1994)]] reject Gul's linear-disappointment-aversion ("linear mixed fan") form *using the very data that inspired it*, and find it dominated on fit-vs-parsimony by mixed fanning and prospect theory. Their verdict — EU fails badly only when paired gambles have *different support* (triangle boundary), i.e. probability-weighting near $p\in\{0,1\}$ is the real action — favors Quiggin's rank-dependent mechanism over a within-act disappointment term, and contradicts [[@Loomes1987|Loomes & Sugden (1987)]]'s finding of a *weak* effect as $p$ first leaves certainty.

A third axis is **what each model cannot do.** [[@Gul1991|Gul (1991)]] concedes his $\beta>0$ model is inconsistent with the common-ratio effect *over losses*, and fans out in only the top or bottom half of the triangle, not both. [[@Quiggin1982|Quiggin (1982)]] buys dominance-preservation at the cost of weaker predictions (no full SSD analogue). [[@DeJarnette2020|DeJarnette et al. (2020)]] sharpen this into an impossibility: across the entire rank-dependent/CPT/disappointment-aversion umbrella (their GLBU class), probability distortion *cannot* accommodate even one risk-averse-over-time-lottery choice without violating Stochastic Impatience — so the whole transitive non-EU toolkit fails on the timing margin, forcing a choice between relaxing intertemporal independence or abandoning impatience.

A fourth tension is **observability of the psychological primitive.** Classical regret/disappointment is identified only through its *distortion of choice from a menu*; [[@Sarver2008|Sarver (2008)]] identifies regret from menu choice *even when it leaves choice from the menu undistorted* — but then shows regret and Gul–Pesendorfer temptation are observationally equivalent on menu data, so the very tractability comes at the price of non-separability.

## Open questions

- Are regret and disappointment **complementary or substitutes**? [[@Loomes1987|Loomes & Sugden (1987)]] leave this open and cannot explain the reversed Type-3 regret result; a unified transitive-plus-intransitive theory is flagged as wanted by [[@Loomes1986|Loomes & Sugden (1986)]].
- How are **prior expectations / reference points formed**? [[@Bell1985|Bell (1985)]] deliberately leaves expectation formation implicit (mean? mode? optimist vs. pessimist), and his odds-based variant implies implausibly infinite disappointment as $p\to 0$.
- Can disappointment aversion be reconciled **across gains and losses simultaneously**, and across *both* halves of the probability triangle ([[@Gul1991|Gul (1991)]])? Relaxing his Symmetry axiom (two indices $u_e,u_d$) is only sketched.
- **Which axiom should give way** on the timing margin — intertemporal independence or Stochastic Impatience — and does any dynamically consistent model survive ([[@DeJarnette2020|DeJarnette et al. (2020)]])?
- Can the strength of regret/risk-attitude be **structurally estimated**? [[@Sarver2008|Sarver (2008)]] cannot separate $K$ from uncertainty; [[@Sarver2018|Sarver (2018)]] identifies only maximal feasible sets $\Phi$, not the true $\Phi$.
- Does the [[@Harless1994|Harless & Camerer (1994)]] "menu" verdict survive **richer error models**, losses, many-outcome gambles, and dependence across studies — all explicitly untested?

## Candidate ideas

- **Re-run the $\omega$-vs-$p$ separation at scale with modern incentives.** Replicate [[@Loomes1987|Loomes & Sugden (1987)]]'s design (n=120, suggestive only) with a pre-registered large sample to settle whether the disappointment effect dominates regret, and whether the Type-3 reversal is real.
- **A horse race in the spirit of [[@Harless1994|Harless & Camerer (1994)]] but with structural ML.** Use the completeness/restrictiveness machinery (the ML-theory-evaluation topic) to benchmark Gul, Quiggin, and mixed fanning against a predictive ceiling on existing triangle data — does $\beta$-disappointment leave systematic, recoverable residuals?
- **Test the GLBU impossibility behaviorally.** Build on [[@DeJarnette2020|DeJarnette et al. (2020)]]: elicit time-lottery and atemporal risk choices jointly to discriminate the GEDU (post-discounting curvature $\varphi$) route from the within-period-independence (DOCE) route at the individual level.
- **Identify regret separately from temptation.** Exploit [[@Sarver2008|Sarver (2008)]]'s dynamic extension (menus-of-menus + period-1 choice) experimentally to break the regret/temptation observational equivalence that menu data alone cannot.
- **Estimate mixture-averse ORA preferences on insurance/portfolio microdata.** Operationalize [[@Sarver2018|Sarver (2018)]]'s untested structural form — does willingness-to-pay rising in existing coverage show up in deductible choices, resolving Rabin without first-order risk aversion?
- **Endogenize the reference expectation in disappointment models.** Combine [[@Bell1985|Bell (1985)]]/[[@Gul1991|Gul (1991)]] with an explicit belief-formation rule (linking to the expectations-based reference-dependence program) and test whether the implied $p\to 0$ behavior matches catastrophe/lottery-ticket demand.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Kahneman1979]] — cited by 7 members
- [[@Tversky1992]] — cited by 3 members
- [[@Chen2013]] — cited by 1 member
- [[@Sydnor2010]] — cited by 1 member
- [[@Tversky1981]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
