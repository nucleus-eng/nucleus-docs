---
title: "Abstract: Photopatterned Gel"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

An abstract Module: the class of gels whose shape is set by projected light. It refines [abstract gel](../abstract-gel/spec.md), which refines [Container](../container/spec.md).

**The invariant is that geometry comes from an image rather than from a container.** A thermally or ionically set gel takes the shape of whatever it is poured into. A photopatterned gel sets only where the light falls, so its shape is chosen at the moment of casting and can be different in two places in the same well.

**That is a capability and not a detail.** It is the corpus's route to spatial separation, which is what the Chicago Cascade needs so that two PLA1-gated paths do not lyse each other's compartments. See [Chicago Cascade](../chicago-cascade/spec.md) § Requirements.

**What varies between the two members is the crosslinking chemistry**, and it is not a cosmetic difference.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**Members are a different relation from constituents.** In `compositional-biology-theory`, `glossary.md#T34` makes Constituent a containment relation and `glossary.md#T13` makes membership a matter of what a sort classifies. **A class having members does not give it parts.** It does not give it none either: whether an abstract Module has constituents depends on whether its own class invariant names a composition, and that is decided per class rather than for abstract Modules in general.

**This class has constituents, inherited and extended.** It refines [abstract gel](../abstract-gel/spec.md), whose composition the theory corpus gives as `Gel = OuterSolution ⊞ polymer`. **Photopatterning adds a third factor**: a photoinitiator, which both members carry and which neither parent class requires. So the composition here is a proper extension of the parent's, and that is what makes this a class rather than a label on two members.

:::{table} The two members, by crosslinking chemistry.
| Member | Chemistry | Network |
| --- | --- | --- |
| [PEG-Norbornene](../gel-peg-norbornene/spec.md) | step-growth thiol-ene, 4-arm PEG-norbornene with a PEG4SH crosslinker | defined by the arms and the crosslinker |
| [PEGDA](../gel-pegda/spec.md) | radical acrylate chain-growth | defined by chain propagation |
:::

**Both need a photoinitiator and both use 405 nm.** The light source is the same and the chemistry underneath it is not. Step-growth builds a network of known connectivity from components of known functionality. Chain-growth builds one whose connectivity depends on how far each chain propagates before it terminates.

**The corpus already treats these as unequal for a reason that is not chemistry.** The [PEG-Norbornene](../gel-peg-norbornene/spec.md) page records it as the less harsh of the two. That is a claim about what survives being embedded, which makes it a payload Requirement rather than a gel property, the same shape as the temperature window on the parent page.

# Requirements

Requires a photoinitiator, and requires 405 nm light delivered as a pattern rather than as flood illumination. Flood illumination sets the gel and gives up the only thing this class has.

Requires that whatever is being embedded survives the initiator and the light. **That is the constraint that separates the two members in practice**, and neither member page states it as a number.

:::{attention} What this class requires of its Context is not settled
An abstract Module carries an abstract Context that its members refine, ruled 2026-09-17. **How much that Context term carries, and how much is left to Requirements, is `open.md#O21`** in the theory corpus, whose expressiveness half closed on Jon's ruling of 2026-09-21 and whose selection half is live.

**Here the open question has teeth.** The difference the corpus actually cares about between these two members is how harsh each is on what it holds. That is not a property of either gel alone. It is a relation between the gel and its payload, and until `O21` settles where such a relation is written, this page can name it and cannot type it.
:::

# Processes

None at this level. Photopatterning belongs to the members.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
