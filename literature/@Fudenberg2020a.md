---
citekey: Fudenberg2020a
title: Predicting Cooperation with Learning Models
authors: ["Fudenberg, Drew", "Karreskog, Gustav"]
year: 2020
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/IAWJUMXF"
pdf: /Users/jesper/Zotero/storage/9PTI7GRE/Fudenberg2020b_appendix.pdf
tags: [literature]
keywords: [repeated-prisoners-dilemma, reinforcement-learning, cooperation, out-of-sample-prediction, risk-dominance, semi-grim-strategies]
topics: []
related: [Andrews2022, Fudenberg2019a, Fudenberg2022]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> (no abstract in Zotero) — From the paper: We use simulations of a simple learning model to predict cooperation rates in the experimental play of the indefinitely repeated prisoner's dilemma. We suppose that learning and the game parameters only influence play in the initial round of each supergame, and that after these rounds play depends only on the outcome of the previous round. We find that our model predicts out-of-sample cooperation at least as well as models with more parameters and harder-to-interpret machine learning algorithms. Our results let us predict the effect of session length and help explain past findings on the role of strategic uncertainty.

## Summary
Fudenberg and Karreskog reframe the question "how much do people cooperate in the indefinitely repeated prisoner's dilemma?" as an *out-of-sample prediction* problem rather than an in-sample fitting exercise. They estimate a deliberately spare 6-parameter reinforcement-learning model (IRL-SG) in which treatment and personal experience affect *only* the probability of cooperating in the first round of each supergame; all subsequent play follows a fixed "semi-grim" memory-1 mixed strategy. Calibrated by simulation against a meta-analytic dataset (161 sessions, 17 papers), the model predicts both average cooperation and the time path of cooperation at least as well as Lasso, SVR, and gradient-boosted trees, and clearly *beats* them when extrapolating to unseen treatments or to longer sessions. The key economic message: the dominant driver of cooperation rates is initial-round play, which is reinforced positively when the composite risk-dominance parameter $\Delta_{RD}>0.15$ and negatively when $\Delta_{RD}<0$.

## Research question
Can a simple, interpretable learning model predict the *average* cooperation rate (and its time path) in an indefinitely repeated PD session *before the session is run*, using only the game parameters and the sequence/length of supergames — without conditioning on any of the actual play in that session? And does such a structured model generalize (across treatments and to longer horizons) better than flexible model-free machine learning?

## Method / identification
The PD has payoffs parameterized by the gain to defection against a cooperator $g$ and the loss from cooperating against a defector $l$ (with $g,l>0$, $g<l+1$), and a continuation probability / discount factor $\delta$. Two thresholds matter: the SPE threshold $\delta^{SPE}=g/(1+g)$ (Grim is a SPE iff $\delta\geq\delta^{SPE}$), and the risk-dominance threshold $\delta^{RD}=(g+l)/(1+g+l)$ from Blonski, Ockenfels & Spagnolo (2011). The central regressor is the composite

$$\Delta_{RD}\equiv \delta-\delta^{RD}=\delta-\frac{g+l}{1+g+l}.$$

The **IRL-SG** ("initial-round learning with semi-grim strategies") model assumes every agent uses a memory-1 strategy and that treatments/experience shift only the initial-round cooperation probability:

$$p_i^{\text{initial}}(s)=\frac{1}{1+\exp\!\big(-(\alpha+\beta\cdot\Delta_{RD}+e_i(s))\big)},$$

with experience reinforced across supergames by

$$e_i(s)=\lambda\cdot a_i(s-1)\cdot V_i(s-1)+e_i(s-1),$$

where $a_i(s)=+1$ if $i$ cooperated in the initial round of supergame $s$ and $-1$ otherwise, $V_i(s)$ is the total supergame payoff, $\lambda$ is the learning rate, and $e_i(1)=0$. Non-initial play is a *fixed* semi-grim mixed strategy with $\sigma_{CC}>\sigma_{DC}=\sigma_{CD}>\sigma_{DD}$ (following Breitmoser 2015). Total parameters: $(\alpha,\beta,\lambda,\sigma_{CC},\sigma_{CD/DC},\sigma_{DD})$ — six.

Because no closed form exists for the cooperation time paths, the model is calibrated by **simulation**: a large population is randomly rematched to play exactly the supergame sequence/lengths of a session, updating $e_i(s)$ via the equation above using only simulated (never observed) actions and payoffs. Parameters minimize the MSE between simulated and training-set time paths. Performance is the **cross-validated MSE** (standard 10-fold, split at the session level, repeated 10 times with bootstrapped standard errors), benchmarked against a constant predictor and against OLS-on-$\Delta_{RD}$, Lasso, SVR, and GBT. The completeness-style benchmark of [[@Fudenberg2022|Fudenberg, Kleinberg, Liang & Mullainathan (2022)]] inspires the relative-improvement reporting.

## Data
A meta-analysis built on Dal Bó & Fréchette (2018), augmented with four post-2015 papers (Aoyagi–Bhaskar–Fréchette 2019; Dal Bó–Fréchette 2019; Honhon–Hyndman 2020; Proto–Rustichini–Sofianos 2019). Final dataset: **17 papers, 28 treatments, 161 incentivized lab sessions, 2,612 participants, 232,298 individual choices** (all perfect-monitoring, deterministic-payoff PDs with $\delta>0$). Discount factors range 0.125–0.95; median session has average realized supergame length 6.7 rounds. Average cooperation is 44.1% overall — 10.5% when $\delta<\delta^{SPE}$, 18.6% for $\delta^{SPE}<\delta<\delta^{RD}$, and 53.6% for $\delta>\delta^{RD}$. Conditional cooperation by memory-1 history: CC 96.6%, CD 30.6%, DC 33.2%, DD 5.2%, initial 47.1% — closely matching the semi-grim restriction.

## Key findings
- **In-domain prediction (average cooperation).** IRL-SG attains MSE 0.0138 (73.3% improvement over the constant), edging out the best ML method (Lasso, 0.0143) and beating OLS-on-$\Delta_{RD}$ (0.0189, 63.4%). For the **time path**, IRL-SG MSE is 0.0309 (60.1%) vs best ML (GBT) 0.0316 and OLS 0.0398.
- **Across-treatment extrapolation.** Holding out entire $\Delta_{RD}$-groups, IRL-SG (MSE 0.0177, 80.0% improvement) is *significantly* better than the best ML (SVR, 0.0235) — most model-free methods even fall below OLS-on-$\Delta_{RD}$. This echoes [[@Andrews2022|Andrews, Fudenberg, Liang & Wu (2022)]]: structured models extrapolate better.
- **Session-length extrapolation.** Trained on first halves, IRL-SG predicts second halves with MSE 0.0220 vs GBT 0.0254 and OLS 0.0281 — significantly better.
- **Parameter estimates.** $\alpha=-0.268$ (so $\sim$43.3% first-round cooperation at $\Delta_{RD}=0$), $\beta=1.291$, $\lambda=0.182$ (strong learning), $\sigma_{CC}=0.995$, $\sigma_{CD/DC}=0.355$, $\sigma_{DD}=0.012$. A Shapley decomposition attributes $\approx$88% of last-supergame cross-treatment variation to *learning* rather than the direct parameter effect.
- **Mechanism.** Defection is reinforced more than cooperation when $\Delta_{RD}<0$; the reinforcement gap $\pi(C)-\pi(D)$ is centered at 0 for $0<\Delta_{RD}<0.15$ (explaining flat time trends), and favors cooperation for high $\Delta_{RD}$. The model reproduces "longer-than-expected supergames raise cooperation" because the reward to initial $C$ grows with realized length.
- **Composition of $\Delta_{RD}$ matters.** Treatments with the same $\Delta_{RD}$ but different $(g,l)$ yield different predicted cooperation — explaining why IRL-SG beats OLS-on-$\Delta_{RD}$.
- **Endogenous heterogeneity & long-run variance.** Identical learners diverge purely from random initial play and matching; this can rationalize persistent defectors even in cooperation-friendly games. For intermediate $\Delta_{RD}$, cross-session variance stays large even after 10,000 supergames (e.g. at $\Delta_{RD}=0.11$ the 90% interval is 0%–79% with 16 agents).
- **No gains from complexity.** Adding agent heterogeneity (two types), dropping the semi-grim restriction, or allowing learning at all memory-1 histories yields at most marginal improvement; pure-strategy learning models (belief learning à la Dal Bó–Fréchette 2011, or reinforcement over AllD/Grim/TFT) are significantly *worse*.

## Contribution
The paper shows that a single-type, 6-parameter reinforcement-learning model with fixed non-initial play is *complete enough* to predict aggregate cooperation as well as flexible ML — and strictly better out of domain and over longer horizons. It thereby (i) provides a portable predictive tool usable before an experiment, (ii) gives a behavioral micro-foundation for why $\Delta_{RD}$ predicts cooperation (reinforcement of initial-round actions), (iii) demonstrates that the composite parameter is *not sufficient* — the individual $g,l$ matter — and (iv) cautions that small-sample PD studies with intermediate $\Delta_{RD}$ are inherently high-variance.

## Limitations & open questions
- The analysis is confined to the **perfect-monitoring** PD; with implementation errors or imperfect monitoring, players use longer-memory strategies, and there are "not yet enough experimental studies" to test whether $\Delta_{RD}$ matters or to support this kind of analysis — an explicit invitation for future work once data accrue.
- The model is acknowledged as an **oversimplification** (single learning rule, no closed-form solution; calibration relies on simulation).
- **Demographic/individual covariates are absent**: the authors note heterogeneity gains "might be larger if we had demographic information," citing Proto et al. (2019) on group intelligence — a hook for richer heterogeneous-learning models.
- Predicting the **next individual action** (Online Appendix D/E) needs session data and so cannot serve the out-of-sample task; reconciling within-session prediction with pre-experiment prediction is open.
- The composition-of-$\Delta_{RD}$ effects (role of $g-l$) are predicted but "there is not enough data to directly test" them.
- Irreducible error cannot be estimated (insufficient data for a true completeness measure à la Fudenberg et al. 2022), so how far IRL-SG is from optimal is unknown.

## Connections
Builds directly on the risk-dominance literature for repeated games: Blonski, Ockenfels & Spagnolo (2011), Blonski & Spagnolo (2015), and Chassang (2010), which motivate $\Delta_{RD}$. Empirically it sits atop the Dal Bó & Fréchette (2011, 2018) meta-analytic program and Dal Bó (2005). The semi-grim memory-1 specification comes from Breitmoser (2015), extended by Backhaus & Breitmoser (2018); the additive reinforcement form follows Erev & Roth (1998), with belief-learning and EWA antecedents in Camerer & Ho (1999) and Cheung & Friedman (1997). Methodologically it is part of Fudenberg's "economics as prediction" agenda — [[@Fudenberg2019a|Fudenberg & Liang (2019)]] on predicting initial play, Fudenberg, Kleinberg, Liang & Mullainathan (2022) on completeness, and Andrews, Fudenberg, Liang & Wu (2022) on structured models extrapolating better than ML — and relates to Wright & Leyton-Brown (2017). Mengel, Orlandi & Weidenholzer (2022) on the outsized effect of early realized supergame lengths is both a data source and a competing learning specification.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
