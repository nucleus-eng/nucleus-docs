---
name: nucleus-style
description: Write and review nucleus-docs content against the repo style guide — what each page type is for, what belongs in each section of a Module spec, and what must never appear on a page. Use when authoring, editing, migrating or reviewing any page under docs/ or guides/, when conforming a drafted page, and when deciding where displaced content should go.
---

This is the **procedure**. It states no rules of its own — every rule lives in one file under [`style-guide/`](../../../style-guide/), and this points there. If a rule seems to be missing, add it to the reference, not here.

Read [`principles.md`](../../../style-guide/principles.md) first. It is short, and the rest follows from it.

| Reference | Holds |
| --- | --- |
| [`principles.md`](../../../style-guide/principles.md) | What these documents are; what everything else follows from |
| [`page-types.md`](../../../style-guide/page-types.md) | The four page types, and where displaced content goes |
| [`sections.md`](../../../style-guide/sections.md) | Every section of a Module spec, in order |
| [`conventions.md`](../../../style-guide/conventions.md) | Terminology, figures, citations, what never appears, mechanics |

## Reviewing a page

In this order. The first step finds what is *missing*, which a read-through cannot see. The rest find what is present and wrong.

### 1. Completeness — run the checks first

```bash
python3 scripts/check-composition-tabs.py docs/modules/<name>/   # scoped, fast loop
python3 scripts/check-composition-tabs.py                        # whole corpus
python3 scripts/check-implementations.py
```

Both run in CI on every pull request, so the local run is for speed, not for safety. Run the scoped form while editing one page, and the unscoped form before you finish: **a scoped run only ever sees its own directory.** A Module spec named `<name>-spec.md` rather than `<name>/spec.md` is invisible to the glob, and the check reports it — but only if the run covers the directory it is in.

These enumerate from the dependency graph, and that is the whole reason to run them first. The constituent relation is transitive, so the full closure of a Module is derivable from the pages — a tool can compute the list of things that *should* be on the page and compare. Prose review cannot do this. Reading inspects what is present, and **absence has no textual signature**: a page missing half its composition reads exactly like a page whose composition is short. No amount of care recovers what was never written down.

That asymmetry is why the order in this section is fixed. Step 1 finds what is missing, by enumeration. Steps 2 to 4 find what is present and wrong, by reading. Doing them the other way round means a careful pass over an incomplete page.

Then by hand, against [`sections.md`](../../../style-guide/sections.md):

- Does every section the page needs exist? A missing `# Requirements` is common, and a missing `# Implementations` more so.
- Does the DNA tab list **every** construct in the closure, or only the one that was easy to find? Mark unknown supply routes rather than omitting the row.
- Does every gap carry an `@Editor:` ask, or does it just say "not documented"?

### 2. Boundaries — is this content on the right page?

Use the displacement table in [`page-types.md`](../../../style-guide/page-types.md#where-displaced-content-goes).

**Moving beats trimming.** When you cut a statement of what a Module is *not*, the content it carried usually has a home. Trimming the framing and leaving the paragraph is the common failure.

### 3. Read every prose block

Ask the question from [`principles.md`](../../../style-guide/principles.md#every-page-is-world-readable-because-it-is): **does this describe the Module, or our work on the Module?** The categories are listed in [`conventions.md`](../../../style-guide/conventions.md#what-never-appears).

:::{warning} Do not trust a phrase search here
This is the class that keeps surviving a pass. A grep for the known phrases catches **none** of: "still at the milestone-planning stage", "waiting for Twist", "Interim source", "the 2026-08-14 meeting resolved", "mitigation in progress", "Figure not yet migrated". Every page invents new wording.

A page with zero phrase hits is **not** evidence of conformance, and a score built from phrase hits measures the phrases, not the category.
:::

**When you find a phrasing violation, search the corpus for it before moving on.** These spread. "The requirement is settled" was written once and reached three pages; the same gramicidin admonition reached two; "Source of this page." reached two. A sweep that introduced a phrase introduced it everywhere it fit.

### 4. Sections and prose

Check the page against [`sections.md`](../../../style-guide/sections.md) section by section, and the wording against [`conventions.md`](../../../style-guide/conventions.md).

## Rewriting an internal reference

Most of this text is doing real work — it is how a reader learns a number came from one unreplicated experiment. Deleting the phrase alone makes preliminary data read as settled. Four treatments:

1. **It hedges** — "the source material does not specify…" → characterize the evidence: "not established; a single unreplicated experiment".
2. **It attributes** — a `.docx` or slide number in `# Credits` → drop the citation, keep the person, Node and Lab.
3. **It dates** — "the 2026-08-14 status meeting" → keep the date, drop the meeting.
4. **It is a pointer for us** — "raise on the Chicago questionnaire" → delete, move to `tmp/`.

## When a rule changes

A page conformed under an older version of these rules is not conformant now. Every rule came from reviewing a page that had already passed, so the conformed set is exactly the set most likely to violate a new one. Re-run the whole set after any rule is added — the last such pass produced twenty-two edits across nine pages that had each been called clean.

## Before you finish

Run the pre-PR list in [`conventions.md`](../../../style-guide/conventions.md#before-a-pr).

**Verify token by token.** Diff every number, temperature, construct name and cross-link against the pre-edit file. Reading the diff is not enough: a rewrite that drops a citation can drop a real value in the same sentence, and that is how the PEG hydrogel composition was lost on reporter-lacz.

**The `# Constituent Modules` heading text is load-bearing.** The diagram generator finds the section by its exact words, at any heading depth, so rewording the heading drops the page's constituents out of the graph. Rename anything else on the page freely.

The mermaid `classDef constituent` line is different: the generator *writes* it and never reads it. It is output. Editing it changes the rendered colors and nothing else, and the next run overwrites it.

**Do not rely on being careful about either.** Once the generator lands (it is on PR #222, not on this branch yet), verify instead:

```bash
python3 .claude/skills/mermaid-diagrams/scripts/gen-module-diagrams.py --check
```

It names every page whose block is stale or missing, which is what "silently" used to mean here. A rule that asks an author to remember something is a rule the tool should be enforcing — if you find a way to break the graph that `--check` does not report, fix the generator rather than adding a warning back here.
