---
citekey: Koszegi2006a
title: "Ego Utility, Overconfidence, and Task Choice"
authors: ["Köszegi, Botond"]
year: 2006
type: journalArticle
doi: 10.1162/JEEA.2006.4.4.673
zotero: "zotero://select/library/items/4MIJK5UE"
pdf: /Users/jesper/Zotero/storage/9ISMHWIU/Koszegi2006a.pdf
tags: [literature]
keywords: [ego-utility, overconfidence, beliefs-based-utility, information-acquisition, self-image, task-choice, bayesian-updating]
topics: []
related: [Caplin2001]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper models behavior when a decision maker cares about and manages her self-image. In addition to having preferences over material outcomes, the agent derives "ego utility" from positive views about her ability to do well in a skill-sensitive, "ambitious," task. Although she uses Bayes' rule to update beliefs, she tends to become overconfident regarding which task is appropriate for her. If tasks are equally informative about ability, her task choice is also overconfident. If the ambitious task is more informative about ability, she might initially display underconfidence in behavior, and, if she is disappointed by her performance, later become too ambitious. People with ego utility prefer to acquire free information in smaller pieces. Applications to employee motivation and other economic settings are discussed.

## Summary

Köszegi builds a rational, fully Bayesian model in which an agent derives direct "ego utility" from believing she is good enough for a more ambitious, skill-sensitive activity. Even though beliefs about the underlying ability are unbiased, the endogenous, ego-driven choice of when to stop acquiring free information makes the agent systematically overconfident about which task is appropriate for her. Depending on the informational structure of tasks, this overconfidence in beliefs can produce overconfidence in actions, or it can coexist with timid behavior (self-image protection / "rational hypocrisy") followed by excessively ambitious behavior after disappointment (self-image enhancement). The framework unifies a range of otherwise disparate behavioral patterns within a single discipline of Bayesian updating.

## Research question

How does a decision maker's concern for her self-image — modeled as utility derived directly from positive beliefs about her own ability — distort her instrumental information acquisition and task choice, even when she updates her beliefs about ability in a fully Bayesian, unbiased way? Specifically, when and why does ego utility generate overconfidence, timid underparticipation, and later overambition?

## Method / identification

The paper is a theoretical model with no data. The agent enters with ability $q\sim N(\mu_a,\sigma^2)$, which is also her (correct) prior. There are three periods: an initial learning period 0 and two financial choice periods. In period 0 she can sequentially and freely draw an arbitrary (possibly infinite) number of signals $s_0^j=q+\varepsilon_0^j$, $\varepsilon_0^j\sim N(0,\sigma_s^2)$, and may stop at any time. In each period $t\in\{1,2\}$ she picks $a_t\in\{0,1\}$: the unambitious option 0 pays 0 for certain; the ambitious option 1 pays $x_t=1$ if $s_t=q+\varepsilon_t>0$ and $-1$ otherwise, so success probability rises in $q$.

Following Caplin and Leahy's (2001) beliefs-based utility, the agent is an expected-utility maximizer over an enriched payoff space. Her von Neumann–Morgenstern utility is
$$wu(F_1)+x_1(s_1,a_1)+wu(F_2)+x_2(s_2,a_2),$$
where $F_t$ is the CDF of her beliefs about $q$ and $w$ scales the weight on ego utility. The key structural assumption is a step-function ego utility tightly linked to the decision: $u(F_t)=1$ if $\mu_{F_t}>0$ (she believes the ambitious option is financially superior) and $0$ otherwise. Belief formation is restricted to Bayes' rule, imposing methodological discipline.

Three informational regimes are studied: Assumption A ($s_t$ never observed), Assumption B ($s_t$ always observed), and Assumption C ($s_t$ observed only if $a_t=1$ — i.e., the agent must try the ambitious task to learn). Period-0 information acquisition is a dynamic stopping problem solved via a Bellman equation $V(F_0^j)=\max\{U(F_0^j),\,\mathbb{E}_{F_0^j}[V(F_0^{j+1}(F_0^j,s_0^{j+1}))]\}$; periods 1 and 2 are solved by backward induction. Robustness (Section 3.6, Proposition 7) generalizes to a real-line action space under Assumption 2, requiring only the tight link $u(F)=a^*(F)$ rather than the step form.

## Data

None — this is a pure theory paper. The author marshals psychological evidence (on self-enhancement, memory, and selective information processing) and stylized economic examples (stock-market participation and trading, small business entry, employee motivation, career/educational choice), but estimates nothing.

## Key findings

- **Proposition 1**: An optimal continuation strategy exists in period 0 under Assumption 1 and any of A, B, C.
- **Propositions 2–3 (Overconfidence in beliefs)**: An agent with non-positive mean beliefs always keeps sampling (no tradeoff: information raises both ego and instrumental utility), but with positive mean beliefs she stops with positive probability — she perfectly learns $q$ with probability strictly less than one. Because she stops asymmetrically (stops when she likes her beliefs), more agents end up believing the ambitious option is appropriate than the true ability distribution warrants. Beliefs about $q$ stay unbiased, yet beliefs about the *appropriate action* are biased upward. The stopping rule itself does not bias updated beliefs about $q$ (footnote 7).
- **Overconfidence in actions (Assumptions A/B)**: When tasks are equally informative, the agent cannot manipulate beliefs through choice, so belief overconfidence translates directly into action overconfidence.
- **Proposition 4 + Proposition 5 (Self-image protection / "rational hypocrisy", Assumption C)**: When she must try the ambitious task to learn, an agent with good-but-uncertain beliefs may avoid it to protect her ego, producing a cutoff rule $\mu_{F_0^j}>\mu_1^j\ge 0$. Beliefs and actions decouple: people advertise ability but shy away when challenged. As $w\to\infty$, participation in the ambitious task approaches zero. Expected ego utility and average overconfidence increase in $w$.
- **Proposition 6 (Self-image enhancement, period 2, Assumption C)**: With uncertain negative beliefs, the agent may choose the ambitious task despite expected financial loss, gambling for a good outcome to restore ego utility (cutoff: $\mu_{F_1}>\mu_2$ or $-\mu_2<\mu_{F_1}\le 0$). Protection can occur in either period; enhancement only in period 2.
- **Comparative statics on stakes**: Higher monetary stakes (lower effective $w$) reduce ambitious participation under symmetric observation (A/B) but tend to increase it under C. Without ego utility, participation is stakes-independent.
- **Smaller pieces**: Holding total informativeness fixed, the ego-utility agent strictly prefers to receive free information in smaller pieces (convexity/concavity of ego utility over beliefs, via Jensen's inequality).
- **Proposition 7 (Robustness)**: Under a general real-line action space, overconfidence in beliefs, its translation into action overconfidence, and the protection-then-possible-enhancement time pattern survive for virtually any ego-utility function, provided $u(F)=a^*(F)$.

## Contribution

The paper provides the first unified, disciplined rational model in which ego utility — beliefs-based utility tied to task appropriateness — generates a coherent family of well-documented behavioral anomalies: overconfidence, timidity/underparticipation, hypocrisy between stated ability and revealed choice, and post-disappointment overambition. Crucially it shows these arise *without* abandoning Bayesian updating: the bias enters through endogenous, ego-motivated information stopping and task selection, not through motivated distortion of probabilistic beliefs about ability. It connects self-image management to concrete economic settings (stock-market under-participation with overtrading conditional on entry, small business entry, employee motivation) and yields testable comparative statics on stakes and on informational asymmetry of tasks.

## Limitations & open questions

- The step-function ego utility and the assumption of an arbitrary (possibly infinite) number of free period-0 signals make some predictions extreme; the author flags that with linear ego utility the agent would acquire all information and no distortion arises, so results hinge on convex-then-concave shape.
- The sharp prediction that self-image *enhancement* occurs only in period 2 relies on the unbounded period-0 learning assumption; the author conjectures the qualitative intuition survives but does not prove it generally.
- Modifications (Section 3.5): if free signals remain available in all periods, enhancement distortions vanish but protection persists under C; if learning is scarce, overconfidence can *grow* during the activity rather than diminish — the model does not fully characterize these intermediate cases.
- Completely solving the period-0 stopping problem is "extremely difficult" and explicitly not attempted; only the properties needed for the results are established.
- Whether the identified hypocrisy makes agents feel bad about themselves (a second-order self-image cost) is left outside the model (footnote 9).
- The framework is not taken to data; empirically distinguishing ego-utility mechanisms from alternative accounts of overconfidence is left open.

## Connections

The beliefs-based utility formulation builds directly on [[@Caplin2001|Caplin & Leahy (2001)]] on anticipatory feelings, and relates to Brunnermeier & Parker's (2005) optimal-expectations model and to Bénabou & Tirole's (2002) self-confidence and personal motivation, which share motivated-beliefs themes but differ in mechanism (Köszegi keeps strict Bayesian updating). The self-enhancement/self-protection psychology draws on Baumeister (1998), Greenwald (1980), and Murray & Holmes (1994). The stock-market application connects to Barber & Odean's work on overconfident trading; the indispensability example comes from Brandenburger & Nalebuff (1997). The unified treatment of overconfidence complements behavioral-economics surveys and later motivated-cognition work, and the employee-motivation application speaks to intrinsic/extrinsic motivation literatures. The dynamic information-stopping structure relates to rational inattention and sequential-sampling models of endogenous information acquisition.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
