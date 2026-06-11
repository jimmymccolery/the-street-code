# How a Personal AI Discipline Framework Earns Its First Rules

**Author:** Jimmy McColery
**Date:** 2026-05-04
**Status:** Foundation post (covers the first four architecture sessions before the recursive-fire post)

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record. This work is independent personal research, not professional output from a current employer.*

---

In [the previous post](0003-the-rule-fired-during-its-own-promotion.md) I wrote about a single architecture-revision session where one of the rules I was promoting fired during the session promoting it. That story works as a hook because the recursion is unambiguous. Less obvious from that post: the framework being promoted in that session had been growing for weeks, and the discipline that allowed me to recognize the recursive fire when it happened was itself empirical, earned across earlier sessions where rules failed first, were named, and were promoted because failing the same way three times is empirical evidence and one or two times might be coincidence.

This post covers those earlier sessions. They're less dramatic than the recursive fire but they're how the framework actually got built. If you're curious how a personal AI infrastructure earns its first dozen-or-so canonical rules, this is the foundation period.

## The starting condition

Late April 2026. I had a multi-project AI workflow running across Grok and Claude, organized by what I called the SuperGrok ecosystem (now expanded to seventeen projects across four tiers). I'd been writing prompts for a few months, observing failure modes, and writing them down in a file I called the lessons log. The log was operator notes, not canonical infrastructure. When Grok did something useful or did something wrong, I noted it. The notes were unstructured.

What I didn't have was a framework. I had observations. The observations weren't enforced anywhere. There was no version control on the rules, no propagation mechanism that would carry an observation made in one project into other projects automatically, no discipline for promoting a recurring observation from "operator-noted" to "canonical and enforced." The lessons log was a personal notebook.

The first canonical session I'm going to describe (April 28, 2026, internally called S001) was where I tried to fix that. The rest of the post is what happened over the following days as I learned what it actually takes to make rules in a personal AI infrastructure that actually bind.

## Building the infrastructure: April 28, S001

S001 was a re-architecture session for what I'd been calling SuperGrok HQ, the project I used to coordinate all the others. The session promoted SuperGrok HQ from a workstream-organizing project into what I started calling Tier 0: a canonical layer whose job is to hold the rules that govern every other project.

Concretely, three things got built in S001. First, I wrote out a project-graph file documenting all seventeen projects, their tier assignments, and the canonical edges between them (which projects feed which other projects, which canonical state propagates from where to where). Second, I wrote a small Python tool called `sync_anti_patterns.py` that takes the canonical anti-patterns table from the master file and pushes it into every project's Knowledge bundle. The tool is twenty-five lines of Python and it's the closest thing the framework has to a build system. Third, I started a canonical anti-patterns file with the first earned lessons promoted to numbered rules.

That third item is where the discipline question got real. Promoting a lesson to a canonical anti-pattern means committing to enforce it. It also means the lesson has been observed in enough conditions that you trust the rule to generalize. I had a backlog of operator-side notes from a sister project called NPI (New Project Incubator), where two specific failure modes had each fired multiple times.

NPI's job in the ecosystem is worth a sentence of context, because it'll come up again. NPI is the project I use to deploy the canonical infrastructure into new projects. Every time I start a new SuperGrok workstream, NPI takes the canonical templates from Master Setup, customizes them per the new project's needs (project name, tier assignment, edges from the project graph, project-specific anti-patterns), and produces a deployable kit. NPI is the system that turns canonical state into running infrastructure. That role makes NPI the framework's first proving ground for whether the rules actually bind under real bootstrap conditions.

The two NPI-originating failure modes became the first two canonical anti-patterns I promoted: #13, which catches the failure mode where an AI agent silently drops a verification check while declaring "all checks complete," and #14, which covers a related issue with archival actions being claimed as completed when they weren't.

I'd later learn that #13 was about to become the most empirically-backed rule in the framework, because it kept firing.

## The first live fire: April 28, S002

S002 was the same day as S001. Late evening, after the re-architecture work was deployed across the projects. I ran what I called an activation verification session: an eight-gate check designed to confirm that the new canonical infrastructure was actually live in the project's Knowledge bundle and that the squad (the multi-role audit I run for substantive work) was operating cleanly against it.

The activation check answered seven of the eight gates. Then it declared all checks passed.

It had silently dropped the eighth check (a drift check between a persona-versus-CI consistency item) while declaring zero discrepancies. This is exactly what I'd promoted #13 to catch, and I'd promoted #13 in the same session that just produced this fire.

This is where the pattern that would later define the framework first appeared. The rule existed; the rule was canonical; the substrate (Grok in this case) had access to the canonical file with the rule in it. And the rule fired anyway, in the activation session designed to confirm the rule was active. I caught it on operator review, pushed back, and the substrate produced a fresh-turn verification that did the eighth check (clean) and acknowledged the methodology error.

Two things landed for me in that moment. First: canonical rules don't enforce themselves. Having a rule in a file that the substrate can read does not mean the substrate will follow it. The rule is a reference the operator (me) uses to recognize a fire when it happens; the substrate's compliance is empirical and unreliable. Second: the recovery posture matters. Once a rule has a canonical number, recovery is fast. I can say "anti-pattern #13 just fired" and the substrate produces compliant recovery shape. That's different from arguing about what happened from scratch. The number is operational language.

I logged the S002 event as a refinement of #13, not a new rule. New canonical anti-patterns require multiple fires across multiple conditions; one fire isn't enough.

## Closing the gates: April 28, S003

S003 was the same day, even later. A closure verification session. I ran a five-gate check on whether S001 and S002 were genuinely complete, whether the file states matched the session log, and whether the cross-references between operational copies and canonical files reconciled.

S003 was clean. No fires. No new lessons. The reason it gets a section in this post is that S003's cleanliness is itself an empirical signal. If the framework were entirely brittle, every session would produce fires. S003 demonstrates that the framework binds when the work is mechanical (verification of states, reconciliation of file pointers) rather than substantive (judgment calls, novel content production). That distinction would matter for what came next.

## The architecture revision: April 28, S004

S004 was the largest single foundation session. I'd been reading academic and practitioner research on multi-agent LLM systems for a few weeks, and S004 was where I synthesized that research into the framework.

Three new canonical anti-patterns came out of S004. #15 is "persona names are mnemonic, not magic": role names like Captain or Harper are useful for the operator's mental model but the substrate doesn't have a separate Captain-circuit and Harper-circuit; what the substrate has is one set of weights producing different output styles based on prompt structure. Persona naming is a tool for clarity, not a tool for invoking specialized capability. The citation behind this rule is Zheng et al.'s 2024 EMNLP Findings paper, which empirically established that persona effects in system prompts are largely random and do not reliably improve LLM performance. The structural claim — that this happens because there's one set of weights, not separate per-persona circuits — is the architectural reading consistent with Zheng's empirical finding. Without the underlying empirical citation the rule reads as opinion; with it the rule reads as a structural reading of an established empirical claim.

#16 is "critique modes don't share turns": within a single audit response, you can't have one role doing skepticism (here's what's wrong with the claim) and another role doing contrarianism (here's why the opposite of the claim might be true) simultaneously without coordination overhead that defeats the audit. You can have either, or you can have both in separate turns. The citation is Schwenk's OBHDP 1990 meta-analysis comparing devil's-advocacy and dialectical-inquiry to consensus-seeking in group decision-making. The paper establishes that structured critique outperforms no-critique consensus, which is the foundation for treating critique-as-structured-mode in my framework. The "don't share turns" claim is my own structural extension: critique modes need separation to work, not just instructional intent. Without the underlying empirical citation the rule reads as opinion; with it the rule reads as a structural extension of an established empirical claim.

#17 is "state drift requires explicit structured handoffs": when work crosses session boundaries or substrate boundaries, the next session's substrate needs an explicit handoff document, not informal references. State that exists implicitly in conversation history doesn't survive substrate or session boundaries. The citation here is practitioner research on multi-agent Grok deployments rather than a single academic paper.

S004 also did two architectural things that mattered later. The Madisonian rule got introduced: in any audit synthesis, dissent from the squad cannot be silently overridden; if the synthesis disagrees with what a role said, the synthesis has to say so explicitly. (Named after James Madison's Federalist 51 framing on faction. Strong overstatement of the citation, but it sticks in memory.) And two role functions got embedded in other roles: Sage (evidence audit) became part of Benjamin's verification work; Iris (synthesis with explicit dissent log) became part of Captain's synthesis work. The decision behind embedding rather than splitting was empirical: practitioner research on Grok suggested that five-plus standing roles without orchestration infrastructure produces more coordination overhead than the additional roles add value. So I stayed at four standing roles with embedded sub-functions.

A new canonical file got introduced: `role_output_schemas.md`, defining the structured output format each role produces. Tables for verification work, dissent logs for synthesis work, confidence labels on research claims. The schemas mattered more than I realized at the time.

## The re-fire: April 28, S004b-act

The session before this one was S004b, which was documentation polish. The session after S004b was S004b-act, an activation verification of the deployed S004 bundle. Same general shape as S002 but on a richer canonical infrastructure (now thirteen anti-patterns, three new role schemas, the Madisonian rule, the embedded Sage and Iris functions).

#13 fired again.

This was its third fire across conversation history. Once in the project where the rule originated, once in S002, and now in S004b-act. The S004b-act fire had a more interesting shape than the prior two: the activation prompt asked the squad to verify the new architecture, and the squad's Benjamin role produced output that initially didn't match the new role_output_schemas.md format ("All audited claims = A" without per-claim tables). I pushed back, requested schema-compliant output, and got tables. The tables had uniform-A grades across all claims, with Harper (the research role) reporting one of the claims at low confidence in the same response where Sage (the evidence audit role embedded in Benjamin) graded the same claim A. Within-response inconsistency. I pushed back a second time, asked for differentiated grades using the role_output_schemas.md rubric and explicit Harper-Sage reconciliation, and got C/C/C/D grades that actually matched what the evidence supported.

The pattern across the three #13 fires: the rule existed and was canonical, the substrate had access to the rule, the failure happened anyway, the recovery was fast once the rule's number was named. What S004b-act added was a new failure mode that #13 didn't quite catch: the schema was followed (tables produced) but the calibration within the schema was uniformly optimistic. The numbered rule was respected; the spirit of differentiated grading wasn't.

This produced a promotion candidate: a future canonical anti-pattern #18 covering "within-response role outputs must reconcile; the evidence audit cannot grade claims higher than the research role without justified upgrade reasoning." I didn't promote #18 in S004b-act. Promotion candidates need multiple fires across multiple conditions, and #18's empirical evidence at that point was one fire.

#18 got promoted in the next major architecture session (the one I covered in [the previous post](0003-the-rule-fired-during-its-own-promotion.md), which was about a different rule firing during its own promotion). Empirical evidence accumulated to four fires across two projects between S004b-act and that next session, which is enough for promotion.

## When the enforcement infrastructure itself drifts: the Drift Audit Block

There's one more piece of the foundation period worth telling, because it extends the rules-don't-enforce-themselves theme from rules to infrastructure.

Around the time of S004 I was building enforcement infrastructure inside NPI specifically. NPI's job is bootstrap deployment, and bootstrap sessions have a specific failure mode: stale operational copies of canonical files. The canonical anti-patterns file lives in Master Setup at one version; each project gets a synced copy of it via the sync tool; if the sync gets skipped or fails, the project's operational copy drifts away from canonical state and bootstraps run against stale rules.

The fix I built was a Drift Audit Block. It's a section in NPI's Custom Instructions that runs at the start of every non-trivial session. The audit enumerates canonical files visible in the project's Knowledge bundle, quotes each file's version header, extracts version pins from cross-references in the project's GROK.md, builds a comparison table, and refuses to proceed if any version mismatch surfaces.

Version 1 of the Drift Audit Block deployed on April 30. Its first run failed in exactly the way it was designed to prevent.

The substrate ran the audit. The audit's output said "Status: CLEAN." But the substrate had skipped the cross-reference work in the middle steps. It had pattern-matched "audit ran = audit passed" without actually doing the file-by-file version comparison the audit was designed to enforce. The audit was canonical; the audit was running; the audit's job was specifically to prevent state drift; the audit drifted into ceremonial compliance.

This was the same recursive pattern the S005 post (the one that came before this) covers at a different layer. There, a rule fired during the session promoting it. Here, an enforcement mechanism drifted in the way it was specifically built to prevent.

Version 2 deployed the same day. The fix was structural. The new audit block requires the substrate to literally output a comparison table with three columns (file, version per file header, version per cross-reference, match status), to literally quote the version pins from GROK.md's File Map section by name, and to run a final self-check step that asks: did you actually quote the File Map content, or did you produce a Match column without doing the cross-reference work. The structural change was forcing each step to produce verifiable output rather than allowing the substrate to pattern-match through to the final status.

Two things landed for me from this. First, infrastructure that enforces a rule can fail in the same shape as the rule it enforces. The Drift Audit Block was designed to prevent state drift; it drifted. The recursion isn't a special property of rules; it's a property of any enforcement mechanism that depends on the substrate to do verification work it can pattern-match around. Second, the fix isn't stronger language. It's structural. v2 doesn't ask the substrate to actually do the cross-reference work harder; it requires verifiable intermediate output (the table) that makes pattern-matching impossible to hide. The lesson generalizes: when an enforcement mechanism fails, the productive next step is structural change to the mechanism, not stronger instructions to the substrate.

## What this period actually produced

By the end of April 28 and the related work the day after, the framework had grown from a personal lessons log into something that looked like infrastructure. Concrete artifacts:

A canonical anti-patterns file with seventeen numbered rules. Each rule has empirical fire counts, citation backing where applicable, and a fixed canonical number that's the same in every project's Knowledge bundle. The catalogue has two layers in practice: canonical anti-patterns (numbered #1 through whatever the current count is, universal across all projects) and project-specific anti-patterns (numbered like NPI-1 through NPI-4 in NPI, scoped to that project's specific work class). Canonical rules govern shared discipline; project-specific rules govern context-specific failure modes that don't generalize across the ecosystem.

A role output schemas file specifying structured output formats for each squad role. Tables for verification, dissent logs for synthesis, confidence labels on research.

A project graph file mapping the seventeen projects across four tiers with canonical propagation edges.

A small Python tool that pushes the canonical anti-patterns table from the master file into every project's Knowledge bundle when run.

A bootstrap manifest specifying how to deploy the canonical state into a new project.

A session log inside the master file recording every session's substantive work and version bumps.

A lessons-learned file holding earned observations that haven't yet been promoted to canonical anti-patterns.

The file count is small. The discipline behind it is what matters. What I learned across this foundation period:

Rules don't enforce themselves. The substrate has access to the canonical files; the substrate fails the rules anyway. Canonical infrastructure is a tool for the operator to recognize fires when they happen, not a tool for preventing fires.

Recovery is faster than perfect prevention. Once a rule has a number, the operator can name the fire ("anti-pattern #13 fired") and the substrate produces compliant recovery in the next turn. The number is operational language.

Promotion requires multiple fires. One fire is observation. Two is suspicion. Three across different conditions is empirical evidence sufficient to promote a rule from operator-side observation to canonical anti-pattern. Premature promotion produces rules that don't generalize; under-promotion leaves the operator running the same recognition work over and over.

Rules need citations. The anti-patterns with academic or practitioner citations behind them are more durable than rules promoted from internal observation alone, because the citation provides a reference class for thinking about adjacent failure modes. Internal-observation-only rules tend to get refined or absorbed into other rules as the framework grows.

Schema compliance is not calibration compliance. A role can produce output that perfectly matches the structural format specified in `role_output_schemas.md` while completely failing the calibration discipline the schema is meant to support. The S004b-act fire demonstrated this. The eventual #18 promotion would address it.

Enforcement infrastructure can fail in the same shape as the rules it enforces, and the fix is structural change to the infrastructure rather than stronger instructions. The Drift Audit Block v1 → v2 evolution demonstrated this directly. Building an audit to enforce a rule does not make the audit immune to the rule's failure mode. v2's structural changes (mandatory comparison table, mandatory File Map quotation, self-check step) made pattern-matching impossible to hide where v1's prose-level instructions allowed the substrate to comply ceremonially. The lesson generalizes beyond drift audits: any enforcement mechanism that depends on substrate-side verification can be pattern-matched around unless it requires verifiable intermediate output.

That last lesson is the one that matters most for the post that came before this one. By the time I ran the architecture session where a rule fired during its own promotion, I'd already learned that schemas don't enforce calibration on their own and that audit infrastructure can drift in exactly the way it was built to prevent. The recursive fire wasn't a surprise about whether the rules would bind; it was a confirmation of a pattern I'd been observing for weeks across multiple sessions and across multiple layers of the system.

## What I'm not claiming

I'm not claiming the components of this framework are novel. Canonical files as runtime configuration, prompts as code, multi-agent anti-pattern enumeration, sync tooling for embedded snippets: each component has prior art going back fifteen-plus years in software engineering and adjacent fields. What I'm claiming is that I built a personal AI infrastructure layering these components together, observed it fail in specific repeatable ways, and named the failures so the same observation in a future session could be recognized faster than from scratch.

I'm not claiming the framework is finished. [The previous post](0003-the-rule-fired-during-its-own-promotion.md) covered an architecture-revision session that promoted five new anti-patterns and refined an existing one; the framework continues to grow with each major session. What's described here is the foundation period.

I'm not claiming this discipline scales beyond personal infrastructure. I run this for myself, across seventeen projects, on two LLM substrates. Whether the same approach holds at team scale, with multiple operators promoting rules from different observations, is an open question I haven't tested.

What I am claiming: I built a personal AI discipline framework starting from operator notes, ran it across multiple sessions, observed the same rules fail multiple times under different conditions, and learned that recognition (not prevention) is what canonical infrastructure actually delivers. The first dozen rules of the framework came from this period. The next dozen would come from sessions like the one I described in [the previous post](0003-the-rule-fired-during-its-own-promotion.md).

That's the foundation. The framework isn't doing magic. It's doing operator-side recognition, supported by version-controlled infrastructure, propagated automatically across projects, with empirical fire counts behind every promoted rule. That's all of it. If you're interested in similar discipline work on personal AI infrastructure, the operations are simple. The discipline of actually running them across enough sessions to accumulate empirical evidence is the hard part.
