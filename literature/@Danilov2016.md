---
citekey: Danilov2016
title: Can Contracts Signal Social Norms?
authors: ["Danilov, Anastasia", "Sliwka, Dirk"]
year: 2016
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/WGBK7USD"
pdf: /Users/jesper/Zotero/storage/HXIRAVIH/Danilov2016.pdf
tags: [literature]
keywords: [social-norms, incentive-contracts, signaling, conformity, principal-agent, lab-experiment, trust]
topics: []
related: [Gneezy2000, Sliwka2007]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We investigate whether incentive schemes signal social norms and thus affect behavior beyond their direct economic consequences. A one-shot principal-agent experiment is studied, in which prior to contract choice principals are informed about the past actions of other agents and thus have more information about norms of behavior. Compared to a setting in which principals are uninformed, agents exert substantially higher effort under a fixed wage contract when they are aware that an informed principal chose this contract. The informed principal's choice apparently signals a norm not to exploit trust, which leads to more trustworthy behavior. This mechanism's robustness is explored in further experiments.

## Summary

Through a series of one-shot principal-agent lab experiments, Danilov and Sliwka show that a contract is not just an incentive device but a *signal* about prevailing social norms. When agents know the principal chose a fixed (trust) wage while being informed about the past behavior of other agents, they exert substantially higher effort than when the same contract is chosen by an uninformed principal — effort rises by 25-42% under the trust contract, while effort under performance-contingent pay is essentially unaffected. The mechanism rests on a preference for conformity: an informed principal's willingness to offer a trust wage credibly reveals that shirking is uncommon in the population, and conformist agents respond by not exploiting that trust.

## Research question

Can the choice of an incentive scheme convey information about prevailing social norms of behavior, and thereby affect agents' actions *beyond* the contract's direct economic consequences? Specifically: does an identical contract elicit different effort when agents know it was selected by a principal who is better informed about others' past behavior?

## Method / identification

The core design is a one-shot principal-agent game. Each pair receives a €6 endowment. The principal (employer) chooses between a fixed wage / "trust" contract $t$ (unconditional €5) and a performance-contingent contract $c$ (€5 only on success). The agent picks effort $e\in[0,100]$ at cost $c(e)=e^2/1200$; effort equals the probability the principal earns €12. Effort under *both* contracts is elicited via the strategy method before the agent learns the principal's choice.

The main manipulation is a 2×2 between-subjects design crossing **Baseline vs. Norms** with **Costless vs. Costly**. In the *Norms* treatment, principals are shown a table of 10 real agents' efforts from a prior Baseline session; agents are told the principal saw such a table but not its contents. In the *Costly* setting the contingent contract carries an extra €2 cost to the principal, shifting relative contract attractiveness and hence the signal's informativeness. 691 subjects, 25 sessions, zTree/ORSEE at Cologne; 80-93 dyads per treatment. The identifying contrast is a difference-in-difference (Trust contract × Norms treatment) in OLS regressions with clustered standard errors.

A formal signaling model (Appendix B), generalizing [[@Sliwka2007|Sliwka (2007)]] to continuous types, underpins the design. Agent utility is

$$u_A(\pi_A,\pi_P)=\pi_A+\theta_A\cdot\pi_P,$$

where $\theta_A$ is prosociality. Agents are *steadfast* (exogenous $\theta$) or *conformist* ($\theta_A=E[\theta\mid \text{info}]$, matching the population norm $N$). With fraction $\eta$ steadfast, optimal efforts are $e_t(\theta)=\theta B/c$ under trust and $e_c(\theta)=(b+\theta(B-b))/c$ under the contingent contract, so $\partial e_t/\partial\theta = B/c > \partial e_c/\partial\theta=(B-b)/c$ — conformist effort is more sensitive to beliefs about the norm under the trust contract. The principal privately observes $N$, making it a signaling game.

## Data

Primary experimental data from 691 subjects across the four core treatments, plus auxiliary experiments: incentivized first-party belief elicitation (last 16 sessions, quadratic-loss scoring), strategy-method elicitation of 92 principals' contract choices across five ranked tables, and separate online third-party belief experiments (Contingent Contract Beliefs $N=57$, Trust Contract Beliefs $N=61$, Baseline Beliefs $N=60$).

## Key findings

- **Main effect.** Effort under the fixed wage rises 25% (Costless, $p=0.0575$) and 42% (Costly, $p=0.0034$) in Norms vs. Baseline; contingent-pay effort is unchanged (insignificant). The difference-in-difference is significant ($p=0.0552$ Costless, $p=0.0004$ Costly) and almost entirely driven by the fixed-wage increase. The fraction choosing very low effort (0-4) under the fixed wage drops sharply (e.g., 40.7%→17.5% Costly), and effort variance falls — norms signaling yields more consistent behavior.
- **No cost effect.** The Costly vs. Costless contrast in effort reactions is insignificant; the model rationalizes this via countervailing forces (Proposition 1(ii): the separating cut-off $\bar N$ falls with cost $k$, so separation is easier but the effort response weaker).
- **Belief channel (premise 1).** Both first-party and impartial third-party beliefs about others' effort shift with the observed contract: observers infer higher effort under whichever contract the principal chose.
- **Principal behavior (premise 2).** Principals adapt contract choices to observed prosociality — choosing the fixed wage more for prosocial tables (ranks 1-2) and less for selfish ones (ranks 4-5).
- **Theory.** *Proposition 1*: if $B>\frac{b}{c}(w-k)$ and $\eta$ is large, a unique separating equilibrium exists with cut-off $\bar N$; post-trust norm beliefs exceed post-contingent beliefs, and $\bar N$ is decreasing in $k$. *Corollary 1*: in any separating equilibrium, norms signaling raises trust-contract effort and lowers contingent-contract effort relative to no signaling. *Proposition 2* characterizes when a pooling equilibrium (always contingent) survives.

## Contribution

The paper provides clean causal evidence that contracts signal norms and shift behavior even when agents' actions are unobservable to peers, there is no technological complementarity, and no ex-post feedback. This isolates an *intrinsic preference for conformity* as the driver, ruling out image concerns (Bénabou & Tirole, 2012) and coordination/complementarity channels (Friebel & Schnedler, 2011; van der Weele, 2012). It is the first experimental test of the [[@Sliwka2007|Sliwka (2007)]] signaling mechanism, extending that model to continuous types, and connects the crowding-out literature (Gneezy & Rustichini, 2000) to contracts-as-norm-signals.

## Limitations & open questions

- The authors flag that elicited first-party beliefs are endogenous and possibly subject to false-consensus or self-serving justification; third-party online beliefs may be inaccurate because observers struggle with indirect inference.
- The strategic inference "what exactly does a strategically chosen contract reveal about the norm?" requires higher common knowledge of rationality than the simpler "an informed principal offering a fixed wage cannot have seen many shirkers."
- They call for field studies of how incentive-structure changes affect norms (e.g., eliciting norms before/after a change, à la Burks & Krupka, 2012).
- In small firms/communities agents may already have precise norm information; how contract choices affect norms within *mutually observable subgroups* is open.
- Disentangling alternative mechanisms (guilt aversion, comparison effects) is argued away with the design but not separately structurally identified.

## Connections

The central mechanism extends [[@Sliwka2007|Sliwka (2007)]] on contracts signaling trust norms, and relates closely to Bénabou and Tirole (2012) on social esteem and expressive law, and to Friebel and Schnedler (2011) and van der Weele (2012) on complementarity-based norm information. The crowding-out motivation draws on [[@Gneezy2000|Gneezy and Rustichini (2000)]] and the survey by Bowles (2008), with related crowding effects in Fehr and Falk (2002), Fehr and Rockenbach (2003), and Falk and Kosfeld (2006). The guilt-aversion alternative invokes Battigalli and Dufwenberg (2007) and Ellingsen et al. (2010). The social-history results echo Berg, Dickhaut, and McCabe (1995) and norm-conformity findings in Krupka and Weber (2009). Galbiati, Schlag, and van der Weele (2013) study endogenous vs. exogenous sanctions in a coordination game. Other work on contracts and social norms not focused on signaling includes Hart and Moore (2008), Kessler and Leider (2012), and Bartling and Schmidt (2015).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
