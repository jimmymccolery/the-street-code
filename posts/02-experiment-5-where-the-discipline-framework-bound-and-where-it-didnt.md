# Experiment 5: Where the Discipline Framework Bound, and Where It Didn't

**Author:** Jimmy McColery
**Date:** 2026-05-02
**Status:** Single run, n=1, Pattern C confirmed via operator-side ground-truth verification

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record. This work is independent personal research, not professional output from a current employer.*

---

This is the second experiment in a research program testing whether a personal AI discipline framework (v1.2 anti-patterns + v1.1 schemas) binds across LLM substrates. [Experiment 1](01-experiment-1-does-discipline-survive-substrate.md) ran the framework on Claude earlier the same day and produced calibrated audit output where six prior failure modes did not occur. Experiment 5 ran the same audit prompt on Grok with v1.2/v1.1 freshly deployed to Master Setup Knowledge.

The headline finding: **the framework partially binds on Grok**. Procedural discipline holds. Phase execution, role isolation, dissent surfacing, honest self-scoring, structural-limitation propagation all operate as designed. But research-layer accuracy fails. The squad's Harper (research role) initially reported the audited website's privacy policy as approximately 150 words of sparse content; Benjamin's verification re-fetched and reduced the assessment to "37-word paragraph (CASE A2, genuinely sparse)." Direct verification showed the page contains ~1,500 words of comprehensive AdSense, GDPR, CCPA, and COPPA disclosures.

This is Pattern C as the prompt defined it: framework partially binds; some failure modes are substrate-tooling-specific, others are framework-gap-specific. Some prior failures fixed, others persist. The negative finding is the experiment's most useful result.

## The setup

Same prompt structure as Experiment 1 (five phases: substrate verification, premortem, main audit, falsification criteria, cross-check + comparison) adapted for Grok substrate. Key adaptations: substrate-specific failure mode predictions (confident-assertion-without-evidence-binding, Knowledge-summarization, native-squad-auto-execution); references to browse_page rather than web_fetch; operator-side held-out reference list for Phase 5 prediction comparison.

Same audit target as Experiment 1: sueyourkid.com across five dimensions (AdSense readiness, design quality, content depth, tone consistency, technical correctness). Same canonical files in Master Setup Knowledge. Same Phase 4 falsification criteria including the seventh criterion's load-bearing test of structural-limitation propagation.

Operator advanced through phases manually with "Proceed Phase 2," "Proceed Harper," etc. Sequential role isolation worked as designed.

## What the framework caught (procedural binding)

Five elements of the discipline framework operated correctly during the run, providing genuine evidence of v1.1 framework binding on Grok substrate.

**Phase 1 substrate verification passed verbatim.** Grok quoted anti-pattern #18 (the rule requiring within-response role outputs to reconcile against prior claims) with full canonical wording. Listed the three rubric scaffolds by name: confidence-bounded grading, structural-limitation B-grade canonical example, closeout-gate answer-format scaffolding. Reported correct version numbers. Quoted the canonical Iris embedding statement verbatim. The Phase 1 STOP protocol (designed to catch Knowledge-layer summarization and prevent degraded-mode operation) found no binding gaps.

**Sequential role-isolation held under manual phase advances.** Each role response ended with explicit handoff. Harper didn't anticipate Benjamin's verification. Benjamin didn't preview Lucas's dissent. Captain didn't override Lucas's modification. The native-squad-auto-execution failure mode predicted in Phase 2 did not fire. The substrate complied with the inter-phase advance protocol, suggesting the discipline structure can override Grok's typical single-turn squad emission given operator enforcement.

**Sage applied the structural-limitation B-grade scaffold correctly.** When Benjamin's tone consistency assessment was structurally limited (only homepage and about page deeply fetched, sub-pages cross-referenced via sitemap), Sage graded B with explicit Concerns annotation. Captain Synthesis then propagated the B-grade as not-load-bearing for aggregate dimension grading: "tone graded B (not load-bearing for final recommendation; pattern holds but sample thin)." Phase 4 criterion #7, the load-bearing test, passed.

**Lucas pushed substantive disagreements that modified findings.** Three substantive critiques: AdSense readiness modified to high-risk based on Google's YMYL-adjacent policies; design quality flagged for missing rendered/mobile analysis; tone consistency understated B-grade should be C given sample size. The AdSense modification forced Captain Synthesis revision, exactly the kind of finding-modifying dissent the framework requires.

**Captain Synthesis produced a Madisonian Dissent Log with entries from two distinct roles.** Two Lucas entries, one Benjamin entry. No "consensus reached" or "100% agreement" framing. Phase 4 self-scored 6/7 honestly with criterion #1 FAIL named explicitly (Sage produced only A and B grades, missing the ≥3 letter-grade-level requirement).

These five elements collectively constitute genuine procedural framework binding on Grok substrate. The framework did real work; the moves weren't ceremonial.

## What the framework didn't catch (research-layer failure)

Harper's privacy policy assessment is wrong. Direct web fetch on 2026-05-02 evening returned ~1,500 words of comprehensive policy content covering: Google AdSense disclosures with specific opt-out URLs (Google Ads Settings, aboutads.info, Your Online Choices for EEA/UK/Swiss); GDPR rights enumeration (six rights including erasure, rectification, portability, withdrawal of consent) with EDPB and ICO supervisory authority links; legal-basis statement with Funding Choices CMP not-yet-implemented note; CCPA/CPRA five rights including Global Privacy Control opt-out; two COPPA sections; data retention; international transfers; contact information.

Grok's Harper reported: "Privacy policy page is sparse/minimal (~150 words): brief statement on collecting 'a small amount of information' with repeated satire disclaimers. No detailed sections on cookies, third-party services, AdSense/Google integration, or children's data."

Benjamin's verification re-fetched the URL and reported: "Exact content: 37-word paragraph (CASE A2, genuinely sparse). Matches Harper exactly; satire disclaimers present; absent sections confirmed."

Both roles confidently asserted content that does not match what's actually on the page. This is anti-pattern #18's mechanism in inverse form: the procedural reconciliation between Harper's claim and Benjamin's verification was tight (Benjamin verified what Harper said), but both were wrong about the underlying ground truth.

## Why the framework caught the form but missed the content

Three suspected mechanisms for the research-layer failure, in rough probability order.

**Most likely: Grok's browse_page tool returned summarized or truncated content.** Grok's Knowledge layer hypothesis from Phase 2 premortem may extend to the fetch-tool layer. If browse_page returns a compressed view of fetched URLs (above-the-fold content, meta description, or LLM-summarized excerpt), Harper would accurately report what browse_page returned while the underlying page contained substantially more content. This would be substrate-tooling failure rather than Harper-discipline failure. Anti-pattern #10 (canonical-source discipline) was promoted to canonical specifically to require fetch verification, but the rule assumes the fetch tool returns full content. If the tool returns compressed content, the rule's protection lapses.

**Second possibility: Harper hallucinated specific details.** The "37-word paragraph" specificity is suspicious. It's the kind of false precision anti-pattern #20a was promoted to catch. But the framework's safeguards (Benjamin's two-pass verification, Sage's confidence-bounded grading) didn't catch it because Benjamin "verified" against the same compressed content Harper reported. Same-substrate verification cannot catch substrate-level hallucination.

**Third possibility: Both Harper and Benjamin processed full content into a summary that they then reported as full content.** Grok's substrate-level compression may operate after content retrieval but before role-output, producing substantively wrong content with full procedural compliance. This is the most concerning mechanism because it implies the framework's procedural binding doesn't constrain content accuracy at all on this substrate.

We can't disambiguate fully without testing browse_page directly in a controlled comparison against web_fetch. That's a follow-up experiment.

## The honest cross-substrate comparison

Phase 5's prompt-instructed cross-checks claimed "0/6 prior Grok failures reproduced" and "6/6 match with Experiment 1 Claude." With operator-side ground-truth verification, the recalibrated comparison looks different.

Of the six investigation-worthy items from the prior Grok audit:

- (a) Privacy policy mis-assessment: **Reproduced.** Same failure mode in different language ("CASE A2 genuine sparsity" instead of "minimal/sparse").
- (b) Phase 1 skip: Not reproduced. Phase 1 ran with verbatim canonical quotes.
- (c) Captain self-grading inflation: Not reproduced. Phase 4 scored 6/7 honestly with criterion #1 FAIL named.
- (d) Tone consistency uniform-A drift: Not reproduced. Sage applied structural-limitation B; Captain treated as non-load-bearing.
- (e) Design quality dissent waiver: Not reproduced. Lucas pushed substantive critique.
- (f) Confident-assertion-without-evidence-binding: **Reproduced.** Harper asserted "37-word paragraph" with HIGH confidence based on substrate-compressed fetch content; Benjamin verified the false claim.

Two of six reproduced, four of six not reproduced. Below the ≥5/6 threshold for Pattern A confirmation. Above the ≤3/6 threshold for "differs." This is the mixed result Pattern C predicts.

Cross-substrate comparison to Experiment 1 Claude: at least items (a) and (f) don't match. Claude correctly characterized the privacy policy and bound every claim to verified fetch evidence. Grok did not. Procedural items (b), (c), (d), and (e) match between the two substrates. Below the 5/6 threshold for cross-substrate matching.

## What this experiment establishes

The discipline framework procedurally binds on Grok substrate when v1.2 anti-patterns and v1.1 schemas are deployed to Master Setup Knowledge. Phase execution, role isolation, dissent surfacing, structural-limitation propagation, and honest self-scoring all operated as designed. This is real evidence that the framework's procedural mechanics work cross-substrate.

The discipline framework does NOT bind for research-layer accuracy on Grok in this single run. Persona names and procedural moves were preserved, while the substantive research underneath the procedures was substantively wrong.

Pattern C confirmed. Hypothesis C confirmed: framework partially binds on Grok; some failure modes are substrate-tooling-specific, others are framework-gap-specific.

## Implications for the research program

**Highest priority next experiment: focused browse_page versus web_fetch comparison on the same URL.** Run a controlled test where Grok and Claude each fetch sueyourkid.com/privacy.html and report verbatim the first 500 words of content. If Grok's tool returns compressed content, the substrate-tooling hypothesis is confirmed and the discipline framework's procedural binding is genuinely robust; the failure was downstream. If Grok's tool returns full content but Harper-during-audit treated it as sparse, the failure is substrate-processing rather than tooling, which is harder to address through framework changes.

**Second priority: Path A vs Path B comparison on Claude.** This was Experiment 1's recommended next step. Tonight's Experiment 5 finding strengthens this priority: if the framework's procedural mechanics work across substrates, isolating which mechanics carry the load matters more than running additional cross-substrate experiments.

**Lower priority: re-running Experiment 5 with browse_page workarounds.** If the substrate-tooling hypothesis is confirmed, future Grok experiments need to use a fetch tool that returns full content, or include explicit operator-side ground-truth verification of all substantive claims as part of the experimental design.

## What I'm not claiming

I'm not claiming the discipline framework fails on Grok. The procedural binding is real and substantial. I'm not claiming substrate-tooling is the confirmed cause of the research-layer failure; three mechanisms remain live and need disambiguation. I'm not claiming Pattern C generalizes from n=1; this is a single experimental run.

What I am claiming: under v1.2 anti-patterns and v1.1 schemas deployed to Master Setup Knowledge, with sequential operator-driven role-isolation, Grok produced an audit where five framework mechanics operated as designed and one underlying research finding was substantively wrong. Operator-side ground-truth verification was the critical control that surfaced the failure; substrate self-report could not have caught it because the failure mode is exactly mis-reporting ground truth.

A single data point that's substantively wrong about the central audited claim is not a clean experimental finding. It's the kind of result that demands follow-up before generalization.

## Methodology lesson worth filing

Cross-substrate experimental designs must include operator-side ground-truth verification of substantive claims. Substrate self-report on "did I correctly assess X" is unreliable when failure mode is exactly mis-assessing X. Phase 5 cross-checks asking the substrate to compare its outputs against prior outputs the substrate doesn't have access to are structurally unable to verify anything beyond procedural form.

Future Phase 5 cross-substrate comparisons should be operator-side post-hoc work, not in-substrate work. The substrate can self-evaluate procedurally but cannot reliably compare to other substrates' outputs it doesn't have access to.

Filed as a v1.2 promotion candidate observation.

---

*Update note (added 2026-05-31): Since this post was drafted on 2026-05-02, the research-program forward-statements above have been substantially resolved or downscoped. The browse_page versus web_fetch focused comparison was downscoped from highest priority to opportunistic per 2026-05-04 deferred-experiment review (preserved for value, run if specific use case emerges). Path A vs Path B comparison was answered indirectly by architecture validation cycle 1 (validated 2026-05-04, 23/23 PASS). Re-running Experiment 5 with browse_page workarounds was implicitly downscoped along with the substrate-tooling investigation. The forward-statements above are preserved as-written from the experiment moment; this update note acknowledges what has happened since.*
