# Council #11 Candidacy Items — Filed 2026-07-11 at Council #10 Close

**Filed by:** CC on operator directive after Council #10 aggregate close-out
**Origin:** Council #10 substrate deployment (Grok + Opus + Perplexity) surfaced 5 framework-scale amendments + 1 framework hygiene audit as candidacies beyond Item 156's scope
**Council #10 close-out:** `~/Desktop/COUNCIL-10-DEPLOY/council-work/aggregate-close-out.yaml`
**Council #11 nominal window:** September 2026 or accelerated per operator judgment
**Substrate strategy recommendation:** K=3 (Grok + Opus + Perplexity per Council #10 empirical vindication); ChatGPT DR skip unless specific item benefits

---

## Item 158 — Framework-wide citation hygiene audit

**Origin:** Perplexity Substrate C (Council #10) surfaced 10 novel citation-hygiene findings (N-10 through N-20) via Depth-0 byte-level verification of Item 156's ~100 citations. 4 systematic drift patterns identified. Opus Substrate B (N-2) surfaced framework-wide Post 0146 ±30% mis-attribution independently. Composes.

**Scope:** Primary-source verification pass across all canonical Posts + Council items + spec files. Grep for known drift patterns (author fusion, year misattribution, constant misattribution to wrong year, fabricated attributions). Substrate C's 10 findings provide initial coverage; extend to full corpus (~200 canonical files).

**Systematic drift patterns identified:**
1. **Author fusion** — e.g. "Sabater-Sierra" fuses J. Sabater + C. Sierra (N-10)
2. **Year misattribution** — e.g. Dunbar 1993 human 148/150 figure cited to Dunbar 1992
3. **Constant misattribution to wrong year of same author-pair** — e.g. Newman-Girvan 2004 Q≥0.3 threshold cited to Girvan-Newman 2002 (N-11)
4. **Fabricated attributions** — e.g. Hollander β=likability (N-15) + Latane 1981 "canonical .4" (N-13) + Levine 2002 β=0.5 (N-14)

**Method:**
- Deploy Perplexity Computer with strict boolean schema (proven at 80.4% verified rate in Council #10)
- OR ChatGPT DR with citation-verification role
- Estimate 2-4hr substrate time for full corpus
- Deliverable: per-citation record with authors_match / year_match / venue_match / effect_size_match / sample_size_match booleans + correction_needed strings + primary_source_url

**Priority:** HIGH (composes with Item 159 Post 0146 re-attribution)

**Impact if ratified:**
- Framework citation reliability rises from ~80% baseline to ~95%+
- Prevents future substrate deployments from re-surfacing already-known drift
- Establishes primary-source verification as ongoing framework hygiene practice

**Substrate role:** verification-focused (Perplexity or ChatGPT DR); adversarial + consistency substrates optional

**K=2 quorum requirement:** for any correction pattern with framework-wide impact (multi-file grep), require K=2 verification before framework-wide application

---

## Item 159 — Post 0146 ±30% coupling bound framework-wide re-attribution

**Origin:** Opus Substrate B (Council #10) N-2 finding: MEMORY_INFORMED_MODULATION_MAGNITUDE (±30% Layer 4→5 coupling bound) is real (file 04 Item 155 precedent line 249 references it) but is NOT in Post 0146. Post 0146 is a conceptual essay containing no numeric coupling spec. Item 156 agenda + spec + file 04 all mis-cite. Predates + exceeds Item 156.

**Framework-wide impact:** grep pattern "per Post 0146" for ±30% / MEMORY_INFORMED_MODULATION_MAGNITUDE / Layer-4→5 numeric spec surfaces multiple files (not just Item 156).

**Two disposition paths (Opus's option (a) vs (b)):**

**Option (a):** Amend Post 0146 canonical body to actually canonize MEMORY_INFORMED_MODULATION_MAGNITUDE + Layer-4→5 numeric coupling spec. This would make the widespread "per Post 0146" citations correct.

**Option (b):** Leave Post 0146 as the conceptual essay + re-point every "±30% per Post 0146" citation to actual definition site (code constant OR different Post). Opus's recommendation: "(b) is cheaper and more honest."

**Method:**
- grep -r "per Post 0146" across ~/Projects/the-street-code/ + ~/Projects/sim-ai/architecture/ + ~/Projects/the-street-code/posts/
- Determine actual definition site for MEMORY_INFORMED_MODULATION_MAGNITUDE (likely code constant in sim-ai or a different canonical Post)
- If Option (b): re-cite each occurrence with correction note
- If Option (a): amend Post 0146 canonical body

**Priority:** HIGH — framework-wide citation reliability + immediately actionable

**Composes with Item 158** — Post 0146 re-attribution is a special-case citation hygiene fix within the broader framework-wide audit

**Ratification signal expected:** Option (b) preferred per Opus recommendation + cheaper + more honest + preserves Post 0146 as conceptual essay it already is

---

## Item 160 — Rule 27 Non-Inertness Gate category-slippage clarification

**Origin:** Opus Substrate B (Council #10) N-3 finding: Rule 27's canonized precedent measures K/N over NAMED OUTPUT VARIABLES within one harness (H-mem-7: 3/3 channels {totalEncoded, longFrac, meanValence}; H-rescue-6: 3/4 rescue-choice channels). Item 156 constructs K/N over separate HYPOTHESES, conflating "hypothesis" with "channel." N=8 never enumerated. K=5/N=8 = 62.5% below precedent band (75-100%). v2 K=9/N=15 miscounts H-11 (15pp criterion structurally below Rule 27's ≥20% gate) + H-6 (correlation orthogonal to differentiation).

**Proposed Rule 27 clarification amendments to canonical body:**

1. **Pin "channel" definition:** "channel" = named output variable within one harness, NOT hypothesis. Precedent: H-mem-7 K=3 counted over {totalEncoded, longFrac, meanValence} named channels within one harness; H-rescue-6 K=3 counted over {rescue-choice distribution, guilt_b delta, vindictive-satisfaction fires, moral-violation fires}.

2. **State K/N floor:** ≥75% (precedent band from prior CLEARED ships is 75-100%). Aggregate below 75% flags optimism concern requiring justification.

3. **Separate gate-channels from validity-hypotheses:** Only differentiation-type hypotheses (≥20% population spread over named output variable) count toward K/N gate. Correlation / accuracy / stability / seed-fraction hypotheses are VALIDITY tests, orthogonal to gate accounting.

4. **Add usage note:** future architectural extensions must explicitly enumerate N as named output variables at candidacy filing. Missing enumeration triggers Rule 27 audit at Council review.

**Priority:** MEDIUM_HIGH — canonization prevents category-slippage recurrence in future architectural extensions

**Impact if ratified:** Rule 27 body becomes self-verifying (any candidacy must enumerate channels); Item 156's K=5/N=8 → K=5/N=5 (100%) after validity-hypothesis reclassification (already applied in Item 156 spec correction per Council #10 close-out); future Council candidacies inherit the discipline

**K=2 quorum requirement:** substrate cross-check on the canonical amendment language

---

## Item 161 — Rule 20 extension: agenda-vs-spec compression discipline

**Origin:** Opus Substrate B (Council #10) N-4 finding: Item 156's spec (file 02) markedly more rigorous than agenda (file 00). Agenda drops caveats spec carries (Klein 2022 flag §8.1.6, MS SPECULATIVE §8.1.5, N-Sim tick-loop dependency §8.2.7). 2 of Grok's 5 material findings (TMT-stale + tick-loop) were ALREADY IN SPEC — only novel relative to agenda. Consumer adjudicating off agenda alone over-rates confidence + mis-specifies provisional subset.

**Framework methodology issue:** When compressed surface (agenda) routes to ratification consumers (substrates, operators, future Councils), the compressed version smooths uncertainty the full version documents. This is a systematic write-side/read-side drift.

**Two disposition paths:**

**Option (a):** Rule 20 extension mandating consumer-side caveat re-attachment when compressed surface routes to ratification consumers. Consumers (substrates + operators + future CCs) must load spec caveats before adjudicating from agenda.

**Option (b):** Reconciliation of compressed surface up to spec's caveat level at filing time. Agenda MUST carry all SPECULATIVE-EXTRAPOLATION + CALIBRATION-CHOICE + CONTESTED + REJECT-STALE flags from the underlying spec.

**Option (c):** Hybrid — route spec (not agenda) to ratification consumers by default; keep agenda as index only.

**Priority:** MEDIUM — prevents Council #10-style discovery of agenda-vs-spec drift at substrate-deployment cost

**Impact if ratified:** substrate deployments after Council #11 receive spec-level rigor; reduces Rule 25 pre-flight substrate deployment cost by not re-surfacing caveats already in spec

**Ratification signal:** Option (c) hybrid may be cheapest — instruct substrate deploy kits to attach spec (not agenda) as primary evidence, retain agenda as index; agenda-only consumers get warning banner

---

## Item 162 — Rule 28 enforcement pattern for architectural extensions

**Origin:** Opus Substrate B (Council #10) N-6 finding: Item 156 endorses Rule 28 conceptually + explicit per-layer example (§4.1 "spread ...topology before overrides") but does NOT enumerate reducer paths OR per-field preservation tests OR grep audit for 9 new nested layers (Beta params, Axelrod F=8×q=5 vector, 4-needs, SNI 4-factor, etc.). Compliance DEFERRED to implementation. Item 154 defect-of-record is the exact silent-field-nuke bug this multiplies ~9×.

**Proposed Rule 28 amendment:** formalize enforcement pattern for architectural extensions adding N nested state fields:

1. **Design-time enumeration mandate:** candidacy filing must enumerate reducer paths per new nested layer + per-field preservation regression test coverage. Missing enumeration triggers pre-substrate-review return.

2. **Ship gate:** Rule 28 compliance is PR-blocking. Ship not allowed without:
   - `npm run audit-reducers` clean pass (catches fully-listed nested-state rebuilds missing ...spread)
   - Per-field preservation regression test per new nested field per reducer path (≥1000-iter for hot-path reducers per pairFieldPreservation.test.ts precedent)
   - Reducer-audit grep clean across all N layers
   - `normalizeWorldState()` load-time backfill covers all new fields

3. **Post-ship audit:** for the next 3 substrate ships adding fields, audit-fire count feeds Rule 28's own validation. If audit fires ≥1 per ship, upgrade to DEFLATE candidacy at next Council.

**Priority:** MEDIUM — Item 156 Tier 10 substrate implementation is the immediate test case; formalizing enforcement pattern now prevents Item 154-scale defects during 9-layer expansion

**Impact if ratified:** Rule 28 becomes self-enforcing; substrate ships with new nested fields must pass gate BEFORE landing PR; framework empirical validation of Rule 28 mandate #2 built into implementation cadence

**Cross-refs:**
- Item 154 (Rule 28 origin — defensive-reducer discipline canonization)
- Item 155 (post-mortem harness — provides infrastructure for Rule 28 audit)
- Item 156 Council #10 hard gate 3 (this enforcement pattern as Tier 10 ship gate)

---

## Item 163 — Rule 19 EMPIRICAL-TRANSLATION new flag class

**Origin:** Opus Substrate B (Council #10) N-7 finding + K=3 substrate quorum resolution on Holt-Lunstad divergence: converting OR (odds ratio, dichotomous) to per-tick continuous hazard multiplier is a MODELING ASSUMPTION not a source-reported quantity. Grok said "INVALID EXTRAPOLATION"; Opus said "standard endpoint-calibrated Cox hazard form is defensible continuous extension"; Perplexity Depth-0 said "modeling assumption not source-reported." Convergence: form is defensible; needs explicit flag beyond existing SPECULATIVE-EXTRAPOLATION + CALIBRATION-CHOICE + CONTESTED + REJECT-STALE + UNVERIFIED categories.

**Proposed Rule 19 new flag class:**

**EMPIRICAL-TRANSLATION** — covers:
- OR → per-tick hazard multiplier translations (e.g. Holt-Lunstad)
- Dichotomous → continuous mappings (e.g. rescue-choice binary → softmax over 4 options with weighted modulators)
- Ratio → per-tick rate mappings (e.g. RR → per-tick mortality)
- Cross-sectional → longitudinal-per-tick mappings (e.g. cross-sectional survey → per-tick affect trajectory)
- Group-level → agent-level mappings (e.g. population-mean effect → per-Sim modulator)

**Distinguishing features from existing flags:**
- vs SPECULATIVE-EXTRAPOLATION: EMPIRICAL-TRANSLATION covers modeling FORM (Cox hazard is defensible); SPECULATIVE-EXTRAPOLATION covers CONSTRUCT extension (mapping a construct to a domain it wasn't tested in)
- vs CALIBRATION-CHOICE: EMPIRICAL-TRANSLATION covers the TRANSLATION method; CALIBRATION-CHOICE covers specific designer-set numeric values
- vs CONTESTED: EMPIRICAL-TRANSLATION is not about replication status; CONTESTED is about literature disagreement on effect existence/magnitude
- vs REJECT-STALE: EMPIRICAL-TRANSLATION preserves the underlying finding as valid; REJECT-STALE indicates the finding itself doesn't replicate

**Usage examples:**
- Holt-Lunstad OR=1.50 → ln(1.50)=0.405 β for hazard_multiplier = exp(-β·SNI): EMPIRICAL-TRANSLATION flag (form defensible; magnitude needs deflation for OR-vs-HR common-outcome bias OR timescale calibration)
- Rescue-choice softmax coefficient extraction from Levine 2002 qualitative-experimental paper: BOTH EMPIRICAL-TRANSLATION (quantitative extraction from qualitative source) AND CALIBRATION-CHOICE (specific numeric value)
- Bar-Haim 2007 threat-attention meta-analysis d=0.45 (group-level) → per-Sim modulator (agent-level): EMPIRICAL-TRANSLATION (group→agent) flag

**Priority:** MEDIUM — enables precise flagging of the ~40+ CALIBRATION-CHOICE constants in Phase 1 roadmap mechanisms + prevents future Council substrate deployments from surfacing "modeling assumption" concerns as novel findings

**Impact if ratified:** Rule 19 flag taxonomy becomes more precise; substrate deployments can pre-flag EMPIRICAL-TRANSLATION items at candidacy filing time; framework's Rule 22 (verify-against-canonical) can extend to include EMPIRICAL-TRANSLATION method verification

**Ratification signal expected:** RATIFY — Council #10 K=3 quorum on Holt-Lunstad already demonstrates the flag class is needed

---

---

## Item 164 — Rescue-arrival probability + signal_for_rescue frequency calibration sweep

**Origin:** F2 dominancePrestigeDualHierarchy ship 2026-07-11 late evening — `npm run postmortem` seed-42 3000-tick session surfaced anomaly:

> **tick 6000** [`signal_for_rescue_without_rescue_outcome`] — Sim B fired signal_for_rescue 810 times with no rescue outcome. Rescue-arrival probability calibration + location bias worth reviewing.

Postmortem verdict: `Field-nuke suspected: false` (Rule 28 not violated). Anomaly is PREEXISTING calibration concern surfaced during F2 ship gate verification, NOT caused by F2 (which is a new module not yet wired into tickIslandWorld action loop per roadmap Phase 1 dependency ordering).

**Scope:**
- Investigate rescue-arrival probability per tick under signal_for_rescue action
- Location-bias analysis: does signal_for_rescue at certain positions have systematically lower rescue-arrival probability?
- Signal-decay analysis: does signal effectiveness decay after N consecutive signal fires?
- 5-seed variance analysis to confirm calibration issue not a seed-42-specific artifact

**Anchor context:** Stage 3.8 M1-M12 rescue-choice architecture ships assumed baseline rescue-arrival probability calibrated at implementation time; postmortem surfacing suggests re-calibration may be needed. This composes with Item 162 Rule 28 enforcement pattern — postmortem discipline (existing Item 155 mandate) catches these calibration drifts, but the fix pathway (revise magic-number rescue probabilities) is separate.

**Priority:** MEDIUM — not ship-blocking (F2 doesn't touch rescue mechanics; anomaly predates F2); should be resolved before Phase 1 mechanism F4 gossipSemantics ships if F4 wires into rescue-choice modulator (which it might via Sommerfeld 2007 reputation-noise for third-party observers).

**Method:**
- Extract rescue-arrival probability distribution across last 5 stage-3-8 empirical harness runs
- Run `npm run postmortem -- --ticks 11000` at 5 seeds (42, 100, 200, 300, 400)
- Compare signal_for_rescue → rescue-arrival rates across seeds
- If calibration adjustment needed, adjust rescue-arrival probability constants in islandWorld.ts + re-run harness

**Ratification signal:** RATIFY at Council #11 with calibration sweep results attached; framework's rescue-arrival probability becomes primary-anchor-informed rather than designer-set-only.

---

## Cross-item composition + dependency graph

```
Item 158 (framework citation audit) ─┬─ enables Items 159 + 160 substrate cross-checks
                                     └─ substrate role: Perplexity/ChatGPT DR verification

Item 159 (Post 0146 re-attribution) ─── depends on Item 158 audit for full-corpus scope
                                       (or can proceed standalone with grep-scope)

Item 160 (Rule 27 clarification)  ──── independent; canonical amendment

Item 161 (Rule 20 extension)      ──── independent; canonical amendment

Item 162 (Rule 28 enforcement)    ──── Item 156 Tier 10 implementation is immediate test case;
                                       Rule 28 body amendment

Item 163 (Rule 19 EMPIRICAL-TRANSLATION) ── enables N-2 through N-20 corrections to be
                                            re-labeled with precise flag; Rule 19 body amendment
```

## Substrate deployment strategy for Council #11

**Recommended:** K=3 (Grok + Opus + Perplexity) per Council #10 empirical vindication. ChatGPT DR skip unless a specific item benefits.

**Substrate role emphasis:**
- **Grok DeepSearch:** adversarial-skepticism on framework-wide corrections (does the citation drift really exist? Are the proposed corrections themselves correct?)
- **Claude Opus ET:** consistency check on Rule 19/20/27/28 amendments (do the amendments preserve internal consistency across canonical rules?)
- **Perplexity Computer (byte-verification):** primary-source verification of Items 158 + 159 corrections at Depth-0

**Aggregate close-out target:** produce framework-wide corrections + amendment texts for Rules 19/20/27/28 ready for operator ratification at Council #11 close.

## Items NOT filed as Council #11 candidacies (retained CC framing scope only)

- **Opus N-8** ("Fire #11" conflation in CC framing prompt): CC framing discipline note only; Item 156 itself is clean; no Council candidacy needed.
- **Opus N-9** ("Rule 19 = Fable-5-audit precedent" shorthand): CC framing discipline note only; refer to Rule 19 by canonical name Marcus Reed Protocol when precision matters.
- **Opus N-1 self-retraction** (Rule 25 spoofability novelty claim): substrate self-discipline example; canonical Rule 25 already documents self-attestation unenforceable; no candidacy pathway.

## Ratification tracking

**Status:** ALL 6 items filed for Council #11 review at Council #10 close 2026-07-11.

**Operator ratification signature at Council #11 close:** to be filled September 2026 or accelerated per operator judgment.

**Council #11 accelerated close pathway:** if operator wants same-session ratification (Council #10 precedent), K=3 substrate deployment + aggregate close-out could complete in 4-6hr session.

END OF COUNCIL #11 CANDIDACY FILINGS.
