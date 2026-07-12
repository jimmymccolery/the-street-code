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

## Item 165 — Phase 1 lifelikeness batch citation-hygiene amendments (63 corrections)

**Origin:** Phase 1 lifelikeness roadmap COMPLETE 2026-07-11 late: 8 mechanisms shipped (F2 dominancePrestigeDualHierarchy + F1 accommodationResponse + F5 forgivenessProcess + D5 moralEmotionsFamily + D3 empathyDualSystem + B2 habitStrength + D4 prolongedGriefTrajectories + F4 gossipSemantics) with 200+ primary-source anchors integrated + Non-Inertness Gate CLEAR 3/3 at 100% + Verdict PASS 5/5 across all 8. Parallel research-agent verification sweeps (dual-agent citation audits per ship in the pattern established at F1) surfaced **63 citation corrections** requiring framework-registry integration. Extends the N-10 through N-20 correction band filed at Council #10 close (Item 158 origin data) into N-21 through N-63 territory.

**Type:** BATCH citation-hygiene amendment (Rule 19 Marcus Reed Protocol anti-fabrication discipline + composes with Council #11 Item 158 framework-wide audit).

**Severity:** HIGH — 63 corrections across 8 Phase 1 mechanisms; 4 phantom citations flagged; 1 REJECT-STALE flag on uniform-decay claim; systematic drift patterns overlap Item 158's initial 4-pattern taxonomy but extend it.

**Preceded by:**
- Council #10 Item 156 8-correction batch integrated at close-out (N-10 through N-20)
- Council #10 close-out amendments (Post 0146 mis-attribution N-2, Rule 27 category-slippage N-3, etc.)

### Rationale

The Phase 1 lifelikeness ship cadence (8 mechanisms in ~24hr session per operator directive) exposed a systematic citation-drift signal at ~7-8 corrections per mechanism ship even after Council #10's tightened Rule 19 discipline. This aligns with Item 158's Perplexity Substrate C hypothesis that framework-wide citation reliability is ~80% baseline. The dual-agent verification pass integrated at each ship is the mechanism producing these findings at ship time rather than deferring to a later audit sweep.

Filing this batch as Item 165 rather than folding into Item 158 preserves:
1. **Attribution to the ship that surfaced each correction** (F2/F1/F5/D5/D3/B2/D4/F4 provenance)
2. **Amendment scope separation** — Item 158 = framework-wide audit method; Item 165 = specific corrections already surfaced needing registry integration
3. **Council #11 disposition granularity** — batch RATIFY on Item 165 corrections independent of Item 158 method ratification

### Corrections by mechanism (63 rows)

| N-XX | Ship | Wrong citation | Correct citation | Severity | Source |
|------|------|---------------|-----------------|----------|--------|
| N-10 | F1 | Kito 2017 | Kito 2005 J Soc Psych 145(2):127-140 | MEDIUM | already Council #10 |
| N-11 | F1 | Sbarra JCCP | Sbarra 2015 Emotion 15(3):387-394 | MEDIUM | already Council #10 |
| N-12 | F1 | Fincham J Family Psych | Fincham 2000 J Soc Clin Psych 19(2):267-285 | MEDIUM | already Council #10 |
| N-13 | F1 | Vangelisti-Sprague | Vangelisti-Crumley 1998 Comm Monographs 65(3):173-196 | MEDIUM | already Council #10 |
| N-14 | F1 | Aung-Puts WIRE | Aung-Puts 2020 Curr Opin Psych 33:118-125 | MEDIUM | already Council #10 |
| N-15 | F1 | Adams 2004 (venue drift) | Adams 2004 JPSP 88(6):948-968 | LOW | already Council #10 |
| N-16 | F5 | Ricciardi 2013 anterior temporal | Ricciardi 2013 SCAN 8(8):839-844 DLPFC+IPL+precuneus | HIGH | Agent B — region mis-attribution |
| N-17 | F5 | Ysseldyk 2007 Basic Applied Soc Psych | Ysseldyk 2007 Personality & Individual Differences | MEDIUM | Agent B |
| N-18 | F5 | Fisher-Exline 2006 J Positive Psych | Fisher-Exline 2006 Self and Identity 5(2):127-146 | MEDIUM | Agent B |
| N-19 | F5 | Wenzel-Okimoto 2012 | Wenzel-Okimoto-Hornsey 2017 | MEDIUM | Agent B — 2012 paper mis-cited |
| N-20 | D5 | Elison 2006 J Family Violence | Elison 2006 SBP 34(2):161-168 | MEDIUM | Agent A+B convergent |
| N-21 | D5 | Stuewig 2015 Aggressive Behavior | Stuewig 2015 Child Psych & Human Dev 46(2):217-227 | MEDIUM | Agent A |
| N-22 | D5 | de Hooge 2007 Emotion | de Hooge 2007 Cognition & Emotion 21(5):1025-1042 | MEDIUM | Agent B |
| N-23 | D5 | Cryder 2012 Emotion | Cryder 2012 PSPB 38(8):1049-1059 | MEDIUM | Agent A |
| N-24 | D5 | Robins-Noftle 2005 | Tangney-Stuewig-Martinez 2014 | MEDIUM | Agent B — anchor superseded |
| N-25 | D5 | Batson-Kennedy-Nord 2007 JPSP | Batson-Kennedy-Nord 2007 EJSP 37(6):1272-1285 | MEDIUM | Agent A |
| N-26 | D5 | Layous 2017 Emotion | Layous 2017 J Positive Psychology 12(4):385-398 | MEDIUM | Agent B |
| N-27 | D3 | Wondra-Ellsworth (venue drift) | Wondra-Ellsworth 2015 Psych Review 122(3):411-428 | MEDIUM | Agent A |
| N-28 | D3 | Smith 2009 Neuropsychology Review | Smith 2009 Psychological Record 59(3):489-510 | MEDIUM | Agent A |
| N-29 | D3 | Roth-Hanania Dev Psych | Roth-Hanania 2011 Infant Behav & Dev 34(3):447-458 | MEDIUM | Agent B |
| N-30 | D3 | Cikara 2014 TICS | Cikara 2014 JESP 55:110-125 | MEDIUM | Agent A |
| N-31 | D3 | Nightingale (partial) | Nightingale 1991 JGIM 6:420-423 PARTIAL | LOW | Agent B — PARTIAL flag |
| N-32 | D3 | Decety-Cowell (full article) | Decety-Cowell 2014 TICS 18(7):337-339 SHORT FORUM | LOW | Agent A — commentary not review |
| N-33 | D3 | Ben-Ami Bartal (byline drift) | Inbal Ben-Ami Bartal-Decety-Mason 2011 Science 334(6061):1427-1430 | MEDIUM | Agent B |
| N-34 | B2 | Dickinson-Balleine 1994 title drift | "Motivational Control of Goal-Directed Action" Anim Learn Behav 22(1):1-18 | MEDIUM | Agent A |
| N-35 | B2 | Gardner 2012 general SRHI review | Gardner 2012 SRBAI-derivation paper IJBNPA 9:102 | MEDIUM | Agent B — SRBAI-specific |
| N-36 | B2 | Schwabe-Wolf 2013 NBR 37(9):1740-1749 | Schwabe-Wolf 2013 Trends in Cog Sci 17(2):60-68 | MEDIUM | Agent A |
| N-37 | B2 | Aarts-Verplanken-van Knippenberg 1998 JEP 18(2) | Aarts 1997 Acta Psychologica 96(1-2):1-14 | MEDIUM | Agent A |
| N-38 | B2 | Robbins-Costa 2017 Neuron 96(5) | Robbins-Costa 2017 Current Biology 27(22):R1200-R1206 | MEDIUM | Agent B |
| N-39 | B2 | Schwabe-Höffken 2013 Neuropsychopharmacology | Schwabe-Höffken 2011 J Neurosci 31(47):17317-17325 | MEDIUM | Agent A |
| N-34-D4 | D4 | Bonanno-Kaltman 2001 Psych Bull 127(1) | Bonanno-Kaltman 2001 Clin Psych Rev 21(5):705-734 | HIGH | Agent A |
| N-35-D4 | D4 | Galatzer-Levy-Bonanno 2012 J Pers Assessment 94 | Galatzer-Levy-Bonanno 2012 Soc Sci Med 74(12):1987-1994 | HIGH | Agent A |
| N-36-D4 | D4 | Bonanno-Boerner 2007 Death Studies | Bonanno-Boerner 2007 JAMA letter 297(24):2693 | HIGH | Agent A |
| N-37-D4 | D4 | Wayment-Vierthaler 2002 Death Studies 26(2) | Wayment-Vierthaler 2002 J Loss & Trauma 7(2):129-149 | HIGH | Agent A |
| N-38-D4 | D4 | Anusic-Lucas 2014 EJP 28(6) | Anusic-Lucas 2014 J Personality 82(5):367-378 | HIGH | Agent A |
| N-39-D4 | D4 | Utz-Reidy 2004 J Gerontology 59B | Utz-Reidy 2004 J Family Issues 25(5):683-712 | MEDIUM | Agent A |
| N-40-D4 | D4 | Bratt 2017 author list ambiguous | Bratt-Stenström-Rennemark 2017 Aging & Mental Health 21(6):602-608 | LOW | Agent A |
| N-41-D4 | D4 | Currier-Holland-Neimeyer 2006 JCP 62(10):1327 | Currier-Holland-Neimeyer 2006 Death Studies 30(5):403-428 | HIGH | Agent B |
| N-42-D4 | D4 | Kersting 2009 JAD 121(1-2):13 | Kersting 2009 Am J Psychiatry 166(12):1402-1410 | HIGH | Agent B |
| N-43-D4 | D4 | O'Connor 2019 Psych Bulletin | O'Connor 2019 Psychosomatic Medicine 81(8):731-738 | HIGH | Agent B |
| N-44-D4 | D4 | Field-Sundin 2001 parental death | Field-Sundin 2001 CONJUGAL bereavement JSPR 18(3):347-361 | MEDIUM | Agent B — sample-desc |
| N-45-D4 | D4 | Meier-Carr-Currier-Neimeyer 2013 Death Studies 37 | Meier 2013 J Soc Clin Psych 32(3):315-334 | HIGH | Agent B |
| N-46-D4 | D4 | Simon-Shear 2007 Comprehensive Psychiatry 48(5) | Simon-Shear 2008 Psychiatry Research 159(1-2):31-36 | HIGH | Agent B |
| N-47-D4 | D4 | Bennett-Vidal-Bornstein 2005 Death Studies | PHANTOM; use Bennett-Hughes-Smith 2005 OMEGA 51(1):33-52 | HIGH | Agent B — PHANTOM |
| N-48 | F4 | Dores Cruz 2021 PSPS 16(2); Van Kleef+Balliet authors | Dores Cruz-Nieper-Testori-Martinescu-Beersma 2021 G&OM 46(2):252-285 | HIGH | Agent A — journal+authors |
| N-49 | F4 | Wu 2016 srep 5:18102 (pet-dogs paper) | Wu-Balliet-Van Lange 2016 srep 6:23919 | HIGH | Agent A — PHANTOM/mis-attribute |
| N-50 | F4 | Beersma-Van Kleef 2011 PSPB 37(11):1499-1503 | Beersma-Van Kleef 2011 SPPS 2(6):642-649 | HIGH | Agent A |
| N-51 | F4 | Dores Cruz 2019 EJSP | Dores Cruz 2019 Frontiers Psychology 10:1190 | MEDIUM | Agent A |
| N-52 | F4 | Hess-Hagen 2006 (conflated single paper) | TWO papers: EHB 27(3):231-245 aggression + Human Nature 17(3):337-354 gossip veracity | HIGH | Agent A+B — conflation |
| N-53 | F4 | Waddington 2005 ERRJ 17(4) | Waddington 2005 JOOP 78(2):221-236 | MEDIUM | Agent A |
| N-54 | F4 | Wu-Balliet-Van Lange 2015 NHB/ERSP | Wu 2015 Evolution and Human Behavior 37(3):193-201 | MEDIUM | Agent A |
| N-55 | F4 | Peters-Kashima 2007 AJP 59(3):167-172 | Peters-Kashima 2007 JPSP 93(5):780-797 | HIGH | Agent B |
| N-56 | F4 | Peters-Kashima 2015 JLSP 34(3):274-283 | Peters-Kashima 2015 EJSP 45(6):784-798 | MEDIUM | Agent B |
| N-57 | F4 | Grosser 2010 Personnel Psychology; Kilduff coauthor | Grosser-Lopez-Kidwell-Labianca 2010 G&OM 35(2):177-212 | HIGH | Agent B |
| N-58 | F4 | Grosser 2012 gossip triads GOM 37(4):429 | UNVERIFIED PHANTOM; alt: Grosser 2012 Organizational Dynamics 41(1):52-61 | HIGH | Agent B — PHANTOM |
| N-59 | F4 | Fine 1977 Man 12(3-4):451-465 | Fine 1977 J Communication 27(1):181-185 | MEDIUM | Agent B |
| N-60 | F4 | Waddington-Fletcher 2005 ERRJ | Waddington-Fletcher 2005 J Health Org Mgmt 19(4-5):378-394 | MEDIUM | Agent B |
| N-61 | F4 | Kuo-Chang-Quinton 2015 J Business Ethics 129(3):591 | Kuo-Chang 2015 Int J HRM 26(18):2288-2307 | MEDIUM | Agent B |
| N-62 | F4 | Redhead-Dunbar 2013 Evolutionary Psychology 11(1):102-113 | UNVERIFIED PHANTOM; DROP; use Dunbar 1997+2004 instead | HIGH | Agent B — PHANTOM |
| N-63 | F4 | Turner 2003 Communication Studies | Turner 2003 Communication Monographs 70(2):129-141 | LOW | Agent B |

**Note on numbering:** D4 corrections were internally numbered N-34 through N-47 during D4 ship notes (labeled as `N-34-D4` etc. above to disambiguate from B2's N-34-N-39). Council #11 verification substrate should treat the 63 corrections as a single flat sequence for RATIFY disposition; the internal per-ship numbering preserves provenance.

### Phantom citations (recommend DROP + substitute)

Four phantom citations surfaced. Each was searched exhaustively (Google Scholar + JSTOR + PubMed + publisher DOI resolvers + author-page verification); none resolves to a real paper matching the cited claim:

1. **Redhead-Dunbar 2013 Evolutionary Psychology 11(1):102-113** — extensive search failed to locate. **Recommend DROP; substitute with Dunbar-Marriott-Duncan 1997 Human Nature 8(3):231-246 + Dunbar 2004 RGP 8(2):100-110.**

2. **Grosser-Lopez-Kilduff-Wu-Cronin 2012 GOM 37(4):429-471 "gossip triads"** — no such paper found. **Recommend DROP; substitute with Grosser-Lopez-Kidwell-Labianca 2010 GOM 35(2):177-212** OR Grosser 2012 Organizational Dynamics 41(1):52-61 pending verification.

3. **Bennett-Vidal-Bornstein 2005 Death Studies** — recommend REJECT-STALE. **Substitute: Bennett-Hughes-Smith 2005 OMEGA 51(1):33-52** OR **Bennett-Smith-Hughes 2005 Aging & Mental Health 9(4):348-353**.

4. **Wu-Balliet-Van Lange 2015 Sci Reports 5:18102** — is actually a pet-dogs paper, not the cited cooperation-under-reputation claim. **Correct anchor: Wu 2016 Scientific Reports 6:23919** (gossip-reputation cooperation paradigm).

### REJECT-STALE flag

- **Kashima 2000 PSPB 26(5):594-604 uniform-40%-decay-per-stage claim:** actual mechanism reported in the paper is CONTENT-SELECTIVE bivariate (~10% consistent-with-stereotype content retention / ~30% inconsistent-with-stereotype content decay). Substrate calibrations should NOT anchor to "uniform 40% decay per transmission stage." Framework F4 gossipSemantics ship's decay function must be revised to content-selective bivariate form OR flagged with EMPIRICAL-TRANSLATION (per Council #11 Item 163) if the uniform-decay approximation is retained as a modeling choice. **Recommend REJECT-STALE on the uniform-decay reading.**

### Additional NEW anchors surfaced during research (registry integration candidates)

Research sweeps surfaced 6 primary-source anchors NOT previously in the framework registry. Candidate additions for future ship anchoring rather than corrections:

- **Dores Cruz 2021 Phil Trans B 376:20200301** — tripartite gossip valence distribution 35.9% neg / 32.6% pos / 31.5% neutral; anchor for F4 gossip-valence baseline
- **Dores Cruz 2019 Frontiers in Psychology 10:1190** — 5th gossip motive EMOTION_VENTING beyond the 4-motive Beersma-Van Kleef 2012 taxonomy
- **McCloskey-Johnson 2021 Personality & Individual Differences 181:111000** — HEXACO C × habit content-conditional interaction (β=-0.06 risky habits; β=+0.20 protective habits); anchor for B2 habitStrength cross-trait moderator
- **Van Ast 2023 Neurobiology of Stress + PLOS One 2024** — preregistered null replications of Schwabe-Wolf 2009 stress → habit shift; B2 habitStrength stress-modulator; flag existing Schwabe-Wolf 2009 anchor as CONTESTED
- **Turner-Mazur-Wendel-Winslow 2003 Communication Monographs 70(2):129-141** — relational-ruin restraint on same-friend gossip; F4 gossip-target-selection anchor
- **Meier-Carr-Currier-Neimeyer 2013 J Soc Clin Psych 32(3):315-334** — rumination as mediator between anxious attachment and complicated grief; D4 attachment-pathway anchor

### Proposed disposition

**RATIFY** the 63-correction batch as framework-registry amendments at Council #11 close. Batch composition:

- **60 registry-update corrections** (N-10 through N-63)
- **4 phantom-DROP corrections** with substitute anchors where load-bearing
- **1 REJECT-STALE flag** on Kashima 2000 uniform-decay claim
- **6 NEW anchor registrations** for framework registry future-ship use

### Method for Council #11 verification

1. **Substrate byte-level verification:** deploy Perplexity Computer (or ChatGPT DR) with citation-verification role on the 63-row correction table. Follows Council #10 Substrate C precedent (Perplexity produced N-10 through N-20 at Council #10 close).
2. **K=2 quorum:** any correction with framework-wide grep-impact requires K=2 substrate verification before framework-wide application (per Item 158 method).
3. **Phantom citation DROP:** must be K=2 verified as unlocatable; not just "not found by one substrate."
4. **REJECT-STALE Kashima:** requires primary-source page-scan verification of the actual reported mechanism (content-selective bivariate).

### Composes with

- **Item 158** (framework-wide citation hygiene audit) — Item 165 is a specific 63-correction batch feeding into the Item 158 method's scope
- **Item 159** (Post 0146 ±30% coupling bound framework-wide re-attribution) — same class of citation-drift concern at different scope
- **Item 163** (Rule 19 EMPIRICAL-TRANSLATION flag) — Kashima 2000 uniform-decay if retained would be EMPIRICAL-TRANSLATION flag candidate

### Priority

**HIGH** — 63-correction backlog blocks clean citation-registry export until integrated. Deferral to Council #12 (November nominal window) risks additional Phase 2 ship citations compounding on top of the uncorrected Phase 1 batch. Accelerated-close at Council #11 recommended.

### Ratification signal expected

**RATIFY (batch)** — corrections are all specific + verifiable + accompanied by Agent A/Agent B provenance; phantom flags are exhaustively-searched; REJECT-STALE flag has clear alternative mechanism specified. Batch ratification pattern precedent: Council #10 Item 156 N-10 through N-20 8-correction batch RATIFY.

### Cross-refs

- Council #10 Item 156 close-out (N-10 through N-20 precedent + Council #10 close-out amendments)
- Council #11 Item 158 (framework-wide citation hygiene audit; Item 165 is a scoped batch feeding into Item 158 method)
- Council #11 Item 159 (Post 0146 re-attribution)
- Council #11 Item 163 (Rule 19 EMPIRICAL-TRANSLATION)
- 8 Phase 1 ship postmortems at `~/Projects/sim-ai/` commits F2 `9c96ae1` · F1 `1409a34` · F5 `b0481bb` · D5 `aac3eb6` · D3 `37f8b64` · B2 `49940e3` · D4 `ef1f7f3` · F4 `a0c0391`

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

Item 165 (Phase 1 batch citation corrections) ── scoped subset of Item 158 method;
                                                  K=2 substrate verification on 63-row table;
                                                  4 phantom-DROP + 1 REJECT-STALE (Kashima 2000)
                                                  + 6 NEW anchors for registry integration
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

**Status:** ALL 8 items filed for Council #11 review at Council #10 close 2026-07-11 (Items 158-164 filed at Council #10 close; Item 165 filed 2026-07-11 late post-Phase-1 lifelikeness completion).

**Operator ratification signature at Council #11 close:** to be filled September 2026 or accelerated per operator judgment.

**Council #11 accelerated close pathway:** if operator wants same-session ratification (Council #10 precedent), K=3 substrate deployment + aggregate close-out could complete in 4-6hr session.

END OF COUNCIL #11 CANDIDACY FILINGS.
