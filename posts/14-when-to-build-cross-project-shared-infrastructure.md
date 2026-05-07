# When to Build Cross-Project Shared Infrastructure

**Author:** Jimmy McColery
**Date:** 2026-05-07
**Status:** Operational lesson from one cross-site shared infrastructure pattern established 2026-05-04; n=1 wrapper consumer to date; design-trade-off-grounded rather than multi-fire-grounded; suggestive not conclusive

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record. This work is independent personal research, not professional output from a current employer.*

---

When you have similar tooling concerns across multiple projects (build processes, deployment patterns, configuration conventions), there's a choice point about where the shared concerns live. The default for one or two projects is per-project duplication: copy what works, adjust per project, accept that corrections require updating each project independently. The default works fine until it doesn't. Somewhere around three projects with overlapping tooling concerns, the duplication cost crosses the shared-infrastructure setup cost. Past that threshold, per-project duplication becomes the more expensive option.

This isn't an abstract trade-off. It's an empirical question about specific projects and specific tooling concerns. For static-site deployment to a particular hosting provider, the answer landed at three: at three or more sites with similar deployment patterns, shared infrastructure scales as 1:N where per-project duplication scales linearly. The trigger isn't "three projects" generically; it's "three projects with shared tooling concerns specific enough that duplication produces measurable coordination overhead."

The empirical case: 2026-05-04, the operator's static-site cluster reached the threshold. Four domain-agnostic deployment lessons (connection conventions, security conventions, document-root conventions, tooling conventions) got promoted from per-site documentation to shared cluster reference. First wrapper consumer migrated the same week. The pattern documents an explicit trigger condition, an operational shape, and a generalization claim. This post covers the trade-off, the trigger condition, the empirical instance, and what generalizes beyond the specific static-site domain.

## The trade-off: linear duplication vs 1:N shared reference

Per-project duplication scales linearly. Each new project that joins the cluster requires copying the relevant lessons or conventions. Each correction to those lessons requires updating multiple files. Drift accumulates as projects diverge: corrections that get applied to one project don't propagate to the others; what was canonical at copy-time becomes stale; the duplicated content's relationship to the lived state of any given project loosens over time.

Shared reference scales as 1:N. Lessons live in one location at the cluster level. Consuming projects reference via thin wrapper: a small per-project file pointing to the shared location plus the project-specific values that don't generalize. Corrections to the shared content propagate to all consumers via single update. The wrapper preserves what's project-specific; the shared reference holds what's domain-agnostic.

Both approaches have setup costs. Per-project duplication's setup cost is per-project: each new consumer absorbs the duplication overhead independently. Shared reference's setup cost is upfront: extracting the domain-agnostic content from per-project context, designing the wrapper pattern, migrating the first consumer. The trade-off inverts at some project count. When the cluster is small (one or two projects), duplication's coordination cost is lower than shared-reference's setup cost; the projects don't yet justify the upfront investment. When the cluster grows, the inversion happens.

Where exactly the inversion happens depends on the similarity of the projects' tooling concerns. Higher similarity means more domain-agnostic content available for sharing, which lowers shared-reference's setup cost relative to duplication's coordination cost.

## The trigger condition: three or more similar projects

Three is the documented trigger threshold for the static-site case. The reasoning: at three projects, shared-reference setup costs amortize across the cluster; at two, per-project duplication remains defensibly cheaper than the upfront extraction work. Two-project case is genuinely judgment territory: operators with strong shared-reference muscle memory may extract early; operators conservative on upfront investment may duplicate longer. Three-project case is where the inversion becomes empirically clear.

The threshold isn't universal. It's calibrated to the specific tooling concerns' similarity within the cluster. For static-site deployment to a single hosting provider with the same tooling stack, similarity is high: most lessons earned for one site apply directly to the others. Three works because the domain-agnostic content is dense relative to project-specific values.

For project clusters with lower tooling similarity, the threshold may be higher. Multiple repos with similar build/deploy patterns but different language ecosystems may need four or five projects before shared reference earns its setup cost. Multiple research projects with overlapping workflow conventions but project-specific data structures may have higher thresholds still.

The trigger isn't "three projects" generically. It's "three projects with shared tooling concerns specific enough that duplication produces measurable coordination overhead." Specificity matters. Two superficially similar projects with shallow shared concerns won't justify shared reference at any project count.

## The empirical instance

The pattern got established 2026-05-04 during static-site deployment work. Operational shape: a shared reference file at the cluster's top-level directory, plus thin wrapper files in each consuming project. The wrappers contain site-specific values (domain names, deployment paths, project-specific configuration) and a pointer to the shared reference. The shared reference holds what's domain-agnostic across the cluster.

The shared file documents four domain-agnostic deployment lessons earned across the operator's static-site cluster. Connection conventions: which client tool handles the deployment surface cleanly. Security conventions: how to handle credentials without passing them through command-line history. Document-root conventions: where the hosting provider expects files to land. Tooling conventions: which protocol and port the hosting provider's static service runs on. Each lesson was earned at per-site cost; promoting them to shared reference means new consumers inherit the lessons without re-paying the cost.

First wrapper consumer migrated 2026-05-04. Second wrapper migration pending. The pattern documents an explicit operational follow-through: a 5-step checklist for adopting new sites into the cluster.

The cross-project shared infrastructure family has a second instance with different content type and different structural shape (cross-project drain archives via flat archival), suggesting the broader family generalizes beyond static-site deployment though n=2 cluster instances remains thin foundation for strong generalization claims.

## What this generalizes to

The pattern isn't static-site-specific. Any cluster of similar projects with shared tooling concerns has the same structural opportunity. Multiple repos with similar build/deploy tooling. Multiple research projects with overlapping workflow conventions. Multiple AI-assisted projects with shared canonical-state discipline. The trade-off is the same shape: per-project duplication scales linearly; shared reference scales as 1:N; the inversion happens when project count and tooling-concern similarity together justify the upfront extraction work.

The required components transfer. A shared reference at the cluster level holding domain-agnostic content. Thin wrapper files in each consuming project holding project-specific values plus a pointer to the shared reference. The wrapper preserves what's project-specific; the shared reference holds what's domain-agnostic. The folder-naming convention scales: a top-level cluster directory holding the shared file, plus the cluster's name reflecting the kind of concerns shared rather than the specific consumers.

What doesn't transfer is calibration. The specific trigger threshold (three works for static-site deployment with high tooling similarity; other clusters may require four, five, or higher). The specific shared lesson contents (calibrated to the specific tooling environment). The methodology shape is generalizable; the calibration is operator-and-context-specific.

## What I'm not claiming

I'm not claiming the pattern is novel. Cross-project shared infrastructure has prior art across software engineering monorepo conventions, organizational shared-services patterns, and configuration-as-code practices. What I'm claiming is the operational shape calibrated for personal AI infrastructure work: small project clusters where the trade-off plays out at lower project counts than enterprise-scale shared services.

I'm not claiming the empirical evidence proves the pattern generalizes. One full pattern instance with one wrapper consumer to date. The structural argument suggests the inversion holds across other tooling-concern clusters; the empirical evidence here doesn't establish that.

I'm not claiming three is the universal trigger threshold. Three works for static-site deployment with high tooling similarity. Other clusters may invert at four, five, or higher depending on tooling-concern similarity within the cluster.

## What I am claiming

I'm claiming cross-project shared infrastructure scales as 1:N where per-project duplication scales linearly. The inversion happens when projects with similar tooling concerns accumulate past the threshold where shared-reference setup costs amortize cleanly across the cluster.

I'm claiming three is the documented trigger condition for static-site deployment with high tooling similarity. The structural argument suggests similar inversions exist for other tooling-concern classes: multiple repos with similar build/deploy tooling, multiple research projects with overlapping workflow conventions, multiple AI-assisted projects with shared canonical-state discipline. The thresholds may differ; the inversion shape doesn't.

I'm claiming the pattern's operational shape (shared reference at cluster level; thin wrappers in consumers; site-specific values in wrappers; methodology in shared reference) generalizes beyond the specific static-site deployment domain.

That's the post.
