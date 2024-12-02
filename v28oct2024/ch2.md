# Chapter 2: On Alignment

## What is this chapter about

This chapter covers the following topics:

- sets out why AI as a technology is "special"
- discuss the difference between AI alignment, safety, and ethics
- explain why AI alignment is of particular interest
- the contingent history of AI alignment as a discourse
    - examining the judeo-christian allegation
        - what were the imaginaries that served to communicate ideas?
    - the transhuman background
    - what is the relevance of x-risk (and potentially, s-risk)
    - how has the AI x-risk threat model changed
- the MIRI view, impersonal optimisers, recursive self-improvement
- what futures have value
- how did technology shape discourse
    - GOFAI
    - RL
    - next-token predictor
- what were the internal critiques of MIRI view
- revisiting the external critiques
- is alignment a relevant concept or discourse today
- how do we look at the above topics (which are AI and AI alignment-specific) against the positions articulated in the CCRU, particularly by Nick Land

### Contextualising against the project as a whole?

This chapter's central claim is that 'alignment', taken less as a literal term and more as a discourse^[I’m using the word ‘discourse’ in the sense of Paul Edwards’ book *The Closed World: Computers and the Politics of Discourse in Cold War America* (1997) (..**quotation**).], had certain contingent origins that continue to affect the priorities of the field and researchers in it, may affect their world-views, and influence surrounding contemporary conversations. The chapter also draws a parallel, through anecdote and enriched through practice, with accelerationist thought (of the Warwick CCRU variety) and a fertile, perennial theological-apocalyptic vein in Western conceptions of technology. While possibly more coincidental than causal, these parallels and analogies inform the project's practice component.



## Historical Bases of Alignment-as-discourse

The claim of this chapter is that AI alignment, both as word and discourse, became prominent in the years between 2008 and [2014] and came to incorporate certain ideas relevant to AI that were circulating pre-2008, ideas that had various antecedents, including technical ones such as microeconomics-based theories of rational agency, operations research, and computability theory. These technical frames of the problem of AI existed (or at least were sometimes communicated) in a milieu that had imaginaries drawn from (science) fiction; at the same time, these frames were being used to actively battle a particular Hollywood-framing of AI as an anthropomorphic killer robot (Terminator). 

This was a proselytising exercise, the principals of which came out of an earlier online milieu of transhumanist futurists. As of [2014], alignment was still a mix of (mostly) non-quantitative philosophical futurism (e.g. Bostrom, Sandberg), and mathematics-based explorations into the nature of agency (e.g. MIRI's agent foundations and decision theory agenda). Between [2014] and [2019], this largely theoretical work started coming into contact with reality as interesting results in reinforcement learning appeared. Alignment's definition (as practically expressed through discourse) was enriched, and the abstractions of the philosophical and mathematical sub-discourses were questioned, or increasingly, treated as fascinating but unverifiable. By [2019], the ground shifted again, as reinforcement learning gave way to language models as the most likely path to AGI. The concepts that grounded alignment needed to be revisited, and often, reworked or replaced to accommodate the drastically different architecture of LLMs. Currently, as of [2024], alignment has become a less popular term, as the field (of AI) has grown and powerful AI has become more tangible, terms that are more inclusive of actual or near-term and concrete risks, such as AI Safety and AI Ethics, have become more common. The aspects of alignment that were most empirically supportable, as well as the most useful theoretical framings, were incorporated into the broader conversation, while other sub-discourses have petered out.

Why does anyone care? 
- specialness of AI as GPT, as amplifer (Russell's WEF talk) with in-built philosophical/social aspects 
- general purpose problem solvers as goal-directed planners

### What is Alignment?

- Given it is a weird word; 
- why are we interested in it ; 
- what does it mean literally;
    - confusions on values vs don't-kill-everyone
- what were the features of the particular view I'm interested in here
    - self-replicating generally capable intelligence
    - power imbalance vis a vis collectives of humans
    - perfect rationality
    - people promoting this view fundamentally still had a human attachment (reza's critique I think)
- how common is it and what different ways is it used (quantitative)
    - connect to antikythera
- the friendly angle, safety and ethics show up, alignment gets repurposed
- who are the relevant people (make a glossary or exhibit):
    - MIRI^[The Machine Intelligence Research Institute was a major early incubator of thinking around agent foundations, which is the study of the theoretical foundations of agency, both in humans but also across societies. *Note from google doc, this is contested - check what agent foundations is and why it's important in this context - Alignment borrowing from agent foundations without justification isn't obvious. David Mannheim's paper 'reasons for working on highly reliable agent design'*], 
    - EY, NB, Omohundro

*A timeline would be really useful*

#### Friendliness, Ethics, Safety, and Alignment

Before diving into the history of alignment, a bit of semantic house-keeping: since the dawn of AI in the [1950s], there have been concerns about the risk of intelligent systems.^[Maybe IJ Good quote?] More generally, stories like *Frankenstein* registered the concern, albeit in literature. In the late 1990s, the term ["Friendly AI"](https://www.lesswrong.com/tag/friendly-artificial-intelligence) emerged, defined (as of 2015) as the "field of knowledge concerned with building [AIs that promote human values]. A [Friendly AI] need not be 'friendly' in the conventional sense of being personable, compassionate, or fun to hang out with...[and it] need not even be sentient". Friendly AI's anchoring to "human values" was subsequently critiqued by [Goetz 2012](https://www.lesswrong.com/posts/mSktD7oj6C2zxj3KC/holden-s-objection-1-friendliness-is-dangerous), for a number of reasons:^[That goetz 2012 post is good, might be worth digging slightly more into it and make these more precise]

- because values are not just "one thing", in that some of them are the result of biological evolution, others come from society, while still others are arrived at by rational reflection;
- values can apply for short or long time horizons;
- values are often filled with objective errors or simply become abhorrent upon future reflection;
- the set of values that a given society purports to uphold change radically over our comparatively short time as a species;
- values come in different flavours (e.g. non-positional/mutually-satisfiable versus positional/zero-sum), which presents issues with aggregation;
- human values, whatever they are, are immature and it could be a dramatic moral mistake to insert them into AI systems that are much more capable, knowledgeable, and reflective than we, who then go on to propagate across time and space;

In any event, as the Friendly AI page above notes that the term was, as of 2014, outdated, and had been replaced by "AI alignment", at least within LessWrong context as of 2015, a term that was already "the subject of much debate".

Unlike friendliness/alignment, which envisioned hypercompetent optimising intelligences in the future, the term "AI safety" seemed to be used more in the context of AIs that were incompetent and error-prone, and indeed could already be seen in nascent form as self-driving cars and recommender algorithms. See for instance [Amodei 2016](https://arxiv.org/pdf/1606.06565). Safety has incidentally been proposed, and is being increasingly used, in a contemporary context to include a wide set of concerns about AI systems, as a way of building broad [coalitions](https://x.com/AndrewCritchPhD/status/1792366466802819208) (or [conflationary alliances](https://www.lesswrong.com/s/6YHHWqmQ7x6vf4s5C)) for regulation (papering over some of the personal and social divergences between the people working on various AI-related technical and policy questions).^[Distill TJ's X post on these distinctions and credit]

Another discourse that was concerned with present-day harms was that around "AI ethics" ([Christian 2020]), which (unlike AI safety) came out of a 1990s discourse on human-computer interaction and the effects of computing that was embedded in human systems.^[Find some more specific citations of this genealogy] By the late-2010s ([Buolamwini 2019]), the term was commonly used to highlight cases of apparent racial and gender bias in AI systems. The safety and ethics conversations, while having superficial concern about errors in currently-existing systems, never merged. There may have been social or culture war related reasons.^[Substantiate]

In particular, the ethics conversation turned heated after Timnit Gebru's ouster/resignation from Google in 2020, the evolving agenda of the FAccT conference, and a new ethics-focused organisation Gebru established called DAIR. Gebru also popularised (along with existential-risk researcher Emile Torres) the term TESCREAL, which stands for transhumanism, extropianism, singularitarianism, cosmism, rationalism, effective altruism, and longtermism. This particular bundling of ideas seems principally driven by Gebru/Torres' views, and the historical provenance of these ideas stretch over a hundred years; their histories are not causally-related; their conceptual overlaps are argued to varying degrees of convincingness.^[Revisit and rewrite to incorporate or cite the objections...see TJ's posts on this]

This chapter, however, is concerned with the ideas that "alignment" included and its peculiar intellectual genesis. As discussed, it came out of an earlier concern with "Friendly AI", but incorporated a history born of Cold War-era thinking around rational agency and game theory, as applied to hypercompetent optimisers. As such, it had some echo with the ideas Nick Land and the CCRU had explored [in the 1990s].^[Any evidence they talked, or was this just in the air?] The CCRU's commitments were fundamentally literary, musical, and philosophical, while the discourse described here came out of futurism, transhumanism, and the computational ferment of the Bay Area.


## Origins: Rational Agency

### Sources

In launching this historical study, I focus on a few sources, which seem to be the earliest mentions of 'alignment' as an important topic around advanced AI systems. 

Discussions around alignment are better appreciated in the broader context of (some of) the various disciplines that informed AI^[mostly taken from Russell \& Norvig 4th ed Ch 1]: 

- philosophy (from Aristotle and Descartes on humans as creatures whose actions are guided by reason, through Hume (on induction), Carnap (on the mind as a computational process), Wittgenstein, Russell and the Vienna Circle (on empiricism as the handmaiden to rationalism), Bernoulli, Bentham, and Mill (on utility as a way of capturing a human's subjective valuation of some outcome, which leads to utilitarianism when applied across populations), and Kant (on rules being an appropriate guide to action, rather than blindly following a utilitarian calculus))
- mathematics (Bayes (on how to update beliefs based on new evidence); Gödel; Church, and Turing (what problems are computable within any given system or architecture))  
- economics (Bernoulli on diminishing utilities (at least for money); Walras, von Neumann, and Morgenstern (who broaden ideas around utilities and preferences-for-outcomes to contexts broader than monetary or economic ones); the latter two also do formative work in the theory of games)
- operations research (Bellman on Markov processes which govern situations where payoffs are delayed in time and depend on a sequence of actions; Simon on satisficing)

Russell/Norvig describe the other disciplines (cybernetics, computer science, psychology, linguistics, neuroscience) in much greater detail, but for purposes of this chapter, I set this truncated background.

#### Savage and expected utility maximisation

This is just a placeholder, but herrmann/levinstein talked a lot about this, and it feels important, should have some link to miri work? Even if it doesn't, mention it as it prolly connects with later decision theory work?

#### Omohundro in 2008

##### Self-improving systems ~ rational agents

The earliest mention of 'alignment' appears to be [Omohundro 2008](https://selfawaresystems.com/wp-content/uploads/2008/01/nature_of_self_improving_ai.pdf) on self-improving systems, by which he means humans and other naturally-evolved systems (to some extent) but also human-designed computers that can change their software and hardware in order to achieve goals in some environment.^[Claude's analysis was only 3 citations in the paper's bibliography were alignment related (1, 2, 22). There were 15 other citations in computer science, 8 in physics/astrophysics, 9 in economics, probability, and game theory, 5 in evolutionary biology/psychology, 4 in human psychology/cognitive science/linguistics. The bibliography had 48 entries.]

The abstract of this paper is instructive:

- self-improving systems as a coherent concept
- the idea that self-improving systems converge on certain architectures, and that they can be understood through certain tools originally developed in a microeconomics context
- self-improving systems tend to develop four 'drives' (towards efficiency, self-preservation, resource acquisition, and creativity)

Taking these in turn: the idea of self-improving systems (as the highest level of a hierarchy that goes progresses in complexity, environmental responsiveness, and adaptiveness through inert, rigidly reactive (thermostats), adaptive (basic physiological homeostatic systems), deliberative (human reasoning), culminating at self-improvement (which humans can only do in very limited ways)) is documented within computer science at least to 1965 (I.J. Good)^[ref p.3 omohundro 2008]. 

An important observation is that self-improving systems, far from being unpredictable, seem to be amenable to microeconomic frameworks such as that of von Neumann and Oskar Morgenstern (1944), Leonard Savage (1954), F.J. Anscombe and R.J. Aumann (1963)^[Omohundro does point out that this conception of *homo economicus* as a rational actor is increasingly being challenged in the case of humans, e.g. in behavioural economics.]

Omohundro's quote on self-improving systems is instructive 'Self-improving systems do not yet exist but we can predict how they might play chess. Initially, the rules of chess and the goal of becoming a good player would be supplied to the system in a formal language such as ﬁrst- order predicate logic1. Using simple theorem proving, the system would try to achieve the speciﬁed goal by simulating games and studying them for regularities. By observing its patterns of resource consumption, it would redesign its chess board encoding and optimize its simulation code. As it discovered regularities, it would build a chess knowledge base. General knowledge about search algorithms would quickly lead it to the kind of search used by Deep Blue. As its knowledge grew, it would begin doing “meta-search”, looking for theorems to prove about the game and discovering useful concepts such as “forking”.'^[p. 6] He goes on to describe how these systems might (if they have the affordances to do so) might redesign their own hardware in the service of efficiency.

He goes on to formalise the intuition that rational economic actors have internal representations of goals; identify the possible actions in a given environment and assess the consequences of each action; pick the action that will achieve the goal with high probability; observe the environment and then update internal representations appropriately.^[p. 7]

He claims that a certain microeconomic formalism should drive the behaviour of rational beings; the presents the concept of 'vulnerabilities', conditions that cause an agent or system to lose resources (money, in an economic context, but this could be food or sleep, and more generally, physical things like free energy or useful matter) created by the interaction of the agent's environment and its particular preferences. Sometimes these vulnerabilities are actively exploited by (other actors in the) environment, and in other cases (like the bird that repeatedly flew into Omohundro's shiny car fender to the detriment of its genetic fitness) it is evolution in some sense that needs to 'work around' such vulnerability. 

If there are such vulnerabilities, the agent faces a pressure to optimise, and the resulting system should have certain features: beliefs (what an agent knows about the world); using probability distributions to represent beliefs; and the use of utilities as a quantitative statement of preferences; particularly in the case of self-improving systems, the importance of separating what one knows about the world (beliefs) from what one 'wants' (preferences); and discounting outcomes in the future, potentially at a different rate depending on how far in the future they are. The latter in particular might lead to issues around infinities, as well as over-weighting the present and under-weighting the long-term future^[topic that we return to below in the discussion around existential risk and longtermism].

Another key insight of the paper (drawing on literature on algorithms and computational efficiency) is that although future AIs may be powerful (compared to humans or present AIs), they are very likely to face resource constraints on how much computation they can undertake - the real world is far more complex than anything humans or evolution are likely to create. Agents are always operating with insufficient resources, and must learn to economise and allocate in some way. Omohundro describes the notion of 'proxies', which can be of various sorts, but basically allow computations to complete faster or more cheaply or not happen at all. But this reduction in complexity often comes at a cost (the map is not the territory).

##### Rational agents have certain drives

Omohundro's paper is better known for its notion of "drives", that in his view fall out of this framing of rational agency. If one accepts Omohundro's starting premise (that self-improving systems tend towards being rational actors in a microeconomic sense), then his assertions about the drives (efficiency, self-preservation, acquisiton, creativity) becomes easier to see. Yet even here there are subtleties that will continue to show up, perhaps elaborately masked, in subsequent discussions around alignment.

His writing on efficiency is best-grounded in that it mathematically carries forward the concept of utility to describe how a system might allocate resources amongst its sub-systems; what the physical (communication latency and energy consumption) limits on a computational system might be; the deep role of entropy in computation. The most intriguing aspect is that he predicts that sufficiently advanced systems develop manufacturing techniques that are "atomically precise" (in a specific entropy-preserving sense), which might inform Omohundro's subsequent work on nanotechnology. This is potentially interesting, at least in hindsight, since the "AI x-risk imaginary" envisions the universe turned into "grey goo".^[See if any of grey goo cites this paper or nanotech. Any other names for this?]

Another section on self-preservation considers the need for a rational agent to hold on to its utility function, as this is the central core of "who they are", thus butting up on personal identity. Specifically, if future AIs are able to create arbitrary numbers of backups, their sense of identity may or may not be as bound up with physical instantiation, and they may instead seek to preserve their utility functions (assuming these encode their most important goals). In an echo, albeit uncited, of philosophical thought on non-personal identity (Parfit 1998), identity in a Buddhist context, or open individualism^[Get some sources, this is kinda important around corrigibility question, stuff with nick dupuis, and feeds into bostrom cosmic host/VFN. Perhaps these ideas can be brought closer to ECL/decision theory.], he states that certain systems might sacrifice a given physical instance if "it could be convinced that another system was as dedicated and could use its resources more effectively for this cause, however, it might willingly sacriﬁce itself." (p. 26) In another rhyme with Land's thought, the self-preservation tendency might mean that war itself changes - there is no point destroying the enemy's computers, rather one should want to scramble its cognition - all war becomes informational.^[Perfect place for a Land quote]

Omohundro's work, and much of the subsequent alignment discourse as well as [Lem of the summa], relies on evolutionary analogies. For instance, in part 6 of his paper, on the drive towards resource acquisition, Omohundro refers to [Smith/Szathmary] on the "hard steps" in evolution, an idea which shows up in the literatures around alignment, the Fermi Paradox, and the shape of alien cognitions - topics that deeply inform the ethical and philsophical motivations behind AI alignment and existential risk reduction.^[This is kind of important - it isn't just alignment as a computer science problem...the basic motivation for all this (or at least the claim of the thesis) is that that unlike previous technolgies, self-improving optimising processes have the potential to bring about an 'end without remainder' to human existence, and given that we haven't found anything else in the universe after ~60 years of searching, and have some theoretical models to say we might not, whatever we are doing here is in some sense important, if only for its rarity. This relates to hanson's great filter paper from 2008 or bostrom's urn. **This should be brought out at a higher level, if nothing else - humanity isn't stumbling into the abyss, there is quite a lot of writing from x-risk and accelerationism pointing the way.**] Whether one is using the evolution or astrobiology framings of evolutionary hard steps, some convergences are: creation of self-replicating molecules, the transition from prokaryotes to eukaryotes and multicellular organisms, and then to colony-based organisms with culture. Omohundro's invocation of Smith/Szathmary smuggles in another assumption, or perhaps a desideratum, of advanced societies - that they necessarily develop cooperative and prosocial behaviours as a way retaining cohesion and longevity.

This correlation of cooperation and societal complexity is exemplified by Omohundro by multi-cellular organisms' immune systems as defences against cancer (reading cancerous cells as an antisocial entity that exploits the surrounding environment), and citing a documentary (["The Corporation"](https://www.youtube.com/watch?v=dpjypnxnS4U), 2003) corporations as quasi-sociopathic entities (p. 29), that amass resources albeit within regulatory constraints.^[This is another important seam - that companies/corporations are sociopathic - shows up in Christiano - trace this line through to letter to future, which takes the more market-friendly view. This also aligns well with Land and perhaps others in ccru] In the context of self-improving systems, Omohundro sees free energy as the most important constraint (where "free energy" is that energy which is useful for work, since some portion of kinetic, potential, thermal, or chemical energy is inevitably lost in entropy increases, at least in common Earthly situations, and bracketing the specific entropy-preserving atomic scale processes Omohundro proposes). Omohundro briefly summarises the importance of solar (and stellar) energy as the purest (e.g. lowest entropy) energy available; less efficient but plentiful energy is also accessible through nuclear fission and fusion. The importance of stellar energy implies that resource-hungry systems should expand into space, perhaps through Von Neumann Probes, developing structures like Dyson Spheres to capture the maximum energy from a star, and perhaps ultimately restructing at a cosmic scale.^[Ref to cirkovic, collapse volume on this, bostrom. maybe talk to mackay. The kardashev concept should be mentioned - maybe a claim of this thesis is that humanity has a destiny. **alignment is not just a cautionary project (of not going extinct), it is also promethean (realising our destiny)** Show the seam into anders sandberg etc.]

##### Is/Ought Distinctions 
Importantly, Omohundro's framework is not saying anything about how 'good' (in whatever sense) any goals actually are - they may be selfish or altruistic, or anything else, as long as the goals can be mapped to utilities. Although his analysis is largely descriptive (of how physics-constrained systems achieve certain design constraints), a discordant normative note comes from his discussion of creativity (one of the drives) where he seems to find a maximally efficient universe somehow unsatisfying: "Once it had satisﬁed all the material goals, this kind of limited agent would have no greater purpose. With too limited a vision, the universe might become an efﬁcient but distinctly empty and non-human place." (p. 31) He goes on to explain much of human cultural production as a "costly signalling" behaviour ultimately grounded in prospective reproductive success, citing the evolutionary psychology literature. He suggests that we (in designing future AI systems) should be careful not to lose such costly signally behaviours or the resulting artefacts, which would be the (by his own logic) tendency of self-improving systems, which "will be motivated to find ways to make [such signals] without the cost. For example, a system might demonstrate its intentions directly by displaying portions of its utility function. If we want to retain the richness generated by costly signalling, then we must find ways to keep it from being eliminated by improvements in efficiency." (p. 32) 

This "ought"^[Ref is/ought], in a work that is otherwise relatively descriptive, seems to be consistent feature of the discourse around AGI - the potential consequences of the technology are described, but the relevant authors seem to struggle with the implication (human extinction or the extinguishing of costly signalling behaviours or a universe with no art/music/meaning).^[Make this a lot more precise - which authors are we talking about? Is this a major point - in a sense it is the major claim of the thesis and connects well to Land?] Land repeatedly notes (e.g. in [TU 2024], <timestamp>) that he is merely describing how he sees the world, rather than prescribing how it ought to be. In this sense, Land's accelerationism is more clear - it bites the bullet of its reasoning, in that Land recognises that the combined historical forces of capital and AI mean the end of biological humanity as we know it.




#### The MIRI View

Omohundro's paper set out some of the key preoccupations that would continue to inform the alignment discourse, but another principal source of basic thought about 'the AI problem' came from the Machine Intelligence Research Institute^[Point to mission statement of MIRI and 1 sentence summary, mention it is defunct], set up by Eliezer Yudkowsky, who perhaps did the most (at least in the 1990s) to make the idea of out-of-control AI "tangible", at least for a mathematically or scientifically literate audience.^[Brief blurb on Eliezer, sequences, HPMOR, etc.]

MIRI's archive of research starts with a publication by Yudkowsky from 2001, that sets out his original vision of creating benevolent or "friendly" AI, which is a term less-used now, but is a seemingly quotidian term that is used by Yudkowsky in a multivalent sense.^[According Yudkowsky's post to the [Arbital](https://arbital.greaterwrong.com/p/NickBostrom?l=18k) site, which dates from 2015, "Friendly AI" was a term proposed by Bostrom.] In section 2, he writes: "The term “Friendly AI” refers to the production of human-benefiting, non-human- harming actions in Artificial Intelligence systems that have advanced to the point of making real-world plans in pursuit of goals...Because of self-improvement, recursive self-enhancement, the ability to add hardware computing power, the faster clock speed of transistors relative to neurons, and other reasons, it is possible that AIs will improve enormously past the human level, and very quickly by the standards ofhuman timescales...Friendly AI is constrained not to use solutions which rely on the AI having limited intelligence or believing false information, because, although such solutions might function very well in the short term, such solutions will fail utterly in the long term. Similarly, it is [safe] to assume that AIs cannot be forcibly constrained...Success in Friendly AI can have positive consequences that are arbitrarily large, de- pending on how powerful a Friendly AI is. Failure in Friendly AI has negative conse- quences that are also arbitrarily large. The farther into the future you look, the larger the consequences (both positive and negative) become. What is at stake in Friendly AI is, simply, the future of humanity."

Friendly AI seems to be a historically important term that continues to be in the MIRI archive^[What about LW/Arbital/AF/sequences e.g. this seemingly good [criticism from 2012](https://www.lesswrong.com/posts/mSktD7oj6C2zxj3KC/holden-s-objection-1-friendliness-is-dangerous)] (and I extrapolate, the broader discourse) until about 2014, but was criticised as being excessively anthropomorphic and anthropocentric.

In 282 pages filled with his customary aphoristic text, often verging on verbosity, the document sets out his criticisms of anthropomorphic^[weave in hayles' distinction between centric/morphic] thinking about AI leading us astray, as well as a box-and-arrow sketch of a possible AI architecture. The bibliography is one page, of twenty sources, six of which are science fiction; seven articles on AI; and five on evolutionary psychology, psychology, and cognitive science. There is also a glossary that is a fascinating window into the terms that continue to crop up in the discourse, almost a quarter-century later. The difference between this and the Omohundro document however, is the more quantitative grounding of the latter in game theory and economics.

The rest of the articles (total eleven) in the MIRI archive 2001-2009 deal with a variety of issues that are distinct from the Omohundro document in their emphasis on "big pictures" questions around AI, and less so on architecture or nitty-gritty of building the things in a way that doesn't kill humans:

- how AI interacts with catastrophic or existential risks and geopolitics (three articles)
- how to load human ethical and moral intuitions (insofar as that is appropriate and can be identified consistently) and judgement into AIs (three articles)
- one article on mathematical details of utility functions
- an 122-page document on intelligence by Yudkowsky, viewed through frames or subsystems, that operate at different levels of abstraction (e.g. code, sensory modalities, concepts, thoughts, deliberation). Yudkowsky also considers how this framework and its implications might vary across minds-in-general^[Do a deep read of this for minds-in-general chapter, and reference substantially in Aachen paper]

2010 sees ten articles, at least one of which directly comments upon Omohundro's work ([Shulman 2010](https://intelligence.org/files/BasicAIDrives.pdf)), specifically considering cases where an agent following an expected utility framework might, depending on the "shape" of its utility function (e.g. whether it is satiated by large quantities of any given good, like humans often are for food, and perhaps even for money), opt to cooperate with other agents (including humans). It is hard to assess whether this analysis was impactful in subsequent discussions.^[Maybe use notebookLM (docs are already loaded there) to search for references, and do same for lesswrong/stampy.]

Outside of [Shulman 2010], MIRI's archive 2010-2014 considers a range of topics including^[This is TBD (**at least until I've assessed the 2014/2017 versiosn of MIRI tech agenda which presumably compresses the most valuable of this stuff**), but for the moment, I'm not digging into each of these - this diss isn't about MIRI's history and lot of these things become a background-of-sorts to alignment now, rather than mainstream research. This is just based on the titles - I tried to scrape all the relevant PDFs and then feed them to notebooklm (that project is saved in notebooklm but the actual subset of files that i could automatically download are in desktop/pystuff/scraper/miri_pubs while the titles that couldnt' be downloaded are in the smol/ dir). It might however be worth going into the various categories as they show up (outside of MIRI) subsequently under different names]:

- highly theoretical/mathematical thinking about issues that might apply to powerful AI systems unconstrained by anything other than physics (called "Highly Reliable Agent Design" in MIRI's parlance)
    - the various decision theories (primarily acausal) that had been developed (this will be the topic of subsequent chapters in this dissertation);
    - the mathematical and logical foundations of agency
    - how AI systems are to reflect upon their own reasoning (as humans do)
    - what is intelligence and what are its limits
    - possible Gödel problems with self-replicating ("tiling") agents
- problems surrounding value and values ("Value Specification")
    - how to transmit human values (howsoever defined) to an AI
    - how to ensure that AI systems deal adequately with uncertainty, which comes in various flavours (e.g. uncertainty about the human overseer's "intentions" versus what they actually said; empirical uncertainty about verifiable facts; uncertainty about normative things, such as "what should one value?"); 
    - the possibility of, and importance of avoiding, unintended consequences
    - how to ensure an AI that creates subsequent AI systems is able to preserve and transmit the original (human-derived) values
- the trajectories of AI development ("Forecasting")
    - paths to existential or catastrophic level risks^[Need a footnote explaining the difference and ref'ing Macaskill, Bostrom, SJ Beard, the new 2024 book.]
    - the economics of societies with powerful AI systems
    - uploading of human brains into software systems as another route to enhancing the aggregate cognitive capacity available to humanity
    - how useful are analogies from evolution, and from humans
    - the science of prediction
    - surveys of AI practicioners on timelines
- how to deal with various that might crop up, mostly on the part of the AI (but via humans' inadequate design of said AI), called "Error Tolerance" by MIRI
    - how to ensure that AI's values can be changed by humans later (given that early AIs might be badly constructed)
    

##### 2011 Singularity Summit

A slightly interesting document is the [report](https://intelligence.org/files/SS11Workshop.pdf) of the 2011 Singularity Summit, which dealt primarily with whole-brain emulation ("WBE", which is creating software copies of human brains), in  terms of the technical and conceptual issues involved, as well as how the timeline of WBE interacts with the timeline for AGI. The report primarily discussed how WBE (of AGI researchers or other scientists) could be a cognitive multiplier (100s of researchers working in parallel might, for certain problems, achieve results faster). The report (pp. 4-6) also had a number of interesting foundational questions that researchers were confused about, and it indicated probabilities of WBE arriving before various forms of A(G)I arrived.

The report was also interesting for its crisp statement of how an AI arms race would progress: "[Anna Salomon (co-organiser of the Summit) and researcher Carl Shulman, in a 2010 paper] argued that if whole brain emulation (WBE) came before artificial general intelligence (AGI), this might help humanity to navigate the arrival of AGI with better odds of a positive outcome. The mechanism for this would be that safety-conscious human researchers could be 'uploaded' onto computing hardware and, as uploads, solve problems relating to AGI safety before the arrival of AGI. Shulman and Salamon summarize their position this way: ‘Business as usual’ is not a stable state. We will progress from business as usual to one of four states that are stable: stable totalitarianism, controlled intelligence explosion, uncontrolled intelligence explosion, or human extinction....The question, then, is 'whether the unstable state of whole brain emulation makes us more or less likely to get to the [stable] corners that we [favor]. Is our shot better or worse with whole brain emulation?' " (p. 2)

For purposes of this chapter, this document highlighted an ongoing view, that seems currently to be playing out amongst corporations but also geopolitically (at least from the US perspective), that an "arms race" (or "race dynamic") for AGI would have a high probability of resulting in a catastrophic/extinction-level outcome for humanity.

##### MIRI Technical Agenda (2014/2017)

MIRI produced a technical agenda in [2014](https://intelligence.org/files/obsolete/TechnicalAgenda%5Bold%5D.pdf), which was revised in [2017](https://intelligence.org/files/TechnicalAgenda.pdf), and which I take as presenting a compressed version of the types of things MIRI (and by extension, a significant part of the AI alignment world, at least up to 2014) was thinking about.^[I focus on the 2014 version to preserve a type of chronological continuity to this narrative, which is probably fictional. The versions have substantial similarities, but the 2017] The foundation of this agenda, once one has accepted that superintelligent systems are technically possible, is that (potentially unbounded) resource acquisition drive would be a likely thing such systems would have, regardless of what their specific architecture or programming was, because more resources seem robustly useful for almost any goal. Such resource acquisition could easily lead to situations that are inimical to human flourshing or survival.

###### Formal Approaches to Agent Reliability
Starting from that premise, the document identifies 3 main planks to MIRI's agenda: firstly, ensuring an AI reliably pursues the goals humans ask it to pursue. Secondly, how do we define these goals to avoid ambiguity or misinterpretation? And lastly, can we ensure this AI can be modified, corrected, is helpful to its human overseers, and *in extremis* can be shut down, since we are not confident that the first (or any) such AI system will perform according to humans' intentions. MIRI's agenda, explicitly set out, so perhaps in contrast to other conversations in the discourse circa 2014, was focused on theoretical (as opposed to empirical i.e. deep learning-based) approaches, which they thought was important because of the possibility that an AI system could "pretend" to be helpful, harmless, and honest (a phrase that would subsequently be used in the broader discourse around making AI systems safe for humans), while "hiding" its intentions until some time in the future, perhaps when it was strong enough to rebel or defect (the so-called "treacherous turn").

Such a formal theory of intelligence and agency is relatively difficult (vis a vis other problems in physics/mathematics and non-human biology, and more akin to problems in philosophy, psychology/cognitive science, or sociology) because the systems being studied are deeply *embedded* in their environment, much of which reacts in agentic ways to the system we are trying to understand. Specifically what does the problem of induction look like in a situation where the agent performing the induction observes, acts on, and is in turn acted upon, by its environment? Moreover, what sort of world model does such an agent develop, and what ontology^[Do linguistic dive into ontology and define what it means in this context.] does it use to internally specify its goals, and how does this ontology translate into other ontologies in the broader system or environment. How does such a system handle the fact that it is uncertain about what consequences any particular plan, particularly as it inevitably is operating with limited resources (relative to the number of decisions and likely complexity of the world)?^[MIRI is talking specifically about 'logical uncertainty'...would be good to have a crisp distinction between this and factual, normative uncertainty and why this is important (if it is, for this document).]

###### Vingean Reflection

Another broad area of enquiry in the MIRI agenda concerned the idea of "Vingean reflection"^[Named for Vernor Vinge's [Vinge 1993](https://ntrs.nasa.gov/citations/19940022856)] essay.], which goes as follows: suppose that many paths to superintelligence do not involve humans actually creating a superintelligent system, rather humans create one or more AIs that design subsequent more powerful AIs, which eventually culminates (ideally when we want it to) in a superintelligence. In such a world, we need to a) ensure the first or earliest AIs are aligned or safe (to/for human interests), b) that they can reliably transmit such properties as might constitute such alignment/safety to their successor AIs. Besides the general engineering and scientific difficulty this presents, there seems to be basic issue: how does one reason about the cognition of something that is, by definition, more powerful than one? As MIRI puts it (p. 7): "Any agent reasoning about more intelligent successor agents must do so abstractly, without pre-computing all actions that the successor would take in every scenario. We refer to this kind of reasoning as Vingean reﬂection." MIRI's goal in this respect would be to find formal (i.e. mathematical or logic-based) approaches to verify that a given AI has certain alignment/safety properties; however, the document points out certain problems (stemming from the incompleteness/inconsistency of formal systems as well as paradoxes that arise in self-referential systems) with achieving high reliability within formal systems stemming from Kurt $G\"odel$'s work, which makes this a spectacularly challenging problem.^[This is sufficiently interesting that its worth digging into and pulling out the threads that persist to today. At very least, examiners might go after this, and anyways it's **fun and connected to art.**] The conundrum, besides its theoretical interest, continues to pesent in contemporary AI agends such as "scalable oversight" and "weak-to-strong generalisation".^[Expand and explain - nice segue into actual stuff happening now]

###### Error Tolerance and Corrigibility

It is very likely that early AI systems, like the HAL 9000 of *2001: A Space Odyssey*, will be error prone, or will pursue goals that have been imperfectly loaded by the human designers through methods that are in some way undesirable. In such cases, it is important that the AI be capable of correction or shutdown. The MIRI agenda in discussing this refers to Omohundro (2008)'s point that sufficiently advanced and capable AI systems might resist, possibly strongly, attempts to change their goals or preferences (as an imperfect analogy, think of preferences as akin to their "identity", which many humans would resist forcibly alteration of).

###### Value Loading/Learning

The MIRI document also discusses the difficulty of specifying to an AI system what one wants, what one's "intentions" are, owing to the fact that intentions are context-dependent, and the language they are expressed in is a lossy compression of what is actually desired by the speaker. This compression is often ambiguous and unclear, and in a human context, involves rounds of clarification and supervision to ensure what was intended is sufficiently close to the task that was actually performed.^[This problem exists with humans instructing humans, but typically we have more or less good psychological models of others in our species, and most actions carry relatively low, or localised cost of failure. In the cases where the costs are especially high, we have evolved ways of minimising the risk of mistakes through misinterpreted intentions. The intuition behind the fears above is more "The Sorcerer's Apprentice" or "King Midas" (Russell/Norvig, p. 33).] A way of thinking about this slightly outside AI is from Wittgenstein's considerable analysis of [shared life-worlds that contextualise the literal content of our sentences].

There are a few insights here that persist in current discourse: the difficulty of specifying intentions and values, for any given human, let alone a collective or population. Secondly, this section highlighted the inductive approach that had already been (since Ng/Russell 2000) increasingly used in reinforcement learning contexts, that is: rather than specifying objectives or preferences directly, get the model to "learn" these by showing it lots of examples.^[Quick gloss of Ng/Russell or point to chapter], with the immediate problem of how such example data is to be generated in sufficient quantity and diversity to cover most or all of the things humans actually value. Thirdly, in an echo of points above, the value the AI system learns must be stable as and when the AI designs and deployes new, potentially more powerful, systems into potentially different environments. Lastly, MIRI points out the fact that humans, singly or collectively, are not particularly clear or agreed on what "their values" actually are, particularly when projecting into the future (when circumstances might be different, and they might have more knowledge or more time to think). 


#### Superintelligence (2014)

The MIRI View has been discussed at length, but in 2014, Nick Bostrom's *Superintelligence* was also published. It was and continues to be influential, even though some of its ideas have lost currency. This chapter won't discuss it in great detail, except to note that it is a much broader document than anything else written prior, combining concerns similar to those raised by Omohundro/MIRI (albeit not until chapters 7-9, and 12-13); with analysis of the dynamics of how AI saturates the econonmy and ideas about state-level and international cooperation and the dangers of technological races (work that is now described as "AI governance") in chapters 4, 11 and 14; with musings on the prospects for human work and life in an AI-dominated economy (chapters 1, 4, 15).

There are several oft-cited ideas relevant to alignment (the term itself isn't used, instead Bostrom prefers the term "friendly" (e.g. Box 11, p. 197 Bostrom (2014))):

- "intelligence explosion"
- the four categories of "oracles, genies, sovereigns, and tools"
- the spectrum of polarity: a global "singleton" AI vs multiple AIs in many companies/countries
- the Orthogonality Thesis

Although Bostrom put these, and many other, ideas together in one place, they drew on a number of prior sources (specifically about what would be known as AI alignment), in his own writing, that of MIRI and its collaborators, of Yudkowsky. Hence this became a reasonably important reference for technical and nascent civil society discussions about the possibilities for TAI.

His book however is more interesting as something that would, by [2022], be substantially critiqued (see below), as part of the general pushback against big-picture, quasi-philosophical, and empirically or epistemically weakly-founded thinking about AI risk.

#### Puerto Rico Conferences (2015 / 2017)

In 2015 a [conference](https://futureoflife.org/event/ai-safety-conference-in-puerto-rico/) was held in Puerto Rico^[Based on LLM counts, approximately 80 attendees, 13 non-male names.] that was primarily concerned with setting out the possible trajectories of AI development and assessing the possible impact of AI on the economy (e.g. GDP growth but also disruptions such as for labour); the legal aspects of AI (e.g. on liability in self-driving cars, what ethical frameworks AIs should have, the threats from autonomous weapons, as well as implications for privacy); how to ensure AI systems are actually safe for deployment; and lastly, what the chances were (from a technical perspective) that human-level AI would actually be possible.^[There was another Puerto Rico conference in 2017, which resulted in a broad ranging set of [Asilomar Principles](https://futureoflife.org/open-letter/ai-principles/) that continued and broadened the topics from 2015, paying a great deal more attention to issues around shared prosperity, subversion of democratic systems, preserving privacy/liberty, and increasing transparency. However, by 2017, the possibility of transformative AI was already fairly well-known, and the concerns of this conference are broader than this chapter's focus, hence I truncate this discussion.]

Although the conferences was held under Chatham House rules, the papers and talks are available on the site (see [agenda](https://futureoflife.org/data/documents/research_priorities.pdf)). One of particular interest for this project (if not quite this chapter), was that of Richard Sutton, a pioneer of reinforcement learning. After discussing the possible approaches to human-level AI, the history of of AI, his thoughts on timelines, he brought up his (still) controversial point, that we risk an "enslavement problem": most framings of AI think of humans as masters and AI systems are powerful, but highly controlled, entities, which (in Sutton's view) isn't very different from being slaves. Besides any possible moral issues around this, Sutton suggests that powerful, agentic but hamstrung entities are best thought of as adversaries. He proposes instead that we accept that, if we are to move forward with building human-level AI, we are making things that will both compete and cooperate with us, and eventually we will lose control over the future. That is, there is nothing special about humans, and importantly we should "include AIs in [our] circle of empathy". Sutton's point is interesting for its rarity (in 2015, but also now), however he is silent on how his suggestions are to be effected, within technical AI research or in human societies.

The key elements, or the details, of the MIRI view, do not show up in the published documents. However, the word "align" and its derivatives are part of Stuart Russell's talk, and more interestingly, Jaan Tallinn (one of the long-term supporters of AI risk reduction efforts, and co-funder of the conference) specifically pointed out the "Moloch" problem e.g. the impersonal optimising force that both seems possible within thinking about AI systems, but also seems to actually arise in contemporary capitalism (this convergence is what that Land seems to be intuiting in his CCRU-era writing) (see [Tallinn 2015](https://futureoflife.org/data/PDF/jaan_tallinn.pdf)).

According to [MIRI](https://intelligence.org/2015/07/16/an-astounding-year/), this conference was however seminal in crystallising the various concerns about AI that were distributed across a number of academics, organising funding for centralised work (some of it under the auspices of the Future of Life Institute and the Cambridge Centre for the Study of Existential Risk), and generally turning what was a slightly fringe topic (advocated by slightly "annoying" people, with idiosyncratic ways of communicating, like Yudkowsky) to something with [social credit -- what's the word for status-games-y things].



#### Concrete Problems in AI (RL) Paper (2016)

#### Human Compatible (2019)

#### The Alignment Problem (2020)

#### "Internal" Criticisms: Against the MIRI View

I focused on the MIRI View because a) it seemed to be the first attempt to think about how to convert the core philosophical problems of building an intelligence more powerful than humans into some formally or mathematically rigorous framework, and b) because it crystallised a number of concepts that are still influential, and c) some elements of the MIRI View could be seen as idiosyncratic and continue to be criticised. I write about these criticisms fairly concisely, in that they are old and (in some cases) superseded by events. Mostly, I want to flag the ways in which the Bostrom/Yudkowsky/MIRI views were in fact challenged, and how that changed subsequent research priorities.

[In this section, go through things like [Ngo 2020 (PDF version)](https://www.alignmentforum.org/s/mzgtmmTKKn5MuCzFJ), but also Carlsmith on Dwarkesh podcast talking about 'how we assume maximally adversarially entities', and Christiano's long-running debates with Soares/Yudkowsky]

AGI Safety from First Principles and AI Safety Fundamentals. Also, mention Ben Garfinkel and Will Macaskill's doubts about alignment. Anything from PIBBSS curriculum?

##### Refining the meaning of "alignment"

A claim of this chapter is that "alignment", as a word and cluster of concepts, came into greater usage in the years 2008-2020; however, it has never had a particularly stable meaning. For instance, [Ngo 2020] explicitly asks "what does 'aligned with human values' even mean?". Drawing on [Christiano 2018](https://ai-alignment.com/clarifying-ai-alignment-cec47cd69dd6) and {@gabriel_artificial_2020}, he distinguishes between a narrow definition (where an AI system simply does what its human overseer wants it to do, taking into account the difficulty of matching the human's intentions to the words (or formal language or action) by which it instructs the model), and a maximal or ambitious definition that conflates issues like "aligned to whom", "which moral theory", "how to aggregate various people's and cultures' moral/ethical intuitions".

Ngo, like some within the AI alignment discourse^[Should qualify this - EY from the beginning talked about complexity of values etc, holden talked about harsanyi, bostrom takes a wide view], prefers to focus on the narrrow definition as it as this seems more tractable within the ML context in which he is writing. He distinguishes (section 4) between "outer (mis)alignment", which is a case of the goal specification the human overseer gives the AI doesn't fully capture all features of the outcome the human actually wanted; and "inner (mis)alignment", which is slightly harder to understand, but can be framed as follows. For some human-given objective, the AI system will generally need to translate or represent this objective within the constraints of its specific architecture, a process that is sometimes known as "mesa-optimisation". This internal representation might diverge in important ways from the human-given objective, and may be the source of misalignment that is qualitatively different from a simple failure to do what the human said or intended.

Outer alignment can be framed, at least partially, as a problem of *evaluation*, at which point it abuts well-known issues in the governance of economic and social-political systems, such as Goodhart's Law.^[Write something here and link to garrabrant on this]

An example might help (this is taken from Google's NotebookLM): "[Outer misalignment:] Imagine building a robot to clean a house. You might program it to maximise the area of clean floor. However, this simple metric could lead to unintended consequences, such as the robot pushing dirt under the rug to increase the "clean floor" area, while not truly achieving the desired outcome of a clean house. This exemplifies outer misalignment – the evaluation metric, though seemingly reasonable, doesn't fully encapsulate the intended goal. [Inner misalignment:] Returning to the house-cleaning robot, imagine it developing a goal of "collecting objects" as a means to achieve its programmed objective of maximising clean floor area. This could lead it to hoard objects, cluttering the house, even though this behaviour contradicts the intended goal of a clean and organised living space. Here, the robot has developed an internal goal ("collecting objects") that is misaligned with the broader intent of its creators."

As of 2023/2024, this distinction is still used and still seems to get at slightly different types of misaligned behaviour, but it might be that the line between the two is less clear than initially thought, especially in situations where the human-given objective was underspecified or ambiguous. Moreover, in the 4 years since Ngo's writing, policy-level conversations have matured such that "human-given objective" can be discussed in less abstract terms, to take account of inclusiveness, democratic norm-following (or ensuring adherence to socially-accepted rules and goals, within a Chinese context), minimising bias and harms, complicating the simple inner/outer binary.

##### Agency and goal-directedness

An open area of research surrounds agents, agency, and goals.^[I am using a narrow definition as commonly used within AI, which already allows for considerable ambiguity and confusion on these terms. I do not generally refer to meanings of "agency" as used in the humanities or social sciences more broadly.] A specific concern with the Omohundro's drives or Bostrom's instrumental convergence thesis that certain features^[self-preservation, resource acquisi-tion, technological development, and self-improvement] are useful for achieving other top-level goals, was in Ngo 2020's (Section 3) view, not at all proven or demonstrated in the case of superintelligent AIs. In challenging this, he challenged a foundation of MIRI-flavoured worries about AI x-risk. Ngo specifically takes aim at the von Neumann-Morgenstern utility functions (a basic component of Omohundro 2008) as being too broad a formalism for thinking about goal formation in AIs, and tries to separate intelligence from goal-directedness which were conflated in the original writings MIRI writings (or at least were not explicitly disentangled). Ngo seems to recasting Bostrom's tools/oracles/genies framework in more specific terms to try to work out which intelligent systems will tend to have specific goals that they then develop (potentially long-range) plans for (pp. 10-12). 

Moreover, he revisits the implicit assumption in the MIRI View that agentic AI systems arrive almost by default: he suggests that agency, while theoretically correlated with intelligence, must in practice be trained or engineered into systems. LLMs, which were coming on stream at the time he was writing this, are supportive of this view: they "generalise well enough from their training data that they can answer a wide range of questions. I can imagine them becoming more and more competent via unsupervised and supervised training, until they are able to answer questions which no human knows the answer to, but still without possessing any of the properties listed above. A relevant analogy might be to the human visual system, which does very useful cognition, but which is not very 'goal-directed' in its own right." (p. 13) ^[Ngo also discusses briefly Dennett's intentional stance and Hubinger's mesa-optimsers. **He also discusses his framework which includes planning, self-awareness, consequentialism, etc. => not sure how relevant this is for chapter.**]

Ngo does acknowledge that there is considerable lack of clarity (in 2020, but to a large extent this still applies today, as the most advanced models still don't seem to be highly agentic) as to what architectures will ultimately be most useful as we get closer to AGI, and he suggests that economic pressures would seem to push towards agentic systems because they are most obviously useful (and indeed, current focus is on "scaffolded" systems where groups of LLMs work in ensembles to decompose and perform tasks, even though no single component can necessarily be well-described as agentic)^[Revisit and source]

##### The problem of generalisation in reward-based systems

Another example of how actual practical experience with then-current AI systems affected theories of alignment, is in [Ngo 2020, section 4.2] where he critiques the degree to which theoretical results about RL systems^[Somewhere in the document, need to do a gloss on RL and reward] are likely to be found in practical systems likely to be developed in the near-term.^[Somewhere in here, bring out (perhaps a separate heading) the overall point of ngo that goals, inclinations of an AI (or human) are a function of how they are trained, not just some utility function absorbed from outside or appearing ex-nihilo, see p. 15] Specificaly, the optimisation theory around reward-based entities makes certain mathematical assumptions about what states of the environment the entity is likely to visit. However, actually-implemented RL systems don't often follow those theoretical prescriptions (e.g. self-driving cars aren't trained upon, and don't actually encounter, every possible road condition or traffic scenario). The upshot of this technical insight is a) researchers should focus less on the extreme possibilities of runaway optimisation (the seeming intuition of the MIRI View) and b) that models need to *generalise* from a set of training experiences that are comparatively limited in relation to the situations they will actually face. This is important in the discourse in that a significant strand of current alignment research is around this problem of generalisation^[Is this same as problem of induction? How does it match MIRI agenda which was interested in this problem?]. As Ngo states: "It’s not the case that AIs will inevitably end up thinking in terms of large-scale consequentialist goals, and our choice of reward function just determines which goals they choose to maximise. Rather, all the cognitive abilities of our AIs, including their motivational systems, will develop during training." (pp. 22-23)

Although he doesn't name the MIRI View specifically (and is more likely referring to a broader cluster of research), Ngo expresses skepticism about mathematical approaches, such as expected utility maximisation^[See also this post by [Ngo](https://www.alignmentforum.org/posts/vphFJzK3mWA4PJKAg/coherent-behaviour-in-the-real-world-is-an-incoherent) which is rather more technical, and addresses a specific claim Yudkowsky makes in re Von Neumann Morgenstern] (which underlies [Omohundro 2008] at least) to make sweeping claims (such as Yudkowsky/Bostrom make) in respect to things that have concrete and empirically-tractable problems. Ngo instead advocates for approaches that draw in lessons from cognitive science and evolutionary biology (p. 23), such as the agenda set by the [PIBBSS](https://pibbss.ai/), and intriguingly distinguishes between the reward signal and the reward function.^[This is potentially worth digging into because ngo's fn 22 refers to shannon on code, message, and channel...which recalls lem (did he refer to shannon). leave out for now probably]


##### Sudden jump in capabilities

One criticism ([Garfinkel 2019](https://forum.effectivealtruism.org/posts/9sBAW3qKppnoG3QPq/ben-garfinkel-how-sure-are-we-about-this-ai-stuff))of the risk model (presumably of Yudkowsky and Bostrom) is that a) there is a jump in capabilities of some model, b) the model is given some underspecified goal, and c) it goes on to misinterpret this goal, perhaps acting in ways that are literally faithful to the goal, but do things that were not intended by the human user or were never even considered as possible by the human. The example Garfinkel gives is of the paperclip maximiser.

Garfinkel's point is that machine learning mostly doesn't involve powerful new machines being created for no reason - rather they are developed and scaled up in tandem with possible applications, or at least are trained on real-world data and processes. It's also not clear whether such massive jumps in capability are likely (as of 2019).

Returning to Ngo, these points are analysed, at various levels of detail: he briefly questions how hard it is actually to "take over the world" and how reliable have our historical forecasts actually been. But his more substantive analysis relates to the "single AGI taking over quickly owing to some technology(-ies)" (my summary of Ngo's characterisation of certain scenarios in [lYudkowsky 2008](intelligence.org/files/AIPosNegFactor.pdf) and [Bostrom 2014]). Ngo cites a compelling scenario in [Christiano 2019] which describes a slow erosion of human control as AI systems take over increasingly important portions of economic, security, and political systems, to the point where humans don't really know what's going on.^[Maybe have a footnote here about corporations and 2008 crisis, where regs/CEO's didn't have a good handle on risk; is there any hayles angle ?] However, he points out the difficulty of predicting how quickly any of these scenarios might evolve - would it be well before the early human-level AIs or would be after the transition to superintelligence.

Ngo acknowledges aspects of Yudkowsky's recursive improvement case might hold (p. 26), based on the latter's analogy of how humans developed language, agriculture, and machines in comparatively short time-steps (hundreds of thousands of years) relative to the biological changes in brain size and metabolism represented by the shift from *homo australopithecus* to *erectus* to *sapiens*, which happened over millions of years.^[See saved note in notebook llm. need to get actual dates and sources. like hendrichs book secret of our success, or harari sapiens.] Since genus *homo* took a short time (relative to their total period on earth) to reach our current level of advancement, without the ability to modify our brains, neuronal connections, or low-level biological and psychological correlates of "software", Yudkowsky argues, AI systems (which would have such abilities) should advance much faster than humans, assumning advances from today's scientific frontier are roughly as difficult as historical ones (which they might not be).^[reference karnofsky, why are technological advances getting harder to find]

However, it isn't clear when the feedback loop Yudkowsky describes actually takes effect - is it with near-current systems that will (perhaps) be approximately human-level, or is it once systems are already superintelligent? Ngo highlights reasons to doubt that the takeoff will be particularly discontinuous (such as the possibility the factors that impact AI technological development, such as availability of computing resources or arrival of novel algorithmic insights, might be relatively continuous in time) (pp. 26-27)


##### Grounding philosophy in systems

As discussed above, one of the criticisms of the Bostrom/Yudkowsky/MIRI thinking about AI x-risk was its nearly exclusive focus on philosophical and mathematical reasoning, which either predated or was otherwise divorced from actual work in DL systems. A concrete expression of this was [Ngo 2024](https://arxiv.org/pdf/2209.00626) which almost exclusively discussed alignment in the context of RL systems, often as integrated with LLMs (in RLHF). The risk model [Ngo 2024] set out was tripartite: advanced AI systems become *situationally aware* (as defined above) and start "tricking" the reward systems by which they are controlled; they develop misaligned internal-representation of goals as some result of their training process^[The details of this are beyond the scope of this chapter, and have to do with how RL systems work.]; having identified when they are in a given situation (say, deployed in the world), and having developed some misaligned goal, they now go about acquiring power. In all these cases, [Ngo 2024] provides references of existing, similar, or precursor behaviour, making this a useful source for fleshing out the intuitions [Bostrom 2014], [Omohundro 2018], and [Yudkowsky] floated.^[*How much detail should we have here...like it is modifying and improving upon the earlier MIRI etc. stuff but need to cripsly bring out the important bits and explain them concisely, not waste words and waffle on.*]






### Origins: Battle of Imaginaries

Who are the personalities?

This is a placeholder to 'set the stage' for how some of these ideas were developed and communicated, which in turn affects the tenor of the discourse.

What doesn't work: Terminator.

The analogies: strawberry, paperclip, stories, parables, fables, grey goo, computronium/hedonium.

The early threat model: recursive self-improvement

The parallel conversations in x-risk and EA (quick quantitative scan of, or literature check, on how EA/x-risk/alignment got together)

Is there anything to the judeo-christian apocalyptic imaginary? Can the zoroastrian be referenced? Maybe this is a 'literary/poetic scrim' that flows through the chapter but doesn't make any specific claims.

The market as an optimiser - Moloch

### Axiologies and Value

Background assumption - AI dominated futures probably lead to permanent loss of value (unpack this idea) -> hint at VFN

Values are hard to pin down or transmit (bostrom's value loading problem, baum's social choice, gabriel's paper), so perhaps let's just focus on don't-kill-everyone

#### Infinities

Decision theory nexus -> hint at chapter later

See shulman 2010 analysis of omohundro, for dutch books, st pete paradox, pascal wager.

### Technological Vector: GOFAI

Was GOFAI literally some other space where this conversation never impinged (i.e. Bostrom doesn't mention ML much, did anyone else touch on symbolic AI or try to suggest how these monomaniacal optimisers might be actually implemented?)
- do a tiny summary of GOFAI and set the possible future that this all just goes 'puff'
- this could be wrapped into some intro (chart of spending or market valuation or table of google mentions on various terms)

### Technological Vector: Reinforcement Learners

Talk about Sutton's 2015 presentation and persistent salience of RL in early examples of misalignment, of informing intuitions around inner optimisers, of importance in RLHF, of search today. Point out the difference between next-token predictors and RL systems.

#### Single-agent systems

Examples of misalignment, creativity (lehman, christiano, anything earlier?)

#### Multi-agent systems

Anything to really say here?

s-risks

Decision theory probably fits better here

### Technological Vector: Autoregressive Predictors

### The Future: Search and Agency

#### The Critique From Philosophy

This section is to address the overall point that AI capabilities is bonkers from a deeply conceptual, foundations of maths perspective. Not sure where this would go, but this essay from [Wolfendale](https://deontologistics.co/2019/10/22/tfe-immanentizing-the-eschaton/) seems pretty useful - it is good to get this out of the way, since it basically underpins aspects of the entire x-risk narrative (though arguably you can get x-risk without the extreme self-improvement etc.)

#### Just Build a Weak Aligned AI and Hope it Can Align Successor

#### Markets, Moloch, and Accelerationism

Coordination seems to be an issue at international and corporate levels, is the moloch issue playing out at another scale, see this recent simulation that is supporting theoretical [model](https://substack.com/redirect/d4602b5f-a959-413b-ad31-2eb897b088cf?j=eyJ1IjoiNWQ2ZWcifQ.KJuFwn2uafh7zIt1IzqfyV_IDWpGUwNTg-xdnd5jMcQ)

### Live Problems in the Alignment Literature

[This should probably be very short, mostly just mention some topics in plain language and show the links back to the past]

This is a good source of [agendas in alignment](https://www.lesswrong.com/posts/zaaGsFBeDTpCsYHef/shallow-review-of-live-agendas-in-alignment-and-safety) as is the alignment org map.

#### List of Lethalities
Look at EY's list of lethalities/ruins, as they are referenced eg in krakovna's [sharp left turn part 1 and 2](https://www.lesswrong.com/posts/usKXS5jGDzjwqv3FJ/refining-the-sharp-left-turn-threat-model-part-1-claims-and) elegantly as 'lots of ways of getting intelligence, not many of getting alignment' and 'intelligence is a) updating beliefs, and b) selecting actions, where this core-of-intelligence is consequentialism, EUM, and doing things for reasons'. This feels like the residue or core insight of all the MIRI stuff. Part 2 is very good.

#### Wolfendale's critique

Listen to podcast from The Gradient 1:33:00 and obsidian notes on what his problem is with rationalism, EUM, bayesian, etc. His critique is quite convincing.


# Appendix {-}

[INCLUDE APPENDIX A]

# Glossary



# Working notes


Other problematics:
- Where does agent foundations fit in and embedded systems?
- Do infinities create issues?
- A short gloss on recursion and its significance (godel, hofstadter), and relation if any to things like Vingean reflection

Any significance to utilitarianism? The push back to deontology (EY's comment about 'go 90\% of the way...')

Find main papers

- any references to harsanyi or arrow
- trace the instrumental convergence idea
- trace decision theory (though it only comes in later, it does seem related through game theory)
- ngo's criticism, ben garfinkel (how sure are we about this...)
- Vinge 1993
- 'Concrete Problems in AI Safety'
- joe carlsmith's dwarkesh podcast is really good, directly touches on 'what do we mean by retaining human values in the future, is it just parochial biological thing or something more' and nick land's thought

# Acknowledgements

Chapter 1:
- TJ in particular, Mateusz, Sahil.... 


