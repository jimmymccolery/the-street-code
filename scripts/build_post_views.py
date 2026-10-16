#!/usr/bin/env python3
"""Keep the Layer-2 post views complete.

POSTS-INDEX.md (Layer 1) is the master list: one line per post with proj / task / phase /
discipline / status / supersedes fields. The four Layer-2 views group posts by one of those
fields. They were written by hand in July 2026 as curated selections and then fell behind.

This script keeps the hand-written text of every view untouched and appends, inside marked
blocks, a COMPLETE list of posts for each section, generated from POSTS-INDEX.md. Re-running
it replaces only the marked blocks, so the curated notes never drift and the lists never lag.

    python3 scripts/build_post_views.py            # rewrite the generated blocks in place
    python3 scripts/build_post_views.py --check    # exit 1 if any view is out of date (CI)

Views: POSTS-BY-PROJECT.md (proj), POSTS-BY-PHASE.md (phase), POSTS-BY-CC-TASK.md (task),
POSTS-BY-DISCIPLINE.md (discipline), POSTS-SUPERSESSION-CHAIN.md (supersedes, appendix only).
"""
import argparse, pathlib, re, sys, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent / "posts"
INDEX = ROOT / "POSTS-INDEX.md"
B, E = "<!-- generated:begin {key} -->", "<!-- generated:end {key} -->"
TODAY = datetime.date.today().isoformat()


def parse_index():
    posts = {}
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(0\d{3}) \| ", line)
        if not m:
            continue
        parts = [p.strip() for p in line.split(" | ")]
        rec = {"date": parts[1], "title": parts[2]}
        for p in parts[3:]:
            if ":" in p:
                k, v = p.split(":", 1)
                rec[k] = v.strip()
        rec["proj"] = [x for x in rec.get("proj", "").split(",") if x]
        rec["task"] = [x.strip() for x in rec.get("task", "").split(",") if x.strip()]
        rec["discipline"] = [x.strip() for x in rec.get("discipline", "").split(",") if x.strip()]
        rec["phase"] = rec.get("phase", "")
        rec["supersedes"] = rec.get("supersedes", "none")
        posts[m.group(1)] = rec
    return posts


def line(pid, rec):
    flag = "" if rec.get("status", "published") == "published" else f" [{rec.get('status')}]"
    return f"- {pid} {rec['title']}{flag}"


# ----------------------------------------------------------------------------- section rules
# Each view: ordered (heading, matcher) pairs. A post may appear under several headings.
# "Other" buckets collect what no rule claimed so nothing can silently vanish.

def proj_sections(posts):
    keys = [("sim-ai", "sim-ai"), ("bowling-tycoon-simulation", "bowling-tycoon-simulation"),
            ("street-code-methodology", "street-code"), ("cross-cutting", "cross-cutting"),
            ("companion-product-workspace", "companion-product-workspace"),
            ("primary-backend-project", "primary-backend-project"),
            ("companion-life-builder-product", "companion-life-builder-product"),
            ("master-setup", "master-setup")]
    out = {h: [p for p, r in posts.items() if v in r["proj"]] for h, v in keys}
    out["no project scope recorded"] = [p for p, r in posts.items() if not r["proj"]]
    return out


def phase_sections(posts):
    def group(ph):
        if ph == "era-independent": return "era-independent"
        if ph in ("Phase-1", "Phase-2", "Phase-3", "Phase-4+"): return ph
        if ph.startswith(("Phase-1", "phase-1")) and re.match(r"[Pp]hase-1[0-3]", ph): return "Phase-10 to Phase-13"
        if ph.lower().startswith("phase-14"): return "Phase-14 and the post-close arcs"
        if ph.lower().startswith("phase-15"): return "Phase-15 v3 stages and A1 calibration"
        if ph.startswith("schema-architecture"): return "schema-architecture v0.2 canonization"
        if ph.startswith("2026-07-07"): return "2026-07-07 session arcs"
        if ph == "shipped": return "shipped substrates"
        return "other phase bindings"
    out = {}
    for p, r in posts.items():
        for ph in r["phase"].split(","):
            out.setdefault(group(ph.strip()), []).append(p)
    order = ["era-independent", "Phase-1", "Phase-2", "Phase-3", "Phase-4+", "Phase-10 to Phase-13",
             "Phase-14 and the post-close arcs", "schema-architecture v0.2 canonization",
             "2026-07-07 session arcs", "Phase-15 v3 stages and A1 calibration", "shipped substrates",
             "other phase bindings"]
    return {k: sorted(set(out[k])) for k in order if k in out}


TASK_FAMILIES = ["character-authoring", "empirical-BUILD", "methodology-research", "multi-substrate-audit",
                 "marcus-reed-audit", "anti-fabrication", "operator-realism-check", "canonization-propagation",
                 "deployment-verification", "council-methodology", "personality-architecture",
                 "memory-architecture", "cross-cultural-personhood", "framework-research",
                 "substrate-methodology", "discipline-enforcement", "verification-validation"]
TASK_KEYWORDS = {  # free-form tags (posts 0173 onward) folded into a family by keyword; the tag is shown
    "canonization-propagation": ["canonization", "propagation"], "council-methodology": ["council"],
    "anti-fabrication": ["anti-fabrication", "rule-19", "fabrication"], "marcus-reed-audit": ["marcus-reed"],
    "multi-substrate-audit": ["multi-substrate", "triangulation", "cross-substrate"],
    "verification-validation": ["verification", "validation", "harness", "typecheck", "regression"],
    "memory-architecture": ["memory"], "personality-architecture": ["personality", "hexaco", "attachment", "habitus"],
    "cross-cultural-personhood": ["cultural", "personhood", "intersection"],
    "deployment-verification": ["deployment", "emission", "wiring"], "empirical-BUILD": ["empirical", "build", "stage-"],
    "framework-research": ["schema", "research", "architecture"], "character-authoring": ["anchor", "authoring", "npc"],
}


def task_sections(posts):
    out = {h: [] for h in TASK_FAMILIES}
    other = []
    for p, r in posts.items():
        placed = False
        for t in r["task"]:
            if t in out:
                out[t].append(p); placed = True
        if not placed:
            for fam, kws in TASK_KEYWORDS.items():
                if any(any(k in t.lower() for k in kws) for t in r["task"]):
                    out[fam].append(f"{p}~kw"); placed = True
            other.append(p)
    res = {h: sorted(set(v)) for h, v in out.items() if v}
    if other:
        res["posts with free-form task tags, 0173 onward, also listed above by keyword where a family fits"] = sorted(set(other))
    return res


DISC_FAMILIES = [
    ("Rule 20 Family A — canonization-propagation gap discipline", ["rule-20", "canonization-propagation"]),
    ("Rule 14 Madisonian — cross-substrate Council verdict discipline", ["rule-14", "madisonian", "council-methodology"]),
    ("Rule 19 — anti-fabrication + Marcus Reed Protocol", ["rule-19", "anti-fabrication", "marcus-reed"]),
    ("Rule 11 — substrate-role specialization", ["rule-11", "substrate-specialization", "substrate-triangulation", "multi-substrate"]),
    ("operator-realism-check discipline", ["operator-realism"]),
    ("verify-against-canonical-files discipline", ["verify-against-canonical", "class-h"]),
    ("post-audit-correction extension discipline", ["post-audit-correction"]),
    ("rule-24 addendum-preserves-immutability and correction-notice propagation", ["rule-24", "addendum-preserves"]),
]


def discipline_sections(posts):
    out = {h: [] for h, _ in DISC_FAMILIES}
    none, other = [], []
    for p, r in posts.items():
        tags = [t.lower() for t in r["discipline"]]
        if tags == ["none-applicable"] or not tags:
            none.append(p); continue
        placed = False
        for h, kws in DISC_FAMILIES:
            if any(any(k in t for k in kws) for t in tags):
                out[h].append(p); placed = True
        if not placed or any(not any(k in t for _, kws in DISC_FAMILIES for k in kws) for t in tags if t != "none-applicable"):
            other.append(p)
    res = {h: sorted(set(v)) for h, v in out.items() if v}
    res["none-applicable"] = sorted(none)
    res["posts carrying discipline tags outside the canonized families, listed with their tags"] = sorted(set(other))
    return res


# ----------------------------------------------------------------------------- rendering
def render_block(key, heading_posts, posts, show_tags=None):
    pids = heading_posts
    lines = [B.format(key=key), f"**Complete list, generated {TODAY} from POSTS-INDEX.md ({len(pids)} posts):**", ""]
    for pid in pids:
        kw = pid.endswith("~kw"); pid = pid.replace("~kw", "")
        rec = posts[pid]
        extra = ""
        if show_tags:
            extra = "  · " + ", ".join(rec[show_tags])[:160]
        if kw:
            extra = "  · by keyword: " + ", ".join(rec["task"])[:140]
        lines.append(line(pid, rec) + extra)
    lines += [E.format(key=key)]
    return "\n".join(lines)


def strip_generated(text):
    text = re.sub(r"\n*<!-- generated:begin [^>]+ -->.*?<!-- generated:end [^>]+ -->\n*", "\n\n", text, flags=re.S)
    return normalise(text)


def normalise(text):
    return re.sub(r"\n{3,}", "\n\n", text).rstrip("\n") + "\n"


def plural(n):
    return f"{n} post" if n == 1 else f"{n} posts"


def slug(h):
    return re.sub(r"[^a-z0-9]+", "-", h.lower()).strip("-")[:48]


def rebuild_view(path, sections, posts, show_tags=None, trailing=()):
    """Fixed point of one rebuild pass: the first pass may shift a blank line; the second settles it."""
    text = path.read_text(encoding="utf-8")
    for _ in range(3):
        new = _rebuild_text(text, sections, posts, show_tags, trailing)
        if new == text:
            break
        text = new
    return text


def _rebuild_text(text, sections, posts, show_tags=None, trailing=()):
    """Append a generated block to each existing '## heading' section whose name matches; add new
    sections (before any trailing prose section) for headings the file does not have yet."""
    text = strip_generated(text)
    out_lines = []
    lines = text.split("\n")
    # map existing headings to section keys by prefix match on the heading name
    heads = [(i, l) for i, l in enumerate(lines) if l.startswith("## ")]
    def key_for(heading):
        name = re.sub(r"\s*\(.*$", "", heading[3:]).strip().lower()
        for k in sections:
            if name == k.lower():
                return k
        return None
    used = set()
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("## "):
            k = key_for(l)
            # update the count in the heading
            if k:
                used.add(k)
                base = re.sub(r"\s*\(.*$", "", l)
                l = f"{base} ({plural(len(sections[k]))}; complete list below, generated from POSTS-INDEX.md)"
            out_lines.append(l)
            # copy the section body up to the next heading or the trailing '---'
            j = i + 1
            while j < len(lines) and not lines[j].startswith("## "):
                j += 1
            body = lines[i + 1:j]
            # insert the generated block before the closing '---' of the section if present
            if k:
                sep = len(body)
                for idx in range(len(body) - 1, -1, -1):
                    if body[idx].strip() == "---":
                        sep = idx; break
                body = body[:sep] + [render_block(slug(k), sections[k], posts, show_tags)] + body[sep:]
            out_lines.extend(body)
            i = j
        else:
            out_lines.append(l); i += 1
    text = "\n".join(out_lines)
    # new sections
    new = [k for k in sections if k not in used]
    if new:
        block = "\n".join(f"## {k} ({plural(len(sections[k]))}; complete list below, generated from POSTS-INDEX.md)\n\n"
                          + render_block(slug(k), sections[k], posts, show_tags) + "\n---\n" for k in new)
        marker = next((f"\n## {t}" for t in trailing if f"\n## {t}" in text), None)
        if marker:
            text = text.replace(marker, block + marker, 1)
        else:
            text = text.rstrip("\n") + "\n\n---\n\n" + block
    return normalise(text)


def supersession_appendix(path, posts):
    text = strip_generated(path.read_text(encoding="utf-8"))
    rows = [(p, r["supersedes"]) for p, r in sorted(posts.items()) if r["supersedes"] not in ("none", "")]
    chains = text
    lines = [B.format(key="supersedes-fields"), f"## Supersedes fields recorded in POSTS-INDEX.md (generated {TODAY})", "",
             "Every non-empty `supersedes:` value in the master index, with whether a chain above mentions the superseding post.", "",
             "| Superseding post | supersedes field | chain mentions it |", "| --- | --- | --- |"]
    for p, s in rows:
        mentioned = f"Post {p}" in chains or f"→ Post {p}" in chains or f"{p} " in chains
        lines.append(f"| {p} | {s} | {'yes' if mentioned else 'NO, add a chain'} |")
    lines += ["", E.format(key="supersedes-fields")]
    return normalise(text.rstrip("\n") + "\n\n" + "\n".join(lines))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    posts = parse_index()
    targets = {
        ROOT / "POSTS-BY-PROJECT.md": (proj_sections(posts), None, ("Cross-project citation patterns",)),
        ROOT / "POSTS-BY-PHASE.md": (phase_sections(posts), None, ("Phase binding decision heuristics",)),
        ROOT / "POSTS-BY-CC-TASK.md": (task_sections(posts), "task", ()),
        ROOT / "POSTS-BY-DISCIPLINE.md": (discipline_sections(posts), "discipline", ("Discipline canonization threshold reference",)),
    }
    def nodate(t): return re.sub(r"generated \d{4}-\d{2}-\d{2}", "generated", t)
    stale = []
    outputs = {}
    for path, (sections, show_tags, trailing) in targets.items():
        covered = {p.replace("~kw", "") for v in sections.values() for p in v}
        missing = sorted(set(posts) - covered)
        if missing:
            sys.exit(f"{path.name}: rules leave {len(missing)} posts unplaced: {missing[:10]}")
        outputs[path] = rebuild_view(path, sections, posts, show_tags, trailing)
    sup = ROOT / "POSTS-SUPERSESSION-CHAIN.md"
    outputs[sup] = supersession_appendix(sup, posts)
    for path, new in outputs.items():
        if nodate(new) != nodate(path.read_text(encoding="utf-8")):
            stale.append(path.name)
            if not a.check:
                path.write_text(new, encoding="utf-8")
    if a.check:
        if stale:
            print("out of date:", ", ".join(stale)); sys.exit(1)
        print("Layer-2 views match POSTS-INDEX.md"); return
    print("rewrote generated blocks in:", ", ".join(stale) if stale else "nothing (already current)")
    for path, (sections, _, _) in targets.items():
        print(f"  {path.name}: " + "; ".join(f"{k.split(' — ')[0][:34]}={len(v)}" for k, v in sections.items()))


if __name__ == "__main__":
    main()
