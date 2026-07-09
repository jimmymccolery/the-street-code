---
name: Path A independent verification of Fable audit corrections (dogfooding Item 141 K-of-N quorum discipline)
scope: Independent WebFetch re-verification of Fable §A.2.3 (Arc Sift attribution) + Fable §A.2.4 (Reagan corpus scope) findings
filed: 2026-07-09 late (post Fable audit response)
disclosure: Section 6 UNVERIFIED convention applies — see §6 below
supersedes: does NOT supersede prior Rule 24 addendum on Track 1c corrections; APPENDS refined findings via independent verification
---

# Path A independent verification — Fable audit corrections

## 1. Purpose

Framework operator directed Path A independent verification of Fable audit's two citation-correction findings, dogfooding the newly-filed Item 141 K-of-N cross-substrate quorum discipline to the corrections themselves. If framework's independent verification confirms Fable's numbers, framework earns a small credibility recovery. If it doesn't, we have a new finding.

Method: WebFetch of primary sources — Item 141 K=2 quorum discipline satisfied at n=2 (Fable + framework independent verification).

## 2. Verification 1 — Arc Sift IJCAI 2022 attribution

**Fable §A.2.3 claim:** IJCAI 2022 proceedings paper #686 is "Automated Sifting of Stories from Simulated Storyworlds" by **Wilkins Leong, Julie Porteous, John Thangarajah, pp. 4950-4956**.

**Framework independent verification (2026-07-09 late):**
Direct WebFetch of `https://www.ijcai.org/proceedings/2022/686` returned VERBATIM:
- Full Title: "Automated Sifting of Stories from Simulated Storyworlds"
- Authors: "Wilkins Leong, Julie Porteous, John Thangarajah"
- Page Range: "4950-4956"
- DOI: `https://doi.org/10.24963/ijcai.2022/686`
- Abstract first sentence: "Story sifting (or story recognition) allows for the exploration of events, stories, and patterns that emerge from simulated storyworlds."

**Verdict: Fable's finding VERIFIED at K=2 quorum.**

Framework's original Track 1c "correction" that proposed injecting **"Kumaran, Freiknecht, Alexander, Porteous 2022 pp. 4949-4956"** as the IJCAI 2022 companion is confirmed FABRICATED at all four attribution axes:
- Author 1 "Kumaran" — not among the actual authors
- Author 2 "Freiknecht" — not among the actual authors
- Author 3 "Alexander" — not among the actual authors
- Author 4 "Porteous" — actually is an author (partial coincidence; Julie Porteous is on both AAMAS 2022 + IJCAI 2022 papers)
- Page range 4949-4956 — off by one (actual is 4950-4956)

**Framework home-substrate row (CC Opus 4.7 Track 1c Round 6) for Rule 19 miss-rate table:** the Arc Sift row is confirmed pure fabrication. K=2 quorum discipline applied to Fable's correction PASSED verification.

## 3. Verification 2 — Reagan 2016 corpus scope

**Fable §A.2.4 claim:** Published EPJ Data Science DOI paper states "1,327 books"; earlier arXiv preprint states 1,737; Fable's audit inspection was against third-party-hosted preprint copy (flagged UNVERIFIED-at-audit-time whether live arXiv v2 matches).

**Framework independent verification (2026-07-09 late):**

Full arXiv version history via arXiv abstract page + individual PDF WebFetch + pdftotext extraction:

| Version | Date | Corpus scope | Verified at |
|---|---|---|---|
| arXiv v1 | 2016-06-24 | **1,737 books** | pdftotext abstract line 16 + Fig. 3 caption line 361 + methods line 179 |
| arXiv v2 | 2016-07-06 | **1,737 books** | pdftotext abstract line 16 + Fig. 3 caption line 368 + methods line 191 |
| arXiv v3 | 2016-09-26 | **1,327 books** | pdftotext abstract line 17 + Fig. 3 caption line 468 + methods line 272 |
| EPJ Data Science journal | published 2016 | **1,327 books** | Fable audit + arXiv v3 matches |

**Verdict: Fable's finding PARTIALLY VERIFIED with refinement.**

Fable's claim that published EPJ Data Science says 1,327 is CONFIRMED.
Fable's claim that arXiv preprint says 1,737 is CONFIRMED for v1 + v2 (NOT v3).

Between arXiv v2 (2016-07-06) and arXiv v3 (2016-09-26), Reagan et al. **revised the corpus scope from 1,737 → 1,327 books** (documented across abstract + methods + Fig. 3 caption). The journal DOI publication preserves the v3 revised figure.

**Framework's Track 1c error refinement:**

My original Track 1c "correction to n=1,737" was NOT pure fabrication — it cited a real number from real earlier preprint versions (v1 + v2). The error was **version-provenance mixing**: attributing the v1/v2 preprint number to the journal DOI (which shows the v3 revised figure). WebFetch during Track 1c research pass landed on a preprint or preprint-derived source without version discrimination + silently validated the v1/v2 number against the journal DOI citation.

**Novel Rule 19 sub-shape (refined from prior addendum §2):** **preprint-version corpus-revision mismatch under single-source WebFetch verification.** This is DIFFERENT from the Arc Sift pure fabrication — the number was real but attached to the wrong version's citation. Framework future artifacts must pin arXiv version identifier (v1/v2/v3) when citing preprint OR use published DOI + journal figure.

## 4. Refined framework home-substrate row (Rule 19 miss-rate table)

Amending the row filed in `rule-24-addendum-track-1c-close-out-corrections-2026-07-09.md` §5:

| Substrate | Miss-rate context | Detail |
|---|---|---|
| **CC Opus 4.7 (Track 1c Round 6)** | **1 pure fabrication + 1 version-provenance mismatch** at n=2 attempted corrections | Arc Sift "Kumaran et al." fabricated at 4 attribution axes; Reagan n=1,737 real number cited against wrong (journal) DOI |

Framework's Item 141 K-of-N quorum discipline applied to this session's own corrections:
- **Arc Sift correction:** rejected via K=2 quorum (framework's home substrate vs Fable's independent WebFetch — Fable correct)
- **Reagan corpus correction:** partially accepted via K=2 quorum with version-provenance refinement (both substrates correct at their scoped versions; framework's error was cross-version attribution)

**Item 141 candidacy strengthened:** this Path A verification is Item 141's first operational application to framework's own corrections. K=2 quorum discipline caught 2 of 2 errors + refined the second finding beyond binary right/wrong to a novel Rule 19 sub-shape.

## 5. Framework operational implications

1. **Future citation-verification via WebFetch MUST pin version identifiers** for preprints when the source has revision history. arXiv provides `v1`/`v2`/`v3` URL segments; framework artifacts citing preprints must include the version.
2. **Reagan 2016 canonical citation for framework future artifacts:**
   - When citing journal (DOI 10.1140/epjds/s13688-016-0093-1): use n=1,327
   - When citing arXiv v1 or v2: use n=1,737
   - When citing arXiv v3: use n=1,327 (matches journal)
3. **Fable's Stage 7 spec §63 caption "1,327 Gutenberg books" is CORRECT.** Framework's clean-room guide v2 §1 cross-check confirms Fable's spec cites the published journal figure accurately.
4. **Framework's Item 133 filing at Council #9 agenda `AGD:2851` referencing Fable's 1,327 stands.** No correction needed at Item 133 body.
5. **Framework's Track 1c commit message `a94fdb6` claiming "n=1,737 (previously miscited as 1,327 in framework prep artifacts)" is publicly incorrect + git-history immutable.** Rule 24 correction discoverable via prior addendum + this Path A verification artifact.

## 6. Section 6 UNVERIFIED

Claims investigated but not confirmed to primary-source full-text verification at authoring:

1. **arXiv v3 → EPJ Data Science journal publication date + corpus scope continuity.** Framework confirmed v3 (2016-09-26) contains 1,327; Fable confirmed published journal contains 1,327; journal publication date not independently verified in this Path A pass. Downstream: framework accepts on Fable's authority + arXiv v3-to-journal figure-preservation is the reasonable inference; would benefit from journal publication metadata verification in future.
2. **v2-to-v3 revision motivation.** Reagan et al. filed no comment field on any of the 3 arXiv versions per arxiv.org/abs/1606.07772. The 1,737 → 1,327 revision (a reduction of 410 books; ~24%) is not documented in metadata. Framework does NOT claim to know the reason. Downstream: no framework artifact should attribute motive to the revision.
3. **Version-provenance mismatch sub-shape novelty.** Framework filed this as novel Rule 19 sub-shape distinct from pure fabrication. Fable audit did NOT explicitly distinguish these two error classes; Fable §A.2.4 grouped them under the same "correction is contested + inverted" finding. Framework's refinement is our own contribution + subject to Council #9 review.

## 7. Cross-references

- Fable 5 adversarial audit `fable-5-adversarial-audit-2026-07-09.md` §A.2.3 + §A.2.4 + §A.2.R
- Prior Rule 24 addendum `rule-24-addendum-track-1c-close-out-corrections-2026-07-09.md` §2 + §3 + §5
- Council #9 Item 141 candidacy (K-of-N cross-substrate quorum rule) — first operational application per this Path A verification
- Reagan et al. 2016 EPJ Data Science DOI 10.1140/epjds/s13688-016-0093-1 (n=1,327 journal)
- arXiv 1606.07772 v1 + v2 (n=1,737) + v3 (n=1,327)
- Leong, Porteous, Thangarajah 2022 IJCAI-22 pp. 4950-4956 DOI 10.24963/ijcai.2022/686

## 8. Status

**Path A independent verification CLOSED at n=2 quorum discipline.** Both Fable audit corrections VERIFIED (Arc Sift binary; Reagan with version-provenance refinement). Framework home-substrate row refined + Item 141 K-of-N quorum discipline first operational application filed as candidacy anchor.
