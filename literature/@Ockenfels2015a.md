---
citekey: Ockenfels2015a
title: Bonus Payments and Reference Point Violations
authors: ["Ockenfels, Axel", "Sliwka, Dirk", "Werner, Peter"]
year: 2015
type: journalArticle
doi: 10.1287/mnsc.2014.1949
zotero: "zotero://select/library/items/YZX4PHH2"
pdf: /Users/jesper/Zotero/storage/EHWB7JZT/Ockenfels2015a.pdf
tags: [literature]
keywords: [reference-dependent-preferences, bonus-pay, pay-transparency, loss-aversion, social-comparison, subjective-performance-evaluation, negative-reciprocity]
topics: []
related: [Bolton2000, Fehr1999, Prendergast1996, Prendergast2002]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We investigate how bonus payments affect the satisfaction and performance of managers in a large multinational company. We find that falling behind a natural reference standard for a fair bonus payment (a "reference point violation") reduces satisfaction and subsequent performance. The effects are mitigated if information about one's relative standing toward the reference point is withheld. A model and a laboratory experiment provide complementary insights and additional robustness checks.

## Summary
Combining personnel-record compensation data with survey responses from managers of a large multinational, the authors show that *reference point violations*—receiving a bonus below the salient 100%-of-budget standard—lower both job satisfaction and subsequent performance, in an asymmetric (loss-averse) way: falling short hurts much more than overshooting helps. Crucially, these effects appear only where relative standing is *transparent* (Germany), not where bonus percentages are hidden (the U.S.). A reference-dependent social-utility model explains the asymmetry, the disappearance of the kink under noisy information, and the resulting clustering ("compression") of bonuses at the reference point; a $2\times2$ lab experiment confirms transparency as the driving mechanism.

## Research question
How do bonus payments—and specifically the *transparency* of one's relative standing toward a natural reference standard for a fair bonus—affect employees' job satisfaction, their subsequent performance, and supervisors' bonus-allocation patterns?

## Method / identification
Three complementary pieces.

**(1) Field data / regressions.** The firm's bonus system assigns each manager a bonus target ("budget"); the supervisor sets the actual payment as a *bonus percentage* $z_i$ of that target, with a fixed total budget per department (so raising one manager above 100% forces another below). The 100% bonus percentage is thus a natural reference point. Satisfaction is modeled with an asymmetric (kinked) specification allowing different slopes below and above 100%:
$$\text{JobSatisfaction}_i = \alpha + \beta \cdot X_i + \gamma\cdot(z_i-100)\cdot I\{z_i>100\%\} + \delta\cdot(100-z_i)\cdot I\{z_i<100\%\} + \varepsilon_i,$$
where $\gamma$ captures positive and $\delta$ negative deviations from 100%. The reference-point hypothesis predicts $\delta$ significantly negative and $\gamma$ positive but small. Germany (transparent percentages) vs. the U.S. (nontransparent) provides a *falsification / difference* design: ratings are visible in both, so controlling for performance rating isolates the role of percentage transparency.

For **performance**, the unit of analysis is the supervisor. $\text{DevRef}_{st}$ is the share of "fully meets expectations" managers pushed below 100% by supervisor $s$ in year $t$. With supervisor fixed effects:
$$\text{Rating}_{s,t+1} = \alpha + \beta\cdot\text{DevRef}_{st} + \gamma\cdot X_{st} + \delta\cdot Y_{s,t+1} + a_s + \varepsilon_{st},$$
identifying within-supervisor variation in violation frequency on the supervisor's own next-year rating (clustered SEs).

**(2) Theory (Online Appendix C).** A reference-dependent social-utility function with a kink at the reference standard—a Fehr–Schmidt / Bolton–Ockenfels type when the standard is the average colleague bonus, or loss aversion relative to a 100% entitlement when it is an aspiration level. Managers hold a *prior* over the (positively correlated) bonus distribution and update on their own bonus. As prior precision falls, the kink in *expected* social utility flattens and vanishes in the limit—agents who care about the reference point behave as if they do not when their relative standing is vague. Endogenizing a budget-constrained supervisor who values both rating accuracy and managers' well-being (à la Prendergast–Topel) yields *bonus clustering at the reference point* under transparency (positive mass exactly at the average bonus) but a continuous distribution under nontransparency.

**(3) Lab experiment.** A $2\times2$ design crossing bonus inequality (EQUAL vs. UNEQUAL: 120%/80% split) with TRANSPARENCY vs. NONTRANSPARENCY. Two workers co-write an essay via GoogleDocs/chat; a third subject (supervisor) ranks them; followed by a public-good game and a dictator game to disentangle outcome-based fairness from intention-based reciprocity. 120 subjects, 10 independent observations per cell, Cologne lab, ORSEE recruitment, z-Tree.

## Data
Personnel records (salaries, bonus targets, bonus percentages, five-point performance ratings, hierarchy) of managers in a >100,000-employee multinational, headquartered in Germany with a large U.S. subsidiary, *matched* to survey responses (job/bonus satisfaction on a 1–7 scale, free-text comments). 468 supervisor-year observations (Germany) and 504 (U.S.) for the performance regressions. Plus original lab data (120 subjects).

## Key findings
- **Asymmetric satisfaction (Observation/Model D3):** In transparent Germany, $\delta<0$ is significant while $\gamma$ is ~0—falling below 100% sharply lowers satisfaction; exceeding it does not raise it. A 10-point cut below budget lowers the probability of reporting high satisfaction by ~4–6 percentage points. In the U.S., the raw asymmetry appears via ratings but *vanishes once performance ratings are controlled* (Models US4/US5), pinning the effect on percentage transparency, not culture.
- **Performance (Table 2):** In Germany, a higher share of below-100% violations lowers the supervisor's *next-year* rating (D1/D2, coef. ≈ $-0.57$ to $-0.68$, sig. 1%); economically, giving all "fully meets" managers 100% would raise the supervisor's own evaluation by ~0.68 SD. No significant effect in the nontransparent U.S. (falsification).
- **Negative reciprocity (Table 3):** The performance penalty is concentrated among supervisors *perceived as evaluating inappropriately* and vanishes for the most accurate ones, consistent with negative reciprocity rather than pure outcome-based inequity.
- **Bonus compression:** Harmful violations lead supervisors to compress the bonus distribution toward the 100% reference point—matching the model's clustering prediction under transparency.
- **Lab:** No satisfaction differences across bonus levels under NONTRANSPARENCY; under TRANSPARENCY, 80% workers report satisfaction 2.4 points lower than 100% while 120% workers are only 0.9 higher—replicating the field asymmetry. Public-good contributions and dictator transfers do not cleanly track bonus level (the negative response is not well explained by simple outcome-based fairness).

## Contribution
Provides large-scale field evidence that a *naturally occurring* reference point degrades the effectiveness of performance-pay incentives, and isolates *transparency of relative standing* as a first-order, manipulable design lever. Unlike prior work on fixed wages or total compensation, it studies performance-related pay under a fixed total budget, links field + theory + lab, and shows the firm subsequently redesigned its bonus rules (fixing bonus percentages per grade) in response.

## Limitations & open questions
- The authors *could not cleanly disentangle* the two candidate reference standards—social comparison (average colleague bonus) vs. aspiration level (entitlement to 100%); they find no clear aspiration effect and flag separating them as future work.
- They are *not confident transparency is generally undesirable*: nontransparency may harm procedural-fairness perceptions, reduce trust, raise fear of exploitation, and in their own data is associated with *more* (hidden) violations—so the welfare trade-off is open.
- Possible residual Germany–U.S. cultural confounds cannot be fully excluded, though several checks argue against them.
- Causality of the satisfaction→performance link is argued via asymmetry and the U.S. falsification rather than randomized assignment of bonuses in the field.
- Out-of-equilibrium supervisor behavior (some supervisors not realizing the harm) suggests the studied institution was not in equilibrium—raising open questions about optimal bonus-system design.

## Connections
Builds on reference-dependent and social-preference models—[[@Fehr1999|Fehr and Schmidt (1999)]], [[@Bolton2000|Bolton2000]]]] (Bolton–Ockenfels ERC), and loss aversion in the Köszegi–Rabin tradition—and on subjective-evaluation theory ([[@Prendergast1996|Prendergast and Topel 1996]]; [[@Prendergast2002|Prendergast 2002)]]. It operationalizes Akerlof–Yellen's fair wage–effort hypothesis and Bewley's pay-inequity findings with field data. Closely related field studies: Mas (2006) on arbitration reference points, Card et al. (2012) on wage-transparency and satisfaction, Cohn et al. (2014) on asymmetric wage cuts, and Barankay (2012) on relative-ranking feedback. The transparency mechanism connects to social-psychology work on the accessibility of comparison standards (Mussweiler and Damisch 2008).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
