---
citekey: Caplin2001
title: Psychological Expected Utility Theory and Anticipatory Feelings
authors: ["Caplin, Andrew", "Leahy, John"]
year: 2001
type: journalArticle
doi: 10.1162/003355301556347
zotero: "zotero://select/library/items/97LUYUSD"
pdf: /Users/jesper/Zotero/storage/GAPZUJJM/Caplin2001.pdf
tags: [literature]
keywords: [anticipatory-emotions, psychological-expected-utility, time-inconsistency, anxiety, asset-pricing, equity-premium-puzzle, decision-under-uncertainty]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We extend expected utility theory to situations in which agents experience feelings of anticipation prior to the resolution of uncertainty. We show how these anticipatory feelings may result in time inconsistency. We provide an example from portfolio theory to illustrate the potential impact of anticipation on asset prices.

## Summary
Caplin and Leahy build a "psychological expected utility" (PEU) model in which agents derive utility not only from physical prizes but from anticipatory emotions, such as anxiety, hope, and suspense, experienced while uncertainty is still unresolved. Methodologically, they keep the full apparatus of expected utility, including the substitution axiom, but enlarge the prize space to include "psychological states" (states of mind). Because anticipatory feelings depend on future uncertainty and dissipate as that uncertainty resolves, preferences become time inconsistent. Applied to a two-period Lucas-tree asset-pricing model, anxiety over risky payoffs lowers safe-asset returns and raises required returns on risky assets, offering a complementary account of the equity-premium and risk-free-rate puzzles, and predicting "overreaction" to possibility rather than probability.

## Research question
Can the anticipatory emotions that psychologists treat as central to decision making, especially anxiety, fear, and worry, but also savoring and suspense, be brought inside the rational-choice framework of expected utility? And what new economic predictions, particularly for asset pricing and the timing of choices, follow once utility is allowed to depend on feelings experienced *before* uncertainty resolves?

## Method / identification
The model has three components. (1) A space of **psychological states** replaces the standard prize space: there are two periods with state spaces $X_t \subseteq \mathbb{R}^{n_t}$, and the product $X = X_1 \times X_2$ carries the topology of weak convergence on Borel lotteries $P(X)$. (2) A description of **physical lotteries** and how their uncertainty resolves over time. (3) A continuous mapping connecting physical lotteries to mental states.

Preferences $\succeq$ on $P(X)$ satisfy standard axioms (Assumption 1): completeness/transitivity, the **substitution axiom**, an Archimedean condition, an additive-separability condition $(p_1,p_2)=(q_1,q_2)\Rightarrow p\sim q$, and continuity. By Fishburn's representation theorem this yields (Proposition 1) a bounded continuous EU representation that is time-additive, $U(x)=U_1(x_1)+U_2(x_2)$.

Crucially, anticipation is encoded through timing: the period-$t$ psychological state realizes at the *end* of period $t$, so feelings arise only in period 1 and concern the period-2 uncertainty still unresolved. To formalize "evolving uncertainty," the authors adopt Kreps and Porteus's [1978] temporal lotteries: with $Z_1$ the first-period prize space and $L_2$ distributions over period-2 prizes, define $Y_1 = Z_1 \times L_2$, and a continuous map $\phi: Y_1 \to X_1$ that delivers the mental state induced by an outcome $y_1=(z_1,l_2)$. Induced first-period utility takes the form $V_1(z_1,l_2)=U_1(\phi(z_1,l_2)) + \beta\,E_{l_2}[U_2(z_2)]$, which looks standard except that $l_2$, the residual lottery, enters first-period utility. The mapping $\phi$ is "what gives the theory structure."

A general two-period decision problem is then posed (Assumption 2: Euclidean action/state spaces, compact-valued continuous constraint correspondences, Markov transition $Q(B,s)=\Pr\{s_2\in B\mid s_1=s\}$). Because period-1 feelings depend on the period-2 *strategy* (different but payoff-equivalent continuations can yield different anticipation), preferences are time inconsistent. The authors handle this in the spirit of Strotz [1955]: they define **consistent strategies** $\Pi^C(s_1)$ as those whose period-2 policy is optimal in every contingency, and select the consistent strategy best from the period-1 viewpoint, equivalently the period-1-preferred subgame-perfect equilibrium of the game between the period-1 and period-2 "selves." Using an adaptation of Harris [1985], they prove existence (Proposition 2).

## Data
None. This is a theory paper. The empirical content is illustrative: the authors marshal existing psychological experiments (e.g., Nomikos et al. on waiting-period anxiety; Miller and Mangan on "monitors" vs. "blunters"; Lerman et al. on declined genetic-test results; Averill and Rosenn on the "head in the sand" shock experiment; Harless and Camerer's meta-study on gambles of differing support) to motivate the assumptions, but they estimate nothing.

## Key findings
- **Proposition 1 (representation).** Under Assumption 1, $\succeq$ on psychological lotteries has a bounded continuous EU representation with a time-additive form $U_1(x_1)+U_2(x_2)$.
- **Proposition 2 (existence).** An optimal (period-1-preferred consistent) strategy exists despite time inconsistency.
- **Asset pricing.** In a two-period Lucas-tree economy where utility is $V_1(c_1,l_2)=u_1(c_1,a(l_2))+\beta E_{l_2}[u_2(c_2)]$ and anxiety $a(\cdot)$ is aversive ($\partial u_1/\partial a<0$), the asset FOC pins down the price $p_n$ of asset $n$ as the standard discounted-payoff term *plus* an anxiety term $(\partial u_1/\partial a)(\partial a/\partial\theta_n)$. With a linear anxiety specification $a(l)=-\alpha E c_2 + \gamma \operatorname{var}(c_2)$, the marginal effect on anxiety of holding asset $n$ is $-\alpha E s_n + 2\gamma \operatorname{cov}(c_2,s_n)$. A riskless asset reduces anxiety, so its price rises and the **risk-free rate falls** ("peace of mind"); a sufficiently risky asset (large $\gamma$ relative to $\alpha$) raises anxiety, lowering its price and raising its required return, an **equity premium**. Kreps-Porteus is recovered as the time-consistent special case.
- **Possibility, not probability.** If anticipatory emotion responds to discrete mental images (Damasio), anxiety is sensitive to whether an event is *possible* rather than to fine probability changes, rationalizing apparent overreaction to small-probability events and the asset-market overreaction to news.
- **Time course and attention.** Anxiety has a U-shaped time profile and depends on when a threat is recognized ($T_0$) versus when it hits ($T^\ast$), a margin absent from static risk aversion; agents may rationally avoid information ("head in the sand").
- **Substitution axiom defended.** Anticipation invalidates the *static* substitution axiom (as Pope [1985] argued), but the authors show it is *restored* once the state space is enriched to include feelings.

## Contribution
The paper founds a tractable, rationality-preserving way to put anticipatory emotions into economic models, the PEU model, and shows it is a strict generalization of Kreps-Porteus that adds time inconsistency and a richer per-period assignment of utility. It distinguishes anticipatory *anxiety* from static *risk aversion*, argues conventional risk-aversion surveys (e.g., Barsky et al.) understate the effect of uncertainty on asset prices, and supplies a unified lens on the equity premium, information avoidance, savoring/commitment, suspense and gambling, mood and risk-taking, and information-disclosure policy (e.g., when a central bank should withhold bad news).

## Limitations & open questions
- **Time inconsistency requires a solution-concept commitment.** The Strotz/subgame-perfect selection is one of several defensible standards; the authors flag that "without time consistency, there is no presumption that indifference extends back" and that the choice of selection among indifferent period-2 policies materially affects period-1 payoffs.
- **The structure lives in $\phi$ (and $a(\cdot)$), which is assumed, not derived.** The general model is "relatively unstructured"; predictions hinge on the posited shape of the anxiety/anticipation mapping.
- **Non-uniqueness of the psychological model behind a given reduced form.** Because Kreps-Porteus does not pin down the cross-period assignment of utility, "many different psychological expected utility models reduce to the same Kreps-Porteus model" (welfare analysis is taken up in Caplin and Leahy [1999]).
- **Infinite-regress worry.** Rejecting substitution would be warranted only if no complete model of psychological states exists, i.e., if one were forced into "anticipatory feelings about anticipatory feelings ... ad infinitum"; the authors assume a complete description suffices but do not resolve where to truncate.
- **Welfare and policy are sketched, not settled.** The information-disclosure example (suppress vs. release bad news) and retirement-planning/financial-education trade-offs (anxiety today vs. better preparation tomorrow) are posed as open normative questions.
- **Two periods only.** The framework is explicitly two-period; richer dynamic time profiles of anxiety (the U-shape, the role of $T_0$ vs. $T^\ast$) are motivated but not embedded in a multi-period model here.

## Connections
The direct ancestor is Kreps and Porteus [1978] on temporal resolution of uncertainty; PEU generalizes it by dropping time consistency and specifying per-period utility, and connects to the recursive-utility asset-pricing tradition of Epstein-Zin [1989], Weil [1990], and Farmer [1990] on the equity-premium and risk-free-rate puzzles (Mehra-Prescott). The deterministic anticipation model of Loewenstein [1987] is the precursor the authors extend to uncertainty; their highlighted critique is that "since his model is deterministic, it is ill-suited to capturing anticipatory emotions, such as anxiety, that are predicated on an uncertain future." The treatment of time inconsistency follows Strotz [1955] with existence via Harris [1985]. Within behavioral decision theory it sits beside the disappointment models of Bell [1985] and Loomes and Sugden [1986] (which PEU faults as static), the nonexpected-utility program responding to Allais, and Machina's [1989] concession that separability can be rational if consequences are described deeply enough. The companion papers Caplin and Leahy [1997, 1999] develop suspense, savoring/commitment (the nonrefundable-ticket vacation example), and the doctor-patient information problem; the program is part of the psychology-and-economics agenda surveyed by Rabin [1998], drawing on Damasio [1994], Lazarus [1966], and the anxiety literature (Spielberger, Miller, Breznitz).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
