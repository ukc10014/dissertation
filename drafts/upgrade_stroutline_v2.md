---

title: Reasons for Persons, or the Good Successor Problem
date: \today
---

abstract: \noindent Recent advances in AI may have increased the risk of human extinction or disempowerment. However, they have also made tangible our possible evolution into a machine-based species.  Many may feel that a world from which our biological descendants have disappeared would be a worse one, in some irreducible or objective sense.  But what about a world where certain values could be passed on to a superintelligence - values that seem to be convergently present amongst human cultures, such as respect for artistic creativity or for ecological diversity?  Would this still be a terrible outcome, and if so, precisely why?  The topic is controversial and confusing, yet it seems useful to set out the relevant views from philosophy, ecology and astrobiology, as well as conceptual AI. The ambition is to construct a thought experiment that asks why and how humanity's technological successor should carry the torch of intelligence forward throughout our lightcone.


# Structural Outline

These are things I want to cover - other than the first section (Overview) which corresponds to the writing sample required for the upgrade - they do not have a one-to-one correspondence with chapters.

## Chapter 0: Overview (and likely sample writing for the upgrade)

Humanity's future with AI is a [`wicked problem'](https://en.wikipedia.org/wiki/Wicked_problem) with aspects that span technology, existential/suffering risk, public policy, and philosophy.  AI is also discussed in a politically polarised context that complicates object-level issues.  This section sets out the scope and primary concerns of the project.

**Thought experiment**: I site this project as something like a thought-experiment, in that it should be grounded in physically-possible reality; the nature of the topic means that the project also has a speculative element, but again, I hope to maintain the plausibility of hard science fiction.  I also hopt to make explicit any potential is/ought confusions buried in my analysis.

Imagine a (future) world with one or more artificial superintelligence(s) (ASIs) but where biological humans have disappeared (bracketing the precise manner or cause of their disappearence).  

Below are some considerations for how we can we think about this world? [^1]  The completed project will likely focus on certain aspects that there is a) substantial academic (or equivalent) literature on, b) where I believe some contribution can be made, and c) that might be subject to some pratice-based investigation.

[^1]: Note: although this project is not explicitly about (AI-originated) human *extinction*, the distinction/overlap between extinction/evolution is important (see this [post](https://www.lesswrong.com/posts/HaGTQcxqjHPyR9Ju6/unpicking-extinction) for a summary). 

- what might `the shape' (the physical, cognitive, and social organisation) of these ASIs be ([[#^025a15]])?
- what are (some of) the paths from today's AI to ASI ([[#^77220f]])?
- is it meaningful to talk about the proposed world (without humans) having value ([[#^f89d2e]])?
- phrases like 'aligning AI to human values' are used by technologists, politicians, and media figures.  
    - What of humanity's (diverse, complex and fragile) value set would we like to see in our successor species?  
    - Put another way, of the things `we' collectively do today, is there anything we would be sad to find absent in the future I have posited?  
    - What technical issues arise when aggregating values or preferences?
- is it reasonable or justifiable that we should have any opinions at all on what values our much-more-powerful successors have?
- write down a `taxonomy of possible futures': e.g. empty universes/astronomical waste, paperclip/squiggle maximisers, optimisers for hedonium or utilitronium, but also ones that are more obviously positive (from my perspective) ([[#^bd3c7f]])
    - defend (or dismiss) my proposed candidates for human final values: a battle against entropy through created complexity, which in concrete terms means art and perhaps respect for nature's diversity ([[#^bd3c7f]])
- the practice is inherently woven into the research process [[#^c164a6]] and specifically focuses on simulation as both research method and illuminating theoretical grounding ([[#^bd3c7f]])

### Contextualising the project within existing discourse

This project is, by virtue of its topic and the references I use, adjacent to a number of conversations in the critical (post-)humanities.  I note those adjacencies, with a view to completeness, but in most cases do not argue for or against the points raised.

These adjacent conversations include: 
- the critical discourse around post/trans-humanism (e.g. allegations of eugenicism, universalism, technophilia, etc. coming from people like Braidotti, Gebru, Torres, Bender, etc.).  These are valid criticisms but not the principal focus of my project.
- there are obviously concerns about race/gender bias and job loss owing to automation, supposed negative impact on human creativity, etc.  These also are not in-scope.
- the curious re-animation of  accelerationism (via [e/acc](https://en.wikipedia.org/wiki/Effective_accelerationism)) has probably just muddied the waters, and it isn't very clear whether any lasting insight will come out of it - for now it is out-of-scope.
- I have discussed some of these topics in [this post](https://www.lesswrong.com/posts/HaGTQcxqjHPyR9Ju6/unpicking-extinction).




## Chapter 1: From LLMs to superintelligence

^77220f

I think it might be useful to a non-AI specialist reader to clarify jargon (AI, AGI, ASI, HLMI, etc.) and relate current models to more advanced AI that is envisioned in this project.  An early version exists at the [AI Risk Observatory Novacene](http://airo-ne.org/site/home.html).
- why are we talking about ASI (as opposed to human-level or AGI which seem hard enough)?
- rebut the `stochastic parrot' narrative
- draw possible trajectories to ASI from current AI
- host results of my practical research in AI Safety Camp

## Chapter 2: The design space of possible minds

^025a15

What types of minds are possible?  We are familiar with humans, a few animals (pets as well as wild), and now are making the first synthetic, modestly general intelligences.  Yet this probably doesn't exhaust the possibilities for what `shape' (physical and cognitive) intelligence might take, and this in turn may impact things like: how much agency they have, their goals/values, propensity for deception, and alignment with human well-being.[^2]

[^2]: This line of enquiry fell out of my research for this [essay](https://wiki.ljudmila.org/Kanad_Chakrabarti:_After_Interregnum,_Indra%27s_Net), which asked whether an ASI would have reasons to make (anything we recognise as) art.  

More generally, if certain types of minds are inherently deceptive or misaligned (with human interests), this increases the chance of bad outcomes for humanity.  On the other hand, cooperation and norm-following might be game-theoretically correct strategies for sufficiently rational beings (unlike humans or other primates).  This overlaps with [[#^f79d3e]] and [[#^f89d2e]].

This topic was presented in April at [POM Aachen](https://www.pomconference.org/pom-aachen-2024/), in collaboration/consultation with [Anders Sandberg](https://www.ox.ac.uk/news-and-events/find-an-expert/dr-anders-sandberg) at University of Oxford, and will be submitted as a paper.


## Chapter 3: Minds in societies

^f79d3e

Intelligence in human societies is a mostly a phenomenon of culturally-transmitted knowledge accumulated over generations - it would be useful to understand this better and ask whether that might hold for ASI.  This interacts with [[#^025a15]]
- I'm particularly interested in how AIs interact with humans, each other, aliens: decision theory and evolved norms in multi-agent settings [^3]
- studying how AIs interact is experimentally tractable through simulations and fits in well with practice - this has been the main topic I explored at [AI Safety Camp 2024](https://aisafety.camp/previous-camps/), and will be documented [here](http://ukc10014.org/) (probably by June 2024).

[^3]: I suspect decision theory, evolutionary equilibiria, prisoners' dilemnas, etc. are not so well-known outside the rationalist discourse, and it might be valuable to explain it because they might re-frame (as contingent products of particular cultural-evolutionary trajectories that are localised in time and geography) some of the things we think of as uniquely human: `morality', `values', etc. ^2a1f99 ([[#^c164a6]]) 
	


## Chapter 4: The view from nowhere (VFN)

^f89d2e

This (the view-from-nowhere or VFN) is one of the least clear and quagmire-prone elements of the project.

Abstract of the chapter:
Most conceptions of value, at least in the Western Greek-Judeo-Christian tradition, place the human as the site of value and the judge of value.  Consequentialist or utilitarianist systems straightforwardly aim at quantified well-being for people, while deontological and virtue-ethics strains seek a more abstract definition, yet still presuppose the human.  Moral realist views, particularly of the non-naturalist variety, try to set out a realm of moral facts which are not of this (physics-determined) world yet are still accessible through reflection, again by human subjects.

These approaches make sense, or at least have the weight of hundreds or thousands of years of accumulated insight to recommend them and we discard them at our peril.  Yet, they seem inadequate when dealing with other sentient species which do not share our lifeworld or our collective histories (bracketing contemporary views on whether such universals are meaningful or helpful terms).  For instance, how would we explain promise-keeping or truth-telling to a whale, assuming for a moment we could understand its language.  More pertinently, assuming we had an AI highly capable of reasoning - how would we communicate these intuitions which are so grounded in brute facts of our existence?  Why should we expect, on reflection, that these arguments should be convincing, not to mention binding, upon radically different sentient agents? After all, the story of human thought is that convergence on values, if any, is halting and demonstrates contention even amongst humans alive today (and in the past), who share similar biologies.

It may prove impossible to complete eliminate all subjects (even if we assume no humans in this thought experiment); however, by definition, there would be ASI(s).  How can our current notions of subjectivity be extended to include such beings?  Does the literature around animal sentience offer a way?


### Sharing the future with our mind-children

^c85c5f

VFN is important because decisions we make with respect to AI/ASI may need to be justified from a perspective broader than `what is good for a particular group of humans' or even `what is good for humanity'.
- an example that [Joscha Bach](https://joscha.substack.com/) gives: 
    - imagine that we stop building AGI indefinitely, and as a result are ill-prepared to deal with various statistically probable (on a sufficiently long timescale) risks: a pandemic more deadly than COVID-19, population decline, catastrophic war, a major asteroid strike or simply fail to reach technological maturity[^4]
    - it could be argued, that in such a case, we will have wasted part of the cosmic [endowment](https://nickbostrom.com/astronomical/waste) (of low entropy energy), and (depending on one's position on questions of population ethics) committed a grave injustice in respect of future, never-to-be-born generations 
- a more straightforward case is that of `AI shutdown': if we are about to shut down (i.e. kill) an AI that is sentient and morally-valuable, we need to have some justification for this (that is species or substrate-neutral).

[^4]: There are lots of assumptions above (e.g. how confident are we that AGI might help avoid other existential risks versus itself increase existential risk)

### Adjacent perspectives

VFN feels quite close to the discourse around moral realism discourse as well as ideas (e.g. Bach) on complexity-as-value.  It also sounds like things Singer, Wittgenstein, Nagel have argued, but initial reading suggests their contexts were quite different from what I'm interested in.

There might be interesting overlaps with indigenous or non-Western thought (Buddhism/Shinto) or panpsychism, but I'm not anxious to go too deep on this tangent (at least in the dissertation).


## Chapter 5: Propositions upon final goods

^bd3c7f

What might humanity's contribution to value be? What do we do that is valuable in a (VFN) sense, i.e. the universe would be poorer if these didn't exist?
- put another way, what precisely is wrong with a [`paperclip/squiggle maximiser'](https://www.lesswrong.com/tag/squiggle-maximizer-formerly-paperclip-maximizer) (or, for that matter, an optimiser for anything like utilitronium, hedonium, etc.)?
- following Bach, I propose *`created complexity as a way of resisting entropy'* as a major source of VFN value.  Specifically, I think of possible types of complexity: firstly, aesthetic objects or art (subject to an appropriate definition); secondly, the diversity that evolution creates in ecological systems.
    - I have an intuition that art, beauty, and aesthetic reflection might be close to final or terminal goals for humans, and (speculatively) for other advanced intelligences.  Connecting this, via writers like Alva Noe, to such literature as supports Bach's view, could carry substantial weight in this project.
	- this intersects with **practice** in development of my project to get AIs to talk credibly about artwork, discussed as a concept [here](https://tripleampersand.org/work-art-age-cybernetic-criticism/), and as an [artwork](http://ukc10014.org/fixedp.html). See also [[#^0aa37d]]

# Appendices

## Simulation arguments

My intuition is that simulation is a rich thread (as opposed to a distinct chapter) that holds this project together, both in theory and practice. 
- the topic's genesis is AI researcher Paul Christiano's [post](https://ai-alignment.com/sympathizing-with-ai-e11a4bf5ef6e); his argument depends substantially upon simulation (as a way to `test' candidate successor civilisations for their `niceness')
- thinking about simulated worlds has weird implications for [[#^2a1f99]] and [[#^f89d2e]] 
- the possibility that we will soon be simulating agentic intelligences might be anthropic evidence regarding for how `real' our own world is (per the Simulation Argument of [Bostrom](https://simulation-argument.com/))
- as a practical matter, much AI research uses simulations and [my](http://ukc10014.org/exorbp.html) [artistic](http://ukc10014.org/sicul.html) [practice](http://ukc10014.org/islands2.html) and [writing](http://ukc10014.org/writing.html) have long been preoccupied by this topic



## Current state of the project
The breadth of the project's interests has required me to develop a viable approach such that I can say something that both fits within the guidelines of a art practice-based PhD and is legible to the broader alignment community with whom I interact (and who, to a certain extent, are my research sources).

- In April 2024 at the [Politics of the Machine Conference](https://www.pomconference.org/pom-aachen-2024/) at RWTH University (Aachen), I presented a draft of a paper, co-written with Professor Anders Sandberg (University of Oxford) on the `design space of possible minds' ([[#^025a15]])
- In March 2024, I gave a short lecture-video documenting a research collaboration with Jascha Sohl-Dickstein (ex-Google Brain): the fractal nature of learning (the shape of the high-dimenstional loss function of a very simple neural network is visualised and sonified) within AI systems is placed in context of Stanislaw Lem's prescient writing on non-human intelligence, evolution, and the possibility that our norms might be a mere accident of biological and cultural history
- In January 2024, I presented an initial version of [[#^0aa37d]] at Goldsmiths, and documented [here](http://ukc10014.org/fixedp.html)
- From late 2023, an essay that speculating about an ASI's propensity to make art are published [here](https://wiki.ljudmila.org/Kanad_Chakrabarti:_After_Interregnum,_Indra%27s_Net)
- My research practice is heavily integrated with AI models as described in [[#^d958bf]], and in both 2023 and 2024 I have participated in AI Safety Camp, a programme for empirical and theoretical research into AI alignment.  The results are documented [here](https://aisafety.camp/previous-camps/), but 2024's project involved understanding the decision-making procedures and propensity for deception/collusion in current language models.  In 2023, I looked at practical ways of working in human-AI cyborg teams to solve cognitive tasks.
- In December 2023, I considered this project's aims in light of conversations around human extinction, as well as criticisms of post/trans-humanism (see above), written up [here](https://www.lesswrong.com/posts/HaGTQcxqjHPyR9Ju6/unpicking-extinction)


## On practice (artistic and otherwise)

^c164a6

### What constitutes `practice'?

I draw a distinction between practice (as something any scientific researcher does every day, perhaps to help them understand a topic or communicate with peers, and which may be `creative' by any ordinary definition of the term) and artistic practice.  I am doing both in this project, and see both as falling within the 50/50 definition of `practice-based PhD'.

### Models as cyborg research partners

^d958bf

- further to my prior work on [Cyborgism](https://www.lesswrong.com/posts/iFBdEqEogtXcjCPBB/the-compleat-cybornaut) (part of AI Safety Camp, a research initiative I am involved with) I have integrated LLMs deeply into my research, planning, and writing process
- as I document [here](https://www.lesswrong.com/posts/k93NEoXZq6CdXegdx/philosophical-cyborg-part-1), present LLMs aren't great at generating useful (philosophical, artistic, or other qualitative) insight, but I would like to see if any progress can be made here (probably in collaboration with others)

### Future Claimant's Representative

^c11478

- the ideas in [[#^c85c5f]]  are to be presented through a `*ludic essay*' (a film/video essay implemented in a game engine, which may be viewed cinematically or through a VR/AR headset)
- the narrative is inspired by a quasi-legal construction: a representative of unborn/uncreated future generations of sentient beings, who is known as the `future claimant's representative' (abbrev. FCR, originally suggested by Baucom in an ecological context)
- in my rendering of Baucom's idea, the FCR in the ludic essay is a portal or voice that presents the thought experiment that underpins this project

### The dissertation as creative product

- I see the dissertation as existing in multiple formats - a) a static, academic document for Goldsmiths repository (which perhaps might become a future book), and b) an online site that allows for dynamic or self-paced exploration of the topics and integrates non-text elements (such as outputs from [[#^d958bf]] or specific points in [[#^c11478]])
- I have previously explored this, usually as [websites](http://ukc10014.org/media/qm_2018-master/index.html) for [exhibitions](https://ukc10014.github.io/neu/), [stand-alone artefacts](http://airo-ne.org/site/home.html), or [press releases](https://www.artistsallianceinc.org/wp-content/uploads/2020/11/calling@sweeneyshoal_pr_rr_110620.pdf).

### Aesthetics, art-writing, and value

^0aa37d

- I am interested in the capacity of multimodal models (LMMs) like GPT-4V or SORA to examine, deconstruct, and interpret artwork.  I do not expect current models can have a credible subjective aesthetic response (or even what the criteria for determining this might be), but I think there is a lot that we (art-educated human subjects) say about an artwork that is fact-based and effable (i.e. concrete statements that describe a work, draw comparisons with other work, etc.) and should, in theory, be accessible to a model.
- Opinions about art are made in collective or social settings (i.e. are a product of cultural learning and transmission): to what extent can this be replicated and studied in groups of interacting models? 
- I made a proof-of-concept at [Goldsmiths](http://ukc10014.org/fixedp.html) in January 2024 and plan to develop this further
- this line of investigation can be seen as a manifestation of [[#^bd3c7f]] but I also investigate the extent to which models that are fine-tuned for art or aesthetic purposes (i.e. fed the e-flux or comparable corpus of writing)


# Sources

In the interests of brevity, this is a list of names to be replaced by a bibliography.  I have broken the sources out but of course there is much overlap between the buckets.

## Artists
- Stanislaw Lem
- Pierre Huyghe
- Philippe Parreno
- Liam Gillick
- Robert Smithson

## Art theory

I see art theory (plus practice) as being what makes this project legible within an upgrade/viva context, i.e. grounds the project in something that Goldsmiths can evaluate (as opposed to being something better situated in computer science, philosophy, etc.)

- Alva Noe
- Martin Heidegger or writers in his lineage (e.g. Yuk Hui, Giorgio Agamben)
- Walter Benjamin
- Katherine Hayles
- Donna Haraway
- possibly: Eugene Thacker, Clare Colebrook, Carey Wolfe

## Philosophy
- Nick Bostrom
- Derek Parfit
- David Chalmers
- Peter Singer
- Reza Negarestani
- Peter Wolfendale

## AI
- Joscha Bach
- Anders Sandberg
- Paul Christiano
- Eliezer Yudkowsky
- David Deutsch


\newpage

# References {-}

\setlength{\parindent}{-0.2in}
\setlength{\leftskip}{0.2in}
\setlength{\parskip}{8pt}
\vspace*{-0.2in}
\noindent