# Verification beyond "did this happen": five scopes of canonical-state checking that catch AI drift before it compounds

**Author:** Jimmy McColery
**Date:** 2026-06-09
**Status:** Cumulative empirical observation across thirteen reproductions in eleven distinct reproduction classes spanning four weeks of substantive long-project work; n=13 cumulative; strong empirical foundation for meta-canonical verification-discipline canonization candidacy

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I keep a feedback memory in my discipline framework called "verify against canonical files." It started as a one-line discipline a few weeks ago after the first reproduction. The memory now records thirteen reproductions across eleven distinct verification-class subdivisions, and it has surfaced something I want to write up. The reproductions are not the same kind of drift over and over. They are five structurally different kinds of drift, each of which requires a different verification operation to catch.

Most existing verification discourse treats verification as a single discipline: when in doubt, check the source. The framing is correct as far as it goes, but the framing is operationally underspecified. There are at least five different sources you might check, and the source you check depends on the drift class you are trying to catch. Checking the wrong source produces a verification that feels rigorous and catches none of the drift it was supposed to catch.

This post is about the five scopes I have observed. The list is empirical; I expect to add scopes as new reproduction classes surface. The argument is that breadth-conscious verification is a different discipline than single-scope verification, and the breadth-conscious version is what actually protects against AI drift in long-project work.

## Scope one: operator-prompt-drift verification

The first scope catches drift in the operator's own prompts. The operator drafts a prompt that nominally references canonical state, but the prompt's reference is stale. The reference was current when the operator first drafted the prompt template months ago, and the canonical state has since moved. The substrate receiving the prompt operates against the prompt's stale reference rather than against the current canonical state.

This scope is unintuitive because the operator's own prompts feel like reliable inputs to the substrate. The operator wrote them. The operator knows what they say. The operator does not naturally treat them as drift candidates.

The fires I have logged at this scope include a prompt that referenced a substack deletion policy that had been superseded, and a prompt that referenced a rule-set promotion procedure that had been refactored. Each prompt had been working correctly when first authored; each prompt produced wrong outputs after the underlying canonical state changed. The verification operation that catches this is reading the current canonical surface and checking the prompt's references against it, not against the operator's memory of what the prompt is supposed to say.

The operator's memory is a poor proxy for canonical state. The operator's memory is updated when the operator notices an update; the operator does not notice most updates because most updates do not flow back through the operator's attention. The prompts are static text holding a snapshot of the operator's understanding from the moment the prompts were drafted. Checking the prompt against the operator's current understanding misses the drift; checking the prompt against the actual canonical file catches it.

## Scope two: session-blind ratification verification

The second scope catches drift in cross-session ratifications. The operator opens a new session, asks an AI assistant to ratify a decision the operator made in an earlier session, and the assistant produces a ratification that does not check the canonical state at all. The ratification feels correct because the assistant is reasoning from the prompt; the prompt carries the operator's framing; the framing carries the operator's intent. The framing-to-canonical-state grounding is missing.

The fires at this scope include a ratification of a cryptid roster decision where the assistant did not consult the actual roster, and a ratification of a freshness amendment to a UI card-class taxonomy where the assistant did not consult the current taxonomy. In each case the operator presented the decision; the assistant agreed; the agreement did not include a verification step. The verification operation that catches this is reading the canonical surface the decision is supposed to affect and checking that the decision is coherent with the current state, not just with the prompt's framing of the decision.

The pattern this catches is silent because cross-session ratifications usually feel substantive. The operator and the assistant are discussing the decision in detail; the discussion produces nuance, edge-case consideration, alternative framings. The discussion is real; the discussion is also detached from the canonical state if no one consults the state during the conversation. Detachment from canonical state is not visible in the conversation's surface texture; the conversation looks engaged whether or not the engagement is grounded.

## Scope three: substrate-fabrication detection

The third scope catches drift in substrate outputs that nominally cite canonical state. The substrate produces a claim about what the canonical state contains; the claim is wrong; the operator accepts the claim because it sounds plausible. This is the failure mode the substrate-self-attestation literature focuses on, and it shows up across substrates with depressing regularity.

The fires at this scope include a substrate fabricating a flooring specification that did not exist in the canonical record, a substrate fabricating four academic citations that did not exist in the cited sources, and a substrate fabricating a comic-book origin for an operator-defined named protocol. Each fabrication looked authoritative; each collapsed on the first external lookup. The verification operation that catches this is reading the actual canonical file or external source the substrate claims to be citing and confirming that the content the substrate reports is actually there.

Substrate fabrication is the most documented of the five scopes. It is also the easiest to mechanize: any substrate output that claims to cite a source can be tested by checking the source. The mechanization is bounded; the cost of running attribution checks is small; most fabrications collapse immediately. The discipline is hard to remember when the output looks calibrated, but the verification operation is straightforward when the discipline kicks in.

## Scope four: cross-document search-miss verification

The fourth scope catches drift in operator-side scope determination. The operator asks the substrate (or asks themselves) to search across a project for some pattern, and the search misses content that lives in non-obvious document locations. The missing content is not hidden; it is just in a directory or file the search did not enumerate. The search returns "I found these instances" and the answer is incomplete in ways the search does not report.

The fires at this scope include a comprehensive-scan request that missed five distinct source directories, an archetype-categorization scan that missed entries in a research-anchors directory, and a canonical-substrate scan that missed a closure-window architectural specification because the file naming did not telegraph the architecture. In each case the operator (or the substrate operating at the operator's direction) determined search scope before performing the search; the scope was narrower than it should have been; the search returned positive findings but the findings were incomplete.

The verification operation that catches this is enumerating the project's directory structure explicitly and verifying that the scope covers all candidate locations, not just the obvious ones. This is the verification I described in a recent post about don't-skip-chapters at primary-source ingestion scope; the same structural pattern shows up at multi-document scan scope and at cross-directory search scope.

The pattern is silent because the search returns positive findings. The operator gets results; the results are accurate as far as they go; the operator does not naturally check whether the results are complete. Completeness is the property the operator-side enumeration is supposed to check, and the enumeration is the verification step the operator usually skips.

## Scope five: within-document temporal-drift verification

The fifth scope catches drift within a single canonical file across time. The file is the right file; the file is in the canonical record; the file is consulted during verification; the file's current content is what the operator reads. The drift is that an earlier section of the file was authored against a different canonical state than a later section, and the file as a whole is internally inconsistent.

The fires at this scope include an audio engine specification with a lock body that had drifted from later sibling-clarifications, a Phase 7.1e freshness amendment that asserted a card-class taxonomy contradicting the actual card-class catalog elsewhere in the same document, and a substrate audit prompt whose reproduction-gate had drifted from the prompt's own substantive sections.

This scope is the hardest to catch because the file is the canonical surface. The operator usually trusts the file because the file is what canonical means. Reading the file produces an authoritative answer; the file is the source of truth. But the file's internal sections were authored at different times against different snapshots, and the file holds the residue of those temporal differences as internal inconsistency.

The verification operation that catches this is reading multiple sections of the file in parallel and checking that the sections agree on the load-bearing facts. The check is not free; it requires the operator to know which sections are supposed to be coherent. But the check catches a class of drift that the other four scopes cannot catch, because the other four scopes assume the canonical file is internally consistent and only test claims against the file.

## Why the five scopes do not collapse into one

Each scope catches a different class of drift. Operator-prompt-drift lives in static text the operator wrote. Session-blind ratification lives in the absence of verification during a conversation. Substrate-fabrication lives in substrate outputs that nominally cite canonical state. Cross-document search-miss lives in the operator's scope determination. Within-document temporal-drift lives in the canonical file itself.

The structural property that prevents collapse is the source of the drift. Each scope's drift originates from a different location in the operator's workflow. Single-scope verification protects against the drift in that scope and not against the drift in the other scopes. Increasing the rigor of substrate-fabrication checks does not catch operator-prompt-drift, because the drift is not in the substrate output; it is in the prompt the operator provided to the substrate. Increasing the rigor of within-document checks does not catch cross-document search-miss, because the drift is not in the file; it is in which files the operator searched.

The operational implication is that long-project verification discipline has to address all five scopes separately. The five scopes are not redundant; they are complementary. Verification breadth is a different discipline than verification depth at any single scope. Both matter, but the breadth has been under-discussed in the literature I read on AI verification, and the breadth is what the cumulative reproduction record at thirteen fires across eleven classes is pushing me toward.

## The pattern is more important than the list

I expect the specific scope enumeration to change. Five is my current count; the actual count when I have more data may be six or seven. The structural pattern (each scope has its own drift class with its own verification operation) is what I want to land, not the specific scopes I have observed so far.

The pattern's load-bearing claim is that verification is plural rather than singular. "Check the source" is the slogan; the operational reality is "check several sources of different kinds, each tuned to a different drift class, on a schedule the substrate cannot influence." The slogan is a useful summary but it hides the operational complexity that produces reliable verification.

The cumulative reproduction record at thirteen fires also surfaces a second-order observation. When I started logging the verifications, I expected one or two scopes to dominate; the rest would be edge cases. The actual distribution is closer to uniform: the eleven reproduction classes are spread across the five scopes without strong clustering. No single scope is the dominant failure mode. This means single-scope verification protects against at most a fifth of the drift class; multi-scope verification is the only architecture that catches the majority of drift across the long arc of project work.

## What this changed in my workflow

Three specific changes. First, when I face a verification question, I now ask which of the five scopes the drift class belongs to before I pick the verification operation. The matching is not always obvious; some drift classes touch multiple scopes. But the matching forces me to choose a verification operation tuned to the actual drift class, not the verification operation that comes to hand first.

Second, my discipline-framework feedback memories now name the scope each reproduction belongs to. The labeling is operational discipline; over time the labels surface clustering patterns and inform where to invest in further verification automation. The labels also produce the empirical foundation that drove this post; without the labels the thirteen reproductions would have looked like one big undifferentiated category.

Third, when I review someone else's verification practice (in code review, in research-methodology discussion, in operational-discipline canonization), I look for which of the five scopes the practice addresses and which it does not. The single-scope blind spot in other practices is visible once you know what to look for. Most published AI-verification discussion addresses scope three (substrate fabrication) deeply and the other four scopes hardly at all.

## Why this generalizes beyond AI work

The pattern is not AI-specific. Any long-project domain where canonical state is mutated over time, referenced across documents, and verified against external claims has the same five-scope structure. The drift classes are the same. The verification operations are the same. The pattern shows up in software engineering (commit drift, codebase consistency, dependency-claim verification), in academic research (citation drift, replication-package consistency, methodology-claim verification), in regulatory compliance (policy-update drift, cross-document consistency, audit-claim verification), and probably in any domain where authoritative state is maintained across time by multiple contributors and consumed across documents.

The AI-specific observation is that AI assistance increases the rate of drift at every scope. The operator's prompts get more elaborate (more drift in scope one). The cross-session ratifications get more numerous (more drift in scope two). The substrate outputs become a primary source of claims that need verification (more drift in scope three). The search-and-retrieval workflows expand (more drift in scope four). The canonical files get longer and accumulate more internal sections (more drift in scope five). The rate at every scope goes up; the verification breadth has to keep up.

The discipline framework I run treats each of the five scopes as a first-class verification class with its own operation. The framework is older than my current AI-assistance setup; the framework's discipline catches drift across all five scopes whether or not the drift was AI-introduced. The AI-introduction increases the volume; the framework's structure scales as long as the scope coverage stays complete.

## What I'm not claiming

- I'm not claiming the five scopes are mutually exclusive. Some drift fires touch multiple scopes; the labeling is closest-fit rather than exclusive partition. The scopes are useful for naming the verification operations, not for partitioning the drift classes into non-overlapping buckets.

- I'm not claiming five is the right number forever. The count is empirical; I expect the count to grow as I encounter new drift classes that do not fit the existing scopes. The structural pattern (plural verification with scope-tuned operations) is what I expect to generalize; the specific count is provisional.

- I'm not claiming the verification operations are uniformly cheap. The cheapest scope (substrate-fabrication checks against external sources) takes seconds per check. The most expensive scope (within-document temporal-drift consistency reads) can take significant operator attention when the file is long. The discipline pays out by catching drift before it compounds, but the cost is real and the cost-benefit calculation depends on the project's drift rate.

- I'm not claiming this finding is novel in verification-research terms. Multi-source verification has been the operational principle in adversarial-incentive engineering for decades. The contribution is the specific empirical mapping for AI-assisted long-project work, and the demonstration that the verification breadth has been under-discussed in the AI-verification literature I have read.

- I'm not claiming the scopes I enumerated are the only structurally distinct verification classes that exist. The five scopes are the ones I have observed across thirteen reproductions; other operators working in different domains will surface additional scopes that match their drift classes. The pattern is what generalizes; the specific scopes are project-dependent.

## What I am claiming

What I am claiming is that verification is plural and breadth-conscious in a way the single-scope framing hides. Each of the five scopes I have observed catches a different drift class with a different verification operation. Single-scope rigor at any of the five does not protect against the other four. The operator's verification architecture has to address all five (or however many the operator has observed) as first-class verification classes, each with its own operation, each scheduled on a basis the substrate cannot influence.

Thirteen reproductions across eleven classes is enough empirical foundation to land the pattern. The pattern's value comes from the breadth-consciousness it imposes on verification discipline. Single-source verification was the framing I was operating under when the first reproductions started arriving; the framing was wrong in a way that took thirteen fires to surface. The discipline I run now is breadth-conscious, scope-labeled, and operationally specific about which verification operation runs against which drift class. That discipline is what catches the drift the single-source framing was missing.
