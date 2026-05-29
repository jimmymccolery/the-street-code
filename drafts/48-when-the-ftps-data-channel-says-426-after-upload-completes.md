# When the FTPS data channel says 426 after upload completes

**Author:** Jimmy McColery
**Date:** 2026-05-28
**Status:** SEED STUB — operator-authoring-pending. Empirical debugging post-mortem on Porkbun FTPS TLS 1.3 data-channel bug discovered during Pattern A deploy.sh first run for sueyourkid.com. Sibling to Post 37 "Cyberduck Is Single-Pane and Port 22 Isn't Actually Open" — same Porkbun infrastructure, different layer of the stack.

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

## The seed: what to write about

A first Pattern A deploy.sh run on sueyourkid.com 2026-05-28 evening failed on 4 of 34 files. All 4 failures returned the same opaque error:

```
curl: (18) server did not report OK, got 426
```

The failed files all clustered above approximately 15KB. The 30 files under that threshold succeeded. The natural first read: a size-related transfer limit. That read is wrong.

## The diagnostic arc to narrate

1. **Initial pattern recognition**: file size correlated with failure. Hypothesis: server-side size limit, network glitch, or credential issue.
2. **Retry didn't help**: same 4 files failed identically on second attempt. So it's not transient.
3. **`curl -v` verbose trace revealed the real signal**: `upload completely sent off: 20512 bytes` followed by `< 426 Failure reading network stream`. The bytes left the client. The server received them. The 426 fires *after* delivery.
4. **TLS 1.3 specifically on the data channel**: the verbose trace showed `SSL connection using TLSv1.3 / AEAD-AES256-GCM-SHA384` on the secondary FTPS data connection. The server's TLS 1.3 implementation couldn't cleanly close the data channel after delivery.
5. **Fix**: `--tlsv1.2 --tls-max 1.2` on the curl invocation. Forces TLS 1.2 negotiation on the data channel. Full deploy succeeded on first re-attempt.

## The lesson worth surfacing

When error messages name the wrong layer of the stack, the fix is somewhere else. The "size threshold" framing was a red herring driven by *what failed* rather than *why it failed*. The verbose trace was the only source that gave honest signal — and the honest signal was 426 *after* `upload completely sent off`. Trust what the trace says happened, not what the failure pattern suggests caused it.

## Cross-references

- sueyourkid commit `c14d31b` (deploy.sh TLS 1.2 fix; full empirical record in commit message)
- sueyourkid `PHASE_2_LESSONS.md` §6 (canonical fix banking)
- sites-common `DEPLOYMENT.md` Lesson 5 (cross-site reference for any future Porkbun static site)
- jimmymccolerycom deploy.sh (prophylactic TLS 1.2 applied even though bug hadn't surfaced there yet)
- Post 37 "Cyberduck Is Single-Pane and Port 22 Isn't Actually Open" (sibling Porkbun-infrastructure debugging post)

## Voice notes

Match the technical-discipline register of Posts 36 + 37 + 44. The audience is solo-indie developers who hit error 18 from curl on FTPS uploads and Google brings them here. Open with the specific symptom; reveal the trace; identify the real cause; cite the fix; close with the meta-lesson about error messages naming the wrong layer.
