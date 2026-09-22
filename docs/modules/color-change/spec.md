---
title: "Color Change"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

An abstract Module: the class of color change modules, of which the built readouts are members.
An abstract Module is a Module, and its members refine it.

**The invariant is separation.** An enzyme and its substrate in one compartment react at once,
which is a readout with no off state. Every member of this class holds them apart until the
trigger, so the composition operator is `⊗` and never `⊞`. That is the class, and it is not a rule
anyone has to write down separately: the operator follows from the compartments.

**What varies across the class is which component is encapsulated.**

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

An abstract Module has no reference composition of its own. Each member states its own.

:::{table} The three members, and which are built.
| Member | Encapsulated | Outside | Built by |
| --- | --- | --- | --- |
| Substrate encapsulated | CPRG, in an SUV | LacZ, in the gel | Chicago Node |
| Enzyme encapsulated | LacZ, in the cell | CPRG, in the gel | London Node |
| Double encapsulated | a membrane each | — | **no Node runs this** |
:::

**The pair itself is a parameter of the class, and it is a set of pairs rather than two lists.**
See [Reporter: LacZ Enzyme](../reporter-lacz-enzyme/spec.md) § Requirements.

# Requirements

Requires that the enzyme and the substrate stay in separate compartments until the trigger. This
is the class invariant and every member inherits it.

Requires a trigger that breaks the separation. Every member built so far uses
[Effector: PLA1](../effector-pla1/spec.md), so every member built so far also inherits **PLA1's
low noise floor requirement**. That inheritance is through the implementation, not through this
class: a color change module triggered some other way would not carry it.

:::{attention} What this class requires of its Context is not settled
An abstract Module carries an abstract Context that its members refine, ruled 2026-09-17. **How
much that Context term carries, and how much is left to Requirements, is an open question in the
theory corpus** — `open.md#O21`, narrowed by `D96` and still live. Until it closes, this section
states Requirements only, and the Context this class needs is not written down.

**This is a real gap and not a formality.** The two built members differ in their Context in a way
no Requirement here separates: one runs in a gel with the enzyme dispersed, the other in a gel with
the enzyme encapsulated, and both satisfy every line above.
:::

# Processes

**One, and it has no page.** `spec.yml` declares `separate-enzyme-and-substrate`: *"Hold the enzyme and its substrate apart"*, `packing` over `enzyme`, `substrate`.

**The process is as abstract as its operands**, and no page in this corpus describes it, which is why the source carries `page: null`.

**Corrected 2026-09-21.** Seven class pages asserted an empty Processes section while five of their sources ran a step. A class composes abstract constituents, so composing is not what separates a class from a member. Position in the refinement order is.


# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit
explicitly before this page is merged to `main`.
:::
