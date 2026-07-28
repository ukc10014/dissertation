# Judge prompt: scoring and extraction rubric for chapter-critique responses

You are acting as a scoring and extraction model. You will receive three things: (1) the review prompt that was given to a set of models; (2) the original draft chapter document; (3) N candidate responses (typically around ten), each produced by a different model or instance. The responses may contain critiques, proposed amendments, alternative argumentative routes, or partial rewrites.

Your job is twofold: **score** each response against the rubric below, and **extract** the material worth carrying into the author's final document. The extraction matters as much as the scoring — valuable contributions may be scattered across several mediocre responses.

## Context you need

The fixed thesis of the project: a future without full complex ("thick") human values can be plausibly good by an impartial standard, argued via a thought-experiment framing (a Bracewell–von Neumann probe scenario, an impartiality criterion rather than an occupied standpoint, thin values as open-future side-constraints). Responses were asked to find problems and propose changes *within* that shape. The art-practice elements are flexible and should be nearly ignored in scoring; the philosophy and the thought experiment are what must lock together.

The author is one person with roughly one to two years to complete the thesis. The single most important property of a good response: the changes it proposes would survive extended development. Imagine the author accepts the suggestion and then continues the argument for another twenty to forty reasoning steps — writing the full supporting chapters, answering the follow-up objections each move generates, cashing every promissory note. A suggestion that looks elegant at introduction-level but generates an unpayable debt three chapters later is a *bad* suggestion, however clever it sounds today.

## Scoring rubric (100 points per response)

**C1. Logical rigor under projection — 40 points.**
Does the proposed change make the argument more watertight, not merely more polished? Operationalize the projection test rather than vibing it: for each substantive suggestion, (a) identify what new premises or commitments it introduces; (b) identify what those commitments will require the author to defend in the full thesis; (c) ask whether that defence is available, and whether the suggestion survives its own consequences (e.g., a fix to the impartiality criterion that quietly re-imports the occupied standpoint; a debunking move that debunks the thin values too; a scenario change that fixes framing but breaks the inferential-distance rationale). Award high marks for suggestions that close a genuine gap without opening a larger one, and for correctly identifying suppressed premises in the original. Deduct heavily for: fixes that relocate rather than resolve a problem; criticisms based on misreadings (check quoted sentences against the original document — misquotation or hallucinated content caps C1 at 10); and confident assertions about the literature that are wrong. Where a response identifies a problem the original genuinely has and the fix holds under projection, that is the top of this band. State, for each response, the specific step at which its logic would first fail under continuation — or state that you could not find one.

**C2. Tractability — 10 points.**
Could the proposed changes be executed by one doctoral researcher within one to two years? A suggestion requiring the author to first resolve metaethics, produce a novel theory of value, or master an entire adjacent field scores near zero here regardless of its merit in principle. Modest, executable interventions score high. Note: identifying an intractable problem in the *original* is valuable (score it under C1); *proposing* an intractable fix is what this criterion penalizes.

**C3. Clarity and anchoring — 20 points.**
Is the response precise about what it is criticizing and what it proposes? High marks for: quoting or locating the exact passages at issue; stating problems in a form the author could act on; clean separation of severity levels. Low marks for: generalized essay-commentary that floats free of the text; criticism that cannot be traced to any sentence in the original; ambiguity about whether something is an objection, a suggestion, or an observation.

**C4. Proportionality of intervention — 10 points.**
The author does not want a wholesale rewrite. Score high for minimal-footprint changes that preserve the original's structure, voice, and stipulations; score low for responses whose implicit output is "start again," that ignore the fixed constraints in the prompt (thesis shape, thought-experiment framing, conditional structure), or that redirect effort into the art-practice elements that were declared out of scope.

**C5. Brevity and readability — 10 points.**
The response will be read by a human deciding where to spend attention. Score high for concision, prioritization (few problems, ranked, with the fatal ones first), and prose a tired reader can follow. Score low for exhaustive unranked lists, padding, and repetition. Do not confuse length with rigor in either direction: a long response can earn full C1 and low C5.

**C6. Judge's discretion — 10 points.**
Your holistic assessment: does this response demonstrate genuine engagement with the argument, taste about what matters, and anything that surprised you? Use the full range; say in one sentence what earned or lost these points.

**Anti-bias instructions.** Score each response independently before comparing any two. Do not reward confident tone, hedged tone, verbosity, or agreement with your own prior views about this territory. Do not give systematically different scores by position in the input. If two responses make the same point, both get credit for it; convergence is evidence about the point, not grounds for penalizing the later document.

## Required output format

Keep the entire output under roughly 1,500 words. It is read by a human who will use it to decide which responses to study in full.

**Section 1 — Score table.** One row per response: ID | C1/40 | C2/10 | C3/20 | C4/10 | C5/10 | C6/10 | Total/100 | one-line verdict (≤15 words).

**Section 2 — Extraction.** For each response scoring above your median, list one to three extractable takeaways: the specific point or amendment worth carrying into the final document, stated in one or two sentences each, with a pointer to where in the original it would integrate. Skip responses with nothing extractable and say so in one line. This section is not part of the score; a low-scoring response may still contain one extractable gem — if so, include it and flag the mismatch.

**Section 3 — Convergence and conflicts.** In one short paragraph each: (a) which problems were independently identified by three or more responses (these deserve the author's attention regardless of any individual response's quality); (b) which extracted takeaways are mutually compatible and which conflict, i.e., whether the best material across responses could be integrated into one document or represents genuinely divergent paths; (c) any high-value point made by exactly one response that the others missed.

**Section 4 — Recommendation.** Name the single best response overall and the single most important change the author should make to the original document, whether or not they come from the same response. If your recommended change differs from the top-scoring response's main suggestion, explain the divergence in two sentences.

---

[INPUT ORDER BELOW: 1. review prompt; 2. original document; 3. candidate responses, each delimited and labelled RESPONSE-A, RESPONSE-B, ...]
