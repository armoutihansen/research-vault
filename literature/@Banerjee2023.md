---
citekey: Banerjee2023
title: "Optimal incentive contracts with a spiteful principal: Single agent"
authors: ["Banerjee, Swapnendu", "Chakraborty, Somenath"]
year: 2023
type: journalArticle
doi: 10.1016/j.mathsocsci.2023.01.005
zotero: "zotero://select/library/items/F7Z87LL8"
pdf: /Users/jesper/Zotero/storage/BK8NTDTY/Banerjee and Chakraborty - 2023 - Optimal incentive contracts with a spiteful principal Single agent.pdf
tags: [literature]
keywords: [moral-hazard, social-preferences, spite, inequity-aversion, optimal-contract, principal-agent]
topics: ["[[social-preferences-contract-theory]]"]
related: [Andreoni2002, Banerjee2017, Camerer2011, Dufwenberg2004, Englmaier2012, Falk2006, Falk2008, Fehr1999, Itoh2004, Rabin1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We, first with discrete outcomes and continuous effort, characterize the optimal contracts when a spiteful principal interacts with an other-regarding agent. We show that the optimal wage is weakly decreasing in principal's spitefulness. When the principal and the agent have exactly opposite other-regarding preferences, under certain situations, we get back the self-regarding benchmark optimal contract. Next with continuous outcomes and general functional forms, we characterize the optimal wage schedule and get back the sufficient statistics result when the principal and the agent have exactly opposite other-regarding preferences.

## Summary

A theory paper that pushes the social-preferences-in-contract-theory agenda in a new direction: instead of the usual inequity-averse or reciprocal *agent* facing a self-regarding principal, here the *principal* is **spiteful** (enjoys being ahead, à la [[@Falk2008|Fehr et al. 2008]]) while the agent is other-regarding (inequity-averse or status-seeking, à la [[@Fehr1999|Fehr & Schmidt 1999]] / Neilson & Stowe 2003). Working a single-agent moral-hazard problem in two stages — a closed-form binary-outcome model and a general continuous-output model — the authors show the optimal success wage is weakly decreasing in the principal's spite $\pi$, and that when principal spite and agent inequity aversion are exactly equal and opposite ($\pi=\alpha$) the self-regarding benchmark contract (and the sufficient-statistics result) re-emerges.

## Research question

What does optimal incentive contracting look like when the *principal* is spiteful — i.e. derives utility from being ahead of the agent and disutility from being behind — interacting with an other-regarding agent in a single-agent hidden-action setting? How does the optimal wage schedule move with the principal's spitefulness $\pi$ and the agent's other-regardingness $\alpha$, and under what conditions does the standard self-regarding optimum reappear?

## Method / identification

A principal–agent moral-hazard model, solved analytically in two settings.

**Closed-form binary model (Section 2).** Both parties risk-neutral. Agent picks effort $e\in[0,1]$ (interpreted as the success probability) at cost $e^{2}/2$; project returns $b$ on success, $0$ on failure. Limited liability $w_j\ge 0$ and $w_s\ge w_f$ hold. Other-regarding preferences use a Fehr–Schmidt / Neilson–Stowe modification, with $g(r)=r$ for tractability ("linear" other-regardingness). The principal's state-$j$ utility is
$$U_{P,j}=\begin{cases} b_j-w_j+\pi\,g(b_j-2w_j) & b_j\ge 2w_j\\ b_j-w_j-\pi\,g(2w_j-b_j) & b_j<2w_j,\end{cases}$$
so $\pi\ge 0$ is the spite parameter (enjoy favourable inequity, suffer unfavourable inequity). The agent's utility on success is $U_{A,s}=w_s-\alpha(b_s-2w_s)$, with $\alpha\ge 0$. The paper solves both the contractible-effort (first-best) case and the non-contractible case via the first-order approach, reducing the program to maximising $U_P=[w_s-\alpha(b-2w_s)]\,[b-w_s+\pi(b-2w_s)]$ subject to the IC constraint $e=w_s-\alpha(b-2w_s)$ and the participation constraint $e[w_s-\alpha(b-2w_s)]-e^2/2\ge u$. A key reduced-form object is $\Delta=\frac{1+3\alpha+\pi+4\alpha\pi}{1+2\alpha+2\pi+4\alpha\pi}$, with $\Delta\lessgtr 1$ tracking whether the principal is ahead ($\pi\ge\alpha$) or behind. An alternative specification lets the principal compare her payoff with the agent's *net* payoff $w_s-e^2/2$.

**General model (Section 3).** Continuous output $x$ with density $f(x\mid e)$ (MLRP assumed), general convex other-regarding functions $S(\cdot)$ for the principal and $G(\cdot)$ for the agent, and general agent utility $u(\cdot)$. The principal maximises $\int f(x\mid e)\{x-w(x)+\pi S(x-2w(x))\}\,dx$ subject to PC and (under non-contractibility) the IC first-order condition. Lagrangian methods yield the wage-schedule slope $w'(x)$ and comparative statics in $\pi$; second-order sufficiency requires $G''(\cdot)>S''(\cdot)$.

## Data

None — this is a purely theoretical contribution; the "Data availability" statement confirms no data was used. The introduction cites lab/field measurement of other-regarding parameters (e.g. [[@Andreoni2002|Andreoni & Miller 2002]]; Grosskopf & Pearce 2020) only as motivation.

## Key findings

- **Proposition 1 (binary, non-contractible effort).** The optimal contract is $\{\hat{w}_s=\tfrac{b\Delta}{2},\hat{w}_f=0\}$ for low outside options $0\le u<\tfrac{b^2}{8}[\Delta-2\alpha(1-\Delta)]^2$, and $\{\hat{w}_s=\tfrac{\sqrt{2u}+\alpha b}{1+2\alpha},\hat{w}_f=0\}$ once the PC binds. Optimal effort $\hat{e}=\hat{w}_s-\alpha(b-2\hat{w}_s)>0$.
- **Self-regarding benchmark reversion.** When $\pi=\alpha$ the principal's "spite effect" and the agent's "inequity-aversion effect" exactly cancel, so the principal offers the self-regarding benchmark success wage (when PC slack); when $\pi>\alpha$ the spite effect dominates and the success wage is weakly below benchmark for all outside options; when $\pi<\alpha$ the agent's status-seeking dominates and the wage can exceed the benchmark (with pathological intermediate ranges).
- **Corollary / Proposition 3.** A ceteris paribus increase in principal spite $\pi$ weakly lowers the optimal success wage; under non-contractibility with a risk-averse agent, more spite pushes the wage-schedule slope $w'(x)$ away from $1/2$ toward $0$ (reinforcing the agent's inequity-aversion / risk-aversion effect). With a risk-neutral agent under non-contractibility, $1/2<w'(x)<1$ and spite reinforces the incentive effect (extreme incentives).
- **Linear contractible benchmark.** With contractible effort and a risk-neutral agent the optimal linear contract has slope $1/2$ for a linearly spiteful principal; first-best effort $e_{FB}=\frac{b(1+\alpha+\pi)}{1+2\pi}$ falls in $\pi$, rises in $\alpha$, and equals the self-regarding first best when $\pi=\alpha$.
- **Proposition 7 (general model).** The sufficient-statistics result holds exactly when $\pi=\alpha$ with matched other-regarding functions ($G''(\cdot)=S''(\cdot)$); otherwise optimal contracts load on information non-relevant to effort choice. Spite again weakly lowers the optimal wage.
- **Alternative specification.** When the principal compares payoffs taking the agent's effort cost $e^2/2$ into account, the self-regarding benchmark is *not* recovered even under exactly opposite preferences.

## Contribution

First paper (alongside the companion working out the multi-agent case) to analyse optimal contracting with a *spiteful principal who is ahead* in a moral-hazard setting, as opposed to Englmaier & Wambach's (2005, 2010) inequity-averse principal — crucially, spite works *against* the agent's inequity concern rather than reinforcing it. It extends [[@Banerjee2017|Banerjee & Sarkar (2017)]] from discrete to continuous effort, delivering smooth contracts and the clean "exactly opposite preferences ⇒ self-regarding benchmark" result that discrete effort obscures, and characterises the optimum for *all* combinations of $\pi$ and $\alpha$ rather than only the strongly other-regarding region.

## Limitations & open questions

- **Single agent only.** The multiple-agent case (with peer comparison among agents) is explicitly deferred to future research — the paper's title flags "Single agent."
- **Measurability of $\alpha$ and $\pi$.** The authors flag a "Caveat": the cardinal magnitude of the other-regarding parameters is hard to interpret; only ordinal comparisons ("relatively more spiteful") are defensible, leaving empirical calibration open.
- **Functional-form dependence.** Closed-form results rely on linear ($g(r)=r$) other-regardingness; the general model assumes $G''(\cdot)>S''(\cdot)$ and a sufficiently convex $G$ for second-order conditions, plus the first-order approach validity (MLRP) — robustness to these is assumed, not proven.
- **Sensitivity to the comparison object.** The benchmark-reversion result is fragile: it disappears once the principal nets out the agent's effort cost when comparing payoffs, suggesting the "what is compared to what" modelling choice deserves more scrutiny.

## Connections

The contracting-with-social-preferences lineage runs through Englmaier & Wambach (2005, 2010) on optimal incentive contracts under inequity aversion, [[@Itoh2004|Itoh (2004)]] on an other-regarding agent facing a self-regarding principal, Dur & Glazer (2008) on workers who envy their bosses, and [[@Englmaier2012|Englmaier & Leider (2012)]] on reciprocal agents (building on [[@Rabin1993|Rabin 1993]]; [[@Dufwenberg2004|Dufwenberg & Kirchsteiger 2004]]; [[@Falk2006|Falk & Fischbacher 2006]]). The closest antecedent is [[@Banerjee2017|Banerjee & Sarkar (2017)]] on an other-regarding principal with discrete effort. The preference primitives draw on [[@Fehr1999|Fehr & Schmidt (1999)]] and Neilson & Stowe (2003) for distributional inequity aversion, with the "spite" definition taken from [[@Falk2008|Fehr et al. (2008)]] and Fehr & Fischbacher (2005). Motivating evidence on measuring social preferences cites [[@Andreoni2002|Andreoni & Miller (2002)]], [[@Camerer2011|Camerer (2011)]], and Grosskopf & Pearce (2020); loss-aversion contracting analogues include de Meza & Webb (2007). The general model's sufficient-statistics framing connects to the Holmström-style moral-hazard tradition.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
