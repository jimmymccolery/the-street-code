# Drafting brief — Post 90 "The Split: Valence Is Not Stress"

**Status:** Brief only; not yet drafted. NEW brief 2026-06-10 PM per Round 7 R5 design.
**Target slot:** Post 90 within Posts 89-96 retraction/correction block. Per R5 design: the load-bearing DC1 correction post — explains why "emotion" is too broad for implementation.
**Scope verdict (per disclosure rule v1.0):** SAFE — pure methodology + open-academic primary-text citations (Russell circumplex; Faul & LaBar 2023; possibly Hesp 2021 if read). No Memory Lanes protected scope.
**Length target:** 3000-4000 words per R5 design.

## Thesis

Modified-C-bis's first-pass V1 specification treated "emotion" as a single scalar — call it "mood" — that affected encoding, retrieval, and decision-making uniformly. Round 7 surfaced a DC1 ("Decision-Critical 1") correction: emotion is not a single variable. The empirical literature consistently distinguishes at least three separable affective dimensions: valence (positive vs negative), arousal (high vs low activation), and stress (a separable third axis with distinct neurobiological correlates per Goldfarb & Phelps 2017 + Faul & LaBar 2023). Conflating them into one variable produced an architecture where mood-conditioned encoding could not distinguish "happy" from "manic" from "fortified-by-stress." The DC1 correction is load-bearing because the encoding filter, the retrieval bias, and the policy-rigidity threshold all need DIFFERENT components of affect. Post 90 explains the correction and its implementation consequences.

## Sections (outline)

1. **Hook:** "The first version of this framework had a single emotion variable. The literature consistently distinguishes at least three. The framework's emotion variable broke at every place it had to interact with implementation."

2. **The original conflation.** Show what the first-pass V1 spec did: one `mood` scalar in [-1, 1] driving the Layer 3 accumulator. Show 3-4 places this conflation broke:
   - A character ending a busy successful shift had high `mood`, but their HIGH-AROUSAL HIGH-VALENCE state should bias encoding differently than a character in a LOW-AROUSAL HIGH-VALENCE state (contented). Same `mood` value; different encoding filter needs.
   - A character under chronic stress with positive valence (e.g., a pinboy hustling for tips during a busy night) has different policy-rigidity than a low-stress positive-valence character. Same `mood`; different decision-rule applies.
   - Mood-congruent retrieval (per Eich 1995) is conditional on emotion-DIMENSION-match, not single-scalar-match. The conflation can't model retrieval correctly.

3. **The DC1 correction: three separate fields.** Define the three fields explicitly:
   - **Valence** [-1, +1]: positive vs negative affect. Russell circumplex (1980 *JPSP* 39(6):1161-1178). Drives content bias in encoding (positive valence over-weights positive-tagged events; negative valence over-weights negative-tagged events).
   - **Arousal** [0, 1]: low (deactivated, calm) vs high (activated, alert). Russell circumplex. Drives policy-rigidity + habit-fallback (high arousal → cached policy reliance; low arousal → exploratory).
   - **Stress** [0, 1]: separable from arousal per Goldfarb & Phelps 2017 (stress shifts hippocampal-to-striatal memory; distinct biological pathway). Drives encoding-fidelity (high stress → narrow attention; selective encoding of threat-relevant features).
   - Optional **control/dominance** [-1, +1] per PAD model (Mehrabian 1996); deferred Phase-8.x unless V1 requires.

4. **Implementation diagram.** One implementation diagram showing how the three fields flow through the architecture:
   - Layer 3 accumulator holds (valence, arousal, stress) — three separate scalars updated independently at different time constants
   - Encoding filter (Layer 1 → Layer 2) reads valence (content bias) + stress (attention narrowing) + traits
   - Decision policy reads arousal (rigidity gate) + valence (preference shift)
   - Retrieval bias reads valence + arousal (mood-congruent retrieval per Eich 1995)

5. **The Goldfarb & Phelps 2017 + Faul & LaBar 2023 grounding.** Goldfarb & Phelps establish stress as a separable axis from arousal (different memory-system trade-offs). Faul & LaBar's 2023 reanalysis of Bower 1981 sharpens the mood-congruent-memory effect under modern methodology. These citations are recent + their venues were corrected via R7 R6 catches. (Reference: "Goldfarb & Phelps 2017 venue Current Opinion in Behavioral Sciences 14:47-53 not Annual Review" — this was one of R7's catches; see Post 89 retraction table.)

6. **What the split unlocks.** With three separate fields, the architecture can:
   - Model "stress-eating" behavior (stress without negative valence)
   - Distinguish "burned-out" (low arousal, negative valence, accumulated stress) from "sad" (low arousal, negative valence, low stress)
   - Match real-life patterns where players observe characters and find them MORE believable because their affective states are dimensionally accurate

7. **V1 implementation cost.** This is a schema change — three scalars instead of one. Encoding filter, retrieval bias, decision policy each need an updated read pattern. ~18-30 hours BUILD-side per R5 ratification candidate table.

8. **What DC1 doesn't do.** It does not move the framework toward phenomenal-consciousness claims. The three fields are computational state variables; the framework's structural-only discipline (Modification 6 Amendment Round 8 Revision) still holds. The fields are observation-channels in the agent's generative model; the agent does not "feel" them in any subjective sense.

9. **Closing.** The DC1 split is one of those corrections where "the framework is wrong because the literature is right." Modified-C-bis is stronger after the split because it can now produce characters whose affective states FEEL accurate rather than averaged.

## Key citations

- **Russell, J. A. (1980).** A circumplex model of affect. ***JPSP*** 39(6):1161-1178.
- **Goldfarb, E. V., & Phelps, E. A. (2017).** Stress and the trade-off between hippocampal and striatal memory. ***Current Opinion in Behavioral Sciences*** 14:47-53. (Venue corrected via R7 R6.)
- **Faul, L., & LaBar, K. S. (2023).** Mood-congruent memory revisited. ***Psychological Review*** 130(6):1421-1456.
- **Mehrabian, A. (1996).** Pleasure-arousal-dominance: A general framework. *Current Psychology* 14:261-292. (If PAD optional dominance field invoked.)
- **Eich, E. (1995).** Searching for mood dependent memory. *Psychological Science* 6(2):67-75.

## Cross-links

- LINKS BACK TO: Post 89 (the retraction table includes DC1 split)
- LINKS FORWARD TO: Post 91 (attachment-encoding correction), Post 92 (sentiment override), Post 94 (consolidation), Post 96 (V1 spec)
- IMPLEMENTATION TIE: Round 9 generative-model formalization arc (DC1 split is a Q1 state-space enumeration input)

## Drafting prerequisites

- Operator-side direct read of Russell 1980 circumplex (~30 min; canonical).
- Faul & LaBar 2023 close-read for mood-congruent revision (~1 hour).
- Goldfarb & Phelps 2017 read for stress-axis separability (~1 hour).

## Hour estimate

At observed velocity: ~5-7 hours drafting + revision pass + diagram drafting. Target 3000-4000 words.
