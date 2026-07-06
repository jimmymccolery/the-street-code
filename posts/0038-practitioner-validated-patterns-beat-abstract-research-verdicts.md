<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0038
title: Practitioner Validated Patterns Beat Abstract Research Verdicts How a Codrops Demo Shipped My PS1 Shader
date_published: 2026-05-24
status: published
superseded_by: none
domain: Methodology finding that pre-validating architecture against shipped practitioner code (Codrops PS1 shader demo) beats implementing directly off abstract research verdict (Grok custom ShaderMaterial recommendation)
project_scopes: pin-paradise, street-code-methodology
cc_task_relevance: substrate-methodology, methodology-research, verification-validation
phase_binding: Phase-1, era-independent
discipline_family: Rule-11-substrate-specialization, verify-against-canonical-files
canonical_rule: When research surfaces architectural intent but practitioner code surfaces implementation detail let architecture be pre-validated against shipped practitioner code Phase A surface check reads what practitioners actually shipped
load_bearing_claims:
  - Pass 1 six iterations vs Pass 2 six commits zero reverts asymmetry is methodology finding not architectural difficulty
  - Grok Pass 2 verdict said implement custom ShaderMaterial from scratch (architecturally sound but reinvents MeshLambertMaterial)
  - Codrops React-Three-Fiber demo showed onBeforeCompile extension of built-in material producing shorter path
applicability_triggers:
  - CC receiving research substrate recommendation for architectural pattern
  - CC deciding whether to implement off research verdict directly or Phase A check against shipped code first
  - CC building shader/rendering work where documentation is often stale
mechanism_details:
  - RoomToLife chair-prototype shader spike 2026-05-15 to 2026-05-16
  - Two-pass shader: screen-space posterize/dither/gamma + vertex-level snap and Lambert with flatShading
  - Grok cited Liutikov + Heckel + Codrops as three practitioners plus one architectural pattern
cross_refs:
  - Post 0036 PKCE magic link (adjacent RoomToLife work)
  - Post 0039 cross-substrate triangulation
-->

# Practitioner-Validated Patterns Beat Abstract Research Verdicts: How a Codrops Demo Shipped My PS1 Shader

**Author:** Jimmy McColery
**Date:** 2026-05-24
**Status:** Single methodology finding with a concrete shipped-feature anchor; n=1 within-session evidence + cross-substrate convergence; the rule generalizes wherever research surfaces architectural intent but practitioner code surfaces implementation detail.

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

## What I was building

In mid-May 2026 I was shipping the chair-prototype shader spike for RoomToLife (user-facing name: "My 90s Bedroom"), a personal cozy-room project building toward a December 2026 V1. The look I wanted was Dreamcast-era 1999, not modern-rendering 2026: chunky polygons, hard per-vertex shading, subtle pixel jitter at vertex projection, posterized lighting. The visual signature mattered because the whole product is a 90s evocation; getting the rendering wrong would break the era from the first frame.

The shader stack splits into two passes. Pass 1 is screen-space: posterize the lit color, optional Bayer dither, gamma curve to approximate CRT-era encoding. Pass 2 is vertex-level: snap each vertex's projected position to a low-resolution grid (the classic PS1 wobble), use per-vertex Lambert lighting with `flatShading` for hard polygon edges. Pass 1 is the surface treatment; Pass 2 is the geometry treatment. Both ship together to produce the signature.

I went through both passes across a single super-session on 2026-05-15 through 2026-05-16. Pass 1 took six iterations to land; Pass 2 shipped in six commits, zero reverts, zero recovery commits. The asymmetry isn't a story about Pass 1 being harder than Pass 2 architecturally. The asymmetry is the methodology finding this post is about: when I let the architecture for a pass be pre-validated against actual shipped practitioner code instead of against an abstract research verdict, the build went straight.

## The research verdict

Mid-Pass-1, after two visual-eval failures on the boombox prototype, I paused for a Grok research arc. Grok covered both Pass 1's gamma-curve hypothesis (validated, high confidence) and Pass 2's vertex-level architecture (described in nine research-scope sections). For Pass 2 specifically, Grok's recommendation was: implement a custom `ShaderMaterial` from scratch that replaces the GLB asset's built-in material. The reasoning was architecturally sound. A custom `ShaderMaterial` gives you full control over the lighting model, vertex projection, and per-vertex interpolation; you can implement per-vertex Lambert and NDC vertex snap directly without fighting the built-in pipeline.

Grok cited references: Roman Liutikov's PS1-style Three.js work, Heckel's PS1 vertex-jitter writeup, a Codrops article on PS1-inspired shaders for React-Three-Fiber (`react-three-fiber` is the React renderer for Three.js, the WebGL library underneath). Three named practitioners; one stated architectural pattern (custom `ShaderMaterial`).

If I had implemented Pass 2 directly off the Grok verdict, I would have written a custom `ShaderMaterial` from scratch, mapped my GLB assets' materials onto it manually, and worn the consequences. The implementation is possible. It's also a meaningful amount of code, and Three.js's built-in `MeshLambertMaterial` already implements per-vertex Lambert with quality lighting math; rewriting it to add vertex snap is bringing a typewriter to a printer fight.

## The Phase A surface check

Before implementing Pass 2 I asked Claude Code to do a Phase A pass on the cited references. Phase A in my workflow means: read what the practitioners actually shipped, not what the research summary claims they shipped.

When CC examined the cited references, the Phase A check surfaced a divergence. Codrops's article (*"How to Create a PS1-Inspired Jitter Shader with React-Three-Fiber"*, published 2024-09-03) read as using Three.js's `onBeforeCompile` hook to patch the shader source of the built-in `MeshLambertMaterial` at compile time, rather than a custom `ShaderMaterial` from scratch. The patch injects vertex-snap math into the existing vertex shader and adjusts the lighting interpolation to behave as flat per-vertex. The base material's lighting pipeline, asset binding, GLB-material compatibility, and shader-permutation handling all stay intact; the patch surgically modifies the parts that need to be different.

Roman Liutikov's Three.js PS1 work read as using the same pattern. Same `onBeforeCompile` hook, same patch-strategy against the built-in material, same survival of the base material's downstream behavior. Two independent practitioners, neither citing the other, converging on the same concrete implementation per CC's Phase A read. Different from Grok's verdict, which had described the same architectural intent (vertex snap + per-vertex Lambert + flat shading) but via a custom `ShaderMaterial` rather than the `onBeforeCompile` patch.

The convergence was the load-bearing signal. Two practitioners with no obvious shared author pipeline, both shipping production code for the same aesthetic on the same renderer, both reaching for `onBeforeCompile` rather than the architecturally-purer custom-material approach. That isn't a coincidence; it's an implementation pattern that's been validated against the actual constraints (GLB compatibility, asset-binding ergonomics, shader-permutation matrix, compile-cache reuse) that production code has to handle and demo code doesn't.

## The decision

I went with `onBeforeCompile`-on-`MeshLambertMaterial`. The decision was something like: when two independent practitioners ship the same implementation and a research verdict describes a different implementation, weight the practitioners. The research is reasoning about what should work architecturally; the practitioners have already discovered what does work operationally. The two aren't symmetric. Practitioner code carries the empirical residue of the integration problems the research verdict can't enumerate from outside the work.

This isn't a general claim that practitioners are right and researchers are wrong. The two roles produce different kinds of evidence. Research surfaces the architectural intent (what the shader needs to do: vertex snap, per-vertex Lambert, flat shading). Practitioner code surfaces the implementation pattern that actually ships under production constraints (how to do it: patch the built-in material rather than rewrite it). When they agree on both, you have one consolidated direction. When they diverge on implementation, the practitioner pattern is the load-bearing input because it's the one that already carries the contact with reality.

The discipline that made the decision land cleanly was the Phase A surface check: before implementing, ask the execution substrate to read the actual practitioner code that the research verdict cites. The Phase A check is a few minutes of work and it caught a divergence that would have shaped every Pass 2 commit downstream. Without it, Grok's verdict would have read as authoritative and I would have implemented the harder pattern.

## The result

Pass 2 went straight. The execution arc, six commits total:

- **B1 (commit `01b9699`):** DreamcastMesh component wired into the chair prototype; first GLB asset bound; `onBeforeCompile` patch applied.
- **B2 first attempt (commit `d033bf0`):** scene composition + camera kept; operator visual eval at toggle: *"This is much more in-line with what I have in mind."*
- **B2 vertex-snap bump (commit `1eff0be`):** raised vertex snap to 640×480 NDC for subtler silhouette quantization after operator caught a too-extremely-applied artifact on the previous tune.
- **B2 cache-key reconcile (commit `d07b96b`):** updated `customProgramCacheKey` to match the live 640×480 grid; shader permutation cache stays correct.
- **ROADMAP amend (commit `8b71972`):** Pass 2 outcome documented in `ROADMAP.md`; gating criterion satisfied on desktop and mobile.
- **Decision 2 Option B outcome (commit `f513e62`):** Phase 5 implementation proper unblocked per the gating criterion's pass-with-caveats outcome.

Six commits, zero reverts, zero recovery commits. By contrast, Pass 1 had taken six iterations including one explicit recovery commit (`8f167e3`) to back out an over-correction stacked from three compounded changes. The Pass 1 arc was applying a screen-space recipe somewhat blindly; the research arc happened mid-Pass-1 after two empirical failures had already burned iterations. Pass 2's arc was applying a practitioner-validated pattern from the start, with the architecture pre-validated against actual shipped code.

I'm not claiming the two passes were comparable in implementation difficulty. They weren't; Pass 2's vertex-snap math is in some ways simpler than Pass 1's gamma-curve tuning, and the practitioner pattern delegates the lighting model to the built-in material so you don't have to maintain it yourself. But the iteration-count asymmetry maps to the methodology asymmetry: when the architecture is pre-validated against shipped practitioner code, the build doesn't need to discover what works during the build.

## The rule

Research validates *what* to do; practitioner code validates *how*. When research and practitioner code converge on both layers, you have a consolidated direction worth a high prior. When they diverge on the *how* (research describes one implementation, two independent practitioners ship a different one), the practitioner pattern is load-bearing because it carries the empirical residue of the integration constraints research can't enumerate from outside the work.

The discipline that catches the divergence is cheap. Read the practitioner code the research cites, before implementing the research's described pattern. The cost is a few minutes per cited reference; the benefit, when divergence exists, is avoiding the harder implementation path. I caught one divergence this session; the divergence shaped every Pass 2 decision; the savings compound across the rest of the Phase 5 work that Pass 2's architecture unblocks.

The convergence threshold matters too. One practitioner using a pattern is interesting; two independent practitioners using the same pattern is strong signal. The convergence rules out coincidence (one practitioner could be reasoning from the same imperfect template the research draws from); it rules out shared author pipeline if the practitioners are in different communities (Codrops is a React-focused tutorial site; Roman Liutikov publishes his own Three.js explorations on personal channels). Independence + convergence is the load-bearing combination.

## What I'm not claiming

- I'm not claiming the Grok research verdict was wrong. It was architecturally reasonable; a custom `ShaderMaterial` from scratch would have worked. It just wasn't what the practitioners had actually shipped, and the implementation distance between "architecturally reasonable" and "what production code does" is exactly the territory where practitioner evidence beats research evidence.
- I'm not claiming the practitioners are right because they're practitioners. The argument is about the kind of evidence they produce, not about a priesthood of execution. Practitioner code has been shaped by integration constraints that any post-hoc summary necessarily smooths over; the residue is what makes it load-bearing for an implementation decision.
- I'm not claiming two-practitioner convergence is sufficient evidence to skip Phase A. It's necessary signal but not sufficient justification; the Phase A surface check is what actually verified the convergence. Without reading the code, "Codrops + Liutikov both use this pattern" is itself a claim that needs verifying.
- I'm not claiming this generalizes outside of code. The pattern (research vs practitioner divergence on implementation) is well-defined in software because shipped code is publicly inspectable. In domains where practitioner evidence isn't inspectable (strategy, sales, parenting), the convergence signal is weaker and the verification cost is higher.
- I'm not claiming the PS1 shader is shipped to V1. It's shipped to the chair prototype and the ROADMAP `Phase 5` gating criterion is satisfied on desktop and mobile; `Phase 5` implementation proper (the room-scale build) is unblocked but not yet executed. The empirical evidence here is the prototype + the gating outcome, not a shipped V1.

## What I am claiming

When you're about to implement a pattern that an AI research substrate describes, and the research cites concrete practitioner work, spend the few minutes to read the practitioner code before you implement the research's described pattern. The research and the practitioner code may agree, in which case you've consolidated your direction with no additional cost. If they diverge on implementation, the practitioner pattern is load-bearing, and the cost of doing the harder thing the research described is the cost of the build going through the iteration arc the practitioners have already walked. The Phase A surface check that catches the divergence is one of the cheapest disciplines you can apply, and one of the highest-leverage when the divergence is real.

Practitioner-validated patterns beat abstract research verdicts when they diverge. The shipped PS1 shader is the artifact; the methodology lesson is the one worth carrying.
