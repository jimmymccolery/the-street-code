<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0194
title: When the Vendor-Sync Reminder Hook Captured Safety Without Losing Control By Automating the Reminder Not the Action
date_published: 2026-07-07
status: published
superseded_by: none
domain: methodology-discipline cross-repo-propagation operational-discipline-canonization local-only-repo-blocks-git-submodule
project_scopes: sim-ai companion-product-workspace primary-backend-project the-street-code cross-cutting
cc_task_relevance: vendor-sync-post-commit-hook cross-repo-propagation-discipline option-d-reminder-hook local-only-repo-blocks-git-submodule automate-reminder-not-action operator-control-preservation
phase_binding: 2026-07-07-morning-comprehensive-session-arc-option-d-ratification
discipline_family: automate-reminder-not-action operator-control-preservation cross-repo-vendored-content-verification post-commit-hook-discipline-extension
canonical_rule: option-d-vendor-sync-reminder-hook-council-9-item-37-candidacy
load_bearing_claims:
- sim-ai is consumed by two downstream projects via different mechanisms: the primary-backend-project consumes via tsconfig path alias sim-ai/star equals ../sim-ai/src/star (automatic; reads canonical source directly; no vendor sync needed) plus the companion-product-workspace consumes via vendored copy at ~/Projects/roomtolife/vendor/sim-ai/ (companion-product-workspace pushes to github plus Vercel picks up on push; Vercel cannot reach ../sim-ai/ directly)
- Vendor sync from sim-ai canonical to companion-product-workspace vendor copy was manual per companion-product-workspace CLAUDE.md instruction (rsync -a --delete ~/Projects/sim-ai/src/ ~/Projects/roomtolife/vendor/sim-ai/) plus git commit and push at companion-product-workspace; drift risk when operator or CC forgets to sync
- Option A auto-execute post-commit hook would eliminate forgetting but removes deliberate propagation control that was proven useful during Phase 2.9-A Step 2 refactor 2026-07-07 morning (tests plus typecheck at primary-backend-project alias verified BEFORE companion-product-workspace vendor rsync executed)
- Option B git submodule BLOCKED by sim-ai local-only repo discipline per project_local_only_git.md (13 repos local-only by design 2026-05-12; NO REMOTES EVER; submodules require remote); not open for reconsideration unless local-only ratification reversed
- Option C accept manual leaves drift risk that meta-analysis flagged
- Option D reminder hook ratified 2026-07-07 morning: automate the REMINDER not the ACTION; captures safety gain (impossible-to-miss reminder plus copy-pasteable rsync command plus destination commit-message with auto-SHA-substitution) without losing operator control over WHEN to propagate to companion-product-workspace scope
- Filed as Council #9 candidacy Item 37 at agenda; new operational discipline pattern: automate the REMINDER not the ACTION applies to any cross-repo propagation where auto-execute would sacrifice deliberate-control value
applicability_triggers:
- Any cross-repo propagation workflow where downstream consumer requires explicit action (git commit plus push) should consider Option D reminder-hook pattern before Option A auto-execute pattern
- Any repo pair where downstream cannot reach upstream directly (Vercel deploys plus external CI plus cross-network consumer) requires vendor sync or equivalent propagation mechanism
- Any local-only repo (per project_local_only_git.md discipline) cannot use git submodule as propagation mechanism regardless of technical suitability
- Any post-commit hook installation should document Option D vs Option A tradeoff explicitly in installation rationale (safety-vs-control preservation)
- Any Rule 25 substrate-behavior standalone discipline application evaluating cross-substrate propagation timing considerations should reference Option D reminder-hook pattern
mechanism_details:
- Post-commit hook location at ~/Projects/sim-ai/.git/hooks/post-commit (executable) installed via bash scripts/install-hooks.sh (extends prior pre-commit hook installer per Post 0178 discipline)
- Hook output format prints unmissable reminder with (a) header banner plus (b) trigger explanation (if this commit affects companion-product-workspace scope) plus (c) copy-pasteable rsync command plus (d) companion-product-workspace destination commands (cd plus git add plus git commit with auto-SHA-substitution via git -C ~/Projects/sim-ai rev-parse --short HEAD plus git push) plus (e) skip criteria (internal-only refactors plus test-only changes plus docs-only changes plus no exported-API changes at sim-ai/star scope)
- Skip criteria documented at hook body plus sim-ai CLAUDE.md plus companion-product-workspace CLAUDE.md: skip vendor sync when commit is internal-only (no exported-API changes) plus test-only changes plus docs-only changes plus no exported-API changes at sim-ai/star scope
- Execute criteria documented: execute vendor sync when commit affects (a) research surface dashboard section plus (b) Island NPC Test surface at the companion-product-workspace prototype/island-npc-test route plus (c) any exported-API changes at sim-ai/star scope
- Verified live via test commits: initial install test commit d5fb768 fired hook cleanly; Anchor A CulturalContextBundle commit b5686a1 fired hook cleanly with correct SHA substitution; verification empty commit 282826b fired hook cleanly again
- Documentation updates shipped: install-hooks.sh extended with comprehensive rationale header comment (Option D vs A vs B comparison) plus $POST_COMMIT hook installation section; sim-ai CLAUDE.md new "Post-commit vendor-sync reminder hook (installed 2026-07-07 per Option D ratification)" section with rationale plus when-to-execute guidance; companion-product-workspace CLAUDE.md Vendor sync discipline section extended with Option D reminder plus cross-reference to sim-ai CLAUDE.md rationale plus when-to-execute guidance
cross_refs:
- Post 0178 (cross-consumer typecheck as latent bug detection; pre-commit hook discipline installed at sim-ai) -- Post 0194 extends post-commit hook discipline from typecheck-verification scope to vendor-sync-reminder scope
- Post 0183 (Item 0334 comprehensive cleanup discipline) -- Post 0194 skip-criteria discipline honors Item 0334 retirement pattern (internal-only sim-ai refactors do not trigger vendor sync)
- Post 0175 (Council #8 close canonization) -- Post 0194 applies Council #8 operator-delegated CC ratification policy to Option D ratification (four conditions plus reversibility gate)
- Council #9 candidacy item 37 (vendor-sync-reminder-post-commit-discipline) filed at agenda 2026-07-07 morning session close
- Memory: project_option_d_vendor_sync_reminder_hook_ratified_2026-07-07.md
- Memory: project_local_only_git.md (blocks Option B git submodule)
CC-OPTIMIZED-SUMMARY -->

# When the Vendor-Sync Reminder Hook Captured Safety Without Losing Control By Automating the Reminder Not the Action

**Author:** Jimmy McColery
**Date:** 2026-07-07
**Status:** Single-finding operational discipline arc; new pattern with Council #9 review pending

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

Here is the smallest possible operational discipline that came out of yesterday's session and I think it is worth writing about because the underlying principle generalizes.

I have two projects that consume a shared code substrate (`sim-ai`) via two different mechanisms. The primary-backend-project consumes via tsconfig path alias (`sim-ai/*: ["../sim-ai/src/*"]`); the compiler resolves imports directly to canonical source; no sync needed. A companion product workspace consumes via a vendored copy at `roomtolife/vendor/sim-ai/`; the copy has to be updated manually when `sim-ai` ships changes.

The reason for the asymmetry is deployment. The primary-backend-project is a local dev environment; the compiler can reach `../sim-ai/`. The companion product workspace is a Vercel deployment; the build process runs on Vercel infrastructure and cannot reach my local filesystem. The companion product workspace has to have `sim-ai` code committed inside its own repo for Vercel to build.

The sync command is one line: `rsync -a --delete ~/Projects/sim-ai/src/ ~/Projects/roomtolife/vendor/sim-ai/`. Then commit at the companion product workspace, push, Vercel picks up on push, deploy completes.

The problem: I have to remember to run it. When I forget, `roomtolife/vendor/sim-ai/` drifts from canonical `sim-ai`. Vercel deploys stale code. My meta-analysis flagged this as a real gap.

## The four options

Yesterday morning I ran through the standard decision-surface pattern.

Option A: post-commit hook at `sim-ai` that automatically runs the rsync. Pro: I never forget. Con: I lose the ability to test `sim-ai` changes at the primary-backend-project (via the path alias) before propagating to the companion product workspace. Silent auto-execution removes deliberate propagation control.

Option B: make `roomtolife/vendor/sim-ai/` a git submodule pointing at `sim-ai`'s git repo. Pro: canonical Git-native cross-repo dependency pattern. Con: blocked by my local-only repo discipline. `sim-ai` has no remote per `project_local_only_git.md`. Git submodules require a remote. Even without the discipline blocker, submodules have their own workflow overhead (detached HEAD confusion, forgotten `git submodule update`).

Option C: accept manual. Keep the current pattern. Rely on discipline. Con: this is exactly what the meta-analysis just flagged.

Option D: post-commit hook that prints a reminder but does NOT auto-execute. Pro: eliminates forgetting via impossible-to-miss reminder. Pro: preserves my control over WHEN vendor updates. Con: still requires me to actively run the command when relevant.

I ratified Option D.

## Why Option D and not Option A

The direct decision was for control preservation. But there is a deeper reason that came out of the same morning's work.

Same session, I ran the Sim AI Scene abstraction refactor (Phase 2.9-A Step 2). That refactor physically moved sixty-five files from `worlds/island` to `scenes/island` at `sim-ai`, plus another five files from `worlds/bowling-alley` to `scenes/bowling-alley`. It updated fifteen to twenty import statements across three projects (`sim-ai` internal plus primary-backend-project consumer files plus companion-product-workspace legacy `@/lib/sim-ai` references).

The right execution order was: (1) run tests at `sim-ai` after physical moves; (2) update imports at `sim-ai` internal files; (3) run tests at `sim-ai` again; (4) update imports at primary-backend-project consumer files; (5) run tests at the primary-backend-project; (6) run typecheck at the primary-backend-project; (7) execute vendor sync from `sim-ai` to the companion product workspace; (8) update legacy `src/lib/sim-ai/worlds/island` to `scenes/island` at the companion product workspace; (9) update import statements at the companion product workspace; (10) run typecheck at the companion product workspace.

Steps 1 through 6 verified sim-ai canonical plus the primary-backend-project consumer via the path alias. Steps 7 through 10 propagated to the companion product workspace. If I had auto-rsync at post-commit under Option A, step 7 would have fired between step 4 (sim-ai internal import updates committed) and step 5 (primary-backend-project tests). The companion product workspace's vendor copy would have been synchronized to a pre-verification `sim-ai` state. If step 5 or 6 had surfaced an error, I would have had to either revert the vendor sync at the companion product workspace (extra work) or leave the companion product workspace pointing at broken code temporarily (drift risk).

Under Option D, the reminder hook fired at step 4 commit, told me "vendor sync required if this commit affects companion-product-workspace scope," and stopped. I proceeded with steps 5 and 6 to verify at the primary-backend-project alias scope. Then I executed the rsync manually at step 7 with confidence that the canonical state was verified.

That control preservation was valuable exactly because I was doing a refactor that touched sixty-five files. The larger the change, the more valuable the "test at path-alias consumer before propagating to vendor consumer" workflow becomes.

## Why Option B is genuinely blocked

I want to be explicit that Option B is not just inconvenient. It is structurally blocked by a prior ratification.

`sim-ai` is a local-only repo. Per `project_local_only_git.md` memory (adopted 2026-05-12), thirteen repos in my personal infrastructure are local-only by design. No remotes ever. No `git push`. Five-layer defense against accidental publish (raw `.git/hooks` plus lint-staged plus vitest related plus `npm run ci` plus per-repo enforcement).

Git submodules require the parent repo to reference the child repo via a URL or path plus a specific commit hash. The path form works only if both repos live at consistent absolute paths across all consumer machines; that is not the case for my setup. The URL form requires a remote; my local-only ratification blocks that.

I could reverse the local-only ratification for `sim-ai`. That would open a different set of tradeoffs (publishing risk, credential management, GitHub Actions overhead, backup implications). I have not chosen to reverse it. As long as I do not, Option B stays blocked.

## What the hook actually does

The hook is small. About twenty-five lines of bash. Installed at `~/Projects/sim-ai/.git/hooks/post-commit` via `bash scripts/install-hooks.sh`. The install script also installs the existing pre-commit hook from Post 0178 discipline; both hooks share a single installer.

After every `sim-ai` commit, the hook prints a bordered reminder block:

```
🔔 sim-ai committed. companion-product-workspace vendor sync required for Vercel.

If this commit affects companion-product-workspace scope (research surface dashboard OR
Island NPC Test surface OR any exported-API changes):

  rsync -a --delete ~/Projects/sim-ai/src/ ~/Projects/roomtolife/vendor/sim-ai/

Then at the companion product workspace:

  cd ~/Projects/roomtolife
  git add vendor/sim-ai
  git commit -m '[vendor sync] sim-ai <auto-SHA>'
  git push

Skip if this commit is internal-only (no exported-API changes; internal
refactor scope; or test-only).
```

The `<auto-SHA>` is substituted automatically via `git -C ~/Projects/sim-ai rev-parse --short HEAD`. So I can copy-paste the entire commit message including the current commit's SHA without editing.

The hook stops there. It does not run rsync. It does not modify the companion product workspace. It does not touch git state at the companion product workspace. My subsequent action is fully my choice.

## What this actually canonizes

The pattern is: automate the REMINDER, not the ACTION.

The pattern applies wherever four conditions hold together. First, there is a workflow with a required subsequent action (in this case, `rsync` plus commit plus push at consumer). Second, forgetting the subsequent action produces drift risk (in this case, stale Vercel deploys). Third, auto-executing the subsequent action sacrifices useful deliberate control (in this case, "test at path-alias consumer first" workflow value). Fourth, an unmissable reminder is technically feasible (in this case, post-commit hook stdout output).

When all four hold, the reminder-hook pattern preserves the safety gain (no forgetting) without paying the control-cost (no premature auto-execution).

I filed this as Council #9 candidacy Item 37 at the agenda draft (Council #9 target window 2026-09-05 through 2026-10-05). The filing includes the four-condition framing plus falsification threshold candidate (if operator systematically ignores reminder and drift accumulates greater than two weeks between `sim-ai` commits and companion-product-workspace vendor sync, discipline is empirically falsified as ineffective).

## What I'm not claiming

I am not claiming Option D is universally correct. Option A auto-execute is genuinely better when the deliberate-control value is zero (for example, docs-only propagation where there is no test-before-propagate value to preserve). The choice depends on whether Condition Three holds (auto-execution sacrifices useful control).

I am not claiming Option D scales to large teams. Post-commit hooks are per-machine; team members do not get the reminder without installing the hook themselves. For solo operator infrastructure this is fine; for team infrastructure the pattern would need CI-integrated reminders instead of local hooks.

I am not claiming the reminder is unmissable in the strict sense. If I have a long tail of terminal output and the reminder scrolls past, I could plausibly miss it. In practice the bordered format plus `🔔` emoji plus stdout position immediately after commit makes it very hard to miss. But "unmissable" is aspirational not proven.

I am not claiming the discipline eliminates drift risk. It reduces it. If I actively decide to skip the rsync (because I think the commit is internal-only) but the commit actually did change exported API, drift still occurs. The skip-criteria documentation at both sim-ai CLAUDE.md and companion-product-workspace CLAUDE.md tries to be clear about when to sync versus when to skip, but judgment is required.

What I am claiming is this: after ratifying Option D and installing the hook yesterday morning, the reminder fired three times over the rest of the session. Each firing was appropriate and produced the intended action or intended skip. The first firing (test commit at install time) required no sync (internal test). The second firing (Anchor A bundle commit b5686a1) required sync (bundle is an exported API change). The third firing (verification empty commit 282826b) required no sync (empty commit). The mechanism worked as designed. Whether the pattern reproduces at longer time horizons and across other cross-repo propagation workflows will be the Council #9 empirical test.
