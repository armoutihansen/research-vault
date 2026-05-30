---
citekey: Benartzi2002
title: How Much Is Investor Autonomy Worth?
authors: ["Benartzi, Shlomo", "Thaler, Richard H."]
year: 2002
type: journalArticle
doi: 10.1111/1540-6261.00472
zotero: "zotero://select/library/items/NESZ74K5"
pdf: /Users/jesper/Zotero/storage/SJVYPDUX/Benartzi2002.pdf
tags: [literature]
keywords: [behavioral-finance, choice-overload, retirement-savings, extremeness-aversion, defined-contribution-plans, constructed-preferences, investor-autonomy]
topics: []
related: [Samuelson1988, Simonson1992, Tversky1990]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> There is a worldwide trend towards defined contribution savings plans, where investors are often able to select their own portfolios. How much is this freedom of choice worth? We present retirement investors with information about the distribution of outcomes they could expect to obtain from the portfolios they picked for themselves, and the same information for the median portfolio selected by their peers. A majority of our survey participants actually prefer the median portfolio to the one they picked for themselves. We investigate various explanations for these findings and offer some evidence that the results are partly attributable to the fact that investors do not have well-defined preferences.

## Summary
Against the standard presumption that a larger choice set cannot make a consumer worse off, Benartzi and Thaler ask whether retirement investors actually benefit from picking their own portfolios in defined-contribution (401(k)/403(b)) and privatized social-security accounts. Using survey experiments in which participants rate the *distribution of projected retirement income* (5th/50th/95th percentiles) from three unlabeled portfolios — their own, the peer average, and a peer-median (or expert-chosen) portfolio — they find that a majority prefer a portfolio someone else picked over their own. The effect survives controls for diversification, differences of opinion, and the assumed equity premium. A third experiment shows investors exhibit *extremeness aversion* over portfolios, violating independence of irrelevant alternatives, which the authors read as evidence that investors lack well-defined preferences. Bottom line: investor autonomy is "not worth much."

## Research question
Do participants in defined-contribution savings plans gain utility from the ability to choose their own retirement portfolios, and if so, is the gain worth the administrative and cognitive cost of offering many choices? The authors frame this as an *empirical* (not philosophical) question: are self-selecting investors happier with their own choices than with the choices an average peer or an expert would make for them?

## Method / identification
The core design is a within-subject revealed-preference survey run in two field settings, plus a between-subject framing experiment.

- **UCLA 403(b) survey (Section I).** 170 participants self-reported demographics and *current contribution* allocations (chosen over account balances because of documented inertia — Samuelson–Zeckhauser report a median of zero changes over a working life; Ameriks–Zeldes find 78% made no change in 10 years). For each subject, the commercial tool Financial Engines (founded by William Sharpe) projected the retirement-income distribution (5th, 50th, 95th percentiles, before-tax current dollars) for three portfolios: (a) the participant's own, (b) the peer **average** allocation, (c) a peer **median** portfolio. Because the median is ill-defined with $>2$ asset classes, they sorted portfolios by estimated risk (standard deviation $\sigma$), took the median-$\sigma$ value, then read the corresponding allocation off Financial Engines' mean–variance efficient frontier. Participants then rated three *unlabeled* portfolios A/B/C on a 1–5 attractiveness scale, not knowing one was their own. 157 of 170 completed the follow-up. Significance assessed via paired $t$-tests.
- **SwedishAmerican survey (Section II).** A sharper test: every employee is auto-assigned a portfolio by the manager ProManage; 351 (36%) *opted out* to self-direct. Surveying 59 of these self-selectors, the three portfolios rated were own / peer-average / the ProManage portfolio designed for that individual. ProManage chose the customized portfolios while Financial Engines did the projections, keeping advice and projection independent. This isolates a subpopulation that explicitly *announced a preference* for autonomy.
- **Extremeness-aversion experiment (Section III).** Between-subjects test of whether preferences are stable. Four hypothetical social-security programs A–D of increasing risk, each with two equally likely payouts: A is certain $900/month; B is 50-50 $1{,}100$/$800$; C is $1{,}260$/$700$; D is $1{,}380$/$600$ — with diminishing risk compensation capturing efficient-frontier concavity. Subjects faced one of three menus: $\{A,B,C\}$ (C framed as extreme), $\{B,C\}$ (neutral), or $\{B,C,D\}$ (C framed as middle). Since B and C appear in every condition, a rational subject's $C \succ B$ ranking must be invariant; extremeness aversion predicts $C \succ B$ is rarest in $\{A,B,C\}$ and most common in $\{B,C,D\}$. (The authors flag this as a *joint* test of extremeness aversion and Simonson–Tversky "trade-off contrast," and do not try to separate them.)

## Data
Field survey data, no archival panel. UCLA: 170 solicited / 157 completed; mean age 41, income \$54,236, balance \$44,701, annual contribution \$5,355; average own allocation 21% cash, 7% bonds, 44% large-cap, 7% international, 21% small-cap. SwedishAmerican: 351 opt-outs, 59 completed; mean age 45, income \$50,002, balance \$75,852, contribution \$4,442; average equity allocation 86% (ProManage's 92%). Extremeness experiment: $n=96$ (ABC), $80$ (BC), $100$ (BCD) UCLA staff. Income distributions supplied by Financial Engines under a 5.7% assumed equity premium.

## Key findings
- **UCLA:** Own and peer-average portfolios are statistically indistinguishable (mean ratings 3.07 vs 3.05; 42% prefer each, 16% indifferent). The peer-**median** portfolio is rated markedly higher (3.86–3.87; $t=5.80$); **62% prefer the median to their own, only 21% prefer their own.** The ranking holds within low/moderate/high own-risk subgroups.
- **Robustness:** Results are not explained by inefficiency (70% of own portfolios were already on the frontier per Financial Engines; restricting to efficient portfolios still gives 3.01 / 3.14 / 3.79), by differences of opinion (own return forecasts explain $\le 5\%$ of equity-allocation variation), by an inflated equity premium (subjects were *more* bullish than the software, implied premium $\approx 7.3\%$ vs 5.7%), or by stale preferences (subsample with low assets/contribution ratio: 2.91 / 2.99 / 3.85). Citing Brennan–Torous, a mismatched allocation is costly: for relative risk aversion of 2, moving from the optimal 100%-stock to no-stock allocation cuts expected utility by 37% over 20 years.
- **SwedishAmerican:** Even committed self-directors rate the peer average as attractive as their own (3.03 vs 2.75, $t=1.25$, insignificant) and the expert ProManage portfolio *significantly higher* than their own (3.50 vs 2.75, $t=2.84$); 61% prefer ProManage's portfolio to their own.
- **Extremeness aversion:** Share preferring $C \succ B$ rises monotonically with framing — 29.2% in $\{A,B,C\}$, 39.0% in $\{B,C\}$, 53.8% in $\{B,C,D\}$ — all differences significant at 0.05. Portfolio choice violates independence of irrelevant alternatives, just like the Simonson–Tversky camera experiment.

## Contribution
The paper empirically challenges the textbook claim that expanding the choice set is weakly welfare-improving, in the high-stakes, infrequent-choice domain of retirement savings. It introduces a clean revealed-preference yardstick — rating *unlabeled* outcome distributions of one's own vs peer/expert portfolios — and shows autonomy delivers little or negative utility. It links lab findings on constructed preferences and extremeness aversion (Lichtenstein–Slovic, Tversky–Thaler, Simonson–Tversky) to real retirement decisions, and draws concrete policy and plan-design implications: a near-maximum of benefit is reached with few options (not hundreds), and the labeling/range of "model" or "lifestyle" funds implicitly nudges allocations (e.g., the equity share implied by "the middle" portfolio depends entirely on the menu's endpoints, including under leverage).

## Limitations & open questions
- The authors explicitly **disclaim generality**: they do *not* claim people always prefer the median; investors with genuinely unusual, well-known tastes (the "Polish hip-hop" analogy) may rationally keep their own portfolio. Open question: characterize when autonomy *does* add value.
- They concede "more work needs to be done to nail [the choice-count cost-benefit] down" — the optimal number of options is left unquantified.
- The extremeness experiment is a **joint test** of extremeness aversion and trade-off contrast; disentangling the mechanisms is left open.
- Endowment/attachment may dampen the result in the field: Fellner–Guth–Maciejovsky show subjects pay to keep a self-chosen mix even when alternatives have identical risk/return; the surveys deliberately hid ownership, so measured preference for others' portfolios may overstate willingness to switch.
- Self-reported allocations (UCLA), small completed samples (59 at SwedishAmerican; even smaller analytic subsamples), use of current contributions as a preference proxy, and projections from a single vendor with one assumed return model are acknowledged measurement caveats.
- Whether one can *elicit* preferences and build a "right" portfolio is shown to be hard precisely because preferences are constructed/incoherent — an open design problem for advice tools and defaults.

## Connections
This is a behavioral-finance cornerstone within the Benartzi–Thaler retirement-savings program: it complements Benartzi & Thaler (2001) on naive "1/n" diversification and menu effects, and their (1999) work on how outcome-distribution displays drive equity allocation. It sits beside Iyengar & Lepper (2001) on choice overload (jam/chocolate experiments), the constructed-preferences/preference-reversal tradition (Lichtenstein & Slovic 1971/1973; [[@Tversky1990|Tversky & Thaler 1990]]), and [[@Simonson1992|Simonson & Tversky (1992)]] on extremeness aversion and trade-off contrast. On the welfare-cost side it draws on Brennan & Torous (1999) and Markowitz (1952) mean–variance efficiency; on inertia it uses [[@Samuelson1988|Samuelson & Zeckhauser (1988)]] and Ameriks & Zeldes (2000). The policy framing engages Diamond (2002) on social-security privatization administrative costs and Sweden's 450-fund reform, and connects to Choi et al. (2002) on defaults/implicit advice — anticipating the later "Save More Tomorrow" and libertarian-paternalism / nudge agenda.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
