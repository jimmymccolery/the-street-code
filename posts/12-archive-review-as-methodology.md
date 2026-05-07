# Archive Review as Methodology

**Author:** Jimmy McColery
**Date:** 2026-05-06
**Status:** Operational lesson from one structured archive review across 109 files; suggestive not conclusive

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record. This work is independent personal research, not professional output from a current employer.*

---

AI-assisted work output accumulates faster than any individual review can metabolize. Across multiple sessions and substrates, archives pile up: drain outputs from earlier chats, prompt experiments that almost worked, research artifacts that informed decisions later canonized elsewhere, files whose substance moved into the canonical record but whose archival shells persisted. The default response when something feels missing is ad-hoc review: search the archive for what memory says should be there. The default response is unreliable. Cherry-picking from memory pulls items that feel relevant rather than items that are demonstrably canonical-state-misaligned, which is a different question.

The structured alternative is multi-stage: inventory pass first; recovery candidate identification with verification gates; severity calibration with explicit rejection list; deferral discipline for items below the resolution bar; per-stage self-grade. Each stage produces output that downstream stages depend on. Skip the inventory and recovery becomes cherry-picking from memory with structure layered on top. Skip the verification gates and recovery decisions ship items that feel like they should be recovered but aren't actually canonical-state-misaligned.

The empirical case: a 109-file archive accumulated across eight days and multiple substrates, reviewed via this discipline, produced eight recovery candidates (one HIGH, four MED, three LOW) plus six explicit rejections plus ten deferrals. Verification discipline caught three Claude-side near-misses during recovery deployment that would have produced canonical-state drift if shipped as written. This post covers the methodology and what its gates actually catch.

## Why ad-hoc review fails

The failure mode is structural, not effort-related. Ad-hoc review starts from memory of what's missing: a sense that a specific drain output should be findable, that a particular research artifact informed a decision but didn't get filed. Memory is the search query. The archive gets searched against that query. If the query matches a filename, the item gets recovered. If the query doesn't match, the item stays in the archive even when it's substantively important.

The problem is that memory's signal of importance correlates poorly with canonical-state-misalignment. An item feels missing because it was salient at the time it was created: vivid, recent, mentioned in a recent conversation. An item is actually misaligned because canonical state references it without it being preserved, or because it contains substance not propagated to canonical files, or because its absence would create a gap in the audit chain. The two questions don't reduce to each other. Memory's salience signal can fire on items that are already canonically preserved (just feels missing because the operator didn't remember the propagation); the same signal can stay silent on items that are genuinely misaligned (forgotten because the work shifted to other contexts).

Ad-hoc review also reads filenames, not content. Archives accumulate filenames as the visible surface. A reviewer glancing at filenames pattern-matches to memory's importance signal, which compounds the salience problem rather than correcting it. Substantive content review requires opening files, reading them, cross-checking against canonical state. That's a different operation, and it doesn't scale via filename glance.

The structural fix is to invert the order: start from the archive contents (inventory pass), not from memory (search query). Let what's there determine what gets reviewed, then test each candidate against canonical state. Memory becomes one input among many, not the primary signal.

## The methodology's structure

The discipline operates in five stages, each producing output that downstream stages depend on. The structure isn't elegant; it's empirical: what survived after one full run on a 109-file archive and one round of operator-side judgment about what worked.

**Stage 1: Inventory pass.** Strategic sampling, not file-by-file exhaustive read. Read all canonical reference files (anti-patterns catalog, lessons-learned, GROK.md, context.md) plus key archive precursors plus six diff/checksum comparisons plus ~25 archive files in detail. The PDFs got skipped: binary-bulky, content already summarized in their filenames plus downstream lessons. The output is a five-section document covering inventory overview (counts, dates, extensions, originating substrate, topical clustering); longitudinal patterns observed across the archive's time span; recovery candidates; deferral recommendations; per-section self-grade. Each section has structural specificity, not just summary.

**Stage 2: Recovery candidate identification.** From the inventory's longitudinal patterns and topical clustering, surface candidates whose absence from canonical state would create demonstrable misalignment. Each candidate gets named, located in archive, severity-rated (HIGH / MED / LOW), and given an "if recovered, where it goes" target path. The discipline that makes this stage load-bearing rather than memory-driven: every candidate gets confirmed by reading the relevant canonical file directly, not by inferring from related context. Anti-pattern #10 in operation throughout: canonical-source discipline at every recovery decision.

**Stage 3: Severity calibration with explicit rejection list.** The recovery candidates aren't evaluated in isolation. The methodology requires an explicit rejection list: items that looked recoverable on first inventory pass but failed the canonical-state-misalignment test. The rejection list is part of the methodology, not residue from it. Showing the work of rejection forces calibration that "recover everything that feels relevant" doesn't.

**Stage 4: Deferral discipline for items below the resolution bar.** Some candidates are real but not yet resolvable: needs trigger conditions (fresh attention in a future session; specific need for deferred content; appetite for methodology research). The methodology distinguishes deferral from rejection. Deferred items keep their context attached for future resolution rather than getting collapsed into "we considered and rejected this."

**Stage 5: Per-section self-grade.** Decomposed grading per stage, not uniform-A default. Section 1 grade considers inventory completeness against archive's actual surface area; Section 2 considers pattern detection against what canonical record corroborates; Section 3 considers recovery candidate quality against operator-side judgment; Section 4 considers deferral discipline against trigger condition specificity. The grades disrupt the uniform-A default that single-grade self-assessment produces.

## What the verification gates caught

The methodology surfaced three near-misses during recovery deployment: Claude-side initial actions that would have produced canonical-state drift if shipped without the verification gates firing. Each near-miss was caught by a specific mechanism the methodology requires; none was caught by general carefulness or operator memory.

**Near-miss 1: Wrong source path assumption.** During Decision 1 (RC-1, the highest-severity recovery candidate), Claude-side proposed a source path for the file that didn't match where the file actually lived in archive. The path was plausible (adjacent to where similar files lived in the archive's topical clustering), but the specific file wasn't there. The methodology's search fallback (verify the file exists at the proposed path before treating the recovery as resolved) caught the mismatch. Without the search fallback, the recovery would have shipped a path reference to a nonexistent file. The downstream effect: canonical record would have referenced a recovery target that didn't exist.

**Near-miss 2: Undeclared near-named duplicate.** During Decision 3 Step 1 (RC-5, the GB-3 fate determination case study), the archive contained two files with names so close that one could be mistaken for the other on filename glance. Claude-side initially treated them as the same file. The methodology's proactive notice discipline (when files have similar names, declare both before treating either as the recovery target) surfaced the duplicate. Without that discipline, recovery would have shipped one file as the canonical version while leaving the other in archive, and the wrong one might have been chosen.

**Near-miss 3: Undeclared workstream-related artifact.** During Decision 4 (RC-4, the AdSense compliance research prompt), the archive contained a related artifact (a verdict PDF) that wasn't part of RC-4's named scope but was operationally adjacent to it. Claude-side initially treated RC-4 as the recovery target without surfacing the related artifact. The methodology's proactive notice discipline (declare adjacent items even when they're not named in the recovery candidate) caught the omission. The verdict PDF moved alongside RC-4 to the same target directory; redundant duplicate elsewhere in archive got deleted as cleanup. Without proactive notice, the workstream would have shipped split across two locations.

Each gate fired because the methodology required a specific check at a specific stage. General carefulness wouldn't have caught any of the three; the gates did.

## What this generalizes to

The pattern isn't archive-review-specific. Any AI-assisted work output that piles up across sessions and needs review (drain outputs from earlier chats, prompt experiments banked across substrates, research artifacts produced in one project that become canonical in another, methodology research material accumulated across sessions) has the same structural problem and the same structural fix.

The required components transfer: an inventory pass that surfaces what's actually there rather than what memory says is there; canonical-state verification at each candidate decision; severity calibration with explicit rejection list; deferral discipline for items below the resolution bar; per-stage self-grade. The discipline scales independent of accumulated output size: 100 files, 1,000 files, or 10,000 files needs the same structural shape. Strategic sampling at the inventory stage handles size; verification gates at the recovery stage handle accuracy; deferral discipline at the resolution stage handles incompleteness without collapsing it into rejection.

What doesn't transfer cleanly: the specific severity tiers, the specific rejection criteria, the specific deferral trigger conditions. These are calibrated to the operator's canonical state and the specific accumulated work's substantive density. A different archive's HIGH would be a different threshold; a different review's deferral conditions would key off different trigger surfaces. The methodology shape is generalizable; the calibration is operator-and-context-specific.

## What I'm not claiming

I'm not claiming this methodology is novel. The components (strategic sampling for inventory, canonical-source verification at decision points, severity-tiered recovery, deferral discipline, decomposed self-grading) have prior art across information architecture, software engineering review practices, and research methodology. What I'm claiming is the operational synthesis: these components combined into a five-stage discipline that produces output ad-hoc review misses.

I'm not claiming the empirical case proves the generalization. One full run on a 109-file archive across one operator's accumulated work is n=1. The structural argument suggests the methodology should hold at larger scale, across multiple operators, and across different substrate ecosystems. The empirical evidence here doesn't establish those.

I'm not claiming the verification gates catch everything. Three near-misses caught; whether others slipped through is unknown. The methodology bounds known failure modes; it doesn't prove absence of unknown ones.

## What I am claiming

I'm claiming I built a structured archive review methodology, ran it on a 109-file accumulated archive, and produced concrete output: eight recovery candidates with severity calibration, six explicit rejections, ten deferrals with trigger conditions. The methodology ran clean through full execution.

I'm claiming the verification gates surfaced three Claude-side near-misses during recovery deployment that would have produced canonical-state drift if shipped without firing. The gates aren't theoretical; they caught specific errors at specific stages.

I'm claiming the pattern generalizes to any accumulated AI-assisted work output that piles up across sessions. Inventory pass first; canonical-state verification at each candidate; severity calibration with rejection list; deferral discipline; per-stage self-grade. The components have prior art; the operational synthesis produces what ad-hoc review misses.

That's the post.
