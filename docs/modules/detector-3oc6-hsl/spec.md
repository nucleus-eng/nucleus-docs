---
title: "Detector: AHL"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The AHL Detector module is a LuxR/pLux genetic sensor that detects the _E. coli_ quorum-sensing molecule 3-oxohexanoyl-L-homoserine lactone or 3OC6-HSL. LuxR binds AHL and activates the pLux promoter, driving expression of a downstream effector gene (e.g., [deGFP](../reporter-degfp/spec.md)). 

This Module is composed into the [AHL Sensing Cell](../ahl-sensing-cell/spec.md), driving GFP expression, and the [London Cascade](../london-cascade/spec.md), driving PLA1 expression for a colorimetric readout.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Not the same molecule as the IV-HSL Emitter module
[Emitter: IV-HSL](../emitter-ivhsl/spec.md) documents a *different* acyl-homoserine lactone system: it produces N-isovaleryl-L-homoserine lactone (IV-HSL, a branched-chain HSL detected by BjaR) rather than detecting it, and IV-HSL is chemically distinct from the 3OC6-HSL detected by this module. The two are not interchangeable and this page makes no claim about compatibility between them.
:::

:::{attention} Not yet validated in Nucleus Cytosol
All data below comes from bacterial S30 lysate (Promega) and POPC synthetic cells built from S30 lysate, not from Nucleus Cytosol. 
:::

:::{figure} mechanism-schematic.png
Schematic representation of the AHL Detector mechanism. LuxR, constitutively expressed from p70, binds 3OC6-AHL as it diffuses in from outside the synthetic cell. LuxR–AHL activates the pLux promoter, driving gene expression (here: GFP). The phospholipid-bilayer inset of the original panel is cropped out as unrelated to the sensing mechanism.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA

:::{attention} Construct not in `nucleus-eng/DNA`
The LuxR/pLux AHL sensor plasmid used in the synthetic cell encapsulation work below is referred to as `pLux-GFP` (in-house stock, Elani lab) and has no catalog number or sequence file recorded. It is not present in [`nucleus-eng/DNA`](https://github.com/nucleus-eng/DNA) and does not appear to have originated from a prior repository either — it needs to be submitted before this Designs table can cite a real sequence file. Do not treat the name `pLux-GFP` as a stable identifier: the bacterial-lysate characterization below (Module 1) references only an unnamed "sensing plasmid" and does not confirm it is the same construct as the synthetic cell encapsulation plasmid (Module 3). Flagging this rather than assuming identity.
:::

| **Name**   | **Length (bp)** | **File**                     |
| ---------- | --------------- | ---------------------------- |
| `pLux-GFP` | not available   | not yet in `nucleus-eng/DNA` |
| `LuxR`     | ?               | ?                            |

::::

::::{tab-item} Cytosol

| **Component**   | **Stock**   | **Final** | **− AHL (µL)** | **+ 10 µM AHL (µL)** |
| --------------- | ----------- | --------- | --------- | --------------- |
| Premix          | 2.5x        | 1×        | 20        | 20              |
| Extract         | 3.33x       | 1×        | 15        | 15              |
| Amino acid mix  | 10x         | 1×        | 5         | 5               |
| Sensing plasmid | 2000 ng/µL  | 40 ng/µL  | 1         | 1               |
| 3OC6-HSL        | 1 mM        | 10 µM     | 0         | 0.5             |
| RNase inhibitor | 40 000 U/mL | 800 U/mL  | 1         | 1               |
| Water           | —           | —         | 8         | 7.5             |

:::{attention} Composition reconstructed, needs verification
Two rows are inferred rather than computed. The 3OC6-HSL stock is given as 1 mM, the only value that yields the 10 µM final stated in the column header, the Outer Solution tab and Expected Behavior; the source's 50 mM would require 0.01 µL. The condition columns are also swapped relative to the source, in which the column headed **− AHL** was the one carrying the AHL. The RNase inhibitor is left as sourced at 800 U/mL, which is genuinely lower than the 2000 U/mL on the S30 spec rather than a scaling error. @Editor(london): confirm all three with the London Node before bench use.
:::

::::

::::{tab-item} Outer Solution

| **Component**         | **Concentration** |
| --------------------- | ----------------- |
| Potassium L-glutamate | 578 mM            |
| HEPES, pH 7.4         | 72 mM             |
| Glucose               | 300 mM            |
| 3OC6-HSL              | 10 µM             |

::::

:::::

# Expected Behavior

## Cytosols

3OC6-HSL expresses a downstream effector gene at increasing strength with increasing 3OC6-HSL concentration up to 10 µM. This system has only been validated in [S30 Lysate](../s30-lysate/spec.md).  

:::{attention} Missing Characterization Data
- S30 lysate 
- Nucleus Cytosol 
:::

## Cells

This module has been validated in [S30 Lysate Synthetic Cells](../london-chassis/spec.md) with extracellular target molecule at 10 µM.

:::{attention} Missing Characterization Data
Needs microscopy image of cells with (+) and without (-) target molecule.
:::

# Requirements

Requires sigma-70 promoter transcription and translation (e.g., *E. coli* RNA polymerase, as supplied by [S30 Lysate](../s30-lysate/spec.md)). The pT7 transcription in [Base Cytosol](../base-cytosol/spec.md) does not drive the pLux promoter.

Requires 3OC6-HSL. If used in a synthetic cell, no transport module is required: 3OC6-HSL diffuses from outer solution across a lipid bilayer.

# Implementations

- [London DevCell](../../implementations/london-devcell/main.md): this Module supplies AHL sensing for the London quorum-sensing demo.

# Processes

No process page documents building this Module or assembling it into a reaction.

# Credits

Developed by Ion Ioannou and Jonah McDonald (London Node, Elani Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
