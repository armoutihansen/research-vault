---
citekey: Carpenter2016
title: "Motivating Agents: How Much Does the Mission Matter?"
authors: ["Carpenter, Jeffrey", "Gong, Erick"]
year: 2016
type: journalArticle
doi: 10.1086/682345
zotero: "zotero://select/library/items/3DAIPJUS"
pdf: /Users/jesper/Zotero/storage/9ZQU9NPG/Carpenter2016.pdf
tags: [literature]
keywords: [mission-motivation, motivated-agents, real-effort-experiment, incentives, principal-agent, prosocial-motivation, field-experiment-design]
topics: []
related: [Benabou2003, Besley2005, Trueblood2013]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Economic theory predicts that agents work harder if they believe in the mission of the organization. We conduct a real-effort experiment with workers whose mission preferences are known, randomly assigning them to organizations with clear missions to create both matches and mismatches. Our estimates suggest that matching is a strong motivator, especially compared to mismatches. Further, we find that performance pay increases effort, though mostly among mismatched workers who substitute pay for matching. Our results suggest the importance of defining a clear mission to an organization and highlight the significance of sorting, screening, and compensation policies.

## Summary
Carpenter and Gong run a real-effort lab experiment that cleanly separates the motivational effect of a worker-organization "mission match" from the confounding selection effects that plague observational data. Using the 2012 US presidential election as a source of naturally occurring, diametrically opposed missions (Obama vs. Romney campaigns), they randomly assign students of known political preference to stuff campaign letters for one candidate, crossing match/mismatch with weak/strong financial incentives in a 2x2 design. The headline result: matched workers produce 72% more output than mismatched workers, and high-powered piece rates raise effort most for the mismatched, acting as an imperfect substitute for mission alignment. They find no evidence that incentives crowd out mission-driven motivation.

## Research question
Holding selection constant, how large is the pure causal effect of mission alignment on worker effort? And, when workers are mismatched (uninspired by the organization's mission), can high-powered financial incentives (piece rates) substitute for the missing intrinsic, mission-based motivation? A subsidiary question asks whether the intensity of a worker's mission preferences moderates these effects.

## Method / identification
The core is a real-effort lab experiment (not chosen-effort), deliberately chosen because the literature (Van Dijk, Sonnemans, and Winden 2001) shows real-effort designs yield conservative treatment estimates. The empirical design is a 2x2 between-subjects factorial: mission match vs. mismatch, crossed with weak vs. strong incentives, with random assignment of both factors.

The conceptual framework (appendix A.1) is a standard linear-contract principal-agent model. The agent receives wage $w$ plus piece rate $p$ per unit of effort/output $e$, with convex effort cost $C(e)$ where $C_e>0$ and $C_{ee}>0$. Mission-oriented agents (following [[@Besley2005|Besley and Ghatak 2005)]] receive a mission-utility increment $M(e,g)$ with $M_e>0$, $M_{ee}<0$, where $g$ is the intensity of mission preference ($M_g>0$, $M_{gg}<0$, and complementarity $M_{eg}>0$). A match indicator $v\in\{-1,1\}$ ($v=1$ match, $v=-1$ mismatch) signs this term, so the agent maximizes
$$U(e)=(w+pe)+vM(e,g)-C(e),$$
yielding the first-order condition $p+vM_e=C_e$. The model nests the standard agent at $g=0$ (i.e. $M(e,0)=0$). Agents work iff the participation constraint $U(e^*)>\underline{U}$ holds against an unknown reservation utility. The framework delivers signed comparative statics: $e^*_{v=1}>e^*_{v=-1}$ (matching raises effort, intensive margin) and matching raises the probability the participation constraint binds (extensive margin); $de^*/dp>0$ for all; and crucially $de^*(v=-1)/dp>de^*(v=1)/dp$, i.e. incentives bite harder for mismatches because additive separability gives matched workers a common cost curve but larger working benefits, pushing them further up the (steeper) marginal-cost region. Intensity predictions: $de^*(v=1)/dg>0$ but $de^*(v=-1)/dg<0$.

Estimation is OLS:
$$\text{Output}_i=\alpha+\beta_1\text{Match}_i+\beta_2\text{Incentive}_i+\beta_3(\text{Match}_i\times\text{Incentive}_i)+X_i'\lambda+\varepsilon_i,$$
where the interaction $\beta_3$ captures the differential incentive effect for matches, and controls $X$ include first-round "ability", political preferences, gender, ethnicity, US-birth, voter registration, and self-reported minimum-wage effort. The extensive margin uses a binary "produced any output" outcome; the intensive margin conditions on working. Preference intensity is elicited separately via a $100 dictator game splitting money with a candidate's campaign (per Carpenter and Myers 2010). Mission match is varied exogenously by random campaign assignment; preferences were measured ~2 weeks earlier via a web survey using the 7-point ANES party-ID Likert scale, with stratification by anonymous postal-box number to balance matches/mismatches given the Democratic skew of the campus.

## Data
Original experimental data: 12 sessions, 207 participants (Middlebury College students), fall 2012. Outcome is letters correctly addressed and stuffed in a 15-minute production phase. A prior uncompensated "ability" round (stuffing thank-you notes for the college) provides a baseline productivity control. Incentive arms: base $20; base + $0.50/letter; base + $1.00/letter (the two piece-rate arms collapsed since they do not differ statistically). Letters were real campaign mailers addressed to independent voters in Hamilton County, Ohio. Average earning was $25.74. Balance checks across 15 covariates show essentially no significant differences (one marginal ability difference, favoring against finding incentive effects); pre/post political-preference correlation is high ($r=.9$), confirming preference stability.

## Key findings
1. Matching is a strong motivator: matched workers produce ~72% more than mismatched (15.63 vs. 9.07 letters); one matched worker equals ~1.7 mismatched workers. Decomposed: matching raises the probability of working by 33 percentage points (a 56% extensive-margin increase over the 66% mismatch participation rate) and raises conditional output by ~19% (intensive margin).
2. Incentives raise effort overall by ~35% (10.49 to 14.18 letters), via an 8% extensive-margin and ~23% intensive-margin increase.
3. The signature result confirms the model's differential prediction: piece rates raise matched output only ~13% but mismatched output ~86%; incentives recover more than two-thirds (~68%) of the productivity lost to a poor match. The $\text{Match}\times\text{Incentive}$ interaction is negative and significant at 1%, so incentives are an imperfect substitute for mission matching.
4. Intensity asymmetry (table 4): among matches, preference intensity has no significant effect, but among mismatches stronger preferences reduce output (each $10 of dictator-game giving cuts ~0.47 letters, ~5%; any positive giving cuts output ~31%), consistent with $de^*(v=-1)/dg<0$.
5. Upper-bound decomposition: using zero dictator-game givers as a "no-match" reference, matching raises output ~27% while mismatching lowers it ~43%; the 72% match-vs-mismatch figure is thus an upper bound driven heavily by the mismatch disincentive. Incentives raise mismatch output to roughly the no-match level and no-match output to roughly the matched level.
6. No crowding-out: contrary to [[@Benabou2003|Benabou and Tirole (2003)]] and the evidence reviewed in Bowles and Polania-Reyes (2012), incentives do not depress matched workers' effort; matched workers still gain a small increment.

## Contribution
The paper provides the first clean experimental estimate of the pure motivational effect of mission match on real effort, purged of selection, and the first to estimate both the match benefit and the mismatch penalty within one design. Unlike prior chosen-effort or charity-donation experiments (Fehrler and Kosfeld 2014; Tonin and Vlassopoulos 2010, 2015; Gerhards 2012), workers here perform a genuine task tied directly to the organization's mission rather than donating earnings. It supplies direct empirical confirmation of the [[@Besley2005|Besley and Ghatak (2005)]] substitutability prediction between mission preferences and high-powered incentives, with concrete HR-policy implications: write and use a clear mission to attract and screen intrinsically motivated workers (economizing on costly incentives); where screening is infeasible, high-powered pay can repair most of the mismatch deficit without harming matched workers (per-unit cost was $2.10 with piece rates vs. $1.72 without, while mission alignment's effect is far larger).

## Limitations & open questions
- By design the study removes selection ("mechanism experiment" in the sense of Ludwig, Kling, and Mullainathan 2011), so it does not speak to the equilibrium staffing of real campaigns or how sorting interacts with the estimated effects; integrating selection with the motivational effect is left open.
- It is artificial that workers can be assigned to the opposing campaign; real mismatches arise differently (e.g. mission drift, tight labor markets), and external validity to such settings is asserted, not tested.
- The "no-match" group (zero dictator-game givers) is not randomly assigned, so the match/mismatch decomposition is treated cautiously; the authors flag possible confounds (though they find no income correlation).
- The link between an individual worker's input and ultimate mission success is weak in this setting (one vote among many); whether the result holds when that link is even more tenuous is noted as an open situation many mission-oriented workers face.
- Whether and why principals derive nonpecuniary benefits from a mission, and how they choose missions, is explicitly outside scope.
- Welfare implications for agents are ambiguous: better-funded firms could exploit worker goodwill (the Apple-retail anecdote), an equity/welfare question left unresolved.
- Generalizability is limited to tasks that are not personally satisfying but feel worthwhile via the mission (clerical, manual, military, low-level bureaucratic work); the sample is college students.

## Connections
The theoretical backbone is [[@Besley2005|Besley and Ghatak]] (2005, AER) on competition and incentives with motivated agents, whose substitutability prediction this paper tests; it builds on Francois (2000) on public-service motivation and Akerlof and Kranton (2005) on identity in organizations. The crowding-out non-result engages [[@Benabou2003|Benabou and Tirole (2003)]] and the survey by Bowles and Polania-Reyes (2012). Methodologically it follows the real-effort tradition of Van Dijk, Sonnemans, and Winden (2001), Gneezy and List (2006), and Hennig-Schmidt, Sadrieh, and Rockenbach (2010), and contrasts with chosen-effort / donation designs of Fehrler and Kosfeld (2014), Tonin and Vlassopoulos (2010, 2015), Gerhards (2012), and Gregg et al. (2011). Preference-intensity elicitation draws on Carpenter and Myers (2010), candidate placement on Krupka and Weber (2013), and the sorting/self-selection logic on Salop and Salop (1976) and Lazear and Oyer (2013). The substitutability of working-in vs. donating echoes [[@Trueblood2013|Brown, Meer, and Williams (2013)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
