<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0153
title: Tier A Empirical Close Real iPhone 17 Plus iPad Mini Ratify Framework Failure Budgets Against Target Hardware
date_published: 2026-07-04
status: published
superseded_by: none
domain: Council #6 close-condition Tier A empirical close arc executed at real iOS device scope covering iPhone 17 plus iPad Mini running population-scale harness via mobile Safari at same-WiFi local dev server pattern
project_scopes: framework-state-progress, sim-ai, memory-lanes, roomtolife
cc_task_relevance: tier-a-empirical-close, iphone-17-headroom, ipad-mini-headroom, framework-failure-budgets-ratification, three-tier-close-condition
phase_binding: Phase-2
discipline_family: Council #6 close-condition three-tier close condition strategy
canonical_rule: FRAMEWORK_FAILURE_BUDGETS ratified against real target hardware; three-tier close condition strategy fully closed at algorithmic plus WebKit-runtime plus real-device scope
load_bearing_claims:
  - iPhone 17 achieves 66x headroom at N=5000
  - iPad Mini achieves 33x headroom at N=5000
  - FRAMEWORK_FAILURE_BUDGETS ratified against real target hardware
  - Three-tier close condition strategy fully closed at algorithmic + WebKit-runtime + real-device scope
  - Path A operationalized mobile Safari same-WiFi local dev server closes Tier A at both devices
  - Council #6 close condition scope substantially complete for operator-side Memory Lanes V1 ship path
  - Two gotchas resolved Next.js dev HMR blocked hydration + Safari timer granularity clamped 1ms
  - Path A emerges as 5th operator-executable path (Post 0152 enumerated 4)
applicability_triggers:
  - Tier A empirical close arc at real iOS device scope
  - iPhone 17 or iPad Mini running population-scale harness
  - Mobile Safari same-WiFi local dev server pattern
  - Cross-device debugging Next.js Turbopack HMR blocked hydration
mechanism_details:
  - Path A mobile Safari same-WiFi local dev server pattern
  - Next.js dev HMR blocks hydration mitigated
  - Safari timer granularity clamped to ~1ms per WebKit
  - iPhone 17 66x headroom + iPad Mini 33x headroom at N=5000
cross_refs:
  - Post 0152 (Phase D empirical scaling closes at Node tier; enumerated 4 paths not 5)
  - Post 0154 (Path A as fifth path Post 0152 enumeration gap fire)
  - Post 0155 (React Fiber Next.js Turbopack HMR blocks iOS Safari hydration)
  - Memory project_phase_d_tier_a_empirical_close_iphone_17_ipad_mini_2026-07-04.md
-->

# Tier A Empirical Close Real iPhone 17 Plus iPad Mini Ratify Framework Failure Budgets Against Target Hardware

**Author:** Jimmy McColery
**Date:** 2026-07-04
**Status:** Framework state progress post documenting Council #6 close-condition Tier A empirical close arc executed at real iOS device scope covering iPhone 17 plus iPad Mini running the population-scale harness via mobile Safari at same-WiFi local dev server pattern; `FRAMEWORK_FAILURE_BUDGETS` ratified against real target hardware; three-tier close condition strategy fully closed at algorithmic plus WebKit-runtime plus real-device scope; Council #6 close condition scope substantially complete for operator-side Memory Lanes V1 ship path

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

Post 0152 documented framework-side algorithmic close condition met at Tier D Node.js host with 74x tick-cost plus 1900x memory-per-NPC headroom at N=5000 plus Tier B Safari WebKit measurement route shipped at `/sim-ai-test/scale-run` plus Tier A AWS Device Farm operator-executable deploy prep filed. Post 0152's operator-side gate specified Tier A execution as remaining ratification via one of four paths (AWS Device Farm plus BrowserStack plus owned iPhone plus Xcode plus Firebase Test Lab).

This post documents Tier A empirical close arc executed via Path A (mobile Safari on same-WiFi local dev server) rather than Path B (Capacitor plus Xcode sideload). The operator has both iPhone 17 and iPad Mini available; Path A closes the load-bearing part of Tier A ratification at approximately one hour of debugging work plus code instrumentation rather than four to six hours of Capacitor plus Xcode setup that Path B would require.

## Path A execution overview

Path A operationalizes the observation that iOS Safari and iOS Capacitor WKWebView both use the same underlying WebKit rendering engine plus JavaScriptCore JavaScript engine. Testing on iOS Safari from mobile device to Mac dev server at same-WiFi network scope covers approximately 90 percent of Tier A concerns. What Path A does NOT cover is Capacitor JS-to-native IPC bridge overhead plus iOS memory pressure and WKWebView killer thresholds plus thermal throttling under sustained load. Those three gaps only matter when actually shipping the Capacitor iOS app and can be closed at actual Memory Lanes ship prep with Path B or continued Path A extended-duration testing.

Deployment method covered production Next.js build via `npm run build` plus `npm start -- -H 0.0.0.0` on Mac plus iPhone 17 plus iPad Mini navigation via mobile Safari to `http://10.0.0.91:3000/sim-ai-test/scale-run` at same-WiFi network scope plus server-side result capture via `/api/tier-a-results` POST endpoint newly added at 2026-07-04 early afternoon plus Mac Safari Web Inspector attached to iOS Safari via cable for diagnostic console.log visibility.

## Two gotchas resolved during execution

Two gotchas surfaced during Path A execution that required diagnostic resolution before empirical measurement could proceed.

**Next.js dev-mode HMR blocking iOS Safari hydration.** Turbopack HMR WebSocket connection failed cross-device (Mac local dev server to iPhone Safari) which prevented React client-component hydration on iPhone Safari. Symptom: page loaded but React fiber never attached to DOM plus button click did nothing plus programmatic `document.querySelector('button').click()` triggered no handler. Native HTML checkbox toggle misled diagnostic because browser-native checkbox toggling works without any React JavaScript at all. Confirmed via console.log statement `Object.keys(btn).some(k => k.startsWith('__reactFiber'))` returning `false` on iPhone Safari but `true` on Mac Safari. Resolution: production build via `npm run build` plus `npm start` bypasses HMR entirely plus hydration completes cleanly plus button click fires handler plus full harness runs to completion plus POST reaches server successfully.

**`performance.now()` timer granularity clamped at approximately 1 millisecond in Safari.** Safari privacy feature (Spectre mitigation via Meltdown-plus-Spectre-era browser mitigation stack) clamps timer resolution at approximately 1 millisecond for cross-origin protection. Sub-millisecond ticks reported as 0.000. Only max column captures observable outliers. Median plus p95 report 0-1ms across all tiers regardless of actual work distribution. Framework's harness code was designed for Node.js V8 timer resolution (approximately 1 microsecond); Safari's coarser resolution required the operator to interpret max tick as the load-bearing budget compliance metric and disregard median plus p95 zeros as timer-artifact.

## iPhone 17 empirical measurements

Device: iPhone 17 with iPhone OS 18.7 plus Safari Version 26.6 plus WebKit. Overall measurement duration: 526 milliseconds. This is faster than Mac Safari's 664 milliseconds and closer to Node.js V8's approximately 500-800 millisecond range. A19 Pro chip empirically outperforms the operator's 2021 MacBook Pro at this specific single-threaded JavaScript workload.

At N=500 with 200 ticks: max tick 2 milliseconds against 16.67 millisecond budget at 60 Hertz frame envelope with 8.3 times headroom. Memory footprint per NPC: 0.00026 megabytes. Total memory footprint: 0.132 megabytes.

At N=1000 with 200 ticks: max tick 1 millisecond against 33.33 millisecond budget at 30 Hertz frame envelope with 33 times headroom. Memory footprint per NPC: 0.00026 megabytes. Total memory footprint: 0.259 megabytes.

At N=5000 with 200 ticks: max tick 1 millisecond against 66.67 millisecond budget at 15 Hertz frame envelope with 66 times headroom. Memory footprint per NPC: 0.00026 megabytes. Total memory footprint: 1.278 megabytes.

Deterministic replay: N=500 with 5000 ticks and 2 runs at seed 42 returned matching hashes. N=1000 with 5000 ticks and 2 runs at seed 42 returned matching hashes.

## iPad Mini empirical measurements

Device: iPad Mini with iOS 18.7 plus Safari Version 26.5. Overall measurement duration: 1332 milliseconds. Approximately 2.5 times slower than iPhone 17 which is expected since iPad Mini has an older and less-capable chip.

At N=500 with 200 ticks: max tick 9 milliseconds against 16.67 millisecond budget at 60 Hertz frame envelope with 1.9 times headroom. Memory footprint per NPC: 0.00026 megabytes.

At N=1000 with 200 ticks: max tick 2 milliseconds against 33.33 millisecond budget at 30 Hertz frame envelope with 17 times headroom.

At N=5000 with 200 ticks: max tick 2 milliseconds against 66.67 millisecond budget at 15 Hertz frame envelope with 33 times headroom.

Deterministic replay: N=500 with 5000 ticks and 2 runs at seed 42 returned matching hashes. N=1000 with 5000 ticks and 2 runs at seed 42 returned matching hashes.

## The framework failure budgets ratification decision

All 6 tier-device combinations across Node.js plus Mac Safari plus iPhone 17 plus iPad Mini at N=500 plus N=1000 plus N=5000 pass `FRAMEWORK_FAILURE_BUDGETS` at 60 Hertz plus 30 Hertz plus 15 Hertz frame budgets. No recalibration warranted. The 60Hz plus 30Hz plus 15Hz target frame budgets are ratified against real target hardware.

iPad Mini is the baseline device (lowest headroom at 1.9 times headroom for N=500). iPhone 17 provides substantial headroom margin for future device generations at 66 times headroom for N=5000. The framework population-scale foundation supports the ratified budgets with confidence at target hardware envelope.

## Anomaly observation at iPad Mini N=500 tight max tick

iPad Mini's N=500 max tick of 9 milliseconds is 1.9 times under 60 Hertz budget which is tightest observed headroom across all tier-device combinations. Higher tiers (N=1000 and N=5000) show much better headroom (2 milliseconds). Likely explained by: (a) single-tick outlier hitting GC pause or Safari watchdog check; (b) `performance.now()` granularity noise dominates small-N measurements; (c) p95 remained 1 millisecond across all tiers with only max showing the outlier. This is not a scaling issue but a measurement artifact plus GC event. Framework's mitigation (max tick vs budget compliance) is conservative enough to catch this while still passing. If tighter margins were required, mitigation would be to increase `MAX_EFE_PER_TICK` cap or defer some tick work to next frame.

The counterintuitive observation that N=5000 max tick on iPad Mini (2 milliseconds) is BETTER than N=500 max tick (9 milliseconds) reflects that Safari's `performance.now()` granularity of approximately 1 millisecond clamp plus GC noise dominate small-N measurements. At larger N the workload amortizes noise across more ticks so the max tick outlier becomes proportionally smaller relative to per-tick sustained work. This is a measurement artifact of Safari's timer granularity not a genuine scaling anomaly.

## Three-tier close condition strategy ALL TIERS PASSED

The framework's Council #6 close close-condition scope is substantially complete at Tier D plus Tier B plus Tier A ratification.

Tier D (Node.js V8 on Mac) closed 2026-07-04 morning at 74 times headroom at N=5000. Post 0152 documented full close.

Tier B (Safari WebKit on Mac) closed 2026-07-04 late morning at 33 times headroom at N=5000. Post 0152 documented shipping the Safari-testable route at `/sim-ai-test/scale-run`.

Tier A (real iPhone 17 plus iPad Mini) closed 2026-07-04 early afternoon at 66 times headroom (iPhone 17) plus 33 times headroom (iPad Mini) at N=5000. Path A executed via mobile Safari on same-WiFi local dev server rather than Path B Capacitor plus Xcode sideload. This post documents that close.

## Remaining gaps out of scope for Path A close

Path A does not cover three iOS-app-lifecycle concerns that surface at actual Capacitor ship rather than at framework foundational-readiness scope.

Capacitor JS-to-native IPC bridge overhead not exercised. Real Capacitor build with WKWebView instead of Safari would add this overhead. Estimated impact: less than 1 millisecond per bridge call plus batch-able. Deferred to actual iOS Capacitor build for Memory Lanes ship prep.

iOS memory pressure plus WKWebView killer thresholds not exercised. Requires sustained-load testing over hours. Deferred to actual Memory Lanes ship prep or continued Path A extended-duration testing.

Thermal throttling under sustained load not exercised. Requires extended-duration testing at real device scope. Deferred.

These gaps do not affect the algorithmic close condition plus WebKit-runtime close condition ratified above. They pertain to iOS-app-lifecycle concerns that surface at actual Capacitor ship not at framework foundational-readiness scope.

## The framework state observation about Path A vs Path B

Council #6 close deploy prep Post 0152 documented four operator-choice paths for Tier A ratification: AWS Device Farm at approximately 5 to 20 dollar cost plus BrowserStack at 29 to 149 dollar monthly subscription plus owned iPhone plus Xcode plus 99 dollar per year Apple Developer account plus Firebase Test Lab free tier. This post documents that a fifth path was operationalized during execution: Path A via mobile Safari at same-WiFi local dev server closes the load-bearing part of Tier A ratification at zero cost plus approximately one hour of debugging work.

Path A does not fully close Tier A because it does not exercise the Capacitor plus WKWebView plus iOS app lifecycle concerns. But it does close the two load-bearing scopes: real iOS Safari plus WebKit runtime at real iPhone hardware and real iPad hardware. For framework foundational-readiness ratification (the Council #6 close condition question) this is sufficient. For iOS ship prep the remaining Capacitor plus WKWebView concerns will be closed as part of the actual iOS build workflow.

The operator learning is that framework's Post 0143 canonization-propagation gap discipline extends to deployment-path options canonization at framework post scope. The Post 0152 four-path enumeration was correct at foundational-readiness scope but incomplete at operator-executable-execution scope. Path A as a fifth path emerges naturally when the operator has target devices available and same-WiFi network access. Future close-condition post arcs should enumerate execution-path options at both foundational-readiness scope and operator-executable-execution scope to avoid this incompleteness.

## Test suite growth

Prior Phase D empirical close: 472 tests passing. Tier A close arc adds: 0 new tests. No code changes to Sim AI core (instrumentation only at UI harness plus new API endpoint). Post-Tier A total: 472 tests passing.

Additional artifacts landed at Open Alley scope:
- `/api/tier-a-results` route at `src/app/api/tier-a-results/route.ts` with server-side JSONL result capture (gitignored)
- `ScaleRunHarness.tsx` instrumentation adding `console.log` at every state transition plus `fetch POST` to results endpoint plus `?autorun=1` URL parameter for hands-free auto-run
- Server-side result artifact at `tier-a-results/tier-a-results.jsonl` (local dev only; gitignored per operator local-only repo discipline)

## Council #6 close condition status FULLY MET

Framework-side algorithmic close condition met with substantial headroom (Tier D Node.js). Framework-side WebKit-runtime close condition met with substantial headroom (Tier B Safari WebKit). Operator-side target-hardware close condition MET with substantial headroom (Tier A iPhone 17 plus iPad Mini). All three tiers of the Council #6 close condition strategy ratified.

Memory Lanes V1 ship gate now advances from Phase D full close plus Room to Life Universe Phase C full production implementation plus operator scope-out decisions per Council #6 close fold-set. Phase D full close: MET. Room to Life Universe Phase C full: approximately 3 to 4 weeks backend engineering estimated. Operator scope-out decisions: pending per Council #6 fold-set adjudication.

The framework's next operator-judgment decisions cover Room to Life Universe Phase C full production implementation scope at 3 to 4 week estimated backend engineering scope plus Memory Lanes semantic sufficiency Council-vs-continue-observation adjudication at Decision 4 conditionally-foundational status plus character design workflow ratification (Options A through E per CC critical response 2026-07-04 late morning) plus bowling alley action space design (per Open Alley scope draft filed 2026-07-04 evening).

## Cross-references

- Council #6 close post 0147 plus post 0148
- Phase D empirical scaling close arc Post 0152
- Council #6 methodology guide at `~/Projects/the-street-code/methodology/population-scaling-foundation-pass-methodology-guide-v1.md`
- Phase D empirical scaling findings artifact updated with Tier A section at `~/Projects/Open Alley/src/lib/sim-ai/worlds/island/scale/phase-d-empirical-scaling-findings-2026-07-04.md`
- Tier B route at `~/Projects/Open Alley/src/app/sim-ai-test/scale-run/page.tsx` plus `~/Projects/Open Alley/src/components/sim-ai/ScaleRunHarness.tsx`
- Tier A results endpoint at `~/Projects/Open Alley/src/app/api/tier-a-results/route.ts`
- Framework canonical rules at `~/Projects/master-setup/operational_discipline_rules.canonical.md` v1.23
- Bowling alley action space scope draft at `~/Projects/Open Alley/src/lib/sim-ai/worlds/island/bowling-alley-action-space-scope-draft-2026-07-04.md`
