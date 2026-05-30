---
citekey: Armouti-Hansen2024a
title: Efficiency wages with motivated agents
authors: ["Armouti-Hansen, Jesper", "Cassar, Lea", "Deréky, Anna", "Engl, Florian"]
year: 2024
type: journalArticle
doi: 10.1016/j.geb.2024.03.001
zotero: "zotero://select/library/items/5W9H9FVJ"
pdf: /Users/jesper/Zotero/storage/V2IE584B/Armouti-Hansen et al. - 2024 - Efficiency wages with motivated agents.pdf
tags: [literature]
keywords: [gift-exchange, efficiency-wages, prosocial-motivation, reciprocity, biased-beliefs, principal-agent, lab-experiment]
topics: []
related: [Benabou2003, Besley2005, Bolton2000, Cassar2018, Charness2002, DellaVigna2022, Dufwenberg2004, Fehr1993, Fehr1999, Rabin1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Many jobs serve a social purpose beyond profit maximization, contributing positively to society. This paper uses a modified principal-agent gift-exchange game with positive externality (prosocial treatment) to study how workers' prosocial motivation interacts with the use of efficiency wages in stimulating effort. We find that prosocial motivation and efficiency wages are independent in stimulating effort: compared to a standard gift-exchange game (GE treatment), the presence of the externality shifts the agents' effort choice function upwards without affecting its slope. Thus, if principals were profit-maximizers, wage offers should be the same in both treatments. However, principals offer higher wages in the prosocial treatment. We show that this is due to principals in the GE treatment highly underestimating agents' reciprocity and thereby offering wages below the profit-maximizing level. Results from robustness-checks further suggest that our findings are unlikely to be driven by a simple efficiency effect.

## Summary

In a laboratory gift-exchange experiment, adding a positive social externality to a job (the agent's effort triggers a charitable donation) raises agents' effort at every wage but does not change the slope of the effort–wage function. So prosocial motivation and reciprocity are *independent* (additively separable) motivators, and a profit-maximizing principal should offer the *same* wage with or without the externality. Yet principals offer higher wages in the prosocial treatment. The paper traces this to *biased beliefs*: in the standard gift-exchange treatment principals badly underestimate agents' reciprocity (the eﬀort–wage slope) and therefore pay below the profit-maximizing wage, whereas in the prosocial treatment their beliefs are well-calibrated and they pay near-optimally. Two further treatments show the effect is driven by the externality itself, not by the higher total surplus it mechanically creates.

## Research question

Are workers' prosocial motivation (caring about the social impact of the job) and reciprocity toward the employer complements, substitutes, or independent in motivating effort? How does their relationship shape equilibrium wage contracts, and do principals correctly anticipate agents' responses when setting wages? The applied target is the wage differential between profit and non-profit / mission-oriented organizations.

## Method / identification

A one-shot principal–agent gift-exchange game with incomplete contracts, run as a between-subjects lab experiment. The theory frames the benchmark: agent utility is additively separable,
$$U(w,m,e;\theta) = w - \tfrac{c}{2}e^2 + M(w,m,e;\theta),$$
where $w$ is wage, $e\in\{1,\dots,10\}$ effort, $m$ the job's social impact, and $M\ge 0$ an intrinsic-benefit term governed by a type vector $\theta\sim F_\theta$. Prosocial motivation is the cross-partial $M_{em}\ge 0$; reciprocity is the cross-partial $M_{ew}\ge 0$. A risk-neutral principal maximizes $r\,\bar e^{*}(w,m)-w$. Comparative statics yield three predictions: (1) the minimum acceptable wage falls in $m$ ($\bar w_m<0$); (2) optimal effort rises in $m$ for any wage ($\bar e^{*}_m>0$); (3) the profit-maximizing wage rises iff the interaction term $\bar M_{ewm}>0$ — i.e. it depends on whether the social impact steepens or flattens the effort–wage slope, which is *a priori* indeterminate.

Identification rests on the *strategy method*: each agent states an accept/reject decision and an effort level for every possible wage offer $w\in\{1,3,5,10,15,\dots,95\}$, reconstructing each agent's full optimal effort function (and hence its slope) rather than a single point. Principals' *beliefs* about agents' effort at each wage are elicited in an incentivized, unprimed manner, plus a "guessed profit-maximizing wage." This lets the authors compute, per pair, the offered wage, the belief-implied ("expected") profit-maximizing wage, the guessed profit-maximizing wage, and the *actual* profit-maximizing wage, and to test whether principals are optimizing against true vs. distorted beliefs. Charitable motivation is measured ex ante via a dictator-with-charity game and used as a control to rule out a direct donation motive.

## Data

Lab experiment at the University of Cologne (z-Tree). Main study (Sept. 2016): 190 students, 94 GE / 96 prosocial. Two robustness treatments added later: a *neutral* treatment (May 2022, n = 90) where the donation recipient is the agent's least-preferred charity / an anonymous student, and an *efficiency* treatment (Oct. 2022, n = 120) where total surplus equals the prosocial treatment but the extra surplus goes to the principal (payoff $35e-w$ rather than $10e-w$), removing the externality. Average earnings 13.72 euro. Effort costs $c(e)$ follow the [[@Fehr1993|Fehr et al. (1993)]] schedule (well approximated by the quadratic with $c\approx 0.38$). Data available on request.

## Key findings

- **Result 1 (Prediction 1):** the average minimum acceptable wage is marginally lower in the prosocial treatment (more agents accept wages below the outside option of 5).
- **Result 2 (Prediction 2):** for any given wage, effort is higher under the externality, but the *slope* of the effort–wage function is unchanged (treatment×wage interaction near zero). Prosocial motivation and reciprocity are thus independent — utility is additively separable in social purpose and wage-reciprocity.
- **Result 3:** contrary to the profit-maximizing prediction (which, given equal slopes, implies equal wages), principals offer significantly higher wages in the prosocial treatment (about 36 vs. 26 points, $p=0.01$).
- **Result 4 (mechanism):** in *both* treatments principals act as profit-maximizers given their beliefs (offered wage ≈ guessed/expected profit-maximizing wage). The wage gap arises because GE-treatment principals hold *biased beliefs*: they sharply underestimate the effort–wage slope (agents' reciprocity) — at $w=95$ expected effort is ~60% below actual — so their offered wage sits well below the true profit-maximizing wage. In the prosocial treatment beliefs are calibrated and wages are near-optimal. A direct charitable motive is ruled out (its interaction is insignificant; principals do not pay above their own guessed profit-maximizing wage).
- **Robustness:** the neutral treatment lands "in between" (weaker prosocial pull), and the efficiency treatment behaves like GE — principals again underestimate the slope and underpay. So the result is driven by the *externality* (a third party benefiting), not by pure efficiency, and is independent of which specific third party benefits (consistent with Cassar 2019).

## Contribution

Shows that efficiency wages and an organization's social purpose are *complements* in motivating effort — not because of agents' preferences (where they are independent) but because of *principals' biased beliefs*: the social mission de-biases employers' expectations of reciprocity. This is a "new hidden benefit" of social mission and offers a novel channel for the profit/non-profit wage differential (mission-oriented organizations more likely to sustain efficiency wages). It provides a new explanation for why one-shot gift-exchange yields lower efficiency than repeated settings — agents *are* reciprocal, but principals fail to anticipate it — and contributes incentivized, strategy-method elicitation of principals' beliefs in this context.

## Limitations & open questions

- **Externality vs. efficiency not fully separated:** even with the efficiency treatment, inequity aversion specific to the principal (vs. a third party) could confound the comparison; the endogeneity is not cleanly resolved.
- **One-shot only:** rules out reputation but ignores long-term relationships and learning; the authors conjecture pessimistic beliefs persist because an under-paying principal never observes the counterfactual (cf. Caria & Falco 2022).
- **Exogenous, costless social impact:** the mission is fixed and imposes no cost on the employer. An explicit open extension: make the social impact *costly* to the principal (CSR investment), which might induce CSR-reciprocity or, conversely, backlash — and ask whether employers predict these responses or develop new biases.
- **No self-selection:** agents cannot sort into mission vs. non-mission jobs; the authors expect effects to strengthen with selection.
- **External validity / abstraction:** strategy method and monetary effort levels are artificial; lab control imposes the model's assumptions directly.

## Connections

Builds on the standard gift-exchange paradigm of [[@Fehr1993|Fehr, Kirchsteiger & Riedl (1993)]] and Brown, Falk & Fehr (2004), and on reciprocity models ([[@Rabin1993|Rabin 1993]]; [[@Dufwenberg2004|Dufwenberg & Kirchsteiger 2004]]; Falk & Fischbacher 2005) and distributional preferences ([[@Fehr1999|Fehr & Schmidt 1999]]; [[@Bolton2000|Bolton & Ockenfels 2000]]; [[@Charness2002|Charness & Rabin 2002]]). The mission-motivation framing follows [[@Besley2005|Besley & Ghatak (2005)]], Bénabou & [[@Benabou2003|Tirole]] (2003, 2006), and Cassar (2019), with intrinsic-benefit warm-glow from Andreoni (1989, 1990). The independence-vs-interaction question parallels Kosfeld et al. (2017) (purpose and incentives independent, purpose and recognition negatively interacting), Bartling, Fehr & Schmidt (2012), Kvaløy, Nieken & Schöttner (2015), and Ichniowski, Shaw & Prennushi (1997). The biased-beliefs mechanism connects to Caria & Falco (2022) on employers underestimating worker reciprocity, and to belief-formation work by Fehr (2009) and Schwerter & Zimmermann (2020). The field evidence on gift-exchange it speaks to includes Gneezy & List (2006), Hennig-Schmidt, Sadrieh & Rockenbach (2010), and [[@DellaVigna2022|DellaVigna et al. (2022)]]; the profit/non-profit wage-differential debate draws on Handy & Katz (1998), Preston (1988), Leete (2001), Mocan & Tekin (2003), and Børsting & Thomsen (2017). The survey reference throughout is [[@Cassar2018|Cassar & Meier (2018)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
