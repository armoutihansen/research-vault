---
citekey: Koszegi2010
title: Utility from anticipation and personal equilibrium
authors: ["Kőszegi, Botond"]
year: 2010
type: journalArticle
doi: 10.1007/s00199-009-0465-x
zotero: "zotero://select/library/items/QBNBE4BB"
pdf: /Users/jesper/Zotero/storage/TIEF96L7/Koszegi2010.pdf
tags: [literature]
keywords: [personal-equilibrium, anticipatory-utility, reference-dependent-preferences, time-inconsistency, disappointment-aversion, informational-preferences, behavioral-economics]
topics: []
related: [Caplin2001, Eliaz2006, Koszegi2006b, Koszegi2009, Loewenstein1987]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> I develop a dynamic model of individual decisionmaking in which the agent derives utility from physical outcomes as well as from rational beliefs about physical outcomes (“anticipation”), and these two payoff components can interact. Beliefs and behavior are jointly determined in a personal equilibrium by the requirement that behavior given past beliefs must be consistent with those beliefs. I explore three phenomena made possible by utility from anticipation, and prove that if the decisionmaker’s behavior is distinguishable from a person’s who cares only about physical outcomes, she must exhibit at least one of these phenomena. First, the decisionmaker can be prone to self-fulfilling expectations. Second, she might be time-inconsistent even if her preferences in all periods are identical. Third, she might exhibit informational preferences, where these preferences are intimately connected to her attitudes toward disappointments. Applications of the framework to reference-dependent preferences, impulsive behaviors, and emotionally difficult choices are discussed.

## Summary
Kőszegi builds a two-period model in which a decisionmaker cares not only about physical outcomes but also about her period-1 *anticipation* (rational beliefs about future outcomes), and crucially allows anticipation to *interact* with physical payoffs. Because future preferences depend on today's beliefs while rational beliefs depend on future behavior, standard backward induction breaks down. He proposes **personal equilibrium** — beliefs and behavior jointly fixed by a self-consistency requirement — as the solution concept. The paper isolates three behaviors this generates that are impossible under expected utility: self-fulfilling (multiple, utility-ranked) expectations, endogenous time inconsistency under identical preferences, and disappointment-driven informational preferences. The central result is an *observational-equivalence* theorem: rule out all three and the agent is indistinguishable from a classical expected-utility maximizer. This paper is the methodological foundation of the expectations-as-reference-point program (Kőszegi–[[@Koszegi2006b|Rabin 2006]], 2007).

## Research question
How should one model an agent whose utility from anticipating the future *interacts* with utility from physical consumption, and what does adding this anticipatory component imply for *observable choice* relative to classical models (expected utility; Kreps–Porteus; Caplin–Leahy)? Specifically, when is such an agent behaviorally distinguishable from a classical decisionmaker, and what is the exhaustive list of new behaviors?

## Method / identification
A purely theoretical, axiomatic/decision-theoretic construction. The setup: two periods $t\in\{1,2\}$; physical outcomes $z_t\in Z_t$ (Polish spaces); an irreversible *anticipatory outcome* $f_1\in F_1\equiv\Delta(Z_2)$ realized in period 1 (after $z_1$ and the period-2 problem $d_2$, but before period-2 choice — see the timing in Fig. 1). Each self $t$ has a vNM utility $u_t$ over the enriched space $Z_1\times F_1\times Z_2$. The key innovation over Caplin–Leahy (CL) is that $u_t$ need *not* be additively separable between $f_1$ and the physical outcomes; imposing that separability recovers CL exactly.

The solution concept is **personal equilibrium**: a profile $(\sigma_1,\sigma_2,\phi)$ of strategies plus an *anticipation function* $\phi:Z_1\times D_2\to F_1$ such that (1, *Optimization*) each self maximizes expected utility, with self 1 solving $\sigma_1\in\arg\max_{\gamma\in d_1}E_\gamma\,E_{\phi(z_1,d_2)}u_1(z_1,\phi(z_1,d_2),\cdot)$ and self 2 maximizing $E_\gamma u_2(z_1,f_1,\cdot)$; and (2, *Internal Consistency*) $\phi(z_1,d_2)=\sigma_2(z_1,\phi(z_1,d_2),d_2)$ — beliefs equal the outcome distribution they induce. This is a single-player, multiple-self analog of subgame-perfection (and of Geanakoplos–Pearce–Stacchetti psychological equilibrium); it coincides with subgame-perfection when utility is anticipation-independent. Neither self chooses $\phi$.

To make the comparison classes precise, the paper formally defines what it means to "behave according to" EU, Kreps–Porteus (KP), and CL, and introduces behavioral restrictions that each shut down one phenomenon: **stability** (any two personal-equilibrium choices leave self 2 indifferent), **time consistency** (Definition 4: $E_{f_1'}u_2(z_1,f_1,\cdot)>E_{f_1}u_2(z_1,f_1,\cdot)\Rightarrow E_{f_1'}u_1(z_1,f_1',\cdot)>E_{f_1}u_1(z_1,f_1,\cdot)$, i.e. whenever self 2 wants to deviate, self 1 must have wanted the deviation), and **information neutrality**. Disappointment aversion is measured by
$$T_{z_1}(z_2,z_2')\equiv\big(u_1(z_1,\delta_{z_2},z_2)-u_1(z_1,\delta_{z_2},z_2')\big)-\big(u_1(z_1,\delta_{z_2'},z_2)-u_1(z_1,\delta_{z_2'},z_2')\big),$$
the excess of disutility-from-disappointment over utility-from-pleasant-surprise; $T_{z_1}\ge 0$ defines disappointment aversion, and a triangle-inequality form $T_{z_1}(z_2,z_2')=\sum_{k=1}^{K}\lvert v_k(z_1,z_2)-v_k(z_1,z_2')\rvert$ defines *regular* disappointment aversion.

## Data
None — this is a pure theory paper. Motivation draws informally on psychological and field evidence (emotional distress and impulse control; choice-overload/default effects in supermarket and retirement-savings studies of Iyengar–Lepper, Iyengar–Jiang, Madrian–Shea), but there is no estimation.

## Key findings
- **Theorem 1 (existence):** if every feasible $d_2$ is convex, a personal equilibrium exists (mixed strategies are needed in general). A *preferred* personal equilibrium also exists.
- **Self-fulfilling expectations (Sect. 3.1, Example 1):** anticipation–behavior feedback can yield multiple personal equilibria in which self 2 *strictly* prefers her chosen option in each — so the agent cannot simply pick the higher-utility equilibrium. This is impossible under EU/KP/CL, where chosen options must be indifferent. The expectations-based loss-aversion model of Kőszegi–[[@Koszegi2006b|Rabin (2006)]] is a leading instance.
- **Endogenous time inconsistency (Sect. 3.2, Examples 2–3):** even when $u_1=u_2$ (identical preferences over streams), the agent can fail to maximize that common utility, because self 2 does not internalize her effect on the *already-realized* period-1 anticipation. **Observation 1** shows time consistency suffices to make self 1's favorite option a personal equilibrium. A striking corollary is *context-dependence*: behavior over a single decision can depend on unchosen alternatives (Example 3).
- **Informational preferences ↔ disappointment aversion (Sect. 3.3, Theorem 2):** assuming $u_1$ linear in $f_1$ (neutralizing the classical source of informational preferences), (1) information neutrality $\iff$ disappointment neutrality; (2) *resolution loving* (prefers early full resolution) $\iff$ disappointment averse; (3) *regular* disappointment aversion $\Rightarrow$ information loving. Example 4 exhibits a disappointment-averse agent who prefers full resolution yet refuses *partial* information — non-monotone informational preferences that KP cannot represent.
- **Theorem 3 (observational equivalence to EU):** under non-satiation, if the agent is time consistent, information neutral, and stable, she behaves according to EU. Hence the three phenomena are an *exhaustive* list — any behavior distinguishable from EU must display at least one of them.
- **Theorem 4 (equivalence to KP):** under non-satiation, time consistency, and additive separability of $u_2$ in $f_1$, the agent behaves according to KP — so the only behavioral departures from KP concern anticipation–outcome interaction or time inconsistency. Theorems 3 and 4 are *tight*: dropping any assumption falsifies them.

## Contribution
Provides a general, application-ready framework and the **personal equilibrium** solution concept for decisionmaking with anticipatory utility that interacts with physical outcomes — the formal engine later used to "close" expectations-as-reference-point models (Kőszegi–Rabin 2006, 2007, 2009; Heidhues–Kőszegi pricing work). Its signature payoff is the surprising *reduction*: despite the apparent richness of anticipation-based preferences, all novel choice behavior collapses to exactly three identifiable phenomena, giving researchers a checklist (does a new model violate stability, time consistency, or information neutrality?) for understanding where its non-classical predictions come from. It also delivers a clean characterization linking informational preferences to disappointment management, distinct in spirit from the timing-of-resolution primitives of KP/CL.

## Limitations & open questions
- **No revealed-preference foundation (Sect. 6.2):** self 1's preferences over streams where outcomes diverge from expectations are *not* identified — under rationality, expectations must equal the outcome distribution, so e.g. $u_1(z_1,f_1,z_2)=z_2$ and $u_1=E[f_1]$ generate identical behavior. The author suggests eliciting preferences via a *representative* who chooses on the agent's behalf, creating an expectation/outcome wedge.
- The three phenomena are "quite broad"; the author flags that **much more work is needed for a detailed characterization** of multiplicity and time inconsistency sufficient to pin down behavioral consequences.
- Defining a notion of *purely anticipation-related* time inconsistency would be desirable, but "it is not clear what such a concept would mean," forcing reliance on a general time-consistency notion.
- The framework cannot capture information relevant only under a counterfactual past decision — e.g. **regret** (cf. Loomes–Sugden 1982) is outside the model.
- Rationality may be less natural here: agents deriving utility from anticipation might prefer *not* to hold rational beliefs (optimism/self-deception à la Brunnermeier–Parker, Bénabou–Tirole); a full model of motivated beliefs is left for future work.
- The three applications (reference dependence; emotions and self-regulation; intimidating/avoided decisions) are sketched, not fully developed — explicit invitations for follow-up modeling.

## Connections
The paper is the theoretical spine of **expectations-based reference-dependence**: Kőszegi & [[@Koszegi2006b|Rabin (2006]], 2007, 2009) adopt personal (and *preferred* personal) equilibrium to close their loss-aversion model, and Heidhues & Kőszegi (2005, 2008) apply it to firm pricing with loss-averse consumers. It directly extends **[[@Caplin2001|Caplin & Leahy (2001)]]** psychological expected utility by allowing anticipation–outcome interaction, and positions itself against **Kreps & Porteus (1978)** and the timing-of-resolution literature (Epstein–Zin 1989; Grant–Kajii–Polak 1998, 2000; Skiadas 1998). The solution concept generalizes **Geanakoplos, Pearce & Stacchetti (1989)** psychological equilibrium to a single-player/multiple-self setting and relates to **intergenerational-altruism** models (Hori–Kanaya, Bergstrom). On disappointment–information links it connects to **Dillenberger (2008)** and Kőszegi–[[@Koszegi2009|Rabin (2009)]]; on limits of informational preferences to **[[@Eliaz2006|Eliaz & Spiegler (2006)]]**. Antecedents on anticipatory emotions and time inconsistency include **[[@Loewenstein1987|Loewenstein (1987)]]**, and the broader self-control tradition (Strotz; Phelps–Pollak; Laibson) supplies the backdrop for the self-regulation application.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
