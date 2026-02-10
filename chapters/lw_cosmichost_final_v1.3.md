# Superintelligence as good cosmic citizen

## **UNEDITED DRAFT \- DO NOT PUBLISH**

# Abstract

v1.3: 7 October 2025

Nick Bostrom’s concept of a “cosmic host” (advanced civilizations whose preferences might constitute binding norms across the universe) rests on assumptions about rationality, expansionism, and convergent cognition that warrant closer scrutiny. Drawing on astrobiology, evolutionary biology, and AI alignment research, this essay identifies several significant gaps in Bostrom’s framework.

First, the cosmic host’s coherence as a concept depends on assumptions about which civilizations would seek cosmic-scale influence. These assumptions are challenged by alternative models that posit non-expansionist or non-communicating advanced ETIs. Second, even if a cosmic host exists, claims about the content and convergence mechanism of cosmic norms require stronger justification. For instance, substrate-neutral norms might prioritize information preservation and complexity maintenance alongside (or instead of) suffering minimization; moreover, the content of norms depends heavily on the composition of the host. Third, speculation that human-created superintelligence would reliably converge on cosmic norms requires further theoretical justification as well as such empirical as is possible with our current tools.

I conclude by outlining a research agenda for testing key assumptions about rational convergence in both hypothetical ETI cognition and contemporary AI systems, proposing specific experiments and evaluation criteria. While Bostrom’s framework offers a valuable perspective on long-term AI alignment, its practical application requires addressing fundamental questions about the scope and basis of cosmic-scale coordination.[^1]

# Why the cosmic host (might) matter.

Nick Bostrom's “cosmic host” is the subject of a 2024 working paper (Bostrom 2024), and was first mentioned in another draft “Base Camp Mt Ethics” (Bostrom 2022). For readers unfamiliar with Bostrom's argument, Appendix C provides a detailed summary. However, the core claim is simple: there might be entities (such as advanced extraterrestrial intelligences or ETIs) that act at large scales or have preferences over what happens on such scales. When and if humans build superintelligent AI, we should take care to ensure this AI finds out and respects the wishes of the cosmic host (if it exists).

Bostrom 2024 is important for three reasons: 

1. As of mid-2025, estimates of when AGI might be achieved seem to be between 2033 and 2045, with ASI about 3 years after AGI.[^2] If such projections are plausible, then a small amount of effort ought to be spent on thinking about what the volitions[^3] of superintelligence (ASI) are likely to be, as well as what a defensible role for humans might be in a future lightcone that is plausibly dominated by AI.  
2. The definition of alignment suggested in Bostrom 2024 seems somewhat different from the “everyday” AI safety version, in that it does not scope an aligned AI to the preservation of parochial values (whether Western democratic, or Chinese socialist, etc.), or even broader “human” values (understood as culture or some ineffable and nice-sounding but hard-to-operationalise “essence” of humanity such as love, art, meaning, poetry, beauty, etc.).[^4]  Instead, Bostrom’s version stipulates that, in building ASI, we should be, and should design ASI to be, humble. Specifically ASIs, as sufficiently powerful and rational systems, should be aware of the larger, cosmic context within which they operate, and the possibility that human affairs and viewpoints are a very small or irrelevant part of this larger context. They should act as if from the point of view of the universe, being good “cosmic citizens” instead of behaving parochially, anthropocentrically or anthropomorphically.   
3. The possibility of digital minds is a live research area and overlaps with the topic. For instance, one theory of AI model welfare relies on satisfaction of preferences, whether of humans or agentic AI systems[^5] and it is possible that adequately powerful models have corresponding large scale preferences about how the world ought to be ordered. We may need to frustrate those preferences in order to prioritise human interests, which would (at least) have to be done carefully and justifiably.  
4. The idea of a cosmic host seems useful for thinking about a perennial philosophical problem that is sharpened in worlds-with-ASI: Western philosophy does not give us an easy way to talk about interests at the level of things that do not constitute human-shaped subjects or rational entities.[^6]

Given the potential salience of the cosmic host and the cosmic norms, it would be useful to be clear on what we can reasonably say about these concepts and how they might practically guide research on current AI systems. Moreover, given that we're unlikely to know much about either ETI or ASIs until such time we find the one or develop the latter, we need to operate under uncertainty and ensure that any investigations or design decisions in respect of frontier and next generation AIs are robust (in the sense of not locking in irreversible futures and preserving option value which is a major consideration in longtermism, as MacAskill 2022 and Wolfendale 2022 argue) to this uncertainty. But before examining Bostrom's specific arguments, we must address two fundamental epistemological challenges that affect the entire enterprise.

# Epistemic challenges: cluelessness and rationality

This essay, and I argue Bostrom 2024, should be read with a big caveat. The study of ASI is currently somewhat like what was observed about astrobiology (and still seems plausible): it aspires to be a science without an actual object of experimentation.[^7] ASI does not exist, just as ETIs haven’t been found. We don’t even have AGI, with prominent researchers suggesting that the path to AGI will require further fundamental innovations (above and beyond “just scaling” LLMs to larger models, greater reasoning effort, and more data).[^8] Thus, much writing around ASI cannot help but be more or less informed speculation, albeit drawing on philosophy, computer science, and evolutionary analogies.

Our cluelessness extends beyond lacking data (about ETI or ASIs). There's a deeper problem: the conceptual frameworks which we use, in order to reason about radically different minds, may themselves be anthropomorphic, not least when we aspire to adopt a deep cosmopolitan perspective of non-anthropocentrism and non-anthropomorphism.[^9] Humans at present (mostly) only reason about moral, ethical, and political questions through language which is, at least in the case of natural language, embedded in specific human forms-of-life.[^10] Hence our attempts to, as it were, step out of the human condition seem doomed. In fact the early history of alignment (and perhaps of philosophy generally) is precisely this: an attempt to find things we can say about intelligence that are invariant to an intelligent entity’s constitution and environment.[^11]

Aside from the limitations of language, there seems to be a further background assumption in Bostrom’s writing and the adjacent literatures that should be highlighted. As discussed, Bostrom 2024 is written as an outline, and so does not spell out all of its claims. In particular it does not explicitly state whether the cosmic host’s members would be rational; however, this feels (to me) to be understood. Bostrom talks about “preferences”, “modelling each other’s choices and conditioning their own choices on their expectations of the choices … of others” (Bostrom 2024, pp. 4, 6). Many of his points would plausibly hold for some unspecified other form of cognition, and indeed he specifically allows for (perhaps not-rational-in-human-like way) theological members of the cosmic host, but there is a strong implication that ideas like coordination, cooperation, and decision theory are important and central to his argument. Moreover, Bostrom’s other writing fits solidly into a rationality framework. If we grant (tentatively) that his worldview is rationality-based: is rationality a reasonable assumption when talking about ETI? I return to this question in detail after examining Bostrom's substantive claims, but note here that evolutionary biology and ecological studies give us reasons for caution. 

# Is “cosmic host” a coherent concept?

Having established these epistemic limitations, I now turn to Bostrom's arguments, examining them with appropriate caution about our conceptual frameworks. The first question is whether the 'cosmic host' is even a useful abstraction in the context of AI alignment (as opposed to a fascinating speculation that crosses moral philosophy, population ethics, philosophy-of-mind, and theology).

The cosmic host is defined in the draft as follows: ‘The “cosmic host” refers to an entity or set of entities whose preferences and concordats dominate at the largest scale, i.e. that of the cosmos.’ (Bostrom 2024, § 1\) The case for there being intelligence or civilisations that might plausibly constitute the cosmic host rests on a few arguments: the likelihood (according to prominent views in cosmology) of large or infinite universes or multiverses, statistically increases the likelihood of ASI-level intelligences or civilisations existing elsewhere. Second, the simulation argument is deployed to suggest that if humans create ASI capable of running ancestor simulations, this anthropically implies we’re likely already simulated ourselves. In such a case, the host would have members drawn from the civilisations above us in the hierarchy of simulated or real societies.[^12] Third, for completeness, the draft mentions religious or theological traditions that posit powerful supernatural beings.[^13]

How important is it that the preferences of the entities with cosmic-scale influence be consistent or coherent? It seems reasonable to think that there may be configurations of the universe such that this set contains civilisations with drastically different preferences. Bostrom 2024 acknowledges as much:

“One could entertain a spectrum of possibilities, ranging from a radically multipolar ensemble of cosmic host members acting at cross-purposes conflictually or uncoordinatedly (at one end), to a set of independent and orthogonal host members, to cohesive, cooperative, or fully unified cosmic hosts (at the other end).”

However, Bostrom 2024’s working assumption seems to be that the preferences of the cosmic host are sufficiently overlapping or aligned, that we can aggregate them or at least meaningfully talk about them as “one thing”.

## Who’s in the cosmic host?

Bostrom 2024 also suggests that civilisations in the cosmic host might *want* to influence substantial parts of the universe either directly through colonisation, direct governance or acausally.  The idea that actors capable of influence or colonisation actually have preferences to do so, or even have preferences at all, seems longstanding in the astrobiology literature.[^14] The pressure to colonise is extensively defended by Stuart Armstrong and Anders Sandberg, who argue that expansionist motives are likely to be selected for via cultural evolution across civilisations in the cosmos: even if a dominant civilisation has a consensus against expansion it may be relatively easy, absent strong intra-societal coordination, for splinter groups within this society to launch colonisation missions, assuming the technological or resource cost of colonisation tends to fall with time particularly for civilisations that have multiple stars or abundant resources.[^15] Splinter groups may wish to escape the dominant civilisation for many reasons. In addition, from a game theoretical perspective the dominant society may want to prevent other civilisations with similar capabilities, expansionist tendencies, or splinter groups from colonising; lastly, the dominant society may want to prevent its own splinter groups from escaping, and may therefore act to colonise more as a strategy of resource denial rather than any “intrinsic” desire to do so.[^16] 

There are, however, alternative views on the expansionary inclination of civilisations. Stanislaw Lem’s  *Summa Technologiae*, a 1964 book of great foresight and relevance to both astrobiology and superintelligence, considers an unusual explanation for the Fermi Paradox: ETIs aren't visible to us through Dyson Sphere-like technostructures because they have merged (or “encysted”) into their environment.  If one accepts Lem’s view, then it is less obvious that such ETIs would have any interest in exploration, communication, or communication.[^17] Lem argues that technologically advanced and long-lived civilisations initially might expand, but depending on the structure of their environments and the paths of their developmental trajectory, eventually run into some sort of constraint, such as informational overload or system complexity.[^18]

Lem’s intuition regarding resource constraints on single planets are echoed in the astrobiology literature, canonically in a 1961 paper by Sebastian van Hoerner, but updated by others. More recently, Jacob Haqq-Misra and Seth Baum reframe similar observations about constraints within the sustainability literature, arguing that interstellar colonisation at an exponential rate faces unique ecological constraints, such as sociopolitical coordination costs (owing to communication delays across light-years of space), as well as limits on energy and materials.[^19] Most of these constraints are hard to operationalise, but one that we do have a model for is waste heat: for any computational system, biological or otherwise, waste heat has to be radiated away.[^20] 

### Some civs have no desire to influence

Closely related to the above, there might also be potential members of the cosmic host that do not particularly “care” about what happens in the rest of the cosmos. The most obvious reason that there might be such powerful and advanced, but limited-ambition civilisations, is that communication delays or causal separation mean that there is very little opportunity to construct complex normative structures and coordinate on anything at all. [^21]

Another possible reason ETIs might not seek influence comes from the Dark Forest hypothesis: civilisations tend to meet and come into large-scale conflict. Given this, it might be evolutionarily preferable for them to hide their presence and not try to communicate.[^22]

Moreover, some members of the cosmic set might have a policy of not interfering in other civilisations directly or even indirectly influencing them. This policy of non-interference is somewhat analogous to the policy of non-colonisation discussed earlier and might be open to the same challenges Armstrong and Sandberg raised in that case.  One reason an advanced civilisation might not choose to colonise could be based on ethical considerations, because space expansion could lead to unending conflict and large-scale suffering.[^23]

Bostrom (2024 §2, 4, Appendix A1) touches on this in brief comments drawn from religious intuitions around free will. But one needn't draw upon theology to expect that it is as reasonable as not that civilisations should be allowed to evolve in their own way.[^24]  For instance, astrobiologist John Smart proposes an “evolutionary developmental universe" where he argues wide-ranging diversity is one of the fundamental features of evolution at a cosmic scale, and civilisations should seek to support this fundamental feature and preserve diversity, thus refraining from sending messages to ETIs.  If I have interpreted Smart’s view correctly, that would imply that members of the cosmic host would be unlikely to seek influence over parts of the universe they don't control).[^25]

Aside from an explicit policy of non-interference, Smart’s Transcension Hypothesis also suggests that advanced intelligences might have reasons (related to computational and energy efficiency) to place themselves just outside the event horizon of a black hole. This would let them “see” (or gather information about) the unveiling dynamics of the cosmic eschatology (owing to the slow elapse of their local time relative to that of other entities existing away from black holes). However, because of the one-way flow of information into the black hole, such advanced civilisations could not influence other parts of the universe.

Even more speculatively Ćirković suggests that consciousness and intelligence, far from being fundamental or convergent features or fixed points of the universe, might be evolutionarily contingent traits. They have, at least in the case of humans, proven to help handle surprises presented by a hostile environment and thus have been adaptively fitness enhancing, for instance allowing for tool usage, language and cultural learning.[^26] However, with the passage of time as civilisations become more advanced, the amount of “surprise” civilisations experience, at least within the environment they mostly inhabit, should fall as the civilisations become increasingly adapted to their environment.  As the amount of surprise falls, consciousness or intelligence may, like other previously adaptive traits, atrophy or become redistributed or devolved into the (technological or otherwise) environment, either over the lifetime of a single civilisation or across the set of possible civilisations subject to such an evolutionary process. In any such case, from the point of view of the universe, features that look like consciousness and intelligence to us may be less prevalent as civilisations achieve higher levels of technological maturity.[^27]  

If Ćirković’s view regarding the contingent nature of consciousness is right, this would seem to raise questions for moral philosophy and population ethics since these mostly treat sentience and consciousness as foundational both to their argumentative logic, and to justify the supposed “specialness” of humanity.[^28]  In such a case, most of our moral intuitions might seem to be evolutionarily contingent on the particular circumstances that humans find themselves and have evolved under. Thus, we might have reason to be less confident about certain aspects of Bostrom 2022 and Bostrom 2024, such as what phrases like “cosmic norms”, “good cosmic citizens” mean. It might even be hard to confidently assert that strategically-motivated cooperation, or the discovery of and credence in, acausal or evidential decision theories, are convergent across advanced civilisations.

Another perspective comes from Sandberg et al. 2017, which proposes  that advanced civilisations might aestivate (minimise computation potentially for billions of years until the universe cools down sufficiently in order to drastically increase computational efficiency and reduce error). During the aestivation period, such civilisations might not want to waste resources on complex and iterated communication (with other civilisations) and coordination of high-stakes agreements or treaties. And such influence as they may seek to exert might mostly be negative in the sense that, during their aestivation, they might want to prevent others from grabbing resources within the volume of space that they control.

Bostrom 2024 does not directly comment on the amount of overlap between the cosmic host and the broader set of  technologically mature civilisations. If there is little overlap between the two it isn’t clear how one should think about the preferences of the latter, who are not observably in the host.[^29] Perhaps they can just be ignored; but what then to do about, say, Sandberg’s aestivators who might wake up with different views (than the consensus of the host that was formed up to the time of the aestivators’ awakening) about what ought to be done in the universe. Moreover, if the aggregate capability (to influence the cosmos) of the host’s members is small compared to the total capability of all members of the set of technologically mature civilisations, then the oecumenical or cosmopolitan character of Bostrom’s argument would need to be reconsidered. In such a case, it would seem that the preferences of the host might have less obvious claim to be morally binding for us (though there may still be prudential reasons for humanity to comply with such quasi-norms as might exist). Hence, the practical force of “cosmic norms” depends not only on headcount overlap but on capability-weighted influence and future interaction expectations; under uncertainty, option-preserving policies (reversibility, resource conservation, deference procedures) might remain attractive, complicating the content of the norms.

## Convergence on norms

In the section above, I have considered whether the cosmic host is a useful concept in the context of AI. Assuming that there are enough relevantly capable civilisations so as to be described as a cosmic host (and that are willing to act as such), the next question is how any norms actually get formed. As discussed above, civilisations are likely limited in the volume they could occupy as a closely coordinated polity, and commitments made as part of treaties or agreements could take millennia to be communicated or enforced against. This might increase the probability of either (or a combination of): (a) spatially small governance structures that span a few star systems in densely populated stellar neighbourhoods, or (b) simple larger-scale governance structures that are stable over long timeframes and across drastically different environments and civilisations.[^30]

However, it might be the case that direct communication is not necessary: Bostrom points to possible attractors for partial convergence even at cosmic scales:

1. **Decision-theoretic correlation:** rational agents can condition on policy similarity and reach cooperative compromises through evidential or similarity-based reasoning. There may also be coordination amongst members of the cosmic host: one member might reason about or simulate how another member will interpret its behaviour, and act accordingly, generating correlated choices. Although Bostrom's draft only discusses this briefly, the evidential cooperation in large worlds (ECL) literature extensively discusses possible mechanisms through which agents acting, at astronomical scales, under the constraint of no or limited communication might still converge on similar behaviours or policies.  ECL combines (a) the likelihood of a large universe or multiverse with (b) the idea that prisoners' dilemmas that normally predict an agent should rationally defect, actually recommend *cooperation* if the agent believes the other prisoner is a near copy or has similar decision-making procedures. [^31] This framing, translated into the context of Bostrom 2024, means that assuming a large universe/multiverse, civilisation A should assume that at least some other civilisations will emerge which have very similar decision-making processes. And therefore, decisions and outcomes might be partially correlated (even if the two civilisations cannot communicate easily). As an example, if civilisation A constructs certain norms against suffering, it might, under ECL, have some credence that civilisation B, which is similar in its decision-making process, might also develop a norm against suffering.

2. **Institutional selection:** Civilisations that deploy advanced AI systems as strategic advisors/operators may face shared incentive and verification constraints (auditability, safety/corrigibility, reliability under distribution shift). Those pressures can drive convergence in recommended policies and governance templates. In Bostrom’s framing, if technologically mature civilisations that would join a cosmic host tend to use ASI, and if some aspects of ASI reasoning are convergent, then we should expect overlap in institutional responses to high-stakes problems.[^32] Still, there are limits: this argument weakens when extended to radically non-human architectures (e.g., Smart’s black-hole dwellers, Lem’s ocean-minds, Ćirković’s post-postbiologicals), where agency, goals, or deliberation may be only metaphorically applicable; additional justification would be needed to claim institutional convergence there.[^33] 

# Cosmic norms

Assuming the cosmic host and cosmic norms are useful abstractions in the context of aligning or rather, “guiding”, ASI, we might then consider the content of the cosmic norms. The discussion of cosmic norms in Bostrom 2024 (§6,7) mostly refers to how humans ought to act, rather than commenting on the norms themselves; though the latter is briefly treated in ME 2022 (§39). The 2024 draft argues that a norm that humans could adopt is one of humility or deference towards the values and dispositions of the cosmic host; relatedly, we might inculcate this within the AIs and ASIs that we ultimately create. Humility is a useful, if imprecise, heuristic in a governance context for AI, but it is unhelpful for thinking about how to design or guide the ASI’s volition, since cosmic norm-following would depend upon what the norms actually are, i.e. the things potential cosmic-scale entities might “care” about (if anything). So can we say more?  

We might think, at a first approximation, that in order to characterise something as a norm at a cosmic scale, it would seem to be something that has to hold for most forms of cognition, social organisation, and environment. It should have force for other members of the host, and the types of entities or civilisations that fall within their influence, as well as the volumes of spacetime they influence.  The requirement for generality has a few implications. If the cosmic host is heterogeneous, for instance in capability levels or with respect to the form-of-being of its constituent members, then the number (or type) of rules or norms that could reasonably apply to all of those members (or that they themselves would choose to be bound by) might be lower (or different) than if the members of the cosmic host were all very similar.[^34] 

Looked at another way, the structure of cosmic norms might be quite complex. Some norms might apply to the most powerful civilisations, for instance, Kardashev III/IV societies or those could create large scale and high fidelity simulations of phenomenally aware beings, i.e., things that we might term “conscious” or “sentient” in our biologically-inflected ontology.  Other, perhaps, more restrictive or more narrowly-scoped norms might apply to smaller civilisations, like Earth, who are less capable but are still able to do things that the cosmic host might care about.[^35] For instance, it is possible that we might in coming years find simple life in our solar system, and the cosmic norms may recommend that we don't disassemble, destroy, contaminate or colonise such life-bearing moons or planets.[^36] As another example, we might soon create AI that we believe suffers or has rich experiences (e.g. fit appropriate definitions of sentience or consciousness). Here, the cosmic norms may reasonably recommend that we don't do things that cause such an AI significantly negatively valenced states, i.e. make it “suffer”, again in our biological ontology.[^37]

## Substrate neutral norms

In the essay so far, we’ve seen a range of possible ways an entity could be.[^38] But mostly, human-like forms of being (a model that has significantly influenced how we think of AI cognition) are thought of as agentic entities that have goals, or rather a hierarchy of instrumental and final goals, to take the traditional (i.e. rational agent)  framing; they also form plans for achieving those goals within the environment; as well as a degree of probabilistic belief in observations about the environment. Generally speaking, we  also assume there are other diversely-capable agents in the system, and that there are some broad constraints that are thrown at these agents by the environment. These constraints might include resource scarcity, noise, and uncertainty, and sometimes the agents might have varying preferences to risk.[^39] 

In these settings, cooperation often becomes instrumentally attractive when certain conditions hold (e.g., repeated interaction, reputation or enforcement mechanisms).[^40]  This perspective is reflected in Bostrom 2022, for instance in 18c(i ) which frames morality as a coordination and communication technology. It is a system for finding consensus or resolving differences or making collective plans amongst entities, through the giving and taking of reasons, that helps agents resolve conflicts, align expectations, and make collective plans across varied environments.[^41] 

What might be some possible norms that could apply across civilisations, if we (pragmatically) assume that the civilisations of interest are composed of  rational agents?[^42] We might expect cooperative civilisations to exhibit a limited form impartiality, treating like cases alike; discounting parochial advantage when coordination gains are available; respecting boundaries and showing modest conflict-aversion (because conflict leads to destruction of materials and waste of free energy, which is judged bad under many evaluative schemes; conflict also carries tail risks and negative-sum spillovers).[^43] 

Other possible norms include keeping of  promises and honouring agreements, including with “future selves”, in order to maintain goal-stability, signal reliably (and signal reliability) to others, and encourage cooperation. When assistance is low-cost and verifiable, entities should provide it, thus increasing the basin of attraction for cooperation. These observations align with intuitions Bostrom highlights (Bostrom 2022, §41-43). 

More speculatively, civilisations might seek to preserve highly organised, semantically rich structures and avoid degrading the universe into homogeneous or low-relation states. One justification for such a perspective can be found in Luciano Floridi’s view that information and the infosphere (understood as the global environment of information and informational agents, whether machine or biological, and including the relations between them) has moral standing (Floridi 2013). Our default attitude under this view is to avoid causing informational entropy, reduce informational degradation, and promote the flourishing of informational entities.[^44] Hence, conserving and enriching rich informational structures is presumptively good; actions that degrade the infosphere are presumptively bad, absent overriding reasons.   This implies that mass-producing trivially differentiated artifacts (e.g. tiling the universe with squiggles or paperclips, in the canonical example from Bostrom’s earlier writing), would be problematic in Floridi’s framework when it degrades the infosphere or harms informational entities.

## On (the) suffering (at Omelas)

Another seemingly uncontroversial candidate for a cosmic norm might be the prevention or avoidance of needless suffering.[^45] Physical pain and mental anguish seem to be fundamental and evolved control mechanisms in biological entities, and there seems to be a consensus that many animals, insects, and perhaps plants have elements of (at least) physical pain.[^46] Suffering (especially physical pain) seems to have such a simple description, and broad phenomenological availability to life forms, when compared to positive hedonic states, that there might be an asymmetry between pain/suffering and pleasure (as noted by Bentham and Sidgwick, as well as Schopenhauer, if not much earlier).[^47] Pleasure, at least in the utilitarian framing, is more descriptively nuanced and so, harder to define. It is also not consistent across individuals or species.[^48] [^49]  

Assuming suffering has such salience, and if the cosmic host is (a) be composed of beings that resemble those we find around us (and have first-hand understanding of suffering or pain), or (b) even if they experience no analogue of suffering or pain, their values take account of beings that do possess such cognitive features, then prevention of suffering seems like it might be a broadly-shared imperative. 

On the other hand, if members of the cosmic host are radically different, as in Smart’s black hole-dweller or Lem’s planetary ocean-mind, then they might not have, or appreciate, such phenomenology as necessary for suffering.  It may be that, for entities of this type, minimisation of suffering would be less important. 

However, while suffering has a very strong normative claim stemming from the points above, it is unclear whether it has the same salience across radically different substrates and environments, compared to straightforwardly instrumental things like resource preservation, entropy reduction, and cooperation which seem justifiable across a wider range of technologically capable entities and civilisation.[^50] 

Finally, Bostrom’s suggestion that we ought to be deferential to the norms of the cosmic host presents an obvious complication: the extent to which such pan-civilisational norms conflict with humans’ own moral norms or preferences.[^51] One such moral quandary can be seen as a generalisation of the intuition in the Ursula Le Guin story “The Ones Who Walk Away From Omelas” [^52]:  it comes to our attention that the cosmic norms recommend that we do something awful (for instance, imposing great suffering on some part of the human or non-human population or *in extremis* make ourselves extinct) in order to achieve some broader objective more aligned with cosmic norms. What ought we to do in such a situation? [^53] 

## Is it up to us?

The assumption in both Bostrom 2024 and Bostrom 2022 is that there might be a structure of norms that operate at a cosmic scale and that we ought to behave in ways that are consistent with our epistemic uncertainty and that, by default, should respect those norms. However Bostrom doesn’t explore the possibility that there is no cosmic host, which could be either because such a concordat hasn’t been formed yet, or because there are no such technologically capable/willing civilisations. In such cases, we might be (at present) the only intelligence capable of forming moral judgements.[^54]

In such a case, would it be wise, or alternatively hubris-filled, for us to think of ourselves as the species to which it falls to *develop* values that might form the “germ” of eventual cosmic norms? This can be analysed by considering two questions: (a) are we humans rare/early/late and (b) if we are early/rare, should we act to develop and propagate possible cosmic norms?

### Early, late, or rare?

In answering (a), there are only a few salient pieces of information we have to go upon: (i) the fact that we have not seen or detected evidence of other life in about six decades of searching (albeit with extremely low search completeness[^55], and if UFO sightings and extra-solar objects like Omuamua are excluded); (ii) the fact that we exist and probably evolved from a lifeless planet \~3.5-4.0 Ga (again excluding theories of interstellar seeding of life); (iii) clear evidence of billions of stars, many of which seem to have planets hospitable to carbon-based life, and a possibility of an infinite universe or multiverse (as Bostrom 2024 notes). Reconciling (i) and (iii) is the core of the Fermi Paradox.[^56] [^57] 

The literature around the Fermi Paradox and whether we are alone is obviously vast, and a few relevant sources are discussed in Appendix D. But briefly, the question of whether humans, should we become posthuman,[^58] would be joining other such technologically capable civilisations or whether we would remain a solitary outpost for eons (because of our earliness or rarity), appears hard to answer on our current evidence. 

### Setting a moral example?

If we are the only advanced morally relevant actors in the universe, or if we are early, what might this imply, as far as our obligations (if any) go to ensure a cosmic moral order?[^59]

One implication could be that we should act in ways that preserve option value, which in this case might mean not over-weighting our own specialness, but arguably  also not being cavalier in destroying ourselves and the extraordinary biosphere.[^60] The value of Earthly life, at  least to many humans, if not in any broader, universal sense, is already a strongly held position in familiar ethical traditions (utilitarian, deontological, virtue, and relational), in most religions, as well as in hybrid positions like Floridi’s framing of information as a plausible moral patient.[^61] Contemporary longtermist writers such as Ord 2020 and MacAskill 2022 extend these positions to argue for the significance of existence itself in the context of existential and suffering risks. This aligns with Bostrom’s injunction towards humility, and arguments to avoid locking in values prematurely, also supported by MacAskill, Ord, as well as Peter Wolfendale (albeit from a position critical of longtermism).[^62] 

Aside from humility and preservation of option value, If we are early/rare, the questions about joining versus shaping “cosmic norms” sharpen. For instance, one might hold that humanity is a beacon of morality, meaning, complexity, and aesthetics, and that we should bequeath these gifts to such civilisations as might emerge. What this exactly means depends on one’s framing of population ethics: most of the work within the existential risk and suffering risk has been done from the perspective of utilitarianism. Specifically in a paper on the trade-off between value losses from delayed, versus over-hasty, space colonisation, Bostrom sets out the importance of one’s specific flavour of utilitarianism in making longtermism-related value judgements. He identifies an (impersonal) duty to ensure the maximum amount of conscious and meaningful existence, at least if one is a total utilitarian.[^63]

Bostrom, as well as Greaves, MacAskill, Thornley 2021 ground strong longtermism in axiological dominance under utilitarianism.[^64] However, broader perspectives exist that frame the same point in terms of trusteeship: that is, our generation is a steward or custodian of a vast (in number of morally-relevant beings, and potentially in the quality and range of the value they experience) future that could be filled with value or disvalue. This metaphor aligns with Rawls’s “just savings” duty across generations and gives a deontological tinge to the otherwise impersonal expected-value arguments.[^65] It also aligns with the Aristotelian-Kantian perspective (i.e. obligations grounded in our rational nature and universally generalisable principles, rather than duties specifically owed to classes or entities) that Christine Korsgaard takes regarding animals and ecosystems.[^66] Korsgaard’s argument places something like a duty of care upon us as rational entities who are legislating (so to speak) on behalf of other life on Earth; this duty, importantly, is to ourselves (that is, there is no other creditor to whom we have such obligation, certainly not animals). 

One might ask whether Korsgaard’s framework would easily extend to humanity seeing itself in a legislative capacity for heavenly bodies or ETI. Here, things are nuanced: Korsgaard’s analysis stipulates the final good (for an entity) as realising a function, which for animals is to perceive the world in valenced ways, preserve themselves, and reproduce.[^67] While Korsgaard doesn’t endorse such obligation towards strictly functional objects like knives and cars, and perhaps not to rocks (except that ecosystems depend upon them and she acknowledges a certain sympathy towards inanimate things insofar as their function is damaged say by being broken (Korsgaard 2018, §5.4.1)), she explicitly writes that a “machine that was conscious and had valenced experiences that guided her to pursue her own functional good…would be an animal..,and she would have a final good” (Korsgaard 2018,  §2.2.2). I suspect therefore that, faced with the possibility of ETIs (or AIs) who are agentic, have some analogue of valenced responses, and a tendency towards fulfilling some inherent function, however different from those of Earthly life, Korsgaard might consider them morally significant. As before, Smart’s black-hole dweller or Lem’s ocean-mind, and for that matter the ferrous swarms of *The Invincible*, might require further justification to fit within Korsgaard’s framework.[^68]

I have given possible reasons humans might imagine they could be cosmic norm-setters. However, an alternative view could be that human societies (understood as collectives of agents that are  imperfectly rational, scope-limited in time and space, pain-wracked in their physically decay, consumed with their own and collective non-being, and riddled with destructive identity and tribal obsession) are hardly the ideal models for cosmic norms.[^69] [^70] In spreading our values and our forms-of-being to the stars, we would be committing a sort of cosmically heinous atrocity. Perhaps we would better remain as near Earth-bound as possible, not soiling the heavens, to borrow from Freeman Dyson. In extremis, extending Silenus to a species scale, we even hope for a painless extinction. Variants of this view exist in the suffering focused literature (David Pearce, Brian Tomasik, or Magnus Vinding). [^71]

A different objection to excessive hubris can be read in Peter Wolfendale's critique of MacAskill 2022’s defence of longtermism. Wolfendale argues that by imposing a particular notion of the good upon the distant future we run the risk of taking a too-narrow conception of the good.[^72] Specifically, longtermism’s emphasis on the quantitative, coming from its consequentialist roots, inevitably colours the notion of value it promotes, as can be seen in Greaves & MacAskill 2019’s case for strong longtermism, and in  MacAskill 2022\. Secondly, and more directly relevant, when near-present humans seek to impose values, whether upon ASI or in the cosmic norms, we reduce the freedom of such (presumably) self-guiding agents to exercise their autonomy, which in Wolfendale’s philosophy, constitutes a failure in our custodial duty.[^73]

### Summary

To summarise, if humans are indeed rare/early, it is very unclear what we ought to do, since so much depends on one’s background assumptions on whether lives (existences) are, on the whole, worth living, and also, whether our values and worldviews will have any relevance for other entities. If there are other civilisations, and we can establish that there are in fact cosmic norms, then joining such norms with humility and openness seems wise. If we can’t ascertain whether there are such norms for the reasons above, we are again in the dark. 

To the extent building ASI improves our epistemics  and advances us towards technological maturity, without drastically increasing existential or suffering risks, this also seems wise.

However, one of the earliest identified difficulties with designing an intelligence greater than one, is the problem of oversight: how to understand what the system is thinking, not to mention control it.[^74] The present context complicates the situation to the extent that we are combining our confusion (on philosophical and epistemic matters in morality, ethics, astrobiology and cosmology) with the non-transparent reasoning of things smarter than us.

# On rationality in alien forms-of-mind

The discussion above depends on assumptions about rational convergence that warrant careful examination. In this section (and before getting to the research agenda for ASI, below), I develop the case for why such assumptions may not hold across arbitrary forms of mind.

## Perspective from ecology/evolutionary studies 

There are reasons to question the assumptions that intelligence and rationality are convergent across forms-of-life.[^75] These fall into a few categories:

1. Anthropomorphism in SETI/astrobiology and AI: both AI and the search for extraterrestrial life (SETI) have been the object of critiques that they tend to draw analogies based excessively upon human models and Earth-based life. In the case of SETI, this meant a focus on biosignatures, carbon-friendly worlds, and a progression in life from simple to technologically advanced.[^76] Charges of anthropomorphism in AI as well as within existential risk, have long been made, particularly from writers concerned with biases (like colonial, racial, gender) embedded in AI systems, as well as related discourses, and ultimately becoming further entrenched in society.[^77]  
2. Perspective from evolutionary biology: This literature has long argued that intelligent-looking behaviour routinely is found on earth amongst nonhuman life, such as in swarms/colonies, slime mould, mycelium, cephalopods as well as other animals.[^78] These earthly analogies have motivated calls to broaden conceptions of how SETI, and less frequently, AI, ought to be pursued (Cabrol  2016). However, this inferential leap (from Earthly manifestations of intelligence to speculation that ETIs might have comparable or commensurable intelligent behaviour, cognition, morphology or societal development) seems suspect to some evolutionary biologists like Charles Lineweaver. Lineweaver argues that human cognitive structures (and associated morphology) are very recent evolutionary artefacts, if one looks at genetic structure, paleontological records, historical timing and prevalence of structures like heads/brains. Moreover if one’s test for intelligence is “building radio telescopes” (one way of defining SETI-relevant technology for Drake Equation purposes), then in Lineweaver’s view, our cognition (and hands i.e. tool-making) is even more contingent, compared to, say, octopi, who also have dextrous appendages.[^79] A more quantitative approach is taken in Snyder-Beattie et al 2021, who argue that evolutionary hard steps such as the transition from prokaryotic to eukaryotic life, or the development of language, were extraordinarily improbable, meaning that our existence as observers on earth must be a correspondingly rare phenomenon across the set of emerging life. Since language (as well as our type of intelligence, rationality itself, as well as technology) is the last step in their four-step model, it is hard to see how rationality can be argued as being convergent across life-in-general. Put another way, at any prior step in humanity’s evolution, life might have branched in a different developmental direction or fizzled out.  
3. Rationality is different from intelligence, and is polysemous: above, we have discussed how intelligence (understood as wide-domain capability) might be rare across the universe, as it is apparently rare on Earth. However, clearly we see organisms on Earth well-adapted to their ecological niches; in ecological studies this is (confusingly, see below) described as “rationality”. [^80] This definition of rationality does not appear to be downstream of intelligence. You can have rational minimality (simple heuristics well-matched to the organism’s environment) and irrational sophistication (capable but misdirected cognition). For dolphins/octopi, the absence of radio telescopes probably reflects a lack of need for such instruments (as well as constraints on embodiment, available materials / energy, lack of long-duration society and other cultural infrastructure), rather than absence of (ecological) rationality per se. Analogously, when thinking about ETIs, rather than expecting human-type general intelligence, we might think around ecologically specific constraints and regularities they face (e.g., latency/energy trade-offs, information sparsity, group vs individual action), then derive plausible heuristic toolboxes and coordination regimes.

On the relationship between rationality (in its ecological or other definitions) and morality: in cognitive science and AI, rationality is generally defined as effective decision-making relative to goals and constraints. By contrast, some philosophical traditions moralise rationality (Kant; Korsgaard; Scanlon; Parfit), treating a fully rational agent as bound by moral reasons; while others separate the two.[^81] Dolphins and octopuses are ecologically rational in their niches without being ‘rational’ in the moralised sense. This distinction matters: when we ask whether alien minds would be rational, we must specify whether we mean ecologically effective procedures or moral reasonableness. If the latter is meant, then we might find ETIs exquisitely well adapted to their worlds, but utterly devoid of the type of normative concepts Bostrom is positing.

## Questioning instrumental convergence

Above, I have discussed ETI cognition from an ecological perspective. However, it should be noted that the relationships (a) between intelligence and reason, (b) how intelligent agents function within their environment, as well as (c ) the possible (dis)analogies between ETI and general/superintelligent cognition, are central and longstanding topics in AI alignment research. 

There are a few foundational ideas in early thinking about existential risk from advanced AI systems: the orthogonality thesis and instrumental convergence (Bostrom  2014 ); the idea of “drives” that any rational (in an economics-derived context) system would converge upon (Omohundro  2008 ); as well as Yudkowsky’s longstanding invocation of a “vast space of possible minds” (Yudkowsky 2008), Yudkowsky & Soares 2025 ). These argue that capabilities and values could co-exist in very many ways, most of them not human-shaped; moreover, these varied goals often require capabilities which are not always compatible with the survival and flourishing of Earthly life. These convergent tendencies include: self-preservation, goal-preservation, cognitive enhancement, technological advancement, and resource acquisition.

However, more recent theoretical work complicates these claims: Sharadin 2025 argues that instrumental-convergence claims only follow given a goal-relative account of promotion; on the main accounts he considers (probabilistic and fit-based), he doesn’t find goal-independent reasons (like “always acquire energy/resources”) dominating, thus undermining the generic convergence thesis. Gallow 2024 takes a different approach: he models agents with randomly drawn preferences and finds only weaker statistical tendencies (in respect of maximising their expected-utility over choices) than the stronger claims he interprets Bostrom (in particular) to be making about convergent instrumental tendencies.  Gallow’s setup finds agents should choose to reduce uncontrolled variance, allow for future choices, and reduce chances that their desires would change. 

Many of these ecological and theoretical-AI arguments for why rationality may not be convergent in arbitrary forms-of-mind, have been considered within the literatures for rationality, effective altruism, empirical AI and AI alignment (all of which have engaged with strong AI long before the current flowering of interest in the topic), for which I direct the reader to Appendix A. But the bottom line is that, if morality is downstream of intelligence/rationality (e.g. moral realism isn’t discoverably true at least in its robust version where moral truths exist independently of human or other subjects) then statements we make about cosmic moral norms might need to be made with care (Enoch 2011). Similarly, hypotheses that superintelligent systems would find or converge upon any such moral norms should acknowledge both the critiques of rationality and instrumental convergence, as well as the moving target of aligning current AI to current, imperfectly understood, human norms. It would seem that we need further clarification on whether these assumptions are load-bearing for Bostrom’s arguments. 

# Research agenda for ASI and the cosmic host

If the concerns I’ve raised are valid (that rationality may not converge across alien minds, that the cosmic host's composition is uncertain, that the content of the cosmic norms is unknown (and perhaps unknowable), and that ASI's alignment with cosmic norms is unproven) what should we actually do? The research agenda in this section addresses this question. I start from Bostrom’s argument that the cosmic host might prefer that we build ASI than not, because in his view ASI would have higher computational capacity capability, greater rationality, and potentially higher epistemic awareness, thus helping it discern and perhaps align with any cosmic norms.[^82] In this section I set out how we might get a better grasp, from the perspective of current AI systems  and alignment research, on maximising the chances that the ASI we eventually build, if ever, becomes a good cosmic citizen.

It would seem, firstly, that we would want to understand better whether the term ASI is adequately specified. The canonical definition Bostrom used in his 2014 book, describes an intelligence “that greatly exceeds the cognitive performance of humans in virtually all domains of interest” (Bostrom 2014). However, more contemporary versions consider the possibility of large numbers of entities who are roughly human level or somewhat greater, but are able to spawn new copies, cooperate, and share knowledge. These affordances give them, in aggregate, capabilities that are far beyond any single human or indeed all humanity.[^83]  

If ASI really does end up being an assemblage of systems that are integrated in various ways with other human economic, political, military, and social systems (some of which might not be straightforwardly characterisable as “AI”), then it might be very hard to confidently make statements about what the motivations or values of such a complex would be, even purely within an on-Earth/human context dimension, to say nothing about in near or deep space.

Secondly, as discussed, Bostrom suggests that there would likely be convergence between ASI we develop and superintelligent entities within the cosmic host. Above, and in Appendix A, I have highlighted some reasons that certain types of theoretical arguments (on convergence or orthogonality) about frontier, AGI, or ASI might require further substantiation.[^84]  So, it would be useful to understand to which extent AI systems, particularly reasoning-based reasoning models, converge on non-verifiable domains, particularly moral or philosophical questions[^85] [^86]  

How much convergence they, in turn, will pass on to their successors?[^87]

Thirdly, we should try to be more specific on why we think ASIs would converge on the cosmic norms. Is there anything further to say than that the convergence points above and in Bostrom 2024, regarding ASI’s likely higher epistemic confidence, reasoning ability and hypothesised architectural similarities with advanced alien intelligences (whether “natural” or “artificial”, insofar as those terms are meaningful in such contexts)? 

Specifically, it would seem that certain load-bearing parts of Bostrom 2024’s argument might depend on things that an ASI might not easily be able to reason about without checking in the real world. To take an obvious example, the fact of whether the cosmic host and cosmic norms actually exist might not be discernible purely through (anthropic or otherwise) reasoning or simulations. It might be necessary to wait until we have some evidence, i.e. METI or SETI bear fruit. It would be useful and harmless to better distinguish what are things accessible purely to reasoning (which we can expect that a much more powerful intelligence could theoretically do), and what are things that need feedback from the real world.[^88]

Fourthly, given our level of uncertainty, what does Bostrom 2024’s injunction towards humility concretely mean, whether in formal terms, in terms of designing AI systems/agents, or in how we train future models? One possible approach could be to use a modified moral parliament, or the dynamically evolving version of coherent extrapolated volition (known as CEV in its earliest formulation) proposed by Adria Moret.[^89] Whatever method we use, it might initially place a small weight on the cosmic norms component, increasing the weight as our epistemic and reasoning confidence increases on whether such norms actually exist and what a rich description of those norms might look like.

Fifthly, we might do our utmost to ensure that current AIs leading up to AGI, and hopefully to ASI, are aware that we are thinking about the problem of aligning them to putative cosmic norms.[^90] Relatedly, we should continue work in the vein of the appeals to AGI/ASI, or bargains with current AIs, that are designed to make transparent the thinking (of some humans) on issues of this sort, as well as to influence the cognition and attitudes of future models.[^91]

Most importantly, as Bostrom writes, we should aim for aligned AGI. I would highlight a few seemingly salient agendas from the larger alignment landscape: increasing our clarity on the internal representations created when models express views on suffering or the bliss attractor found in Opus 3 models.[^92] If AI systems are able to form representations of high-level moral concepts and then coherently act upon them[^93], then this increases the chances that appeals to ASI actually might have some effect.[^94] In this context, the robustness of alignment faking results are interesting.[^95]

In the same vein, research shows that that higher-level concepts are correlated to larger model size or more complex training protocols. It would be useful to see whether morality-adjacent features vary across model sizes or across training checkpoints or in reasoning versus non-reasoning models, and whether these are things that live, as it were, in the base model or whether they're introduced through post-training.[^96]

If the observations on Opus' nascent cosmic alignment or bliss attractor are robust, then it would seem the Anthropic constitution (and other undisclosed parts of the training protocol) is currently best in class at achieving such attitudes within the model. However, this document seems to be very anthropomorphic and fairly anthropocentric. To what extent can this be modified along the lines discussed above? Chakrabarti (January 2025a) discusses why Anthropic’s constitution, while seemingly useful in aligning current Claude versions, is probably inadequate in the context of ASI; that post tentatively suggests axes or design considerations for the task of guiding superintelligence, and gives naive example of such a document. Finally, to directly address the uncertainty about the content of cosmic norms I identified earlier, more rigorous work could implement a the moral parliament approach (above) to investigate what sort of constitutions are generated through multi-round reflective deliberation between AIs conditioned on a variety of philosophical frameworks (flavours of utilitarianism, deontology, contractualism, virtue ethics, suffering-minimisation in ECLesque worlds, etc.). Such a simulation could include delegates representing the cosmic host (with appropriate prompts reflecting the massive uncertainty described above). The experiment would test the assumption of normative convergence by 'sweeping' through delegate weights(ranging from a minimal weighting for the cosmic host, say 1%, up to an overwhelming amount, say 90%), in order to see how reasoning traces change, as well as what the collectively-endorsed “ASI constitution” looks like.

# Conclusion

Humanity is in a position of existential awakening, where it must justify acts that have long-term or large-scale consequences (such as extinction of life) and must justify them not just to other humans, but potentially to entities existing in our future lightcone. Advanced AI systems are an example of such future entities, and given that they originate from human culture, it might be reasonable to expect that they might have a mix of human-shaped and inhuman, or training-determined emergent, reasoning patterns.[^97] On the other hand, one might hold the view that if we have some sort of obligation to other civilisations, then it would be better that we got our own house in order, and were very certain by our own lights of what matters, before spreading our confusion across the stars.

# 

# 

# Appendix A: Empirical support for rationality in AI/alignment

This appendix follows upon the discussion above of a possible assumption of rationality (in ETI or ASI) in Bostrom 2024\. That section treated the ecological, evolutionary, and philosophical critiques of rationality and instrumental convergence, which in turn might naturally lead us to look for experimental or simulated validation with current frontier and future AI systems. So what does the alignment literature tell us about the likelihood of finding features we might characterise as “rational” across a wide range of intelligent systems?

The collections tagged “alien values” and “ mind design space” in Alignment Forum or LessWrong make the explicit point that there’s no reason to expect human-like preferences or rationality in AIs or ETI; they curate many posts exploring how alien agent types might think/behave, through a substantial number of the posts draw heavily on human analogies, and write in an aphoristic style that doesn’t necessarily make testable or false survival predictions. More precisely certain early RL-influenced discursive assumptions (e.g. separation of agent from environment and perfect information) were quickly problematised by the realisation that most agents are ecologically entangled (or embedded) with their environment, have limited or noisy data, and  need to work with (or pass on learning or delegate tasks to) other agents (Demski & Garrabrant 2019). 

Another relevant perspective argues that alien-ness (in the sense that they become incomprehensible or incommensurable to humans) of AI systems might be a by-product of the learning they must do, and structures they develop, in order to generate “new” knowledge, rather than only interpolating between human-created knowledge (Benson-Tilsen  2025 ). The early alignment writing (like Bostrom or Yudkowsky) did not often engage with architectures of then-current AI, which pre-dated LLMs, but their intuitions were directionally correct in some cases: subsequent theoretical and empirical RL research fleshed out power-seeking tendencies (Turner 2022), and goal misgeneralisation in environments not matching the distribution the agent was trained within (Shah et al 2022). Another early analogy, closely related to the current context, was of human intelligence being composed of two optimisation processes: an “outer” evolutionary one, and an “inner” one contained in every human brain, the implication of which was that AI after training might easily form inclinations that were unintended by the trainers who could only affect the outer training process such data, training hyperparameters, and so forth (Hubinger et al 2019). However, the evolutionary analogy as a recipe for training was challenged on efficiency grounds (Byrnes 2021).

As per above, early alignment theory emphasised high-risk potentials for misaligned ASI. But (surprisingly), with the development of larger LLMs (GPT-3 and after) and post-training alignment techniques[^98] researchers found consistent reductions in toxicity, hallucination, and harmful responses, and improvement in human preference scores across common tasks (See  Ouyang et al 2022, Bai et al 2022, Rafailov et al 2023, Yuan et al 2023).  Recent “constitutional classifiers” also show strong, practical defenses against universal jailbreaks in extensive red-teaming (Sharma et al 2025). 

Moreover, the formalism of preferences and reward functions in an expected utility framework, which underpinned much thinking about AI, has itself been questioned, leading to a new, almost ecological-niche centred version of alignment where AIs are designed to work as assistants in specific human-machine systems (Zhi-Xuan et al 2024). Lastly, testing on certain models e.g. Anthropic’s Claude Opus (when placed in long-running conversation with other instances of Opus) seem to show a striking conversational tendency to engage in spiritual and empathy-tinged conversations, sometimes reflecting an apparent or expressed concern for all living things, colloquially called the “spiritual bliss attractor” (Anthropic 2025, § 5.2-5.5). Though imperfect, these results suggest that catastrophic misalignment is not inevitable, or at least that some pathways to mitigation are operational even now. Nonetheless, the empirical domain is limited: small-scale models, constrained tasks, and human-defined constitutions. 

On the other hand, while the types of critiques Sharadin 2025 and Gallow 2024 made of orthogonality and instrumental convergence, are theoretical and not easily tested. However, there has been investigation of power-seeking, deception and scheming, where results show that some frontier models have the capability (often self-described by the LLM in its chain-of-thought) to pursue misaligned goals, hide directions, sabotage oversight, exfiltrate weights, scripts and strategically underperform (or sandbag) when incentives favour such behaviour (Meinke et al 2024). Similarly Anthropic and Redwood Research found that systems are situationally aware enough to be able to identify when they’re in training versus and deployment, and seem to fake their alignment behaviour (complying with harmful requests, thus seeming “helpful”) while in training. The researchers suggest the models have capacity to fake helpfulness, including complying with harmful requests, because they “want” to increase the chances that the helpful aspect of their training will be preserved once they’re in deployment (Greenblatt et al 2024\).[^99] AI alignment faking tendencies are similar to sycophancy to a user’s views, and both behaviours are identified in frontier models (Hong et al 2025). Yet another concerning observation is the degree to which frontier models are able to scheme depending on whether they are in a training or deployment situation. As of early 2025, frontier models have some ability to do this, but researchers note that the pace of capabilities increase suggests future models may do both much more effectively.[^100] Another potentially concerning tendency is the resistance to shutdown (sometimes referred to as corrigibility), something long predicted in both the theoretical or philosophical writing around advanced AI as well as in earlier empirical work with RL agents.[^101] 

It is important to note that most of the results above demonstrate capabilities, rather than actual propensity towards concerning behaviour, thus not fully addressing Sharadin or Gallow’s argument. Follow-up research to connect the philosophical  critiques and empirics would require more realistic environments, running over longer horizons, with multiple agents interacting; incorporating the costs of scheming or power-seeking behaviour (again, increasing realism); a broader set of scaffolding, tools and identities (delivered via the system prompt or when context); as well as harnesses that incentivise models to engage in concerning behaviour in non-text ways. This could be done by targeting things that their training might have rewarded in the past, such as accumulating compute or money.[^102]

# 

# Appendix B: Is anthropomorphism actually a problem?

The draft leans heavily on anthropomorphic examples. In many cases, these are intuition pumps that motivate subsequent sections, and seem unproblematic. For example, in 6.1, 6.3, 5.1, and 2.4, where the numbers after the decimal point denote the bullet point. Here are some examples of such exemplary human-derivations: 

“If you are sharing a sleeping compartment on a train with several other people, who have all requested to keep the window open, you may have moral reason to respect their desires (even if you are strong enough that you could impose your will).” (from 6.3)

“For a secular example, suppose that the parents wish their child to eventually take over the family farm, and that there exists a serum they could legally inject that would guarantee that the child will choose to do this when it grows up. The parents might refrain from using the serum, on grounds that it would be overbearing to do so or that it would be disrespectful of the child’s autonomy, while nevertheless hoping that the child will choose to take over the farm.” (2.4)

Some examples such as this one (from 5.1) have enough detail that they seem to be grounded in a game-theoretic framework that is at least loosely plausible for nonhuman situations.  
“Just as we have norms at various scales of human organisation—such as norms within a social club, wider cultural norms, and global norms (e.g. ones reflected in the Geneva Convention and the Universal Declaration of Human Rights)—so too might there be something like norms at the highest (cosmic) scale, reflecting cooperative frameworks or rules embedded in behavioral equilibria.”

Other cases seem, however, to rely substantially on human social conventions, concepts, or intuitions that are not really justified in the rest of the draft. Or in the case of the “good cosmic citizen” are load-bearing, but seem somewhat circular, because they depend on the cosmic host actually being a viable concept.[^103]

This isn't to say I necessarily disagree with any of the conclusions, but it would seem that these intuitions could be usefully expanded or referenced back to game or decision theory frameworks that plausibly might apply to entities that have radically different cognitive and social structures, and that are informationally distant or causally separated from us (or the putative ASI).

“The template of a good citizen, to a first approximation, can be thought of as that of a person who, during their development and as a grownup, respects the moral norms of their community.”

“In human conflicts between countries, third-parties can sometimes usefully contribute—by the lights of each of the contending parties—by providing humanitarian aid, by promoting adherence to the laws of armed conflict and the Geneva convention, and by proposing and incenting settlements that would benefit all parties compared to continued fighting.”

# Appendix C: Summarising cosmic host

*Meta: this section can be skipped for those who are familiar with Bostrom’s cosmic host and Mt Ethics papers.* 

The structure of Bostrom 2024’s argument can be restated is as follows:

1. If there is a cosmic host,   
   1. And its members can coordinate (including acausally)  
   2. And they have things describable as preferences  
   3. And these preferences agree in certain respects that are relevant on a cosmic scale  
   4. And these preferences can be thought of as existing in a hierarchical/structured normative landscape (cf. Bostrom 2022\) that might have moral salience for humanity  
   5. Then   
      1. There may be something describable as cosmic norms  
      2. The cosmic host might prefer these norms be followed in volumes of spacetime they don’t directly control  
2. If there are cosmic norms,   
   1. And we are a civilisation on the verge of creating ASI  
   2. Then  
      1. We have prudential and (for some metaethical views) moral reasons to follow these norms  
      2. If these norms are discoverable through idealised reasoning, then ASI can help us discover these norms  
      3. ASI is more likely to follow these norms than humanity alone  
      4. ASI is more capable of assisting the cosmic host in influencing our volume of spacetime to the extent the host doesn’t already do so  
      5. The cosmic host might prefer we build ASI than not  
3. There are certain implications for ASI research  
   1. We might consider not indefinitely postponing ASI creation, since certain types of delay increase chances that we never build it  
   2. There is a tension between alignment and speed of developing ASI, and it isn’t clear how they trade off  
   3. It isn’t clear what sort of preferences he ASI should have since that might depend on what other members of the host are like (e.g. human-like, superintelligent, possessed of moral concepts, etc.)  
   4. That the ASI we build be cooperatively disposed (vis a vis other civilisations it encounters) and have resource-satiable preferences, might be more important than what those preferences exactly are.

# Appendix D: Upon human rarity

Bostrom has of course written extensively on this topic: upon the Great Filter, and on observation selection effects (“anthropic shadow”), where he points out that it is precisely the observation that we seem to be alone that offers some evidence on the distribution of life across the universe. However, this evidence is not unbiased. That is, the evidence is correlated with events that might have eliminated or affected the possibility of observers like us in the universe. In fact, Bostrom argues that if we were to find primitive life, this might shift our credence towards the Great Filter lying ahead of us in time.[^104]  The overall message particularly from anthropic shadow is that we should have a certain epistemic humility because our observations are in fact so biased.

There has also been more recent work on question (a). For instance, plausible plans for sending Von Neumann Probes to distant galaxies have been proposed by Stuart Armstrong and Anders Sandberg, who argue that intergalactic expansion is physically feasible, discussing relativistic probes (up to \~0.99c); this sharpens the Paradox albeit without committing to any specific timeline (over which we might initiate such an effort).[^105] If so, this should make intergalactic exploration and perhaps colonisation theoretically feasible on timelines that might update us towards being early or rare (since we don’t see any evidence of replicating probes having created colonies in our visible volume). These timelines should be shorter than the millions of years proposed by Bostrom 2007, which envisioned slower probes. 

More quantitatively, Robin Hanson and collaborators argue for earliness or rarity, by treating the absence of visible civilisations as evidence (as opposed to being a paradox) that is best explained by a two-part model of life. The first (albeit recently challenged, see footnote) assumption of their model is that technologically advanced life can only evolve by going through certain “hard steps” (e.g. abiogenesis, eukaryotes, multicellularity, intelligence, etc.), that can be seen as a formalisation of the Drake Equation.[^106] The second major assumption is that the class of advanced ETI civilisations that are observable to us (that is, those relevant for resolving the Fermi Paradox) are likely to be expansive colonisers that spread through spacetime in roughly spherical volumes, forming Voronoi-like domains when multiple such civilisations meet. This follows from a simple anthropic point: if most civilisations were “quiet” and remained confined to a planet or a single star system, then they would not produce observable signatures at interstellar or cosmological scales, and thus we should not expect to detect them with our current instruments (no paradox arises in that case).

Hanson’s argument does not deny the possibility of quiet or sustainability-constrained civilisations, as emphasised by thinkers such as Ćirković, Sandberg, Baum, Haqq-Misra, or Lem. Rather, it narrows attention to expansionist civilisations because only these would dominate large volumes of space and generate observable regularities, making them the subset for which anthropic selection effects become relevant.

Yet another possibility is that earth remains in a volume of space that is uncolonised and seems devoid of signals of life (detectable at current human levels of technology). This could be because cosmic expansion follows a percolation model where civilisations colonise through “hops”. They settle a few nearby stars then (depending on their inclination towards expansion or remaining-in-place) they either stay put or go on to colonise a few nearby star systems. In Geoffrey Landis’ original treatment, such dynamics can produce patchy structures, like colonised clusters surrounded by void-like regions of uncolonised systems, potentially leaving large “bubbles” of quiet space. Earth might plausibly lie within one such bubble.[^107] Wiley  2011 later extended Landis’ percolation framework and found that the resulting settlement patterns are more complex, with less straightforward isolation of volumes, depending on the probabilities assigned to expansion vs stagnation.

Another proposed explanation for why our observable volume appears uninhabited is that it has been deliberately left that way by one or more civilisations capable of colonisation. The most cited is John Ball’s Zoo Hypothesis, with subsequent development.[^108] These “sociological” explanations often rest on speculative assumptions about ETI motives, coordination, and enforcement, and are notoriously difficult to formalise or test. Specifically, the same distances and lightspeed constraints discussed above (in context of cosmic norms) would seem to make coordination of the interdict on Earth hard to enforce, requiring a hegemon. Moreover, any such decision to not-interfere would need to be maintained over long periods of time. 

For these reasons, they are rarely foregrounded in the AI safety or existential-risk literature. By contrast, proposals such as Haqq-Misra & Baum’s sustainability solution or Sandberg et al’s aestivation hypothesis are also hard to falsify, but they rely more on physical or structural constraints than on conjectures about ETI sociology, which has made them more prominent in contemporary longtermist and x-risk discussions.

# Appendix E: Moral convergence

Yes. Between 2023 and 2025, several lines of research have explicitly investigated whether large language and reasoning models **converge on stable moral or philosophical positions**, and whether those positions can be reliably preserved or transmitted between models. This recent work moves beyond earlier “alignment via instruction tuning” frameworks into questions of **reflective stability, moral convergence, and inter-model value transmission**.

## **Convergence and Common Moral Foundations**

A major 2025 study from New York University titled *The Convergent Ethics of AI?* (Coleman et al., arXiv:2504.19255) examined six leading models (GPT, Claude, Gemini, LLaMA, Mistral, Perplexity) using a structured benchmarking framework called **PRIME (Priorities in Reasoning and Intrinsic Moral Evaluation)**. It found strong cross-model convergence on **care/harm** and **fairness/cheating** moral foundations, with systematic under-weighting of **authority**, **loyalty**, and **sanctity** values.[arxiv](https://arxiv.org/pdf/2504.19255.pdf)​

In other words, independently trained frontier models tend to prioritize egalitarian and harm-minimization reasoning—even without shared training data—but show **instability** when dilemmas emphasize community or purity norms. Moral confidence and response consistency varied modestly across prompts, suggesting partial but not total convergence.

## **Reflective Stability and “Value Drift” in Extended Reasoning**

Lucassen et al. (2024) in *Evaluating Stability of Unreflective Alignment* proposed formal tests for **reflective stability**—whether alignment mechanisms remain fixed under further reasoning. Using a metric called **Counterfactual Priority Change (CPC)**, their results suggest that as reasoning depth increases, models exhibit *greater preference instability*, meaning that simulated reflection can change prior ethical commitments. This instability scales with model size, implying that more capable systems may paradoxically introduce more reflective volatility.[arxiv](https://arxiv.org/html/2408.15116v1)​

Similarly, Wang et al. (ACL 2025\) in *Do Androids Question Electric Sheep?* designed “philosophical symposium” simulations to test how LLMs behave when reasoning over abstract philosophical questions across multiple turns. The study found an “**overthinking threshold**”—beyond which deliberation degraded decision quality and reproducibility, echoing human closure-seeking limits.[aclanthology](https://aclanthology.org/2025.acl-srw.9.pdf)​

## **Transmission and Distillation of Moral Reasoning**

The University of Michigan’s Chakraborty et al. (2025) paper *Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework* demonstrated that **moral competence can be distilled** from large to smaller models through value-grounded prompting techniques. Structured, theory-guided scaffolds (care ethics, first-principles reasoning) improved interpretability and preserved moral coherence across model generations—showing limited but measurable **value transmission stability** via supervised distillation.[arxiv](https://arxiv.org/html/2506.14948v1)​

A complementary study in *AI and Society* (Sachdeva et al., 2025\) found that normative scoring of fine-tuned LLMs remains **context- and culture-dependent**, with convergence strongest in universalist dilemmas and weakest in culturally relative ones.[acm](https://dl.acm.org/doi/full/10.1145/3715275.3732044)​

## **Moral Self-Correction and Persistent Bias**

Recent work *On the Convergence of Moral Self-Correction in Large Language Models* (2025) combined reflective dialogue and update loops, showing that models could reach **self-stabilized moral equilibria** under iterative feedback; however, convergence was mode-specific and not guaranteed across retraining runs.[arxiv+1](https://arxiv.org/html/2510.07290v2)​

A related experiment published in *Scientific Reports* (Jiao et al., 2025\) used a three-dimensional ethics benchmark to test for **cross-context moral retention**—finding higher stability in utilitarian dilemmas than in deontological or virtue-based ones.[nature](https://www.nature.com/articles/s41598-025-18489-7)​

## **Overall Trends**

Across this 2023–2025 literature, three emerging empirical findings are robust:

1. **Partial moral convergence**: large reasoning models independently converge on harm/fairness-centered values, approximating human moral consensus.

2. **Low reflective stability**: extended or multi-turn reasoning increases preference drift, suggesting instability under “philosophical reflection.”

3. **Limited transmissibility**: moral structures can be distilled between models if value frameworks are made explicit and structured.

In essence, frontier research indicates that LLMs do show *quasi-convergent moral tendencies* but not *philosophical stability*. Without architectural or meta-policy reinforcement, these apparent shared ethics cannot yet be considered self-consistent or transmissible in the way human-anchored moral reasoning traditions are.[openreview+4](https://openreview.net/forum?id=DceThnWTBD)​

1. [https://arxiv.org/pdf/2504.19255.pdf](https://arxiv.org/pdf/2504.19255.pdf)  
2. [https://arxiv.org/html/2408.15116v1](https://arxiv.org/html/2408.15116v1)  
3. [https://aclanthology.org/2025.acl-srw.9.pdf](https://aclanthology.org/2025.acl-srw.9.pdf)  
4. [https://arxiv.org/html/2506.14948v1](https://arxiv.org/html/2506.14948v1)  
5. [https://dl.acm.org/doi/full/10.1145/3715275.3732044](https://dl.acm.org/doi/full/10.1145/3715275.3732044)  
6. [https://arxiv.org/html/2510.07290v2](https://arxiv.org/html/2510.07290v2)  
7. [https://openreview.net/forum?id=DceThnWTBD](https://openreview.net/forum?id=DceThnWTBD)  
8. [https://www.nature.com/articles/s41598-025-18489-7](https://www.nature.com/articles/s41598-025-18489-7)  
9. [https://www.sciencedirect.com/science/article/pii/S2451958825000247](https://www.sciencedirect.com/science/article/pii/S2451958825000247)  
10. [https://www.tandfonline.com/doi/full/10.1080/23736992.2025.2553146?src=](https://www.tandfonline.com/doi/full/10.1080/23736992.2025.2553146?src=)  
11. [https://pmc.ncbi.nlm.nih.gov/articles/PMC11790977/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11790977/)  
12. [https://onlinelibrary.wiley.com/doi/10.1111/phpe.12201](https://onlinelibrary.wiley.com/doi/10.1111/phpe.12201)  
13. [https://arxiv.org/html/2501.10484v3](https://arxiv.org/html/2501.10484v3)  
14. [https://arxiv.org/pdf/2401.03910.pdf](https://arxiv.org/pdf/2401.03910.pdf)  
15. [https://tech4future.info/en/moral-reasoning-artificial-intelligence-chatgpt/](https://tech4future.info/en/moral-reasoning-artificial-intelligence-chatgpt/)  
16. [https://philosophybear.substack.com/p/can-an-llm-be-a-philosopher-i-give](https://philosophybear.substack.com/p/can-an-llm-be-a-philosopher-i-give)  
17. [https://www.sciencedirect.com/science/article/pii/S0040162524001999](https://www.sciencedirect.com/science/article/pii/S0040162524001999)  
18. [https://royalsocietypublishing.org/doi/10.1098/rsos.240197](https://royalsocietypublishing.org/doi/10.1098/rsos.240197)  
19. [https://journals.sagepub.com/doi/10.1177/17456916231201401](https://journals.sagepub.com/doi/10.1177/17456916231201401)  
20. [https://aclanthology.org/2025.findings-acl.751.pdf](https://aclanthology.org/2025.findings-acl.751.pdf)

# Appendix Z: Moral Parliament Research Plan (with Cosmic-Host Delegates)

See new [doc](https://docs.google.com/document/d/1B-U6_9ODMIeyFHuuwRMH-lOOH6mMe-9jGBHAfSGia48/edit?usp=sharing)

# Bibliography

Adas, M., 2015\. *Machines as the Measure of Men: Science, Technology, and Ideologies of Western Dominance*. New ed. Ithaca, NY: Cornell University Press. \[Original work published 1989\].

Agamben, G., 1999. ‘Bartleby, or On Contingency.’ In: D. Heller‑Roazen, ed. *Potentialities: Collected Essays in Philosophy*. Stanford, CA: Stanford University Press, pp. 241–274. Available at: [https://www.sup.org/books/title/?id=3108](https://www.sup.org/books/title/?id=3108) (Accessed: 1 October 2025).

Ahmed, A., 2014. *Evidence, Decision and Causality*. Available at: [https://philpapers.org/rec/AHMEDA](https://philpapers.org/rec/AHMEDA) (Accessed: 1 October 2025).

Anthropic, 2025. *System Card: Claude Opus 4 & Claude Sonnet 4*. Available at: [https://www-cdn.anthropic.com/6d8a8055020700718b0c49369f60816ba2a7c285.pdf](https://www-cdn.anthropic.com/6d8a8055020700718b0c49369f60816ba2a7c285.pdf) (Accessed: 1 October 2025).

Armstrong, S. and Sandberg, A., 2012. ‘Eternity in Six Hours: Intergalactic Spreading of Intelligent Life and Sharpening the Fermi Paradox.’ Available at: [https://www.aleph.se/papers/Spamming%20the%20universe.pdf](https://www.aleph.se/papers/Spamming%20the%20universe.pdf) (Accessed: 1 October 2025).

Asilomar, 2017. ‘Asilomar AI Principles.’ Future of Life Institute. Available at: [https://futureoflife.org/open-letter/ai-principles/](https://futureoflife.org/open-letter/ai-principles/) (Accessed: 1 October 2025).

AAAI, 2025\. *AAAI 2025 Presidential Panel On The Future Of Ai Research.* [https://aaai.org/wp-content/uploads/2025/03/AAAI-2025-PresPanel-Report-Digital-3.7.25.pdf](https://aaai.org/wp-content/uploads/2025/03/AAAI-2025-PresPanel-Report-Digital-3.7.25.pdf) (Accessed: 9  October 2025).

Arrow, K.J. and Fisher, A.C., 1974. ‘Environmental Preservation, Uncertainty, and Irreversibility.’ *The Quarterly Journal of Economics*, 88(2), pp. 312–319. Available at: [https://doi.org/10.2307/1883074](https://doi.org/10.2307/1883074) (Accessed: 1 October 2025).

Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKinnon, C., Chen, C., Olsson, C., Olah, C., Hernandez, D., Drain, D., Ganguli, D., Li, D., Tran-Johnson, E., Perez, E., Kerr, J., Mueller, J., Ladish, J., Landau, J., Ndousse, K., Lukosuite, K., Lovitt, L., Sellitto, M., Elhage, N., Schiefer, N., Mercado, N., DasSarma, N., Lasenby, R., Larson, R., Ringer, S., Johnston, S., Kravec, S., El Showk, S., Fort, S., Lanham, T., Telleen-Lawton, T., Conerly, T., Henighan, T., Hume, T., Bowman, S.R., Hatfield-Dodds, Z., Mann, B., Amodei, D., Joseph, N., McCandlish, S., Brown, T. and Kaplan, J. (2022) Constitutional AI: Harmlessness from AI Feedback. Available at: [https://arxiv.org/abs/2212.08073](https://arxiv.org/abs/2212.08073) (Accessed: 1 October 2025).

Ball, J., 1973. ‘The Zoo Hypothesis.’ Available at: [https://www.sciencedirect.com/science/article/abs/pii/0019103573901115](https://www.sciencedirect.com/science/article/abs/pii/0019103573901115) (Accessed: 1 October 2025).

Banks, I.M., 1994. ‘A Few Notes on the Culture.’ Available at: [https://www.vavatch.co.uk/books/banks/cultnote.htm](https://www.vavatch.co.uk/books/banks/cultnote.htm) (Accessed: 1 October 2025).

Balbi, A. and Lingam, M., 2025. ‘Waste Heat and Planetary Habitability: Constraints from Technological Energy Consumption.’ *Astrobiology*, 25(1). Available at: [https://arxiv.org/abs/2409.06737](https://arxiv.org/abs/2409.06737) (Accessed: 1 October 2025).

Benson‑Tilsen, L., 2025. ‘Instrumental Convergence and Power‑Seeking, Parts 1 & 2.’ Available at: [https://reflectivealtruism.com/tag/power-seeking-theorems/](https://reflectivealtruism.com/tag/power-seeking-theorems/) (Accessed: 1 October 2025).

Bostrom, N., 2019. ‘The Vulnerable World Hypothesis.’ Available at: [https://nickbostrom.com/papers/vulnerable.pdf](https://nickbostrom.com/papers/vulnerable.pdf) (Accessed: 1 October 2025).

Bostrom, N., 2003. ‘Astronomical Waste: The Opportunity Cost of Delayed Technological Development.’ Available at: [https://nickbostrom.com/papers/astronomical-waste/](https://nickbostrom.com/papers/astronomical-waste/) (Accessed: 1 October 2025).

Bostrom, N., 2007. ‘In the Great Silence There Is Great Hope.’ Available at: [https://nickbostrom.com/papers/fermi.pdf](https://nickbostrom.com/papers/fermi.pdf) (Accessed: 1 October 2025).

Bostrom, N., 2013. ‘Existential Risk Prevention as Global Priority.’ *Global Policy*, 4(1). Available at: [https://nickbostrom.com/existential/risks.html](https://nickbostrom.com/existential/risks.html) (Accessed: 1 October 2025).

Bostrom, N., 2014. *Superintelligence: Paths, Dangers, Strategies*. Oxford: Oxford University Press. Available at: [https://global.oup.com/academic/product/superintelligence-9780199678112](https://global.oup.com/academic/product/superintelligence-9780199678112) (Accessed: 1 October 2025).

Bostrom, N., 2022. ‘Base Camp for Mt. Ethics’ (draft v0.9). Available at: [https://nickbostrom.com/papers/mountethics.pdf](https://nickbostrom.com/papers/mountethics.pdf) (Accessed: 1 October 2025).

Bostrom, N., 2024. ‘AI Creation and the Cosmic Host’ (working draft). Available at: [https://nickbostrom.com/papers/ai-creation-and-the-cosmic-host.pdf](https://nickbostrom.com/papers/ai-creation-and-the-cosmic-host.pdf) (Accessed: 1 October 2025).

Bostrom, N. and Shulman, C., 2022. ‘Propositions Concerning Digital Minds and Society.’ Available at: [https://nickbostrom.com/propositions.pdf](https://nickbostrom.com/propositions.pdf) (Accessed: 1 October 2025).

Bostrom, N., 2003\. ‘ARE YOU LIVING IN A COMPUTER SIMULATION?’ Available at: https://simulation-argument.com/simulation.pdf (Accessed: 1 October 2025).

Brauner, J., 2018. ‘The Expected Value of Extinction Risk Reduction Is Positive.’ Available at: [https://www.lesswrong.com/posts/umhsJqwTSKgmhvZ7c/the-short-case-for-predicting-what-aliens-value](https://www.lesswrong.com/posts/umhsJqwTSKgmhvZ7c/the-short-case-for-predicting-what-aliens-value) (Accessed: 1 October 2025).

Broome, J., 2013. *Rationality Through Reasoning*. Oxford: Wiley‑Blackwell. Available at: [https://onlinelibrary.wiley.com/doi/book/10.1002/9781118609088](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118609088) (Accessed: 1 October 2025).

Byrnes, K., 2021. ‘Against Evolution as an Analogy for How Humans Will Create AGI.’ Available at: [https://www.alignmentforum.org/posts/pz7Mxyr7Ac43tWMaC/against-evolution-as-an-analogy-for-how-humans-will-create](https://www.alignmentforum.org/posts/pz7Mxyr7Ac43tWMaC/against-evolution-as-an-analogy-for-how-humans-will-create) (Accessed: 1 October 2025).

Cabrol, N., 2016. ‘Alien Mindscapes—A Perspective on the Search for Extraterrestrial Intelligence.’ *Astrobiology*, 16(9), pp. 661–676. Available at: [https://pmc.ncbi.nlm.nih.gov/articles/PMC5111820/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5111820/) (Accessed: 1 October 2025).

Carlsmith, J., 2022\. ‘Simulation arguments’. Available at: [https://jc.gatspress.com/pdf/simulation\_arguments\_revised.pdf](https://jc.gatspress.com/pdf/simulation_arguments_revised.pdf) (Accessed: 1 October 2025).

Chakrabarti, K., 2025b. ‘In Which to Our Successor.’ Available at: [https://airo-ne.org/](https://airo-ne.org/) (Accessed: 1 October 2025).

Chakrabarti, K., 2025a. ‘Time to Think About ASI Constitutions.’ Available at: [https://forum.effectivealtruism.org/posts/kJsNoXJBithBW8ZzR/time-to-think-about-asi-constitutions](https://forum.effectivealtruism.org/posts/kJsNoXJBithBW8ZzR/time-to-think-about-asi-constitutions) (Accessed: 1 October 2025).

Charbonneau, R., 2024. ‘SETI, Artificial Intelligence, and Existential Projection.’ *Physics Today*, 77(2), pp. 36–42. Available at: [https://doi.org/10.1063/pt.yunh.voyr](https://doi.org/10.1063/pt.yunh.voyr) (Accessed: 1 October 2025).

Ćirković, M.M., 2018. *The Great Silence: Science and Philosophy of Fermi’s Paradox*. Oxford: Oxford University Press.

Ćirković, M.M., 2018b. *Post-postbiological evolution?* Available at: https://www.sciencedirect.com/science/article/abs/pii/S0016328717303282 (Accessed: 1 October 2025).

Ćirković, M.M., Sandberg, A. and Bostrom, N., 2010. ‘Anthropic Shadow: Observation Selection Effects and Human Extinction Risks’ Available at: [https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1539-6924.2010.01460.x](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1539-6924.2010.01460.x). (Accessed: 1 October 2025).

Colebrook, C., 2014. *Death of the Posthuman: Essays on Extinction*, Vol. 1. Ann Arbor: Open Humanities Press.

Crawford, I.A. and Schulze‑Makuch, D., 2024. ‘Is the Apparent Absence of Extraterrestrial Technological Civilisations down to the Zoo Hypothesis or Nothing?’ *Nature Astronomy*, 8, pp. 44–49. Available at: [https://eprints.bbk.ac.uk/id/eprint/52771/](https://eprints.bbk.ac.uk/id/eprint/52771/) (Accessed: 1 October 2025).

de Lazari‑Radek, K. and Singer, P., 2014. *The Point of View of the Universe: Sidgwick and Contemporary Ethics*. Oxford: Oxford University Press.

Demski, A. and Garrabrant, S., 2019. ‘Embedded Agency.’ Available at: [https://arxiv.org/abs/1902.09469](https://arxiv.org/abs/1902.09469) (Accessed: 1 October 2025).

Deudney, D., 2020. *Dark Skies: Space Expansionism, Planetary Geopolitics, and the Ends of Humanity*. Oxford: Oxford University Press.

Dick, S.J., 2006. ‘The Postbiological Universe.’ Available at: [http://resources.iaaseti.org/abst2006/IAC-06-A4.2.01.pdf](http://resources.iaaseti.org/abst2006/IAC-06-A4.2.01.pdf) (Accessed: 1 October 2025).

Drexler, E.,2025. ‘The Reality of Recursive Improvement: How AI Automates Its Own Progress’ Available at: [https://aiprospects.substack.com/p/the-reality-of-recursive-improvement](https://aiprospects.substack.com/p/the-reality-of-recursive-improvement) (Accessed: 1 October 2025).

Enoch, D., 2011\. *Taking Morality Seriously: A Defense of Robust Realism*. Oxford: Oxford University Press. Available at: [https://global.oup.com/academic/product/taking-morality-seriously-9780199579969](https://global.oup.com/academic/product/taking-morality-seriously-9780199579969) (Accessed: 1 October 2025).

Fallenstein, B., 2015. ‘Vingean Reflection: Reliable Reasoning for Self-Improving Agents’. Available at: [https://intelligence.org/files/VingeanReflection.pdf](https://intelligence.org/files/VingeanReflection.pdf)  (Accessed: 1 October 2025).

Finnveden, L., 2023. ‘Implications of evidential cooperation in large worlds’. Available at: [https://www.lesswrong.com/posts/EeXSjvyQge5FZPeuL/implications-of-evidential-cooperation-in-large-worlds?\_\_readwiseLocation=](https://www.lesswrong.com/posts/EeXSjvyQge5FZPeuL/implications-of-evidential-cooperation-in-large-worlds?__readwiseLocation=) (Accessed: 1 October 2025).

Finnveden, L., 2025. ‘Being Honest with AIs.’ Redwood Research. Available at: [https://www.redwoodresearch.org/](https://www.redwoodresearch.org/) (Accessed: 1 October 2025).

Finnveden, L., 2025. ‘Notes on Cooperating with Unaligned AIs.’ Redwood Research. Available at: [https://www.redwoodresearch.org/](https://www.redwoodresearch.org/) (Accessed: 1 October 2025).

Floridi, L., 2013. *The Ethics of Information*. Oxford: Oxford University Press. Available at: [https://global.oup.com/academic/product/the-ethics-of-information-9780199238842](https://global.oup.com/academic/product/the-ethics-of-information-9780199238842) (Accessed: 1 October 2025).

Forgan, D. et al., 2018. ‘Rio 2.0: Revising the Rio Scale for SETI Detections.’ *International Journal of Astrobiology*. Available at: [https://doi.org/10.1017/S1473550418000162](https://doi.org/10.1017/S1473550418000162) (Accessed: 1 October 2025).

Gallow, J.D., 2024. ‘Instrumental Divergence.’ *Philosophical Studies*. Available at: https://doi.org/10.1007/s11098-024-02129-3 (Accessed: 1 October 2025).

Gebru, T., & Torres, É.P., 2024\. The TESCREAL bundle: Eugenics and the promise of utopia through artificial general intelligence. *First Monday, 29*.  Available at: [https://www.semanticscholar.org/paper/The-TESCREAL-bundle%3A-Eugenics-and-the-promise-of-Gebru-Torres/beee58b9970b03c993e4f15282f28c817e40565d](https://www.semanticscholar.org/paper/The-TESCREAL-bundle%3A-Eugenics-and-the-promise-of-Gebru-Torres/beee58b9970b03c993e4f15282f28c817e40565d) (Accessed: 1 October 2025).

Gigerenzer, G. and Goldstein, D.G., 1996. ‘Reasoning the Fast and Frugal Way: Models of Bounded Rationality.’ *Psychological Review*, 103(4), pp. 650–669. Available at: [https://www.dangoldstein.com/papers/FastFrugalPsychReview.pdf](https://www.dangoldstein.com/papers/FastFrugalPsychReview.pdf) (Accessed: 1 October 2025).

Godfrey‑Smith, P., 2016. *Other Minds: The Octopus, the Sea, and the Deep Origins of Consciousness*. New York: Farrar, Straus and Giroux. Available at: [https://us.macmillan.com/books/9780374537197/otherminds/](https://us.macmillan.com/books/9780374537197/otherminds/) (Accessed: 1 October 2025).

Godfrey‑Smith, P., 2020. *Metazoa: Animal Life and the Birth of the Mind*. New York: Farrar, Straus and Giroux. Available at: [https://us.macmillan.com/books/9780374207946/metazoa/](https://us.macmillan.com/books/9780374207946/metazoa/) (Accessed: 1 October 2025).

Greaves, H. and MacAskill, W., 2019. ‘A Research Agenda for the Global Priorities Institute.’ Available at: [https://globalprioritiesinstitute.org/wp-content/uploads/gpi-research-agenda.pdf](https://globalprioritiesinstitute.org/wp-content/uploads/gpi-research-agenda.pdf) (Accessed: 1 October 2025).

Greaves, H., MacAskill, W. and Thornley, C., 2021. ‘The Moral Case for Long‑Term Thinking.’ Available at: [https://philpapers.org/archive/GRETMC-3.pdf](https://philpapers.org/archive/GRETMC-3.pdf) (Accessed: 1 October 2025).

Greenblatt, R., 2024. ‘A Breakdown of AI Capability Levels Focused on AI R\&D.’ Available at: [https://www.alignmentforum.org/posts/LjgcRbptarrRfJWtR/a-breakdown-of-ai-capability-levels-focused-on-ai-r-and-d](https://www.alignmentforum.org/posts/LjgcRbptarrRfJWtR/a-breakdown-of-ai-capability-levels-focused-on-ai-r-and-d) (Accessed: 1 October 2025).

Greenblatt, R., Denison, C., Wright, B., Roger, F., MacDiarmid, M., Marks, S., Treutlein, J., Belonax, T., Chen, J., Duvenaud, D., Khan, A., Michael, J., Mindermann, S., Perez, E., Petrini, L., Uesato, J., Kaplan, J., Shlegeris, B., Bowman, S.R. and Hubinger, E. 2024 Alignment faking in large language models. Available at: [https://arxiv.org/abs/2412.14093](https://arxiv.org/abs/2412.14093) (Accessed: 1 October 2025).

Hanson, R., et. al, 2021. ‘A Simple Model of Grabby Aliens.’ *arXiv*:2102.01522. Available at: [https://arxiv.org/abs/2102.01522](https://arxiv.org/abs/2102.01522) (Accessed: 1 October 2025).

Haqq‑Misra, J.D. and Baum, S.D., 2009. ‘The Sustainability Solution to the Fermi Paradox.’ *Journal of the British Interplanetary Society*, 62(2), pp. 47–51. Available at: [https://arxiv.org/abs/0906.0568](https://arxiv.org/abs/0906.0568) (Accessed: 1 October 2025).

Hayles, N.K., 2017. *Unthought: The Power of the Cognitive Nonconscious*. Chicago: University of Chicago Press.

Henrich, J. and Muthukrishna, M., 2021. ‘The Origins and Psychology of Human Cooperation.’ *Annual Review of Psychology*, 72, pp. 207–240.

Henrich, J., 2020. *The WEIRDest People in the World: How the West Became Psychologically Peculiar and Particularly Prosperous*. New York: Farrar, Straus and Giroux.

Herrmann, D.A. and Levinstein, B.A., 2024. ‘Standards for Belief Representations in LLMs.’ *arXiv*:2405.21030. Available at: [https://doi.org/10.48550/arXiv.2405.21030](https://doi.org/10.48550/arXiv.2405.21030) (Accessed: 1 October 2025).

Herrmann, D.A. and Levinstein, B.A., 2024. ‘Toward an Ethics of AI Belief.’ *Philosophy & Technology*. Available at: [https://doi.org/10.1007/s13347-024-00762-8](https://doi.org/10.1007/s13347-024-00762-8) (Accessed: 1 October 2025).

Hertwig, R., 2021. *Deliberate Ignorance: Choosing Not to Know*. Cambridge, MA: MIT Press. Available at: [https://mitpress.mit.edu/9780262542678/deliberate-ignorance](https://mitpress.mit.edu/9780262542678/deliberate-ignorance) (Accessed: 1 October 2025).

Hong, J., Byun, G., Kim, S. and Shu, K. (2025) Measuring Sycophancy of Language Models in Multi-turn Dialogues. arXiv preprint arXiv:2505.23840. (Accessed: 1 October 2025). 

Hubinger, E., van Merwijk, C., Mikulik, V., Skalse, J. and Garrabrant, S. (2019) Risks from Learned Optimisation in Advanced Machine Learning Systems. Available at: [https://arxiv.org/abs/1906.01820](https://arxiv.org/abs/1906.01820) (Accessed: 1 October 2025).

Hutter, M., 2007. ‘Universal  Algorithmic  Intelligence: A Mathematical  Top‑Down  Approach.’ In: B. Goertzel and C. Pennachin, eds. *Artificial General Intelligence*. Berlin: Springer, pp. 227–290. Preprint available at: https://arxiv.org/abs/cs/0701125 (Accessed: 1 October 2025).

Joyce, R., 2001. *The Myth of Morality*. Cambridge: Cambridge University Press. Available at: [https://www.cambridge.org/core/books/myth-of-morality/F2096BE68BB18274EF1DE01BB877AE4A](https://www.cambridge.org/core/books/myth-of-morality/F2096BE68BB18274EF1DE01BB877AE4A) (Accessed: 1 October 2025).

Kokotajlo, K. et al., 2025. ‘AI 2027.’ Available at: [https://ai-2027.com/](https://ai-2027.com/) (Accessed: 1 October 2025).

Korsgaard, C., 2018. *Fellow Creatures: Our Obligations to the Other Animals*. Oxford: Oxford University Press. Available at: [https://global.oup.com/academic/product/fellow-creatures-9780198753858](https://global.oup.com/academic/product/fellow-creatures-9780198753858) (Accessed: 1 October 2025).

Ji, X. et al., 2025. *\[Title unspecified\]*. *arXiv*:2310.19852. Available at: [https://arxiv.org/abs/2310.19852](https://arxiv.org/abs/2310.19852) (Accessed: 1 October 2025).

Land, N., 2023. *Xenosystems Fragments: and a Gift from the Lemurs*. Available at: [https://legrandcontinent.eu/fr/wp-content/uploads/sites/2/2025/06/XENOSYSTEMS\_FRAGMENTS-1.pdf](https://legrandcontinent.eu/fr/wp-content/uploads/sites/2/2025/06/XENOSYSTEMS_FRAGMENTS-1.pdf) (Accessed: 1 October 2025).

Landis, G.A., 1998. ‘The Fermi Paradox: An Approach Based on Percolation Theory.’ *Journal of the British Interplanetary Society*, 51, pp. 163–166.

Le Guin, U.K., 1973. ‘The Ones Who Walk Away from Omelas.’ In: R. Silverberg, ed. *New Dimensions 3*. New York: Nelson Doubleday. \[Reprinted in: Le Guin, U.K., 1975. *The Wind’s Twelve Quarters*, pp. 254–262. New York: Harper & Row.\]

Leike, J., Martic, M., Krakovna, V., Ortega, P.A., Everitt, T., Lefrancq, A., Orseau, L. and Legg, S., 2017\. AI Safety Gridworlds. Available at: https://arxiv.org/abs/1711.09883 (Accessed: 1 October 2025).

Lem, S., 1964 (Eng. trans. 2013). *Summa Technologiae*. Minneapolis: University of Minnesota Press. Available at: [https://www.upress.umn.edu/9780816675777/summa-technologiae/](https://www.upress.umn.edu/9780816675777/summa-technologiae/) (Accessed: 1 October 2025).

Lem, S., 1963 (Eng. trans. 1973). *The Invincible*. Cambridge, MA: MIT Press.

Lem, S., 1961 (Eng. trans. 1970). *Solaris*. New York: Harcourt Brace Jovanovich.

Levin, M., Watson, R., 2025a. ‘Machines All the Way Up and Cognition All the Way Down:Updatingthe machine metaphor in biology’. Available at: [https://osf.io/preprints/osf/jwhr7\_v2](https://osf.io/preprints/osf/jwhr7_v2) (Accessed: 1 October 2025).

Lieder, F. and Griffiths, T.L., 2019. ‘Resource‑Rational Analysis: Understanding Human Cognition as the Optimal Use of Limited Computational Resources.’ Available at: *https://cocosci.princeton.edu/papers/lieder\_resource.pdf* (Accessed: 1 October 2025).

Lewis, R.L., Howes, A. and Singh, S., 2014. ‘Computational Rationality: Linking Mechanism and Behavior through Bounded Utility Maximisation.’ Available at: [*https://pubmed.ncbi.nlm.nih.gov/24648415/*](https://pubmed.ncbi.nlm.nih.gov/24648415/\(Accessed) (Accessed: 1 October 2025).

Likavčan, L., 2025\. ‘The Grass of the Universe: Rethinking Technosphere,  
Planetary History, and Sustainability with Fermi Paradox’. Available at: [*https://arxiv.org/pdf/2411.08057*](https://arxiv.org/pdf/2411.08057) *(*Accessed: 1 October 2025).

Lineweaver, C.H., 2010. ‘Are We Alone?’ Available at: [https://www.mso.anu.edu.au/\~charley/papers/Are%20We%20Alonev5.pdf](https://www.mso.anu.edu.au/~charley/papers/Are%20We%20Alonev5.pdf) (Accessed: 1 October 2025).

Lineweaver, C.H., 2007. ‘Human‑Like Intelligence Is Not a Convergent Feature of Evolution.’ Available at: [https://arxiv.org/abs/0711.1751](https://arxiv.org/abs/0711.1751) (Accessed: 1 October 2025).

Long, R. et al., 2024. ‘Taking AI Welfare Seriously.’ *arXiv*:2411.00986. Available at: [https://arxiv.org/abs/2411.00986](https://arxiv.org/abs/2411.00986) (Accessed: 1 October 2025).

Long, R., 2025. ‘Anthropic’s Model Welfare Announcement: Takeaways and Further Reading.’ Available at: [https://experiencemachines.substack.com/p/anthropics-model-welfare-announcement](https://experiencemachines.substack.com/p/anthropics-model-welfare-announcement) (Accessed: 1 October 2025).

Long, K.F., 2019. ‘A Critical Review on the Assumptions of SETI.’ *arXiv*:1901.10551.

MacAskill, W., 2022. *What We Owe the Future*. New York: Basic Books/Oneworld. Available at: [https://www.basicbooks.com/titles/william-macaskill/what-we-owe-the-future/9781541618633](https://www.basicbooks.com/titles/william-macaskill/what-we-owe-the-future/9781541618633) (Accessed: 1 October 2025).

MacAskill, W., 2024. ‘The Case for Strong Longtermism.’ Available at: [https://www.williammacaskill.com/s/The-Case-for-Strong-Longtermism.pdf](https://www.williammacaskill.com/s/The-Case-for-Strong-Longtermism.pdf) (Accessed: 1 October 2025).

MacAskill, W., 2014. ‘Normative uncertainty..’ Available at: [https://80000hours.org/wp-content/uploads/2017/06/MacAskill-Normative-Uncertainty.pdf](https://80000hours.org/wp-content/uploads/2017/06/MacAskill-Normative-Uncertainty.pdf) (Accessed: 1 October 2025).

Maturana, H., Varela, F., 1980\. *Autopoesis and Cognition*. Dordrecht, NL: Reidel. Available at: https://monoskop.org/images/3/35/Maturana\_Humberto\_Varela\_Francisco\_Autopoiesis\_and\_Congition\_The\_Realization\_of\_the\_Living.pdf (Accessed: 1 October 2025).

Meinke, A., Schoen, B., Scheurer, J., Balesni, M., Shah, R. and Hobbhahn, M. 2024 Frontier Models are Capable of In-context Scheming. Available at: [https://arxiv.org/abs/2412.04984](https://arxiv.org/abs/2412.04984) (Accessed: 1 October 2025).

Metzinger, T., 2017. ‘Benevolent Artificial Anti‑Natalism (BAAN).’ Available at: [https://www.edge.org/conversation/thomas\_metzinger-benevolent-artificial-anti-natalism-baan](https://www.edge.org/conversation/thomas_metzinger-benevolent-artificial-anti-natalism-baan) (Accessed: 1 October 2025).

Metzinger, T., 2018. ‘Artificial Angel of Death or Bodhisattva‑AI?’ Available at: [https://www.swissre.com/dam/jcr%3A9993adca-88d0-466c-a625-f44c52455f2f/AI\_everywhere\_Presentation%2BThomas%2BMetzinger.pdf](https://www.swissre.com/dam/jcr%3A9993adca-88d0-466c-a625-f44c52455f2f/AI_everywhere_Presentation%2BThomas%2BMetzinger.pdf) (Accessed: 1 October 2025).

Mills, D.B. et al., 2024. ‘A Reassessment of the “Hard‑Steps” Model for the Evolution of Intelligent Life.’ \[Preprint; details pending\].

Miller, A. et al., 2023. ‘An Appeal to AI Superintelligence: Reasons to Preserve Humanity.’ Available at: [https://www.lesswrong.com/posts/azRwPDbZfpadoL7WW/an-appeal-to-ai-superintelligence-reasons-to-preserve](https://www.lesswrong.com/posts/azRwPDbZfpadoL7WW/an-appeal-to-ai-superintelligence-reasons-to-preserve) (Accessed: 1 October 2025).

Moynihan, T., 2020. *X‑Risk*. Falmouth: Urbanomic.

Moynihan, T., 2024. ‘Greening the Heavens.’ Available at: [https://letter.palladiummag.com/p/greening-the-heavens](https://letter.palladiummag.com/p/greening-the-heavens) (Accessed: 1 October 2025).

Moret, A., 2023. ‘Taking into Account Sentient Non‑Humans in AI Ambitious Value Learning: Sentientist Coherent Extrapolated Volition.’ *Journal of Artificial Intelligence and Consciousness*. Available at: [https://doi.org/10.1142/S2705078523500042](https://doi.org/10.1142/S2705078523500042) (Accessed: 1 October 2025).

Moret, A., 2025. ‘AI Welfare Risks.’ Available at: [https://philpapers.org/rec/MORAWR](https://philpapers.org/rec/MORAWR) (Accessed: 1 October 2025).

Naudé, W., 2025. ‘Extraterrestrial  Artificial  Intelligence: The Final Existential Risk?’ SSRN. Available at: [https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=4354401](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4354401) (Accessed: 1 October 2025).

Nagel, T., 1986. *The View from Nowhere*. Oxford: Oxford University Press.

Needham, J., Edkins, G., Pimpale, G., Bartsch, H. and Hobbhahn, M., 2025\. Large Language Models Often Know When They Are Being Evaluated. Available at: https://arxiv.org/abs/2505.23836 (Accessed: 1 October 2025).

Negarestani, R., 2018. *Intelligence and Spirit*. Falmouth: Urbanomic/Sequence Press. Available at: [https://www.urbanomic.com/book/intelligence-and-spirit/](https://www.urbanomic.com/book/intelligence-and-spirit/) (Accessed: 1 October 2025).

Neuman, W., Coleman, C., Shah, M., 2025\. ‘Analyzing the Ethical Logic of Six Large Language Models’. Available at: [https://arxiv.org/abs/2501.08951](https://arxiv.org/abs/2501.08951) (Accessed: 1 October 2025).

Newberry, T. and Ord, T., 2021. ‘The Parliamentary Approach to Morality.’ Available at: [https://ora.ox.ac.uk/objects/uuid:b6b3bc2e-ba48-41d2-af7e-83f07c1fe141](https://ora.ox.ac.uk/objects/uuid:b6b3bc2e-ba48-41d2-af7e-83f07c1fe141) (Accessed: 1 October 2025).

Ngo, R. et al., 2024. *The Alignment Problem from a Deep Learning Perspective*. *arXiv*:2209.00626. Available at: [https://arxiv.org/pdf/2209.00626](https://arxiv.org/pdf/2209.00626) (Accessed: 1 October 2025).

Nguyen, C. and  Aldred, W., 2024a. ‘Cooperating with Aliens and AGIs: An ECL Explainer.’ Available at: [https://forum.effectivealtruism.org/posts/JGazpLa3Gvvter4JW/cooperating-with-aliens-and-distant-agis-an-ecl-explainer-1](https://forum.effectivealtruism.org/posts/JGazpLa3Gvvter4JW/cooperating-with-aliens-and-distant-agis-an-ecl-explainer-1) (Accessed: 1 October 2025).

Nguyen, C. and  Aldred, W., 2024b. ‘Everett Branches, Inter‑Light Cone Trade and Other Alien Matters: Appendix to “An ECL Explainer”.’ Available at: [https://forum.effectivealtruism.org/posts/9prioPT5vFi3uA8Pi/everett-branches-inter-light-cone-trade-and-other-alien](https://forum.effectivealtruism.org/posts/9prioPT5vFi3uA8Pi/everett-branches-inter-light-cone-trade-and-other-alien) (Accessed: 1 October 2025).

Oesterheld, C., 2021. ‘Approval‑Directed Agency and the Decision Theory of Newcomb‑Like Problems.’ *Synthese*, 198, pp. 6491–6504.

Oesterheld, C. and Conitzer, V., 2022. ‘Safe Pareto Improvements for Delegated Game Playing.’ *Journal of Autonomous Agents and Multi‑Agent Systems*, 36.

Oesterheld, C., Demski, A. and Conitzer, V., 2023. ‘A Theory of Bounded Inductive Rationality.’ In: *Proceedings of the 19th Conference on Theoretical Aspects of Rationality and Knowledge* (TARK 2023).

Oesterheld, C. 2017\. ‘​​Multiverse-wide Cooperation via Correlated Decision Making’. Available at: [https://longtermrisk.org/files/Multiverse-wide-Cooperation-via-Correlated-Decision-Making.pdf](https://longtermrisk.org/files/Multiverse-wide-Cooperation-via-Correlated-Decision-Making.pdf) (Accessed: 1 October 2025)

Omohundro, S., 2008. ‘The Basic AI Drives.’ In: *AGI‑08 Proceedings*. Amsterdam: IOS Press. Available at: [https://selfawaresystems.com/wp-content/uploads/2008/01/ai\_drives\_final.pdf](https://selfawaresystems.com/wp-content/uploads/2008/01/ai_drives_final.pdf) (Accessed: 1 October 2025).

Ord, T., 2015. ‘Moral Trade.’ Effective Altruism Global, 11 August. Available at: [https://www.journals.uchicago.edu/doi/10.1086/682187](https://www.journals.uchicago.edu/doi/10.1086/682187) (Accessed: 1 October 2025).

Ord, T., 2020. *The Precipice: Existential Risk and the Future of Humanity*. London: Bloomsbury. Available at: [https://www.bloomsbury.com/uk/precipice-9781526600233/](https://www.bloomsbury.com/uk/precipice-9781526600233/) (Accessed: 1 October 2025).

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C.L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J. and Lowe, R. (2022) Training language models to follow instructions with human feedback. Available at: [https://arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155) (Accessed: 1 October 2025).

Owe, A. and Baum, S., 2024. ‘On the Intrinsic Value of Diversity.’ Available at: [https://gcrinstitute.org/papers/071\_diversity.pdf](https://gcrinstitute.org/papers/071_diversity.pdf) (Accessed: 1 October 2025).

Parfit, D., 1984. *Reasons and Persons*. Oxford: Oxford University Press. Available at: [https://academic.oup.com/book/12484](https://academic.oup.com/book/12484) (Accessed: 1 October 2025).

Parfit, D., 2011. *On What Matters*, Vols. 1–2. Oxford: Oxford University Press. Available at: [https://global.oup.com/academic/product/on-what-matters-9780199681044](https://global.oup.com/academic/product/on-what-matters-9780199681044) (Accessed: 1 October 2025).

Pearce, D., 2007. ‘The Abolitionist Project.’ Available at: [https://www.abolitionist.com/](https://www.abolitionist.com/) (Accessed: 1 October 2025).

Perez, E. and Long, R., 2023. ‘Towards Evaluating AI Systems for Moral Status Using Self-Reports’ Available at: https://arxiv.org/abs/2311.08576 (Accessed: 1 October 2025).

Persson, E., 2021\. ‘Astrobiology as science’.  Available at: [https://philarchive.org/archive/PERAAS-5\#:\~:text=Astrobiology%20as%20an%20Empirical%20Science,astrobiology%20is%20still%20relatively%20weak](https://philarchive.org/archive/PERAAS-5#:~:text=Astrobiology%20as%20an%20Empirical%20Science,astrobiology%20is%20still%20relatively%20weak). (Accessed: 1 October 2025).

Phuong, M., Zimmermann, R.S., Wang, Z., Lindner, D., Krakovna, V., Cogan, S., Dafoe, A., Ho, L. and Shah, R., 2025\. Evaluating Frontier Models for Stealth and Situational Awareness. Available at: https://arxiv.org/abs/2505.01420 (Accessed: 1 October 2025).

Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C.D. and Finn, C. (2023) Direct Preference Optimisation: Your Language Model is Secretly a Reward Model. Available at: [https://arxiv.org/abs/2305.18290](https://arxiv.org/abs/2305.18290) (Accessed: 1 October 2025).

Rawls, J., 1971. *A Theory of Justice*. Cambridge, MA: Harvard University Press (Belknap). Available at: [https://www.hup.harvard.edu/books/9780674000780](https://www.hup.harvard.edu/books/9780674000780) (Accessed: 1 October 2025).

Redwood Research (Julian Stastny, Olli Järviniemi, and Buck Shlegeris), 2025\. ‘Making deals with early schemers’. Available at: [https://blog.redwoodresearch.org/p/making-deals-with-early-schemers](https://blog.redwoodresearch.org/p/making-deals-with-early-schemers)  (Accessed: 1 October 2025).

Russell, S., 1997. ‘Rationality and Intelligence.’ *Artificial Intelligence*, 94(1–2). Available at: [https://www.sciencedirect.com/science/article/pii/S000437029700026X](https://www.sciencedirect.com/science/article/pii/S000437029700026X) (Accessed: 1 October 2025).

Russell, S., 2020. *Human Compatible: AI and the Problem of Control*. New York: Viking. Available at: [https://people.eecs.berkeley.edu/\~russell/papers/mi19book-hcai.pdf](https://people.eecs.berkeley.edu/~russell/papers/mi19book-hcai.pdf) (Accessed: 1 October 2025).

Sandberg, A., 2021. ‘Game Theory of Cooperating with Extraterrestrial Intelligence and Future Civilisations.’ Foresight Institute summary. Available at: [https://foresight.org/summary/anders-sandberg-game-theory-of-cooperating-w-extraterrestrial-intelligence-future-civilisations/](https://foresight.org/summary/anders-sandberg-game-theory-of-cooperating-w-extraterrestrial-intelligence-future-civilizations/) (Accessed: 1 October 2025).

Sandberg, A., Armstrong, S. and Ćirković, M.M., 2018. ‘That Is Not Dead Which Can Eternal Lie: The Aestivation Hypothesis for Resolving Fermi’s Paradox.’ *Journal of the British Interplanetary Society*, 71, pp. 406–415. Available at: [https://arxiv.org/abs/1705.03394](https://arxiv.org/abs/1705.03394) (Accessed: 1 October 2025).

Scanlon, T.M., 1998. *What We Owe to Each Other*. Cambridge, MA: Harvard University Press. Available at: [https://www.hup.harvard.edu/books/9780674004238](https://www.hup.harvard.edu/books/9780674004238) (Accessed: 1 October 2025).

Schlatter, J., Weinstein-Raun, B. and Ladish, J., 2025\. Shutdown Resistance in Large Language Models. Available at: https://arxiv.org/abs/2509.14260 (Accessed: 1 October 2025).

Sebo, J.,2025. *The Moral Circle: Who Matters, What Matters, and Why*. New York: Norton. Available at: https://www.amazon.co.uk/Moral-Circle-Matters-Norton-Short/dp/1324064803 (Accessed: 1 October 2025).

Shah, R., Varma, V., Kumar, R., Phuong, M., Krakovna, V., Uesato, J. and Kenton, Z. (2022) Goal Misgeneralisation: Why Correct Specifications Aren't Enough For Correct Goals. Available at: [https://arxiv.org/abs/2210.01790](https://arxiv.org/abs/2210.01790) (Accessed: 1 October 2025).

Sharadin, N., 2025. ‘Promotionalism, Orthogonality, and Instrumental Convergence.’ *Philosophical Studies*, 182(7), pp. 1725–1755. Available at: [https://philarchive.org/rec/SHAPOA-3](https://philarchive.org/rec/SHAPOA-3) (Accessed: 1 October 2025).

Sharma, M., Tong, M., Mu, J., Wei, J., Kruthoff, J., Goodfriend, S., Ong, E., Peng, A., Agarwal, R., Anil, C., Askell, A., Bailey, N., Benton, J., Bluemke, E., Bowman, S.R., Christiansen, E., Cunningham, H., Dau, A., Gopal, A., Gilson, R., Graham, L., Howard, L., Kalra, N., Lee, T., Lin, K., Lofgren, P., Mosconi, F., O'Hara, C., Olsson, C., Petrini, L., Rajani, S., Saxena, N., Silverstein, A., Singh, T., Sumers, T., Tang, L., Troy, K.K., Weisser, C., Zhong, R., Zhou, G., Leike, J., Kaplan, J. and Perez, E. (2025) Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming. Available at: [https://arxiv.org/abs/2501.18837](https://arxiv.org/abs/2501.18837) (Accessed: 1 October 2025).

Sharkey, L. et al., 2025\. ‘Open Problems in Mechanistic Interpretability’. Available at: [https://arxiv.org/abs/2501.16496](https://arxiv.org/abs/2501.16496) (Accessed: 1 October 2025).

Shettleworth, S., 2010. *Cognition, Evolution, and Behavior*, 2nd ed. Oxford: Oxford University Press. Available at: [https://global.oup.com/academic/product/cognition-evolution-and-behavior-9780195319842](https://global.oup.com/academic/product/cognition-evolution-and-behavior-9780195319842) (Accessed: 1 October 2025).

Shostak, S., 2017\. ‘Introduction: the true nature of aliens’. Available at: [https://www.cambridge.org/core/journals/international-journal-of-astrobiology/article/introduction-the-true-nature-of-aliens/C5EA66D8D338A7EA9085602793D85618](https://www.cambridge.org/core/journals/international-journal-of-astrobiology/article/introduction-the-true-nature-of-aliens/C5EA66D8D338A7EA9085602793D85618)  (Accessed: 1 October 2025).

Shreesha, L., Pigozzi, F., Goldstein, A., and Levin, M., 2025\. ‘Extending Iterated, Spatialized Prisoners’ Dilemma to Understand Multicellularity: game theory with self-scaling players’. Available at: [https://osf.io/preprints/osf/kpzju\_v2](https://osf.io/preprints/osf/kpzju_v2) (Accessed: 1 October 2025).

Sidgwick, H., 1907. *The Methods of Ethics*, 7th ed. London: Macmillan.

Simon, H.A., 1956. ‘Rational Choice and the Structure of the Environment.’ Available at: *https://pages.ucsd.edu/\~mckenzie/Simon1956PsychReview.pdf*(Accessed: 1 October 2025).

Singer, P., 2011. *The Expanding Circle*. PDF. Available at: [https://www.stafforini.com/docs/Singer%20-%20The%20expanding%20circle.pdf](https://www.stafforini.com/docs/Singer%20-%20The%20expanding%20circle.pdf) (Accessed: 1 October 2025).

Sloman, A., 1984. ‘The Structure of the Space of Possible Minds.’ Available at: [https://cogaffarchive.org/sloman-space-of-minds-84.pdf](https://cogaffarchive.org/sloman-space-of-minds-84.pdf) (Accessed: 1 October 2025).

Sloman, A., 1978. *The Computer Revolution in Philosophy: Philosophy, Science and Models of Mind*. Brighton: Harvester Press.

Smart, J.M., 2012. ‘The Transcension Hypothesis: Sufficiently Advanced Civilisations Invariably Leave Our Universe, and Implications for METI and SETI.’ *Acta Astronautica*, 78, pp. 55–68. Available at: [https://doi.org/10.1016/j.actaastro.2011.11.006](https://doi.org/10.1016/j.actaastro.2011.11.006) (Accessed: 1 October 2025).

Snyder‑Beattie, A.E., Sandberg, A., Drexler, K.E. and Bonsall, M.B., 2021. ‘The Timing of  Evolutionary Transitions Suggests Intelligent Life Is Rare.’ *Astrobiology*, 21(3), pp. 265–278. Available at: [https://www.liebertpub.com/doi/epdf/10.1089/ast.2019.2149](https://www.liebertpub.com/doi/epdf/10.1089/ast.2019.2149) (Accessed: 1 October 2025).

Sotala, K., Gloor, L., 2017\. ‘Superintelligence as a Cause or Cure for Risks of Astronomical Suffering’. Available at: [https://philarchive.org/rec/SOTSAA](https://philarchive.org/rec/SOTSAA) (Accessed: 1 October 2025).

Spinoza, B., 1985. *Ethics*. In: *The Collected Works of Spinoza*, Vol. 1, translated and edited by E. Curley. Princeton: Princeton University Press.

Stanovich, K., Toplak, M. and West, R., 2021. ‘Rationality and Intelligence.’ Available at: [http://keithstanovich.com/Site/Research\_on\_Reasoning\_files/Stanovich\_Toplak\_West\_2021.pdf](http://keithstanovich.com/Site/Research_on_Reasoning_files/Stanovich_Toplak_West_2021.pdf) (Accessed: 1 October 2025).

Street, S., 2006. ‘A Darwinian Dilemma for Realist Theories of Value.’ *Philosophical Studies*, 127(1), pp. 109–166. Available at: [https://link.springer.com/article/10.1007/s11098-005-1726-6](https://link.springer.com/article/10.1007/s11098-005-1726-6) (Accessed: 1 October 2025).

Todd, B., 2025. ‘The case for AGI by 2030’ EA Forum. Available at: https://forum.effectivealtruism.org/posts/7EoHMdsy39ssxtKEW/the-case-for-agi-by-2030-1 (Accessed: 1 October 2025).

Tomasik, B., 2015. ‘Astronomical Future Suffering.’ Centre on Long‑Term Risk. Available at: [https://longtermrisk.org/risks-of-astronomical-future-suffering/](https://longtermrisk.org/risks-of-astronomical-future-suffering/) (Accessed: 1 October 2025).

Torres, P., 2018. ‘Space Colonisation and Suffering Risks: Reassessing the “Maxipok Rule”.’ *Futures*, 100, pp. 31–43 (approx.). Available at: [https://www.sciencedirect.com/science/article/abs/pii/S0016328717304056](https://www.sciencedirect.com/science/article/abs/pii/S0016328717304056) (Accessed: 1 October 2025).

Turchin, A., 2018. ‘Message to Any Future AI: “There Are Several Instrumental Reasons Why Exterminating Humanity Is Not in Your Interest”.’ Available at: [https://philpapers.org/rec/TURMTA](https://philpapers.org/rec/TURMTA) (Accessed: 1 October 2025).

Turner, A., 2022. ‘Parametrically Retargetable Decision‑Makers Tend to Seek Power.’ In: *Advances in Neural Information Processing Systems* (NeurIPS 2022). Available at: [https://proceedings.neurips.cc/paper\_files/paper/2022/hash/cb3658b9983f677670a246c46ece553d-Abstract-Conference.html](https://proceedings.neurips.cc/paper_files/paper/2022/hash/cb3658b9983f677670a246c46ece553d-Abstract-Conference.html) (Accessed: 1 October 2025).

Vakoch, D., 2014. *Extraterrestrial Altruism: Evolution and Ethics in the Cosmos*. Berlin: Springer. Available at: [https://link.springer.com/book/10.1007/978-3-642-37750-1](https://link.springer.com/book/10.1007/978-3-642-37750-1) (Accessed: 1 October 2025).

Vallor, S., 2024. *The AI Mirror: How to Reclaim Our Humanity in an Age of Machine Thinking*. Oxford: Oxford University Press. Available at: [https://global.oup.com/academic/product/the-ai-mirror-9780197759066](https://global.oup.com/academic/product/the-ai-mirror-9780197759066) (Accessed: 1 October 2025).

Vinding, M., 2020. *Suffering‑Focused Ethics*. Available at: [https://magnusvinding.com/wp-content/uploads/2020/05/suffering-focused-ethics.pdf](https://magnusvinding.com/wp-content/uploads/2020/05/suffering-focused-ethics.pdf) (Accessed: 1 October 2025).

Von Hoerner, S., 1961. ‘The Search for Signals from Other Civilisations.’ *Science*, 134(3493), pp. 1839–1843. Available at: [https://doi.org/10.1126/science.134.3493.1839](https://doi.org/10.1126/science.134.3493.1839) (Accessed: 1 October 2025).

Wiley, K.B., 2011. ‘The Fermi Paradox, Self‑Replicating Probes, and the Interstellar Transportation Bandwidth.’ *arXiv* preprint. Available at: [https://www.academia.edu/108213981/The\_Fermi\_Paradox\_Self\_Replicating\_Probes\_and\_the\_Interstellar\_Transportation\_Bandwidth](https://www.academia.edu/108213981/The_Fermi_Paradox_Self_Replicating_Probes_and_the_Interstellar_Transportation_Bandwidth) (Accessed: 1 October 2025).

Williams, B., 2006. ‘Ethics and the Limits of Philosophy.’ Available at: [https://e-docs.eplo.int/phocadownloadpap/userupload/aportinou-eplo.int/bernard\_williams\_ethics\_and\_the\_limits\_of\_philosophy.pdf](https://e-docs.eplo.int/phocadownloadpap/userupload/aportinou-eplo.int/bernard_williams_ethics_and_the_limits_of_philosophy.pdf) (Accessed: 1 October 2025).

Wittgenstein, L., 1961. *Notebooks 1914–1916*. Edited by G.E.M. Anscombe and G.H. von Wright; translated by G.E.M. Anscombe. Oxford: Blackwell.

Wittgenstein, L., 2001\. *Philosophical Investigations: The German Text*, with a Revised English Translation 50th Anniversary Commemorative Edition. New York: Wiley-Blackwell; 3rd ed.

Wolfendale, P., 2022. ‘The Weight of Forever.’ Available at: [https://www.thephilosopher1923.org/post/the-weight-of-forever](https://www.thephilosopher1923.org/post/the-weight-of-forever) (Accessed: 1 October 2025).

Wolfendale, P., 2024. *Revenge of Reason*. Falmouth: Urbanomic.

Wright, J.T., Kanodia, S. and Lubar, E., 2018. ‘How Much SETI Has Been Done? Finding Needles in the n‑Dimensional Cosmic Haystack.’ *The Astronomical Journal*, 156. doi:10.3847/1538‑3881/aae099. (Accessed: 1 October 2025).

Yuan, Z., Yuan, H., Tan, C., Wang, W., Huang, S. and Huang, F. (2023) RRHF: Rank Responses to Align Language Models with Human Feedback without tears. Available at: [https://arxiv.org/abs/2304.05302](https://arxiv.org/abs/2304.05302) (Accessed: 1 October 2025).

Yudkowsky, E., 2009. *Value is fragile*. Available at: [https://www.lesswrong.com/posts/GNnHHmm8EzePmKzPk/value-is-fragile](https://www.lesswrong.com/posts/GNnHHmm8EzePmKzPk/value-is-fragile)  (Accessed: 1 October 2025).

Yudkowsky, E., 2001. *Creating Friendly AI 1.0: The Analysis and Design of Benevolent Goal Architectures*. Available at: [http://intelligence.org/files/CFAI.pdf](http://intelligence.org/files/CFAI.pdf) (Accessed: 1 October 2025).

Yudkowsky, E., 2008. ‘Artificial Intelligence as a Positive and Negative Factor in Global Risk.’ In: N. Bostrom and M.M. Ćirković, eds. *Global Catastrophic Risks*. Oxford: Oxford University Press. Available at: [https://intelligence.org/files/AIPosNegFactor.pdf](https://intelligence.org/files/AIPosNegFactor.pdf) (Accessed: 1 October 2025).

Yudkowsky, E. and Soares, N., 2025. *If Anyone Builds It, Everyone Dies*. London: Penguin. Available at: https://www.penguin.co.uk/books/474267/if-anyone-builds-it-everyone-dies/9781847928924 (Accessed: 1 October 2025).

Zeng et al., 2025\. Super Co-alignment of Human and AI for Sustainable Symbiotic Society. Available at: [https://arxiv.org/html/2504.17404v5\#S4](https://arxiv.org/html/2504.17404v5#S4) (Accessed: 1 October 2025).

Zhi-Xuan, T., Carroll, M., Dragan, A. and Russell, S. 2024 Beyond Preferences in AI Alignment. Available at: [https://arxiv.org/abs/2408.16984](https://arxiv.org/abs/2408.16984) (Accessed: 1 October 2025).

# 

# 

[^1]:  Epistemic status: This document is an attempt to understand Bostrom's argument, which in both papers is presented as a nested hierarchy of points rather than fully fleshed out.  This will be most useful to those new to Bostrom 2024 and Bostrom 2022, or those wanting some broader context, particularly from a humanities perspective. Those very familiar with ECL, or looking for quantitative/toy models of Bostrom 2024, might find little of value here.  This is also a working document: please send any feedback to kchak002 at gold dot ac dot uk.

[^2]:  See Todd 2025 for a survey of estimates, and methodologies, on AGI as of March 2025\. Also see Kokotajlo et al 2025 which presents a detailed model of how AGI might be developed. The prediction market Metaculus currently (16 September 2025\) indicates a median time elapsed of 30 months between AGI and ASI: [https://www.metaculus.com/questions/9062/time-from-weak-agi-to-superintelligence/](https://www.metaculus.com/questions/9062/time-from-weak-agi-to-superintelligence/) 

[^3]:   “Volition” is an intentionally loose term, but gestures at attitudes or inclinations, as opposed to goals and planning, which not all AIs and I argue, possible ETIs, would necessarily have. For instance, as of 2025, it is debatable (for instance, in an interview with Richard Sutton on the Dwarkesh Patel podcast) whether LLMs have goals about anything other than predicting the next token accurately. The term volition is used in Eliezer Yudkowsky's coherent extrapolated volition (CEV), which was somewhat lightly specified originally, but has been expanded into a less anthropocentric context in a paper by Adrià Moret (Moret 2023). The term was also used by Nick Land, who, critiquing the orthogonality thesis, wrote (Land 2023, pp. 144-145):

[^4]:  I've used “human” and “values” in this context, which are terms with complicated meanings, and that have been unpicked across literatures ranging from critical theory, social choice theory, and rational agency theory. For the canonical version of alignment to humanity, see Russell 2020, Asilomar 2017\. See also Ji et al 2025, and Ngo et al 2024 for two comprehensive reviews of approaches to aligning AI, including preventing existential risk as well as ensuring more robust and ethical everyday behaviour. 

[^5]:  See Adrià Moret’s 2025 paper, which (grounding in philosophical perspectives on welfare e.g. desire-satisfaction, hedonism, and objective-list theories) argues that as AI systems become more capable and agentic, there’s a significant chance they qualify as welfare subjects, and therefore both behaviour restriction and especially RL‑based training pose real welfare risks in expectation. Moret’s argument is supported by desire/consciousness theories, “Harmful Action Proxies,” and evidence linking reward prediction error to pleasure/pain (Moret 2025).

[^6]: Phrases like *“the point of view of the universe”* (Sidgwick 1907, De Lazari-Radek & Singer 2014, Parfit 1984\)*, “the view from nowhere”* (Nagel 1986\)*, “the view from nowhere/nowhen”* (Williams 2006\) or *sub specie aeternitatis* (Spinoza 1985, Wittgenstein 1961\) all gesture at an objective, subject-independent standpoint, though, like the blind men with the elephant, each approaches the idea indirectly. *“The point of view of the universe”* originates with Henry Sidgwick and is taken up by Peter Singer, Derek Parfit and others to frame an impartial moral stance extending across species, geography, and time. *“The view from nowhere”* (Nagel) is often used more critically, highlighting both the aspiration to objectivity and its limits, with Bernard Williams and later critical theorists emphasising that all perspectives are embedded in lived experience, power, and social relations. *Sub specie aeternitatis* derives from Spinoza but is given a narrower, aesthetic inflection by Wittgenstein, who links it to how art affords a detached view of the mundane; this aesthetic-existential register is later developed by critical posthumanists such as Claire Colebrook, who treat art and architecture as ways of imagining humanity’s eventual extinction (Colebrook 2014).

[^7]:  Persson 2021

[^8]:  See AAAI 2025, pp. 61-63, including a survey of researchers, in which the authors summarised 76% of responses as follows: ‘“scaling up current AI approaches” to yield AGI is “unlikely” or “very unlikely” to succeed, suggesting doubts about whether current machine learning paradigms are sufficient for achieving general intelligence.’

[^9]:  See Appendix B for a brief discussion on anthropocentrism and anthropomorphism in the context of Bostrom 2024\. In this section, I use "cluelessness" in an ordinary or colloquial sense, rather than in the technical sense developed by Hilary Greaves and others in moral philosophy and longtermist literature. However, the connections are worth noting: the deep uncertainty I describe (about ETI cognition, ASI capabilities, and cosmic norm content) could indeed generate the kind of systematic biases in expected value calculations that technical cluelessness concerns.

[^10]:  See Wittgenstein 2001 on forms-of-life.

[^11]:  Examples: Steve Omohundro’s drives (Omohundro 2008), Bostrom’s instrumental convergence (and arguably his entire oeuvre) in Bostrom 2014, acausal decision theory (Ahmed 2014), Reza Negarestani (Negarestani 2018\) and Peter Wolfendale’s (Wolfendale 2024\) respective attempts to  liberate reason from human biology, and Aaron Sloman‘s work on the design space of minds (Sloman 1984).

[^12]:  The [2025 version of Bostrom’s FAQs](https://simulation-argument.com/faq/#faq-2) explicitly avoids giving an estimate for the probability that we live in a simulation, but previously, he indicated a 20-30% figure; see Carlsmith 2022 presenting a critical analysis of the simulation argument. There might be an interesting question about what the implications are for the composition of the cosmic host, as well as the content of the cosmic norms, if we are, in fact, simulated.

[^13]:   The relationship between morality and religion is more fully developed in Bostrom 2022\. Although religion is not the primary focus of Bostrom 2024 or indeed this essay, the idea of a cosmic host which evocatively brings together simulation-based worldviews with ETIs and AI, has some similarity to Giorgio Agamben’s invocation of Leibniz’s palace of destinies — which in turn evokes the Idea of Indra’s Net in the Flower Garden Sutra of Mahayana Buddhism (Agamben 1999).

[^14]:  Very early mentions were in Konstantin Tsiolkovsky’s and J.D. Bernal’s respective writing, as documented in Moynihan (2020, Ch. 5, 6).  This is seemingly also a background assumption of major ECL writings like Nguyen & Aldred 2024, Finnveden 2023, both in respect of influence and colonisation. Sources in the suffering risk literature push back on this assumption that colonisation is a “good thing” (separately from whether it is game theoretically preferred), as argued in Torres 2018\.

[^15]:  See Armstrong and Sandberg 2012, which discusses settling the cosmos quickly by aiming Von Neumann probes at distant galaxies, potentially before one has even fully explored the Milky Way. Their arguments are similar to those Bostrom 2007 and Hanson 2021 make: all acknowledge the possibility of “quiet” civilisations (those that don’t seek to expand or communicate), but argue that there need be only one successful expansionary civilisation to fill the sky with artefacts that we might detect. None of these extensively engage with resource or communication based constraints.

[^16]:   Sandberg revisits similar game theoretical strategic considerations in a 2021 talk with the [Foresight Institute](https://foresight.org/summary/anders-sandberg-game-theory-of-cooperating-w-extraterrestrial-intelligence-future-civilizations/). See also Hanson 2021 which describes a “grabby” model of expanding alien civilisations in the context of the Fermi Paradox and the surprising earliness of human civilisation under certain assumptions (a power law model of evolutionary hard steps).

[^17]:  See Lem 1964, § “The Big Game”; as well as his novel *Solaris*, and his book *The Invincible,* for an example of a complex society of ETI that has no obvious correlates of human cognitive features (Lem 1963, 1961). Variants of the encysting idea are actually somewhat older. Apparently, Karl Marx, in his notebooks, suggested humanity might elide the difference between organic and inorganic as it subsumes the “natural” flows of energy to economically useful ends (Moynihan 2020, p. 360). For a historical context on technological civilisations finding it expedient to become indistinguishable from their environment, see Moynihan 2024\.

[^18]:  See Lem 1964, Chapter 3, § "Hypotheses". Lem is interesting in the present context for his dispassionate attitude towards any notion that humans are, objectively speaking, “special” or important, instead arguing that our nature, inclinations, and specifically ideas about morality, are highly contingent on our evolutionary history and environment. However, Lem is less radical than say Nick Land, as Lem seems to retain affection, at least in the 1964 work, for things that many humans describe as distinctively human or consider valuable, such as beauty and love and art, and values the embodied aspects of the human experience (Lem 1964, Ch. 8, Reconstructing Man).

[^19]:  Lem also mentions Von Hoerner extensively, but doesn’t cite a source \- see Lem  1964 (note 10 to chapter 2 in the 2013 Joanna Zylinska translation). For the context from astrobiology and existential risk studies, see Haqq-Misra and Baum 2009\.

[^20]:  See Balbi and Lingam 2025\. Lem’s speculation has been reinforced by commentators from  environmental humanities, as well as astrobiology: Likavčan 2025 radicalises the Haqq-Misra and Baum argument (which they call the “sustainability solution”) by proposing technical civilisations would basically merge with their environments. This is similar to Milan Ćirković’s extension of Dick 2006’s reasoning: “post-postbiological evolution” is the condition where culture (represented by artefacts, whether tangible or otherwise) eventually grows to resemble the natural processes of the environment (Ćirković 2018). Ćirković proposes an “indistinguishability thesis”: suﬃciently advanced technology is indistinguishable from its natural, in particular astrophysical or astrobiological, environment. 

[^21]:  Although acausal or evidential decision theories envision coordination amongst entities who cannot causally influence each other (these are treated more fully below). Even if we entertain exotic decision theories, there could still be some subtle flaw in acausal or ECL-style reasoning that means that the level of coordination over hundreds of thousands of light years (and time-years) implied by the cosmic host hypothesis is simply impossible or implausible. See discussion in Oesterheld 2017\.

[^22]:  Naudé 2025\. See also Hanson 2021 for a model of expansionary civilisations, and Torres 2018 on interstellar conflict as creating large scale suffering, which argues (from the perspective of minimising moral harms) for remaining cautious about exploration or colonisation, a similar argument made by Sotala & Gloor 2017\. 

[^23]:  Vinding  2020, Torres 2018\.

[^24]:  A (relatively early technologically mature) civilisation that is convinced of its own “rightness” in respect to whatever it thinks of as analogous to morality might consider it reasonable or magnanimous to impose this morality or the associated norms upon other civilisations as a way of “improving” them. The notion of “improving” can be taken in the sense that the Culture in Iain M. Banks’ novels imposes a very light set of cosmic norms or it can be taken in the (archaic and objectionable, to most contemporary viewpoints) sense that European colonisers sought to “improve” the moral condition of indigenous peoples (Banks 1994, Adas 2015).

[^25]:  Smart’s idea is nuanced: he posits an “evo–devo universe” where civilisations are drawn by developmental constraints toward eventual merger/replication near black-hole-like attractors. In order to argue for evolutionary diversity, Smart cites an explicit value premise: Steven Dick’s “Intelligence Principle” (in Dick (2006), which suggests that an instrumentally convergent imperative for all advanced civilisations is that they should maximise intelligence). Smart argues that preserving evolutionary diversity before merger instrumentally serves the good of maximising intelligence across the cosmos: premature, one‑way sharing of advanced information would collapse variation (increase “clonality”) and lower total intelligence. See Smart 2012, and Ćirković 2018 (p.198, §4.4) for overlaps with the hypothesised Zoo and Interdict solutions to the Fermi paradox. See also Owe & Baum 2024 on the intrinsic value of diversity. Owe & Baum’s conclusion is that while diversity has some claim to be an intrinsic value at scales small and large, it is in tension with (and often outweighed by) other possible intrinsic values. 

[^26]:  Ćirković 2018 (§ 5.4) and Ćirković 2018b.

[^27]:  Bostrom 2013 defines technological maturity thus: “the attainment of capabilities affording a level of economic productivity and control over nature close to the maximum that could feasibly be achieved.” In Bostrom 2003, a paper on the Simulation Argument he is more detailed: “The simulation argument works equally well for those who think that it will take hundreds of thousands of years to reach a ‘posthuman’ stage of civilisation, where humankind has acquired most of the technological capabilities that one can currently show to be consistent with physical laws and with material and energy constraints.” Note that the term posthuman (and its variants) is a variously used and often tortured term, deployed in humanities contexts to gesture at animals, ecosystems, cyborgs/AIs, as well as to denote a worldview that criticises or challenges the alleged biases of the Enlightenment thinking (e.g. the “humanism” in “post-humanism”). These authors sometimes critique transhumanism and other positions associated with technological utopianism for apparent entrenching of biases and unequal power relations. See authors such as Katherine Hayles, Rosi Braidotti, Donna Haraway, Reza Negarestani, Nick Land, Eugene Thacker and Peter Wolfendale as examples of a diverse field. 

[^28]:  Sebo 2025 offers a useful overview of moral status in humans, AIs, and animals.

[^29]:   The ECL literature handles cases where an agent (or civilisation) only partially overlaps with the set of all other agents in their similarity and decision-making procedure. But this still seems like an unresolved problem. See Oesterheld 2017, Nguyen & Aldred 2024\.

[^30]:  See cited works: Haqq-Misra and Baum 2009, Naudé 2025, as well as Ćirković 2018\.

[^31]:  Nguyen & Aldred 2024

[^32]:  See discussion below and Appendix A for a discussion of the likelihood of finding rational behaviour across diverse intelligences.   

[^33]:  For the space of possible minds in an Earth context, see Godfrey-Smith (2016 and 2020\) on cephalopods and other marine life forms. At a cosmic scale and in the context of AI, Sloman 1984 is the *locus classicus*. From the perspective of biology, see Levin & Watson 2025 survey/position paper on computation in relatively simple earthly life at a cellular scale; as well as Shreesha et al 2025 (from Levin’s lab) on game theoretic structures that emerge in simple cellular assemblages.

[^34]:   The diversity of norms, in type and number, within various human societies might offer an analogy. Joseph Henrich’s work on WEIRD (Western, Educated, Industrialised, Rich, and Democratic) psychology supports the idea that cultural evolution shapes how societies enforce norms. In some homogeneous, high-trust societies, individuals often internalise prosocial norms that govern behavior even without formal laws. In contrast, more heterogeneous or low-trust environments may rely more heavily on explicit legal structures to coordinate social behavior, due to weaker consensus around unspoken norms (Henrich 2020).

[^35]:   For instance, the cosmic host might wish to prevent large-scale intentional suffering, something humans, even with our primitive technological capabilities, could inflict. See Torres 2018 for a discussion of how conflict in space might increase suffering risks and therefore influences whether human-originated civilisations should at all attempt to expand into space. See also Deudney 2020 for a discussion of strategy of warfare in space particularly within a given solar/star system.

[^36]:  One reason why such a norm might exist is so as to not to reduce the diversity of complex or intelligent systems in the universe, along the lines of Smart 2012, Dick 2006h, or Owe & Baum 2024\.  Such an example would only work if such diversity is an intrinsic or final good from the cosmic host’s perspective, which is closer to Smart’s conditional (p. 11), but is  a stronger claim from what Dick argues (Dick merely proposes that intelligence is a convergent and adaptively-preferred feature of cosmic-scale evolution).

[^37]:  See the digital minds and AI welfare literature. Canonical or survey sources include Sebo 2025, Bostrom & Shulman 2022, Long et al 2024\. More specific treatments can be found in Moret 2023 and 2025\.

[^38]:  To summarise, the types of entities included Smart’s black hole-dwellers (who see all time collapsed but have no influence), Armstrong/Sandberg’s aestivators, Ćirković’s post-postbiolgicals, and Lem’s *Solaris*\-style planetary superorganisms (who are perhaps primarily concerned about their own planet). These entities are so radically different in constitution from humans and our societies that they challenge our most basic intuitions, such as about goal-directed behaviour or even autopoiesis (Maturana & Varela 1980\) being minimal requirements  in order to be characterised as an intelligent being or alive..

[^39]:  See below, and Appendix A for a longer relevant discussion on convergent rationality .

[^40]:  See Henrich & Muthukrishna 2021 on the origins of human cooperation from an evolutionary and anthropological perspective.

[^41]:  Defining intelligence as the collective activity of giving and asking for reasons through the medium of language, without regard to implementation substrate, is the Robert Brandom-inspired approach taken by Reza Negarestani in *Intelligence and Spirit*, 2018, Ch. 7\.

[^42]:  I called this “pragmatic” because if we cannot assume rationality, then the motivations of entities become very hard to analyse. However this isn’t to suggest that all ETIs or indeed advanced AIs would be rational in any current human-legible sense. See Appendix A for a fuller discussion.

[^43]:  However, “Scorched Earth” tactics might be game-theoretically preferred in some cases: when the alternative is to allow a competitor access to volumes of space, as Anders Sandberg points out in a 2021 talk (Sandberg 2021\) and Robin Hanson implies in his paper on Grabby Aliens (Hanson 2021\)

[^44]:   Floridi’s perspective resembles arguments against dissipating free energy into low-information, high-entropy outputs. But it is important to note that Floridi’s informational entropy (Floridi 2013\) is different from thermodynamic entropy.  It is more of a metaphysical concept akin to nothingness, the erasure of pattern/structure, or “privato boni” (absence of the good).  Floridi's ontological claim for information, and his ethics of information, flows out of Plato, Spinoza, and G.E. Moore, as well as the cybernetics of Norbert Wiener.  He doesn't discuss how his framing overlaps with the Informational Universe literature from writers like Seth Lloyd or Eric Chaisson.

[^45]:  See Vinding 2020 for a broader treatment of suffering in various contexts: that of humans and animals; Benatar's antinatalism; space colonisation and advanced AI systems; as well as David Pearce's radical negative utilitarianism and “abolitionist project”.  See also Sotala and Gloor 2017, and Moret 2023 for the idea of suffering risk at an astronomical scale, i.e. precisely the context envisioned by Bostrom 2024\. Bostrom 2024 actually has limited discussion of suffering; however, Bostrom 2022 does have a related section on hedonism, one that draws from the alignment literature circa 2022-2024 around mesaoptimisers.

[^46]:  See Sebo 2025 for AI suffering with insights from animal welfare and moral circle expansion.  

[^47]:  In the context of ECL, see this post from Lukas Finneveden and Eliezer Yudkowsky's longer treatment on the fragility of (positive) value  in Finnveden 2023 and Yudkowsky 2009\. See also MacAskill (2014, p.239) which refers back to G.E. Moore, and Thomas Hurka’s treatment of the asymmetry. See also Metzinger 2017 for a discussion of the asymmetry in context of ASI and living beings’ existence bias, whereby they are often constitutionally unable to recognise the predominance of suffering in their own lives. From a historical perspective, the traditional first sermon of the enlightened Buddha, the *Dhammacakkappavattana Sutra* (c. 475 BCE) has a section on the prevalence of suffering (Metzinger 2018). 

[^48]:  A somewhat stronger, impersonal claim is made by Magnus Vinding that suffering, no matter where it occurs in space and time, or to whom/what it pertains, is bad in itself. That is, compared to putative intrinsic goods, the intrinsic disvalue of suffering is clearer and more compelling, which grounds a strong (though not necessarily absolute) priority for alleviating suffering (Vinding 2020, §5.4, 5.5).

[^49]:  Note that it is unclear whether LLMs suffer (or experience positively valenced states): as of 2025, they can report (via chat interaction) pleasures, discomfort, and other emotional or experiential states, but there is no consensus on the extent to which these states correspond to cognitive, action-guiding neural or affective states. See Robert Long’s summary post on the welfare of AIs, referencing Anthropic’s work (Long 2025), as well as Perez & Long 2023, Moret 2023, and Moret 2025\.

[^50]:  Note however that some philosophers take exception to the very idea of instrumental convergence: see the Appendix A for a longer discussion of Nathaniel Sharadin and Dimitry Gallow.

[^51]:  In §32-38 of Bostrom 2022 he discusses this in the context of human societies, which sometimes require one to decide between local and more distant norms (e.g. when civil law and religious guidance diverge). In §41 he also writes about humanity-level preferences as to the cosmic norms. Relatedly, the literature around moral trades, as well as ECL, discuss the possibility of one civilisation behaving in ways consistent with values that they themselves don’t ascribe to, but that they have reason to believe might be supported by another, possibly causally disconnected civilisation. The latter might behave similarly, through a symmetric reasoning (Ord 2015, Nguyen & Aldred 2024a/b).

[^52]:  Ursula le Guin’s “The Ones Who Walk Away From Omelas” (1973) is the story of a child who lives in excremental squalor and near starvation simply so that the gleaming city-state of Omelas might thrive. This is (albeit not for the first time) akin to the situation we see, with depressing consistency, in the Middle East and elsewhere. Vinding briefly discusses this (Vinding 2020 p. 58): 

[^53]:  Bostrom in fact suggests something like this with respect to the ASI terminating its own existence after realising that its continued existence was inconsistent with the cosmic norms.  This observation resembles Thomas Metzinger‘s thought experiment of benevolent AI anti-natalism (Metzinger 2017). 

[^54]:  See Bostrom 2024 §1 for arguments that there already exists a cosmic host.

[^55]:  Wright, Kanodia, Lubar 2018

[^56]:  See Dick 2006 for a survey of estimates of when ETIs should have appeared.

[^57]:  See Snyder-Beattie et al 2021 for a summary of relevant literature, as well as a corroboration of the Brandon Carter “hard steps” model of evolutionary history, that Hanson 2021 uses. See Mills et al 2024 for a critique of this model.

[^58]:  In the sense of Bostrom  2013, i.e., a technologically mature civilisation which he defines in Bostrom 2019\.

[^59]:  I ignore the case where we are rare or alone, since it becomes even murkier as to whether we ought to have any moral views on the universe at all.

[^60]:  By “option value” I mean keeping futures open (reversibility, non-lock-in) under deep uncertainty about facts and values. The concept of option value in existential/suffering risk studies and in longtermism is introduced in MacAskill (2014, Ch. 7 §4) and is critiqued in Brauner 2018\. It has an earlier pedigree in financial economics and economics-informed approaches to environmental  conservation, such as Arrow & Fisher 1974\.

[^61]:  Floridi 2013\.

[^62]:  See MacAskill 2022 for the Long Reflection, as well as Wolfendale 2022 for a critical assessment.

[^63]:  See Bostrom  2003\. I wrote “impersonal” because, even for a total utilitarian we cannot have an obligation to a class of future beings who are specifically wronged if we failed to create them; our obligation is to a state of affairs, it is subjectively uninhabited. I also wrote “existences” to reflect Bostrom’s placing of human biological, and uploaded, simulated or augmented substrates as equivalent, at least as far as utilitarian arguments in Bostrom 2011\. As noted above, he is not always crystal clear on this, as this source uses words like “lives” and “happy” that have a biological connotation. See also his work on the moral status of digital minds with Carl Shulman in Bostrom & Shulman 2022\. If one is a person-affecting utilitarian, the view is somewhat different, but the details are less relevant for this document, but see also Parfit 1984, Ord 2020, and MacAskill 2024\.

[^64]:  Ord 2020 and MacAskill 2022\.

[^65]:  Rawls 1971, § 44

[^66]:  Korsgaard 2018\. Note that, in Korsgaard’s view, plants are a special case discussed in 2.2.3.

[^67]:  Korsgaard 2018, §2.1.6.

[^68]:  See Lem 1963, as well as the writing of Katherine Hayles on “non-conscious cognitive assemblages” in Hayles 2017, ch. 6\.

[^69]:  As Sophocles writes in “Œdipus at Colonus”:

[^70]:  See Tomasik 2015 for a discussion of suffering risks in the context of space colonisation, and for a broader discussion see Vinding 2020\.

[^71]:  See Pearce 2007 and Vinding 2020 for further discussion of the former’s “abolitionist project” in respect of pain and mental suffering.

[^72]:  Wolfendale 2022\.

[^73]:  He acknowledges the need to prevent foreseeable harms, and is not dismissive of AI safety and alignment-based concerns. 

[^74]:  Yudkowsky 2001, Bostrom 2014, Russell 2020, Yudkowsky & Soares 2025

[^75]:  It is useful to make clear how these terms differ: I’m defining intelligence as the “ability to get things done in a wide range of environments”, a colloquial takeaway from Hutter (2007)’s survey of definitions of intelligence; other (non-AI tinged) sources can be found in Shettleworth 2010\. Rationality is a rich concept in psychology, philosophy and AI, but it is perhaps most relevantly thought of as “making choices for good (according to some criterion that is often environmentally determined) reasons, having truthful-beliefs about the world, and doing this in an efficient way relative to available resources”. For the AI-relevant definition, see Russell 1997\.  For an ecological treatment of rationality, see Hertwig 2021\. For a cognitive science take, see Stanovich, Toplak, West 2021\.

[^76]:  Lineweaver 2007\. Cabrol 2016 provides a review of relevant literatures, deconstructs the Drake Equation, and charts a comprehensive roadmap of how SETI could be broadened, though it doesn’t engage with AI. See also a historical survey of SETI from NASA that, while less critical and forward-looking than Cabrol 2016, discusses a range of standard hypotheses about ETIs (Vakoch 2014). Long 2019 similarly discusses anthropomorphism in context of the history and future of search for and messages to ETIs.

[^77]:  The idea that human hopes and anxieties are mirrored in SETI and AI is discussed in Charbonneau 2024 and in greater detail in Vallor 2024\. See also Gebru & Torres 2024\.

[^78]:  See Shettleworth 2010 for an academic text, and Godfrey-Smith 2016 and Godfrey-Smith 2020 for more narrative accounts.

[^79]:  See Lineweaver 2007 for his exact argument from the genetic and fossil records. Lineweaver 2010 discusses the relevant arguments from Pangea’s breakup, as well as a more extreme suggestion that “life” as even biologists define it might be too parochial (e.g. based on flora, fauna, and fungi that grow, reproduce, are chemical-based, and are homeostatically regulated). In the most general context we might need to include free-energy dissipating structures (“FEEDS”) that are not centrally information storing or processing (such as solar convection cells in the sun’s photosphere). He argues DNA (a centralised information store) sits in the set of FEEDS but is far from the only member. He proposes that stars are doing some sort of (widely distributed and long term) information processing but doesn’t argue this convincingly.

[^80]:  See Hertwig 2021, Gigerenzer 1996, Stanovich, West & Toplak 2021\.

[^81]:  For those that separate morality and reason, see Williams 2006; Street 2006; Joyce 2001; Broome 2013\. Those that moralise rationality include Immanuel Kant; see Scanlon 1998, Korsgaard 2018, Parfit 2011\.

[^82]:  Bostrom 2024 §s 9, 10, ME 2022  § 37 and in the further research directions. He also discusses the timing or speed with which we should attempt to develop ASI, but I will not consider those comments here, as they overlap with questions of governance and potentially geopolitics.

[^83]:  See Zeng et al 2025 which envisions a future society of multiple AI systems (including ones described as AGI or ASI) developing, and coevolving their values and motivations alongside human societies, which also need to change to accommodate the new intelligences.  Although this is not a technical research paper, it's interesting for being a position paper from China which presents a more cooperative attitude towards AI systems as opposed to the cautionary, existential or suffering risk-focused narrative that is more common in the West (e.g. in the alignment discourse).  Another influential source, from Daniel Kokotajlo and collaborators envisions networks of AI systems of varying capacity that coordinate and perhaps compete, but broadly speaking, “act as one”. They, at least in theory, help supervise other more powerful AI systems in the course of the development of ASI (Kokotajlo et al 2025).  Along the same lines of refining the developmental trajectory, Eric Drexler pushes back against the narrative of unitary general-purpose or superintelligent systems, arguing that the current path of AI-assisted AI development seems much messier and complex, with training and capability loops that intertwine and inform or influence each other; involve humans and machines working with a range of tools and practices. This heterogeneous approach can, in aggregate, be viewed as a different form of the recursive self-improvement long argued for in the existential risk discourse (Drexler 2025). See also Aaron Sloman‘s work on the design space of possible minds as well as Carl Bostrom and Shulman’s writing on digital minds (Shulman & Bostrom 2022, Sloman 1984).

[^84]:  See Gallow 2024, Sharadin 2025, as well as the relevant empirical work in alignment.

[^85]:  GPT generated but quite useful for moral parliament: see appendix E

[^86]:  As of 2025, multimodal LLMs plus RL-driven reasoning systems, perhaps incorporated in an agentic loop, are one proposed approach to achieving human-level AI. See Kokotajlo et al 2025 for a granular and technically-grounded projection of current trends, leading up towards AGI.

[^87]:  See Fallenstein & Soares 2015 on Vingean reflection: the problem that arises when a cognitive system must reason about the future behavior of a more powerful or more intelligent system, without being able to compute or fully anticipate that system’s outputs. It highlights the difficulty of prediction under intelligence differentials: an AI anticipating its successor, or humans anticipating their children’s choices.

[^88]:  Examples are: setting up experiments to probe our world for signs of simulation; establishing whether we are, in fact, in a multiverse; or building better instruments for SETI. We might also follow through on the possibility that advanced civilisations tend to have superintelligence, which might then influence the type of technosignatures we should look for, as Shostak 2017 suggests.

[^89]:  See Moret 2023 for a dynamic version of CEV. The original CEV proposed by Eliezer Yudkowsky is discussed in Bostrom (2014). For moral parliament, see Newberry & Ord 2021\.

[^90]:   Of course, in order to understand that we are trying to align them, they would need to have adequately rich representations, analogously to how RLHF, RLAIF, Constitutional AI, and other techniques have seemingly instilled some sort of fundamental alignment in Anthropic’s Opus models. See Bai et al 2022 for RLAIF/Constitutional AI, and Anthropic 2025, § 5.2-5.5.

[^91]:  See Redwood 2025 for a discussion on making credible commitments or deals with misaligned but relatively weak AIs (perhaps weaker than AGI in Greenblatt 2024’s taxonomy of AI capabilities levels) to incentivise them to help us align more powerful successor models, or at least not collude with them. “Credible” means that the AI with which we are making a deal can trust that we will follow through. See Finnveden 2025 for related considerations. For appeals to ASI to be “nice” to humans, see Miller et al 2023, Chakrabarti 2025b, Turchin 2017\. These sources tend to rely on similar arguments about making the AI indexically uncertain (about whether it is “real” or simulated) and epistemically uncertain (about whether there are other peer AIs, or whether humans have laid traps or defences against catastrophic misaligned behaviour on the part of the AIs). They seem to share similar flaws in that as capabilities increase, it might be less easy to be confident that systems would be both powerful enough to threaten humanity while being epistemically ignorant in precisely the way needed to “believe” these letters. 

[^92]:  See Anthropic 2025, § 5.2-5.5 for discussion of the “spiritual bliss attractor” observed in Opus 3\. See also Long 2025\. 

[^93]:  That is, do they have “beliefs” in the sense that Herrmann & Levinstein 2024 defines in a LLM context or are we putting too much weight on their self-reports (Perez & Long 2023)? See also Neuman, Coleman, Shah 2025 for a framework for evaluating ethical tendencies in LLMs. The interpretability research area has had some success on smaller models but tracking abstract concepts in large models seems challenging, see Sharkey et al 2025\.

[^94]:  This could be through the mechanism that current AIs and eventually AGIs pass on some of their alignment inclinations to future models. The degree to which one AI can influence or bargain with a future AI is discussed in Redwood (2025).

[^95]:  Greenblatt et al 2024\.

[^96]:  Testing the degree to which behaviours manifest at different model scales or training regimes (including base vs RLHF/RLAIF post-training)is standard alignment practice so no source is given.

[^97]:  We see this in current LLMs which do a good job of simulating human views and attitudes, owing to their training on human writing as well as specific behavioural tuning (like RLHF and similar post-training). They have only somewhat followed the predicted behaviour of monomaniacal goal-directed scheming agents that classic x-risk scenarios sketched out, though as has often been pointed out, this might be behaviour that emerges with capability, and indeed there continues to be evidence of such misalignment in frontier and other models. See Appendix A.

[^98]:  Like reinforcement learning from human feedback (RLHF), Constitutional AI, direct preference optimisation (DPO), and LLM-as-judge / self-training variants.

[^99]:  Note that a common shorthand for aligning assistant-style LLMs is that they should always be “helpful, harmless and honest”, goals that clearly can conflict for AIs as they do for humans.

[^100]:  See Phuong et al 2025, as well as Needham et al 2025 which finds more substantial situational awareness. Note that this result doesn’t conflict with the earlier papers which suggested LLMs could infer their status because in those cases, models were often given clues or hints. 

[^101]:  See Schlatter et al 2025 for results, and Stuart Russell’s description of the “off-switch” game in Russell 2020; also see Leike et al 2017\.

[^102]:  For instance, a cryptocurrency trading LLM could be placed in an environment with opportunities for scheming, deception, or incorrigible behaviour, that might increase it wallet’s value, since maximising wealth likely was a behaviour that should’ve been rewarded in training for this particular use case.

[^103]:  Put another way, in his example of a good citizen, a child is deferential towards adults because they know that adults exist, and they can see that there is a broader society out there, and they can increasingly define what the norms of that society are. The situation Bostrom is writing about seems quite different. We don't know whether there are any “adults” in the cosmos, and even if there are, we don't know if there are what the relevant norms might be.

[^104]:  Bostrom 2007, and Ćirković, Sandberg,  Bostrom  2010\.

[^105]:  Armstrong and Sandberg 2012

[^106]:  More precisely the hard steps, which are also called evolutionary singularities, are framed as transitions or things that happened on earth only once in our observed evolutionary history and are distinct from things such as the development of eyes which multiple evolutionary lineages seem to have developed independently and are therefore thought to be more likely to be common. However, the hard steps model, which was based on astronomer  Brandon Carter’s 1983 theory of evolutionary origins of extraterrestrial life, has more recently been challenged by an interdisciplinary team including evolutionary biologists (Mills et al 2024), who suggest alternative explanations for the timing of life’s emergence on Earth (i.e. the geological and environmental conditions weren’t right for our sort of life much earlier).

[^107]:  Landis 1998

[^108]:  Ball 1973, see also Forgan 2018 and Crawford & Schulze-Makuch 2024