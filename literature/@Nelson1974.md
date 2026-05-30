---
citekey: Nelson1974
title: Advertising as Information
authors: ["Nelson, Phillip"]
year: 1974
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/SAUSPWBS"
pdf: /Users/jesper/Zotero/storage/CGIPHWF4/Nelson1974.pdf
tags: [literature]
keywords: [advertising, information-economics, search-goods, experience-goods, signaling, consumer-behavior, industrial-organization]
topics: []
related: [Milgrom1986, Nelson1970]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Nelson argues that the major regularities of advertising behavior can be explained by treating advertising as information, once one distinguishes between *search qualities* (verifiable before purchase) and *experience qualities* (learnable only after purchase). For search goods advertising conveys direct ("hard") information; for experience goods its dominant informational content is simply the *fact that the brand advertises*, which consumers rationally read as a signal of higher utility-per-dollar because the most efficient (highest repeat-purchase) firms have the greatest incentive to advertise. From this single mechanism he derives, and tests against US data, predictions about advertising/sales ratios, media choice, page sizes, durables vs. nondurables, and the role of word-of-mouth. This is the founding statement of advertising as an indirect/signaling information device.

## Research question
How does advertising generate information for consumers, given that the seller controls the message and is interested only in selling more? More specifically: why do consumers rationally respond to seemingly content-free advertising, and how does the search/experience character of a good systematically shape the *amount*, *form*, and *media* of its advertising?

## Method / identification
The paper is theory-driven with auxiliary empirical tests. The core distinction (from [[@Nelson1970|Nelson 1970]]) is between search and experience qualities. For experience goods the consumer's optimal strategy is to sample a fixed number $r$ of brands and keep the best, biasing sampling toward the most-advertised brands.

Advertising revenue is modeled as $R = QPNG_1$ for search goods, where $N$ is potential customers, $Q$ average quantity, $P$ price, and $G_1$ the share of potential customers reached by one or more messages. Only $G_1$ varies with advertising intensity.

He models message accumulation as a continuous-time Markov ("forgetting") process: messages arrive at constant rate $c$, and the forgetting rate is proportional to the number of messages known, with generator matrix $F$ having off-diagonals built from arrival rate $c$ and forgetting rate $a$. Solving the steady state $AF = 0$ gives a Poisson distribution
$$A_i = \frac{d^i}{i!}e^{-d}, \quad d = c/a,$$
so the probability of holding one or more messages is $1 - A_0 = 1 - e^{-d}$.

For experience goods a consumer samples a brand only after receiving a critical number $m \ge 1$ of messages, so revenue uses $G_m$ (share with $m$ or more messages), $R = QPNG_m$. The marginal revenue of advertising is $\mathrm{MRA} = QPN\,\partial G_m/\partial c$, with
$$\frac{\partial G_m}{\partial c} = \frac{d^{m-1}}{a(m-1)!}e^{-d}.$$
He shows that over the declining (decision-relevant) portion, $\partial G_m/\partial c$ is larger for experience goods ($m>1$) than for search goods ($m=1$), so experience goods are advertised more heavily. An appendix adds a *consumer-memory* mechanism: advertising raises name recall, which differentially raises the conditional repeat-purchase probability $P(R\mid I)$ for high-utility brands, giving efficient firms the strongest incentive to advertise.

He also distinguishes mobility (entry/exit, independent of messages held) from forgetting (proportional to messages held), arguing — contra Stigler — that these are distinct processes; he solves the forgetting model and reports the mobility model gives the same results.

## Data
Several small descriptive/empirical tests, not a unified regression: (1) 1957 advertising/sales ratios by industry (drawing on Telser 1964), classified into search vs. experience goods under three alternative classification schemes; (2) page sizes of national-brand ads in the *New Yorker* for all of 1965; (3) ratio of network-television to magazine advertising by good, 1966; (4) ratio of local to national advertising by medium, 1966 (US Census). He explicitly notes the tests do not control for other variables and rely on simple difference-in-means or rank-correlation significance.

## Key findings
- Advertising/sales ratios are significantly higher for experience goods than search goods across all three classifications (means roughly $\bar X_e \approx .034$ vs. $\bar X_s \approx .013$; $t \approx 3.2$–$3.7$).
- The gap in average ad page size between experience and search goods rises monotonically with advertising volume (perfect rank correlation; small-volume advertisers have *smaller* experience-good pages, large-volume advertisers *larger*), consistent with large ads building reputability rather than conveying hard facts.
- Experience goods rely more on television than magazines relative to search goods (geometric-mean TV/magazine ratio 2.45 vs. 1.16; $t = 4.2$), since magazine/newspaper ads impose higher time cost and pay off only when marginal information value is high.
- Nondurable experience goods are advertised more than durable experience goods ($t \approx 1.9$–$2.0$), because word-of-mouth guidance substitutes for advertising more for infrequently purchased goods.
- *Deception is largely irrelevant to the main result*: consumers "deceived" into trusting endorsements are merely "deceived into doing what they should do anyway," so intelligent and naive consumers behave the same.

## Contribution
This is the canonical formalization of advertising as information and the origin of the search/experience distinction's application to advertising (building on [[@Nelson1970|Nelson 1970]]). It supplies the foundational *signaling* intuition — that advertising expenditure per se conveys information about unobservable quality — later formalized by Kihlstrom & Riordan and Milgrom & Roberts, and it reframes the then-dominant "persuasion"/market-power view of advertising (Galbraith, Bain) as informational and pro-competitive.

## Limitations & open questions
Nelson is unusually explicit about what he has *not* done, and these are direct project hooks:
- No general-equilibrium solution for total advertising expenditure; in particular, $m$ in equation (7) is left undetermined ("I have not solved for $m$").
- The combined mobility-and-forgetting stochastic model is "easy to construct" but he cannot solve its equations; only the polar models are solved.
- No explanation of a substantial share of the cross-industry variance in advertising/sales ratios; tests are simple and uncontrolled.
- Advertising's effect on the *utility function* itself (the change-in-taste/persuasion channel) is set aside because no testable theory of taste change exists.
- Advertising's effect on frequency of purchase of the good (vs. brand choice) — e.g. recipes — is not analyzed.
- Stability of the proposed equilibrium is defended only informally (heterogeneous tastes prevent full concentration on the best-advertised brand).

## Connections
Directly extends Nelson's own "Information and Consumer Behavior" ([[@Nelson1970|Nelson 1970]]), where the search/experience taxonomy and the optimal-sampling rule originate. The search-cost foundations come from Stigler (1961), whose treatment of advertising and forgetting/mobility Nelson critiques; related search modeling appears in Gould (1970). On the demand curve under optimal advertising he draws on Demsetz (1959) and Schmalensee (1972). Empirical inputs trace to Telser (1964), Ferguson (1963), Doyle (1968), and Sudman (1962). The paper is the conceptual ancestor of the advertising-as-quality-signaling literature later formalized by Kihlstrom & Riordan (1984) and [[@Milgrom1986|Milgrom & Roberts (1986)]], and it stands against the persuasion/market-power tradition associated with Galbraith and Bain. The experience-good credence/reputation theme also connects to later work on repeat-purchase reputation mechanisms (e.g. Klein & Leffler 1981).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
