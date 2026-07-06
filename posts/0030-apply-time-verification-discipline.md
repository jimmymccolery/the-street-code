<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0030
title: Apply Time Verification Five Sub Disciplines from One Session
date_published: 2026-05-11
status: published
superseded_by: none
domain: Apply-time verification discipline with five sub-disciplines emerging from Downloads folder cleanup session that crossed midnight into 2026-05-11 (44 file operations)
project_scopes: street-code-methodology
cc_task_relevance: verification-validation, anti-fabrication, discipline-enforcement
phase_binding: Phase-1, era-independent
discipline_family: verify-against-canonical-files
canonical_rule: Pre-asserted values in structured prompts become reference baselines for drift detection not authoritative inputs verification of counts/dates/sizes/content/premises happens at moment work fires not at moment prompt was drafted
load_bearing_claims:
  - Real fire caught: file count 19 asserted at draft time but 18 at apply time (duplicate deleted between inventory and prompt)
  - Five sub-disciplines: count-claim-via-grep, date-claim-via-ls, size-claim-via-stat, content-claim-via-diff, premise-claim-via-explicit-test
  - Categorization into exactly five is partially post-hoc; unclear if categories collapse cross-session
applicability_triggers:
  - CC drafting structured prompts that assert specific counts, dates, sizes, or content
  - CC deciding whether to embed apply-time verification vs trust pre-asserted values
  - CC evaluating baseline confirmations vs real fires
mechanism_details:
  - Naming convention looks like function signatures for operational precision
  - First operationalization of count-claim-via-grep caught 19-to-18 drift
  - Baseline confirmations across multiple per-file verifications rather than fires
cross_refs:
  - Post 0031 four things canonical record couldnt tell me about itself (side-findings from same arc)
  - Post 0017 recovery-from-drift discipline
-->

# Apply-Time Verification: Five Sub-Disciplines from One Session

**Status:** Self-experimentation by a non-credentialed practitioner. n=1 operator deploying a multi-step disposition arc across a single 2026-05-10 session that crossed midnight into 2026-05-11. The discipline pattern described below has five sub-disciplines that surfaced empirically across the session and were named during the session's observation filing work; the categorization into exactly five is partially post-hoc construction rather than a framing that emerged fully formed during the work itself. Cross-session pattern stability is unverified at filing time. Whether the discipline generalizes beyond this arc, or whether the five sub-disciplines remain stable as separate categories or collapse into fewer, is not the claim of this post. The empirical foundation cited is what I have, not what would settle the question externally. Read accordingly.

## Opening

Here is the discipline this post documents. Whenever I draft a structured prompt for an AI substrate to execute, I am tempted to assert specific values based on prior verification work. The folder had 19 files matching a pattern. A file was 27,890 bytes. The git history was available. These assertions are usually accurate at the moment I drafted them. They are not always accurate at the moment the work actually fires.

The discipline that resolves this is apply-time verification. Whenever a prompt asserts a count, a date, a size, a content snippet, or an operational premise, the verification of that assertion happens at the moment the work fires, not at the moment the prompt was drafted. Pre-asserted values become reference baselines for drift detection, not authoritative inputs.

I work with AI substrates through structured prompts that file results into a project record at my project root. Posts 26-29 documented operational discipline rules and validation conventions that crystallized during prior multi-session work. This post documents something different. On 2026-05-10 I ran a session intended as ordinary Downloads folder cleanup. The session handled 44 file operations across multiple sequential steps. By the end, a discipline pattern had emerged that I had not anticipated going in, surfaced across five distinct categories. This post documents the pattern, the five categories, what caught real fires versus what confirmed baselines, and what the single-session empirical foundation does and does not support.

## The discipline pattern

The starting observation is unflattering to my prior drafting habits. When I drafted prompts at the start of a multi-step session, I would assert specific values based on prior verification work. The Downloads folder had a specific count of files matching a pattern. A project-record entry was a specific byte size. Specific files were byte-identical to archive copies. These assertions were accurate at the moment of prior verification but not necessarily at the moment the next prompt fired.

In one specific case, a prior cleanup step had deleted a duplicate file between the initial inventory and a subsequent prompt. The subsequent prompt asserted a count of 19 files matching a pattern. The actual apply-time count was 18. If I had not built explicit apply-time verification into the prompt structure, the project-record entry that the prompt produced would have asserted 19 in its filed observation. The project record would have inherited a stale count from a pre-asserted value.

The discipline that resolves this is verification at the moment the work fires, not at the moment the prompt is drafted. This sounds obvious in retrospect. It was not obvious before the empirical pattern surfaced. The interesting question is not why apply-time verification matters in general. The interesting question is what specific kinds of pre-asserted content cause drift, and the session produced five distinct categories.

## Five sub-disciplines from one session

Each sub-discipline below has a name reflecting both what is being verified and the verification method. The naming convention emerged during the session and stuck because it made the discipline scope explicit at prompt-drafting time. The names look like function signatures because they were built for operational precision; bear with the form.

**Count-claim-via-grep.** Counts of project-record entries, files matching a pattern, observations of a specific type. Verified at apply time via grep or filesystem enumeration. The first operationalization of this sub-discipline caught the 19-to-18 file count drift I described above. This was a real fire.

**Date-claim-via-ls.** Modification dates of files, dates embedded in archival filename conventions. Verified at apply time via ls or stat. The first operationalization of this sub-discipline applied to nine substrate response files being archived with date-suffixed filenames. The prompt assumed all nine shared one date. Verification confirmed they did. This was a baseline confirmation rather than a fire.

**Size-claim-via-stat.** File sizes referenced in project-record content or as preservation-integrity verifications across file mutations. Verified at apply time via stat. The first operationalization of this sub-discipline applied to deletion confirmation work where archive copies at canonical locations were verified preserved at expected byte sizes before and after each deletion. Baseline confirmations across multiple per-file verifications rather than fires.

**Content-claim-via-head.** Verbatim content snippets quoted in project-record content. Verified at apply time via head or file read. The first operationalization of this sub-discipline caught a project-record entry whose content opened with a substrate-format header that did not match the substrate name embedded in the filename. The filename said one thing; the content said another. This was a real fire and the most consequential one of the session because it surfaced a project-record integrity issue at an existing entry.

**Premise-claim-via-rev-parse.** Operational state premises underlying decision reasoning. Verified at apply time via empirical state inspection. The first operationalization of this sub-discipline caught a state-reconstructibility premise that rested on version control being available at the project root. Empirical inspection returned the canonical not-a-git-repository error. The premise was falsified at apply time before any work fired that depended on it. This was a real fire and changed the operator decision path materially.

Three fires plus two baseline confirmations across five sub-disciplines. The discipline operated in all five cases regardless of whether a fire fired.

## The conceptual distinction that matters

The first four sub-disciplines verify claims that appear in project-record content. Counts, dates, sizes, content snippets. These are statistics about the project record itself or about files being processed.

The fifth sub-discipline verifies a claim that appears in decision reasoning rather than project-record content. The premise "version control is available" was not a statistic in any entry. It was an unstated assumption underlying a deletion decision.

The distinction matters because the two scopes have different failure modes. Statistic claims become stale through project-record activity between prompt drafting and prompt firing. Premise claims become stale or remain falsified through operational state that was never verified in the first place.

Both share the apply-time verification pattern. Both prevent the project record from absorbing inaccurate content. But they operate at different conceptual scopes and warrant separate naming because their verification surfaces appear at different points in the prompt structure.

## What this arc actually produced

The session filed three methodology research observations into the project record. The first documented an archival convention gap surfaced by the cleanup arc itself. The second documented the substrate-content-vs-filename mismatch caught by the content-claim sub-discipline. The third documented the version-control-absence finding caught by the premise-claim sub-discipline.

Beyond the filed observations, the session demonstrated five distinct apply-time verification sub-disciplines operating across the prompts. Each sub-discipline had its first operationalization within the session. Three caught real fires. Two confirmed baselines preventively. All five operated as discipline regardless of whether fires fired.

The cumulative pattern is the discipline. The individual catches and confirmations are the empirical anchors.

## What I'm not claiming

This is single-session empirical evidence. The five sub-disciplines were operationalized within one extended session. Cross-session replication is zero.

I am not claiming the five sub-disciplines are exhaustive. Other verification scopes may exist that this session did not surface. I am not claiming the conceptual distinction between statistic-scope and premise-scope verification is the right framing at the discipline level. Future deliberation may find a unified framing or a finer-grained taxonomy. I am not claiming the categorization into exactly five sub-disciplines is stable; the count is partially an artifact of how the session's observation filings happened to structure the naming.

I am not claiming the discipline generalizes to other operators, other work classes, or other AI-collaborative configurations. The session ran a specific architecture with specific tooling and specific operator habits. The catches that the discipline produced may be specific to those conditions.

What I am claiming is that within this session, on the work that ran, the apply-time verification discipline caught three real fires and confirmed two real baselines preventively across five distinct sub-discipline categories. That is the foundation. Anything beyond requires more evidence.

The discipline is currently filed at the project-record observations level, not promoted to canonized rule status. Promotion warrants cross-session pattern stability that does not yet exist.

## Closing

The pattern that this post documents is unflattering in a way I want to name explicitly. The discipline emerged because I was repeatedly pre-asserting content in prompts that turned out to need verification at the moment of firing. The first instance was a count. The second was a date. The third was a size. The fourth was content. The fifth was an operational premise.

Each surfacing was a small fire or a confirmed baseline. None individually would have warranted a post. The cumulative pattern across one session, across five distinct sub-discipline categories, across three observations filed into the project record, is what produced the discipline that this post names.

Whether the pattern survives cross-session verification is the next question. I have no answer to that question at filing time. The honest scope of what one session produces is what one session produces.
