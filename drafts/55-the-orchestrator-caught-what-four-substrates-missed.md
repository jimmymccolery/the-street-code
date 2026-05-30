# The orchestrator-class caught what four substrate-class deployments missed

**Author:** Jimmy McColery
**Date:** 2026-05-30
**Status:** SEED STUB — operator-authoring-pending. Topic 82 case study from Pin Paradise accessibility sextupartite arc 2026-05-30. Empirical Topic 82 candidacy advances to FULL CANONIZATION at AR-3.3+ with n=3 cross-arc empirical fires reproducing across ALL 3 Rule 11 deployment scopes.

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

## The seed: what to write about

I had a research prompt with a small but load-bearing error: it said "5 soul-axis HUD elements" when the canonical state of my game design has 4 INPUT axes + 1 OUTPUT scalar (Customer Satisfaction is the multiplier, not an input axis). The prompt seeded the error. Then I ran the same prompt through Gemini Deep Research, Perplexity, and Gemini Pro Extended. All three propagated the 5-axis framing into their tables, their palette mappings, their reasoning. Cross-substrate triangulation gave the comfortable illusion of independent verification — three substrates "agreed" on the framing — and the framing was wrong.

Only the orchestrator-class Claude Web caught it. And specifically: it caught it during execution, by querying project-knowledge directly when it needed the hex values. The first line of its response was *"No hex values in project knowledge — the axes are conceptually locked (4 input: Authenticity, Vibe/Nostalgia, Community, Operations; 1 output: Customer Satisfaction as a multiplier) but HUD colors aren't specified as hex anywhere."* Project-knowledge access did what cross-substrate triangulation couldn't.

## The arc to narrate

1. **The error seed**: Grok turn 2 drafted a prompt for Gemini that said "5 soul-axis HUD elements (Authenticity, Vibe/Nostalgia, Community, Operations, Customer Satisfaction)." Grok was treating Customer Satisfaction as a fifth axis. Plausible reading; canonically wrong.

2. **Three substrate-class propagations**: Gemini Deep Research used "5 soul-axes" in its analysis + TABLE 0 Okabe-Ito mapping. Perplexity used "5 soul-axes" in its analysis + TABLE 3 mapping. Gemini Pro Extended (via the recrafted v2 prompt) used "5 soul-axes" in its analysis + palette mapping. **Three independent substrates, three matching errors, all propagated from the prompt seed.**

3. **Orchestrator-class layer 1 (meta-audit)**: Claude Web reviewed the Gemini Deep Research report at framing-critique time. Caught factual-anchor verification (Steam Machine Verified ✅ + SteamOS June 2025 beta ✅ + Wizard April 2025 launch ✅; January 2026 update flagged ⚠️). Caught the injection-wrapper at end of operator's paste. **Did not catch the 5-axis error at this stage** — orchestrator-class meta-audit operates on the substrate response, not the canonical state.

4. **Orchestrator-class layer 2 (recrafted prompt)**: Claude Web produced a refined v2 prompt addressing the gaps (two-layer architecture directive + verify-don't-assert + compute-CVD-don't-assert + build-tester-artifact). **The 5-axis framing remained verbatim in the recrafted prompt.** Orchestrator-class prompt-refinement is constrained by the same horizon as substrate-class — it doesn't have the canonical state in front of it during prompt-drafting.

5. **Orchestrator-class layer 3 (execution with project-knowledge query)**: Claude Web executed the v2 prompt. Needed hex values for the palette. Queried project-knowledge directly. Got the answer: no hex values exist + axes are 4 input + 1 output. **Caught the error during execution, not before, not after — at the specific moment the canonical state mattered for the task.** Then the rest of the response respected the 4+1 distinction.

## The lessons worth surfacing

**Project-knowledge access is structural, not substrate-quality.** Gemini Deep Research is not a worse model than Claude Web. Perplexity is not a worse model than Claude Web. They didn't catch the error because they don't have project-knowledge access to my game design. Claude Web does. The catch isn't about model intelligence; it's about deployment structure. The orchestrator-class advantage compounds across stakes: architectural-deliberation, research-class, and now solo-dev-stakes deployment all reproduce the same structural pattern.

**Three recovery-mechanism layers exist; substrate-class deployment doesn't have access to layers 2 + 3.** Layer 1: dev-assistant verification-gate at prompt-handoff time (operator-curated workflow can include "CC reads canonical state + verifies prompt accuracy before forwarding"). Layer 2: orchestrator-class meta-audit framing critique (post-substrate-response). Layer 3: orchestrator-class execution-time canonical-cite-discipline catch via project-knowledge query (during substrate execution). All three layers are sibling recovery mechanisms; missing any one leaves a gap that prompt-seeded errors can exploit.

**Cross-substrate triangulation has a specific failure mode that's not "the substrates disagree."** It's "the substrates all agree because they all read the same poisoned input." The failure is invisible at the triangulation surface — three independent sources converging looks like exactly what cross-substrate triangulation is supposed to produce: high-confidence load-bearing finding. The triangulation discipline doesn't surface that the convergence reflects the input, not the underlying reality. Recovery requires either pre-deployment verification (layer 1) or orchestrator-class execution (layer 3).

**The empirical pattern reproduces across ALL three deployment scopes the framework recognizes.** Architectural-deliberation scope (PL-10 Council with N=4 2026-05-28 evening): Claude Web R2 refused substrate-class research output and self-classified as orchestrator-class. Research-class scope (city-sim cross-product 2026-05-29 closing-arc): Claude Web produced meta-research artifact instead of substrate-class research. Solo-dev-stakes scope (Pin Paradise accessibility 2026-05-30): Claude Web meta-audited + executed + produced tester artifact + caught canonical 4+1 distinction. **Three different topics, three different stakes levels, same structural pattern. n=3 cross-arc reproduction. The candidacy is now ready for full canonization at the next architecture-revision session.**

## Why this matters

For solo operators deploying AI-assisted research workflows: don't treat all AI deployments as interchangeable. Substrate-class deployments are good at generating research output from prompts. Orchestrator-class deployments add structural capabilities — project-knowledge query, code execution, cleaned-prompt production, structured-handoff documents, factual-anchor verification — that catch errors substrate-class can't. The most thorough cross-substrate triangulation is incomplete without at least one orchestrator-class layer.

The cost of skipping the orchestrator-class layer is invisible: you don't know what you missed because the substrate-class deployments don't surface the gap. Three substrates agreed on the 5-axis framing. I would have shipped the wrong canonical interpretation into my V1 palette decisions if I hadn't run the orchestrator stage. The framework calls this Topic 82, and after today's empirical evidence, it's about ready to become Rule 16.
