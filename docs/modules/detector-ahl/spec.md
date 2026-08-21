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
Schematic representation of the AHL Detector mechanism. LuxR, constitutively expressed from p70, binds 3OC6-AHL as it diffuses in from outside the synthetic cell. LuxR–AHL activates the pLux promoter, driving gene expression (here: GFP). Cropped from a DevCell Status Update slide deck (14 Aug 2026, p. 13, "Sensor GFP SynCells with lysate (in gel)"); the source panel's phospholipid-bilayer inset has been cropped out as unrelated to the sensing mechanism itself.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA

:::{attention} Construct not in `nucleus-eng/DNA`
The LuxR/pLux AHL sensor plasmid used in the synthetic cell encapsulation work below is referred to as `pLux-GFP` (in-house stock, Elani lab) and has no catalog number or sequence file in the source material. It is not present in [`nucleus-eng/DNA`](https://github.com/nucleus-eng/DNA) and does not appear to have originated from a prior repository either — it needs to be submitted before this Designs table can cite a real sequence file. Do not treat the name `pLux-GFP` as a stable identifier: the bacterial-lysate characterization below (Module 1) references only an unnamed "sensing plasmid" and does not confirm it is the same construct as the synthetic cell encapsulation plasmid (Module 3). Flagging this rather than assuming identity.
:::

| **Name**   | **Length (bp)** | **File**                     |
| ---------- | --------------- | ---------------------------- |
| `pLux-GFP` | not available   | not yet in `nucleus-eng/DNA` |
| `LuxR`     | ?               | ?                            |

::::

::::{tab-item} Cytosol

This is the bacterial-lysate characterization reaction, at 50 µL — twice the 25 µL scale of the reference table on the [S30 Lysate](../s30-lysate/spec.md) spec. The three kit components scale exactly: premix, extract, and amino acid mix sit at 0.4, 0.3, and 0.1 of the reaction volume in both tables, so both describe the same 1× working kit concentrations. The RNase inhibitor does not: 1 µL of 40 000 U/mL into 50 µL gives 800 U/mL here, against 2000 U/mL on the S30 spec.

Volumes are in µL.

| **Component**   | **Stock**  | **Final**  | **− AHL** | **+ 10 µM AHL** |
| --------------- | ---------- | ---------- | --------- | --------------- |
| Premix          | 3.33x      | 1x         | 20        | 20              |
| Extract         | 15 mg/mL   | 1.80 mg/mL | 15        | 15              |
| Amino acids     | 10 µM      | 1.8 µM     | 5         | 5               |
| Sensing plasmid | 2000 ng/µL | 40 ng/µL   | 1         | 1               |
| 3OC6-HSL        | 50 mM      | 0.01 mM    | 0.5       | 0               |
| RNase inhibitor | 40000 U/mL | 800 U/mL   | 1         | 1               |
| Water           | —          | —          | 7.5       | 8               |

:::{warning} Four rows of this table do not reconcile
Recomputing `stock × volume / 50 µL` against the stated final concentration fails for four of the seven reagent rows, and the two condition columns look inverted.

| Row | Stated final | Computes to |
| --- | --- | --- |
| Premix | 1× | 1.33× |
| Extract | 1.80 mg/mL | 4.5 mg/mL |
| Amino acids | 1.8 µM | 1.0 µM |
| **3OC6-HSL** | **0.01 mM (10 µM)** | **0.5 mM — 50× off** |

The 3OC6-HSL row is the one that matters: 0.5 µL of a 50 mM stock into 50 µL gives 0.5 mM, not 10 µM. A 1 mM stock would give exactly 10 µM. Separately, the column headed **− AHL** is the one carrying the 0.5 µL of 3OC6-HSL, which reads as a header inversion. Raised with the London Node (London questionnaire, Q1); do not use this table at the bench until it is answered.
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

3OC6-HSL turns on effector gene expression with increasing strength up to 10 µM. This system has only been validated in [S30 Lysate](../s30-lysate/spec.md).  

:::{attention} Missing Characterization Data
- S30 lysate curves
- Nucleus Cytosol curves (Surendra is validating this module in Cytosol; pull data here)
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

The synthetic-cell-encapsulated and hydrogel-embedded configurations described above are now documented as composed Module pages rather than as a standalone Implementation:

- [AHL Sensing Cell](../ahl-sensing-cell/spec.md): this Sensor Module encapsulated in the [London Chassis](../london-chassis/spec.md) driving GFP expression. 
- [London Cascade](../london-cascade/spec.md): this Sensor Module encapsulated in the [London Chassis](../london-chassis/spec.md) driving expression of [PLA1 Lysis Module](../effector-pla1/spec.md) used as part of the macroscopic colorimetric readout supplied by the [LacZ Reporter](../reporter-lacz/spec.md) and its [CPRG Substrate SUVs](../substrate-cprg-suv/spec.md).

# Credits

Developed by Ion Ioannou and Jonah McDonald (London Node, Elani Lab).
