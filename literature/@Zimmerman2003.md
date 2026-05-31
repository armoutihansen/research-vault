---
citekey: Zimmerman2003
title: "Peer Effects in Academic Outcomes: Evidence from a Natural Experiment"
authors: ["Zimmerman, David J."]
year: 2003
type: journalArticle
doi: 10.1162/003465303762687677
zotero: "zotero://select/library/items/DHFI2HU6"
pdf: /Users/jesper/Zotero/storage/D7QQ5JXQ/Zimmerman2003.pdf
tags: [literature]
keywords: [peer-effects, natural-experiment, random-assignment, education-economics, roommate-effects, causal-identification]
topics: ["[[peer-effects-social-interactions]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> I use data from Williams College to implement a quasi-experimental empirical strategy aimed at measuring peer effects in academic outcomes. In particular, I use data on individual students' grades, their SAT scores, and the SAT scores of their roommates. I argue that first-year roommates are assigned randomly with respect to academic ability. This allows me to measure differences in grades of high-, medium-, or low-SAT students living with high-, medium-, or low-SAT roommates. With random assignment these estimates would provide compelling estimates of the effect of roommates' academic characteristics on an individual's grades. I also consider the effect of peers at somewhat more aggregated levels. In particular, I consider the effects associated with different academic environments in clusters of rooms that define distinct social units. The results suggest that peer effects are almost always linked more strongly with verbal SAT scores than with math SAT scores. Students in the middle of the SAT distribution may have somewhat worse grades if they share a room with a student who is in the bottom 15% of the verbal SAT distribution. The effects are not large, but are statistically significant in many models.

## Summary
Zimmerman exploits the quasi-random assignment of first-year roommates at Williams College as a natural experiment to measure academic peer effects, sidestepping the selection bias that plagues most of the peer-effects literature. Regressing students' grades on their own SAT scores and their roommate's SAT scores, he finds that average peer effects are small and frequently statistically zero. The clearest signal is that students in the middle 70% of the ability distribution earn modestly lower grades (about 0.06-0.09 GPA points) when paired with a roommate in the bottom 15% of the *verbal* SAT distribution, while students at the top and bottom appear largely unaffected. The effects are real but economically minor.

## Research question
Do the academic characteristics of one's peers (here, a roommate's SAT score) causally affect one's own academic performance (grades)? And, by extension, is the peer-effects production technology nonlinear — i.e., are weak, average, or strong students differentially helped or hurt by exposure to weak or strong roommates?

## Method / identification
The core specification is the standard peer-effects regression
$$O_{ic} = \alpha + \beta_1 C_{ic} + \beta_2 C^{Peer}_{ic} + \epsilon_{ic},$$
which is biased whenever peers are non-randomly assigned, i.e. when $\operatorname{cov}(C^{Peer}_i, \epsilon_i) \neq 0$. Zimmerman's identification strategy is to find a setting where $\operatorname{cov}(\mathrm{SAT}^{RM}, \epsilon_{ic}) = 0$ holds by design. He estimates
$$\mathrm{GPA}_{ic} = \alpha + \gamma_c + \beta_1 \mathrm{SAT}_i + \beta_2 \mathrm{SAT}^{RM}_i + \beta_3 X_i + \epsilon_{ic},$$
where $\mathrm{SAT}^{RM}$ is the first-year roommate's SAT (entered combined, or split into verbal and math, and sometimes nonlinearly via bottom-15% / middle-70% / top-15% bins), $\gamma_c$ are cohort fixed effects, and $X_i$ includes race, gender, citizenship, and major dummies. Standard errors are clustered at the roommate level.

The identifying claim is that the Williams Housing Office assigns roommates using only a lifestyle-preference form (single/double, smoking, visitors, noise, neatness, sleep patterns, music/activity tastes) — never SAT, prior achievement, ethnicity, or athletic status. Zimmerman explicitly models the threat: he lets latent "roommate quality" $Q$ depend on SAT *and* on a housing-preference index $H$, with $H$ itself correlated with SAT and with the roommate's $H$. Substituting through yields a reduced form $\mathrm{GPA}_{ic} = \Pi_0 + \Pi_1 \mathrm{SAT}_i + \Pi_2 \mathrm{SAT}^{RM}_i + \eta_i$ in which $\Pi_2$ is biased only if some preference is *both* correlated with SAT and a determinant of GPA *and* heavily weighted in matching. He cannot build an instrument (no data), so instead validates randomness empirically: for the class of '02 he regresses each housing preference on SAT (bivariate) and on GPA (controlling for own SAT, race, gender, citizenship). Only three preferences (least-preferred activity = cultural; least-preferred music = heavy metal or rap) are significant in both — and these are precisely the items the Housing Office weights least, supporting conditional random assignment. He also studies higher aggregates: the SAT composition of the "entry" (a dorm cluster sharing a common space, a surrogate "family" with assigned junior advisors) and the SAT scores of the junior advisors (JAs) themselves.

## Data
Administrative records from Williams College for the entering classes of 1990 through 2001 — roughly 3,151 students with a single roommate in the main regressions (average class size 522). Variables: first-semester and cumulative GPA, own verbal/math/combined SAT, roommate's SAT, entry-level average SAT, JA SAT, plus race, gender, citizenship, and major. A separate class-of-'02 sample (n = 519) with retained housing-preference forms is used for the randomization check. No instrument is available; earlier preference forms were destroyed.

## Key findings
1. **Average roommate effect is essentially zero.** With combined SAT entered linearly (Table 3), the roommate's SAT coefficient is ~0.006-0.007 and insignificant, for both first-semester and cumulative GPA. Own SAT is large (~0.15-0.16 GPA points per 100 points) and persists to graduation.
2. **Verbal dominates math.** When verbal and math are split, the roommate's *verbal* SAT is significant (~0.03 GPA points per 100 points, about 15% of the own-verbal effect) while the roommate's math SAT is not.
3. **Nonlinearity by own ability (Table 4).** Allowing the effect to vary by the student's own SAT bin, peer effects appear only for the *middle 70%*: such a student earns about 0.077 fewer GPA points with a bottom-15%-verbal roommate than with a top-15%-verbal roommate — enough to move a median student to roughly the 42nd percentile. Top- and bottom-15% students are unaffected. The middle-vs-top gap (−0.077 vs −0.038) is not itself statistically distinguishable.
4. **Gender heterogeneity (Table 5).** For men, a bottom-15%-verbal roommate lowers GPA by ~0.088 (median student to ~38th percentile). For women, no verbal effect; instead a small *positive* math effect (+0.070) for middle women with a low-math roommate.
5. **Entry and JA effects are weak (Table 6).** The aggregate SAT composition of the entry and the SAT scores of junior advisors are mostly insignificant; the room/roommate is the meaningful locus.
6. Results are robust to house fixed effects (within-dorm variation), to including multi-roommate rooms, and to moderate changes in percentile cutoffs.

## Contribution
This is a foundational "credibly causal" peer-effects paper. By locating a setting with genuine random assignment of peers, it disentangles true peer influence from the "birds of a feather flock together" selection that confounds earlier work (e.g., Coleman 1966; Evans, Oates & Schwab 1992; Rivkin 1997). The roommate-randomization design became a template for a large subsequent literature on social interactions, and the substantive message — that academic peer effects are real but small, asymmetric (verbal > math), and concentrated among middle-ability students exposed to very weak peers — directly informs debates on tracking, school choice, affirmative action, and the customer-input technology of higher education.

## Limitations & open questions
- **No instrument.** Randomness is argued and validated indirectly via the preference-form regressions; the ideal IV or direct control for the Housing Office's exact matching function is infeasible because of limited form data and small cell sizes under nonlinearity. The author flags this as the central caveat.
- **External validity to a single elite school.** Effects are measured within a highly selective institution where even the bottom-15% student sits near the 75th national percentile; the nonlinearity found here is *not* the same as moving a weak student between resource-poor and resource-rich schools (where peer *and* other resources change jointly).
- **Admissions-induced selection.** Selective admission of low-SAT students conditional on high non-academic qualities ($H$) compresses the variance of latent quality $Q$, potentially attenuating estimated effects; the sign of any residual bias is ambiguous.
- **Mechanism unidentified.** The paper documents the reduced-form grade effect but cannot say *why* verbal composition matters more, why only middle students respond, or why the gender patterns differ — open hooks for mechanism research.
- SAT and grades are imperfect proxies for peer quality and for learning, respectively.

## Connections
Methodologically descends from the selection-bias critique of Evans, Oates & Schwab (1992) and Rivkin (1997), and from Coleman et al. (1966), the canonical (selection-prone) peer-effects study. The nonlinearity theme — mixing may raise aggregate learning if weak students gain more than strong students lose — echoes Henderson, Mieszkowski & Sauvageau (1978) and Robertson & Symons (1996), and connects to Epple & Romano's (1998) theoretical model of school choice with peer-group complementarities. The wage-inequality angle links to Hoxby (1998). Within higher education it updates Hall & Willerman (1963), an early Minnesota roommate study. The social-comparison microfoundations draw on Festinger (1950, 1954) and Goethals, Winston & Zimmerman (1999). It is a direct intellectual precursor to the broad roommate-randomization and social-interactions literature (e.g., Sacerdote and later work).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
