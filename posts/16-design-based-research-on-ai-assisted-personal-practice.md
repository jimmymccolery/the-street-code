# Design-Based Research on AI-Assisted Personal Practice

**Author:** Jimmy McColery
**Date:** 2026-05-07
**Status:** Methodology research positioning paper documenting how a personal AI infrastructure framework maps to design-based research (DBR) requirements; n=1 framework with two formally validated work classes; honest hedges include narrower scope than canonical DBR (solo-operator vs classroom), operator-attested empirical record, transmission gap (no second operator deployed); suggestive not conclusive

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record. This work is independent personal research, not professional output from a current employer.*

---

Solo AI-assisted personal practice has produced substantive findings over the past several months. Anti-pattern catalogs codifying AI failure modes that fire reliably across substrates. Verification protocols that catch errors single-substrate review misses. Architectural validation cycles producing 23-of-23 and 32-of-32 verification records on two distinct work classes. The findings are operationally useful and methodologically interesting.

The standard framing options for this kind of work are inadequate. "Personal methodology" sounds like productivity-hack territory. "Blog post journal" sounds confessional. "AI workflow tutorial" sounds capability-driven. None of these capture what the work actually is: empirical investigation into AI failure modes through iterative deployment cycles with structured verification, generating both operational artifacts and methodological theory.

A stronger framing is available. The work qualifies as design-based research on AI-assisted personal practice: solo practitioner-research in the Brown / Cobb et al. / Cooper et al. tradition, supplemented by Howard Becker's tricks-of-the-trade discipline and Erving Goffman's transcontextual method. The framework maps to DBR requirements with substantive depth in four of nine core requirements, loose mapping in four others, and honest gaps in two. The qualifying claim is not "this is canonical DBR" but "this is design-research-adjacent solo practitioner-research with empirical record substantive enough to support methodological theory generation."

This post covers why design-based research matters here, how the framework maps to DBR requirements, the Becker-Goffman methodological inheritance, cross-field patterns supporting the positioning, and honest hedges about what the framework isn't. The empirical claims rest on two formally validated work classes plus informal accumulation beyond them.

## Why design-based research matters here

Design-based research has a specific provenance worth being precise about. Brown 1992 introduced "design experiments" as methodology for educational research aimed at producing both practical interventions and theoretical understanding. Cobb et al. 2003 articulated five features that distinguish DBR: developing theories of learning, interventionist deployment as test-beds for educational innovation, theory-testing during which new theories form, iterative cycles of invention and revision, and pragmatic accountability where theories must do real work.

The pragmatic-theoretical dual orientation is what makes DBR specifically appropriate for AI-assisted personal practice work. Cobb et al. articulated the calibration as "humble theory must do real work": theoretical claims earn their status through operational consequences, not abstract elegance. Methodology research of this kind isn't separate from operational practice; it emerges through the practice and gets validated by it.

Cooper et al. 2021 normalized DBR's applicability to solo-practitioner research contexts, articulating the researcher-as-instructor case where a single individual occupies both designer and investigator roles. The framework's operator-as-architect-and-practitioner structure maps directly to this configuration. Solo-mode DBR is recognized as legitimate methodological territory rather than a degenerate case of canonical multi-stakeholder DBR.

Wang & Hannafin 2005 defined DBR as "a systematic but flexible methodology aimed to improve educational practices through iterative analysis, design, development, and implementation, based on collaboration among researchers and practitioners in real-world settings." The framework fits the systematic-but-flexible criterion and the iterative analysis-design-development-implementation cycle. The collaboration-among-researchers-and-practitioners requirement is where Cooper et al.'s solo-practitioner accommodation matters: the framework operates without that collaboration but has structural substitutes (cross-substrate verification chain) for the verification function it normally provides.

## How the framework maps to DBR requirements

The framework's relationship to DBR's core requirements is best characterized empirically: substantive depth in four, loose mapping in four, honest gaps in two.

**Tight mappings.** Iterative cycles with revision map directly to Cycle 1 and Cycle 2 architecture validation cycles, where each cycle produces both architectural artifacts and theoretical claims tested against operational fires. Pragmatic accountability (Cobb et al.'s "humble theory must do real work") maps to the framework's canonical promotion gates, where claims earn canonical status only after a multi-fire empirical bar is met. Researcher-as-designer-and-investigator (the Cooper et al. 2021 case) maps to operator-as-architect-and-practitioner: the same individual designs the framework, deploys it, and investigates its empirical record. Prospective/reflective dual orientation maps to Phase 2 Lucas premortem (prospective failure-anticipation) plus Phase 4 falsification criteria (reflective claim-testing).

**Loose mappings.** Real-world contextual deployment is canonical DBR territory in classrooms; the framework operates in solo-operator contexts that are real-world but narrower than DBR's typical scope. Theory generation in DBR canonically produces learning theory; the framework generates AI failure-mode theory, cognate but not identical. Multiple data streams are present in the framework but transparency is one-sided (operator-attested) rather than two-sided peer engagement that canonical DBR depends on. Predictive specificity is supported by operator-recall and session artifacts rather than the formal experimental controls that protect against Hawthorne effects in canonical DBR contexts.

**Gaps.** Practitioner-researcher collaboration is the structural gap canonical DBR builds around; the framework is solo-mode, with cross-substrate verification substituting for the verification function collaboration normally provides. External validity and generalizability rest on n=1 operator without second-operator deployment to date. The transmission test that would establish generalizability hasn't been run.

## The Becker-Goffman methodological inheritance

The DBR framing covers the iterative-empirical structure of the work. It doesn't fully cover the methodological discipline: the operational practices that determine whether the empirical record gets at substantive findings or just produces noise. That discipline traces to two sociological-research traditions: Howard Becker's tricks-of-the-trade and Erving Goffman's transcontextual method.

Becker 1998 articulated the trick concept directly: "A trick is a specific operation that shows a way around some common difficulty," naming and describing operational moves that emerge from concrete research practice rather than abstract methodological theory. The framework's anti-pattern catalog inherits this structure: each anti-pattern names a specific failure mode encountered during substantive AI-assisted work, codifies countermeasures empirically derived from observed fires, and earns canonical status through repeated occurrence rather than theoretical elegance. Concept arises from data; named patterns beat formal procedures.

Goffman 1974 articulated his methodological move at the start of Frame Analysis: "I take a large number of illustrations, variously obtained, and try to get a formulation that is compatible with all of them." Goffman's transcontextual method legitimates accumulating empirical evidence across diverse contexts (different settings, different actors, different behaviors) to establish a single substantive claim that all the illustrations support. The framework's cross-substrate empirical accumulation inherits this structure: anti-pattern fires across multiple AI substrates, multiple work-event types, multiple session windows are treated as equivalent evidence for substrate-class behavior claims. The illustrations come from concrete operational practice rather than constructed cases.

Why Becker and Goffman matter here: methodological inheritance from sociological-research tradition rather than just management consulting or productivity-blog territory.

## Cross-field patterns supporting the positioning

The methodology research positioning gains additional support from cross-field patterns where the framework's structure echoes well-established findings across multiple research traditions.

Independence as the reliability mechanism. The framework's cross-substrate verification chain (work produced on one substrate gets verified on another) is structurally analogous to peer review in DBR contexts and to dialectical inquiry in management research (Schweiger et al. 1986; Schwenk 1990's meta-analysis on devil's advocacy and dialectical inquiry). The pattern across these domains is that independence between work-production and work-verification is the structural source of error-catching reliability, not capability of any single reviewer.

Adversarial structure outperforms consensus structure. Schwenk's meta-analysis demonstrated that dialectical-inquiry decision groups outperformed consensus-seeking groups on decision quality. The framework's verification chain inherits this structural insight: the synthesis substrate produces work; the triangulation substrate looks for what the synthesis substrate missed; consensus-seeking would weaken the catching mechanism. Adversarial structure isn't conflict for its own sake; it's the structural condition under which independent reviewers actually catch what they would otherwise rationalize away.

Pre-mortem discipline. The framework's Phase 2 Lucas premortem stage (anticipating failure modes before drafting begins) maps to Klein 2007's pre-mortem method, a 5-step procedure for systematic failure-anticipation. Klein cited Mitchell, Russo, and Pennington 1989 as the empirical foundation. The actual Mitchell et al. measurement is worth quoting precisely: sure-outcome reasoning produced more reasons identified and a higher proportion of episodic reasons than uncertain-outcome reasoning. The mechanism isn't "30% improvement in identifying causes" (a later reframing); it's that prospective failure-anticipation generates more empirically-specific reasons than reactive analysis.

## What I'm not claiming

I'm not claiming the framework qualifies as canonical DBR. The two structural gaps (practitioner-researcher collaboration and external validity through second-operator deployment) matter; this is solo-operator design-research-adjacent practice rather than canonical multi-stakeholder DBR.

I'm not claiming methodological novelty. The methods being applied are well-established: design-based research (Brown, Cobb et al., Cooper et al.); Becker's tricks-of-the-trade discipline; Goffman's transcontextual method; pre-mortem reasoning (Klein, building on Mitchell et al.); dialectical inquiry (Schweiger et al., Schwenk). What's available here is the specific application to AI-assisted personal practice work, not the methods themselves.

I'm not claiming generalizability beyond personal AI infrastructure work. The transmission gap (no second operator deployed) leaves generalizability untested. The framework's structural argument suggests transferability; the empirical record doesn't yet establish it.

I'm not claiming the empirical theory generated here is on equal footing with the methodological theory. Methodological claims (about discipline structures that catch failure modes) are more defensible than substrate-empirical claims (about specific AI vendors' behaviors at specific points in time). The latter is more contingent on AI ecosystem state than the former.

## What I am claiming

I'm claiming solo AI-assisted personal practice can be productively positioned as design-research-adjacent solo practitioner-research. The Brown / Cobb et al. / Cooper et al. tradition (supplemented by Becker's tricks-of-the-trade and Goffman's transcontextual method) provides methodological grounding more rigorous than "personal methodology" framings without overclaiming canonical-DBR status.

I'm claiming the framework's empirical record is substantive enough to support methodological theory generation. Two formally validated work classes (23-of-23 and 32-of-32 verification records), informal accumulation beyond, and substrate-class behaviors documented across three concurrently-running AI substrates: this is empirical foundation for claims about AI failure modes and discipline structures, not just personal-practice anecdote.

I'm claiming the practical implication for personal AI infrastructure work: the methodological discipline transfers to other operators interested in similarly structured work. The transmission test hasn't been run; the structural argument is that it should run successfully. Becker's tricks, Goffman's transcontextual method, and DBR's iterative-cycle structure transferred across research traditions; nothing about AI-assisted work specifically blocks the same transfer.

That's the post.
