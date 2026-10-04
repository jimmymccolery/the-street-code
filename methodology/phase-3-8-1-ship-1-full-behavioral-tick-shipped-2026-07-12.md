# Phase 3.8.1 Ship 1 — Full Behavioral Tick Foundation — SHIPPED
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL
**Ship commits:** sim-ai; roomtolife pushed

---

## §1 Scope

Foundation ship unblocking all Phase 3.8.1 subsequent work. Promotes `tickSimB` perspective-swap shim → general `tickSimAny(state, simId, params, rng)` supporting K≥3 Sims. Generalizes `detectAndApplyPairInteractions` → `iterateAllPairs` at K≥3 mode. Backward-compat bit-identical at K=2.

## §2 Architecture

### tickSimAny(state, simId, params, rng)
- K=2 canonical: `tickSimAny(state, 'a')` delegates to `tickSingleSim`; `tickSimAny(state, 'b')` delegates to `tickSimB`
- K≥3 extension: full-behavioral per-Sim tick (Layer 3 + M1-M7 + needs + action selection)
- Nearest-neighbor projection for K≥3 `state.simB` slot needed by `decideNextAction` (deferred deep multi-target refactor to Phase 3.9+)

### detectAndApplyPairInteractionsN
- K=2 branch: canonical (a,b) pair delegated to legacy path
- K≥3 branch: `iterateAllPairs(state)` writes to `state.pairMatrix`
- Dead-Sim pairs safely skipped

### Backward-compat gate
`isNSimMode(state)` at `tickIslandWorld` body before tick increment. K=2 `state.sims === undefined` → returns false → N-Sim extension block is no-op → canonical path bit-identical.

## §3 Non-Inertness Gate Verdict — 5/5 PASS @ 100%

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/tickSimAnyFoundation.test.ts` (36 tests including preservation harness)

- **H1 PRIMARY K=2 bit-identical determinism** — 8 tests PASS. `phase1NonInertnessGate.test.ts` 46/46 preserved externally. `state.sims`/`pairMatrix`/`simCount` all remain undefined at K=2 across 200-tick fuzz.
- **H2 PRIMARY K=3 full-tick per-Sim action selection** — 7 tests PASS. Sim C accumulates actionHistory after 200 ticks; needs decay independently for a/b/c; dead/rescued Sims frozen semantics preserved.
- **H3 PRIMARY all-pairs O(N²) coverage** — 8 tests PASS. K=3→3 pairs, K=4→6, K=5→10, K=8→28 (all C(K,2) verified). Canonical (a,b) skipped in N-branch. Dead-Sim pairs safely skipped.
- **H4 VALIDITY Rule 28 defensive-reducer preservation** — 5 tests PASS. sims map + pairMatrix never nuked across 1000-iter fuzz; SimStateSnapshot future-field canary survives round-trip via `tickSimAny`; canonical `state.pair` legacy field preserved.
- **H5 VALIDITY deterministic replay at K=8** — 5 tests PASS. Same seed → bit-identical world state at 100 + 500 ticks; different seeds observably diverge; `listAllSimIds` insertion order stable across 50 ticks (Phase 2.9-C RNG discipline preserved).

Plus 3 substrate-presence sanity tests (K=3-8 smoke test loop).

## §4 Rule 19 Flags Surfaced

**None new.** Leverages Phase 3.8 primitives (`getSimStateById`, `iterateAllPairs`, `isNSimMode`, `readPairMatrixState`, `writePairMatrixState`, `createPairMatrix`) already ratified at Council #11.

**Nearest-neighbor projection for K≥3 `state.simB` slot** is documented CALIBRATION-CHOICE per R3 §1.2 — deep multi-target refactor of `decideNextAction` deferred to Phase 3.9+.

**REJECT-STALE:** None

## §5 Framework Methodology Firsts

- FIRST full-behavioral N-Sim tick promoted from decay-only (populationScaleHarness → tickIslandWorld path via state.sims overlay)
- FIRST `tickSimAny` general per-Sim tick function
- FIRST `isNSimMode` gate discipline at tickIslandWorld
- FIRST backward-compat bit-identical preservation at K=2 with N-Sim extension
- FIRST all-pairs O(N²) O(N²) iteration via iterateAllPairs at K≥3
- FIRST nearest-neighbor projection for `state.simB` slot resolution at K≥3

## §6 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/87 files
- sim-ai full test suite: **2818 PASS** (baseline 2782 → +36 Ship 1 tests across 144 test files)
- sim-ai postmortem: 2 preexisting anomalies (signal_for_rescue_without_rescue_outcome calibration; identical to parent d798fa2; waived per CLAUDE.md sub-step discipline)
- roomtolife precheck: verify-vendor 252/252 PASS

## §7 Deviations from Spec

**One minor deviation:** `populationScaleHarness.tickNSimWorld` upgrade from decay-only → full-behavioral (~40 LOC per R3 §1.4) NOT executed at Ship 1. Rationale: this ship's H1-H5 hypotheses target the Phase 3.8 `state.sims`/`pairMatrix` overlay path (via `createInitialNSimWorldState`), not the legacy `additionalSims` structure at `populationScaleHarness`. All 5 hypotheses PASS against the `state.sims` overlay path.

The `additionalSims` legacy path can be swapped/deprecated at Ship 7 (H4 N=8 performance harness) which is architecturally paired with harness re-authoring.

**Substrate scope:** ~494 LOC substrate + ~636 LOC tests (vs. spec ~810/~800; delta absorbed by leveraging existing Phase 3.8 primitives more heavily than initial estimate).

## §8 Council #11 Candidacy

**Item 231 filed:** Phase 3.8.1 Ship 1 Full Behavioral Tick Foundation ratification.

Sub-items:
- 231.1 tickSimAny general per-Sim tick function
- 231.2 detectAndApplyPairInteractionsN with iterateAllPairs
- 231.3 isNSimMode gate discipline
- 231.4 Nearest-neighbor projection for state.simB slot at K≥3 (CALIBRATION-CHOICE)
- 231.5 populationScaleHarness legacy path deferred to Ship 7

## §9 Downstream Impact

**Enables Phase 3.8.1 Ships 2-7:**
- Ship 2 M9 K≥3 activation cascade (independent, unblocked)
- Ship 3 F2 Boehm coalition activation (depends on Ship 2 for `formCoalitionGroupFromBoehm`)
- Ship 4 F4 Sommerfeld witness triangle activation (depends on Ship 2 for `applyGossipIntergroupDrift`)
- Ship 5a M5+M1+M2+M3 N-Sim propagation
- Ship 5b M6+M4+M7 N-Sim propagation
- Ship 6 UI extensions (N-tab + palette + CPCM)
- Ship 7 H4 N=8 performance harness

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
