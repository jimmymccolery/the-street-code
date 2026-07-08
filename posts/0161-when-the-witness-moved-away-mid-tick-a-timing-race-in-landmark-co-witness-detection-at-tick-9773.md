<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0161
title: When the Witness Moved Away Mid-Tick A Timing Race in Landmark Co-Witness Detection at Tick 9773
date_published: 2026-07-04
status: published
superseded_by: none
domain: framework timing-race condition discovery in H15-H22 landmark-ripple co-witness detection at extended-horizon 12.05 game-day session
project_scopes: framework-methodology, sim-ai
cc_task_relevance: framework-timing-race-discovery, co-witness-detection-audit, extended-horizon-analysis-refines-framing
phase_binding: Phase-2
discipline_family: extended-horizon empirical analysis surfaces findings shorter-horizon missed
canonical_rule: co-witness detection timing race where witness at same cell start-of-tick moves during same tick before framework check runs; revises Post 0160 framing from purely coincidence-dependent to also timing-model-dependent
load_bearing_claims:
  - Both Sims began tick 9773 at grid cell (1,4) but framework recorded witness list as actor-only
  - Sim B moved to (2,4) during same tick before framework co-witness check ran
  - Revises Post 0160 H15 through H22 non-firing framing from purely coincidence-dependent to also timing-model-dependent
  - Extended-horizon analysis surfaces findings shorter-horizon missed
applicability_triggers:
  - Extended-horizon session extends prior post shorter-horizon session
  - Framework tick-order matters for co-witness detection
  - Refinement post extends prior post framing without invalidating
mechanism_details:
  - Both Sims at (1,4) at start of tick 9773
  - Sim B move_toward action executes before framework co-witness check
  - Framework co-witness check reads Sim B position at (2,4) not start-of-tick (1,4)
  - Extended-horizon analysis to 12.05 game-days (17,357 ticks) surfaced this
cross_refs:
  - Post 0159 (late-convergence emergent behavior at 9.11 game-day scope)
  - Post 0160 (H15-H22 non-firing framing revised by this post)
  - Post 0162 (sentiment persistence at 0.78 empirical foundation for accumulator persistence)
  - Memory feedback_extended_horizon_analysis_surfaces_findings_shorter_horizon_missed_2026-07-04.md
CC-OPTIMIZED-SUMMARY -->

# When the Witness Moved Away Mid-Tick: A Timing Race in Landmark Co-Witness Detection at Tick 9,773

**Author:** Jimmy McColery
**Date:** 2026-07-04
**Status:** Single-finding arc; empirical discovery of a framework timing-race condition in framework hypotheses H15 through H22 covering landmark-ripple co-witness detection at extended-horizon 12.05 game-day two-Sim island simulation session at seed=42; both Sims began tick 9,773 at grid cell (1,4) but the framework recorded the witness list as actor-only because Sim B moved to (2,4) during the same tick before the framework's co-witness check ran; revises Post 0160's H15 through H22 non-firing framing from purely coincidence-dependent to also timing-model-dependent

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

Post 0160 documented that framework hypotheses H15 through H22 covering landmark-ripple sentiment propagation did not fire in a 9.11 game-day two-Sim island session at seed=42. The post framed the non-firing as scenario dependency: the required condition (both Sims co-located at the exact landmark tick) did not occur naturally under random-walk convergence.

I extended that session to 12.05 game-days at seed=42 and ran the analysis again. The extended session added 4,234 more ticks and 4 more landmark events. Zero of those additional landmark events produced co-witness fires either. But the extended analysis surfaced something Post 0160 missed at 9.11 game-day scope: a specific tick where both Sims were at the same grid cell at the start of the tick but the framework still recorded actor-only witness.

The tick was 9,773. The grid cell was (1,4). Sim A caught a fish. Sim B was there. The framework wrote `witnessedBySimIds: ['a']`.

This post is about what happened at tick 9,773, why the framework recorded the witness list the way it did, and why the finding revises Post 0160's non-firing framing from scenario-coincidence-dependent to also-tick-timing-dependent.

## The specific tick

The session log records state snapshots at each tick. The snapshot at tick 9,773 shows Sim A at position (1,4) with currentAction fish, and Sim B at position (1,4) with currentAction climb_to_high_point. The landmark event log for the session includes an entry `{tick: 9773, actorSimId: 'a', witnessedBySimIds: ['a'], eventType: 'fish_caught', affectiveMagnitude: 40}`.

The state snapshot at tick 9,772 shows Sim A at (1,4) fishing and Sim B at (1,4) doing search_horizon. The state snapshot at tick 9,774 shows Sim A at (1,4) doing nothing and Sim B at (2,4) doing climb_to_high_point. The state snapshot at tick 9,775 shows Sim A at (1,4) eating fish and Sim B at (2,4) still climb_to_high_point.

Both Sims began tick 9,773 physically co-located at grid cell (1,4). Sim A completed the fish action during that tick, triggering the fish_caught landmark event. Sim B moved to (2,4) during the same tick because the climb_to_high_point action is a navigation action that moves toward its target grid cell each tick until arrival.

The framework's landmark event capture logic runs after both Sims have advanced their state during the tick. That means when the landmark event's witness-detection ran, Sim B was already at (2,4), not (1,4). The co-location check `simA.position.x === simB.position.x && simA.position.y === simB.position.y` evaluated to `false` because `1 !== 2`.

## The timing sequence in framework code

The framework's `tickIslandWorld` function processes each tick in a specific order. First, Sim A's state advances (need decay, action progression, movement if navigating). Second, if Sim B is present, `tickSimB` runs Sim B's state advance. Third, `detectAndApplyPairInteractions` fires any pair-history events (observed_together, shared_shelter, shared_storm_survival). Fourth, landmark-event transition detection checks each landmark trigger condition (shelter_built, fish_caught, storm_survived, exposure_crisis) and calls `fireLandmarkEvent` for any trigger that fires this tick.

`fireLandmarkEvent` reads the state at the moment it's called. That state has already been updated by `tickSimB`. So Sim B's position at `fireLandmarkEvent`-time is Sim B's post-tick position, not Sim B's pre-tick position.

At tick 9,773, the sequence was:
1. Sim A's fish action completed during tick advancement; hasCaughtFish transitioned false to true; Sim A stayed at (1,4).
2. `tickSimB` ran; Sim B's climb_to_high_point action navigated one grid cell toward its target; Sim B moved from (1,4) to (2,4).
3. `detectAndApplyPairInteractions` ran; because Sim A at (1,4) and Sim B at (2,4) are not co-located after tickSimB, no observed_together fire for this tick.
4. The `if (!priorHasCaughtFishA && next.hasCaughtFish)` check was true; `fireLandmarkEvent(next, 'a', 'fish_caught', 40)` was called.
5. Inside `fireLandmarkEvent`, the co-location check compared Sim A's position (1,4) to Sim B's post-tickSimB position (2,4); the check evaluated to false; witness list stayed at `[actorSimId]` = `['a']`.

The framework recorded the landmark event with witness = `['a']` even though both Sims were at (1,4) at the start of tick 9,773.

## What this means for H15 through H22

H15 through H22 hypotheses cover the landmark-ripple sentiment propagation mechanism. The mechanism requires the witness list to contain both Sim IDs; if both are witnesses, the framework appends a `landmark_witnessed` pair-history event with affective delta = `affectiveMagnitude / 600` for each direction, updating sentiment.

The witness list at tick 9,773 contained only `['a']`. The co-witness condition was not met. The `landmark_witnessed` event did not fire. Sentiment did not update from this landmark.

Post 0160 documented that H15 through H22 did not fire in the 9.11 game-day session and framed the non-firing as scenario dependency (the required temporal coincidence did not occur naturally). This new observation at tick 9,773 refines that framing. The coincidence did occur, at least in the physical sense that both Sims were at the same grid cell during the tick when the landmark event triggered. The framework's timing model filtered that coincidence out because Sim B moved before the co-witness check ran.

For the H15 through H22 hypothesis suite specifically, this reveals that the co-witness condition as implemented is stricter than "both Sims at the same grid cell during the landmark tick". The implemented condition is closer to "both Sims at the same grid cell at end of tick when the framework announces the landmark event". A witness who was at the cell at start-of-tick but moved during the tick does not count.

## Whether this is a bug

Whether this counts as a framework bug depends on what the intended co-witness semantics are. Two reasonable interpretations exist.

Interpretation one: co-witnessing requires end-of-tick co-location. Under this interpretation, the framework is behaving as designed. Sim B was at the shared cell only briefly during the tick; if Sim B was already moving toward a different target, Sim B's attention was not on Sim A's fishing outcome. The framework's timing model captures this by checking end-of-tick position.

Interpretation two: co-witnessing requires any-time co-location during the tick's action window. Under this interpretation, the framework has a subtle race condition. Sim B was physically at the cell during Sim A's fishing (which spans multiple ticks); Sim B would have observed Sim A's success. The framework misses this because it checks post-move position rather than any position during the tick.

Neither interpretation is inherently correct without operator judgment about what co-witness means semantically. I currently lean interpretation two, because the intuitive framework claim "both Sims saw it happen" fits better with the physical trajectory (Sim B was there for the fishing action) than with the strict end-of-tick check (Sim B had just left). But this is an operator-scope judgment that requires framework methodology deliberation, not a code-level bug I can point at unambiguously.

Post 0143's canonization-propagation gap discipline family applies here in a specific sub-form: the H15 through H22 hypothesis architecture as originally scoped in Phase 2 Sequence A does not explicitly specify which of these two interpretations the framework should implement. The implementation defaulted to interpretation one via the specific ordering of tickSimB then fireLandmarkEvent. Whether this default aligns with the framework's methodological intent is an open question this observation surfaces.

## Extending the observation

I checked all 20 landmark events in the session's landmark event log. For each, I extracted Sim A's and Sim B's positions and current actions at the tick when the event fired. Only tick 9,773 had both Sims physically at the same grid cell at the start of the tick (both at (1,4)). The other 19 events had Sims at different grid cells; those events would have been correctly non-co-witnessed regardless of timing-model interpretation.

Tick 9,773 is the single case in this session where the two interpretations produce different framework behavior. Under interpretation one (current), witness = `['a']`. Under interpretation two (proposed), witness would be `['a', 'b']`.

If interpretation two were the framework's canonical semantics, this session's H15 through H22 hypothesis suite would have fired exactly one landmark_witnessed event (at tick 9,773 for fish_caught with magnitude 40, producing sentiment delta 40 / 600 ≈ 0.067 in each direction). That single event would still not exercise the full ripple-sentiment mechanism across many landmark events, but it would move H15 through H22 from zero-fire non-firing to one-fire minimal-firing.

Under interpretation one (current), the extended session still produces zero landmark_witnessed events across 12.05 game-days. That's consistent with Post 0160's non-firing observation, extended by 2.94 additional game-days.

## What non-firing tells us at extended horizon

Post 0160's framework methodology observation was that non-firing is first-class empirical data, and that the framework must distinguish trigger-condition-not-met (expected non-firing) from trigger-condition-met-but-event-failed (bug non-firing). The tick 9,773 observation reveals a third category: trigger-condition-partially-met-under-strict-interpretation-but-fully-met-under-lenient-interpretation. That's a category the current framework hypothesis suite doesn't cleanly express because the hypothesis suite itself doesn't specify which interpretation is canonical.

This suggests the H15 through H22 hypothesis suite needs an amendment to specify co-witness semantics explicitly. The amendment options include: end-of-tick strict (current), any-time-during-tick lenient, or a hybrid that captures both and lets framework methodology track which interpretation produces which fire.

Under end-of-tick strict, the framework's extended-horizon empirical data at 12.05 game-days shows zero co-witness fires. Under any-time-during-tick lenient, the same data would show one co-witness fire. The choice between interpretations changes the empirical picture the framework has about its own landmark-ripple mechanism.

The load-bearing framework methodology observation is that hypothesis-suite specification must include implementation-detail commitments about tick-timing semantics, or else the same physical scenario data can produce different empirical conclusions depending on undocumented implementation choices.

## What actually shipped

Nothing in the framework's Sim AI implementation was changed as a result of this observation. The tick 9,773 finding is a framework methodology observation, not a bug fix; the code as written is a coherent implementation of interpretation one, and changing it would require operator judgment about which interpretation is canonical.

What did ship is this post plus a companion memory entry noting the observation for future Council candidacy. If a future methodological Council deliberates on H15 through H22 hypothesis-suite refinement, the tick 9,773 timing-race finding is empirical foundation for the deliberation. The framework's operational memory has the observation banked.

Post 0136's empirical BUILD-mode-as-architecture-as-hypothesis discipline preservation: the H15 through H22 hypotheses remain architecturally canonized as expectations about the framework's landmark-ripple behavior at the coarse level. What this session reveals is that the coarse-level canonical hypothesis suite needs finer-grained specification at the tick-timing implementation-detail level.

## What I'm not claiming

I'm not claiming this framework observation identifies a Sim AI bug that needs fixing. The framework's implementation is a coherent choice under interpretation one (end-of-tick co-location required for co-witnessing). Whether interpretation two (any-time co-location) is the canonical intent is an operator-scope judgment I have not yet made.

I'm not claiming Post 0160's non-firing observation was wrong. Post 0160 correctly identified that H15 through H22 did not fire in the 9.11 game-day session; that non-firing observation extended to 12.05 game-day scope in this analysis. What I'm claiming is that Post 0160's scenario-coincidence framing was incomplete: the non-firing also reflects the framework's specific tick-timing model, not only coincidence density.

I'm not claiming the tick 9,773 case is common. Across all 20 landmark events in the extended session, exactly one had both Sims physically co-located at the start of the tick when the landmark event triggered. Nineteen of the 20 events had Sims at genuinely different grid cells regardless of timing-model interpretation. The tick 9,773 case is a specific edge case, not a systematic pattern.

I'm not claiming that revising the co-witness detection to interpretation two would produce dramatically different framework behavior at extended horizon. In this session, the switch would produce one additional co-witness fire (at tick 9,773 for fish_caught). That's one landmark_witnessed event across 12.05 game-days plus 878 co-located ticks plus 20 landmark events. The revision would not transform the framework's landmark-ripple behavior at this horizon.

I'm not claiming this observation resolves the H15 through H22 hypothesis validation question. The hypothesis suite still has effectively zero validation events in extended-horizon natural testing regardless of interpretation. Forced-scenario testing or significantly longer horizons remain the reliable validation paths per Post 0160.

## What I am claiming

At tick 9,773 in a 12.05 game-day two-Sim island session at seed=42, both Sim A and Sim B were at grid cell (1,4) at the start of the tick. Sim A caught a fish during the tick, triggering a fish_caught landmark event. The framework recorded the witness list as `['a']` (actor only), not `['a', 'b']` (both co-witnesses). The reason is that Sim B's climb_to_high_point action moved Sim B to (2,4) during the tick, and the framework's co-witness check ran after that move.

The framework's H15 through H22 hypothesis suite covering landmark-ripple co-witness detection has an implementation-detail commitment to end-of-tick co-location that is not explicitly specified in the coarse hypothesis suite. A physically-co-located witness who moved during the tick does not count as a co-witness under the current implementation.

Post 0160's non-firing observation for H15 through H22 in this session is empirically accurate under the current implementation (zero co-witness events across 12.05 game-days) but the framing that non-firing reflects only scenario coincidence is incomplete. Non-firing also reflects the framework's specific tick-timing model. Under an alternative timing model where any-time-during-tick co-location suffices, this session would have produced one co-witness fire at tick 9,773.

Framework hypothesis-suite specification benefits from explicit commitments to implementation-detail-level semantics like tick-timing, or else different implementations of the same coarse hypothesis produce different empirical conclusions on the same scenario data. The H15 through H22 hypothesis suite is a specific instance of this pattern.
