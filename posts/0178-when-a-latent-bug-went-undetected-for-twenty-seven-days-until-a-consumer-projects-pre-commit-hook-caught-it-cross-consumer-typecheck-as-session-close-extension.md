<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0178
title: When a Latent Bug Went Undetected for Twenty-Seven Days Until a Consumer Project's Pre-Commit Hook Caught It Cross-Consumer Typecheck as Session-Close Extension
date_published: 2026-07-06
status: published
superseded_by: none
domain: framework-methodology
project_scopes: sim-ai open-alley street-code cross-cutting
cc_task_relevance: pre-commit-hook-discipline cross-consumer-typecheck latent-bug-detection sub-shape-22-strengthening session-close-discipline-extension
phase_binding: era-independent
discipline_family: sub-shape-22-architectural-extension-awareness cross-consumer-typecheck-candidate-methodology-observation session-close-discipline-7th-stage-candidacy
canonical_rule: pre-commit-typecheck-discipline
load_bearing_claims:
- Sim-ai LandmarkEvent field-name mismatch shipped at Phase 3.2-D H-NEW-2 Q56 a7Memory tick loop integration on 2026-07-05 evening commit 05b843b silently degraded landmark memory encoding to baseValenceImpact zero for twenty-seven days
- Discovery pathway was an unrelated post-Phase-11 loose-end sweep polish_queue Item 353 commit at Open Alley whose pre-commit hook runs tsc against aliased sim-ai code and surfaced eight typecheck errors including the three landmark field-name references
- Sim-ai has NO pre-commit hook while Open Alley DOES have one running full typecheck creating asymmetric bug-detection surface where consumer's stricter enforcement catches upstream bugs the direct project silently accepts
- Fix path shipped landmarkValenceSign helper mapping LandmarkEventType to signed valence (exposure_crisis negative-valence; others positive) plus corrected all three field references (subjectSimId to actorSimId + type to eventType + valenceImpact to affectiveMagnitude scaled by sign map)
- Framework methodology observation cross-consumer-typecheck-as-latent-bug-detection-surface candidate discipline filed for Council #9 Item 12 review with n=1 empirical foundation
- Fire n+3 within-Phase-3 for sub-shape 22 architectural-extension-awareness discipline (Post 0168 origination + Post 0174 within-session recurrence at a7Memory Phase 3 extension surface + this post at a7Memory landmark-encoding surface twenty-seven-day-latent recurrence)
- Prevention actions shipped at Phase 12 Item 1 include sim-ai pre-commit hook installation matching Open Alley pattern via scripts/install-hooks.sh plus package.json typecheck script plus CLAUDE.md documentation of the hook plus fix of five additional latent typecheck errors surfaced by the newly-installed hook (state.simB null assertion + IslandWorldState type widening on fires field + IslandWorldState type on E-emotionality test + node types reference on measurePhaseDEmpirical script)
- Full test suite 863 of 863 pass post-fix confirming landmark memory encoding correctness restoration and hook installation
applicability_triggers:
- Any sim-ai commit event now runs pre-commit typecheck automatically
- Any ecosystem substrate authoring event should verify pre-commit hook presence at direct project matching consumer discipline
- Any Rule 20 Family A sub-shape 22 architectural-extension-awareness event at future architectural extension surfaces
- Any session-close discipline evaluation event at ecosystem-substrate-scope should include cross-consumer-typecheck verification or direct-project-pre-commit-typecheck presence
- Any Council 9 review event evaluating cross-consumer-typecheck-candidate-methodology-observation Item 12 filed via this post
mechanism_details:
- Sim-ai pre-commit hook two-section structure section A local-only guard rejecting commit if any remote configured plus section B npm run typecheck aborting commit on any tsc error
- landmarkValenceSign helper function maps LandmarkEventType enum literals to signed integer with exposure_crisis returning -1 and shelter_built + fish_caught + storm_survived returning +1
- Signed valence formula sign multiplied by affectiveMagnitude computed at each memory encoding site (two sites total covering Sim A perspective and Sim B perspective within processMemoryTickPipeline function)
- Cross-consumer typecheck asymmetric discovery pattern activates when direct project lacks pre-commit typecheck hook while consumer project has one and consumes direct-project code via path alias tsconfig configuration; consumer's tsc run against aliased view surfaces errors direct project silently accepts
- Session-close 7th stage candidacy extends Council #8 canonized 6-stage discipline (canonical-file freshness + memory authorship + deployment vs shipped + deployment vs build completion + load-bearing audit + count-ledger n>3) with new stage validating direct-project pre-commit hook presence OR cross-consumer typecheck completion before session close
- Sub-shape 22 empirical foundation strengthens from n=1 (Post 0168 origination Phase 3 mechanical layer) to n+2 (Post 0174 within-session recurrence at a7Memory tick loop integration) to n+3 within-Phase-3 (this post twenty-seven-day-latent recurrence at a7Memory landmark-encoding surface)
- Prevention hook installed at .git/hooks/pre-commit via idempotent scripts/install-hooks.sh script; hook execution ~1-2 seconds total wall-clock keeping commit latency negligible
cross_refs:
- Post 0168 (Extended-verification as third-layer discipline; sub-shape 22 architectural-extension-awareness ORIGINATION)
- Post 0174 (Sub-shape 22 within-session recurrence at a7Memory Phase 3 extension; strengthens to n+2 within-Phase-3)
- Post 0175 (Council #8 canonization outcome + Rule 22 verify-against-canonical-files + Session-close discipline extension to 6 stages)
- Post 0177 (Phase 11 nine-item comprehensive integration arc; loose-end sweep that triggered this discovery)
- Memory file feedback_verify_against_canonical_files.md
- Memory file project_phase_11_nine_item_research_to_code_integration_shipped_2026-07-06.md
- Council #9 review agenda draft Item 12 candidate methodology observation
- Sim-ai scripts/install-hooks.sh
- Sim-ai .git/hooks/pre-commit
-->

# When a Latent Bug Went Undetected for Twenty-Seven Days Until a Consumer Project's Pre-Commit Hook Caught It Cross-Consumer Typecheck as Session-Close Extension

**Author:** Jimmy McColery
**Date:** 2026-07-06
**Status:** PUBLISHED. Methodology finding documenting a twenty-seven-day-latent LandmarkEvent field-name mismatch bug at sim-ai that silently degraded landmark memory encoding to baseValenceImpact zero across Phase 3.2-D H-NEW-2 Q56 a7Memory tick loop integration since 2026-07-05 evening ship. Bug caught only when unrelated post-Phase-11 loose-end sweep at Open Alley invoked a polish_queue Item 353 commit and Open Alley's pre-commit hook ran typecheck against aliased sim-ai code surfacing the errors. Prevention actions shipped: sim-ai pre-commit hook installation matching Open Alley discipline plus five additional latent typecheck errors fixed plus Council #9 Item 12 candidate methodology observation filed for cross-consumer-typecheck discipline.

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*


A latent bug in the sim-ai canonical shared substrate went undetected for twenty-seven days before it was caught by an unrelated pre-commit hook at a consumer project. This post documents the incident, the discovery pathway, the prevention actions shipped, and the framework methodology observation that emerged: cross-consumer-typecheck-as-latent-bug-detection-surface as candidate session-close discipline extension for ecosystem-substrate-scope projects.

## The bug

Sim-ai's processMemoryTickPipeline function at `src/sim-ai/worlds/island/islandWorld.ts` encoded landmark events into per-Sim three-horizon memory (Layer 4 in the ten-layer NPC architecture) using field references that did not exist on the LandmarkEvent schema. The code read `landmark.subjectSimId` where the schema defines `actorSimId`, `landmark.type` where the schema defines `eventType`, and `landmark.valenceImpact` where the schema defines `affectiveMagnitude`. TypeScript would have flagged these as errors, but sim-ai had no pre-commit hook running typecheck at commit time and I never invoked tsc manually against the direct project during Phase 3.2-D through Phase 11 commit landings. The errors silently degraded landmark memory encoding to `baseValenceImpact = 0` (via nullish-coalescing fallback) for every landmark event fired across twenty-seven days of framework work spanning Phases 3.2-D through 11.

The semantic impact was worse than a simple constant-zero degradation. LandmarkEvent's `affectiveMagnitude` is documented as an unsigned 0-100 scale magnitude, but the consuming code expected a signed valence. The `exposure_crisis` landmark type is a negative-valence survival distress event that should encode with negative valence trace; instead it encoded at zero valence like every other landmark type. Landmark memory traces across the entire framework state were therefore uniformly non-informative across Phase 3.2-D empirical validation, Phase 10 Sofroniew audit runtime validation, Phase 11 empirical differentiation study, and every intermediate session that ran the tick loop.

## The discovery pathway

The discovery came via an unrelated arc. Post-Phase-11 loose-end sweep at the-street-code produced a polish_queue Item 353 entry at Open Alley documenting the Item 0334 consultant workflow gate for sim-ai Phase 11 schema-reserved registries. When I invoked `git commit` on the polish_queue.md mutation at Open Alley, Open Alley's pre-commit hook ran `npm run typecheck`. The typecheck ran full tsc across Open Alley source AND the tsconfig-aliased sim-ai substrate consumed via the `sim-ai/*` path alias. That typecheck surfaced the LandmarkEvent field-name errors at sim-ai lines 1338, 1341, 1343, 1344, 1384, 1386, 1388, and 1389 alongside a few additional pre-existing errors in test files and a scale measurement script.

The critical observation is that the pre-existing errors had been visible to any manual tsc invocation at sim-ai for weeks — but no manual invocation had been made because sim-ai had no pre-commit hook enforcing it. Every Phase 3.2-D, Phase 10, and Phase 11 commit landed with the errors intact. Only Open Alley's pre-commit typecheck, running as a side effect of an unrelated hygiene commit, caught them.

## Sub-shape 22 architectural-extension-awareness fire n+3 within-Phase-3

The framework's Rule 20 Family A sub-shape 22 discipline (Post 0168 origination; Post 0174 n+2 within-session strengthening at Q56 a7Memory tick loop integration) addresses the pattern where framework code extends across a new architectural surface without extending awareness across the full extension surface. Sub-shape 22 fires when the extension surfaces at multiple architectural sites but only some sites get the propagation.

The LandmarkEvent field-name mismatch is a fire of sub-shape 22 at n+3 within Phase 3. Q56 a7Memory tick loop integration extended memory encoding to landmark events as one of two encoding pathways (action-completion encoding + landmark-event encoding). The action-completion encoding pathway used the ActionHistoryEntry schema correctly. The landmark-event encoding pathway consumed LandmarkEvent with wrong field names because the pathway's author (me at 2026-07-05 evening) referenced remembered field names rather than reading LandmarkEvent schema at consumption site. Sub-shape 22's specific architectural-extension-awareness gap is: when extending memory encoding across a new event source type, verify the source event schema's actual field names at the consumption site rather than assuming remembered names carry over.

Sub-shape 22 empirical foundation trajectory: n=1 Phase 3.2-D H-NEW-1 origination (Post 0168) → n+2 within-session recurrence at Q56 a7Memory Phase 3 extension (Post 0174) → n+3 within-Phase-3 twenty-seven-day-latent recurrence at Q56 a7Memory landmark-encoding surface (this post).

## Cross-consumer-typecheck candidate methodology observation

The discovery pathway makes the case for a framework methodology observation not previously canonized. When a direct project A lacks a pre-commit typecheck hook and a consumer project B has one, and B consumes A via tsconfig path alias, then B's pre-commit typecheck runs against A's aliased view and surfaces errors A silently accepts. B's typecheck is A's implicit lint. This asymmetric bug-detection surface is a real discipline observation with a concrete prevention action (either install pre-commit typecheck at A OR canonize cross-consumer typecheck run before session close as a step).

The empirical foundation for canonization currently sits at n=1 (this incident). Council #9 Item 12 is filed to accumulate additional fires (or non-fires) over the 60-90 day window and adjudicate whether the pattern promotes to canonical discipline or remains as filed observation. The candidate promotion path is one of two options: (1) canonize as Session-Close 7th Stage extension per Council #8 discipline extension precedent adding cross-consumer-typecheck-OR-direct-project-pre-commit-hook-presence check; (2) canonize as Rule 20 read-side sub-shape at architectural-substrate-project-lacks-typecheck-enforcement gap.

## Prevention actions shipped

Phase 12 comprehensive execution alongside this post shipped:

1. Sim-ai pre-commit hook install script at `scripts/install-hooks.sh` following the Open Alley two-section pattern (local-only guard + typecheck). Idempotent; safe to run after fresh clone or after unrelated `.git/hooks/` mutation.
2. Sim-ai `package.json` new script `"typecheck": "tsc --noEmit"` matching the ecosystem convention.
3. Fix of the LandmarkEvent field-name mismatches at both consumption sites in processMemoryTickPipeline with new `landmarkValenceSign` helper mapping `LandmarkEventType` to signed integer (-1 for `exposure_crisis`, +1 for others) so `signedValence = sign * affectiveMagnitude` computed correctly. Landmark memory encoding now produces intended signed valence traces for the first time since Q56 shipped.
4. Fix of five additional latent typecheck errors surfaced when the newly-installed pre-commit hook ran the first time. Errors were: `state.simB` null-assertion needed at phase210Kindness.test.ts line 440-441; explicit `IslandWorldState` type on `noFireState` and `withFireState` at phase30Fire.test.ts lines 220-221 so the `fires` field widens correctly; explicit `IslandWorldState` type on `sHighE` and `sLowE` plus `IslandWorldState` import at phase3AuditSimBBehavior.test.ts lines 299-300; and `/// <reference types="node" />` triple-slash directive at scale/measurePhaseDEmpirical.ts for `process.version` and `process.platform` references.
5. CLAUDE.md at sim-ai updated to document the pre-commit hook + install pathway + bypass discipline.
6. Council #9 review agenda Item 12 filed for cross-consumer-typecheck-candidate-methodology-observation with n=1 empirical foundation and 60-90 day review window.

Full test suite 863 of 863 pass post-fix confirming both the landmark memory encoding correctness restoration and the pre-commit hook installation.

## Framework state observation

The framework's iterative-narrow-ship discipline (Post 0166 canonization at n=7) plus operator-realism-check discipline (Post 0170 canonization at n=8; Council #8 Rule 21 canonization) plus post-audit-correction discipline (Post 0167 origination; Council #8 Rule 24 canonization) all address discipline gaps at post-authoring or post-publication scope. Sub-shape 22 addresses the architectural-extension-awareness gap at consumption-site scope. The cross-consumer-typecheck candidate methodology observation addresses a distinct scope not previously canonized: the direct-project-typecheck-enforcement-absence gap at ecosystem-substrate scope.

The Phase 10 through Phase 12 arcs (twelve items across three comprehensive-arc mornings) surfaced this incident as the twenty-seven-day-latent tail of Q56 a7Memory shipping. Future ecosystem substrates should install pre-commit typecheck hooks at direct-project scope from day one to eliminate the twenty-seven-day-latent tail entirely; the framework's local-only-repo discipline (no remote, no CI) makes pre-commit the sole enforcement surface, so its absence is architecturally load-bearing.

Council #9 review will adjudicate whether the cross-consumer-typecheck observation promotes to canonical discipline based on evidence accumulated across the 60-90 day window. If additional fires accumulate (either latent bugs caught by cross-consumer typecheck at other ecosystem substrates or missed at other substrates lacking cross-consumer coverage), the case for canonization strengthens. If no additional fires accumulate, the observation may deprecate as accidental incident under Council #8 falsification-clause meta-canonization discipline.
