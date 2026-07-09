---
name: Rule 24 addendum — Track 1c close-out corrections (Fable 5 adversarial audit ratifications)
scope: `track-1c-reagan-arc-close-out-2026-07-09.md` § UNVERIFIED disclosure + citation-attribution corrections
filed: 2026-07-09 late (Fable 5 adversarial audit response)
disclosure: Section 6 UNVERIFIED convention applies — see §6 below
supersedes: does NOT supersede prior artifact (Rule 24 immutability preserves prior state); ADDS corrections as append-only addendum
---

# Rule 24 addendum — Track 1c close-out corrections

## 1. Purpose

Fable 5 adversarial audit `fable-5-adversarial-audit-2026-07-09.md` §A.2 identified 2 CRITICAL citation-correction defects in framework's Track 1c close-out artifact + §A.2.1 identified 1 HYPOTHESIS-SUBSTITUTION overclaim. This addendum preserves prior artifact immutability while filing corrections per Rule 24 canonical-file correction protocol.

## 2. Correction 1 — Reagan 2016 corpus scope: n=1,327 (published EPJ Data Science) NOT n=1,737

**Prior claim (Track 1c close-out §6.1 + phase-3-findings-2026-07-09.md §"Rule 19 disclosure" + commit message `a94fdb6`):** "Reagan 2016 corpus n=1,737 (previously miscited as 1,327 in framework prep artifacts)."

**Fable 5 audit finding (§A.2.4):** The published EPJ Data Science version at DOI 10.1140/epjds/s13688-016-0093-1 states "1,327 books" verbatim. The 1,737 figure appears only in an earlier arXiv preprint revision (v2). Framework's Track 1c close-out cited the journal DOI + attributed the 1,737 figure to it, which is version-inconsistent.

**Corrected framework position:** Reagan et al. 2016 EPJ Data Science 5:31 (DOI 10.1140/epjds/s13688-016-0093-1) reports **n=1,327 books**. This is what framework future artifacts must carry when citing the journal DOI. The arXiv preprint v2 carrying n=1,737 is a distinct version; version provenance must be pinned when either figure is cited.

**Framework attribution of the error:** framework's Track 1c research pass (Rule 19 verification of Reagan 2016) used a WebFetch that landed on a third-party mirror of the arXiv preprint rather than the journal version. "VERIFIED via WebFetch" without version discrimination silently validated the wrong figure against a journal DOI citation. This is a novel Rule 19 sub-shape: **preprint-vs-published version mismatch under single-source WebFetch verification.**

**Downstream constraint:** any framework artifact carrying n=1,737 with EPJ Data Science DOI attribution must be treated as containing an unverified claim per §6 UNVERIFIED convention. Framework does not silently edit those artifacts (Rule 24 immutability); this addendum is the discoverable correction. Commit message `a94fdb6` is public + immutable at git-history level; discoverability of the correction resides in this addendum + the audit-preserved file at `fable-5-adversarial-audit-2026-07-09.md`.

## 3. Correction 2 — Arc Sift IJCAI 2022 attribution: Leong, Porteous, Thangarajah pp. 4950-4956 (NOT Kumaran et al. as clean-room guide "correction" claimed)

**Prior claim (`FABLE-5-BRAINSTORM-IMPLEMENTATION-CLEAN-ROOM-CODING-GUIDE-2026-07-09.md` §2.3 + §4.6):** "Arc Sift IJCAI 2022 companion is Kumaran, Freiknecht, Alexander, Porteous 2022 pp. 4949-4956 (not Leong, Porteous, Thangarajah as Fable's Stage 7 spec §1.3 stated)."

**Fable 5 audit finding (§A.2.3):** Independently verified via `ijcai.org/proceedings/2022/686`. The actual paper is "Automated Sifting of Stories from Simulated Storyworlds" by **Wilkins Leong, Julie Porteous, John Thangarajah, pp. 4950-4956** — the same authors as the AAMAS 2022 extended abstract. There is no Kumaran/Freiknecht/Alexander/Porteous IJCAI 2022 story-sifting companion at those pages. **Framework's "correction" was a fabrication.** Framework's Track 1c research substrate (CC Opus 4.7 via WebFetch) produced a false author list, then framework proposed to propagate the fabrication as a correction to Fable's original correct attribution.

**Corrected framework position:** Fable 5's original Stage 7 spec citation stands as filed: **Leong, Porteous, Thangarajah 2022 IJCAI-22 pp. 4950-4956** (companion to AAMAS 2022 extended abstract with same three authors).

**Framework attribution of the error:** Track 1c research pass produced fabricated author attribution + page-range attribution (both off by one; pp. 4949 vs 4950). Framework's clean-room guide §2.3 + §4.6 propagated the fabrication + instructed downstream Council #9 Item 133 filing to "reflect corrected author attribution." Fable's live-agenda check confirmed Item 133 body at `AGD:2823` currently reads only "Arc Sift AAMAS 2022 + IJCAI 2022 companion" without authors — NOT YET contaminated. Framework must NOT execute the clean-room guide's §4 instruction. Council #9 Item 133 filing retains ambiguous no-author citation until further corroboration OR restores Leong-Porteous-Thangarajah per this addendum.

**Novel Rule 19 sub-shape:** **verification-substrate fabricating a "correction" that inverts a correctly-attributed original.** Framework author accepted the fabricated correction without independent primary-source verification (single-source WebFetch of the "IJCAI 2022 companion" landed on an inaccurate CC-substrate-inferred author list).

## 4. Correction 3 — H24 verdict interpretation: DOES NOT test H3 drift-story invisibility claim (hypothesis substitution)

**Prior claim (Track 1c close-out §4 + clean-room guide §0):** "Fable's central drift-story claim is EMPIRICALLY SUPPORTED at A1 scope on framework's identified signal channel."

**Fable 5 audit finding (§A.2.1 + §B.2):** H24 tests classifier-accuracy enrichment via Reagan-arc DTW features on the 71-baseline + 66-Reagan = 137 candidate feature pool. Fable 5's central drift-story claim is H3 (Stage 7 spec S7:137): "≥25% of Family II matches contain no single event above the SRRS-prior salience threshold" — a distinct hypothesis with distinct pass criterion (Family II trajectory matchers detect stories INVISIBLE to event acceptors). H24 says nothing about invisibility to Family I. **Framework substituted hypotheses in its overclaim.**

**Additionally:** the +6.7pp at k=10 is one reclassified trajectory at N=15; Wilson CIs overlap ([35.7%, 80.2%] baseline k=10; enriched 66.7% sits inside). The enriched feature set NEVER beats the best baseline configuration (k=5, 73.3%, permP=0.003) at any k in the sweep. Post 0182 multi-seed discipline + Gemini R5 HIGH-3 N≥5 discipline both violated for this headline.

**Corrected framework position:** H24 supports the WEAKER claim that Reagan-arc trajectory shape carries bundle-discriminative information on the accommodationFrequency channel at N=15 proof-of-concept scale. H3 remains UNTESTED at framework scope. The k=10 IMPROVES result is one sample requiring multi-seed replication before any Council #9 confidence upgrade rests on it.

**Downstream constraint:** Council #9 Item 133 confidence calibration currently reads "HIGH" (per Fable's live-agenda check at `AGD:2856`). Framework's clean-room guide asked for "MEDIUM to MEDIUM-HIGH upgrade" (a further inconsistency Fable flagged at §B.2). Fable's evidence-based recommendation: recalibrate to **MEDIUM**. Framework agrees: recalibrate Item 133 to MEDIUM pending H24b nested-CV multi-seed replication + H3 Stage 7-lite empirical test (per Fable D.4).

## 5. Framework's home-substrate row addition to Rule 19 miss-rate table

Fable's audit §A.2.R item (3) requires: "Add both episodes as calibration entries to the miss-rate table lineage: this was a CC (Opus 4.7) round, and its citation-correction layer produced 1 fabrication + 1 contested inversion out of 2 offered corrections. The table currently records external-substrate miss rates only; the framework's home substrate earned a row."

**Framework accepts the addition:**

| Substrate | Miss rate | Fabrications / contested |
|---|---|---|
| Perplexity Round 5 | ~33% | 3 CRITICAL citation fabrications + 7 ISBN errors |
| Grok R5a | ~23.5% | prep-pipeline attachment-freshness gap |
| Grok R5b | ~33% | 3 MEDIUM implementation-scope findings |
| Gemini Deep Think Round 5 | ~44% | 2 CRITICAL statistical + 3 HIGH |
| Gemini Deep Research Round 5 | ~25% | 1 CRITICAL Kito 2017 + 3 HIGH |
| **CC Opus 4.7 (Track 1c Round 6, this session)** | **100%** | **2 offered citation corrections, both wrong — 1 fabrication (Kumaran et al.) + 1 contested inversion (Reagan n=1,737)** |

Framework's home-substrate miss rate is now empirically-anchored at n=1 with 100% error rate on offered corrections. This is diagnostic not conclusive at n=1; multi-substrate cross-verification per Fable D.5 K-of-N quorum rule proposal becomes empirically-anchored candidacy at Council #9.

## 6. UNVERIFIED disclosure

Claims investigated in preparing this addendum:

1. **Reagan 2016 published EPJ Data Science n=1,327 verbatim.** Attempted verification: WebFetch reading of Fable's audit citation trail; Fable independently verified via `epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-016-0093-1`. Outcome: VERIFIED via Fable's audit-time WebFetch (framework accepts Fable's cross-verification). Downstream constraint: framework must re-verify at journal source before any future citation cements the correction.
2. **Leong, Porteous, Thangarajah 2022 IJCAI-22 pp. 4950-4956 verbatim.** Attempted verification: Fable audit-time direct fetch of ijcai.org/proceedings/2022/686. Outcome: VERIFIED via Fable's audit-time direct URL fetch (Google Scholar cross-verification). Downstream constraint: framework must re-verify at IJCAI proceedings before Item 133 filing amendment includes authors.
3. **arXiv preprint v2 n=1,737 provenance.** Attempted verification: Fable audit notes third-party-hosted copy consulted. Outcome: UNVERIFIED-at-audit-time whether live arXiv v2 matches. Downstream constraint: framework does NOT cite n=1,737 with arXiv provenance without direct arXiv v2 verification.

## 7. Cross-references

- Fable 5 adversarial audit preserved at `fable-5-adversarial-audit-2026-07-09.md`
- Prior Track 1c close-out artifact: `track-1c-reagan-arc-close-out-2026-07-09.md` (IMMUTABLE per Rule 24; NOT edited)
- Prior phase-3-findings artifact: `~/Projects/Open Alley/scripts/island-sim-scale-calibration/phase-3-findings-2026-07-09.md` (IMMUTABLE per Rule 24; NOT edited)
- Prior clean-room guide: `~/Desktop/FABLE-5-BRAINSTORM-IMPLEMENTATION-CLEAN-ROOM-CODING-GUIDE-2026-07-09.md` (framework artifact; per Rule 24 immutability, NOT edited; Fable audit v2 update ships as separate artifact)
- Rule 24 canonical file correction protocol: `~/Projects/master-setup/operational_discipline_rules.canonical.md`
- Section 6 UNVERIFIED convention: `section-6-unverified-disclosure-convention-2026-07-09.md`

## 8. Status

**Corrections FILED per Rule 24 addendum protocol.** Prior artifacts immutability preserved. Framework proceeds with corrected positions for future work. Council #9 Item 133 confidence recalibration + Item 133 filing amendment covered by subsequent artifact `council-9-item-133-confidence-recalibration-2026-07-09.md`.
