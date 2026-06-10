# Drafting brief — Post 83 "Procedural Persons as a Bayesian Puzzle"

**Status:** Brief only; not yet drafted. Per CW R6 Tier 5 item 19.
**Target slot:** Post 83 (Bayesian-inversion framing for the operator-novel cryptographic-puzzle contribution).
**Scope verdict (per closure memo):** SAFE if structure-only — discuss Bayesian inversion CONCEPT; do NOT name cryptographic-puzzle internals or Item #98 specifics. Protected-scope strict.

## Thesis

When you sketch the structure of a procedural NPC that solves a puzzle about itself, the natural framing is that the NPC and the player are both inferring — but at different layers, with different priors, and from different sides of an information asymmetry. Modified-C-bis frames this as second-order Bayesian model inversion: the player infers about the NPC; the NPC infers about its own world; the structure binds them while keeping the inference layers computationally separate. The cryptographic puzzle is the operator's design-theoretic instantiation of that second-order inversion.

## Key citations (all locked at `architecture/modified-c-bis-canonical-citations-2026-06-09.md`)

- **Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., & Pezzulo, G. (2017).** Active inference: A process theory. ***Neural Computation*** 29(1):1-49. Appendix F naive (V1) / sophisticated (Phase-8.x) distinction.
- **Gray, H. M., Gray, K., & Wegner, D. M. (2007).** Dimensions of mind perception. ***Science*** 315(5812):619. CANONICAL Experience/Agency dimensions; NOT the 2010 *TiCS* review.
- **Waytz, A., Morewedge, C. K., Epley, N., et al. (2010).** Making sense by making sentient: Effectance motivation increases anthropomorphism. ***JPSP*** 99(3):410-435. CANONICAL effectance motivation; NOT the 2010 *TiCS* review.
- **Bouizegarene, N., Ramstead, M. J. D., Constant, A., Friston, K., & Kirmayer, L. J. (2024).** Narrative as active inference. ***Frontiers in Psychology*** 15:1345480. HUMAN-SCOPED; carry substrate-neutrality + functional-equivalence bridge argument.
- **Deane, G. (2021).** Consciousness in active inference. ***Neuroscience of Consciousness*** 2021(2):niab024.
- **AgentCrypt:** arXiv:2512.08104 (Karthikeyan et al.; v3 May 2026). NOT arXiv:2605.03213. Citation pending operator-side full read.

## Structural outline

1. **Hook:** "I asked five substrates how to model NPC self-discovery and got back five different framings of the same structural problem: the player and the NPC are inferring at different layers."
2. **The structural problem.** When the player observes an NPC, the player runs a Bayesian inference about the NPC's hidden states. The NPC runs its own Bayesian inference about its own hidden world-states. These are different inferences in different parameter spaces. Mathematically they cannot be conflated.
3. **The second-order inversion.** Modified-C-bis frames this as second-order Bayesian model inversion (modification 2). The player's inference is about a Bayesian agent. The agent's inference is about the world. The "self-discovery" the NPC undergoes is the NPC's inference about its own model, not the player's inference about the NPC.
4. **The V1-naive / Phase-8.x-sophisticated boundary.** V1 uses present-state-anchored (naive, Appendix F-naive) active inference; the NPC's own self-experience is present-anchored, Episodic-compatible. Phase-8.x banks sophisticated (deep-temporal) active inference. The terminology distinction matters because the same word "active inference" covers both modes; the framework only commits to the naive variant at V1.
5. **Why this changes how you sketch the puzzle.** A puzzle whose computational structure mirrors the second-order inversion creates a different kind of player engagement than a puzzle that treats the NPC as a database to be queried. The puzzle is solvable because the structure is interpretable; the engagement is felt because the structure mirrors the genuine inferential asymmetry between observing and being observed.
6. **Mind-perception canonical anchor.** Gray Gray Wegner 2007 *Science* (Experience/Agency) + Waytz Morewedge Epley 2010 *JPSP* (effectance + unpredictability-triggers-mind-attribution). Explicit correction note: the often-cited 2010 *TiCS* paper is a review, not the origin source.
7. **What I am not claiming + what I am claiming.**

## Voice spec adherence

- Zero em-dash characters. No emojis.
- "What I am not claiming" + "What I am claiming" H2; ~313+ words each.
- Use "present-state-anchored active inference" NEVER "sophisticated active inference" for V1 mechanism. "Sophisticated" appears only in passing reference to the Phase-8.x banked path.
- Frame all narrative-identity references as observer-level player-perceived per F-6; never as the NPC's own self-narrative.

## Disclosure-discipline notes

- Discuss Bayesian inversion CONCEPT only. Do NOT name the cryptographic-puzzle internals.
- Do NOT name protected-scope Memory Lanes apparatus (Item #98 + §22 + cryptographic-puzzle implementation specifics + lane-repair-puzzle internals all PROTECTED).
- Use phrases like "the design sketch I am developing," "a puzzle whose structure," "an indie-tycoon simulation" generically.
- Bouizegarene 2024 is human-scoped; carry the substrate-neutrality + functional-equivalence bridge argument explicitly. Bouizegarene + Deane 2021 are the route to active-inference framing, NEVER Strawson direct.

## Drafting prerequisites

- Modified-C-bis ratification complete (DONE).
- Canonical citations document complete (DONE).
- Wiredu primary-text defense complete (DONE; relevant to relational-personhood layer though Post 83 stays light on cross-cultural framing).
- **OPTIONAL operator-side reading before drafting:** AgentCrypt arXiv:2512.08104 in full (Opus R4: abstract only). If not yet read, draft Post 83 without naming AgentCrypt at all; defer specific cryptographic-primitive references to the design-theory paper at ACM Games R&P.

## Estimated word count

~4,000-5,000 words. This post is dense with technical concepts; longer than the average post.

## Drafting session notes

- The mind-perception correction note (Gray Gray Wegner 2007 + Waytz Morewedge Epley 2010 *JPSP* NOT the 2010 *TiCS* review) can be made in the post itself as a footnote or methodology aside — this transforms a citation-discipline note into a small piece of methodology content the post offers.
- Use the Bouizegarene bridge argument explicitly: "Bouizegarene 2024 documents narrative-as-active-inference for human cognition; I extend it to procedural agents via a substrate-neutrality and functional-equivalence assumption, which the paper neither supports nor forecloses."
- This post is the conceptual foundation for the cryptographic-puzzle design-theory paper at ACM Games R&P. Drafting this post well is the warm-up for the paper.
