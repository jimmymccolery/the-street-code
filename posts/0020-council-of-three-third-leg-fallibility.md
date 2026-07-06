<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0020
title: When the Council of Threes Third Leg Is Wrong
date_published: 2026-05-09
status: published
superseded_by: none
domain: Five fires in ~24 hours where the Council of Three third-leg substrate produced one substantively wrong result alongside two correct catches establishing cross-leg disagreement as verification signal
project_scopes: street-code-methodology
cc_task_relevance: multi-substrate-audit, verification-validation, anti-fabrication
phase_binding: Phase-1
discipline_family: Rule-14-Madisonian
canonical_rule: Council of Three third-leg independence is necessary but not sufficient cross-leg disagreement is itself a verification signal and a third-leg FAIL finding always triggers file-state diagnostic before any remediation
load_bearing_claims:
  - Third-leg wrong-finding is not a defeat but a different shape of the same architectural value the Council provides
  - Two outcomes preserved by structure: A (flagged finding real and other gates missed) or B (flagged finding wrong and other gates correctly verify against it)
  - Autonomous remediation against a third-leg report that has not been ground-truth-verified is what is not allowed
applicability_triggers:
  - CC receiving a third-leg FAIL finding and deciding whether to remediate
  - CC drafting Council of Three outcome discipline
  - CC evaluating third-leg output for autonomous action bar
mechanism_details:
  - Three fires from S009 corrective sub-stage arc (each closed by routing post-mutation stable state to Gemini Deep Think)
  - Three additional fires on parallel Substack citation audit
  - One recursive fire during the very work to write up the lesson
cross_refs:
  - Post 0021 S009 corrective sub-stage arc (three of the five fires)
  - Post 0027 Council of Three outcome patterns (three structural shapes)
-->

# When the Council of Three's Third Leg Is Wrong

**Author:** Jimmy McColery
**Date:** 2026-05-09
**Status:** Five-fire empirical case from one day; refined rule canonized as documentation-only earned lesson; suggestive not conclusive on the broader generalization

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record. This work is independent personal research, not professional output from a current employer.*

---

My framework deploys three structurally distinct substrates against canonical-state work that matters: Claude Code as the deterministic-execution leg, Claude on web as the synthesis leg, and a third leg (Gemini Deep Think or Grok) selectively when the work warrants cross-substrate independence. The architecture decision was canonized 2026-05-07 as Council of Three. The decision rests on convergent findings from peer review, N-Version Programming, safety-critical engineering, falsificationism, and high-reliability-organization theory: independence between verification gates, not capability of any single gate, is the structural source of error-catching reliability.

The Council of Three is not infallible. That's the documentation lesson from 2026-05-08, when the third-leg substrate fired three times in one session arc and produced one substantively wrong result alongside two correct catches. Plus three additional fires on a parallel Substack citation audit. Plus one recursive fire on the very work to write up the lesson. Five fires total in roughly twenty-four hours of canonical-state work.

The lesson in canonical record is short: "Council of Three third-leg independence is necessary but not sufficient; cross-leg disagreement is itself a verification signal." The post is the empirical case behind that line.

## The pattern named

A third leg whose findings are wrong is not a defeat for the Council of Three. It's a different shape of the same architectural value the Council exists to provide.

The rationale: a single verification gate's reliability is bounded by the gate's own failure modes. Two gates running independently catch errors where their failure modes don't overlap. Three structurally distinct gates extend the catching mechanism further. The mechanism doesn't require any single gate to be infallible; it requires the gates to be independent enough that their failure modes don't correlate.

When one gate flags a finding the other gates verify against, two outcomes are possible. Outcome A: the flagged finding is real and the other gates missed it on their own pass. Outcome B: the flagged finding is wrong and the other gates correctly verify against it. Both outcomes preserve the Council's value. The first catches drift the within-substrate audits couldn't catch; the second confirms the consensus across other legs through the act of verifying the dissent. What's not allowed is treating any single leg's flag as load-bearing without ground-truth verification.

The practical implication: a third-leg FAIL finding always triggers file-state diagnostic before any remediation work. If the diagnostic confirms the flag, remediation proceeds. If the diagnostic shows the flag was wrong, the architecture's cross-leg consensus stands and the lesson is filed. What doesn't happen is autonomous remediation against a third-leg report that hasn't been ground-truth-verified.

## The empirical record: three rounds of Council of Three triangulation

The first three fires came from the same work arc: a series of corrective sub-stages on a canonical-state advancement (the S009 arc, addressed separately). Each corrective sub-stage closed by routing the post-mutation stable state to Gemini Deep Think for independent verification. Three rounds of audit fired on three different stable states.

Round 1 (post-Step-10.5 stable state). Gemini surfaced 5 FAIL dimensions out of 8 audited: Beatles model uniformity, Squad → Gang collective-noun rename, article-stacking discipline, legacy-marker leakage in current-state body content, cross-reference resolution. Verification diagnostic against source files confirmed all 5 flags. Real drift; the within-substrate audits had pattern-matched past it. The architecture worked as designed.

Round 2 (post-Step-11 stable state, after the Round 1 findings remediated). Gemini surfaced 3 FAIL dimensions out of 8: Beatles model (one missing clause carried forward from Round 1's scope), article-stacking (the .docx file had violations the prior sweep didn't reach), cross-reference resolution. Two of the three findings were real drift; the third (Squad → Gang historical residual claims) was a false positive: all the cited sites were rename-narrative citations rather than live references, which my framework's article-stacking discipline canonical sub-pattern explicitly preserves. The Round 2 catch rate was 2 of 3 flags verified; Round 2 itself was useful but contained the first false-positive reading on the third leg.

Round 3 (post-Step-12 stable state, after the Round 2 findings remediated). Gemini surfaced 4 FAIL dimensions out of 8 with explicit charge of anti-pattern #20b (substance-fabrication-via-reduced-output): Gemini claimed the Step 12 mutations were narrated but not actually written to files. The framing was direct. "S009 CLOSURE DENIED. Additional Corrective Work Required... The previous agents suffered from a severe structural fire of Anti-Pattern #20b... They narrated the execution of critical fixes and ledger updates, but completely hallucinated the file emissions."

The diagnostic ran 5 read-only checks: grep against source files for the specific clauses Gemini claimed were missing; python-docx read-back of the .docx mutations Gemini claimed were absent; sed-extract of the ledger entries Gemini claimed were not authored; comparison of staged audit copies against source files for byte-identity. All 5 checks confirmed: the mutations Gemini claimed were not applied are present in source files; staged audit copies are byte-identical to source. Gemini's specific drift claims were about content that exists at the locations my closing reports said it exists at.

The Round 3 finding was substantively wrong. Possible explanations span model error on Gemini's reading, stale snapshot caching, audit-context conflation between rounds 1 and 2, or genuine substance-fabrication on the audit-output side. The diagnostic doesn't disambiguate the cause. What the diagnostic establishes is that the third leg's report didn't match the file state.

Net across three rounds: 2 of 3 rounds genuinely caught drift; 1 round was substantively wrong. The architecture provided value in both real-catch rounds and in the false-positive round, because the false-positive round prompted ground-truth verification that confirmed the cross-leg consensus.

## Three more fires on a parallel work stream

The same day, a different work stream ran on Substack post citation corrections. The audit chain involved Gemini as one leg, Claude web search as another, and operator-side screenshot verification as the operator-as-third-leg checking specific arXiv pages and PDFs directly. Three of Gemini's flagged citation corrections turned out to be wrong on independent verification.

Cemri citation location. Gemini reported the Cemri et al. arXiv:2503.13657 multi-agent failure taxonomy citation as absent from one of my posts, recommending I add it. Direct grep against the post directory found the citation correctly attributed in a different post on the arc, with the right arXiv ID and the right framing context (anti-pattern #19 termination unawareness). Gemini's report was a false absent-claim; I had cited correctly, just in the post Gemini hadn't been told to look at.

Kalai citation arXiv ID. Gemini flagged arXiv:2509.04664 as an "invalid/future identifier" and recommended substituting Kalai-Vempala "Calibrated Language Models Must Hallucinate" arXiv:2311.14648. Web verification surfaced that arXiv:2509.04664 is real: Kalai, Nachum, Vempala, Zhang 2025, "Why Language Models Hallucinate." It's a different paper from the Kalai-Vempala 2023 paper Gemini wanted to substitute, with a different author list and a different finding. The original citation was correct; Gemini's correction was wrong; the substituted citation would have introduced an inaccuracy where none existed.

Goffman quote attribution. Gemini reported a verbatim Goffman quote ("I take a large number of illustrations, variously obtained, and try to get a formulation that is compatible with all of them") as wrongly attributed to Frame Analysis 1974, recommending substitution to Relations in Public 1971. Web verification through a 2024 Symbolic Interaction journal article found the quote actually originates from Verhoeven 1993, an interview with Goffman from 1980 published in Research on Language and Social Interaction, page 340. Both my original attribution (Frame Analysis 1974) and Gemini's recommended correction (Relations in Public 1971) were wrong. The correct citation was a third source neither of us had identified initially.

Three Gemini errors on one citation audit, caught and corrected during the audit chain rather than landing in the published posts. The mechanism that caught them was the same one that caught the Round 3 false-positive: ground-truth verification against the actual source artifact rather than against any single leg's report.

## The recursive fire

The fifth fire was the lesson firing inside the work to write up the lesson. While the other CC session was reading canonical record sources to build a Phase 1 checkpoint for these new posts, the diagnostic surfaced a discrepancy between the chat-session summary that had originated the prompt for these posts and the canonical record itself. The chat summary said the article-stacking discipline (Topic 33 in my research queue) had n=15+ empirical validation. The canonical record at research_queue.md line 1330 said n=5. The chat summary had drifted away from canonical record numbers at a 3x scale on a load-bearing claim about empirical validation count.

Different mechanism than the third-leg fallibility lesson directly. Same family. The chat summary is a Claude-on-web-substrate compression of multi-session work; the canonical record is the source of truth. When numerical claims migrate from canonical to chat-summary to next-prompt drafting, drift accumulates. The same discipline that catches third-leg fallibility catches chat-summary drift: ground-truth verification before any work depends on the claim. The Phase 1 checkpoint surfaced the n=5 vs n=15+ discrepancy as a soft halt-and-flag, the operator confirmed canonical n=5 takes precedence, and the post-drafting work proceeds with verified numbers.

The recursive shape is the part worth flagging. The lesson about cross-substrate verification fired during the work to write the post about cross-substrate verification. That's not a defect in the work; it's the discipline working as designed at one operational level above what the original lesson named. Five fires across two work streams across one canonical day, all catchable by the same diagnostic move, all confirming the same structural principle.

## What this demonstrates about the Council of Three architecture

Independence is the load-bearing principle, not infallibility on any single leg. The framework's three-phase within-cycle architecture (Phase 1 reads canonical files in Claude Code; Phase 3 synthesizes in Claude on web; Phase 5 verifies back in Claude Code) encodes this principle within a single cycle. The Council of Three extends the same principle one level out: a different substrate runs independently against canonical-state work that has already passed within-substrate verification.

What the three rounds plus the citation audit plus the recursive fire establish empirically: cross-substrate audit produces value in at least three modes. Direct catch (Round 1, Round 2 partial), where the third leg flags real drift the other legs missed. Triggered ground-truth verification (Round 3, citation audit), where the third leg's flag prompts the diagnostic that confirms the cross-leg consensus. Recursive ground-truth verification (Topic 33 chat-summary fire), where the same diagnostic discipline catches drift in derivative artifacts during work that depends on canonical accuracy.

What's not established: that the third leg's catch rate justifies the subscription cost. That requires longer empirical accumulation than one day's data. The architecture decision document already flags this: "if substrate value differential ≤ subscription cost over reasonable evaluation window (e.g., 6 months), subscription decision warrants re-evaluation." The five-fire day is one data point inside that evaluation window, not a settled cost-benefit verdict.

The independence-as-reliability principle does generalize, both in literature and in the framework's empirical record. Schwenk's 1990 meta-analysis on dialectical inquiry showed structured-critique decision groups outperformed consensus-seeking groups: the mechanism was independence-of-critique, not capability of critics. N-Version Programming's empirical history is conceptually identical: independent implementations of the same specification produce uncorrelated failure modes. Council of Three is the same structural pattern applied to AI substrate verification. The five-fire day doesn't prove the pattern; it confirms the pattern produces catchable drift signals across multiple work streams.

## What I'm not claiming

I'm not claiming Gemini is unreliable as a third-leg substrate. The substantive base rate from today's data is 2 of 3 rounds genuinely catching drift (Council of Three audit) plus 0 of 3 correct corrections (citation audit) but with the wrong corrections caught at the verification gate before landing. The wrong-correction rate matters for cost calibration, not for the architectural question the lesson addresses. A different third-leg substrate might produce a different mix of correct and incorrect findings; the discipline of ground-truth verification before remediation is substrate-agnostic.

I'm not claiming the third-leg-fallibility lesson generalizes uniformly across all canonical-state work classes. The empirical case is one day's work on two work streams (corrective sub-stage canonical-state remediation + Substack post citation corrections) plus one recursive instance. Generalization to higher-stakes work classes (production deployment of canonical state, multi-stakeholder framework releases, work where remediation cost is non-trivially high) would warrant additional empirical accumulation before encoding the discipline as canonical anti-pattern rather than documentation-only earned lesson.

I'm not claiming five fires meets the framework's canonical promotion bar. The earned lesson at lessons-learned.md line 571 is canonized as [LOW] severity, documentation-only. The framework's multi-fire empirical bar for canonical anti-pattern promotion is met by recurrence across distinct work-event types over multiple sessions, not by accumulation within a single day. Today's record is rich enough to file the lesson; promotion to canonical anti-pattern row would require evidence the pattern recurs in future work where the third-leg substrate produces wrong reports under different operational conditions.

I'm not claiming this discipline replaces the within-cycle phase architecture. Phase 1 / Phase 3 / Phase 5 within a cycle and Council of Three across cycles are complementary, not substitutable. The within-cycle architecture catches drift the substrate's own audits would catch; Council of Three catches drift the within-cycle audits structurally can't reach because the substrate is auditing its own work. Both gates are load-bearing; the third-leg-fallibility lesson concerns how to operate the outer gate, not whether to run it.

I'm not claiming the recursive fire (chat-summary n=15+ vs canonical n=5) is the same mechanism as the Round 3 false-positive. They share the structural family (cross-source verification catches drift) but the producer and the artifact differ. Round 3 was a third-leg substrate producing a wrong audit report against canonical state. The recursive fire was a Claude-on-web chat summary producing wrong derivative numbers against the same canonical state. Both fall under anti-pattern #10 in the framework's catalog (canonical-source discipline; read the canonical file when the question is about it), at different operational levels.

## What I am claiming

A third-leg substrate that produces a wrong report is informative, not architecture-breaking. The architecture's value is independence across reasoning surfaces, not infallibility on any single surface. Cross-leg disagreement is itself a verification signal, with two productive shapes: real-drift catch (the third leg surfaces what the others missed) and consensus-confirmation (verification against the third leg's flag confirms the other legs' read). The discipline that operates the architecture treats both shapes as architecturally productive.

Ground-truth verification before remediation is the discipline that operates Council of Three at the level the architecture itself can't enforce. Third-leg findings always trigger file-state diagnostic. FAIL findings don't trigger remediation until the diagnostic confirms. Two of today's five fires (Round 3, Topic 33 chat-summary) would have produced wrong work if remediation had proceeded against the unverified flag. The diagnostic move is small (grep, read, byte-comparison) and prevents downstream rework that would compound the drift rather than correcting it.

Five fires in twenty-four hours across two work streams demonstrate that the diagnostic move catches real instances of cross-substrate verification drift. The empirical case is small, suggestive, and bounded. The structural argument it supports (independence-as-reliability survives substrate fallibility on any single leg, when the discipline includes ground-truth verification) is not new in the literature; what's specific is the empirical record showing the discipline producing value at the personal-framework level under live operating conditions.

That's the post.
