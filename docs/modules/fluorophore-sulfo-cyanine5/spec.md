---
title: "Sulfo-Cyanine5"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Sulfo-Cyanine5 carboxylic acid is a free [Fluorophore](../fluorophore/spec.md): a water-soluble dye that is not attached to a lipid and does not enter a bilayer.

**That is what makes it useful, and it is the opposite of a membrane label.** Encapsulated, it fills the lumen, so a cell shows as a filled circle rather than an outline. A lumen that empties is a lumen whose boundary has failed, which is how this dye reports lysis.

**It is not a [Lipid](../lipid/spec.md)**, which is the one thing separating it from the two membrane labels. [Liss-Rhod PE](../lipid-liss-rhod-pe/spec.md) and [18:1 Cyanine 5 PC](../lipid-cyanine5-pc/spec.md) refine both classes; this one refines Fluorophore alone.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::{table} What [SensorCell[pH ⟶ PLA1]](../ph-sensing-cell/spec.md) records.
| Quantity | Value |
| --- | --- |
| In the lumen | 2 µM, optional |
| Supplier | Lumiprobe 13390 |
| Read at | not recorded |
:::

# Expected Behavior

An encapsulated population shows lumen signal while the boundary holds, and loses it when the boundary fails.

**Loss of the dye is loss of the dye.** Reading it as lysis assumes the dye stays put in the intact state, over the same time and under the same illumination. That assumption belongs to whichever page claims the lysis, and this page does not make it.

# Requirements

Encapsulation. A free dye in the medium reports nothing about any one compartment.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
