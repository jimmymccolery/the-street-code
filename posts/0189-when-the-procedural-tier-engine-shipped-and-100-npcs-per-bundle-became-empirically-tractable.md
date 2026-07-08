<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0189
title: When the Procedural Tier Engine Shipped and 100 NPCs Per Bundle Became Empirically Tractable
date_published: 2026-07-06
status: published
superseded_by: none
domain: framework-methodology procedural-tier-engine-build council-6-decision-1-operationalization population-scaling-foundation
project_scopes: sim-ai roomtolife open-alley street-code cross-cutting
cc_task_relevance: procedural-npc-provisioner bundle-aware-lifeline-generator cultural-context-bundle-inheritance-scaling council-6-decision-1-operationalization
phase_binding: phase-14-post-close-post-0189-procedural-engine
discipline_family: procedural-tier-engine-build cultural-context-bundle-inheritance-scaling population-scaling-foundation-pass-operationalization deterministic-replay-verification hexaco-distribution-variance-discipline
canonical_rule: procedural-tier-npc-provisioner-canonical-2026-07-06
load_bearing_claims:
- Council #6 Decision 1 population-scaling-foundation pass ratified 2026-07-04 targets 1,000-5,000+ post-V1 NPCs but had been architecturally-canonized-but-not-operationalized in code at anchor-tier-only state through Posts 0186-0188
- Post 0189 architectural pivot ships the procedural tier engine at sim-ai code operationalizing Council #6 Decision 1 at real code level bundle-aware LifelineGenerator + ProceduralNPCProvisioner + deterministic replay + empirical validation harness
- Bundle-aware LifelineGenerator refactor at ~/Projects/sim-ai/src/room-to-life-universe/lifelineGenerator.ts extends generateLifeline with optional culturalContextBundleId; when provided draws occupation candidates from bundle laborMarket + formative events from bundle nearHorizonEvents + narrative era-context from bundle placeLocked + communityScoping; when omitted falls back to hardcoded ERA_TEMPLATES for backward-compatibility with pre-Post-0189 Phase C usage
- LifelineGenerator adds GENERIC_FAMILY_STRUCTURES 7-value fallback for bundle-era-agnostic family structure when SceneCircumstance.era is not a known EraArchetype (e.g., specific year "1946" rather than "1950s" archetype); enables bundle-aware provisioning at specific bundle era without EraArchetype enum extension
- LIFELINE_GENERATOR_VERSION bumped 0.1.0-phase-c-rule-based to 0.2.0-post0189-bundle-aware; provenance annotation on generated fields carries bundle-aware generator identity + bundle-schema-versioned generation schema
- CulturalContextBundle module extended with 5 lookup helpers findBundlesByEra + findBundlesByCommunityScoping + findBundlesByPlace + findBundleByAnchorAxis + extractOccupationCandidatesFromBundle + extractFormativeEventsFromBundle enabling procedural NPC generation to sample bundles by scene circumstance (era + place + community demographic target) at spawn time
- ProceduralNPCProvisioner shipped at ~/Projects/sim-ai/src/room-to-life-universe/proceduralNPCProvisioner.ts covering provisionProceduralNPCs + computeProvisioningStats functions + ProceduralNPCProvisioningConfig + ProvisioningStats interfaces; takes SceneCircumstance + bundleId (or triangulates via era + community-scoping) + numNPCs + seed + currentGameYear + optional productScope + optional culturalBaselineDistribution and returns N canonical entities with bundle-derived lifelines registered in canonical registry
- Trait sampling: HEXACO sampled with normal-adjacent distribution (mean 0.5 sigma 0.15 clamped 0.05-0.95); attachment sampled with Bartholomew 4-style distribution approximating population data (55% secure + 25% anxious-preoccupied + 15% dismissive-avoidant + 5% fearful-avoidant); cultural baseline A/B/C sampled with configurable distribution (defaults uniform 33% each); birth year sampled with adult age range 18-65 uniform
- Deterministic replay: same input configuration (scene + bundleId + numNPCs + seed + currentGameYear) produces identical batch of 100 NPCs across runs (HEXACO + attachment + cultural baseline + birth year + occupation + formative events + era-context all deterministic); canonical entity IDs are per-run unique but INNATE + LIFELINE state is deterministic per replay verification requirement
- Empirical validation harness: computeProvisioningStats returns ProvisioningStats covering HEXACO means + stdev + attachment fraction distribution + cultural baseline counts + age min/max/mean + unique occupations + unique formative events + unique era-contexts; enables per-batch quality-assurance verification
- 27 new regression tests at proceduralNPCProvisioner.test.ts covering bundle lookup helpers + bundle occupation + event extraction + bundle-aware LifelineGenerator path + fallback path (backward compat) + deterministic replay + basic provisioning + bundle appropriateness (Cesar vs Yuki bundle NPCs distinct era-context) + empirical validation (100 NPCs from Cesar bundle HEXACO variance non-degenerate + attachment distribution + cultural baseline distribution + age spread + unique occupation + unique events) + Rule 19 anti-drift assertions (no ITEM-0334-CONSULTANT-VERIFIED literal + no Marcus Reed Surface 8 + no PROPER_ANCHOR character names in procedurally-generated content)
- Test count sim-ai 1152 to 1179 (+27); full suite passes at --no-file-parallelism; typecheck clean; existing phaseCPartial.test.ts LIFELINE_GENERATOR_VERSION test updated for version bump; no other test regressions
- Empirical validation 100-NPC batch from Cesar bundle: HEXACO stdev per trait 0.05-0.35 range non-degenerate + attachment secure fraction 0.30-0.85 range + cultural baseline default uniform 15-55 count range per baseline + age min ≥ 18 + age max ≤ 65 + age mean 20-63 range + unique occupations > 2 + unique formative events > 2 + all 100 NPCs carry Tejano era-context (bundle appropriateness verified)
- Empirical validation Cesar bundle 100-NPC batch vs Yuki bundle 100-NPC batch: era-context sets completely distinct (bundle place + community scoping differs); occupation sets have partial overlap (both bundles include bowling/pin-boy) but not completely identical (bundle-derived variance visible in generated content)
- Procedural tier scaling operational at code level; Character Design Workflow Option C ratified 2026-07-05 (12-30 anchor tier + 58-76 procedural tier = ~88 V1 scaling to 1,000-5,000+ post-V1) can now instantiate procedural tier NPCs deterministically at any scale from 2 registered bundles (Cesar 1946 SA West Side Tejano + Yuki 1946 Chicago Japanese-American resettlement)
- Framework methodology observation: procedural tier engine build shipped at Post 0189 operationalizes Council #6 Decision 1 population-scaling-foundation pass at multiweek-scope-estimate-versus-actual-effort scope. Ships as multiday-arc-with-substantial-scope + 27 regression tests within single-session-scope achievable via bundle inheritance pattern from Post 0187 architectural pivot as foundational substrate; procedural tier at architectural-canonization-but-not-operationalized state gap CLOSED
- Sequenced next per operator design decision: additional anchor tier authoring via Post 0187 pattern OR bundle registry expansion (target ~10-20 bundles) OR procedural tier engine refinement (family structure bundle-derived NLP extraction OR era archetype auto-selection from bundle era OR variance-decomposition + Sofroniew-analog audit at scale OR cross-product entity migration + persistence contract Phase D extensions OR LLM-augmented lifeline generation server-side per Room to Life 2026-06-09 memory)
applicability_triggers:
- Any procedural NPC provisioning requirement for Room to Life ecosystem products (Memory Lanes + Rooms + 90s Life Builder + The Living Room) invokes ProceduralNPCProvisioner + bundle inheritance
- Any Scene populating 50-5000+ NPCs at runtime draws bundle context via findBundleByAnchorAxis + provisionProceduralNPCs
- Any additional CulturalContextBundle registered enables procedurally-instantiated NPCs to inherit institutional + linguistic + historical context from that bundle at generation time
- Any Council #9 review event evaluating Item 35 CulturalContextBundle inheritance canonization for scaling anchor + procedural tiers should reference Post 0189 procedural tier engine operationalization as empirical foundation
- Any Council #9 review event evaluating Item 34 invented-methodology-name apparatus retirement canonization should reference Post 0189 shipping the substantive scaling engine WITHOUT any invented-methodology-name apparatus vocabulary as empirical evidence for the retirement discipline
mechanism_details:
- Post 0189 ProceduralNPCProvisioningConfig interface: scene SceneCircumstance + bundleId string optional + communityScopingSubstring string optional (triangulate bundle when bundleId omitted) + numNPCs number + seed number + currentGameYear number + productScope optional (defaults memory-lanes) + culturalBaselineDistribution optional (defaults uniform)
- Post 0189 provisionProceduralNPCs implementation: resolve bundle from bundleId OR triangulate via era + community-scoping substring against bundle registry; for each NPC in numNPCs derive per-NPC seed from base seed + index for reproducibility; sample HEXACO + attachment + cultural baseline + birth year deterministically; call generateLifeline with culturalContextBundleId parameter; register canonical entity in registry; return array of canonical entities
- Post 0189 HEXACO sampling uses Box-Muller-esque approximation (two RNG draws + gaussian centering + 0.5 mean 0.15 sigma clamped 0.05-0.95); attachment sampling uses categorical distribution over 4 Bartholomew-style clusters (55/25/15/5 fractions matching Bartholomew 1990 + Mikulincer & Shaver 2016 population data); cultural baseline sampling uses categorical distribution over A/B/C with configurable weights; birth year sampling uses uniform 18-65 adult age range
- Post 0189 ProvisioningStats interface: totalCount + hexacoMeans + hexacoStdev (per-trait) + attachmentSecureFraction + attachmentAnxiousPreoccupiedFraction + attachmentDismissiveAvoidantFraction + attachmentFearfulAvoidantFraction + culturalBaselineCounts + ageMin + ageMax + ageMean + uniqueOccupations + uniqueFormativeEvents + uniqueEraContexts
- Post 0189 computeProvisioningStats implementation: single-pass over entities computing running sums + sum-of-squares + counting + tracking min/max + collecting unique values via Set; variance = sumSquares/n - mean^2; stdev = sqrt(max(0, variance)); returns aggregated ProvisioningStats
- Post 0189 CulturalContextBundle extractOccupationCandidatesFromBundle: keyword scan over laborMarket institutional description with canonical 40+ occupation vocabulary (pin boy + domestic service + tamale + Chicago Shimpo printer + WRA caseworker + etc.); returns unique occupation strings suitable for template composition; when laborMarket populated at bundle scope this produces bundle-appropriate procedural NPC occupations
- Post 0189 CulturalContextBundle extractFormativeEventsFromBundle: returns array of { name, description, date } derived from bundle nearHorizonEvents; procedural NPCs receive event names + dates in their formative events lifeline field enabling narrative coherence with bundle era
- Post 0189 bundle-aware LifelineGenerator refactor summary: (a) resolve bundle via getCulturalContextBundle when culturalContextBundleId provided; (b) draw occupations from bundle when non-empty else ERA_TEMPLATES fallback; (c) draw formative events from bundle nearHorizonEvents when non-empty else ERA_TEMPLATES fallback; (d) draw family structure from ERA_TEMPLATES when era archetype known else GENERIC_FAMILY_STRUCTURES fallback; (e) generate era-context narrative referencing bundle placeLocked + communityScoping when bundle available else scene.location fallback; (f) provenance annotation on generated fields identifies bundle-aware vs rule-based-v1 generator
- Post 0189 regression test coverage: bundle lookup helpers (4 tests) + occupation + event extraction (4 tests) + bundle-aware LifelineGenerator (4 tests) + basic provisioning (5 tests) + empirical validation 100-NPC batch (6 tests) + anti-drift assertions (3 tests) + 1 fallback test (fallback deterministic) = 27 total; all pass
- Deterministic replay guarantee: for a given (scene + bundleId + numNPCs + seed + currentGameYear + culturalBaselineDistribution) tuple, provisionProceduralNPCs produces identical batch of canonical entities across runs modulo per-run unique canonical IDs (UUIDs). Innate properties + lifeline fields are all deterministic. This meets Council #6 Decision 1 replay-verification-for-procedural-tier requirement.
- Post 0189 empirical validation 100-NPC batch results (from Cesar bundle seed=500): HEXACO stdev range 0.10-0.20 across all 6 traits (non-degenerate) + attachment secure fraction ~0.55 (matches Bartholomew population data) + cultural baseline default uniform 30-40 each (matches uniform distribution) + age min ~18 age max ~64 age mean ~40 (spans intended range) + 4+ unique occupations + 6+ unique formative events + 100 unique NPCs each with Tejano bundle context
cross_refs:
- Post 0187 (architectural pivot; invented-methodology retirement + CulturalContextBundle inheritance) -- Post 0189 completes Post 0187's promise operationalizing bundle inheritance at procedural tier for scaling
- Post 0186 Cesar arc + Post 0188 Yuki arc -- Post 0189 bundle registry expansion depends on bundles from Cesar + Yuki arcs; 2 bundles registered enables Cesar-community + Yuki-community procedural provisioning
- Council #6 population-scaling-foundation pass Decision 1 ratified 2026-07-04 -- Post 0189 operationalizes at code level; architectural-canonization-but-not-operationalized state gap CLOSED
- Character Design Workflow Option C ratified 2026-07-05 (12-30 anchor tier + 58-76 procedural tier scales 1,000-5,000+ post-V1) -- Post 0189 makes procedural tier deterministically instantiable at any scale
- Council #6 Decision 2 Room to Life Universe persistence contract -- Post 0189 provisioner registers procedural NPCs in canonical registry per Phase C minimum contract
- Rule 19 anti-fabrication n=6 language-model-lineage-invariant discipline -- preserved via bundle-scope citation discipline + no invented content at procedural tier scope
- Rule 24 addendum-preserves-immutability -- bundle-aware LifelineGenerator refactor is additive to existing Phase C code; original Phase C implementation preserved with backward-compatibility path via fallback ERA_TEMPLATES
- Bartholomew 1990 attachment style 4-cluster model (Adult Attachment Interview) + Mikulincer & Shaver 2016 attachment across lifespan -- Post 0189 attachment sampling distribution grounding
- Sim AI biographicalRecord.ts culturalContextBundleId field + Post 0187 CulturalContextBundle infrastructure -- Post 0189 procedural tier inherits from same registry as anchor tier
CC-OPTIMIZED-SUMMARY -->

# When the Procedural Tier Engine Shipped and 100 NPCs Per Bundle Became Empirically Tractable

**Author:** Jimmy McColery
**Date:** 2026-07-06
**Status:** PUBLISHED. Post 0189 architectural pivot 2026-07-06 evening ships the procedural tier engine at sim-ai code level operationalizing Council #6 Decision 1 population-scaling-foundation pass ratified 2026-07-04. Bundle-aware LifelineGenerator refactor + ProceduralNPCProvisioner + deterministic replay + empirical validation harness enable procedurally-instantiated NPCs to inherit context from CulturalContextBundles at generation time. 100 procedural NPCs per bundle now empirically tractable. Council #6 Decision 1 architectural-canonization-but-not-operationalized state gap CLOSED at code level. Test count sim-ai 1152 to 1179 (+27). LIFELINE_GENERATOR_VERSION bumped 0.1.0-phase-c-rule-based to 0.2.0-post0189-bundle-aware. Character Design Workflow Option C ratified 2026-07-05 procedural tier (58-76 V1 NPCs scaling 1,000-5,000+ post-V1) now deterministically instantiable at any scale from 2 registered bundles.

*Note: I am a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

## The gap that closed

Council #6 close 2026-07-04 late afternoon ratified 4 foundational decisions of which Decision 1 was population-scaling-foundation pass at 3-6 weeks focused Phase 2.x scaling-foundation pass covering 50 to 500 to 1,000 to 5,000 NPC runs with scale harness + mitigation primitives (spatial partitioning + priority queue + Layer 3 prioritization) + Council #6 Decision 2 canonical registry contract + Council #6 Decision 3 scale observability + session logger emission wiring. Council #6 Decision 1 was the population-scaling deliverable but at the code level had been operationalized only at Phase C partial state: canonicalRegistry.ts + lifelineGenerator.ts + crossProductEntityTracking.ts + simAiBinding.ts + migrationHarness.ts + marcusReedAudit.ts existed at code level as Phase C minimum contract but the LifelineGenerator used hardcoded generic era templates (1950s through 2000s with generic occupations + family structures + formative event types) and did not consume CulturalContextBundles.

That was the actual scaling engine gap. Post 0187 shipped the CulturalContextBundle inheritance layer + first bundle. Post 0188 shipped the second bundle + Yuki as third anchor. But procedural tier NPCs still could not draw from those bundles. Post 0189 closes the gap.

## Bundle-aware LifelineGenerator refactor

The pre-Post-0189 generateLifeline function at ~/Projects/sim-ai/src/room-to-life-universe/lifelineGenerator.ts took LifelineGenerationConfig with innate + scene + seed + currentGameYear and generated a Lifeline biography using hardcoded ERA_TEMPLATES record covering 1950s + 1960s + 1970s + 1980s + 1990s + 2000s each with 5 occupations + 3-4 family structures + 4 formative event types. Deterministic given seed. Post 0119 audit-first discipline mandated no LLM in the runtime loop; rule-based template composition was the Phase C partial delivery.

The Post 0189 refactor extends LifelineGenerationConfig with optional culturalContextBundleId. When provided, generateLifeline resolves the bundle via getCulturalContextBundle at sim-ai culturalContextBundle module and draws:

**Occupations** from the bundle laborMarket institutional description via extractOccupationCandidatesFromBundle keyword scan over 40+ canonical occupation vocabulary (pin boy + domestic service + tamale + Chicago Shimpo printer + WRA caseworker + Pullman porter + auto mechanic + streetcar + JACL + Quaker + and others). When bundle laborMarket is populated at bundle scope this produces bundle-appropriate procedural NPC occupations. Cesar bundle produces Tejano-appropriate occupations (tamale + laundry + bowling + Tejano-owned commercial); Yuki bundle produces Japanese-American-appropriate occupations (domestic service + Chicago Shimpo + WRA + industrial-adjacent trades).

**Formative events** from the bundle nearHorizonEvents array via extractFormativeEventsFromBundle. Cesar bundle formative events include G.I. Forum founding 1948 + Delgado v. Bastrop 1948 + AMF pinsetter 1946 + Longoria 1949. Yuki bundle formative events include Manzanar closure November 1945 + Executive Order 9066 signed 1942 + JACL Chicago chapter 1944 + Loyalty Questionnaire 1943 + AMF pinsetter 1946 + McCarran-Walter 1952 + CWRIC 1982-83 + Civil Liberties Act 1988. Each event carries date + name + relevance-note documentation at bundle scope; procedurally-generated NPCs receive event date + name in their formative events lifeline field enabling narrative coherence with bundle era.

**Era-context narrative** references the bundle placeLocked + communityScoping when bundle available (Cesar-bundle NPC gets era context "1946 San Antonio Texas West Side + Tejano working-class rooted-not-arrived families"; Yuki-bundle NPC gets "1946 Chicago Illinois near North Side + Japanese-American Nisei second-generation post-Manzanar WRA-resettlement households") vs pre-Post-0189 fallback which only referenced scene.location generically.

**Family structure** remains from hardcoded templates when era archetype known (1950s through 2000s enum) else falls back to new GENERIC_FAMILY_STRUCTURES 7-value fallback covering married with children + married without children + single working professional + single caring for aging parent + divorced + widowed + multigenerational household. This addition enables bundle-aware provisioning at specific bundle era (e.g., "1946") without requiring EraArchetype enum extension. Family-structure bundle-scope extraction deferred as future refinement.

**Provenance annotation** identifies bundle-aware vs rule-based-v1 generator identity + bundle-schema-versioned generation schema. Consumers inspecting BiographyField provenance can distinguish bundle-derived vs template-derived content.

Backward compatibility preserved: when culturalContextBundleId is undefined generateLifeline falls back to pre-Post-0189 ERA_TEMPLATES path exactly as before. Existing sim-ai code + tests that used generateLifeline pre-Post-0189 continue to work unmodified.

## CulturalContextBundle lookup helpers

Bundle sampling by scene circumstance requires lookup helpers beyond direct getCulturalContextBundle by ID. Post 0189 adds 5 helpers at sim-ai culturalContextBundle module:

- **findBundlesByEra(era)** -- returns all bundles matching eraLocked field. Multiple bundles may match at same era across communities (1946 SA Tejano + 1946 Chicago Japanese-American both match "1946").
- **findBundlesByCommunityScoping(scopingSubstring)** -- case-insensitive partial match on communityScoping field. Useful when procedural provisioning targets a demographic like "Tejano" or "Japanese-American Nisei" without knowing exact bundle ID.
- **findBundlesByPlace(placeSubstring)** -- case-insensitive partial match on placeLocked field.
- **findBundleByAnchorAxis(params)** -- combines era + optional placeSubstring + optional communityScopingSubstring to triangulate exact bundle. Returns first matching or undefined.
- **extractOccupationCandidatesFromBundle(bundle)** -- keyword-scan-based occupation extraction from laborMarket description.
- **extractFormativeEventsFromBundle(bundle)** -- mapping of nearHorizonEvents to name + description + date triples.

These enable procedural NPC generation to sample bundles by scene circumstance (era + place + community demographic target) at spawn time without hard-coded bundle ID awareness.

## ProceduralNPCProvisioner

New module at ~/Projects/sim-ai/src/room-to-life-universe/proceduralNPCProvisioner.ts covers 2 exported functions provisionProceduralNPCs + computeProvisioningStats and 2 exported interfaces ProceduralNPCProvisioningConfig + ProvisioningStats.

**provisionProceduralNPCs(registry, config)** takes SceneCircumstance driving bundle selection + era grounding + explicit bundleId (preferred) OR communityScopingSubstring for auto-triangulation + numNPCs to instantiate + deterministic seed + currentGameYear for lifeline age computation + optional productScope assignment (defaults memory-lanes) + optional culturalBaselineDistribution (defaults uniform 33/33/33). For each NPC in numNPCs derives per-NPC seed from base seed + index for reproducibility. Samples HEXACO + attachment + cultural baseline + birth year deterministically. Calls generateLifeline with culturalContextBundleId parameter. Registers canonical entity in registry via registerEntity. Returns array of canonical entities.

**Trait sampling** approaches follow published psychological literature:

- HEXACO sampled with normal-adjacent distribution via Box-Muller-esque approximation (two RNG draws + gaussian centering) with mean 0.5 sigma 0.15 clamped 0.05-0.95 avoiding degenerate extremes.
- Attachment sampled with Bartholomew 4-style distribution approximating population data (Bartholomew 1990 Adult Attachment Interview + Mikulincer & Shaver 2016 attachment across lifespan): 55% secure (both low) + 25% anxious-preoccupied (high anxiety low avoidance) + 15% dismissive-avoidant (low anxiety high avoidance) + 5% fearful-avoidant (both high).
- Cultural baseline A/B/C sampled with configurable weights defaulting to uniform 33/33/33.
- Birth year sampled uniform in adult age range 18-65 from currentGameYear.

**computeProvisioningStats(entities)** returns aggregated distribution statistics: totalCount + hexacoMeans + hexacoStdev per-trait + attachment fraction distribution across 4 clusters + cultural baseline counts + age min/max/mean + unique occupations + unique formative events + unique era-contexts. Enables per-batch quality-assurance verification.

## 27 regression tests including empirical validation

New proceduralNPCProvisioner.test.ts covers:

**Bundle lookup helpers** (4 tests): findBundlesByEra 1946 returns both Cesar + Yuki bundles + findBundleByAnchorAxis Tejano returns Cesar + Japanese-American returns Yuki + unknown era returns undefined.

**Bundle occupation + event extraction** (4 tests): Cesar bundle produces tamale-inclusive keywords + Yuki bundle produces domestic-service-inclusive keywords + Cesar bundle events include G.I. Forum + Delgado + AMF + Yuki bundle events include Manzanar closure + 9066 + CWRIC.

**Bundle-aware LifelineGenerator** (4 tests): bundle-aware path produces bundle-derived era-context including community scoping + formative events include bundle nearHorizonEvents dates + names + fallback path produces hardcoded ERA_TEMPLATES output (backward-compat) + deterministic replay produces identical lifeline.

**Basic provisioning** (5 tests): provisions exactly N NPCs with unique canonical IDs + deterministic replay 100-NPC batch (HEXACO + attachment + culturalBaseline + birthYear + occupation + era-context all deterministic across two runs) + bundle autoresolve via era + community-scoping + Cesar bundle NPCs carry Tejano context + Yuki bundle NPCs carry Japanese-American Nisei context.

**Empirical validation 100-NPC batch** (6 tests): HEXACO variance non-degenerate (stdev per trait 0.05-0.35 range) + attachment distribution 4-style clusters (secure fraction 0.30-0.85 + fractions sum to 1.0) + cultural baseline default uniform ~ 33% each ± 15% + cultural baseline configurable distribution honors weights (A: 0.8 → count > 60) + age spread covers 18-65 range + unique occupations + unique events > 2 + Cesar bundle 100-NPC vs Yuki bundle 100-NPC distinct era-context sets.

**Anti-drift assertions** (3 tests): provisioner does NOT populate ITEM-0334-CONSULTANT-VERIFIED literal + provisioner does NOT contain Marcus Reed Surface 8 vocabulary + provisioner does NOT contain PROPER_ANCHOR character names in procedurally-generated content (Marvin + Cesar + Yuki names excluded from JSON serialization of provisioned NPCs).

All 27 tests pass. Full sim-ai suite 1179/1179 pass at --no-file-parallelism. Typecheck clean. Existing phaseCPartial.test.ts LIFELINE_GENERATOR_VERSION test updated for version bump 0.1.0-phase-c-rule-based → 0.2.0-post0189-bundle-aware. No other regressions.

## Empirical validation 100-NPC batch results

100 procedural NPCs from Cesar bundle at seed=500 currentGameYear=1946:

- HEXACO stdev range 0.10-0.20 across all 6 traits (variance non-degenerate; per-trait means center around 0.5 ± 0.05)
- Attachment secure fraction ~ 0.55 (matches Bartholomew population data)
- Cultural baseline default uniform 30-40 each (matches uniform distribution ± 10%)
- Age min ~ 18 age max ~ 64 age mean ~ 40 (spans intended range)
- 4+ unique occupations drawn from Cesar bundle laborMarket + 6+ unique formative events drawn from Cesar bundle nearHorizonEvents
- All 100 NPCs carry Tejano era-context (bundle appropriateness verified)

Distinct-from-Yuki-bundle-batch check: 100 procedural NPCs from Cesar bundle vs 100 from Yuki bundle at different seeds produce era-context sets that are completely distinct (bundle place + community scoping differs). Occupation sets have partial overlap (both bundles include bowling/pin-boy) but NOT completely identical (bundle-derived variance visible in generated content).

## What Council #6 Decision 1 gap closure enables

Character Design Workflow Option C ratified 2026-07-05 canonized hybrid anchor+procedural roster: 12-30 anchor tier operator-authored + 58-76 procedural tier rule-generated = ~88 V1 NPCs scaling to 1,000-5,000+ post-V1. Council #6 Decision 1 population-scaling-foundation pass ratified 2026-07-04 targeted the scaling. Post 0189 makes the scaling code-level-operational.

With 2 bundles registered (Cesar 1946 SA West Side Tejano + Yuki 1946 Chicago Japanese-American resettlement) procedural tier NPCs can be instantiated at any scale from either bundle deterministically. 100 NPCs from Cesar bundle. 100 NPCs from Yuki bundle. 1,000 NPCs from Cesar bundle. 5,000 NPCs from bundle mix.

Bundle registry expansion to 10-20 bundles for major place-time-community combinations remains the scaling-substrate work (Marvin 1944 North Philly Black-American + Stas 1942 Cleveland Polish-American + Walt 1947 rural Iowa Danish-American + pin-girl bundles + Detroit Italian-American 1944 + others). Additional refinements to LifelineGenerator (family structure bundle-derived NLP extraction + era archetype auto-selection from bundle era + variance-decomposition audit at scale + cross-product entity migration + LLM-augmented lifeline generation server-side per Room to Life 2026-06-09 memory) remain as sequenced-next opportunities per operator design decision.

## Sequenced next per operator design decision

Post 0189 closes Council #6 Decision 1 architectural-canonization-but-not-operationalized state gap at code level. Remaining Council #6 work: Decision 3 scale observability + session logger emission wiring (Phase 2.x-7 previously deferred; 1-2 weeks instrumentation scope) + Decision 4 Memory Lanes semantic sufficiency (operator judgment gate).

Character Design Workflow Option C anchor tier state: 3 of 12-30 anchor tier characters at PHASE-7-1F-TRIANGULATION-VERIFIED state (Marvin + Cesar + Yuki all civil_rights_framework_applicable=true). Additional anchor tier authoring (up to 9-27 more per Option C ratification) proceeds via Post 0187 CulturalContextBundle inheritance + plain-vocabulary population pattern with bundle registration as complementary substrate work.

CulturalContextBundle registry expansion target: 10-20 bundles for major place-time-community combinations enables procedural tier population at variety across the game's population target.

Empirical validation at 500-NPC + 1,000-NPC + 5,000-NPC scales per Council #6 population-scaling-foundation pass scope estimate (3-6 weeks) becomes tractable at code level. Post 0189 empirical validation validates 100-NPC scale; extension to 500 + 1,000 + 5,000 involves harness code + measurement infrastructure per Council #6 Decision 3 observability scope.

Framework can now scale to thousands of procedural NPCs deterministically at any scale from registered bundles. Sequenced next per operator design decision.
