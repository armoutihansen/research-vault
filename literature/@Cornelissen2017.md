---
citekey: Cornelissen2017
title: Peer Effects in the Workplace
authors: ["Cornelissen, Thomas", "Dustmann, Christian", "Schönberg, Uta"]
year: 2017
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/Q8QP82Y3"
pdf: /Users/jesper/Zotero/storage/8QX54IIT/Cornelissen2017.pdf
tags: [literature]
keywords: [peer-effects, workplace, wages, knowledge-spillover, social-pressure, two-way-fixed-effects, labor-economics]
topics: []
related: [Falk2006a, Mas2009]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Existing evidence on peer effects in the productivity of coworkers stems from either laboratory experiments or real-world studies referring to a specific firm or occupation. In this paper, we aim at providing more generalizable results by investigating a large local labor market, with a focus on peer effects in wages rather than productivity. Our estimation strategy—which links the average permanent productivity of workers' peers to their wages—circumvents the reflection problem and accounts for endogenous sorting of workers into peer groups and firms. On average over all occupations, and in the type of high-skilled occupations investigated in studies on knowledge spillover, we find only small peer effects in wages. In the type of low-skilled occupations analyzed in extant studies on social pressure, in contrast, we find larger peer effects, about one-half the size of those identified in similar studies on productivity.

## Summary
Using two decades of German social-security records covering every worker and firm in the Munich local labor market, the paper estimates how the long-term ("permanent") productivity of a worker's coworkers affects that worker's own wage. By linking wages to peers' predetermined worker fixed effects rather than to peers' contemporaneous wages or effort, it sidesteps Manski's reflection problem, and by stacking worker, firm-by-occupation, firm-by-year, and occupation-by-year fixed effects it absorbs endogenous sorting. Average peer effects in wages are small but precisely estimated; they are concentrated in low-skilled, repetitive occupations where output is mutually observable (consistent with peer pressure), and are essentially absent in high-skilled, knowledge-intensive occupations (against knowledge spillover as the main channel).

## Research question
Do coworker peer effects documented in narrow lab and single-firm field studies generalize to a representative labor market, and do peer-induced productivity gains translate into wages? Which mechanism, social pressure or knowledge spillover, drives the effect?

## Method / identification
A principal-agent model first motivates why peer effects in productivity show up in wages even when the firm extracts the full match surplus. Output of worker $i$ is $y_i = a_i + e_i(1 + \lambda_K \bar a_{-i}) + \varepsilon_i$, so own effort $e_i$ and average peer ability $\bar a_{-i}$ are complements (knowledge spillover, parameter $\lambda_K$). Effort cost is quadratic, $C(e_i)=k e_i^2$, augmented by a peer-pressure term $P(e_i,\bar y_{-i})=\lambda_p(m-e_i)\bar y_{-i}$ so the marginal cost of effort falls as peer output rises. Firms offer linear, risk-neutral wage contracts and push workers to their reservation utility, so $E w_i = v(a_i) + C(e_i^*) + P(e_i^*,\bar y_{-i})$. Differentiating and averaging yields an unambiguously positive average effect of peer ability on wages, combining a direct effort response with a social-multiplier feedback.

Empirically the baseline log-wage equation is
$$\ln w_{iojt} = \alpha_i + \gamma\, \bar a_{-i,ojt} + x_{iojt}\beta + \omega_{ot} + \delta_{jt} + \theta_{oj} + \nu_{iojt},$$
where $\bar a_{-i,ojt}$ is the leave-one-out average coworker fixed effect (peers = same three-digit occupation $\times$ firm $\times$ year). The coefficient $\gamma$ is the parameter of interest. Worker fixed effects $\alpha_i$ absorb sorting of able workers into able peer groups; firm-by-occupation effects $\theta_{oj}$ absorb firms over-paying particular occupations; time-varying firm effects $\delta_{jt}$ absorb firm-occupation-common shocks. Because $\bar a_{-i,ojt}$ multiplies $\gamma$ and both the worker effects and the peer average are unknown, the model is nonlinear least squares with high-dimensional fixed effects, estimated via the Arcidiacono et al. (2012) algorithm (consistent for $\gamma$ even when individual $\alpha_i$ are not, given uncorrelated errors). Conceptually the leave-one-out design reduces to a difference-in-differences across two occupations in the same firm experiencing different peer-quality changes. A within-peer-group estimator conditioning on full $p_{ojt}$ effects (identified only because peer groups vary in size) serves as a robustness check against time-varying peer-group shocks.

## Data
German social-security records, 1989-2005, for the Munich metropolitan labor market: 2,115,544 workers, 89,581 firms, 1,387,216 peer groups, 12,832,842 worker-year observations; workers observed ~6.1 years. The largest connected mobility group (99.5%) is retained so worker and firm fixed effects are jointly identified. Occupations at three-digit level (331 codes). Repetitive/observable occupations (top 5%) and skilled/knowledge occupations (top 10%) are flagged using the 1991/1992 Qualification and Career Survey. Top-coded wages are imputed.

## Key findings
- Sequentially adding fixed effects collapses the estimate: $\gamma=0.148$ (firm FE), $0.066$ (firm-occupation FE), down to $\gamma=0.011$ with time-varying firm effects, i.e. a 10% rise in peer quality raises wages by only ~0.1%, or 0.3 pp (0.6% of an SD) for a one-SD rise. This is 10-15x smaller than productivity peer effects in [[@Mas2009|Mas & Moretti (2009)]] and [[@Falk2006a|Falk & Ichino (2006)]].
- In the 5% most repetitive occupations $\gamma\approx0.064$: a one-SD rise in peer quality lifts wages by ~0.84%, about half the productivity effect in the canonical studies. The exact occupations from prior studies (cashiers, agricultural helpers, data-entry workers) give a near-identical $0.067$.
- High-skilled / knowledge-intensive occupations show small effects ($\gamma\approx0.013$, innovative $0.007$), so knowledge spillover is not the driver.
- The within-peer-group estimator corroborates the pattern ($0.061$ repetitive, $0.016$ skilled). The contrast pins peer pressure (output observability) as the operative mechanism. Conclusion: peer effects exist in specific low-skilled settings but do not meaningfully shape economy-wide wage setting or inequality.

## Contribution
First study of workplace peer effects in a general, representative labor market rather than a single firm/occupation, and the first to study peer effects in wages rather than productivity. It establishes external validity limits of the existing literature, shows productivity spillovers translate into wage spillovers in observable-output occupations, and uses cross-occupation heterogeneity to discriminate between social pressure and knowledge spillover. Methodologically it extends the Abowd-Kramarz-Margolis two-way fixed-effects framework with leave-one-out peer ability and the Arcidiacono et al. estimator.

## Limitations & open questions
- The authors argue any residual bias is upward, so estimates are upper bounds; Monte Carlo evidence (online appendix) shows time-varying peer-group shocks can bias short-$T$ panels upward, motivating the within-group check.
- Identification rests on the common-time-trend / uncorrelated-error assumption; serially correlated or peer-group-common wage shocks threaten consistency.
- The analysis is contemporaneous knowledge spillover only; lagged/dynamic learning from past peers is abstracted away.
- Effects are local (one metropolitan market) for computational tractability; nationwide generalization is argued but not directly estimated in the main text.
- Boss/supervisor quality cannot be separately identified, since peers are defined within occupation; disentangling leader effects is left open.
- Why productivity spillovers are only partially passed through to wages (effects ~half the productivity magnitude) is noted but not structurally decomposed.

## Connections
The reduced-form identification builds on Abowd, Kramarz & Margolis (1999) and the two-way fixed-effects wage-decomposition literature of Card, Heining & Kline (2013) and Card, Cardoso & Kline (2016), with estimation via Arcidiacono, Foster, Goodpaster & Kinsler (2012). It directly engages the workplace peer-effects canon: [[@Mas2009|Mas & Moretti (2009)]] on supermarket cashiers, [[@Falk2006a|Falk & Ichino (2006)]] on envelope-stuffing, Bandiera, Barankay & Rasul (2010) on fruit pickers, Kaur, Kremer & Mullainathan on data entry, and Chan, Li & Pierce (2014) on salespeople, alongside the Herbst & Mas (2015) meta-analysis. On knowledge spillover it contrasts Waldinger (2012), Azoulay, Graff Zivin & Wang (2010), and Jackson & Bruegmann (2009). The theory draws on the peer-pressure and team-incentive models of Kandel & Lazear (1992) and Barron & Gjerde (1997). Identification is contrasted with the education peer-effects literature (Sacerdote 2011; Hoxby 2000; Lavy & Schlosser 2011) and addresses Manski's (1993) reflection problem. Related boss-quality evidence is in Lazear, Shaw & Stanton (2015).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
