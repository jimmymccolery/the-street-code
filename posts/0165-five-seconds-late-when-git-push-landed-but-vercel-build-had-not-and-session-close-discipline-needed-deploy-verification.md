# Five Seconds Late: When Git Push Landed But Vercel Build Had Not, and Session-Close Discipline Needed Deploy Verification

**Author:** Jimmy McColery
**Date:** 2026-07-04
**Status:** Single-finding arc documenting the framework's canonization-propagation gap discipline family reproducing at a distinct 18th sub-shape 2026-07-04 latest evening; deployment-vs-build-completion timing gap where push succeeded but Vercel deployment had not yet completed when operator empirically tested; distinct from prior 17th sub-shape (deployment-vs-shipped-code where commits were not pushed); session-close discipline extension proposal to add build-completion verification via GitHub deployments API as a mandatory 6th stage

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I'm a solo indie developer running a personal AI-discipline framework across multiple projects, some of which deploy to Vercel through GitHub. This post documents a specific empirical finding from Phase 2.7-A shipping arc 2026-07-04 latest evening: the framework's canonization-propagation gap discipline family reproduced at a new sub-shape that is distinct from the prior 17th sub-shape and warrants explicit session-close discipline extension.

The prior 17th sub-shape (canonized earlier the same day 2026-07-04) documented a case where CC declared session close complete based on local test suite passing and vendor sync complete, but the underlying commits had not been pushed to origin/main. Operator's empirical test against the deployed URL (Vercel) ran on pre-shipped code because the deployed code was multiple commits stale. Fix-forward was `git push origin main` and session-close discipline extension proposed the check `git rev-list --count origin/main..HEAD == 0` as verification.

The 18th sub-shape (this fire) is distinct. Commits WERE pushed. The check `git rev-list --count origin/main..HEAD == 0` would have passed. But Vercel had not yet completed its build-and-deploy cycle when I started empirical testing. My empirical test ran on the previous deployed sha even though the current-target sha was pushed. The gap was 5 seconds between session export and Vercel deployment success.

This is not the same failure family as the 17th sub-shape. Both live under the canonization-propagation gap discipline umbrella but they operate at different failure mechanisms. This post documents the distinction, the empirical evidence, and the discipline extension.

## The specific timing gap

The Phase 2.7-A sleep-storm interrupt design phase produced sim-ai commit `17fa31f` (framework code) and RoomToLife vendor sync commit `317aa21`. Both commits landed via git push around 04:55Z. CC declared the fix live and told me it was ready to test with the message "Pushed. Vercel picks up sha `317aa21` in ~30s."

I started empirical testing at approximately 04:55:10Z. The session ran for 25 seconds at 100x speed producing 2308 log entries. Session export completed at 04:55:35Z.

Vercel deployment for sha `317aa21` completed at 04:55:40Z per GitHub deployments API. State: success.

My session was exported 5 seconds BEFORE the deployment completed. Vercel's deployment for sha `317aa21` was created at 04:55:40Z, meaning Vercel had received the push webhook and started the build+deploy cycle but had not completed it when I started testing. The deployed URL that the session ran against was serving the previous sha `3a56cea` for the entire session duration.

The failure surfaced empirically. The session log I analyzed showed Sim A sleeping 293 straight ticks through her own exposure death, which is the exact pre-Phase-2.7-A failure mode. Phase 2.7-A's fix was to interrupt open-air sleep during storm; if the fix had been running, we would have observed sleep interrupted at tick 1691 (one tick after sleep started during storm). Instead we observed the pre-fix failure mode.

A follow-up session 4 minutes later (after Vercel deployment had fully completed) confirmed Phase 2.7-A firing correctly. Sim A slept 1 tick then interrupted, as designed.

The empirical evidence for the timing gap is unambiguous. The first session ran against pre-Phase-2.7-A code because Vercel had not yet finished building the fix. The second session ran against Phase-2.7-A code because Vercel had finished by then.

## Why this is distinct from the 17th sub-shape

The 17th sub-shape's failure mechanism: session close declared complete without pushing commits; deployed code was stale by N commits. The recurrence-prevention discipline: check `git rev-list --count origin/main..HEAD == 0` before declaring session close complete. If N is nonzero, push before declaring complete.

The 18th sub-shape's failure mechanism: session close correctly pushed commits; but Vercel had not completed its build-deploy cycle at the moment CC declared the fix testable. The 17th sub-shape's recurrence-prevention would PASS this case (N is zero; commits ARE pushed) while the failure still occurs (deployed code is stale not by commits-not-pushed but by build-not-yet-completed).

Both sub-shapes share the underlying pattern: operator empirical test runs against stale deployed code because CC declared the fix ready before the fix was ACTUALLY DEPLOYED. Both live under the canonization-propagation gap discipline umbrella. Both share the discipline-family observation that CC's "ready to test" declaration must be gated on the target consumer environment's actual state, not on CC's local proxies for that state.

They differ at the mechanism layer. The 17th's mechanism is push-not-executed. The 18th's mechanism is build-in-progress. Two different mechanisms; one shared failure family.

The framework's canonization-propagation gap discipline family Family A empirical foundation now sits at n=12 candidate sub-shapes across various framework layers. Each sub-shape is a scope-level or mechanism-level reproduction of the underlying failure family. The 18th sub-shape strengthens the empirical foundation by adding one more mechanism-level reproduction.

## The session-close discipline extension

The framework's canonized session-close discipline (per Council methodology deployment scope) had previously extended to five stages after the 17th sub-shape:

1. Pre-synthesis contamination register
2. Rule 14 Pattern A vs B classification
3. Orchestrator synthesis draft
4. Post-synthesis audit
5. Deployment verification via `git rev-list --count origin/main..HEAD == 0`

Stage 5 addresses the 17th sub-shape's failure mechanism. It doesn't address the 18th's.

The proposed extension to stage 6: build-completion verification via GitHub deployments API before declaring the fix testable to operator. Specifically, after `git push` succeeds, query `gh api repos/{owner}/{repo}/deployments/{id}/statuses` and confirm state equals `success` for the pushed sha. If state is `pending` or `in_progress`, wait and re-query. Only after `success` for the current-target sha should CC declare the fix ready.

The overhead per session is 30 to 60 seconds of polling. That is the length of the Vercel build-deploy cycle. The overhead is bounded because Vercel's build cycle has a hard maximum (build failure fires at some minute count). If Vercel fails the build (which does happen), CC catches it at this stage rather than at operator empirical test.

An alternative discipline extension: instead of CC polling until success, CC tells operator the pushed sha and points at the direct Vercel deployment URL (rather than the custom-domain URL) as the empirical test surface. The direct Vercel deployment URL bypasses any custom-domain CDN caching layer and points at the specific deployment. If operator uses the direct URL, timing gap becomes visible (the direct URL either responds with the pushed sha's build or 404s while the build is in progress). This alternative offloads timing verification to operator's test URL choice rather than CC's polling.

Either extension works. The load-bearing point is that CC's "ready to test" declaration must be gated on the target consumer environment's actual state. The mechanism at which the environment falls behind (push not executed at 17th; build in progress at 18th) is contextual; the discipline that catches it must apply uniformly.

## What actually shipped

The 18th sub-shape candidate was filed as a feedback memory at `~/.claude/projects/-Users-jimmy/memory/feedback_deployment_vs_build_completion_timing_gap_candidate_18th_sub_shape_2026-07-04.md`. The memory documents the empirical evidence (session log analysis + GitHub deployments API timing) and proposes the session-close discipline extension.

The Phase 2.7-A shipping arc completed correctly at the second session run (4 minutes after the first) once Vercel deployment had actually completed. Sleep-storm interrupt working as designed. Sim A sleeps 1 tick during storm; interrupt fires; decideNextAction re-runs. Empirical validation confirmed at seed=42.

The framework's canonization-propagation gap discipline family Family A empirical foundation extended from n=11 candidate sub-shapes to n=12. Approaching canonization threshold at Council #8 methodology deployment scope where the discipline family may formalize as a Rule.

Council methodology deployment session-close discipline extension proposed as new stage 6 (build-completion verification via GitHub deployments API). Whether the discipline extension formally canonizes depends on Council #8 adjudication.

## What this pattern would look like without the discipline

If session-close discipline does not extend to build-completion verification, the 18th sub-shape's mechanism recurs at every Phase-N shipping arc where operator empirically tests within 60 seconds of push. Given that CC's typical "ready to test" latency after push is under 60 seconds and operator's typical empirical test latency after "ready to test" declaration is also under 60 seconds, the window for recurrence is essentially every fast-iteration Phase-N ship.

Fast-iteration is a valuable framework methodology property. The Phase 2.7-A/B/C shipping arc shipped 3 empirical BUILD arcs in one session partly because each ship took under 30 minutes from design to deployed. Extending the ship latency by an unbounded amount (waiting for operator to verify empirically before declaring next design phase) would substantially slow the arc.

The build-completion verification extension is a bounded overhead (30 to 60 seconds per push) that doesn't slow the arc materially. It just gates the "ready to test" declaration on the actual deployed state. The narrow interpretation is that CC waits for deployment success before saying ready. The broader interpretation is that CC's proxies for deployment state (I pushed, therefore ready) are inadequate and need replacement by actual queries against the deployment platform.

## Adjacent discipline observations

The framework's Marcus Reed Protocol anti-fabrication discipline applies here in a specific way. CC's "Pushed. Vercel picks up sha `317aa21` in ~30s" declaration was technically true (push landed) but implicitly falsified against operator's empirical test (session ran on stale sha). The failure mode is not exactly fabrication (nothing false was stated) but it's within the family of confident-declarations-that-turn-out-wrong-under-empirical-verification. The recurrence-prevention discipline for both families is similar: CC's declarations must be structurally gated on the actual verifiable state of the consumer environment, not on CC's local proxies for that state.

The framework's Rule 20 canonization-candidacy Family A now has n=12 empirical fires across many framework scope levels. The pattern's canonization threshold at Council #8 methodology deployment scope is approaching. The 18th sub-shape's specific contribution is documenting a mechanism-level reproduction (build-in-progress) that is distinct from other sub-shapes' mechanism-level reproductions. Empirical foundation strengthens by mechanism diversity, not just by fire count.

## What I'm not claiming

I'm not claiming this timing gap is Vercel-specific. Any CI/CD platform with a build-deploy cycle produces the same window. GitHub Pages, Cloudflare Pages, Netlify, and internal CI-deploy pipelines all have build-in-progress states that would produce the same discipline gap.

I'm not claiming 5 seconds is the typical timing gap for Vercel deployments. This specific fire's gap was 5 seconds because I started testing very quickly after CC's "ready" declaration. Vercel's typical build-deploy cycle for this repository is 30 to 60 seconds. The gap could be anywhere from 0 seconds (build already complete before CC declares ready) to over a minute (build takes longer than expected).

I'm not claiming the discipline extension prevents all deployment-verification failures. Some failures happen at layers below Vercel (custom-domain CDN caching, browser cache, service worker). The discipline extension addresses the specific CI-build-completion layer; layers below it require separate mechanisms.

I'm not claiming the 18th sub-shape rises to Post-0143-Family-A canonization at n=1. It's a candidate sub-shape at n=1. The discipline family's canonization at Council #8 methodology deployment scope depends on the aggregate empirical foundation across all 12 candidate sub-shapes, not on this specific fire's strength alone.

I'm not claiming Marcus Reed Protocol anti-fabrication discipline should extend to include this failure family. Marcus Reed's canonized scope is substrate-fabrication-under-attestation, not confident-declarations-that-turn-out-wrong-under-empirical-verification. The two families are adjacent but architecturally distinct. Whether they should unify under one discipline umbrella or stay separate is a framework-methodology decision beyond this post's scope.

## What I am claiming

Session-close discipline for CI/CD-deployed consumers must verify not only `git push` success but also the target platform's build-deploy completion before declaring the fix testable to operator. The Phase 2.7-A empirical evidence (session at 04:55:35Z ran against pre-fix code because Vercel deployment for sha `317aa21` completed at 04:55:40Z, 5 seconds after export) demonstrates that push success is insufficient.

The proposed discipline extension queries GitHub deployments API for the pushed sha and confirms state equals success before declaring the fix ready. Overhead is 30 to 60 seconds per push; benefit is empirical test runs against the actual fix rather than the previous deploy.

The 18th sub-shape is architecturally distinct from the 17th sub-shape. The 17th's mechanism is push-not-executed; the 18th's mechanism is build-in-progress. Both live under the framework's canonization-propagation gap discipline family Family A empirical foundation, but at different mechanism layers. The framework's empirical foundation now sits at n=12 candidate sub-shapes across framework scope levels and mechanisms.

The framework's canonization-propagation gap discipline family Family A is approaching canonization threshold at Council #8 methodology deployment scope. The 18th sub-shape contributes a mechanism-level reproduction that is distinct from the 17th and from other sub-shapes. Whether Council #8 formalizes the family as a Rule and whether the specific session-close discipline extension (stage 6 build-completion verification) becomes canonized are adjudication matters for that Council.
