---
citekey: Simonson1992
title: "Choice in Context: Tradeoff Contrast and Extremeness Aversion"
authors: ["Simonson, Itamar", "Tversky, Amos"]
year: 1992
type: journalArticle
doi: 10.2307/3172740
zotero: "zotero://select/library/items/SQHSQDF4"
pdf: /Users/jesper/Zotero/storage/UH9MEV4Y/Simonson1992.pdf
tags: [literature]
keywords: [context-effects, tradeoff-contrast, extremeness-aversion, compromise-effect, attraction-effect, loss-aversion, consumer-choice]
topics: ["[[context-effects-attraction-compromise]]"]
related: [Huber1982, Simonson1989, Tversky1972]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Consumer choice is often influenced by the context, defined by the set of alternatives under consideration. Two hypotheses about the effect of context on choice are proposed. The first hypothesis, tradeoff contrast, states that the tendency to prefer an alternative is enhanced or hindered depending on whether the tradeoffs within the set under consideration are favorable or unfavorable to that option. The second hypothesis, extremeness aversion, states that the attractiveness of an option is enhanced if it is an intermediate option in the choice set and is diminished if it is an extreme option. These hypotheses can explain previous findings (e.g., attraction and compromise effects) and predict some new effects, demonstrated in a series of studies with consumer products as choice alternatives. Theoretical and practical implications of the findings are discussed.

## Summary
A landmark behavioral-marketing paper proposing two general principles that organize the growing list of context effects in consumer choice. **Tradeoff contrast** holds that an option becomes more attractive when the exchange rates (tradeoffs) among the surrounding alternatives — whether encountered in the past (background) or present in the offered set (local) — are unfavorable to those others, and vice versa. **Extremeness aversion** holds that, because disadvantages loom larger than the corresponding advantages, intermediate options gain share at the expense of extremes. Across 22 between-subjects experiments with realistic consumer products (cameras, PCs, gasoline, tires, cassette players, dental insurance, etc.), the authors show these two principles subsume the attraction/asymmetric-dominance and compromise effects and generate new predictions — enhancement, detraction, and polarization — many of which violate value maximization and regularity.

## Research question
How is consumer choice between alternatives systematically influenced by the *context* — the set of alternatives under consideration, including options encountered in the past — and can the disparate documented context effects be unified under a small number of psychological principles that depart from value maximization (VM)?

## Method / identification
The classical benchmark is **value maximization (VM)**: each alternative $x=(x_1,\dots,x_n)$ has a context-independent value $V(x)$ and the consumer picks the option with the highest value, implying preferences are independent of the choice set. The paper proposes two principles that violate this.

**Tradeoff contrast.** Options vary on two attributes (e.g., quality $x_1$ and price $x_2$). The tendency to prefer $x$ over $y$ is enhanced when other comparisons in the context exhibit exchange rates *worse* than that implied by $x$ vs. $y$. Two variants are studied: *background contrast* (induced by previously encountered pairs/triples whose slope — e.g., \$4/K vs. \$0.5/K of PC memory — is manipulated) and *local contrast* (induced within the offered set). Using $P(x;y)$ for the share of $x$ in set $\{x,y\}$ and the normalized share $P_z(x;y)=P(x;y;z)/[P(x;y;z)+P(y;x;z)]$, tradeoff contrast predicts e.g. $P_z(y;x)>P(y;x)$ when $z$ is dominated by $y$ but not $x$ (asymmetric dominance), and milder **enhancement** ($D_x(y)=P_x(y;z)-P(y;z)>0$) and **detraction** ($D_x(w)<0$).

**Extremeness aversion.** Extending loss aversion, disadvantages are defined *relative to the other alternatives in the set* rather than to a neutral reference point and are weighted more heavily than advantages. For a middle option $y$ in $x{\mid}y{\mid}z$ (with $x_1<y_1<z_1$, $x_2>y_2>z_2$), this predicts the **betweenness inequality** $P_x(y;z)>P(y;z)$ and $P_z(y;x)>P(y;x)$ — the middle option loses *less* share than VM implies. Two forms are distinguished: **compromise** (both inequalities hold; disadvantages loom larger on both attributes) and **polarization** (only one holds; asymmetry across attributes).

The **design** uses a "Survey of Consumer Preferences" questionnaire (3–14 problems, 5–25 min) administered between-subjects in classrooms; 100–220 participants per experiment, mostly business/psychology students at three West-Coast universities, some executives. Realistic stimuli (catalog pictures, descriptions, inspectable paper-towel samples) were used; some subjects were told a randomly drawn choice would be honored. Effects are read off share differences across versions with $t$-tests.

**Theoretical model.** A context-dependent additive ("contingent additive") model: $V^S(x)=\sum_i v_i^S(x_i)$ where the set $S$ adjusts the rate-of-exchange weights (capturing tradeoff contrast) and reference point. Generalizing to $v_i^S(x_i)=w_i^S f_i[v_i(x_i)-v_i(m_i^S)]$, with $m_i^S$ the minimal level of attribute $i$ in $S$: compromise arises when both $f_i$ are strictly concave; polarization when one is concave and the other linear.

## Data
Original experimental data from 22 between-subjects studies (no secondary dataset); product categories include 35mm cameras, personal computers, unleaded gasoline, tires, paper towels/facial tissues, microwaves, cash-vs-pen, calculator batteries, calculators, portable grills, AM/FM cassette players, dental insurance, and binoculars. Several studies reuse data from [[@Simonson1989|Simonson (1989)]].

## Key findings
- **Background contrast.** Subjects exposed to a high cost-of-memory background later chose the bigger-memory PC far more (52% vs. 18%); for gifts, a \$5/coupon background pushed 73% to the larger-cash gift vs. 47% under \$15/coupon. Effect holds even with a *single* background comparison (PCs $t=4.7$; tires $t=3.7$), and cannot be explained by attribute-range manipulations.
- **Asymmetric dominance / attraction.** Replicated with richer, familiar, quality-assessable products (microwaves, paper towels, facial tissues, Cross pen) — adding an inferior option $z$ raises the share of the similar superior option even when all options are reviewed, ruling out information-based explanations.
- **Enhancement and detraction.** Adding a non-dominated extreme $x$ raises the relative share of adjacent $y$ (enhancement, mean $D_x(y)\approx.15$) and lowers that of $w$ (detraction, mean $\approx -.15$); regularity is *not* violated here, unlike asymmetric dominance.
- **Compromise effect.** The middle option gains share: e.g., the mid-camera's relative share rose from .50 to .57 when a top camera was added; replicated with calculators, grills, and even *unavailable* added extremes — violating the betweenness inequality and hence VM/regularity.
- **Polarization.** When attributes differ in salience (quality vs. price), adding a middle option disproportionately favors the high-quality/high-price option over the low-quality/low-price one (AM/FM cassettes: $D_z(y)=.29$, $p<.01$; $D_y(x)=-.34$). The low-quality option is "the big loser"; regularity violated in 6 of 7 comparisons.

## Contribution
Unifies the previously scattered literature on context effects (attraction, compromise) under two psychologically grounded principles — tradeoff contrast and extremeness aversion — and shows they predict *new* effects (enhancement, detraction, polarization). It documents systematic, robust violations of value maximization and regularity using realistic, familiar consumer products evaluated with full information, and offers a parsimonious **contingent additive model** with marketing implications for product-line positioning, the power of "decoy" and compromise products, and the deal/promotion premium attributable to asymmetric dominance.

## Limitations & open questions
- *Why does extremeness aversion attach to quality/performance but not to price?* The authors have "no definite answer" and only speculate that quality defines the goal while price is a means; conditions giving rise to polarization "warrant further study."
- *When is the betweenness inequality satisfied vs. violated?* Hypothesized to hold when consumers evaluate options on *absolute* rather than relative characteristics — left for future research.
- *Effect of unavailable alternatives* is inconsistent (sometimes increases the dominated option's share, per Farquhar and Pratkanis 1987) and "calls for further research."
- *Conscious vs. unconscious mediation.* Aggregate choices were the only dependent variable; process measures (verbal protocols, information-acquisition patterns) "might improve our understanding."
- *Estimating the contingent additive model.* The full model "cannot be readily estimated from aggregate data"; developing a simplified, estimable version to revise standard VM-based prediction methods (e.g., conjoint) is left for future research.

## Connections
Directly extends loss aversion and reference-dependence (Kahneman, Knetsch, and Thaler 1991; Tversky and Kahneman 1991) by redefining the reference point relative to other alternatives in the set. It builds on and unifies the **attraction/asymmetric-dominance effect** ([[@Huber1982|Huber, Payne, and Puto 1982]]; Huber and Puto 1983) and the **compromise effect** ([[@Simonson1989|Simonson 1989]]), and engages the constructive-preference view (Bettman, Johnson, and Payne 1991; Payne, Bettman, and Johnson 1992). The formal model draws on contingent weighting (Tversky, Sattath, and Slovic 1988) and is developed further in Tversky and Simonson (in press, "Context-Dependent Preferences"). Its challenge to context-independent VM bears on probabilistic choice models (Luce 1977; McFadden 1973; [[@Tversky1972|Tversky 1972]]) and on conjoint-based market-share prediction (Green and Srinivasan 1990), with practical links to sales promotions (Blattberg and Neslin 1990) via the asymmetric-dominance interpretation of deals.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
