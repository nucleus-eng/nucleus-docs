# Nucleus documentation style guide

These pages are **reference documentation** for Module and Process specifications. They are not status trackers, lab notebooks, or progress reports.

Write for the global compositional biology community: engineers and scientists who will use a page to build something. Not for the author, not for an editor, and not for the person who happened to run the experiment.

Read this file first. Detail lives in [`style-guide/`](style-guide/).

## The four page types

| Type | Location | Genre |
| --- | --- | --- |
| **Module** | `docs/modules/<name>/spec.md` | Specification — a definition |
| **Process** | `docs/processes/<name>/main.md` | Specification of a procedure — a definition |
| **Implementation** | `docs/implementations/<name>/main.md` | A worked example — a report |
| **Guide** | `guides/` | Tutorial, reference, contribution |

Compositions — chassis, sensing cells, cascades — are Modules. Integration is an activity, not a page type. See [`page-types.md`](style-guide/page-types.md).

## A specification is a definition, not a report

A Specification states **Composition**, **Function**, and **Requirements**. Anything else is off-spec.

*Function* and *Expected Behavior* are the same thing: `Function` is the formal term, `Expected Behavior` is the section name on the page. Never use them as if they differed.

A spec describes an idealization of the Module, not one realization of it. Experiments are evidence that the defined Function holds — never the source of the definition. A result produced by several Modules together is evidence for the composed thing, so it belongs on that page or on an Implementation, not on a constituent's page.

Expected Behavior describes **what the reader will see if they follow the page**. Write "X Module is expected to…", not a past-tense account of one experiment.

## Write for an unknown composer

A Module exists to be composed into systems its author never imagined. Do not write a spec around the one composition you happen to know about.

State what the Module **is**. Do not state what it is not. Negative space is not composition — the `# Constituent Modules` list is already the boundary statement, so prose repeating it adds nothing and prose defending it presumes a reader who arrived confused from a neighboring page.

When you cut a statement of what a Module is not, move what it carried. An option that is not part of this Module usually belongs on an Implementation page, because choosing between options is what those pages are for. Trimming the framing and leaving the content behind is the common failure.

If a boundary feels urgent while you write, check whether it is urgent for the reader or only for you because you just wrote the adjacent page.

## Sentences

Be direct. Say more with fewer words — text that survives review is usually half as long with the same technical content.

State requirements; do not argue for them. Reasoning belongs in Expected Behavior or nowhere.

**Say it once.** If a fact appears twice on a page, one of the two is in the wrong section. Decide which section owns it and delete the other.

Follow Simplified Technical English, pragmatic mode. Do not hard-wrap paragraphs.

## Never on a page

**Treat every page as world-readable, because it is.**

- **Internal documents.** No questionnaires, status decks, meeting transcripts, or `.docx` filenames. Status and hedging live in `tmp/`, for agents and editors.
- **Editor-directed text.** Address the editor with an `@Editor:` or `@Developer:` tag, never in prose. Screen for stray `@` before every PR.
- **Revision history.** "Earlier revisions of this page…" describes the document, not the Module.
- **Meta-commentary.** "flattened one level deep", "not duplicated here", "this page exists to name…".
- **Hedged attribution.** Never "attribution is pending confirmation". Never invent a name, Node, or Lab.

Preliminary data is published behind the `status:` frontmatter and its banner, plus an `:::{attention}` block where needed. That is what carries the doubt — not hedging prose, and not a pointer to an internal source.

## Structural passes

When moving structure rather than rewriting content: nothing is deleted, only relocated. Misplaced content stays on the page and gets reported. The diff should show structure moving, not prose changing.

Renaming a heading is a link change. Run `python3 scripts/check-links.py --offline-only docs/` afterward.

## References

- [`page-types.md`](style-guide/page-types.md) — what belongs on each type, and where displaced content goes
- [`sections.md`](style-guide/sections.md) — Overview, Reference Composition, Expected Behavior, Requirements, Credits
- [`conventions.md`](style-guide/conventions.md) — terminology, figures, tables, citations, mechanics
