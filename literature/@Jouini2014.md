---
citekey: Jouini2014
title: On Portfolio Choice with Savoring and Disappointment
authors: ["Jouini, Elyès", "Karehnke, Paul", "Napp, Clotilde"]
year: 2014
type: journalArticle
doi: 10.1287/mnsc.2013.1767
zotero: "zotero://select/library/items/QE8DTGMI"
pdf: /Users/jesper/Zotero/storage/LTAW59JF/Jouini2014.pdf
tags: [literature]
keywords: [endogenous-beliefs, anticipatory-feelings, disappointment-aversion, portfolio-choice, skewness-preference, savoring]
topics: []
related: [Akerlof1982, Bell1985, Brunnermeier2005, Brunnermeier2007, Caplin2001, Gollier2010, Gul1991, Loomes1986]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We revisit the model proposed by Gollier and Muermann [Gollier C, Muermann A (2010) Optimal choice and beliefs with ex ante savoring and ex post disappointment. Management Sci. 56(8):1272–1284; hereafter, GM]. In the GM model, for a given lottery, agents form anticipated expected payoffs and the set of possible anticipations is assumed to be exogenously fixed. We propose sets of possible anticipations that are endogenously determined. This permits us to compare and evaluate in a consistent manner lotteries with different supports and to revisit the portfolio choice problem. We obtain new conclusions and interesting insights. Our extended model can rationalize a variety of empirically observed puzzles such as a positive demand for assets with negative expected returns, preference for skewed returns, and underdiversification of portfolios. This paper was accepted by Rakesh Sarin, decision analysis.

## Summary
The paper revisits the [[@Gollier2010|Gollier–Muermann (2010)]] "savoring and disappointment" model of endogenous belief formation. In GM, an agent picks an *anticipated expected payoff* $y$ that trades off ex-ante savoring (pleasure from optimistic dreams) against ex-post disappointment, but the admissible set of anticipations is fixed *exogenously*. Jouini, Karehnke and Napp instead tie the feasible set of anticipations to the lottery's own support: you can only believe an outcome is possible if it actually is. This single change — feasible subjective beliefs must be absolutely continuous with respect to the objective distribution — makes the criterion comparable across lotteries with different supports and produces a "support effect" in portfolio choice. The extended model rationalizes several puzzles (positive demand for negative-mean assets, preference for skewness, under-diversification, simultaneous insurance and gambling) but, as a cost, can violate first- and second-degree stochastic dominance unless an extra condition on the relative weight of savoring is imposed.

## Research question
Can the structural savoring/disappointment model of endogenous beliefs be made internally consistent across lotteries with *different* supports, and what new conclusions for portfolio choice follow once the set of admissible anticipations is determined endogenously by the lottery rather than fixed exogenously?

## Method / identification
This is a theoretical decision-theory and portfolio-choice paper; no data. The agent's intertemporal welfare is a weighted sum of an ex-ante (savoring) term evaluated at a subjectively anticipated expected payoff $y$ and an ex-post (disappointment) term evaluated at the realized payoff relative to $y$. Writing $U(c,y)$ for the felicity of payoff $c$ under anticipation $y$, the agent chooses $y$ to maximize a functional $F(x,y)$ aggregating savoring and disappointment, with $k$ the intensity (weight) of anticipatory feelings.

The key departure from GM: feasible subjective probability distributions are required to be absolutely continuous with respect to the objective distribution $Q$. Operationally, for a lottery with support $[x_{\min},x_{\max}]$, the only admissible anticipated expected payoffs are those attainable by reweighting the *existing* outcomes — so $y$ must lie within the convex hull of the support and cannot fall outside it. Under no uncertainty (a sure payoff), the only admissible anticipation is that sure payoff itself: "if there is no uncertainty, then there is nothing to dream or to be disappointed about." Two structural consequences follow: (i) welfare is invariant to adding zero-probability outcomes to the support, and (ii) in the portfolio problem the range of admissible anticipations is not bounded by exogenous constants but expands endogenously with the investment $\alpha$ in the risky asset, since $\alpha$ stretches the support of payoffs.

The portfolio problem maximizes welfare over the position $\alpha$ in a risky asset $\tilde{x}$ given initial wealth $z$. Comparative statics are derived via the cross-partials of $U$ and $F$. A central regularity condition is $F_y(x,x)\ge 0$ for all $x$, interpreted as "savoring weight high enough relative to disappointment." The habit-formation specification $U(c,y)=u(c-\eta y)$ is used as a worked case, where $F_y(x,x)\ge 0$ holds iff $k\ge \frac{\eta}{1-\eta}$.

## Data
None — purely theoretical (decision theory / portfolio choice). Empirical "puzzles" (state-lottery demand, skewness preference, under-diversification, Friedman–Savage insurance-plus-gambling) are cited from the literature as targets the model rationalizes, not as data analyzed here.

## Key findings
- **Proposition 3.1.** If $U_{yc}>0$ (disappointment aversion; automatically satisfied under habit formation $U(c,y)=u(c-\eta y)$), then any FSD-dominated shift in $Q$ weakly reduces the optimal anticipated payoff $y^{*}$. This is the *only* GM stochastic-dominance result that survives the endogenous-support change.
- **Failure of stochastic dominance.** In general the preference functional need not respect first- or second-degree stochastic dominance: enlarging risk widens the support, admitting a more favorable savoring/disappointment trade-off and possibly higher welfare. Appendix counterexamples are provided.
- **Proposition 3.2 (internality).** The following are equivalent: (1) $W$ satisfies the internality requirement (binary-lottery welfare lies between its worst and best outcomes); (2) $F_y(x,x)\ge 0$ for all $x$; (3) any FSD-dominated shift weakly reduces welfare. Pure disappointment models violate internality (per Gneezy, List and Wu, 2006); the condition restores FSD compatibility.
- **Proposition 3.3 (negative-mean demand).** For a bounded, nonzero, zero-mean risk $\tilde{x}$ with $F_y(z,z)\neq 0$, the optimal investment $\alpha^{*}$ is nonzero. Perturbations then yield negative-mean risks with positive demand — rationalizing demand for state lotteries and lottery-type stocks.
- **Comparative statics on savoring.** As in GM, $\partial y^{*}/\partial k \ge 0$ (more anticipatory feeling biases beliefs toward optimism). But unlike GM — where stronger savoring raised risk aversion and *cut* the risky allocation — here a *support effect* can outweigh the risk-aversion effect, so the risky allocation may *increase* with the savoring weight.
- **Rationalized puzzles.** Preference for skewed returns (à la [[@Brunnermeier2007|Brunnermeier et al., 2007]]), portfolio under-diversification (Mitton and Vorkink, 2007), and simultaneous demand for insurance and lotteries (the Friedman–Savage puzzle), consistent with Lopes' hope/fear theory and Shefrin–Statman behavioral portfolio theory.

## Contribution
The paper supplies a decision criterion that extends GM to lotteries with heterogeneous supports by endogenizing the admissible-anticipation set through absolute continuity. Where the supports of GM's exogenous set and the objective distribution coincide it is a genuine extension; otherwise it is a *modification* yielding different welfare levels. The reframing delivers a "support effect" absent in GM and lets a single savoring/disappointment mechanism jointly rationalize negative-mean asset demand, skewness preference, under-diversification, and the insurance-plus-gambling puzzle.

## Limitations & open questions
- **Stochastic dominance is not automatic.** The criterion can violate FSD/SSD; consistency requires the extra restriction $F_y(x,x)\ge 0$. Characterizing the full class of preferences and parameter regions where dominance holds is left partly open (developed via counterexamples in the appendix rather than a complete taxonomy).
- **Reference-point dependence.** The model is stated to be consistent with both certainty-equivalent reference points (Gul, 1991) and expected-payoff reference points (Bell, 1985; Loomes and Sugden, 1986); which is empirically appropriate is not resolved.
- **Absolute-continuity assumption.** Restricting beliefs to be absolutely continuous w.r.t. the objective distribution is a modeling choice; GM's singular-belief case is excluded, and the boundary between "extension" and "modification" of GM depends on whether GM's set $C$ matches the objective support.
- **No empirical or experimental test.** The puzzles are rationalized qualitatively; calibration and structural estimation of $k$, $\eta$, and the savoring/disappointment weights are not attempted.

## Connections
The paper is a direct response to [[@Gollier2010|Gollier and Muermann (2010)]] and inherits the "optimal expectations / optimal beliefs" approach of [[@Brunnermeier2005|Brunnermeier and Parker (2005)]] and [[@Brunnermeier2007|Brunnermeier, Gollier and Parker (2007)]], tracing endogenous-belief modeling to [[@Akerlof1982|Akerlof and Dickens (1982)]]. The disappointment building blocks are [[@Bell1985|Bell (1985)]], [[@Loomes1986|Loomes and Sugden (1986)]], and [[@Gul1991|Gul (1991)]], with anticipatory-feelings utility from [[@Caplin2001|Caplin and Leahy (2001)]]. The internality/uncertainty-effect critique draws on Gneezy, List and Wu (2006). Portfolio and puzzle connections include Friedman and Savage (1948) on insurance-plus-gambling, Lopes (1987) on hope and fear, Shefrin and Statman (2000) behavioral portfolio theory, Mitton and Vorkink (2007) on skewness and under-diversification, Kumar (2009) and Bali, Cakici and Whitelaw (2011) on lottery-type stocks, and Constantinides (1990) for the habit-formation specification.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
