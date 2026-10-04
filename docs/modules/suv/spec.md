---
title: "SUV"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [`substrate-cprg-suv`](../substrate-cprg-suv/spec.md).
<!-- /gen:position -->

A **Small Unilamellar Vesicle** — a single lipid bilayer closed around an aqueous interior, in the size regime the name denotes. **What makes a Module a member is the process that closes it**: every member of this class is produced by [Encapsulation: Extrusion](../../processes/encapsulate-suv/main.md).

**One member today**, and the one-member-class caution applies: this class is written because the glossary names it and the route produces it, not because two things needed a parent.

**The house vocabulary has required this distinction for longer than the class has existed.** `glossary.narrows` refuses the bare word "vesicle" at error level and tells the author to *"name the class — GUV, SUV or LUV"*. Three names, and until now no pages behind them.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**A bilayer closed around a payload**, and this class states no formulation: its members differ in both the membrane and what is inside. What they share is the route and the size regime it produces.

**Size.** Set by the extrusion membrane. Its one member targets 400 nm through a 400 nm polycarbonate membrane.

# Members

:::{table} Every Module produced by this route.
| Member |
| --- |
| [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md) |
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
