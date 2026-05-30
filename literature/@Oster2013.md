---
citekey: Oster2013
title: "Limited Life Expectancy, Human Capital and Health Investments"
authors: ["Oster, Emily", "Shoulson, Ira", "Dorsey, E. Ray"]
year: 2013
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/JZUMFT3Z"
pdf: /Users/jesper/Zotero/storage/JRWE3HAM/Oster2013.pdf
tags: [literature]
keywords: [human-capital, life-expectancy, health-capital, natural-experiment, education, competing-mortality-risks]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Oster, Shoulson, and Dorsey use individuals at risk for Huntington disease (HD) as a natural experiment to estimate the causal effect of life expectancy on human-capital investment. Because HD is a single-gene autosomal-dominant disorder with predictive genetic testing and slow, age-variable symptom onset, the authors can compare otherwise-similar people who differ only in what they know about their own (sharply truncated) life expectancy. Learning one carries the HD mutation — via testing or via early symptom onset — substantially lowers post-secondary education and promotion-oriented job training, with no effect on pre-revelation decisions (high-school completion). The implied elasticity of demand for college with respect to life expectancy is about 1.0; the same revelation also reduces smoking cessation and cancer screening, supporting the competing-mortality-risk / health-capital corollary.

## Research question
Does longer life expectancy causally raise human-capital investment, as the Becker–Ben-Porath human-capital model predicts? And quantitatively, how large is the elasticity of educational (and health-capital) investment with respect to life expectancy, so that it can be used to calibrate growth models and decompose cross-country and over-time variation in schooling?

## Method / identification
The paper exploits within-at-risk-population variation in *when* an individual learns they carry the HD mutation, holding the genetic 50-percent-risk baseline fixed. Two complementary identification strategies are used.

(1) **Genetic testing.** Among asymptomatic individuals tested young (at or before age 28, no symptoms by 35), the authors estimate
$$D_i = \alpha + \beta_1(\text{Tested Negative})_i + \beta_2(\text{Tested Positive})_i + \gamma X_i + \varepsilon_i,$$
where $D_i$ is an education outcome, $X_i$ are demographic controls (gender, country, recruitment method), and untested individuals form the omitted category. The key contrast is $\beta_1$ versus $\beta_2$ (negative versus positive test) — both groups *chose* to test, so they are balanced on pre-testing characteristics, whereas the tested-vs-untested gap is confounded by selection into testing.

(2) **Symptom onset (event study).** Because onset age varies and onset reveals status, the authors group individuals by onset age (15–18, 19–22, 23–28, vs. no symptoms by 30 for education; 20–30, 31–40, vs. none by 40 for job training) and regress outcomes on these onset-group dummies. Earlier onset means status is revealed before the schooling decision, so effects should "fan out" with earlier onset. Magnitudes are rescaled by the share of each group *eligible* to still make the college decision at onset, and disability-adjusted using observed work histories.

Identification is defended with: balancing tests on pre-HD covariates; falsification on high-school completion (decided before revelation) and on older asymptomatic testers (revealed after schooling); evidence that early symptoms do not impair cognition (mini-mental and cognitive batteries flat over early onset) or are not driving behavior via motor disability, depression, or anxiety. Elasticities combine the regression coefficients with HD life-table survival, DALYs, and discounted returns to schooling (online Appendix A).

## Data
The Cooperative Huntington Observational Research Trial (COHORT), an observational study at 44 US sites: ~2,500 individuals with education and smoking outcomes, plus a smaller Analysis of Life Decisions (ALD) sub-study (~325 manifest/pre-manifest HD) collecting job-training, mammogram, and colonoscopy data designed for this paper. Variables include UHDRS motor scores, CAG-repeat gene status, self-reported age of first symptoms, and demographics. The sample is non-random (recruited at clinics, family members, support groups), which the authors stress is a threat to external — not internal — validity. Macro decompositions add US Census college-completion data, Social Security life tables, and World Development Indicators tertiary-enrollment data.

## Key findings
- **Education (testing).** Learning a positive test result lowers schooling: gene-negative testers complete ~0.9 more post-HS years and are ~24 pp more likely to earn a bachelor's degree (positive-vs-negative $p\approx0.01$). High-school completion is unaffected (falsification passes); older testers show no negative-vs-positive gap (falsification passes). The testing coefficient implies an ~82 percent reduction in college completion among eligible individuals.
- **Education (symptoms).** Effects scale monotonically with earlier onset: onset 15–18 cuts post-HS years by ~1.7 and bachelor completion by ~0.34; the divergence appears at college start/completion, not high school.
- **Job training.** Promotion/advancement training falls with earlier onset (onset 20–30: ~-0.27); robust to occupation controls; *routine* ("required") training is, if anything, higher — ruling out a job-type story.
- **Elasticities.** Elasticity of college completion w.r.t. life expectancy ≈ 1.0 (symptom-based; higher, ~2.3, from testing), and ≈ 1.1–1.4 for job training — close to Jayachandran and Lleras-Muney (2009).
- **Macro applications.** Plugging $\eta\approx1$ into the Acemoglu and Johnson (2007) framework implies their null life-expectancy–growth result would require an implausibly negative TFP elasticity, suggesting a non-neoclassical mechanism. Life-expectancy differences explain ~8–20 percent of over-time US college growth and ~20–30 percent of cross-country tertiary-enrollment gaps (median ~18 percent).
- **Health capital.** Mutation carriers (by testing or symptoms) are much less likely to quit smoking and to undergo cancer screening, consistent with Grossman (1972) health capital and competing mortality risks (Dow, Philipson, and Sala-i-Martin 1999).

## Contribution
A uniquely clean microeconomic test of the foundational human-capital prediction that life expectancy drives investment, using a Mendelian-randomization-like genetic setting that sidesteps the reverse-causality and omitted-variable problems plaguing cross-country and cross-sectional work. It improves on the small prior HD study by adding genetic-testing identification, onset-age variation, more outcomes, and richer controls, yielding precise, theory-relevant *elasticities* usable to discipline endogenous-growth models and to quantify life expectancy's share of schooling variation. It also delivers rare empirical support for the health-capital / competing-risks corollary.

## Limitations & open questions
- **External validity.** The estimates capture response to an *explicit, discrete revelation* of limited life expectancy; the authors argue this likely *biases elasticities upward* relative to diffuse cross-country life-expectancy variation, and is most applicable to discrete health changes (e.g., vaccination campaigns).
- **Selection.** The COHORT sample is non-random (engaged, treatment-seeking families), limiting generalization; smoking-by-early-symptoms analysis specifically fails balance and is flagged as more tentative.
- **Equilibrium scope.** Estimates reflect only the individual's *own* schooling response to their life expectancy; they do not capture parental investment responses, health-enabled schooling gains (Miguel and Kremer 2004; Bleakley 2007), or general-equilibrium effects — so they understate total impacts.
- **Mechanism residuals.** Possible confounds from early cognitive/motor symptoms, depression, anxiety, and smoking-as-self-medication are argued away but not fully eliminated; small sibling-pair sample (~25) limits within-family inference.

## Connections
The theoretical scaffold is Becker (1964) and Ben-Porath (1967) on human-capital investment over the life cycle, and Grossman (1972) plus Dow, Philipson, and Sala-i-Martin (1999) on health capital and longevity complementarities under competing risks. The growth-theory motivation draws on Mankiw, Romer, and Weil (1992), and the endogenous-mortality-growth literature (Kalemli-Ozcan 2002; de la Croix and Licandro 1999; Soares 2005; Chakraborty 2004). The central macro foil is Acemoglu and Johnson (2007), whose disease-driven life-expectancy instrument finds no growth effect — Oster et al. use their micro elasticity to argue this requires a non-neoclassical channel; Eggleston and Fuchs (2012) on late-life mortality gains supports the match between the HD setting and modern life-expectancy gains. Closest empirical relatives using mortality-environment variation are Fortson (2011) and Jayachandran and Lleras-Muney (2009) on HIV/AIDS and maternal mortality, and Stoler and Meltzer (2013), who likewise study at-risk-for-HD individuals; cross-sectional precedents include Hazan (2009, 2012). Oster (2012) provides the companion finding that worsening health can reduce protective behavior, the flip side of the health-capital complementarity documented here.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
