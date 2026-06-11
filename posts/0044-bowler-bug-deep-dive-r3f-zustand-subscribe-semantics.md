# The bowler-visible-at-off-lane-spawn bug: a React + R3F + Zustand subscribe semantics deep-dive

**Author:** Jimmy McColery
**Date:** 2026-05-27
**Status:** Single-finding bug deep-dive from one specific React + R3F + Zustand interaction failure mode; n=1; the diagnostic pattern (incremental fixes per discovered system, with visual-test driven discovery between fixes) is the methodology I'd want to defend, not the specific bug

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

During the Phase 6.1 multi-lane refactor I covered in Post 42, I introduced a bug that took three separate fixes to fully resolve. The symptom was simple: after pressing a dev keybinding that cycled the focused lane mid-walk, the bowler character would reappear visible at an off-lane spawn position instead of resuming wherever in their walk animation they had been. The bug was caught by the operator-side visual-test cycle (Post 43 covers why the per-phase visual-test discipline contains bugs like this) inside the Phase 4.A commit that introduced it.

The interesting thing about the bug isn't the symptom. It's that the symptom traced to a subtle interaction between three independently-correct subsystems: React's JSX prop diffing semantics, the physics engine's RigidBody position re-application on prop reference change, and Zustand's default subscribe semantics (no fireImmediately option set). Each of the three subsystems was behaving exactly as documented. The combination produced the bug. Each of the three fixes solved one part of the interaction. None of the three fixes alone fully resolved the symptom; only all three together stopped the bowler from teleporting to off-lane spawn.

This post documents what each of the three subsystems was doing, why their interaction produced the symptom, and the three-fix path I walked to resolve it. The audience is React Three Fiber developers and state-management practitioners who hit subtle three-system-interaction bugs and want a worked example of how the diagnosis went.

## Context: what changed in Phase 4.A

Quick context for the React Three Fiber stack involved: I'm building a bowling-alley tycoon sim using React Three Fiber (the React renderer for Three.js) plus Rapier (a physics engine compiled to WebAssembly; I use it through `react-three-rapier`, the React wrapper) plus Zustand (a state management library; the project's state store).

Before Phase 4.A, the `<Physics>` provider from react-three-rapier lived inside each per-lane scene component. The single-lane setup meant: one scene, one physics world, one set of physics bodies. Phase 4.A moved the `<Physics>` provider up the React tree to a multi-lane scene wrapper, creating a single shared physics world that would eventually host bodies from multiple lanes simultaneously.

The architectural intent was correct: single shared physics world. The latent bug was created by what the relocation did to component persistence patterns. Before the move, when the focused lane changed, the whole per-lane scene (including Physics, all RigidBodies, and all kinematic visual meshes like the bowler) unmounted and re-mounted with the new lane's geometry. After the move, the Physics provider stayed mounted across focus changes (because it lives in the parent); per-lane component instances persisted; only the props they received changed. The persistence pattern is what set up the three-system interaction.

## The three-system interaction

The bowler is a kinematic visual mesh, not a RigidBody. It moves via a useFrame hook that lerps the mesh position toward a target position derived from its current animation state (walking up to the throw line, standing at the line, walking back to exit, or absent). The mesh's `visible` and `position` props are set in JSX:

```jsx
<mesh
  ref={meshRef}
  position={spawnPosition}
  visible={false}
/>
```

The bowler subscribes to its lane's `bowlerPhase` field via Zustand `subscribe()`. When `bowlerPhase` changes, the subscribe handler updates the mesh's visibility, position, and animation target via direct ref-mutation. The standard imperative-side-effect pattern for React Three Fiber.

The bug: when the focused lane changed mid-walk, the bowler's mesh started visible at the new lane's spawn position instead of resuming where it had been mid-walk. Three systems combined to produce this.

### System 1: React/R3F JSX prop diffing

React Three Fiber's reconciler diffs JSX props between renders by reference equality (the same primitive comparison React uses). When a prop's value is reference-equal to its previous render's value, R3F skips re-applying it to the Three.js object the JSX represents.

The `visible={false}` prop in the bowler's JSX has the value `false`, a primitive. Across renders, `false` is always reference-equal to `false`. So R3F skips re-applying it on every render after the first. This is correct optimization behavior; React Three Fiber doesn't burn cycles re-setting `mesh.visible = false` when nothing has changed.

The consequence under component persistence: if some imperative code (like the bowler's subscribe handler) had earlier set `mesh.visible = true` directly via ref-mutation, subsequent React renders don't reset it to `false`. The prop value didn't change reference-equality, so R3F doesn't touch the mesh. The bowler stays visible.

### System 2: useMemo'd position props

The bowler's position prop uses a useMemo'd value:

```jsx
const spawnPosition = useMemo(
  () => offsetPosition(SPAWN_BASE, laneId),
  [laneId]
);
```

When `laneId` is in the dependency array and `laneId` changes (because the focused lane cycled), useMemo recomputes. The recomputed value is a new array reference, even if the array's contents happen to match. R3F's prop diff catches the reference change. R3F DOES re-apply the new position to the mesh.

The consequence: position gets re-applied on focus change, teleporting the mesh from wherever it was (mid-walk somewhere on the lane) to the new lane's spawn coordinates.

### System 3: Zustand subscribe default semantics

The bowler subscribes to its lane's `bowlerPhase` via Zustand's `subscribe()` method. Default semantics: the listener fires only when the subscribed value changes. The listener does not fire on subscribe.

When the focused lane changes, the bowler component re-renders with the new lane context. The subscribe call re-runs (with the new lane's selector). But the listener doesn't fire on re-subscribe by default; it waits for the next change to the new lane's `bowlerPhase` value. If the new lane's `bowlerPhase` happens to already be the value it would have been set to anyway, no listener call happens.

The consequence: the subscribe handler that would have correctly updated mesh visibility and position based on current `bowlerPhase` doesn't fire on focus change. Mesh state stays at whatever the previous imperative writes left it at, mutated only by R3F's prop reapplication (System 2).

### The combination produces the bug

Walk through what happens when focused lane changes mid-walk:

1. Bowler is mid-walk on Lane A. Subscribe handler had earlier set `mesh.visible = true`, `mesh.position` to some intermediate point along the walk path.
2. Focused lane changes to Lane B (dev keybinding press).
3. Bowler re-renders with new lane context. New `useMemo` recomputes spawn position for Lane B.
4. R3F prop diff catches that `position` prop reference changed; re-applies to mesh. Mesh.position teleports to Lane B's spawn coordinates.
5. R3F prop diff sees that `visible` prop value is still `false` (reference-equal); skips re-applying. Mesh.visible stays `true`.
6. Subscribe handler doesn't fire (Lane B's `bowlerPhase` hasn't changed since the subscribe started).
7. Result: mesh visible at Lane B's spawn position, no animation logic running, no subscribe-handler reset.

Each system is doing what it's supposed to do. The combination doesn't recover the correct mesh state.

## The three-fix path

I walked the diagnosis incrementally, applying one fix per discovered system. Each fix solved one part; only the third fix actually eliminated the bug class.

**Fix 1: Pass `fireImmediately: true` to the Zustand subscribe call.** With `fireImmediately`, the listener fires on subscribe with the current value, not waiting for a change. On focus change, the subscribe handler runs with the new lane's `bowlerPhase` value, correctly resetting mesh visibility and position based on current animation state. This fixed cases where the new lane's bowler was in the same phase as the prior lane's bowler had been; the listener fired, the handler ran, mesh state recovered.

But it didn't fix cases where the new lane's `bowlerPhase` was in a state the handler had no explicit reset logic for (specifically the between-throws-stand-at-line state). The handler was a no-op for that phase; the mesh stayed wherever the previous imperative writes had left it.

**Fix 2: Add explicit visibility and position resets to the handler's between-throws-stand-at-line case.** The handler now explicitly sets `mesh.visible = true` and `mesh.position` to the throw-line coordinates when the bowler enters the stand-at-line phase, even though semantically nothing about the bowler's position should have changed in that phase. The redundant write is a defensive reset against the prior imperative state.

This fixed the between-throws case. But it didn't fix the underlying class of bugs that came from component persistence across focus change. Any future bowler-state changes that didn't include explicit imperative resets would still have the same teleport-to-off-lane symptom under the right conditions.

**Fix 3: Force clean React remount via a `key={focusedLaneId}` prop on the multi-lane scene wrapper.** When the focused lane changes, the React key changes, which causes React to unmount the entire subtree and re-mount fresh. Fresh mount means: no persisted refs, no persisted imperative mutations, no prop-reapplication-without-handler-reset surprises. The mesh starts at its JSX-initial state, the subscribe runs from scratch with `fireImmediately` so the handler fires with current `bowlerPhase`, and mesh state is correct because it just started fresh.

Fix 3 alone would have eliminated the bug class. But I applied Fixes 1 and 2 in the order I discovered each system; in hindsight, the diagnostic path I walked (caught each system one at a time via visual-test cycle) was the value, even though Fix 3 was the cleanest single intervention.

## The general principle

Prop diffing semantics and state subscription semantics are subtle. The subsystems involved (React's reconciliation reference-equality optimization, React Three Fiber's prop diff cascade, Zustand's default-listener-fires-only-on-change behavior) are individually documented and individually correct. Their combinations produce bugs that don't surface in any single subsystem's test surface.

Visual-test driven discovery is the diagnostic pattern that surfaces these interactions. Unit tests on the bowler component, integration tests on the state store, and even end-to-end tests on the single-lane focused flow would not have caught this bug; the bug required a specific keystroke sequence (focus-cycle mid-walk) that targeted the component-persistence-across-prop-change scenario. Visual-test cycles between commits (Post 43 covers the discipline) catch these patterns where automated tests don't, because operator attention exercises the keystroke sequences that interaction bugs require.

Assume nothing about how subsystem combinations behave under conditions none of the subsystems individually were designed for. Verify mesh state imperatively (in the subscribe handler, not via JSX prop reliance) under all expected state transitions. Use React keys to force clean remounts when component persistence introduces more failure surface than it saves; the cost of remounting is usually less than the cost of debugging prop-vs-imperative-state divergence.

## What I'm not claiming

- I'm not claiming this bug pattern affects every React + R3F + Zustand application. It requires the specific component-persistence-across-prop-change scenario I had: a kinematic mesh whose position is JSX-prop-driven, plus imperative mesh mutation via subscribe handler, plus prop dependency on a value that changes when component context changes. Applications that don't combine these conditions don't hit this interaction.
- I'm not claiming `key={focusedLaneId}` is always the right escape hatch. It eliminates a bug class but loses physics state across focus changes (any in-progress physics simulation gets reset). I accepted that trade-off because at the multi-lane scale the bug class was more expensive than the lost physics state; other applications might not have the same trade-off math.
- I'm not claiming I would have caught this without operator-side visual testing. Unit tests, integration tests, and automated end-to-end tests didn't surface this kind of three-system interaction. The visual-test cycle between commits is what surfaced the symptom; the diagnostic walk through the three systems is what produced the fix.
- I'm not claiming the fix-order I applied was optimal. In hindsight, Fix 3 alone would have eliminated the bug class. I applied Fixes 1 and 2 first because I discovered each system incrementally; the diagnostic path was the value, even though the final intervention superseded the earlier ones.

## What I am claiming

Three-system-interaction bugs in React + R3F + Zustand applications are real, subtle, and not surfaced by individual-subsystem testing. The visible symptom (a mesh in the wrong place) traces to interactions between independently-correct subsystems. Diagnostic pattern that worked here: incremental fixes per discovered system, with visual-test driven discovery between fixes, each fix committing independently as part of the phase-decomposition discipline (Post 43).

The general principle: assume nothing about how subsystem combinations behave under conditions none of the subsystems individually were designed for. Specifically, watch for the combination of imperative mesh mutation (via subscribe handler or useFrame), JSX prop diffing (which preserves some props and reapplies others based on reference equality), and state subscription semantics (which may or may not fire on subscribe). The combination is where the bugs live.

The standing empirical claim is one bug, three systems, three fixes. The diagnostic pattern (incremental per-discovered-system fixes, visual-test-driven discovery between fixes) is the methodology I'd want to defend across future interaction-class bugs; the specific bug is the empirical anchor for the methodology. Whether other React + R3F + Zustand applications produce the same interaction class under similar focus-cycle-mid-state-change conditions is the standing extension; I'd expect the pattern to recur but I haven't tested it outside this one fire.
