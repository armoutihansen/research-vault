---
citekey: Lazear2000
title: Performance pay and productivity
authors: ["Lazear, Edward P."]
year: 2000
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/L8GSXB99"
pdf: /Users/jesper/Zotero/storage/2Y29HUI2/Lazear2000.pdf
tags: [literature]
keywords: [performance-pay, piece-rates, incentives, worker-sorting, personnel-economics, productivity]
topics: []
related: [Gneezy2000, Lazear1981]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Lazear exploits a natural experiment at Safelite Glass Corporation, which between 1994 and 1995 switched its autoglass installers from hourly wages to a piece-rate scheme (with a wage guarantee). A simple model of heterogeneous workers predicts that the switch raises average output, attracts and retains more able workers, and increases the variance of output. Using monthly worker-level output (units-per-associate-per-day) on roughly 31,000 person-months, all predictions are confirmed: productivity rises about 36% overall, of which roughly 20 percentage points is a pure within-worker incentive effect and the remainder reflects sorting/selection. About half of the worker-specific productivity gain is passed back to workers as higher pay.

## Research question
What happens to productivity, worker composition, and the distribution of output when a firm switches from paying hourly wages (with a minimum output standard) to paying piece rates? Can a clean before-and-after, within-worker comparison separate the incentive effect from sorting and confirm that workers respond to monetary incentives as standard price theory predicts (refuting claims that monetizing incentives reduces output)?

## Method / identification
The paper combines a theoretical model with a panel before-and-after design.

Theory. Workers differ in ability $A$ with density $g(A)$ and distribution $G(A)$. A worker of ability $A$ producing output $e$ has utility
$$\text{Utility} = \text{Income} - \frac{C(e)}{A},$$
with $C'>0$, $C''>0$, so higher-ability workers bear lower disutility for any output. Under an hourly wage the firm posts a wage $W$ and a minimum standard $e_0$; all hired workers produce exactly $e_0$. The marginal accepted worker $A_0$ satisfies $W = C(e_0)/A_0$, and the upper cutoff $A_h$ solves $W - C(e_0)/A_h = R(A_h)$, where $R(A)$ (with $R'(A)>0$) is the rent obtainable elsewhere. The firm chooses $(e_0, W)$ to maximize
$$\max_{e_0, W} \int_{A_0}^{A_h}\left(e_0 - \frac{C(e_0)}{A}\right) g(A)\,dA,$$
yielding first-order conditions implying $C'(e_0)/A_0 > 1$: the standard forces the least able to overproduce relative to their efficient level while the most able underproduce — the hourly contract is a compromise optimal for almost no one. Under a linear piece rate $be - K$, a risk-neutral worker chooses $e$ from $C'(e)/A = b$, so output becomes type-specific. Safelite's actual scheme is a guaranteed draw plus piece rate, $\text{Compensation} = \max[W,\, be - K]$. Three propositions follow: (1) effort weakly rises and strictly rises for high enough $b$; (2) average ability of the workforce rises (the lower cutoff is unchanged, $A_0^* = A_0$, while the upper cutoff rises, $A_h^* > A_h$); (3) the variance of ability and output rises — both because high types now sort in and because output is type-specific rather than pinned at $e_0$. The sufficient condition for (2) and (3) is that some workers take the guarantee while others produce on the piece-rate portion.

Identification. The empirical strategy regresses $\ln(\text{UAD})$ on a PPP dummy plus month and year dummies; adding worker fixed effects (3,181 individual dummies) isolates the within-worker incentive effect from sorting. A tenure/PPP-tenure specification rules out a Hawthorne (transitory) effect. Separations are modeled with logits of a SEPAR dummy on PPPFLAG, UAD, and their interaction to test the sorting predictions.

## Data
Personnel records from Safelite Glass Corporation (Columbus, Ohio), the largest US autoglass installer. The PPP (performance pay plan) was phased in over 18 months, so most workers are observed under both regimes. Unit of observation is the person-month: 38,764 person-months over 19 months (about 2,040 workers/month, 3,707 distinct installers), with 31,104 "good" person-months after dropping partial months. Key variable is UAD (units-per-associate-per-day; mean 2.96, SD 1.53). Other variables include base hourly rate ($11.47), actual pay ($2,250/month), PPP-formula pay, cost-per-unit, sick hours, and a separation dummy.

## Key findings
- Proposition 1 (effort/output). Mean UAD is 20% higher under piece rates in raw means (2.69 to 3.23); with month/year controls the PPPFLAG coefficient on $\ln(\text{UAD})$ is 0.36 — a 36% firm-wide productivity gain.
- Decomposition. Adding worker fixed effects drops the coefficient to 0.20 — a pure within-worker incentive effect (a given worker installs 20% more after the switch). Roughly 5/9 of the 36% is incentives; the rest is sorting and the phase-in pattern.
- No Hawthorne effect. PPPTENUR has a positive coefficient (0.26) on top of a 0.29 PPPFLAG coefficient, so the effect grows over time (to about 55% after a year) rather than decaying.
- Proposition 2 & 3 (sorting and variance). Output SD rises (1.41 to 1.58). Turnover rises overall (~+0.7 pp/month) but the UAD×PPPFLAG interaction in the separation logit is negative: high-ability workers are retained, low-ability workers leave. Histograms shift right (modal worker moves from 2–3 to 3–4 units/day).
- Rent sharing. Within-worker pay rises 9.6% while within-worker output rises 20%, so incumbents capture about half the return to their own productivity gain. Firm-wide wage cost rises only ~6.5% against the 36% output gain, so profitability rises.
- Side effects. Paid sick hours fall ~60% (almost entirely via sorting, not within-worker behavior).

## Contribution
Provides rare, clean field evidence — a within-firm, within-worker before/after comparison — that pay-for-performance raises productivity, and quantifies the unusually large magnitude (36% firm-wide, 20% pure incentive). It cleanly decomposes the total effect into incentive versus sorting/selection channels, documents that piece rates raise the mean, variance, and upper tail of the ability distribution exactly as theory predicts, and shows roughly half the gain is shared with workers. It directly refutes sociological claims that monetizing incentives lowers output, and frames compensation choice as an equilibrium trade-off between productivity gains and measurement/quality/risk costs.

## Limitations & open questions
- A single firm and a single data point: "the case for piece rates seems especially strong" here because output is easily measured and quality defects (broken windshields) are quickly detected and attributable. Managerial and professional jobs may not be suited to piecework — generalizability is explicitly limited.
- Profitability is inferred, not directly measured: no data on the implementation/measurement costs of the monitoring system are available, so the welfare conclusion rests on the assumption that these costs do not swamp the gains.
- Ability is unobserved and proxied by realized output, confounding ability with tenure (the new-hire ability comparison must be tenure-adjusted).
- Quality is handled institutionally (re-do at own cost, peer pressure) rather than measured; the paper does not estimate the quality cost of piece rates.
- The selection/equilibrium question — why some firms optimally retain hourly wages — is posed but not estimated; measuring the cost side of the compensation-choice trade-off is left open.

## Connections
Builds directly on Lazear (1986) "Salaries and Piece Rates," which sets out when output-based pay is optimal, and on the tournament/incentive tradition of [[@Lazear1981|Lazear & Rosen (1981)]]. The measurement-cost concerns draw on Baker (1992) on incentive contracts and performance measurement, and Fama (1991) on time- versus output-based pay. The peer-pressure quality mechanism comes from Kandel & Lazear (1992). Related empirical pay-method work includes Brown (1992) on wage levels and methods of pay, Paarsch & Shearer (1996) on tree planters in British Columbia (output gains but faster fatigue), and Fernie & Metcalf (1996) on jockeys. The behavioral counterclaim it refutes — that extrinsic monetary incentives can crowd out effort — connects to the motivation-crowding literature (e.g., Frey & Oberholzer-Gee 1997; [[@Gneezy2000|Gneezy & Rustichini 2000]]) and the early piece-rate discussion in Slichter (1928).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
