# Drafting brief — Post 91 "Re-Sourcing Trait Encoding from HEXACO to Attachment"

**Status:** Brief only; not yet drafted. NEW brief 2026-06-10 PM per Round 7 R5 design.
**Target slot:** Post 91 within Posts 89-96 retraction block. Per R5 design: makes the attachment correction legible to game developers.
**Scope verdict:** SAFE — methodology + open-academic citations. No protected scope.
**Length target:** 3000-4500 words per R5 design.

## Thesis

Modified-C-bis's first-pass V1 specification used HEXACO honesty-humility (H) as the trait dimension driving relational-encoding modulation. Round 7 surfaced a correction: HEXACO H is the right trait for cooperation/exploitation tendencies (its empirical strength per Hilbig & Zettler 2009 + Thielmann & Hilbig 2015) but the WRONG trait for relational-encoding bias. The correct trait source for relational encoding is **attachment style** per Fraley, Waller & Brennan 2000 (ECR-R). Specifically: attachment avoidance maps to LOWER relational encoding (the agent encodes relational events less richly); attachment anxiety maps to suspicious-or-false-positive relational appraisal (the agent over-encodes threat-relevant relational signals). Post 91 walks through this re-sourcing in a way that's legible to game developers without requiring deep psychometric background.

## Sections (outline)

1. **Hook:** "I tried to use one personality trait to drive multiple things. The literature says: stop. Different traits drive different cognitive functions. Here's what I had to re-source."

2. **The original HEXACO-everywhere mistake.** First-pass spec used HEXACO H for: cooperation (correct), generosity (correct), AND relational-event encoding (wrong). Show how the conflation broke a 3-4-NPC interaction scenario.

3. **What HEXACO H is actually for.** HEXACO H (honesty-humility) is empirically validated as the trait dimension for exploitation/cooperation behaviors. Citations:
   - Ashton & Lee 2009 HEXACO-60 *Journal of Personality Assessment* 91(4):340-345
   - Hilbig & Zettler 2009 *Journal of Research in Personality* 43(3):516-519 (venue corrected via R7)
   - Thielmann & Hilbig 2015 *Personality and Social Psychology Bulletin* 41(11):1523-36 (venue corrected via R7)
   - Zettler, Thielmann, Hilbig & Moshagen 2020 *Perspectives on Psychological Science* 15(3):723-760

4. **What attachment style is actually for.** Attachment Theory (Bowlby 1969/1982 + Ainsworth et al. 1978 + Fraley, Waller & Brennan 2000 ECR-R) is empirically validated as the trait substrate for relational-event encoding + retrieval. Two dimensions:
   - **Attachment avoidance:** discomfort with closeness + reluctance to depend. Maps to LOWER relational encoding (avoidant agents pay less attention to relational signals; encode less detail; retrieve less easily).
   - **Attachment anxiety:** worry about partner availability + fear of rejection. Maps to HIGHER false-positive relational appraisal (anxious agents over-encode threat-relevant relational signals; over-attribute negative intent; selective recall of relationship-threatening events).

5. **Implementation: trait-modulated encoding filter.** Show the encoding filter with the corrected trait sources:
   - Cooperation/exploitation actions → HEXACO H modulates (no change)
   - Generosity ladder → HEXACO H modulates (no change)
   - Relational-event encoding (Layer 1 → Layer 2 filter) → attachment avoidance + attachment anxiety modulate (CORRECTED)
   - Pair-history accumulation → attachment style modulates encoding-weight per pair-event

6. **The Fraley & Hudson 2014 caveat.** Attachment styles in early adulthood are stable on the order of years, not lifetime. The framework should NOT treat attachment as immutable trait; treat as stable-but-modifiable. For NPCs over a 30-year arc, attachment style may shift in response to major life events (per Fraley & Hudson 2014). This is a V1.x refinement, not V1 critical-path.

7. **What the re-sourcing unlocks.** Characters with the same HEXACO H profile but different attachment styles behave differently in relational contexts:
   - Secure: rich relational encoding + accurate appraisal
   - Anxious: rich relational encoding + over-pessimistic appraisal
   - Avoidant: thin relational encoding + under-attentive appraisal
   - Fearful-avoidant: thin relational encoding + over-pessimistic appraisal

8. **V1 implementation cost.** Schema change — attachment style is a 2-dimensional latent + ECR-R 18-item answers can seed each character. Encoding filter adds attachment-modulator. ~16-28 hours BUILD-side per R5 ratification candidate table.

9. **Cross-cultural caveat.** ECR-R is WEIRD-sample-derived (Henrich et al. 2010 *BBS* 33(2-3):61-83 critique). Cross-cultural validity has been studied (Mikulincer & Shaver 2016) but the WEIRD-defaults problem applies. Posts 100-104 cross-cultural sequence covers the broader handling. For Post 91: cite the caveat; flag that attachment-style application across cultural contexts requires the operator's WEIRD-defaults discipline.

10. **Closing.** "HEXACO is excellent at what it measures. Attachment is excellent at what IT measures. The framework was using HEXACO for both because HEXACO was the trait the operator knew best. The literature is unambiguous; the re-sourcing is the right move." Honest about the why.

## Key citations

- **Ashton, M. C., & Lee, K. (2009).** The HEXACO-60. *JPA* 91(4):340-345.
- **Hilbig, B. E., & Zettler, I. (2009).** Pillars of cooperation. *JRP* 43(3):516-519.
- **Thielmann, I., & Hilbig, B. E. (2015).** The traits one can trust. *PSPB* 41(11):1523-36.
- **Fraley, R. C., Waller, N. G., & Brennan, K. A. (2000).** ECR-R. *JPSP* 78(2):350-365.
- **Bowlby, J. (1969/1982).** *Attachment and Loss, Vol. 1: Attachment*. Basic Books.
- **Ainsworth et al. (1978).** *Patterns of Attachment*. Erlbaum.
- **Mikulincer, M., & Shaver, P. R. (2016).** *Attachment in Adulthood*. Guilford.
- **Fraley, R. C., & Hudson, N. W. (2014).** Attachment stability research review.
- **Henrich, J., Heine, S. J., & Norenzayan, A. (2010).** The WEIRDest people. *BBS* 33(2-3):61-83.

## Cross-links

- LINKS BACK TO: Post 89 (retraction table includes HEXACO → attachment re-source), Post 90 (DC1 split)
- LINKS FORWARD TO: Post 92 (sentiment override + pair-specific memory), Post 102 (communal accountability in cross-cultural sequence)
- IMPLEMENTATION TIE: Round 9 generative-model formalization (Q1 trait state-space + Q3 belief-update filter)

## Drafting prerequisites

- Operator-side read of Fraley, Waller & Brennan 2000 ECR-R paper (~1.5h).
- Mikulincer & Shaver 2016 *Attachment in Adulthood* selected chapters (~3-5h; ~50-80 pages relevant).
- Fraley & Hudson 2014 stability review (~30 min).

## Hour estimate

At observed velocity: ~5-7 hours drafting + revision pass. Target 3000-4500 words.
