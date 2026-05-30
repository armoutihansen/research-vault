---
citekey: Sarver2018
title: Dynamic Mixture-Averse Preferences
authors: ["Sarver, Todd"]
year: 2018
type: journalArticle
doi: 10.3982/ECTA12687
zotero: "zotero://select/library/items/Y97IIW2B"
pdf: /Users/jesper/Zotero/storage/GIVFTBPI/Sarver2018b.pdf
tags: [literature]
keywords: [mixture-aversion, optimal-risk-attitude, recursive-utility, non-expected-utility, comparative-risk-aversion, stock-market-participation, rabin-paradox]
topics: []
related: [Gul1991, Kahneman1979, Quiggin1982, Sydnor2010]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> To study intertemporal decisions under risk, we develop a new recursive model of non-expected-utility preferences. The main axiom of our analysis is called mixture aversion, as it captures a dislike of probabilistic mixtures of lotteries. Our representation for mixture-averse preferences can be interpreted as if an individual optimally selects her risk attitude from some feasible set. We describe some useful parametric examples of our representation and provide comparative statics that tightly link decreases in risk aversion to larger sets of feasible risk attitudes. We then present several applications of the model. In an insurance problem, mixture-averse preferences can produce a marginal willingness to pay for insurance coverage that increases in the level of existing coverage. In investment decisions, our model can generate endogenous heterogeneity in equilibrium stock market participation, even when consumers have identical preferences. Finally, we demonstrate that our model can address the Rabin paradox even in the presence of reasonable levels of background risk.

## Summary
Sarver embeds a new family of non-expected-utility risk preferences into the Epstein–Zin (1989) recursive framework. The behavioral primitive is a single axiom, *mixture aversion*: a dislike of probabilistic mixtures of lotteries. The paper's main theorem shows this axiom is equivalent to the recursive certainty equivalent being convex in probabilities, which by duality yields an *optimal risk attitude* (ORA) representation: the agent behaves as if she optimally selects a utility transformation $\varphi$ (her "risk attitude") from a feasible set $\Phi$ to maximize her continuation value. Comparative statics tie *lower* risk aversion to *larger* feasible sets $\Phi$. The model uniquely separates risk aversion from preference for diversification, letting it deliver novel predictions in insurance (willingness to pay rising in existing coverage), asset markets (endogenous heterogeneous participation among identical agents), and small-stakes risk (resolving the Rabin paradox even with background risk).

## Research question
Can a tractable, axiomatically founded recursive model of dynamic risk preferences simultaneously (i) maintain risk aversion, (ii) relax preference for diversification, and (iii) allow aversion to *marginal* increases in risk to *decrease* with existing risk exposure, in order to explain anomalies (probabilistic insurance, deductible demand, limited and heterogeneous stock-market participation, the Rabin paradox) that defy time-separable expected utility and standard recursive Kreps–Porteus (EZKP) utility?

## Method / identification
Pure decision-theoretic / axiomatic. The primitive is a binary relation $\succeq$ on the space $D$ of infinite-horizon temporal lotteries, where $D$ is homeomorphic to $C\times\Delta(D)$ for a compact, connected metrizable consumption space $C$ (the Epstein–Zin domain). The starting point is an **Epstein–Zin (EZ) representation** $(V,u,W,\beta)$ with
$$V(c,m)=u(c)+\beta\,W\!\left(m\circ V^{-1}\right),$$
where $W$ is a certainty equivalent on distributions of continuation values (satisfying $W(\delta_x)=x$ and FOSD-monotonicity) and $\beta\in(0,1)$. Appendix A.1 supplies an axiomatic characterization of the EZ form via weak order, nontriviality, continuity, stationarity, a Debreu (1960) separability axiom, and FOSD (Proposition 3).

The central restriction is **Axiom 1 (Mixture Aversion)**: for all $c,c'\in C$ and $m,m'\in\Delta(D)$,
$$\left(c,\tfrac12 m+\tfrac12 m'\right)\succeq (c',m)\;\Longrightarrow\;(c,m')\succeq\left(c',\tfrac12 m+\tfrac12 m'\right).$$
Measuring the value of probability shifts in units of current consumption, this says the gain from raising the weight on $m$ from $0$ to $\tfrac12$ is weakly smaller than from $\tfrac12$ to $1$ (a generalized certainty-effect / "mental preparation" intuition). The identification strategy is duality: a convex $W$ is a supremum of affine (expected-utility) functionals, which converts the certainty equivalent into an optimization over transformations $\varphi$. Comparative risk aversion uses the Chew–Epstein (1991) definition and is identified up to affine transformation via *maximal* sets of transformations (since dominated $\varphi$'s are unidentifiable).

## Data
None — this is a theory paper. The applications (insurance deductibles, stock-market participation, the Rabin calibration) are worked analytically using parametric ORA examples; no estimation or empirical dataset is used, though the model is calibrated against documented behavioral patterns (Kahneman–Tversky probabilistic insurance, Sydnor's over-insurance of modest risks, low/heterogeneous equity participation).

## Key findings
- **Theorem 1 (main representation).** Given an EZ representation, the following are equivalent: (1) $\succeq$ satisfies mixture aversion; (2) the certainty equivalent $W$ is convex in probabilities; (3) $\succeq$ has an **optimal risk attitude (ORA) representation** $(V,u,\Phi,\beta)$,
$$V(c,m)=u(c)+\beta\sup_{\varphi\in\Phi}\int_D \varphi\!\left(V(\hat c,\hat m)\right)dm(\hat c,\hat m),\qquad \sup_{\varphi\in\Phi}\varphi(x)=x\ \ \forall x.$$
The constraint $\sup_\varphi\varphi(x)=x$ makes the model collapse to time-separable utility under certainty; under risk the agent "selects her risk attitude" $\varphi$. Despite the optimization, any ORA representation is *more* risk averse than time-separable EU with the same $(u,\beta)$ (Corollary 2.1), since $\sup_\varphi E[\varphi(V)]\le E[\sup_\varphi\varphi(V)]=E[V]$.
- **Proposition 1.** A convex, lower-semicontinuous $W$ is FOSD-monotone iff it is generated by nondecreasing $\varphi$; it is SOSD-monotone (risk averse) iff generated by nondecreasing *concave* $\varphi$. This is a non-differentiable, convexity-based analogue of Machina's (1982) local expected utility.
- **Proposition 2 / Corollary 1.** Risk-averse EZKP utility (concave aggregator $h$) is a special case of ORA, with $\varphi(x\mid\gamma)=\gamma+\frac{h(x)-h(\gamma)}{h'(\gamma)}$; with exponential $h_\theta$ one obtains the entropic form $\frac1\theta\log E[\exp(-\theta V)]$ optimized over a target $\gamma$ and risk-sensitivity $\theta$ (with cost $\tau(\theta)$). The parametric family connects to Ben-Tal–Teboulle's *optimized certainty equivalent* and (via Example 2's kinked transformation) to Yaari's dual model.
- **Theorem 2 (uniqueness).** Two maximal ORA representations of the same preference coincide up to a common affine transformation: $\beta_1=\beta_2$, $u_2=\alpha u_1+\lambda(1-\beta_1)$, and a bijection $f$ between maximal sets with $\varphi_2(\alpha x+\lambda)=\alpha\varphi_1(x)+\lambda$.
- **Theorem 3 (comparative risk aversion).** $\succeq_1$ is more risk averse than $\succeq_2$ iff (up to affine transformation) the maximal set $\Phi_1^*$ injects into $\Phi_2^*$ — a more risk-averse agent has a *smaller* set of feasible risk attitudes. Corollary 2 specializes this: more flexibility (a larger $\Phi$, lower $\theta$, or lower cost $\tau$) means less risk aversion.
- **Applications.** With certainty equivalents of the cost form $\sup_{\theta,\gamma}\{\int\varphi(x\mid\gamma,\theta)\,d\mu-\tau(\theta)\}$, aversion to marginal risk can *fall* with exposure. This yields (4.1) willingness to pay more for the last dollar of insurance coverage than the first; (4.2) endogenous heterogeneity in equilibrium stock-market participation among ex-ante identical consumers; (4.3) a resolution of the Rabin (2000) paradox not relying on first-order risk aversion and robust to moderate background risk; and (4.4) consistency with violations of EU concentrated near the boundary of the probability simplex.

## Contribution
Introduces mixture aversion and the ORA representation, a parsimonious recursive non-EU model. Its distinguishing feature, established via Figure 1's taxonomy, is that it is the *only* model among recursive rank-dependent utility, betweenness, disappointment aversion, and cautious expected utility that can relax preference for diversification (quasiconcavity in random variables) while retaining risk aversion (SOSD-monotonicity) — results from Dekel (1989) and Chew–Karni–Safra (1987) show the others cannot. It also generalizes risk-averse EZKP utility and risk-averse rank-dependent utility, provides a convexity-based local-expected-utility theory complementing Machina's differentiability-based one, and supplies clean comparative-statics linking risk aversion to set inclusion of feasible transformations.

## Limitations & open questions
- The exact feasible set $\Phi$ is **not identified**; only maximal (or, in the Supplement, minimal) canonical sets are recoverable, because pointwise-dominated transformations leave choice behavior unchanged.
- The axiomatic analysis is restricted to **compact, connected** consumption spaces; extension to unbounded $C=\mathbb{R}_+$ (used in the applications) requires bounded-growth assumptions and is only sketched.
- The local-expected-utility result relies on **convexity rather than differentiability**, since $W$ is generally non-differentiable; reconciling this with the Machina-style differentiable literature is left partly to the Supplement.
- The companion paper (Sarver 2017) is needed to develop the full stock-market-participation rationale (low participation, bond-only portfolios); the present paper only demonstrates the heterogeneity mechanism.
- Empirical/structural estimation of the ORA representation and the cost function $\tau(\theta)$ is not attempted and is a natural open direction.

## Connections
Builds directly on the recursive framework of Epstein & Zin (1989, 1990) and the temporal-lottery domain of Kreps & Porteus (1978), with the EZ axiomatization paralleling Chew & Epstein (1991). The mixture-aversion intuition descends from the certainty effect of Allais (1953) and [[@Kahneman1979|Kahneman & Tversky (1979)]], and from probabilistic insurance as analyzed by Wakker, Thaler & Tversky (1997). The ORA representation generalizes risk-averse rank-dependent utility ([[@Quiggin1982|Quiggin 1982]]; Yaari 1987; Segal 1989), and relates to betweenness (Chew 1983; Dekel 1986), disappointment aversion ([[@Gul1991|Gul 1991]]; Routledge & Zin 2010), and cautious expected utility (Cerreia-Vioglio, Dillenberger & Ortoleva 2015). The parametric examples coincide with Ben-Tal & Teboulle's (1986, 2007) optimized certainty equivalent and Yaari's (1987) dual model. The local-expected-utility analysis extends Machina (1982) and Cerreia-Vioglio, Maccheroni & Marinacci (2017). The small-stakes application engages the Rabin (2000) paradox and the calibration critiques of Safra & Segal (2008); the participation application connects to Barberis, Huang & Thaler (2006) on narrow framing and the household-finance literature (Mankiw & Zeldes 1991; Guiso & Sodini 2013), while the deductible evidence draws on [[@Sydnor2010|Sydnor (2010)]]. Comparative statics use monotone-comparative-statics tools from Milgrom & Shannon (1994) and Quah (2007), and the duality and additive-separability machinery from Debreu (1960) and Gul & Pesendorfer (2004). Closely related conceptually are Kreps & Porteus (1979), Machina (1984), and Ergin & Sarver (2015) on psychological/unobservable commitments.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
