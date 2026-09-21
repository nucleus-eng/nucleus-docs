---
title: "Abstract: Gel"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

An abstract Module: the class of hydrogels, of which the four paged gels are members. It refines [Container](../container/spec.md), and an abstract Module is a Module.

**The invariant is that a polymer network holds things in fixed relation to one another.** A gel does not enclose what it holds. It fixes where things are, while leaving them in contact with the solution around them. That is what separates it from a Membrane, which is the other child of Container.

**What varies is how the network is made to set**, and that is the one axis the four members differ on.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**Members are a different relation from constituents.** In `compositional-biology-theory`, `glossary.md#T34` makes Constituent a containment relation and `glossary.md#T13` makes membership a matter of what a sort classifies. **A class having members does not give it parts.** It does not give it none either: whether an abstract Module has constituents depends on whether its own class invariant names a composition, and that is decided per class rather than for abstract Modules in general.

**This class does have constituents, and they are already written down.** `codimension-is-a-coordinate.md:32` in the theory corpus states `Gel = OuterSolution ⊞ polymer`, same compartment, no membrane between them. That is a Composition in the `T33` sense with both factors abstract, so a gel is a polymer mixed into the solution it will become, and every member refines both factors rather than supplying them.

**So an empty composition would be false for this page**, which is not true of every abstract Module. The distinction is per class and this one falls on the composed side.

:::{table} The four members, by what makes the network set.
| Setting mechanism | Member | The trigger |
| --- | --- | --- |
| Thermal | [ULGA](../gel-ulga/spec.md) | cooling |
| Ionic | [Alginate](../gel-alginate/spec.md) | divalent calcium |
| Photopatterned | [PEG-Norbornene](../gel-peg-norbornene/spec.md) | 405 nm light, step-growth thiol-ene |
| Photopatterned | [PEGDA](../gel-pegda/spec.md) | 405 nm light, radical acrylate |
:::

**The two photopatterned members form a subclass of their own**, because light does something the other two triggers do not: it sets the gel's geometry from a projected image rather than from the shape of its container. See [abstract photopatterned gel](../abstract-photopatterned-gel/spec.md).

:::{table} The temperature window.
| Band | Value | Source |
| --- | --- | --- |
| Working window for the class | **8 °C to 50 °C** | supplier materials specification, via Jon, 2026-09-21 |
:::

:::{attention} The two ends of that window are different quantities, and the upper one is not a working temperature
**8 °C is a gelling point and 50 °C is a melting point.** They are not the two ends of a band of gelling points, and **50 °C is not a temperature at which vesicles can be mixed into a gel.**

**The window is still correct at this level, because the gel is not what forbids 50 °C.** The polymer is fine there. What forbids it is whatever is being embedded. **The narrower limit is a Requirement the payload imposes on its Container**, not a property of any gel, so it belongs on the page of the thing being held, pointing here. Recording a tighter window on a member page would put a fact about vesicles on a page about polysaccharide.

**Ruled by Jon, 2026-09-21:** *"that's the right range to put on the abstract module because the tighter temperature requirements come from the biology we put in the gels."*

**Still missing: a measured gelling point for any stock in use.** The figure above is a catalog value for a nominal product, not a measurement of what either Node holds. @Editor(london) and @Editor(chicago): what temperature does your agarose actually set at?
:::

# Requirements

Requires a solvent phase to form in. Every member in this corpus is cast into the outer solution it will become.

:::{attention} What this class requires of its Context is not settled
An abstract Module carries an abstract Context that its members refine, ruled 2026-09-17. **How much that Context term carries, and how much is left to Requirements, is `open.md#O21`** in the theory corpus, whose expressiveness half closed on Jon's ruling of 2026-09-21 and whose selection half is live.

**This class is where that question has its sharpest instance.** The temperature window above is a parameter that refines down the class, and the narrowing does not come from any member's own material properties. It comes from outside, as an imposition from whatever is embedded. If a refinement edge can be made of something that is not a property of either end of it, the boundary between the abstract Context term and Requirements is not where either reading of `O21` has been putting it.
:::

# Processes

None at this level. The embedding processes belong to the members: [Hydrogel Embedding: ULGA](../../processes/embed-ulga-hydrogel/main.md) and [Hydrogel Embedding: Alginate](../../processes/embed-alginate-hydrogel/main.md).

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
