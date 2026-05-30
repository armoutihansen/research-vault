---
citekey: Tversky1992
title: "Advances in prospect theory: Cumulative representation of uncertainty"
authors: ["Tversky, Amos", "Kahneman, Daniel"]
year: 1992
type: journalArticle
doi: 10.1007/BF00122574
zotero: "zotero://select/library/items/KX4LCED2"
pdf: /Users/jesper/Zotero/storage/WYCQBZXY/Tversky1992.pdf
tags: [literature]
keywords: [cumulative-prospect-theory, loss-aversion, probability-weighting, rank-dependent-utility, decision-under-risk, reference-dependence, fourfold-pattern]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We develop a new version of prospect theory that employs cumulative rather than separable decision weights and extends the theory in several respects. This version, called cumulative prospect theory, applies to uncertain as well as to risky prospects with any number of outcomes, and it allows different weighting functions for gains and for losses. Two principles, diminishing sensitivity and loss aversion, are invoked to explain the characteristic curvature of the value function and the weighting functions. A review of the experimental evidence and the results of a new experiment confirm a distinctive fourfold pattern of risk attitudes: risk aversion for gains and risk seeking for losses of high probability; risk seeking for gains and risk aversion for losses of low probability.

## Summary
This is the foundational paper introducing **cumulative prospect theory (CPT)**, the rank-dependent successor to the 1979 original. It replaces separable decision weights with a *cumulative* (Choquet) functional applied separately to gains and losses, which (i) restores stochastic dominance, (ii) extends the model to any finite number of outcomes and to uncertain (not just risky) prospects, and (iii) permits distinct weighting functions for gains and losses. The two organizing principles are **diminishing sensitivity** (which makes the value function S-shaped and the weighting function inverse-S-shaped) and **loss aversion** (which makes the value function steeper for losses). A within-subject experiment with 25 subjects estimates the value-function exponent at $0.88$, the loss-aversion coefficient at $2.25$, and weighting-function parameters $\gamma=0.61$ (gains), $\delta=0.69$ (losses), and confirms the **fourfold pattern of risk attitudes**.

## Research question
Can a single descriptive model of choice under risk and uncertainty simultaneously (a) accommodate the major empirical violations of expected utility theory — framing effects, nonlinear preferences, source dependence, risk seeking, and loss aversion — while (b) respecting stochastic dominance and (c) scaling to arbitrarily many outcomes? The paper asks what formal valuation rule and what shapes of the value and weighting functions are needed, and what behavioral axioms characterize that rule.

## Method / identification
The model is a **two-part rank-dependent / Choquet representation**. Outcomes of a prospect $f=(x_i,A_i)$ are ranked, $x_i>x_j \iff i>j$, with positive subscripts for gains, negative for losses. The overall value is the sum of two Choquet integrals,
$$V(f)=V(f^+)+V(f^-),\qquad V(f^+)=\sum_{i=0}^{n}\pi_i^+ v(x_i),\quad V(f^-)=\sum_{i=-m}^{0}\pi_i^- v(x_i).$$
Decision weights are **differences of capacities** $W^+, W^-$ (nonadditive set functions with $W(\varnothing)=0$, $W(S)=1$, monotone in inclusion):
$$\pi_i^+ = W^+(A_i\cup\cdots\cup A_n)-W^+(A_{i+1}\cup\cdots\cup A_n).$$
For risky prospects the capacities reduce to strictly increasing probability-weighting functions $w^+,w^-:[0,1]\to[0,1]$ with $w(0)=0,\ w(1)=1$, applied to *cumulative* probabilities. Within each sign the weights sum to 1, but for **mixed prospects the total can differ from 1** because gains and losses use separate capacities — this is what distinguishes CPT from the standard one-part Choquet model.

The qualitative shape assumptions are: $v$ concave for gains ($v''(x)\le 0,\ x\ge0$), convex for losses, and steeper for losses ($v'(x)<v'(-x),\ x\ge0$); and $w$ concave near 0, convex near 1 (inverse-S), yielding subadditivity for small probabilities and superadditivity near certainty. Under preference homogeneity the value function is identified as a **two-part power function** $v(x)=x^\alpha$ for $x\ge0$ and $-\lambda(-x)^\beta$ for $x<0$ (eq. 5), and the weighting function as $w(p)=p^\gamma/(p^\gamma+(1-p)^\gamma)^{1/\gamma}$ (eq. 6). Parameters are recovered per subject by nonlinear regression on certainty equivalents.

The **appendix** gives the axiomatization. The key relation is Schmeidler's **comonotonicity**; CPT is characterized (Theorem 1) by **comonotonic independence** plus **double matching** ($f^+\sim g^+$ and $f^-\sim g^- \Rightarrow f\sim g$). Theorem 2 sharpens this via tradeoff-consistency conditions: EU requires tradeoff consistency (TC), cumulative utility theory requires comonotonic TC (CTC), and CPT requires **sign-comonotonic tradeoff consistency (SCTC)** plus double matching. Proofs build on Wakker's additive-representation theorem for lower-triangular subsets.

## Data
Original within-subject experiment: 25 graduate students (Berkeley/Stanford), three one-hour computer sessions, paid a $25 flat fee. Certainty equivalents for 28 positive and 28 negative two-outcome prospects (plus 8 mixed/translated problems) were elicited indirectly via a sequence of choices between the prospect and a descending series of seven sure amounts (so cash equivalents are *derived from choices*, not stated). Six prospects were repeated to gauge reliability (test–retest correlation $\approx 0.55$). The paper also reuses two independence-test surveys (156 money managers; 98 students) and cites external incentive studies (Camerer 1989; Kachelmeier & Shehata 1991).

## Key findings
- **Fourfold pattern of risk attitudes** (the central result): risk aversion for gains and risk seeking for losses at moderate/high probability; risk seeking for gains and risk aversion for losses at low probability. The full pattern held for 22 of 25 subjects; for $p\ge.5$ all 25 were risk averse over gains and risk seeking over losses.
- **Parameter estimates:** median value-function exponent $\alpha=\beta=0.88$ (diminishing sensitivity); median loss aversion $\lambda=2.25$; weighting parameters $\gamma=0.61$, $\delta=0.69$ — i.e. the weighting function is inverse-S, overweighting small probabilities and underweighting moderate/high ones.
- **Loss aversion magnitude:** for 50/50 mixed bets, the gain must be roughly twice the loss for acceptability ($\lambda\approx 2$); small positive translations of mixed prospects (Table 6) produce large effects that the reference-free standard rank-dependent model cannot explain.
- **Empirically, $w^+(p)=w^-(p)$** fits better than the rank-dependent restriction $w^+(p)=1-w^-(1-p)$: all 25 subjects had $w^+(.5)<.5$ and $w^-(.5)<.5$.
- **Common-consequence (Allais-type) violations** occur under uncertainty as well as risk, and are inconsistent with regret theory and Fishburn's SSA model; they imply subadditivity of the weighting function.
- **Incentives:** the qualitative violations (and marked small-probability overweighting) persist with large real stakes (Kachelmeier–Shehata), so they are not artifacts of hypothetical or trivial payoffs.
- **Theorems 1–2** axiomatically characterize CPT via double matching + sign-comonotonic tradeoff consistency, nesting EU and cumulative utility theory as special cases.

## Contribution
CPT became the workhorse descriptive model of decision under risk and uncertainty. Relative to 1979 prospect theory it (i) guarantees first-order stochastic dominance without an editing-phase patch, (ii) handles many-outcome and genuinely uncertain (capacity-based) prospects, (iii) separates gain and loss weighting, and (iv) supplies a clean axiomatic foundation distinguishing it from EU and from the one-part rank-dependent / Choquet model. It also delivers portable functional forms and parameter estimates ($\alpha=0.88$, $\lambda=2.25$, $\gamma=0.61$) that remain standard benchmarks.

## Limitations & open questions
The authors are explicit that the cumulative functional "is unlikely to be accurate in detail." Their stated open problems:
- **Source dependence of weighting functions.** Ellsberg-type and competence effects (Heath & Tversky 1991) imply that different sources of uncertainty need *different* weighting functions, some lying entirely above others. Estimating decision weights for uncertain (non-probabilistic) events is flagged as "a promising domain for future research."
- **Instability of decision weights.** Weights may depend on the *formulation* of prospects and on the number, spacing, and level of outcomes (curvature is more pronounced when outcomes are widely spaced). CPT could be generalized to capture this, but possibly at the cost of giving up the separability of values and weights — a trade-off the authors leave unresolved.
- **No formal theory of framing.** The editing/framing phase that precedes valuation has no formal model.
- **Constructive, contingent choice.** Choice involves heuristics and editing operations that depend on elicitation and context and "do not readily lend themselves to formal analysis," so any such theory is "approximate and incomplete."
- **Behavior near probability endpoints** is ill-behaved: very small probabilities can be greatly overweighted *or* neglected, which the smooth weighting form does not pin down.

## Connections
Direct successor to **Kahneman & Tversky (1979)** prospect theory and to **Tversky & Kahneman (1986, 1991)** on framing and loss aversion. The cumulative functional adapts the rank-dependent representations of **Quiggin (1982)**, **Yaari (1987)**, **Weymark (1981)**, and **Schmeidler (1989)** (Choquet integral over capacities), with axiomatics drawn heavily from **Wakker (1989a,b, 1991, 1992)** and the joint-receipt approach of **Luce & Fishburn (1991)**. It empirically adjudicates against **regret theory (Loomes & Sugden)** and **Fishburn's SSA**. The fourfold pattern and small-probability overweighting connect to lottery/insurance demand, the Allais and Ellsberg paradoxes, and downstream work on probability weighting (Prelec 1998), ambiguity, and reference-dependent preferences. For a researcher in social preferences and choice modeling, this is the canonical reference-dependent utility specification and the source of the standard loss-aversion and probability-weighting parameterizations.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
