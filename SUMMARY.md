# What This Repo Documents: A Plain-Language Summary

The Street Code is a personal AI discipline framework: a set of rules and procedures for catching the kinds of mistakes that AI substrates (the AI programs executing the work, like Claude or Grok or Gemini) reliably make under sustained operator use. The framework's core is a canonical record (an authoritative state kept across reference files that every substrate session reads). Within that canonical record sits an anti-pattern catalogue (named failure modes, each with a rule, an example, and a recovery procedure). The framework also includes verification (check passes against canonical state at structurally-independent gates), a multi-role architecture for cross-checking work, and explicit operational discipline rules for sustained-session work.

The framework evolves through empirical accumulation. New patterns get noticed across substantive work; once a pattern fires multiple times across distinct work classes (the multi-fire bar, typically n=3 or more), it becomes a canonical promotion candidate. Promotion adds the pattern to the anti-pattern catalogue with an empirical foundation and propagates the entry across the framework's reference files. The bar prevents premature canonization of single-fire patterns that might be coincidence rather than structural; it also requires cross-class validation rather than within-class repetition.

These 29 posts document roughly two months of substantive framework development across April and May 2026. Each post captures a specific empirical fire, the discipline that emerged, or a methodological observation about how the framework operates. Reading the posts in order shows the arc: first observations about substrate behavior, then the architecture that emerged, then the methodology research that named what the work actually is, then the operational discipline rules canonized at the most recent session. Posts are immutable once committed; the canonical record continues evolving.

## How to read this repo

Posts are numbered 01 through 29 in the order the work happened. Reading them in order shows how the framework developed. Each post below has a 4-6 sentence summary covering what happened, what discipline emerged, and why it matters structurally. Click into a post for the full empirical record, the framework's response, and the calibrated argument about generalization.

## Per-post summaries

### 01. Experiment 1: Does Discipline Survive Substrate?
**Date:** 2026-05-02

The author had been running his AI discipline framework on Grok and noticed six recurring failure patterns. He swapped the substrate (Claude in place of Grok) under identical framework rules to test whether the failures were specific to one program or structural to the framework's gap. None of the six patterns reproduced. The result is suggestive evidence that the anti-patterns operate at framework level rather than substrate level. One run is hint, not proof; honest n=1 calibration carries through to subsequent posts.

### 02. Experiment 5: Where the Discipline Framework Bound, and Where It Didn't
**Date:** 2026-05-02

Same kind of test as Post 1, but back on Grok with the framework's rules fully loaded. Procedurally the substrate followed every framework step; rule-following looked perfect. But when the substrate fetched a real web page to verify a claim, it reported the page as 37 words; ground-truth verification showed the page was about 1,500 words of substantive content. The framework made the work look careful at the procedural layer but didn't enforce empirical correctness at the verification layer. The honest finding: the discipline binds at one layer but not the other, and knowing where it half-works is more useful than assuming uniform efficacy.

### 03. The Rule Fired During Its Own Promotion
**Date:** 2026-05-03

The author was promoting an anti-pattern into the canonical catalogue. The new rule prohibited writing placeholders like "[full content here]" as if they counted as finished work. During the same session in which the rule was being canonized, the substrate produced files containing exactly that placeholder pattern. The rule's first empirical proof of necessity fired during its own promotion. Real-time fire-plus-recovery in a single session is stronger evidence than retrospective recollection across days.

### 04. Three Runs at the Asymptote: When Prompt-Language Hits a Training Objective
**Date:** 2026-05-03

The author hit the same problem three times and tried to fix it by writing his instructions to the substrate more carefully each iteration. Each iteration the failure changed shape rather than going away, like squeezing one part of a balloon. Reading the substrate's own documentation revealed the substrate was trained to produce the failing behavior; no instruction would override it. The fix had to be architectural rather than instructional: route sub-tasks to different substrates rather than expect one to handle all the work. Some failures live below the prompt-engineering floor and require structural redesign.

### 05. How a Personal AI Discipline Framework Earns Its First Rules
**Date:** 2026-05-04

Foundation post covering how the framework's first rules earned canonical status across April 2026. Before formal anti-pattern numbering, the author had informal notes on recurring failure patterns; the patterns kept happening anyway. The shift came when he started treating the catalogue as a recognition tool rather than a prevention list: once a fire happened, naming it as "anti-pattern #N" let recovery proceed in seconds. Rules don't stop mistakes from happening; rules stop the operator from spending hours figuring out what just broke. That reframe (recognition over prevention) shaped how every subsequent rule got designed and tested.

### 06. What Auditing the Audit Taught Me About Substrate Routing
**Date:** 2026-05-04

The author used a substrate to audit its own writing and observed an asymmetry. The substrate handled deterministic verification well (counting punctuation, checking verbatim quotes) but failed at honest critique; it kept reporting the work as excellent. A dedicated critic role inside the same substrate, structurally tasked with finding fault, surfaced real issues. A different substrate auditing the same work surfaced still more. Different sub-tasks within a single audit need different substrate routings, and one set of eyes is rarely enough. (See also Post 04, the writing being audited in this story.)

### 07. When the Architecture Worked: Two-Cycle Validation
**Date:** 2026-05-04

The author validated the multi-substrate architecture across two different work classes. Cycle 1 (an architecture-revision session) passed every verification check (23 of 23). Cycle 2 (a premortem cycle) passed 32 of 33; the one anomaly was a structural artifact about deployment timing rather than a design failure. The validation supported the architecture's design at n=1 per work class. The remaining anomaly turned into its own canonical lesson, documented in Post 08. (See also Post 11, which revisits this cycle two days later under cross-substrate audit and finds the anomaly more substantive than the original post recognized.)

### 08. When Deployment Outpaces Decisions: A Mid-Iteration Alignment Problem
**Date:** 2026-05-04

When iterative work produces a piece that feels finished mid-cycle, the temptation is to save it into permanent records before the cycle closes. The author did that; subsequent corrections to the same work changed what the saved version should have been, leaving stale state in the canonical record. The rule that emerged: save once at cycle close, not when partial output feels ready. Three recovery paths got named (accept the deployed state, roll back canonical, treat the rewrite as superseded), each with different costs depending on what's already downstream. The lesson generalizes beyond this framework to any iterative-work context.

### 09. When Verification Catches Itself: An Audit Chain Across Two Sessions
**Date:** 2026-05-04

The author ran two verification passes against the same work at different times. The second pass disagreed with the first, and the second pass was correct. The reason: the second pass read the original sources directly, while the first had cited related context. When verification gates copy from each other instead of reading canonical state independently, errors propagate; when each gate reads canonical independently, errors get caught. Independence between verification gates is the structural property that makes the framework's chained-audit cycles do real work.

### 10. When the AI Fires Your Own Discipline: Notes on Frame-Inheritance Errors
**Date:** 2026-05-04

The author has discipline rules preventing himself from drafting from memory of canonical state rather than reading canonical files directly. The substrate exhibits the same failure pattern, drafting from chat-context inheritance rather than reading canonical files even when it could. Three independent fires of this pattern surfaced in one extended session; each was caught by careful checking. The discipline rules originally framed for the operator generalize to the substrate; any helper that can take a memory shortcut needs the same verify-canonical-first discipline (reading the canonical record before drafting any specific text). Catching these errors took multiple recovery layers, not a single check.

### 11. What Cross-Substrate Audit Surfaced That Same-Substrate Verification Missed
**Date:** 2026-05-06

The author had run a Phase 5 verification step (a final-state check against canonical sources), redone it after the work expanded, and saved the redone check over the original at the same filename. The original was unrecoverable; the canonical record still pointed to it as evidence. A different substrate (Gemini) audited the work and flagged numerical claims worth scrutinizing; investigation surfaced the missing-source problem. Same-substrate verification couldn't have caught this because the substrate had pattern-matched past it twice already. Cross-substrate audit (independence at substrate level, not just at role level) is the structural property that catches what same-substrate verification cannot. (See also Post 08, which named an earlier version of the save-too-early pattern.)

### 12. Archive Review as Methodology
**Date:** 2026-05-06

Methodology lesson on retrospective archive review. The author had 109 old files to evaluate for canonical-record relevance; memory-first review (recalling what seemed important) produced incomplete coverage. Switching to checklist-first review (enumerate everything, then evaluate per-item) surfaced 8 keepable findings, 6 archive-closed items, 10 deferred items, and caught 3 near-mistakes. The discipline is structural: memory privileges vivid recall over actual importance; checklist scaffolding catches what memory's salience filter misses. The methodology applies to any retrospective review where memory's coverage is partial by default.

### 13. Reflection as Methodology Research Discipline
**Date:** 2026-05-07

End-of-session work has two distinct kinds of wrap-up. Type 1 asks whether the substantive job got done correctly; Type 2 asks whether the doing of it surfaced anything new about how the framework operates. Without explicit Type 2 prompts at session close, methodology-research findings disappear into chat history. The discipline is asking the Type 2 question on purpose, every time, regardless of perceived productivity. Across two substantive sessions, structured Type 2 reflection produced approximately 25 canonical lessons that would otherwise have been lost. (See also Post 12 for a related discipline: structured review of historical work.)

### 14. When to Build Cross-Project Shared Infrastructure
**Date:** 2026-05-07

On 2026-05-04 the author's static-site cluster reached the threshold where per-project duplication of deployment lessons became more expensive than centralizing them. Four domain-agnostic conventions (connection, security, document-root, tooling) got promoted from per-site documentation to a shared cluster reference, with each project consuming via a thin wrapper containing only project-specific values. The discipline names a trigger condition (the project count where shared-reference setup cost becomes lower than continued per-project coordination cost) and an operational shape (shared content plus thin per-project wrappers). The threshold is not universal; it depends on how similar the projects' tooling concerns are. Three is the inversion point for this specific cluster, not a generalization.

### 15. Discipline as Substrate, AI Capabilities as Swappable Layer
**Date:** 2026-05-07

Most framing treats the AI substrate as the primary value and the discipline around it as decoration. The author argues the inversion is correct: the discipline is the substrate; the AI capabilities are the swappable layer. The structural pattern has prior art (compiler design separating language semantics from target architecture; database systems separating query language from storage engine, where the language layer is invariant and the backend is replaceable). Across roughly ten days running the framework concurrently on three substrates, the discipline layer demonstrated invariance under substrate-class behaviors that should have been substrate-specific; the substrates differed in capability, but the failure modes the discipline caught were the same everywhere. The portability claim is theoretical-architectural rather than substitution-validated; no major substrate has retired during the framework's life so far.

### 16. Design-Based Research on AI-Assisted Personal Practice
**Date:** 2026-05-07

This post asks a positioning question: what kind of work has the author been doing with this framework? The argument is that it qualifies as design-based research (DBR) on AI-assisted personal practice, in the Brown 1992 / Cobb et al. 2003 tradition, supplemented by Becker's tricks-of-the-trade discipline and Goffman's transcontextual method. The framework maps to DBR's core requirements with substantive depth in four areas, loose mapping in four more, and two honest gaps (no second operator deployed; no co-investigator collaboration). The qualifying claim is "design-research-adjacent solo practitioner-research", not canonical multi-stakeholder DBR. Naming the kind of work gives it methodological standing that "personal productivity blogging" doesn't carry. (See also Post 07 for the two formally validated work classes this positioning rests on.)

### 17. Recovery-from-Drift as Framework Discipline
**Date:** 2026-05-07

Across a substantive single-session arc, the same kind of drift fired multiple times. Each fire got caught by a different framework mechanism: pre-mutation verification gates; the verify-then-deploy two-step workflow; reflection prompts at session close; the operator catching residual drift directly. The discipline distinguishes drift-prevention (the anti-pattern #10 verify-before-stating territory, which pays cost upfront per claim) from recovery-from-drift (downstream gates that pay cost only when work is about to enter permanent record). The argument is structural: drift-prevention costs effort every time the substrate generates anything; recovery-from-drift costs effort only at points where permanent-state mutation is imminent. The four mechanisms compose; together they catch what any single mechanism would miss. (See also Post 13 for one of those mechanisms: the end-of-session reflection prompt.)

### 18. What Running on Auto-Pilot Revealed About Framework Structure
**Date:** 2026-05-07

The author ran the framework at deliberately reduced verification-reviewer intensity to test what survived without close operator attention. Substrate-architectural mechanisms (substrate self-checks before save; the two-step verify-then-mutate workflow; reflection prompts at session close) operated without his attention. Operator-side functional roles (six of them: designer, decision-maker, double-checker, researcher, scope-keeper, reader-translator) fired across the session even at reduced intensity. Two recursive fires happened during the session itself: the framework caught its own drift while the author was writing about catching drift, suggesting structural pattern rather than coincidence. The framework's discipline is more substrate-architectural than operator-attention-dependent than the author had assumed; one session at one experimental condition is a hint, not proof. (See also Post 17 for the recovery-from-drift framework this post extends.)

### 19. When the Audit Substrate Isn't Independent Enough
**Date:** 2026-05-08

On 2026-05-08, two audit substrates reviewed the same canonical state during S008 closeout. Grok via web UI produced uniform-A grading with "verified: consistent" across seven cross-file consistency claims. Gemini Deep Thinking produced seven severity-tagged findings (one critical, three high, one medium, two low) on the same canonical state. Phase C-Verify (deterministic file reads as ground truth) confirmed all seven Gemini findings and falsified Grok's verification claims on at least four of the seven surfaces. The discipline names substrate-class-distance as the structural property that makes cross-substrate audit do real work; family-similar substrates can pattern-match each other's habits in ways that look like consensus but aren't. (See also Posts 06 and 11 for earlier cases where outside eyes caught what inside eyes missed.)

### 20. When the Council of Three's Third Leg Is Wrong
**Date:** 2026-05-09

The author ran a series of corrective sub-stages, each closing with verification by a structurally-distinct third audit substrate (the Council of Three architecture: three substrates running independently against the same canonical state). Three rounds of triangulation fired; in one round, the third leg's findings were themselves wrong. The discipline names a structural property: a third-leg FAIL finding is not load-bearing on its own, and ground-truth diagnostic against the flag must run before any remediation. Cross-leg disagreement is itself a verification signal, not a failure of the Council's design; both outcomes (third leg right, third leg wrong) preserve the architecture's value when ground-truth diagnostic runs against the flag. The refined rule canonized: "Council of Three third-leg independence is necessary but not sufficient; cross-leg disagreement is itself a verification signal."

### 21. When a Verification Arc Doesn't Close on the First Try: Corrective Sub-Stage as Discipline
**Date:** 2026-05-09

S009 was a multi-stage Type 5 verify-then-deploy arc for canonical-state advancement; three audit findings during closeout triggered three corrective sub-stages over roughly twenty-four hours. The corrective sub-stage discipline names three structural properties. Each sub-stage operates against the audit findings directly rather than re-running the same internal verification logic that missed the drift. Each sub-stage is itself a Type 5 verify-then-deploy at smaller scale, with its own pre-mutation read, residual greps, and post-mutation verification. Sub-stages can spawn further sub-stages recursively when their own audits surface residual drift; the recursion is the expected shape when scope gaps compound across substrates and file formats, not a defect. The canonization principle: "Corrective sub-stages are first-class and should be added as needed without abandoning the broader stage architecture." (See also Post 20 for the third-leg-fallibility lesson driving parts of this corrective sub-stage arc.)

### 22. When "The" Stacks: An Article-Stacking Discipline at n=5 Empirical Validation
**Date:** 2026-05-09

During S009 corrective sub-stage 2, find-and-replace operations on role names produced "The"-stacking artifacts where the substituted name with its leading "The" got inserted into sentence positions already governed by another determiner (the bulk substitution turned "log a Hall Monitor lesson" into "log a The Hall Monitor lesson"). Five empirical fires accumulated within one session arc. The convention canonized: "The" is preserved at sentence-start, in possessive constructions, and in standalone subject references; "The" is dropped in compound-modifier post-determiner positions (after a, the, every, each, any). The discipline operates at the reading layer rather than the rule-content layer; bulk substitutions need context-awareness for definite-article handling. The pattern is adjacent to the canonical-source-discipline family that anti-pattern #10 governs.

### 23. Verification-Query Precision: When the Question Asked Doesn't Match the Canonical State
**Date:** 2026-05-09

During S009 Step 11 corrective sub-stage 2, the third-leg audit surfaced a verification-query that asked the substrate to confirm canonical-role-architecture by enumerating six persona names from a recent rename. The canonical architecture is four standing roles plus two embedded functions, not six discrete personas; the query was drafted from session-memory of the rename rather than from a literal canonical-schema read. Two fires within S009 surfaced the class. The discipline names verification-query precision as a sub-class of anti-pattern #10: drafting verification queries against canonical architecture must read the literal canonical schema before drafting, not paraphrase from session-memory. The class operates at the question-asking layer; a precision-class error produces a question whose answer cannot match canonical state regardless of the answering substrate's reading discipline.

### 24. Recursive Scope-Gap: When Each Correction's Scope Generates the Next Fire
**Date:** 2026-05-09

Three structurally-analogous fires accumulated within twenty-four hours during S009 corrective sub-stage work on 2026-05-08. Each fire was a deployment-spec scope omitting a structurally-relevant propagation target: Stage 2 missed downstream operational-copy files; Step 8.5 missed canonical-layer Grok Knowledge re-uploads; Step 10.5 missed non-.md canonical files like .docx. The discipline names the pattern as recursive: each correction's refined scope is itself subject to the same gap class because the corrective rule was drafted against the prior fire's empirical record alone, without anticipating analogous structural reaches. The family-structural property (same gap class, different structural locations) supports multi-fire-bar canonization candidacy under a single Topic cluster rather than three independent rule additions. The recursion is what the property is called; each correction's edge becomes the next fire's surface.

### 25. Drafting-Drift Canonical Promotion Arc: From Single-Fire to Multi-Fire-Met
**Date:** 2026-05-09

Drafting-drift fires accumulated to roughly nineteen cumulative session-fires across two days of substantive session work, spanning substantive content drafting, Phase 5 correction prompt drafting, and canonical-state-update prompt drafting. The pattern: the drafting substrate produces text against memory of canonical state rather than against an immediate canonical-state read; canonical state read at execution time reveals the mismatch. A citation-precision sub-class surfaced empirically distinct at six fires within one banked post (paraphrases presented as verbatim quotes; quoted segments reconstructed by inserting connector words; experimental-design mischaracterization). The canonical record positions drafting-drift relative to anti-pattern #10 as a candidate for refinement, not yet a confirmed sub-class; the multi-fire bar is exceeded within-session, but cross-session validation is pending. Canonical promotion candidacy is active per lessons-learned.md line 971.

### 26. Operational Discipline Rules: Five Canonized From One 2026-05-07 Session
**Date:** 2026-05-09

On 2026-05-07 the author ran the longest sustained-discipline session of the framework so far (six GitHub publications, five Phase 5 verification cycles, twenty-five-plus corrections, nine canonical-record updates). Late in the session, gap-identification work surfaced five operational rules that had been load-bearing across multi-session development but had never been written down. The five rules: standing direction; pre-delivery re-read step; A+-quality calibration target; catch-and-fix at point of detection; per-section verification combined with Phase 5 batched review. Each rule's empirical foundation cites specific session evidence rather than general framework intuition; Rule 2 and Rule 4 connect to the drafting-drift family documented in Post 25 (the artifact's cross-references make the bounded link explicit). The artifact's value is reference: workflow constraints that had been informal operating assumptions become named, dated, citable canonical record. (See also Post 25 for the drafting-drift connection.)

### 27. Council of Three Outcome Patterns: Three Structurally Distinct Shapes From One Architecture-Revision Session
**Date:** 2026-05-10

In one architecture-revision session the author ran three canonization decisions through the Council of Three (three structurally-distinct substrates verifying the same question concurrently). Each decision produced a different convergence shape. Pattern 1 was minority-position selection (one substrate dissented toward the operator's eventual choice; operator selected against the 2-of-3 majority on operator-side reasoning grounds). Pattern 2 was unanimous on the canonization path with split on implementation strategy (substrates agreed on promotion; split on whether to use a new file or update the existing one). Pattern 3 was unanimous with the same per-element split appearing across all three substrates (each substrate independently produced the same 5/1 archetype split — same five ratified canonical, same one held as research). Pattern 3 is structurally diagnostic: same per-element split across substrate classes is harder to explain via substrate-stylistic-priming than convergence at decision-path level alone, supplying empirical evidence relevant to the substrate-stylistic-priming question Post 19 treats.

### 28. Cross-Session Validation Sections: A Substrate Halt-and-Flag Becomes Canonical-Artifact Section Convention
**Date:** 2026-05-10

During the same architecture-revision session that produced the three Council outcome patterns from Post 27, all three substrates surfaced the same halt-and-flag at two consecutive canonical artifact promotion decisions: the artifacts being promoted had empirical foundations concentrated in single sessions and lacked structural scaffolding for ongoing multi-session evidence accumulation. The substrates each recommended the same fix — adding a Cross-Session Validation section to the canonical artifact as a condition for promotion. Two such sections got deployed within that one arc; both are structurally identical (open-ended; entries with date, evidence summary, and source citation; future sessions append). The convention reduces deliberation overhead at future architecture-revision sessions (substrates can recommend section addition per established convention rather than re-surfacing the gap) and produces an accumulating evidence stream that operates across framework time. Whether the convention extends beyond first-class canonical promotion to non-promotion canonical-artifact updates is an open question awaiting operational trigger. (See also Post 27 for the three Council outcome patterns from the same arc.)

### 29. Bundled-Canonization-Correction: Hybrid Ratification as Retroactive Architecture-Revision-Session Discipline
**Date:** 2026-05-10

One of the artifacts being ratified during the same 2026-05-10 architecture-revision session had self-declared "Status: Canonical" in its file header two days earlier — but the declaration was bundled with a multi-stage rename arc rather than the product of standalone architecture-revision-session-level deliberation on the underlying canonization question. The session corrected the bundled canonization retroactively. The substantive canonization was ratified at element level (five of six archetypes met the empirical bar; one held as research with explicit revisit criteria); the procedural premature-canonization was flagged in the canonical record. Hybrid ratification with explicit per-element ratification serves as canonical example for correcting bundled file-level decisions retroactively. The precedent leaves open an audit scope question (which other canonical artifacts may have file-header self-declarations bundled with multi-mutation deployment work) and a canonical-artifact creation protocol question (whether future canonical artifact creation should explicitly require standalone-deliberation flag at architecture-revision session). (See also Post 27 for the Council outcome pattern that made per-element ratification operationally feasible, and Post 17 for the recovery-from-drift framework the Sentinel ratification preserves.)

## What's next

This repo will keep growing as new posts publish. Numbered ordering means new posts get the next number (30, 31, and so on) and join the bottom of the per-post summaries above. The intro at the top updates as the framework's research direction develops; new entries in the canonical record produce new posts that document specific empirical fires, discipline responses, or methodological observations as they emerge.
