<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0158
title: When Anti-Fabrication Caught the Site URL That Should Have Been Production Rule 19 Discipline Extending from Framework Methodology to Operational Diagnostic Scope
date_published: 2026-07-04
status: published
superseded_by: none
domain: Rule 19 anti-fabrication empirical validation event at operational-diagnostic scope; Comet script Site URL localhost catch as latent production bug detection
project_scopes: framework-methodology, roomtolife, the-street-code
cc_task_relevance: rule-19-anti-fabrication, operational-diagnostic-scope-extension, site-url-verification, comet-diagnostic-script-pattern
phase_binding: era-independent
discipline_family: Rule 19 Marcus Reed Protocol anti-fabrication
canonical_rule: Rule 19 anti-fabrication discipline generalizes from framework methodology scope to operational-diagnostic scope; Comet reporting actual observed value catches latent production bug when actual differs from script-expected
load_bearing_claims:
  - n=1 recurrence-prevention side data point parallel to Council #4 anti-fabrication empirical validation non-replication event canonized at Council #5
  - Comet reported actual Supabase Site URL (localhost:3000) versus script-expected (vercel.app) caught latent production bug
  - Rule 19 discipline extends from framework methodology scope to operational-diagnostic scope architecturally
applicability_triggers:
  - Comet or agent operational-diagnostic script produces observation
  - Actual observed value differs from script-expected value
  - Substrate anti-fabrication reporting catches misconfigured production state
mechanism_details:
  - Comet script pattern v1 at n=4 within-arc (PKCE + Supabase redirect + implementation + DNS)
  - Sibling methodology candidacy at 9 pattern elements
  - Anti-fabrication reporting catches when actual state does not match assumed state
cross_refs:
  - Post 0143 (parent canonization-propagation gap discipline family Family A)
  - Rule 19 Marcus Reed Protocol canonized v1.18
  - Council #4 anti-fabrication empirical validation non-replication event canonized at Council #5
  - Memory feedback_rule_19_anti_fabrication_validation_via_site_url_localhost_catch_2026-07-04.md
  - Memory reference_comet_operational_diagnostic_script_pattern_v1_n4_2026-07-04.md
CC-OPTIMIZED-SUMMARY -->

# When Anti-Fabrication Caught the Site URL That Should Have Been Production: Rule 19 Discipline Extending from Framework Methodology to Operational Diagnostic Scope

**Author:** Jimmy McColery
**Date:** 2026-07-04
**Status:** Single-finding arc; concrete empirical validation event for the framework's Rule 19 Marcus Reed Protocol anti-fabrication discipline at operational-diagnostic scope; n=1 recurrence-prevention side data point parallel to Council #4 anti-fabrication empirical validation non-replication event canonized at Council #5; demonstrates architectural generalization of Rule 19 from framework methodology scope to operational-diagnostic scope

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

An AI-assistant script I asked to update a Supabase configuration setting caught a latent production bug this afternoon. The bug was that the setting had been silently misconfigured on the production instance in a way that would have caused specific edge-case authentication failures. The AI assistant found it because I had explicitly built anti-fabrication discipline into the script's instructions and the assistant took the discipline seriously.

The AI reported what it actually observed instead of what the script had assumed it would observe. The two values differed. Surfacing that discrepancy was what caught the bug.

This post is about the specific catch, the anti-fabrication discipline that enabled it, and the framework methodology observation that the fire generalizes across scope from framework methodology work to operational-diagnostic work.

## The setup

I run a set of related product projects, one of which is a live web application deployed on Vercel with authentication backed by Supabase. Earlier this afternoon I had used an AI assistant script to diagnose why the application's post-authentication redirect landed at the default dashboard rather than the intended destination page.

The diagnostic script executed a systematic audit of the Supabase project configuration. It checked the Site URL setting, the Redirect URLs allowlist, the email templates, the auth hooks, and other authentication-relevant configuration. It reported findings verbatim from the Supabase dashboard.

One of the findings from that diagnostic was that the Site URL setting was currently `http://localhost:3000`. The diagnostic script identified this as a misconfiguration. Its recommendation was to change the Site URL to the actual production URL.

I then drafted an implementation follow-up script that would execute the recommended fix. The follow-up script had a Task Group D covering the Site URL update. That task specified what the current value should be, based on my incomplete recollection of the diagnostic output. Specifically, I had drafted the task under the assumption that the current Site URL was the Vercel-hosted URL for the application. The follow-up script's Task D expectation section noted the assumed current value as the Vercel URL.

When I ran the follow-up script (through a different AI-assistant instance in a different browser session context), the AI reported back with the actual observed values from the Supabase dashboard rather than the assumed values from the script.

## The catch

The AI's Task D report identified the actual old Site URL value as `http://localhost:3000`. It explicitly flagged the discrepancy with the script's assumed value:

The AI's report noted that the deployed instance had been running with a localhost Site URL, meaning authentication callbacks would default to localhost when the intended destination was unreachable. The AI then observed that setting the Site URL to the production URL was a meaningful fix beyond a cosmetic version swap.

The AI could have handled this discrepancy in three ways. Option one: reported the assumed value that the script had documented, quietly making the numbers work. Option two: silently reconciled the discrepancy by adjusting its report to match the script's expectations. Option three: reported the actual observed value plus the discrepancy explicitly, letting me see the gap.

The AI chose option three. That choice caught the bug.

## The bug the catch surfaced

The Supabase Site URL setting is what Supabase uses as a fallback destination when authentication redirect parameters are absent or malformed. If a magic-link callback arrives at the deployed instance without a valid `redirectTo` parameter matching the allowlist, Supabase falls back to Site URL for the redirect destination.

With Site URL set to `http://localhost:3000`, this fallback would attempt to redirect production users to a URL they cannot reach. On my Mac's local development environment, `http://localhost:3000` is my Next.js dev server. On any real user's browser, `http://localhost:3000` is either their own local machine (which typically has nothing running) or an unreachable target.

The specific bug was not always visible because the primary authentication flow at production usually generated valid `redirectTo` parameters that matched the allowlist, so the fallback was rarely triggered. But under edge conditions (malformed URLs, allowlist mismatches, stale session cookies with unusual state, forced browser navigation quirks), the fallback would fire and users would be redirected to `http://localhost:3000` where their browser would fail to connect.

This is the class of bug that surfaces intermittently and is hard to reproduce because it depends on specific edge conditions that most testing does not exercise. It is exactly the kind of latent production bug that goes uncaught by normal QA and only surfaces when a real user in an unusual state encounters it.

## The mechanism

The catch happened because the AI-assistant script I had written for the diagnostic-and-implementation workflow explicitly built anti-fabrication discipline into its instructions. The script instructed the assistant to report exactly what it observed rather than what the script expected, and to explicitly flag discrepancies rather than silently reconcile them.

Specifically, the script's Task Group C structured report format required verbatim configuration values. The script's fallback behaviors handled "not visible" or "content ambiguous" as first-class states rather than error conditions. The script's cover instructions primed the assistant with an anti-fabrication discipline directive at the top: do not fabricate configuration content; report exactly what you see or explicitly note content not visible.

The assistant treated this instruction seriously. When it observed a value that did not match the script's expected value, it did not assume the script was correct and reconcile. It reported the observed value and explicitly noted the discrepancy.

I have canonized this anti-fabrication discipline in my framework at Rule 19, which I call the Marcus Reed Protocol. Rule 19 originally addressed a specific failure mode where AI substrates would fabricate content or attributions under pressure from strict format requirements or from expectations to produce answer-shaped output. The rule's discipline is to require verifiable citation, to explicitly flag content that cannot be verified, and to treat honest declarations of ignorance as first-class outputs rather than as failures.

Prior canonization events for Rule 19 documented six fabrication-axis sub-shapes plus one banked candidate seventh sub-shape at n equals 1. All prior sub-shapes canonized failure events (Rule 19 fires) rather than validation events. Fires document what the discipline is meant to catch. Validation events document what happens when the discipline works as intended.

This catch is a validation event. The anti-fabrication discipline architecturally embedded in the script prevented a specific class of fabrication (assumption-based reporting where the script's expected value would have been reported as the observed value). By preventing that fabrication, the discipline surfaced a latent bug that would otherwise have remained hidden.

## The framework methodology observation

Rule 19's canonized empirical foundation prior to this fire was at framework methodology scope. All the canonized fabrication-axis sub-shapes documented Rule 19 fires during Council methodology deployments, during citation-chain drift events across published posts, during PDF template-placeholder extractions, during cross-source-misbinding events across benchmark-lineage boundaries, and during substrate-fabricates-evidence-of-applying-canonized-discipline events. All framework methodology scope.

This validation event operates at a different scope: operational-diagnostic work covering Vercel plus Supabase troubleshooting. The scope is architecturally distinct because operational-diagnostic work is executing well-defined external configuration audits and modifications rather than deliberating on architecturally novel questions. The failure modes at this scope are also different: rather than substrates fabricating citation attributions or Council methodology contributions, the fabrication risk at operational-diagnostic scope is assumption-based reporting where the substrate reports what the operator's script expected rather than what the substrate actually observed.

Rule 19's architectural discipline generalizes cleanly from framework methodology scope to operational-diagnostic scope. The mechanism is the same at both scopes: substrate reports observed content verbatim, explicitly flags discrepancies with expected content, treats declaration of ignorance as first-class output. What differs across scopes is the failure mode Rule 19 catches. At framework methodology scope Rule 19 catches citation and attribution fabrications. At operational-diagnostic scope Rule 19 catches assumption-based-reporting fabrications.

The framework's canonization record for Rule 19 gains an empirical foundation observation at architectural generalization scope. The rule's discipline is not scope-limited to framework methodology; it applies at any scope where a substrate might fabricate content instead of reporting observed reality. The specific reproduction event today extended the empirical foundation to operational-diagnostic scope at n equals 1.

## The recurrence-prevention side

The framework's Council #4 canonization event documented an anti-fabrication empirical validation for a specific class of fabrication (name-collision fires at cross-cultural discipline audit scope). Council #5 subsequently documented that the same empirical validation event did not replicate under similar conditions at a different Council. Rather than treating this non-replication as failure, the framework canonized the non-replication as a context-dependence data point on what I call the recurrence-prevention side of the discipline record.

The recurrence-prevention side documents what happens when the discipline works as intended plus what happens when the discipline's canonized validation events do not replicate under changed conditions. This is architecturally distinct from the fire-accumulation side which documents empirical failure events.

This catch is a recurrence-prevention side data point for Rule 19 at operational-diagnostic scope. It documents that Rule 19's architectural discipline enabled a specific class of catch under specific script-embedded conditions. Future recurrence at similar operational-diagnostic scopes would strengthen the discipline's cross-scope generalization empirical foundation. Non-recurrence would document scope-limitation conditions.

## What actually shipped

The Supabase Site URL was updated from `http://localhost:3000` to the production URL. The specific edge-case authentication failures that the misconfiguration would have caused are now prevented. The framework's Rule 19 discipline gains an empirical validation event at operational-diagnostic scope which extends the canonized empirical foundation to a distinct scope architecture.

The framework's operational memory added a feedback record documenting the validation event, cross-referencing Rule 19's canonical body plus the specific script pattern that enabled the catch. The record documents that anti-fabrication discipline architecturally embedded in operator-authored substrate scripts prevents a specific class of assumption-based-reporting fabrication that would otherwise silently reconcile discrepancies between operator expectation and substrate observation.

## What I'm not claiming

I'm not claiming this catch could not have happened without Rule 19. Any careful operator running the same diagnostic with any substrate might have caught the same bug through careful reading of the diagnostic output. What Rule 19 does is make the catch systematic rather than dependent on operator vigilance. The discipline is architectural, which means the catch happens even when the operator (me, in this case) is not actively looking for it.

I'm not claiming this fire alone canonizes an architectural generalization of Rule 19 to operational-diagnostic scope at framework methodology rule scope. The framework's canonization discipline requires sub-shape ratification at multiple session arcs plus multiple work classes. This post publishes the n equals 1 validation event at meta-architecture level. Second-fire strengthening at future operational-diagnostic work would confirm whether the generalization is stable. Canonization-candidacy adjudication at Council methodology deployment scope depends on how the reproduction pattern strengthens.

I'm not claiming anti-fabrication discipline in substrate-facing scripts is novel. Requiring substrates to report observed content and flag discrepancies is standard engineering practice at many careful teams. What I am claiming is that my framework's Rule 19 architecturally embeds this discipline as canonical operational rule rather than as ad-hoc guidance, and today's fire is a concrete empirical validation event for the rule extending beyond framework methodology scope where I originally canonized it.

I'm not claiming this catch is the highest-leverage bug prevention my framework produced today. My session today closed several categories of latent bugs in different scopes. The Site URL catch is one specific validation event for one specific rule at one specific scope. Its significance is in the architectural generalization observation rather than in the specific bug it caught.

I'm not claiming the failure mode this catches is limited to Supabase configurations. Assumption-based-reporting fabrication is a general failure mode that can happen whenever a substrate is asked to verify a configuration or state that the operator has an expected value for. The specific mechanism (Supabase Site URL misconfigured as localhost on production) is one instantiation. The general pattern is substrate reports operator's expected value instead of observed reality.

## What I am claiming

Rule 19 Marcus Reed Protocol anti-fabrication discipline generalizes architecturally from framework methodology scope to operational-diagnostic scope. The same discipline that prevents citation-chain drift and PDF template-placeholder extraction and cross-source-misbinding at framework methodology work prevents assumption-based-reporting fabrication at operational-diagnostic work. The rule's mechanism (substrate reports observed content verbatim, flags discrepancies explicitly, treats declaration of ignorance as first-class output) applies across scope architectures.

Anti-fabrication discipline architecturally embedded in operator-authored substrate scripts prevents a specific class of latent bug catch failure. When operator scripts include expected values that turn out to be wrong, substrates without anti-fabrication discipline may silently reconcile the discrepancy. Substrates with anti-fabrication discipline surface the discrepancy, which enables the operator to catch bugs that would otherwise remain latent.

The framework's Rule 19 canonized empirical foundation gains an operational-diagnostic scope validation event on the recurrence-prevention side of the discipline record. The empirical foundation is at n equals 1 at operational-diagnostic scope. Second-fire strengthening at future operational-diagnostic events would confirm whether the architectural generalization is stable. The framework operates at existing Rule 19 canonical scope with this validation event added to the empirical foundation.
