# Sections of a Module spec

Order: Overview, Reference Composition, Expected Behavior, Requirements, Implementations, Materials, Downloads, Credits. Omit a section rather than stubbing it empty — except Expected Behavior Contexts, below.

Top-level sections are `#`, subsections `##`. Never skip a level.

## Overview

What the Module is and what it does. Mechanism and schematic figures go here. A figure showing the Module inside a Base or Developer Cell is a system-context figure and belongs in `## Cells` instead.

## Reference Composition

A tab-set: the generated `Module Dependencies` diagram, then one tab per part of the system.

### Naming the tabs

**A tab names a place in the system or a stage in the recipe. Never a property of the table.**

`Working Concentrations` is the failure case. Every composition tab lists working concentrations, so the name says nothing. It appears on exactly the three cascade pages, and always for the same reason: the table was keyed by Module rather than by location, so no location was left to name the tab after. Fix the table and the name follows.

**One axis per tab-set.** Do not mix a compartment (`Cytosol`) with a supply route (`In Situ Expression`) with a figure (`Schematic`) in the same row of tabs. A reader cannot tell whether such tabs are alternatives or additions.

The common vocabulary, in tab order:

| Tab | Holds |
| --- | --- |
| `Module Dependencies` | The generated diagram. Always first. Not a composition. |
| `DNA` | The constructs: name, length, file. |
| `Cytosol` / `Inner Solution` | What is inside. |
| `Membrane` | The bilayer. |
| `Outer Solution` | What is outside. |

`Cytosol` names what fills the compartment; `Inner Solution` names the compartment. Use `Cytosol` when the interior is one, and `Inner Solution` when it is not — a dye liposome's interior is HPTS and Optiprep, with no expression machinery, so it is not a cytosol. These are different claims, not two names for one thing.

Not every Module has all of these. A membrane has no cytosol, a cytosol has no membrane, and a formulation inventory such as `base-cytosol` is organized by recipe stage (`PMix`, `SMix`, `Final Reaction`) instead. The axis stays consistent within a page; which set of names applies follows from what the Module is.

**No figures in this section.** A schematic belongs in `# Overview`.

**Do not nest compartments inside a tab as bold pseudo-headings.** A `Cell` tab containing bold "Inner solution", "Membrane" and "Outer solution" should be three tabs.

### Systems with more than one population

A cascade spans two liposome populations plus the exterior, so compartment names alone do not reach. Put the population at the top level and keep the same axis:

```
Module Dependencies | DNA | Sensing Cell | Substrate SUV | Outer Solution
```

Each population tab carries captioned tables for its own compartments. Captioned tables are not pseudo-headings — the rule above forbids bold text standing in for structure, not multiple tables in one tab.

Keying by location rather than by Module also removes rows that only ever existed to give each Module one. A component expressed from DNA already counted — PLA1 in the London Cascade — is not something the reader adds, so it has no location and needs no row. Its mechanism belongs in `# Overview`.

**A construct appearing in both `DNA` and a location tab is correct.** `DNA` establishes identity — which construct, how long, which file. The location tab gives the dose in context. That duplication is doing two different jobs.

`base-cell` is the reference: `Cytosol | Membrane | Outer Solution`, one axis, no exceptions.

### The tables

**Recurse until the table says something.** Soft limit one layer, hard limit two:

1. Flatten one level.
2. If that layer is non-empty and not merely a restatement of the page, stop.
3. If it is empty or degenerate — "it is Base Cytosol and that's it" — recurse one more level.
4. Never go deeper than two.

`base-cell` is the reference for the output: a short lead-in that adds information, then the full component table.

A lead-in sentence above a table must add something the table does not. `base-cell`'s survives because it names the reporter DNA. Citation-only rows with no numbers are not sufficient — working concentrations should appear.

Column headers are short: "Working concentration", not "Working concentration in combined synthetic cell reaction".

The DNA tab is called `DNA`. Purified proteins get no row there: an expression construct is a DNA row, a purchased reagent a Materials row, MW and UniProt a composition row.

Keep both `<!-- gen:composition-diagram -->` markers and the `# Constituent Modules` heading exactly as they are — the diagram generator matches both with hardcoded strings, and a page missing either drops out silently.

## Expected Behavior

What the reader will see if they follow the page. Write "X Module is expected to…".

Subdivide by Context: `# Expected Behavior` → `## <Context>`. Contexts in use today are Cytosols, Cells and Gels.

> That list is a template convention, not an ontology. No claim is made that it is complete or principled. Do not write a rule that depends on the set being closed.

Three cases, and they differ:

- **Data exists** → `## <Context>` plus the data.
- **Untested but plausible** → `## <Context>` plus a `:::{warning} Not yet validated` block. Do not omit the section.
- **Inapplicable by design** → no section. State it as a Requirement.

Performance data is not its own heading; it lives inside the Context it was measured in.

## Requirements

One line per component that imposes something — not a single generic sentence covering the page. Name a concrete satisfying Module and link it:

> Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).

There is no path dependence. Given a set of Modules to compose you get a set of Requirements, under one composition operator that is fully transitive. "Per route" is not a thing.

Incompatibilities are Requirements, not Expected Behavior. A requirement the reader must satisfy cannot live in a composition tab.

Every Nucleus construct uses a pT7 promoter unless the page says otherwise, because the system is built for PURE and T7 RNAP. Exceptions are *E. coli* sigma-70 promoters and promoterless cloning vectors. Check each page.

State requirements; do not argue for them.

**Known gap.** A Module shipping two promoter variants — PLA1's `T7pro-PLA1-T7term` and `P70lux-PLA1-term` — currently carries both on one page with two Requirements lines. The intended resolution is abstract Functions: an abstract Module abstracts over both constructs and requires only *transcription*, while each concrete Module requires its own promoter. Nucleus has not adopted abstract Modules yet. Until it does, the one-page workaround is accepted.

## Credits

Short and unhedged. Node before Lab. The attested forms:

```
Developed by <Name> (b.next).
Developed by <Name> and <Name> (<X> Node, <Y> Lab).
Developed by the <X> Node (<Y> Lab and <Z> Lab).
Developed by b.next.
Developed by [<Name>](<ORCID URL>) (<X> Node, <Y> Lab).
Module developed by the [<Y> Lab](<URL>).
Module contributed by <Name> (<Y> Lab, <Institution>). Validation data by <Name> (b.next).
Reformulated from <source> by <Name> and <Name> (b.next).
Adapted from [<source>](<URL>) ([Author et al., year](https://doi.org/...)).
```

The DevNote author is the authoritative contributor. Never invent a name, Node, or Lab, and never cite an internal status document here.
