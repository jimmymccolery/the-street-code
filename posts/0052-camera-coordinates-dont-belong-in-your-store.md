<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0052
title: Camera coordinates don't belong in your store: discrete state vs continuous position in R3F
date_published: 2026-05-31
status: published
superseded_by: none
domain: R3F architecture discipline camera state placement vs Zustand store
project_scopes: pin-paradise
cc_task_relevance: r3f-camera-state-management, zustand-vs-refs-decision, discrete-vs-continuous-state-classification
phase_binding: era-independent
discipline_family: none-applicable
canonical_rule: Continuous camera position lives in refs not in store; discrete camera state (which vantage point is active) lives in store
load_bearing_claims:
  - React community default is store-based state which invites putting camera coordinates there too
  - Store re-render cost on every animation frame breaks R3F performance
  - Discrete state (active vantage) belongs in store; continuous position belongs in Three.js scene graph or refs
applicability_triggers:
  - When building R3F apps with Zustand or Redux
  - When deciding where camera state lives
  - When newcomer patterns are being questioned during architectural review
mechanism_details:
  - Store subscriptions triggering per-frame re-renders defeat R3F rendering model
  - Discrete slots vs continuous coordinates is the classification axis
cross_refs:
  - Post 0051 (atomic Zustand state machines)
-->

# Camera coordinates don't belong in your store: discrete state vs continuous position in R3F

**Author:** Jimmy McColery
**Date:** 2026-05-31
**Status:** Technical engineering post; architecture discipline from production R3F multi-lane scene

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

If you're building anything in React Three Fiber with a Zustand store (or Redux, or any external state-management library), you will eventually hit the question of where camera state lives. The camera position is part of the scene's interactive surface; the user can shift focus, pan between targets, zoom, transition between vantage points. State management is the React community's default answer to "interactive surface."

Your camera coordinates should not live in your store.

This is one of those patterns that newcomers to R3F regularly trip over because the React mental model says "interactive state goes in the store," and external state managers like Zustand have made store-based state so cheap to write that the natural reach is to put the camera position there too. The reach is wrong. This post is about why, and what the right shape looks like.

## The newcomer mistake

The straightforward implementation looks reasonable on first pass:

```ts
// In your Zustand store
interface CameraState {
  position: [number, number, number];
  lookAt: [number, number, number];
  setPosition: (p: [number, number, number]) => void;
  setLookAt: (l: [number, number, number]) => void;
}
```

```tsx
// In your R3F scene
function MyCamera() {
  const position = useStore((s) => s.position);
  const lookAt = useStore((s) => s.lookAt);
  return <PerspectiveCamera position={position} lookAt={lookAt} />;
}
```

The pattern compiles. The pattern even works for static camera positions. The pattern blows up the moment you try to animate the camera through any kind of transition.

## Why it blows up

Smooth camera transitions in R3F run inside `useFrame`, which fires on every render frame (60 times per second on a typical display, 90 or 120 times per second on high-refresh-rate displays). If the camera's position is sourced from the Zustand store, every frame of the transition has to do this:

1. Compute the new position for the current frame.
2. Call `setPosition` in the store with the new coordinates.
3. Zustand fires the subscriber notification.
4. Every component subscribed to `position` re-renders.
5. The new position propagates to the rendered camera.

Step 4 is where the failure mode lives. If you have other components that read `useStore((s) => s.position)` (for example, a HUD that shows the current camera coordinates, or a debug overlay, or a minimap that highlights the camera focus), every one of those components re-renders 60 to 120 times per second across the entire transition. The HUD that was supposed to be a static debug surface becomes the hottest re-rendering surface in your scene.

The deeper failure mode is that you've effectively re-implemented R3F's frame loop on top of React's render loop. R3F already provides a frame-driven update mechanism (`useFrame`) that doesn't require store updates or React re-renders. By routing camera updates through the store, you've added a layer of indirection that the framework already optimized away.

The result is technically functional but architecturally upside-down. Camera position is continuous (changes every frame during animations); React render cycles are discrete and expensive (one render per state change, with reconciliation and diffing overhead). Putting continuous state in a discrete-render system is the structural mistake.

## The discipline: discrete in store, continuous in useFrame

The clean separation is:

- **Discrete state in the store.** `focusedLaneId: string`. `cameraMode: "follow" | "free" | "cinematic"`. `targetEntityId: string | null`. Anything that changes infrequently and that other components legitimately need to subscribe to.

- **Continuous state in `useFrame`.** `camera.position`. `camera.lookAt`. Animation progress. Anything that changes every frame and that only the camera driver needs to read or mutate.

The two layers communicate one-way. The store says "focused lane is now 35-A"; the camera driver reads that change via `useEffect`, captures the source and target camera positions, then runs a spline animation in `useFrame` that imperatively mutates `camera.position`. No store updates happen during the spline. The camera driver mutates Three.js objects directly; React knows nothing about the frame-by-frame interpolation.

Here's the shape:

```tsx
function CameraSplineDriver() {
  const camera = useThree((s) => s.camera);
  const focusedLaneId = useStore((s) => s.focusedLaneId);

  // Spline state lives in a ref, not in React state.
  // Mutations to ref values do not trigger re-renders.
  const splineRef = useRef({
    stage: "idle" as "idle" | "pullBack" | "pan" | "pushIn",
    stageElapsed: 0,
    sourcePosition: new THREE.Vector3(),
    targetPosition: new THREE.Vector3(),
    sourceLookAt: new THREE.Vector3(),
    targetLookAt: new THREE.Vector3(),
    pullBackPosition: new THREE.Vector3(),
  });
  const previousFocusedRef = useRef(focusedLaneId);

  // Trigger spline on discrete focus change.
  useEffect(() => {
    if (focusedLaneId === previousFocusedRef.current) return;

    const sourceOffset = LANE_OFFSETS[previousFocusedRef.current];
    const targetOffset = LANE_OFFSETS[focusedLaneId];

    const spline = splineRef.current;
    spline.stage = "pullBack";
    spline.stageElapsed = 0;
    spline.sourcePosition.fromArray(sourceOffset);
    spline.targetPosition.fromArray(targetOffset);
    spline.pullBackPosition.set(
      spline.sourcePosition.x,
      spline.sourcePosition.y + PULL_BACK_Y,
      spline.sourcePosition.z,
    );
    spline.sourceLookAt.set(sourceOffset[0], 0, sourceOffset[2]);
    spline.targetLookAt.set(targetOffset[0], 0, targetOffset[2]);

    previousFocusedRef.current = focusedLaneId;
  }, [focusedLaneId]);

  // Frame-by-frame imperative drive.
  useFrame((_, delta) => {
    const spline = splineRef.current;
    if (spline.stage === "idle") return;

    spline.stageElapsed += delta;

    if (spline.stage === "pullBack") {
      const t = Math.min(spline.stageElapsed / PULL_BACK_DURATION, 1);
      const eased = 1 - (1 - t) * (1 - t); // ease-out quadratic
      camera.position.lerpVectors(
        spline.sourcePosition,
        spline.pullBackPosition,
        eased,
      );
      camera.lookAt(spline.sourceLookAt);
      if (t >= 1) {
        spline.stage = "pan";
        spline.stageElapsed = 0;
      }
      return;
    }

    // ... pan + pushIn stages omitted for brevity
  });

  return null; // No JSX; the driver mutates camera imperatively.
}
```

The pattern factors cleanly:

- The store carries `focusedLaneId: string`. Components subscribing to focus state get re-renders only when the focused lane actually changes. The HUD that shows "Focused Lane: 35-A" re-renders once per focus change, not once per frame.

- The spline state lives in a ref. Mutations to ref values don't trigger React re-renders, but the values persist across frames. The animation state machine (stage, elapsed time, source position, target position) lives outside the React state lifecycle.

- The frame driver reads the ref, mutates the camera, never touches the store. The camera animation is happening at the Three.js layer; React knows nothing about it.

- The trigger transitions from discrete to continuous via `useEffect`. When `focusedLaneId` changes (discrete event, React responds), the effect captures the new source and target into the ref (one-way handoff to the continuous layer). The `useFrame` callback then runs the spline.

## The three-stage spline as a portable pattern

The specific cinematic shape my scene uses is a three-stage spline: pull back from the source vantage, pan to the target vantage at the elevated camera height, push in to the target vantage. The durations are 0.4 seconds pull-back with an ease-out curve, 0.6 seconds pan at constant velocity, 0.5 seconds push-in with an ease-in curve. Total transition is 1.5 seconds.

The three-stage shape is a portable building block for any focus-shift camera animation. It looks more cinematic than a single straight-line interpolation because it mirrors how a human cinematographer would frame a shift: lift, traverse, drop. The lift and drop ease curves give the transition a sense of physical weight; the linear pan at altitude lets the eye track the spatial relationship between the source and target without jitter.

You don't need to use this specific shape. You do want some shape that's more elaborate than a linear interpolation, because linear-interp camera transitions in tycoon-scale scenes (where the camera moves across substantial spatial distances) read as jarring. The three-stage spline is the cheapest shape that doesn't read as jarring.

The implementation pattern (state machine in a ref, stage transitions in `useFrame`, imperative camera mutations) holds regardless of which spline shape you choose. Single-stage linear interp, four-stage with hold-at-midpoint, easing variations: all of them fit the same scaffolding.

## What about Drei's CameraControls?

The drei library's `<CameraControls>` component provides a higher-level abstraction over camera transitions. For a wide class of scenes, especially anything with orbit-controls-like interaction, drei's component is the right tool and you don't need to implement the spline driver from scratch.

The case where you'd hand-roll the driver instead of using drei is when your camera transitions are tightly coupled to non-camera state (focus changes, gameplay events, narrative beats) and you want full control over the transition timing and curve. The drei abstraction is great when you want "smooth camera that does the right thing"; the hand-rolled driver is what you reach for when you want "spline that takes exactly 1.5 seconds with this specific three-stage shape and these specific easing curves."

The discrete-in-store / continuous-in-useFrame discipline applies either way. Drei's component reads camera state from its own internal state, not from your Zustand store. If you put camera coordinates in your store and tried to pass them to drei's component, you'd be fighting two state systems that don't know about each other.

## When does camera state legitimately belong in the store?

The discipline isn't "no camera state in the store ever." It's "no continuous camera state in the store." Discrete camera state can and often should live in the store.

Examples of discrete camera state that belongs in the store:

- **Camera mode.** `"follow" | "free" | "cinematic" | "first-person"`. Mode changes are discrete events; components legitimately need to subscribe to "is the camera in cinematic mode."

- **Focused entity ID.** `focusedLaneId: string`. The discrete event that triggers the spline. HUD components subscribe to render "currently focused: lane 35-A."

- **Camera preset selection.** If your scene has named camera presets (overhead, side, behind-the-bowler), the active preset ID is discrete and store-managed.

- **Transition lock.** A boolean for "transition in progress" that other systems read to avoid firing competing camera commands.

Each of these changes infrequently (event-driven, not frame-driven). Each is read by multiple consumers. Each fits the store's strengths (selector-based subscribe, time-travel debug, save/restore).

The continuous coordinates (`camera.position.x`, `camera.position.y`, etc.) belong in the camera object itself. The frame-by-frame interpolation belongs in `useFrame`. The transition state machine belongs in a ref. Nothing about continuous frame-by-frame mutation belongs in the React state lifecycle.

## What I'm not claiming

- I'm not claiming this pattern is universally applicable. Some scenes have such simple camera needs that store-based camera positions don't cause measurable performance issues. For static camera scenes with no animated transitions, the discipline is overkill.

- I'm not claiming Zustand is uniquely bad at this. The same pattern applies to Redux, Recoil, Jotai, MobX, or any external state manager with selector-based subscribe semantics. The structural mistake is "continuous state in discrete-render system," not "Zustand specifically."

- I'm not claiming hand-rolled splines are universally better than drei's `<CameraControls>`. They're better when you need tight coupling to non-camera state and full control over transition shape; they're worse when you'd be re-implementing what drei already does well.

- I'm not claiming the three-stage spline shape is canonical. Other shapes (Bezier curves, dolly-zoom variations, head-tracked transitions) all fit the same implementation scaffolding. The three-stage shape is what I landed on for the specific scene; other scenes may want other shapes.

- I'm not claiming this finding is novel. The discrete-in-store / continuous-in-useFrame discipline shows up in R3F community discussions, in pmndrs documentation, and in production R3F codebases shipped by serious indie devs. What's specific to this post is the framing as a discipline with a name, the explicit anti-pattern of putting camera coordinates in the store, and the seven-stage decomposition of the spline driver shape.

## What I am claiming

Continuous camera state (position, lookAt, rotation) does not belong in your external state manager. The structural reason is that camera updates fire 60 to 120 times per second during animations, and routing every frame's update through the store's subscribe notification mechanism produces re-renders across every component subscribing to the camera state. The downstream consumers don't actually need the re-renders; they only need the discrete events (focus changes, mode changes, preset selections).

The clean separation is discrete state in the store, continuous state in `useFrame` with a ref-backed state machine. The store carries the event-driven layer; the `useFrame` carries the per-frame layer; the two communicate one-way via `useEffect` that captures discrete events into ref-mutable spline state.

The discipline pays for itself the moment your scene has more than one HUD component that reads camera-related state. Without the discipline, every animated transition forces all HUD components to re-render through the transition. With the discipline, transitions are invisible to the React render system; only the discrete event (start of transition, end of transition) appears at the store layer.

The empirical record this post stands on is a multi-lane R3F scene with six lanes, an interactive HUD, debug overlays, and cinematic camera transitions between lanes. Camera transitions run smoothly at 60 frames per second on integrated GPUs; the HUD re-renders only when discrete focus events fire; the store stays uncoupled from the frame loop. The discipline is one architectural decision that paid back the time it took to think through, several times over.
