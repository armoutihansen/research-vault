---
citekey: Grunewald2022
title: Information manipulation and competition
authors: ["Grunewald, Andreas", "Kräkel, Matthias"]
year: 2022
type: journalArticle
doi: 10.1016/j.geb.2021.11.007
zotero: "zotero://select/library/items/WYZFW3CT"
pdf: /Users/jesper/Zotero/storage/53FDWRFL/Grunewald2022.pdf
tags: [literature]
keywords: [information-manipulation, signal-jamming, competition, institutions, fake-news, bayesian-updating, backfiring]
topics: []
related: [Lazear1981, Nalebuff1983]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> In the last decade, social media and the Internet have amplified the possibility to circulate false information among an audience, which has become a serious threat to the credibility of politicians, organizations, and other decision makers. This paper proposes a framework for investigating the incentives to strategically manipulate the audience's belief under different institutions and in various competitive environments. We show that more rigorous institutions against information manipulation can lead to higher manipulation intensities in equilibrium. Complementary, we study what kind of competitive environment is particularly susceptible to the manipulation of information.

## Summary
Two players with uncertain quality compete before an audience that observes a noisy public signal about each. Players can covertly and at a cost manipulate that signal (signal jamming); the audience updates Bayesianly and the player with the higher posterior expected quality (the "posterior lead") wins. The paper characterizes equilibrium manipulation intensities across two payoff environments (constant prizes vs. payoffs affine in the posterior lead) and studies how anti-manipulation institutions affect them. Its headline result is that more rigorous institutions can *backfire*: by making signals appear more trustworthy, they induce the audience to rely more heavily on news, restoring or amplifying incentives to manipulate.

## Research question
Which competitive environments are most susceptible to strategic information manipulation, and how do institutions that suppress false information in the media (e.g., a public agency, a law forcing deletion of fake content) affect players' equilibrium incentives to manipulate? In particular: can stricter institutions perversely increase manipulation?

## Method / identification
A two-player game of perfect Bayesian equilibrium in pure strategies. Each risk-neutral player $i\in\{A,B\}$ has quality $q_i\sim N(\bar q_{i0},\sigma_{i0}^2)$, unknown to players and audience. Player $i$ chooses a hidden manipulation intensity $f_i\ge 0$ at cost $c(f_i)$ ($c(0)=c'(0)=0$, $c''>0$, $c''$ bounded below by $\underline c>0$). The audience observes a linear signal
$$s_i = q_i + \beta\cdot(f_i+\varphi_i),\qquad \varphi_i\sim N(0,\sigma_\varphi^2),$$
where $\varphi_i$ is exogenous noise and $\beta>0$ is the reduced-form institution parameter: *lower $\beta$ = more rigorous institutions* (in the limit $\beta\approx 0$ the audience learns $q_i$ exactly). Crucially, institutions cannot discriminate between players' intentional manipulation and exogenous false information — they scale $f_i+\varphi_i$ jointly. By DeGroot (1970), Bayesian updating gives posterior mean $\bar q_{i1}=\bar q_{i0}+\gamma_i(s_i-\beta\hat f_i-\bar q_{i0})$ with updating weight
$$\gamma_i := \frac{\sigma_{i0}^2}{\beta^2\sigma_\varphi^2+\sigma_{i0}^2},$$
where $\hat f_i$ is the audience's (equilibrium) belief about $i$'s intensity. Payoffs are a piecewise function of the posterior lead: $u^H(\bar q_{i1}-\bar q_{j1})$ if $i$ leads, $u^L(\cdot)$ otherwise, with $u^H(x)>u^L(x)$. Two environments are studied: (i) **constant payoffs** $u^H=\bar u^H>\bar u^L=u^L$; (ii) **affine payoffs** $u^H=\bar\eta+\eta_H(\bar q_{i1}-\bar q_{j1})$, $u^L=\bar\eta+\eta_L(\cdot)$ with $\eta_H\ge|\eta_L|$. The composed stochastic term $\delta_i$ is normal with density $g_i$ and cdf $G_i$. Comparative statics in $\beta$ are decomposed into an **information effect** $\frac{\partial(\beta\gamma_i)}{\partial\beta}\cdot E_i$ and an **environment effect** $\beta\gamma_i\cdot\frac{\partial E_i}{\partial\beta}$.

## Data
None — this is a pure theory paper. No empirical data or simulation beyond illustrative numerical figures (Figs. 1–2) of the environment effect for chosen parameter values (e.g., $\sigma_{i0}^2=\sigma_{j0}^2=\sigma_\varphi^2=4$, $\beta=0.5$).

## Key findings
- **Proposition 1** (FOC): In any interior pure-strategy equilibrium, $f_i^*$ solves $\beta\gamma_i\,E_i = c'(f_i^*)$, where the bracket $E_i$ collects $u^H{}'$, $u^L{}'$ and the jump $(u^H(0)-u^L(0))g_i(\Gamma_i)$. $E_i>0$ always.
- **Information effect direction**: $\frac{\partial}{\partial\beta}(\beta\gamma_i)=\gamma_i-\frac{2\beta^2\sigma_\varphi^2\gamma_i}{\beta^2\sigma_\varphi^2+\sigma_{i0}^2}$. More rigorous institutions raise manipulation incentives (via this channel) iff $\beta^2\sigma_\varphi^2>\sigma_{i0}^2$, i.e., when most signal variance is exogenous noise rather than genuine quality uncertainty.
- **Corollary 1 / 2**: Existence and characterization of unique interior equilibria under constant ($\beta\gamma_i(\bar u^H-\bar u^L)g_i(\Gamma_i)=c'(f_i^*)$) and affine ($\beta\gamma_i[\eta_H-(\eta_H+\eta_L)G_i(\Gamma_i)]=c'(f_i^*)$) payoffs.
- **Proposition 2** (environment susceptibility): The prior lead $\bar q_{i0}-\bar q_{j0}$ is decisive. Constant payoffs yield high manipulation in *balanced* races but negligible manipulation when one player has a large prior lead (winner predetermined). Affine payoffs sustain manipulation even in *unbalanced* races (at least one player still competes for the margin). Hence affine payoffs dominate for heterogeneous players; constant payoffs dominate for homogeneous players.
- **Proposition 3** (constant payoffs, institutions): The environment effect has the same sign for both players; backfiring occurs (both players manipulate more under stricter institutions) iff initial heterogeneity $|\bar q_{i0}-\bar q_{j0}|$ exceeds a threshold $\chi_i^{const}(\beta)$ — even when the information effect is negative. Mechanism: lower $\beta$ raises $\sigma_{\delta_i}^2$, making the outcome less predictable and restoring the trailing player's chance.
- **Proposition 4** (affine payoffs, institutions): The environment effect is negative only for the *trailing* player ($\bar q_{i0}<\bar q_{j0}$); only the initially trailing player raises manipulation under stricter institutions, and backfiring can occur even when the information effect is strictly positive.
- **Discussion/robustness**: The backfiring result hinges on institutions being unable to discriminate intentional vs. exogenous false information. If instead institutions directly eliminate players' manipulation (remove $\beta$ from the players' channel), stricter institutions unambiguously reduce manipulation.

## Contribution
Provides a tractable signal-jamming model of *competitive* information manipulation (two senders, costly signals) that bridges (a) the signal-jamming literature (single-agent: Stein 1989; Holmström 1999; Meyer & Vickers 1997) and (b) reduced-form institutions against fake news. Two novel insights: it shows that susceptibility to manipulation depends jointly on the payoff structure and on initial heterogeneity, and it identifies a backfiring channel by which transparency-fostering institutions can increase manipulation. It complements the tournament/contest and forecasting-contest literatures by endogenizing how the competitive environment shapes manipulation, and contrasts with Bayesian persuasion (Kamenica & Gentzkow 2011), which assumes commitment and costless signals.

## Limitations & open questions
- Players are assumed *not to know their own quality* (standard in signal jamming). The authors note that with private information about types the audience's updating must account for type-dependent manipulation; they conjecture results are robust (citing Edmond 2013 for existence) but do not prove it.
- Institutions are modeled in *reduced form* via a single parameter $\beta$; richer or strategic institutional design is left open.
- The analysis restricts to pure-strategy interior equilibria and to constant/affine payoff structures (with identical constants $\bar\eta$); generalization to nonlinear (e.g., quadratic) payoffs is asserted to transfer but is "technically involved."
- Only two players and a single audience holding a point belief; richer audiences, multiple players, or repeated interaction are not treated.

## Connections
Technically rooted in the signal-jamming literature: Holmström (1999) on career concerns, Meyer & Vickers (1997), Stein (1989), and propaganda models (Little 2012, 2017; Edmond 2013). The competitive twist builds on the authors' own Grunewald & Kräkel (2017) and Miklós-Thal & Ullrich (2015), who show competition can overturn standard signal-jamming comparative statics. The "transparency can backfire" theme parallels Prat (2005), Dubey & Wu (2001), and Dubey & Haimanko (2003) in moral-hazard settings, though those lack underlying quality the audience seeks to learn. Reputational cheap talk relates via Levy (2004), Ottaviani & Sørensen (2006a,b), Morris (2001), and Ely & Välimäki (2003). The costless-commitment alternative is Bayesian persuasion (Kamenica & Gentzkow 2011, 2016, 2017; Crawford & Sobel 1982; Gentzkow & Kamenica 2014). Payoff-structure applications draw on tournaments ([[@Lazear1981|Lazear & Rosen 1981]]; [[@Nalebuff1983|Nalebuff & Stiglitz 1983]]), vertical product differentiation (Shaked & Sutton 1982), parliamentary-vote models (Fishburn & Gehrlein 1977; Grossman & Helpman 1996), and influence activities (Milgrom 1988; Milgrom & Roberts 1988). The fake-news motivation cites Allcott & Gentzkow (2017) and Lazer et al. (2018).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
