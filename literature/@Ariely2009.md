---
citekey: Ariely2009
title: Doing Good or Doing Well? Image Motivation and Monetary Incentives in Behaving Prosocially
authors: ["Ariely, Dan", "Bracha, Anat", "Meier, Stephan"]
year: 2009
type: journalArticle
doi: 10.1257/aer.99.1.544
zotero: "zotero://select/library/items/EJLU9BZH"
pdf: /Users/jesper/Zotero/storage/8Z6XLQI9/Ariely2009.pdf
tags: [literature]
keywords: [prosocial-behavior, image-motivation, crowding-out, monetary-incentives, signaling, field-experiment, charitable-giving, behavioral-economics]
topics: ["[[prosocial-behavior-image-signaling]]"]
related: [Benabou2006, Gneezy2000]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> This paper experimentally examines image motivation--the desire to be liked and well regarded by others--as a driver in prosocial behavior (doing good), and asks whether extrinsic monetary incentives (doing well) have a detrimental effect on prosocial behavior due to crowding out of image motivation. Using the unique property of image motivation--its dependency on visibility--we show that image is indeed an important part of the motivation to behave prosocially, and that extrinsic incentives crowd out image motivation. Therefore, monetary incentives are more likely to be counterproductive for public prosocial activities than for private ones. (JEL D64, L31, Z13)

## Summary
Ariely, Bracha, and Meier provide direct experimental evidence that *image motivation*—the desire to be seen by others as a good person—drives prosocial behavior, and that monetary rewards can backfire precisely because they *dilute the signaling value* of the prosocial act. Their key empirical lever is the observation, formalized in Bénabou and [[@Benabou2006|Tirole (2006)]], that image concerns operate only when behavior is *visible*. A 2×2×2 lab experiment ("Click for Charity") plus a field study ("Bike for Charity") show the signature interaction: monetary incentives raise effort when giving is private but have no (or slightly negative) effect when giving is public. Because incentives only matter where image is absent, they conclude that money crowds out image motivation, making extrinsic rewards counterproductive for highly visible prosocial activities (e.g., hybrid cars, public blood drives) relative to invisible ones.

## Research question
Is image motivation a genuine driver of prosocial behavior, and—if so—do extrinsic monetary incentives *crowd out* that image motivation, thereby becoming less effective (or counterproductive) the more publicly visible the prosocial act is? The deeper question is mechanistic: *why* do monetary incentives sometimes reduce prosocial effort, as in Titmuss (1970) on blood donation? The paper proposes signal dilution via image as the channel, distinct from prior explanations (intrinsic-motivation crowding, trust destruction, social-vs-monetary framing).

## Method / identification
The theoretical scaffold is the Bénabou–[[@Benabou2006|Tirole (2006)]] model. An agent choosing prosocial effort $a$ has utility
$$U(a) = (v_a + y v_y)\,a + R(a,y) - C(a),$$
where $v_a$ is intrinsic value, $y$ is the extrinsic/monetary reward (valued at $v_y$), $C(a)=\tfrac{k}{2}a^2$ is convex cost, and $R(a,y)$ is image (reputational) utility. Image is
$$R(a,y) = x\big[\gamma_a\,E(v_a\mid a,y) - \gamma_y\,E(v_y\mid a,y)\big],$$
where $x$ is the *visibility* of the action, $\gamma_a$ the concern for being seen as altruistic, and $\gamma_y$ the concern for not being seen as greedy. With $(v_a,v_y)$ jointly normal, the optimal individual supply (Proposition 1, BT) is
$$a^* = \frac{v_a + v_y y}{k} + \bar\mu_a\,\rho(y) - \bar\mu_y\,\chi(y),$$
with $\rho(y) = \frac{\sigma_a^2 + y\sigma_{ay}}{\sigma_a^2 + 2y\sigma_{ay} + y^2\sigma_y^2}$ and $y\chi(y) = 1-\rho(y)$. Aggregate supply is $\bar a = \frac{\bar v_a + \bar v_y y}{k} + x\,r(y)$, where $x\,r(y)$ is the (constant, $a$-independent) image term and $r(y)=\gamma_a\rho(y)-\gamma_y\chi(y)$.

Two falsifiable hypotheses follow. (i) **Image-Motivation Hypothesis** (Prop. 2): $\partial a/\partial x > 0 \iff r(y)>0$, i.e., raising visibility raises effort for a positively-perceived ("good") cause and lowers it for a "bad" cause. (ii) **Effectiveness Hypothesis** (Prop. 3): if $r(y)>0$ then $\partial a'(y)/\partial x < 0$—monetary rewards are *less* effective the more visible the act—which is equivalent to crowding out of image motivation, $r'(y)<0$. The Appendix proves Prop. 3 for $\sigma_{ay}=0$ and shows it survives small $\sigma_{ay}\neq 0$ (the condition reduces to a quadratic in $\sigma_{ay}$). A subtle point: even when $a'(y)>0$ (rewards still raise effort on net), the *visibility-dependent* attenuation alone implies crowding out of image, so the test does not require incentives to literally backfire.

**Lab design ("Click for Charity").** A real-effort task: subjects alternately press the X and Z keys for up to 5 minutes; each completed pair triggers a donation on a *decreasing* schedule (1 cent/pair for the first 200 pairs, 0.5 cents for the next 200, … down to 0.01 cents above 1,200 pairs). Between-subjects 2×2×2 design over 161 Princeton undergraduates, manipulating: (1) **cause**—American Red Cross vs. National Rifle Association, classified post hoc as "good"/"bad" by each subject's stated belief about whether the Princeton majority identifies with it (−5 to +5 scale); (2) **visibility**—private/anonymous vs. public (subjects announced their charity, earnings, and donation to the room); (3) **incentive**—a random subset additionally earned money for themselves on the same schedule, publicly known. A separate **"Limit" treatment** (26 subjects, high personal pay-for-clicks with bonuses up to \$20) pins down the physical ceiling on key-pressing to rule out a mechanical explanation. Identification of the crowding-out interaction comes from the *private-incentive × public* coefficient in an OLS regression of key-pairs on incentive, public, cause, and the interaction (robust SEs).

## Data
Primary data are author-generated experimental observations. Lab: 161 Princeton undergraduates (154 in the main analysis after dropping 7 with neutral charity perceptions) plus 26 in the Limit treatment. Field: 151 MIT gym-goers in "Bike for Charity." No external/observational dataset; the introduction cites Independent Sector (2001) US giving statistics (89% of households donate, averaging \$1,620/year) only as motivation.

## Key findings
1. **Image motivates giving (good cause).** With no personal incentive, public effort far exceeds private: ~822 vs. ~548 key-pairs ($p<0.05$), confirming the Image-Motivation Hypothesis.
2. **Money crowds out image (the central result).** Adding personal incentives raises private effort from 548 to 740 pairs ($p<0.05$) but produces an *insignificant decline* (822→702) in public. So incentives work only where image is absent. The interaction term (private-incentive × public) in Table 1 is large and negative, significant at 95% ($\approx -316$ key-pairs).
3. **Holds for a "bad" cause.** For the negatively-perceived charity, public/private effort do not differ without incentives (low, censored levels), but incentives again raise private effort sharply (204→559 pairs, $p<0.05$) while barely moving public effort—supporting the Effectiveness Hypothesis even when image is negative.
4. **Not a ceiling artifact.** Limit-treatment subjects averaged 1,290 pairs (nobody below 900) vs. 822 for the public good-cause condition where 50% pressed fewer than 900 pairs ($p<0.01$); public subjects had ample headroom, so the null incentive effect is not mechanical.
5. **Field replication.** "Bike for Charity" (miles cycled, \$1/mile) reproduces the pattern: incentives raise private effort ($+0.56$ miles, $p<0.01$) but not public; the public×incentive interaction is negative and significant at the 10% level despite self-selection biases that work *against* the hypothesis.

## Contribution
First clean experimental isolation of *signal dilution via image* as the mechanism behind incentive crowding-out, separating it from intrinsic-motivation crowding, trust effects, and framing. By exploiting visibility $x$ as the exogenous switch that turns image on/off, the paper turns the abstract Bénabou–Tirole model into a directly testable, falsifiable prediction and confirms it in lab and field. It thereby refines Titmuss: monetary incentives reduce prosocial behavior *conditional on the act being public*, yielding a concrete policy lever—use extrinsic incentives for invisible prosocial activities (water boilers, anonymous donations) and avoid making them salient for visible ones (hybrid cars, public donor lists).

## Limitations & open questions
- **Monetary vs. non-monetary incentives.** The authors flag this explicitly: do *non-monetary* extrinsic rewards (e.g., carpool-lane access for hybrids) dilute the signal as much as cash? "Solving this issue is left for future work."
- **Field design weaknesses.** Bike for Charity lacks a fully randomized compensation scheme and pre-announced random cause assignment, inviting selection (image-concerned people avoid private-incentive or ambiguous-cause conditions). The authors call for further field investigation of the extrinsic–image interaction.
- **External validity of the task.** Key-pressing/cycling are stylized; ability heterogeneity (a non-homogeneous cost $C(a,\theta)$) departs from the model's assumption, though the authors argue ability is not signaled and thus not part of $v_a$.
- **Self-image left constant.** The design treats self-image as a fixed constant across conditions (independent of $x$); how money interacts with *self*-signaling is untested.
- **Censoring for the bad cause.** Low effort levels raise censoring concerns the authors acknowledge.

## Connections
The theoretical backbone is Bénabou and [[@Benabou2006|Tirole (2006)]], "Incentives and Prosocial Behavior" (AER), with related image/signaling models by Janssen and Mendys-Kamphorst (2004) and Seabright (2004); the social-approval-in-utility tradition traces to Akerlof (1980), Ellingsen and Johannesson (2007), and Hollaender (1990). On crowding-out, the paper situates itself against Titmuss (1970) and the motivation-crowding literature of Frey and Oberholzer-Gee (1997), Frey and Jegen (2001), [[@Gneezy2000|Gneezy and Rustichini]] (2000a "A Fine Is a Price"; 2000b "Pay Enough or Don't Pay at All"), and Mellström and Johannesson (2005) on blood donation. Visibility-of-giving evidence comes from Andreoni and Petrie (2004), Rege and Telle (2004), Soetevent (2005), and Dana, Cain, and Dawes (2006). Signaling-of-status accounts of charity (Glazer and Konrad 1996; Harbaugh 1998a,b) and alternative crowding channels—trust destruction (Falk and Kosfeld 2006; Fehr and Falk 2002; Fehr and List 2004) and social-vs-monetary framing (Heyman and Ariely 2004)—are the rival mechanisms this paper distinguishes itself from. Survey context is provided by Fehr and Schmidt (2003) and Meier (2007).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
