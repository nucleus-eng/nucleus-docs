---
title: "Abstract: Pore"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

An abstract Module: the class of pores, of which the three paged pores are members.

**It refines nothing, and that is the point.** A pore is not a kind of container and not a kind of membrane. It is a **component that composes with a membrane** to make that membrane permeable. The theory corpus writes the operation as `passive_transport : Pore[passive] ⊗ Membrane ⟶ Membrane[permeable]`, so a pore and a membrane are two operands and the permeable membrane is the product.

**The invariant is that it lets something cross a boundary it does not itself provide.**

**What varies is what gets through**, and the three members do not agree on how to say it.

:::{attention} The `membrane-pore-*` naming invites a wrong reading
All three members are named `membrane-pore-<something>` and none of them is a Membrane. The name reads as a kind of membrane and means a pore for a membrane. [Abstract: Membrane](../membrane/spec.md) says the same thing from the other side. The pages are not renamed here: the names are load-bearing in links, sources and the DNA repo.
:::

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**Members are a different relation from constituents.** In `compositional-biology-theory`, `glossary.md#T34` makes Constituent a containment relation and `glossary.md#T13` makes membership a matter of what a sort classifies.

**This class has one constituent: the pore-forming agent.** A pore is the thing that makes the hole. What it makes the hole in belongs to the composition the pore enters, not to the pore.

:::{table} The three members, and what each selects on.
| Member | Passive? | Selects on |
| --- | --- | --- |
| [alpha-Hemolysin](../membrane-pore-ahly/spec.md) | yes | **mass**, about 3 kDa, inner diameter 1.6 to 4.6 nm |
| [Cx43](../membrane-pore-cx43/spec.md) | yes | **mass**, about 1 kDa |
| [Gramicidin A](../membrane-pore-gramicidin/spec.md) | yes | **charge and identity** |
:::

:::{attention} `transport` is the abstract operation and is refined by two
**Jon, 2026-09-21:** *"that signature should be `passive_transport`! `active_transport` has selectivity on what is transported, and requires energy. `transport` generally is more abstract and is refined by passive and active transport."*

So there are three operations, not one with a bracket: `transport` at the top, refined by `passive_transport` and `active_transport`. **The energy term and the selectivity are what mark the second**, and every member on this page performs the first refinement.

**This is a correction to `compositional-biology-theory`'s `signature.md` and has been sent there.** That file writes the operation as `transport` with the refinement carried in the argument bracket, `Pore[active]` rather than `transport_active`, which is its `D22`. Jon's reading puts a refinement on the operation as well.
:::

**The split the theory offers does not separate them.** `Pore[passive]` against `Pore[active]`, by the energy spent, is a correct partition that puts all three paged pores in one cell. `Pore[active]` has no paged member in this corpus and that is not a defect: the abstract layer is free on the signature.

**What does separate them is not a partition yet.** Two select on mass and one on charge and identity, and the two that select on mass differ threefold in the cutoff. Nothing in the corpus states that as an axis.

# Requirements

Requires a membrane to make permeable. It is not one, and it does nothing on its own.

**Requires that the membrane survive it.** [Gramicidin A](../membrane-pore-gramicidin/spec.md) is the case: it caused premature lysis in the pH cascade, rupturing CPRG-loaded liposomes and producing nonspecific color, and was left out of the colorimetric demonstration for that reason. See [Effector: PLA1](../effector-pla1/spec.md) § Expected Behavior.

:::{attention} What this class requires of its Context is not settled
An abstract Module carries an abstract Context that its members refine, ruled 2026-09-17. **How much that Context term carries, and how much is left to Requirements, is `open.md#O21`** in the theory corpus, whose expressiveness half closed on Jon's ruling of 2026-09-21 and whose selection half is live.
:::

# Processes

None. An abstract Module names a class; the processes belong to its members.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
