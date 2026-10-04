# Phase 3.8.1 Ship 5b — M6+M4+M7 N-Sim Composition Wire Propagation — SHIPPED
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL
**Ship commits:** sim-ai; roomtolife pushed

---

## §1 Scope

Higher-scope N-Sim composition wire propagation wave — 3 mechanisms shipped in single ship. **Largest single-mechanism scope in Phase 3.8.1 (M6 Bowlby Ch11 multi-figure hierarchy).**

## §2 Architecture

### M6 Bowlby 1969 Ch11 Multi-Figure Attachment Hierarchy (~250 LOC + 23 tests)

**New state field:** `attachmentFigureHierarchy: readonly SimId[]` on SimAttachmentBehavioralState.

**New helper:** `selectPrimaryAttachmentFigure(simId, state)` argmax composite score:
- `SENTIMENT_WEIGHT = [omitted]` (pair sentiment)
- `PROXIMITY_WEIGHT = [omitted]` (Chebyshev inverse; `MAX_DIST = [omitted]`)
- `TENURE_WEIGHT = [omitted]` (ticks known; `TENURE_SATURATION_TICKS = [omitted]`)
- `SECONDARY_PROTEST_MULTIPLIER = [omitted]`

Bowlby monotropy dead-figure exclusion preserved.

**Lazy-seed guard** in `getOrInitSimActivation` handles pre-Ship-5b legacy state without hierarchy field.

Wire @ 3776/3787 refactored per-observer for K≥3.

### M4 Kline 2015 K≥3 Teaching Typology Unlock (~200 LOC + 24 tests)

**Satisfies N-76 candidacy scope-clarify.**

- Vicarious wire @ 8646 refactored to WITNESS-SET iteration around mastery events
- **Schunk 1987 similar-model preference:** `SCHUNK_1987.SIMILAR_MODEL_WEIGHT_SLOPE = [omitted]` (weight formula omitted)
- **Kline 2015 signal-based teaching detection** (K=3 minimum: teacher + student + signal-observer): `SIGNAL_BASED_WEIGHT = [omitted]`
- **Kline 2015 evaluative-feedback teaching detection** (K=3 minimum: teacher + student + evaluator): `EVALUATIVE_FEEDBACK_WEIGHT = [omitted]`

### M7 DSM-5 Criterion A4 Witness-Set Trauma Propagation (~180 LOC + 20 tests)

- `registerTraumaExposure` @ 2859/2966 iterates witnesses
- **Kaltman-Bonanno 2003:** peritraumatic dissociation propagates to witnesses
- **Alisic 2011 tertiary-witness reduced magnitude** (`ALISIC_2011.TERTIARY_WITNESS_MULTIPLIER = [omitted]`) — tertiary witness of `attacked_by` registers trauma at reduced magnitude relative to primary
- DSM-5 Criterion A4 broad "witnessing in person" applied at partner_death (all alive Sims); attacked_by uses Ship 4-style proximity gate via `WITNESS_OBSERVATION_RADIUS`

## §3 Non-Inertness Gate Verdict — 67/67 PASS @ 100%

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/ship5bM6M4M7NSimPropagation.test.ts`

- **M6 attachment behavioral:** 23/23 PASS — H1×6 Bowlby Ch11 multi-figure hierarchy + H2×3 argmax stability + H3×4 Bowlby monotropy dead-figure exclusion + V1×4 K=2 backward-compat + V2×6 including K=8 1000-iter Rule 28 fuzz
- **M4 self-efficacy:** 24/24 PASS — H1×4 witness-set iteration + H2×4 Schunk 1987 similar-model preference + H3×4 Kline 2015 signal-based unlock + H4×3 Kline 2015 evaluative-feedback unlock + V1×5 K=2 preserved + V2×3 Rule 28 preservation
- **M7 trauma appraisal:** 20/20 PASS — H1×3 DSM-5 A4 witness-set iteration + H2×3 Kaltman-Bonanno peritraumatic propagation + H3×5 Alisic 2011 reduced tertiary magnitude + V1×4 K=2 preserved + V2×5 Rule 28 preservation

## §4 Empirical Anchors (K=2 verified)

- **Bowlby 1969 Ch11** *Attachment* multi-figure hierarchy canonical
- **Bandura 1997** *Self-Efficacy* four sources
- **Kline 2015** BBS 38:e31 teaching typology (satisfies N-76 candidacy scope-clarify)
- **Schunk 1987** similar-model preference
- **DSM-5-TR Criterion A4** witnessing in person
- **Kaltman-Bonanno 2003** peritraumatic dissociation
- **Alisic 2011** child-witness of violence d≈0.15-0.30 (tertiary magnitude anchor)

## §5 M6 attachmentFigureHierarchy Rule 28 Verdict

**CLEAN.** K=8 1000-iteration fuzz test (V2c) confirms hierarchy field is NEVER nuked/undefined for alive observers under randomized sentiment/distance/tenure/aliveness inputs. Lazy-seed guard in `getOrInitSimActivation` handles pre-Ship-5b legacy state.

## §6 Rule 19 Flags Surfaced

**CALIBRATION-CHOICE (9 new constants):**
- `BOWLBY_HIERARCHY.SENTIMENT_WEIGHT = [omitted]` + `PROXIMITY_WEIGHT = [omitted]` + `TENURE_WEIGHT = [omitted]` + `MAX_DIST = [omitted]` + `TENURE_SATURATION_TICKS = [omitted]` + `SECONDARY_PROTEST_MULTIPLIER = [omitted]`
- `SCHUNK_1987.SIMILAR_MODEL_WEIGHT_SLOPE = [omitted]`
- `KLINE_2015_TEACHING.SIGNAL_BASED_WEIGHT = [omitted]` + `EVALUATIVE_FEEDBACK_WEIGHT = [omitted]`
- `ALISIC_2011.TERTIARY_WITNESS_MULTIPLIER = [omitted]`

**EMPIRICAL-TRANSLATION:**
- `selectPrimaryAttachmentFigure` argmax translates Bowlby qualitative hierarchy to composite scalar
- Alisic 2011 child-witness of violence d≈0.15-0.30 translated to `attacked_by` tertiary reduced magnitude

**REJECT-STALE:** None

## §7 Framework Methodology Firsts

- FIRST Bowlby 1969 Ch11 multi-figure attachment hierarchy substrate
- FIRST `selectPrimaryAttachmentFigure` argmax algorithm (composite: sentiment × distance × tenure)
- FIRST Kline 2015 signal-based teaching typology unlock at K≥3 (satisfies N-76 candidacy scope-clarify)
- FIRST Kline 2015 evaluative-feedback teaching typology unlock at K≥3
- FIRST Schunk 1987 similar-model preference weighting on vicarious source
- FIRST DSM-5 Criterion A4 witness-set trauma propagation
- FIRST Alisic 2011 tertiary-witness reduced magnitude anchor

## §8 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/87 files
- sim-ai full test suite: **3054 PASS** (baseline S5a close 2987 → +67 Ship 5b tests exactly per spec)
- sim-ai postmortem: 2 preexisting anomalies (identical to Ship 3 postmortem baseline; unrelated to Ship 5b substrate; waived)
- roomtolife: precheck GREEN + vendor sync verified

## §9 Deviations from Spec

**Broader witness-set for partner_death:** applied "all alive Sims" per DSM-5 Criterion A4 broad "witnessing in person" — co-location gate for partner_death deferred to Ship 5b v2 (CALIBRATION-CHOICE flag). For `attacked_by`, applied Ship 4-style proximity gate via `WITNESS_OBSERVATION_RADIUS`.

**Substrate scope:** 834 LOC across 4 substrate files (vs. spec ~630); +204 LOC absorbed by 9 new CALIBRATION-CHOICE constants + lazy-seed guard + multi-mechanism cross-references. Test count matches target exactly (67/67).

## §10 Council #11 Candidacy

**Item 236 filed:** Phase 3.8.1 Ship 5b M6+M4+M7 N-Sim propagation ratification.

Sub-items:
- 236.1 Bowlby 1969 Ch11 multi-figure attachment hierarchy substrate
- 236.2 selectPrimaryAttachmentFigure argmax composite scalar (EMPIRICAL-TRANSLATION from qualitative Bowlby)
- 236.3 Kline 2015 K≥3 teaching typology unlock (satisfies N-76 scope-clarify)
- 236.4 Schunk 1987 similar-model preference weighting
- 236.5 DSM-5 Criterion A4 witness-set trauma propagation
- 236.6 Alisic 2011 tertiary-witness reduced magnitude anchor (EMPIRICAL-TRANSLATION from child-witness d≈0.15-0.30)
- 236.7 Broader witness-set for partner_death (co-location gate deferred to v2)

## §11 Downstream Impact

**All N-Sim substrate composition wiring COMPLETE (Ships S1-S5b).** Ships 6+7 can now run in parallel:
- **Ship 6** UI extensions (N-tab + 8-color SIM_AURA_PALETTE + aggregate-over-N CrossPlaneCouplingMatrix; ~690 LOC UI)
- **Ship 7** H4 N=8 performance harness (8 hypotheses; standalone tsx script; ~2200 LOC)

**Then Ship 8** Phase 3.8.1 close-out consolidation.

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
