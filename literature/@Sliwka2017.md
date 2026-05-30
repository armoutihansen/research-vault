---
citekey: Sliwka2017
title: Wage Increases and the Dynamics of Reciprocity
authors: ["Sliwka, Dirk", "Werner, Peter"]
year: 2017
type: journalArticle
doi: 10.1086/689189
zotero: "zotero://select/library/items/BLVTXJG7"
pdf: /Users/jesper/Zotero/storage/AJCLKVP5/Sliwka2017.pdf
tags: [literature]
keywords: [gift-exchange, reciprocity, reference-dependence, loss-aversion, wage-dynamics, real-effort-experiment, narrow-bracketing]
topics: []
related: [Akerlof1982, Benartzi1995, Dufwenberg2004, Falk2006, Fehr1993, Kahneman1979, Koszegi2006b, Ockenfels2015, Rabin1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We investigate how workers' performance is affected by the timing of wages in a real-effort experiment. In all treatments, agents earn the same wage sum, but wage increases are distributed differently over time. We find that agents work harder under increasing wage profiles if they do not know these profiles in advance. A profile that continuously increases wages by small amounts raises performance by about 15% relative to a constant wage. The effort reactions can be organized by a model in which agents reciprocally respond to wage impulses, comparing wages to an adaptive reference standard determined by the previous wage.

## Summary

Sliwka and Werner run a real-effort lab experiment in which the *timing* of wage increases is varied while holding the total wage budget fixed. When workers do not know the full wage profile in advance, a profile of small, frequent (continuous) increases raises total output by about 15% relative to a constant wage at no extra cost to the principal. A single large surprise increase produces only a transient bump that fades as workers "get used to" the new wage. The patterns are organized by a model of reciprocity with an *adaptive* reference standard: workers compare each wage to the previous period's wage, so it is the recurring *incidence* of an increase, not its size, that sustains effort. A control experiment that reveals the full profile ex ante eliminates the timing effect, confirming the reference-standard mechanism.

## Research question

Can the persistence of gift exchange (positive reciprocity) be increased by appropriately *timing* wage increases over an ongoing relationship, holding the total wage sum constant? And which behavioral channel — a fixed vs. an adaptive reference standard — best explains the dynamic effort reactions?

## Method / identification

The core is a model of reciprocity with reference-dependent wage evaluation plus a real-effort experiment cleanly designed to rule out repeated-game confounds.

**Model.** An agent works for a principal over $T$ periods. In period $t$ the agent receives wage $w_t$, exerts effort $e_t$ at cost $c(e_t)$ with $c''>0$, and the principal's return equals $e_t$. The agent has reciprocal social preferences (after Cox, Friedman, and Gjerstad 2007): utility is
$$u^A_t = v^A_t + h(v_t)\cdot v^P_t,$$
where $v^A_t = w_t - c(e_t)$ and $v^P_t = e_t - w_t$ are the material payoffs, and $h(v)$ maps the agent's "emotional state" $v_t$ into the weight placed on the principal's payoff, with $h'>0$, $h''\le 0$. The emotional state evolves as
$$v_t = (1-\alpha_t)\,v_{t-1} + \alpha_t\, f(w_t - w^r_t),$$
with the impulse function
$$f(\Delta) = v_0 + r\cdot\begin{cases} \Delta & \text{if } \Delta\ge 0,\\ \lambda\,\Delta & \text{if } \Delta<0,\end{cases}$$
where $\Delta = w_t - w^r_t$, $r$ scales reciprocal inclinations, and $\lambda\ge 1$ captures loss aversion (disappointments loom larger than elations). The parameter $\alpha_t\in(0,1]$ is "memory/inertia": $\alpha_t=1$ means only the most recent impulse matters (no memory), $\alpha_t = 1/t$ means all past impulses are averaged equally (long memory).

Two reference standards are contrasted. A **fixed standard** sets $w^r_t = w_0$ (the initial reference wage) for all $t$ — a "broad bracketer" judging generosity by cumulative wages. An **adaptive standard** sets $w^r_t = w_{t-1}$ — a "narrow bracketer" judging the most recent change; combined with short memory this is myopic loss aversion ([[@Benartzi1995|Benartzi and Thaler 1995]]). Effort solves $c'(e_t) = h(v_t)$.

**Experiment.** 216 agents and 216 principals (main experiment, Cologne CLER, z-Tree). Each agent–principal pair interacts for eight 250-second periods of a tedious real-effort task (counting the digit 7 in number blocks). Crucially, principals are *never* informed of period-by-period performance, and agents know this — so wages cannot reward or punish, ruling out reputation/repeated-game incentives and giving a clean causal read on reciprocity. Principals choose ex ante between two of four profiles, all paying 1,000 ECU total but differing in size/frequency of increases: **Baseline** (125 each period, 0 increases), **T_Sudden** (100 then 150, one 50-ECU jump in period 5), **T_Successive** (four irregular 25-ECU increases), **T_Continuous** (seven regular 10-ECU increases). Agents do not know the total sum or other profiles. A second **Info** experiment (140 agents) reveals the full profile ex ante.

## Data

Original lab experiment data. Main experiment: 432 participants (216 agent–principal pairs), 1,688 agent-period observations across 14 sessions (July–August 2013). Info control: 280 participants, 9 sessions (March 2015). Plus an online survey of 102 German HR managers (via the DGFP) ranking the four profiles by expected performance. Analysis uses random-effects regressions of $\log(\text{output}+1)$ with subject-clustered robust SEs, controlling for trial-period speed as an ability proxy.

## Key findings

- **Proposition 1:** effort is monotonically increasing in the emotional state, strictly increasing in $w_t$ and decreasing in $w^r_t$.
- **Corollary 1:** if $w_t = w^r_t$ every period, effort stays constant at $e_0 = a(v_0)$ — so fully anticipated wages (where actual = reference) make timing irrelevant.
- **Proposition 2 (fixed standard):** effort can exceed the reference level $e_0$ only if $w_t > w_0$. The data reject this: T_Continuous already beats Baseline in period 3 (by ~15%) while its wage is still *below* Baseline.
- **Proposition 3 (fixed standard, nondecreasing wages):** once effort increases in some period it must increase in all later periods, even those without further increases.
- **Proposition 4 (adaptive standard, stable wage):** if the wage is held constant, effort rises iff the prior emotional state was below $e_0$ and falls otherwise — i.e., elevated effort "wears off" after an increase. Supported: T_Sudden's bump decays back to Baseline by period 8; performance dips in no-increase periods.
- **Proposition 5 (Appendix):** under an adaptive standard, repeated equal increases raise performance toward a stable upper bound exceeding the constant-wage level.
- **Empirics:** all increasing profiles start *below* Baseline in period 1 (lower initial wage); only **T_Continuous significantly raises total output (~15%, p<.05)**, driven entirely by the second half (~25% gain). Disentangling absolute level vs. size vs. incidence: it is the *incidence* of an increase (a positive dummy) — not its ECU size — that predicts effort, so $h(v)$ is effectively concave. The continuous-increase treatment effect is concentrated among self-reported positively reciprocal agents (no reciprocity effect in Baseline). In the **Info** experiment, no profile produces significant per-period or total effects — timing vanishes once wages are anticipated. Many experimental principals (only ~52%) fail to pick increasing profiles, yet HR managers correctly rank multiple-increase profiles as superior.

## Contribution

First systematic, *budget-neutral* comparison of wage *schedules* (rather than levels), isolating timing of increases as a costless lever for sustaining gift exchange. Provides a tractable reciprocity model that nests fixed (broad-bracketing) vs. adaptive (narrow-bracketing / myopic-loss-aversion) reference standards and yields sharp, testable, divergent effort dynamics. Empirically shows persistence of positive reciprocity is achievable via frequent small stimuli, explains why single surprise raises fade (echoing Gneezy and List 2006), rationalizes secrecy of pay profiles, and offers a novel reciprocity-based rationale for deferred/seniority pay absent any firing threat.

## Limitations & open questions

- The last-period dip in T_Successive/T_Continuous raises a worry that repeated-increase effects eventually vanish; the authors argue against this (Proposition 5 upper bound, significant penultimate-period gains) but cannot fully rule it out within 8 periods — how persistent are effects over longer horizons?
- The model does not pin down which profile maximizes revenue: numerical simulations show the ranking depends on $\lambda$ (loss aversion) and the elasticity of effort to the emotional state, so there is no clean a priori prediction of the optimal schedule.
- The adaptive standard mispredicts one transition (it implies a period-1-to-2 rise in T_Successive that is not observed), suggesting the simple two-parameter memory process is incomplete.
- External validity: short lab horizon, artificial counting task, secrecy of total budget; field generalization (especially the deferred-compensation argument) is conjectural.
- The mechanism behind why principals systematically under-choose increasing profiles while HR professionals get it right is left open.

## Connections

Builds directly on the gift-exchange literature ([[@Fehr1993|Fehr, Kirchsteiger, and Riedl 1993]]; [[@Akerlof1982|Akerlof 1982]]) and the reciprocity-preference models it uses or contrasts ([[@Rabin1993|Rabin 1993]]; [[@Dufwenberg2004|Dufwenberg and Kirchsteiger 2004]]; [[@Falk2006|Falk and Fischbacher 2006]]; Cox, Friedman, and Gjerstad 2007). The reference-dependence and loss-aversion machinery comes from [[@Kahneman1979|Kahneman and Tversky (1979)]] and Köszegi and [[@Koszegi2006b|Rabin (2006)]], with the adaptive-standard-plus-short-memory case equating to myopic loss aversion ([[@Benartzi1995|Benartzi and Thaler 1995]]) and the broad/narrow-bracketing distinction of Read, Loewenstein, and Rabin (1999) and Thaler (1999); Camerer et al. (1997) on taxi drivers is the canonical narrow-bracketing field analogue. The transient-bump result directly parallels field experiments by Gneezy and List (2006) and Bellemare and Shearer (2009); the reciprocity-heterogeneity result echoes Cohn, Fehr, and Götte (2015). It extends [[@Ockenfels2015|Ockenfels, Sliwka, and Werner (2015b)]] on multi-step increases and connects to deferred-pay incentive theory (Lazear 1979; Huck, Seltzer, and Wallace 2011) and preferences for rising wage profiles (Loewenstein and Sicherman 1991; Frank and Hutchens 1993; Grund and Sliwka 2007).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
