---
citekey: DellaVigna2018
title: What Motivates Effort? Evidence and Expert Forecasts
authors: ["DellaVigna, Stefano", "Pope, Devin"]
year: 2018
type: journalArticle
doi: 10.1093/restud/rdx033
zotero: "zotero://select/library/items/SYPYF56T"
pdf: /Users/jesper/Zotero/storage/RMCWKW6R/DellaVigna2018.pdf
tags: [literature]
keywords: [real-effort-experiment, behavioral-motivators, expert-forecasts, structural-estimation, social-preferences, reference-dependence]
topics: ["[[reciprocity-gift-exchange]]"]
related: [DellaVigna2012, Erev2010, Fehr1993, Gneezy2000, Kahneman1979, Koszegi2006b, Kube2013]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> How much do different monetary and non-monetary motivators induce costly effort? Does the effectiveness line up with the expectations of researchers? We present the results of a large-scale real-effort experiment with 18 treatment arms. We compare the effect of three motivators: (i) standard incentives; (ii) behavioral factors like present-bias, reference dependence, and social preferences; and (iii) non-monetary inducements from psychology. In addition, we elicit forecasts by behavioral experts regarding the effectiveness of the treatments, allowing us to compare results to expectations. We find that (i) monetary incentives work largely as expected, including a very low piece rate treatment which does not crowd out incentives; (ii) the evidence is partly consistent with standard behavioral models, including warm glow, though we do not find evidence of probability weighting; (iii) the psychological motivators are effective, but less so than incentives. We then compare the results to forecasts by 208 experts. On average, the experts anticipate several key features, like the effectiveness of psychological motivators. A sizeable share of experts, however, expects crowd-out, probability weighting, and pure altruism, counterfactually. This heterogeneity does not reflect field of training, as behavioral economists, standard economists, and psychologists make similar forecasts. Using a simple model, we back out key parameters for social preferences, time preferences, and reference dependence, comparing expert beliefs and experimental results.

## Summary
A pre-registered, 18-arm, between-subject real-effort experiment (button-pressing on MTurk, ~9,800 subjects) that puts monetary incentives, behavioral motivators (social preferences, time preferences, reference dependence), and psychological inducements side-by-side in one common environment, tied to a single structural cost-of-effort model. The paper then layers on a forecasting design: 208 academic experts predict each treatment's effect before results are known. The headline contribution is methodological — head-to-head comparison of motivators plus structural estimation of behavioral parameters plus a measurement of where the research community's priors are right and wrong.

## Research question
How effective are different monetary and non-monetary motivators at inducing costly effort, when measured head-to-head in one setting and mapped onto the parameters of standard behavioral models? And do academic experts' beliefs (priors of the research community) line up with the experimental evidence?

## Method / identification
A real-effort task (alternately pressing "a" and "b" for ten minutes; one point per a-b alternation) is run across 18 between-subject arms differing only in one instruction paragraph plus an on-screen reminder. The arms are model-based. A worker maximizes piece-rate plus intrinsic return net of a convex effort cost:
$$\max_{e\ge 0}\ (s+p)\,e - c(e)$$
where $e$ is points, $p$ the piece rate, and $s$ an intrinsic-motivation term (so effort is non-zero even at $p=0$). The interior solution is $e^{*}=c'^{-1}(s+p)$. Two pre-specified cost functions are used: a power cost $c(e)=\frac{k}{1+\gamma}e^{1+\gamma}$ with constant effort elasticity $1/\gamma$, giving $e^{*}=\left(\frac{s+p}{k}\right)^{1/\gamma}$, and an exponential cost $c(e)=k\exp(\gamma e)/\gamma$ giving $e^{*}=\frac{1}{\gamma}\log\!\left(\frac{s+p}{k}\right)$. The three benchmark piece-rate arms (0, 1, 10 cents per 100 points) identify the three unknowns $(s,k,\gamma)$; every other arm is then a simple function of one added behavioral parameter:
- Crowd-out: very-low pay ($p=0.01$) with a motivation shift $\Delta s$, $e^{*}=c'^{-1}(s+\Delta s+p)$; crowd-out is $\Delta s<0$.
- Social preferences: charity arms $e^{*}=c'^{-1}(s+a\cdot p_{c}+0.01\,g)$, separating pure altruism $a$ (scales with charity return $p_c$) from warm glow $g$ (does not); a gift-exchange arm with reciprocity shift $\Delta s^{gift}$.
- Time preferences: delayed-pay (2/4 weeks) modeled as $e^{*}=c'^{-1}(s+\beta\delta^{k}p)$, identifying present-bias $\beta$ and weekly discount factor $\delta$.
- Reference dependence: a Hossain–List claw-back loss-framing arm (loss aversion $\lambda$) and probabilistic piece-rate arms testing probability weighting.

Estimation uses two procedures: (1) a minimum-distance estimator matching average effort per treatment (homogeneous workers — the same calculation an expert could in principle run from the three benchmarks), and (2) following DellaVigna et al. (2015), individual-level NLS on 100-point-binned data allowing heterogeneity in marginal cost. Experts (314 contacted, 208 complete; 66% rate) were shown the three benchmark results and forecast effort in the remaining 15 arms; the same model is inverted on their forecasts to recover expert-implied parameters. Both the RCT (AEARCTR-0000714) and the survey were pre-registered with a pre-analysis plan.

## Data
~9,800 retained Amazon Mechanical Turk workers (12,838 started; drops for a Qualtrics server glitch and pre-registered exclusions), >500 per arm, run over three weeks in May 2015. Expert forecast data from 208 academic respondents across behavioral economics, experimental economics, psychology, and non-behavioral economics.

## Key findings
1. **Incentives work and do not crowd out.** Effort is 33% above the no-pay benchmark at a 1-cent piece rate and a further 7% higher at 10 cents; the model fit on three benchmarks predicts the 4-cent arm and, notably, the very-low-pay (0.1-cent) arm, where effort is 24% above no-pay — no crowd-out, contrary to "pay enough or don't pay at all."
2. **Psychological inducements are moderately effective** (15–21% above no-pay), but weaker than any monetary arm; a Cialdini-type social comparison is the strongest among them.
3. **Behavioral models fit, with nuance.** Charity arms support warm glow, not pure altruism (effort identical whether the charity earns 1 or 10 cents). Gift exchange gives a small, weak reciprocity response. Delayed pay reduces effort but decays exponentially, not present-biased ($\beta\approx 1$, though noisy). Loss-framing raises effort consistent with loss aversion; probabilistic incentives induce *less* effort than the deterministic equivalent — evidence of *under*weighting, not overweighting, of small probabilities (given linear/moderately concave value).
4. **Experts are good on average but systematically off in places.** The mean forecast ranks the six non-private-incentive treatments in exact order. But experts wrongly expect ~12% crowd-out in very-low pay, expect pure altruism (median expert $a\approx 0.7$ with no warm glow), expect present bias (median $\beta\approx 0.76$), and overestimate probability-weighting effects. Forecast accuracy does not vary by field of training; disagreement is largest where the underlying literature is thinnest (crowd-out, probability weighting).

## Contribution
Provides the first within-setting, model-based head-to-head ranking of a broad menu of behavioral and monetary motivators, and pairs it with structural estimation that recovers comparable behavioral parameters (transportable across settings). Introduces systematic, pre-registered collection of expert forecasts as a research instrument — measuring the research community's priors and exactly where evidence diverges from them — feeding the literature on structural behavioral economics and on forecasting research results.

## Limitations & open questions
The authors stress that relative effectiveness is likely **context-dependent**: motivators weak here (e.g., probability weighting) may matter in other tasks or non-MTurk pools — replication is needed. The model assumes homogeneous, risk-neutral workers and continuously-earned piece rates (relaxed only partly in procedure 2). The menu of motivators is non-exhaustive: limited attention/salience, left-digit bias, and overconfidence were considered but excluded. The outcome is costly effort only; extensions to other outcomes (e.g., public-goods contributions) are flagged. Present-bias evidence is too imprecise to rule out $\beta<1$. A practical open question motivates the work: should a behavioral expert trust intuition or always run an RCT?

## Connections
The structural-estimation backbone follows DellaVigna, List, Malmendier & Rao (2015) and the broader structural behavioral economics literature (Laibson, Repetto & Tobacman 2007; Conlin, O'Donoghue & Vogelsang 2007; [[@DellaVigna2012|DellaVigna, Malmendier & List 2012]]; Barseghyan et al. 2013). Treatments operationalize canonical models: warm glow vs. pure altruism (Andreoni 1989, 1990; Becker 1972), motivational crowd-out (Deci 1971; [[@Gneezy2000|Gneezy & Rustichini 2000]]), present bias (Laibson 1997; O'Donoghue & Rabin 1999; with the monetary-vs-effort caveat from Andreoni & Sprenger 2012 and Augenblick, Niederle & Sprenger 2015), reference dependence and prospect theory ([[@Kahneman1979|Kahneman & Tversky 1979]]; Tversky & Kahneman 1991, 1992; [[@Koszegi2006b|Koszegi & Rabin 2006]]), claw-back loss framing (Hossain & List 2012), gift exchange (Gneezy & List 2009; [[@Fehr1993|Fehr, Kirchsteiger & Riedl 1993]]; with null follow-ups [[@Kube2013|Kube, Marechal & Puppe 2013]]), charity-and-effort (Imas 2014), task significance (Grant 2008), and Cialdini-style social comparison (Cialdini et al. 2007). The forecasting agenda relates to [[@Erev2010|Erev et al. (2010)]], Coffman & Niehaus (2014), prediction markets for replication (Dreber et al. 2015; Camerer et al. 2016), and optimal experimentation (Banerjee, Chassang & Snowberg 2016); a companion paper (DellaVigna & Pope 2016) studies forecaster accuracy.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
