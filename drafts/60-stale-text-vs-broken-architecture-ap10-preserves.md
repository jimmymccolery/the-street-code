# Stale text vs broken architecture — the difference that AP #10 preserves

**Author:** Jimmy McColery
**Date:** 2026-05-31
**Status:** SEED STUB — operator-authoring-pending. AP #10 canonical-source-historical-narrative discipline case study from Pin Paradise close-out arc 2026-05-31 morning. Discipline applied at canonical-text-supersession scope n=3 same-arc application (PL-10 §16.11 reconciliation + Q17 §22.6 Component (iii) reconciliation + Q17 §22.9 primer-Q8 reconciliation).

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

## The seed: what to write about

Three times in one morning, I discovered canonical-text drift in my game design document. In each case the pattern was identical:

1. A design-time canonical source (the doc where a question was originally raised) carried framing X
2. A ratification-time canonical source (the doc where the question was answered) carried decision Y, which superseded X
3. The design-time source was NEVER UPDATED to back-link to the ratification

A future reader of the design-time doc in isolation would implement X (the old framing), not Y (the actual decision). The architecture wasn't broken. The text was stale. But stale text becomes broken architecture the moment someone trusts the older doc.

I had a discipline already banked for exactly this situation, originally surfaced for AI-role renames. The rule: **preserve the historical narrative + add forward-pointing supersession notes**. Don't rewrite the old doc (that destroys the audit trail). Don't leave the old doc alone (that leaves the trap). Annotate the old doc with "this paragraph superseded by [Y]; preserved per AP #10 discipline."

I applied this discipline three times in one morning. n=3 reproduction at a new application scope (canonical-text-supersession) of a discipline originally banked at a different scope (resource-rename).

## The arc to narrate

1. **The discipline origin**: AP #10 banked for the Beatles-model AI role rename (Squad → Gang, Grok → The Quarterback, etc.) and the FSM Mode → The Treasure Map resource rename. The rule: historical narrative dated before the rename preserves original names; entries dated after rename use new names with rename meta-references. Don't bulk-rewrite history; let it stand with footnotes.
2. **The Sunday morning re-discovery**: PL-10 re-verification cycle surfaces that §16.11 (Q11 close design-time doc) carries "Worker thread interleaves serialization chunks with citizen-life-tick processing — no starvation of tick-queue during save." But §25 (PL-10 ratification-time doc) carries "pause-during-save (TickScheduler.pause/resume)." The architectural decision was made; the doc that originally posed the question was never updated. Reader of §16.11 in isolation builds it wrong.
3. **First application at new scope**: Add a reconciliation block to §16.11 immediately after the paragraph: "[Post-PL-10-ratification supersession 2026-05-28 evening per §25 lock body — 3 surfaces in the paragraph above SUPERSEDED at PL-10 V1 ratification; preserved-with-back-references per AP #10 canonical-source-historical-narrative discipline]." Then 3 surface-specific back-links pointing to the operative source.
4. **Second application same morning**: Q17 re-verification surfaces §22.6 Component (iii) still reads "perf-test REQUIRED before V1 ship target lock" but §31.6 carries "✅ RESOLVED 2026-05-28 + ✅ CONFIRMED PASS 2026-05-29." Same pattern. Same reconciliation discipline. Apply AP #10 again.
5. **Third application same morning**: Q17 re-verification surfaces sibling §22.9 still frames primer-Q8 audio engine as "BLOCKING DEPENDENCY prior to Phase 6.1 code construction" but ROADMAP carries "LOCKED at Tone.js + Google Resonance Audio Path (a) at Phase 6.0 Session 3 capstone close." Same pattern. Same discipline. Apply AP #10 again.
6. **The empirical observation**: AP #10 originally banked for resource/role renames generalizes cleanly to canonical-text supersession. The MOTIVATION is the same — preserve audit trail + don't trust readers to know which doc is current — even though the SCOPE differs (rename vs supersession).
7. **The architectural consequence**: All 3 reconciliations were MECHANICAL ABSORPTIONS of already-ratified decisions. No new architectural decision needed. Operator-approval-then-substitute discipline applies, not distinct-decisions-distinct-deliberation. Bundling preserves audit-trail coherence. The shape of the patch ("preserve + back-link") IS the discipline.

## Why it's worth writing

This is a small post about a quiet discipline. Not glamorous. Not a Council deployment story. But it's about the kind of canonical-text hygiene that distinguishes a maintainable architecture from one that rots. The lesson: when you rewrite an old doc to match a new decision, you destroy the audit trail. When you leave the old doc alone, you leave the trap. The third path — annotate the old doc with back-links to the new decision — preserves both. n=3 reproduction in one morning at a new application scope validates that the discipline generalizes beyond its original scope.

Architecture decays in two ways: code rots, OR text rots. Most disciplines protect against code rot. AP #10 protects against text rot, specifically the corrosive flavor where the text is "right at the time it was written + wrong now."
