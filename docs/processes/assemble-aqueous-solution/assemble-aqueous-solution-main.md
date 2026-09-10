---
title: Assemble Aqueous Solution
status: draft
---

# Overview

Assemble Aqueous Solution combines aqueous components into a single compartment, where they share the volume and each other's resources. It is the most general mixing act in this documentation, and every process below it inherits its behavior rather than choosing one.

Its two instances:

- [Assemble Cytosol](../assemble-cytosol/assemble-cytosol-main.md) — a reaction that will be encapsulated. Reserves a slot for whatever a particular reaction adds.
- [Assemble Outer Solution](../assemble-outer-solution/main.md) — the solution encapsulated things sit in, and that a gel dissolves into. Reserves nothing.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# What every instance shares

**The result is one compartment.** Everything combined shares the volume, the buffer and whatever else is in it. Nothing is separated by a boundary, which is what distinguishes this from encapsulation and gel embedding — those produce results whose parts keep their own compartments.

**The operator lives here, not on the derivatives.** Because the result is one compartment, this process mixes; and because every derivative is an instance of it, every derivative mixes too. That is inherited rather than decided. A newly written derivative needs no decision about which operator applies — the question is already answered by what it is an instance of.

This matters when reading a composition: a step's operator is a fact about its process, not a property of the particular things being combined. Module composition sources record it in an `abstract:` field naming this process.

# What the two instances do not share

| | Assemble Cytosol | Assemble Outer Solution |
| --- | --- | --- |
| Reserved headroom | yes — a fixed slot in a pinned total | none |
| What it becomes | the inside of a synthetic cell | the outside, and the gel matrix |
| Osmolarity | set by its own recipe | matched to the cytosol it will surround |

**The headroom is the real difference.** A cytosol recipe pins its total volume and holds part of it back, so a sensing construct or a reporter enzyme can be added without diluting anything else. An outer solution has no such slot: it is made to a composition and used.

The two are matched rather than independent. An outer solution is formulated to the osmolarity of the cytosol it will surround, because a mismatch drives encapsulated contents across the bilayer before anything else can happen.

# Requirements

Requires that everything combined is soluble and stable together at the working concentrations, since there is no boundary keeping any of it apart.

Requires, where the result will meet an encapsulated population, that its osmolarity is matched to that population's interior.

# Processes

- [Assemble Cytosol](../assemble-cytosol/assemble-cytosol-main.md)
- [Assemble Outer Solution](../assemble-outer-solution/main.md)
