# Cyberduck Is Single-Pane and Port 22 Isn't Actually Open: Five Earned Lessons from a 2026 Static-Site Deploy

**Author:** Jimmy McColery
**Date:** 2026-05-24
**Status:** Five concrete deploy-time lessons from one personal static-site shipping arc; each lesson empirically grounded; the through-line generalizes to "deploy-time empirical truths beat documentation."

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

## What I was deploying

In May 2026 I shipped a personal satire site (sueyourkid.com) to production on Porkbun static hosting. Sixteen mock-legal case pages, a few sitewide assets, the usual `robots.txt` + `sitemap.xml` bracket. The site itself is unimportant for this post; what matters is the deployment arc, because five things I learned during it were each the kind of lesson where the documentation said one thing and the empirical reality said another. None of the five was conceptually hard. Each one cost me time because I trusted what I read instead of testing what was true.

This post captures those five lessons. The aim is the same one PHASE_2_LESSONS.md (the in-project notes file these are drawn from) opens with: for the next person, future-me included, who does a Porkbun-class static-site deploy. If you're doing one and you read this first, you should save a few hours.

The lessons live at two scopes. Lessons 1, 2, 4, and 5 generalized across multiple Porkbun static sites I've shipped and now live in a shared canonical file (`~/Projects/sites-common/DEPLOYMENT.md`); each per-site project references that shared file rather than re-stating them. Lesson 3 stayed project-specific to the sueyourkid deploy because the Google Search Console submission only fires once per site. [Post 14](14-when-to-build-cross-project-shared-infrastructure.md) covers when the cross-project-shared-infrastructure pattern earns its keep; that pattern is what makes lessons 1, 2, 4, and 5 portable across sites.

The five lessons in shipping order.

## 1. Cyberduck is single-pane

Cyberduck shows only the remote server in its window. It is not a two-pane FileZilla-style local-versus-remote view. If you grew up on FileZilla or Transmit and you're expecting two halves of the window to drag between, you'll spend a minute hunting for the "show local pane" toggle that doesn't exist.

The intended workflow is: open Cyberduck connected to the remote, open a separate Finder window pointed at the local source directory, drag files from Finder into Cyberduck. That's it. The single-pane design is opinionated about delegating the local view to the OS's native file browser instead of duplicating it inside the app.

If you're expecting two panes and don't see them, that's not a bug. That's the design.

## 2. Port 22 isn't actually open

Porkbun's UI shows you a credentials block labeled "FTP Credentials" with a `PORT=22` field. The hostname is `pixie-ss1-ftp.porkbun.com`. The natural read is: SFTP on port 22, standard SSH-based file transfer, point any SFTP client at it.

Port 22 is not open on that host.

Empirically:

```
$ nc -zv pixie-ss1-ftp.porkbun.com 22
nc: connectx to pixie-ss1-ftp.porkbun.com port 22 (tcp) failed: Operation timed out

$ nc -zv pixie-ss1-ftp.porkbun.com 21
Connection to pixie-ss1-ftp.porkbun.com port 21 [tcp/ftp] succeeded!
```

The actual service is FTPS, specifically FTP-SSL with explicit AUTH TLS, on port 21. In Cyberduck, you pick "FTP-SSL (Explicit AUTH TLS)" from the protocol dropdown. If you try `sftp` from a terminal first, it'll just hang, and if you don't know what you're looking at, the hang reads like a network problem instead of a configured-wrong problem.

The only honest signal in the credentials block is the hostname itself: `pixie-ss1-ftp.porkbun.com` says `ftp`, not `sftp`. Trust the hostname over the port number. The port number in the UI is wrong: the docs and the reality have diverged.

Generalization: when a credentials block disagrees with itself across fields, do not trust the field that's easiest to type into your client. Test what's actually open. `nc -zv` is the cheapest test you can run.

## 3. Google Search Console wants the full sitemap URL for Domain properties

Google Search Console has two property types. URL-prefix properties verify a specific origin (`https://sueyourkid.com/`) and accept sitemap submissions as relative paths like `sitemap.xml`. Domain properties verify ownership of an entire domain via a DNS TXT record and are the right choice if you want a single property covering your apex plus any subdomains plus both protocols.

I went with the Domain property because it's the more general configuration and Google's own docs recommend it for most sites. Then I submitted `sitemap.xml` in the Sitemaps field. The submission appeared to do nothing. No error message, no acknowledgement, no entry in the sitemap list.

The Domain property type requires the full URL in the Sitemaps field. `https://sueyourkid.com/sitemap.xml` works. `sitemap.xml` silently fails. The Sitemaps field is the same UI element in both property types, but it accepts different inputs depending on which property type owns it, and the failure mode for the wrong input is silence rather than rejection.

Generalization: when a form accepts your input without complaint and then doesn't do what you expected, the input may have been parsed differently than it was rendered. Re-read the field's docs for the specific property type you're in, not the docs for the field in general.

## 4. Don't pass passwords as command-line arguments

I wrote an `expect` script to automate the Cyberduck connection step. The first version took the password as `$1`:

```
./connect.exp 'mypassword' jimmy pixie-ss1-ftp.porkbun.com
```

That password ends up in three places I didn't think about:

- Shell history, at `~/.zsh_history`. Visible to anything that can read my home directory.
- The process list, visible via `ps` to other users on the machine. Even on a single-user Mac the process table is enumerated by anything that asks; the habit assumes a multi-user context where it stops being low-stakes.
- Any tool-call transcript that captured the command. AI workflow logs in particular tend to record exact commands; if the command had a password in it, the password is now in those logs.

Three persistence layers I didn't intend. On a single-user Mac with no shared system this is low-stakes, but the habit is wrong, and the habit transfers to multi-user contexts where it stops being low-stakes.

The pattern instead: keep secrets in a gitignored credentials file and have the script read from the file directly.

```
# .porkbun-credentials  (in .gitignore)
HOSTNAME=pixie-ss1-ftp.porkbun.com
PORT=21
USERNAME=sueyourkid.com
PASSWORD=<value>
```

```
# in script
source .porkbun-credentials
expect ... -c "send -- \"$PASSWORD\r\""
```

No argv, no history, no process list, no transcripts. The credentials file is read at script run time and the value never enters the argument list of anything.

If a password has already been passed as an argv, the right move is to rotate it before investigating anything else. Porkbun makes rotation trivial; the time cost is small and the persistence-cleanup cost of trying to scrub three sources is much larger than the rotation cost. Rotate first; understand the leak surface second. I did the rotation step on this deploy.

## 5. Porkbun's document root is `/`

When the FTPS connection lands, you're directly in the document root. There is no `/public/`, `/htdocs/`, `/www/`, or `/site/` subdirectory to navigate into. A file at `/index.html` (where `/` is the connection's root path) is served at `https://yoursite.com/`. A file at `/styles.css` is served at `https://yoursite.com/styles.css`.

This is the simplest of the five lessons, but it's the one I most expected to be wrong, because every other shared-hosting environment I've used in the past two decades had a wrapper directory. cPanel hosts had `/public_html`. nginx defaults had `/var/www/html`. Apache hosts had `/htdocs`. The pattern was so consistent that I assumed Porkbun had one too, dropped my files into a directory I created called `/public/`, watched the site 404 across the board, and figured out the obvious shortly after.

If you find yourself uploading into a subdirectory and the site returns 404s, you're one level too deep. Move the files up to the connection root and the URLs will resolve.

Generalization: assumptions imported from previous environments cost time precisely in proportion to how unconscious they were. The wrapper-directory assumption was so ingrained I didn't notice I was making it. The cheapest test for any new hosting environment is to upload one file and `curl` the URL; if you get a 404, you're either in the wrong place or you're missing the file, and which one is true takes about ten seconds to discriminate.

## The through-line

The five lessons share a shape. In each one, the documentation (or the UI labeling, or the convention from an adjacent environment) said one thing, and the empirical reality said another. The cost of trusting the documentation was always recoverable, but it was always also unnecessary; in every case, a five-minute empirical test before the trust step would have caught the divergence and saved the recovery time.

That isn't a deep finding. "Test the thing instead of trusting the docs" is older than software. What's worth pulling out is the recognition pattern: each of these lessons was a place where I'd absorbed a convention or read a UI element and then proceeded as if the convention or the label was authoritative. The discipline that catches this kind of failure isn't general skepticism (general skepticism makes every deploy unbearable). The discipline is specifically: at the moment you reach for a UI label or a piece of documentation as authoritative input to an irreversible action, run the cheapest empirical test that confirms the label is honest. `nc -zv` for a port. `curl` for a URL. One file uploaded for a hosting layout. Each test costs under a minute. Each one would have prevented one of these five lessons from becoming a lesson.

I shipped the deploy, the site works, and these are now written down somewhere I'll re-encounter the next time I bring a Porkbun site up. The lessons file in the project canonicalized them locally; the shared file at `~/Projects/sites-common/DEPLOYMENT.md` carries the four that generalized; this post carries them out to anyone else who hits the same arc.

## What I'm not claiming

- I'm not claiming any of these five lessons is novel. Cyberduck's single-pane design is documented. Porkbun's FTPS-on-21 reality is in their support threads if you go looking. The GSC Domain-property sitemap requirement is in Google's own docs. The argv-password failure mode is standard security guidance. The document-root layout is in Porkbun's hosting docs. None of this is news.
- I'm not claiming the deploy was complicated. It wasn't. A static site is about as simple as production hosting gets. The lessons here are about friction at the documentation-versus-reality seam, not about technical complexity.
- I'm not claiming I tested everything I should have. I tested the things I happened to think of. The five lessons here are the five places where I didn't test and got bitten; the lessons file I haven't written are the places where I didn't test and didn't get bitten because I happened to guess right.
- I'm not claiming the "test before trusting docs" discipline scales linearly. Past a certain frequency it becomes its own friction. The specific shape that's worth applying is the one tied to irreversible actions: if you're about to spend ten minutes uploading or thirty seconds rotating something, the under-a-minute empirical test pays for itself.
- I'm not claiming Porkbun is bad. Porkbun is fine. The UI has one wrong field and the docs have a few gaps; that's true of approximately every hosting provider. Documenting where the gaps are is more useful than complaining about the gaps existing.

## What I am claiming

When you're deploying a static site to a hosting environment you haven't used before, the cheapest discipline you can apply is to run a one-minute empirical test at every step where a UI label, a convention from an adjacent environment, or a piece of documentation is about to drive an irreversible action. `nc -zv` for ports. `curl` for URLs. One file uploaded for document root layout. The tests are tiny. The lessons they prevent are real. Five of them happened on this one deploy, and writing them down is what makes the cost transferable to the next deploy rather than re-paid.

If you're about to ship a Porkbun static site and you read this first, you should save a few hours.
