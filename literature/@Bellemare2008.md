---
citekey: Bellemare2008
title: Measuring Inequity Aversion in a Heterogeneous Population Using Experimental Decisions and Subjective Probabilities
authors: ["Bellemare, Charles", "Kröger, Sabine", "Van Soest, Arthur"]
year: 2008
type: journalArticle
doi: 10.1111/j.1468-0262.2008.00860.x
zotero: "zotero://select/library/items/DEC5LQ46"
pdf: /Users/jesper/Zotero/storage/V9Z7DS3L/Bellemare2008.pdf
tags: [literature]
keywords: [inequity-aversion, ultimatum-game, subjective-expectations, structural-estimation, social-preferences, population-heterogeneity]
topics: ["[[inequity-aversion-distributional-preferences]]"]
related: [Bolton2000, Fehr1999]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We combine choice data in the ultimatum game with the expectations of proposers elicited by subjective probability questions to estimate a structural model of decision making under uncertainty. The model, estimated using a large representative sample of subjects from the Dutch population, allows both nonlinear preferences for equity and expectations to vary across socioeconomic groups. Our results indicate that inequity aversion to one's own disadvantage is an increasing and concave function of the payoff difference. We also find considerable heterogeneity in the population. Young and highly educated subjects have lower aversion for inequity than other groups. Moreover, the model that uses subjective data on expectations generates much better in- and out-of-sample predictions than a model which assumes that players have rational expectations.

## Summary
The paper estimates a structural model of distributional (inequity-averse) preferences from ultimatum-game choices, while sidestepping the usual need to *assume* what proposers believe about responders. Instead of imposing rational expectations, it directly elicits proposers' subjective probabilities that each offer will be accepted, and models preferences and beliefs jointly so that the two can be separately identified and allowed to correlate. Using a representative Dutch internet panel, it finds that aversion to one's own disadvantage is increasing and concave (not linear, as in Fehr–Schmidt), that there is large unobserved heterogeneity, that optimism about acceptance is negatively correlated with disadvantageous-inequity aversion, and that the subjective-expectations model fits and forecasts (including out-of-sample to a dictator game) markedly better than a rational-expectations counterpart.

## Research question
Can preferences and beliefs be *separately identified* in games of proposal and response—where a proposer's payoff depends on the responder's reaction—without imposing untestable assumptions (e.g. rational expectations) on beliefs? Concretely: what is the shape of inequity aversion (linear vs. nonlinear, advantageous vs. disadvantageous), how does it vary across a broad population, and does incorporating directly elicited subjective expectations improve explanatory and predictive power relative to assuming proposers' beliefs equal the observed aggregate acceptance rates?

## Method / identification
The core is a structural micro-econometric model of distribution-based preferences estimated by **maximum simulated likelihood** (Ox). Subject $i$'s utility from own payoff $y_{self}$ and the other's payoff $y_{other}$ is a flexible, possibly nonlinear and asymmetric inequity-aversion function:
$$v_i = y_{self} - \alpha_{1i}\max\{y_{other}-y_{self},0\} - \alpha_{2i}\max\{y_{other}-y_{self},0\}^2 - \beta_{1i}\max\{y_{self}-y_{other},0\} - \beta_{2i}\max\{y_{self}-y_{other},0\}^2$$
Here $\alpha$ governs aversion to one's *own* disadvantage and $\beta$ to *advantageous* inequity; the quadratic terms ($\alpha_2,\beta_2$) capture nonlinearity. Setting $\alpha_2=\beta_2=0$ recovers the linear **[[@Fehr1999|Fehr–Schmidt (1999)]]** model, which the design nests. Linear coefficients carry observed and unobserved heterogeneity: $\alpha_{1i}=\exp(x_i'\alpha_1+u_i^\alpha)$, $\beta_{1i}=\exp(x_i'\beta_1+u_i^\beta)$, while $\alpha_{2i},\beta_{2i}$ load on an intercept plus a responder dummy. A proposer is assumed to maximize *expected* utility $Q_{ij}v_{ij}$ using his own subjective acceptance probability $Q_{ij}$ for offer $j$ (utility is zero if rejected); choice noise enters additively as $Q_{ij}v_{ij}+\lambda_i e_{ij}$ with logistic differences, and the noise scale $\lambda_i=\exp(x_i'\lambda)$ varies with characteristics and role. Responders accept offer $j$ iff $v_{ij}+\lambda_i e_{ij}>0$.

Beliefs are modeled rather than plugged in, for two reasons the authors stress: (i) a **framing effect**—elicited acceptance vs. rejection wording yields different probabilities; (ii) potential **endogeneity**—reported probabilities may correlate with the same unobservables driving preferences, biasing estimates if taken as exogenous. They posit a latent "true" probability $Q_{ij}^*=x_i'\delta+\gamma_j+u_i^P$ (a two-limit tobit censored to $[0,1]$, with option effects $\gamma_j$ and optimism term $u_i^P$), and a *reported* probability $P_{ij}^*=x_i'\delta+\gamma_j+\phi_j F_i+u_i^P+e_{ij}^P$ where $F_i\in\{+1,-1\}$ flags the accept/reject frame and $\phi_j$ is a symmetric framing bias. The unobserved heterogeneity vector $(u_i^\alpha,u_i^\beta,u_i^P)$ is tri-variate normal with free covariance, allowing **correlation between preferences and beliefs**—the key feature absent from prior subjective-expectations choice models. Imposing symmetry on $\phi_j$ is what identifies framing and the $\gamma_j$ from belief data alone. A second model assuming rational expectations (beliefs = observed aggregate acceptance rates, no belief equation) is estimated for comparison.

## Data
A field experiment on the **CentERpanel**, a representative internet panel of ~2000 Dutch households (March 2004). Of 1410 contacted, 1263 completed and 1223 were analyzable: **377 proposers and 335 responders in the ultimatum game; 260 proposers and 251 responders in the dictator game**. Proposers split 1000 CentERpoints (10 euro) over a discretized 8-allocation set excluding the equal split (forcing commitment above/below 500). Responder strategies were elicited via the **strategy method** (Selten 1967) over all 8 offers. Proposers additionally answered subjective probability questions ("how many of 100 would accept offer $j$"), randomly framed as acceptance or rejection probabilities, asked *after* choices to avoid contaminating behavior. Dictator-game proposer data were held out for out-of-sample testing only.

## Key findings
- **Nonlinear, concave disadvantageous-inequity aversion**: $\alpha_2$ estimates are significantly negative—aversion to one's own disadvantage is increasing and *concave* in the payoff gap. No nonlinearity in advantageous inequity ($\beta_2$). This nonlinearity vanishes under rational expectations.
- **Subjective beats rational expectations**: the subjective-expectations model fits young proposers' offers far better (rational expectations under-predicts 450/550 CP offers by 7.5/5.5 pp, over-predicts 150 CP by ~11 pp) and predicts the held-out dictator distribution well, whereas rational expectations puts 67% mass on zero offers.
- **Heterogeneity and selfish young/educated**: substantial unobserved heterogeneity in both preferences and beliefs; advantageous-inequity aversion rises with age and falls with education; young, highly educated, non-working subjects are among the *most selfish*, closest to own-payoff maximization—and closest to Fehr–Schmidt's student-calibrated values.
- **Belief–preference correlation**: $u_i^\alpha$ and $u_i^\beta$ are significantly positively correlated; optimism $u_i^P$ is significantly *negatively* correlated with $u_i^\alpha$—optimists have lower disutility from having less.
- **Framing and anticipated non-monotonicity**: significant negative framing parameters $\phi_j$ (except near the equal split); many responders are "plateau" types rejecting overly generous offers, and proposers' stated acceptance beliefs decline beyond the equal split, showing they *anticipate* this non-monotonicity despite no learning.

## Contribution
Methodologically, it shows how directly elicited subjective probabilities can resolve the Manski (2002, 2004) identification problem in proposal-and-response games, separately recovering flexible preferences and beliefs—and, uniquely, allowing them to be correlated to avoid endogeneity bias and support causal statements about beliefs' effect on choices. Substantively, it generalizes Fehr–Schmidt to nonlinear asymmetric inequity aversion, estimates the *entire population distribution* of preferences from a representative (not student) sample, and documents that lab/student calibrations systematically understate population-wide inequity aversion.

## Limitations & open questions
- The utility function is identified only up to a monotonic transformation, so the authors deliberately keep $v_i$ linear in $y_{self}$ and avoid further nonlinearities/interactions, expecting accurate estimation otherwise to be infeasible.
- **Efficiency concerns cannot be separately identified** from inequity aversion: negative disadvantageous-disutility for high offers may reflect efficiency motives, but the design cannot disentangle this.
- Whether the strong age effect is a **cohort effect or a genuine age effect** is left open and flagged for future research, as is external validation against real-world other-regarding behavior (charity, volunteering).
- The ultimatum game may be a poor environment to *test* specific fairness models (Andreoni, Castillo, Petrie 2003); the authors estimate but do not formally test Fehr–Schmidt against alternatives ([[@Bolton2000|Bolton–Ockenfels 2000]]; Cox–Friedman–Gjerstad 2007), calling for richer data with larger choice sets to enable such tests.
- Subjective beliefs carry a substantial framing bias that must be modeled away; comparison of internet vs. "identical" lab experiments, and whether experience reduces inconsistent/plateau behavior, are left for future work.

## Connections
Directly extends **[[@Fehr1999|Fehr and Schmidt (1999)]]** linear inequity aversion to a nonlinear, heterogeneous, population-level estimator, and contrasts with the [[@Bolton2000|Bolton–Ockenfels (2000)]] and Cox–Friedman–Gjerstad (2007) fairness models. The identification strategy follows **Manski (2002, 2004)** on measuring expectations and decision rules, and **Nyarko and Schotter (2002)**, who likewise elicited beliefs and found subjects best-respond to stated rather than inferred beliefs. The representative-sample design follows the field-experiment turn of Harrison, Lau, and Williams (2002) and the authors' own Bellemare and Kröger (2007). Plateau/non-monotone responder behavior connects to Huck (1999), Güth–Schmidt–Sutter (2003), Tracer (2004), and Hennig-Schmidt–Li–Yang (2008); role-dependence of preferences to Goeree and Holt (2000) and Gächter and Riedl (2005); the framing/"losses loom larger" interpretation to Tversky–Kahneman and Thaler.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
