---
name: nucleus-style
description: Write and review nucleus-docs content against the repo style guide — what each page type is for, what belongs in each section of a Module spec, and what must never appear on a page. Use when authoring, editing, migrating or reviewing any page under docs/ or guides/, when conforming a drafted page, and when deciding where displaced content should go.
---

Read [STYLE-GUIDE.md](../../../STYLE-GUIDE.md) first — it is under 800 words and states the principles. This skill is the working procedure that applies them.

Detail lives in three references, loaded as needed:

- [`style-guide/page-types.md`](../../../style-guide/page-types.md) — the four page types, and where displaced content goes
- [`style-guide/sections.md`](../../../style-guide/sections.md) — every section of a Module spec, in order
- [`style-guide/conventions.md`](../../../style-guide/conventions.md) — terminology, figures, citations, mechanics

## The one idea

These pages are **reference documentation**, not status trackers. A Specification states
Composition, Function and Requirements, and is a **definition, not a report**. An
Implementation page is the one place where a report is the right genre.

Everything else follows from that.

## Reviewing a page

Work in this order. The first two catch what is *missing*, which is invisible to a
read-through; the rest catch what is *present and wrong*.

### 1. Completeness — run the checks

```bash
python3 scripts/check-composition-tabs.py docs/modules/<name>/
python3 scripts/check-implementations.py
python3 scripts/check-links.py --offline-only docs/
```

`check-composition-tabs.py` compares each page's Reference Composition tabs against the
transitive closure in its own generated dependency diagram. A page can read perfectly and
still be missing half its composition — that is the failure mode a prose pass cannot see.

Then check by hand:

- Does every section the page needs exist? A missing `# Requirements` is common.
- Does the DNA tab list **every** construct in the closure, or only the one that was easy
  to find? Mark unknown supply routes rather than omitting the row.

**Tag every gap you leave behind.** A cell reading "not documented" records the gap but
asks nobody to close it. Give the tab an attention block naming what is missing and who
should find it:

```
:::{attention} Composition not fully documented
@Editor: the outer-solution osmolarity components for this cascade are not recorded.
Confirm with the London Node.
:::
```

`@Editor:` and `@Developer:` are the sanctioned forms. The pre-PR screen for stray `@` is
what stops one shipping unresolved — it is a reminder to close them, not a ban on writing
them.

**`# Implementations` lists Implementations, and lists all of them.** Two failures, both
found by `check-implementations.py`:

- A cascade is a **Module**, however composed. Only pages under `docs/implementations/`
  belong in this section. Modules that use this Module do not belong here
  either. On a composed Module the dependency diagram already shows them; on a leaf
  Module — a detector, reporter, membrane, cytosol — there is no diagram, so name them in
  one Overview sentence instead.
- The relation is symmetric. If an Implementation is built from this Module, this Module
  lists that Implementation. The reverse half is the one that rots: nobody revisits twelve
  Module pages when an Implementation gains a Module.

### 2. Boundaries — is this content on the right page?

| Content | Belongs on |
| --- | --- |
| Evidence that this Module's Function holds | this page, Expected Behavior |
| A result produced by several Modules together | the composed Module, or an Implementation |
| A specific demo run | the Implementation page |
| Step-by-step method | the Process page |
| An option not part of this Module's Composition | the Implementation that would choose |
| Status, provenance of internal sources, open questions | `tmp/`, not the repo |

**Moving beats trimming.** When you cut a statement of what a Module is *not*, the content
it carried usually has a home. Trimming the framing and leaving the paragraph is the
common failure.

### 3. What must never appear

Treat every page as world-readable, because it is.

- **Internal documents** — questionnaires, status decks, meeting transcripts, `.docx`
  filenames, slide numbers. Including inside `# Credits`.
- **Editor-directed text** — use an `@Editor:` or `@Developer:` tag, never prose.
- **Revision history** — "Earlier revisions of this page…" describes the document.
- **Meta-commentary** — "flattened one level deep", "not duplicated here".
- **Hedged attribution** — never "attribution is pending confirmation".

Preliminary data is published behind the `status:` banner and an `:::{attention}` block.
That is what carries the doubt.

### 4. Sections and prose

- **Say it once.** A fact appearing twice means one copy is in the wrong section.
- **Requirement or observation?** A Requirement is what the reader must provide or avoid.
  An observed property is Expected Behavior, even when it sounds like a warning.
- **Expected Behavior is what the reader will see** — "X Module is expected to…", not a
  past-tense account of one experiment.
- **Credits is one sentence.** Node before Lab.
- **`# Processes`, plural.** It links the Process pages and carries preparation parameters
  — target size, extrusion passes, purification, storage. A number describing *how you make
  it* is process data even in a table, and does not belong in Reference Composition. If no
  Process page covers the combination, one sentence saying so, and stop.
- **`Inner Solution` is the compartment inside any liposome.** Not `Luminal Cargo`. Use
  `Cytosol` only when the contents are an expression system.
- Half the length, same technical content.

## Rewriting an internal reference

Most of this text is doing real work — it is how a reader learns a number came from one
unreplicated experiment. Deleting the phrase alone makes preliminary data read as settled.
Four treatments:

1. **It hedges** — "the source material does not specify…" → characterize the evidence:
   "not established; a single unreplicated experiment".
2. **It attributes** — a `.docx` or slide number in `# Credits` → drop the citation, keep
   the person, Node and Lab.
3. **It dates** — "the 2026-08-14 status meeting" → keep the date, drop the meeting.
4. **It is a pointer for us** — "raise on the Chicago questionnaire" → delete, move to
   `tmp/`.

## Before you finish

```bash
git ls-files docs/ | grep -E '\.(md|csv)$' | xargs vale
codespell docs/
python3 scripts/check-composition-tabs.py
python3 scripts/check-links.py --offline-only docs/
python3 scripts/check-dropdowns.py && python3 scripts/check-toc.py && python3 scripts/check-file-placement.py
grep -rnE '@[A-Za-z]' docs/ --include='*.md' | grep -vE '@(Editor|Developer):' && echo "STRAY TAG — resolve before publishing"
```

`@Editor:` and `@Developer:` are the sanctioned forms and are expected on a `status: draft`
page — they are how a gap asks to be closed. The screen exists to catch anything else, and
to remind you that tagged gaps must be resolved before a page is published, not to forbid
writing them.

**Verify token by token.** Diff every number, temperature, construct name and cross-link
against the pre-edit file. A structural pass should change structure, not facts.

**Never touch** the `# Constituent Modules` heading or mermaid `classDef constituent` —
the diagram generator matches both with hardcoded strings, and a page missing either drops
out of the generator silently.
