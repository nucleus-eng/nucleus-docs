---
title: "Cytosol"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [`solution`](../solution/spec.md). Refined by [`base-cytosol`](../base-cytosol/spec.md), [`s30-lysate`](../s30-lysate/spec.md), [`sensor-cytosol`](../sensor-cytosol/spec.md).
<!-- /gen:position -->

A class: a cell-free expression mix, holding everything a transcription and translation
reaction needs. Two members.

**It refines nothing, and it exists because the demo integration paths disagree.** The AHSL integration path builds its
sensor cytosol on [S30 Lysate](../s30-lysate/spec.md). The aTc and pH integration paths build theirs on
[Base Cytosol](../base-cytosol/spec.md). A meet over the three integration paths reaches that slot and finds
two occupants, so the slot needs a name.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**Members are a different relation from constituents.** In `compositional-biology-theory`,
`glossary.md#T34` makes Constituent a containment relation and `glossary.md#T13` makes
membership a matter of what a sort classifies.

**This class names what its members are for, not what they are made of**, and that is a
measurement rather than a style choice.

:::{table} The two members share one constituent and no process.
| Member | Operator | Constituents |
| --- | --- | --- |
| [Base Cytosol](../base-cytosol/spec.md) | `mixing` | S-mix, tRNA, P-mix, ribosomes, RNase inhibitor |
| [S30 Lysate](../s30-lysate/spec.md) | `mixing` | S30 premix, S30 extract, amino acid mix, RNase inhibitor |
:::

**Both mix, two of two.** A cell-free reaction that kept its machinery in separate compartments
would not run, so `mixing` is the invariant and `packing` is not available to this class.

**The only shared constituent is the RNase inhibitor**, which protects the reaction rather than
performing it. The source records that reading as an open item instead of asserting it.

# Requirements

Requires nothing of a Context that its members do not require. One member is a defined
mix and the other is a cell extract, so their tolerances differ and belong to their own pages.

# Constituent Modules

- [Expression machinery](#) — a defined mix in one member, a cell extract in the other. No page: a class composes abstract constituents.

# Processes

<!-- check-composition-tabs: waived, this page carries no generated diagram -->

See the composition source. The step this class runs is stated there, and it has no page
because no process in this corpus performs it at this grain.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit
explicitly before this page is merged to `main`.
:::
