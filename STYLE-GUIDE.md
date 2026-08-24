# Nucleus documentation style guide

These pages are **reference documentation** for Module and Process specifications. They are not status trackers, lab notebooks, or progress reports.

Write for the global compositional biology community: engineers and scientists who will use a page to build something. Not for the author, not for an editor, and not for the person who happened to run the experiment.

## The four page types

| Type | Location | Genre |
| --- | --- | --- |
| **Module** | `docs/modules/<name>/spec.md` | Specification — a definition |
| **Process** | `docs/processes/<name>/main.md` | Specification of a procedure — a definition |
| **Implementation** | `docs/implementations/<name>/main.md` | A worked example — a report |
| **Guide** | `guides/` | Tutorial, reference, contribution |

Compositions — chassis, sensing cells, cascades — are Modules. Integration is an activity, not a page type.

## The rules

Every rule lives in exactly one file under [`style-guide/`](style-guide/). Nothing is restated here, so there is one place to change when a rule changes.

| File | Holds |
| --- | --- |
| [`principles.md`](style-guide/principles.md) | What these documents are, and what the other rules follow from. **Read this one first.** |
| [`page-types.md`](style-guide/page-types.md) | What belongs on each page type, and where displaced content goes |
| [`sections.md`](style-guide/sections.md) | Every section of a Module spec, in order |
| [`conventions.md`](style-guide/conventions.md) | Terminology, figures, citations, what never appears, mechanics |

If those four disagree with each other, `principles.md` wins and the other file is wrong.

## Applying them

`.claude/skills/nucleus-style/SKILL.md` is the working procedure: what order to review in, which checks to run, and how to verify a pass did not lose anything. It states no rules of its own — it points here.

Two checks find what reading cannot, because absence is invisible on the page:

```bash
python3 scripts/check-composition-tabs.py    # tabs must cover the dependency graph
python3 scripts/check-implementations.py     # Implementations are Implementations, both ways
```

The full pre-PR command list is in [`conventions.md`](style-guide/conventions.md#before-a-pr).
