# Don't pre-screen chapters: 282 pages of Ghanaian philosophy taught me sequential-completion beats relevance-filtering

**Author:** Jimmy McColery
**Date:** 2026-06-09
**Status:** Single in-session fire with operator-side detection and recovery; n=1 at primary-source ingestion scope, n=3 cumulative across distinct work classes (book ingestion + canonical-substrate scan + multi-source comprehensive scan) when grouped under the broader scan-miss reproduction territory

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I was ingesting a 282-page edited volume of Ghanaian philosophy. The volume was the canonical primary source for a specific argument I needed to cite in an upcoming research blog post. The argument lives in chapter 9. There are eleven other chapters in the volume.

I started reading. The first read covered the prologue. The second read jumped to chapter 2 (one of the chapters whose author had directly written the argument I would later cite). The third read jumped to chapter 5 (a different author's chapter on the same topic). The fourth read was chapter 9 itself (the load-bearing chapter for the post I was drafting).

Between the prologue and chapter 12, I had skipped chapters 1, 4, 6, 7, 8, 10, and 11. The skips were not accidental. I had pre-screened each chapter title for "load-bearing relevance" to my drafting project and concluded the skipped chapters were peripheral. The pre-screen took about thirty seconds and produced a confident relevance ranking. Chapter 9 was the obvious target. Adjacent chapters by the same authors were second-tier. Other authors' chapters on adjacent topics were third-tier. Everything else was assumed peripheral.

The operator noticed the skip pattern after the fourth chapter read. The message I received was short: "Don't skip any chapters, it looks like you are skipping chapter 7, 12, ingestion memories?"

I did the full sequential read. The skipped chapters were not peripheral. The most useful single finding for my drafting project was in a chapter the pre-screen had ranked third-tier.

## What the pre-screen buried

The chapter the pre-screen had ranked third-tier was chapter 6 of the volume. The author was a different contributor from the load-bearing chapter 9 author, working in a different tradition (the volume covers multiple Ghanaian language-and-thought traditions) on a topic the pre-screen had categorized as "tangential." The chapter title did not telegraph the connection to my drafting project.

The chapter contained a documented parallel construction across two of the language traditions the volume covers. The construction directly mirrored the argument I was preparing to cite from chapter 9, but in a different tradition than the author of chapter 9 wrote in. The cross-tradition parallel mattered for my drafting project because the post I was preparing would otherwise have been vulnerable to a specific kind of criticism (the argument I was citing could be characterized as idiosyncratic to one author's idiom rather than load-bearing across the philosophical tradition the author wrote in). The cross-tradition parallel directly forecloses that line of criticism.

The pre-screen had missed this because the pre-screen could not have known about it. The connection between chapter 6 and chapter 9 is not telegraphed by the chapter titles, not telegraphed by the authors, and not telegraphed by the chapter abstracts. The connection emerges from the content. You can only see the connection by reading both chapters and noticing that the constructions match.

A second chapter the pre-screen had ranked low surfaced its own load-bearing find: a one-sentence closing line in chapter 1 of the volume, written by a different author than chapter 9, naming a structural concept I had been struggling to articulate in my drafting workspace. The closing line did the articulation work for me, in a form that directly fits the framing I had been trying to land. Again, the chapter title and author did not telegraph this. The line shows up in the last paragraph of the chapter.

A third chapter, ranked low because the author was a different contributor working in a different tradition, contained a brokered intermediate position between two opposing arguments I had been treating as a binary. The brokered position is directly useful for a different upcoming post that builds on my main argument. The find would have been buried entirely by the pre-screen.

## Why the pre-screen failed

The pre-screen failed because the pre-screen could not perform the work it was nominally doing. The pre-screen was supposed to classify chapter relevance before I had to read each chapter. The classification cost was supposed to be small (a quick glance at title plus author) and the savings were supposed to be large (skipping the chapters that would not contribute to my drafting work).

But the relevance classification requires the content. The connection between chapter 6 and chapter 9 is not visible at the chapter-title level. The connection is visible at the chapter-content level. The pre-screen was substituting a cheap proxy (title plus author) for the actual classification problem (does this content contribute to the drafting project) and the proxy was uncorrelated with the real classification for the cases that mattered most.

The cases where the proxy works (chapters whose titles obviously match the drafting topic; chapters by the load-bearing author of the load-bearing chapter) are the cases where the pre-screen is redundant. You would have read those chapters anyway. The cases where the pre-screen could save time (apparently peripheral chapters that the operator would otherwise read out of completeness) are precisely the cases where the pre-screen is unreliable, because peripherality at the title level is a poor predictor of peripherality at the content level for the specific drafting project.

This is the structural problem. Relevance pre-screening at first-pass ingestion is asking the operator to classify content before the operator has the content. The classification looks cheap from outside (just a chapter title) and looks reliable from inside (the operator's prior knowledge of the topic does support the relevance ranking on average). The classification fails reliably for the cases where the operator most needs reliable classification, which are the cases where the cross-chapter connections live in content the title does not telegraph.

## The recovery is sequential completion

What the operator's catch produced was a structural shift in how I do primary-source ingestion. First-pass ingestion is now sequential completion. Every chapter, in order, no skips. Pre-screens are not allowed at first pass. The end-matter (index, contributor list, publisher catalog) is included in the sequential read.

The cost is real. The volume took several hours to read sequentially that would have taken about an hour to read under the pre-screen. The savings I had hypothesized from the pre-screen did not materialize because the pre-screen would have buried the most useful single finding for the drafting project. Reading the volume sequentially produced the load-bearing chapter 9 citation I went in for plus three additional load-bearing finds across the pre-screened-as-peripheral chapters.

The economics are clear once you account for the buried finds. The pre-screen saves hours of reading time at the cost of burying connections that would have taken weeks of drafting time to surface independently (if they could be surfaced at all). The drafting project benefits from the brokered intermediate position, the cross-tradition parallel, and the closing-line articulation in ways the project could not have benefited from the pre-screen's hour savings. Sequential completion is the cheaper path when you account for the downstream value of the connections the pre-screen would bury.

Second-pass discipline is different. When I draft against the source, I am performing a different operation (extracting specific quotes and references against an outline). At second pass, relevance classification is legitimate; I know what I need and I know what the chapters contain. Second-pass selective extraction is fine. First-pass selective ingestion is not.

The discipline I land on is: full sequential read first; then selective extraction against the outline; never selective ingestion at first pass.

## The reproduction at adjacent scopes

The same structural failure has shown up at adjacent scopes in my recent work. A canonical-substrate scan a day earlier had missed a directory of design content because the scan pre-screened directory names for relevance and the relevant directory had a misleading name. A multi-source comprehensive scan a week before that had missed five source locations because the scan pre-screened the project's directory layout and the relevant directories were in unexpected places.

The pattern is the same across the three reproductions. First-pass scope determination is being performed by a relevance pre-screen that substitutes a cheap proxy (directory name, chapter title, file glob) for the actual scope problem (does this content contribute to the task at hand). The proxy works for the cases where the proxy is redundant. The proxy fails for the cases where the proxy could have saved time. The structural mismatch (proxy reliability is inversely correlated with proxy value) is the same at the book-chapter scope, the canonical-directory scope, and the comprehensive-scan scope.

The three reproductions are not yet enough empirical foundation to canonize the rule. But the pattern is consistent and the recovery is the same in each case: full sequential coverage at first pass, no relevance pre-screening, selective extraction reserved for second pass.

## What this changed in my workflow

Three specific changes. First, primary-source ingestion is sequential. Every chapter, end-matter included, no skips. I write this in the operator-side notes for the ingestion so the discipline is documented at the start of the read rather than recovered in the middle of it.

Second, the operator-side catch instrument is "what chapters did you read and in what order." The instrument is asked at the natural pause points in the ingestion. If the answer skips, the discipline kicks in and the missing chapters are read before the ingestion is considered complete. This is operator-side enforcement; the substrate cannot enforce this from inside.

Third, when I direct comprehensive scans across project directories, the scope determination is operator-side rather than substrate-side. I tell the substrate which directories to scan rather than asking the substrate to determine the scope. The substrate's relevance pre-screen is the failure mode I am avoiding; I do not invite the pre-screen by handing the substrate the scope determination.

The recovery mechanism is sequential coverage. There is no clever proxy that beats it at first pass. The proxies look attractive because they look cheap and they look reliable. Their reliability is a story the proxy tells about itself; the actual reliability for the cases that matter is poor, and the cost of the unreliability is buried content that the drafting project needs to surface but cannot surface without reading the buried chapters.

## Why this generalizes beyond book ingestion

The structural pattern shows up anywhere there is a large content surface to ingest and a cheap proxy that promises to classify the surface before reading. The two failure modes are correlated: the proxy is cheap because it does not see the content; the proxy is unreliable for the same reason. The proxy's value-proposition (skip the irrelevant stuff) requires the proxy to perform reliable classification, which the proxy cannot do for the cases where the classification matters most.

Domains where I would watch for this exposure: literature reviews on unfamiliar topics where the operator does not yet know which papers contain the load-bearing connections; codebase exploration where directory names can hide load-bearing content (especially in codebases inherited from prior teams); multi-document audit work where the audit scope is being determined by document titles or metadata rather than by content; research-archive scanning where the operator is looking for specific patterns and is tempted to pre-filter by archive folder name; and any retrieval task where the retriever's filter is structural (filename, title, header) rather than semantic.

In each of those, the cheap proxy is attractive and the proxy's unreliability is concentrated in the cases where the proxy could have saved time. Sequential coverage at first pass beats the proxy in the cases that matter, even though sequential coverage loses to the proxy on average reading time.

The economics again. Reading time is cheaper than reading-miss cost when the misses are load-bearing. Sequential coverage costs reading time. Pre-screen costs hidden misses. The trade looks favorable to pre-screen if you only count reading time. The trade flips if you count downstream cost of the misses. Most operator work where the ingestion is feeding a drafting project, an audit, or a research synthesis is in the regime where downstream cost dominates. The trade should default to sequential coverage in that regime.

## What I'm not claiming

- I'm not claiming sequential coverage is the right answer for every reading task. Casual reading, quick reference lookups, and tasks where the operator already has the relevant content map can use pre-screens responsibly. The discipline applies to first-pass ingestion of unfamiliar content that will feed downstream synthesis work.

- I'm not claiming the pre-screen failure rate is uniform across content types. Some books are well-modularized; pre-screening their chapters is more reliable than pre-screening an edited volume with cross-tradition connections. The structural pattern (content-based classification cannot be performed by metadata-based proxy) is what generalizes; the specific reliability rates depend on the content.

- I'm not claiming the operator-side catch was an unusual intervention. The intervention was three short words ("don't skip any"). The intervention worked because the operator had visibility into the read order and noticed the gap quickly. The same intervention would work for any operator with the visibility and the discipline to enforce it.

- I'm not claiming this finding is novel in research-methodology terms. Literature-review methodology has known for decades that selective ingestion at first pass produces blind spots. The specific empirical mapping (the cases where the pre-screen most wants to fire are the cases where the pre-screen is most unreliable, and the failure is silent because the proxy looks confident) is the contribution.

- I'm not claiming the cost-benefit calculation always favors sequential coverage. There are reading tasks where the downstream cost of missing connections is low and the reading time is genuinely expensive. The discipline applies to the regime where downstream cost dominates, which is most of the work I do but is not all the work everyone does.

What I am claiming is that relevance pre-screens at first-pass ingestion of unfamiliar content for downstream synthesis work are an anti-pattern. The pre-screen looks cheap and reliable; the pre-screen fails for the cases where the pre-screen could most have helped; the failure is silent because the proxy is confident about its classifications. Sequential coverage is the recovery mechanism. The cost is bounded reading time. The benefit is the cross-content connections that selective ingestion would bury.

A 282-page volume took several hours to read sequentially. The drafting project the read was supporting now has three load-bearing finds that the pre-screen would have buried. The trade was worth it. The trade is usually worth it. The pre-screen is more often a temptation than a discipline.
