---
citekey: Koszegi2009
title: Reference-Dependent Consumption Plans
authors: ["Kőszegi, Botond", "Rabin, Matthew"]
year: 2009
type: journalArticle
doi: 10.1257/aer.99.3.909
zotero: "zotero://select/library/items/U3729KB6"
pdf: /Users/jesper/Zotero/storage/YNQ3JFHJ/Koszegi2009.pdf
tags: [literature]
keywords: [reference-dependent-preferences, loss-aversion, expectations-based-reference-point, news-utility, precautionary-savings, information-preferences, prospect-theory]
topics: []
related: [Bell1985, Benartzi1995, Caplin2001, Gul1991, Kahneman1979, Koszegi2006b, Tversky1981]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We develop a rational dynamic model in which people are loss averse over changes in beliefs about present and future consumption. Because changes in wealth are news about future consumption, preferences over money are reference-dependent. If news resonates more when about imminent consumption than when about future consumption, a decision maker might (to generate pleasant surprises) overconsume early relative to the optimal committed plan, increase immediate consumption following surprise wealth increases, and delay decreasing consumption following surprise losses. Since higher wealth mitigates the effect of bad news, people exhibit an unambiguous first-order precautionary-savings motive. (JEL D14, D81, D83, D91)

## Summary

Kőszegi and Rabin extend their expectations-based reference-dependence program to a fully dynamic setting in which utility derives from *changes in rational beliefs* about present and future consumption, with bad news weighted more heavily than good news (loss aversion). The key new primitive is that news about imminent consumption can resonate more strongly than news about distant consumption. From this single device the paper derives a coherent set of predictions about informational preferences (a taste for receiving information early and clumped together), consumption-based foundations for loss aversion over money, dynamically inconsistent overconsumption that is exacerbated by prior uncertainty, asymmetric responses to wealth surprises, and a novel first-order precautionary-savings motive.

## Research question

How does loss aversion defined over *changes in beliefs about present and future consumption* shape (i) preferences over the timing and granularity of information about an exogenous future event, (ii) attitudes toward monetary risk, and (iii) intertemporal consumption-savings behavior? Can a consumption-based "news utility" model unify prospect theory, habit formation, and endowment-effect accounts of reference dependence?

## Method / identification

A discrete-time formal model with periods $0,\dots,T$. In each period $t\geq1$ a $K$-dimensional consumption vector $c_t$ is realized. Instantaneous utility is the sum of reference-independent "consumption utility" plus gain-loss utility from belief revisions:
$$u_t = m(c_t) + \sum_{\tau=t}^{T}\gamma_{t,\tau}\,N\!\left(F_{t,\tau}\mid F_{t-1,\tau}\right).$$
Here $\gamma_{t,t}=1$ (contemporaneous gain-loss utility) and $0<\gamma_{t,\tau}<1$ increasing in $t$ for $\tau>t$ (prospective gain-loss utility that weakens with temporal distance to the outcome). Gain-loss utility uses an *ordered (percentile-by-percentile) comparison* between new and old belief distributions:
$$N(F^k_{t,\tau}\mid F^k_{t-1,\tau}) = \int_0^1 \mu\!\left(m^k(c_{F_{t,\tau}}(p)) - m^k(c_{F_{t-1,\tau}}(p))\right)dp,$$
where the universal gain-loss function $\mu(\cdot)$ satisfies Kahneman–Tversky-style properties (A0)–(A4): continuity with $\mu(0)=0$, monotonicity, loss aversion ($\mu(y)+\mu(-y)<\mu(x)+\mu(-x)$ for $y>x>0$), diminishing sensitivity ($\mu''<0$ for $x>0$, $\mu''>0$ for $x<0$), and a kink with loss-aversion coefficient $\lambda=\mu'_-(0)/\mu'_+(0)>1$. A linear subcase (A3') sets $\mu'_+(0)=\eta$, $\mu'_-(0)=\lambda\eta$ to isolate loss aversion from diminishing sensitivity. Because preferences depend on the sequence of expectations, the model is closed with a belief-formation theory: the implemented plan must be a **preferred personal equilibrium (PPE)** — a state-contingent plan that, in each period and contingency, prescribes a credible continuation plan and a current action maximizing expected reference-dependent utility given the expectations the plan itself generates, solved by backward recursion. Applications use $T=2$ specializations (information example; monetary-risk model with background risk; two-period consumption-savings problem with budget $c_1+c_2=W$ and concave $m$).

## Data

None — this is a pure theory paper. It marshals existing experimental evidence (Gneezy & Potters 1997 myopic loss aversion; Bellemare et al. 2005; Haigh & List 2005) as motivation and consistency checks, but estimates nothing.

## Key findings

- **Information preferences.** Proposition 1: collapsing two signals into one without delaying them strictly raises welfare (people dislike piecemeal/"dribbling" information). Proposition 2: receiving signals earlier raises welfare when $\gamma_{t,\tau}$ strictly increases in $t$, and is welfare-neutral when $\gamma_{t,\tau}=1$. Propositions 3–4: a sufficiently weak isolated signal always harms welfare, yet a small signal is *preferred* when the decision maker has just received or is about to receive other information — predicting the comparative static that the more information one already receives, the more additional information one wants.
- **Monetary preferences.** Gains and losses in money are news about future consumption, so people attend to small wealth changes even when these contribute negligible consumption risk; this rationalizes some "narrow bracketing" as a preference rather than an error. Depending on when uncertainty in a risk set $D$ is resolved and integrated with background risk, behavior reduces to prior reduced-form models (prospect-theory PPE, disappointment aversion à la Bell/Loomes–Sugden, or CPE) — and the model predicts *which* applies. When isolated-risk uncertainty is drowned in contemporaneous background risk, behavior is approximately risk neutral.
- **Overconsumption.** With deterministic wealth and $\gamma=\gamma_{1,2}<1/\lambda$, the ex ante optimal equal-split plan $c_1=c_2=W/2$ is not consistent: the marginal incentive to overconsume in period 1 is $\eta(1-\gamma\lambda)m'(W/2)>0$, so any PPE has $c_1>W/2$. This dynamic inconsistency resembles present-bias/temptation models but arises for a different reason (raising the period-1 reference point). Distinctively, prior uncertainty *exacerbates* overconsumption: there exist $\gamma$ such that sufficient wealth uncertainty induces overconsumption at every wealth level, even though no single deterministic wealth level would.
- **Asymmetric responses & precautionary savings.** Small wealth increases are fully consumed in period 1; small wealth decreases are fully absorbed in period 2. Because low consumption utility is more painful than high is pleasant, the consumer dislikes period-2 consumption uncertainty and saves more to lower marginal utility — an unambiguous *first-order* precautionary-savings motive, stronger than expected-utility-of-wealth accounts.

## Contribution

Provides consumption-based microfoundations for reference-dependent monetary preferences (news about future consumption as the carrier of gain-loss utility), unifying prospect theory, habit formation, and endowment-effect models within one dynamic framework. Introduces prospective gain-loss utility and the temporal-decay parameter $\gamma_{t,\tau}$, the ordered-comparison belief metric, and the PPE solution concept for dynamic expectations-based preferences. Generates novel predictions — information clumping/timing preferences, uncertainty-driven overconsumption, and a first-order precautionary-savings motive — and shows when narrow bracketing is rational versus a mistake.

## Limitations & open questions

The authors are explicit about several weaknesses. (1) The model takes as a *primitive* the set of decisions and risks a person is focusing on; predictions hinging on prior expectations (e.g., that prior uncertainty raises overconsumption) may be hard to test because what people were contemplating is unobservable. (2) It also takes as primitive the *dimensions* over which gain-loss utility is evaluated separately; a dynamic setting introduces awkward cases (e.g., consumption 100 vs. 101 periods out being treated as separate gain and loss when they plausibly compensate). (3) The lagged-reference-point assumption makes the prediction that streams of small news drive utility to $-\infty$ calibrationally unrealistic at vanishing time steps; a weighted average of past beliefs is suggested as a fix. (4) The theory fails to explain narrow bracketing of simultaneously-resolved choices ([[@Tversky1981|Tversky–Kahneman 1981]]; Rabin–Weizsäcker), so genuine bracketing mistakes remain outside the rational framework. (5) Agents may *mispredict* how future expectation changes will affect their feelings (projection bias), weakening any expectation-management motives. (6) Discounting, time-inconsistent immediate gratification, and richer multi-period consumption paths in the monetary model are left for future work. Suggested applications: self-control/budgeting/mental accounting, escalating auction bidding, and contemplation preceding choice.

## Connections

Builds directly on Kőszegi & [[@Koszegi2006b|Rabin]] (2006, 2007) on expectations-based reference-dependent preferences and personal equilibrium, and extends Stone (2005), who first identified expectations-based overconsumption for deterministic wealth. The gain-loss function follows [[@Kahneman1979|Kahneman & Tversky (1979)]] prospect theory via the (A0)–(A4) axioms of Bowman, Minehart & Rabin (1999). Contemporaneous and antecedent "news utility" work includes Matthey (2005, 2006), Hsee & Tsai (2008), and Kimball & Willis (2006); anticipatory-utility and information-preference models include [[@Caplin2001|Caplin & Leahy]] (2001, 2004), Caplin & Eliaz (2003), and Kőszegi (2006a); the present-bias and temptation benchmarks it is contrasted against are Laibson (1997), O'Donoghue & Rabin (1999), and Gul & Pesendorfer (2001). The monetary-preference analysis connects to Barberis, Huang & Thaler (2006), disappointment aversion of [[@Bell1985|Bell (1985)]] and Loomes & Sugden (1982), and the narrow-bracketing/myopic-loss-aversion literature of [[@Benartzi1995|Benartzi & Thaler (1995)]], Read, Loewenstein & Rabin (1999), Thaler (1999), with supporting experiments by Gneezy & Potters (1997), Bellemare et al. (2005), and Haigh & List (2005). Habit-formation antecedents include Duesenberry (1952) and Ryder & Heal (1973); endowment-effect work includes Knetsch (1989) and Kahneman, Knetsch & Thaler (1990); related one-shot-resolution and disappointment intuitions appear in Palacios-Huerta (1999), [[@Gul1991|Gul (1991)]], and Dillenberger (2008).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
