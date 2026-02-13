# Notes: Integrating Cosmic Host v1.4 Additions into the Dissertation

**Date:** 12 Feb 2026
**Context:** These notes capture Claude's analysis of what `cosmichost_v1.4.md` adds over `lw_cosmichost_final_v1.3.md`, and how those additions should feed into the dissertation chapters (primarily ch_03 / the theoretical analysis chapter and the LLM experiments chapter `ch_03_reorg.md`).

**Why this document exists:** The conversation context where these integration points were first discussed was about to be compressed. This is a durable record so Kanad can compact that session and pick up the integration work later.

---

## 1. What v1.4 Adds Over v1.3

### 1a. "Rationality in the Space-of-Minds" framework (entirely new)

v1.3 jumps fairly quickly into cosmic norms content (substrate-neutral norms, suffering, "is it up to us?"). v1.4 inserts a substantial new section *before* the cosmic host analysis that distinguishes three types of rationality:

- **Ecological rationality** — niche-adapted intelligence (slime mould, swarms, cephalopods)
- **Game-theoretic rationality** — cooperation as a low-level computational solution
- **Philosophical/moral rationality** — the moralised sense (Kant, Korsgaard, Scanlon)

This is valuable because it makes explicit something v1.3 left implicit: Bostrom's argument quietly assumes philosophical rationality is convergent across minds, but ecology shows that intelligence routinely exists without it.

**Integration note:** This three-way distinction should anchor the theoretical chapter (ch_02 or wherever the Bostrom analysis lands). It's the backbone of the "questioning convergence" argument.

### 1b. Minimal Large World Subset (MLS) — new concept

v1.4 proposes a minimal set of norms plausibly selectively favoured across diverse intelligences:
- Epistemic fidelity
- Impartiality (scale-sensitive moral weight)
- S-risk priority
- Large-world cooperation
- Caution / reversibility

This is a constructive contribution that v1.3 doesn't have. It gives a positive answer to "well, if rationality isn't convergent, is *anything* convergent?" — and the answer is: maybe this minimal set, but notably it's thinner than what Bostrom or the alignment community typically assumes.

**Integration note:** The MLS concept directly feeds into the moral parliament experiment design in ch_03_reorg. It could serve as one of the delegate positions (a "minimal cosmopolitan" delegate). It also connects to the SMUCWUF framing already in ch_03_reorg.

### 1c. The "Fun Remainder" (FR) — new concept

v1.4 develops an extended analysis of what's left over after ecological + game-theoretic + minimal moral rationality: the aesthetic, experiential, process-oriented dimensions of human life (play, awe, wonder, ongoingness). This draws on:
- Yudkowsky's Fun Theory / Complexity of Value
- Alva Noë (play, art as attention-organising)
- Kieran Setiya (atelic vs telic activities)
- Helen de Cruz (awe/wonder as epistemic drivers)
- Peter Wolfendale (aesthetics as the source of terminal goals)

And then asks the critical question: is the Fun Remainder just biological baggage promoted as The Good? Are Eliezer's concerns about a "lightcone without fun" special pleading for our form-of-life?

**Integration note:** This is arguably v1.4's most original contribution. It connects the cosmic host analysis to Wolfendale's broader philosophical framework (aesthetics as the locus of terminal-goal formation), which is clearly important for the dissertation's overall argument. The FR/Wolfendale material should be prominent in the theoretical chapter. The "whence terminal goals" subsection (v1.4 lines 107-113) is particularly strong — it offers a causal story for why aesthetic capacity might be constitutive of general intelligence rather than mere anthropomorphic ornamentation.

### 1d. Expanded astrobiology and alternative ETI models

v1.4 significantly expands the discussion of non-expansionist civilisations beyond what v1.3 had:
- Lem's "encystment" / merging with environment (from *Summa Technologiae*)
- Haqq-Misra & Baum on ecological constraints on colonisation
- Smart's Transcension Hypothesis (black-hole dwellers)
- Ćirković on consciousness as evolutionarily contingent (may atrophy in advanced civs)
- Sandberg et al. on aestivation hypothesis
- Dark Forest hypothesis

v1.3 had some of this but v1.4 is much more thorough and makes the argument stronger that "who's in the cosmic host?" is genuinely uncertain.

**Integration note:** The Ćirković point (consciousness as contingent, potentially atrophying) is philosophically significant and connects to the broader dissertation theme about whether "human values" are the right target for alignment. This should be in the theoretical chapter.

### 1e. Appendix on acausal trade / "is there a bargain to be done?"

Entirely new in v1.4. Frames humanity as "cosmic midwives" with potential acausal bargaining power. Three considerations: leverage, continuity (chain of value-preserving commitments from current models through AGI to ASI), cheapness (preserving humanity costs virtually nothing at cosmic scales).

**Integration note:** This is speculative but interesting, and connects to the LLM experiments (can current models serve as the foundation for a chain of commitments?). Probably belongs as an appendix or discussion section rather than core argument.

### 1f. LLM experiment proposals (expanded)

v1.4 has two concrete experiment proposals that v1.3 only gestured at:
1. **Moral parliament with cosmic-norms dial** — sweep delegate weights from 1% to 90% cosmic-host deference
2. **Curious agent forming its own terminal goals** — LLM + RL agent + scratchpad, no specified goal

**Integration note:** These are already partially absorbed into ch_03_reorg's design. The moral parliament experiment is clearly being developed there. The curious-agent experiment may be out of scope for the dissertation but could be mentioned as future work.

### 1g. Appendix on empirical support for rationality in AI/alignment

Large new appendix surveying alignment literature on convergence, power-seeking, deception, alignment faking, the "bliss attractor" in Opus 3, etc. This is the empirical grounding for the theoretical claims.

**Integration note:** Parts of this are already reflected in ch_03_reorg (bliss attractor discussion, Opus 3 vs Opus 4 comparison). The rest should be checked for material that belongs in the theoretical chapter's literature review.

---

## 2. Suggested Integration Strategy

The v1.3 text currently forms the basis of the theoretical analysis (it's cleaner, more focused, publication-ready prose). The v1.4 additions should be integrated as follows:

1. **Rationality framework (1a) + MLS (1b):** Integrate into theoretical chapter as a new section *before* the cosmic host analysis. This sets up the conceptual machinery for questioning convergence.

2. **Fun Remainder + Wolfendale (1c):** Integrate into theoretical chapter as a section on "what human values actually are" that bridges the rationality discussion and the cosmic norms discussion. This is where the dissertation's original contribution is strongest.

3. **Expanded astrobiology (1d):** Merge into the existing "who's in the cosmic host?" section of v1.3, selectively. Don't need all of it — the Ćirković and Smart points are most philosophically interesting.

4. **Acausal bargain (1e):** Keep as appendix or discussion section.

5. **Experiment proposals (1f):** Already being developed in ch_03_reorg. Cross-reference.

6. **Empirical appendix (1g):** Mine for citations and arguments that strengthen the theoretical chapter. Don't dump it wholesale.

---

## 3. Key Passages to Preserve from v1.4

These are passages from v1.4 that are particularly well-written or conceptually sharp and should survive integration:

- The MLS definition (v1.4 lines 70-76) — clean, citable formulation
- "Fun as biological baggage promoted as The Good" (v1.4 lines 99-103) — strong provocation
- Wolfendale on aesthetics as terminal-goal formation (v1.4 lines 107-113) — core philosophical contribution
- The FR question: "for an arbitrary intelligence, does having the FR matter for capability?" (v1.4 line 105) — this is the crux
- The Ćirković argument on consciousness atrophying (v1.4 from the expanded astrobiology in the v1.3 equivalent section around lines 66-70 of v1.3's structure, but substantially developed in v1.4)

---

## 4. What to Watch Out For

- v1.4 has a lot of editorial notes and TODOs at the top (lines 1-12) that are useful reminders but shouldn't migrate into chapter text
- v1.4's LLM questions appendix (lines 200+) is interesting but may be redundant with ch_03_reorg's own question set
- Some v1.4 material (particularly the empirical appendix) overlaps with what's already in ch_03_reorg — need to decide which chapter owns what

---

*These notes were generated by Claude Code on 12 Feb 2026 to preserve integration context across sessions.*
