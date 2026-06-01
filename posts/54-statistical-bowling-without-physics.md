# Statistical bowling: how to simulate background lanes without physics

**Author:** Jimmy McColery
**Date:** 2026-05-31
**Status:** Technical engineering post on the physics-versus-statistical split for multi-entity scene rendering; production code from a six-lane bowling-sim React Three Fiber scene

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

A bowling alley has between 24 and 48 lanes in most commercial installations. The bowling tycoon sim I'm building solo as Early Access for October 31, 2026 starts at 36 lanes and scales up from there. Each lane runs an independent bowling game: a bowler walks to the line, throws a ball at ten pins, scores the throw, advances the frame, eventually completes a ten-frame game and starts the next bowler.

The problem this post is about: you cannot run 36 lanes worth of bowling physics simultaneously in a browser. A single bowling lane physics simulation with one ball plus ten pins plus collision response plus pin-toppling cascade is already substantial computational work. Multiply by 36 and the framerate collapses. The naive approach (just render all the lanes with full physics) does not ship.

The approach my sim uses splits the active lanes into two classes: a small number of physics lanes that run full Rapier physics simulation with interactive bowlers, and a larger number of statistical lanes that produce visually identical bowling output through a 1Hz RNG-driven state machine with no physics simulation at all. This post is about how the statistical-lane mechanism works, why it produces a visually indistinguishable result from physics-driven bowling, and how the pattern generalizes to any tycoon or simulation game where background entities need to feel alive without the cost of full physics.

## The split

At V1 the sim runs four active lanes: two physics lanes with full Rapier simulation (interactive bowlers, real ball trajectory, real pin-collision cascade, scoring computed from the actual fallen-pin count), and two statistical lanes with no physics (RNG generates the fallen-pin count, the scoring system advances against the RNG output, the visual rendering reflects the state). The remaining 32 lanes in the V1 alley are stubs (visible geometry but no per-lane simulation state; functionally inert for V1).

The split is per-lane configurable, not global. A lane is one of three classes (active-physics, active-statistical, stub) and the class is part of the lane's persisted state. Operators can promote a stub lane to active-statistical when bowlers show up, or promote an active-statistical lane to active-physics when the player wants to interact with it directly. The class is the data; the rendering system reads the class and decides what to render.

The two physics lanes are the focal lanes. The two statistical lanes are background. The framerate budget at V1 is sufficient for two physics lanes plus two statistical lanes plus the 32 stubs; the budget scales to more statistical lanes before it scales to more physics lanes because the per-statistical-lane cost is roughly one render of the pin meshes plus a 1-Hz state-machine tick.

## What statistical lanes don't do

Statistical lanes have no Rapier RigidBody instances. The ball is not rendered as a physics object; it is not rendered at all on statistical lanes. There is no ball trajectory simulation, no pin-collision response, no friction calculation, no impulse propagation, no continuous collision detection. The Rapier physics world contains zero physics bodies sourced from statistical lanes.

There is no per-frame physics tick for statistical lanes. The `useFrame` callback in React Three Fiber does not advance any per-lane state for statistical lanes; the only useFrame work that touches statistical lanes is the camera spline driver (which mutates camera position and lookAt across all visible geometry uniformly).

There is no bowler walk animation on statistical lanes. The bowler character mesh is not instantiated on statistical lanes; there is no walk-back, no throw motion, no aim cycle. The statistical lane geometry is pin meshes plus floor plus lane backdrop, full stop.

There is no scoring physics dependency. The score for a frame is computed from the same scoring code that physics lanes use, but the inputs to that scoring code (how many pins fell on this throw, how many pins were standing before this throw) come from the RNG state machine instead of from a physics outcome readback.

## What statistical lanes do do

The state machine that drives statistical lanes runs on a 1-Hz tick. Once per second, a `setInterval` callback iterates over every active-statistical lane and advances its state. The mechanism is intentionally low-frequency: human perception of "someone is bowling on that lane" does not require continuous animation; the eye accepts the per-second pin-state update as evidence that bowling is happening.

The state machine has the same phase shape as physics lanes (idle, partialResetting, resetting, freshRackBetweenThrows, rolling, scoring) but only a subset of phases are reachable on statistical lanes. The reachable phases are idle (waiting to throw), partialResetting (between throws within a frame), resetting (between frames), and freshRackBetweenThrows (immediately after a strike). The rolling and scoring phases are physics-only; statistical lanes skip them.

Per tick, for each active-statistical lane that is not currently focused and not in gameOver state:

- If the lane is in `resetting`: advance the frame number, clear the reset buffer, transition to idle.
- If the lane is in `partialResetting` or `freshRackBetweenThrows`: transition to idle.
- If the lane is in `idle`: generate the number of newly-fallen pins via a weighted RNG, apply the throw outcome (which advances the throw counter, updates the standing-pin count, computes the partial-frame score, and decides whether the frame ended), and transition to the appropriate post-throw phase.
- If the lane is somehow in `rolling` or `scoring` (which should only happen if the operator briefly focused the lane and then switched away mid-physics), recover by forcing back to idle and treating the in-flight throw as a 0-pin throw.

The RNG is weighted to produce bowling-realistic outcomes. The current V1 RNG is a 50/50 split between "strike" (all standing pins fall) and "partial" (uniformly sampled fallen count from 0 to the standing count). This is calibration-stub territory; Phase 8.x will replace it with skill-profile-driven distributions that produce per-bowler realistic outcome shapes. The mechanism is independent of the calibration; you can swap the RNG without touching the state machine.

The visual rendering reads the lane's pin-state field. Each pin in the ten-pin rack has a boolean (standing or fallen). When the throw outcome is applied, the pins that fell become falses; when the rack is reset between frames, all pins become trues again. The pin mesh's visibility (or position, depending on the asset) reflects the boolean. The visual update is reactive to the state change, which means the pins flip between standing and fallen at the moment the state machine ticks.

## Why this looks like bowling

A human observer watching a statistical lane sees: pins standing, then a beat, then pins fallen, then a longer beat, then pins standing again, then another beat, then pins partially fallen. The pattern repeats at one update per second. The observer's pattern-matching layer reads this as "someone is bowling on that lane" because the cadence and the pin-state changes match what bowling looks like when you cannot see the bowler.

The cadence matters more than the missing details. A bowling alley environment has visual noise (other people moving, lane oil reflections, scoring monitors, bar activity in the foreground). The eye does not lock on any one background lane for long. The per-second cadence of state changes is sufficient to populate the observer's "things are happening" signal without requiring the observer to inspect any specific lane.

The absence of a bowler character on statistical lanes is also less visible than you might expect. In a 3D rendering with depth, the bowler at any background lane is small enough to be optionally visible; the eye fills in the missing bowler from the pin-state changes plus the contextual environment. Players occasionally notice the missing bowlers when they look directly at a background lane; the noticing rate is much lower than the rate at which they accept the lane as active.

The statistical-lane technique works because human perception is more pattern-recognition than pixel-inspection. The pattern matters; the pixel detail does not, at background-lane scale.

## The recovery edge case

One edge case earned its own engineering attention: lanes that are statistical at most times but briefly physics when the operator focuses on them.

The user-facing affordance is that the player can press Shift-L to cycle focus through lanes. When the player focuses on a previously-statistical lane, the lane temporarily promotes to active-physics for the duration of focus (so the player can interact with the bowler, watch real throws, hear real pin-collision sound). When the player switches focus away, the lane reverts to active-statistical.

The reversion creates a state-machine risk. The lane could be mid-physics-throw at the moment focus changes. The physics state machine is in `rolling` or `scoring`. When the lane reverts to statistical, the next 1-Hz statistical tick sees the lane in a physics-only phase and does not know how to advance it. Without a recovery path, the lane gets stuck.

The recovery path: if a statistical lane is in `rolling` or `scoring` at tick time, force the lane back to idle. The in-flight throw is treated as a 0-pin throw (no pins fall). The lane scores the 0-pin throw against the frame and advances normally. The lost throw is a documented V1 trade-off: physics state is not preserved across focus changes for V1 scope; full physics-state persistence is a later-phase scope.

This trade-off is one of the V1-bug-acceptance decisions worth documenting (covered separately in another post in this series). The recovery path lives in the state machine because the alternative (full physics-state preservation) is substantially more engineering work for substantially less player-visible benefit at V1 scale.

## Why this pattern generalizes

The statistical-lane mechanism is not bowling-specific. The pattern applies to any simulation or tycoon game where background entities need to feel alive without expensive simulation.

The general shape:

- The simulation has many entities that operate independently in parallel.
- Each entity has a state machine with a few discrete phases.
- The state machine produces visible state changes at human-perceptible cadence (typically once per second to once per few seconds).
- Foreground entities (where the player is actively interacting) run the full simulation.
- Background entities run a reduced simulation that produces the same visible state-machine transitions but skips the expensive per-tick work.

Examples of the pattern outside bowling:

- A city builder where most buildings produce output via a slow timer rather than per-frame production simulation. The visible smoke from chimneys flickers at human-perceptible cadence; the output ticks per second; the visual matches without the full production model.
- A restaurant tycoon where most patrons eat via a state machine (ordering, eating, paying) that ticks once every few seconds. Foreground patrons might get more detailed AI; background patrons fill the room with state-machine output.
- A multi-elevator office building where the elevators move via discrete state transitions at the per-floor level rather than continuous physics. Foreground elevators (the ones the player is watching) animate smoothly; background elevators teleport between floors at perceptible cadence.

The pattern is "discrete state-machine output at perceptible cadence" instead of "continuous physics or animation." The foreground exception preserves the full-fidelity experience where the player is looking; the background reduction recovers the framerate budget the foreground costs.

The 1-Hz cadence is the parameter to tune for your specific simulation. Too slow and the lanes look frozen between updates; too fast and you have approximated the cost of full physics. One update per second worked for bowling because human-bowling cadence is roughly one throw per 10-20 seconds, and the visible state changes happen at the per-throw frequency. Tune the cadence to whatever your simulation's natural rhythm is.

## The state-machine separation

One architectural decision worth flagging: the state-machine code is the same for physics lanes and statistical lanes. The phase shape (idle, partialResetting, resetting, freshRackBetweenThrows, rolling, scoring) and the transitions between phases (which phase follows which on what input) are unified. Physics lanes reach more phases because the rolling and scoring phases are physics-driven; statistical lanes use a subset.

The unified state-machine code matters because it lets a lane move between classes without rewriting state. A stub becomes active-statistical when bowlers show up: same state-machine, just gets ticked now. An active-statistical becomes active-physics on focus: same state-machine, just gets driven by Rapier outcomes now. The class is the rendering and tick-source decision; the per-lane state is the same shape regardless of class.

This is the same pattern as the dual-render-mode separation in many other domains. The data model is uniform; the rendering and update mechanism is class-specific. The flexibility to move entities between classes without state translation is what makes the pattern scale to large entity counts.

## What I'm not claiming

- I'm not claiming this pattern is novel. RTS games have used "fog of war" plus state-machine simulation of unseen entities since the late 1990s. City builders have used per-tile statistical models instead of per-agent simulation since Sim City. What this post adds is the specific bowling-sim application plus the unified state-machine separation that lets entities move between fidelity classes without state translation.

- I'm not claiming the 50/50 strike-versus-partial RNG produces realistic bowling distributions. It does not. The current RNG is a calibration stub for V1 that gets replaced with skill-profile-driven distributions in Phase 8.x. The state machine is independent of the RNG; the calibration is a separate concern.

- I'm not claiming 1-Hz is universally the right cadence. Bowling has roughly one throw per 10-20 seconds at observation cadence; one update per second is fast enough to feel alive and slow enough to be cheap. Other simulations with faster or slower natural rhythms need different cadence calibration.

- I'm not claiming statistical-lane output is indistinguishable from physics-lane output under direct inspection. If a player focuses on a statistical lane and watches it carefully, the absent bowler and the absent ball trajectory are noticeable. The pattern works at background-lane attention level; it would not work at foreground attention level.

- I'm not claiming the recovery edge case is the optimal solution. Treating in-flight throws as 0-pin throws is a V1 trade-off that prioritizes implementation simplicity over physics-state preservation. The trade-off has a documented cost (the lost throw) that some players will notice. The alternative (full physics-state preservation across focus changes) is more engineering work for limited V1 benefit; the cost-benefit favored the trade-off for V1.

## What I am claiming

For simulation or tycoon games with many independent entities operating in parallel, splitting entities into foreground (full simulation) and background (reduced simulation at perceptible cadence) is a viable framerate-budget strategy. The reduction does not need to be elaborate. A state machine ticking at human-perceptible cadence, driving visible state changes that the human pattern-matching layer reads as "entity is active," works for a wide range of simulations.

The unified state-machine code matters. If the state machine is the same shape for foreground and background entities, entities can move between classes without state translation, which is what makes the pattern scale to large entity counts where some entities transit between classes during a session.

For bowling specifically: a 1-Hz state-machine tick driving a six-phase per-lane FSM, with the rolling and scoring phases unreachable on statistical lanes and the recovery path forcing stuck physics-phase lanes back to idle, produces visually indistinguishable background bowling at a tiny fraction of the per-lane cost of physics. The pattern handles four lanes at V1 (two physics, two statistical) and scales cleanly to dozens of statistical lanes before the framerate budget reappears as the binding constraint.

The empirical record this post stands on is a production six-lane R3F bowling-sim codebase running the pattern across 930 vitest tests, with operator-side visual verification of the statistical-lane visual integrity confirming the "looks like bowling" outcome at background attention level. The pattern is one architectural decision that paid back the engineering time it cost, several times over, by recovering the framerate budget that full-fidelity per-lane simulation would have consumed.
