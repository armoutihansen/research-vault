---
citekey: Koszegi2022
title: Fragile self-esteem
authors: ["Koszegi, Botond", "Loewenstein, George", "Murooka, Takeshi"]
year: 2022
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/MMQPBPEL"
pdf: /Users/jesper/Zotero/storage/4GVL9349/KHoszegi2022.pdf
tags: [literature]
keywords: [self-esteem, personal-equilibrium, mood-congruent-memory, overconfidence, impostor-syndrome, self-handicapping, behavioral-economics]
topics: []
related: [Bell1985, Benabou2006, Koszegi2006b, Koszegi2007, Koszegi2009, Loomes1986, Oster2013a]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We develop a model of fragile self-esteem—self-esteem that is vulnerable to objectively unjustified swings—and study its implications for choices that depend on, or are aimed at enhancing or protecting, one's self-view. In our framework, a person's self-esteem is determined by sampling his memories of ego-relevant outcomes in a fashion that in turn depends on how he feels about himself, potentially creating multiple fragile "self-esteem personal equilibria." Self-esteem is especially likely to be fragile, as well as unrealistic in either the positive or the negative direction, if being successful is important to the agent. A person with a low self-view might exert less effort when success is more important. An individual with a high self-view, in contrast, might distort his choices to prevent a collapse in self-esteem, with the distortion being greater if his true ability is lower. We discuss the implications of our results for mental well-being, education, job search, workaholism, and aggression.

## Summary
The paper formalizes "fragile self-esteem"—a self-view that can swing dramatically without new information—by coupling the psychology of mood-congruent memory with the economic notion of personal equilibrium. Because how a person feels about himself shapes which memories he recalls, and those recalled memories in turn justify how he feels, the model admits multiple self-esteem personal equilibria (SEPs). The most consequential case is high-but-fragile self-esteem ("insecurity"), which can only go down. A signature result is that both the subjective self-view $\tilde{a}$ and the objectively correct ability $a$ jointly drive behaviour, so that among people with identical high self-esteem the lower-ability ones engage in the most ego-defensive distortion. The framework rationalizes workaholism, self-handicapping, choking, the impostor syndrome, and ego-driven aggression within one mechanism.

## Research question
Existing economic models of biased self-views assume a person acts at any moment on a single (probabilistic) belief, behaving identically to someone holding the same realistic belief. How can we instead model self-esteem that is *fragile*—simultaneously holding conflicting self-views, where mood can trigger a discontinuous collapse—and what behavioural patterns (overconfidence, impostor syndrome, self-handicapping, workaholism, aggression) does fragility explain that single-belief models cannot?

## Method / identification
Pure theory. The agent has an evidentiary base of past binary payoffs $\{s_1,\dots,s_n\}$ with $s_i\in\{0,k\}$; failure pays $0$, success pays $k>0$, and $k$ measures the *importance of success* (psychological ego-drive plus economic stakes). Realistic ability $a\in[0,1]$ is the proportion of successes. Recall is mood-congruent: in mood $m$ the agent recalls outcome $s_i$ with probability $g(s_i-m)/\sum_{i'} g(s_{i'}-m)$, where $g(\cdot)$ is positive, single-peaked and symmetric around zero. Average recalled memory is $E[s\mid m]$. A **self-esteem personal equilibrium (SEP)** (Definition 1) is a level of self-esteem $\tilde{a}$ that is a locally stable fixed point of $m=E[s\mid m]$; equivalently, since $m=k\tilde{a}$, a locally stable solution of $\tilde{a}=\mathrm{Prob}[\text{success}\mid\tilde{a}]$. Graphically, SEPs are points where the "mood-memory curve" crosses the 45-degree line from above. Definition 2 selects the SEP reached from a seed self-view $\tilde{a}_0$. **Fragility** (Definition 3) means there are multiple SEPs; **stability** is the smallest shock that shifts the agent to the other SEP. The agent is sophisticated—he anticipates SEP determination and knows the other SEP exists—but still forms his self-view as a naive average of mood-sampled memories. The framework builds on personal equilibrium from Kőszegi (2010) and Kőszegi & [[@Koszegi2006b|Rabin (2006)]]. Choice extensions add effort technologies and disappointment-aversion-style mood shocks $(1-p)r$ on success, $-pr$ on failure.

## Data
None—this is a theoretical paper. Section 2.1 surveys (but does not estimate from) the psychology evidence on mood-congruent memory and judgment (e.g. Bower 1981; Blaney 1986) that motivates the central assumption.

## Key findings
- **Existence/multiplicity (Fact 1, Prop. 1):** a SEP always exists; under convexity/decay conditions on $g$ there are at most two SEPs.
- **Importance and fragility (Prop. 2):** with homogeneous evidence ($a=0$ or $a=1$), or small $k$, self-esteem is not fragile; for interior $a$ and sufficiently large $k$ (under Assumption 1, $\lim_{x\to\infty} g(x)x=0$) self-esteem is necessarily fragile. Ego-driven, high-stakes domains breed fragility.
- **Realism (Prop. 3):** for large $k$ there is one unrealistically high ($\tilde{a}>a$) and one unrealistically low ($\tilde{a}<a$) SEP and no realistic one; as $k\to 0$ the SEP set approaches $\{a\}$, as $k\to\infty$ it approaches $\{0,1\}$. Higher ability makes the high SEP more realistic, the low SEP less so. Counter to classical intuition, stakes *reduce* belief accuracy.
- **Sufficiently unrealistic beliefs reveal fragility (Prop. 4):** $\tilde{a}-a\le -1/2$ implies a low fragile SEP; $\tilde{a}-a\ge 1/2$ implies a high fragile SEP. This unifies overconfidence (high SEP) and impostor syndrome (low SEP) in one model.
- **Shocks (Prop. 5):** higher ability stabilizes the high SEP and destabilizes the low SEP; the flimsier the evidence behind high self-esteem, the more fragile it is. Fragility can be more informative about true ability than the self-view itself.
- **Effort / choking (Prop. 6):** for small $k$ effort rises in $k$ (classical); for large $k$ in the *low* SEP effort can *fall* in $k$ and $\to 0$ as $k\to\infty$ (a novel choking mechanism), while in the *high* SEP effort rises in $k$ toward 1. The perverse incentive response is confined to low-self-esteem agents.
- **Ego-defensive effort (Prop. 7):** without fragility the agent exerts no mood-protecting effort; with fragility he exerts effort over a range of shocks, and this effort is *decreasing* in true ability—the opposite of signalling models.
- **Avoiding shocks / self-handicapping (Sec. 5.2):** a high-SEP agent prefers very high or very low success probabilities to intermediate ones and prefers right-skewed to left-skewed risk, rationalizing self-handicapping (trivially easy or impossibly hard tasks).

## Contribution
First economic theory in which a subjective self-view and an objective assessment *simultaneously* drive behaviour, so observably identical beliefs map to different actions depending on true ability. It imports mood-congruent memory into economics via an *endogenous* recall context (a two-way memory–self-esteem feedback), distinguishing it from exogenous-cue memory models (Mullainathan 2002; Bordalo et al. 2020). It unifies the previously separate literatures on unrealistically positive self-views (overconfidence) and unrealistically negative ones (impostor syndrome), and provides a formal account of psychological constructs—fragility, insecurity, narcissism, self-handicapping, workaholism—previously discussed only qualitatively. It also delivers a memory-based reinterpretation of well-being dynamics (temporary effect of positive recall, lasting effect of brief trauma, dependence on shock timing).

## Limitations & open questions
The authors explicitly flag several abstractions as open directions. (1) **Endogenous $k$:** they assume the importance of success is exogenous, yet people may (sub)consciously choose it—e.g. Claude Steele's "disidentification," lowering $k$ to protect self-esteem. (2) **Multidimensional self-esteem:** the scalar self-view ignores cross-domain externalities and the volatility-dampening role of "diversified" self-esteem (Linville 1985, 1987), though spillovers across domains can erode that benefit. (3) **Outcomes in degrees:** the binary success/failure framework cannot capture how more volatile experience histories heighten fragility (e.g. PTSD from a single severe episode versus many minor failures). (4) **Reference dependence:** they conjecture that making feelings sensitive to recent *changes* in self-esteem (à la Kőszegi & [[@Koszegi2009|Rabin 2009]]) would render even the low SEP vulnerable to temporary further collapse, making it especially hard to escape a low SEP. (5) Empirical testing is proposed (eliciting $\tilde{a}$ against a measure of $a$, or narcissism scales) but not carried out.

## Connections
The model rests on the personal-equilibrium apparatus of Kőszegi (2010) and Kőszegi & [[@Koszegi2006b|Rabin (2006)]], with multiplicity echoing Spiegler (2016). It belongs to the ego/anticipatory-utility tradition of Carrillo & Mariotti (2000), Bénabou & Tirole (2002, 2011), Gervais & Odean (2001), Prelec & Bodner (2003), and Kőszegi (2006), but its central memory mechanism is closest to and contrasted with Bénabou & Tirole's (2011) self-signalling model of moral identity. On biased recall it relates to Mullainathan (2002), Bernheim & Thomadsen (2005), Bodoh-Creed (2019), Enke et al. (2019), Bordalo et al. (2020, 2021), and Wachter & Kahana (2021), differing through endogenous context and utility consequences. The shock-avoidance analysis adopts disappointment aversion from [[@Bell1985|Bell (1985)]], [[@Loomes1986|Loomes & Sugden (1986)]], and Kőszegi & [[@Koszegi2007|Rabin (2007)]]. On misspecified learning lowering belief accuracy it compares with Heidhues, Kőszegi & Strack (2018) and Bushong & Gagnon-Bartsch (2021). Other related self-image and overconfidence work includes Bénabou & [[@Benabou2006|Tirole (2006)]], Kőszegi & Li (2008), Grossman & van der Weele (2017), Bodner & Prelec (1996), [[@Oster2013a|Oster, Shoulson & Dorsey (2013)]], and naivete models of O'Donoghue & Rabin (1999) and Eliaz & Spiegler (2006).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
