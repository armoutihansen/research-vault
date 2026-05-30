---
citekey: Benjamin2010
title: Social Identity and Preferences
authors: ["Benjamin, Daniel J.", "Choi, James J.", "Strickland, A. Joshua"]
year: 2010
type: journalArticle
doi: 10.1257/aer.100.4.1913
zotero: "zotero://select/library/items/5FAM6CHY"
pdf: /Users/jesper/Zotero/storage/N7SMX942/Benjamin2010.pdf
tags: [literature]
keywords: [social-identity, time-preference, risk-aversion, priming, behavioral-economics, self-categorization, identity-economics]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Social identities prescribe behaviors for people. We identify the marginal behavioral effect of these norms on discount rates and risk aversion by measuring how laboratory subjects' choices change when an aspect of social identity is made salient. When we make ethnic identity salient to Asian-American subjects, they make more patient choices. When we make racial identity salient to black subjects, non-immigrant blacks (but not immigrant blacks) make more patient choices. Making gender identity salient has no effect on intertemporal or risk choices. (JEL D81, J15, J16, Z13 )

## Summary
Benjamin, Choi, and Strickland import the "priming" methodology from social psychology into experimental economics to isolate the *causal* effect of social-identity norms on two primitive preference parameters: the discount rate and the degree of risk aversion. By randomly making ethnic, racial, or gender identity salient to laboratory subjects and then eliciting time and risk preferences with incentive-compatible mechanisms, they recover the marginal behavioral effect of strengthening a category affiliation. The headline results: priming Asian-American ethnicity makes subjects markedly more patient; priming race makes native (non-immigrant) blacks more patient but does not move immigrant blacks; priming gender has no effect on either time or risk preferences.

## Research question
Do norms attached to social identities causally shape fundamental economic preferences (time and risk preferences), and can the *sign and magnitude* of those norms be inferred experimentally? Field correlations between social-category membership and economic outcomes (Asian-American human-capital accumulation, lower black financial wealth and stock-market participation, more conservative female investing) are confounded with socioeconomic status, opportunity sets, and peer effects. The paper asks whether identity norms play a causal role once that confounding is broken via random assignment.

## Method / identification
The identification rests on **self-categorization theory**: environmental "primes" temporarily raise the salience of a social category, tilting behavior toward that category's norm. The authors formalize this in an Akerlof–Kranton-style model. For an action $x$ (e.g. degree of immediate gratification or risk avoidance), an individual in category $C$ with affiliation strength $s\geq 0$ chooses $x$ to maximize
$$U=-(1-w(s))(x-x_0)^2-w(s)(x-x_C)^2,$$
where $x_0$ is the identity-free preferred action, $x_C$ is the category-prescribed norm, and $w(s)\in[0,1]$ with $w(0)=0$, $w'>0$ is the decision weight on the category. The first-order condition gives
$$x^*(s)=(1-w(s))\,x_0+w(s)\,x_C,$$
a convex combination of the personal optimum and the norm. A prime perturbs $s$ to $s+\varepsilon$, so the treatment effect is
$$x^*(s+\varepsilon)-x^*(s)\approx \frac{dx^*}{ds}\varepsilon=w'(s)\,(x_C-x_0)\,\varepsilon,$$
whose **sign equals the sign of $x_C-x_0$**. Hence priming reveals whether the norm pushes toward more patience ($\gamma_C<\gamma_0$, with $\gamma$ the degree of impatience) or more risk aversion ($\rho_C>\rho_0$, with $\rho$ the degree of risk-averse behavior). A key methodological corollary: directional priming effects generalize to the population even if sample $\bar s$, $x_0$, and $w(\cdot)$ differ, provided $x_C-x_0$ shares its sign across groups. The authors also show that the prediction "stronger identifiers respond more to priming" is *not* a valid test of the theory, since the cross-derivative $d^2x^*/ds^2$ can take either sign depending on whether $w''>0$ (susceptibility) or $w''<0$ (saturation).

**Experimental design.** Two between-subjects experiments. Identity salience is manipulated via a "background questionnaire" (asking about family languages/generations for Asian ethnicity; race/roommate or gender/dormitory opinions for Experiment 2), modeled on Shih, Pittinsky, and Ambady (1999); controls answer innocuous questions (meal plans, cable, on/off-campus living). Time preferences are elicited via binary choices between a smaller-sooner and larger-later payment; risk preferences via binary choices between a sure amount and a probabilistic gamble. One choice is randomly selected for real payment, with delayed payments implemented by post-dated checks.

**Econometrics.** The time-preference dependent variable is the *log of the continuously compounded weekly reservation interest rate* (the double-log transform imposes conditional log-normality and rules out negative discount rates); the risk dependent variable is the reservation risk premium. Because choices are observed only at finitely many interest rates / risk premia, estimation uses **interval regression** (Stewart 1983), a generalization of tobit. Standard errors are clustered by subject; medians are emphasized over means due to outliers.

## Data
Original laboratory data. Experiment 1: 137 Harvard undergraduates (71 Asian-descent, 66 white-descent), 46 intertemporal and 18 risk choices. Experiment 2: 511 students (280 Temple, 231 Michigan) randomized to race-salience, gender-salience, or control; blacks classified as immigrant if they or a parent were born outside the U.S.; 24 intertemporal and several small- and large-stakes risk choices, plus an SAT-style math quiz and a shortened Spielberger State-Trait Anxiety Inventory used as manipulation checks.

## Key findings
1. **Asian ethnicity → patience.** Priming cuts the proportion of impatient choices by 14 percentage points (significant at 1%); the median required weekly interest rate for "$4 now vs. one week" falls from 8.8% to 2.1%. Whites are unaffected (ruling out a common channel), and there is no effect on Asian risk choices.
2. **Native-black race → patience.** Race salience significantly lowers native blacks' reservation interest rate (median Temple rate falls from 23.2% to 10.9% for the one-week trade-off). **Immigrant blacks show no effect**, and whites are unaffected in the full sample. This contradicts Sowell and Murray's claim of an impatient black norm and implies racial discount-rate norms do *not* explain the black–white or native–immigrant capital-accumulation gaps.
3. **Gender → no effect.** Making gender salient has no significant effect on men's or women's patience or risk aversion; in particular, no evidence of a stronger male risk-seeking norm.
4. **Suggestive risk and white effects (believer subsample).** Restricting to subjects who believed payment promises (35–53% reported some disbelief), priming race raises native blacks' reservation risk premium by 23 points (significant at 1%), consistent with risk norms depressing native-black stock-market participation; priming also makes whites significantly more patient, hinting at a patient white racial norm. These subsample results are flagged as fragile (endogenous selection, lost power).
5. **Robustness.** Effects replicate across both schools in sign; primes had no effect on math-quiz performance or anxiety, ruling out stereotype threat/lift and emotional-state channels; 90% of Michigan subjects denied thinking about experimenter wishes, undercutting demand effects; results survive dropping skeptics and ill-behaved responders.

## Contribution
The paper is an early and influential demonstration that **social identity causally moves core economic primitives** (discount rates, risk aversion), not just stated attitudes or social preferences. Methodologically it repurposes psychological priming as an identification strategy for economists: by taking self-categorization theory as given and priming categories with *unknown* norms, the behavioral response reveals the norm's content and sign. This inverts the psychology literature, which primes known norms to test the theory. It also operationalizes Akerlof and Kranton's identity-economics framework into a tractable, testable model with sharp sign predictions.

## Limitations & open questions
- **Highly selected samples** (elite university students) with non-representative baseline preferences; external validity to general populations rests on the sign-invariance argument rather than level estimates.
- **Payment credibility:** between 35% and 53% of Experiment-2 subjects reported some disbelief in payment promises, adding noise/bias; the believer-subsample (risk, white-patience) results lose significance or rest on endogenously selected, much smaller samples and are explicitly to be read "with caution."
- **Immigration status unmeasured for the Experiment-1 control group**, so immigration cannot enter as an uninteracted regressor there.
- **Mechanism opacity:** the model treats $w(s)$ and the norm $x_C$ as primitives; the paper cannot pin down *why* native-black norms favor patience or why gender norms are inert, nor whether $w''$ is positive or negative.
- **Multiple-hypothesis testing / Type I error** is acknowledged; cross-school consistency is the only informal correction.
- **Transitory vs. steady-state:** primes perturb $s$ only temporarily; whether repeated real-world primes accumulate into persistent preference change (and the welfare/policy implications of a "benevolent policymaker" using primes for savings or voting) is left open.

## Connections
The theoretical backbone is **Akerlof and Kranton (2000)**, "Economics and Identity," which the quadratic-loss model directly operationalizes. The priming manipulations adapt **Shih, Pittinsky, and Ambady (1999)** on ethnicity/gender salience and math performance, and the broader self-categorization tradition (James 1890; Turner 1985). On contested black-norm claims it engages **Sowell (1975, 1981)** and **Murray (1984)** versus patience-emphasizing accounts (Storing, West, Bell). Preference-elicitation and validation draw on **Frederick, Loewenstein, and O'Donoghue (2002)** for time discounting and **Barsky et al. (1997)**, Dohmen et al. (2005), and Sahm (2007) for risk measurement; the inertia argument for long-run policy relevance leans on **Madrian and Shea (2001)** and **Choi et al. (2002)**. It is adjacent to economics-of-identity work on discrimination and group identity (Hoff and Pandey 2006; **Chen and Li 2009**) and on incentive effects in experiments (Camerer and Hogarth 1999; Holt and Laury 2002). The acting-white field literature (Austen-Smith and Fryer 2005; Fryer and Torelli 2005) motivates the confounding problem the experiment is designed to escape.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
