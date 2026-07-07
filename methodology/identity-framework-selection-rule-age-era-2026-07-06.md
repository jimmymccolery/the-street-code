---
title: Identity-Framework-Selection Rule — Age × Era
version: 1.0
status: RATIFIED
ratified: 2026-07-06
ratification_pathway: operator-delegated CC ratification per Marcus Reed Surface 8 §4 audit OJ-1 resolution
supersedes: none (new methodology decision)
scope: BiographicalRecord.extendedTemplate.identityStage population for civil-rights-framework-applicable anchors
council_9_review_agenda_item: 20 (see council-9-review-agenda-draft-2026-07-05.md)
---

# Identity-Framework-Selection Rule — Age × Era

## Empirical trigger

Marcus Reed Surface 8 §4 retrospective canon audit for Marvin Okafor (Claude Opus
Extended Thinking, 2026-07-06) raised Surface 2 cross-anchor-coherence FLAG:

> "Grok and Perplexity use Cross Nigrescence as the primary identity frame; Opus and
> ChatGPT argue Cross is anachronistic for a 1944 child (its Immersion/Internalization
> stages presuppose a late-1960s Black-consciousness movement; validated on young
> adults) and use MMRI (Sellers 1998) + racial-socialization (Boykin & Toms; Hughes
> et al.) instead. If Cesar and Yuki are then analyzed under whichever framework
> their substrate happens to reach for, the three 'sibling instances' will carry
> inconsistent identity frameworks."

Without a canonical selection rule, each anchor's substrate research would inherit a
different identity framework based on substrate happenstance rather than principled
match between framework applicability window and anchor age × era.

## The rule

**For each civil-rights-framework-applicable anchor, the identity-development framework
applied to `IdentityStageMarker.frameworkCitation` and (optionally)
`IdentityStageMarker.dimensionalPosition` is selected by the anchor's age × era at the
canonical simulation-window date, NOT by substrate-preference.**

### Framework selection by anchor axis

| Framework | Anchor axis (applicability window) | Rationale |
|---|---|---|
| **Cross 1971 / 1991 Nigrescence + CRIS** | Late-adolescent through adult (16+), post-1968 Black-consciousness movement OR retrospective adult Black-identity narrative | Cross's Pre-Encounter → Encounter → Immersion-Emersion → Internalization → Internalization-Commitment stages presuppose the late-1960s Black-consciousness movement. CRIS revision (Cross & Vandiver 2001) validated on young-adult samples. Applying to a pre-1968 child produces anachronism. |
| **MMRI (Sellers 1998) + racial-socialization (Boykin & Toms 1985; Hughes et al. 2006)** | Pre-1968 children AND cases where dimensional-position better fits than stage progression | MMRI is dimensional (centrality + regard + ideology) not stage-based; racial-socialization is process-oriented (transmission events from parents to child). Both fit developmental context of a Black child in pre-Civil-Rights-Movement era without importing 1960s-consciousness anachronism. |
| **Phinney MEIM 1992 + revised MEIM-R (2007)** | Adolescent-to-emerging-adult (13-25) ethnic-identity in multi-ethnic contexts; not exclusive to Black-American frame | Phinney's ethnic-identity model applies across ethnic groups; instrument-driven. Applies to Latinx and Asian-American anchors where MMRI is Black-specific. Cesar de la Rosa (1970s San Antonio adolescent) primary candidate. |
| **Nagata 2015 transgenerational trauma + gaman-endurance frame** | Japanese-American post-Manzanar / concentration-camp descendants | Nagata's transgenerational Japanese-American incarceration research + gaman cultural-endurance frame. Yuki Tanaka (1946 post-Manzanar child) primary candidate. Alternative to MMRI/Phinney for JA-specific developmental context. |
| **Cass 1979 sexual-identity stages OR later modifiers (Savin-Williams 2010+)** | Sexual-orientation identity progression post-liberation era; NEVER applied to minors | Existing three-layer orientation R11 spec at biographicalRecord.ts already carries this axis; Cass 1979 is stage-based, ordinal. Do not populate for minors — encode via `sexualOrientationLocked` LockedProtectedField instead per child-safety discipline. |

### Applied to current + upcoming anchors

- **Marvin Okafor** (1944, 12yo, Black-American Philadelphia): **MMRI + racial-socialization** (pre-1968 child; Cross anachronistic). Populated 2026-07-06 per this rule.
- **Cesar de la Rosa** (1975 Item 1137 context, adolescent, Tejano San Antonio): **Phinney MEIM + Latinx cultural-identity scholarship** at Cesar audit round. NOT MMRI (Black-specific). NOT Cross (Nigrescence Black-specific).
- **Yuki Tanaka** (1946 post-Manzanar Item 1139 context, child, Japanese-American): **Nagata transgenerational trauma + gaman-endurance frame + racial-socialization**. NOT Cross. NOT MMRI (Black-specific).
- **Walt Petersen** (Item 1138, Danish-American Iowa farm kid): NO civil-rights framework applicable per Item 1138 metadata (`civil_rights_framework_applicable: false`). This rule does not apply.

## Enforcement mechanism

1. **Schema:** `IdentityStageMarker.frameworkType?: 'stage' | 'dimensional'` extension shipped 2026-07-06 (biographicalRecord.ts). Populated when framework is dimensional (MMRI, Phinney dimensional axis, racial-socialization process-oriented).
2. **Regression test:** `marvinPhase71fSchemaPopulation.test.ts` asserts `frameworkCitation` contains 'MMRI' + 'Sellers 1998' + 'racial-socialization' AND does NOT contain 'Cross 1971' or 'Nigrescence' for Marvin. Sibling tests will ship at Cesar + Yuki audit rounds.
3. **Substrate deployment:** Phase 7.1f substrate research prompts for future civil-rights-framework-applicable anchors will name the required framework family per this rule, gating substrate framework-selection freedom.

## Council #9 review agenda item

Filed as Item 20 candidate methodology observation at
`~/Projects/the-street-code/methodology/council-9-review-agenda-draft-2026-07-05.md`.
Review question: after n=1 fire (Marvin) + n=2 anchor rounds (Cesar + Yuki),
whether this rule warrants canonization to Rule 26 promotion tier OR remains a
methodology-observation candidate.

## Rule 19 anti-fabrication compliance

This rule is METHODOLOGY selection, NOT protected-class content. Substrate-training-
knowledge concerns do not apply: the rule is about which established academic
framework to apply, and framework applicability windows are documented in the
foundational sources (Cross 1971 introduction; Sellers 1998 MMRI validation
paper; Phinney 1992 MEIM development paper; Nagata 2015 review). Rule 19 discipline
around substrate-generated protected-class *content* is preserved by continuing to
require Phase 7.1f substrate-triangulation pathway for the dimensional-position
population itself.

---

## Rule 24 correction addendum — 2026-07-06 evening (Cesar arc empirical validation)

**Discipline:** Rule 24 addendum-preserves-immutability. Rule body above is PRESERVED VERBATIM. Corrections + refinements are appended below.

**Trigger:** Phase 7.1f Cesar de la Rosa substrate-triangulation research 2026-07-06 evening surfaced 2 CC-side errors at this canonical rule file (my Post 0186 authoring) + 1 substantive rule refinement from 3/4 substrate convergence.

### Correction 1 — Cesar example era WRONG (1975/1970s adolescent → 1946 age 11)

**Defect:** Table row at Phinney MEIM framework (§Framework selection by anchor axis) says "Cesar de la Rosa (1970s San Antonio adolescent) primary candidate." Application example (§Applied to current + upcoming anchors) says "Cesar de la Rosa (1975 Item 1137 context, adolescent, Tejano San Antonio)."

**Both are WRONG per source authority.** Item 1137 at `~/Projects/Open Alley/content-kb/personalities/item-1137-cesar-delarosa-1946-pin-boy-san-antonio.md` is authoritatively 1946, age 11 (`personality_id: pp:personality:cesar-delarosa-1946`; `era_active: 1940s`; demographic: "11-year-old Tejano (Mexican-American) boy in San Antonio 1946"). Pin-boy occupation is itself era-anchoring since AMF automatic pinsetters displaced hand-pinsetting c. 1946 debut + commercial mid-1950s.

**Substrate confirmation:** 4/4 substrate convergence on era = 1946 age 11 (Grok silent self-correct + Opus explicit + ChatGPT explicit + Perplexity explicit at top of dossier).

**Corrected framework applicability example (replaces both original references):**
- **Cesar de la Rosa** (1946 Item 1137 context, age 11, rooted-Tejano-not-immigrant San Antonio): **Quintana 1994 + 1998 ethnic-perspective-taking model as PRIMARY + Ruiz 1990 Chicano/Latino Crisis-Resolution shame-axis + Bernal & Knight 1990 childhood ethnic identity components** at Cesar audit round. Phinney MEIM 1990/1992 + MEIM-R 2007 BELOW instrument floor at age 11 (validated on 13+ per Roberts et al. 1999); retained as construct-and-developmental-horizon only. Berry 1997 + Rumbaut 1994 DECLINED as primary on anti-erasure grounds (immigrant frameworks mis-fit rooted-Tejano populations; perpetual-foreigner-erasure risk). Anzaldúa 1987 valid as ETIC analyst lens, anachronistic as EMIC self-understanding for 1946 child. NOT MMRI (Black-specific). NOT Cross (Nigrescence Black-specific).

### Correction 2 — Framework selection table under-specified for age × era × developmental-instrument-floor × group-position stack

**Defect:** Original rule table gates framework selection by anchor axis (age × era) but under-specifies within-framework-family developmental-instrument-floor discipline. For pre-Phinney-instrument-floor Latinx children (age 6-12), the rule as originally stated would select "Phinney MEIM + Latinx cultural-identity scholarship" — which is **partially correct at framework-family scope** but **wrong at specific-framework scope** because Phinney MEIM was validated on 13+ (Roberts et al. 1999 established structure on young adolescents; MEIM-R Phinney & Ong 2007 targets adolescents and young adults; consensus per Rivas-Drake et al. 2014 + Umaña-Taylor et al. 2014 that abstract exploration-driven identity work available in adolescence with formal-operational cognition, not at age 11).

**Substrate confirmation:** 3/4 substrate convergence on refinement (Claude Opus Extended Thinking + ChatGPT Deep Research + Perplexity Comet Fable 5 all independently proposed Quintana + Ruiz + Bernal for age-11 subject). Grok DeepSearch used Phinney MEIM as primary (1/4 outlier; correctly noted anachronism risk but did not substitute).

**Refined framework selection table (extends original table for Latinx pre-adolescent subjects):**

| Framework | Anchor axis (applicability window) | Rationale |
|---|---|---|
| **Quintana 1994 + 1998 ethnic-perspective-taking model** | Latinx children age 6-18 (Level 1 literal ~6-10 → Level 2 social-nonliteral ~10-14 → Level 3 group-consciousness adolescent) | Built on 97 interviews with Mexican-American children/youth ages 6-18. Exact population + age span match for Cesar-type anchors. Nun-slap + sister's exegesis = textbook Level-2 acquisition event. |
| **Ruiz 1990 Chicano/Latino Crisis/Resolution** | Latinx shame-axis sub-framework at any age; Causal stage for pre-adolescent + Cognitive/Consequence/Working-Through/Successful-Resolution for adolescent/adult | Fits nun-slap-vs-family-affirmation tension. Do NOT inflate to Cognitive/Consequence for pre-adolescent — those stages presuppose adolescent identity-work capacity. |
| **Bernal & Knight 1990** | Latinx childhood ethnic identity components (age 6-10 primary; extensible to 11-12 with mature-for-age caveat) | 5 components (self-identification / constancy / knowledge / role behaviors / feelings/preferences) validated on Mexican-American children. Correct schema-population lattice for age-11 Cesar-type anchor. |
| **Phinney MEIM 1990/1992 + Roberts et al. 1999 + MEIM-R 2007** | Adolescent-to-emerging-adult (13-25) ethnic-identity in multi-ethnic contexts | **BELOW instrument floor for pre-adolescent subjects.** Retain as construct-and-developmental-horizon only for age 6-12 anchors. Instrument applicable at Yuki age 16 Item 1139 round. |
| **Anzaldúa 1987 Borderlands consciousness** | ETIC analyst lens only for pre-1987 subjects; EMIC for post-1987 mestiza-consciousness subjects | Nepantla + linguistic terrorism accurately NAME what happens to Cesar-type subjects but are 1987 vocabulary; do NOT project into pre-1987 subject emic self-understanding. |
| **Berry 1997 acculturation + Rumbaut 1994 segmented assimilation** | Immigrant-arrival subjects only | **DECLINED as primary lens for rooted subjects** (Tejano families predating 1848 annexation; Filipino families predating 1898 annexation; etc.). Perpetual-foreigner-erasure risk. Berry admissible only as bidimensional heritage-x-participation descriptive heuristic. |

### Applied to current + upcoming anchors (corrected + refined 2026-07-06 evening)

- **Marvin Okafor** (1944, 12yo, Black-American Philadelphia): **MMRI + racial-socialization** (pre-1968 child; Cross anachronistic). Populated 2026-07-06 per Post 0186 pre-refinement. (Note: 12yo is at boundary of pre-Phinney-instrument-floor + Phinney-adjacent; MMRI + racial-socialization framing at Marvin round remains valid; no re-population required.)
- **Cesar de la Rosa** (1946, age 11, rooted-Tejano San Antonio): **Quintana + Ruiz + Bernal per refined rule 2026-07-06 evening**. Pending Marcus Reed audit round.
- **Yuki Tanaka** (1946, age 16 per Item 1139 demographic, Japanese-American post-Manzanar Chicago): **Nagata 2015 transgenerational trauma + gaman-endurance frame + Phinney MEIM 1990/1992 within instrument floor at 16**. At 16 Yuki IS within Phinney instrument floor; Phinney MEIM applies AS instrument + Nagata + gaman as culturally-specific augmentation. Pending Yuki audit round.
- **Walt Petersen** (Item 1138, Danish-American Iowa farm kid): NO civil-rights framework applicable per Item 1138 metadata (`civil_rights_framework_applicable: false`). This rule does not apply.

### Enforcement mechanism refinement

Regression test at Cesar audit round shipment must assert:
- `frameworkCitation` contains 'Quintana' + '1994' + '1998' + 'Ruiz' + '1990' + 'Bernal'
- `frameworkCitation` does NOT contain 'Phinney' as primary (Phinney permissible only as construct-horizon in parenthetical)
- `frameworkCitation` does NOT contain 'Berry' or 'Rumbaut' (declined on anti-erasure grounds)
- `frameworkCitation` does NOT contain 'Anzaldúa' as emic frame (etic-only lens for 1946 subject)

Substrate deployment prompts for future pre-adolescent Latinx anchors will name Quintana + Ruiz + Bernal per this refined rule, gating substrate framework-selection freedom at deployment-time (per Council #9 Item 28 review question 3).

### Council #9 filing update

Item 28 (age × era framework-selection rule) empirical foundation strengthens from n=1 to n=2 at Cesar arc (both Marvin + Cesar populations comply). Refinement adds within-framework-family developmental-instrument-floor discipline as sub-rule for Latinx pre-adolescent axis. Full strengthening to n=3 pending Yuki audit round. Cross-anchor coherence FLAG at Marcus Reed Surface 8 §4 Marvin round audit resolved via age × era rule; Cesar round Marcus Reed audit pending independent adjudication of refined framework selection.

