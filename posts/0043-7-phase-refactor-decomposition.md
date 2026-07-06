<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0043
title: 7 Phase Architectural Refactor Decomposition How to Ship Invasive Changes Without Breaking Flow
date_published: 2026-05-27
status: published
superseded_by: none
domain: Methodology lesson: pre-refactor sub-design proposal decomposing invasive work into 7 commit-sized phases each with acceptance gate contains bugs to phase that introduced them
project_scopes: pin-paradise, cross-cutting
cc_task_relevance: methodology-research, empirical-BUILD
phase_binding: era-independent
discipline_family: Rule-14-Madisonian
canonical_rule: Per-phase acceptance gate forces naming what each phase is for before source code commits to decision that would need undoing multi-substrate AI review of proposal surfaces ambiguities in gate definitions
load_bearing_claims:
  - Seven phases: prerequisites, module split, state shape transition, scene-tree architecture, subsystem migrations (with 4.A/4.B/4.C/4-full-gate splits), test scaffolding, cleanup
  - Multi-substrate AI review before BUILD surfaced missing Phase 0 prerequisites and one phase collapsed into another
  - Visual-test cycle between phases contained bugs like Phase 4.A physics provider relocation bug
applicability_triggers:
  - CC drafting phase decomposition for invasive architectural refactor
  - CC evaluating per-phase acceptance gate (measurable, behavioral, structural)
  - CC assessing whether a phase should split further mid-BUILD
mechanism_details:
  - Acceptance gates mixed: measurable (test count green, type-check pass), behavioral (focused-lane gameplay unchanged), structural (single shared physics world in place)
  - Phase 4 split into 4.A physics architecture / 4.B placeholder replacement / 4.C background simulation / 4-full-gate
  - Companion to Posts 41 and 42 explaining design-arc-then-BUILD-execution context
cross_refs:
  - Post 0041 architectural lock cycles
  - Post 0042 multi-lane bowling BUILD day
  - Post 0044 bowler bug deep dive (Phase 4.A bug)
-->

# 7-phase architectural refactor decomposition: how to ship invasive changes without breaking flow

**Author:** Jimmy McColery
**Date:** 2026-05-27
**Status:** Methodology lesson from a single 7-phase refactor; n=1, suggestive not conclusive on generalization beyond this refactor class

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

Invasive refactors fail one of two ways. They get rushed, which introduces bugs that take longer to fix than the refactor itself. Or they get bogged down, accumulating so much context that progress stalls and the half-done state becomes load-bearing while you debate whether to ship or revert. Both failure modes burn time differently but they burn it.

The trick I used for a recent multi-lane refactor in a bowling-alley tycoon sim I'm building was a written pre-refactor design proposal that decomposed the work into seven discrete commit-sized phases, each with its own acceptance gate. Posts 41 and 42 in this repo cover the design-arc-then-BUILD-execution context end-to-end. This post is about the decomposition pattern specifically: what the 7 phases looked like, why per-phase acceptance gates matter, and the visual-test cycle that ran between phases to contain bugs to the phase that introduced them.

## The pattern

Pre-refactor, I wrote a sub-design proposal that named the refactor's scope, identified the architectural shifts each phase would require, and stated an acceptance gate for each phase. The acceptance gate was the answer to "how do I know this phase actually shipped what it was supposed to ship, without breaking anything downstream." Some gates were measurable (test count must stay green; type-check must pass); some were behavioral ("focused-lane gameplay unchanged"); some were structural ("single shared physics world architecturally in place"). The combination forced me to name what each phase was for, before any source code committed to a decision that would need to be undone if the phase turned out wrong.

The proposal went through a multi-substrate AI review process before BUILD work began. That review surfaced ambiguities in the gate definitions, missing prerequisite work (a Phase 0 of pure pre-refactor utilities that needed to land before any state-shape changes), and one phase that the original draft had collapsed into another (the multi-physics-lane full-acceptance-gate work that splits cleanly from the statistical-lane visual rendering it depends on). The proposal ratification produced a 7-phase decomposition that I trusted enough to execute against without re-litigating during BUILD.

## The seven phases

The decomposition for this specific refactor produced phases shaped like this:

- **Phase 0: prerequisites.** Pure pre-refactor utilities. Zero behavioral change target. Refactor existing code into shapes the multi-lane phases will need (extract a factory function from a module constant; convert an imperative reducer to a pure function returning a delta) without changing any external behavior.
- **Phase 1: module split.** Extract pure logic plus types plus spatial constants from an existing state store into a sibling pure-logic module. The state store keeps Zustand orchestration; pure logic moves out for testability and reusability.
- **Phase 2: state shape transition.** Replace the single-entity state shape with a `Record<string, EntityState>` keyed by entity ID. Update all consumer components to entity-aware access patterns. The acceptance gate: single-entity behavior preserved at first focused entity.
- **Phase 3: scene-tree architecture.** Per-entity scene rendering. Context for entity ID passing. Visual placeholders for non-focused entities. The acceptance gate: focused entity renders identically to pre-Phase-3 state.
- **Phase 4: subsystem migrations.** This phase split further into 4.A (physics architecture refactor), 4.B (placeholder replacement with decorative rendering), 4.C (background simulation orchestrator), and 4-full-gate (multi-entity simultaneous rendering with cross-entity isolation). Each sub-phase committed independently.
- **Phase 5: test scaffolding.** Add the unit tests that gate the atomicity invariants the refactor depends on. The acceptance gate: test coverage exists at the per-entity state transition layer.
- **Phase 6: next-cycle prerequisites kickoff.** Optional. Identify what the next refactor cycle will need that this one didn't ship. Not BUILD-complete blocking.

The phase shapes generalize. The Phase 0 prerequisite pattern works whenever an invasive refactor needs preparatory utility extraction. The Phase 1 module-split pattern works whenever state-management code has accreted pure logic that wants to live separately. The Phase 2 state-shape transition pattern works whenever a single-entity shape needs to scale to multiple entities. The "Phase 4 splits further" pattern works whenever a phase turns out to have internal substructure during execution.

## Acceptance gates per phase

Each phase had a stated acceptance gate. Examples from the actual decomposition:

- Phase 0: "Full vitest suite passes unchanged. No behavioral observable in browser changes."
- Phase 2: "Single-lane behavior preserved at first V1 lane (the focused one). Test count green. Type-check passes."
- Phase 4.A: "Single shared Physics world architecturally in place. Focused lane gameplay unchanged."
- Phase 5: "Test coverage gates atomicity preservation plus collision-group encoding correctness. 41 new tests passing."

The gate is the answer to "what would tell me this phase isn't done yet?" If the gate doesn't pass, the phase isn't done, regardless of how many commits or how much time went into it. Gates that are too loose let phases drift; gates that are too strict force scope creep into a phase that should ship. The right gate names a structural property the phase exists to establish, plus a verification that establishes the property held.

## The visual-test cycle

After each phase committed, I'd run the dev server in a browser and exercise the focused-entity behavior. The exercise was a fixed sequence: trigger the work that the entity is supposed to do, verify the visual output matches expected, verify the state transitions matched expected. If the visual test caught something off, I'd diagnose in conversation, apply a fix, commit the fix as part of the same phase, re-run the visual test, then move to the next phase.

The cycle caught one substantial bug during the Phase 4.A sub-phase. A focus-cycle keystroke sequence produced a state where a kinematic mesh appeared at the wrong world coordinates. Took three fixes to fully resolve. The first fix solved a Zustand subscribe default-semantics issue; the second solved a handler that was a no-op for one of the entity states; the third forced clean React remount via a key prop to eliminate the entire interaction class. Each fix lived in its own commit because the phase-decomposition discipline contained the bug to its own phase rather than letting it compound across phases.

The bug would have shipped past Phase 4.A and surfaced later if the per-phase visual test hadn't run. Catching it inside its own phase meant the diagnosis was contained: I knew the symptom had appeared in this phase, not three phases ago, so I could focus the investigation on what this phase had changed. The diagnosis took one focused conversation; catching the same bug three phases later would have meant disentangling the symptom from intervening changes, plus likely fixing it under the pressure of "but the next phase already builds on this."

## What happens when you skip phases

The anti-pattern is one big merge: commit everything as a single squashed change after running the full test suite at the end. The anti-pattern fails three ways when the refactor is invasive.

First, the verification gate at the end isn't structural. A green test suite plus a working browser session means "no obvious regression at this scope right now," but it doesn't establish the per-phase architectural properties the refactor was supposed to establish. You can't tell from the end state whether the physics-world relocation worked because the structural property was achieved, or because some other accidental factor made it look like it did.

Second, when something does break, the bisect surface is the whole refactor. If the visible bug surfaces under a keystroke sequence the end-of-merge test didn't cover, the bisect window is hundreds of file changes instead of one phase's worth. Diagnosis cost compounds against the merge size.

Third, the bog-down failure mode kicks in once context accumulates. The half-done state has enough load-bearing pieces that reverting the merge means losing real progress, but committing the merge means committing a refactor that hasn't been verified at its structural-property layer. The decision becomes "ship the bog-down" versus "lose the work," and neither option is good.

## Why this pattern generalizes

The 7-phase decomposition isn't specific to game-sim or React Three Fiber work. The same shape applies to invasive refactors in other contexts:

- Database migrations decompose into prerequisite-utility-extraction plus schema-shape-transition plus consumer-component-migration plus data-backfill plus verification scaffolding. Each phase committable; each phase with an acceptance gate (read traffic still works; write traffic still works; data integrity holds).
- API rewrites decompose into request-shape-prerequisites plus internal-logic-extraction plus public-surface-replacement plus consumer-call-site-migration plus deprecation-removal. Each phase verifiable independently.
- Framework upgrades (React major-version bumps, build-tool migrations) decompose into prerequisite-utility-extraction plus configuration-shape-transition plus per-module migration plus test-scaffolding for the new shape. Each phase reversibly small.

The common shape across these contexts: pre-refactor design discipline plus phase decomposition plus per-phase acceptance gates plus verification cycle between phases. The discipline is invariant; what changes is the per-context phase content and the per-context acceptance criteria. The 7-phase number is incidental to the specific refactor I ran; the count would scale up or down based on refactor scope. What matters is that each phase is committable independently, each phase has an acceptance gate, and verification runs between phases not just at the end.

## What I'm not claiming

- I'm not claiming 7 is the magic number of phases. The decomposition granularity depends on refactor scope. The right phase count is "as many as needed for each phase to be reversibly small with a clear acceptance gate"; for this specific refactor that was 7.
- I'm not claiming pre-refactor written design proposals are always worth the time cost. Some refactors don't need this overhead. The discipline pays off when the refactor is invasive enough that the cost of getting an early phase wrong compounds across later phases. Local refactors (one feature; no cascading state changes; one-file scope) usually don't benefit.
- I'm not claiming this pattern fires equally well solo versus on a team. I've only fired it solo, with multi-substrate AI orchestration providing the pre-refactor review pass. A team could fire the same pattern with peer review or design-doc review playing the role the AI substrates played for me; whether the discipline-versus-overhead ratio works out differently in a team context is a question I haven't tested.
- I'm not claiming AI-substrate ratification of the design proposal is required. It was helpful for catching ambiguities in my gate definitions and surfacing the Phase 0 prerequisite work I'd originally missed. But the BUILD-time discipline (commit per phase; visual-test between phases; bug-fix in the phase that introduced the bug) is what produced the speed, not the substrate ratification of the proposal.

## What I am claiming

When a refactor is invasive enough to feel risky, breaking it into N reversible commits with per-N acceptance gates and operator-side verification cycles between commits is faster overall than the more common "one big merge" alternative. The discipline that enables shipping invasive refactors fast is the discipline of breaking work into small reversible commits with verification gates.

The pattern's load-bearing pieces are three: pre-refactor written design proposal that names per-phase acceptance gates before any source code commits; per-phase commit discipline that contains each phase's work to its own reversible unit; verification cycle between phases that catches bugs at the smallest possible blast radius. Each piece does something the others don't. The proposal forces naming what each phase is for before getting into the work, which surfaces ambiguities while they're still cheap to fix. The per-phase commits make reversal possible without losing intermediate progress. The verification cycle catches bugs in the phase that introduced them, which contains diagnosis cost.

The standing empirical claim is one 7-phase refactor that produced a 40-commit BUILD day with zero broken-main commits. n=1 on the pattern at this refactor scale. Whether other operators running other invasive refactors under similar phase-decomposition discipline produce similar outcomes is the standing empirical extension. The pattern's shape generalizes to other contexts (database migrations; API rewrites; framework upgrades) under the same architectural argument, but those generalizations are descriptive of how the pattern would apply, not empirical evidence that it has applied successfully outside the one fire this post documents. Counter-narrative to "ship fast equals skip design"; the discipline that produces shipping speed at invasive-refactor scale is the discipline of breaking work into small reversible commits with verification gates.
