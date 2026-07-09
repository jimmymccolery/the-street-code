#!/usr/bin/env bash
# audit.sh — Deterministic pre-publication audit checks for the-street-code corpus
#
# Encodes the mechanical subset of methodology/post_audit_checklist.md.
# Judgment-based items (disclosure compliance, Madisonian Gate attribution,
# F-18 framing) stay with the human pass per the checklist's documented
# scope-amendment.
#
# Exit code 0 = all blocking checks pass (warnings may still surface).
# Exit code 1 = at least one blocking check failed.
#
# Usage: ./scripts/audit.sh (run from repo root)

set -u  # strict undefined-var; but NOT -e so all checks run even if one fails

FAIL=0
WARN=0

# Color helpers (no-op if not in a terminal)
if [ -t 1 ]; then
  R='\033[31m'; G='\033[32m'; Y='\033[33m'; N='\033[0m'
else
  R=''; G=''; Y=''; N=''
fi

pass()  { printf "${G}PASS${N}  %s\n" "$1"; }
fail()  { printf "${R}FAIL${N}  %s\n" "$1"; FAIL=$((FAIL+1)); }
warn()  { printf "${Y}WARN${N}  %s\n" "$1"; WARN=$((WARN+1)); }
info()  { printf "      %s\n" "$1"; }

echo "================================================================"
echo " The Street Code — deterministic audit"
echo " $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "================================================================"

# ----------------------------------------------------------------------
# A. Em-dash discipline (applies post 0036 onward per 2026-06-30 amendment)
# ----------------------------------------------------------------------
echo
echo "A. Em-dash discipline (scope: posts 0036+)"
em_total=$(grep -ho '—' posts/0036-*.md posts/00[4-9]*-*.md posts/01*-*.md posts/02*-*.md posts/03*-*.md posts/04*-*.md posts/05*-*.md posts/06*-*.md posts/07*-*.md posts/08*-*.md posts/09*-*.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$em_total" -eq 0 ]; then
  pass "no em-dashes (U+2014) in posts 0036+"
else
  fail "$em_total em-dashes found in posts 0036+ (current discipline violation)"
  grep -l '—' posts/0036-*.md posts/00[4-9]*-*.md posts/01*-*.md posts/02*-*.md posts/03*-*.md posts/04*-*.md posts/05*-*.md posts/06*-*.md posts/07*-*.md posts/08*-*.md posts/09*-*.md 2>/dev/null | sed 's/^/      /'
fi
em_legacy=$(grep -ho '—' posts/000[1-9]-*.md posts/001[0-9]-*.md posts/002[0-9]-*.md posts/003[0-5]-*.md 2>/dev/null | wc -l | tr -d ' ')
info "legacy em-dashes in posts 0001-0035 (scope-amended; not a violation): $em_legacy"

# ----------------------------------------------------------------------
# B. Slot uniqueness + gap profile
# ----------------------------------------------------------------------
echo
echo "B. Slot uniqueness + gap profile"
dupes=$(ls posts/ | grep -oE '^[0-9]{4}' | sort | uniq -d)
if [ -z "$dupes" ]; then
  pass "no duplicate four-digit slot numbers"
else
  fail "duplicate slot numbers found:"
  echo "$dupes" | sed 's/^/      /'
fi

gaps=$(ls posts/ | grep -oE '^[0-9]{4}' | sort -u | awk 'NR>1 && $1+0!=p+1{printf "GAP after %04d -> %04d\n",p,$1+0} {p=$1+0}')
expected_gap="GAP after 0106 -> 0110"
if [ "$gaps" = "$expected_gap" ]; then
  pass "single expected gap (0107-0109 retraction)"
elif [ -z "$gaps" ]; then
  warn "no gaps found — confirm the 0107-0109 retracted-slot gap is still intentionally preserved"
else
  fail "unexpected gap profile:"
  echo "$gaps" | sed 's/^/      /'
fi

# ----------------------------------------------------------------------
# C. SUMMARY.md / posts/ bijection
# ----------------------------------------------------------------------
echo
echo "C. SUMMARY.md / posts/ bijection"
posts_nums=$(ls posts/*.md 2>/dev/null | grep -oE '/[0-9]{4}' | tr -d '/' | sed 's/^0*//' | sort -n)
summary_nums=$(grep -oE '^### [0-9]+\.' SUMMARY.md 2>/dev/null | grep -oE '[0-9]+' | sed 's/^0*//' | sort -n)
only_posts=$(comm -23 <(echo "$posts_nums") <(echo "$summary_nums"))
only_summary=$(comm -13 <(echo "$posts_nums") <(echo "$summary_nums"))

if [ -z "$only_posts" ] && [ -z "$only_summary" ]; then
  pass "every post has a SUMMARY entry and vice versa (modulo the 107-109 aggregate retraction entry which uses non-standard ### 107-109. format)"
else
  if [ -n "$only_posts" ]; then
    fail "posts/ entries without SUMMARY entry:"
    echo "$only_posts" | sed 's/^/      /'
  fi
  if [ -n "$only_summary" ]; then
    fail "SUMMARY entries without posts/ file:"
    echo "$only_summary" | sed 's/^/      /'
  fi
fi

# ----------------------------------------------------------------------
# D. Frontmatter consistency (scope: posts 0036+; legacy 0026-0035 preserved per immutability)
# ----------------------------------------------------------------------
echo
echo "D. Frontmatter consistency (scope: posts 0036+)"
missing_count=0
for f in posts/0036-*.md posts/00[4-9]*-*.md posts/01*-*.md posts/02*-*.md posts/03*-*.md posts/04*-*.md posts/05*-*.md posts/06*-*.md posts/07*-*.md posts/08*-*.md posts/09*-*.md; do
  [ -f "$f" ] || continue
  grep -q '^\*\*Author:\*\*'  "$f" || { echo "      MISSING **Author:** in $f"; missing_count=$((missing_count+1)); }
  grep -q '^\*\*Date:\*\*'    "$f" || { echo "      MISSING **Date:** in $f"; missing_count=$((missing_count+1)); }
  grep -q '^\*\*Status:\*\*'  "$f" || { echo "      MISSING **Status:** in $f"; missing_count=$((missing_count+1)); }
  grep -q '^\*.*AI'   "$f" || { echo "      MISSING AI-assistance disclosure note in $f"; missing_count=$((missing_count+1)); }
done
if [ "$missing_count" -eq 0 ]; then
  pass "all posts 0036+ have required frontmatter (Author/Date/Status + disclosure note)"
else
  fail "$missing_count frontmatter omissions in posts 0036+ (current discipline violation)"
fi
# Document the legacy gap as informational
legacy_missing=0
for f in posts/002[6-9]-*.md posts/003[0-5]-*.md; do
  [ -f "$f" ] || continue
  grep -q '^\*\*Author:\*\*'  "$f" || legacy_missing=$((legacy_missing+1))
  grep -q '^\*\*Date:\*\*'    "$f" || legacy_missing=$((legacy_missing+1))
  grep -q '^\*\*Status:\*\*'  "$f" || legacy_missing=$((legacy_missing+1))
  grep -q '^\*.*AI'   "$f" || legacy_missing=$((legacy_missing+1))
done
info "legacy frontmatter omissions in posts 0026-0035 (scope-amended; not a violation): $legacy_missing"

# ----------------------------------------------------------------------
# E. Orphan / empty-header detection
# ----------------------------------------------------------------------
echo
echo "E. Orphan H2 header detection"
orphan_count=0
for f in posts/*.md; do
  result=$(awk '
    /^## /{
      if (prev_h2 && !content_seen) print FILENAME": orphan H2: " prev_line;
      prev_h2=1; content_seen=0; prev_line=$0; next
    }
    /^[^[:space:]]/{ if (prev_h2) content_seen=1 }
  ' "$f")
  if [ -n "$result" ]; then
    echo "$result" | sed 's/^/      /'
    orphan_count=$((orphan_count+1))
  fi
done
if [ "$orphan_count" -eq 0 ]; then
  pass "no orphan H2 headers (H2 immediately followed by another H2 without content between)"
else
  fail "$orphan_count files with orphan H2 headers"
fi

# ----------------------------------------------------------------------
# H. Section 6 UNVERIFIED disclosure convention (methodology + posts adoption 2026-07-09+)
#    Per Fable 5 adversarial audit §C.4 lint-rule proposal + Council #9 Item 141+142 candidacy.
#    Framework-scope methodology documents authored 2026-07-09+ must carry either
#    a "## Section 6 UNVERIFIED" heading with schema-conformant entries OR the
#    literal token NONE-CLAIMED. Backfilling legacy artifacts uses LEGACY-SWEEP INDEX (deferred).
# ----------------------------------------------------------------------
echo
echo "H. Section 6 UNVERIFIED disclosure convention (methodology 2026-07-09+ + forward-app scope)"
sec6_missing=0
sec6_malformed=0
# Framework-scope methodology documents authored 2026-07-09 late onwards. Prior artifacts
# are pre-convention per Rule 24 immutability + LEGACY-SWEEP INDEX deferral.
sec6_files="methodology/a2-phase-a-close-out-2026-07-09.md \
methodology/a2-phase-b-close-out-2026-07-09.md \
methodology/a2-phase-c-extension-status-2026-07-09.md \
methodology/a2-phase-d-close-out-2026-07-09.md \
methodology/track-1c-reagan-arc-close-out-2026-07-09.md \
methodology/section-6-unverified-disclosure-convention-2026-07-09.md \
methodology/a2-non-inertness-gate-planning-2026-07-09.md"
for f in $sec6_files methodology/rule-24-addendum-*-2026-07-09.md; do
  [ -f "$f" ] || continue
  # Check for Section 6 header (variations: "## 6." "## 6 " "## Section 6" or NONE-CLAIMED sentinel)
  if grep -qE '^## (6\.|6 |Section 6|[0-9]+\. UNVERIFIED)' "$f" 2>/dev/null || grep -q "NONE-CLAIMED" "$f" 2>/dev/null; then
    :  # present
  else
    fail "Section 6 UNVERIFIED disclosure MISSING in $f"
    sec6_missing=$((sec6_missing+1))
  fi
done
if [ "$sec6_missing" -eq 0 ]; then
  pass "Section 6 UNVERIFIED disclosure present in all framework-scope methodology 2026-07-09+ artifacts"
fi

# ----------------------------------------------------------------------
# F. Cross-reference sanity (warn-pass; non-blocking)
# ----------------------------------------------------------------------
echo
echo "F. Cross-reference sanity (informational)"
unresolved=$(grep -rhoE 'Post [0-9]+' posts/*.md 2>/dev/null | grep -oE '[0-9]+' | sort -un | while read n; do
  # Force base-10 interpretation to avoid printf treating "08" / "09" / "0128" as octal
  nn=$(printf '%04d' "$((10#$n))")
  if ! ls posts/${nn}-*.md >/dev/null 2>&1; then
    # 107-109 are retracted; expected unresolved
    if [ "$((10#$n))" -lt 107 ] || [ "$((10#$n))" -gt 109 ]; then
      echo "Post $n (no posts/${nn}-*.md)"
    fi
  fi
done)
if [ -z "$unresolved" ]; then
  pass "all Post NN references resolve (107-109 retracted-slot references appropriately excluded)"
else
  warn "unresolved Post NN references (may be drafts or out-of-range; review):"
  echo "$unresolved" | sed 's/^/      /'
fi

# ----------------------------------------------------------------------
# G. Citation hygiene (warn-pass; non-blocking)
# ----------------------------------------------------------------------
echo
echo "G. Citation hygiene (informational)"
CIT=research/citations/modified-c-bis-canonical-citations.md
if [ -f "$CIT" ]; then
  uncited=$(grep -rhoE 'arXiv:[0-9]{4}\.[0-9]{4,5}' posts/*.md 2>/dev/null | sort -u | while read id; do
    grep -qF "$id" "$CIT" || echo "$id"
  done)
  if [ -z "$uncited" ]; then
    pass "all arXiv citations in posts/ appear in master citation reference"
  else
    warn "arXiv citations in posts/ not in master citation reference:"
    echo "$uncited" | sed 's/^/      /'
  fi

  # Spot-check the known transposition trap (AgentCrypt arXiv:2512.08104 NOT 2605.03213)
  if grep -rln 'arXiv:2605.03213' posts/*.md >/dev/null 2>&1; then
    fail "AgentCrypt transposition error: arXiv:2605.03213 found in posts/ (should be arXiv:2512.08104)"
  else
    pass "no AgentCrypt transposition error (arXiv:2605.03213) in posts/"
  fi
else
  warn "master citation file $CIT not found; citation hygiene skipped"
fi

# ----------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------
echo
echo "================================================================"
echo " Audit summary"
echo "================================================================"
if [ "$FAIL" -eq 0 ]; then
  printf "${G}PASS${N} — corpus passes all blocking checks (warnings: %s)\n" "$WARN"
  exit 0
else
  printf "${R}FAIL${N} — %s blocking check(s) failed (warnings: %s)\n" "$FAIL" "$WARN"
  exit 1
fi
