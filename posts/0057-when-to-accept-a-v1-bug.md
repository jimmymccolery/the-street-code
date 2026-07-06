<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0057
title: When to accept a V1 bug: documenting trade-offs in early-access game development
date_published: 2026-05-31
status: published
superseded_by: none
domain: bug triage discipline for early-access V1 shipping
project_scopes: pin-paradise, street-code-methodology
cc_task_relevance: v1-bug-triage, early-access-shipping-decisions, documentation-discipline-for-known-issues
phase_binding: era-independent
discipline_family: none-applicable
canonical_rule: A narrow class of V1 bugs should ship with the release when cost-of-fix-now is high and cost-of-shipping-with-it is acceptable, disciplined by honest documentation
load_bearing_claims:
  - Standard fix-every-bug discipline is correct for gameplay-blocking crash-producing or confusing bugs
  - Second class exists where fix cost is high and ship cost is acceptable
  - The hard part is honest triage without sliding into fix-never-ship-anyway rationalization
  - Documentation discipline is what makes acceptance honest
applicability_triggers:
  - When shipping V1 or Early Access with known-issue backlog
  - When making bug triage decisions on solo indie project
  - When authoring team-transparency around trade-offs
mechanism_details:
  - Explicit acceptance-with-documentation surfaces trade-off honestly to players
  - Framework applied to subsequent triage decisions to avoid backsliding
cross_refs:
  - Post 0049 (design mode vs code mode)
  - Post 0063 (loose-end audits post-commit hygiene)
-->

# When to accept a V1 bug: documenting trade-offs in early-access game development

**Author:** Jimmy McColery
**Date:** 2026-05-31
**Status:** Single-finding arc on the bug-triage discipline for shipping at V1; n=1 trade-off from a multi-lane bowling-sim BUILD cycle

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

The standard indie-dev shipping discipline says: fix every bug before you ship. The discipline is correct for the wide class of bugs that block gameplay, produce crashes, or surface confusingly to players. The discipline is also incorrect for a narrower but real class of bugs that ship with the V1 because the cost of fixing them right now is high and the cost of shipping with them is acceptable. The second class is the one this post is about.

The hard part is not the discipline. The hard part is the triage decision: which bugs go in each class, and how do you make the call honestly without sliding into "fix never, ship anyway" rationalization. The bowling-alley tycoon sim I'm building solo as Early Access for October 31, 2026 surfaced one such bug during a recent BUILD cycle. The triage decision went toward "accept and document." This post is about how that decision got made, the documentation discipline that made the acceptance honest, and the framework I'm now applying to subsequent triage decisions.

## The bug

The sim renders multiple bowling lanes simultaneously. Two of the V1 lanes run full physics simulation with interactive bowlers; the player can press Shift-L to cycle which lane is currently focused (i.e., which lane the camera is centered on and which lane the bowler interaction targets).

During a Phase 4.A refactor that promoted the per-lane physics setup to support multi-lane rendering in a single shared physics world, an interaction edge case appeared. If the player pressed Shift-L while a bowling ball was mid-flight on the currently-focused lane, the focus cycled to the next lane, and the previously-focused lane's in-flight throw was lost. The ball that was mid-flight stopped existing in the simulation; the throw was scored as a zero-pin throw (functionally a gutterball, even if the ball had been on a clean trajectory toward a strike); the lane state advanced to the next throw normally.

The mechanism was specific. The Phase 4.A refactor used React component remounting (via a `key={focusedLaneId}` prop) to force a clean lane state when focus changed. The clean remount eliminated a class of subtle bugs related to lane state crossing between focuses (covered in detail in Post 44). The trade-off was that the remount also discarded any in-flight physics state. The bowling ball's `RigidBody` got destroyed during the unmount; the ball stopped existing.

A real player encountering this bug would see: I was about to strike, I pressed Shift-L to check another lane, my throw scored zero. The complaint pattern would be "the game ate my throw." The frustration is genuine; the bug is visible; the bug is reproducible.

## The triage decision

The fix that would eliminate the bug entirely was clear at the design layer. Multi-physics-lane simultaneous rendering with per-lane RigidBody persistence (so that lane 17-A's ball remains in the physics world even when focus is on lane 35-A) would let the in-flight throw complete normally regardless of focus changes. The design for this fix existed at the architectural level; the implementation was scoped for a later phase of the BUILD arc.

The question was whether to ship the fix in the Phase 4.A scope or to ship the bug to V1 and fix in a later phase. The factors that informed the decision:

The full fix was substantial engineering work. Persistent per-lane RigidBody management across focus changes required a refactor of how lane state attached to the physics world. Estimates put the work at three to five BUILD-day equivalents (using the 40-commit BUILD-day as the unit). The Phase 4.A scope was already taking the codebase through a meaningful refactor; piling the per-lane persistence work on top would have extended the Phase 4.A arc past the operator-bandwidth threshold.

The bug was edge-case. Players who press Shift-L mid-throw would experience the lost throw. Players who let throws complete before cycling focus would never see the bug. The natural play pattern (watch your throw resolve, then maybe look at other lanes) does not produce the bug. The bug appears only when the player cycles focus during the few-second window when a ball is mid-flight.

The bug was diagnosable. When the bug fired, the lost throw was attributable to the focus change. A player could (a) reproduce the bug intentionally by pressing Shift-L mid-throw, (b) understand the connection between the action and the outcome, and (c) avoid the bug by not pressing Shift-L mid-throw. The mental model the player would build (avoid focus changes during physics) is approximately correct; the workaround is straightforward.

The bug was bounded. The lost throw scored as zero; the lane continued normally; the game did not crash or corrupt save state. The blast radius was one throw's score, not session continuity. The player could continue playing without further consequence.

The full fix was on the BUILD-arc roadmap. The Phase 4 full-acceptance-gate scope (later than Phase 4.A) included the per-lane RigidBody persistence work. The bug was not abandoned; it was deferred to a phase that already included the substantial engineering required.

The triage decision was: accept the bug at V1, document the trade-off explicitly, schedule the fix for the Phase 4 full-acceptance-gate. The decision shipped the Phase 4.A refactor without expanding scope; the deferred fix shipped in a later BUILD commit that referenced the original trade-off context.

## The documentation discipline

The discipline that made the acceptance honest (rather than rationalization) was the documentation discipline. Three artifacts captured the trade-off:

The commit message at the Phase 4.A BUILD commit explicitly named the trade-off. The commit message section "V1 trade-off accepted" listed the bug, the fix that would eliminate it, the reason the fix was deferred, and the phase scheduled for the fix. The commit message was the canonical record of the decision at the time the decision was made.

The downstream commits that referenced the bug (the Phase 4.C statistical-lane stuck-phase recovery commit, which had to handle the edge case where focus changes left a statistical lane mid-physics) referenced the original Phase 4.A trade-off context explicitly. The downstream commits were not surprised by the bug; they read the original trade-off context and built consistent responses on top of it.

The Phase 4 full-acceptance-gate commit that resolved the bug referenced the original trade-off context explicitly. The resolution commit's message documented what the trade-off had been, why the deferred fix was now appropriate, and what the test coverage would catch in the future to prevent regression. The trade-off arc was readable in the git history: original trade-off acceptance, downstream consistent handling, eventual resolution.

The documentation pattern is operationally cheap (a few additional sentences in each commit message at the trade-off acceptance, downstream, and resolution commits) and operationally load-bearing (the trade-off does not get forgotten between phases). The artifact lives in the git history, which is the canonical record of decisions for the codebase. Anyone reading the commit chain at any future point sees the trade-off context.

## The naming distinction

One naming distinction that matters: a "V1 trade-off" is not a "regression."

A regression is an unintended change in behavior that breaks previously-working functionality. Regressions are bugs; the fix is to restore the prior behavior; the discipline is to ship the fix in the same arc as the change that introduced the regression.

A V1 trade-off is an intended change in behavior that produces a known limitation accepted at decision time. Trade-offs are decisions, not bugs; the path forward is documented at decision time; the discipline is to document the trade-off so it does not get conflated with regressions later.

The distinction matters because the response is different. A regression demands an immediate fix. A trade-off demands documentation plus scheduling. Conflating the two produces either over-fixing (treating trade-offs as regressions and burning engineering time on issues that shipped intentionally) or under-fixing (treating regressions as trade-offs and shipping broken functionality with rationalization). The naming discipline forces the triage decision to be explicit about which category each issue belongs in.

In the bowling-sim case, the focus-change-loses-throw issue was explicitly named a "V1 trade-off" in the commit message. The naming made the response category explicit: document, schedule, accept ship. If the same behavior had been an unintended consequence of the Phase 4.A refactor that broke a previously-working feature, the naming would have been "regression" and the response would have been immediate fix within the Phase 4.A scope.

## The eventual resolution

The Phase 4 full-acceptance-gate landed several BUILD cycles after Phase 4.A. The per-lane RigidBody persistence work shipped as a discrete commit with its own scope and its own test coverage. The bug that had been accepted as a V1 trade-off was now resolved.

The resolution commit referenced the original Phase 4.A trade-off context explicitly. The test coverage added to the resolution commit included a specific test case for the focus-change-mid-throw scenario (asserting that the in-flight throw completes normally regardless of focus changes). The test serves as a regression-prevention guard against future refactors accidentally reintroducing the bug; the test name and assertion document the original trade-off context for future readers of the test code.

The trade-off arc closed cleanly. The bug existed for several BUILD cycles between the Phase 4.A trade-off acceptance and the Phase 4 full-gate resolution. During those cycles, the documentation discipline kept the trade-off visible. The downstream BUILD work built consistent handling on top of the trade-off rather than tripping over it. The eventual resolution committed independently with the test coverage that prevents regression.

The cost across the arc was bounded. The Phase 4.A BUILD shipped on schedule because the trade-off accepted the bug rather than expanding scope. The downstream BUILD work consumed a small additional engineering cost to handle the trade-off consistently (the statistical-lane stuck-phase recovery added a few lines of recovery code that would not have existed without the trade-off). The Phase 4 full-gate paid the full fix cost when its scope included the substantial engineering anyway. The total cost was lower than expanding the Phase 4.A scope to include the full fix at Phase 4.A timing, because the Phase 4.A operator-bandwidth budget was already at capacity.

## The pattern

The trade-off-acceptance discipline generalizes to other indie-dev V1 scoping decisions. The framework I'm now applying to subsequent triage decisions has four checks:

The full fix is substantial. If the fix would take less time than the documentation discipline, just fix it. The trade-off discipline is for cases where the fix cost is substantial enough that shipping with the bug saves real engineering bandwidth.

The bug is edge-case. The bug appears only under specific player actions that are not the natural play pattern. Players who play normally never see the bug. Players who reproduce the bug can connect the action to the outcome and avoid the bug.

The bug is diagnosable. When the bug fires, the player can understand what happened and why. The mental model the player builds (avoid the trigger action) is approximately correct. The workaround is straightforward.

The bug is bounded. The bug's blast radius is small (one throw, one frame, one local state change) rather than large (session corruption, save state breakage, gameplay-blocking crash). The player can continue playing without further consequence.

If all four checks pass, the trade-off-acceptance path is viable. If any check fails, the bug should be fixed within the current scope rather than deferred. The framework is a triage filter, not a license to ship broken software.

The documentation discipline is the load-bearing complement to the framework. Trade-off acceptance without documentation is rationalization. The commit-message discipline plus the downstream-reference discipline plus the resolution-reference discipline make the acceptance honest by leaving an auditable trail of the decision and its eventual resolution.

## What I'm not claiming

- I'm not claiming "ship with bugs" is universally correct. Most bugs should be fixed. The trade-off-acceptance discipline applies to a narrow class of bugs that meet specific criteria; the default for any bug that does not meet the criteria is to fix.

- I'm not claiming the four-check framework is exhaustive. Other factors (player-base sensitivity, competitive market expectations, regulatory or compliance requirements, severity of downstream consequences) might shift the triage decision in specific contexts. The four checks are necessary conditions, not sufficient.

- I'm not claiming the documentation discipline is novel. Commit-message discipline as a load-bearing engineering practice has been standard since the rise of distributed version control in the mid-2000s. What this post adds is the specific application of the discipline to V1-trade-off acceptance and the naming distinction (trade-off vs regression) that informs the response category.

- I'm not claiming all indie devs should adopt this framework. The discipline costs operator attention to apply (the trade-off-acceptance decision needs to be deliberate; the documentation needs to be written explicitly; the downstream commits need to reference the trade-off context). For indie devs with smaller scope or simpler codebases, the cost of the discipline may exceed the benefit. The framework is useful when the trade-off-versus-fix decisions are frequent enough that ad-hoc triage produces inconsistent results.

- I'm not claiming the bowling-sim trade-off was the most important V1 decision the BUILD arc produced. Many other decisions (architectural lock choices, scope deferrals, feature cuts) were similarly load-bearing for the V1 ship. The focus-change-loses-throw trade-off is the most legible single-bug instance of the framework in action; other trade-offs in the same arc applied the same discipline to different specific issues.

## What I am claiming

For indie game development targeting V1 with finite operator bandwidth, a subset of bugs that meet specific triage criteria (substantial fix cost, edge-case trigger, diagnosable mental model, bounded blast radius) can be accepted at V1 ship with explicit documentation discipline rather than fixed in the current arc. The acceptance is honest only if the documentation discipline holds: commit-message naming at trade-off acceptance, downstream-commit references to the trade-off context, resolution-commit references to the original trade-off plus regression-prevention test coverage.

The naming distinction between "V1 trade-off" and "regression" is load-bearing for the triage discipline. A V1 trade-off is an intentional decision; a regression is an unintentional break. The response category differs (document and schedule versus immediate fix); the naming forces the triage to be explicit about which category each issue belongs in.

The framework applied to the bowling-sim focus-change-loses-throw bug accepted the bug at the Phase 4.A BUILD commit, handled it consistently in downstream BUILD work, and resolved it at the Phase 4 full-acceptance-gate with regression-prevention test coverage. The trade-off arc closed cleanly across the BUILD cycles; the total engineering cost was lower than expanding the Phase 4.A scope would have been; the player-visible bug existed for several cycles but did not block V1 ship readiness.

The empirical record this post stands on is the one V1-trade-off acceptance in the Phase 4.A BUILD commit (commit message documented the trade-off explicitly), the consistent downstream handling in the Phase 4.C statistical-lane recovery commit, and the resolution at the Phase 4 full-acceptance-gate commit with regression-prevention test coverage. n=1 on the framework application within a single BUILD arc. Whether the four-check framework holds across other indie-dev contexts and other bug classes is the empirical extension worth watching across future BUILD arcs.

The discipline is not "ship with bugs." The discipline is "make the triage decision deliberate, document the trade-offs honestly, schedule the resolution explicitly, and prevent regression at the resolution." The bowling-sim BUILD arc is one instance of the discipline in production; the framework I'm now applying to subsequent triage decisions is the artifact this post is naming.
