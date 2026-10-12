#!/usr/bin/env python3
"""Copy the upstream type order into docs/type-order.yml, header and all.

WHY THIS EXISTS. docs/type-order.yml says "GENERATED. Do not edit." and until
today NOTHING GENERATED IT. It was copied in by hand, which is how #282 landed a
copy taken from an integration branch: it described 107 module sources where main
has 23, and 459 lines of it were never true here. A file that claims to be
generated and has no generator is a file nobody can check.

    publish-type-order.py <upstream signature.posets.yml>            write
    publish-type-order.py <upstream signature.posets.yml> --check    compare

THE UPSTREAM PATH IS AN ARGUMENT AND NOT A DEFAULT, because this repo cannot
assume a sibling checkout and must not guess one. CI cannot run this: the source
is in another repository. So --check is for whoever has both trees, and the
honest statement of its standing is that it is a tool, not a guard.

WHAT IS COPIED: the orders, type_requires, module_slugs and unparsed, as data.
The two files carried identical node sets when this was written -- 68 type nodes,
28 process nodes, same module_slugs -- so no name mapping is applied. IF A MAPPING
IS EVER NEEDED IT GOES HERE AND IS STATED, rather than being done once by hand.

WHAT IS REWRITTEN: the header, and the two `from:` fields. Both name `signature.md`
upstream, a file a reader of this repo cannot open -- the defect #285 fixed BY HAND
IN THE COPY. The first run of this script put them straight back, and
check-reference-voice caught it, which is the whole argument for both: a hand-fix to
a generated file survives exactly until the next generation, and the check is what
noticed. REWRITES BELONG IN THE GENERATOR.
"""
import sys, os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "docs/type-order.yml")

HEADER = """# GENERATED. Do not edit.
#
# The type order: which type refines which, and which page slug names which type.
# A Module's `type:` and `refines:` are checked against this file, and a type here
# need not have a page -- `Container` and `Vesicle[LUV]` have none.
#
# IT IS NOT DERIVED HERE. This repo's own orders come from the sources themselves and
# are published in docs/type-system.posets.yml; a type order cannot be read off them,
# so it is generated upstream and copied in by scripts/publish-type-order.py. Which
# commit it came from is in this file's git history, where a reader can follow it.
#
# `type_requires` is what a TYPE demands, as against what a module demands. It is
# here because a type need not have a page, and a type with no page has no spec.yml
# to carry a claim about itself -- so without this section the order says which types
# exist and nothing about what they need.
#
# `module_slugs` maps a page slug to its type: `outer-solution` is `Solution`.
"""


# Upstream names its own file; this repo states the content instead.
FROM_FIELDS = {
    '    from: "signature.md type table: a row\'s own refines, and the parent-side phrases"':
    '    from: "the upstream type table: a row\'s own refines, and the parent-side phrases"',
    '    from: "signature.md ## Processes: refines in a profile"':
    '    from: "the upstream Process profiles: refines in a profile"',
}


def body(src):
    lines = open(src, encoding="utf-8").read().split("\n")
    i = next(i for i, l in enumerate(lines) if l and not l.startswith("#"))
    out, seen = [], set()
    for l in lines[i:]:
        if l in FROM_FIELDS:
            seen.add(l)
            l = FROM_FIELDS[l]
        out.append(l)
    missing = set(FROM_FIELDS) - seen
    if missing:
        # LOUD, NOT SILENT. An upstream rewording would otherwise slip a repo name
        # into a published file and this script would report success.
        for m in sorted(missing):
            print(f"warning: expected upstream line not found, so not rewritten:\n"
                  f"  {m.strip()}", file=sys.stderr)
    return "\n".join(out)


def main(argv):
    if not argv or argv[0].startswith("--"):
        print(__doc__.strip().split("\n\n")[1], file=sys.stderr)
        return 2
    src, check = argv[0], "--check" in argv
    if not os.path.isfile(src):
        print(f"no such file: {src}", file=sys.stderr)
        return 2
    text = HEADER + body(src)
    if check:
        have = open(OUT, encoding="utf-8").read() if os.path.isfile(OUT) else None
        if have != text:
            print(f"STALE: docs/type-order.yml does not match {src}", file=sys.stderr)
            return 1
        print(f"docs/type-order.yml matches {src}")
        return 0
    open(OUT, "w", encoding="utf-8").write(text)
    print(f"wrote docs/type-order.yml from {src}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
