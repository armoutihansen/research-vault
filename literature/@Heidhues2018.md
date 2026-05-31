---
citekey: Heidhues2018
title: Behavioral Industrial Organization✶
authors: ["Heidhues, Paul", "Kőszegi, Botond", "Bernheim, B. Douglas", "DellaVigna, Stefano", "Laibson, David"]
year: 2018
type: bookSection
doi: 10.1016/bs.hesbe.2018.07.006
zotero: "zotero://select/library/items/85ZSNV43"
pdf: /Users/jesper/Zotero/storage/V34X2UM5/Heidhues2018.pdf
tags: [literature]
keywords: [behavioral-industrial-organization, consumer-naivete, hidden-prices, price-discrimination, bounded-rationality, obfuscation, consumer-protection-policy]
topics: ["[[behavioral-io-naivete-attention]]"]
related: [Gabaix2006, Milgrom1981]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This chapter surveys the literature on behavioral industrial organization, covering four broad topics: (1) how rational firms interact with consumers who make systematic mistakes in evaluating products; (2) how rational firms respond to consumer preferences that differ from those usually assumed in industrial organization; (3) how psychological phenomena affect firms' behavior; and (4) what policy insights—especially on issues in competition and consumer-protection policy—follow from the literature on behavioral industrial organization.

## Summary
This Handbook of Behavioral Economics chapter is the field-defining survey of behavioral industrial organization (BIO): market interactions in which either consumers make systematic mistakes, consumers have non-classical preferences, or firms/managers are themselves behavioral. The authors organize a large and fast-growing theory literature around a single, reusable reduced-form "hidden prices" model and use it to derive when competition protects naive consumers, when it does not, how naivete redistributes welfare across consumers and toward firms, what efficiency distortions arise, and why soft-paternalist interventions and disclosure often fail in equilibrium. Note: at 96 pages this is a comprehensive survey; I read targeted — front matter and contents, the full introduction, and the core analytical sections (the bare-bones model, safety-in-markets, heterogeneous naivete, distortions, and naivete-based price discrimination), with lighter sampling of perception externalities, non-classical preferences, behavioral firms, and policy.

## Research question
What do we learn about market outcomes, welfare, and policy once we replace the classical IO assumption of rational, profit-relevant agents with psychologically well-founded models of (a) consumers who make systematic mistakes ("naive" consumers who ignore part of what they pay), (b) consumers with non-standard preferences (loss aversion, present bias, conspicuous consumption), and (c) firms/managers who are themselves boundedly rational? In particular: when does competition discipline the exploitation of consumer mistakes, and when does it fail or even worsen outcomes?

## Method / identification
The chapter is a theoretical survey built around a single unifying reduced-form model, generalizing [[@Gabaix2006|Gabaix & Laibson (2006)]] and following Heidhues & Kőszegi (2017). Two horizontally differentiated duopolists are located at the endpoints $l\in\{0,1\}$ of the unit interval; consumers are uniformly distributed at locations $y$ and buy at most one unit, incurring transportation cost $t\mid y-l\mid$, where $t>0$ indexes market power. Gross value is $v$, marginal cost $c$. Each firm sets an anticipated price $f_l$ and an additional price $a_l\in[0,a_{\max}]$. The defining assumption: naive consumers ignore $a_l$ when choosing but pay it upon purchase, so perceived utility is $v-f_l-t\mid y-l\mid$ while actual utility is $v-f_l-a_l-t\mid y-l\mid$. Firms understand consumer behavior correctly; the solution concept is symmetric pure-strategy Nash equilibrium. The outside option is available only at the interval endpoints (following Benabou & Tirole, 2016), so $t$ affects competition intensity without affecting purchase attractiveness, distinguishing "imperfectly competitive" from "monopolistic" regimes.

Heterogeneity is introduced by mixing a fraction $\alpha$ of naive and $1-\alpha$ of sophisticated consumers, with equilibrium prices $f(\alpha)=\min\{c+t-\alpha a_{\max},\,v\}$ and $a(\alpha)=a_{\max}$. Exploitation distortions are modeled via a convex "distortionary impact" $k(a_l)$ added to social cost, with three cases (sophisticated-side, naive-side, homogeneous). For the sophisticated-side case the firm solves
$$\max_{f_l,a_l}\ \alpha(f_l+a_l)+(1-\alpha)f_l-c\quad\text{s.t.}\quad v-f_l-k(a_l)=\hat u_l,$$
yielding the optimality condition $k'(a(\alpha))=\alpha$ and deadweight loss $\mathrm{DWL}(\alpha)=(1-\alpha)\,k(a(\alpha))$. The survey embeds dozens of more specialized models (screening, search/obfuscation, loss aversion, commitment, behavioral firms) within or alongside this scaffold, and discusses empirical structural estimation where it fits the conceptual organization.

## Data
None — this is a theoretical survey. It does, however, catalogue empirical and structural work that tests market-level implications, e.g. Ausubel (1991) on credit-card rates, Ellison & Ellison (2009) on add-on/obfuscation pricing at an online retailer, Seim et al. (2016) structurally estimating the Portuguese driving-school market, Gurun et al. (2016) and Ru & Schoar (2016) on targeted mortgage/credit-card offers, and Brown et al. (2012) on "cold-opening" movies.

## Key findings
- **Safety-in-markets benchmark.** If the good is socially valuable ($v>c$) and the market is at least imperfectly competitive, consumer equilibrium welfare is *unaffected* by naivete: competition forces firms to set $a_l=a_{\max}$ but hand the additional-price profits back through lower anticipated prices $f_l$. Under monopoly this fails — naivete lets the firm raise total price $f_l+a_l$ while keeping participation, lowering welfare to $-a_{\max}$ and strengthening the case for competition policy.
- **Cross-subsidy and adverse distribution.** With heterogeneous naivete, naive consumers cross-subsidize sophisticated ones (Gabaix & Laibson, 2006); since naive consumers are often poorer this is a "reverse Robin Hood" effect. Arbitrageurs / adverse-attraction effects (Ellison, 2005; Armstrong & Vickers, 2012) can create a price floor that shifts surplus from sophisticates to firms.
- **Participation and exploitation distortions.** Underestimation of total price acts like a subsidy, inducing inefficient participation (potentially huge — up to half the US credit-card market in Heidhues & Kőszegi, 2015). Exploitation distortions tilt business models toward revenue from hidden fees; the equilibrium additional price $a(\alpha)$ depends on $\alpha$ but *not* on competition $t$, unlike classical predictions.
- **Exploitative innovation.** With a binding price floor, firms have stronger incentives to innovate in *exploitative* (non-appropriable) contract features than in value-increasing improvements (Heidhues et al., 2016).
- **Naivete-based price discrimination.** Because ex-ante beliefs and ex-post behavior diverge for naive consumers, two novel motives arise: second-degree (screening on beliefs; Eliaz & Spiegler, 2006, 2008 — near-sophisticates pool with sophisticates and get efficient commitment contracts) and third-degree discrimination (Heidhues & Kőszegi, 2010).
- **Perception externalities and obfuscation.** Firms have weak incentives to educate and strong incentives to obfuscate; complexity/search-cost models (Carlin, 2009; Chioveanu & Zhou, 2013; Ellison & Wolitzky, 2012; Wilson, 2010) show more competition can *raise* obfuscation. Consumer ignorance is a source of oligopoly power (Scitovsky, 1950).
- **Policy.** Soft-paternalist interventions are often unavailable once equilibrium is accounted for, and disclosure/education may fail or backfire; heavier product/contract regulation and reconsideration of classical predation/collusion explanations may be warranted.

## Contribution
Provides the first comprehensive, conceptually unified treatment of behavioral industrial organization, establishing a common reduced-form "additional price" language that subsumes a sprawling literature and makes its core insights — safety-in-markets, cross-subsidies, participation/exploitation distortions, naivete-based discrimination, perception externalities, and the fragility of soft interventions — directly comparable. It defines the field's inclusion criteria (economically important market interactions; psychologically well-founded decision models) and sets a research agenda emphasizing that the theory is far ahead of the empirics.

## Limitations & open questions
The authors flag numerous explicit gaps, each a potential project hook:
- **Multidimensional heterogeneity** (naivete plus taste) is "relatively unexplored"; most models assume homogeneity in all else.
- **Strategic naivete.** All models assume consumers do not infer their own naivete from observed offers (e.g., do not grow suspicious of overly attractive deals); relaxing this is "useful" but unstudied.
- **Screening under competition** in Section 2-type models when sophisticated consumers can avoid the additional price is not analyzed under general type distributions (only via examples, e.g. Heidhues & Kőszegi, 2010).
- **Empirical/structural BIO is in its infancy** — the authors explicitly call for more empirical IO-style testing of market implications, expecting the theory-then-empirics pattern of classical IO to recur.
- **Identifying hidden prices from market data**, and disentangling behavioral from classical (predation/collusion) explanations, remains open.

## Connections
The unifying model generalizes [[@Gabaix2006|Gabaix & Laibson (2006)]] on shrouded add-on prices and builds directly on the duopoly framework of Heidhues & Kőszegi (2017), with the outside-option formulation from Benabou & Tirole (2016) and Hotelling (1929). Foundations for the additional price draw on Armstrong & Vickers (2012) (overdraft/add-on avoidance), Grubb (2009, 2015a,c) (overconfidence about demand variance), Spiegler (2006b) ("quacks" and law-of-small-numbers), Ellison (2005) (add-on pricing and adverse attraction), and DellaVigna & Malmendier (2004) and Ausubel (1991) (credit markets). Naivete-based screening originates with Eliaz & Spiegler (2006, 2008) and is developed in Heidhues & Kőszegi (2010). Obfuscation and search connect to Carlin (2009), Chioveanu & Zhou (2013), Ellison & Wolitzky (2012), Wilson (2010), Varian (1980), and Scitovsky (1950); disclosure to Grossman (1981) and [[@Milgrom1981|Milgrom (1981)]]. The non-classical-preferences strand links to Kőszegi-Rabin-style loss aversion and present-bias/temptation models of commitment. The piece appears in the same Handbook volume as the chapters by Bernheim, DellaVigna, and Laibson (the listed editors).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
