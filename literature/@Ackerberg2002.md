---
citekey: Ackerberg2002
title: Endogenous Matching and the Empirical Determinants of Contract Form
authors: ["Ackerberg, Daniel A.", "Botticini, Maristella"]
year: 2002
type: journalArticle
doi: 10.1086/339712
zotero: "zotero://select/library/items/K45ULT47"
pdf: /Users/jesper/Zotero/storage/2KENSVV6/Ackerberg and Botticini - 2002 - Endogenous Matching and the Empirical Determinants.pdf
tags: [literature]
keywords: [endogenous-matching, contract-theory, principal-agent, risk-sharing, instrumental-variables, moral-hazard, sharecropping]
topics: []
related: [Prendergast2002a]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero) — Empirical work on contracts typically regresses contract choice on observed principal and agent characteristics. If (i) some of these characteristics are unobserved or partially observed and (ii) there are incentives whereby particular types of agents end up contracting with particular types of principals, estimated coefficients on the observed characteristics may be misleading. The authors address this endogenous matching problem using a data set on agricultural contracts between landlords and tenants in early Renaissance Tuscany. Controlling for endogenous matching has an impact on parameters of interest, and tenants' risk aversion appears to have influenced contract choice. (Reconstructed from the paper's own summary; not the verbatim Zotero abstract, which is empty.)

## Summary
Standard empirical contract-choice studies regress the observed contract form (share vs. fixed-rent, or royalty rate) on observed principal, agent, and task characteristics. Ackerberg and Botticini argue this is biased whenever (a) some relevant characteristics are only observed via proxies and (b) heterogeneous principals and agents endogenously *match* on those characteristics. Matching makes one party's observed traits correlate with the other party's proxy error, contaminating essentially all coefficients of interest. They propose three fixes — geography-based instruments for the matching equation, covariance sign-restriction arguments, and panel/fixed-effects techniques — and apply them to landlord–tenant contracts from the 1427 Florentine catasto. Correcting for matching roughly doubles the estimated wealth (risk-aversion proxy) coefficient and weakens the crop coefficient, recovering evidence for risk sharing that the prior literature had largely failed to find.

## Research question
Do standard regressions of contract form on observed principal/agent characteristics yield misleading coefficients when principals and agents match endogenously on partially observed traits — and once that bias is corrected, is there evidence that risk sharing (and multitasking) actually determines agrarian contract choice?

## Method / identification
The structural setup is a moral-hazard model with full information between the contracting parties. The second-best contract $y$ is linear in principal/task characteristics $p$ and agent characteristics $a$:
$$y = b_0 + b_1 p + b_2 a + e,$$
where $e$ is optimization/measurement error uncorrelated with $p$ and $a$. The econometrician does not observe $a$ (e.g. risk aversion) but a proxy $w$ (wealth) with $a = vw + h$, $h$ mean-independent of $w$. Substituting:
$$y = b_0 + b_1 p + b_2 v w + b_2 h + e,$$
so the targets are $b_1$ and the product $b_2 v$. Endogenous matching is modeled by a linear matching equation
$$p = \gamma_0 + \gamma_1 a + \nu = \gamma_0 + \gamma_1 v w + \gamma_1 h + \nu,$$
where $\nu$ is matching error (search frictions). Without $\nu$, $p$ and $w$ would be collinear and identification hopeless. The core problem: matching makes $p$ correlate with the unobserved proxy component $h$, hence with the composite error $b_2 h + e$ in the choice equation, biasing both $b_1$ directly and $b_2 v$ indirectly.

Three solutions are developed. (1) **Instrumental variables**: find an instrument $z$ that shifts matching but is excludable from the choice and proxy equations. Their preferred instruments are market (town) dummies and town dummies interacted with $w$ — valid because, across geographically isolated markets with different exogenous distributions of $p$, the *slope* of the matching equation differs. Market of residence is excludable from the structural choice equation since theory says only fundamental characteristics matter (modulo income effects on risk aversion, assumed negligible under CARA). (2) **Covariance/sign-restriction**: the observed correlation between $p$ and $w$ signs the unobserved correlation between $p$ and $h$, letting one sign the OLS biases; a first-stage with no $p$–$w$ correlation suggests no matching. (3) **Panel/fixed effects**: landlord fixed effects absorb time-constant unobserved principal traits, handling two-sided matching. Empirically they run linear probability, probit, landlord fixed-effects, linear IV, fixed-effects IV, and a full-information maximum-likelihood (FIML) model coupling an ordered-probit matching equation with the contract-choice equation.

## Data
The 1427 Florentine catasto (a comprehensive Tuscan census and property survey): 902 land plots/contracts held by 128 landlords across three economically isolated towns — Florence, Pescia, San Gimignano. Variables: contract type (62.6% share, 37.4% fixed-rent), crop type (vines/perennial, cereals/annual, or mixed; coded crop = 1 vines, .5 mixed, 0 cereals), and tenant wealth in florins (mean 82.5, proxy for risk aversion). Migration across towns was low (3–13%), supporting the "market is exogenous" instrument assumption. Crucially, land-type distributions differ sharply across towns (e.g. Pescia 75% cereals, San Gimignano 85% mixed), generating exogenous variation that identifies matching.

## Key findings
- Strong evidence of matching: regressing crop on town dummies and wealth (the matching equation) yields a significant *negative* relation — poorer tenants cultivate vines. The slope coefficients $\gamma_1$ differ significantly across towns (all pairwise bootstrapped $p<0.05$), giving valid instruments.
- Naive OLS/probit: crop strongly negative and significant; wealth positive but only mixed/marginal significance (weak in the Pescia–San Gimignano subsample).
- Correcting for matching (IV and fixed-effects IV) makes the **crop coefficient smaller and far less significant**, while the **wealth coefficient grows in magnitude** — in the least-restrictive fixed-effects IV spec the wealth coefficient more than doubles (0.0242 → 0.0530) and becomes significant. Since wealth proxies risk aversion, this revives support for risk sharing.
- The negative matching direction (risk-averse, poor tenants on vines) is read as more consistent with the Holmstrom–Milgrom (1991) multitasking story than with pure crop-riskiness risk sharing.
- The FIML model exposes "bad" identification from nonlinearity of the ordered-probit matching equation; isolating only the good (cross-region) identification leaves both crop and wealth significant.

## Contribution
Brings the largely theoretical matching literature to bear on applied contract-choice econometrics, showing that endogenous principal–agent matching is a distinct and serious identification threat beyond ordinary measurement error, and that examining the matching equation is itself economically informative. Provides concrete IV, covariance, and panel solutions, and supplies rare empirical evidence for risk sharing in agrarian contracts where the prior literature found little.

## Limitations & open questions
- The IV exclusion restriction requires that crop and wealth coefficients be identical across towns; possible cross-town differences in soil/climate or in insurance/capital markets (especially Florence) could invalidate it — they mitigate by also estimating on Pescia–San Gimignano only.
- The proxy-equation instrument validity needs markets to be isolated (no economically motivated migration); only approximately satisfied.
- Nonlinear FIML identification is partly driven by functional-form assumptions ("bad" identification not robust to alternative forms of $w$).
- They do not model *how* matching occurs; an explicit open direction is to build a fully specified structural model from primitives (utility/production functions) jointly modeling matching and contract choice.
- Exact contract shares are mostly unobserved (treated as binary share vs. fixed-rent); limited-liability explanations for the wealth–contract link cannot be fully ruled out.

## Connections
Builds directly on the authors' companion work, Ackerberg and Botticini (2000), which ignored matching, and the working paper Ackerberg and Botticini (1999). The motivating empirical puzzle is Allen and Lueck (1992, 1995, 1999) finding little risk-sharing evidence; [[@Prendergast2002a|Prendergast (2002)]] offers alternative explanations. The theoretical contracting backbone is Holmstrom and Milgrom (1987, 1991, 1994), Grossman and Hart (1983), Mirrlees (1974), and Stiglitz (1974); multitasking specifically follows Holmstrom and Milgrom (1991). On empirical matching it relates to Foster (1998) on marriage markets, MacLeod and Parent (1999) on labor contracts, and Dubois (2002) on endogenous crop choice; theoretical matching-with-contracting models include Shimer and Smith (2000) and Legros and Newman. The market-instrument identification strategy parallels the hedonic identification literature (Epple 1987; Kahn and Lang 1988; Brandt and Hosios 1996). The Tuscan data extend Pudney, Galassi, and Mealli (1998), with historical context from Fenoaltea (1984), Hoffman (1984), and Botticini (2000).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
