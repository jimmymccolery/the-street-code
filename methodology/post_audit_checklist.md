# Post Audit Checklist

**Established:** 2026-06-10 (post-Posts-91-98 session)
**Maintained by:** operator
**Purpose:** systematic pre-publication audit discipline for the-street-code posts; captures failure modes caught across the Posts 81-90 and Posts 91-98 publication arcs so future posts ship without repeating them.

## When to run this audit

Run before commit + push of any post or batch of posts. Each audit takes 5-15 minutes per post depending on density. The audit is a CC-runnable discipline; the operator can also run it manually. The audit is NOT a substitute for the operator's final read with fresh-Substack-reader lens; the audit catches CC-side failure modes that the operator-side read may not surface, and the operator-side read catches reader-experience issues that the audit does not surface. Both are load-bearing.

## The six-item checklist

### 1. Em-dash discipline (applies post 0036 onward)

Voice spec is zero em-dashes (— character, Unicode U+2014). Verify per post:

```bash
grep -c '—' posts/NNNN-*.md
```

Should return `0` for every post drafted from post 0036 onward. Any nonzero result on a post 0036+ is a fix-before-commit.

**Scope amendment (added 2026-06-30):** The em-dash rule was adopted partway through the corpus; posts 0001-0035 predate the rule and carry 118 cumulative em-dashes across 12 files (concentrated in cluster 0025-0035 plus 0005 + 0006). These legacy em-dashes are NOT retroactively fixed per the framework's immutability convention (posts are immutable once committed; corrections arrive as dated update-notes, not silent edits). The scope-amendment makes the spec-vs-corpus gap explicit rather than treating the 118 legacy em-dashes as ongoing violations. Future maintenance: posts 0036+ remain zero-em-dash; the legacy gap stays as visible record of when the rule was adopted (parallel discipline to the 0107-0109 retracted-slot gap which preserves audit-record visibility rather than back-applying corrections).

The Posts 110-128 arc's clean em-dash audit verdict (the maintenance pass that surfaced the scope question in the first place) confirmed the rule's enforcement is reliable when applied at drafting time; the legacy gap is an artifact of rule-adoption timing, not of current discipline.

### 2. Cross-reference accuracy

Every reference to "Post NN" or "Posts NN through MM" in the body or status field must point to an actual published post with content matching the description. The Posts 81-90 batch had 10+ wrong cross-references because draft renumbering from brief-slot to impact-priority ordering did not propagate to internal cross-refs (see `feedback_brief_slot_vs_publication_numbering_mismatch.md` for the canonization of the lesson).

Verification pattern:

```bash
grep -nE "Post [0-9]+|Posts [0-9]+ through [0-9]+|Posts [0-9]+-[0-9]+" posts/NN-*.md
```

For each match, verify the referenced post exists (`ls posts/REF-*.md`) and the description matches the actual post's content.

**Common cross-reference targets that recur:**
- **Post 06** = "What Auditing the Audit Taught Me About Substrate Routing"
- **Post 11** = "What Cross-Substrate Audit Surfaced That Same-Substrate Verification Missed"
- **Post 50** = canonical-content reproduction; substrate self-attestation unenforceable
- **Post 60** = recursive 4-layer catch cascade orchestrator-class
- **Post 70** = Marcus Reed Protocol named-guardrail honored and fabricated
- **Post 77** = substrate-validation-theater under artifact-audit framing
- **Post 82** = two-axis substrate-style preservation model
- **Post 110** = retraction-table lead for Modified-C-bis philosophical-content arc; sixteen-row catalog of empirical corrections across eight rounds
- **Post 112** = Personhood-as-Achievement (Wiredu structural-borrowing engagement; highest cross-cultural exposure post; full 5-element discipline applied)
- **Post 117** = Wiredu mapping does not survive implementation (Option (c) drop; F-17 universalist reversal; F-14 Friston Appendix F parallel retraction)
- **Post 120** = V1 NPC memory spec META-level closer (nine locked V1 elements; Phase-8.x banked scope; Steam V1.0 candidate scope; three retraction-condition triggers)
- **Post 124** = canonical statement of the five-element cross-cultural disclosure discipline
- **Post 128** = WEIRD-defaults-in-the-accumulator closer; Henrich + Crenshaw + Cross schema-placeholder discipline

### 3. Disclosure compliance per Approach 2 soft-disclosure rule

The disclosure rule (`~/Projects/substack/disclosure_rule.md` Approach 2; revisit date 2026-11-04) soft-discloses operator-specific implementation. Specific things to abstract:

**Always abstract these in posts:**
- **DOM/WebGL boundaries** → "two computational layers with different roles" or "two distinct computational layers with different execution semantics"
- **Multi-purpose tray V1 architecture specifics** → "a specific component class" / "a specific architectural surface" (NO Item #98; NO Equipment Alerts; NO Zone 33 mechanic shop; NO specific failure-mode numbers FM2/FM10/FM11/FM14/FM20/FM25)
- **Pin Paradise / Memory Lanes product names** → "a multi-decade bowling-tycoon simulation" or similar directional framing
- **NPC names, roster details, demographic-specific examples** → directional descriptions only
- **Specific schema symbols** (`current_tick`, `tycoon_tick_count`, `schema_version`, `OilerMachineCatalog`, etc.) → generic placeholders
- **Specific quantitative anchors from operator's research arcs** → directional ("specific 1958 industry-survey citation; multiple quantitative anchors at league count, growth rate, and center count") rather than exact (1958 PAS Report 110 BPAA + 54,318 league count + ABC growth 3.3× + 6,600→11,000 center count)

**Always safe to publish in full detail:**
- Methodology research, empirical findings, citation-supported claims, reasoning
- Bowling-industry historical research (public-domain facts; Pinsetter wars 1951-1956; Brunswick B90 1962; AMF 82-70 1963; Volcker shock 1981; Don Carter 1964 Ebonite endorsement; X-Calibur 1991; Kegel Sanction Machine 1988; etc.)
- Generic software architecture patterns (composition-over-modification; atomic state machines; statistical-vs-physics resolution)
- AI discipline framework methodology (anti-pattern enforcement; Madisonian Gate; verify-against-canonical-files; etc.)

**Always defer to operator decision:**
- Anything in the Pin Paradise IP-protected scope per `post-ideas.md` header

### 4. Madisonian Gate attribution

Verify the framing in any post that references the Madisonian Gate:

**Correct framing:**
- "separation-of-powers analog applied to substrate workflows" (matches operator's Posts 15 + 41)
- "Rule 14 in the framework's enumeration" (canonical reference)
- "The Madison attribution is loose; the operational discipline is the load-bearing claim, not the citation"

**Wrong framing (caught in Posts 81-90 audit):**
- "Federalist 10 framing of competing factions producing aggregate stability" — operator's Post 05 cites Federalist 51 (with self-acknowledged hedge), not Federalist 10
- Unhedged Federalist N citation — operator hedged the citation as "Strong overstatement of the citation, but it sticks in memory" in Post 05; CC should match the hedge level

If you absolutely must cite a Federalist number, use Federalist 51 with the same self-acknowledged loose-citation hedge.

### 5. Modification 6 boundary discriminator framing

The framework's Modification 6 boundary discriminator went through correction at Round 8 (F-18 catch). Verify the current correct framing:

**Correct (per Round 8 F-18):**
- "state-space content (no cross-era self-identity variable vs state space that DOES contain one)"
- "behavior whose state-space content excludes cross-era self-identity variables"

**Wrong (retracted per F-18; caught in Posts 81-90 audit):**
- "present-state-anchored behavior" as the Modification 6 boundary discriminator
- "present-state-anchored vs temporally-extended" as the boundary discriminator framing

The terminology "present-state-anchored active inference" remains canonical from Round 6 for the V1 mechanism description; what F-18 retracted was using "present-state-anchored vs temporally-extended" as the boundary discriminator name. The boundary discriminator is state-space content.

### 6. Section structure + empty headers

Check for orphaned empty section headers (an H2 immediately followed by another H2 with no content paragraph between):

```bash
grep -n "^## " posts/NN-*.md
```

Manually verify each H2 has content paragraphs before the next H2. The Posts 81-90 audit caught Post 84 having a duplicate empty `## What this costs the framework` header left over from a comprehensive expansion pass that prepended new content without preserving the section structure.

**Standard closing structure** (per voice spec + recent published convention):
- `## What I am not claiming` — 3-5 paragraphs; each paragraph leads with "I am not claiming X..."; bounds the post's scope explicitly
- `## What I am claiming` — 3-5 paragraphs; first paragraph leads with the central claim directly (no "I am claiming that..." hedge); subsequent paragraphs expand with substantive content (not recap); include "if you are doing X" reader address; "doing more work than I expected" framing in recent posts 70/75/77/80

## Operator-canonical-record facts that recur

These specific facts appear in multiple posts and should be verified against canonical record before drafting/editing:

**Citations:**
- **Friston 2017 Appendix F** = pages 42-43 (verified Round 8 R2 + R4 primary-text reads; F-8 RESOLVED)
- **Friston 2017 §4.4** = Summary, around page 34
- **Friston 2017 §5** = Conclusion, pages 36-37
- **Friston 2017** = *Neural Computation* 29(1):1-49
- **Friston et al. 2021 "Sophisticated Inference"** = *Neural Computation* 33(3):713-763
- **AgentCrypt** = arXiv:2512.08104 (NOT arXiv:2605.03213 which is a different paper)
- **PersonaWeaver** = Qraitem, Saenko, Plummer 2026, arXiv:2601.03396
- **Gray, Gray, Wegner 2007** = "Dimensions of mind perception" *Science* 315(5812):619
- **Colombo and Wright 2021** = *Synthese* 198 Suppl 14:3463-3488

**Cross-cultural / philosophy:**
- **Wiredu Ch.9 pp.193 + 199** = universalist finding CORROBORATED per Round 8 F-17 (UNRETRACTED F-13)

**Framework rules:**
- **Rule 11** = multi-substrate research workflow methodology; canonized 2026-05-26 AR-3.1 Decision 3C
- **Rule 14** = Madisonian Gate Verdict Classification Discipline
- **Rule 17** = CW Project Knowledge Refresh Discipline; canonized 2026-05-31 AR-3.3 Decision 3-3-B
- **Rule 19** = substrate self-attestation unenforceable; n=5+ cumulative across philosophical research arc Rounds 7 and 8

## Failure modes caught in past audits

**Posts 81-90 arc (5 findings, all caught + fixed):**
1. **Cross-reference cascade error.** 10+ wrong cross-references in Posts 81 + 87 from brief-slot vs impact-priority numbering mismatch. Fixed by reframing to "the deeper post is in draft form" + explicit Post 84 references where applicable. Canonized as `feedback_brief_slot_vs_publication_numbering_mismatch.md`.
2. **DOM/WebGL disclosure leak.** Posts 85 + 88 named "Document Object Model layer and a WebGL rendering layer" as specific architectural seam. Fixed by abstracting to "two computational layers with different execution semantics."
3. **Federalist 10 misattribution.** Comprehensive expansion pass added Madison's Federalist 10 attribution; operator's Post 05 cites Federalist 51 with self-acknowledged loose-citation hedge. Fixed by replacing with separation-of-powers framing + explicit "Madison attribution is loose" hedge.
4. **F-18 framing.** Expansion identified "present-state-anchored behavior" as Modification 6 boundary discriminator; F-18 explicitly RETRACTED this. Fixed by rephrasing to "state-space content excludes cross-era self-identity variables."
5. **Empty duplicate section header.** Comprehensive expansion pass left orphaned `## What this costs the framework` empty header in Post 84. Fixed by deleting the duplicate.

**Posts 91-98 arc (0 findings):**
The Posts 81-90 lessons were applied at drafting time rather than retroactively. The no-expansion-pass approach + deliberate abstraction at drafting + cross-ref discipline during renumbering prevented the failure modes from recurring. The clean audit verdict on Posts 91-98 is evidence the checklist's discipline-of-prevention works when applied at drafting time.

**Posts 110-128 arc (1 finding caught post-publication; 3 slots retracted):**
The 22-post shipping arc on 2026-06-29 (3 B2 ready-to-ship methodology drafts at 0107-0109 + 19 B1 philosophical-content briefs drafted into posts at 0110-0128) introduced a new failure mode: **cross-content duplicate-publication**. The 3 B2 drafts in `drafts/` (`draft_canonical-anchor-validation-arc_2026-06-10.md`, `draft_fix-cycle-surface-drift_2026-06-10.md`, `draft_within-decade-dual-deployment-validator_2026-06-10.md`) had ALREADY produced shipped posts 0091, 0092, 0093 on 2026-06-10 during the substrate-methodology arc; the drafts sat in `drafts/` for 19 days because the prior session did not delete them after publishing. When the 2026-06-29 promotion cycle ran, the topic-match audit at slug level missed the equivalence because the draft filenames used different slug conventions than the shipped post slugs. The duplicates shipped as 0107-0109 then were caught + retracted at 2026-06-30. **Mitigation added to step 1 of the How-to-apply checklist below: cross-content equivalence check before promotion.** The retraction is documented at SUMMARY.md entry 107-109 per the framework's transparent-self-correction discipline (parallel to the retraction tables in posts 0089 + 0110).

## How to apply

**For batch publications:**
0. **Cross-content equivalence check (new step per Posts 110-128 audit):** before promoting any draft from `drafts/` to `posts/`, run a `diff` of the draft body against all existing `posts/*.md` files (or grep the draft's opening thesis paragraph against `posts/` to surface any high-similarity matches). The check catches duplicate-publication failure mode where draft filenames may use different slugs than the shipped post slugs of the same content.
1. Draft posts and copy to `posts/` with NNNN-slug naming (four-digit zero-padded; the original "NN-slug naming" convention upgraded to 4-digit at post-0070 era)
2. Run em-dash grep across the batch
3. Run cross-reference grep across the batch and verify each
4. Disclosure-compliance pass: search for forbidden specifics; abstract any found
5. Madisonian Gate / F-18 / specific-citation pass: verify framing matches canonical record
6. Empty-header check: visual scan of H2 sequence
7. Update SUMMARY.md with dense single-paragraph entries (including any retraction-aggregate entries if duplicates surfaced)
8. Update post-ideas.md status fields (skip if posts came from drafts/ briefs rather than idea-queue entries)
9. Single commit + push
10. **Treasure Map regen (new step per Posts 110-128 audit):** run `~/Projects/master-setup/regen_launcher_hashes.py` after publishing batches that meaningfully change `posts/` count or `SUMMARY.md` preamble, so `~/.claude/cc_nav_payload.md` reflects current state for future CC sessions

**For single-post publications:**
Same six steps but at single-post scope.

**For audit-only mode** (the operator runs CC against a published-but-unaudited post):
Run the six checks; report findings categorized by severity; recommend fixes; operator decides on application.

## Cross-references

- `~/Projects/substack/post_template.md` — voice spec + structure variations + pre-publication checklist
- `~/Projects/substack/disclosure_rule.md` — Approach 2 soft-disclosure rule v1.0
- `~/Projects/the-street-code/research/citations/modified-c-bis-canonical-citations.md` — canonical citations for philosophical-sequence posts
- Memory: `feedback_brief_slot_vs_publication_numbering_mismatch.md` — canonized lesson on cross-ref cascade failure mode
- Memory: `project_posts_81_90_publication_arc_2026-06-10.md` — full session arc with the 5 findings detailed
- Memory: `project_posts_91_98_publication_arc_2026-06-10.md` — full session arc demonstrating clean audit when checklist applied at drafting time
- SUMMARY.md entry 107-109 — canonical record of the Posts 110-128 arc's cross-content duplicate-retraction event (3 slots retracted 2026-06-30; preserves the audit-record gap)

## Notes for revision

Update this checklist when:
- A new failure mode surfaces in an audit that isn't already caught by the checklist
- The operator's canonical-record facts update (new canonical citations; new rules canonized; new IP-protected scope items)
- The disclosure rule changes per its 2026-11-04 revisit
- The voice spec evolves
