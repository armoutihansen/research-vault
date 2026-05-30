---
citekey: Koszegi2006
title: Emotional Agency
authors: ["Kőszegi, Botond"]
year: 2006
type: journalArticle
doi: 10.1093/qje/121.1.121
zotero: "zotero://select/library/items/XXJQALMV"
pdf: /Users/jesper/Zotero/storage/FNM5CED4/Koszegi2006.pdf
tags: [literature]
keywords: [anticipatory-emotions, cheap-talk, information-disclosure, belief-based-utility, principal-agent, psychological-games]
topics: []
related: [Caplin2001, Milgrom1981]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper models interactions between a party with anticipatory emotions and a party who responds strategically to those emotions, a situation that is common in many health, political, employment, and personal settings. An "agent" has information with both decision-making value and emotional implications for an uninformed "principal" whose utility she wants to maximize. If she cannot directly reveal her information, to increase the principal's anticipatory utility she distorts instrumental decisions toward the action associated with good news. But because anticipatory utility derives from beliefs about instrumental outcomes, undistorted actions would yield higher ex ante total and anticipatory utility. If the agent can certifiably convey her information, she does so for good news, but unless this leads the principal to make a very costly mistake, to shelter his feelings she pretends to be uninformed when the news is bad.

## Summary
An informed "agent" (doctor, manager, government, parent, lover) whose interests are *perfectly aligned* with an uninformed "principal" nonetheless fails to maximize the principal's welfare, purely because the principal has belief-based *anticipatory emotions*. To make the principal feel better, the agent slants cheap-talk recommendations toward the good-news action; but since emotions ultimately derive from expected physical outcomes, this self-defeating distortion lowers both physical and anticipatory utility. Under certifiable disclosure the mirror result holds: the agent reveals good news and conceals bad news (pretending ignorance) unless concealment risks a very costly wrong action.

## Research question
How does an informed, benevolent agent behave when the information she conveys not only guides a decision but also shapes an uninformed principal's *anticipatory* emotions, and when do these emotions cause welfare losses even though the parties' interests are perfectly aligned?

## Method / identification
A two-period game-theoretic model adapting the anticipatory-utility framework of [[@Caplin2001|Caplin and Leahy]] (2001, 2004) to cheap talk and to a payoff-relevant action. The principal's von Neumann–Morgenstern utility is a convex combination of physical and anticipatory utility,
$$U(\mu,s,t) = w\cdot\!\int h(s',t)\,d\mu(s') + (1-w)\cdot h(s,t),$$
with $w\in(0,1)$ the weight on emotions, anticipatory utility equal to expected physical utility under beliefs $\mu$. The agent privately observes state $s\in[0,1]$; an action $t\in\{0,1\}$ is taken by either party. Assumption (A1) sets $h(s,t)=s-l(s,t)$ with a loss $l\ge 0$, $\min_t l(s,t)=0$, and $L(s)\equiv l(s,1)-l(s,0)$ strictly decreasing with a crossing $s^*$ where $L(s^*)=0$ (so $t=1$ is appropriate for high $s$). The solution concept is *emotional perfect Bayesian equilibrium* (EPBE): agent optimization (message maximizes the principal's utility given inferences), principal optimization, and Bayesian updating. Attention is restricted to "simple" EPBE (messages inducing identical action and anticipatory utility are merged). The author argues EPBE coincides with the psychological-equilibrium concept of Geanakoplos, Pearce & Stacchetti (1989) here but corresponds more closely to the driving intuition. Two regimes are analyzed: cheap talk (Section IV, agent cannot certify $s$) and certifiable disclosure (Section V, the agent can prove $s$ when known but cannot prove ignorance, with informedness probability $\alpha$).

## Data
None — this is a pure theory paper. Section III instead supplies motivating *applications* (doctor–patient, political economy / terror-alert systems, organizational and wartime morale, parenting, romantic relationships, academic advising) and cites empirical and journalistic evidence (e.g., SARS, the DHS color-coded threat system) that agents are cognizant of and respond to principals' emotions.

## Key findings
- **Lemma 1**: In a simple EPBE the agent sends at most two messages with positive probability; communication collapses to a binary "recommendation."
- **Proposition 1 (Ex ante optimal policy)**: The welfare-maximizing rule is to choose $t=0$ iff $s\le s^*$; because anticipatory utility equals expected physical utility ex ante, maximizing physical utility also maximizes anticipatory utility.
- **Proposition 2 (Distortion in action)**: In any informative EPBE there is a cutoff $s^c\in(0,s^*)$ with $t=0$ chosen iff $s\le s^c$ — the good-news action $t=1$ is chosen *too often*. The indifference condition is $w\cdot(E[s-l(s,1)\mid s>s^c]-E[s\mid s\le s^c]) = (1-w)\cdot L(s^c)$, balancing the anticipatory gain of good news against the physical-utility gain of accurate news. The agent fails to maximize the principal's utility *because* she tries to — an informational externality she does not internalize.
- **Proposition 3 (Welfare and existence)**: An informative EPBE exists for $w<\bar w$; the principal's best-EPBE expected utility is strictly decreasing in $w$ (stronger feelings are *self-defeating*), yet still weakly better than committing to a single action.
- **Proposition 4 (Agent chooses $t$)**: The over-use of $t=1$ survives, with a striking new possibility — distortion can be so severe that ignoring all information and always choosing $t=0$ would yield higher welfare, i.e., the agent's private information *reduces* welfare.
- **Subsection IV.D (Commitment)**: Committing to state-contingent norms restores the optimum; even committing to a *fixed* action can raise welfare when the agent chooses $t$ (rationalizing the DHS keeping threat levels persistently elevated).
- **Propositions 7–8 (Certifiable disclosure)**: With $\alpha=1$ a Caplin–Leahy-style unraveling gives full disclosure ($\bar s=0$). With $\alpha<1$ there is a unique threshold $\bar s>0$: the agent discloses good news ($s\ge\bar s$) and conceals bad news, exploiting the possibility she is uninformed to protect feelings; with action choice she additionally discloses very bad news (a set $N$) when needed to induce $t=0$.

## Contribution
Introduces *strategic responses to others' anticipatory emotions* as a distinct economic force, separated from the divergent-interest frictions of standard cheap-talk and disclosure models (Crawford & Sobel 1982; Grossman & Hart 1980). It shows that benevolence plus belief-based emotions alone generate systematic, welfare-reducing communication distortions, links the inefficiency to a Kydland–Prescott-style time-inconsistency / commitment problem, and extends Caplin & Leahy's full-disclosure result to a continuum of states and to settings with action choice.

## Limitations & open questions
- **Static interaction**: The model is two-period. The author flags *dynamic* extensions with multiple communication opportunities, where the *timing* (not just content) of disclosure becomes strategic — bad news may be withheld early and released as the principal grows skeptical or the decision nears.
- **Sophistication assumption**: The principal is strategically sophisticated. A *naïve* principal who takes the agent at face value yields different welfare conclusions (higher $w$ can raise his perceived utility; naïveté can dominate sophistication) — a hook for behavioral/biased-belief modeling.
- **Exogenous relationships**: The principal cannot choose his agent. Endogenizing selection — patients choosing doctors, citizens electing governments, employees choosing employers — and asking when *reputation* or *competition* mitigates or worsens the distortion is named as "an important future agenda."
- The non-disclosable-vs-certifiable dichotomy is extreme; intermediate verifiability and nonlinear anticipatory utility are only partially explored (footnote 5 argues key results survive nonlinearity).

## Connections
Builds directly on [[@Caplin2001|Caplin and Leahy]] (2001, 2004) on anticipatory/psychological utility, and uses the psychological-games equilibrium of Geanakoplos, Pearce and Stacchetti (1989). The cheap-talk machinery descends from Crawford and Sobel (1982) and the expert-advice literature (Scharfstein and Stein 1990; Prendergast and Stole 1996; Dessein 2002). The disclosure results parallel unraveling in corporate finance — Grossman and Hart (1980), [[@Milgrom1981|Milgrom (1981)]], Jung and Kwon (1988), with a textbook treatment in Bolton and Dewatripont (2005). The commitment/welfare logic is explicitly tied to Kydland and Prescott (1977) on time-inconsistent policy. The morale applications relate to Bewley (1999) and to Fang and Moscarini (2005) on overconfidence and wage compression. The broader belief-based-utility and motivated-reasoning agenda connects to Bénabou and Tirole's work on self-image and motivated beliefs, and to Akerlof and Dickens-style models of belief manipulation.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
