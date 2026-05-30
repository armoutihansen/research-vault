---
citekey: Samuelson1988
title: Status quo bias in decision making
authors: ["Samuelson, William", "Zeckhauser, Richard"]
year: 1988
type: journalArticle
doi: 10.1007/BF00055564
zotero: "zotero://select/library/items/J6UU6C2W"
pdf: /Users/jesper/Zotero/storage/H32MWYNG/Samuelson1988.pdf
tags: [literature]
keywords: [status-quo-bias, behavioral-economics, loss-aversion, default-effects, decision-making, framing, endowment-effect]
topics: []
related: [Tversky1974]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Most real decisions, unlike those of economics texts, have a status quo alternative—that is, doing nothing or maintaining one's current or previous decision. A series of decision-making experiments shows that individuals disproportionately stick with the status quo. Data on the selections of health plans and retirement programs by faculty members reveal that the status quo bias is substantial in important real decisions. Economics, psychology, and decision theory provide possible explanations for this bias. Applications are discussed ranging from marketing techniques, to industrial organization, to the advance of science.

## Summary
The paper that named the status quo bias. Across a battery of hypothetical questionnaire decisions (486 MBA and public-policy students) plus two large field studies (Harvard health-plan choices; TIAA-CREF retirement allocations), Samuelson and Zeckhauser show that merely labelling one option as the status quo raises its choice probability far beyond what the canonical rational-choice model permits. They fit a simple linear "response-rate" model quantifying the bias, document it in real high-stakes recurring decisions, and assemble a taxonomy of three explanation classes—rational (transition costs / uncertainty), cognitive (loss aversion, anchoring), and psychological commitment (sunk costs, regret, cognitive dissonance, illusion of control). The bias grows with the number of alternatives and shrinks with the strength of underlying preference.

## Research question
Does the framing of an option as the status quo—doing nothing or retaining a prior choice—significantly affect the probability of its being chosen, in violation of the canonical rational-choice axiom that only preference-relevant features (not labels or position) should influence choice? And if so, is the effect large in consequential real-world decisions, and what explains it?

## Method / identification
Two empirical strategies plus a theoretical taxonomy.

(1) **Controlled questionnaire experiments.** Each subject answered one version of each decision problem (e.g. inheriting a portfolio, choosing a car colour, siting a prison, allocating water). Holding the choice set and preferences fixed, the design manipulated framing: a *neutral* (NEUT) version listing all options on equal footing versus *status quo* (SQ) versions placing one option in the status quo position (the rest becoming alternatives-to-the-status-quo, ASQ). The number of alternatives was varied from two to four (15 versions per question) to test a "numbers effect". Part Two used *sequential* decisions (leasing an airline fleet over two years under good/bad forecasts) where a subject's first-year choice self-selects the status quo for year two; reversing the order of forecasts moves the anchor. No monetary incentives.

The core estimator is a pooled OLS regression imposing adding-up constraints. For an alternative with neutral response rate $\text{NEUT}$, the model posits
$$\text{SQ}=a+b\,\text{NEUT}, \qquad \text{ASQ}=c+d\,\text{NEUT}.$$
Because predicted shares must sum to one (e.g. in the binary case $\text{SQ}_1+\text{ASQ}_2=1$ whenever $\text{NEUT}_1+\text{NEUT}_2=1$), the slopes must be equal, $b=d$, with intercept restrictions $a+c+d=1$ (binary), $a+2c+d=1$ (triples), $a+3c+d=1$ (quads). Intercept and slope dummies for the two-/three-/four-alternative cases test the numbers effect.

(2) **Field studies.** Status quo bias is identified by comparing the choices of *new* enrollees against *old* enrollees who already hold a plan: if old enrollees cling to the incumbent option far more than fresh entrants choose it, that gap is the bias (persistence alone is not, since stable preferences could also produce persistence). A maximum-likelihood adjustment estimates the transfer-rate increase needed to reconcile old- and new-enrollee distributions.

## Data
Three sources. (i) 486 students (mostly first-year MBAs at Boston University plus Kennedy School public-policy students), >96% completing all questionnaire items. (ii) Harvard University health plans: ~9,185 employees across eight plans (two Blue Cross/Blue Shield, six HMOs) over 1980–1986; an earlier Neipp–Zeckhauser (1985) figure that only ~3% of employees switch plans per year. (iii) TIAA-CREF: ~850,000 participants; allocation tables 1981–1986 (61,000 new vs 461,000 old participants in 1986 across five age groups); a 1986 TIAA survey finding only 28% had ever changed their TIAA/CREF split and only one in three considered their initial allocation an informed choice.

## Key findings
- **Robust SQ ordering.** For the large majority of alternatives, response rate is highest in the SQ position, lower in NEUT, lowest in ASQ (e.g. 16/24, 13/18, 17/24 cases fit exactly in the two-/three-/four-alternative tables). A chi-square test rejects equal SQ and ASQ rates at the 10% level in 31 of 54 cases.
- **Estimated bias model.** The pooled regression yields $\text{SQ}=0.17+0.83\,\text{NEUT}$ and $\text{ASQ}=0.83\,\text{NEUT}$ (weighted $R^2=0.72$); the ASQ intercept is insignificantly different from zero and the SQ intercept-plus-slope insignificantly different from one. So both the absolute edge $\text{SQ}-\text{NEUT}$ and relative edge $(\text{SQ}-\text{NEUT})/\text{NEUT}$ shrink as NEUT rises—*unpopular* options gain most from the status quo label.
- **No numbers effect on the equation, but a larger relative bias with more options.** Dummies are jointly insignificant, so the same equation holds regardless of alternative count; because the additive intercept is spread over more rivals, relative status quo advantage grows with the number of alternatives. Illustrative election extrapolation: an incumbent who would draw 50% in a neutral two-way race wins 59–41; with four candidates each at 25% neutral, the incumbent gets 38.5%.
- **Anchoring on continua.** In the water-allocation question, larger status quo allocations stochastically dominate smaller ones (mean allocations 153k, 183k, 200k acre-feet); adjustment is partial. The office-relocation question yields an implicit status quo "cost of moving" of about 37.8% of the move's total value (mean required rent reduction $y=22.4\%$ vs willingness $x/(1+x)=10.1\%$).
- **Sequential anchoring is real but noisier.** Versions 2 and 4 of the fleet-leasing task show statistically significant anchoring ($p=0.001$, $p=0.01/0.05$); versions 1 and 3 do not, the strongest effects appearing where many alternatives are present.
- **Field bias is large.** Old Harvard enrollees retain incumbent BCBS far more than new enrollees choose it (BCBS ~30% overall but only ~10% among new-enrollee-implied shares in some categories); TIAA-CREF allocations are essentially frozen 1981–1986 despite large swings in relative returns.

## Contribution
Coins and operationalises "status quo bias", supplying the first controlled experimental demonstration that option *labelling/position* alone shifts choice in violation of rational-choice descriptive validity, complemented by high-stakes field evidence. It distinguishes status quo bias from genuine persistence, from real transition costs (the perceived-but-unborne "cost" of switching), and from satisficing (Simon)—arguing its model better predicts *which* settings and *how much* suboptimality, unlike satisficing's silence. It connects loss aversion / the endowment effect (Thaler, Kahneman–Tversky), anchoring, sunk-cost escalation, regret avoidance, cognitive dissonance (Festinger–Carlsmith), self-perception, and illusion of control (Langer's football-card lottery: $8.67 vs $1.96 reservation price) into a single decision-making phenomenon, and sketches applications across periodic decisions, search, soft-selling, sticky wages/prices and exit barriers, market competition and pioneer-brand advantage, public policy and the Coase theorem, and Kuhnian scientific paradigm persistence.

## Limitations & open questions
The authors are explicit about gaps and hooks: (i) the experiments use hypothetical, no-stakes, compressed-time tasks and cannot themselves establish the *importance* of the bias in real private/public decisions—"we leave to future research the task of identifying the characteristics of decisions that make a strong status quo bias likely." (ii) The linear OLS specification is "rough-and-ready", ignores the 0–1 boundedness of shares (a logit would be the alternative), and pools all questions without per-question dummies due to data limits. (iii) Rational explanations (transition costs, uncertainty/search, cost of analysis) are admitted to be very hard to *disprove* and could in principle rationalise even the no-cost lab choices (Questions 1 and 5 especially), so the bias is "consistent with, but not solely prompted by" loss aversion. (iv) Whether reframing information (e.g. TIAA showing accumulation under alternative allocations without flagging the current one) could *reduce* the bias is posed as an open design question. (v) The provocative conjecture that more competitors may *reduce* effective competition, and that pioneer-brand shares (58.5/43.6/35.7%) eerily match the experimental predictions, is offered for future testing. (vi) Questions 1–3 "could be recast in continuous form" to test anchoring directly.

## Connections
The intellectual debt is squarely to Kahneman and Tversky's prospect theory (1979) and framing/anchoring work ([[@Tversky1974|Tversky–Kahneman 1974]]; Kahneman–Tversky 1984), and to Thaler's endowment effect (1980) and reluctance to trade (Knetsch–Thaler–Kahneman 1987); the fairness-as-entitlement work (Kahneman–Knetsch–Thaler 1986) supplies the wage/price-stickiness application. Savage (1954) is the rational benchmark; Simon (1957) satisficing and Nelson–Winter (1982) evolutionary search are the bounded-rationality foils. Schmalensee (1982) supplies the rational brand-loyalty model, Langer the illusion of control, Festinger–Carlsmith the dissonance evidence, and Kuhn (1962) the scientific-paradigm analogy. The paper is foundational for behavioural public economics and the later "nudge"/default-effects literature (defaults in retirement savings directly descend from the TIAA-CREF finding).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
