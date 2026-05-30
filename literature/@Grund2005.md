---
citekey: Grund2005
title: "<span style=\"font-variant:small-caps;\">Envy and Compassion in Tournaments</span>"
authors: ["Grund, Christian", "Sliwka, Dirk"]
year: 2005
type: journalArticle
doi: 10.1111/j.1430-9134.2005.00039.x
zotero: "zotero://select/library/items/KSIUKQJS"
pdf: /Users/jesper/Zotero/storage/8V6T6GZS/Grund and Sliwka - 2005 - Envy and Compassion in Tournaments.pdf
tags: [literature]
keywords: [tournaments, inequity-aversion, envy, compassion, promotion-policy, incentive-theory, social-preferences]
topics: []
related: [Bolton2000, Charness2002, Fehr1999, Itoh2004, Lazear1981, Nalebuff1983]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Many experiments and field studies indicate that most individuals are not purely motivated by material self-interest but also care about the well being of others. In this paper, we examine tournaments among inequity averse agents, who dislike disadvantageous inequity (envy) and advantageous inequity (compassion). It turns out that inequity averse agents exert higher efforts than purely self-interested agents for a given prize structure. Contrary to standard tournament theory, first-best efforts cannot be implemented when prizes are endogenous. Furthermore, the choice between vertical and lateral promotions is examined and it is shown that inequity costs have to be traded off against losses in human capital.

## Summary
Grund and Sliwka embed Fehr–Schmidt inequity aversion into the canonical Lazear–Rosen rank-order tournament. Splitting inequity aversion into envy (disutility from being behind, $\alpha$) and compassion (disutility from being ahead, $\beta$), they show that for a fixed prize structure inequity-averse agents exert *more* effort than selfish agents, because envy widens the perceived utility gap between winning and losing. But once the principal optimally designs prizes subject to a participation constraint, this "incentive effect" can be costlessly neutralized while an irreducible "participation effect" (inequity costs) remains, so the tournament can no longer implement first-best effort. The framework is then applied to the vertical-vs-lateral promotion decision.

## Research question
How does inequity aversion (decomposed into envy and compassion) affect equilibrium effort, optimal prize design, and the principal's profit in rank-order tournaments? And what does this imply for the firm's choice between vertical promotions (promote within the group) and lateral promotions (promote across groups)?

## Method / identification
A two-agent rank-order tournament. Agent $i$ produces $q_i=h(e_i)+\varepsilon_i$ with $h$ concave, convex effort cost $C(e_i)$, and i.i.d. noise; the higher $q_i$ wins prize $w_1$, the loser gets $w_2<w_1$, with spread $\Delta w=w_1-w_2$ (negative wages allowed — no limited liability, unlike Demougin & Fluet). Preferences follow Fehr & Schmidt:
$$u_i = w_i - \alpha\max\{w_j-w_i,0\} - \beta\max\{w_i-w_j,0\} - C(e_i),$$
with $\alpha\ge\beta\ge0$ and $\beta<1$. The winner's utility is $w_2+(1-\beta)\Delta w - C(e_i)$; the loser's is $w_2-\alpha\Delta w - C(e_i)$. Let $G$ be the CDF of $\varepsilon_i-\varepsilon_j$ (symmetric, density $g$). The analysis is a two-stage game: (i) characterize the symmetric pure-strategy Nash equilibrium in effort for given prizes via first-order conditions; (ii) solve the principal's profit maximization $2h(e^*)-2w_2-\Delta w$ subject to the binding participation constraint, substituting out $w_2$ and using the envelope theorem for comparative statics. The promotion application introduces $\tau$, the probability a promotion is vertical (envy/compassion only bite under vertical promotion), and a human-capital return difference $\Delta k=k_H-k_L$.

## Data
None — this is a pure theory paper. The authors cite, but do not themselves collect, experimental evidence: Falk & Fehr (2003) on tournament effort exceeding selfish predictions (reproduced as Figure 1), and Harbring & Irlenbusch (2003, 2004) on effort and sabotage.

## Key findings
**Proposition 1 (fixed prizes).** The symmetric equilibrium effort $e^*$ solves
$$\Delta w(1-\beta+\alpha)\,g(0)=\frac{C'(e^*)}{h'(e^*)},$$
so $e^*$ rises in $\Delta w$ and in envy $\alpha$, and falls in compassion $\beta$. Since $\alpha\ge\beta$, inequity-averse agents work harder than selfish ones (the "incentive effect"). **Corollary 1:** with fixed prizes the principal's profit rises in $\alpha$ and falls in $\beta$ — she prefers more envious agents.

**Proposition 2 (endogenous prizes).** The optimally implemented effort $e^{SB}$ satisfies
$$h'(e^{SB})-\frac{C''(e^{SB})h'(e^{SB})-C'(e^{SB})h''(e^{SB})}{(h'(e^{SB}))^2}\cdot\frac{(\alpha+\beta)}{2(1+\alpha-\beta)g(0)}=C'(e^{SB}),$$
with the correction term strictly positive whenever $\alpha$ or $\beta>0$, so $e^{SB}$ falls short of the first-best $h'(e^{FB})=C'(e^{FB})$. Inequity costs equal $(\alpha+\beta)\Delta w$. **Corollary 2:** selfish agents ($\alpha=\beta=0$) yield strictly higher profits; profits strictly decrease in $\beta$, and decrease in $\alpha$ iff $\beta<\tfrac12$ (can increase in $\alpha$ when $\beta>\tfrac12$). The incentive effect vanishes under free prize design (the principal can hit any effort by adjusting $w_2$), but the participation effect (inequity costs) always reduces welfare — analogous to the risk–incentive trade-off.

**Extensions.** Spite ($\beta<0$) raises effort further; if $\alpha<|\beta|$ the principal even over-implements relative to first-best. Sabotage effort also rises with envy. Results extend to $n$-person tournaments with at least $n/2$ winner prizes.

**Proposition 3 (promotions).** For fixed prizes, profit strictly increases in $\tau$: vertical promotions are best (effort-maximizing). For endogenous prizes, lateral promotions economize on inequity costs, so vertical promotion is optimal iff the human-capital loss $\Delta k$ is large enough. Implication: promote laterally across groups doing *related* tasks.

## Contribution
First (jointly with the independent Demougin & Fluet 2003b, but without their limited-liability assumption) to integrate the full two-sided Fehr–Schmidt utility — both envy and compassion — into a rank-order tournament, cleanly separating an incentive effect from a participation effect. It overturns the standard result that symmetric tournaments implement first-best effort, and derives a novel organizational-design implication for promotion policy (vertical vs. lateral), grounded in the social-distance dependence of reference groups.

## Limitations & open questions
- The model assumes envy/compassion are zero (or merely weaker) under lateral promotion; relaxing this is only sketched.
- Reservation utility $U_0$ is taken independent of $\alpha,\beta$ — the authors justify this via social distance but it is an assumption.
- The $n$-person extension is stated without full proof (available on request); with fewer than $n/2$ winners, envy weakens and the effort comparison can reverse.
- Sabotage and heterogeneous-agent cases are treated informally, deferred to the earlier IZA version.
- The authors explicitly flag empirical testing as future work: e.g., do non-tenured assistant professors work harder when a same-field, same-faculty peer is also up for tenure? Outside-hiring as an alternative inequity-cost reducer (it lowers incentives) is also left open.

## Connections
Builds directly on [[@Lazear1981|Lazear & Rosen (1981)]] and the tournament literature ([[@Nalebuff1983|Nalebuff & Stiglitz 1983]]; O'Keefe, Viscusi & Zeckhauser 1984; Lazear 1989 on sabotage). The preference model is [[@Fehr1999|Fehr & Schmidt (1999)]]; the close substitute is [[@Bolton2000|Bolton & Ockenfels (2000)]], with [[@Charness2002|Charness & Rabin (2002)]] offering an alternative social-preference representation. Closest contemporaries are Demougin & Fluet (2003a,b) and Neilson & Stowe (2003) on the incentive/inequity trade-off in individual pay, and Kräkel (2000) and Stark (1990) on relative deprivation in tournaments. Empirical anchors are Falk & Fehr (2003) and Harbring & Irlenbusch (2003, 2004); foundational evidence on inequity aversion comes from Loewenstein, Thompson & Bazerman (1989) and Zizzo & Oswald (2001). Related single-agent and team moral-hazard work includes Englmaier & Wambach (2002), Fehr, Klein & Schmidt (2002), [[@Itoh2004|Itoh (2004)]], and Huck & Biel (2002). The promotion application connects to Chan (1996) on internal promotion vs. external hiring, and status-seeking links to Frank (1985).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
