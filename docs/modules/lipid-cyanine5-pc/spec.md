---
title: "18:1 Cyanine 5 PC"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

18:1 Cyanine 5 PC is a phosphocholine [Lipid](../lipid/spec.md) carrying a cyanine dye, and so also a [Fluorophore](../fluorophore/spec.md). It labels a bilayer in a far-red channel, where [Liss-Rhod PE](../lipid-liss-rhod-pe/spec.md) labels one in a red channel.

**Its reason for existing here is the second channel.** Two populations of liposome in one sample can only be told apart if one carries a label the other does not. A second membrane dye is what makes that possible.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::{table} What [Membrane: POPC](../membrane-popc/spec.md) records.
| Quantity | Value | State |
| --- | --- | --- |
| In the bilayer | 0.1 mol% | The target for the labeled variant |
| Stock | 1 mg/mL | **Disputed.** One record gives 25 mg/mL, which would put the dye at about 2.42 mol% |
| Read at | not recorded | No page here states its excitation or emission |
:::

# Expected Behavior

A bilayer containing it is visible in a far-red channel. Reading it bleaches it, as it does any [Chromophore](../chromophore/spec.md).

# Requirements

None.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
