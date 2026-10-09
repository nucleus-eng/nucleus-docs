---
title: "Pore"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [Membrane Pore: alpha-hemolysin](../membrane-pore-ahly/spec.md), [Membrane Pore: Cx43](../membrane-pore-cx43/spec.md), [Membrane Pore: Gramicidin A](../membrane-pore-gramicidin/spec.md).
<!-- /gen:position -->

A class: a pore-forming agent that composes with a membrane to make that membrane permeable to a cargo.

Every member lets something cross a boundary it does not itself provide. The pore is the one constituent: a protein in two members and a peptide in the third. The membrane it opens is not part of the pore. That membrane belongs to the composition the pore enters.

The member pages are named `membrane-pore-<name>`, which means a pore for a membrane. None of them is a Membrane.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [alpha-Hemolysin](../membrane-pore-ahly/spec.md) | A protein pore of seven monomers. It selects on **mass**: about 3 kDa, through an inner diameter of 1.6 to 4.6 nm |
| [Cx43](../membrane-pore-cx43/spec.md) | A protein hemichannel of six connexins. It selects on **mass**: about 1 kDa |
| [Gramicidin A](../membrane-pore-gramicidin/spec.md) | A peptide that dimerizes across the bilayer into a channel. It selects on **charge and identity**, not size: it conducts monovalent cations and protons |

# Expected Behavior

A Pore is expected to let a cargo cross a membrane that would otherwise hold it. Transport is passive. The cargo equilibrates across the membrane, down its gradient, so what crosses in also crosses out.

# Requirements

Requires a membrane to insert into (e.g. [Membrane: POPC/Chol (7:3)](../membrane-popc-chol/spec.md)).

Requires that the outer solution carry any cargo the interior consumes and the pore passes (see [Outer Solution](../outer-solution/spec.md)).

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
