---
title: "DNA"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [Double-Stranded DNA](../dsdna/spec.md), [Single-Stranded DNA](../ssdna/spec.md).
<!-- /gen:position -->

A class: a Module whose subject is a DNA molecule.

Every member is a nucleic acid polymer, and is identified by its sequence rather than by what the sequence encodes. Members encode different things. The class fixes what they are made of, which is what decides how a nuclease treats them and what a reaction must supply before they do anything.

**Double-stranded unless a page says otherwise.** Jon, 2026-10-05: *"basically all DNA that isn't explicitly ssDNA is double stranded."* So [double-stranded DNA](../dsdna/spec.md) is the default reading of a member that states nothing, and [single-stranded DNA](../ssdna/spec.md) is the one that has to be declared. A page silent on strandedness is not a page with a gap.

A Module that is expressed from DNA is not a member. Its subject is the behavior, and the DNA is a constituent of the reaction that produces it.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [LacZ DNA template](../lacz-dna/spec.md) | The template that encodes beta-galactosidase. The page's subject is the molecule, not the enzyme it yields. |

# Expected Behavior

A member does nothing on its own. It is read, and what reads it is a transcription and translation system supplied by whatever the member is added to. Two members in one compartment are read by the same machinery and compete for it.

# Requirements

Every member requires transcription and translation from its host. That is the requirement a DNA page carries and a protein page does not: a purified protein arrives able to act, and a template arrives able only to be read.

The requirement is stated here in prose rather than declared. `requires:` is a key on a step, and a class with no steps has no step to hang one on. The same gap closed for `impositions` on [Lysis](../lysis/spec.md) when a class-level key was added; nothing has asked for the equivalent here yet.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
