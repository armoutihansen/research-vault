---
citekey: Sacerdote2001
title: "Peer Effects with Random Assignment: Results for Dartmouth Roommates"
authors: ["Sacerdote, Bruce"]
year: 2001
type: journalArticle
doi: 10.1162/00335530151144131
zotero: "zotero://select/library/items/4NGGDKMK"
pdf: /Users/jesper/Zotero/storage/ESNWGILI/Sacerdote2001.pdf
tags: [literature]
keywords: [peer-effects, random-assignment, reflection-problem, social-interactions, education-economics, natural-experiment]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper uses a unique data set to measure peer effects among college roommates. Freshman year roommates and dormmates are randomly assigned at Dartmouth College. I find that peers have an impact on grade point average and on decisions to join social groups such as fraternities. Residential peer effects are markedly absent in other major life decisions such as choice of college major. Peer effects in GPA occur at the individual room level, whereas peer effects in fraternity membership occur both at the room level and the entire dorm level. Overall, the data provide strong evidence for the existence of peer effects in student outcomes.

## Summary
Sacerdote exploits the random assignment of freshmen to dorms and roommates at Dartmouth College to estimate peer effects on academic and social outcomes free of selection bias. Because roommate background is orthogonal to own background under randomization, regressing own outcomes on randomly assigned roommate background yields causal "reduced-form" peer-effect estimates that sidestep Manski's reflection problem. He finds modest but robust peer effects on freshman GPA (operating at the room level) and strong peer effects on fraternity/sorority membership (operating at the dorm level), but essentially no peer effect on choice of major or varsity athletics. The paper is a landmark demonstration that natural-experiment randomization can credibly identify social interactions.

## Research question
Do residential peers causally affect a student's outcomes, and if so, which outcomes and at what level of aggregation (roommate vs. dorm)? More specifically: can one cleanly identify peer effects while avoiding the selection, simultaneity, and contextual-vs-endogenous identification problems that plague observational peer-effects studies?

## Method / identification
The identifying strategy is random assignment of roommates. Dartmouth's Office of Residential Life sorts housing forms into 32 blocks defined by gender and four self-reported lifestyle questions (smoking, music while studying, late hours, neatness), shuffles within blocks, and fills rooms in randomized block order. Assignment is therefore random *conditional on* the blocking covariates — exactly Rubin's [1977] "assignment to treatment group on the basis of a covariate." Identification is verified empirically: regressions of own pretreatment characteristics on roommate pretreatment characteristics (Table II) show no significant relationship (joint $F(5,1543)=0.50$, $p=.78$), whereas in the earlier non-randomized cohorts roommate math SAT predicts own SAT with a $t$-statistic of 5.0.

The structural framework posits, for roommates $i$ and $j$:
$$\text{GPA}_i = \delta + \alpha(\text{ACA}_i + \mu_i) + \beta(\text{ACA}_j + \mu_j) + \gamma\,\text{GPA}_j + \epsilon_i,$$
where $\text{ACA}$ is a single academic index (a weighted average of SAT I, SAT II, and rescaled high-school class rank) and $\mu$ is classical measurement error from not observing true ability. Here $\beta$ is the contextual (background) effect and $\gamma$ the endogenous (outcome-feedback) effect, the latter carrying a social multiplier through $1/(1-\gamma^2)$. Substituting the symmetric equation for $j$ into that for $i$ gives the reduced form
$$\text{GPA}_i = \pi_0 + \pi_1\,\text{ACA}_i + \pi_2\,\text{ACA}_j + \eta,$$
estimated by OLS with block dummies and standard errors clustered at the room level. Because roommate assignment is random, $\pi_2$ — the coefficient on roommate background — is not contaminated by selection and is interpreted causally. Separating the structural $\beta$ and $\gamma$ requires very restrictive assumptions (no unobserved background, no measurement error) and is relegated to Sacerdote [1999]. Sacerdote also reports the OLS regression of own GPA on roommate GPA, which is subject to the reflection problem and not causal but informative about outcome correlation, and probits for binary outcomes (fraternity membership, late graduation, econ major, varsity athlete). Nonlinearity and interaction are probed by interacting bottom-25 / middle-50 / top-25 percent dummies for own and roommate academic index.

## Data
Administrative records from Dartmouth's database for the graduating classes of 1997 and 1998 — the first randomly assigned cohorts. From an initial 2181 students, dropping singles (222), missing housing forms (209), substance-free-dorm placements (26), and special roommate requests (135) yields $N=1589$ (53% doubles, 44% triples, rest quads). Pretreatment covariates: SAT scores, high-school class rank, public/private high school, home state, and an admissions academic index. Outcomes: term-by-term GPA, time to graduation, fraternity/sorority membership, major, athletics. The UCLA Higher Education Research Institute Survey of Incoming Freshmen supplies two additional variables (high-school beer drinking; self-assessed probability of graduating with honors) for up to 83% of the sample.

## Key findings
- **GPA (room level).** OLS of own freshman GPA on roommate GPA gives a coefficient of $0.12$ ($t=3.1$); a one-SD increase in roommate GPA raises own GPA by about $0.05$. The effect survives dorm fixed effects, and a randomly chosen non-roommate floormate's GPA is uncorrelated with own GPA, ruling out common dorm/floor shocks. Causal background regressions show "roommate top 25 percent" raises own GPA by about $0.05$–$0.06$ (significant), while "roommate bottom 25 percent" has no effect.
- **The freshman roommate GPA effect fades by senior year** — own senior GPA is uncorrelated with freshman roommate's senior GPA — whereas own academic index predicts GPA equally in freshman and senior years.
- **Fraternity membership (dorm level).** If your randomly assigned freshman roommate joins a fraternity, you are about 8% more likely to join — striking given joining happens sophomore year. Among two-person rooms where both join, 27% join the *same* house vs. 5% under independence. The dorm-level participation rate has a much larger effect (coefficient $\approx 0.32$) than the room-level effect, and dorm-average high-school beer use predicts joining. The relevant peer group is the whole dorm.
- **No major / athletics effects.** Roommate's economics major does not predict own ($\partial y/\partial x = -0.018$, $t=-0.69$); a contingency-table test accepts independence in major choice. Roommate varsity-athlete status does not predict own.
- **Nonlinearity / interactions.** Little evidence of nonlinearity (spline slopes statistically equal). Modest interaction evidence: a top roommate helps a bottom student — $(\text{own}=\text{bottom},\text{roommate}=\text{bottom})$ effect $-0.331$ vs. $(\text{own}=\text{bottom},\text{roommate}=\text{top})$ effect $-0.16$ ($p=.013$).

## Contribution
Provides among the cleanest early causal estimates of peer effects by leveraging genuine random assignment, thereby solving the selection problem and obtaining reduced-form estimates immune to Manski's reflection problem. Demonstrates that the relevant reference group is outcome-specific (room for GPA, dorm for fraternities), and that peer effects vary sharply across outcomes — present for effort/social affiliation, absent for major. Establishes the roommate natural experiment as a workhorse research design.

## Limitations & open questions
- Roommate estimates are an explicit **lower bound** on total peer influence, since students interact with many non-roommate peers; the framework cannot net these out.
- The reduced form **does not separate contextual ($\beta$) from endogenous ($\gamma$) effects** without very restrictive assumptions, so social-multiplier magnitudes are not identified here.
- Mechanisms (social learning, agglomeration, endogenous preference formation) are **not distinguished**.
- External validity: subjects are older, on-campus, and a highly selected, low-heterogeneity group; effects "may be even more critical and long lasting earlier in students' lives... or in a context where there is more student heterogeneity." Sacerdote names replication in other educational settings as "a fruitful area of future research."
- The "27 percent as large as the own effect" headline magnitude is **not robust** to which own/roommate coefficients are compared.

## Connections
The identification problem is framed entirely around Manski [1993] (reflection problem; contextual vs. endogenous effects). The paper is a near-twin of Zimmerman [1999] (Williams College roommates), reaching consistent conclusions on modest GPA peer effects and own-roommate background interactions. It builds on the social-interactions modeling of Glaeser, Sacerdote, and Scheinkman [1996] (crime and social interactions, explaining cross-dorm variance in fraternity participation) and the measurement framework of Glaeser and Scheinkman [1998]. It contrasts with instrument-based approaches — Case and Katz [1991], Gaviria and Raphael [1999], Borjas [1992], Evans, Oates, and Schwab [1992] — whose exogeneity is harder to defend. Motivating peer-effects literature includes the Coleman Report [1966], Harris [1998] (the "nurture assumption"), and neighborhood work (Jencks and Mayer [1990]; Katz, Kling, and Liebman [2001], Moving to Opportunity). Policy stakes connect to the school-choice and tracking debates (Epple and Romano [1998]; Hoxby [2000]; Kremer [1997]). The methodological lineage runs through Rubin [1977] on covariate-based assignment.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
