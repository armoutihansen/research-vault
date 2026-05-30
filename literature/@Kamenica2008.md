---
citekey: Kamenica2008
title: "Contextual Inference in Markets: On the Informational Content of Product Lines"
authors: ["Kamenica, Emir"]
year: 2008
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/DL5XZ9IH"
pdf: /Users/jesper/Zotero/storage/SYSBTKKW/Kamenica2008.pdf
tags: [literature]
keywords: [contextual-inference, compromise-effect, choice-overload, premium-loss-leader, product-line-signalling, rational-context-effects]
topics: []
related: [Benabou2003, Gabaix2006, Huber1982, Iyengar2000, Kalai2002, Sarver2008, Sen1993, Simonson1989, Simonson1992, Tversky1974]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Context can influence decisions. This malleability of choice is usually invoked as evidence that people do not maximize stable preference orderings. In a market equilibrium, however, context conveys payoff-relevant information to consumers. Consequently, these consumers rationally violate naïve formulations of standard choice theoretic principles. I identify informational asymmetries under which apparently anomalous behaviors, namely the compromise effect and choice overload, arise as market equilibria. Firms respond to consumers' contextual inference; in case of the compromise effect, a firm may introduce premium loss leaders (expensive goods of overly high quality that increase the demand for other goods).

## Summary

Kamenica shows that two canonical "behavioral" anomalies of choice — the compromise effect and choice overload — can emerge as equilibria of a standard market with utility-maximizing consumers, once one recognizes that the product line a firm offers is itself informative. Uninformed consumers rationally infer payoff-relevant information (the hedonic value of quality, or the popularity of varieties) from the *set* of goods made available. This "contextual inference" reconciles context-sensitive behavior with stable preferences, generates sharp testable predictions, and implies that firms will sometimes distort their menus — e.g., by stocking a *premium loss leader* — to manipulate the beliefs of the uninformed.

## Research question

Can context effects that are usually taken as evidence *against* stable preference orderings — specifically the compromise effect and choice overload — instead arise in market equilibrium among fully rational, utility-maximizing consumers who treat the firm's product line as a signal? And how do profit-maximizing firms respond to such inference?

## Method / identification

A signalling-game model. There is a continuum of consumers (indexed $i$) and a single firm. Each technologically feasible variety $x\in X$ has marginal cost $c_x$ and stochastic fixed cost $K_x$ (the randomness in fixed costs supplies exogenous variation in which goods appear). Consumer $i$ has quasi-linear utility $u(\theta_i,s,x)-p_x+\varepsilon_{ix}$, with i.i.d. shocks $\varepsilon_{ix}$, $E[\varepsilon_{ix}]=0$, individual type $\theta_i\in\Theta$, and a *global preference parameter* $s\in S$. A fraction $\alpha\in[0,1)$ of consumers do not know $s$; they share a common prior $\pi$ over $S$ and update to a posterior $\pi(s\mid M)$ after observing the firm's product line $M\subseteq X$. Prices are taken as exogenous (an earlier version, Kamenica 2006, endogenizes them). The solution concept is Perfect Bayesian Equilibrium refined by the **D1 criterion** (Banks–Sobel 1987; Cho–Kreps 1987); without D1, "threat beliefs" would support any menu as an equilibrium when most consumers are uninformed.

A consumer engages in *contextual inference* when $\pi(s\mid M)\neq\pi(s)$. Let $\bar u(\theta,x\mid M)=\int_S u(\theta,s,x)\,d\pi(s\mid M)-p_x$. The **compromise effect** is defined on a partial order $\succ$ in price–quality space: type $\theta$ exhibits it if there exist $x_0\succ x_1\succ x_2$ with $x_1=\arg\max_x \bar u(\theta,x\mid\{x_0,x_1,x_2\})$ yet $\bar u(\theta,x_0\mid\{x_0,x_1\})>\bar u(\theta,x_1\mid\{x_0,x_1\})$ (the middle good is chosen from the triple but not from a pair). **Rational choice overload** holds for type $\theta$ if there exist $M\subsetneq M'$ with $\max_{x\in M}\bar u(\theta,x\mid M)>\max_{x\in M'}\bar u(\theta,x\mid M')$ — a smaller menu yields strictly higher attainable utility.

For the compromise effect the model is specialized to three vertically differentiated goods $\{x_0,x_1,x_2\}$ with $q_j<q_k$, $c_j<c_k$, $p_j<p_k$ for $j<k$, two taste types $\theta_l<\theta_h$, utility $\theta_i s q_j-p_j+\varepsilon_{ij}$, and a binary $S=\{\underline s,\bar s\}$ where $s$ is the *hedonic value of quality* (translating technical units like lumens or MHz into "brightness" or "speed"). The optimal good for each type flips with $s$. For choice overload, $N$ equally-priced flavors with common markup $p-c$; each consumer has one favorite flavor; the uninformed know neither their favorite nor the popularity distribution $\lambda$ over flavors.

## Data

None — this is a pure theory paper. It marshals existing empirical/anecdotal evidence ([[@Simonson1989|Simonson 1989]] calculator-battery compromise effect; [[@Iyengar2000|Iyengar–Lepper 2000]] jam study; the Williams-Sonoma bread-maker anecdote; Iyengar–Huberman–Jiang 2004 401(k) participation) to motivate and illustrate the mechanism, but estimates nothing.

## Key findings

- **Proposition 1:** In any equilibrium, uninformed low-type consumers exhibit the compromise effect with positive probability. Intuition: from $\{x_0,x_1\}$ the uninformed $\theta_l$ cannot tell whether $x_2$ is absent because $\underline s$ or because $K_2$ was high, so they fall back on the prior and pick $x_0$; from $\{x_0,x_1,x_2\}$ the presence of $x_2$ reveals $\bar s$ and makes $x_1$ optimal. Crucially, choices made in the *richer* context are the ex-post-optimal ones — the opposite of Hsee (2000).
- **Proposition 2:** With a positive measure of uninformed consumers ($\alpha\in(0,1)$), there is a threshold $\lambda'<1$ such that if the low-type fraction $\lambda_l>\lambda'$, the firm introduces the highest-quality good $x_2$ with positive probability *even when its per-se profit is negative* — a **premium loss leader**. The high quality good credibly signals high $s$ (informed demand for $x_2$ rises in $s$), boosting uninformed demand for $x_1$. The firm would like to commit to introduce $x_2$ only in $\bar s$, but cannot credibly do so. Some informed consumers ($\alpha<1$) are essential for D1 to bite.
- **Lemma 3:** With homogeneous markups, the firm always introduces the *most popular* flavors. Hence average popularity of available flavors falls as the menu widens.
- **Proposition 4 / Proposition 5 (choice overload):** Uninformed demand is strictly higher under a smaller product line — within an equilibrium (Prop. 4, a *manipulation* prediction: shrink the menu in a fixed market) and across equilibria with different $\alpha$ (Prop. 5, a *cross-market* prediction). Because informed consumers prefer wider menus and uninformed prefer narrower ones, the equilibrium product line shrinks in $\alpha$, and the uninformed are worse off when there are *more* informed consumers — a reversal of the usual informed-on-uninformed positive externality (Salop–Stiglitz 1977).

## Contribution

Provides a unified, microfounded, rational-choice account of two effects normally cited as failures of standard preference theory, deriving them as equilibria with *standard* preferences rather than assuming choice-set-dependent preferences. It introduces the equilibrium notion of a premium loss leader and the result that uninformed surplus can *decrease* in the number of informed consumers. It yields a battery of testable predictions (ex-post optimality ranking of inconsistent choices; the prediction that randomized or popularity-labeled menus eliminate the anomalies) and connects choice overload to live policy debates (Social Security / Medicare / 401(k) menu design), arguing welfare effects of expanding options hinge on whether suitable popularity information accompanies them.

## Limitations & open questions

- The model **cannot account for anchoring** effects where information is demonstrably irrelevant ([[@Tversky1974|Tversky–Kahneman 1974]]; Ariely–Loewenstein–Prelec 2003) — contextual inference is explicitly not the whole story.
- Prices are exogenous; endogenizing them requires extra structure (retail cost shocks) to keep prices from fully revealing $s$.
- Static: the author flags a **dynamic model** in which the current product line feeds back into the *proportion* of uninformed consumers next period as an open direction.
- Explicit empirical questions left open: Do firms actually introduce goods purely to manipulate beliefs? If a small menu is known to be unrelated to popularity, does choice overload still obtain? Are consumers with more typical preferences more prone to choice overload? The ex-post-optimality prediction (measure satisfaction/returns from larger vs. smaller contexts) also remains to be tested.

## Connections

Builds directly on Wernerfelt (1995), who first formalized that ignorance of absolute but knowledge of relative tastes can generate the compromise effect; informal precursors are Luce & Raiffa (1957) and [[@Sen1993|Sen (1993)]]. The compromise effect itself is [[@Simonson1989|Simonson (1989)]] and [[@Simonson1992|Simonson & Tversky (1992)]]; the attraction effect ([[@Huber1982|Huber, Payne & Puto 1982]]) and joint–separate evaluation reversals (Hsee 2000; Bazerman, Loewenstein & White 1992) are reinterpreted via uncertainty about $s$. Choice overload evidence comes from [[@Iyengar2000|Iyengar & Lepper (2000)]], Boatwright & Nunes (2001), Bertrand et al. (2005), and Iyengar, Huberman & Jiang (2004); concurrent rational-choice accounts include Norwood (2006) and Kuksov & Villas-Boas (2007), with related welfare logic in Mirrlees (1987) and regret-based treatments by Irons & Hepburn (2007) and [[@Sarver2008|Sarver (2008)]]. The signalling apparatus draws on Banks & Sobel (1987) and Cho & Kreps (1987); related inference-from-context models include Bénabou & [[@Benabou2003|Tirole (2003)]], Anand & Shachar (2004), and [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]]. It sits within behavioral industrial organization (DellaVigna & Malmendier 2004; Heidhues & Kőszegi; [[@Gabaix2006|Gabaix & Laibson 2006]]; Spiegler 2006; Eliaz & Spiegler 2007), but uniquely derives nonclassical behavior from standard preferences, and the informed/uninformed externality contrasts with Salop & Stiglitz (1977) and the preference-externality work of Waldfogel (2003) and George & Waldfogel (2003).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
