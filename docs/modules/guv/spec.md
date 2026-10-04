---
title: "GUV"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [`vesicle`](../vesicle/spec.md). Refined by [`ahsl-sensing-cell`](../ahsl-sensing-cell/spec.md), [`atc-sensing-cell`](../atc-sensing-cell/spec.md), [`base-cell`](../base-cell/spec.md), [`cell-base-cytosol-popc-chol`](../cell-base-cytosol-popc-chol/spec.md), [`cell-s30-popc`](../cell-s30-popc/spec.md), [`dye-liposomes`](../dye-liposomes/spec.md), [`guv-cprg`](../guv-cprg/spec.md), [`ph-sensing-cell`](../ph-sensing-cell/spec.md), [`theophylline-sensing-cell`](../theophylline-sensing-cell/spec.md).
<!-- /gen:position -->

A **Giant Unilamellar Vesicle** — a single lipid bilayer closed around an aqueous interior, in the size regime the name denotes. **What makes a Module a member is the process that closes it**: every member of this class is produced by [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md).

**Every synthetic cell documented here is a GUV**, which is what makes this the largest of the three classes rather than a carrier-side detail.

**Size and material are independent axes.** This class is the size one; [Liposome](../liposome/spec.md) is the material one, and both refine [Vesicle](../vesicle/spec.md). A member of this class may also be a liposome, so the two parents do not compete.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**A bilayer closed around a payload**, and this class states no formulation: its members differ in both the membrane and what is inside. What they share is the route and the size regime it produces.

**Size.** Micron scale. No diameter is stated by any member, and none is stated here.

# Members

:::{table} Every Module produced by this route.
| Member |
| --- |
| [SensorCell[3OC6-HSL ⟶ PLA1]](../ahsl-sensing-cell/spec.md) |
| [SensorCell[aTc ⟶ PLA1]](../atc-sensing-cell/spec.md) |
| [Base Cell](../base-cell/spec.md) |
| [Cell: Base Cytosol, POPC/Chol (9:1)](../cell-base-cytosol-popc-chol/spec.md) |
| [Cell: S30 Lysate, POPC](../cell-s30-popc/spec.md) |
| [Dye Liposomes](../dye-liposomes/spec.md) |
| [GUV: CPRG](../guv-cprg/spec.md) |
| [SensorCell[pH ⟶ PLA1]](../ph-sensing-cell/spec.md) |
| [SensorCell[theophylline ⟶ LacZ]](../theophylline-sensing-cell/spec.md) |
:::

# Constituent Modules

- [Membrane](../membrane/spec.md) — the bilayer that closes. Which one is the member's choice
- **Payload** — what it closes around, and it has no class page: a cytosol, a substrate or a dye, depending on the member

# Expected Behavior

A member holds its interior apart from the outside until something breaches the bilayer. **The class says nothing about what that is** — lysis, a pore, or no breach at all.

# Requirements

Requires a membrane that closes, and an interior to close around.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
