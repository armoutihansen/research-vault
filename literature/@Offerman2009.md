---
citekey: Offerman2009
title: "A truth serum for non-bayesians: Correcting proper scoring rules for risk attitudes"
authors: ["Offerman, Theo", "Sonnemans, Joep", "Van De Kuilen, Gijs", "Wakker, Peter P."]
year: 2009
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/2T5FE538"
pdf: /Users/jesper/Zotero/storage/YBGZ53VR/Offerman et al. - 2009 - A truth serum for non-bayesians Correcting proper scoring rules for risk attitudes.pdf
tags: [literature]
keywords: [proper-scoring-rules, belief-elicitation, risk-attitudes, ambiguity, non-expected-utility, incentive-compatibility, subjective-probability]
topics: ["[[experimental-belief-elicitation]]"]
related: [Gneiting2007]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> Proper scoring rules provide convenient and highly efficient tools for incentive-compatible elicitations of subjective beliefs. As traditionally used, however, they are valid only under expected value maximization. This paper shows how they can be generalized to modern ("non-expected utility") theories of risk and ambiguity, yielding mutual benefits: users of scoring rules can benefit from the empirical realism of non-expected utility, and analysts of ambiguity attitudes can benefit from efficient measurements using proper scoring rules. An experiment demonstrates the feasibility of our generalization.

## Summary
Proper scoring rules (Brier, 1950; Good, 1952) are the workhorse mechanism for incentive-compatible **belief elicitation**: a single choice pins down an agent's quantitative degree of belief in an event. But their classical justification assumes the agent maximizes expected *value* (risk neutrality). Since risk aversion, probability weighting, and ambiguity attitudes are pervasive, the reported number $r$ is generally **not** the agent's subjective probability $p$. This paper diagnoses how large that distortion is and supplies a tractable correction. The core payoff is a single observable mapping — the **risk correction** — recovered from each subject's choices over scoring-rule prospects with *known* objective probabilities; inverting it converts any subsequently reported $r$ into a corrected subjective belief. The construction is doubly useful: it rescues scoring-rule belief measurement from the risk-neutrality assumption, and it gives ambiguity researchers an efficient instrument (one choice per event) in place of the laborious binary-preference ladders traditionally needed to measure non-expected-utility parameters.

## Research question
Under modern (rank-dependent / non-expected-utility) theories of decision under risk and ambiguity, what value $r$ does an agent optimally report in a proper scoring rule, and how can one **invert** the observed report to recover the true subjective belief — correcting for risk attitude, probability weighting, and ambiguity attitude — using only a feasible, behaviorally observable calibration?

## Method / identification
The instrument is the **quadratic scoring rule (QSR)**: for an event $E$ the agent chooses $r\in[0,1]$ and receives the prospect
$$\big(1-(1-r)^2\big)_E\,\big(1-r^2\big),$$
i.e. payoff $1-(1-r)^2$ if $E$ obtains and $1-r^2$ otherwise. Under expected value the optimum is the truth, $r=p$ (Corollary 1, reproducing Brier). The paper instead evaluates the prospect under the **general (rank-dependent) model**, where an event weight $W(E)$ and a utility $U$ replace probability and linear value. The first-order condition gives the central optimality characterization:

> **Theorem 1.** For $r>0.5$ the optimal report satisfies
> $$r=r_E=\frac{W(E)\,U'(1-r^2)}{W(E)\,U'(1-r^2)+(1-W(E))\,U'(1-(1-r)^2)},$$
> with the $r<0.5$ case following from a QSR symmetry (Observation 1) applied to $E^c$.

So $r_E$ is distorted by the **marginal-utility ratio** (the risk-attitude channel) and by the **weighting function** $W$ (probability-weighting / ambiguity channel). Identification runs *backwards*: rather than assuming a parametric model to predict choices, the authors use observed choices on **objective-probability** prospects to estimate the agent's reporting map $R(p)$. Its inverse $R^{-1}$ is the **risk correction**: applied to any report $r$ over a subjective event, $R^{-1}(r)$ yields the corrected subjective probability. The headline practical result, **Corollary 4**, shows the correction needs only this observable curve and holds for *general* proper scoring rules, so practitioners can skip the decision-theoretic derivations and apply one calibration. Aggregate estimation fits utility-curvature parameters $\alpha$ and weighting parameters $\beta$ by maximum likelihood across treatments, with nested likelihood-ratio tests on restrictions such as $\alpha=1$ (linear utility) and $\beta=1$ (no weighting).

## Data
Original lab experiment. $N=93$ students (45 economics, 13 psychology, 35 other) across the two main treatments, run in six groups of ~16 at computers; four subjects with implausible reports were dropped (89 retained). A separate control treatment $t=\text{ALLnp}$ (no use of the word "probability") had $N=44$. Each subject completed a **stock-price part** — judging whether each of several stocks would rise/fall over six months given a price chart, with the evaluation date (1 June 1991) chosen far in the past so subjects could not recognize stocks — and a **calibration part** with 20 objective-probability events ($p=0.05,0.10,\dots,0.95$) resolved by two ten-sided dice. The QSR paid 10,000 points per question for four-digit score precision; ALL paid every decision, ONE paid one randomly selected decision.

## Key findings
1. **Reports systematically deviate from beliefs.** The calibration curves $R(p)$ are clearly non-identity, confirming that uncorrected scoring-rule reports conflate belief with risk/weighting attitudes; restrictions $\alpha=1,\beta=1$ are rejected at the 1% level.
2. **The risk correction works.** Inverting the observed calibration curve substantially reduces the gap between reported and true probabilities; for most subjects a simple quadratic fit $p=a+br+cr^2$ is virtually indistinguishable from the decision-theoretic curve, making the correction trivially applicable (supports Corollary 4).
3. **Beliefs are genuinely non-additive.** The **additivity bias** (the extent to which reported probabilities of complementary events fail to sum to one) is reduced by the correction — risk-corrected average additivity bias ~0.126 vs. ~0.136 uncorrected — but *not eliminated*. Residual non-additivity is attributed to genuine **ambiguity attitudes**, not measurement artifact.
4. **Payment protocol affects curvature.** $\beta_{\text{ONE}}<\beta_{\text{ALL}}$: paying only one decision induces more concave (risk-averse) utility curvature than paying all decisions — a methodological caution for incentive design.

## Contribution
Provides the first incentive-compatible foundation for proper scoring rules under modern non-expected-utility theory, turning a 1950s expected-value tool into a "truth serum for non-Bayesians." It delivers (i) a theoretical optimality characterization (Theorem 1) showing precisely which distortions enter, (ii) a practitioner-ready, model-light correction (Corollary 4) needing only an objective-probability calibration, and (iii) experimental proof of feasibility. Conversely it hands ambiguity researchers a far more efficient elicitation instrument than binary-preference methods.

## Limitations & open questions
- The correction **reduces but does not eliminate** additivity violations; cleanly separating genuine non-additive belief from residual measurement error remains open.
- The empirical analysis exploits structure only on $[0.5,1]$; behavior on $[0,0.5]$ (where probability weighting is empirically least settled, mixing under- and overweighting) is set aside (Observation A2), leaving the full-domain correction less validated.
- Validity rests on subjects having no private information about the (disguised, historical) stocks; external validity to settings with real expertise or stakes is untested.
- The protocol-dependence of estimated curvature ($\beta_{\text{ONE}}\ne\beta_{\text{ALL}}$) flags an unresolved interaction between payment mechanism and the very risk attitudes being corrected for.
- Whether the calibration transports across domains/time for a given agent (stability of the risk correction) is not established.

## Connections
The decision-theoretic backbone is **rank-dependent utility** (Quiggin, 1982) and **Choquet expected utility / probabilistic sophistication** for ambiguity (Schmeidler, 1989), with **cumulative prospect theory** (Tversky & Kahneman, 1992) supplying inverse-S weighting; objective probability is treated as a limiting subjective case (Machina, 2004; Wakker, 2009). It builds on the classical proper-scoring-rule literature (Brier, 1950; Good, 1952; Savage, 1971) and early warnings about risk aversion in scoring rules (Winkler & Murphy, 1970; Johnstone, 2007a,b). On elicitation it complements survey-based belief measurement (Manski, 2004), experimental scoring-rule use (Nyarko & Schotter, 2002; McKelvey & Page, 1990), prediction markets (Wolfers & Zitzewitz, 2004), and the Bayesian truth serum (Prelec, 2004). Probability-weighting estimates connect to Gonzalez & Wu (1999), Abdellaoui (2000), and Bleichrodt & Pinto (2000); the general statistical theory is unified by [[@Gneiting2007|Gneiting & Raftery (2007)]]; the ambiguity motivation traces to Ellsberg (1961), Knight (1921), and Keynes (1921).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
