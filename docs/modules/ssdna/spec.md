---
title: "Single-Stranded DNA"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [DNA](../dna/spec.md). Refined by nothing on this branch.
<!-- /gen:position -->

A class: a DNA molecule that is one strand.

It refines [DNA](../dna/spec.md) by strandedness. What it is made of is unchanged; what differs is that the bases are unpaired, so the strand is free to pair with a complement.

**Membership has to be declared.** Double-stranded is the default for a DNA Module that says nothing, so a member of this class is one whose page says single-stranded in so many words.

That availability is what makes a member useful. A single strand can be annealed, displaced, or used as a trigger, none of which a paired strand can do without first coming apart.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

No member has a page. **Four input ids are attested instances**, all on [pH Detector](../detector-ph/spec.md) and the cascades built on it: `ph-responsive-ssdna`, `trigger-ssdna`, `trigger-ssdna-in-duplex` and `toehold-switch-dna`.

| Member | What makes it a member |
| --- | --- |
| — | No single-stranded DNA has a Module page. The class is declared because [Anneal the pH-Trigger Duplex](../../processes/anneal-ph-trigger-duplex/main.md) takes two of them and produces something else. |

# Expected Behavior

A member pairs with its complement when the two are brought together under annealing conditions. Until then its bases are available, which is what a toehold exploits.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
