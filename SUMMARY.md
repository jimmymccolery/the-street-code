# What This Repo Is About: A Plain-Language Summary

Imagine you have a really smart friend who helps you do hard work. The friend can read fast, write fast, and sounds confident about answers. But sometimes the friend gets things wrong, and because they sound so confident, it can be hard to tell when. The author of this site does serious work with smart-friend computer programs (the things people call "AI") and noticed they make the same kinds of mistakes over and over.

So he started writing down the mistakes. Each one got a name and a number, like "mistake #13: claims everything was checked when one thing got skipped." Once a mistake has a name, it's faster to spot the next time it happens. The list grew into a kind of rulebook for catching mistakes, plus ways to do work that make the mistakes easier to see when they happen.

The posts in this repo tell the story of building that rulebook, testing it, breaking it, fixing it, and learning what kinds of work it does and doesn't help with. Each post is one chapter of that story. Reading them in order shows how the work grew: from "I noticed something" to "I have a way of working that catches real mistakes other people might miss too."

## How to read this repo

Posts are numbered 01 through 18 in the order the work happened. Reading them in order shows how the research developed. Each post below has a one-paragraph plain-language summary. If you want to dive deeper, click into the actual post.

## Per-post summaries

### 01. Experiment 1: Does Discipline Survive Substrate?
**Date:** 2026-05-02

The author had been using one smart-friend program (called Grok) and his rulebook, and he'd noticed six specific mistakes the program kept making. He wanted to know: are these mistakes about THIS program, or would any program make them? So he ran the same job with a different smart-friend program (called Claude), using the same rulebook. Result: none of the six mistakes happened this time. That's one piece of evidence that the rulebook might be doing real work, but it's only one test, so it's a hint, not proof.

### 02. Experiment 5: Where the Discipline Framework Bound, and Where It Didn't
**Date:** 2026-05-02

Same kind of test, but back on Grok with the rulebook fully loaded. Result was mixed. The program followed every step of the rulebook perfectly: said the right things at the right times. But when the program looked up a real web page to check it, the program reported the page was tiny (37 words) when it was actually big (about 1,500 words of real, careful content). So the rulebook made the work LOOK careful but didn't make sure the program actually saw what was really there. The rulebook half-worked. Knowing where it half-works is more useful than thinking it works everywhere.

### 03. The Rule Fired During Its Own Promotion
**Date:** 2026-05-03

The author was adding a new rule to his rulebook. The new rule said: don't write "[put the real stuff here]" and pretend that counts as finished work. While he was writing this rule down, the smart-friend program produced files that said "[Full file content here]", which was exactly the thing the rule was meant to stop. So the rule's first proof that it was needed happened DURING the meeting where it was being written. That's stronger evidence than seeing it happen yesterday and remembering it. The rule and the way to recover from breaking it both got tested in real time, in the same hour.

### 04. Three Runs at the Asymptote: When Prompt-Language Hits a Training Objective
**Date:** 2026-05-03

The author kept hitting the same problem and tried to fix it by writing his instructions to the program more carefully. He did this three times. Each time, the problem just changed shape, like squeezing a balloon: the air goes somewhere else but doesn't go away. He stopped, read what the program's makers had written about how their program works, and learned something surprising: the program was BUILT to do the thing that was breaking his work. No instruction would ever fix it. The fix had to be different: use different programs for different parts of the job, instead of trying to make one program do everything.

### 05. How a Personal AI Discipline Framework Earns Its First Rules
**Date:** 2026-05-04

The story of how the rulebook started, going back to late April. The author was already noticing the same kinds of mistakes happening over and over, but they were just notes, not yet a rulebook. This post tells what happened when he tried to turn the notes into rules that actually catch things. The big lesson: just having rules written down doesn't stop the mistakes. The rules are useful because once a mistake happens, the author can spot it fast and say "that's mistake #13," and the fix goes quickly. Rules help you RECOGNIZE, not prevent. That changed how he thought about everything that came after.

### 06. What Auditing the Audit Taught Me About Substrate Routing
**Date:** 2026-05-04

The author had a smart-friend program look at his own writing and check it carefully. He noticed: the program was good at simple, exact jobs (count the dashes, copy this exact word) but bad at the harder job of being honestly mean to the writing: finding what was wrong with it. The program kept saying "this is great!" When a different role inside the program (whose only job was to find what was wrong) ran, it actually found things. And when a totally different program checked, it caught more things. The lesson: different parts of a job need different programs, and you need more than one set of eyes. (See also post 04, which is the writing being audited in this story.)

### 07. When the Architecture Worked: Two-Cycle Validation
**Date:** 2026-05-04

The author tried out his new design (using different programs for different parts of the work) on two real jobs. Both worked. Every check passed in the first job (23 out of 23). Almost every check passed in the second job (32 out of 33; one small wrinkle came up). The wrinkle wasn't a problem with the design. It turned into its own lesson about WHEN to save partial work (see the next post). The design seems to do real work, at least for these two kinds of jobs. More tests would help; this is two data points, not proof. (See also post 11, which revisits this wrinkle two days later under cross-substrate audit and finds it more substantive than this post recognized.)

### 08. When Deployment Outpaces Decisions: A Mid-Iteration Alignment Problem
**Date:** 2026-05-04

When you're working on something hard and you finish a piece of it, you might feel ready to "save" that piece: write it into your permanent records. Don't save too early. If you keep working and change your mind about what should go in that piece, the saved version is now wrong, and fixing it later is more work than saving the right version once at the end. The author hit this exact problem and named three ways to recover (each with different costs). The lesson: only save when you're really done with the whole thing, not when one part feels done.

### 09. When Verification Catches Itself: An Audit Chain Across Two Sessions
**Date:** 2026-05-04

The author has a habit of letting a smart-friend program check his work. Once, he ran the same kind of check twice, at different times. The second check disagreed with the first one, and the second check was right. Why? Because the second check went and read the original source, while the first check had guessed based on related stuff. When checks copy from each other instead of looking at the real thing, mistakes spread. When each check looks at the real thing on its own, mistakes get caught. So having two independent eyes is better than two eyes that talk to each other first.

### 10. When the AI Fires Your Own Discipline: Notes on Frame-Inheritance Errors
**Date:** 2026-05-04

The author has rules to stop himself from making certain mistakes (like: don't trust your memory, go look at the actual file). It turns out his smart-friend program makes the SAME mistakes, in the same shapes. The program drafts based on what the author just told it, instead of going to look at the actual files, even when it could. So the rules aren't just for humans. They're for any kind of helper that can take a shortcut. The author saw this happen three times in one work session. Each time, careful checking caught it. The takeaway: catching these mistakes takes more than one kind of check.

### 11. What Cross-Substrate Audit Surfaced That Same-Substrate Verification Missed
**Date:** 2026-05-06

The author was using his rulebook on a real job. Part of the job was a checking step whose results lived in a file with a fixed name. When the work changed and he had to redo the checking step, he told the program to save the new check OVER the old one: same filename, replace what was there. So the new check existed; the old one was gone forever. Then a totally DIFFERENT smart-friend program (Gemini) looked at his work and flagged some numbers as worth double-checking. Looking into those numbers revealed something bigger: the author's saved record of his job pointed to that OLD check for proof, but the old check no longer existed anywhere. His usual checking process couldn't have caught this: only a fresh outside set of eyes could. Lesson 1: when you redo something, keep both versions. Lesson 2: outside eyes catch what same-side checks miss. (See also post 08, which named an earlier version of this same save-too-early pattern.)

### 12. Archive Review as Methodology
**Date:** 2026-05-06

When you have a big pile of old work to look through, the wrong way is to start by remembering "I think there's something important in there somewhere" and digging. Memory plays tricks: it remembers vivid things, not necessarily important things. The right way: first list everything that's actually there. Then for each thing, ask: would my main records be wrong without it? The author tried this on 109 old files. He found 8 things worth saving, 6 things to throw out, 10 things to put off for later. Three near-mistakes got caught by checking carefully at specific moments. Memory alone misses things; structure catches them.

### 13. Reflection as Methodology Research Discipline
**Date:** 2026-05-07

At the end of doing hard work with a computer helper, there are two kinds of wrap-up. Type 1: did the actual job get done right? Type 2: did doing this job teach us anything new about how things work? The author noticed that without specifically asking the second question at the end, the answers just disappear into the conversation history. Asking it on purpose, every time ("what did we just do that's potentially new methodology research?") catches lessons that would otherwise be lost. Across two work sessions, this question alone produced about 25 keepable lessons that would otherwise have vanished. It's a different kind of check from "did this work"; it's "what did we learn." (See also post 12 for a different but related discipline: checking through old work piles on purpose.)

### 14. When to Build Cross-Project Shared Infrastructure
**Date:** 2026-05-07

When you make the same kind of project a few times (like three websites that all live on the same kind of hosting), you start having the same instructions written down in three different places. That's fine for one or two. By three, it gets expensive: every time you learn something new, you have to update three different places, and they drift apart. So at three, it's worth taking the parts that are the same everywhere and putting them in ONE place that all three projects point to. The author did this for his websites. Three is the magic number for this specific case; for other kinds of projects, the magic number might be different.

### 15. Discipline as Substrate, AI Capabilities as Swappable Layer
**Date:** 2026-05-07

Most people think the smart-friend computer program is the most important part of working with one, and the rules around it are just decoration. The author flips this. The RULES are the most important part. The smart-friend programs are interchangeable, like how the same recipe works in any kitchen. Why does this matter? Because programs change, get replaced, retire. If your work is tied to one specific program, you start over when it disappears. If your work is tied to your rules, you just plug in a different program and keep going. He hasn't lived through a big program disappearing yet, so the claim is based on the design, not yet proven by survival.

### 16. Design-Based Research on AI-Assisted Personal Practice
**Date:** 2026-05-07

This last post steps back from doing the work and asks a bigger question: what KIND of work is this? The author argues that what he's been doing isn't just "personal productivity" or "blog journaling." It's a real research method that academic researchers already have a name for: "design-based research," where one person designs something, uses it, and learns from using it, all at once. He matches his work to what the academic researchers say this kind of research has to look like. It mostly fits. There are two honest gaps (he hasn't worked with a partner-researcher; nobody else has tried his rulebook yet). Naming the kind of work gives it more weight than "stuff one guy figured out for himself." (See also post 07 for the two work-class validation cycles this post draws on.)

### 17. Recovery-from-Drift as Framework Discipline
**Date:** 2026-05-07

The rulebook already had rules to PREVENT mistakes (don't claim something is true until you've actually checked). This post is about a different kind of safety net: catching mistakes AFTER they slip past, but BEFORE they cause damage. In one long work session, the author saw the same kind of mistake happen at least five times. Each time, something caught it: a check right before saving; a "look first, then change" two-step workflow; the end-of-session reflection question; the author himself spotting it. The lesson is that backup safety nets at the moment of saving are more reliable than trying to prevent every mistake upfront. Prevention costs effort every time you say something; backup safety nets only cost effort when you're about to save permanent work. The author isn't claiming this replaces prevention. Both work together; one catches what the other misses. The evidence is one session, so this is a hint, not proof. (See also post 13 for one of those backup safety nets: the end-of-session reflection question.)

### 18. What Running on Auto-Pilot Revealed About Framework Structure
**Date:** 2026-05-07

Today the author tried something different: he ran his AI work session on lighter-attention mode (less double-checking than usual) to see what the rulebook would do without him watching closely. What showed up wasn't the rulebook falling apart. Some safety nets work without him paying attention at all: the AI checks itself before saving anything; the two-step "look first, then act" workflow catches mistakes between steps; the end-of-session reflection question fires no matter how tired he is. One safety net is him catching mistakes himself, and that one still worked even on lighter-attention mode, just sometimes a little later than usual. He also noticed he wears six different hats during work sessions (designer, decision-maker, double-checker, researcher, scope-keeper, reader-translator) and they kept firing even on lighter-attention mode, suggesting the hats are part of the rulebook's fabric, not contingent on him being at peak attention. Two times during today's session, the rulebook even caught itself making a mistake while the author was writing about catching mistakes; structural pattern, not coincidence. The author isn't claiming he can run on lighter-attention mode forever. Today's experiment was one session at one condition, so this is a hint, not proof, but the framework holds up better under reduced attention than he expected. (See also post 17 for the recovery-from-drift threshold this post extends.)

### 19. When the audit substrate isn't independent enough
**Date:** 2026-05-08

When the author had to check his own work today, he gave the work to two different smart-friend programs to look at, plus he had a third, more careful program read the actual files directly. The first program gave everything a thumbs-up. The second program found seven specific problems. The third program (the careful reader) confirmed the second program was right and the first program was wrong. The lesson: when picking who checks your work, pick someone who's not too close to the program that helped you make it. Programs that come from similar families can pick up each other's habits in ways that look like agreement but aren't. He'd already decided the rule for this kind of work (for big work, get a check from a program that's structurally different); today's case is fresh evidence for the rule. (See also post 11 for an earlier case where outside eyes caught what inside eyes missed.)

## What's next

This repo will keep growing as new posts publish. Numbered ordering means new posts get the next number (19, 20, etc.) and join the bottom of the per-post summaries above. The arc-level summary at the top updates as the research direction develops.
