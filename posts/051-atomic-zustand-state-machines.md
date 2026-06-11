# Atomic Zustand state machines: testing multi-entity updates with reference equality

**Author:** Jimmy McColery
**Date:** 2026-05-31
**Status:** Technical engineering post; 7-test pattern from production Zustand state-machine codebase

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I'm building a bowling-alley tycoon sim with multiple lanes rendering simultaneously. Two lanes run full physics with interactive bowlers; two lanes run statistical resolution as background simulation; two lanes are stubs reserved for future activation. All six lanes share a single Zustand store with a per-lane state shape that includes phase, bowler phase, throw number, frames, current frame index, scoring counters, and game-over flags.

The multi-lane shape creates a specific testing problem I want to put on the table: how do you verify that a per-lane state transition is atomic and isolated, given that the store holds all lanes in one shape and any per-lane update has to compose into a single `set()` call?

The pattern I landed on uses reference equality assertions for both atomicity and cross-entity isolation. Seven tests cover the full discipline. The pattern generalizes beyond bowling lanes to any multi-entity Zustand state machine.

## The atomicity discipline and why it matters

A lane state transition in this sim updates roughly ten fields at once: `phase` moves from `aiming` to `partialResetting`, `bowlerPhase` moves from `atThrowLine` to `walkingBack` or stays put depending on whether the frame completed, `throwNumber` increments or resets to 1, `frames[currentFrameIndex]` gets the new throw appended, `currentFrameIndex` advances if the frame completed, `gameOver` becomes true if the tenth frame closed, `finalScore` gets computed if the game ended, `lastThrowFallenCount` and `standingAtThrowStart` update to the new throw's data, and `frameCompleted` flips per the frame state.

If those updates landed across multiple `set()` calls, React would re-render between calls with the lane in an intermediate state. Mid-throw renders would show the bowler walking back while the lane was still mid-scoring, or `gameOver` flipped to true while `finalScore` was still null. The visible artifacts are real; I caught one of them during early development before the atomicity discipline landed. The fix was to centralize the transition computation in a pure reducer that returns a single composed `Partial<MultiAlleyState>` delta, then have the caller apply the delta via one `set(delta)` call.

```ts
// applyLaneThrowOutcome: pure reducer
function applyLaneThrowOutcome(
  state: MultiAlleyState,
  laneId: LaneID,
  fallenCount: number,
  standingBefore: number,
): Partial<MultiAlleyState> {
  // ... computes the new lane state ...
  return {
    lanes: {
      ...state.lanes,
      [laneId]: nextLaneState,
    },
  };
}

// Caller: single set() call
const delta = applyLaneThrowOutcome(state, "17-A", 7, 3);
set(delta);
```

The atomicity discipline is the contract. The test pattern verifies the contract holds.

## Testing the atomicity contract

The first test asserts that the delta contains all the transition fields composed into one object. Not separate properties on the delta root; not split across multiple deltas; all in `delta.lanes[laneId]` as a single composed lane object.

```ts
it("ATOMICITY: delta is a SINGLE composed object; caller applies in one set()", () => {
  const state = freshMultiState();
  const delta = applyLaneThrowOutcome(state, "17-A", 7, 3);
  const updatedLane = delta.lanes!["17-A"];
  expect(updatedLane.phase).toBe("partialResetting");
  expect(updatedLane.bowlerPhase).toBe("atThrowLine");
  expect(updatedLane.throwNumber).toBe(2);
  expect(updatedLane.standingAtThrowStart).toBe(3);
  expect(updatedLane.lastThrowFallenCount).toBe(7);
  expect(updatedLane.frameCompleted).toBe(false);
  expect(updatedLane.frames).toBeDefined();
  expect(updatedLane.currentFrameIndex).toBe(0);
  expect(updatedLane.gameOver).toBe(false);
  expect(updatedLane.finalScore).toBeNull();
});
```

Every transition field gets asserted. The test will catch any future refactor that splits the transition into multiple lane-state writes or any accidental field-drop where the delta doesn't contain a field the contract requires. The assertions are not load-bearing for the field values per se; they're load-bearing for "all transition fields appear together in one composed lane state."

This is the Type-Discrimination Gate pattern at the test layer. The reducer's return type is `Partial<MultiAlleyState>`, which is permissive: any subset of the state's keys is type-valid. The atomicity test narrows the permissive type to the specific shape the caller needs (a single `lanes[laneId]` write containing all transition fields). The test catches what the type system can't.

## Testing cross-entity isolation

The atomicity test alone isn't sufficient. A reducer could produce an atomic per-lane delta that also accidentally mutates other lanes' references. That would force every lane subscription to re-render on every per-lane transition, defeating Zustand's selector-based subscribe optimization.

The isolation test uses reference equality to verify other lanes' references stay stable across the update:

```ts
it("ISOLATION: updating lane 17-A does NOT mutate lane 35-A state", () => {
  const state = freshMultiState();
  const before35 = state.lanes["35-A"];
  const delta = applyLaneThrowOutcome(state, "17-A", 7, 3);
  // delta.lanes is a new Record with all original lanes + updated 17-A.
  // Other lane references should be preserved (not new objects).
  expect(delta.lanes!["35-A"]).toBe(before35);
  expect(delta.lanes!["17-J"]).toBe(state.lanes["17-J"]);
  expect(delta.lanes!["35-P"]).toBe(state.lanes["35-P"]);
});
```

The `toBe` assertion is reference equality (Vitest and Jest both use `Object.is` for `toBe`, which is reference equality for objects). If the reducer accidentally replaced `lanes["35-A"]` with a structurally-identical-but-distinct object, the test fails. The structural equivalent test (`toEqual`) would pass on the mistake; reference equality catches what structural equality misses.

A second isolation test extends the discipline to stub lanes (lanes that exist in the state shape but aren't actively running):

```ts
it("ISOLATION: stub lanes' references are preserved across updates", () => {
  const state = freshMultiState();
  const before27A = state.lanes["27-A"];
  const before35B = state.lanes["35-B"];
  const delta = applyLaneThrowOutcome(state, "17-A", 7, 3);
  expect(delta.lanes!["27-A"]).toBe(before27A);
  expect(delta.lanes!["35-B"]).toBe(before35B);
});
```

Why two isolation tests instead of one? Because the active-lane isolation test and the stub-lane isolation test catch different failure modes. A reducer might correctly preserve other active-lane references but accidentally re-create stub-lane references during the `{...state.lanes, [laneId]: nextLaneState}` spread. Or vice versa. Splitting the assertions across two tests makes the failure mode legible when a regression happens.

## Testing immutability for subscribe triggers

Zustand's subscription system uses reference comparison to decide whether subscribers re-render. The convention is: if the new state contains a new reference at a path a subscriber cares about, the subscriber re-renders. If the reference is the same, the subscriber skips.

This cuts both ways. The isolation tests above verify that other lanes' references stay stable so their subscribers skip. The immutability tests verify that the target lane's reference changes so its subscribers fire.

```ts
it("IMMUTABILITY: delta.lanes is a NEW Record reference (triggers Zustand subscribe)", () => {
  const state = freshMultiState();
  const delta = applyLaneThrowOutcome(state, "17-A", 7, 3);
  expect(delta.lanes).not.toBe(state.lanes);
});

it("IMMUTABILITY: delta.lanes['17-A'] is a NEW lane object (triggers per-lane subscribe)", () => {
  const state = freshMultiState();
  const before17A = state.lanes["17-A"];
  const delta = applyLaneThrowOutcome(state, "17-A", 7, 3);
  expect(delta.lanes!["17-A"]).not.toBe(before17A);
});
```

The `not.toBe` assertion catches the failure mode where the reducer would mutate the lane object in place. In-place mutation of a Zustand state object is a well-documented mistake; the subscriber re-render logic doesn't fire because the reference didn't change. Selectors that depend on the mutated path return stale data.

Two immutability tests instead of one for the same reason as the isolation tests: the lanes-Record reference and the per-lane-object reference are distinct surfaces. A reducer could correctly produce a new lanes Record while accidentally reusing the lane object (which a structural copy would catch but reference equality won't, because the structural copy would produce a new reference). Or correctly produce a new lane object while reusing the lanes Record (which the spread operator would normally prevent, but a manual mutation could break). Splitting the assertions makes the failure surface legible.

## The seven-test pattern

In total, the test scaffolding for the reducer contract uses seven tests:

1. **The base composition test.** Verifies the reducer produces a delta with the expected shape and field values for a happy-path input.
2. **ATOMICITY: single composed object.** Verifies all transition fields appear together in one composed lane state.
3. **ISOLATION: active lanes preserved.** Verifies other active lanes' references stay stable.
4. **ISOLATION: stub lanes preserved.** Verifies stub lanes' references stay stable.
5. **IMMUTABILITY: new Record reference.** Verifies `delta.lanes` is a new reference for the Zustand subscribe trigger.
6. **IMMUTABILITY: new lane object.** Verifies `delta.lanes[laneId]` is a new object for the per-lane subscribe trigger.
7. **Composition on a second lane.** Verifies the same contract holds when the target lane is different (catches lane-specific bugs in the reducer's handling of per-lane variations).

Plus an additional composition test for statistical lanes (different `pinsetter_type` field) that exercises the reducer's handling of the lane-type variation surface.

The pattern is repeatable. Any new reducer that produces a `Partial<MultiAlleyState>` follows the same seven-test outline: base composition, atomicity, isolation across siblings, immutability of the Record and the target entity, plus per-variation composition coverage.

## Why this generalizes beyond Zustand

The pattern is a multi-entity state-machine testing discipline, not a Zustand-specific one. Any state-management library that uses immutable updates plus reference-comparison subscriptions hits the same testing surface:

- **Redux** with selectors and `useSelector`. The same atomicity/isolation/immutability discipline applies. Reducers produce delta objects; subscribers re-render based on reference comparison; tests verify the contract.
- **React `useReducer`** with state-tree shape. Same pattern. The reducer returns the new state; downstream code compares references; tests verify atomicity and per-key isolation.
- **Jotai** with atom families. Different surface, but the per-atom isolation and atomic-update discipline still applies. Reference equality on sibling atoms verifies isolation.
- **Valtio** with proxy state. Partly different (proxy auto-tracks accesses) but the atomicity discipline still applies at the update site, and reference-equality tests on sibling-entity proxies verify isolation under the assumption that updates are atomic per entity.

The structural element is that any multi-entity state shape where entities have independent lifecycles needs the cross-entity isolation discipline. Subscribers that select on entity X should not re-render when entity Y updates. The test pattern verifies the discipline.

## The Type-Discrimination Gate framing

The reducer's return type `Partial<MultiAlleyState>` is intentionally permissive. The state shape has many top-level keys; the reducer only writes a subset; the type accommodates the subset. The trade-off is that the type system can't distinguish "this delta is a well-formed lane transition" from "this delta accidentally writes a random subset of fields."

The atomicity test discriminates the type. The Type-Discrimination Gate pattern I'm applying is: the type system says "any subset of MultiAlleyState," the runtime contract says "exactly one composed lane state update with all transition fields," and the test enforces the runtime contract. The test is the load-bearing discrimination mechanism.

This framing matters because the alternative is to tighten the reducer's return type to something like `LaneTransitionDelta = { lanes: { [K in LaneID]?: LaneState } }`. That tightening would help at the type layer but it doesn't compose well with the broader store pattern where some reducers write multiple top-level keys at once. Keeping the permissive `Partial<MultiAlleyState>` type and discriminating in tests is the discipline that scales as the store grows.

## What I'm not claiming

- I'm not claiming reference-equality testing is universal best practice. It catches specific failure modes (accidental object replacement, in-place mutation) that structural-equality testing misses. For codebases where those failure modes are rare, the additional test count may not be load-bearing.

- I'm not claiming the seven-test pattern is exhaustive. It covers the atomicity, isolation, and immutability surfaces. Other test surfaces (e.g., per-field correctness across the full input space, edge-case handling for split conversions or perfect games) are independent and need their own coverage.

- I'm not claiming this discipline is novel. Immutable update patterns plus reference-equality testing are well-established in the Redux ecosystem and have been since the Redux DevTools time-travel debugging shipped in 2015. What's specific to this post is the Type-Discrimination Gate framing applied to multi-entity state machines under Zustand, and the seven-test outline that operationalized the discipline for a six-lane production codebase.

- I'm not claiming the cost of seven tests per reducer is universally worth it. The cost-benefit tilts toward the tests when the multi-entity state shape has independent-lifecycle entities and when subscribers select on specific entities (so cross-entity isolation actually matters at render time). For state shapes without those properties, fewer tests may suffice.

- I'm not claiming this pattern catches all atomicity failures. It catches the failure modes the test outline targets (atomicity, isolation, immutability). Atomicity violations across multiple `set()` calls in async code paths, or atomicity violations that happen at the React render layer rather than the reducer layer, need different test patterns (React Testing Library integration tests, async-render race-condition tests).

## What I am claiming

For multi-entity Zustand state machines where per-entity transitions must be atomic and cross-entity isolation must be preserved, a seven-test outline with reference-equality assertions covers the contract surface. The tests catch atomicity violations (transition fields split across multiple writes), isolation violations (sibling entities accidentally mutated), and immutability violations (in-place mutations that break Zustand subscribe trigger semantics).

The pattern is portable to any immutable-update state-management library with reference-comparison subscriptions: Redux, useReducer, Jotai, Valtio with appropriate adjustments per library. The structural element is the multi-entity shape plus the reference-comparison subscriber semantics; libraries with those properties hit the same testing surface.

The Type-Discrimination Gate framing extends to any reducer whose return type is permissive (e.g., `Partial<State>`) but whose runtime contract is specific. The type system can't enforce the contract; the tests do. Pushing the discrimination to the test layer keeps the reducer types compositional at the store surface while still catching reducer-shape regressions.

The empirical record is a six-lane production codebase running through 930 vitest tests with the seven-test pattern applied to every multi-entity reducer. Zero atomicity bugs caught by operator-side visual test since the pattern landed. Several atomicity drift attempts caught by the test layer during development before reaching visual test. The discipline pays for its test-count cost in catches that would otherwise have produced visible state-tear artifacts in a multi-entity rendering pipeline.
