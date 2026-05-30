---
citekey: Frank2014
title: Expenditure cascades
authors: ["Frank, Robert", "Levine, Adam", "Dijk, Oege"]
year: 2014
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/U9GMXWZ9"
pdf: /Users/jesper/Zotero/storage/4IRMYMMU/Frank2014.pdf
tags: [literature]
keywords: [relative-income-hypothesis, expenditure-cascades, conspicuous-consumption, income-inequality, savings-rate, financial-distress]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Prevailing economic models of consumer behavior completely ignore the well-documented link between context and evaluation. We propose and test a theory that explicitly incorporates this link. Changes in one group's spending shift the frame of reference that defines consumption standards for others just below them on the income scale, giving rise to expenditure cascades. Our model, a descendant of James Duesenberry's relative income hypothesis, predicts the observed ways in which individual savings rates respond to changes in both own and others' permanent income, as well as numerous other stylized fact patterns that are difficult to reconcile with prevailing models.

## Summary
Frank, Levine, and Dijk revive Duesenberry's relative income hypothesis to explain why U.S. savings rates have fallen and household financial distress has risen as income inequality has grown. Their core idea is the *expenditure cascade*: when those at the top of a reference group spend more, they shift the consumption frame for the people just below them, who spend more in turn, propagating the impulse down the income ladder. A simple recursive consumption model formalizes this, and first-difference regressions on U.S. county-level Census data (1990–2000) show that rising local inequality is positively and significantly associated with three observable proxies for financial distress: bankruptcy filings, divorce, and long commutes.

## Research question
Why is observed consumption (and the corresponding decline in savings) so much larger than the permanent income / life-cycle hypotheses predict, and does growing income inequality within local reference groups causally drive households below the top to spend more and save less? More generally, can a context-dependent (relative income) model of consumption account for stylized facts that the standard absolute-income models cannot?

## Method / identification
The paper contrasts two consumption models. The permanent income benchmark sets consumption proportional to permanent income,
$$C_i = k Y_i,$$
which implies that spending is independent of others' incomes, $dC_i/dY_j = 0$ for all $i \ne j$, so distributional changes leave individual spending unchanged. The authors instead adopt a relative-income variant in which consumers are ranked in descending order of permanent income and each is influenced by the consumption of the person ranked just above them:
$$C_i = k(1-a) Y_i + a\, C_{i+1},$$
where $a \in [0,1]$ governs the strength of the upward demonstration effect. At $a=0$ the model collapses to the permanent income hypothesis; at $a=1$ spending is set entirely by the next-higher consumer. The recursion implies that a $\$100$ increase in spending by one consumer raises the spending of the four people ranked just below by $100a$, $100a^2$, $100a^3$, $100a^4$ respectively — the cascade. A numerical illustration with an 11-member reference group, $k=0.8$, $a=0.5$ shows that raising only the top two incomes lowers the savings rates of everyone below and cuts the group's average savings rate.

Because individual reference groups are unobservable, the empirical test proxies reference-group inequality by geographic-area inequality (preferring narrow units: 100 most populous U.S. counties over states). Inequality is measured by the Gini coefficient (preferred for Lorenz consistency) and the P90/P50 ratio. The Census lacks county savings data, so the authors test footprints of financial distress instead. Estimation uses a first-difference specification to absorb area fixed effects:
$$\Delta \text{dep}_i = a + b\,\Delta \text{ineq}_i + c\,\Delta x_i + \Delta u_i,$$
with $\Delta$ taken between 1990 and 2000 (both at similar business-cycle points), and $x_i$ a vector of economic and socio-demographic controls drawn from each outcome's prior literature. White's test checks for heteroskedasticity.

## Data
U.S. Decennial Census micro and summary files for 1990 and 2000, for the 50 states and the 100 most populous counties. Outcomes: non-business bankruptcy filings (American Bankruptcy Institute, 1989/1999), proportion of the population aged 15+ currently divorced, and proportion of workers with a daily commute of one hour or more. Inequality variables (Gini, P90/P50) computed from Census income data; controls include income at the 20th/50th percentile, two-worker share, unemployment, household size, race shares, age shares, education, women's labor-force participation, welfare benefits, density, and population.

## Key findings
- Bankruptcy: a 1% rise in the Gini is associated with a 7.39% rise in non-business bankruptcies ($p=0.002$). Given the average 4.41% Gini increase, this implies roughly a 33% increase in filings — plausible against the observed 148% average rise. Absolute income of the 20th-percentile earner has a small negative, significant effect.
- Divorce: a 1% rise in the Gini is associated with a 0.49% increase in the share currently divorced (marginally significant), implying about a 2.16% increase given the average Gini change.
- Commuting: a one-unit rise in the Gini ($\Delta\text{Gini}$ specification) is associated with a 0.392 rise in the share with hour-plus commutes; the average Gini increase of 0.018 implies +0.0071 in that share (about 7,000 people per million workers).
- All three results are robust across state and county samples (county fits are tighter) and are consistent with the cascade model but not the permanent income hypothesis.
- The model also rationalizes the U.S.–Europe savings gap (mirroring the inequality gap) and Duesenberry's observation that, holding absolute income fixed, black families in segregated neighborhoods saved at higher rates than white families.

## Contribution
The paper formalizes and empirically operationalizes the relative-income / demonstration-effect tradition (Duesenberry, Veblen) as a tractable recursive consumption model, and supplies cross-sectional, area-level evidence linking local inequality to multiple independent measures of household financial distress. It offers a unified account of falling savings rates, rising debt, and cross-national savings differences that the dominant absolute-income models cannot generate.

## Limitations & open questions
- Personal reference groups are unobservable; the authors use geographic inequality as a crude proxy and cannot directly observe how a person responds to *their own* reference group's spending — they flag this explicitly as the ideal test they cannot run.
- The Census provides no household savings rates by area, forcing reliance on indirect distress proxies rather than savings directly.
- County-level analysis uses nominal (not real) income for lack of local price indices.
- The structural parameter $a$ (strength of upward comparison) is not estimated; the model is illustrative rather than fully identified.
- The rationality question is left open: the authors argue context-responsiveness need not imply myopia (school quality tied to local property values; interview-suit signaling), but concede myopia is psychologically salient and that whether top spending induces others to spend more must ultimately be settled empirically.

## Connections
The model is an explicit descendant of Duesenberry (1949) and draws on Veblen's (2001/1899) conspicuous consumption and Frank's own *Choosing the Right Pond* (1985). It positions itself against the permanent income hypothesis of Friedman (1957) and the life-cycle model of Modigliani & Brumberg (1955), citing Mayer (1972) on why savings rates rise with permanent income. On why the rich save more it connects to Carroll (1998) and Dynan-type work; on inequality and emulation to Bowles & Park (2005). The myopia discussion engages the self-control and hyperbolic-discounting literature: Thaler & Shefrin (1981), Laibson (1998), and O'Donoghue & Rabin (1999). The empirical proxies build on prior literatures in bankruptcy (Fay, Hurst & White, 2002; White, 2007), divorce (Stevenson & Wolfers, 2006, 2007; Friedberg, 1998), and commuting (Khattak et al., 2000; Levinson & Kumar, 2006). Inequality measurement draws on Wolff (2002) and Smeeding (2001).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
