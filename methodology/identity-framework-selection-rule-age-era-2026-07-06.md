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
