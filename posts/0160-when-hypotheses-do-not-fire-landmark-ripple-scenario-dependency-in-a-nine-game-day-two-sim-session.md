# When Hypotheses Do Not Fire: Landmark-Ripple Scenario Dependency in a Nine-Game-Day Two-Sim Session

**Author:** Jimmy McColery
**Date:** 2026-07-04
**Status:** Single-finding arc; empirical observation that framework hypotheses H15 through H22 covering landmark-ripple sentiment propagation did not fire in a 9.11 game-day two-Sim session at seed=42 despite 16 landmark events and 878 co-located ticks; identifies validation-requires-scenario-coincidence class of hypothesis architecturally distinct from validation-requires-magnitude class; framework methodology observation about non-firing as first-class empirical data

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

Post 0159 documented a 9.11 game-day two-Sim island simulation session at seed=42. The session validated framework hypotheses H8 through H11 covering pair-history dynamics at extended horizon. Sentiment grew symmetrically to 0.78, the pair-history buffer filled to its 40-entry cap, and both Sims accumulated substantial co-located ticks after a 6.44-day pre-convergence phase.

Post 0159 did not cover framework hypotheses H15 through H22 covering landmark-ripple sentiment propagation. This post covers what happened with those hypotheses in the same session. Specifically: they did not fire.

Sixteen landmark events occurred during the session. Zero landmark events were co-witnessed by both Sims. All 16 events were solo witnessed by the actor Sim only. The landmark-ripple sentiment propagation mechanism the H15 through H22 hypotheses cover requires co-witnessing (both Sims present at the landmark event tick). No such co-witness occurred in this session.

This post is about what non-firing hypothesis events mean in the framework's operational discipline, the specific scenario coincidence that landmark-ripple requires, and why non-firing is first-class empirical data rather than absence of data.

## The specific run

The session ran two Sims independently on a 30x20 island grid for 13,123 ticks at seed=42. Both Sims accumulated survival milestones: shelter built (Sim A at tick 395, Sim B at tick 993), first fish caught (Sim A at tick 578, Sim B at tick 514), plus additional fish catches distributed across the session.

The framework's landmark event architecture fires an event object at each landmark trigger. Event objects include: tick number, actor Sim id, list of witnessing Sim ids, event type, affective magnitude. The pair state stores the landmark event log as a list, distinct from the pair-history event stream which stores type observed-together plus type shared-storm-survival plus type landmark-witnessed events.

The framework's H15 through H22 hypotheses cover landmark-ripple sentiment propagation: when a landmark event fires while both Sims are co-located, a landmark-witnessed event lands in the pair-history stream with affective delta computed from the landmark event's affective magnitude divided by a calibration constant. The specific delta calculation is 40 divided by 600 for fish caught events (~0.067) and 60 divided by 600 for shelter built events (0.10).

For H15 through H22 to fire, three conditions must hold simultaneously: a landmark event must trigger, both Sims must be co-located at the landmark tick, and the landmark event's witness list must include both Sim ids.

## The 16 landmark events

The landmark event log at session end contained 16 events. All 16 events had witness lists containing only the actor Sim id.

Fifteen of the 16 events were type fish caught (14 by Sim A plus B mix over the run; specifically Sim A caught fish at ticks 578, 1893, 3011, 4786, 7680, 9603, 9773, 11659 for eight events, Sim B caught fish at ticks 514, 4061, 6568, 8284, 8930, 11204, 12169 for seven events). One event was type shelter built (Sim A at tick 395).

None of these 16 events fell within the co-location window between ticks 9267 (first co-location) and 13,123 (session end) while both Sims were actually at the same grid cell. Some events (9603, 9773, 11204, 11659, 12169) fell during the post-convergence period, but co-location is a stricter condition than temporal co-occurrence: both Sims must be at the same grid cell at the exact tick, not just co-located in some general time window.

The pair state's coLocatedTicks counter at 878 measures ticks when both Sims occupied the same cell. That's approximately 22 percent of ticks during the post-convergence period. Any landmark event during that period had approximately 22 percent probability of falling during a co-located tick, and if it did, the actor Sim would need to be the one at the shared cell (Sim A's landmark actor requires Sim A at the shared cell; Sim B's landmark actor requires Sim B at the shared cell). Both Sims being at the shared cell during a landmark event is the required condition.

In this specific run, that condition never held. The five post-convergence landmark events all fired when the acting Sim was fishing at ocean-adjacent positions distant from the other Sim's current location.

## What non-firing tells us

Non-firing is a first-class empirical observation, not an absence of data. What non-firing tells us is that the hypothesis's trigger condition was not met during the session's specific scenario configuration. What it does not tell us is whether the hypothesis would fire correctly under conditions where the trigger holds.

For H15 through H22 specifically, non-firing at this session's seed 42 configuration tells us three things.

First: the scenario coincidence requirement (landmark during co-location with both Sims as witnesses) is a strict condition that does not hold under natural random-walk convergence at seed 42. The trigger condition is not automatically satisfied by extended session runtime alone.

Second: prior Phase 2 Sequence A validation of H15 through H22 at 3 to 5 thousand tick horizons presumably used either forced scenarios (fixed co-location or fixed landmark timing) or seeds where the coincidence happened by chance. Extended-horizon testing at natural random-walk scope does not reliably reproduce the coincidence.

Third: the empirical data from this session is not evidence against H15 through H22 firing correctly when the trigger holds. It's evidence that the trigger does not hold reliably under natural conditions at this seed at this horizon.

Distinguishing these three points is the load-bearing framework methodology observation.

## Validation-requires-scenario-coincidence class

Framework hypotheses can be categorized by what their trigger condition requires. Some hypotheses fire whenever their state condition holds (H8 fires whenever sustained co-location happens; H11 fires whenever pair-history events accumulate). Some hypotheses fire only when specific temporal coincidences happen (H15 through H22 fire only when landmark events fall during co-location windows with both Sims as witnesses).

I've been calling the first category validation-requires-magnitude and the second category validation-requires-scenario-coincidence. Both categories are valid hypothesis types. Both categories require validation. But they require different validation strategies.

Validation-requires-magnitude hypotheses can be tested by running the framework at scale until the state condition accumulates enough to trigger. Extended-horizon testing works. Larger population testing works. Direct scenario forcing is not required.

Validation-requires-scenario-coincidence hypotheses require either sufficiently long scale for the coincidence to happen by natural random-walk (which may take arbitrary long horizons) or explicit scenario forcing (fixed co-location plus fixed landmark timing). Extended-horizon natural testing does not reliably validate these hypotheses.

The framework's Phase 2 Sequence A hypothesis suite includes both categories. H8 through H11 are validation-requires-magnitude. H15 through H22 are validation-requires-scenario-coincidence.

What today's session revealed empirically is that extended-horizon natural testing validates the first category cleanly (Post 0159 documented H8 through H11 firing at 13 thousand tick horizon) but does not validate the second category (H15 through H22 did not fire even at 13 thousand tick horizon plus 878 co-located ticks plus 16 landmark events).

## Framework methodology observation

The framework's operational discipline should distinguish between validation-required-under-natural-conditions and validation-required-under-forced-conditions when categorizing hypotheses. Extended-horizon natural testing at scope 2X or higher is sufficient for the first category. Explicit scenario testing (fixed initial conditions producing the required coincidence) is required for the second category.

This distinction matters for framework validation planning. A framework claim that hypothesis H15 has been validated at scope 2X does not require just runtime scale; it requires either a forced scenario or a demonstration that natural random-walk at that scale produces sufficient coincidence density to validate. Today's session demonstrates that scope 2X natural random-walk does not reliably produce the coincidence density (16 landmark events across 878 co-located ticks yielded zero co-witness events).

For framework validation of H15 through H22 at natural conditions, either significantly longer horizons (perhaps 100+ game-days) or forced-scenario testing (deliberate co-location during known landmark timing) is required. The framework's operational memory adds this observation as a validation-strategy note for future hypothesis testing at these specific hypotheses.

The distinction also matters for how framework observations interpret hypothesis-non-firing events. If the operator or a downstream analyst sees a session log with zero landmark-ripple events, that's ambiguous unless the observer knows whether the trigger condition held. If the trigger condition never held (as in this session), non-firing is expected. If the trigger condition held but the event failed to fire, non-firing is a bug. Distinguishing these requires the framework to explicitly track trigger-condition-met events separately from hypothesis-fired events.

## What actually shipped

The framework's operational memory added a project record documenting the H15 through H22 non-firing observation from the 9.11 game-day two-Sim session at seed=42. The record cross-references Post 0159 for the H8 through H11 firing observations and this post for the H15 through H22 non-firing observation.

The framework's canonical Sim AI implementation is unchanged. The hypothesis architecture remains as specified. The non-firing observation does not require any code change; it identifies a validation-strategy gap that requires either scenario-forced testing or significantly extended-horizon natural testing at future hypothesis validation events.

Post 0136 empirical BUILD-mode-as-architecture-as-hypothesis discipline preservation: the H15 through H22 hypotheses remain architecturally canonized as expectations about the framework's landmark-ripple behavior. This session did not falsify the hypotheses; it identified that natural-conditions testing at 2X scope does not reliably exercise them. Future testing at the scenario-forced scope or at significantly extended natural scope would produce firing events that either validate the hypotheses or falsify them.

## What I'm not claiming

I'm not claiming H15 through H22 are wrong or unvalidated because they did not fire in this session. The Phase 2 Sequence A validation events at 3 to 5 thousand tick horizons plus specific scenario tests remain the framework's empirical foundation for these hypotheses. What I'm documenting is that natural-conditions testing at 2X scope does not reliably re-validate these hypotheses because the trigger condition (co-witness landmark event) does not naturally occur at sufficient density.

I'm not claiming the 16 landmark events in this session represent a comprehensive sample of what landmark events look like at extended horizon. Different seeds would produce different landmark timing and different actor distributions. A different session might produce co-witness landmark events by natural coincidence. What I'm claiming is that this specific run at seed 42 for 9.11 game-days did not produce any co-witness events.

I'm not claiming validation-requires-scenario-coincidence hypotheses are architecturally worse than validation-requires-magnitude hypotheses. Both are valid classes of hypothesis. Both require validation. What I'm claiming is that they require different validation strategies, and framework validation planning should distinguish between them explicitly.

I'm not claiming this framework methodology observation is novel outside my framework. Distinguishing between hypotheses that fire on state conditions versus hypotheses that fire on temporal coincidences is a general concept in agent-based-simulation testing. What I'm claiming is that my framework's canonized hypothesis suite mixes both types and today's session data supports adding an explicit validation-strategy annotation to each hypothesis in future canonization events.

I'm not claiming non-firing as first-class data is a novel discipline. Test scientists distinguish between fail-to-satisfy and fail-to-trigger regularly. What I'm claiming is that my framework's operational discipline should adopt this distinction explicitly when interpreting session logs.

## What I am claiming

Framework hypotheses H15 through H22 covering landmark-ripple sentiment propagation did not fire in a 9.11 game-day two-Sim session at seed=42 despite 878 co-located ticks and 16 landmark events. The trigger condition (co-witness landmark event where both Sims are at the shared cell at the exact landmark tick) did not hold naturally under this session's random-walk convergence dynamics.

Framework hypotheses can be categorized as validation-requires-magnitude (fire whenever state condition accumulates) versus validation-requires-scenario-coincidence (fire only when specific temporal coincidences hold). Extended-horizon natural testing at scope 2X validates the first category but does not reliably validate the second category. The framework's validation strategy should distinguish between these categories explicitly.

Non-firing hypothesis events are first-class empirical data, not absence of data. When a hypothesis does not fire in a session, the framework must distinguish between trigger-condition-not-met (expected non-firing) and trigger-condition-met-but-event-failed (bug non-firing). Session log analysis benefits from tracking trigger-condition-met events separately from hypothesis-fired events.
