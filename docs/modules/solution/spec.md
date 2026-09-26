---
title: "Solution"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [`container`](../container/spec.md). Refined by [`cytosol`](../cytosol/spec.md), [`outer-solution`](../outer-solution/spec.md).
<!-- /gen:position -->

An abstract Module: the class of things that hold other things in dissolution. Two members: the [Outer Solution](../outer-solution/spec.md) and the [Cytosol](../cytosol/spec.md), each with members of its own.

**The invariant is that what it holds is free to move.** A Solution keeps its solutes in one phase and separates them from nothing. That is the whole of the class, and it is what distinguishes it from its two siblings.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**This class names no composition, so it has no constituents.** Its invariant is an operation, and an operation is not a composition. `glossary.md#T33` in `compositional-biology-theory` makes a Composition an explicit expression giving an object as a combination of others, and nothing gives Solution as a combination of anything. `inputs: {}` and `process_steps: []` are claims here rather than gaps, on the [Container](../container/spec.md) precedent.

:::{table} The three ways a Container holds, and what each one separates.
| Sibling | How it holds | What it separates | Inside is |
| --- | --- | --- | --- |
| [Membrane](../membrane/spec.md) | a closed bilayer | contents from the outside, by a barrier something must cross | a volume |
| [Gel](../gel/spec.md) | a polymer network | nothing, only position | a position |
| **Solution** | dissolution | nothing | one phase |
:::

**Gel and Solution are the pair that look alike and are not.** Neither puts a barrier between what it holds and what is outside, so a reader may take one for the other. **The difference is that a gel fixes position and a solution does not**, and the colorimetric cascades depend on it: they place an enzyme and its substrate in one gel and rely on the two not meeting, which works because the gel holds position.

# Requirements

None stated at this level.

:::{attention} The one measured axiom belongs to a member, not to this class
`compositional-biology-theory`'s `cytosol-does-double-duty.md` measured what survives when the outer phase's axioms are written out. **Exactly one did**: osmolarity matched to the interior, which that file calls a compatibility condition between adjacent strata. [Outer Solution](../outer-solution/spec.md) reached the same figure from this corpus's side and independently.

**It belongs to that member and not to this class**, and the second member is what settles it. A [Cytosol](../cytosol/spec.md) *is* the interior, so it cannot carry an axiom about matching osmolarity across a membrane to one. **What this class does state has not been written**, which is the live gap: both members hold solutes in one phase and separate them from nothing, and no axiom captures it.
:::

# Processes

**None, and the source agrees.** `spec.yml` declares no `process_steps`.

:::{note} The one-member guard fired on this class for about an hour
`one_member_classes()` in [`scripts/render-position.py`](../../../scripts/render-position.py) reported this class when [Outer Solution](../outer-solution/spec.md) was its only member. **Jon ruled [Cytosol](../cytosol/spec.md) a second member the same afternoon and the query is back to 0 of 17.**

**Worth keeping because the guard did its job.** It was recorded here rather than suppressed, with Cytosol named as the exit condition and explicitly not assumed, and the exit arrived. **The parent is the thinner of the two classes** — the theory corpus finds four axioms surviving for Cytosol against one for the outer phase — and a richer class refining a poorer one is what refinement is.
:::

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
