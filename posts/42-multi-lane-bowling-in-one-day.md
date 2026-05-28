# We shipped multi-lane bowling in one day: Phase 6.1 BUILD complete in 40 commits

**Author:** Jimmy McColery
**Date:** 2026-05-27
**Status:** Single-session arc writeup from one BUILD execution day; n=1, suggestive not conclusive on phase-decomposition discipline at this refactor scale

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

The companion to this post (Post 41: "13 architectural-lock cycles in 7 days") covered seven days of pre-BUILD architectural lock discipline. This post is what happened on day eight: 40 commits across one working day, multi-lane bowling shipped, zero broken-main commits, an operator-side visual test cycle between every BUILD phase that caught one substantial bug before it could compound.

The top-line number (40 commits in a day) is the headline. The real story is the discipline that made the day possible. This post walks through what shipped, how the phase-decomposition pattern contained the work, and what the visual-test cycle caught.

## What the refactor actually was

The codebase I was working in is a bowling-alley tycoon sim I've been building solo. Before day eight, it rendered one interactive bowling lane: one bowler walking up to a throw line, one bowling ball rolling down one lane, one rack of ten pins, one CRT-style scoresheet overhead. All physics ran in a Rapier (the WebAssembly physics engine react-three-rapier wraps for React Three Fiber) world that lived inside the lane component itself.

The Phase 6.1 BUILD refactor took that single-lane architecture and made it four-lane: two lanes with full Rapier physics including interactive bowlers, two lanes with statistical resolution running on a 1Hz background simulator (no physics; pin state advances via simple weighted RNG every 1000 milliseconds; visually indistinguishable from "someone's bowling there" without the physics cost). The Rapier world moved up to a multi-lane scene wrapper; per-lane Rapier collision groups prevented the bowling ball on one lane from colliding with pins on the other lane (40 meters of cross-bank distance in the world coordinates); the React state-management layer (Zustand) shifted from a single-lane state shape to a `Record<string, LaneState>` keyed by lane ID, with per-lane action targeting and a per-lane phase timer hook running independent gameplay loops.

That's the surface description. The architecturally invasive part is the per-lane state shape transition (every component reading from the store had to migrate from `useAlleyStore(s => s.phase)` to `useAlleyStore(s => s.lanes[s.focusedLaneId].phase)` or to a new `useFocusedLane(s => s.phase)` convenience hook) and the physics-provider relocation (which introduced a latent component-persistence bug that surfaced under a specific keystroke sequence; more on that below).

## The seven-phase decomposition

The pre-BUILD architectural-lock arc had produced a sub-design proposal that decomposed the refactor into seven discrete phases. The proposal was ratified by a multi-substrate AI review process (the methodology covered in Post 41 plus an architectural-design pattern I'll cover in a follow-up post). The phases:

- **Phase 0: Pre-work prerequisites.** Zero behavioral change target. Refactor existing utilities into shapes that the multi-lane phases will need.
- **Phase 1: Module split.** Extract pure lane logic plus types plus spatial constants from the existing state store into a sibling pure-logic module. Zustand orchestration stays in the original store.
- **Phase 2: Multi-lane state shape transition.** Replace the single-lane state shape with `Record<string, LaneState>`. Update all consumer components to lane-aware access patterns.
- **Phase 3: Multi-lane R3F architecture.** Per-lane scene rendering. Lane context. Camera-focus spline. Visual markers for non-focused active lanes.
- **Phase 4.A: Physics architecture refactor.** Move the Rapier `<Physics>` provider from per-lane scene up to the multi-lane root. Single shared physics world.
- **Phase 4.B: Statistical lane visuals.** Replace placeholder geometry for the non-physics lanes with decorative lane rendering (floor plus pin meshes; no Rapier).
- **Phase 4.C: Statistical resolution orchestrator.** 1Hz background simulator advancing the statistical lanes' state machines.
- **Phase 4 full-acceptance-gate.** Render BOTH physics lanes simultaneously (was just the focused one through Phase 4.C). Per-lane Rapier collision groups. Per-lane RigidBody management.
- **Phase 5: Test scaffolding.** Vitest atomicity unit tests on the per-lane state transition functions. 41 new tests covering factories plus spatial helpers plus collision-group encoding plus atomicity invariants.

Each phase was a discrete commit (or two if bug-fix iteration was needed). Each phase had a stated acceptance gate. Phase 2's acceptance gate, for example, was "single-lane behavior preserved at first V1 lane" (because the multi-lane shape was in place but rendering still happened only at the focused lane). Phase 4.A's acceptance gate was "single shared Physics world architecturally in place; focused lane gameplay unchanged." Phase 5's was "test coverage gates atomicity preservation plus collision-group encoding correctness."

## The visual-test cycle

After each phase committed, I'd run the dev server in a browser and exercise the focused lane: bowl a frame, watch the bowler walk up, watch the ball roll, watch the pin reset, verify the scoresheet updated. If the visual test caught something off (a bowler appearing in the wrong place, a ball trajectory looking weird, a pin failing to reset), I'd diagnose the bug in conversation, apply a fix, commit the fix as part of the same phase, re-run the visual test, then move to the next phase.

The cycle caught one substantial bug. After Phase 4.A (the physics-provider relocation), a focus-change keystroke sequence I'd added as a dev keybinding produced a state where the bowler became visible at an off-lane spawn position instead of resuming whatever animation state they were in. Took three fixes to fully resolve. Each fix lived in its own commit because the phase-decomposition discipline contained the bug to its own phase rather than letting it compound across phases. I'll cover the three-system interaction that produced the bug in a separate post; the short version is that the visible symptom traced to interactions between React JSX prop diffing, Rapier RigidBody position re-application, and Zustand subscribe default semantics.

The bug-fix cycle added two extra commits to the day's count. Without the per-phase visual test discipline, the bug would have shipped past Phase 4.A and surfaced later under harder-to-bisect circumstances. Catching it inside its own phase meant the diagnosis took one focused conversation; catching it three phases later would have meant disentangling the symptom from intervening changes.

## Representative commits

The 10 BUILD-phase commits ran from `39b2cd6` (Phase 0 pre-work complete) through `f0aff17` (Phase 5 test scaffolding complete; Phase 6.1 BUILD-complete declared). A few representative hashes:

- `39b2cd6` (Phase 0): pre-work refactor; pin rack origins moved to a factory function; scoring outcome reducer converted from imperative to pure functional shape returning a `Partial<LaneState>` delta
- `1a4e761` (Phase 2): multi-lane state shape transition; `Record<string, LaneState>` introduced; all 10 consumer components migrated to lane-aware access
- `0670441` (Phase 4.A): physics architecture refactor; `<Physics>` provider moved from per-LaneScene up to multi-lane root
- `0f876b8` (Phase 4 full-gate): multi-physics-lane simultaneous rendering; per-lane collision groups encoded via the Rapier `interactionGroups` bit-encoding pattern
- `f0aff17` (Phase 5): 41 vitest tests covering atomicity plus spatial helpers plus collision-group encoding

The full sequence is in the public repo's commit log.

## The ending state

By close of day, the dev server rendered four lanes simultaneously. Two physics lanes with full Rapier simulation: a bowler walks up to the throw line on each, throws independently of the other lane's bowler, the ball rolls under physics, pins scatter on impact, the scoresheet updates per-lane. Two statistical lanes with the background simulator: lane geometry visible at its world-space spatial offset, pin meshes toggling between standing-and-fallen visually every second or so as the RNG produces statistical throw outcomes. A dev keybinding cycles focus across the four lanes; the camera animates through a three-stage spline (pull back, pan across, push in) over 1.5 seconds.

The 41 vitest tests covered the pure-function layer: factory functions producing valid lane state, spatial offset application across coordinate translation, collision-group bit encoding correctness, scoring reducer atomicity (the per-lane state transition function must produce a single composed delta object covering all atomicity-related fields, so the caller can apply via one Zustand `set()` call without intermediate renders showing partial state). All 41 passing.

## Why the discipline shipped the speed

The counter-narrative claim is that phase decomposition plus visual-test cycle is what enabled shipping multi-lane in a day, not what slowed it down. Three reasons the discipline pays off at refactor scale:

First, each phase is reversibly small. Phase 4.A teleported a load-bearing component up the tree; if it had broken something I couldn't fix, I could revert that one commit and have the architecture back at Phase 3 with everything else preserved. Big-bang refactors with everything in one commit lose this property.

Second, the visual test surfaces bugs at the smallest possible blast radius. The bowler-off-lane bug surfaced one phase after the change that introduced it. Three intervening phases later, the same symptom would have required bisecting against the intervening changes to localize. Smaller blast radius equals faster diagnosis.

Third, acceptance gates per phase prevent scope creep. Each phase had a stated acceptance criterion. When the criterion passed I moved on; when it didn't, I either fixed forward or reverted. There was no "while I'm here let me also fix..." pressure, because each phase's scope was bounded by its acceptance gate.

The decomposition discipline took time to produce (the sub-design proposal was ratified during the pre-BUILD design arc covered in Post 41). On the BUILD day, that pre-BUILD time compounded. Each commit could focus on its own scope without re-litigating an architectural decision that should have been settled. The discipline is what makes the speed possible; the speed is not what gets sacrificed to enable the discipline.

## What's next

Phase 6.2 is the next architectural cycle. The candidacy backlog includes worker-thread streaming serialization (the Q9 V1-critical-path implication from the architectural-lock arc), a perf-test sandbox for the Q5 §22 lane oil computational budget gate, and Float32 BVH macro-precision empirical validation at the cross-bank distances that the multi-lane physics world now needs to handle. The 5-month V1 Early Access target sits at October 31, 2026; the multi-lane infrastructure shipped on day eight is the foundation everything downstream compounds against.

Two companion posts are queued: one covering the seven-phase decomposition discipline as a generalizable methodology (the pattern applies to invasive refactors well outside R3F or game-sim contexts), one covering the three-system-interaction bug (React JSX prop diffing plus Rapier RigidBody position re-application plus Zustand subscribe default semantics) that the visual-test cycle caught during Phase 4.A.

## What I'm not claiming

I'm not claiming 40 commits in a day generalizes to all refactors. This was a specific decomposable architectural shift with cascading state-shape implications. Refactors without the cascade property (one-feature-at-a-time changes; local-scope additions) probably don't benefit from this much decomposition overhead.

I'm not claiming the 7-phase decomposition pattern is universal. I've fired it once at this scale; n=1. The pattern's generalizability is a claim I'd want more empirical anchors to defend.

I'm not claiming solo dev plus AI collaboration is faster than a senior-engineer team for this kind of refactor. This isn't a comparative study. It's a description of what one solo developer with multi-substrate AI orchestration plus a written pre-refactor design proposal produced over one working day.

I'm not claiming the bugs I caught with per-phase visual tests would have shipped to production. Some would have been caught later by automated tests or by integration testing; some by users. What I'm claiming is more specific: I avoided catching-cost compounding by catching the bowler-off-lane bug inside its own phase rather than three phases later.

What I am claiming: phase decomposition discipline at this refactor scale enabled shipping invasive multi-lane architecture in one working day without any broken-main commits and with operator-side bug catches that fired between commits rather than accumulating downstream. The pre-BUILD investment that produced the seven-phase decomposition (covered in Post 41) compounded measurably at BUILD time. For projects whose architectural decisions cascade, this kind of phase decomposition plus visual-test cycle plus per-phase acceptance gates is faster overall than the more common "one big merge" alternative.
