---
title: "Double-Stranded DNA"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [DNA](../dna/spec.md). Refined by [LacZ DNA template](../lacz-dna/spec.md).
<!-- /gen:position -->

A class: a DNA molecule that is two strands paired.

It refines [DNA](../dna/spec.md) by strandedness, as [single-stranded DNA](../ssdna/spec.md) does, and the two are siblings rather than one above the other.

**The two are not symmetric in what a page must say.** Double-stranded is the default: a DNA Module silent on strandedness is one of these, and single-stranded is the case that has to be declared.

A member is the product of annealing rather than an operand of it. Pairing is what makes it stable and what makes it inert: the bases are spoken for, so nothing further hybridises to it without displacing something.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

**This is the default case, so membership is the rule rather than the exception.** A DNA Module that says nothing about strandedness is one of these. `ph-trigger-duplex` is attested as a product, and the twelve DNA template and plasmid input ids across the corpus are members by the same default.

| Member | What makes it a member |
| --- | --- |
| [LacZ DNA template](../lacz-dna/spec.md) | A template, and templates are double-stranded. Its page never says so, which is exactly what the default is for. |

# Expected Behavior

A member holds its two strands together until something releases them. The pH duplex is the worked case: acidic pH frees the trigger strand, which is the whole mechanism of the detector that uses it.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
