---
citekey: Koszegi2007
title: Reference-Dependent Risk Attitudes
authors: ["Kőszegi, Botond", "Rabin, Matthew"]
year: 2007
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/XGM3AWCR"
pdf: /Users/jesper/Zotero/storage/KXFG2CUL/Koszegi2007.pdf
tags: [literature]
keywords: [reference-dependent-utility, expectations-based-reference-point, loss-aversion, first-order-risk-aversion, prospect-theory, personal-equilibrium]
topics: []
related: [Bell1985, Gul1991, Kahneman1979, Koszegi2006b, Loomes1986, Shalev2000]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We use Kőszegi and Rabin's (2006) model of reference-dependent utility, and an extension of it that applies to decisions with delayed consequences, to study preferences over monetary risk. Because our theory equates the reference point with recent probabilistic beliefs about outcomes, it predicts specific ways in which the environment influences attitudes toward modest-scale risk. It replicates "classical" prospect theory--including the prediction of distaste for insuring losses-when exposure to risk is a surprise, but implies first-order risk aversion when a risk, and the possibility of insuring it, are anticipated. A prior expectation to take on risk decreases aversion to both the anticipated and additional risk. For large-scale risk, the model allows for standard "consumption utility" to dominate reference-dependent "gain-loss utility," generating nearly identical risk aversion across situations.

## Summary
Kőszegi and Rabin apply their expectations-based reference-dependent utility model to monetary risk. Because the reference point is the agent's recent probabilistic beliefs about outcomes, risk attitudes become endogenous to the environment: the same preferences generate "classical" prospect-theory behavior for surprise risks but first-order risk aversion when risk and insurance are anticipated, and they predict that prior expectation of risk reduces risk aversion. For large stakes, consumption utility dominates and behavior reverts to near-standard expected utility, reconciling wildly different measured risk-aversion coefficients across scales.

## Research question
How do reference-dependent preferences—when the reference point is endogenously fixed by recent rational expectations rather than the status quo—shape attitudes toward monetary risk, and can a single preference specification unify the seemingly contradictory risk attitudes (prospect-theory loss-seeking, insurance demand, the disposition effect, the endowment effect for risk, and standard large-stakes risk aversion) observed across domains?

## Method / identification
The paper is theoretical. Utility over a wealth outcome $w$ relative to a riskless reference level $r$ is
$$u(w\mid r)=m(w)+\mu\big(m(w)-m(r)\big),$$
where $m(\cdot)$ is standard "consumption utility" and $\mu(\cdot)$ is "gain-loss utility" satisfying loss aversion and diminishing sensitivity (axioms A1–A4, and a sharper piecewise-linear A3'). The reference point is allowed to be a probability measure $G$, so a stochastic outcome $F$ is evaluated as expected reference-dependent utility under "mixed feelings":
$$U(F\mid G)=\int\!\!\int u(w\mid r)\,dG(r)\,dF(w).$$
Preferences are linear in probabilities (no nonlinear decision weights), which the authors note deliberately gets some low-probability-insurance predictions "wrong." For modest stakes $m(\cdot)$ is taken linear.

Three reference-point regimes are analyzed: (i) **surprise** situations, where expectations $G$ are exogenous and fixed independently of the choice set (the limiting low-probability case); (ii) **unacclimating personal equilibrium (UPE)**, where the agent rationally anticipates her choice set but commits only shortly before the outcome, so the reference point equals the expected behavior—a fixed-point/self-confirming condition (related to Shalev's 2000 "loss-aversion equilibrium"); and (iii) **committed/preferred personal equilibrium (CPE/PPE)** for delayed-consequence decisions where the agent can commit early. Results are derived as propositions; a parameterized example ($m(w)=10{,}000\ln w$, $\mu(x)=\eta x$ for $x\ge0$ and $\mu(x)=-3\eta\sqrt{-x}$ for $x<0$) tabulates willingness-to-pay and implied CRRA coefficients.

## Data
None—this is a theory paper. The only "data" is a calibrated numerical example (Table 1: three fifty-fifty gambles at $100, $10,000, and $500,000 stakes under various expectations and background risks). The authors cite empirical risk-aversion estimates from others (Barsky et al. 1997; Chetty 2003, 2005; Mehra & Prescott 1985; Sydnor 2006; Schechter 2005) to motivate the scale-dependence puzzle.

## Key findings
- **Proposition 1** (endowment effect for risk): under linear $m$ and A3', a lottery added to a *risky* reference point is more readily accepted than when added to a riskless one. Setting $H=w$, $G=F$ yields: a person is less risk averse in *eliminating* a risk she expected to face than in *taking on* the same risk she did not expect.
- **Proposition 2**: for a positive-EV lottery $F$, the agent is locally risk neutral when the reference lottery is sufficiently widely distributed, will accept small multiples of $F$ and reject $-F$, and displays more risk aversion for gains than for mixed gambles; prior expectation of risk lowers risk aversion.
- **Proposition 3**: an agent who anticipates both a risk and the possibility of insuring it is *first-order* risk averse.
- **Propositions 4, 7, 8**: the more a risk can be prepared for (commitment), the greater the displayed risk aversion—risk aversion is higher under an expected insurance decision than none, and higher still under early commitment (CPE > PPE/UPE > surprise).
- **Surprise results** (replicating prospect theory): on a surprise modest loss the agent is risk *loving* (distaste for insuring losses), explaining low-deductible avoidance and expensive extended warranties only out of equilibrium; also rationalizes the **disposition effect** (Odean 1998; Genesove & Mayer 2001) via expected resale price as reference point.
- **Proposition 9** (large-scale risk): when diminishing sensitivity is significant, the expected utility of a very risky gamble is essentially independent of the reference point ($|U(F\mid r')-U(F\mid r)|<\epsilon$), so consumption utility $m(\cdot)$ dominates and behavior approaches standard expected utility. This reconciles single-/double-digit CRRA at large stakes with triple-digit (or "embarrassingly large") implied CRRA at modest/small stakes.

## Contribution
Provides the first unified, expectations-based account of monetary risk attitudes that simultaneously generates prospect-theory behavior for surprises, first-order (Segal-Spence type) risk aversion for anticipated insurable risks, an endowment effect for risk, the disposition effect, and standard large-stakes risk aversion—all from one preference specification with comparative-statics predictions on how the environment (prior expectations, anticipation, commitment timing, background risk) shifts risk taking. It sharpens and operationalizes Kőszegi & [[@Koszegi2006b|Rabin (2006)]], shows the full $m(\cdot),\mu(\cdot)$ are recoverable from behavior (Appendix B), and explains the scale-dependence of measured risk aversion.

## Limitations & open questions
- **Choice-set primitive / narrow bracketing**: the model takes as given the set of decisions and risks the agent considers, separate from all risks she actually faces. Little is known about "the extent, patterns, and effects of such bracketing phenomena"—if agents fully integrated all background risk, reference dependence would barely matter.
- **Welfare ambiguity**: it is unclear whether gain-loss sensations belong in a welfare measure; narrow bracketing and underestimation of reference-point adjustment may make people over-weight transient gain-loss feelings, so a welfare measure "is likely to be closer to consumption utility than we assume."
- **Underestimation of reference-point change** has behavioral implications the model does not fully capture (people may fail to appreciate how shedding risky expectations sheds loss sensations).
- **Salience/attention**: the model treats all outcomes symmetrically, but losses and foregone losses differ in salience (Sydnor 2006), implying possibly stronger insurance demand than predicted.
- **Anticipatory emotions** (anxiety) are omitted yet seem important in risky financial decisions.
- **Multiperiod consumption**: results are derived in a single-period wealth setting and not verified for a full multiperiod consumption model.
- **Low-probability insurance**: linearity in probabilities makes some predictions (e.g., insuring low-probability losses) wrong by construction.

## Connections
The paper builds directly on Kőszegi & [[@Koszegi2006b|Rabin (2006)]] and is the risk-focused companion to that expectations-based reference-dependence program. Its utility form relates closely to Sugden (2003), and to the gain-loss separations of [[@Bell1985|Bell (1985)]], [[@Loomes1986|Loomes & Sugden (1986)]], and Köbberling & Wakker (2005); alternatives that collapse the reference lottery into a certainty equivalent include [[@Bell1985|Bell (1985)]], [[@Loomes1986|Loomes & Sugden (1986)]], [[@Gul1991|Gul]] (1991, disappointment aversion), and [[@Shalev2000|Shalev (2000)]], whose "loss-aversion equilibrium" corresponds to the UPE concept here. It contrasts with status-quo prospect theory of [[@Kahneman1979|Kahneman & Tversky (1979)]]. Disposition-effect work by Odean (1998), Genesove & Mayer (2001), and the prospect-theory formalization by Gomes (2005) and Barberis & Xiong (2006) is reinterpreted. Closely related findings on first/second-order risk aversion and background risk appear in Barberis, Huang & Thaler (2006). Empirical anchors for the scale-dependence argument come from Rabin (2000), Barsky et al. (1997), Chetty (2003, 2005), Mehra & Prescott (1985), Sydnor (2006), and Schechter (2005); the break-even effect references Thaler & Johnson (1990); endowment-for-risk evidence cites Knetsch & Sinden (1984) and Birnbaum et al. (1992).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
