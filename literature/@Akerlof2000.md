---
citekey: Akerlof2000
title: Economics and Identity
authors: ["Akerlof, George A.", "Kranton, Rachel E."]
year: 2000
type: journalArticle
doi: 10.1162/003355300554881
zotero: "zotero://select/library/items/AQU3HDKX"
pdf: /Users/jesper/Zotero/storage/LBKZD8DM/Akerlof2000.pdf
tags: [literature]
keywords: [identity-economics, social-categories, utility-function, discrimination, social-exclusion, gender, oppositional-identity]
topics: []
related: [Rabin1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper considers how identity, a person's sense of self, affects economic outcomes. We incorporate the psychology and sociology of identity into an economic model of behavior. In the utility function we propose, identity is associated with different social categories and how people in these categories should behave. We then construct a simple game-theoretic model showing how identity can affect individual interactions. The paper adapts these models to gender discrimination in the workplace, the economics of poverty and social exclusion, and the household division of labor. In each case, the inclusion of identity substantively changes conclusions of previous economic analysis.

## Summary
Akerlof and Kranton import "identity" — a person's sense of self, tied to membership in social categories and to the behavioral prescriptions those categories carry — into the economist's utility function. Following or violating the prescriptions for one's category yields gains or losses in identity, which sit alongside standard pecuniary payoffs. A prototype Green/Red game shows that identity generates a new kind of externality (one person's actions threaten another's self-image, provoking costly responses) and can rationalize behavior that looks maladaptive. The framework is then applied to three settings — gender and occupational segregation, oppositional identities and poverty, and the household division of labor — each time overturning a prediction of the prior literature. This is the founding paper of "identity economics."

## Research question
Can a person's identity — self-image anchored in socially defined categories and the prescriptions attached to them — be formalized inside standard economic theory, and does doing so change the predictions of existing models of discrimination, poverty, and the household? More broadly: what economic phenomena that current economics "cannot well explain" (self-destructive behavior, identity-based conflict, preference manipulation, choice of who to be) become tractable once identity enters the utility function?

## Method / identification
The paper is theoretical. Its central object is an augmented utility function
$$U_j = U_j(a_j, a_{-j}, I_j),$$
where $a_j$ are $j$'s own actions, $a_{-j}$ others' actions, and $I_j$ is $j$'s identity (self-image). Identity itself is a function
$$I_j = I_j(a_j, a_{-j}; c_j, \varepsilon_j, P),$$
with $c_j$ the assignment of people to social categories $C$ (as perceived by $j$), $\varepsilon_j$ $j$'s given characteristics, and $P$ the prescriptions specifying ideal attributes and appropriate behavior for each category. Changes in utility flowing through $I_j$ are called gains or losses in identity. An individual chooses actions (and, where categories are non-ascriptive, possibly the category assignment) to maximize $U_j$; the authors are deliberately agnostic about whether the agent is conscious of these motivations.

The core analytic device is a **prototype Green/Red game** (Section III). Everyone is "Green"; the prescription is that Greens do Activity One. A person with a taste for an activity earns $V$ from matching her taste, zero otherwise. Choosing Activity Two costs a self loss $I_s$ ("not a true Green"). When two agents $i,j$ are paired, $i$ choosing Activity Two imposes an identity externality $I_o$ on $j$; $j$ may then "respond," restoring her identity at cost $c$ to herself while inflicting loss $L$ on $i$. Person One (taste for One) moves first; Person Two (taste for Two) follows. The model is solved for subgame-perfect equilibrium and the authors map $I_s$, $I_o$, $c$, $L$ onto the psychodynamic theory of personality (internalization, the superego, anxiety from violating internalized rules). The applied sections embed this structure into specific economic environments (a firm assigning workers to gendered jobs; a community choosing identities and work).

## Data
None — this is a pure theory paper. The argument is supported throughout by *existing* empirical and ethnographic evidence cited illustratively: Goldin's occupational-segregation series (two-thirds of workers would have had to switch jobs for parity in 1970, falling to 53 percent by 1990); ethnographies of oppositional identity (MacLeod's Hallway Hangers, Willis's "lads" vs. "earholes," Whyte's Corner Boys); and program evaluations (Job Corps vs. JOBSTART). No new dataset or estimation.

## Key findings
- **Four subgame-perfect outcomes of the prototype game.** Person One deters Person Two when $c < I_o$ and $I_s < V < I_s + L$; Person One responds but does not deter when $c < I_o$ and $I_s + L < V$; Person One does not respond and Two deviates when $c > I_o$ and $I_s < V$; and Person Two never deviates regardless when $I_s > V$. The thresholds make explicit how identity parameters, not just prices, determine behavior.
- **Identity as a new externality and a microfoundation for "distaste."** Men's apparent "distaste" for working alongside women (Becker/Arrow-style discrimination) is reinterpreted as a genuine identity loss when women enter "men's" jobs; firms internalize this by segregating occupations. This rationalizes persistent occupational segregation and the sharp post-1970 decline as a shift in societal gender prescriptions rather than tastes or productivity.
- **Oppositional identity and poverty.** In the poverty/exclusion model, Greens suffer a loss $r$ from non-acceptance by the dominant culture while Reds do not; Reds earn $v_i - a$ from working. An All-Green equilibrium exists iff $r < I_o^R$; for higher $r$, Mixed or All-Red equilibria emerge. Crucially, social exclusion ($r>0$) alone induces some to adopt an oppositional Red identity and "not work," **even absent any conformity-generating externalities** ($I_o^R = I_o^G = k = 0$) — a departure from conformity-based models. Comparative statics reproduce Wilson's account: middle-class out-migration and the disappearance of work push more of the community toward Red identities. The model also explains why residential Job Corps (which removes trainees from the neighborhood, lowering $r$) can succeed where non-residential JOBSTART fails.
- **General point.** In each application, adding identity overturns or enriches a standard result: "self-destructive" behavior becomes rational given low endowments and high exclusion, and policy levers act through prescriptions and category assignment.

## Contribution
Founds **identity economics**: the first formal incorporation of self-image and social categories into a utility function with broad economic application. It shows that many standard psychological and sociological concepts — self-image, ideal type, in-group/out-group, social category, identification, anxiety — fit naturally and yield testable, non-standard predictions across labor, poverty, and household economics. It reframes choice of identity as potentially "the most important economic decision people make" and supplies a unified, general channel for non-pecuniary motivation.

## Limitations & open questions
The authors flag several open problems as a research agenda. (1) **Endogenous formation of identity-based preferences** — where do prescriptions and categories come from? They note evolutionary-psychology and social-cognition accounts but argue these struggle with the variety of categories across societies and time. (2) **Comparative work across space and time** — why "class" or "race" differ across countries, why gender/racial integration varies across industries, what drives the rise and fall of ethnic tension. (3) **Manipulation of identity** — advertisers, politicians, and activists have incentives to change prescriptions; modeling this strategically is left open. (4) **Many further domains** (retirement, labor relations, schooling) where documented social categories could be plugged in for new results. The models themselves are deliberately stylized (two categories, simple prescriptions, full analysis relegated to an available appendix), inviting richer specifications.

## Connections
The reinterpretation of taste-based discrimination builds directly on Becker (1971) and Arrow (1972), and the human-capital/participation accounts of Mincer & Polachek (1974), Bulow & Summers (1986), and Lazear & Rosen (1990); Goldin (1990a, 1990b) supplies the gender "auras" and pollution-theory of discrimination. The household application engages the collective/bargaining tradition of Manser & Brown (1980), McElroy & Horney (1981), and Lundberg & Pollak (1993). The poverty model is contrasted with conformity-based social-interaction models — the authors' own Akerlof (1997) "Social Distance" paper and Brock & Durlauf (1995) — and with Bénabou (1993, 1996) on neighborhood externalities. The identity-response mechanism is explicitly linked to [[@Rabin1993|Rabin's (1993)]] fairness model, where agents pay to punish unkindness; Folbre (1994) and Sen (1985) are cited as precursors gesturing at identity, and Montgomery (1994, 1997) on role theory and cognitive dissonance. The line of work continues in Akerlof & Kranton's later writing on identity and schooling and their book *Identity Economics*, and connects to social-preference and norm-based modeling (e.g., Bénabou & Tirole on identity and motivation).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
