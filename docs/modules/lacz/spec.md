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
**Position.** Refines nothing declared. Refined by [`lacz-dna`](../lacz-dna/spec.md), [`reporter-lacz-enzyme`](../reporter-lacz-enzyme/spec.md).
<!-- /gen:position -->

A class: beta-galactosidase, however it is supplied. Two members.

**It exists because an operand must accept either form.** [LacZ Reporter](../reporter-lacz/spec.md) can be built by expressing the enzyme from a template or by adding it purified, and its operand should not have to choose. An operand naming a class means any member satisfies it, which is how [Cell](../cell/spec.md) takes a [Cytosol](../cytosol/spec.md) and either base cytosol or S30 lysate answers.

**It refines nothing.** An enzyme is not a container, a cytosol or a reporter. It is a component a reporter reaction takes.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::{table} The two members differ in what they require, not in what they do.
| Member | Form | Requires |
| --- | --- | --- |
| [LacZ DNA template](../lacz-dna/spec.md) | a construct | an expression system |
| [LacZ Enzyme](../reporter-lacz-enzyme/spec.md) | purified protein | a supplier |
:::

**Both deliver beta-galactosidase activity**, which is why an operand can take either. In `compositional-biology-theory` they are **co-satisfying**, `glossary.md#T28`: two Formulations of one Specification, separated by a formulation predicate.

# Constituent Modules

- A source of beta-galactosidase — a template in one member, the purified protein in the other. No page: a class composes abstract constituents

# Requirements

Requires nothing of a Context that its members do not. What each member requires is the whole difference between them and is stated on their own pages.

# Processes

None here. Its two members are obtained rather than made: one is ordered from a supplier and the other is a DNA construct. [Pore](../pore/spec.md) has the same shape for the same reason.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit
explicitly before this page is merged to `main`.
:::
