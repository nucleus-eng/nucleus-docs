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
**Position.** Refines [`container`](../container/spec.md). Refined by [`outer-solution`](../outer-solution/spec.md).
<!-- /gen:position -->

An abstract Module: the class of things that hold other things in dissolution. One member today, the [Outer Solution](../outer-solution/spec.md), which has two of its own.

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

:::{attention} One axiom may belong here, and it is not settled whether it does
`compositional-biology-theory`'s `cytosol-does-double-duty.md` measured what survives when the outer phase's axioms are written out. **Exactly one did**: osmolarity matched to the interior, which that file calls a compatibility condition between adjacent strata.

[Outer Solution](../outer-solution/spec.md) reached the same figure from this corpus's side and independently, and its source records the invariant as *"an osmolarity, not an ingredient list"*. **Whether that axiom belongs to this class or only to that member is open**, and it turns on whether every Solution is suspended around something.
:::

# Processes

**None, and the source agrees.** `spec.yml` declares no `process_steps`.

:::{attention} This class has one member, and the guard says so
`one_member_classes()` in [`scripts/render-position.py`](../../../scripts/render-position.py) reports a class with exactly one member. That query went from 1 to 0 on 2026-09-21, when a LacZ restructure dissolved the last one, and **this class puts it back to 1**.

**Recorded rather than suppressed.** The guard is right that a one-member class is worth a second look. The answer here is an exit condition rather than a change to the tree: [Cytosol](../cytosol/spec.md) is a root today and is an aqueous phase holding solutes, which is this invariant. **Whether it refines this class is not ruled and is not obvious** — the theory corpus finds four axioms surviving for Cytosol against one for the outer phase, so Cytosol is the richer class and may sit beside this one rather than under it.
:::

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
