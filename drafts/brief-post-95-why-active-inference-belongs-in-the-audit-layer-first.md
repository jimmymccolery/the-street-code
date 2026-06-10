# Drafting brief — Post 95 "Why Active Inference Belongs in the Audit Layer First"

**Status:** Brief only; not yet drafted. NEW brief 2026-06-10 PM per Round 7 R5 design.
**Target slot:** Post 95 within Posts 89-96 retraction block. Per R5 design: explains tractability risk + prototype-first sequencing.
**Scope verdict:** SAFE — methodology + Friston-active-inference citations + implementation analysis. No protected scope.
**Length target:** 3000-4500 words per R5 design.

## Thesis

Active inference is the mathematical apparatus Modified-C-bis uses to ground its NPC decision-making mechanism. Round 7 R5 surfaced a sharpened operationalization recommendation: even under Path A operator ratification (sophisticated active inference promoted to V1; Round 8 ratification 2026-06-10 PM), the safest sequencing is **active inference in the AUDIT layer first, runtime layer second**. The audit-layer use analyzes NPC decisions after-the-fact using the active-inference apparatus to detect whether decisions match the framework's structural-only-position-(a) discipline. The runtime-layer use drives the NPC's actual decisions during play. The audit layer can ship at lower computational cost (offline analysis; per-decision rather than per-frame); the runtime layer requires the 4-audit mandatory test surface + horizon-bound + state-space-content discipline operative in real-time. Post 95 explains why prototype-first sequencing is the right risk discipline + how the framework operationalizes "audit first" vs "runtime first."

## Sections (outline)

1. **Hook:** "Modified-C-bis uses active inference for NPC decision-making. The tempting move is: ship it as the runtime. The disciplined move is: ship the audit layer first + earn the runtime promotion in V1.x."

2. **What active inference does for NPCs.** Brief recap (1-2 paragraphs) of position-(a) structural-only sophisticated active inference per Modification 6 Amendment Round 8 Revision (state-space-content boundary; not horizon-depth). The NPC scores candidate actions by expected free energy; the action with lowest EFE is selected. Naive inference for V1 cost (single-step EFE); sophisticated inference for Phase 8.x → V1 critical-path under Path A ratification.

3. **The tractability risk at 88-NPC scale.** Walk through the arithmetic:
   - 88 NPCs × ~10 decisions/game-minute × 60 game-minutes/game-hour × ... = ~tens of thousands of EFE evaluations per game-hour
   - Sophisticated inference adds recursive belief-about-belief evaluation (per Friston 2017 Appendix F + Friston 2021)
   - Even with τ ≤ 3 horizon bound (Round 8 R3 spec; secondary defense-in-depth), per-decision compute grows
   - At iOS V1 target framerate (~30 fps), per-frame budget tightens further

4. **The audit-layer use of active inference.** Define it clearly:
   - NPCs make decisions via cached/heuristic policies during runtime (cheap; predictable per-frame budget)
   - At consolidation boundaries (yearly pass per Post 94) OR at developer-triggered audit points, run active-inference apparatus offline to evaluate whether the NPC's cached-policy choices align with the position-(a)-compatible EFE-minimization the framework's discipline commits to
   - Flag deviations for designer review (a regular bowler suddenly tipping outside expected pair-sentiment trajectory; might indicate cached-policy stale)
   - This is the use case where active inference earns its theoretical complexity by being a CHECK rather than a DRIVER

5. **Why audit-first is the safer sequencing.**
   - Audit layer can ship with fewer operational risks (offline; no per-frame cost; failures don't crash gameplay)
   - Provides empirical data on whether NPCs actually need sophisticated-inference scoring at all (maybe cached policies suffice for the V1 1950s baseline)
   - Buys time for the 4-audit mandatory test surface to mature before sophisticated inference is in the player-facing path
   - Lets the operator publish posts about active inference (Posts 89-104) without claiming runtime-deployed sophisticated inference until empirically warranted

6. **The Path A operator ratification context.** Operator ratified Path A 2026-06-10 PM ("most comprehensive solution"). Path A promotes sophisticated active inference + structural-only self-reflection to V1 critical-path. The audit-first sequencing is compatible with Path A: it sequences the IMPLEMENTATION, not the RATIFICATION. Sophisticated inference is still committed to V1 (per Path A); audit-first means it lands in the audit layer V1.0 + earns its way to runtime promotion in V1.x based on test data.

7. **The 4-audit mandatory test surface.** Recall from Round 8 R4 Section 4 + the Modification 6 Amendment Round 8 Revision:
   - State-Space Content Audit (PRIMARY): generative model tensor enumeration; no cross-era self-identity variable
   - Amnesia Re-initialization Test (MANDATORY): zero-history reset returns era-baseline behavior
   - Markov-Blanket Isolation Test: NPC recursive belief-updating doesn't read player-side narrative state
   - Horizon Bound τ ≤ 3 (SECONDARY): defense-in-depth, not boundary itself

   These four audits are themselves audit-layer apparatus. Running them is exactly the audit-layer use case Post 95 advocates for.

8. **Honest scope: what audit-first doesn't solve.**
   - It doesn't solve the "is sophisticated inference even necessary for V1 game-feel" question (empirically open until tested)
   - It doesn't solve the marketing-copy discipline (Trigger 2 phenomenal-claim-leakage risk applies regardless of audit-vs-runtime)
   - It doesn't reduce the cross-cultural disclosure exposure (still 5-element discipline applies)

9. **Round 9 generative-model formalization arc connection.** Post 95 closes by noting Round 9 (NPC generative-model formalization; trigger satisfied 2026-06-10 PM; V1-BUILD-blocking under Path A) will spec the audit-layer + runtime-layer pairing concretely. The audit-first sequencing recommendation is operational-discipline-level; the formalization arc translates it to math.

10. **Closing.** Active inference is too theoretically powerful to ship as runtime by default. Audit-first earns the runtime promotion empirically. Honest sequencing > tempting moves.

## Key citations

- **Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., & Pezzulo, G. (2017).** Active inference: A process theory. *Neural Computation* 29(1):1-49. Appendix F pp. 42-43.
- **Friston, K., Da Costa, L., Hafner, D., Hesp, C., & Parr, T. (2021).** Sophisticated Inference. *Neural Computation* 33(3):713-763.
- **Bowers, J. S., & Davis, C. J. (2012).** Bayesian just-so stories. *Psychological Bulletin* 138(3):389-414. (Falsifiability anchor for why audit-first is safer than runtime-first.)
- **Colombo, M., & Wright, C. (2021).** First principles in the life sciences. *Synthese* 198(Suppl 14):3463-3488. (Process-theory-not-principle anchor.)

## Cross-links

- LINKS BACK TO: Post 89 (retraction table — "no naive active-inference runtime" was one of the V1 corrections)
- LINKS FORWARD TO: Post 96 (V1 NPC memory spec includes audit-vs-runtime sequencing) + Posts 97-99 (hybrid path includes cached-policies + slow-consolidation = audit-first compatible)
- IMPLEMENTATION TIE: Round 9 formalization arc Q4 EFE decomposition specifies audit-vs-runtime apparatus

## Drafting prerequisites

- Operator-side direct read of Friston 2017 Appendix F pp. 42-43 (~30 min; F-14 RESOLVED via R8 R2 + R4).
- Operator-side read of Friston 2021 *Sophisticated Inference* (~6-10h; Path A prerequisite).
- Brief read of Bowers & Davis 2012 falsifiability critique (~1h; informs the audit-first defense vs unfalsifiable-runtime concern).

## Hour estimate

At observed velocity: ~5-7 hours drafting + revision pass + audit-vs-runtime architecture clarification. Target 3000-4500 words.
