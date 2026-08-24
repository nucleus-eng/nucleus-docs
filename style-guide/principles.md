# Principles

The rules in the other reference files follow from these. Where a case is not covered, decide it from here.

## These pages are reference documentation

Not status trackers, not lab notebooks, not progress reports. Write for the global compositional biology community: engineers and scientists who will use a page to build something. Not for the author, not for an editor, and not for the person who ran the experiment.

Tone is an engineering brief. Simple, direct, technical language: what the thing is, and how it works.

## A specification is a definition, not a report

A Specification states **Composition**, **Function**, and **Requirements**. Anything else is off-spec.

*Function* and *Expected Behavior* are the same thing: `Function` is the formal term, `Expected Behavior` is the section name on the page. Never use them as if they differed.

A spec describes an idealization of the Module, not one realization of it. Experiments are evidence that the defined Function holds — never the source of the definition. A result produced by several Modules together is evidence for the composed thing, so it belongs on that page or on an Implementation, not on a constituent's page.

Expected Behavior describes **what the reader will see if they follow the page**, not a past-tense account of one experiment. [sections.md](sections.md#expected-behavior) gives the construction.

This is the one place the genre inverts: an Implementation page *is* a report. See [page-types.md](page-types.md).

## Write for an unknown composer

A Module exists to be composed into systems its author never imagined. Do not write a spec around the one composition you happen to know about.

State what the Module **is**. Do not state what it is not. Negative space is not composition — the `# Constituent Modules` list is already the boundary statement, so prose repeating it adds nothing and prose defending it presumes a reader who arrived confused from a neighboring page.

When you cut a statement of what a Module is not, move what it carried. An option that is not part of this Module usually belongs on an Implementation page, because choosing between options is what those pages are for. Trimming the framing and leaving the content behind is the common failure.

If a boundary feels urgent while you write, check whether it is urgent for the reader or only for you because you just wrote the adjacent page.

## Every page is world-readable, because it is

The test is one question asked of every prose block: **does this describe the Module, or does it describe our work on the Module?** The second kind comes out.

A list of banned phrases will not find it — every page invents new wording. The categories, with examples seen so far, are in [conventions.md](conventions.md#what-never-appears). The examples are a seed, never a checklist.

Anything that is not for the public — status, hedging, provenance of internal documents, notes between agents and editors — lives in `tmp/`. Preliminary data is published behind the `status:` banner and an `:::{attention}` block. That is what carries the doubt.

Where a page has a gap, tag it: an attention block naming what is missing and who should find it, marked `@Editor:` or `@Developer:`. A cell reading "not documented" records a gap; a tagged block asks someone to close it.

## Say it once

If a fact appears twice on a page, one of the two is in the wrong section. Decide which section owns it and delete the other.

Be direct. Text that survives review is usually half as long with the same technical content. State requirements; do not argue for them — reasoning belongs in Expected Behavior or nowhere.

Follow Simplified Technical English, pragmatic mode. Do not hard-wrap paragraphs.

## Structural passes

When moving structure rather than rewriting content: nothing is deleted, only relocated. Misplaced content stays on the page and gets reported. The diff should show structure moving, not prose changing.

Renaming a heading is a link change. Run `python3 scripts/check-links.py --offline-only docs/` afterward.
