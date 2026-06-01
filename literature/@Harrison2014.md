---
citekey: Harrison2014
title: Eliciting subjective probabilities with binary lotteries
authors: ["Harrison, Glenn W.", "Martínez-Correa, Jimmy", "Swarthout, J. Todd"]
year: 2014
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/8KJ6R4S6"
pdf: /Users/jesper/Zotero/storage/USIDQ8QX/Harrison et al. - 2014 - Eliciting subjective probabilities with binary lotteries.pdf
tags: [literature]
keywords: [belief-elicitation, proper-scoring-rules, binary-lottery-procedure, subjective-probability, risk-aversion, experimental-economics, rank-dependent-utility]
topics: ["[[experimental-belief-elicitation]]"]
related: [Berg1986, Gneiting2007, Hossain2013, Karni2009, Offerman2009, Roth1979, Tversky1992]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> We evaluate a binary lottery procedure for inducing risk neutral behavior in a subjective belief elicitation task. Prior research has shown this procedure to robustly induce risk neutrality when subjects are given a single risk task defined over objective probabilities. Drawing a sample from the same subject population, we find evidence that the binary lottery procedure also induces linear utility in a subjective probability elicitation task using the Quadratic Scoring Rule. We also show that the binary lottery procedure can induce direct revelation of subjective probabilities in subjects with popular Non-Expected Utility preference representations that satisfy weak conditions.

## Summary
Proper scoring rules such as the Quadratic Scoring Rule (QSR) elicit subjective probabilities truthfully only if the agent is risk neutral. Because lab subjects are systematically risk averse even over small stakes, raw QSR reports are biased toward $0.5$ (the report that smooths payoffs across events). This paper asks whether pairing the QSR with a Binary Lottery Procedure (BLP) — paying the scoring-rule output as *points* that set the win probability in a two-prize lottery — induces linear utility and restores truthful belief revelation. The authors develop the theory (truthful reporting under SEU and, under weak conditions, under Rank-Dependent Utility), then run a controlled lab experiment over a genuinely subjective event (an unknown Bingo-cage composition). Non-parametric tests and a structural model support the claim that the BLP mitigates risk-aversion distortion and recovers latent beliefs.

## Research question
Does the Binary Lottery Procedure, combined with the Quadratic Scoring Rule, induce risk-neutral (linear-utility) behavior in a *subjective* probability elicitation task, so that subjects directly report their latent subjective beliefs without the analyst needing to correct for risk attitudes — and does this hold for non-Expected-Utility preferences?

## Method / identification
**Mechanism (theory).** For a binary event $R/W$ with latent belief $\pi_R$, the QSR pays $S(\theta\mid R)=\alpha-\beta(1-\theta)^2$ if $R$ occurs and $S(\theta\mid W)=\alpha-\beta(0-\theta)^2$ if $W$ occurs ($\alpha=\beta=100$, report $\theta\in\{0,\dots,100\}$). Under the BLP these scores are *points* defining the objective probability $p_R(\theta)=S(\theta\mid R)/100$ of winning \$50 (else \$0). Under Subjective Expected Utility with Reduction of Compound Lotteries, normalizing $U(\$50)=1,U(\$0)=0$, valuation collapses to the subjective average win probability
$$SEU(\theta)=\pi_R\,p_R(\theta)+(1-\pi_R)\,p_W(\theta)=Q(\theta).$$
Conditions $Q'(\theta^*)=0,\ Q''<0$ give the unique optimum $\theta^*=100\,\pi_R$ — truthful revelation independent of $U(\cdot)$. The non-EU extension shows a **Rank-Dependent Utility** agent reports the same $\theta^*$: with $RDU(\theta)=w(Q(\theta))$, the FOC $w'(Q(\theta^*))Q'(\theta^*)=0$ reduces to $Q'(\theta^*)=0$ when $w'>0$. Uniqueness follows from **Proposition 1**: if $w(\cdot)$ is strictly increasing and $Q(\cdot)$ strictly concave, $w(Q(\cdot))$ is strictly quasi-concave. Sufficient conditions: ROCL for binary lotteries, probabilistic sophistication (Machina–Schmeidler), $U$ increasing and unique up to affine transform, $w$ strictly increasing, and a strictly concave scoring rule.

**Experimental identification.** Two between-subjects treatments: control **M** (scores paid directly in money) and **P** (scores paid in points via the BLP). Each subject makes exactly one belief decision — avoiding the Random Lottery Incentive Method, whose validity requires the Independence axiom and would preclude estimating RDU.

**Structural estimation.** A latent ML model assumes CRRA utility $U(x)=x^{1-r}/(1-r)$ with a Wilcox (2011) contextual-error logit link and noise parameter $\mu$. Since $r$ is not identified from M-treatment belief reports alone, lottery-choice data from the same pool (following Andersen et al.) are *stacked* with belief responses to jointly estimate $r$ and $\pi_R$; the belief likelihood is a multinomial logit over the 101 reports. The RDU variant adds a Prelec weight $w(p)=p^{\gamma}/(p^{\gamma}+(1-p)^{\gamma})^{1/\gamma}$ permitting the inverted-S shape.

## Data
Original laboratory experiment: 138 subjects across 4 sessions (68 in M, 70 in P) from the Georgia State University pool. The subjective event is the composition of "Bingo Cage 2," built behind a divider from a number drawn from "Bingo Cage 1"; subjects see a noisy spin-based stimulus but never learn the true count until after deciding. A randomly selected, fixed-paid Verifier confirms procedural integrity. Lottery-choice data for risk-attitude identification are pooled from prior experiments on the same population.

## Key findings
- **Hypothesis 1 (BLP mitigates risk aversion):** M reports cluster nearer $50$ than P reports, as predicted if risk aversion pulls money-paid reports toward the payoff-smoothing midpoint. Mean distance-from-50 is $14.2$ (M) vs $18.7$ (P); one-sided Fisher–Pitman permutation $p=0.02$; one-sided Kolmogorov–Smirnov $p=0.02$ excluding session 3 (near-50:50 composition gives that test low power; pooled $p=0.23$).
- **Hypothesis 2 (BLP improves accuracy):** P reports are closer to the true red-ball count (mean distance $12.8$ vs $15.2$); Fisher–Pitman $p=0.02$, KS $p=0.04$, P stochastically dominating M. Since the design grants neither group a perceptual advantage, this reflects linear utility / truthful reporting, not superior perception.
- **Hypothesis 3 (recovery of latent beliefs):** The structural model recovers M-subjects' underlying beliefs; after correcting for risk attitudes the adjusted M beliefs shift toward mean P reports, and the hypothesis that risk-adjusted M beliefs equal mean P reports cannot be rejected, under both EUT and RDU.
- **Theory:** truthful $\theta^*=100\pi_R$ under SEU and (via Proposition 1) under RDU.

## Contribution
First clean experimental test of whether the QSR+BLP recovers *genuinely subjective* probabilities — earlier tests ([[@Hossain2013|Hossain & Okui 2013]]) used urns with objectively known compositions, which does not test belief recovery. It extends the BLP validation of Harrison et al. (2013) from objective-probability risk tasks to subjective belief elicitation, and adds the theoretical result that direct revelation survives under Rank-Dependent Utility, broadening robustness beyond Expected Utility. It positions the BLP as an alternative to ex-post structural risk correction (Andersen et al.) for incentive-compatible belief elicitation.

## Limitations & open questions
- Small sample (138), one decision per subject; tests lose power near a 50:50 composition (session 3), and one idiosyncratic report (100 red) materially moves P means.
- Risk attitude $r$ is not identified within-subject for belief reporters; it is borrowed from pooled lottery data of the same population, assuming a common (or demographically conditioned) CRRA — a maintained, untested assumption.
- The non-EU result covers RDU but not other classes (e.g. Gul disappointment aversion, reference-dependent models); the authors invite their examination and note reference-dependent models' indeterminacy under free reference points.
- Flagged avenues: a functional-analysis treatment of which preference representations admit proper scoring rules, and scoring rules with salient incentives for hard cases such as low-probability elicitation.
- The BLP relies on ROCL and non-stochastic prizes; behavioral failures of compound-lottery reduction would undermine the induced linearity.

## Connections
Builds on Harrison, Martínez-Correa & Swarthout (2013), which validated the BLP over objective probabilities, and on the binary-lottery tradition of Smith (1961), [[@Roth1979|Roth & Malouf (1979)]], and [[@Berg1986|Berg et al. (1986)]], against the skeptical findings of Cox & Oaxaca (1995) and Selten et al. (1999). Scoring-rule foundations connect to [[@Gneiting2007|Gneiting & Raftery (2007)]] and to the parallel "randomized QSR" / "binarized scoring rule" work of Schlag & van der Weel (2013) and [[@Hossain2013|Hossain & Okui (2013)]]. The structural risk-correction alternative is Andersen et al.'s joint estimation of risk and beliefs, rooted in Savage (1954); the error specification follows Wilcox (2011) and Harrison & Rutström (2008). The RDU machinery draws on probabilistic sophistication (Machina & Schmeidler 1992, 1995) and inverted-S weighting ([[@Tversky1992|Tversky & Kahneman 1992]]). Alternative elicitation mechanisms include Grether (1992), Köszegi & Rabin (2008), [[@Offerman2009|Offerman et al. (2009)]], [[@Karni2009|Karni (2009)]], Holt & Smith (2009), and Trautmann & van de Kuilen (2011). Concerns about the Random Lottery Incentive Method cite Cox et al. (2011) and Harrison & Swarthout (2012).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
