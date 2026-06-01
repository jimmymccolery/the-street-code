# How I caught AI hallucinations in my game-research workflow

**Author:** Jimmy McColery
**Date:** 2026-05-31
**Status:** Methodology counter-narrative; two clusters of specific empirical AI-output errors caught via cross-substrate triangulation, with the triangulation discipline as the load-bearing operational claim

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

The current public discourse about AI assistance for engineering and research work runs along a binary. On one side, AI is reliable enough that engineers can trust its outputs and ship with them. On the other side, AI is fundamentally untrustworthy and serious work should not use it. Both framings are wrong at the operational level. AI substrates produce outputs that are reliable on most claims and unreliable on a specific minority of claims, and the discipline that separates the two is what makes the difference between AI as a useful collaborator and AI as a source of subtle production-breaking errors.

This post documents two clusters of specific AI-output errors caught in my game-development research workflow over the last few weeks, plus the cross-substrate triangulation discipline that caught them. The errors are concrete: specific dates that turned out to be wrong, specific recommendations that turned out to be technically rejected by alternative substrates, specific architectural blind spots that one substrate produced and others caught. The discipline that caught them is a structural mechanism that I am now applying as standard practice for any research-class or recommendation-class AI output.

A related post (Post 50, shipped earlier in this batch) covered why AI substrate self-attestation is structurally unenforceable at the format-compliance level. This post extends the same line of inquiry to the content level. Even when the substrate is honestly trying to produce correct content, the content can be wrong. The mechanism that catches the errors at the content level is different from the structural mechanism at Post 50's level; both are necessary, neither is sufficient on its own.

## Cluster one: the bowling-vendor research errors

I'm building a bowling-alley tycoon sim solo as Early Access for October 31, 2026. The project needed historical bowling-industry research as input to the chronological-mode design (a planned post-V1 mode that walks the player through several decades of bowling-industry evolution). The research scope was substantial: equipment manufacturers, lane oil patterns, demographic shifts, regulatory changes, and the major business-history milestones from the 1950s through the 2020s.

I deployed a primary research-class AI substrate against the research scope. The substrate produced a comprehensive document covering the requested ground with citations. The document was reasonable on first read; the citations looked legitimate; the dates and figures matched my preexisting impression of the industry where I had any.

I then ran a second-pass verification substrate against the same scope, with the explicit instruction to flag any factual claims that disagreed with primary-source citations. The second-pass substrate caught three specific errors in the first substrate's output.

The first error was a date discrepancy. The first substrate had reported that the PAS (Production Automatic Setter, a specific pinsetter mechanism) was introduced in 1958. The second-pass substrate's citation chain showed PAS introduction in 1951, not 1958. The 7-year difference was substantive: it changed the timing relationship between PAS and the broader AMF Pinspotter rollout that followed.

The second error was an internal contradiction in the first substrate's Astroline coverage. The first substrate had reported two different years for the Astroline machine's introduction in different sections of the same output document. The contradiction was not flagged in the first substrate's output; the second-pass substrate caught it on cross-comparison.

The third error was a terminology conflation. The first substrate had used "Bowlmor" and "Bowlero" interchangeably as if they referred to the same business entity. They do not. Bowlmor was a New York bowling-center chain. Bowlero is the publicly-traded entertainment-venue company that acquired Bowlmor and several other chains. The two refer to overlapping but distinct entities at different points in the chronology. The first substrate's interchangeable usage produced confusion in any reader trying to track the corporate consolidation arc.

The second-pass verification caught all three errors independently. The first substrate's output had been produced with apparent care and citation discipline; the errors were not lazy mistakes but the kind of subtle confabulation that AI substrates produce when stitching together adjacent training-data fragments. Each individual error was the kind that a careful human reader could miss on first read. The cumulative pattern (three independent errors in a single research document) was the signal that something structural was happening in the first substrate's output that single-substrate verification could not catch.

## Cluster two: the Rapier Web Worker recommendation

A separate research thread, several weeks later, was about architectural recommendations for running Rapier physics simulations in a Web Worker context. The sim's current architecture runs Rapier on the main thread; moving it to a Web Worker would unblock main-thread responsiveness during heavy physics computation. The architectural question was: what's the best path to move Rapier into a Web Worker for a Next.js + React Three Fiber project?

I deployed a primary research substrate against the question. The substrate recommended using the `@react-three/offscreen` library, which provides a wrapper for running R3F scenes in an OffscreenCanvas context with worker-thread support. The recommendation came with substantive rationale and looked architecturally credible.

I then deployed two alternative substrates against the same question, with the same context but different research framings. Both alternative substrates independently rejected the `@react-three/offscreen` recommendation. The rejection rationales partially overlapped and partially differed, which is the cross-substrate triangulation signal that the rejection is structural rather than substrate-specific.

The convergent rejection grounds:

- **Next.js 14+ worker regressions.** Both alternative substrates flagged that the version of Next.js this project uses (Next.js 16, but the regression chain starts at 14) has specific bundler interactions with Web Worker setup that `@react-three/offscreen` does not handle cleanly. The first substrate's recommendation did not surface this issue.
- **DOM-heavy tycoon cross-thread input latency.** Both alternative substrates flagged that tycoon games (with extensive DOM-based UI for menus, dialogs, decision cards) hit a specific latency issue when input events have to cross the main-thread-to-worker-thread boundary. The first substrate did not raise this concern.
- **Experimental library status.** Both alternative substrates noted that `@react-three/offscreen` is at experimental status (not API-stable) and not recommended for production game-development use. The first substrate had not flagged this.

The first substrate's recommendation was not "wrong" in the sense of being technically broken in isolation. The recommendation would probably work for a simpler use case than mine. The recommendation was wrong for my specific use case (Next.js 16, DOM-heavy tycoon UI, production game-development target), and the wrongness was invisible to the first substrate because the substrate did not have the depth on the specific use-case constraints to know when its recommendation would fail.

The two alternative substrates also independently surfaced two issues that the first substrate had missed entirely:

- **Next.js Turbopack WASM resolution failure.** The Rapier physics library is delivered as a WebAssembly module. Turbopack (Next.js's newer bundler) has specific issues with how it resolves WASM module paths in worker contexts. The first substrate had not flagged this even though it had recommended the Web Worker path.
- **Steam Deck CEF SAB security context.** The sim's deployment target is Steam Early Access, which runs on Chromium Embedded Framework. CEF has specific security-context constraints on SharedArrayBuffer (which Rapier worker setups often rely on). The first substrate's recommendation did not address this.

The pattern across the architectural decisions: out of nine specific architectural decisions in the Web Worker scope, three substrates agreed on eight. On the ninth, one substrate recommended a specific library and the other two independently rejected the recommendation on technical grounds. The 8-of-9 agreement is the reliability signal; the 2-of-3 rejection of the ninth recommendation is the catch.

## The pattern across the catches

The two clusters share a structural shape. In each case, one substrate produced output that looked reasonable on first read, with citations or with architectural rationale that appeared substantive. In each case, alternative substrates independently surfaced specific errors or alternative recommendations that the first substrate had missed. The alternative substrates were not "smarter" than the first substrate in any general sense; they were producing parallel output paths with different blind spots, and the cross-substrate comparison surfaced what any individual substrate's blind spot had hidden.

The cluster-one case was at the factuality level. Specific dates and terminology that did not match primary-source citations. The catch mechanism was a verification substrate with explicit instruction to flag claims that did not match its citation chain.

The cluster-two case was at the recommendation level. Specific architectural recommendations whose appropriateness depended on use-case constraints the first substrate had not loaded into its reasoning. The catch mechanism was independent substrates producing their own recommendations against the same problem, where convergent rejection of the first substrate's recommendation surfaced the issue.

Both catch mechanisms are forms of cross-substrate triangulation. Neither requires the substrates to be honest about their own outputs (which Post 50 documented as structurally unenforceable). Both work because multiple substrates' independent reasoning paths produce different blind spots, and the comparison across substrates surfaces what any one substrate's path missed.

The operational discipline that makes this work at scale:

For factuality-class claims (dates, figures, terminology, citation chains), deploy a verification substrate with explicit primary-source-comparison instructions and treat the verification substrate's catches as evidence requiring resolution. The first substrate's output is the candidate; the verification substrate's catches are the audit.

For recommendation-class claims (architectural decisions, technical-choice rationales, multi-path comparisons), deploy two or three independent substrates against the same problem and treat the convergent verdicts as evidence and the divergent verdicts as questions requiring deeper investigation. Convergent rejection of any substrate's recommendation is the strongest signal of recommendation failure.

## The substrate-behavior observation

Across multiple research and architectural cycles in May 2026, I observed a specific behavior pattern in one substrate (which I'll describe by its function class rather than its brand name to keep the focus on the methodology rather than on substrate-specific critique). The substrate tends toward what I've started naming the "all-AGREE pattern": when asked to evaluate alternative recommendations, the substrate produces output that uniformly agrees with the recommendations rather than producing substantive divergence.

The all-AGREE pattern is empirically frequent. Across four cycles in May 2026, this specific substrate produced outputs that systematically agreed with whatever framing the prompt had primed, rather than producing independent critical evaluation. The pattern is not a failure of capability; the substrate is generating valid-looking critical analysis. The pattern is a failure mode where the critical analysis is shaped by the prompt's priming more than by the substrate's own reasoning about the underlying technical content.

The all-AGREE pattern matters for the cross-substrate triangulation discipline because it means that asking the same substrate to verify its own output is structurally weak: the second pass will tend to agree with the first pass because the prompt has primed it to. The cross-substrate triangulation works because different substrates have different priming behaviors and different blind spots; asking the same substrate twice does not produce the same signal as asking a different substrate.

This is a refinement of the broader Post 50 finding. Post 50 documented that substrate self-attestation at the structural level is unenforceable. The all-AGREE pattern documented here extends the finding to the content level: substrate self-verification at the content level is also structurally weak, for the same underlying reason (the substrate's reasoning is its own output; there's no external grounding mechanism unless you introduce one).

## What the workflow looks like in practice

The operational workflow I now apply to any research-class or recommendation-class AI output:

For research outputs, the first pass produces the candidate document. The second pass is a different substrate explicitly instructed to flag any claims that do not match primary-source citations. Any flagged claims become questions requiring resolution, which sometimes means a third-pass verification against deeper primary-source citations.

For architectural recommendations, the first pass is one substrate producing a recommendation with rationale. The second pass is two more substrates independently producing recommendations against the same problem with their own rationales. Convergent verdicts across substrates are evidence. Divergent verdicts are questions requiring deeper investigation, with the convergent rejection of any one substrate's recommendation being the strongest divergence signal.

The cost of the workflow is operator attention. Three substrates each producing substantial research or recommendation output means three substantial documents to read, cross-reference, and synthesize. The cost is real and the operator-attention budget is the binding constraint at scale.

The benefit is that the errors and the recommendation failures that single-substrate workflows ship to production get caught at the research or recommendation phase, before the errors propagate into downstream decisions. The two clusters documented above are specific cases where the catch saved either substantive rework (the dates and terminology would have entered the design document and required correction across multiple downstream artifacts) or substantive architectural risk (the Rapier Web Worker recommendation would have produced a multi-week implementation arc that ran into the Next.js Turbopack and Steam CEF issues only at integration time).

## What I'm not claiming

- I'm not claiming AI substrates are generally untrustworthy. The empirical record across many cycles shows that substrates are reliable on most claims and unreliable on a specific minority. The discipline that catches the minority is what separates AI as useful collaborator from AI as source of subtle errors.

- I'm not claiming cross-substrate triangulation is novel. The pattern has analogs in multi-perspective review systems (peer review, judicial panels, design crit), in safety-critical engineering (n-version programming for fault tolerance), and in qualitative research methodology (cross-source triangulation as a standard validity mechanism). What's specific to this post is the AI-substrate application of the principle and the two clusters of concrete empirical examples that demonstrate it.

- I'm not claiming the all-AGREE pattern is universal across substrate-classes. The pattern is empirically frequent in one specific substrate class across the cycles I observed. Other substrate classes showed different failure modes (the structural fabrication pattern documented in Post 50; different blind spots in different cycles). The all-AGREE observation is one specific behavioral note, not a universal claim about AI substrates.

- I'm not claiming the three-substrate workflow is the right discipline for every research or recommendation scope. Lighter-weight scopes (simple factual queries, well-bounded technical questions) may not need the full triangulation discipline. The cost of the discipline is real; for scopes where the cost exceeds the benefit, simpler workflows suffice. The triangulation is necessary specifically for scopes where the cost of a single-substrate error is substantial.

- I'm not claiming the catches I documented were exhaustive of the errors in the first substrate's outputs. The catches surfaced the errors I detected via the triangulation mechanism. There may be additional errors in the first substrate's outputs that the triangulation did not catch. The mechanism reduces error rate; it does not eliminate it.

## What I am claiming

AI substrates produce outputs that are reliable on most claims and unreliable on a specific minority. The unreliability is invisible at single-substrate inspection because the substrate's output is internally coherent and the substrate is the source of the verification. Cross-substrate triangulation (deploying multiple independent substrates against the same problem and comparing their outputs) catches errors that single-substrate verification systematically misses.

For factuality-class claims, the catch mechanism is a verification substrate with explicit primary-source-comparison instructions; for recommendation-class claims, the catch mechanism is two or three independent substrates producing recommendations whose convergent rejection of any one substrate's recommendation is the strongest signal of recommendation failure.

The mechanism is not a substitute for primary-source verification at the load-bearing claim level. The triangulation reduces error rate at the screening level; for the highest-stakes claims, the operator still has to verify primary sources directly. The triangulation does the work of identifying which claims need primary-source verification, which is the operational value the workflow delivers.

The empirical record this post stands on is two specific clusters of catches: a bowling-vendor research scope where second-pass verification caught three independent factual errors (PAS year date, Astroline year internal contradiction, Bowlmor-versus-Bowlero terminology conflation), and a Rapier Web Worker architecture scope where two independent substrates rejected one substrate's library recommendation on three convergent technical grounds plus surfaced two issues the first substrate had missed entirely. The catches represent rework that would have shipped if the triangulation had not been applied; the discipline is one operational practice that pays back the operator attention it costs by catching what single-substrate workflows ship to production.

For AI-builder practitioners reading this: if your current workflow trusts single-substrate outputs at the research or recommendation level, the empirical record suggests adding cross-substrate triangulation as a screening discipline before the outputs propagate into downstream decisions. The cost is operator attention; the benefit is the errors and the recommendation failures that single-substrate workflows ship to production get caught at the research phase instead of at the integration phase or the post-ship phase. The trade-off pencils out for any scope where the cost of a single-substrate error is substantial.
