# UI Ship C — Tier 2 Gauge Additions — SHIPPED
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL
**Ship commits:** sim-ai; roomtolife pushed

---

## §1 Scope

3 Tier 2 gauges per Ship C research at `/tmp/ui-ship-c-research.md`. Research-enriched design; single substrate addition (§2 pure helper) + UI overlay.

## §2 Additions

### Gauge 1: M2↔M1 Feedback Oscilloscope (§10.10 SelfModelPanel; ~157 LOC UI)
Overlay dual-signal chart per research:
- M2 `selfWorthThreatSignal × 100` (red)
- M1 `self_esteem_b` (cyan)
- Translucent yellow shading over ticks where SWT > `HIGGINS_COLLAPSED.SOCIOMETER_AMPLIFICATION_THRESHOLD` (0.5; amplifier gate active)

UI-side 300-tick ring buffer per-Sim in IslandSimulation.tsx mirroring `pairRelationalHistory` pattern. Sample every tick. Phase-lag detection DEFERRED per anti-gold-plating (Ship D candidate).

### Gauge 2: Directionlessness Continuous Meter (§10.7 NarrativeRecapPanel; ~230 LOC total)
Replaces binary Slice 2 `detectDirectionlessness` output with continuous [0, 1] score:

```
score = [formula omitted]
```

Where:
- `r_ratio = clamp01(opens/max(1,closes) / 3.0)` over 200-tick window (Kreminski Loose Ends anchor)
- `r_stagnation = clamp01((tick - maxLandmarkTickInWindow) / 200)` (Kreminski anchor)
- `r_frust = avg(relatedness_frust_a, relatedness_frust_b) / 100` (M5 composition)
- `r_velocity = clamp01(1 - avg(|lastVelocitySignal|) / 0.10)` (M3 Carver-Scheier)

Color bands: green 0-0.30 / yellow 0.30-0.60 / red 0.60-1.0. Preserves solid red DIRECTIONLESS pill when score ≥ 0.6 AND binary predicate fires.

**Substrate change:** new pure `computeDirectionlessnessScore` helper (156 LOC substrate + 43 test LOC) leaving existing `detectDirectionlessness` + `applyDirectionlessnessDetection` unchanged; 4 existing Slice 2 tests preserved.

### Gauge 3: M6 hyperactivationBranch Chip Promotion (§10.12 AttachmentTraumaPanel; ~35 LOC)
Colored chip replacing plain-text render at lines 3026-3037. Own-view only per Bowlby subjective working models. Uses existing `HYPERACTIVATION_BRANCH_COLOR` map. New `HYPERACTIVATION_BRANCH_GLYPH` map. Preserves contradictory-branch red 2px border at :2987. Timestamp OMITTED (branch quasi-static — derives from AttachmentStyle at Sim creation via `classifyHyperactivationBranch`).

**Branch enum correction (from research):** substrate uses `hyperactivation/deactivation/balanced/contradictory` — NOT `secure/anxious/avoidant/disorganized` (those are AttachmentStyle categories that MAP TO branches).

## §3 Empirical Anchors

- **Oscilloscope:** Higgins 1987 CONTESTED-MODERATE collapsed + Lazarus-Folkman 1984 + Leary-Baumeister 2000 M1 sociometer
- **Directionlessness score:** Kreminski Loose Ends AIIDE 2022 (2 anchored signals: ratio + stagnation) + Ryan-Deci 2000 M5 relatedness + Carver-Scheier 1998 M3 velocity
- **M6 chip:** Bowlby 1969 subjective internal working models + Mikulincer-Shaver 2003 meta-strategy classification

## §4 Non-Inertness Gate Verdict

Test file: `narrativeRecapSlice2.test.ts` — 2 new tests:
- **H_C1 monotonicity:** open thread without close raises score — PASS
- **H_C2 composition:** relatedness_frust rise alone raises score — PASS

Test count: 2780 → 2782 (+2)

## §5 Rule 19 Flags Surfaced

1. **§1 phase-lag detection DEFERRED** per anti-gold-plating (Ship D candidate for cross-correlation `argmax_lag Σ swt(t)·se(t-lag)`)
2. **§2 weights CALIBRATION-CHOICE** (values omitted)
3. **§2 EMPIRICAL-TRANSLATION** on M5 relatedness_frust + M3 velocity composition (only Kreminski ratio + stagnation signals empirically anchored)
4. **§2 DIRECTIONLESSNESS_VELOCITY_REF = [omitted] CALIBRATION-CHOICE** (framework baseline expectedVelocity 0.03 task / 0.05 identity; 0.10 as active-progress ceiling)
5. **§3 branch quasi-static in current substrate** — derives from AttachmentStyle at Sim creation; timestamp OMITTED to avoid misleading UI
6. **§3 branch enum correction** — substrate uses `hyperactivation/deactivation/balanced/contradictory` NOT `secure/anxious/avoidant/disorganized`

## §6 Framework Methodology Firsts

- FIRST M2↔M1 feedback loop live plot (dual-signal overlay + amplifier-gate shading)
- FIRST directionlessness continuous meter replacing binary Slice 2 predicate output
- FIRST M6 hyperactivation branch styled chip promotion (own-view only per Bowlby internal working models subjectivity)
- FIRST slice2 pure helper co-existence pattern (`computeDirectionlessnessScore` alongside existing `detectDirectionlessness` + `applyDirectionlessnessDetection` — backward-compat preservation)
- FIRST Ship-B ↔ Ship-C parallel-flight collision-free execution on shared IslandStage345Panels.tsx monolith (Ship B landed first at ed9d7e5; Ship C picked up baseline cleanly at a6fe5ed)

## §7 Ship Verification

- sim-ai typecheck: PASS
- sim-ai Rule 28 audit: PASS 0/87 violations
- sim-ai full test suite: **2782 PASS** (baseline 2780 → +2 H_C1 + H_C2)
- roomtolife precheck: GREEN (typecheck + build 4.9s + manifest verify)

## §8 Deviations from Research Spec

- **Vendor commit split** (research spec assumed single roomtolife commit): roomtolife commit-msg hook enforces `vendor-sync:` prefix separately from feature commits (project discipline gate). Vendor sync landed as sibling prior to UI.
- **§2 wrapper IIFE** for host binding — computes score once shared across both Sim A/B NarrativeRecapPanel instances; ~15 LOC style choice not in research spec.
- **§1 oscilloscope inline in SelfModelPanel** (not standalone panel like §11e); attached as titled section following M2 appraisal chip pair per research §1 layout intent.
- **LOC overshoot §2 (~230 vs research 90):** substrate helper docblock verbosity + comprehensive Rule 19 flags + wrapper IIFE for host binding.

## §9 Council #11 Candidacy

**Item 228 filed:** UI Ship C Tier 2 gauges ratification.

Sub-items:
- 228.1 M2↔M1 oscilloscope + amplifier-gate shading discipline
- 228.2 Directionlessness continuous meter formula (weighted sum with 2 empirically-anchored + 2 EMPIRICAL-TRANSLATION signals)
- 228.3 Slice 2 pure helper co-existence backward-compat pattern
- 228.4 M6 hyperactivation branch chip promotion (own-view only + branch enum correction from research prompt)
- 228.5 Ship B↔C parallel-flight collision-free execution pattern

## §10 Downstream Impact

**Enables Ship D** (Tier 3):
- Bowlby × Hierarchy interaction gauge — architectural projection (M6→F2 wire does not exist per Ship D+E research; requires Council #11 candidacy filing for real wire)
- Shared-suffering cohesion composite (M6+D4+F1)
- D5 Compass of Shame active-branch routing (world-scope state at `islandWorld.ts:1008` fully queryable per Ship D+E research)
- Memory retrieval trace (requires additive substrate change: `retrievedTraces` field on `MemoryInformedDecisionInfo`)

**Enables Ship E** (legacy audit): Layer3TrajectoryChart patch (~50-75 LOC) — only real stale panel per Ship D+E research (5-channel legacy vs canonical 9 channels missing relational_integrity_b + communal_standing_b + self_esteem_b).

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
