# Audit Baseline — 2026-06-30

**Established:** 2026-06-30 (during the comprehensive cleanup pass)
**Scope:** Full corpus (125 published posts at slots 0001-0128 with 0107-0109 retracted)
**Purpose:** Record the verified-clean baseline state for future regression investigations

---

## Deterministic checks executed

### 1. Em-dash discipline

| Scope | Count | Verdict |
|---|---|---|
| Posts 0036-0128 (current discipline; clean target) | 0 em-dashes (U+2014) | ✓ PASS |
| Posts 0001-0035 (pre-amendment legacy; preserved per immutability) | 118 em-dashes across 12 files (0005, 0006, 0025-0029, 0031-0035) | ✓ Scope-amended per `post_audit_checklist.md` 2026-06-30 amendment; NOT retroactively fixed |
| **Corpus-wide net** | 118 legacy em-dashes acknowledged as scope-amended; 0 violations against current discipline | ✓ **PASS** |

**Verification command:**
```bash
total=$(grep -ho '—' posts/0036-*.md posts/00[4-9]*-*.md posts/01*-*.md 2>/dev/null | wc -l)
[ "$total" -eq 0 ] && echo "PASS post-0036+ clean" || echo "FAIL: $total em-dashes in post-0036+"
```

### 2. Slot uniqueness + gap profile

| Check | Result |
|---|---|
| Duplicate four-digit slot numbers | 0 (no duplicates) |
| Sequence gaps | Single intentional gap: 0107-0109 (retracted-duplicates of 0091-0093 per 2026-06-30 documentation in SUMMARY.md entry) |
| Slot ordering in SUMMARY.md | Sequential except for the 0107-0109 retraction-aggregate entry; matches posts/ directory state |

**Verification command:**
```bash
ls posts/ | grep -oE '^[0-9]{4}' | sort | uniq -d  # empty = no dupes
ls posts/ | grep -oE '^[0-9]{4}' | sort -u | awk 'NR>1 && $1+0!=p+1{print "GAP after "p" -> "$1} {p=$1+0}'
# Expected: "GAP after 0106 -> 0110" (the intentional retraction gap)
```

### 3. Frontmatter consistency (scope: posts 0036+)

| Check | Result |
|---|---|
| Posts 0036-0128 with `**Author:**` field | 93 / 93 ✓ |
| Posts 0036-0128 with `**Date:**` field | 93 / 93 ✓ |
| Posts 0036-0128 with `**Status:**` field | 93 / 93 ✓ |
| Posts 0036-0128 with italic AI-assistance disclosure note | 93 / 93 ✓ |
| **Legacy gap (posts 0026-0035; 10 files)** | 33 cumulative frontmatter omissions across the four fields (Author/Date/Status/disclosure-note); these are preserved per immutability convention per the 2026-06-30 scope amendment in `post_audit_checklist.md`. |

The legacy frontmatter gap is parallel to the legacy em-dash gap (posts 0005-0035 with 118 em-dashes). Both gaps reflect spec-drift where the convention was tightened partway through the corpus; the immutability convention preserves the original posts rather than back-applying corrections, with the gap documented openly as visible audit record (parallel discipline to the 0107-0109 retracted-slot gap).

### 4. SUMMARY.md / posts/ bijection

| Check | Result |
|---|---|
| Posts in `posts/` not in `SUMMARY.md` | 0 |
| SUMMARY.md entries without corresponding `posts/` file | 0 (the 107-109 retraction-aggregate entry intentionally has no corresponding file per the gap convention) |

### 5. Orphan H2 headers

| Check | Result |
|---|---|
| Posts with H2 immediately followed by another H2 with no content between | 0 |

### 6. Cross-reference sanity (informational)

| Check | Result |
|---|---|
| `Post NN` / `Posts NN-MM` references in posts/ | All references in posts 0110-0128 resolve to existing posts; references to 107-109 are appropriately limited (the retracted slots are referenced only in the retraction discussion in posts 0110, 0117, and in SUMMARY.md entry 107-109) |
| Posts 0036+ internal cross-refs | Use "post 0XXX in this arc" format; verified consistent during the 0110-0128 shipping arc |

---

## Repo-level state at baseline

| Metric | Value |
|---|---|
| Tracked files | 167 |
| Published posts | 125 |
| Date range | 2026-05-02 → 2026-06-29 |
| Total post word count | ~331,000 |
| SUMMARY.md | 745 lines / ~398 KB |
| Drafts | 14 idea-queue placeholders (slots 48-61) + INDEX.md + CANON.md |
| Methodology docs | post_audit_checklist.md + this baseline + README.md |
| Brand assets | 14 images + README.md + audits/ subdirectory |
| Research citations | research/citations/modified-c-bis-canonical-citations.md |
| License | MIT |

---

## What this baseline does NOT cover

These items require human judgment, not deterministic checks, and were not validated in this baseline pass per the audit checklist's "Judgment-based audit items NOT automated" note:

- **Disclosure compliance** (per Approach 2 soft-disclosure rule): abstract Memory Lanes specifics; product names; schema symbols; specific quantitative anchors from operator research arcs. These require reading-for-meaning passes, not pattern-matching.
- **Madisonian Gate attribution / Federalist hedge level**: ensuring posts that mention the Madisonian Gate use Federalist 51 with the loose-citation hedge per Post 05's framing, not Federalist 10.
- **Modification 6 boundary discriminator framing**: ensuring posts use "state-space content" framing per F-18 retraction, not the retired "present-state-anchored vs temporally-extended" framing.

These judgment-based items operate at the operator-side audit pass; the baseline above covers the mechanical subset that CI could enforce.

---

## How to use this baseline

When investigating a suspected regression:
1. Re-run the verification commands above against the current tree
2. Compare against this baseline's results
3. Any divergence is a regression worth investigating (or a deliberate change that should be documented as a new baseline)

When establishing a subsequent baseline (e.g., post-future-arc), copy this file with a new date suffix and update the metrics + verdicts to match current state. Do not overwrite this 2026-06-30 baseline — it is the reference point for the Posts 110-128 arc's clean-audit verdict.
