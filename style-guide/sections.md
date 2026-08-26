# Sections of a Module spec

Order: Overview, Reference Composition, Expected Behavior, Requirements, Implementations, Processes, Materials, Downloads, Credits. Omit a section rather than stubbing it empty — except Expected Behavior Contexts, below.

Top-level sections are `#`, subsections `##`. Never skip a level.

## Overview

What the Module is and what it does. Mechanism and schematic figures go here. A figure showing the Module inside a Base or Developer Cell is a system-context figure and belongs in `## Cells` instead.

## Reference Composition

A tab-set: the generated `Module Dependencies` diagram, then one tab per part of the system.

**Derive the tab set. Do not read it off the table that is already there.** Enumerate the transitive closure of `# Constituent Modules` — the generated diagram already computes it — and add anything the Requirements name. Every compartment and every genetically encoded part in that closure gets a tab.

Requirements imply tabs too. A lysis Module requires a membrane, because there is nothing to lyse without one, so it carries a Membrane tab even though no membrane appears in its own constituent list.

**A tab may say the composition is not documented. It may not be absent.** An absent Membrane tab reads as "this Module has no membrane"; a Membrane tab saying the composition is undocumented reads as the truth. Where a value is missing, say so in the cell and [tag the gap](principles.md#say-it-once). `scripts/check-composition-tabs.py` enforces this.

**Composition is the design, not a completed run.** The tabs state how the Module works when it works — not a transcript of the best experiment anyone has managed. A reaction that omits one of the Module's own constituents is a component test: evidence that a part works, and so Expected Behavior. Where the design values are not yet backed by an assembled run, keep them and mark it with an `@Editor:` block.

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

`Inner Solution` is the compartment inside a liposome, whatever the liposome carries — a lumen holding substrate is an inner solution, not a `Luminal Cargo`. `Cytosol` names what fills that compartment when the contents are an expression system. Use `Cytosol` when the interior is one, and `Inner Solution` when it is not — a dye liposome's interior is HPTS and Optiprep, with no expression machinery, so it is not a cytosol. These are different claims, not two names for one thing.

Not every Module has all of these. A membrane has no cytosol, a cytosol has no membrane, and a formulation inventory such as `base-cytosol` is organized by recipe stage (`PMix`, `SMix`, `Final Reaction`) instead. The axis stays consistent within a page; which set of names applies follows from what the Module is.

**No figures in this section.** A schematic belongs in `# Overview`.

**Do not nest compartments inside a tab as bold pseudo-headings.** A `Cell` tab containing bold "Inner solution", "Membrane" and "Outer solution" should be three tabs.

### Systems with more than one population

A cascade spans two liposome populations plus the exterior, so compartment names alone do not reach. Put the population at the top level and keep the same axis:

```
Module Dependencies | DNA | AHL Sensing Cell | Substrate SUV | Outer Solution
```

Population tabs take the Module's real name. `AHL Sensing Cell`, not `Sensing Cell` — a cascade page usually sits beside two others whose sensing cells are different Modules.

Each population tab carries captioned tables for its own compartments. Captioned tables are not pseudo-headings — the rule above forbids bold text standing in for structure, not multiple tables in one tab.

Keying by location rather than by Module also removes rows that only ever existed to give each Module one. A component expressed from DNA already counted — PLA1 in the London Cascade — is not something the reader adds, so it has no location and needs no row. Its mechanism belongs in `# Overview`.

**A construct appearing in both `DNA` and a location tab is correct.** `DNA` establishes identity — which construct, how long, which file. The location tab gives the dose in context. That duplication is doing two different jobs.

`base-cell` is the reference: `Cytosol | Membrane | Outer Solution`, one axis, no exceptions.

**This section contains composition tables and nothing else.** Preparation parameters — target diameter, extrusion passes, purification method, storage — describe how the Module is made, so they belong under `# Processes`. Not evidence, not sourcing notes, not another Module's result. A table of the reaction parameters that produced a result is Expected Behavior — and where the result belongs to a different Module, it belongs on that Module's page.

State a gap inside the tab it affects, in the row where the number would go. A tab holding no table is not a tab.

**A composition tab carries a table, not a sentence pointing at another page.** Where a Module inherits its membrane or cytosol from a chassis, reproduce the table and name the source in the caption — a reader composing this Module should not have to open two more pages to learn its lipid fractions. The one exception is a Module whose composition is not specific to any one host: [Effector: PLA1](../docs/modules/effector-pla1/spec.md) acts on any phospholipid membrane it reaches, so it names the membranes it has been used with instead of inventing a single table.

### The tables

**One contributor means no line-item table.** A composed Module's tab lists each constituent that contributes to that compartment. Where exactly one does, the abstraction adds nothing — a union over a single set is that set — so give the constituent's own composition table instead of a row pointing at it. A tab whose only informative cell reads "unchanged from X" is a link wearing a table's clothes. Keep the line-item form only where two or more constituents genuinely combine.

**Optional components do not change a Module's identity.** Two compositions that differ only in a component the spec marks optional are the same Module. The Chicago Membrane lists `(Optional) Liss Rhod PE` at 0.1%, so a membrane written as `89.9 / 10 / 0.1` and one written as `9:1 POPC:cholesterol` are the same membrane, not two formulations. Do not write a note distinguishing them.

More generally: deciding whether some material *is* a named Module is not a comparison of two tables for equality. It is a question of whether the material satisfies that Module's specification, and a specification tolerates what it marks optional. Comparing tables cell by cell forces an exact match the spec never asked for, and every optional row then reads as a difference.

**A DNA tab lists unique sequences; a compartment tab lists what is added.** The two differ whenever parts are combined before use — two annealed oligos are two sequences and one pipetting step. Give every sequence its own row in the DNA tab, and the combined reagent one row in the tab for the compartment it enters, quoted by whichever strand the rest of the corpus quotes.

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

**Say what measured it.** Every result names the Process that produced it, as a link:

> Colour developed within 3 h at 37 °C, scored by eye — see [Colorimetric Readout](../docs/processes/colorimetric-readout/main.md).

A result with no named readout is not yet a claim about the Module. "Only slightly discernible" describes the instrument as much as the biology, and nothing on the page tells a reader which. That is the live case on [London Cascade](../docs/modules/london-cascade/spec.md): the +AHL/−AHL gap may be a weak signal or a weak readout, and the two call for opposite work — more optimisation, or a better assay.

Where no Process page exists for the readout, say what was used in prose and mark it `@Editor:`. Do not drop the detail because there is nowhere tidy to link.

**How it was read decides what can be known.** A bulk measurement reports a population average and cannot show how much individual cells differ; imaging individual liposomes can. Two readouts of one Module are not competing versions of a result — they answer different questions, and both belong under the Context they were run in.

## Requirements

One line per component that imposes something — not a single generic sentence covering the page. Name a concrete satisfying Module and link it:

> Requires pT7 transcription and translation (e.g. [Base Cytosol](../docs/modules/base-cytosol/spec.md)).

**One clause per line.** A sentence that joins three requirements with "and" is three requirements. A reader checking whether their system qualifies must first take the sentence apart. Split it yourself.

**`e.g.` names something that satisfies the Requirement. `see` names a cross-reference.** Do not use `e.g.` for the Module that *imposes* the constraint — it reads as though that Module meets it. "Requires that no LacZ protein share a compartment with CPRG (e.g. [LacZ Reporter])" has it backwards: the reporter is the source of the requirement, so write `see`.

There is no path dependence. Given a set of Modules to compose you get a set of Requirements, under one composition operator that is fully transitive. "Per route" is not a thing.

**Dependence on configuration is a different thing, and it is real.** A Module that ships two constructs has a Requirement per construct, and composing it picks one. Write the condition as a trailing clause so the line still reads as a single Requirement:

> Requires sigma-70 transcription and translation, when using `P70lux-PLA1-term` (e.g. [S30 Lysate](../docs/modules/s30-lysate/spec.md)).

Not "Using `P70lux-PLA1-term` requires…", which buries the Requirement behind its condition. Order does not matter; which variant you built does. See the Known gap below — it is the same thing.

A **Requirement** is something the reader must provide, or must avoid, for the Module to function. An **observed property** of the system is Expected Behavior, even when it sounds like a warning. "Gramicidin A causes premature rupture" is a finding. "Do not include gramicidin A" would be a requirement. Write the finding.

**A prohibition asserts a result. Point at the result.** Telling a reader to avoid something claims the system fails otherwise, and that claim needs a figure, a dataset or a citation behind it somewhere on the page. Where none exists, the honest form is the control that would settle it, tagged `@Editor:` like any other gap. `ph-cascade` writes both forms four lines apart — "Do not add gramicidin A to the colorimetric configuration" against "Requires a control that separates sensing-driven color from acid-driven leakage." The second is the one to copy.

A hedge in the supporting prose and an imperative in this section cannot both be right. Theophylline against LacZ is the other page-set where they are, and its own admonition says the mechanism is unestablished.

A requirement the reader must satisfy cannot live in a composition tab.

**Say when the page already satisfies a Requirement it inherited.** A composed Module takes on its constituents' Requirements and can also meet them, and the reader cannot tell the two apart without being told. `atc-sensing-cell` writes the met case:

> Requires pT7 transcription and translation (e.g. [Base Cytosol](../docs/modules/base-cytosol/spec.md)), supplied here by the [Chicago Chassis](../docs/modules/chicago-chassis/spec.md).

**A composed Module lists what a composer must still supply, not everything its parts require.** That follows from "say it once" and from writing for an unknown composer: the constituent pages already hold their own Requirements, and a reader who needs the full set gets it by following the links. Restating an inherited Requirement that this page satisfies makes the page look harder to use than it is; dropping one it does *not* satisfy makes it look easier. Neither is recoverable from the text today.

Every Nucleus construct uses a pT7 promoter unless the page says otherwise, because the system is built for PURE and T7 RNAP. Exceptions are *E. coli* sigma-70 promoters and promoterless cloning vectors. Check each page.

State requirements; do not argue for them.

**Known gap.** A Module shipping two promoter variants — PLA1's `T7pro-PLA1-T7term` and `P70lux-PLA1-term` — currently carries both on one page with two Requirements lines, written with the trailing-clause form above. The intended resolution is abstract Functions: an abstract Module abstracts over both constructs and requires only *transcription*, while each concrete Module requires its own promoter. Nucleus has not adopted abstract Modules yet. Until it does, the one-page workaround is accepted.

## Implementations

Only pages under `docs/implementations/`. A cascade is a Module however composed it is, and a Module that uses this Module does not belong here either. On a composed Module the dependency diagram already shows those relations. A leaf Module has no diagram, so name what it composes into in one Overview sentence.

The relation is symmetric: if an Implementation is built from this Module, this Module lists that Implementation. `scripts/check-implementations.py` checks both halves.

Every Module link inside this section reads as a claim, prose included. Naming the cascade a reader passes through asserts that a cascade is an Implementation, and it is not — it is a Module however composed it is. Describe the path in words and link only the Implementation. A caveat about the entries goes in a tagged admonition after the list, as `reporter-xyle` does.

## Processes

Link every Process page related to this Module, in the order a bench user meets them. That means both directions: the processes that **build** the Module, and the processes that **use** it — an assay that reads it, a downstream step it feeds. A page listing only its own preparation hides half of what a reader came for. Where the relation is not obvious from the title, gloss it in a few words.

Include any preparation parameters that are not composition — target size, extrusion passes, purification method, storage before use. A number that describes *how you make it* is process data even when it sits in a table.

If no Process page covers the combination, say so in one sentence and stop. "No process page documents assembling this cascade end to end." Do not explain what a reader should not assume, and do not leave instructions for a future editor — those go in `tmp/`.

## Credits

Credits is **one sentence**. Not a paragraph, and never a second paragraph carrying a caveat. Validation status belongs in Expected Behavior or the status banner; whether attribution has been confirmed belongs in `tmp/`. Node before Lab. The attested forms:

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
