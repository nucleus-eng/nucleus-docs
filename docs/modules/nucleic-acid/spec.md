---
title: "Nucleic Acid"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [DNA](../dna/spec.md), [RNA](../rna/spec.md).
<!-- /gen:position -->

A class: a Module whose subject is a nucleic acid molecule.

Every member is a chain of nucleotides joined by a phosphodiester backbone, and is identified by its sequence rather than by what the sequence encodes or does. The class fixes what members are made of, which is what decides how a nuclease treats them and what has to read them before anything happens.

**Its two refiners are classes rather than molecules.** [DNA](../dna/spec.md) and [RNA](../rna/spec.md) refine it by sugar, and every concrete Module arrives below one of them. No Module names this page as its parent. A real molecule has a sugar, so it belongs under one of the two.

A Module that is expressed from a template is not a member, and neither is one that produces a transcript. In both cases the subject is the behavior and the nucleic acid is a constituent of the reaction.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [DNA](../dna/spec.md) | A deoxyribose backbone. Double-stranded unless a page says otherwise. |
| [RNA](../rna/spec.md) | A ribose backbone. The sugar is the whole of the difference at this level. |

# Expected Behavior

A member does nothing on its own. It is read, and what reads it is supplied by whatever the member is added to.

Any member is cleaved by a nuclease that matches it. **Which nuclease is the narrowing a child carries, not a fact at this level.** `rna-nucleolysis` refines `nucleolysis` and names the RNase case, which fourteen sources attest by adding an inhibitor. The DNA side has no attested member, so it stays unwritten.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
