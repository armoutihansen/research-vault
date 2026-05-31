---
citekey: Berns2007
title: Intertemporal choice – toward an integrative framework
authors: ["Berns, Gregory S.", "Laibson, David", "Loewenstein, George"]
year: 2007
type: journalArticle
doi: 10.1016/j.tics.2007.08.011
zotero: "zotero://select/library/items/FUHZ5WZH"
pdf: /Users/jesper/Zotero/storage/FL6JZXYF/Berns2007.pdf
tags: [literature]
keywords: [intertemporal-choice, hyperbolic-discounting, neuroeconomics, self-control, dynamic-inconsistency, time-preference, present-bias]
topics: ["[[anticipatory-utility-motivated-beliefs]]"]
related: [Loewenstein1987]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Intertemporal choices are decisions with consequences that play out over time. These choices range from the prosaic – how much food to eat at a meal – to life-changing decisions about education, marriage, fertility, health behaviors and savings. Intertemporal preferences also affect policy debates about long-run challenges, such as global warming. Historically, it was assumed that delayed rewards were discounted at a constant rate over time. Recent theoretical and empirical advances from economic, psychological and neuroscience perspectives, however, have revealed a more complex account of how individuals make intertemporal decisions. We review and integrate these advances. We emphasize three different, occasionally competing, mechanisms that are implemented in the brain: representation, anticipation and self-control.

## Summary
This is an interdisciplinary review (TICS, Neuroeconomics) that synthesizes economic, psychological and neuroscientific work on intertemporal choice. It argues that the classical discounted-utility (DU) model, with its single exponential discount rate, is too impoverished to describe how people actually trade off present against future. The authors organize the alternative evidence around four interacting components — time discounting, anticipation, self-control and representation — and advance the thesis that intertemporal behavior emerges from at least two competing neural systems: a "cool", patient, analytic system (associated with prefrontal cortex) and a "hot", impatient, affective system (associated with mesolimbic dopamine circuitry). The integrative payoff is a research program in which neurobiological description constrains and enriches formal economic models.

## Research question
How do people actually make decisions whose consequences unfold over time, and can the disparate findings from economics, psychology and neuroscience be integrated into a single framework? Concretely: is intertemporal choice governed by one all-purpose discounting mechanism, or by several distinct (and sometimes competing) mechanisms implemented in different brain systems?

## Method / identification
This is a conceptual/integrative review rather than an empirical study, so the "method" is a survey and reconciliation of formal models and experimental literatures. The formal backbone is a comparison of discount functions for a reward of magnitude $x$ delayed to time $t$:

- **Exponential (DU) discounting:** value $=\delta^t x$ with a fixed discount factor $\delta\le 1$ (figure uses $\delta=0.95$). Samuelson's DU model implies *dynamic consistency*: "resolutions once made are never broken."
- **Hyperbolic discounting** (Ainslie; Mazur): value weighted by a function inversely proportional to delay, e.g. $\frac{1}{K\cdot t + 1}$ (figure uses $K=0.1$), which decays faster in the short run than the long run, so the agent is more impatient over near-term tradeoffs.
- **Quasi-hyperbolic ($\beta$–$\delta$) discounting** (Phelps–Pollak; Laibson): the piecewise sequence of weights $1,\ \beta\delta,\ \beta\delta^2,\ \dots,\ \beta\delta^t$ with $0<\beta<1$ and $0<\delta<1$, which behaves like exponential discounting beyond the first period but adds an extra present-bias drop $\beta$.

The review derives *preference reversals* / *dynamic inconsistency* from non-exponential discounting via a worked example (Box 1): with $\beta=1/2,\ \delta=1$ the weights are $1,\ \tfrac12,\ \tfrac12,\dots$. An investment with immediate cost 4 and delayed benefit 6 is planned when distant — $\tfrac12(-4)+\tfrac12(6)=1>0$ — but abandoned at the moment of action — $1\cdot(-4)+\tfrac12(6)=-1<0$. The review then contrasts three families of mechanisms that *also* generate present-biased reversals without modifying the discount function: **visceral influences** (hot/cold two-state models), **cue-contingent preferences** (Pavlovian conditioning of drive states), and **temptation preferences** (Gul–Pesendorfer-style models that charge a utility cost of self-control). For the neural evidence it leans on fMRI/neuroimaging correlational designs (notably McClure et al. 2004), GSR/startle measures of anticipatory arousal, lesion studies, and developmental studies of prefrontal maturation.

## Data
None original — this is a review. It re-interprets others' data: animal operant-conditioning studies (rats, pigeons, cotton-top tamarins that cannot wait ~8 s to triple a reward), human discounting experiments, the delay-of-gratification ("pretzel"/marshmallow) paradigm, framing studies (date vs. delay effect; Wilson & Daly's attractive-faces manipulation; Prelec & Loewenstein's French-dinner sequence), drug-deprivation discounting studies, and neuroimaging of anticipation, craving and intertemporal choice.

## Key findings
- **DU is descriptively inadequate.** Exponential discounting counterfactually rules out preference reversals; real relapse rates (e.g. >50% in the first year after quitting smoking), gym non-attendance and credit-card behavior show people routinely break patient plans (*dynamic inconsistency*).
- **Hyperbolic / quasi-hyperbolic discounting** parsimoniously generates these reversals and is experimentally validated, but is only a *partial* account: temporal immediacy is one of many impulsivity drivers alongside sensory proximity and drive states (hunger, thirst, arousal, opioid/nicotine deprivation).
- **Two-systems hypothesis.** Hyperbolic discounting may reflect the "splicing" of two systems — McClure et al. found prefrontal regions engaged by *all* intertemporal choices but mesolimbic dopamine regions engaged *only* when an immediate option was available, and the relative activation predicted choice (though purely correlational).
- **Anticipation can itself confer (dis)utility**, violating DU: people expedite dreaded outcomes (e.g. electric shocks) to shorten aversive waiting; anticipatory neural activity in pain regions and in ventral striatum/orbitofrontal cortex tracks this.
- **Self-control** is a distinct component — implementing a far-sighted plan needs both far-sighted choice and resistance to temptation; ACC is implicated in conflict monitoring and inferior prefrontal cortex in inhibition, but no single region "owns" self-control.
- **Representation/framing** alters discounting: pallid vs. consummatory framing of rewards, date- vs. delay-framing (flatter discounting for dates), reproductively salient cues raising discount rates, and sequence framing producing apparent *negative* time preference (preferring improving sequences).

## Contribution
The paper's contribution is integrative rather than a new theorem: it proposes a unified taxonomy of intertemporal choice built from four components (discounting, anticipation, self-control, representation) and crystallizes the multiple-competing-systems view — patient "cool/analytic" vs. impatient "hot/affective" neural systems — as the most promising modeling frontier in neuroeconomics. It explicitly positions neurobiological evidence as a constraint on, and generator of, economic models, and clarifies that present-biased behavior can arise from several distinct mechanisms (discount-function curvature, visceral states, cues, temptation costs) that produce observationally similar reversals.

## Limitations & open questions
The authors are candid that increased realism has come "at the expense of simplicity," reviving the parsimony-vs-realism tension. Their explicit open problems (Box 2 and Conclusion) are strong project hooks:
- We know *little about how the four mechanisms interact* — making this interaction a stated priority.
- Is there *one all-purpose discounting mechanism or many competing systems*, each with its own time perspective?
- *How can neurobiological data be used to develop and test models* of intertemporal choice, marrying neural and theoretical descriptions, given that choice/preference has historically been treated tautologically?
- *Can a single model span the full range of timescales* (milliseconds to decades) over which intertemporal choices occur, or do different mechanisms apply at different scales?
- *How does the representation of time itself influence intertemporal choice* — in particular, how does representation of the past shape the (prospective) representation of the future?
- The flagship neural evidence (McClure et al.) is correlational and "does not provide definitive evidence of causal relationships."

## Connections
The review is anchored by Samuelson's (1937) DU model and Strotz's (1956) early analysis of dynamic inconsistency. The psychological challenge originates with Ainslie's hyperbolic discounting and Rachlin & Green's commitment/self-control work; the economic formalization runs through Phelps & Pollak (1968) and especially Laibson (1997) "Golden eggs and hyperbolic discounting" (quasi-hyperbolic $\beta$–$\delta$). The self-control modeling literature it draws on includes Thaler & Shefrin's planner-doer model, Gul & Pesendorfer (2001) temptation preferences, Fudenberg & Levine's dual-self model, Bernheim & Rangel on cue-triggered addiction, and O'Donoghue & Rabin / Akerlof on procrastination. The anticipation strand builds on [[@Loewenstein1987|Loewenstein (1987)]] and pain-anticipation neuroimaging; representation/framing draws on Kahneman-style heuristics-and-biases, Mischel's delay-of-gratification studies, Read et al.'s date/delay effect, and Prelec & Loewenstein on sequences. On the neuroscience side it connects to McClure et al. (2004, 2007), Montague & Berns, Schultz's reward-prediction work, and Glimcher et al. on neuroeconomic impulsivity. Frederick, Loewenstein & O'Donoghue's (2002) critical review is the natural companion survey.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
