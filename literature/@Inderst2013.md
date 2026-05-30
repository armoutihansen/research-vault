---
citekey: Inderst2013
title: "Sales Talk, Cancellation Terms and the Role of Consumer Protection"
authors: ["Inderst, Roman", "Ottaviani, Marco"]
year: 2013
type: journalArticle
doi: 10.1093/restud/rdt005
zotero: "zotero://select/library/items/8EJ47BUA"
pdf: /Users/jesper/Zotero/storage/E5XDS4NZ/Inderst2013.pdf
tags: [literature]
keywords: [cheap-talk, return-policy, consumer-protection, credulity, commitment, sales-advice]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This article analyses contract cancellation and product return policies in markets in which sellers advise customers about the suitability of their offering. When customers are fully rational, it is optimal for sellers to offer the right to cancel or return on favourable terms. A generous return policy makes the seller's "cheap talk" at the point of sale credible. This observation provides a possible explanation for the excess refund puzzle and also has implications for the management of customer reviews. When customers are credulous, instead, sellers have an incentive to set unfavourable terms to exploit the inflated beliefs they induce in their customers. The imposition of a minimum statutory standard improves welfare and consumer surplus when customers are credulous. In contrast, competition policy reduces contractual inefficiencies with rational customers, but it is not effective with credulous customers.

## Summary
A monopolist seller commits up front to a price-refund contract, then privately observes a signal about how well the product suits a given customer and advises the customer via cheap talk. The paper's central insight is that a *generous* cancellation/return refund ($q>k$) is a commitment device: because the seller loses margin on every early cancellation, generous terms discipline the seller to recommend purchase only on favourable signals, restoring credibility to otherwise-uninformative sales talk. This rationalizes the "excess refund puzzle" (voluntarily generous return policies) and online retailers' incentives to host candid reviews. The logic flips when customers are *credulous* (take advice at face value): the seller then sets stingy refunds ($q<k$) to exploit inflated beliefs. The two consumer-rationality regimes call for opposite policies—competition policy helps rational customers but not credulous ones, while a statutory minimum refund helps credulous customers without harming rational ones.

## Research question
In markets where sellers advise customers about product suitability, when is sales talk credible, what cancellation/refund terms emerge in equilibrium, and which form of policy intervention—consumer protection (mandatory minimum refunds) versus competition policy—improves welfare and consumer surplus? The answer is shown to hinge on whether customers are rational or credulous.

## Method / identification
A four-stage game-theoretic model with cheap-talk advice. Timing: at $t=0$ the seller commits to a contract $\langle p,q\rangle$ (price $p$ paid on signing, refund $q$ on early cancellation); at $t=1$ the seller privately observes signal $s\in[\underline{s},\overline{s}]$ from distribution $H(s\mid u)$ satisfying MLRP, then sends a cheap-talk message; the customer decides whether to sign; at $t=2$ the customer learns utility $u$ (distributed $G$ on $[\underline{u},\overline{u}]$) and chooses to keep or cancel; at $t=3$ the kept contract yields $u$. The seller bears setup cost $c$ and continuation cost $k$. Posteriors $\psi(u\mid s)$ are ranked by FOSD; signals are perfectly informative at the boundaries ($H(\overline{s}\mid u)=1$, $H(\underline{s}\mid u)=0$).

The seller's profit on a signed contract is rewritten as
$$\pi(s;p,q)=p-(c+k)+\Psi(q\mid s)(k-q),$$
where $\Psi(q\mid s)$ is the probability of cancellation. This makes profit decreasing in $s$ when $q<k$ and increasing in $s$ when $q>k$, which is the engine of the whole analysis. Equilibrium selection picks the informative cheap-talk outcome (partition into purchase / no-purchase) over the babbling equilibrium, with the customer participation constraint $V=0$ binding so all purchase-types pool on one message. Two customer specifications are contrasted: **rational** (correctly anticipate the seller's strategy) versus **credulous** (believe any message at face value). The first-best benchmark uses cutoffs $s^{FB}$ (initiate) and $q=k$ (efficient cancellation). Robustness is checked against menus of contracts and a mechanism-design relaxation (Section 3.3).

## Data
None—this is a pure theory paper. Empirical motivation is drawn informally from the "excess refund puzzle," EU/US cooling-off and cancellation regulations, doorstep-selling reports (Office of Fair Trading 2004), and the management of online reviews (e.g. zappos.com), but no data is analysed or estimated.

## Key findings
- **Lemma 1 (Advice Equilibrium):** With rational customers, positive seller profit requires $q>k$; then a unique interior cutoff $s^*$ exists (purchase iff $s\ge s^*$). With $q\le k$ the seller earns zero profit and there is no trade unless $p=c+k,\,q=k$ (the first-best contract giving the seller zero profit).
- **Lemma 2 (Commitment Effect of Refund):** A higher refund $q\in(k,\overline{u})$ raises the equilibrium price and the cutoff $s^*$. The marginal seller (signal $s^*$) expects more cancellations than the average advised customer believes, so raising $q$ disciplines advice.
- **Proposition 1 (Equilibrium Inefficiency, rational):** Two inefficiencies coexist—(i) ex post over-cancellation ($q>k$) and (ii) ex ante over-signing ($s^*<s^{CB}(q)$). The seller never raises $q$ all the way to the conditionally efficient level. Comparative static: higher setup cost $c$ lowers the chosen $q$.
- **Proposition 2 (Menu robustness):** No non-degenerate menu can be sustained with rational customers, so restricting to a single contract is without loss of generality.
- **Proposition 3 (Exploitative Contract, credulous):** All credulous customers are advised to buy; advice becomes uninformative; true surplus $V_C<0$ and seller profit $\Pi=-V_C$. The seller acts like a monopsonist and sets the refund below efficient, $q<k$, solving $k-q=G(q)/g(q)$.
- **Proposition 4 (Menu, credulous):** With credulous customers a menu *is* feasible and strictly profitable; the optimal menu has the seller always claim the top signal but offer a refund schedule $q(s)$ (increasing in $s$) solving $k-q=\Psi(q\mid s)/\psi(q\mid s)$ pointwise.
- **Proposition 5 (Mandatory Minimum Refund):** A binding minimum refund $q\ge\underline{q}$ strictly raises both consumer and social surplus with credulous customers (surely for $\underline{q}\le k$), but strictly lowers social surplus and leaves consumer surplus unchanged with rational customers. Recommended floor: $\underline{q}=k$.
- **Proposition 6 (Competition Policy):** Raising customers' reservation value $V$ strictly increases both consumer and social surplus with rational customers, but with credulous customers only lowers the price one-for-one—refund and social surplus are unaffected.

## Contribution
The paper unifies cheap-talk advice (Crawford–Sobel) with optimal contract/return-policy design and consumer-protection regulation. Its novel mechanism—generous refunds as a *self-imposed commitment to honest advice*—offers a rational explanation for the excess refund puzzle and for why online retailers commit to generous returns and candid reviews. By embedding two behavioural types (rational vs. credulous) in one model, it delivers a sharp policy taxonomy: competition policy for sophisticated markets, minimum statutory refunds for markets populated by credulous buyers. A simple, robust policy recommendation emerges—mandate a refund at least equal to the salvage value / service-cost saving ($k$)—which never harms rational buyers and protects credulous ones.

## Limitations & open questions
The authors flag several explicit extensions (mostly in the Conclusion and footnotes):
- The baseline abstracts from heterogeneous usage intensities; non-linear pricing (free samples/base capacity for commitment, or quantity discounts to exploit credulity) is conjectured but not modelled.
- The contractual variable is the refund level; the dual variable—the *length* of the cancellation/trial period—is discussed only informally (rational buyers get efficient duration; credulous buyers get inefficiently short trials).
- Agency distortions between seller and sales agent are excluded; the authors conjecture an extension via Inderst–Ottaviani (2009) on incentive provision to a wealth-constrained agent.
- The model assumes either fully rational or fully credulous customers; mixed populations are not solved.
- Signalling timing (offering the contract only after observing $s$) is set aside because the model lacks single-crossing, leaving equilibrium-refinement questions open.
- Secondary/grey markets only partly constrain exploitation; their full interaction with refund policy is sketched, not characterized.

## Connections
The advice stage is a cheap-talk game in the tradition of Crawford & Sobel (1982); credulity follows Kartik, Ottaviani & Squintani (2007) and Ottaviani & Squintani (2006) on naive audiences and communication bias. The return-policy literature it builds on includes Che (1996) on customer return policies for experience goods, Davis–Gerstner–Hagerty (1995) on money-back guarantees, Courty & Li (2000) on sequential screening, and Matthews & Persico (2007) on information acquisition and refunds. The commitment-through-costly-terms logic connects to Grossman (1981) and Milgrom & Roberts (1986) on disclosure and reliance on interested parties, and to the authors' own program on misselling and advice (Inderst & Ottaviani 2009, 2012a, 2012b on commissions, kickbacks, and consumer financial protection). The online-review application engages Dellarocas (2006) on manipulation of opinion forums. Within Jesper's social-preferences/choice-modeling interests, the paper is a clean reference point for how behavioural biases (credulity) interact with market institutions and regulation, and how commitment devices substitute for trust.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
