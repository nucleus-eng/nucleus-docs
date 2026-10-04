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

**A Module page may point downstream. It must not depend downstream.** Reaching forward to a composite to say what this Module is inverts the dependency: the leaf then needs the composite to be legible, while the composite already needs the leaf to exist. A corpus built that way cannot retire, reuse or read a part on its own.

**The test.** Delete the link to the composite. If the sentence no longer says what this Module **is**, **does** or **needs**, the content is on the wrong page.

So a Reference Composition table is never keyed by the Modules that take it — a membrane is the same formulation whoever uses it, and a dose chosen by a consumer is a fact about the consumer. Put that figure in the consuming step's `parameters:`, which is where a number belongs when no single constituent page can state it. Expected Behavior describes the Module acting, not a list of the systems it has appeared in.

**Two things this does not forbid.**

- **One Overview sentence naming what the Module composes into.** A leaf has no generated diagram, so that sentence is a reader's only way forward. [sections.md](sections.md#implementations) sets it, and one sentence is the limit.
- **Naming what observed the Module.** A Module with no visible behavior of its own must say what made it visible — "characterized using the deGFP Reporter" states the measurement. The result itself still belongs on the composed page.

`scripts/check-page-layering.py` reports a link to a downstream Module outside Overview. It reports rather than blocks: a rule with a backlog behind it teaches people to skip the output.

## Every page is world-readable, because it is

The test is one question asked of every prose block: **does this describe the Module, or does it describe our work on the Module?** The second kind comes out.

A list of banned phrases will not find it — every page invents new wording. The categories, with examples seen so far, are in [conventions.md](conventions.md#what-never-appears). The examples are a seed, never a checklist.

Anything that is not for the public — status, hedging, provenance of internal documents, who decided what and when, notes between agents and editors — lives in `tmp/` or in the commit message. Preliminary data is published behind the `status:` banner and an `:::{attention}` block. That is what carries the doubt.

Where a page has a gap, tag it: an attention block naming what is missing and who should find it, marked `@Editor:` or `@Developer:`. A cell reading "not documented" records a gap; a tagged block asks someone to close it.

**A person is not a source.** A reader cannot check a ruling, a conversation or someone's word. If a fact needs support, cite the document it came from: a paper, a DevNote, a supplier page. If there is none, keep the fact and tag the gap `@Editor:`. An Editor may cite a result presented at a group meeting as *(Group Meeting, contributor, date)*, or a private exchange as personal communication. An agent must not make either choice.

## Say it once

If a fact appears twice on a page, one of the two is in the wrong section. Decide which section owns it and delete the other.

Across pages the rule holds for conventions rather than for facts. A physical constant can have more than one correct value: cholesterol is 386.654 g/mol under the older atomic weights and 386.66 under IUPAC 2021. Counting pages does not settle which to use, because the majority spelling can be the superseded one. Pick one reference convention for the corpus and follow it everywhere. Two spellings of one constant is a defect even when both are correct.

Be direct. Text that survives review is usually half as long with the same technical content. State requirements; do not argue for them — reasoning belongs in Expected Behavior or nowhere.

Follow Simplified Technical English, pragmatic mode. Do not hard-wrap paragraphs.

## Structural passes

When moving structure rather than rewriting content: nothing is deleted, only relocated. Misplaced content stays on the page and gets reported. The diff should show structure moving, not prose changing.

Renaming *or removing* a heading is a link change — see [conventions.md](conventions.md#headings-and-captions).

**A rule justified by tool behavior rots when you fix the tool.** State a rule from the content model. If the only reason you can give for it is that a checker complains, either the checker is wrong or the rule is not yet understood — and a guide that accumulates workaround-shaped rules ends up holding rules nobody can justify.

**A clean number is not a measurement.** A scan that reports zero has to be shown capable of reporting non-zero before the zero means anything. Precise output is more persuasive than a hand-wave and gets challenged less, so it is the form a wrong answer most easily hides in.

**Internal consistency is not correctness.** A table whose every row reconciles proves the arithmetic was done, not that the inputs were right: a units error propagates cleanly through every row and looks exactly like a sound table. Test a suspect value against something outside it — a second experiment, the supplier's stock format, the paper the design came from.
