---
title: "Membrane"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [`container`](../container/spec.md). Refined by [`membrane-popc`](../membrane-popc/spec.md), [`membrane-popc-chol`](../membrane-popc-chol/spec.md), [`membrane-popc-chol-chicago`](../membrane-popc-chol-chicago/spec.md).
<!-- /gen:position -->

An abstract Module: the class of lipid bilayers, of which the three paged membranes are members. It refines [Container](../container/spec.md), and an abstract Module is a Module.

**The invariant is a closed lipid bilayer, so what it holds is a volume.** That is what separates it from the [abstract gel](../gel/spec.md), the other child of Container with members here: a gel fixes a position and leaves what it holds in contact with the outer solution, and a membrane encloses.

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
[Pore](../pore/spec.md) is a **component that composes with a membrane**, not a kind of one. The theory corpus writes the operation as `passive_transport : Pore ⊗ Membrane ⊗ Cargo[φₚ] ⟶ Membrane[permeable]; passes down ∇` (`signature.md:203`, `main` at `e40f3de`), so a pore and a membrane are two of three operands and the permeable membrane is the product.

**The three paged pores are named `membrane-pore-*` and that naming invites the wrong reading.** They refine [Pore](../pore/spec.md), which refines nothing here.
:::

# Requirements

Requires a lipid phase to form from, and a process that closes it. Which process is a member's business: the corpus forms bilayers by phase transfer and by film rehydration.

:::{attention} What this class requires of its Context is not settled
An abstract Module carries an abstract Context that its members refine, ruled 2026-09-17. **How much that Context term carries, and how much is left to Requirements, is `open.md#O21`** in the theory corpus, whose expressiveness half closed on Jon's ruling of 2026-09-21 and whose selection half is live.
:::

# Processes

**One, and it has no page.** `spec.yml` declares `close-the-bilayer`: *"Close the bilayer"*, `mixing` over `lipid`.

**The process is as abstract as its operands**, and no page in this corpus describes it, which is why the source carries `page: null`.

**Corrected 2026-09-21.** Seven class pages asserted an empty Processes section while five of their sources ran a step. A class composes abstract constituents, so composing is not what separates a class from a member. Position in the refinement order is.


# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
