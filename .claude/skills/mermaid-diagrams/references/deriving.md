# Deriving diagrams from page structure

Load this when generating diagrams from docs rather than hand-writing them.

A hand-drawn dependency diagram drifts from the pages it describes within weeks,
and the drift is invisible — the diagram still renders, it is just wrong. If the
structure is already written down somewhere in the docs, read it from there.

## The graph is usually already in the pages

Nucleus module pages declare their constituents in a section:

```markdown
# Constituent Modules

- [Input Module A](../input-a/spec.md) — what it contributes
- [Input Module B](../input-b/spec.md)
```

That is a dependency edge list. Extract it:

```python
def constituents(text):
    m = re.search(r"^#+\s*Constituent Modules\s*$(.*?)(?=^#|\Z)", text, re.M | re.S)
    if not m:
        return []
    out = []
    for link in re.finditer(r"\]\(\.\./([A-Za-z0-9._-]+)/spec\.md", m.group(1)):
        slug = link.group(1)
        if slug not in out:
            out.append(slug)
    return out
```

Restrict to tracked files, so gitignored build artifacts do not enter the graph:

```bash
git ls-files docs/modules
```

## Two relations, not one

Composition is not the only edge kind. A module can also *require* something it
is not made of — a substrate that must be present, an enzyme that must be
supplied, a condition that must hold.

| Relation | Meaning | Style |
| --- | --- | --- |
| composition | "is made of" | `A --> B` solid |
| requirement | "must be present for this to function" | `A -.->|requires| B` |

Drawing them the same way is what makes a required-but-not-constituent module
appear as a floating node with no edges. If a node has no edges, check whether it
is actually a requirement of something before deleting it from the diagram.

Requirements are usually prose, so they need declaring explicitly until pages
carry a structured field for them:

```python
REQUIRES = {
    ("reporter-module", "substrate-module"),
    ("reporter-module", "effector-module"),
}
```

## Idempotent insertion

Wrap generated blocks in markers. Regeneration then replaces only what is
between them and never touches hand-written content:

````python
BEGIN = "<!-- gen:composition-diagram -->"
END   = "<!-- /gen:composition-diagram -->"

m = re.search(re.escape(BEGIN) + r".*?" + re.escape(END), text, re.S)
if m:
    text = text[:m.start()] + block + text[m.end():]
else:
    # no marker on this page — report it, do not guess a location
    ...
````

**Do not auto-place a marker that is not there.** Where a diagram belongs on a
page is an editorial decision. Report the pages missing markers and let a human
place them once.

## Three modes worth having

| Mode | Behaviour |
| --- | --- |
| default | write proposals to a scratch directory, touch nothing in `docs/` |
| `--write` | replace content between existing markers |
| `--check` | exit non-zero if any page's block is stale — suitable for CI |

The default being a dry run matters. A generator that writes on first invocation
will eventually write something nobody asked for.

## Scope the graph honestly

**Roots must be declared, not inferred from links.** Pages link to modules they
do not depend on — to explain why something was removed, or to contrast against
a different implementation. Scraping every link puts phantom nodes in the
diagram. Take roots from an explicit list.

**Every node should be a dependency of something in the diagram.** A node with no
path to a root is either a mistake or a signal that the declared roots are wrong.
Both are worth reporting rather than rendering.

**Exclude proposed constituents.** A page may list an alternative it is not
currently using. Including it implies a dependency that does not exist:

```python
EXCLUDE_EDGES = {
    ("some-cascade", "proposed-alternate-reporter"),
}
```

**Subset relationships are checkable, so check them.** If you generate both a
per-subsystem diagram and a whole-system diagram, assert the former is a subset
of the latter. When it is not, one of the two is wrong, and the assertion tells
you which pass introduced it.

## What a generated diagram may and may not claim

It may claim **structure** — what is composed of what — because that is what it
read.

It may not claim **status**. Whether an integration has been demonstrated lives
in status documents on a separate axis, and a generator that draws confirmed
edges is asserting something it never checked.

So either draw every edge plain and caption the diagram as composition-only, or
read status from an explicit field and cite it. Never infer status from the
existence of a composition edge — a page can describe a composition that has
never been assembled.

Put the limit in the caption, not just in the commit message:

> This diagram shows composition only. It does not assert that any integration is
> confirmed.

## A diagnostic worth knowing

A page that *should* be the root of a subsystem, but comes out excluded from its
own dependency graph, has wrong constituents. This is a genuinely useful signal:
one such exclusion revealed a page still listing a component that had been
dropped from the design weeks earlier, which no amount of proofreading had
caught.

Generating the diagram found it because the graph made the absence structural
rather than textual.
