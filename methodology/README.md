# Methodology

**Purpose:** Framework documentation and operational disclosure for The Street Code's AI-discipline methodology.

This folder holds the artifacts that govern how posts get written, audited, and shipped. The framework itself (the canonical rules, anti-patterns, multi-substrate audit chains, retraction discipline) is documented across the corpus in `posts/` and in operator-side canonical files outside this repo (see `~/.claude/cc_nav_payload.md` for the spatial topology). This folder is the publication-side discipline layer that operates over the corpus.

---

## Contents

### `post_audit_checklist.md`

The six-item pre-publication audit discipline applied to every post or batch of posts before commit + push. Established 2026-06-10 post-Posts-91-98 session; captures failure modes caught across the Posts 81-90 and Posts 91-98 publication arcs (cross-reference cascade errors; disclosure leaks; Federalist misattribution; F-18 framing drift; orphan empty headers) and the Posts 110-128 arc (cross-content duplicate-publication caught + 0107-0109 retraction).

Codified checks:

1. **Em-dash discipline** (applies post 0036 onward per 2026-06-30 scope amendment; posts 0001-0035 carry 118 legacy em-dashes preserved per immutability convention)
2. **Cross-reference accuracy** (every "Post NN" reference must resolve)
3. **Disclosure compliance per Approach 2 soft-disclosure rule** (abstract DOM/WebGL boundaries; Memory Lanes specifics; specific schema symbols)
4. **Madisonian Gate attribution** (Federalist 51 with self-acknowledged loose-citation hedge; not Federalist 10)
5. **Modification 6 boundary discriminator framing** (state-space content; not present-state-anchored vs temporally-extended per F-18 retraction)
6. **Section structure + empty headers**

Plus the operational "How to apply" workflow (steps 0-10) covering cross-content equivalence checks, em-dash grep, cross-reference grep, disclosure-compliance pass, citation-framing pass, empty-header scan, SUMMARY.md update, post-ideas.md update, single commit + push, and Treasure Map regen.

### `audit-baseline-2026-06-30.md` (when present)

Recorded clean baselines from full-corpus audit runs. Tracks the state at which the corpus was verified to satisfy the audit checklist's deterministic checks. Used as the reference point for any subsequent regression investigations.

---

## Related

- `../research/citations/modified-c-bis-canonical-citations.md` — Master citation file for the philosophical-content arc (Posts 0110-0128); enforces "primary text > review paper > secondary interpretation" and tracks flag retractions (F-8 through F-18) with direct quotes and page numbers
- `../drafts/INDEX.md` — Current drafts pipeline state + the 2-digit drafts/ vs 4-digit posts/ numbering-system disambiguation
- `../drafts/CANON.md` — Canon-vs-post boundary recommendation (Open Alley architecture/ as canonical home short-term; Room To Life migration post-V1)
- `../SUMMARY.md` — Per-post plain-language index covering all 125 published posts plus the 107-109 retraction entry

---

## Maintenance

When a new failure mode surfaces in an audit that isn't already caught by the checklist, add an entry to `post_audit_checklist.md`'s "Failure modes caught in past audits" section per the established arc-grouping convention (e.g., the "Posts 110-128 arc" entry that documents the cross-content duplicate-publication failure mode).

When the operator's canonical-record facts update (new canonical citations; new rules canonized; new IP-protected scope items), update the "Operator-canonical-record facts that recur" section.

When the disclosure rule changes per its 2026-11-04 revisit (per `~/Projects/substack/disclosure_rule.md`), update step 3 of the audit checklist.

When the voice spec evolves, update the relevant step + add a scope amendment if the evolution is partway-through-corpus (parallel to the 2026-06-30 em-dash scope amendment which preserves the legacy gap per immutability rather than back-applying).
