# Appraisal-Tag Reservation-Plus-Ablation-Gate Execution Guide V1

**Established:** 2026-07-02 evening (post-Council-#2-close session; companion to Posts 0139 + 0140)
**Maintained by:** operator; CC updates on empirical contact
**Purpose:** Clean-room execution guide for the ablation gate that operationalizes (or retires) the reserved `appraisal_tags[]` schema slot canonized at Council #2 close (Post 0140 Decision 1). Standalone-executable: a fresh CC session, fresh substrate, or future-operator can open this file with zero prior context and run the gate end-to-end.
**Provenance:** Council #2 (appraisal tags vs accumulator minimalism) closed 2026-07-02 evening at Pattern B ADOPT-FOLD via Option B per-item deliberation. Consolidated eight-decision amendment package documented in Post 0140; this guide operationalizes Decision 1 schema-placeholder amendment + Decision 5 ablation-battery specification + Decision 6 anti-armor discipline.

---

## What this guide is and is NOT

**This guide is** the standalone-executable operational procedure for the appraisal-tag ablation battery. It enumerates: the four single-Sim ablation conditions per Substrate B specification with pass/fail criteria; the multi-Sim player-visible-ratification protocol per Substrate C specification; the task decomposition across Claude Code (BUILDER surface) and Comet Computer (RESEARCH-AGENT surface); the calibrated prompts for each surface; the per-phase cost estimates; the failure modes plus fallbacks; the handoff artifacts each phase produces; the anti-armor discipline extension per Post 0140 Decision 6.

**This guide is NOT** the architectural spec for the reserved slot (Post 0140 Decision 1 is the spec), the narrative of how Council #2 arrived at the ablation gate (Post 0139 is the narrative), or the substrate outputs themselves (archived at `~/Projects/the-street-code/_archive/2026-07-02-council-2-appraisal-tags/`). The guide points to those artifacts; it does not duplicate their content.

---

## The reserved slot per Post 0140 Decision 1 (recap for standalone use)

`appraisal_tags[]` at Layer 2 consolidation cadence with these named nullable member fields:

- **CORE reserved (target for operationalization):**
  - `agency_attribution`: nullable enum (self-caused / other-caused-intentional / other-caused-accidental / structural / uncertain)
  - `coping_control`: nullable scalar in [-1.0, +1.0]
- **CANDIDATE-PENDING-GATE:** `goal_congruence`: nullable scalar in [-1.0, +1.0] contingent on gate outcome
- **EXCLUDED pending ablation:** `expectedness` (per Substrate B's Condition-4 clamp-prediction-error-vs-H4 test)
- **ROUTED to per-NPC-philosophy dispatch:** `norm_violation` (through Post 0135 Decision 4 normative_profile dispatch behind existing per-NPC-philosophy ablation gate)

Reservation-plus-ablation adoption shape: schema slot reserved at V1-spec level now; operationalization gated on the ablation battery below; anti-armor discipline extension per Decision 6.

---

## The four single-Sim ablation conditions (Substrate B specification)

All four are the framework's specific commitment to test appraisal-tag operationalization empirically at single-Sim scope before multi-Sim ratification (Substrate C's protocol).

### Condition 1 — Intentional vs accidental differential firing

**Question:** does the reduced appraisal-tag set produce differential Layer 2 promotion + entity-index pair-summary + H1 action-distribution outcomes for intentional-betrayal vs accidental-harm events at equal DC1-valence + equal sentiment shift + non-first-occurrence status?

**Procedure:** construct paired fixtures with equal valence/arousal/stress/sentiment deltas. Betrayal fixture: NPC A intentionally deceives NPC B for personal gain. Accidental-harm fixture: NPC A spills a drink on NPC B without seeing them turn. Both fixtures produce equal DC1-split, equal sentiment update, no first-occurrence, no large-sentiment-shift firing at Post 0118's four gates. Run two conditions:
- Run A: existing decomposition only (no appraisal tags)
- Run B: existing decomposition + reduced appraisal-tag set with agency_attribution populated (other-caused-intentional for betrayal; other-caused-accidental for spill) + coping_control populated (low for betrayal; medium for spill)

Compare Layer 2 promotion rate, entity-index pair summaries, H1 action distributions across many candidate actions.

**Pass criterion:** Run B produces measurably differential outcomes across all three surfaces (promotion + pair summary + action distribution) that Run A does not; the differential firing traces to agency_attribution + coping_control fields at the mechanical dispatch layer.

**Fail criterion:** Run A and Run B produce indistinguishable outcomes at all three surfaces. Interpretation: the existing decomposition already carries the differentiation via typed-index category labels + trait-modulated significance; the appraisal-tag schema slot does not add unique signal at single-Sim scope.

### Condition 2 — Semantic-label masking test

**Question:** does the differentiation from Condition 1 depend on the appraisal-tag fields themselves, or on the event-category semantic labels typed indexes carry?

**Procedure:** mask semantic and category labels while preserving affect + pair history + appraisal-tag fields. Run Condition 1's two-run comparison with masked labels.

**Pass criterion:** Run B still produces measurably differential outcomes with labels masked (the appraisal-tag fields alone drive the differentiation).

**Fail criterion:** Run B's differential outcomes collapse when labels are masked. Interpretation: typed-index category labels were carrying the differentiation via content labels; the appraisal-tag schema slot is decorative rather than mechanically load-bearing. Retire the schema slot at V1.

### Condition 3 — Appraisal-tag shuffle test

**Question:** are the appraisal-tag fields driving downstream action + consolidation, or are they decorative labels the framework's mechanical pipeline ignores?

**Procedure:** hold event text + affect constant. Shuffle appraisal-tag assignments (intentional-betrayal fixtures get agency_attribution=other-caused-accidental; accidental-harm fixtures get agency_attribution=other-caused-intentional). Run against downstream action distributions + consolidation outcomes.

**Pass criterion:** downstream action + consolidation outcomes track the shuffled tags (the tags add live signal at the mechanical dispatch layer).

**Fail criterion:** downstream outcomes match the original semantic content rather than the shuffled tags. Interpretation: the appraisal-tag fields are read-decorative rather than mechanically load-bearing; retire the schema slot or add guardrails preventing fabricated tagging from producing arbitrary behavior.

### Condition 4 — Expectedness clamp test (LOAD-BEARING)

**Question:** does an explicit `expectedness` appraisal-tag field add downstream signal beyond what the framework's Post 0137 H4 prediction-error sparse encoding machinery already carries?

**Procedure:** clamp prediction-error values to equal across a sample of Layer 1 events; release the clamp; measure whether adding an `expectedness` appraisal-tag field to Layer 2 consolidation produces downstream action + consolidation differences beyond what prediction-error thresholding alone produces.

**Pass criterion:** expectedness tag produces measurable downstream signal after prediction-error is controlled. Interpretation: expectedness is not H4-duplicate; it may be added to the reserved appraisal-tag slot at subsequent Council methodology deployment.

**Fail criterion:** expectedness tag adds no downstream effect after H4 is active. Interpretation: expectedness is duplicate with H4 prediction-error machinery; keep excluded from V1 reserved slot per Post 0140 Decision 2 (confirmed empirically).

**Why this is the load-bearing condition:** the framework's continued architectural work on the appraisal-tag schema-placeholder slot at V1.x depends on whether expectedness needs a distinct member field. Condition 4 is the specific empirical test that decides. Passing 1-3 while failing 4 corresponds to "the appraisal-tag slot works but doesn't need an expectedness member" — the exact composition Post 0140 Decision 2 canonizes.

---

## The multi-Sim player-visible-ratification protocol (Substrate C specification)

Deferred to Phase 2+ per Post 0138 validation-vs-ratification discipline. Single-Sim Conditions 1-4 above establish mechanism validation; the multi-Sim protocol establishes player-visible ratification.

**Setup:** use existing BUILD-mode prototype (Post 0136-0138 empirical infrastructure) with one station cluster populated with 20-50 procedural NPCs run over simulated 2-5 in-game years via existing consolidation pass. Parallel builds:
- Build A: existing decomposition only (valence + arousal + stress + sentiment + attachment + typed-index)
- Build B: existing decomposition + reduced appraisal-tag set per Post 0140 Decision 1 CORE reservation

**Playtester recruitment:** 20-40 target-audience playtesters (indie management sim fans via Discord/Steam wishlist channels) for 45-90 min blinded sessions. Directed scenarios: league night management, automation rollout response, staff/customer incident handling.

**Pre-registered metrics:**
- **Legibility:** attribution accuracy quiz (multiple-choice on causal "why" for observed reactions; target >60% in B vs A) + confidence ratings
- **Behavioral divergence:** % playthroughs with unique observable outcomes (specific petitions, faction splits, pair avoidance, loyalty arc forks) exclusive to B
- **Engagement:** station dwell time, repeat visit rate, qualitative "NPC depth/reactive intelligence" Likert + think-aloud on perceived causality
- **Longitudinal:** post-session save analysis for relational_mode + typed-index divergence

**Pass criterion:** legibility attribution accuracy > 60% in B; behavioral divergence produces measurable unique outcomes exclusive to B; engagement metrics positive at operator-ratifiable magnitude.

**Fail criterion:** legibility below threshold; behavioral divergence not observable to players; engagement metrics indistinguishable across builds. Interpretation: the appraisal-tag slot may still be mechanically operational at single-Sim scope (Conditions 1-4 passing) but does not surface player-visible differences at multi-Sim scope; demote to internal-only bookkeeping.

Compare to Post 0136 H3 baselines. Blinded where feasible; collect open feedback on genre fit.

---

## Task decomposition across surfaces

The gate composes work across two substrates. Neither can execute the whole gate alone; the composition is what makes the gate schedulable at reduced total cost.

**Claude Code (BUILDER surface):** filesystem access, terminal execution, git operations, simulation runs against local prototype code, data export as CSV, code audit, single-Sim ablation execution. Owns Conditions 1-4 execution in full via local Sim AI Phase 1 test suite extension.

**Comet Computer or operator-driven Playtest coordination (RESEARCH-AGENT surface):** playtester recruitment via Discord/Steam channels, blinded session execution, pre-registered metrics collection, statistical analysis. Owns multi-Sim Phase 2+ playtester coordination.

---

## Phase 1 — Claude Code (BUILDER surface)

**Estimated cost: 10-18 hours BUILD-side work**

**Objective:** execute Substrate B Conditions 1-4 against Sim AI Phase 1 test suite extension; produce Condition 1-4 handoff artifacts for operator ratification.

### Phase 1 task list

1. **Prototype appraisal-tag schema slot integration (2-3h).** Throwaway code. Extends Layer 2 storage form to carry the nullable member fields per Post 0140 Decision 1 CORE reservation (agency_attribution + coping_control) plus CANDIDATE-PENDING-GATE (goal_congruence). Design constraint: consolidation-only computation (no per-frame appraisal); nullable fields; sparse population per event.

2. **Prototype consolidation-time appraisal-tag population heuristic (2-4h).** Throwaway code. Reads Layer 1 event's semantic-content tags + causal-index links + pair-history context; populates agency_attribution enum + coping_control scalar at consolidation cadence. Design constraint: heuristic must be principled enough that Conditions 1-3 test dispatch-through-the-fields rather than heuristic-labeling accident.

3. **Extend Sim AI Phase 1 test suite with paired fixtures for Condition 1 (2-3h).** Deterministic scenario fixtures for intentional-betrayal + accidental-harm at equal DC1-valence. Run both fixtures under Run A (no appraisal tags) + Run B (with appraisal tags). Measure Layer 2 promotion + pair summaries + H1 action distributions.

4. **Condition 2 execution (1-2h).** Mask semantic + category labels in Condition 1's fixtures; re-run comparison.

5. **Condition 3 execution (1-2h).** Shuffle appraisal-tag assignments across Condition 1's fixtures; re-run comparison.

6. **Condition 4 expectedness clamp test (2-3h).** Extend the test suite with prediction-error clamping infrastructure; run appraisal-tag-with-expectedness vs appraisal-tag-without-expectedness comparison; measure downstream effect after prediction-error is controlled.

7. **Handoff artifact production (1-2h).** `phase-1-report.md` documenting per-Condition PASS/FAIL + specific empirical measurements + honest weakness flags.

### Phase 1 handoff artifacts

Produce `~/Desktop/appraisal-tag-gate-phase-1-handoff-YYYY-MM-DD/` folder containing:
- `phase-1-report.md` — Conditions 1-4 results with PASS/FAIL classifications + measurement summaries
- `phase-1-data.csv` — per-fixture measurements exported for operator ratification
- `phase-1-limitations.md` — honest weakness flags

---

## Phase 2 — Operator + Playtester coordination (RESEARCH-AGENT surface)

**Estimated cost: 20-40 hours (operator + playtester + statistical analysis)**

**Objective:** execute Substrate C multi-Sim protocol for player-visible ratification per Post 0138 validation-vs-ratification discipline.

Deferred to operator-scheduled Phase 2+ empirical work per Post 0136 pause discipline. Details in Substrate C's specification (Post 0140 Decision 5).

---

## Phase 3 — Operator ratification + write-back (Claude Code executes)

**Estimated cost: 1-2 hours operator + 2-4 hours Claude Code**

**Objective:** operator reviews Phase 1 handoff + Phase 2 handoff (if executed); ratifies aggregate verdict (or contests it); Claude Code executes canonical mutations matching ratified verdict.

### Phase 3 task list

1. **Operator reads Phase 1 handoff report** (+ Phase 2 handoff if executed).
2. **Operator ratifies aggregate verdict or contests.** Per Rule 10 Conservative-Bias, ambiguous ablation results default to KEEP RESERVED unless operator has design-side reason to force operationalization decision.
3. **Claude Code executes canonical mutation per ratified verdict:**
   - **If OPERATIONALIZE ratified:** produce V1.x operationalization spec (new post + SUMMARY.md update + post-ideas.md status). Cost estimate: 40-80 hours BUILD-side work per Post 0140 Decision 1 CORE member.
   - **If RETIRE ratified:** schema migration removes the reserved slot; forward-reference amendment documents the empirical finding; SUMMARY.md updated; auto-memory documents the retirement.
   - **If PARTIAL ratified:** operationalize CORE members (agency_attribution + coping_control) while retiring or deferring CANDIDATE-PENDING-GATE (goal_congruence) per per-item ratification.
4. **Update auto-memory** regardless of verdict.
5. **Run `~/Projects/master-setup/regen_launcher_hashes.py`** to refresh CC nav payload if posts change.

---

## Anti-armor discipline extension (Post 0140 Decision 6)

The reserved `appraisal_tags[]` slot does NOT become a decorative label without operational commitment. Specific commitments:

- The slot's members must be either operationalized per the ablation-battery pass criteria OR retired-with-empirical-record documenting why the slot did not ratify. The reservation-only-permanent status is NOT the target.
- `agency_attribution` does NOT become a demographic proxy. If Phase 1 or Phase 2 reveals empirical-driven-by-demographic-features, the field is retired rather than operationalized as demographic proxy.
- `coping_control` does NOT operationalize below the framework's operator-ratifiable signal-magnitude threshold. If Phase 2 multi-Sim signal is below-threshold, the field is retired rather than operationalized on below-threshold empirical foundation.
- `goal_congruence` CANDIDATE-PENDING-GATE status is disclosed at schema-placeholder documentation; no operationalization commitment pre-ablation.

The anti-armor discipline is the framework's canonical commitment to prevent schema-placeholder inflation without operational depth.

---

## Cost aggregation

| Phase | Surface | Estimated cost |
|---|---|---|
| Phase 1 (single-Sim ablation battery) | Claude Code | 10-18h |
| Phase 2 (multi-Sim playtester ratification; deferred) | Operator + playtesters | 20-40h |
| Phase 3 (operator ratification + canonical mutations) | Operator + Claude Code | 3-6h |
| **Total ablation gate execution** | **Composed** | **33-64h** |
| V1.x operationalization per CORE member (if PASS) | Claude Code | 40-80h |
| Schema retirement (if FAIL) | Claude Code | 2-4h |

Comparable to Post 0130 relationship-mode ablation gate (25-48h) and Post 0135 per-NPC-philosophy-profile ablation gate (25-48h per family). Slightly higher due to Phase 2 multi-Sim playtester coordination overhead.

---

## Cross-references

- **Post 0139** — Council #2 close narrative; documents Pattern B classification + Substrate B v1 pre-push framework-state discipline catch + orchestrator-layer primary-text adjudication catching A' template-placeholder-extraction-as-authorship
- **Post 0140** — Eight-decision amendment package spec + methodology insight artifact + Rule 14 n=4 empirical foundation + Rule 19 body extension canonizing PDF template-placeholder fabrication-axis sub-shape
- **Post 0128** — Schema-placeholder discipline precedent (cultural_context_tag + intersectional_position_tags[] + identity_stage); parallel pattern to `appraisal_tags[]` slot
- **Post 0130** — Council #1 relationship-mode reserved-slot spec; parallel reservation-plus-ablation pattern
- **Post 0135** — Council #4 per-NPC-philosophy-profile BANK spec; norm-violation routes here per Decision 1
- **Post 0118** — Consolidation architecture with four promotion criteria (affective spike + pair-history + trait-modulated + first-occurrence); Post 0140 Decision 4 forward-reference amendment notes agency/blame absent from criteria
- **Post 0137** — H4 prediction-error sparse encoding; Substrate B's Condition-4 clamp test decides whether expectedness needs distinct member field
- **`~/Projects/the-street-code/methodology/per-npc-philosophy-profile-reservation-and-ablation-gate-v1.md`** — sibling methodology guide; Post 0140 Decision 3 modifies its Condition 2 procedure
- **`~/Projects/the-street-code/_archive/2026-07-02-council-2-appraisal-tags/`** — Council #2 substrate outputs (A/A'/B v1 + v2/C/D) + orchestrator synthesis
- **`~/.claude/projects/-Users-jimmy/memory/project_council_2_close_pattern_b_2026-07-02.md`** — Council #2 arc close memory
- **`~/.claude/projects/-Users-jimmy/memory/feedback_substrate_pdf_template_placeholder_extraction_as_authorship_new_2026-07-02.md`** — new fabrication-axis sub-shape memory
- **`~/.claude/projects/-Users-jimmy/memory/feedback_canonization_propagation_gap_memory_layer_vs_canonical_file_layer.md`** — Council #2 deploy CW sanity check catch memory

---

## Guide revision protocol

Update this guide when:
- Any phase runs and surfaces a procedure refinement (Phase 1 fixture design, Phase 2 recruitment protocol, Phase 3 ratification pattern)
- Post 0140 Decision 3 per-NPC-philosophy-profile ablation-gate Condition-2 modification runs and surfaces cross-guide integration insight
- The paired substrate-discipline lesson evolves (deployment prompt calibration changes)
- Framework canonical files that this guide cross-references update in ways that affect guide content

Do NOT retroactively edit the guide's core procedure after a phase begins execution; per the framework's immutability convention, mid-execution scope changes are anti-pattern territory. Add dated update-notes at the guide's foot instead.
