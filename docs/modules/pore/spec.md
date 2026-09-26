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
**Position.** Refines nothing declared. Refined by [`membrane-pore-ahly`](../membrane-pore-ahly/spec.md), [`membrane-pore-cx43`](../membrane-pore-cx43/spec.md), [`membrane-pore-gramicidin`](../membrane-pore-gramicidin/spec.md).
<!-- /gen:position -->

An abstract Module: the class of pores, of which the three paged pores are members.

**It refines nothing, and that is the point.** A pore is not a kind of container and not a kind of membrane. It is a **component that composes with a membrane** to make that membrane permeable. The theory corpus writes it as `passive_transport : Pore ⊗ Membrane ⊗ Cargo[φₚ] ⟶ Membrane[permeable]; passes down ∇` (`signature.md:203`, `main` at `e40f3de`), so a pore and a membrane are two of three operands and the permeable membrane is the product. See the note under Reference Composition.

**The invariant is that it lets something cross a boundary it does not itself provide.**

**What varies is what gets through**, and the three members do not agree on how to say it.

:::{attention} The `membrane-pore-*` naming invites a wrong reading
All three members are named `membrane-pore-<something>` and none of them is a Membrane. The name reads as a kind of membrane and means a pore for a membrane. [Membrane](../membrane/spec.md) says the same thing from the other side. The pages are not renamed here: the names are load-bearing in links, sources and the DNA repo.
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

**Landed in `compositional-biology-theory` at `e40f3de`**, read here at that commit rather than taken on report. Three operations where there was one, `signature.md:201` to `205`:

```
transport         : Pore ⊗ Membrane ⊗ Cargo[φ]            ⟶ Membrane            ; passes across ∇
passive_transport : Pore ⊗ Membrane ⊗ Cargo[φₚ]           ⟶ Membrane[permeable] ; passes down ∇
active_transport  : Pore ⊗ Membrane ⊗ Cargo[φₐ] ⊗ ATP|GTP ⟶ Membrane[pumping]   ; moves against ∇
```

**The bracket moved off the Pore and onto the Cargo**, on Jon's *"refine the argument bracket for the transported thing"*. That is the part that reaches this page. `Pore[passive]` and `Pore[active]` were sorts when this page was written and are not sorts now: there is one `Pore`, and the passive against active distinction lives on the operation and on what it carries.

**The parent is bare on both sides**, `Pore ⊗ Membrane ⊗ Cargo[φ]` in and plain `Membrane` out, so each child adds brackets on both and refinement is one move applied twice. **The direction stays after the semicolon rather than being absorbed into the codomain**, because a permeable membrane is permeable whichever way things cross and only the word `pumping` made the bracket look like it carried direction.
:::

**The split this page was written against no longer exists, and the reason is better than the one given here before.** `Pore[passive]` against `Pore[active]` was a correct partition that put all three paged pores in one cell, so the axis did no work. Since `e40f3de` it is not an axis on the Pore at all: there is one `Pore` sort, and passive against active is a distinction between two operations. **A class cannot be split by a property of an operation it is an argument to.**

**What does separate them is not a partition yet.** Two select on mass and one on charge and identity, and the two that select on mass differ threefold in the cutoff. Nothing in the corpus states that as an axis.

# Requirements

Requires a membrane to make permeable. It is not one, and it does nothing on its own.

**Requires that the membrane survive it.** [Gramicidin A](../membrane-pore-gramicidin/spec.md) is the case: it caused premature lysis in the pH cascade, rupturing CPRG-loaded liposomes and producing nonspecific color, and was left out of the colorimetric demonstration for that reason. See [Effector: PLA1](../effector-pla1/spec.md) § Expected Behavior.

:::{attention} What this class requires of its Context is not settled
An abstract Module carries an abstract Context that its members refine, ruled 2026-09-17. **How much that Context term carries, and how much is left to Requirements, is `open.md#O21`** in the theory corpus, whose expressiveness half closed on Jon's ruling of 2026-09-21 and whose selection half is live.
:::

# Processes

**None here, and that is this class rather than a rule about classes.** No process in this
corpus makes a generic pore, so `spec.yml` carries one constituent and no step.

**An earlier version of this line said the processes belong to a class's members, as though a
class could not run one.** Five of the seven sourced classes do. `membrane` closes a bilayer
from a `lipid`, and `gel` sets from an `outer-solution` and a `polymer`. Their operands carry
`page: null`, so a class composes abstract constituents. **Composition is not what separates a
class from a member.** Position in the refinement order is, which the line below states.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
