#!/usr/bin/env python3
"""
verify-mechanical-fix — Rule 24 mechanical-fix invariant checker (Item 142 candidacy).

Per Fable 5 adversarial audit §D.8 proposal, this script implements the
"normalization-invariant diff test" for mechanical compliance-repair edits:
after applying the normalization the fix claims to perform to BOTH pre- and
post-fix text, the diff must be EMPTY.

Usage:
  python3 verify-mechanical-fix.py --pre-ref REF --post-ref REF \
    --normalization NAME --paths PATH1 PATH2 ...

Currently-supported normalizations:
  em-dash-to-double-hyphen  -- Replace U+2014 with " -- " (spaced) or "--"
  frontmatter-insertion     -- Strip the Author/Date/Status/*Note:* block
                                inserted after the first H1 header
  em-dash+frontmatter       -- Both normalizations applied
"""
import subprocess
import sys
import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def get_content_at_ref(ref: str, path: str) -> str:
    r = subprocess.run(
        ['git', 'show', f'{ref}:{path}'],
        capture_output=True, text=True, cwd=REPO_ROOT,
    )
    if r.returncode != 0:
        raise RuntimeError(f"git show {ref}:{path} failed: {r.stderr}")
    return r.stdout


def normalize_em_dashes(text: str) -> str:
    return text.replace(' — ', ' -- ').replace('—', '--')


def strip_frontmatter_insertion(text: str) -> str:
    """Strip 6-line inserted block starting at **Author:** line."""
    lines = text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        if lines[i].startswith('**Author:** '):
            j = i + 3
            if j < len(lines) and lines[j] == '':
                j += 1
            if j < len(lines) and lines[j].startswith('*Note:'):
                j += 1
            if j < len(lines) and lines[j] == '':
                j += 1
            i = j
            continue
        result.append(lines[i])
        i += 1
    return '\n'.join(result)


NORMALIZATIONS = {
    'em-dash-to-double-hyphen': normalize_em_dashes,
    'frontmatter-insertion': strip_frontmatter_insertion,
    'em-dash+frontmatter': lambda t: strip_frontmatter_insertion(normalize_em_dashes(t)),
}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument('--pre-ref', required=True)
    p.add_argument('--post-ref', required=True)
    p.add_argument('--normalization', required=True, choices=list(NORMALIZATIONS.keys()))
    p.add_argument('--paths', nargs='+', required=True)
    args = p.parse_args()

    norm = NORMALIZATIONS[args.normalization]
    any_failed = False
    print(f"verify-mechanical-fix -- normalization={args.normalization}")
    print(f"  pre  ref: {args.pre_ref}")
    print(f"  post ref: {args.post_ref}")
    print()
    for path in args.paths:
        pre = get_content_at_ref(args.pre_ref, path)
        post = get_content_at_ref(args.post_ref, path)
        pre_norm = norm(pre)
        post_norm = norm(post)
        match = pre_norm == post_norm
        name = path.split('/')[-1][:60]
        print(f"  {'✓' if match else '✗'} {name}")
        if not match:
            any_failed = True
            for j, (pl, pol) in enumerate(zip(pre_norm.split('\n'), post_norm.split('\n'))):
                if pl != pol:
                    print(f"    FIRST_DIFF line {j+1}:")
                    print(f"      pre : {pl[:80]!r}")
                    print(f"      post: {pol[:80]!r}")
                    break
    print()
    if any_failed:
        print("VERDICT: mechanical-fix invariant FAILED — Rule 24 addendum path applies")
        return 2
    print(f"VERDICT: mechanical-fix invariant HOLDS at n={len(args.paths)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
