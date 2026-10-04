# Rule 29 K=2 Target-Verification Canonization Candidacy
## Council #11 Item 211 (BANK-PENDING-SECOND-FIRE)

**Filed:** 2026-07-12
**Status:** BANK-PENDING (n=1 fire below Rule 27 n=4 canonization threshold; above Rule 28 n=1 canonization precedent — substrate quorum decision)
**Session:** c70eb795-58d8-4708-933f-acae498a56ce

---

## §1 Proposed Rule 29 Text

> **Rule 29 — K=2 Target-Verification for Agent-Issued Corrections**
>
> When any substrate (K=1 solo, K=2 parallel-agent pair, or K=3 parallel quorum) issues a "correction" claim against a named target document (roadmap, canonical file, spec, prior candidacy, methodology artifact), the correction MUST be grep-verified against the actual target document's byte contents BEFORE Council-scope filing.
>
> Agent claims about what a document contains are inference-under-citation-pressure until grep-verified; presenting them as Council-scope correction filings without target-verification is a Rule 29 fire.
>
> **Enforcement:** Retract fabricated corrections at Council filing time; log to retraction registry; issuing substrate carries no ratification credit for retracted claim.

## §2 Empirical Foundation

### Fire evidence (n=1)

**M2 K=2 anchor research pair (2026-07-12):**
- Both Agent A and Agent B independently filed:
  - **N-69:** "Silvia 2001 registered replication attenuation" — CLAIMED to exist in Phase 2 roadmap draft
  - **N-70:** "Vansteenkiste 2020 BPNSFS attribution as Higgins-attenuation" — CLAIMED to exist in Phase 2 roadmap draft
- Grep audit confirmed:
  - Roadmap correctly cites Tangney 1998 as primary Higgins attenuation at line 102
  - Roadmap correctly tags Vansteenkiste 2020 as CONTESTED-MEASUREMENT per Heissel 2024 at line 59 (Heissel 2024 subsequently corrected to Murphy 2022 per N-79)
  - Neither Silvia 2001 phrasing nor Vansteenkiste-as-Higgins-attribution present in roadmap
- Both agents produced **FALSE convergent claims** — K=2 convergence produced FALSE consensus
- Retracted at M3 candidacy amendment

### Counterfactual evidence (n=3 correct corrections that DID target-verify)

- **M5 pair (N-79):** correctly identified Heissel 2024 → Murphy 2022 PMID 36442044; grep-verified against roadmap line 59
- **M6 pair (N-84):** correctly identified Waters-Beauchaine 2003 → Waters et al. 2000 Child Development 71(3):684-689; grep-verified against agent prompt (not roadmap; substrate docs)
- **M7 pair (N-85/N-86/N-87/N-88):** correctly identified citation hygiene items; grep-verified against target docs

## §3 Precedent Alignment

- **Rule 27 (Non-Inertness Gate) precedent:** canonized at n=4 fires per Council #9 accelerated close
- **Rule 28 (defensive-reducer) precedent:** canonized at n=1 fire per Council #9 Item 154
- Rule 29 candidate: n=1 fire (M2 pair fabrication)

**Substrate quorum decision (K=3 required):**
- Option A: BANK-PENDING-SECOND-FIRE — defer canonization until n≥2 fires observed (Rule 27 precedent — conservative)
- Option B: RATIFY at n=1 per Rule 28 precedent (aggressive; K=2 convergence produced FALSE consensus is architecturally novel + amplifier)
- Option C: extend Rule 19 as sub-shape #7 rather than new Rule 29 — per Agent 1 recommendation citing Rule 19 sub-shape #7 BANK precedent

## §4 Enforcement Mechanism

Recommended implementation:
1. **Pre-filing target-verification:** any agent issuing an N-XX correction MUST include grep-command evidence in the candidacy filing (line number + verbatim text extracted from target doc)
2. **Post-hoc audit:** Council substrate C (Perplexity byte-verification) performs grep-verification during ratification; retract at council time if target-verification fails
3. **Registry:** retracted corrections logged in Council #XX close-out artifact as log-only (never re-filed as active)

## §5 Retroactive Audit Scope (CONDITIONAL on Rule 29 ratification)

Per Agent 6 research recommendation, tiered selective audit:

- **Tier A (MANDATORY):** ~20-25 K=2/K=3 framework-internal corrections → grep-verify (~2-3 hours substrate time)
- **Tier B (SPOT-CHECK):** ~30 solo framework-internal corrections → random 10-sample; expand if ≥2 fabrications detected
- **Tier C (NO AUDIT):** ~55 external primary-source citations → already covered by K=2 + Perplexity Depth-0 byte-verification discipline

**Total retroactive audit scope:** ~50-55 corrections mandatory + spot-check (Tier A + B).

## §6 Cross-Reference to Rules 19/20/27/28

- **Rule 19** (anti-fabrication citations): Rule 29 extends Rule 19 from EXTERNAL citation-scope to INTERNAL target-content-scope. K=2 pair fabricated NOT an external citation (they didn't invent a paper) but INTERNAL target claim (they invented what an internal document contained).
- **Rule 20** (multi-source triangulation): Rule 29 supplements Rule 20 for internal-document-target claims specifically
- **Rule 27** (Non-Inertness Gate): orthogonal; Rule 29 is filing-time discipline, Rule 27 is behavior-time discipline
- **Rule 28** (defensive-reducer): orthogonal; Rule 29 is documentation discipline, Rule 28 is state-preservation discipline

**Distinction from all 6 existing Rule 19 canonized sub-shapes:**
- Rule 19 sub-shapes cover external-attribution correctness
- Rule 29 covers internal-document target-verification
- Sub-shape #7 BANK precedent supports Option A defer strategy

## §7 Recommended Disposition

**BANK-PENDING-SECOND-FIRE per Council #11 substrate B (Opus ET consistency check) decision.**

If additional K=2/K=3 hallucination-audit fires surface during Council #11 retroactive audit (Tier A/B) OR during Phase 3 continued execution, promote Rule 29 to formal canonization at Council #12.

Alternative aggressive path (per Rule 28 n=1 precedent): RATIFY at Council #11 with Tier A retroactive audit as immediate follow-up.

## §8 Council #11 Filing

**Item 211** — Rule 29 K=2 target-verification for agent-issued corrections
- Type: canonical rule candidate
- Empirical foundation: n=1 fire + n=3 counterfactuals
- Recommended disposition: **BANK-PENDING** (substrate B decides A/B/C options above)
- Signature-gated (Batch 1 per Council #11 deployment plan)
- Retroactive audit CONDITIONAL scope: Tier A ~20-25 items + Tier B ~30 items spot-check

## §9 Framework Methodology Firsts

- FIRST K=2 hallucination-audit rule candidacy in framework
- FIRST Rule 29 candidate distinct from Rule 19 external-attribution scope
- FIRST tiered retroactive audit protocol (Tier A mandatory + Tier B spot-check + Tier C skip)
- FIRST filing with n=1 fire + n=3 counterfactuals empirical bracketing

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce

**Precursor artifact:** Agent 6 research at `/tmp/group-substrate-and-rule-19-canonization-research.md`
**Council #11 deployment package reference:** the deployment folder §"Item 211"
