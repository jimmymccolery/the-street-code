<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0055
title: Multi-entity Rapier physics in a single shared world: per-lane collision groups
date_published: 2026-05-31
status: published
superseded_by: none
domain: technical engineering Rapier collisionGroups 32-bit bit-encoding for shared world multi-entity isolation
project_scopes: pin-paradise
cc_task_relevance: rapier-physics-architecture, multi-arena-isolation, r3f-rapier-integration
phase_binding: era-independent
discipline_family: none-applicable
canonical_rule: Use single shared Rapier World with per-body collisionGroups 32-bit membership+filter encoding rather than multiple Physics providers
load_bearing_claims:
  - Multiple World instances work in principle but react-three-rapier assumes single Physics provider
  - Multiple providers create bridge-reconciliation cost per tick
  - Collision groups filter at broadphase layer and are fast
  - Bit-encoding format is thinly documented; this post fills the gap
applicability_triggers:
  - When multiple independent physics simulations coexist in same R3F scene
  - When designing multi-arena or multi-play-area game with Rapier
  - When per-entity isolation is required without multiple physics worlds
mechanism_details:
  - 32-bit integer per body encodes membership mask and interaction filter mask
  - Bodies with non-overlapping masks never produce collision events
cross_refs:
  - Post 0054 (statistical bowling without physics)
-->

# Multi-entity Rapier physics in a single shared world: per-lane collision groups

**Author:** Jimmy McColery
**Date:** 2026-05-31
**Status:** Technical engineering post on the Rapier `collisionGroups` 32-bit encoding for cross-entity isolation in a shared physics world; production code from a multi-lane bowling-sim React Three Fiber scene

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

If you're using Rapier physics in a React Three Fiber project and you have multiple independent simulations running in the same scene (multiple arenas, multiple play areas, multiple sandbox zones), you eventually hit the question of how to keep their physics bodies from interacting. The naive approach is to spin up multiple Rapier `World` instances, one per simulation. That works in principle but R3F's `react-three-rapier` integration assumes a single `<Physics>` provider wrapping the scene, and running multiple Physics providers means running multiple React-Rapier bridges with their own per-tick reconciliation cost. The integration friction is real.

A cleaner approach uses Rapier's built-in collision-groups filtering inside a single shared world. Each body declares which collision groups it belongs to and which collision groups it can interact with; bodies whose membership and filter masks do not overlap will never produce a collision event. The mechanism is fast (Rapier filters at the broadphase layer) and the implementation is a single 32-bit integer per body. The documentation around the bit-encoding format is thin, which is the gap this post fills.

This post documents the bit-encoding I'm using in production for a multi-lane bowling sim where two bowling lanes run full Rapier physics simultaneously in a single shared world. The same pattern applies to any multi-arena, multi-zone, or multi-player-team simulation that needs per-zone isolation.

## The problem

The sim runs two physics lanes (lane IDs 17-A and 35-A) plus two statistical lanes (no physics) plus 32 stub lanes (no per-lane simulation) in a single R3F scene with a single `<Physics>` provider wrapping the whole alley geometry. The two physics lanes are spatially separated in the world (lane 35-A is offset 40 meters from lane 17-A on the X axis), but the Rapier physics world does not care about spatial separation; it cares about object intersection.

Without any collision filtering, a ball thrown on lane 17-A would not crash into pins on lane 35-A directly because the pins are 40 meters away on a different lane. But the ball that goes into the pit on lane 17-A continues to bounce around in the pit area for several seconds, and the ball-return mechanism eventually moves the ball back to the rack. During that travel, the ball is at various heights and positions; the spatial-separation assumption is fragile under high-velocity throws and edge-case trajectories. The robust approach is to isolate the lanes at the physics layer so that no possible trajectory of any body on lane 17-A can ever produce a collision event with any body on lane 35-A.

Rapier provides the mechanism for this isolation: collision groups.

## The Rapier collision-groups encoding

Rapier's `collisionGroups` field on a RigidBody (or a Collider) is a single 32-bit unsigned integer. The integer is split into two halves:

- The **upper 16 bits** encode the body's **membership groups**: a bitmask indicating which groups this body belongs to.
- The **lower 16 bits** encode the body's **filter groups**: a bitmask indicating which groups this body will interact with.

Two bodies produce a collision event if and only if the membership of each body intersects the filter of the other body. Specifically: bodies A and B produce a collision event if `(A.membership & B.filter) != 0 AND (B.membership & A.filter) != 0`.

The bidirectional check matters because it lets you build asymmetric interaction rules. A body can be a member of group X and want to filter only group X, while another body is a member of group X and wants to filter every group. The asymmetric setup produces interactions for the second body but not the first.

For most multi-zone simulations, the asymmetric capability is unnecessary; the simple per-zone isolation case wants `membership == filter` so that bodies on the same zone interact normally and bodies on different zones do not interact at all. This is the case my bowling sim uses.

## Per-lane group assignment

The implementation assigns one bit per physics lane. Lane 17-A gets bit 0 (membership and filter both have bit 0 set; integer value `(1 << 16) | 1 = 0x00010001`). Lane 35-A gets bit 1 (integer value `(1 << 17) | 2 = 0x00020002`). When future physics lanes are added, they get bit 2, bit 3, et cetera, up to 16 lanes maximum (the upper 16 bits of the 32-bit integer become the constraint).

The function that computes the integer per lane:

```ts
const V1_PHYSICS_LANE_IDS = ["17-A", "35-A"] as const;

export function laneCollisionGroups(laneId: string): number {
  const idx = V1_PHYSICS_LANE_IDS.indexOf(laneId);
  if (idx === -1) return 0xffffffff;
  const groupBit = 1 << idx;
  return (groupBit << 16) | groupBit;
}
```

The fallback `0xffffffff` for non-physics lanes means "all membership groups, all filter groups," which is the all-interact mask. This fallback is a safety net rather than an active path; statistical and stub lanes do not mount RigidBodies at all, so they never call the function in production. The mask is the documented safe default per the Rapier convention.

The per-lane integer feeds into the RigidBody's `collisionGroups` prop. Every body that belongs to a lane (the Ball, the ten Pins, the Floor mesh, the PitSensor, the future Ball-return mechanism) reads the lane's collision-groups integer from a single source of truth and applies the same integer to its body. Bodies on lane 17-A all get `0x00010001`; bodies on lane 35-A all get `0x00020002`. Cross-lane collisions are filtered at the Rapier broadphase; the application layer never sees a cross-lane collision event.

## React Three Fiber integration

The `react-three-rapier` library provides two paths for passing the collision-groups integer to a RigidBody. The first path is the `interactionGroups` helper, which takes a membership-bitmask and a filter-bitmask separately and produces the encoded 32-bit integer:

```ts
import { interactionGroups } from "@react-three/rapier";

const groups = interactionGroups(
  [0], // membership groups (zero-indexed array of group numbers)
  [0], // filter groups (zero-indexed array of group numbers)
);
```

The helper expects array indices, not bit positions. The encoded result for `interactionGroups([0], [0])` is `0x00010001`, which matches the raw bit math for lane 17-A.

The second path is raw bit math passed directly to the `collisionGroups` prop:

```tsx
<RigidBody collisionGroups={laneCollisionGroups("17-A")}>
  {/* ... */}
</RigidBody>
```

Both paths produce the same 32-bit integer. The choice between them is style: the helper is more readable for developers who haven't seen the bit encoding before; the raw math is more direct for codebases where the per-zone computation is centralized in a function like `laneCollisionGroups` above.

For my codebase, the raw math is the production path because the per-lane integer needs to be computed in code that runs outside React component context (the lane state factories, the physics-body initialization, the test scaffolding for atomicity invariants). The helper works fine in React render context, but the centralized function pattern means one place to update if the bit-encoding logic ever needs to evolve.

## Application to per-body types

Every physics body that belongs to a lane needs the lane's collision-groups integer applied. In the bowling-sim case, that is five RigidBody types per lane:

- **Ball**: the thrown bowling ball. Spawns at the bowler's release point, travels down the lane, hits pins, ends in the pit. Belongs to its lane's group.
- **Pin** (ten per lane): the ten bowling pins in the rack. Belongs to its lane's group; collides with the lane's Ball; never collides with the next lane's Ball or Pins.
- **Floor**: the lane surface that the ball rolls along. Belongs to its lane's group; the Ball collides with the Floor for friction and gravity response; the next lane's Ball never sees this lane's Floor.
- **PitSensor**: the trigger volume at the end of the lane that detects ball arrival for scoring. Belongs to its lane's group; only this lane's Ball can trigger this lane's sensor.
- **Ball-return mechanism** (future): the path that returns the ball to the rack after the throw. Belongs to its lane's group; isolated from cross-lane interactions.

The centralized `laneCollisionGroups(laneId)` function lets each body's component read its lane's integer from one place. The component's responsibility is to pass the integer to its RigidBody; the per-lane integer is a single source of truth.

## The atomicity guarantee

One thing the collision-groups mechanism explicitly does not handle: enforcing that all bodies on the same lane share the same group integer. If lane 17-A's Ball has `0x00010001` and lane 17-A's Pin has `0x00020002` (i.e., the Pin's per-lane assignment is wrong), the Ball and Pin will not collide and the lane's bowling simulation breaks silently. The bug is invisible at the type-system layer (both integers are valid `collisionGroups` values) and invisible at the visual layer (the Ball just rolls past the Pins without knocking them down).

The discipline that catches this kind of bug is test coverage of the collision-groups encoding. The test suite I run includes assertions that every body initialized on a given lane reads its integer from `laneCollisionGroups(laneId)` rather than from a hard-coded value or a stale copy. The test catches refactors that accidentally break the centralization (a developer copy-pastes a body initialization and forgets to update the lane ID; the bit-encoding diverges from the lane assignment). The encoding correctness is testable at the unit-test layer; you do not need a physics integration test to catch the divergence.

## Generalization beyond bowling

The pattern generalizes to any multi-zone or multi-arena physics simulation:

- **Multi-arena fighting games**: each arena gets one group bit; players in arena A do not produce collision events with players in arena B. The shared physics world handles all arenas' physics with one Rapier instance.

- **Multi-player tag teams**: each team gets one group bit; teammates do not collide with each other but do collide with opposing teams. Adapting requires asymmetric membership-versus-filter (teammates have shared membership but only opposing groups in the filter mask), which is well-supported by the 16-bit encoding.

- **Sandbox zones in a builder game**: each player's sandbox zone gets one group bit; players' bodies do not interact across zones. The shared world handles all zones' physics at once.

- **Vehicle classes in a racing game**: cars belong to one group, motorcycles to another, pedestrians to a third; the asymmetric filtering encodes which classes interact with which.

The 16-bit ceiling on group count is the binding constraint. You can have up to 16 distinct groups in a single shared world before you need to either reduce groups or run multiple Physics providers. For most multi-zone simulations, 16 groups is plenty; the bowling-sim case uses 2 groups for 2 physics lanes at V1 and could scale to 16 physics lanes before hitting the ceiling.

If you need more than 16 groups, the next-step architectural decision is whether to run multiple Physics providers (one per group cluster) or to introduce a software-layer collision-filter pass on top of Rapier's broadphase. The multiple-Physics-providers path is the cleaner architectural choice but the per-tick reconciliation cost is real. The software-filter path keeps the single Physics provider but moves the filtering work from Rapier's broadphase to application code, which is slower per check but flexible per filter rule.

## What I'm not claiming

- I'm not claiming the 32-bit encoding is the only way to do collision filtering in Rapier. Rapier also supports custom filter callbacks (per-collision JavaScript functions that decide whether two bodies should interact). The callback approach is more flexible but slower per check; the bit-mask approach is faster but more constrained. For most multi-zone simulations, the bit-mask is the right trade-off.

- I'm not claiming the bowling-sim two-lane setup stresses the mechanism. Two groups in 32 bits is a small example of what the encoding supports. A more taxing setup would use 8-12 groups with asymmetric filter masks; the bowling case is a clean demonstrator but does not test the upper limits of the encoding's flexibility.

- I'm not claiming Rapier's documentation on `collisionGroups` is uniformly thin. The mechanism is documented in the Rust API reference and in some of the lower-level Rapier examples. The thin documentation is on the JavaScript/TypeScript bindings via `react-three-rapier`, where the bit-encoding format is referenced but not laid out as concretely as this post does. The library's `interactionGroups` helper assumes you have already mapped group numbers to bit positions; this post fills in the bit-position step.

- I'm not claiming the centralized `laneCollisionGroups` function is novel. The pattern (single source of truth for per-zone configuration values) is standard. What's specific to this post is the application of the pattern to Rapier collision-groups encoding in a multi-lane bowling-sim context, with the specific bit-encoding documented at the level of detail Rapier's TypeScript docs don't always reach.

- I'm not claiming bit-mask collision filtering replaces all forms of physics-layer isolation. For some setups (very large entity counts; dynamic group assignment at runtime; per-entity custom filter rules), runtime callback filters or multiple Physics providers are the better fit. The bit-mask approach is the cheap default for stable group assignments; the alternatives exist for cases where the bit-mask constraints bite.

## What I am claiming

For multi-zone or multi-arena physics simulations in React Three Fiber + `react-three-rapier`, a single shared `<Physics>` provider with per-zone collision-groups bit-mask isolation is a viable architecture that avoids the per-tick reconciliation cost of running multiple Physics providers. The encoding is a single 32-bit integer per body, with the upper 16 bits encoding membership groups and the lower 16 bits encoding filter groups. Bodies whose membership and filter masks do not overlap never produce collision events.

The per-zone bit-mask computation is best centralized in a single function (`laneCollisionGroups(laneId)` in the bowling-sim case) so every body in a given zone reads its integer from one source of truth. The centralization is testable at the unit-test layer, which catches the silent failure mode where a body's integer drifts from its zone assignment and the physics simulation breaks invisibly.

The pattern scales to 16 zones before the 16-bit membership ceiling becomes the binding constraint. For most multi-zone simulations, 16 zones is plenty. For simulations that exceed 16 zones, the architectural choice between multiple Physics providers and software-layer collision filters depends on whether the per-tick reconciliation cost or the per-check filter cost is the dominant concern.

The empirical record this post stands on is a production multi-lane bowling-sim codebase running two physics lanes in a single shared Rapier world with the bit-mask isolation discipline applied across 930 vitest tests. Zero cross-lane collision artifacts caught by operator-side visual test since the discipline landed. The mechanism is one architectural decision that paid back the bit-math time it cost by making the multi-lane physics-world architecture viable without the multi-Physics-provider overhead.
