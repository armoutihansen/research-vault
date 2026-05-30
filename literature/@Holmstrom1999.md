---
citekey: Holmstrom1999
title: "Managerial Incentive Problems: A Dynamic Perspective"
authors: ["Holmström, Bengt"]
year: 1999
type: journalArticle
doi: 10.1111/1467-937X.00083
zotero: "zotero://select/library/items/5299X327"
pdf: /Users/jesper/Zotero/storage/3EU7WWTV/Holmstrom1999.pdf
tags: [literature]
keywords: [career-concerns, signal-jamming, managerial-incentives, moral-hazard, reputation, risk-taking, bayesian-learning]
topics: []
related: [Akerlof1970, Gibbons1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The paper studies how a person's concern for a future career may influence his or her incentives to put in effort or make decisions on the job. In the model, the person's productive abilities are revealed over time through observations of performance. There are no explicit output-contingent contracts, but since the wage in each period is based on expected output and expected output depends on assessed ability, an "implicit contract" links today's performance to future wages. An incentive problem arises from the person's ability and desire to influence the learning process, and therefore the wage process, by taking unobserved actions that affect today's performance. The fundamental incongruity in preferences is between the individual's concern for human capital returns and the firm's concern for financial returns. The two need be only weakly related. It is shown that career motives can be beneficial as well as detrimental, depending on how well the two kinds of capital returns are aligned.

## Summary
A foundational career-concerns paper (written 1982, published 1999) that formalizes Fama's (1980) conjecture that labour-market reputation can discipline managerial moral hazard even without explicit output-contingent contracts. Holmström builds a dynamic Bayesian-learning model in which the market infers a manager's unknown ability from a noisy output history and pays a competitive wage equal to expected output. Because effort raises perceived ability, an implicit incentive emerges, but Holmström shows that the resulting effort path is generally inefficient: it decays over time, is distorted by transient learning, and is misaligned whenever technology is non-linear. A second part shows that the same career-concern logic creates an incongruity in *risk* preferences, making managers act risk-averse even when risk-neutral. The paper introduces what Fudenberg and Tirole later named "signal jamming."

## Research question
Can reputational (career) concerns in a competitive labour market substitute for explicit incentive contracts in policing managerial moral hazard, both for work effort and for investment/risk-taking decisions? Under what conditions does this implicit mechanism deliver efficient behaviour, and when does it fail?

## Method / identification
A multi-period equilibrium model of an unobservable-action ("signal-jamming") type. A risk-neutral manager produces output $y_t=\eta+a_t+\varepsilon_t$, where $\eta$ is unknown talent (Gaussian prior, mean $m_1$, precision $h_1$), $a_t$ is unobserved effort, and $\varepsilon_t\sim N(0,h_\varepsilon^{-1})$. Disutility $g(a_t)$ is increasing and convex. A competitive, risk-neutral market sets the wage equal to expected output conditional on the output history, $w_t(y^{t-1})=E[y_t\mid y^{t-1}]=E[\eta\mid y^{t-1}]+a_t(y^{t-1})$.

Equilibrium is a fixed point: wages depend on the conjectured decision rule, and the manager's optimal rule maximizes the discounted stream $\sum_t \beta^{t-1}\big(E w_t - E g(a_t)\big)$ taking the wage rule as given. In equilibrium the market is not fooled — it observes $z_t=\eta+\varepsilon_t=y_t-a_t(y^{t-1})$ — yet the manager is trapped supplying expected effort (a "rat race"). Gaussian updating gives the posterior mean as a random walk and precision evolving deterministically: with fixed talent $h_{t+1}=h_t+h_\varepsilon$ (so $\eta$ becomes fully known). To obtain a permanent effect, talent is made stochastic ($\eta_{t+1}=\eta_t+\delta_t$, $\delta_t\sim N(0,h_\delta^{-1})$), giving a stationary precision $h^*$ and a stationary updating weight $\mu^*=1+\tfrac12 r-\sqrt{\mu^* r^2+r}$ with $r=h_\delta/h_\varepsilon$. Part 3 uses two-period examples with a binary project (success probabilities $\pi_T>\pi_N$ for talented/untalented managers) and Bayesian talent updating $\eta^+,\eta^-$ to study investment/risk-taking, including a verifiable-information case and a non-verifiable "lemons" case.

## Data
None — this is a pure theory paper. The only empirical reference is Medoff and Abraham (1980), cited informally to suggest that younger workers are more productive, consistent with the model's prediction of early-career over-investment in effort.

## Key findings
- **Proposition 1 (work effort).** The stationary effort level $a^*$ is never above the efficient level $\bar a$ (defined by $g'(\bar a)=1$), satisfying $\frac{\beta(1-\mu^*)}{1-\mu^*\beta}=g'(a^*)$. Efficiency obtains only in the knife-edge case $\beta=1$ with $\sigma_\delta^2>0$; effort is closer to efficient the larger is $\beta$, the higher is output precision, and the more stochastic is talent.
- **Proposition 2 (dynamics).** Optimal effort $a_t$ converges monotonically to $a^*$. When initial precision $h_1<h^*$ (the natural case for young managers), effort converges from *above* — young people over-invest in effort because reputation returns are largest when beliefs are diffuse. Transient inefficiency can be substantial even without discounting.
- **Non-linear technology.** Linearity is essential for efficiency. With output $f(\eta+a)$, convex $f$ (Jensen) implies over-supply of effort, concave $f$ under-supply; job-matching makes returns to ability convex (Rosen 1982), and pure signalling (schooling) yields wasteful effort.
- **Risk-taking incongruity.** Career concerns generate a genuine divergence in risk preferences: the manager cares about the success likelihood $\pi_T$ (which reveals talent) while the firm cares about payoffs $(y_+,y_-)$. A risk-averse — even a risk-neutral — manager becomes excessively conservative because failure carries a negative talent signal. In the non-verifiable single-project case, the only equilibrium is the degenerate "lemons" outcome ($t=1$): no investment is made. Stock options are conjectured to help by removing downside risk.

## Contribution
Provides the first explicit dynamic model of career concerns, formalizing and substantially qualifying Fama (1980). It establishes the "signal-jamming" paradigm — unobserved actions distort a public learning process — distinct from classical signalling because the agent need have no private information and actions are observed only with noise. It shows time is not unambiguously beneficial for incentives: it helps police effort but can *create* risk-taking problems. The framework underpins a large literature on reputation, herding, and short-termism in organizations and capital markets.

## Limitations & open questions
Holmström is explicit that the paper "raised rather than answered questions." Stated open problems: (i) a full dynamic model with explicit contracts plus career concerns (combining implicit and explicit incentives) remains to be developed; (ii) the optimal resolution of the risk-taking incongruity is not analyzed — in particular whether stock options are optimal "has to await a more careful analysis"; (iii) effects of convex payoffs in talent, managers having superior information about own talent (risk-taking as a positive signal), and richer investment outcomes could overturn the conservatism result; (iv) the model may explain why corporate investment procedures are detailed and centralized — securing proper talent evaluation, not just project selection. Holmström also notes (in the 1999 addendum) that the introduction's third paragraph "no longer reflects my current thinking."

## Connections
Directly formalizes Fama (1980) and builds on the wage-dynamics model of Harris & Holmström (1982). The risk-taking section critiques the static reward-design models of Wilson (1968) and Ross (1973), and the lemons equilibrium invokes [[@Akerlof1970|Akerlof (1970)]]. It sits in the moral-hazard tradition of Holmström (1979), Mirrlees (1976), Harris & Raviv (1979), Shavell (1979), and Grossman & Hart (1983); the time-resolves-incentives intuition comes from Radner (1981) and Rubinstein (1981). The signal-jamming label is due to Fudenberg & Tirole (1986). It launched the empirical and theoretical career-concerns literature, including [[@Gibbons1992|Gibbons & Murphy (1992)]], Dewatripont, Jewitt & Tirole (1999), Meyer & Vickers (1997), Holmström & Ricart i Costa (1986), and the short-termism/herding work of Narayanan (1985), Stein (1989), and Scharfstein & Stein (1990); Milgrom & Roberts (1988) on influence activities is closely related.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
