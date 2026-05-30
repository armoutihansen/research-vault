---
citekey: Grunewald2017
title: Advertising as signal jamming
authors: ["Grunewald, Andreas", "Kräkel, Matthias"]
year: 2017
type: journalArticle
doi: 10.1016/j.ijindorg.2017.09.003
zotero: "zotero://select/library/items/MSXITSWB"
pdf: /Users/jesper/Zotero/storage/ZHVUJ8Q9/Grunewald2017.pdf
tags: [literature]
keywords: [signal-jamming, informative-advertising, experience-goods, price-competition, vertical-differentiation, bayesian-updating]
topics: []
related: [Bagwell2007, Mayzlin2014, Milgrom1986, Nelson1970]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper considers a model of informative advertising that allows firms to jam the consumers' signals on product quality before choosing prices at a second stage. We find that the price competition at the second stage may overrule the basic insights from the signal-jamming approach in other areas of application. As a consequence, a firm may advertise more intensely the higher is the difference of the expected product qualities. Moreover, a firm's optimal advertising intensity can decrease with quality uncertainty.

## Summary
Grunewald and Kräkel build a two-stage duopoly model of "complex experience goods" (drugs, computers, mobile phones) where neither firms nor consumers know consumption quality ex ante, and where firms can spend on advertising to *jam* the noisy quality signals consumers receive before prices are set. Because advertising is followed by vertically-differentiated price competition à la Shaked–Sutton (1982), the standard signal-jamming intuitions from career-concerns and capital-market models break down. The model delivers two surprising results: the firm with higher expected quality advertises *more* as the expected-quality gap widens (a new rationale for the Nelson positive advertising–quality correlation), and optimal advertising intensity can *decrease* in quality uncertainty—the opposite of the classic signal-jamming prediction.

## Research question
How do firms' optimal advertising intensities for complex experience goods depend on (i) the degree of vertical product differentiation (the gap in expected qualities) and (ii) the degree of consumption-quality uncertainty, once advertising-as-signal-jamming is embedded in a market with downstream price competition rather than a single-stage setting?

## Method / identification
A two-stage game between profit-maximizing firms $A$ and $B$ selling vertically differentiated goods of uncertain consumption quality $q_i$. Neither firms nor consumers know $q_i$; it arises from the match between the good's features and consumer tastes. Priors are normal, $q_i\sim N(\bar q_{i0},\sigma_{i0}^2)$ with $\bar q_{i0}>0$.

**Stage 1 (advertising).** Each firm picks intensity $a_i\ge 0$. Advertising triggers two imperfect signals: with probability $\gamma(a_i)$ a consumer sees firm $i$'s ad (with $\gamma(0)=0$, $\gamma'>0$), and consumers observe an additive quality signal
$$s_i = q_i + a_i + \varepsilon_i,\qquad \varepsilon_i\sim N(0,\sigma_\varepsilon^2),$$
where advertising $a_i$ biases the signal upward (the jamming channel). Advertising costs $c(a_i)$ are convex ($c(0)=c'(0)=0$, $c',c''>0$); a reduced-form benefit $h(a_i)$ (brand awareness/reputation) satisfies an Inada condition ($\lim_{a_i\to0}h'=\infty$, $h''<0$) that rules out zero-advertising boundary equilibria.

**Bayesian updating.** Consumers do not observe the RHS of the signal equation but use $s_i$ and their degenerate equilibrium belief $\hat a_i$ to update. Posterior mean and variance are
$$\bar q_{i1}=\bar q_{i0}+\Sigma_i\,(s_i-\hat a_i-\bar q_{i0}),\qquad \sigma_{i1}^2=\Sigma_i\sigma_\varepsilon^2,\qquad \Sigma_i:=\frac{\sigma_{i0}^2}{\sigma_\varepsilon^2+\sigma_{i0}^2}.$$
$\Sigma_i$ is the updating weight; it rises with prior uncertainty $\sigma_{i0}^2$ and with signal precision $1/\sigma_\varepsilon^2$.

**Stage 2 (prices).** A simplified Shaked–Sutton (1982) vertical-differentiation game: full market coverage, unit mass of consumers of type $\theta\sim U[\underline\theta,\bar\theta]$ with $\bar\theta=\underline\theta+1$, utility $\theta q_i-p_i$. If $\bar q_{i1}>\bar q_{j1}$, equilibrium stage-2 profits are $\pi_i^*=\bar\Theta(\bar q_{i1}-\bar q_{j1})$, $\pi_j^*=\underline\Theta(\bar q_{i1}-\bar q_{j1})$ with $\bar\Theta:=(2\bar\theta-\underline\theta)^2/9>\underline\Theta:=(\bar\theta-2\underline\theta)^2/9$. Both firms gain from product differentiation since it relaxes price competition.

**Solution concept.** Pure-strategy Perfect Bayesian Equilibrium with *passive beliefs* (quality beliefs do not depend on observed prices), solved by backward induction. Two regimes are analyzed: high consumer heterogeneity ($\bar\theta\ge 2\underline\theta$) and low heterogeneity ($\bar\theta<2\underline\theta$, a winner-take-all stage-2 outcome where the higher-quality firm captures the whole market and $\pi_j^*=0$).

## Data
None — this is a pure theory paper. The authors motivate the setting with empirical references (Crawford and Shum, 2005; [[@Mayzlin2014|Mayzlin et al., 2014]] on online-review manipulation) but estimate nothing.

## Key findings
- **Lemma 1:** in any positive-advertising PBE with passive beliefs, consumers' beliefs about advertising intensities are degenerate, and both advertising and quality beliefs are homogeneous across consumers.
- **Propositions 1–2:** a unique interior pure-strategy equilibrium exists under a concavity condition (6); the Inada condition on $h$ rules out boundary (zero-advertising) equilibria, so attention to interior equilibria is without loss. Optimal intensities solve the first-order condition (7) involving $\Sigma_i$, $\bar\Theta$, $\underline\Theta$ and the likelihood $G_i(\Omega_i)$ that the rival offers the higher-quality good.
- **Corollary 1:** $a_i^*$ increases in own prior quality $\bar q_{i0}$ and decreases in the rival's $\bar q_{j0}$. The firm likely to be "strong" at stage 2 advertises more (to enlarge the posterior quality spread and its profit); the likely "weak" firm advertises less (to preserve differentiation and avoid sharpening competition). This yields a new rationale for the [[@Nelson1970|Nelson]] (1970, 1974) positive advertising–quality correlation, and contrasts sharply with Holmström (1999) (prior ability does not affect jamming effort) and Höffler and Sliwka (2003) (both contestants' efforts fall in the prior-ability gap).
- **Proposition 3:** $a_i^*$ can *decrease* in quality uncertainty $\sigma_{i0}^2$. Two forces compete: the **signal-jamming effect** (higher $\Sigma_i$ makes advertising shift more posterior mass upward, raising intensity) versus the new **likelihood effect** (higher $\sigma_{i0}^2$ raises the probability of being in the weak stage-2 position, where own advertising is harmful). Condition (9) gives exactly when the likelihood effect dominates; a necessary condition is $\bar q_{i0}>\bar q_{j0}$—only the ex-ante leader can be discouraged, because exogenous luck erodes its lead, whereas a laggard is brought "back into the race."

## Contribution
The paper shows that the central insights of the signal-jamming literature (Holmström 1999; Stein 1989; Meyer and Vickers 1997; Höffler and Sliwka 2003) hinge on single-stage, no-competition settings and do not survive when jamming is followed by oligopolistic price competition. It provides a tractable, normal-Bayesian model of advertising for complex experience goods, generates a novel mechanism behind the advertising–quality correlation, and identifies the "likelihood effect" that can reverse the standard uncertainty–advertising comparative static.

## Limitations & open questions
The authors flag several extensions explicitly: (1) combine signal-jamming (unobservable) advertising with *observable* signaling advertising to study how product features allocate a firm's spend across the two forms and the welfare consequences; (2) endogenize *product quality choice*—the model may predict that ex-ante identical firms adopt asymmetric strategies (one high-quality/heavy-advertising, one low-quality/no-advertising) to benefit from differentiation; (3) analyze consumer-surplus and welfare implications, since advertising raises costs passed to consumers but also reshapes (potentially softens) price competition. The model also relies on normality, passive beliefs, full market coverage, fixed total demand, and statistically independent shocks.

## Connections
The signal-jamming machinery descends from Holmström (1999) on career concerns and Höffler and Sliwka (2003) on jamming tournaments, with antecedents in Riordan (1985), Stein (1989), Meyer and Vickers (1997), Fudenberg and Tirole (1986), and Caminal and Vives (1996); the authors' own Grunewald and Kräkel (2014) treats non-Bayesian consumer beliefs. On informative advertising of experience goods the paper builds on [[@Nelson1970|Nelson]] (1970, 1974) and the signaling tradition of [[@Milgrom1986|Milgrom and Roberts (1986)]], Fluet and Garella (2002), and Linnemer (2002, 2012), as well as the match-information strand of Lewis and Sappington (1994), Meurer and Stahl (1994), and Anderson and Renault (2009). The stage-2 vertical-differentiation game is Shaked and Sutton (1982). Closely related signal-jamming-as-advertising work includes Bar-Isaac and Deb (2014) and Drugov and Troya-Martínez (2015); Miklós-Thal and Ullrich (2015) similarly find competition can reverse signal-jamming intuitions in a one-stage tournament. Surveys by [[@Bagwell2007|Bagwell (2007)]] and Renault (2016) situate the broader advertising literature.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
