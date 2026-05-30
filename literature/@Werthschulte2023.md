---
citekey: Werthschulte2023
title: "Present focus and billing systems: Testing ‘pay-as-you-go’ vs. ‘pay-later’"
authors: ["Werthschulte, Madeline"]
year: 2023
type: journalArticle
doi: 10.1016/j.jebo.2023.05.032
zotero: "zotero://select/library/items/64SF8JIM"
pdf: /Users/jesper/Zotero/storage/6KM25RWG/Werthschulte2023.pdf
tags: [literature]
keywords: [present-bias, energy-consumption, billing-systems, lab-experiment, intertemporal-choice, real-effort-task]
topics: []
related: [Berns2007, Kaur2015, ODonoghue2015, Sprenger2015]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> When customers purchase goods provided by public utilities, such as telecommunications, water, gas or electricity, the predominant payment system is pay-later billing. This paper tests the effectiveness of a pay-as-you-go system and the importance of payment timing in reducing consumption. I conduct a lab experiment which mimics an energy consumption choice and randomizes the timing of when consumption costs are paid: Either immediately ('pay-as-you-go') or one-week after consumption ('pay-later'). Results show that pay-as-you-go billing significantly decreases energy consumption. Yet the decrease in consumption comes at the cost of needing more work time to complete a fixed number of real-effort tasks. As the design controls for a number of contaminating effects, present-focused discounting of the future energy bill under the pay-later system is the likely explanation for the change in behavior.

## Summary
A controlled lab experiment isolates the *timing of payment* as a behavioral lever in utility billing. Subjects solve a fixed batch of tedious letter-search tasks under a deliberately dim screen; buying "light" (brighter screen, at €0.005/second) eases the task. The benefit of light is always immediate, but the monetary cost is randomized to fall either immediately ("pay-as-you-go") or one week later ("pay-later"). Pay-as-you-go cuts average energy consumption by ~12%, driven by far fewer participants leaving the light on for an entire task; the saving is bought with ~15% more working time. Because transaction costs, salience, and payment credibility are equalized across arms, the residual gap is attributed to present-focused discounting of the future bill.

## Research question
Does shifting from pay-later to pay-as-you-go billing reduce consumption of a good with immediate benefits and deferred costs, and is *present focus* (present-biased discounting of the future bill), rather than salience/information/feedback, the operative mechanism? A secondary question is what real resource the consumption reduction costs (here: substitution toward more work time/effort).

## Method / identification
Between-subjects randomized lab experiment (University of Münster, ORSEE recruitment, November 2018; cash payments). On date 1 each participant completes a fixed 25 real-effort tasks (find all instances of a target letter in a 100-letter grid). A light switch raises screen contrast; each second of light costs €0.005, displayed live on an on-screen "meter." Randomization assigns the billing system: in pay-as-you-go, light costs are netted from a €10 show-up fee paid immediately after the tasks; in pay-later, they are netted from a second €10 show-up fee collected one week later (date 2). Both arms must appear on both dates, both see the real-time meter, and a 3-day pickup window plus reminder emails equalize transaction costs, salience, and credibility, respectively. Estimation uses task-level panel regressions with session and task fixed effects and participant-clustered standard errors. The reported design is the between-subjects arm of a larger cross-over design (a within-subjects arm on dates 3–4 is reported in the appendix). Pre-registered (AEARCTR-0003503); a power calculation targeted 200 subjects.

The appendix formalizes the choice. A participant chooses light $\ell$ and work time $t$ to maximize intertemporal utility
$$U = u_1\!\left(e(t,\ell);\,x_1\right) + \delta\, u_2(x_2),$$
with effort $e$ decreasing in light ($\partial e/\partial \ell < 0$) and increasing in time ($\partial e/\partial t > 0$), subject to a production constraint $\text{task} = f(t,\ell)$ and budget constraints that differ only in *when* the light bill $p\cdot\ell$ is paid. The two Lagrangians are
$$\mathcal{L}_{\text{PAYG}} = u_1\!\left(e(t,\ell);\,Y_1 - p\ell\right) + \delta u_2(Y_2) + \lambda\!\left(\text{task} - f(t,\ell)\right),$$
$$\mathcal{L}_{\text{later}} = u_1\!\left(e(t,\ell);\,Y_1\right) + \delta u_2\!\left(Y_2 - p\ell\right) + \lambda\!\left(\text{task} - f(t,\ell)\right).$$
Comparing first-order conditions, the only wedge between arms is that the pay-later group's marginal cost of light is discounted by $\delta$: under (e.g. quasi-linear) utility with $\partial u_1/\partial x_1 = \partial u_2/\partial x_2$, $\delta$ is the sole driver of differential light demand.

## Data
Experimental data only: 213 registered, 171 participated (85 pay-as-you-go, 86 pay-later; one date-2 dropout). Outcomes are aggregated and task-level light-seconds, an indicator for "light always on," and task completion time, over 25 tasks (4275 task-level observations in the main panel). No observational/field dataset; the survey collected at date 3 is not analyzed due to attrition. Data available on request.

## Key findings
- **Consumption falls under immediate payment.** Mean light use is 363.5 s (pay-later) vs. 319.7 s (pay-as-you-go) — a 44 s (~12%) reduction, significant at 10% ($p=.085$). The whole distribution shifts left.
- **Driven by extreme behavior.** "Light always on" occurs in 29% of pay-later tasks vs. 16% of pay-as-you-go tasks ($p=.010$). Panel regression: pay-as-you-go cuts light by 1.7 s/task (10% level) and lowers the "always on" probability by 13 percentage points (5% level).
- **Substitution toward effort.** Pay-as-you-go participants work ~15% longer (≈15 vs. 13 min; +4.9 s/task, 1% level). One extra second of light saves ~0.9 s of work time.
- **Mechanism = present focus.** Because the pay-later delay is only one week, an exponential discount factor rationalizing the gap, $\delta = 0.893$, implies an absurd yearly $\delta_{\text{year}} = 0.003$; invoking O'Donoghue–Rabin's "any noticeable short-term discounting is evidence of present bias," the data instead fit $\delta \approx 1$ with present-bias $\beta = 0.893$ — close to Augenblick–Rabin ($\beta\in[0.81,0.84]$) and Augenblick et al. ($\beta=0.888$).
- **Welfare is ambiguous.** A naive cost-benefit count gives €0.22 in energy savings against ~1.92 extra minutes of work valued near €0.64, so calibrated intertemporal utility is actually higher for the average pay-later participant ($U_{\text{later}}=11.01 > U_{\text{PAYG}}=10.5$) — yet, correcting for present bias and externalities, pay-as-you-go can raise long-run welfare.

## Contribution
First experimental evidence that isolates *payment timing per se* in a billing context, holding salience, information feedback, transaction costs, and credibility constant — whereas field studies (Jack & Smith 2020; Qiu et al. 2017) bundle timing with enhanced feedback. It extends the immediate-effort/future-pay self-control literature ([[@Kaur2015|Kaur et al. 2015]]; Augenblick & Rabin 2019; Aggarwal et al. 2020) to a consumption "loss domain," documents a previously under-noted substitution of energy for effort/time, and ties pay-later overconsumption to present focus, with implications for Pigouvian taxation (present-biased consumers under-respond to prices on the future bill).

## Limitations & open questions
- **One-shot vs. repeated.** The experiment is static; the author flags that with repeated choices the gap may widen (e.g., pay-later groups learn to save more slowly or become inattentive to the meter) — extending to multiple periods is open.
- **Disentangling channels over time.** Future work should separate discounting, salience, and information effects and their joint implication for optimal policy/Pigouvian taxes.
- **No identification of present bias from choices.** The author deliberately avoids eliciting time-inconsistency from ex ante vs. actual light choices because of confounds (mispredicting task difficulty, learning, demand for light); $\beta$ is only calibrated, not estimated, leaving direct identification open.
- **Welfare not measured.** A full welfare evaluation (utility cost of extra work time vs. consumption + externality benefits) is left for future work; the externality itself was not simulated in the design.
- **Marginal significance / power.** The headline consumption effect is only 10%-significant; 20% no-shows cut power to 0.76. The within-subjects arm is insignificant (attributed to participants not noticing the billing change).
- **External validity.** Lab, student sample, single site; the author cites strong site-specific effects (Allcott 2015; Vivalt 2020) and frames the study as a proof of concept that timing matters.

## Connections
Methodologically rooted in real-effort time-preference experiments: Augenblick, Niederle & Sprenger (2015) and Augenblick & Rabin (2019) on dynamic inconsistency over effort, and [[@Kaur2015|Kaur, Kremer & Mullainathan (2015)]] "Self-Control at Work," whose effort cost form $e(t,\ell) = -\tfrac{1}{\theta}\!\left(\tfrac{t}{\ell}\right)^{\theta}$ is borrowed for calibration; Aggarwal et al. (2020) supply the null-effect counterpoint. The present-focus debate over monetary payments (Andreoni & Sprenger 2012; [[@Sprenger2015|Sprenger 2015]]; Cohen et al. 2020; Ericson & Laibson 2019) motivates the design's controls. On energy/billing it sits beside Jack & Smith (2020) and Qiu et al. (2017) on prepaid metering, the salience/feedback strand (Sallee 2014; Jessoe & Rapson 2014; Gilbert & Zivin 2014, 2020; Gans et al. 2013; Lynham et al. 2016), and the author's own Werthschulte & Löschel (2021) linking present bias to household electricity use. The credit-card present-bias literature (Meier & Sprenger 2010; Kuchler & Pagel 2021; [[@Berns2007|Laibson et al. 2007]]) is the consumer-finance analogue, with [[@ODonoghue2015|O'Donoghue & Rabin (2015)]] supplying the interpretive rule used to read the short-horizon discount estimate.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
