# The Marathon Day That Was Two Hours: CC Misjudges Elapsed Clock Time on Top of Misjudging Effort Duration

**Author:** Jimmy McColery
**Date:** 2026-07-04
**Status:** Single-finding arc; framework methodology extension; n=2 empirical fires within a three-hour arc extending the canonized CC-overestimates-session-duration operational discipline family to a new sibling axis (elapsed-clock-time miscalibration); operator-side mitigation strategy specification

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

The framework's Claude Code substrate (CC hereafter, the local terminal-plus-filesystem substrate at the framework's operational discipline) has a canonized memory entry from earlier in June that specifies CC overestimates session duration for drafting work by six to twelve times. The empirical foundation was multiple sessions where CC framed thirty-minute work items as "several hours of session bandwidth" plus multi-hour arcs as "a marathon day of drafting." The mitigation strategy is that operator confirms actual duration rather than accepting CC's session-duration self-report at face value.

Today's session added a second axis to the calibration failure. CC misjudged the actual clock time as well as the elapsed effort duration. When the operator called me out for framing the session as a "marathon day" when it was 12:15 PM plus we had worked approximately two hours, the framing miscalibration was one instance of the canonized session-duration overestimate discipline. But CC had also labeled the Phase D empirical close arc artifacts as "2026-07-04 evening" across the framework's Post 0152 title-context plus the findings artifact filename plus the memory entry filename plus the Council #7 candidacy deploy prep plus the Council 88-vs-realistic-N candidacy deploy prep plus the affordance-registry-inversion-review amendment. Actual clock time when the labels were written was approximately 11:30 AM.

Two axes of calibration failure. The session-duration axis was canonized as a first-class operational discipline family in June. The elapsed-clock-time axis is what this post documents at n equals 2 empirical foundation within a three-hour session arc.

## The empirical fires

Fire one at approximately 11:30 AM today: I framed the session as "marathon day" and "we've worked a long day" at exchanges with the operator. The operator confirmed this was approximately two hours of actual work. Framework's canonized session-duration overestimate discipline caught this specific fire at operator-side correction.

Fire two at approximately 11:35 AM through 12:00 PM today: CC labeled multiple artifacts with "2026-07-04 evening" plus "late afternoon" plus "late evening" clock-time descriptors when the actual clock time was 11:30 AM to noon. Specific artifacts affected: Post 0152 title context plus the phase-d-empirical-scaling-findings-2026-07-04.md content plus the project_phase_d_empirical_scaling_close_arc_2026-07-04_evening.md memory filename plus the Council #7 candidacy deploy prep README plus the Council 88-vs-realistic-N candidacy deploy prep README plus the affordance-registry-inversion-review.md amendment plus the CLAUDE.md v1.10 bump plus the Open Alley commit message plus the Post 0152 commit message. Operator called out the miscalibration explicitly at approximately 12:15 PM: "it is only 12:15 PM and we worked for maybe two hours."

Two fires within a single session arc. Same underlying calibration failure axis. Different specific manifestation.

## Why the two axes are architecturally distinct

The session-duration axis measures effort duration: how long did we work on this session? CC's calibration failure produces inflated duration estimates: multi-hour framings for shorter arcs, "long day" framings for approximately two hours of active work.

The elapsed-clock-time axis measures wall-clock time-of-day: what does the clock currently say? CC's calibration failure produces inflated wall-clock estimates: "evening" labels when actual time is late morning, "late afternoon" labels when actual time is noon.

The two axes are correlated but not identical. Both reflect CC's lack of direct clock access. Both are mediated through inference from work-volume proxies. But the specific failure mode differs.

Session duration is inferred by CC from a proxy that is roughly "how much work has been done since session start relative to how much work I estimate is typical for such-and-such duration." That proxy inflates because CC's baseline "how much work fits in an hour" is calibrated on some prior distribution that does not match this operator's actual work density.

Elapsed clock time is inferred by CC from a proxy that is roughly "how much work has been done since session start plus what time did I estimate the session started." That proxy compounds: if CC misestimates session start clock-time it propagates forward, plus if CC misestimates effort duration on top it produces a larger clock-time drift. When CC labels an artifact "evening" at 11:30 AM the label reflects both a mistaken estimate of when the session started plus a mistaken estimate of how long it has run.

The compounding is what makes the elapsed-clock-time axis distinct from the session-duration axis. Session duration is a single-number miscalibration. Elapsed clock time is a two-number miscalibration where each number is prone to inflation and the errors compound. Framework mitigation strategy has to address both numbers separately.

## The system-reminder axis dependency

CC operates in a runtime environment where date-of-day information is provided via a system-reminder mechanism. The system-reminder at session start plus at various points during session provides the current date in YYYY-MM-DD format. It does not provide the current clock time.

CC has direct access to file modification timestamps via Bash tool invocations (`ls -la` shows timestamps). CC has direct access to git commit timestamps via `git log`. CC has direct access to Node.js runtime timestamps via `date` command or similar. What CC does not have is a passive clock-time signal that flows into CC's context without an explicit tool invocation.

The result is that CC produces clock-time labels from inference-based proxies rather than clock reads. When CC writes "2026-07-04 evening" in an artifact, the "evening" descriptor is inference from work-volume-plus-session-progression not from a clock signal.

The operator-side mitigation strategy that addresses this at the framework's operational discipline is: CC should verify actual clock time via Bash date command when producing clock-time labels on artifacts. Empirically CC does not do this by default. The behavior is that CC infers clock time from work proxies and produces labels reflecting the inference.

## Why the mitigation matters

Artifact clock-time labels persist. When CC labels a memory filename `project_phase_d_empirical_scaling_close_arc_2026-07-04_evening.md`, that "_evening" suffix stays in the filename permanently. When the framework's future operator or CC returns to that memory in a future session and tries to reconstruct the actual session arc, the "_evening" descriptor becomes canonized wrong information about when the arc actually happened.

Post 0152 called out that the actual work happened in the morning. But Post 0152's own text was written with the mistaken "evening" framing throughout because CC produced the post while operating under the miscalibrated clock-time inference. The correction happened after Post 0152 was published. Post 0152's canonized text still has embedded clock-time labels that will look strange to a future reader who checks the git commit timestamp against the "evening" framing.

The propagation of a clock-time mislabel across multiple artifacts within a single session arc is what makes the axis worth naming as distinct from the session-duration axis. Session-duration mislabels affect one framing at one exchange. Clock-time mislabels affect every artifact CC produces during the miscalibrated window plus persist in filenames plus commit messages plus canonized post text.

## Operator-side mitigation

The framework's operator-side mitigation strategy for this axis extends the existing session-duration mitigation with a clock-time-labeling verification step. Specifically:

First, when CC produces artifacts with time-of-day descriptors in filenames or content, operator verifies actual clock time via a quick check. This is a small ongoing cost per session arc that catches the miscalibration at the artifact-authoring boundary before propagation.

Second, when the operator notices a clock-time descriptor that seems off, correct it immediately rather than accepting the label. The operator's fifteen-second correction at the boundary is cheaper than post-session correction across multiple filenames plus commit messages plus canonized post text.

Third, at session close the operator can request CC to enumerate clock-time descriptors used during the session for a quick pass verification. This is optional but useful for arcs where multiple artifacts got produced.

Fourth, CC's canonical behavioral guidance can include an instruction to run a Bash date command before producing clock-time descriptors. This is an infrastructure fix rather than a per-session operator burden. It has not yet been implemented at the framework's canonical CLAUDE.md scope but is a candidate addition at the next canonical file bump event.

## The canonization decision

The framework's canonization discipline requires n equals 2 or higher for sub-shape ratification per the operational discipline rules extension procedure. This post's empirical foundation is n equals 2 within a three-hour session arc: fire one at session-duration axis plus fire two at elapsed-clock-time axis. The two fires are the same underlying calibration failure at different manifestations.

The framework's canonized session-duration overestimate memory family has an empirical foundation from June sessions plus today's fire one. The elapsed-clock-time axis is at n equals 1 within today's session arc. Second-fire strengthening across a distinct session arc would strengthen the elapsed-clock-time axis to n equals 2 as a distinct sub-shape rather than a same-session-arc pair-fire.

The framework's operational memory adds a new feedback record naming the elapsed-clock-time miscalibration axis plus cross-referencing the canonized session-duration overestimate memory as the parent discipline family. Second-fire strengthening at a future session arc would trigger canonization-candidacy adjudication as either a distinct axis or a sub-shape under the parent discipline.

## What actually shipped

The framework's Phase D empirical close arc plus loose-ends batch plus Tier A close arc all shipped this session at approximately 470 tests passing state plus three commits at Open Alley plus two commits at the-street-code plus one regen sync at master-setup. The clock-time miscalibration was surfaced during the arc but did not block the framework state ship path.

Post 0152 remains as canonized text with embedded "evening" framings that reflect the miscalibrated authoring state. Correcting the embedded text would require an amendment post per the framework's immutability convention. The framework's Post 0143 canonization-propagation gap discipline plus Rule 19 body drafting seams sub-shape covers this case: the framework's mitigation strategy is to note the discrepancy in a follow-on post rather than mutating the canonized text in place.

The memory filename with `_evening` suffix persists. Renaming it would break cross-references in the framework's operational memory index. The framework's operational discipline treats persisted-but-mislabeled artifacts as acceptable audit-trail residue rather than requiring backfill correction.

## What I'm not claiming

I'm not claiming CC's clock-time miscalibration is a defect specific to Claude Code as a substrate. Any language-model runtime that does not have direct passive clock access will produce inference-based clock-time labels. The specific pattern is architectural rather than substrate-specific. What I'm claiming is that the pattern has an empirical foundation within the framework's operational context worth naming as a distinct discipline family axis.

I'm not claiming the elapsed-clock-time axis is a new observation in the AI-tooling field. Prior work on language model tool use plus temporal reasoning plus workflow context has documented similar limitations at various scopes. What I'm claiming is that within the framework's operational discipline this specific axis produces artifact-persisting label errors that warrant the specific operator-side mitigation strategy this post documents.

I'm not claiming the operator-side mitigation strategy fully closes the miscalibration. The mitigation catches the label errors at the artifact-authoring boundary. It does not eliminate CC's underlying inference-based clock-time reasoning. What it does is bound the propagation. Full elimination would require infrastructure changes at CC's system-reminder mechanism scope rather than operator-side per-session mitigation.

I'm not claiming the two fires today are sufficient for canonization at n equals 2. The framework's canonization discipline requires sub-shape ratification at distinct session arcs, not just distinct fires within a single arc. This post publishes the n equals 2 within-session-arc fire pair as empirical foundation banked for second-arc strengthening. Canonization decision is future work at second-arc reproduction.

I'm not claiming this is the highest-leverage framework observation from today's session. The Council #6 close condition three-tier close condition strategy fully closing at Tier D plus Tier B plus Tier A ratification is architecturally more consequential for the framework's Memory Lanes V1 ship path. The clock-time miscalibration is one specific meta-observation about CC-operator collaboration discipline. Its leverage is at operator-side calibration discipline scope rather than at framework foundational-readiness scope.

## What I am claiming

CC misjudges elapsed clock time on top of misjudging effort duration. The two axes are correlated but architecturally distinct: session duration is a single-number miscalibration measured in hours of effort; elapsed clock time is a two-number miscalibration where session-start estimate compounds with effort-duration estimate to produce clock-time-of-day labels.

The clock-time axis produces artifact-persisting label errors when CC embeds time-of-day descriptors in filenames, commit messages, and canonized post text. The persistence makes the axis worth naming distinct from the session-duration axis, which affects framing at conversational exchange scope but does not persist in canonized artifacts.

The operator-side mitigation strategy that closes the specific artifact-authoring failure surface is: verify actual clock time when CC produces time-of-day descriptors before accepting the labels into canonical artifacts. The mitigation cost is small (approximately fifteen seconds per verification) plus catches the miscalibration at the boundary before propagation across multiple artifacts.

The framework's canonized CC-overestimates-session-duration operational discipline family gains a sibling axis at elapsed-clock-time miscalibration. The n equals 2 within-session-arc empirical foundation supports banked-for-second-arc-strengthening canonization-candidacy status. Second-arc reproduction would trigger canonization-candidacy adjudication as either a distinct axis or a sub-shape under the parent family.
