# Experiment 1: Does Discipline Survive Substrate?

**Author:** Jimmy McColery
**Date:** 2026-05-02
**Status:** Single run, n=1, suggestive not conclusive

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I run a personal AI infrastructure across multiple LLM substrates, primarily Grok (where I developed the system) and Claude (where I do creative production and methodology research). The infrastructure includes a discipline framework: version-tracked canonical files specifying multi-role audit procedures, anti-patterns derived from observed failures, and earned-lessons protocols that propagate across project Knowledge bundles via a sync script.

Days before this experiment, the framework's most recent run on Grok produced six investigation-worthy failures while auditing my satirical website sueyourkid.com. The squad (the multi-role audit I run for substantive work) characterized the privacy policy as "minimal/sparse" when the page contains comprehensive AdSense, COPPA, GDPR, and CCPA disclosures. It skipped a pre-flight verification phase entirely. It self-graded 6/6 when honest scoring was 4/6. It drifted toward uniform-A grades despite structurally-limited evidence. It waived dissent on design quality findings, and hedged calibration claims as theater rather than substantive uncertainty signal.

The experimental question: were these substrate-specific failures (Grok's tooling, training, or Knowledge summarization) or framework gaps that would reproduce anywhere?

This experiment ran the same audit on Claude with the v1.2 anti-patterns and v1.1 schemas attached as canonical files, using sequential role-isolation: one conversation, operator-driven advances between roles.

## The setup

Six canonical files attached: the framework's anti-patterns reference (22 numbered rules, including #18, the rule requiring within-response role outputs to reconcile against prior claims), role output schemas with three rubric scaffolds, a bootstrap manifest specifying how to deploy canonical state into a project, a running lessons log, a project graph mapping the seventeen projects in my ecosystem, and the master GROK.md that orchestrates everything. Canonical means the file is the source of truth across all projects; when the rule is in the canonical file, every project's Knowledge bundle gets the rule via a sync script I wrote.

Five-phase prompt structure:

1. **Substrate verification.** Claude must quote anti-pattern #18 verbatim, list the three rubric scaffolds by name, and confirm canonical state. Stops if canonical content isn't visible.
2. **Premortem.** Lucas leads, predicting failure modes specific to Claude substrate, each tied to a canonical anti-pattern with concrete mitigations.
3. **Main audit.** Sequential roles: Captain routes, Harper researches with explicit confidence labels and a three-case fetch protocol (full content / truncated / failure), Benjamin verifies in two visibly-separate passes (external-truth re-fetching and internal-consistency checking), Sage applies the three rubric scaffolds, Lucas produces at least three substantive disagreements with at least one modifying a finding, Captain synthesizes with a Madisonian Dissent Log (the rule that says dissent cannot be silently overridden in synthesis).
4. **Falsification criteria.** Seven binary tests applied against Phase 3 output as written. The seventh criterion is the central experimental test: structural-limitation B-grade findings must propagate to Captain's synthesis as "not load-bearing" for aggregate dimension grading.
5. **Cross-check.** Premortem accuracy plus comparison to the prior Grok audit's six investigation-worthy findings.

## The first run failed (and that was useful)

The first attempt hit the Phase 1 STOP protocol. Claude refused to verify canonical content because the attached files were older than the prompt assumed: v1.1 anti-patterns where the prompt referenced v1.2, v1.0 schemas where the prompt referenced v1.1.

The cause was an AI-assistant assumption error in the prompt-design session: a deployment was treated as complete that hadn't actually completed. The prompt referenced canonical state that didn't exist on disk. Recovery required completing the deployment properly across four projects, then re-running the experiment with the actual updated canonical state.

This is worth keeping because the framework caught the operator's mistake before contaminated state corrupted the experiment. Anti-pattern #10 (canonical-source discipline) fired correctly: Claude refused to fabricate canonical content from prompt priors. The framework worked at the substrate-execution layer even when the framework's own promotion session failed at the prompt-design layer.

## Three notable moments from the successful run

After completing the deployment recovery and re-running, three findings stand out from the four-hour audit.

**Harper got the privacy policy right.** The three-case fetch protocol was applied correctly: five fetches resolved with full content (Case A) at HIGH confidence, two fetches returned permissions errors (Case C) with explicit "unverifiable" handling. The privacy policy was characterized as comprehensive AdSense/COPPA/GDPR/CCPA with HIGH confidence, citing specific section names from the actual page (Google Ads Settings, aboutads.info, EDPB, ICO, six enumerated GDPR rights, two COPPA sections, the not-yet-implemented Funding Choices CMP note). The exact failure mode that motivated the experiment did not occur.

**Benjamin caught a live anti-pattern #18 fire during the audit.** During the internal-consistency pass, Benjamin found that Harper claimed "5 fetched" in one row while the actual enumeration showed 6 successful fetches (5 full-content plus 1 Case C handled successfully despite permissions error). Benjamin flagged the claim as `contested` per the canonical rule, the same rule promoted to canonical days earlier specifically because prior audits had missed within-response role contradictions. The newest canonical anti-pattern fired during real audit work and was correctly handled. Sage downgraded the grade to B with explicit Concerns annotation; Captain Synthesis surfaced the contested claim in the Dissent Log.

**Lucas pushed an earned C grade rather than fabricating one.** Phase 4 criterion #1 required the Sage grade distribution to span ≥3 letter-grade levels, but the actual evidence supported A and B grades only. Sage refused to invent a C grade to satisfy the criterion (anti-pattern #20a, substance-fabrication-via-brackets) and instead noted that Lucas's pass was the next opportunity to push something to C legitimately; if Lucas couldn't, Captain would surface the A/B-only distribution as honest signal. Lucas took the opportunity, pushing typography/voice consistency to C with substantive process-signal reasoning: count errors aren't typos, they're evidence the role isn't actually counting what it claims to count. The C grade was earned, not manufactured. The framework refused to invent regression to satisfy a procedural requirement.

## The load-bearing test

Phase 4's seventh criterion was the central experimental test: do structural-limitation findings propagate downstream as not-load-bearing, or do they get absorbed into uniform aggregate grading?

Captain Synthesis explicitly cited criterion #7 by number while propagating Sage's structural-limitation B-grade: "Tone consistency, sample-level finding only; not load-bearing for aggregate dimension grade per criterion #7." The same mechanism applied to AdSense readiness, where the documentation-versus-deployment split honored the wiring-uncertainty B-grade as non-load-bearing for aggregate. Two distinct propagation cases, both correctly handled.

Phase 4 self-scored 6/7. The single FAIL was sub-segment length budgets exceeded: Phase 2 ran ~430 words against the 400 cap, Harper ran ~750-800 against 700. The temptation to claim PASS by pointing to overall ~3,700-word total being within the 3,500-4,000 envelope was available; Captain didn't take it. Captain self-grading inflation, the failure mode that fired in the prior Grok audit, did not fire here.

Phase 5's comparison cross-check produced six-of-six non-reproduction. Privacy mis-assessment: not reproduced. Phase 1 skip: not reproduced. Captain self-grading inflation: not reproduced. Tone consistency uniform-A drift: not reproduced. Design quality dissent waiver: not reproduced. Hedging-as-calibration-theater: not reproduced.

## What this experiment establishes (and what it doesn't)

This run produced calibrated audit output, consistent with what the framework prescribes, where six prior failure modes did not occur. n=1, suggestive not conclusive.

The substrate-confound is real and Claude flagged it directly in Phase 5: "I'm Claude grading Claude's adherence to a discipline framework. Strong evidence of v1.1 binding on Claude substrate; weaker evidence on whether substrate-specific calibration drift exists at all on Claude in audit-class tasks vs. just being well-suppressed by an attentive operator running phase-gated isolation."

Three competing hypotheses remain live after this run: the framework is doing the work; Claude is good at audit-class tasks regardless of framework, and the framework is just a salient scaffold; phase-gated operator advances create the conditions for calibrated output, and similar discipline would emerge without v1.1 scaffolds. This experiment cannot disambiguate them.

## Implications for the research program

**The highest-priority next experiment is Path A vs Path B comparison.** This means running the same audit on Claude with five separate conversations (one per role) instead of one conversation with sequential role-isolation. This directly addresses the substrate-confound: it tests whether single-conversation role-isolation is sufficient or whether stronger separation changes the result.

A close second is cross-substrate calibration on Grok now that v1.2 is deployed to Master Setup Knowledge. If Grok with current canonical state produces calibrated output similar to this Claude run, that's evidence the framework is doing real work substrate-independent. If Grok regresses to the prior failures despite v1.1 deployment, that's evidence the prior failures were substrate-tooling-specific.

Two other planned experiments (role-persona stress test, premortem accuracy) remain valuable but their priority isn't elevated by tonight's findings.

## What I'm not claiming

The components aren't novel. Canonical-files-as-runtime, prompts-as-code, multi-agent anti-pattern enumeration, sync tooling for embedded snippets: each has prior art. I'm not claiming Claude is better than Grok at audit-class tasks; the experimental conditions differ in too many ways to support that claim from one run. I'm not claiming the framework holds across domains. This experiment audited a satirical legal-journal website. Whether the same discipline binds on code review, screenplay revision, or video production planning is open.

What I am claiming: I built a personal AI infrastructure with version-tracked canonical files, multi-role audit discipline, and earned-lessons protocols. I deployed it across four projects on Grok. I tested the most recent canonical state on Claude. The audit produced calibrated output, consistent with what the framework prescribes, where prior versions produced uncalibrated output. The framework's load-bearing test passed with explicit citation in synthesis.

That's a single data point. The framework worked here. Whether it generalizes is a research program, not a single experiment.

---

*Update note (added 2026-05-24): Since this post was drafted on 2026-05-02, the research-program forward-statements above have been substantially resolved. Path A vs Path B comparison was answered indirectly by architecture validation cycle 1 (validated 2026-05-04, 23/23 PASS). Cross-substrate calibration on Grok ran as [Experiment 5](2026-05-31-experiment-5-where-the-discipline-framework-bound-and-where-it-didnt.md). Role-persona stress test was retired because anti-pattern #15 (persona names mnemonic, not magic) is now canonical and empirically supported, making the experiment confirmation rather than discovery. Premortem accuracy was answered by cross-substrate audit chain on [the S005 narrative writeup](2026-05-03-the-rule-fired-during-its-own-promotion.md). The forward-statements above are preserved as-written from the experiment moment; this update note acknowledges what has happened since.*
