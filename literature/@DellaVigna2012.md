---
citekey: DellaVigna2012
title: "Testing for Altruism and Social Pressure in Charitable Giving *"
authors: ["DellaVigna, Stefano", "List, John A.", "Malmendier, Ulrike"]
year: 2012
type: journalArticle
doi: 10.1093/qje/qjr050
zotero: "zotero://select/library/items/I2ETN9HV"
pdf: /Users/jesper/Zotero/storage/7FL4QPTX/DellaVigna et al. - 2012 - Testing for Altruism and Social Pressure in Charit.pdf
tags: [literature]
keywords: [social-pressure, charitable-giving, warm-glow, altruism, field-experiment, structural-estimation, welfare]
topics: []
related: [Ariely2009, Benabou2006, Charness2002]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Every year, 90% of Americans give money to charities. Is such generosity necessarily welfare enhancing for the giver? We present a theoretical framework that distinguishes two types of motivation: individuals like to give, for example, due to altruism or warm glow, and individuals would rather not give but dislike saying no, for example, due to social pressure. We design a door-to-door fund-raiser in which some households are informed about the exact time of solicitation with a flyer on their doorknobs. Thus, they can seek or avoid the fund-raiser. We find that the flyer reduces the share of households opening the door by 9% to 25% and, if the flyer allows checking a Do Not Disturb box, reduces giving by 28% to 42%. The latter decrease is concentrated among donations smaller than $10. These findings suggest that social pressure is an important determinant of door-to-door giving. Combining data from this and a complementary field experiment, we structurally estimate the model. The estimated social pressure cost of saying no to a solicitor is $3.80 for an in-state charity and $1.40 for an out-of-state charity. Our welfare calculations suggest that our door-to-door fund-raising campaigns on average lower the utility of the potential donors.

## Summary
A landmark field experiment plus structural estimation that decomposes charitable giving into two opposing motives: a *positive* desire to give (altruism / warm glow) and a *negative* desire to avoid the unpleasantness of saying no (social pressure). By announcing a door-to-door solicitation with a flyer—sometimes with a "Do Not Disturb / opt-out" box—the authors let households *sort* in or out before being asked. The flyer lowers the share answering the door (evidence people avoid solicitors), and the opt-out option sharply cuts giving, especially small donations. A minimum-distance structural estimator recovers the social-pressure cost of saying no (~$3.75 in-state, ~$1.44 out-of-state) and implies that, on average, the fund-raising visit *lowers* solicitees' welfare.

## Research question
Is door-to-door charitable giving welfare-enhancing for the giver? More precisely: how much giving is driven by a genuine taste for giving versus by social pressure (the discomfort of declining a face-to-face request), and what does the answer imply for the welfare of the solicited and for fund-raising design?

## Method / identification
The paper combines a randomized field experiment with a behavioral structural model.

**Behavioral model.** An agent with wealth $W$ chooses a donation $g$. Utility from giving is $a\,v(g)$ where $a$ is an (heterogeneous) altruism weight and $v$ is concave; consumption utility is $u(W-g)$, taken locally linear $u(W-g)=W-g$. Declining (or giving below a threshold $g_S$) incurs a social-pressure cost $S$. The key idea: when a visit is *anticipated* via a flyer, the agent first chooses the probability $h$ of being home / opening the door, trading off a quadratic cost of altering home presence $c(h)=\frac{(h-h_0)^2}{2\eta}$ against the (dis)utility of the anticipated encounter. Altruism predicts flyers *raise* presence (seek the solicitor); social pressure predicts flyers *lower* presence (avoid). The opt-out box lowers the cost of declining, isolating the social-pressure channel.

**Field design.** A door-to-door fund-raiser for two charities—La Rabida (in-state children's hospital, well-liked) and ECU (out-of-state hurricane research center)—with three treatments randomized at the solicitor-hour / street level: (i) no-flyer (unanticipated), (ii) flyer (anticipated), (iii) flyer with an opt-out / "Do Not Disturb" box. A *complementary survey experiment* (run 2008–2009) varied payment ($0/$5/$10) and duration (5/10 min) to identify the elasticity $\eta$ of home presence to the desirability of the encounter—a parameter otherwise only parametrically identified.

**Estimation.** A minimum-distance / method-of-simulated-moments estimator choosing $\hat\xi=\arg\min(m(\xi)-\hat m)'W(m(\xi)-\hat m)$, with $W$ the diagonal inverse variance-covariance (identity matrix as robustness). Moments include probabilities of opening the door, giving in amount bins ($0<G<10$, $G=10$, $10<G\le 20$, etc.), completing the survey, and opting out. Functional-form assumptions: altruism $a$ drawn from a normal censored below at 0 (mass point at $a=0$); altruism function $v(g)=\log(\Gamma+g)$ with marginal utility $\frac{a}{\Gamma+g}$ ($\Gamma$ governs pure-altruism vs. warm-glow curvature); social-pressure threshold $g_S=\$10$; $\theta=0$ to capture absent mail/internet giving. Optimization via sequential quadratic programming (Matlab `fmincon`, Powell 1983) with adaptive Simpson quadrature for the theoretical moments. Reduced-form estimates are linear-probability regressions with solicitor and date-town fixed effects, identified off within-solicitor, within-day treatment variation.

## Data
Original field data: ~7,668 households in the charity treatments and ~11,900 in the survey treatments (1,865 in 2008; 10,035 in 2009), solicited door-to-door in towns near Chicago in 2008–2009. Outcomes: answering the door, giving in person, donation amount, opting out, survey completion, and mail/Internet donations.

## Key findings
- **Flyers reduce door-opening by 9%–25%**, indicating households on average *avoid* solicitors—net evidence for social pressure.
- **The plain flyer has ~no effect on giving**: consistent with altruism (sorting in) and social pressure (sorting out) roughly cancelling.
- **The opt-out flyer reduces giving by 28% (in-state) to 42% (out-of-state)**, and the drop is concentrated in **small donations (≤$10)**; donations above $10 slightly increase. ~12% of opt-out households check the box.
- **No substitution to mail/Internet**: only 1 of 7,668 households gave by other means—inconsistent with pure altruism, consistent with warm glow tied to in-person giving and/or social pressure.
- **Structural estimates**: ~75% of solicitees have zero altruism toward the charities; among altruists the altruism function is steeply concave (warm-glow-like, almost no predicted giving above $50). Estimated social-pressure cost of giving zero is **$3.75 in-state** (significant) and **$1.44 out-of-state** (marginally significant). A majority of donors give *more* than they would like; roughly half derive negative utility from the interaction and would have preferred to opt out.
- **Welfare**: a visit lowers welfare by ~$1.10/household (in-state) and ~$0.44 (out-of-state). Counterintuitively the better-liked charity yields a *more* negative welfare impact because its social-pressure cost is larger. Net donations raised were small ($0.24/household in-state; ~$0 out-of-state).

## Contribution
First field-experimental identification and structural estimation of social pressure as a distinct, welfare-relevant motive for charitable giving, separate from altruism/warm glow. Methodologically, it tightly couples a behavioral model to a designed field experiment—at the time, an almost unique pairing (Card, DellaVigna & Malmendier 2011 note only two such top-five-journal field experiments through 2010). Policy-relevant: motivates do-not-solicit lists and, more constructively, *sorting / opt-out* mechanisms that can be win-win—limiting welfare losses while plausibly raising funds by sorting in large altruistic givers.

## Limitations & open questions
- The design identifies motives for **marginal**, not **infra-marginal**, giving; the recovered altruism/social-pressure mix may not generalize to households' large baseline charitable contributions, which may be more altruism- or status-driven.
- Estimates rely on **strong functional-form and parametric assumptions** (locally linear consumption utility, log altruism function, homogeneous social pressure $S$, fixed threshold $g_S=\$10$, $\theta=0$); several are only partly relaxed in robustness checks.
- The elasticity $\eta$ is identified only via an **auxiliary survey experiment** assumed comparable to the charity setting.
- Alternative interpretations (flyer as a low-quality signal; self/other signaling à la Bénabou–Tirole; pure dislike of time with the solicitor) are argued against but not fully excluded.
- Whether sorting/opt-out mechanisms genuinely raise net fund-raising in practice is left as an open empirical question.

## Connections
The altruism-vs-warm-glow distinction draws on Andreoni's impure-altruism / warm-glow theory and relates to Andreoni (2006) on fund-raising. The social-pressure and self-image channels connect to Bénabou & [[@Benabou2006|Tirole (2006)]] on prosocial behavior and identity, Bodner & Prelec (2003) and Grossman (2010) on self-signaling, and to the "moral wiggle room" lab evidence of Dana, Cain & Dawes (2006) and Lazear, Malmendier & Weber. It complements lab social-preference work such as Fehr & Gächter (2000) and [[@Charness2002|Charness & Rabin (2002)]] with field evidence. On fund-raising design it speaks to List & Lucking-Reiley (2002), Landry et al. (2006), [[@Ariely2009|Ariely, Bracha & Meier (2009)]], and Croson & Shang (2009). The structural-behavioral-on-field-data program is shared with Card, DellaVigna & Malmendier (2011), and structural estimation of behavioral models echoes Laibson, Repetto & Tobacman (2007) and Conlin, O'Donoghue & Vogelsang (2007).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
