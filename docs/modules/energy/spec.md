---
title: "Energy"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [Energy: PPK](../energy-ppk/spec.md).
<!-- /gen:position -->

A class: a Module whose Function is to turn a spent nucleotide back into a usable one, such as AMP into ATP.

What every member shares is that it refills a store the reaction draws on. [Base Cytosol](../base-cytosol/spec.md) also makes ATP again, from creatine phosphate, but as one of a cytosol's own functions. It is a Cytosol and not a member of this class.

**One member today, as [Lysis](../lysis/spec.md) has.** A class is written when a Module needs its functional parent, and it does not wait for a second member.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [Energy: PPK](../energy-ppk/spec.md) | PPK2 on 100-mer polyphosphate, which makes ATP from AMP and GTP from GDP. |

# Expected Behavior

A member turns a spent nucleotide back into a usable one, so the reaction it supplies draws on a store that can be refilled.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
