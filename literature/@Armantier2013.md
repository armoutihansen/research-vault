---
citekey: Armantier2013
title: "Eliciting beliefs: Proper scoring rules, incentives, stakes and hedging"
authors: ["Armantier, Olivier", "Treich, Nicolas"]
year: 2013
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/QVF6SNAM"
pdf: "/Users/jesper/Zotero/storage/4D8RN828/Armantier and Treich - 2013 - Eliciting beliefs Proper scoring rules, incentives, stakes and hedging.pdf"
tags: [literature]
keywords: [proper-scoring-rules, belief-elicitation, risk-aversion, hedging, subjective-probability, experimental-economics]
topics: ["[[experimental-belief-elicitation]]"]
related: [Gneiting2007, Karni2009, Manski2004, Offerman2009, Roth1979, Savage1971]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> Proper Scoring Rules (PSR) are popular incentivized mechanisms to elicit an agent's beliefs. This paper combines theory and experiment to characterize how PSR bias reported beliefs when i) the PSR payments are increased, ii) the agent has a financial stake in the event she is predicting, and iii) the agent can hedge her prediction by taking an additional action. In contrast with previous literature, the PSR biases are characterized for all PSR and all risk averse agents. Our results reveal complex distortions of reported beliefs, thereby raising concerns about the ability of PSR to recover truthful beliefs in general decision-making environments.

## Summary
Proper scoring rules reward a reported probability $q$ with state-contingent payments $S_1(q)$ (event occurs) and $S_0(q)$ (event does not occur), designed so a risk-neutral agent truthfully reports her subjective probability $p$. Armantier and Treich ask what PSR actually elicit once the agent is risk averse and embedded in a realistic environment. Combining a unified theory with a large between-subject field experiment, they characterize PSR-induced biases across three forces: the scale of PSR payments (incentives), an exogenous financial stake in the predicted event, and an endogenous hedging opportunity. The message is cautionary: outside the idealized no-stake, risk-neutral benchmark, PSR produce systematic and sometimes unpredictable distortions, so reported probabilities cannot in general be read as subjective beliefs.

## Research question
Do proper scoring rules recover truthful subjective probabilities in realistic decision environments? Specifically, for *all* PSR and *all* risk-averse expected-utility agents, how does the elicited "response function" $R(p)$ deviate from the true belief $p$ when (i) PSR payments are scaled, (ii) the agent holds a financial stake in the event, and (iii) the agent can hedge the prediction with a side investment?

## Method / identification
Theory uses a standard expected-utility framework with a thrice-differentiable, strictly increasing, state-independent utility $u(\cdot)$. A scoring rule $S=(S_1(q),S_0(q))$ is *proper* iff $p=\arg\max_{q}\,pS_1(q)+(1-p)S_0(q)$. The key structural device (Proposition 2.0, following [[@Gneiting2007|Gneiting & Raftery 2007]], [[@Savage1971|Savage 1971]], Schervish 1989) is that $S$ is proper iff there exists a strictly convex $g$ ($g''(q)>0$) with $S_1(q)=g(q)+(1-q)g'(q)$ and $S_0(q)=g(q)-qg'(q)$; "standard" PSR additionally satisfy $g'(1/2)=0$ so payoffs cross at $q=1/2$. The quadratic, logarithmic and spherical rules are all special cases.

The response function is $R(p)=\arg\max_{q}\,pu(S_1(q))+(1-p)u(S_0(q))$. Four propositions are proved (Appendix A):
- **Prop 2.1 (risk aversion):** for standard PSR, $R(p)\succeq p$ iff $p\le 1/2$ — $R$ is *regressive* (crosses the diagonal from above) with fixed point $1/2$, generalizing Winkler & Murphy (1970) to all standard PSR; greater Pratt risk aversion pushes reports further toward $1/2$.
- **Prop 2.2 (incentives):** scaling payments by $a>0$, the sign of $\partial R(p;a)/\partial a$ is governed by relative risk aversion $\gamma(x)=-xu''(x)/u'(x)$: under increasing RRA larger payments make reports *more* uniform, under CRRA payments are irrelevant, and under DRRA smaller payments can *exacerbate* the bias — overturning the folk belief that paying less yields truthful reports.
- **Prop 2.3 (stakes):** an exogenous bonus $\Delta$ when the event occurs equals adding $\Delta$ to $S_1$; it preserves properness but shifts $R$ downward everywhere ($\partial R/\partial\Delta\le 0$), leaving $R$ either regressive with an interior fixed point or wholly below the diagonal.
- **Prop 2.4 (hedging):** with optional investment $\delta\in[0,\bar\delta]$ in an asset paying $k+1$ if the event occurs, the optimum has three regimes around thresholds $\underline p(k)<\bar p(k)$: no investment with increasing $R$ at low $p$; full investment (acting like a stake $(k+1)\bar\delta$) at high $p$; and an intermediate interval where the agent invests partially and reports a *constant* $1/(1+k)$ independent of $p$ — the PSR transfers across states while the asset adjusts risk exposure.

Empirics use a reduced-form estimator $\hat P_{it}=\varphi_i(P_t)+u_{it}$, where $\hat P_{it}$ is the elicited probability for subject $i$ on event $t$, $P_t$ the objective probability, $\varphi_i$ a monotone inverse-S response function ($\varphi(0)=0,\varphi(1)=1$), and $u_{it}$ truncated normal so $\hat P_{it}\in[0,1]$. Seven treatments map onto the propositions: control $T_0$ (QSR); hypothetical $T_1$ and high-incentive $T_2$; low/high stakes $T_3,T_4$ (bonus 2{,}000/8{,}000 FCFA); low/high hedging $T_5,T_6$ ($k=1,3$). Hypotheses H0–H6 are the predicted fixed points and orderings.

## Data
Original field-experiment data: 301 subjects (current/former university students) in Ouagadougou, Burkina Faso, June 2009; min 41, max 48 per treatment; 74% male, median age 25; substantial stakes (max payment 40{,}000 FCFA, exceeding a graduate's monthly entry salary). Subjects forecast outcomes of two ten-sided dice (events with objective probabilities 3% to 90%) under each treatment's scoring/stake/hedging regime.

## Key findings
- **Control ($T_0$):** the response function is regressive with the traditional inverse-S shape and a fixed point near $1/2$, replicating [[@Offerman2009|Offerman et al. (2009)]]. H0 verified.
- **Incentives:** raising real payments (H2) and using hypothetical payments (H1) both shift the response function, contradicting the prediction that incentive scale is irrelevant — consistent with non-CRRA utility (both *Not Verified* as "no change," confirming payments matter).
- **Stakes:** $T_3$'s fixed point shifts toward $1/4$ and $T_4$ lies below the diagonal as predicted (H3, H4 largely verified) — stakes substantially and directionally bias reports downward.
- **Hedging:** the predicted flattening (constant report over an interval) and downward shift appear (H5, H6 partly verified), confirming hedging creates an endogenous-stake distortion.
- Overall (summarized in Table 3): the theoretically derived distortions from incentives, stakes and hedging are mostly empirically relevant.

## Contribution
First unified characterization of PSR biases holding for *all* proper scoring rules and *all* risk-averse EU agents, via the convex-$g$ representation, rather than the quadratic-rule-only treatments of prior work. It is also the first theoretical analysis of PSR under an explicit hedging (endogenous-stake) opportunity, backed by a purpose-built multi-treatment field experiment. The practical upshot: with unobserved stakes or hedging, theory cannot correct PSR biases, and lottery-ticket payment is the only remedy that stays incentive compatible under EU when stakes or hedging are present.

## Limitations & open questions
- Reducing payments to mitigate bias can backfire under DRRA — there is no general payment-scaling fix; designing a mechanism robust to *both* stakes/hedging *and* risk aversion remains open (existing "truth serums" fix one but not the other).
- Karni & Safra (1995): unbiased elicitation via marginal rates of substitution is impossible when stakes are unobserved, even with observable utility and repeated experiments — sharply limiting any incentivized remedy.
- The theory assumes EU; behavior under non-EU (probability weighting, ambiguity) interacting with stakes/hedging is left for future work.
- Whether non-incentivized elicitation may be preferable ([[@Manski2004|Manski 2004]]) is asserted, not resolved — the lab-vs-field debate over how best to elicit beliefs is left open.

## Connections
Builds on the convex-function characterization of proper scoring rules in [[@Gneiting2007|Gneiting & Raftery (2007)]], [[@Savage1971|Savage (1971)]] and Schervish (1989), and generalizes the risk-aversion result of Winkler & Murphy (1970) and Kadane & Winkler (1988). The experimental benchmark (regressive inverse-S response, "truth serum") follows Offerman, Sonnemans, van de [[@Offerman2009|Kuilen & Wakker (2009)]], with related corrections in Andersen et al. (2010). The stakes/hedging concern connects to market scoring rules (Hanson 2003, 2007), peer-prediction (Miller, Resnick & Zeckhauser 2005), and Blanco et al. (2010) on hedging in the lab. The impossibility of unbiased elicitation under unobserved stakes is Karni & Safra (1995); alternative mechanisms are reviewed in Trautmann & van de Kuilen (2011) and [[@Karni2009|Karni (2009)]]. Lottery-ticket payment traces to [[@Roth1979|Roth & Malouf (1979)]] and Allen (1987); the subjective-expectations agenda is [[@Manski2004|Manski (2004)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
