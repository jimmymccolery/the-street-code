# Substrate roles: why I use different AI substrates for different research phases

**Author:** Jimmy McColery
**Date:** 2026-05-31
**Status:** Methodology process-narrative on substrate-role specialization in solo AI-assisted research; observations from a multi-cycle research workflow with n=2 empirical fires on the substrate-role specialization pattern

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

The default way to use AI substrates for research is to pick one substrate and run all phases of the research through it. The substrate produces the brainstorm, the citations, the synthesis, the deliverable. The operator reads the substrate's output and accepts or rejects it. The workflow is simple, the operator-attention cost is bounded, and the output quality is whatever the substrate's strengths and blind spots produce on the specific research question.

This works for a wide class of research scopes where any one capable substrate produces adequate output. It breaks down for research scopes where different phases of the research need different substrate capabilities. A scope that requires generative breadth at the brainstorm phase, citation rigor at the verification phase, and quantitative anchoring at the empirical-validation phase will not be served equally well by any single substrate, because the substrate that's strongest at one phase is not necessarily strongest at the others.

This post documents the substrate-role specialization workflow I've developed for research scopes where phase-by-phase substrate strengths matter, with two empirical fires from bowling-industry historical research that demonstrated the pattern producing measurably better output than single-substrate work would have.

## The phases that have different substrate-fit profiles

Any substantive research arc has phases. The phases differ in what they need from a substrate.

The **brainstorm phase** wants generative breadth. The operator surfaces a research scope; the substrate produces candidate angles, historical anchors, mechanism hypotheses, and adjacent connections. Quality here is measured by the number and creativity of the candidates surfaced; citation rigor is not yet load-bearing because the candidates will be verified later. A substrate that's strong at brainstorming will produce a wide range of candidate angles including some that turn out to be wrong; the wrongness gets caught at later phases. A substrate that's weak at brainstorming will produce a narrow range of obvious candidates, missing the non-obvious connections that would have surfaced the most interesting research arcs.

The **citation phase** wants research rigor with primary-source attribution. The operator hands the substrate a set of claims that need to be backed by citations; the substrate retrieves citation candidates from its training data and surfaces them for verification. Quality here is measured by the proportion of citations that point to real primary or near-primary sources and the precision of the source attribution. A substrate that's strong at citation work will produce citations with verifiable provenance; a substrate that's weak will produce plausible-looking citations that turn out to be hallucinations on inspection. The all-AGREE pattern documented in Post 58 is one specific failure mode at this phase.

The **quantification phase** wants research rigor with numerical anchoring. The operator hands the substrate a set of qualitative claims that need to be anchored by specific numbers (dates, dollar amounts, population counts, percentages). The substrate retrieves quantitative anchors from its training data, attributes them to sources, and assembles them into the kind of data tables that turn qualitative claims into empirically defensible ones. Quality here is measured by the accuracy of the numbers and the cross-source convergence on each anchor. Substrates that handle this phase well tend to be different from substrates that handle brainstorming well; the two capabilities draw on different training emphases.

The **ingestion phase** wants synthesis with canonical-state integration. The operator hands the substrate the accumulated outputs from prior phases plus the project's canonical state; the substrate produces the integration that converts research output into design-document content or implementation-spec content. Quality here is measured by the integration's coherence and the absence of contradiction against existing canonical state. This phase is the most operator-context-heavy and tends to favor substrates with strong project-knowledge handling capability.

Each phase has a different fit profile. The substrate that's strongest at one is not necessarily strongest at another. A workflow that routes each phase to the substrate best fit for it produces better aggregate output than a workflow that runs every phase through whatever single substrate the operator defaulted to.

## The first empirical fire

My first deliberate use of substrate-role specialization was during a bowling-industry historical research arc covering vendor relationships across the 1950-2026 window. The research scope included equipment manufacturers (Brunswick, AMF, Nu-Line, Kegel, multiple smaller players), lane oil pattern technology, demographic shifts in bowler population, regulatory changes at the American Bowling Congress and later USBC, and the major business-history milestones across the seven-decade arc.

The brainstorm phase ran through a substrate I'll call the generative-breadth substrate. The substrate produced a comprehensive candidate list: which equipment manufacturers mattered at which decade, which regulatory shifts affected the industry, which cultural events surfaced in the secondary literature, which adjacent industries (commercial real estate, family-leisure economics, broadcast television, sports endorsements) intersected the bowling industry's arc. The substrate's output for this phase was wider than any single search query would have produced; many of the candidates were known to me already, but several were genuinely novel and turned out to anchor important research threads (the 1981 Volcker shock connection that became Post 47; the 1962 financing bubble that became Post 46; the 1964 Don Carter endorsement that became Post 53). The brainstorm substrate's generative breadth was the load-bearing capability for this phase.

The citation phase ran through a substrate I'll call the research-rigor-with-citations substrate. The candidates from the brainstorm phase became the input; the substrate's job was to produce citation candidates for each. The substrate produced a document with several hundred citation candidates spanning industry trade press, academic sports-history surveys, business-history journals, museum archives, and primary newspaper sources. Many of the citations checked out under direct verification; some did not (covered in Post 58's hallucination-catch cluster). The citation phase produced an order of magnitude more candidate citations than I would have surfaced through unstructured search; the verification overhead was real but bounded.

The quantification phase ran through a substrate I'll call the research-rigor-with-quantification substrate. The qualitative claims that survived the citation phase became the input; the substrate's job was to anchor each surviving claim with specific numbers and cross-source confirmation. The substrate produced a quantitative anchor table covering AMF Pinspotter install counts by year, Brunswick stock prices across the 1957-1965 window, prime rate trajectories through 1981, league participation numbers from the 1979 peak through 2010, Bowlmor acquisition transaction values, USBC string-pinsetter approval timeline. The specific numbers that survived cross-source verification anchored the bowling-economics post series (Posts 45-47) at the level of empirical detail those posts required.

The ingestion phase ran through a substrate with project-knowledge access to the bowling-alley tycoon sim's design document. The substrate's job was to integrate the verified research findings into the design document's chronological-mode content, distinguishing what was load-bearing for V1 from what was deferred to post-V1 expansion. The integration was the operator-context-heavy work that the prior three phases had been building toward.

The aggregate output was substantively better than any one substrate could have produced. The brainstorm phase's breadth surfaced anchors I would have missed; the citation phase's rigor caught hallucinations before they entered canonical state; the quantification phase's specificity gave the resulting posts their empirical anchor density; the ingestion phase's project-knowledge integration produced design-document content that aligned with existing locks. No single substrate handles all four phases equally well; the substrate-role specialization workflow routed each phase to the substrate best fit for it.

## The second empirical fire

The second fire was during a separate research arc, several weeks later, covering Web Worker architecture patterns for running Rapier physics in the bowling-sim project. The scope was smaller (one architectural surface rather than seven decades of industry history) but the substrate-role specialization pattern reproduced.

The brainstorm phase produced candidate architectural patterns (multiple-Physics-providers, single shared Physics with worker-thread offload, software-layer collision filtering, fallback to main-thread Rapier with throttling). The generative-breadth substrate surfaced the candidates with rationale for each.

The citation phase produced library-and-framework citations for each candidate (the @react-three/offscreen wrapper for OffscreenCanvas; the comlink library for worker-thread messaging; the Rapier Rust docs on collision-groups encoding; specific Next.js bundler-interaction documentation). Some citations checked out; some did not. The catch documented in Post 58 (the @react-three/offscreen recommendation that two alternative substrates rejected on three convergent grounds) happened at this phase.

The quantification phase was less load-bearing for this scope because the research question was qualitative-architectural rather than quantitative-empirical. The substrate-role workflow allows for phase-skipping when a phase is not load-bearing for the specific scope; quantification got skipped, and the next phase consumed the surviving citation candidates directly.

The ingestion phase produced the architectural decision document that became Post 55's collision-groups bit-encoding documentation. The substrate-role specialization workflow was the operational scaffolding under that final post; the post itself stands on the aggregated output that the workflow produced.

Two fires, n=2 cross-cycle reproduction, both at research-class scope but with different substantive content. The pattern was the same: phases routed to substrate-fit; aggregate output measurably better than single-substrate work would have produced; verification work bounded because each phase's verification scope was contained to that phase's output.

## What substrate-role specialization is not

The pattern is not "use more substrates." More substrates without role specialization produces more output to integrate with worse signal per substrate-call. The cost of the workflow comes from operator-attention to coordinate across substrates; that cost is justified by the role specialization's quality improvement, not by the multiplicity of substrates per se.

The pattern is not "the same substrate at every phase, just running multiple times." A single substrate run multiple times against the same question produces correlated outputs with the substrate's blind spots replicated across runs; the multiplicity does not surface what the substrate's blind spots hid. Different substrates at different phases produce uncorrelated blind spots that catch each other's misses.

The pattern is not "the same substrate at every phase with different prompts." Prompt variation within a single substrate produces some variation in output but the substrate's underlying training and reasoning patterns persist across prompt variations. Cross-substrate variation surfaces broader differences than within-substrate prompt variation does.

The pattern is not "every research arc needs this workflow." Lighter-weight research scopes (specific factual queries, well-bounded technical questions, single-decision recommendations) do not justify the operator-attention cost of multi-phase substrate routing. The workflow is for substantive research arcs whose value justifies the coordination overhead.

## What it requires of the operator

Substrate-role specialization is operator-attention-heavy. The cost is:

The operator has to maintain a current sense of which substrates are strongest at which phases. Substrate capabilities shift over time as the underlying training and deployment updates evolve; an assignment that was correct six months ago may not be correct now. The operator who routes phases to substrates without periodic re-evaluation will be running stale routing decisions.

The operator has to coordinate substrate outputs across phases. The brainstorm phase's output becomes the citation phase's input; the citation phase's output becomes the quantification phase's input; the operator is the integration agent between phases. Each handoff is operator-attention-intensive because the operator needs to read each substrate's output thoroughly enough to construct the next substrate's input.

The operator has to verify the integration at the ingestion phase against the project's canonical state. The ingestion substrate produces synthesis; the operator validates that the synthesis does not contradict existing canonical state. This is the same operator-context-heavy work the ingestion phase is built for, but the operator is the final validator regardless of which substrate did the substrate-side integration.

The cost is real. The benefit is that the research-class output is measurably better than single-substrate work would have produced. For research scopes where the output quality matters enough to justify the operator-attention investment, the substrate-role specialization workflow is one operational pattern worth applying.

## What I'm not claiming

- I'm not claiming the four-phase decomposition is the only useful phase structure. Different research scopes have different natural phase structures; the brainstorm-citation-quantification-ingestion decomposition fits the empirical research arcs I've been running but other arcs might decompose differently (e.g., a code-generation arc might use a brainstorm-prototype-test-integrate structure with different substrate-fit profiles).

- I'm not claiming substrate capabilities are stable across time. Substrates evolve; a substrate that was strongest at brainstorming six months ago may not be the strongest brainstormer now. The substrate-role specialization workflow needs periodic re-evaluation to maintain its routing accuracy. The current routing I use is current as of recent cycles; future cycles may shift the assignments.

- I'm not claiming the substrate-role workflow is the only way to produce quality research output. Single-substrate workflows with disciplined verification produce adequate output for many scopes. The substrate-role workflow is specifically for scopes where phase-by-phase substrate strengths matter; for scopes where they don't, simpler workflows suffice.

- I'm not claiming the operator-attention cost is universally worth it. The cost is substantial for any non-trivial research arc. For research arcs whose output is low-stakes or short-lived, the cost exceeds the benefit. The pattern is for research arcs whose output enters canonical state and gets compounded against by downstream work; the cost justifies the benefit specifically there.

- I'm not claiming this is a novel methodology. Multi-substrate workflows have been part of the AI-builder community discussion since the rise of capable substrates for research-class tasks. What I'm adding is the specific four-phase decomposition I use and the empirical observation across two arcs that substrate-role specialization produced measurably better output than single-substrate work would have.

## What I am claiming

Different AI substrates have different capability strengths at different research phases. A workflow that routes each phase to the substrate best fit for it produces aggregate research output that is measurably better than single-substrate work would have produced. The substrate-role specialization is constructive (leveraging substrate-class strengths) rather than defensive (catching substrate-class failure modes); it complements the defensive catch mechanisms documented in earlier posts (Posts 50, 58, 60) by addressing the upstream question of where to route phases in the first place rather than the downstream question of how to catch errors after the routing.

The four-phase decomposition that fits my research arcs (brainstorm + citation + quantification + ingestion) is one specific phase structure. Other research scopes might use different decompositions. What's common across decompositions is that any substantive research arc has phases with different substrate-fit profiles; aligning routing to fit profile is the load-bearing operational discipline.

The empirical record this post stands on is two research arcs (bowling-industry historical research producing Posts 45-47 + 53 + 56; Web Worker architecture research producing Post 55) where the substrate-role specialization workflow was applied. Both arcs produced output that the verification mechanisms documented in Posts 50, 58, and 60 validated as substantively better than single-substrate work would have produced. The pattern's broader generalization across other research scopes and other operators is the empirical extension worth watching.

For solo AI-assisted researchers reading this: if your current workflow defaults to running every research phase through whatever single substrate you reach for first, the empirical record suggests considering whether different phases of your research have different substrate-fit profiles and whether routing each phase to the substrate best fit for it would produce better aggregate output. The cost is operator-attention to coordinate across substrates; the benefit is research-class output quality that single-substrate work cannot match for research arcs whose phase-by-phase substrate strengths matter. The trade-off pencils out for any research scope whose output enters canonical state and gets compounded against by downstream work.
