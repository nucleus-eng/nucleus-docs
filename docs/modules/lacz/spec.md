---
title: "LacZ"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [LacZ DNA template](../lacz-dna/spec.md), [LacZ Enzyme](../reporter-lacz-enzyme/spec.md).
<!-- /gen:position -->

A class: β-galactosidase, however it is supplied.

Every member delivers β-galactosidase activity. An operand that names LacZ takes either member, so a Module that needs the enzyme does not have to choose how it is supplied. [LacZ Reporter](../reporter-lacz/spec.md) can express the enzyme from a template or add it purified.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

**Identity.** [UniProt P00722](https://www.uniprot.org/uniprotkb/P00722/entry) — Beta-galactosidase, *Escherichia coli K12*, 1024 residues.

# Members

| Member | What makes it a member |
| --- | --- |
| [LacZ DNA template](../lacz-dna/spec.md) | A DNA construct, `T7pro-LacZ-T7term`, that carries no activity itself. It requires an expression system to make the enzyme. |
| [LacZ Enzyme](../reporter-lacz-enzyme/spec.md) | Purified β-galactosidase from *E. coli*. It requires a supplier. |

# Expected Behavior

Either member gives β-galactosidase activity, which converts [CPRG](../substrate-cprg/spec.md) from yellow to red. The members differ in what they require, not in what they do.

# Constituent Modules

- A source of β-galactosidase — a template in one member, the purified protein in the other

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit
explicitly before this page is merged to `main`.
:::
