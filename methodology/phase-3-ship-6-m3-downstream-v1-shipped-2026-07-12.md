# Phase 3 Ship 6 M3 Downstream Composition Wires v1 — SHIPPED
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL
**Ship commits:** sim-ai + manifest; roomtolife pushed

---

## §1 Scope

Fourth Phase 3 composition wire cascade ship. Activates 2 M3 v1 wires from M3 §7 deferrals. W2/W4-W7 remain v2+.

**Activated:**
- **W1** dynamic task-goal seeding — activates M3 §9 "W5 dormant substrate wire" deviation to behavioral mutation (spec: when Sim's active project goal has children task-goals, spawn task goal with reference-state matching current context)
- **W3** 2-identity-goal velocity-signal arbitration (spec v1: max 2 active identity goals per Sim; higher-velocity goal wins; loser enters 'blocked' status until velocity recovers)

**Higgins CONTESTED-MODERATE preserved:** DO NOT commit to dejection-vs-agitation split in arbitration; structural check via H4.

## §2 Empirical Anchors (K=2 verified from M3 candidacy)

- **Locke-Latham 2002** *Am Psych* 57(9):705-717 — goal specificity + difficulty
- **Higgins 1987** *Psych Review* 94(3):319-340 CONTESTED-MODERATE (collapsed-channel discipline per Council #11 Item 184)
- **Carver-Scheier 1998** hierarchical control — task completion progress propagation

## §3 Architecture

**New helpers:**
- `spawnTaskGoalForProject` — dynamic seeding when project goal + matching action affordance
- `mapActionIdToGoalCategory` — action → goal category mapping
- `spawnSecondIdentityGoal` — 2nd identity goal creation
- `arbitrateIdentityGoals` — velocity-based arbitration + block/unblock dynamics

**New constants:**
- `TASK_GOAL_SEEDING.MAX_TASK_GOALS_PER_PROJECT = [omitted]` (Miller 1956 chunking family)
- `TASK_SPECIFICITY_LIFT_ABOVE_PROJECT = [omitted]` (Locke-Latham direction; magnitude CALIBRATION-CHOICE)
- `HIGGINS_ARBITRATION.VELOCITY_TIE_TOLERANCE = [omitted]e-6` (numerical stability)
- `HIGGINS_ARBITRATION.VELOCITY_UNBLOCK_THRESHOLD = [omitted]` (stall detection)

**Wire sites:**
- W1: `completeAction` in islandWorld.ts BEFORE existing W5 matcher; bounded by MAX_TASK_GOALS_PER_PROJECT + MAX_GOALS_PER_SIM (32); idempotent per (projectGoalId, actionId) tuple
- W3: `tickIslandWorld` M3 progress block AFTER `evaluateGoalHierarchyProgress`; dynamic (not one-shot) — blocked goals unblock when they recover velocity + active stalls

## §4 Non-Inertness Gate Verdict

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/ship6M3Downstream.test.ts` (26 tests)

- **H1 PRIMARY (Locke-Latham 2002):** dynamic seeding ≥3 task goals per active project across matching action-affordances — PASS
- **H2 PRIMARY (Higgins 1987):** 2-identity-goal Sim → velocity-based arbitration produces 100pp status split (≥15pp threshold) — PASS
- **H3 VALIDITY (Carver-Scheier 1998):** task completion propagates progress up to project-level via existing `onGoalCompleted` path — PASS
- **H4 VALIDITY (Higgins CONTESTED-MODERATE collapsed):** no dejection/agitation channel-committing fields on GoalNode or HIGGINS_ARBITRATION constants — PASS (structural check)
- **H5 EDGE-CASE:** 3rd identity goal rejected; max 2 active enforced — PASS

**Verdict:** PASS 26/26 @ 100% clear rate

## §5 Rule 19 Flags Surfaced

**CALIBRATION-CHOICE:**
- MAX_TASK_GOALS_PER_PROJECT = [omitted] (Miller 1956 chunking family)
- TASK_SPECIFICITY_LIFT_ABOVE_PROJECT = [omitted] (Locke-Latham direction only)
- HIGGINS_ARBITRATION.VELOCITY_TIE_TOLERANCE = [omitted] (numerical stability)
- HIGGINS_ARBITRATION.VELOCITY_UNBLOCK_THRESHOLD = [omitted] (stall detection)

**COLLAPSED-CHANNEL discipline preserved:**
- Council #11 Item 184 discipline extended to M3 arbitration substrate
- Arbitration path does NOT commit to dejection-vs-agitation channel split
- H4 structural check verifies absence of channel-committing fields

**REJECT-STALE:** None

## §6 Framework Methodology Firsts

- FIRST M3 dynamic task-goal seeding (activates M3 §9 W5 dormant substrate)
- FIRST M3 2-identity goal arbitration wire
- FIRST Higgins CONTESTED-MODERATE collapsed-channel discipline extended to M3 arbitration substrate
- FIRST velocity-signal arbitration with block/unblock dynamics
- FIRST idempotent-tuple-keyed goal seeding pattern

## §7 Deviations from Spec

**Test count 26 vs 15-20 spec target:** +6 tests for backward-compat + baseline preservation section; no scope creep or test omission.

**Postmortem:** 2 anomalies `signal_for_rescue_without_rescue_outcome` present at Ship 5 baseline; preexisting rescue calibration issue unrelated to Ship 6 wires. Waived per rescue-arrival calibration follow-up track.

**Deferred per M3 §7 v2+:**
- W2 cultural bundle priors (Iyengar-Lepper 1999)
- W4 Ordóñez 2009 goals-gone-wild
- W5 Wrosch 2003 disengage-reengage
- W6 Locke-Latham public-commitment amplifier (Hollenbeck 1989)
- W7 Sheldon-Kasser 2001 goal-content well-being

## §8 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/85 files
- sim-ai full test suite: **2529 pass** (baseline 2503 → +26 Ship 6 tests; preexisting phaseD flaky surfaced on 1 concurrent run then passed on isolated re-run)
- sim-ai postmortem: 2 preexisting anomalies waived (Ship 5 baseline reproducibility)
- roomtolife precheck: GREEN

## §9 Council #11 Candidacy

**Item 216 filed:** Phase 3 Ship 6 M3 downstream composition wire v1 ratification.

Sub-items:
- 216.1 W1 dynamic task-goal seeding activation discipline (idempotent per tuple + bounded)
- 216.2 W3 2-identity goal velocity-signal arbitration + block/unblock dynamics
- 216.3 Higgins CONTESTED-MODERATE collapsed-channel discipline extension to M3 arbitration (Item 184 continuation)
- 216.4 CALIBRATION-CHOICE magnitude preservation (MAX_TASK_GOALS_PER_PROJECT = [omitted] Miller 1956 chunking; TASK_SPECIFICITY_LIFT = [omitted] Locke-Latham direction)

## §10 Downstream Impact

**Enables Phase 3 Ship 7** (M7 downstream + naming collision resolution — 5 wires; final Phase 3 composition cascade ship).

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
