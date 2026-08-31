---
title: "TODO: Category: Module Name"
# Title format: "Category: Name" — e.g. "Base: Cytosol", "Base Membrane: POPC/Chol", "Chicago Chassis"
subtitle: "Module Specification"
status: draft  # draft | unvalidated-published | validated-published — see CLAUDE.md "Page status"
thumbnail: schematic.png
site:
    hide-toc: true
    numbered_references: false
---

<!-- FORMULATION TEMPLATE.
Use this template for something you mix: cytosols, membranes, chassis, cells, dye liposomes.

Use the FUNCTIONAL MODULE template (spec-functional.md) instead for a part you add to
someone else's recipe: detectors, reporters, effectors, emitters, controls, pores, energy.

The difference is not where the module sits in the composition tree — it is whether the page
documents a recipe or a function. Base Cell is a composed module but reads as a recipe; a
membrane pore is a membrane but reads as a function. -->

# Overview

One paragraph. State what the formulation is, what it is for, and how it differs from its
siblings. Lead with the thing itself, then place it against the alternatives a reader might
confuse it with:

"The Chicago Membrane is a 90:10 POPC:cholesterol phospholipid bilayer used in every liposome
in the Chicago DevStudio Demo. Compare to Base Membrane (70:30 POPC:cholesterol), which uses
more cholesterol, and London Membrane, which is pure POPC. Optionally, this membrane can
include 0.1 mol% fluorescently tagged lipids to aid visualization."

For a chassis or cell, name the demo it serves and the constituents it combines:

"The London Chassis is used for the London Node's DevStudio Demo and combines S30 Lysate with
a 100% POPC membrane. This cell is extended in downstream demo variants by adding sensing and
reporter modules."

<!-- Status banner — keep consistent with the `status:` frontmatter field (CLAUDE.md "Page
status"). Delete the banner entirely once `status: validated-published`. -->

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

<!-- What goes in the tube, as tabs. The usual tab set for an encapsulated formulation is
Inner Solution (or Cytosol) → Membrane → Outer Solution. For a membrane-only page, a single
composition table with an optional-additives table is enough and no tab-set is needed.

Flatten a composed formulation ONE level deep: each direct constituent gets a line with its
working concentration or fraction. Do not re-expand a constituent into its own components —
Base Cytosol's ~100 PURE-system components stay on Base Cytosol's page. Citation-only rows
with no numbers are not sufficient. See CLAUDE.md "Composition table depth". -->

:::::{tab-set}

::::{tab-item} Inner Solution

:::{table}
:label: comp-TODO-inner

| Component | Stock concentration | Final concentration | Volume for one reaction (µL) |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |
| Total volume (µL) | | | TODO |
:::

::::

::::{tab-item} Membrane

:::{table}
:label: comp-TODO-membrane

| Component | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) | Notes |
| --- | --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO | TODO |
:::

TODO: one sentence pointing at the membrane's own spec for the full formulation, if this page
is not that spec.

::::

::::{tab-item} Outer Solution

:::{table}
:label: comp-TODO-outer

| Component | Concentration |
| --- | --- |
| TODO | TODO |
:::

TODO: state the osmolarity target, and that it should be matched empirically with a
vapor-pressure osmometer rather than assumed.

::::

:::::

# Expected Behavior

<!-- What you should see when the formulation is prepared correctly — yield, morphology,
size, brightness, stability over the incubation. Descriptive, not a promise.

Where a context has not been tested, say so plainly:
  :::{warning}
  This formulation has not yet been demonstrated in a synthetic cell.
  :::
-->

TODO: What a correct prep looks like, and how you would know it failed.

# Processes

<!-- A pointer at the assembly process, not a restatement of it. Protocol steps belong on the
Process page. Use "Process" — not "Protocols" — for this section.

If a method detail has nowhere else to live because no Process page covers it yet, keep it
here rather than dropping it, and open an issue for the Process page. Never delete sourced
method detail on the grounds that it is misplaced. -->

TODO: This formulation is assembled using [TODO: Process Name](../../processes/TODO/main.md).

# Materials

<!-- Critical materials and purchased reagents. Keep vendor links in their own Link column.
If this table is a lab-ready BOM, its `:label:` must be `bom-<directory-name>` — the label
must keep matching the directory name (check-bom-labels.py rule 1). -->

:::{table}
:label: bom-TODO

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO | TODO | TODO | [link](TODO) |
:::

# Credits

<!-- THE DEVNOTE AUTHOR IS THE AUTHORITATIVE CONTRIBUTOR. Where this module has a backing
DevNote, credit its author. Only fall back to the variants below when no DevNote exists.

Do not upgrade a collective attribution into a person-level one, and do not invent a Node or
Lab. "Node" is a proper noun (Chicago Node, London Node).

  Person, b.next:  Developed by <Name> (b.next).
  Person, node:    Developed by <Name> and <Name> (<X> Node, <Y> Lab).
  Collective:      Developed by the <X> Node (<Y> Lab and <Z> Lab).
  External group:  Module developed by the [<Y> Lab](URL).
  Withheld:        Contributor attribution is pending confirmation. <Why.>
-->

Developed by TODO.
