---
title: Reasons for Persons, or the Good Successor Problem
author: Kanad Chakrabarti
date: \today
abstract: \noindent Can we imagine evolving to a technologically mature species (meaning the creation of advanced synthetic intelligence and expanding to the stars), while remaining aware and preventing of the possible risks for all sentient beings that such trajectories present.  This is an unruly topic spanning philosophy, computer science, evolutionary studies, and ecology, but one suited to the multi-disciplnary, multi-level approach supported by Goldsmiths.  Firstly, I unpick tensions in the AI safety/alignment discourse between people concerned about existential risk, the risks of astronomic suffering, accelerationists, and evolutionists.  I summarise the context for tensions in the historical and cultural milieus of thinking about AI risk.  These tensions are relevant because they play out in research agendas; one such agenda considers the decision theories that advanced AIs might adopt, a topic I investigate through empirical work with current and frontier models.  Decision theories, in turn, seem to have deep connections to accumulated, ethical intuitions and philosophies, potentially across cultures and religions.  They also might offer a framework to revisit currently unfashionable perspectives like ‘the point of view of the universe’, which seem implicit in the ethics of worlds where humans, non-human animals, AIs, and potentially aliens might hope to co-exist.  In addition to practical work with AI systems, methodologies include mapping relevant ideas in the analytic or utilitarianism-derived tradition to analogues in the continental discourse (the latter is more common in art writing).  This is a practice-based project, meaning I use physical and conceptual objects to ‘imagine the unspeakable’, such as the phenomenology of an AI or the universal perspective above.  It should be noted that such a project has obvious echoes of ideologically charged movements such as transhumanism; relevant critiques are important and deserved, however those are not the central concerns of the project.

papersize: letter
fontsize: 11pt
documentclass: article
fontfamily: librebaskerville
linestretch: 2
link-citations: true
linkReferences: true
colorlinks: true
indent: true
bibliography: [bibliography_ukc.bib]
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  #- \fancyhead[L]{Left Header Text}
  - \fancyhead[R]{V:Goldsmiths 13/6/24}
  #- \fancyhead[R]{Right Header Text}
  - \fancyfoot[C]{Page \thepage}
---

These are things I want to cover - the first section ([@sec:ZERO]) corresponds to the writing sample required for the upgrade, hence is slightly more fleshed out.  See also {@sec:APP} for notes on the practice element and considerations relevant to the practice as-a-whole. 

# Overview {#sec:ZERO}

## Research question {#sec:QUESTION}
The thesis topic is as follows^[It is somewhat narrower in scope than the abstract implies]. Imagine a future world that has some combination of recognizable biological humans, machine-human cyborgs, as well as various orders of AGI.^[This definition would be expanded in the dissertation e.g. "recognisable biological humans" might include humans with various implants and modest genetic modifications; AGI is being used to gesture at "advanced AI" i.e. machines at near-human capability in a broad range of tasks] For the avoidance of doubt, such an imagined world could be one where there are no humans or other animals but there are AGIs; conversely, it could be one where there are no AGIs -- just humans and animals.  Leaving aside whether such a world is stable or how it would be formed, how can we think about notions of value in such a world?^[For the moment, I am slightly fuzzy on what is meant by 'world': whether it is just Earth or a more spacefaring context.  Discussions around AGI/ASI are adjacent to space exploration and astrobiology, and particularly come up in [@sec:space_of_minds].  For more on long-term trajectories, see [@BaumTrajectories], and for considerations of value in respect of populations see [@Greaves2017].]

## Why is this topic worth researching?
- AI risk is a `wicked problem' [@KarnofskyWPE] with aspects that span technology, existential/suffering risk, public policy, and philosophy [@BostromPCD], [@MetzingerASA], [@AlthausGloorRRA]. AI is also discussed in a politically polarised context that complicates object-level issues. [@McquillanAI] 
- This project is adjacent to a number of conversations in the critical (post-)humanities.  I note those adjacencies, with a view to completeness, but do not view those adjacencies as central to my project.^[A number of criticisms are raised about the "project" of AI, AGI, alignment including: the critical discourse around post/trans-humanism (e.g. allegations of eugenicism, universalism, technophilia, accelerationism etc.) [@BraidottiTP] [@ManzoccoTEH] [@McquillanAI] [@Gebru].]

Humanity's future with AI is a [`wicked problem'](https://en.wikipedia.org/wiki/Wicked_problem) [@KarnofskyWPE] with aspects that span technology, existential/suffering risk, public policy, and philosophy [@BostromPCD], [@MetzingerASA], [@AlthausGloorRRA].  AI is also discussed in a politically polarised context that complicates object-level issues. [@McquillanAI]  This section sets out the scope and primary concerns of the project.

**Thought experiment**: This project resembles a thought-experiment, in that its speculations aim to be grounded in physically-possible reality; in this it is similar to hard science fiction in the vein of Iain M. Banks or Vernor Vinge ([@BanksE], [@VingeFUT]).  I also hope to make explicit any potential is/ought confusions buried in my analysis. [@sep-hume-moral]

Imagine a (future) world with one or more artificial superintelligence(s) (ASIs) but where biological humans have disappeared (bracketing the precise manner or cause of their disappearence).

Below are some considerations for how we can we think about this world?^[Note: although this project is not explicitly about (AI-originated) human *extinction*, the distinction/overlap between extinction/evolution is important (see [@ChakrabartiUE] for a summary).]  The completed project will likely focus on certain aspects that there is a) substantial academic (or equivalent) literature on, b) where I believe some contribution can be made, and c) that might be subject to some pratice-based investigation.

- what might "the shape" (the physical, cognitive, and social organisation) of these ASIs be ([@sec:POSS_MINDS])?
- what are (some of) the paths from today's AI to ASI ([@sec:PATH_TO_ASI])?
- is it meaningful to talk about the proposed world (without humans) having value ([@sec:VFN])?
- phrases like 'aligning AI to human values' are used by technologists, politicians, and media figures.  
    - What of humanity's (diverse, complex and fragile) value set would we like to see in our successor species? [@GabrielAIV] [@OrdTP] 
    - Put another way, of the things `we' collectively do today, is there anything we would be sad to find absent in the future I have posited?  
    - What technical issues arise when aggregating values or preferences?
- is it reasonable or justifiable that we should have any opinions at all on what values our much-more-powerful successors have?  On what basis can we speculate at all about these successors' cognition at all? [@SandbergTML] [@BanksE]
- write down a `taxonomy of possible futures'( see [@BostromS]: e.g. empty universes/astronomical  [@DaiBAW], paperclip/squiggle maximisers, optimisers for hedonium or utilitronium, but also ones that are more obviously positive (from my perspective) ([@sec:FINAL_GOODS])).
    - defend (or dismiss) my proposed candidates for human final values: a battle against entropy through created complexity, which in concrete terms means art and perhaps respect for nature's diversity ([@sec:FINAL_GOODS]).
- the practice is inherently woven into the research process ([@sec:PRACTICE]) and specifically focuses on simulation as both research method and illuminating theoretical grounding ([@sec:SA])


## Historical milieu and assumptions {#sec:ASSUMP}

An understanding of this project's principal concerns will be enhanced by examining its philosphical assumptions and the social milieu of the various communities that dominated the early days and that, like all collectives, continues to change.  This isn't meant to be a social history of artificial intelligence (which is amply covered by others^[Find pasquinelli, etc., and books on EA history, brian christian.], but to pull out a few signposts which some have interpreted as marinating a very specific worldview.)

- 1990s: Bay Area rationalists
- Oxford school
- the deep learning era
- contemporary alignment
- TESCREAL

### Contextualising the project within existing critical discourse

This project is adjacent to a number of conversations in the critical (post-)humanities.  I note those adjacencies, with a view to completeness, but in most cases do not argue for or against the points raised.^[See also the note on two cultures and artistic practice below.]

These adjacent conversations include:

- the critical discourse around post/trans-humanism (e.g. allegations of eugenicism, universalism, technophilia, etc.).  These are valid criticisms but not the principal focus of my project. [@BraidottiTP] [@ManzoccoTEH] [@McquillanAI] [@Gebru]
- there are obviously concerns about race/gender bias and job loss owing to automation, supposed negative impact on human creativity, etc.  These also are not in-scope.
- the curious re-animation of  accelerationism (via [e/acc](https://en.wikipedia.org/wiki/Effective_accelerationism)) has probably just muddied the waters, and it isn't very clear whether any lasting insight will come out of it - for now it is out-of-scope.
- I have discussed some of these topics in [@ChakrabartiUE].

## Perspective from philosophy {#sec:PHILO}
To a large extent this is a philosophical project, owing to its breadth, and philosophy suggests two ways of examining the topic: a bottom-up or concrete way that starts from the world we observe today, the other is a top-down and more abstract or speculative one.^[This project institutionally sits within an art practice-based programme, hence it draws from a range of disciplines and practice, acting as a meta-discpline ([@FullerM]) that hopefully generate knowledge that would be less available to any one of those disciplines individually.] 

### A plurality of value
In the bottom-up approach, we start from today's world, compiling a list of preferences^[Following [@RussellHC] I use preferences to encompass morality, ethics, but also aesthetic choices, rather than "values", as the latter term sometimes might lead to confusion.  A broad overview of relevant topics can be found in [@gabriel_artificial_2020]]. Some of those preferences will be convergent across societies today, but a number of those will be diverse across societies, potentially incompatible, and generally not amenable to aggregation.'^[Recognising that these preferences cannot be aggregated and we’re not able to say anything about humanity as a whole. See [@gabriel_artificial_2020], [@weidinger_2023] and [Karnofsky on Harsanyi](https://forum.effectivealtruism.org/posts/iupkbiubpzDDGRpka/other-centered-ethics-and-harsanyi-s-aggregation-theorem#2___for_each_person__we_can_talk_meaningfully_about_which_states_of_the_world_are__better_for_them__than_others__).  There may be relevant insight in social sciences, e.g. [Habermas'](https://www.lesswrong.com/posts/QKgJ46JckosGcdZa3/the-ideal-speech-situation-as-a-tool-for-ai-ethical) "ideal speech situation".] And then we look at a range of different future world scenarios going from the multi-species one I just described [@sec:QUESTION] all the way to an empty world, or a world with perhaps one or more super-intelligences. In such a case, is there anything we can say about this grid of preferences versus worlds? 

### Nowhere/nowhen
The top-down approach is to explore a very specific question: the "view from nowhere", and set out the history of the term, including its similar terms like *sub specie eternitatis* and "the point of view of the universe", as well as how substantively related are they.  There is an important philosophical and historical context that led to those terms, as well as the substantial challenges to these universalist perspectives, both in philosophy as well as in a broader social and cultural context.^[**Besides Nagel, Wittgenstein, and Sidgwick/Singer, Bernard Williams, Elizabeth Anscombe** this should include **Clare Colebrook/Donna Haraway** and perhaps **Negarestani**; critical perspectives could perhaps start with **Braidotti, Wark on Anna Tsing, Moynihan**] It would be useful to also examine selected non-western literature for instance Buddhism to see if there are any analogous concepts.^[**Can we say a bit more on this?**]

### Evolutionary perspective {#ref:space_of_minds}
A point possibly underappreciated in the humanities is how human preferences, particularly morality and ethics, and perhaps aesthetics, seem to have been the product of a particular biological and cultural evolutionary context.  They are contingent, and we must recognize that some arbitrary design of mind ^[Bracketing whether such a design is something we can get to from where we are right now], might not hold these particular preferences. Depending on one's views on moral realism, the "oughts" many of us cherish (as manifested in preferences) are, to some extent, grounded in the current and historical "is"-es of the world.

Hence it seems valuable to sketch out^[**Ref to sources from RWTH talk**] what the design space of possible minds is, and set out some possible implications for the reasoning in [@sec:PHILO].^[As mentioned, this project sits in an Art Department, which is more forgiving and rather encourages speculation and thought-experiments.  In the interests of rigour however, I make it clear when I am veering into the more speculative.]


# Chapter 1: From LLMs to superintelligence {#sec:PATH_TO_ASI}


It might be useful to a non-AI specialist reader to clarify jargon (AI, AGI, ASI, HLMI, etc.) and relate current models to more advanced AI that is envisioned in this project.^[An early version exists at the [AI Risk Observatory Novacene](http://airo-ne.org/site/home.html).]

- why are we talking about ASI (as opposed to human-level or AGI which seem hard enough)?
- rebut the `stochastic parrot' narrative
- draw possible trajectories to ASI from current AI
- discuss results of my practical research in AI Safety Camp (see {@sec:PRACTICE})

# Chapter 2: The design space of possible minds {#sec:POSS_MINDS}

What types of minds are possible?  We are familiar with humans, a few animals (pets as well as wild), and now are making the first synthetic, modestly general intelligences.  Yet this probably doesn't exhaust the possibilities for what `shape' (physical, cognitive, social) intelligence might take, and this in turn may impact things like: how much agency they have, their goals/values, propensity for deception, and alignment with human well-being.^[This line of enquiry fell out of my research for this essay [@ChakrabartiAI], which asked whether an ASI would have reasons to make (anything we recognise as) art.]  

More generally, if certain types of minds are inherently deceptive or misaligned (with human interests), this increases the chance of bad outcomes for humanity.  On the other hand, cooperation and norm-following might be game-theoretically correct strategies for sufficiently rational beings (unlike humans or other primates). [@OesterheldECL]  This overlaps with [@sec:SOC_OF_MIND] and [@sec:VFN].

This topic was presented in April at [POM Aachen](https://www.pomconference.org/pom-aachen-2024/), in collaboration/consultation with [Anders Sandberg](https://www.ox.ac.uk/news-and-events/find-an-expert/dr-anders-sandberg) at University of Oxford, and will be submitted as a paper.


# Chapter 3: Minds in societies {#sec:SOC_OF_MIND}

Intelligence in humans is mostly a phenomenon of culturally-transmitted knowledge accumulated over generations - it would be useful to understand this better and ask whether that might hold for ASI.  This interacts with [@sec:POSS_MINDS]

- I'm particularly interested in how AIs interact with humans, each other, aliens: decision theory and evolved norms in multi-agent settings^[I suspect decision theory, evolutionary equilibiria, prisoners' dilemnas, etc. are not so well-known outside the rationalist discourse, and it might be valuable to explain it because they might re-frame (as contingent products of particular cultural-evolutionary trajectories that are localised in time and geography) some of the things we think of as uniquely human: 'morality', `values', etc. ([@sec:PRACTICE]]
- studying how AIs interact is experimentally tractable through simulations and fits in well with practice - this has been the main topic I explored at [AI Safety Camp 2024](https://aisafety.camp/previous-camps/), and will be documented [here](http://ukc10014.org/) (probably by June 2024).

 
	


# Chapter 4: The view from nowhere (VFN) {#sec:VFN}


This (the view-from-nowhere or VFN) is one of the least clear and most quagmire-prone elements of the project.^[VFN feels quite close to the discourse around moral realism discourse as well as ideas (e.g. Bach) on complexity-as-value.  It also sounds like things Peter Singer, Ludwig Wittgenstein, Thomas Nagel have argued, but initial reading suggests their contexts were quite different from what I'm interested in.  There might be interesting overlaps with indigenous or non-Western thought (Buddhism/Shinto) or panpsychism.]

**Abstract of the chapter:**
Most conceptions of value, at least in the Western Greek-Judeo-Christian tradition, place the human as, at once, both the site and the judge of value.  Consequentialist or utilitarianist systems straightforwardly aim at quantified well-being for people, while deontological and virtue-ethics strains seek a more abstract definition, yet still presuppose the human.  Moral realist views, particularly of the non-naturalist variety, try to set out a realm of moral facts which are not of this (physics-determined) world yet are still accessible through reflection, again by human subjects.

These approaches make sense, or at least have the weight of hundreds or thousands of years of accumulated insight to recommend them and we discard them at our peril.  Yet, they seem inadequate when dealing with other sentient species which do not share our lifeworld or our collective histories (bracketing contemporary views on whether such universals are meaningful or helpful terms).  For instance, how would we explain promise-keeping or truth-telling to a whale, assuming for a moment we could understand its language.  More pertinently, assuming we had an AI highly capable of reasoning - how would we communicate these intuitions which are so grounded in brute facts of our existence?  Why should we expect, on reflection, that these arguments should be convincing, not to mention binding, upon radically different sentient agents? After all, the story of human thought is that convergence on values, if any, is halting and demonstrates contention even amongst humans alive today (and in the past), who share similar biologies.

It may prove impossible to complete eliminate all subjects: in this thought experiment, we assume no humans; however, by definition, there would be ASI(s).  How can our current notions of subjectivity be extended to include such beings?  Does the literature around animal sentience offer a way? [@SeboLong]


## Sharing the future with our mind-children {#sec:SHARING}

VFN is important because decisions we make with respect to AI/ASI may need to be justified from a perspective broader than 'what is good for a particular group of humans' or even `what is good for humanity'.

- an example that [Joscha Bach](https://joscha.substack.com/) gives: 
    - imagine that we stop building AGI indefinitely, and as a result are ill-prepared to deal with various statistically probable (on a sufficiently long timescale) risks: a pandemic more deadly than COVID-19, population decline, catastrophic war, a major asteroid strike or simply fail to reach technological maturity^[There are lots of assumptions above (e.g. how confident are we that AGI might help avoid other existential risks versus itself increase existential risk), see [@MacAskillWWO]]    
    - it could be argued, that in such a case, we will have wasted part of the cosmic [endowment](https://nickbostrom.com/astronomical/waste) (of low entropy energy), and (depending on one's position on questions of population ethics) committed a grave injustice in respect of future, never-to-be-born generations [@MacAskillWWO] [@OrdTP]
- a more straightforward case is that of `AI shutdown': if we are about to shut down (i.e. kill) an AI that is sentient and morally-valuable, we need to have some justification for this (that is species or substrate-neutral). [@MetzingerASA] [@SeboLong]


# Chapter 5: Propositions upon final goods {#sec:FINAL_GOODS}


What might humanity's contribution to value be? What do we do that is valuable in a (VFN) sense, i.e. the universe would be poorer if these didn't exist?

- put another way, what precisely is wrong with a ['paperclip/squiggle maximiser'](https://www.lesswrong.com/tag/squiggle-maximizer-formerly-paperclip-maximizer) (or, for that matter, an optimiser for anything like utilitronium, hedonium, etc.)?
- following Bach, I propose *`created complexity as a way of resisting entropy'* as a major source of VFN value.  Specifically, I think of possible types of complexity: firstly, aesthetic objects or art (subject to an appropriate definition); secondly, the diversity that evolution creates in ecological systems.
    - I have an intuition that art, beauty, and aesthetic reflection might be close to final or terminal goals for humans, and (speculatively) for other advanced intelligences.  Connecting this, via writers like Alva Noe [@NoeTE], to such literature as supports Bach's view, could carry substantial weight in this project.
	- this intersects with **practice** in development of my project to get AIs to talk credibly about artwork, discussed as a concept [@ChakrabartiWAA], and as an [artwork](http://ukc10014.org/fixedp.html). See also [@sec:AESTHETICS]

# Appendices {#sec:APP}

## Simulation arguments {#sec:SA}

My intuition is that simulation is a rich thread (as opposed to a distinct chapter) that holds this project together, both in theory and practice.[@ChakrabartiBGU] 

- the topic's genesis is AI researcher Paul Christiano's thought-experiment [@ChristianoWUA]: his argument depends substantially upon simulation (as a way to 'test' candidate successor civilisations for their `niceness')
- thinking about simulated worlds has weird implications for [@sec:VFN], as well as for ethics and decision theory [@OesterheldECL]
- the possibility that we will soon be simulating agentic intelligences might be anthropic evidence regarding for how `real' our own world is (per the Simulation Argument of [Bostrom](https://simulation-argument.com/))
- as a practical matter, much AI research uses simulations and [my](http://ukc10014.org/exorbp.html) [artistic](http://ukc10014.org/sicul.html) [practice](http://ukc10014.org/islands2.html) and [writing](http://ukc10014.org/writing.html) have long been preoccupied by this topic [@ChakrabartiGET] [@ChakrabartiSCD]



## Current state of the project {#sec:STATE}
The breadth of the project's interests has required me to develop a viable approach such that I can say something that both fits within the guidelines of a art practice-based PhD and is legible to the broader alignment community with whom I interact (and who, to a certain extent, are my research sources).

- In April 2024 at the [Politics of the Machine Conference](https://www.pomconference.org/pom-aachen-2024/) at RWTH University (Aachen), I presented a draft of a paper, co-written with Professor Anders Sandberg (University of Oxford) on the `design space of possible minds' [@sec:POSS_MINDS]
- In March 2024, I gave a short lecture-video documenting a research collaboration with Jascha Sohl-Dickstein (ex-Google Brain): the fractal nature of learning (the shape of the high-dimenstional loss function of a very simple neural network is visualised and sonified) within AI systems is placed in context of Stanislaw Lem's prescient writing on non-human intelligence, evolution, and the possibility that our norms might be a mere accident of biological and cultural history [@LemST], [@BrattonArcasTMI]
- In January 2024, I presented an initial version of [@sec:AESTHETICS] at Goldsmiths, and documented [here](http://ukc10014.org/fixedp.html)
- From late 2023, an essay that speculating about an ASI's reasons to make art is published [@ChakrabartiAI]
- My research practice is heavily integrated with AI models as described in [@sec:CYBORG], and in both 2023 and 2024 I have participated in AI Safety Camp, a programme for empirical and theoretical research into AI alignment.  The results are documented [here](https://aisafety.camp/previous-camps/), but 2024's project involved understanding the decision-making procedures and propensity for deception/collusion in current language models.  In 2023, I looked at practical ways of working in human-AI cyborg teams to solve cognitive tasks.
- The empirical work/practice described above has required me to learn Python as well as an ecosystem of machine-learning software, such as PyTorch, as well as develop skills in data generation, curation, and training small models.
- In December 2023, I considered this project's aims in light of conversations around human extinction, as well as criticisms of post/trans-humanism (see above)[@ChakrabartiUE].


## On practice (artistic and otherwise) {#sec:PRACTICE}

### What constitutes `practice'?

This project involves^[This is a meta-question of this project: what is needed to present an empirical AI research output as a valid presentation for the purposes of the PhD's practice component?  This, in turn, is connected to the [two cultures](https://mindsalmostmeeting.com/episodes/the-two-cultures) issue though I argue art sits slightly outside that binary.] multiple notions of practice, both as in scientific research such as working with LLMs, and the (to my knowledge, less explicitly defined) practice of artistic investigation within the PhD context.  I see both as falling within the 50/50 definition of 'practice-based PhD'. [@SnowTC]

### Models as cyborg research partners {#sec:CYBORG}
- further to my prior work on [Cyborgism](https://www.lesswrong.com/posts/iFBdEqEogtXcjCPBB/the-compleat-cybornaut) for AI Safety Camp (see {@sec:STATE}) I have integrated LLMs deeply into my research, planning, and writing process.
- as I document [here](https://www.lesswrong.com/posts/k93NEoXZq6CdXegdx/philosophical-cyborg-part-1), present LLMs aren't great at generating useful (philosophical, artistic, or other qualitative) insight, but I would like to see if any progress can be made here (in collaboration with others within empirical AI research).

### Fine-tuning upon the anthropology of AI researchers
Some aspects of my project have a strange position in the AI alignment discourse: they are, at the same time, not discussed explicitly (perhaps because they are too 'fringe' or repugnant), yet seem to be plausible or probable consequences of current developments in AI.  I would like to interview a number of AI researchers and ask them direct questions relevant to this project, collect the data, and build an anonymised dataset used to fine-tune a LLM (as an aid to my own research, as well as a submission-via-practice for the PhD).

### Future Claimant's Representative {#sec:FCR}

- the ideas in [@sec:SHARING]  are to be presented through a `*ludic essay*' (a film/video essay implemented in a game engine, which may be viewed cinematically or through a VR/AR headset) [@ChakrabartiGET]
- the narrative is inspired by a quasi-legal construction: a representative of unborn/uncreated future generations of sentient beings, who is known as the `future claimant's representative' (abbrev. FCR, originally suggested by Baucom in an ecological context [@BaucomFCR].

### The dissertation as creative product

- I see the dissertation as existing in multiple formats - a) a static, academic document for Goldsmiths repository (which perhaps might become a future book), and b) an online site that becomes a tool for other researchers (e.g. potentially including the fine-tuned LLM above)
- This is in line with my previous projects, usually as [websites](http://ukc10014.org/media/qm_2018-master/index.html) for [exhibitions](https://ukc10014.github.io/neu/), [stand-alone artefacts](http://airo-ne.org/site/home.html), or [press releases](https://www.artistsallianceinc.org/wp-content/uploads/2020/11/calling@sweeneyshoal_pr_rr_110620.pdf).

### Aesthetics, art-writing, and value {#sec:AESTHETICS}

- I am interested in the capacity of multimodal models (LMMs) like GPT-4V or SORA to examine, deconstruct, and interpret artwork.  I do not expect current models can have a credible subjective aesthetic response (or even what the criteria for determining this might be), but I think there is a lot that we (art-educated human subjects) say about an artwork that is fact-based and effable (i.e. concrete statements that describe a work, draw comparisons with other work, etc.) and should, in theory, be accessible to a model. [@ChakrabartiWAA]
- Opinions about art are made in collective or social settings (i.e. are a product of cultural learning and transmission): to what extent can this be replicated and studied in groups of interacting models? 
- I made a proof-of-concept at [Goldsmiths](http://ukc10014.org/fixedp.html) in January 2024 and plan to develop this further
- this line of investigation can be seen as a manifestation of [@sec:FINAL_GOODS] but I also investigate the extent to which models that are fine-tuned for art or aesthetic purposes (i.e. fed the e-flux or comparable corpus of writing) express opinions that are 'more aligned' (less deceptive and more pro-human).


\newpage

# References {-}

\setlength{\parindent}{-0.2in}
\setlength{\leftskip}{0.2in}
\setlength{\parskip}{8pt}
\vspace*{-0.2in}
\noindent