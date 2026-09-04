---
title: "TODO: Category: Module Name"
# Title format: "Category: Name" — e.g. "Reporter: deGFP", "Detector: tetR-aTc", "Effector: PLA1"
subtitle: "Module Specification"
status: draft  # draft | unvalidated-published | validated-published — see CLAUDE.md "Page status"
thumbnail: schematic.png
site:
    hide-toc: true
    numbered_references: false
---

<!-- FUNCTIONAL MODULE TEMPLATE.
Use this template for a part you add to someone else's recipe: detectors, reporters,
effectors, emitters, controls, membrane pores, energy modules.

Use the FORMULATION template (spec-formulation.md) instead for something you mix:
cytosols, membranes, chassis, cells, dye liposomes.

The difference is not where the module sits in the composition tree — it is whether the
page documents a recipe or a function. Base Cell is a composed module but reads as a
recipe; a membrane pore is a membrane but reads as a function. -->

# Overview

One paragraph. State what the module is, what it does, and what it adds to or modifies in Base Cytosol. Lead with the module name and its function, and include the parameters that define that function (substrate, pore diameter, purification tag, excitation wavelength). Don't open with preamble — start with the thing:

"The PPK energy Module generates ATP and GTP from AMP and GDP, respectively, using inorganic polyphosphate (100mer) as a phosphate donor."

"The ClpXP control Module uses the ClpXP protease complex to enable the programmable degradation of ssrA-tagged target proteins using ATP for energy."

This paragraph carries the module's Function in the sense CLAUDE.md defines it — the designed behavior. Everything below describes Composition, observed Behavior, and Requirements.

<!-- Status banner — keep consistent with the `status:` frontmatter field (CLAUDE.md "Page
status"). New modules start as `status: draft` with the Draft banner. When complete but not
yet validated in the current Cytosol, switch to `status: unvalidated-published` and use the
"Not yet validated" banner. When validated, set `status: validated-published` and delete the
banner entirely. -->

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

<!-- Use this banner instead when status is `unvalidated-published`:
:::{attention} Not yet validated
This Module has not been validated in Nucleus Cytosol. <Optional specifics, e.g. "Expected
performance data below is from PURExpress.">
:::
-->

<!-- FIGURE PLACEMENT. Three kinds of figure, three homes, no overlap:
  - Mechanism / overview schematic (how it works) → here, in Overview.
  - Module Dependencies diagram (generated, what it is composed of) → a tab in
    Reference Composition below. It depicts composition, so that is where it belongs.
  - System-context figure (the module shown inside a Base or Developer Cell) → the
    "## Cells" subsection under Expected Behavior. See CLAUDE.md.
-->

:::{figure} schematic.png
:name: fig-schematic
:align: center
:width: 75%

TODO: One sentence describing what the schematic shows. Boxes are physical objects; arrows
are processes. If the figure is not original, credit the source and license (e.g. "Figure by
Author et al. used under CC-BY-4.0 / cropped from original.").
:::

# Reference Composition

<!-- What the module is made of: its dependency diagram, its sequences, and what goes in the
tube. Keep the tab order Module Dependencies → DNA → composition tables.

For a composed module, flatten the composition ONE level deep: list each direct constituent
with its working concentration. Do not re-expand a constituent into its own sub-components —
that belongs on the constituent's page. See CLAUDE.md "Composition table depth". -->

:::::{tab-set}

<!-- The marker pair immediately below delimits the GENERATED Module Dependencies tab, built
from this page's `# Constituent Modules` section by the `mermaid-diagrams` skill. Keep BOTH
markers exactly as written — the generator finds its block by matching them, and a page
missing one silently drops out of the generator with no error anywhere. Nothing hand-written
goes between them; edit the composition, not the diagram.

Delete the markers and the tab together if this module has no constituent Modules.

Regenerate after ANY edit to `# Constituent Modules`:
  python3 <nucleus-skills>/skills/mermaid-diagrams/scripts/gen-module-diagrams.py --check
Nothing runs this for you — it is not in CI and not a pre-commit hook. -->

<!-- gen:composition-diagram -->
<!-- /gen:composition-diagram -->

::::{tab-item} DNA

<!-- Sequence-level identity for this module's constructs. Files link to .gb/.gbk/.dna in
nucleus-eng/DNA. Length (bp) is an identity CLAIM, not a label — it must equal the target
file's GenBank LOCUS length. Run `python3 scripts/check-dna-refs.py` to verify.

Do not add a row because a construct name resembles a DNA-repo filename. If the source
construct differs from the Nucleus construct in any way, that is equivalence and not
identity — use the "Nucleus equivalent" block from CLAUDE.md instead of a row here.

Purified proteins do NOT get a table here. A protein is one of three things:
  - an expression construct  → a DNA row above, pointing at its pET28a .gb
  - a purchased reagent      → a Materials row, with vendor and catalog number
  - MW / oligomeric state    → a Reference Composition row
-->

:::{table}
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `TODO: pConstruct-Name` | TODO | [TODO: filename.gb](https://github.com/nucleus-eng/DNA/blob/main/TODO) |
:::

::::

::::{tab-item} Cytosol

<!-- The reaction as assembled. Give stock and final concentrations, and volumes. Where the
module has an induced and uninduced condition, use one column per condition. -->

:::{table} TODO: Composition of the Module in Base Cytosol at reaction concentration
:label: comp-TODO-module

| Component | Stock Concentration | Final Concentration | − TODO (µL) | + TODO (µL) |
| --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO |
| **Total** | | | **TODO** | **TODO** |
:::

::::

:::::

# Expected Behavior

<!-- What the module actually does, per context. One subsection per context in which the
module has been run: Cytosols, Cells, Gels. Delete contexts that do not apply.

Expected Behavior is descriptive, not normative — it is what the thing does, not a promise.
Performance data (dose-response, kinetics, yields) is not its own section; it lives inside
the context subsection it was measured in.

Where a context has not been tested, say so plainly rather than omitting it:
  :::{warning}
  This module has not yet been demonstrated in a synthetic cell.
  :::

Where a context has been tested but the data is not written up, name the gap:
  :::{attention} Missing characterization data
  - TODO: what measurement is missing
  :::
-->

## Cytosols

TODO: What happens in bulk cytosol. Sensitivity, dynamic range, signal and noise floor where
known. Figures and performance tables go here.

## Cells

TODO: What happens when encapsulated. Note whether the module requires transport across the
membrane, and whether the response is uniform or a subpopulation.

# Requirements

<!-- Functional or compositional elements whose presence — or absence — is required for this
module to work as described. This is where incompatibilities live, NOT in Expected Behavior.

Most cytosolic modules require transcription and translation; state it explicitly:
  Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).
-->

TODO: Requirements, one per paragraph or bullet.

# Implementations

<!-- Composed Modules and Implementations that use this Module. Link each. -->

- [TODO: Name](../TODO/spec.md): TODO, one clause on how it is used here.

<!-- Citations & references:
     Do NOT add a manual "# References" section. MyST auto-generates one at the bottom of the
     page from the DOI links cited inline. Cite each source inline where it is discussed —
     narrative ("as shown by [Author et al., YYYY](https://doi.org/…)") or parenthetical.
     DevNotes with a 10.63765/… DOI must be cited via their doi.org link to autogenerate.
     Non-DOI sources stay as plain inline links (issue #138). -->

# Materials

<!-- Critical materials and purchased reagents. Keep vendor links in their own Link column
rather than wrapping the manufacturer name — see docs/processes/make-trna/main.md for a
well-formatted example. If this table is a lab-ready BOM, its `:label:` must be
`bom-<directory-name>` (check-bom-labels.py rule 1). -->

:::{table}
:label: critical-materials

| Material | Description | Manufacturer | Part # | Storage | Link |
| --- | --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO | [link](TODO) |
:::

# Downloads

<!-- Card grid linking to the generated lab-ready protocol PDF and Bill of Materials, matching
the convention on process pages (CLAUDE.md "MyST syntax conventions"). Delete this section if
the module has no generated artifacts.

`generated/` is gitignored — never commit the PDFs themselves. See the `build-boms` skill. -->

::::{grid} 1 1 1 2

:::{card}
:header: **TODO: Step-by-Step Protocol**
:footer: *Implemented using Nucleus Cytosol*
{button}`Download <TODO.pdf>`
:::

:::{card}
:header: **TODO: Materials**
:footer: *Implemented using Nucleus Cytosol*
{button}`Download <TODO.pdf>`
:::

::::

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

Link ORCIDs where available. Where attribution comes from a slide deck or status document
rather than from the team, that caveat belongs on the DevCells program page, not repeated
per module. -->

Developed by TODO.
