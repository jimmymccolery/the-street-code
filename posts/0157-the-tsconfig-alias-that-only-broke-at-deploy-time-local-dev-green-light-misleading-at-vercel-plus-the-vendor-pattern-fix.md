<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0157
title: tsconfig Alias That Only Broke at Deploy Time Local Dev Green Light Misleading at Vercel Plus the Vendor Pattern Fix
date_published: 2026-07-04
status: published
superseded_by: none
domain: NEW candidate sub-shape 9 cross-deployment-environment architecture gap; tsconfig alias resolves locally but fails at Vercel
project_scopes: framework-methodology, roomtolife, sim-ai
cc_task_relevance: canonization-propagation-verification, tsconfig-alias-audit, vendor-pattern-fix, cross-deployment-verification
phase_binding: era-independent
discipline_family: Rule 20 candidacy Family A canonization-propagation gap sub-shape 9
canonical_rule: cross-deployment-environment architecture gap sub-shape 9 fires when tsconfig alias resolves locally but fails at Vercel build environment; vendored fix into roomtolife/vendor/sim-ai
load_bearing_claims:
  - n=1 fire Path 2 tsconfig alias sim-ai/*: [../sim-ai/src/*] works locally but fails at Vercel
  - Consumer-deployment build environment scope architecturally distinct from prior 8 sub-shapes
  - Vendored fix into roomtolife/vendor/sim-ai closes the gap
  - Rule 20 Family A n=3 candidate sub-shapes strengthening (subshapes 7 + 8 + 9)
applicability_triggers:
  - tsconfig alias resolves locally but fails at deployed environment
  - Cross-consumer shared code needs deployment-environment verification
  - Vendor pattern preferred over path alias for deployed consumers
mechanism_details:
  - Path 2 tsconfig alias sim-ai/* mapped to ../sim-ai/src/* works locally
  - Vercel build environment does not resolve path outside project root
  - Vendor pattern copies source into roomtolife/vendor/sim-ai for build isolation
  - Cross-consumer verification catches this at deploy time not local dev
cross_refs:
  - Post 0143 (parent canonization-propagation gap discipline family Family A)
  - Post 0154 (sub-shape 7 enumeration-completeness)
  - Post 0158 (Rule 19 discipline extension to operational-diagnostic scope)
  - Memory feedback_canonization_propagation_gap_cross_deployment_architecture_candidate_9th_sub_shape_2026-07-04.md
CC-OPTIMIZED-SUMMARY -->

# The tsconfig Alias That Only Broke at Deploy Time: Local Dev Green Light Misleading at Vercel Plus the Vendor Pattern Fix

**Author:** Jimmy McColery
**Date:** 2026-07-04
**Status:** Single-finding arc; concrete instantiation of the Post 0143 canonization-propagation gap discipline at NEW candidate sub-shape (cross-deployment-environment architecture gap); n=1 empirical fire; Rule 20 candidacy Family A empirical foundation strengthening at third within-arc candidate sub-shape ahead of Council #7 methodology deployment adjudication; broadly reproducible for React/Next.js/TypeScript developers extracting shared code across deployed consumers

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I extracted a shared TypeScript package from one of my Next.js projects this afternoon. Local type check passed. Local test suite passed. Both consumer projects showed clean typecheck output when I updated their `tsconfig.json` path aliases to point at the new shared package. I pushed the changes to GitHub. Vercel started building. Then I refreshed my production site and nothing had changed.

The bug turned out to be that the tsconfig path alias I chose works fine in local development but not at Vercel deployment. Local development sees both projects on my Mac's filesystem; Vercel only clones the consumer repo, so the path alias resolves to a directory that does not exist. Vercel's build failed silently and served the last successful deployment, which was still the code from before my extraction. The whole afternoon of extraction work was invisible to the actual production site.

This post is about the diagnostic sequence that surfaced the failure, the specific tsconfig pattern that broke, the vendor pattern I used to fix it, and the framework methodology observation the fire instantiates. The technical bug is well-scoped. The discipline lesson generalizes.

## The setup

I run a small ecosystem of related products under a single publisher brand. Two of the products are Next.js applications that share substantial cognitive substrate code (a Sim AI system plus a canonical entity registry). Until this afternoon, that shared code lived inside one of the products (I will call it Consumer-A) at `src/lib/sim-ai/` and `src/lib/room-to-life-universe/`. The other product (Consumer-B) did not have this code at all.

The extraction plan was straightforward. Move the shared code to a new first-class project at `~/Projects/sim-ai/`. Have both consumers import from the shared location via TypeScript path aliases. This preserves canonical single-source-of-truth for the shared code plus removes the need to duplicate it across products.

I executed the extraction in about eight minutes. I created the new project structure, moved the files, added a package.json plus tsconfig.json plus vitest config. I updated the tsconfig at Consumer-A to include a path alias mapping `sim-ai/*` to `../sim-ai/src/*`. I ran type check at Consumer-A: passed. I ran the full test suite: 1881 tests passed. I ran the shared package's own test suite at the new location: 472 tests passed. I updated three import sites at Consumer-A via sed. Type check still passed.

Then I added the same tsconfig alias at Consumer-B, ported one component from Consumer-A to Consumer-B, ran type check at Consumer-B: passed. I committed everything, pushed the Consumer-B commits to GitHub, and waited for Vercel to deploy.

The Vercel deployment completed. I refreshed the Consumer-B production site. Nothing new was visible. Anywhere.

## The false positive

My first instinct was that Vercel had not picked up the latest commit. I checked the Vercel dashboard and it showed the deployment as complete with the correct commit hash. I refreshed the site again. Still no change.

My second instinct was browser caching. I did a hard refresh. Same result.

My third instinct was that I had somehow missed a code change locally. I checked git log to confirm the commits included the new component. They did. I checked the file contents to confirm the new dashboard section was there. It was.

The dashboard rendered the way it had before my changes. The new component that consumed the shared package was not visible. This was after Vercel confirmed the deployment succeeded.

The mental model I had been operating under was: my local development environment matches production closely enough that a passing local type check plus passing local test suite implies the code will work at Vercel. Both projects use identical Next.js versions. Both projects use identical TypeScript configurations except for the path aliases I had just added. There was no reason to expect a divergence between local behavior and deployed behavior.

The mental model was wrong. Specifically, it did not account for the fact that Vercel builds run in an isolated filesystem environment where only the consumer repository is available. Any path alias that resolves to a location outside the repository fails at Vercel's build time even when it works fine on my local Mac.

## The diagnostic that broke through

I ran `npm run build` at Consumer-B locally. This is the production build command that Vercel also runs internally. Within a few seconds, the build failed with a specific error.

The error message pointed at a Next.js webpack module resolution failure. The import path `sim-ai/sim-ai/worlds/island/sessionLogger` in my ported component had resolved through the tsconfig alias to `../sim-ai/src/sim-ai/worlds/island/sessionLogger`. Locally, this file existed at that path relative to the Consumer-B project directory because my `~/Projects/` directory has both `sim-ai/` and Consumer-B's project folder as siblings. On Vercel, only Consumer-B's project directory exists in the build environment. The `../` in the path alias resolves to Vercel's own working directory root, which does not contain a `sim-ai/` folder.

The load-bearing observation is that TypeScript's type check does not fetch actual files during compilation. It builds a virtual graph based on the tsconfig configuration. As long as the tsconfig alias is syntactically valid, type check succeeds even when the files it points at do not exist at runtime. Type check is a compile-time verification. Actual module resolution is a runtime verification. They are not the same check.

I had been treating passing type check as evidence that the extraction was working. What passing type check actually meant was that my TypeScript code was internally consistent given the type declarations it referenced. Whether those type declarations correspond to files that will exist at build time in Vercel's environment is a separate question that type check does not answer.

## The fix

I chose the pragmatic fastest fix. I copied the shared package's source into Consumer-B's own repository at `vendor/sim-ai/`. I updated Consumer-B's tsconfig alias from `sim-ai/*: ["../sim-ai/src/*"]` to `sim-ai/*: ["./vendor/sim-ai/*"]`. I ran `npm run build` locally at Consumer-B: build succeeded. The `/prototype/island-npc-test` route was in the compiled output.

I committed the vendored copy plus the updated path alias, pushed to GitHub, and waited for Vercel. Within about ninety seconds, Vercel completed the new build. I refreshed the production site. The new dashboard section rendered. The new component route worked.

The fix accepts a specific tradeoff. The shared package now has two source-of-truth locations. The canonical location at `~/Projects/sim-ai/` is what Consumer-A consumes via `../sim-ai/src/*` path alias (Consumer-A is a local-only project that never deploys to a hosted environment, so the path alias works). The vendored copy at `~/Projects/roomtolife/vendor/sim-ai/` is what Consumer-B consumes via `./vendor/sim-ai/*` path alias plus what Vercel builds. Updates to the shared code need to propagate to both locations. If they diverge, one consumer will use stale code.

I banked the divergence risk as a future architecture task. The workable options are automation via a sync script, structural change via a git submodule (which requires the shared package to have a git remote), publication to an npm registry, or restructuring both projects into a monorepo. Each option has different tradeoffs. The vendor pattern I chose is the immediate mitigation; a longer-term architecture pass will pick the durable solution.

## The framework methodology observation

I run a personal AI discipline framework I call The Street Code. The framework's canonized operational discipline rules include what I have named the canonization-propagation gap discipline family, canonized at Post 0143 as a Rule 20 candidacy at n equals 6 empirical fire sub-shapes plus additional sub-shape strengthening events since.

The prior canonized sub-shapes cover: (1) canonical-file-vs-memory-layer gap; (2) intra-file-append gap; (3) register-classification-layer gap; (4) Rule 19 body drafting seams gap; (5) entry-label semantic-precision gap; (6) regen-timing-gap. Two additional candidate sub-shapes were filed earlier this session: (7) enumeration-completeness gap between foundational-readiness scope and operator-executable-execution scope at framework post publication; (8) tracking surface staleness gap at project canonical tracking surface scope.

This fire files a candidate ninth sub-shape at a distinct scope: cross-deployment-environment architecture gap. The canonization event (architectural pattern extraction of shared TypeScript code with path alias consumption) succeeded at local development scope but failed at deployed consumer build environment scope. The failure surfaced only when I ran the production build locally to reproduce Vercel's build. Type check at local scope passed. Test suite at local scope passed. But the deployment environment's module resolution failed.

The candidate ninth sub-shape is architecturally distinct from prior sub-shapes because it operates at consumer-deployment build environment scope where the deployment environment's filesystem visibility differs from local development's filesystem visibility. Prior sub-shapes operate at framework methodology scope (Rules 1 through 8) or project canonical tracking surface scope (sub-shape 7 and 8). This candidate operates at deployment build-time module resolution scope which is a distinct architectural layer.

The framework's mitigation strategy for this sub-shape is to extend the operational-diagnostic discipline with cross-deployment-environment verification when architecture extraction affects deployed consumers. The specific step that was missing is running the production build locally after the extraction. Running `npm run build` at the deployed consumer's project directory locally would have surfaced the module resolution failure before the push to Vercel. The verification sequence I now use is: type check plus test suite plus production build plus push plus deployed build succeeds.

## What actually shipped

The Path 2 hybrid sequencing execution (shared package extraction plus consumer integration) completed successfully after the vendor pattern fix. Consumer-A imports from the canonical shared package location via path alias and works locally. Consumer-B imports from the vendored copy via path alias and builds cleanly at Vercel. The dashboard at Consumer-B's production site now shows the new component section rendering correctly. The end-to-end architectural pattern is empirically proven at deployed scope.

The candidate ninth sub-shape for the canonization-propagation gap discipline family is filed at the framework's operational memory. Rule 20 candidacy Family A empirical foundation gains a third within-arc candidate sub-shape addition. Council #7 methodology deployment adjudication scope will determine whether these candidate sub-shapes enter canonized rule body at Rule 20 canonization or represent distinct Rule 20 candidacies at different scope architectures.

The framework's operational-diagnostic discipline is extended in the operational memory with the production-build-locally verification step. Future architecture extractions affecting deployed consumers will run this step before push.

## What I'm not claiming

I'm not claiming this failure mode is a Vercel bug. Vercel's build isolation is a legitimate and expected property of any deployment platform that isolates each deployment. The bug is in my mental model that treated local development environment as sufficiently equivalent to the deployment environment. The discipline lesson is on my side, not on Vercel's.

I'm not claiming the vendor pattern is the correct long-term fix. It is the fastest immediate mitigation that accepts a specific tradeoff (divergence risk between two source-of-truth locations). Longer-term options (automation, git submodule, npm registry, monorepo restructure) are architecturally cleaner. I chose the fastest workable option for today because getting the deployment unbroken was time-sensitive; I banked the durable solution for a future architecture pass.

I'm not claiming this discipline lesson generalizes cleanly to all framework language ecosystems. TypeScript path aliases have specific semantics that produce this particular gap between type check and runtime module resolution. Rust workspaces, Python namespace packages, and Java classpath configuration have different semantic layers that fail differently. The specific mechanism I documented is TypeScript-plus-Next.js-plus-Vercel. The general pattern is deployment-environment-differs-from-development-environment and its verification requires environment-specific check, but the specific verification step differs by ecosystem.

I'm not claiming this fire alone canonizes the candidate ninth sub-shape at the framework's operational discipline rule scope. The framework's canonization discipline requires n equals 2 or higher for sub-shape ratification per the Rule-set extension procedure. This post publishes the n equals 1 fire at meta-architecture level. Second-fire strengthening at future cross-deployment-consumer extraction events would confirm whether the sub-shape is stable. Canonization-candidacy adjudication at Council methodology deployment scope depends on how the reproduction pattern strengthens.

I'm not claiming this pattern is novel outside my framework. Deployment-environment isolation and its impact on shared-code extraction are well-known patterns in the broader software engineering discipline. Monorepo tooling (Nx, Turborepo, Lerna) exists specifically because this class of problem is common enough to warrant tooling. What I am claiming is that my framework's operational discipline had not previously named this specific gap between local development verification and deployment environment verification as a canonization-propagation gap sub-shape, and today's fire empirically instantiates it.

## What I am claiming

Local TypeScript type check plus local test suite plus even local development server passing are not sufficient evidence that a shared-code extraction pattern will work at the deployment environment. The load-bearing verification is the production build command executed locally at the consumer project directory. Missing this step produces silent failures at deployment where the deployed build fails and the deployment platform serves the last successful build.

The tsconfig path alias approach for shared-code extraction has a specific scope limitation: it works for local development and for deployment environments that have access to the target directory. It fails for deployment environments (like Vercel's per-project build isolation) that only clone the consumer repository. Consumers deployed to build-isolated platforms require a fix that makes the shared code available inside the consumer's repository at build time.

The vendor pattern (copying shared code into the consumer's own repository at a vendor directory) is a workable immediate mitigation. It accepts divergence risk between the canonical source and the vendored copy. Longer-term options are automation via sync script or git submodule or npm registry publication or monorepo restructure. Each has different tradeoffs; the choice depends on the framework's ecosystem constraints.

The framework's canonization-propagation gap discipline family (Post 0143) gains a candidate ninth sub-shape from this fire: cross-deployment-environment architecture gap. The empirical foundation is at n equals 1 within this session's Path 2 execution. Second-fire strengthening at future cross-deployment-consumer extraction events would confirm whether the sub-shape is stable or an isolated fire. The framework operates at existing canonization-propagation gap discipline scope with this candidate added to the empirical foundation.
