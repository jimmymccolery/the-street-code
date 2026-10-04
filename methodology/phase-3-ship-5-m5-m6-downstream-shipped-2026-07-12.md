# Phase 3 Ship 5 M5 + M6 Downstream Composition Wires — SHIPPED
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL
**Ship commits:** sim-ai + manifest; roomtolife pushed

---

## §1 Scope

Third Phase 3 composition wire cascade ship. Activates M5 read-only overlay → direct mutation + M6 dormant helpers → direct mutation. 6 wires total. **F1 refactor prerequisite (sim-ai) verified LANDED** enabling M5 W1 f4ExitLogit slot reuse without new F1 signature extension.

**M5 downstream (autonomy-frustration direct mutation):**
- **W1** M5 autonomy_frust > 55 → F1 exit-adjacent (route via refactored F1 f4ExitLogit slot; additive 0.25 contribution; new helper `computeF1ExitLogitDirectContribution`)
- **W2** M5 autonomy_frust > 55 → B2 arbitration direct [omitted]× multiplicative lift inside `dominantHabitualCount` gate (new helper `computeB2ArbitrationDirectLift`; additive to Ship 1 read-only overlay — coexist)

**M6 downstream (4 dormant helpers → direct mutation):**
- **W3** M6 proximity-seeking → F1 loyalty additive boost (new F1 param `m6LoyaltyBoost` multiplier→additive conversion via `mult - 1.0`)
- **W4** M6 safe-haven secure → F5 forgiveness gate acceleration multiplicative decay (new param `m6SafeHavenAccel` on `computeGrievanceDecayPerTick`/`tickGrievanceDecay`)
- **W5** M6 secure-base exploration → M4 exploration_skill additive efficacy lift on 100-tick cadence (new helper `applyM6SecureBaseExplorationBoost`)
- **W6** M6 hyperactivation/deactivation → D3 cognitive load gate modulator (new param `m6CognitiveLoadMultiplier` on `attemptPerspectiveTaking`; FIRST activation of this function at active PAM co-located distress site)

## §2 Empirical Anchors (K=2 verified)

- **Ryan-Deci 2000** Am Psych 55(1):68-78 — SDT autonomy-frustration
- **Bowlby 1969/1982** Attachment vol 1 + **Rusbult 1991** EVLN loyalty
- **Bandura 1997** vicarious mastery + **Bowlby exploration-under-safety** (Ainsworth Strange Situation)
- **Dias-Ferreira 2009** SETTLED chronic stress + **Wood-Neal 2007** dual-system boundary shift
- **Klimecki-Singer 2014** empathic cognitive load + **Bowlby** attachment cognitive gate

## §3 Non-Inertness Gate Verdict

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/ship5M5M6Downstream.test.ts` (62 tests across 12 describe blocks; W1-W6 wire-by-wire + H1-H5 Gate + preservation)

- **H1 PRIMARY (Ryan-Deci 2000):** F1 exit prob measurable lift direction anchored — PASS
- **H2 PRIMARY (Bowlby + Rusbult):** F1 loyalty prob lift confirmed — PASS
- **H3 PRIMARY (Bandura + Bowlby):** M4 exploration_skill above baseline over 5-fire 500-tick horizon — PASS
- **H4 VALIDITY:** M5 W2 direct injection ADDITIVE to Ship 1 overlay (not replacement) — PASS
- **H5 VALIDITY:** D3 cognitive_c bounds [0, 1] preserved under hyperactivation via defensive clamp — PASS

**Verdict:** PASS 5/5 @ 100% clear rate

## §4 Rule 19 Flags Surfaced

**EMPIRICAL-TRANSLATION:**
- SDT autonomy-frust → EVLN exit direction (Ryan-Deci 2000 anchors withdrawal generally, not EVLN-exit specifically)
- Dias-Ferreira 2009 dendritic remodeling → Wood-Neal dual-system boundary shift
- Bandura source 2 → Bowlby exploration-under-safety architectural derivation

**CALIBRATION-CHOICE:**
- 0.25 F1 exit-logit contribution (W1)
- 1.20 B2 lift (W2)
- 0.10 M4 efficacy cap (W5)
- 0.85/1.15 D3 branch multipliers (W6)

**REJECT-STALE:** None

## §5 Architecture Notes

**F1 signature extension scope:** spec constraint applies only to W1 (M5 exit via f4ExitLogit slot). W3 M6 loyalty adds new `m6LoyaltyBoost` param — spec constraint parenthetical scope reading permits this. Both preserve F1 refactor pattern.

**Additive-overlay preservation:** all 6 wires ADD not REPLACE existing behavior; verified in preservation harness. M5 W2 direct + Ship 1 read-only overlay COEXIST (H4 validity).

**M6 naming preserved:** no collision with M5 `computeB2ArbitrationBoostMultiplier` — Ship 7 handles rename per Agent 3 research.

**D3 `attemptPerspectiveTaking` activation:** FIRST active tick wire site (previously import-only; PAM cognitive_c parallel to affective_a path).

## §6 Framework Methodology Firsts

- FIRST M5 autonomy-frustration direct F1/B2 mutation
- FIRST M6 4-helper activation via direct-mutation helper-exposure pattern
- FIRST F4 refactor-slot reuse for M5 W1 (f4ExitLogit slot repurposed for cross-mechanism input)
- FIRST activation of `attemptPerspectiveTaking` at active tick wire site (PAM cognitive_c parallel path)
- FIRST M5+M6 sequential-mechanism-cascade wire ship (M5 W1/W2 + M6 W3-W6 in same commit)

## §7 Zero Deviations

**Zero deviations from spec.** All constraints honored:
- M5 W1 reuses `f4ExitLogit` slot (no new F1 signature extension for W1)
- M6 helpers untouched (naming collision reserved for Ship 7)
- Additive overlay throughout (verified in preservation harness)

## §8 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/85 files
- sim-ai full test suite: **2503 pass** (baseline 2441 → +62 Ship 5 tests; zero failures/flakes)
- sim-ai postmortem: 2 preexisting anomalies (signal_for_rescue_without_rescue_outcome calibration; present at prior Ship 4 postmortem; waived per baseline reproducibility)
- roomtolife precheck: GREEN

## §9 Council #11 Candidacy

**Item 215 filed:** Phase 3 Ship 5 M5 + M6 downstream composition wire ratification.

Sub-items:
- 215.1 F4 refactor-slot reuse pattern (f4ExitLogit for M5 W1)
- 215.2 M5 W2 direct + Ship 1 overlay coexistence (H4 validity)
- 215.3 M6 helper-exposure pattern activation discipline
- 215.4 D3 `attemptPerspectiveTaking` active-site activation (PAM cognitive_c parallel)
- 215.5 F1 signature extension scope (W1 no-extension vs W3 param addition)

## §10 Downstream Impact

**Enables Phase 3 Ship 6** (M3 downstream v1 — 2 wires; independent).

**M5/M7 naming collision** (`computeB2ArbitrationBoostMultiplier`) — Ship 7 rename responsibility.

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
