---
citekey: DellaVigna2022
title: Estimating Social Preferences and Gift Exchange at Work
authors: ["DellaVigna, Stefano", "List, John A.", "Malmendier, Ulrike", "Rao, Gautam"]
year: 2022
type: journalArticle
doi: 10.1257/aer.20190920
zotero: "zotero://select/library/items/EZ7VC5KS"
pdf: /Users/jesper/Zotero/storage/29UPASPN/DellaVigna2022.pdf
tags: [literature]
keywords: [social-preferences, gift-exchange, warm-glow, field-experiment, structural-estimation, worker-effort, reciprocity]
topics: ["[[reciprocity-gift-exchange]]"]
related: [Abeler2011, Akerlof1982, Benabou2003, Benabou2006, Besley2005, Charness2002, DellaVigna2012, DellaVigna2018, Dufwenberg2004, Englmaier2012, Falk2006]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We design three field experiments to estimate how workers' social preferences toward their employer motivates their work effort. We vary the pay rates offered to workers, the return to the employer, and employer generosity demonstrated via unexpected gifts. Workers exert effort even without private incentives, but their effort is insensitive to the return to the employer. This is consistent with "warm glow" but not pure altruism. The gifts have no effect on productivity, but engender extra work. This difference is explained partly by the finding that extra work is much more responsive to incentives than is productivity. (JEL C93, J24, J28, J33, M52)

## Summary
Across three field experiments with a unified "pay-rate design," workers' effort toward their employer is best described by warm glow (or a workplace norm) rather than pure (Beckerian) altruism: effort is positive even without incentives and drops when work is discarded, yet is insensitive to the stated return to the employer. Gifts have no measurable effect on productivity (Experiment 1) but raise discretionary extra work (Experiments 2–3); the discrepancy is largely an elasticity artifact, since the extra-work margin is far more responsive to incentives than productivity. The key methodological contribution is showing that varying the worker pay rate lets one recover the cost-of-effort function and thereby structurally estimate social-preference parameters, enabling comparison across heterogeneous tasks.

## Research question
What is the strength and nature of workers' vertical social preferences toward their employer? Specifically, do workers behave as pure altruists (effort rising in the employer's net return) or as warm-glow agents (effort insensitive to the employer's payoff)? And do unexpected gifts induce reciprocity, i.e., gift exchange in the sense of [[@Akerlof1982|Akerlof (1982)]]?

## Method / identification
A simple structural model of effort. Worker $i$ maximizes $u(e_i)=L+p_W e_i-C_i(e_i)+A(\text{Gift},p_E,p_W)\,e_i$, where $L$ is lump-sum pay, $p_W$ the worker pay rate, $C_i$ a convex cost of effort, and $A$ a social-preference weight on per-unit effort. The first-order condition gives $e_i^*=C'^{-1}\!\left(p_W+A\right)$. Two interpretations of $A$ are nested: pure altruism, $A=(\alpha+\mathbf{1}_{Gift}\alpha_{Gift})(p_E-p_W)$, in which effort rises in the employer's net return $p_E-p_W$; and warm glow, $A=(a+\mathbf{1}_{Gift}a_{Gift})\,\bar{p}_E$, where $\bar{p}_E$ is the average employer return used only to normalize $a$, so $\partial e^*/\partial p_E=0$. The two motives are distinguished by the cross-derivative ratio: under altruism $(\partial e^*/\partial p_E)/(\partial e^*/\partial p_W)=\alpha/(1-\alpha)$, while warm glow predicts a zero numerator.

The central identification insight is that prior gift-exchange experiments could not recover preferences because the cost function $C$ and the perceived employer return $p_E$ were both unobserved. The pay-rate design fixes both: varying $p_W$ traces out $C'^{-1}$, and the design either states $p_E$ to workers or uses a task with a natural value measure. A paid "training" round in which output is discarded (so $A=0$) further isolates the cost function from social preferences.

Estimation assumes $C_i(e_i)=c(e_i)\eta_i$ with $\eta_i$ log-normal heterogeneity, and two families for $c$: power, $c(e)=e^{1+\gamma}/(1+\gamma)$ (constant elasticity $1/\gamma$), and exponential, $c(e)=\exp(\gamma e)/\gamma$. Under power cost the estimating equation is $\log(e_{i,t})=\tfrac{1}{\gamma}\log(p_{W,t}+A)-\tfrac{1}{\gamma}k_i-\tfrac{1}{\gamma}f(t)+\epsilon_{i,t}$, with individual fixed effects $k_i$ and a learning/fatigue term $f(t)$; the exponential case is identical but with $e_{i,t}$ (not its log) on the left. Experiment 1 is estimated by nonlinear least squares (clustered by session); the extra-work experiments model corner solutions (censoring at the no-extra-work and maximum-extra-work bounds) and are estimated by maximum likelihood.

Three preregistered (AEARCTR-0000502) experiments: Exp. 1, a six-hour envelope-stuffing productivity task with within-subject piece-rate ($0/10/20$ cents) and employer-return (donor match) variation plus between-subject gifts (positive monetary $14, in-kind thermos, negative $3); Exp. 2, a two-hour data-coding task with a request for up to one hour of extra work under wage-rate ($0/25/50$ cents per minute) and gift (monetary, in-kind, early in-kind) arms; Exp. 3, an online address-checking task with piece-rate ($1/2/4$ cents) variation, a $0.40 monetary gift, and quantitative employer-return variation.

## Data
Three original field-experimental datasets: 446 in-person workers (Exp. 1, the largest in-person gift-exchange sample the authors know of), 300 workers (Exp. 2), and roughly 2,000 online workers (Exp. 3). Workers were recruited for one-time jobs to shut down repeated-game incentives. Data are publicly archived (DellaVigna, List, Malmendier, and Rao 2022).

## Key findings
1. Productivity is inelastic: moving the piece rate from 0 to 20 cents raises output only 12%, an elasticity near $0.1$ ($\hat\gamma\approx9.5$). 2. Effort is insensitive to the employer's return: doubling it via a donor match raises output an insignificant 1.6%, but output drops about 10% when work is discarded in training. 3. Structural estimates of Experiment 1 reject pure altruism ($\hat\alpha=-0.01$, s.e. 0.04) but find large warm glow ($\hat a=0.46$, s.e. 0.07 toward the charity; $0.73$ toward the grocer). 4. Gifts have no significant productivity effect in Experiment 1 (e.g., positive monetary $\hat a_{Gift}=0.15$, in-kind $-0.04$, negative $-0.10$, all insignificant). 5. The extra-work margin is far more elastic, and there gifts significantly raise effort (Exp. 2: monetary +5.6 min, in-kind +4.2, early in-kind +6.6; Exp. 3: monetary +1.9 addresses), though smaller than even the lowest financial incentive. 6. Translated into reciprocity parameters, gift effects cannot be statistically distinguished across experiments for monetary gifts, partly reconciling the apparent productivity/extra-work discrepancy as an elasticity phenomenon.

## Contribution
First systematic field-experimental estimates of the nature of workers' social preferences toward employers, showing they are warm-glow-like (encompassing mission preferences, intrinsic motivation, norms, and signaling), not Beckerian altruism. Methodologically, it makes the case for the pay-rate design, which recovers cost-of-effort parameters, maps reduced-form effects to structural parameters, and permits comparison across tasks; it also documents that the higher-elasticity extra-work margin yields more powered, cost-effective gift-exchange tests than productivity tasks.

## Limitations & open questions
The authors explicitly leave open the lack of gift effects in the productivity experiment (especially for in-kind gifts, where they reject equality with Experiment 2): possible explanations they cannot adjudicate are that the complex within-subject design dampened surprise, that late-experiment effort becomes habitual, or that gifts need an explicit "channel"/request to reciprocate. The model does not separate the sub-mechanisms inside warm glow (mission, intrinsic motivation, norms, signaling), and signaling à la Bénabou and [[@Benabou2006|Tirole (2006)]] would predict pay-rate effects the model ignores. The model assumes incentives do not crowd out intrinsic motivation, abstracts from pay-inequity aversion and horizontal coworker preferences, and the value of work in Experiment 2 is unobserved and assumed at 50 cents. They call for future work to adopt the extra-work design and to disentangle alternative social motives.

## Connections
Builds on the gift-exchange tradition begun by [[@Akerlof1982|Akerlof (1982)]] and tested in the field by Gneezy and List (2006), Kube, Maréchal, and Puppe (2012, 2013), and Cohn, Fehr, and Goette (2014), with the extra-work design adapted from [[@Abeler2011|Abeler, Falk, Goette, and Huffman (2011)]]. The warm-glow interpretation derives from Andreoni (1989) and connects to mission preferences in [[@Besley2005|Besley and Ghatak (2005)]], intrinsic motivation and signaling in Bénabou and [[@Benabou2003|Tirole]] (2003, 2006), identity in Akerlof and Kranton (2005), and meaningful work in Ariely, Kamenica, and Prelec (2008). The structural behavioral-economics approach follows [[@DellaVigna2012|DellaVigna, List, and Malmendier (2012)]], Augenblick, Niederle, and Sprenger (2015), and [[@DellaVigna2018|DellaVigna and Pope (2018)]], with cost-of-effort estimation building on Shearer (2004) and Andreoni and Sprenger (2012). Reciprocity foundations draw on Fehr and Gächter (2000), [[@Charness2002|Charness and Rabin (2002)]], [[@Dufwenberg2004|Dufwenberg and Kirchsteiger (2004)]], and [[@Falk2006|Falk and Fischbacher (2006)]]. The return-to-employer variation parallels [[@Englmaier2012|Englmaier and Leider (2012)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
