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

WHAT IS COPIED: THE WHOLE BODY, from the first non-comment line, with the
FROM_FIELDS substitutions applied. Not a chosen set of keys. This line read
"the orders, type_requires, module_slugs and unparsed" until 2026-10-12,
when the published file had SEVEN top-level keys and the upstream had gained
two more that this script was already copying. A description of what a
generator copies drifts; the code does not, so the code is what is stated.
Re-run it whenever upstream changes -- `--check` says when that is due.
The two files carry identical node sets -- re-measured 2026-10-12 against theory
15bcb95 at 76 type nodes and 41 process nodes, same module_slugs -- so no name
mapping is applied. IF A MAPPING IS EVER NEEDED IT GOES HERE AND IS STATED, rather
than being done once by hand. THE FIGURES READ "68 type nodes, 28 process nodes"
when this was written and were stale within a day; the identity is what the claim
rests on, not the size, so the identity is what --check tests. Do not trust the
numbers in this paragraph over a run.

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
#
# `bracket_aliases` maps a flat spelling to the type node it means, for the one place
# a type name cannot be written as it is spelled. An operation id in a spec.yml is
# `op[Type]`, and scripts/spec-yml-schema.yml matches the bracket against
# `[A-Za-z0-9]+(,[A-Za-z0-9]+)*` -- no nesting. So `degrade[DNA[linear]]` is invalid
# by construction, and a type whose own name carries a bracket has no spelling inside
# an operation id. The alias is how a checker resolves one.
"""


# Upstream names its own file; this repo states the content instead.
FROM_FIELDS = {
    '    from: "signature.md type table: a row\'s own refines, and the parent-side phrases"':
    '    from: "the upstream type table: a row\'s own refines, and the parent-side phrases"',
    '    from: "signature.md ## Processes: refines in a profile"':
    '    from: "the upstream Process profiles: refines in a profile"',
}


# A FLAT SPELLING FOR A BRACKETED TYPE, 2026-10-12. STATED, NOT DERIVED.
#
# WHY IT EXISTS. `DNA[linear]` became a type node on 2026-10-12, when topology was
# made a refinement axis over `DNA`. Three sources already wrote `degrade[linearDNA]`
# -- docs/functions/degrade/function.yml, docs/modules/s30-lysate/spec.yml and a
# comment in docs/modules/nucleic-acid/spec.yml -- and `linearDNA` is not a node, so
# the schema's own worked example, `degrade[DNA]` meets `degrade[linearDNA]` because
# DNA is wider, resolves to "no node" and the comparison silently falls back to
# exact match.
#
# THE SCHEMA PREDICTED THIS DAY AND NAMED THE CONDITION. spec-yml-schema.yml under
# `provides:`: "A type with no node compares only to itself, which is why `linearDNA`
# is exact today and A TOPOLOGY AXIS WOULD CHANGE THAT." The axis landed. The
# condition has occurred.
#
# WHY A MAP AND NOT A RENAME. The three sources cannot write `DNA[linear]` -- the id
# pattern forbids a bracket inside a bracket. Upstream cannot rename the node either:
# the bracket form is how a parameter axis is written there, ruled on the day the
# rows were added. Neither side is wrong and neither can move, which is exactly when
# a mapping is the answer rather than a workaround.
#
# ONE ENTRY, NOT A SCHEME. `DNA[circular]` gets no alias because nothing writes one,
# and inventing a spelling for a type nobody references is how `make` and `assay`
# reached ten sources. An operation id naming a bracketed type with no alias here is
# a finding for whatever checker reads this file, not something to guess at.
BRACKET_ALIASES = {
    "linearDNA": "DNA[linear]",
}


def alias_block(src):
    """The alias map, with every target checked against the order being published."""
    import yaml
    nodes = set()
    doc = yaml.safe_load(open(src, encoding="utf-8")) or {}
    for key in ("type_refinement", "process_refinement"):
        o = ((doc.get("orders") or {}).get(key) or {})
        nodes.update(str(x) for x in (o.get("nodes") or []))
    out = ["bracket_aliases:"]
    for flat in sorted(BRACKET_ALIASES):
        node = BRACKET_ALIASES[flat]
        if node not in nodes:
            # LOUD, NOT SILENT, for the reason the FROM_FIELDS warning gives: an
            # alias pointing at a node the order does not have is worse than none.
            print(f"warning: alias {flat} -> {node}: no such node upstream, "
                  f"so it is not published", file=sys.stderr)
            continue
        out.append("  %s: '%s'" % (flat, node))
    if len(out) == 1:
        out = ["bracket_aliases: {}"]
    return "\n".join(out) + "\n"


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
    text = HEADER + body(src) + alias_block(src)
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
