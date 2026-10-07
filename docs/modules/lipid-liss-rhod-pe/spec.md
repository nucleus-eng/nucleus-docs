---
title: "Liss-Rhod PE"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Lissamine Rhodamine PE (Liss-Rhod PE) is a phosphoethanolamine [Lipid](../lipid/spec.md) carrying a rhodamine dye, and so also a [Fluorophore](../fluorophore/spec.md). It is mixed into a bilayer at a fraction of a mole percent, where it makes the bilayer visible without being enough of the bilayer to change it.

**It reports where the membrane is, and nothing else.** The dye rides on the lipid, so it is in the bilayer rather than in the lumen or the medium. A reader looking for the lumen needs a different dye, and [Sulfo-Cyanine5](../fluorophore-sulfo-cyanine5/spec.md) is the one this corpus uses for that.

**It is an instrument and not part of the recipe.** Its presence or absence does not make one membrane a different membrane, which is why [Membrane](../membrane/spec.md) declares the label optional on the class rather than letting one member claim the dye tells it apart from another.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::{table} What the membranes here use.
| Quantity | Value | Where |
| --- | --- | --- |
| Molar mass | 1301.71 g/mol | [POPC/Chol (9:1)](../membrane-popc-chol-9-1/spec.md) |
| Stock | 1 mg/mL | [POPC/Chol (9:1)](../membrane-popc-chol-9-1/spec.md) |
| In the bilayer | 0.05 mol% to 0.1 mol% | [POPC/Chol (7:3)](../membrane-popc-chol/spec.md), [POPC/Chol (9:1)](../membrane-popc-chol-9-1/spec.md) |
| Read at | 540 nm excitation, 580 nm emission | [Dye Liposomes](../dye-liposomes/spec.md) |
:::

# Expected Behavior

A bilayer containing it is visible in a red channel, as an outline rather than a filled circle. Reading it costs signal: the excitation that makes it visible is what bleaches it, so a long time series ends dimmer than it began.

**One channel cannot separate two populations that both carry it.** Where a sample holds two kinds of liposome and both use this label, the red channel shows both and distinguishes neither.

# Requirements

None.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
