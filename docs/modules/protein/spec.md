---
title: "Protein"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [LacZ Enzyme](../reporter-lacz-enzyme/spec.md), [XylE](../xyle-protein/spec.md).
<!-- /gen:position -->

A class: a Module whose subject is a protein.

Every member is a chain of amino acids, and is identified by that chain rather than by what it does. Members do different things. The class fixes what they are made of, which is what decides how a protease treats them.

A Module that uses a protein is not a member. A Module whose Function is performed by a protein it expresses has that protein as a product, and the Module's subject is the behavior rather than the molecule.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [LacZ Enzyme](../reporter-lacz-enzyme/spec.md) | Beta-galactosidase, supplied purified. The page's subject is the protein itself, not a reaction that uses it. |
| [XylE](../xyle-protein/spec.md) | Catechol 2,3-dioxygenase. Supplied as a DNA template and expressed, but the page's subject is the enzyme. |

# Expected Behavior

Any member is digested by a broad-spectrum protease that reaches it. A step that digests protein in a compartment digests every member present in that compartment, whatever each one does.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
