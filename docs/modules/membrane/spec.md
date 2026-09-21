---
title: "Abstract: Membrane"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

An abstract Module: the class of lipid bilayers, of which the three paged membranes are members. It refines [Container](../container/spec.md), and an abstract Module is a Module.

**The invariant is a closed lipid bilayer, so what it holds is a volume.** That is what separates it from the [abstract gel](../abstract-gel/spec.md), the other child of Container with members here: a gel fixes a position and leaves what it holds in contact with the outer solution, and a membrane encloses.

**What varies is the lipid composition**, and in this corpus that is the only axis.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**Members are a different relation from constituents.** In `compositional-biology-theory`, `glossary.md#T34` makes Constituent a containment relation and `glossary.md#T13` makes membership a matter of what a sort classifies.

**This class has one constituent and it is the only one it needs.** A bilayer is lipid in a bilayer arrangement. Nothing else is required to be a membrane, and everything that makes one membrane differ from another is which lipids.

:::{table} The three members.
| Member | Lipids | Node |
| --- | --- | --- |
| [London Membrane: POPC](../membrane-popc/spec.md) | POPC with DSPE-PEG2000 | London |
| [Base Membrane: POPC/Chol](../membrane-popc-chol/spec.md) | POPC with cholesterol | shared |
| [Chicago Membrane: POPC/Chol](../membrane-popc-chol-chicago/spec.md) | POPC with cholesterol and Liss Rhod PE | Chicago |
:::

:::{attention} A Pore is not a member of this class
[Abstract: Pore](../pore/spec.md) is a **component that composes with a membrane**, not a kind of one. The theory corpus writes the operation as `passive_transport : Pore[passive] ⊗ Membrane ⟶ Membrane[permeable]`, so a pore and a membrane are two operands and the permeable membrane is the product.

**The three paged pores are named `membrane-pore-*` and that naming invites the wrong reading.** They refine [Abstract: Pore](../pore/spec.md), which refines nothing here.
:::

# Requirements

Requires a lipid phase to form from, and a process that closes it. Which process is a member's business: the corpus forms bilayers by phase transfer and by film rehydration.

:::{attention} What this class requires of its Context is not settled
An abstract Module carries an abstract Context that its members refine, ruled 2026-09-17. **How much that Context term carries, and how much is left to Requirements, is `open.md#O21`** in the theory corpus, whose expressiveness half closed on Jon's ruling of 2026-09-21 and whose selection half is live.
:::

# Processes

None. An abstract Module names a class; the processes belong to its members.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
