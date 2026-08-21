---
title: "Detector: AHL"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

@Claude rename filepath to `docs/modules/detector-3OC6-HSL` . Rename title and any references to this page appropriately.
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

:::::{tab-set}

::::{tab-item} Schematic
:::{figure} mechanism-schematic.png
LuxR, constitutively expressed from p70, binds 3OC6-AHL as it diffuses in from outside the synthetic cell. LuxR–AHL activates the pLux promoter, driving gene expression (here: GFP). Cropped from a DevCell Status Update slide deck (14 Aug 2026, p. 13, "Sensor GFP SynCells with lysate (in gel)"); the source panel's phospholipid-bilayer inset has been cropped out as unrelated to the sensing mechanism itself.
:::
::::

::::{tab-item} DNA

:::{attention} Construct not in `nucleus-eng/DNA`
The LuxR/pLux AHL sensor plasmid used in the synthetic cell encapsulation work below is referred to as `pLux-GFP` (in-house stock, Elani lab) and has no catalog number or sequence file in the source material. It is not present in [`nucleus-eng/DNA`](https://github.com/nucleus-eng/DNA) and does not appear to have originated from a prior repository either — it needs to be submitted before this Designs table can cite a real sequence file. Do not treat the name `pLux-GFP` as a stable identifier: the bacterial-lysate characterization below (Module 1) references only an unnamed "sensing plasmid" and does not confirm it is the same construct as the synthetic cell encapsulation plasmid (Module 3). Flagging this rather than assuming identity.
:::

| **Name**   | **Length (bp)** | **File**                     |
| ---------- | --------------- | ---------------------------- |
| `pLux-GFP` | not available   | not yet in `nucleus-eng/DNA` |
| `LuxR`     | ?               | ?                            |  |
::::

::::{tab-item} Cytosol Composition

@Claude: check this and harmonize against [S30 spec](../s30-lysate/spec.md). 

| **Component**   | **Stock**  | **Final**  | **− AHL** | **+ 10 µM AHL** |
| --------------- | ---------- | ---------- | --------- | --------------- |
| Premix          | 3.33x      | 1x         | 20        | 20              |
| Extract         | 15 mg/mL   | 1.80 mg/mL | 15        | 15              |
| Amino acids     | 10 µM      | 1.8 µM     | 5         | 5               |
| Sensing plasmid | 2000 ng/µL | 40 ng/µL   | 1         | 1               |
| 3OC6-HSL        | 50 mM      | 0.01 mM    | 0.5       | 0               |
| RNase inhibitor | 40000 U/mL | 800 U/mL   | 1         | 1               |
| Water           | —          | —          | 7.5       | 8               |

::::

::::{tab-item} Outer Solution Composition

| **Component**         | **Concentration** |
| --------------------- | ----------------- |
| Potassium L-glutamate | 578 mM            |
| HEPES, pH 7.4         | 72 mM             |
| Glucose               | 300 mM            |
| 3OC6-HSL              | 10 µM             |

::::

:::::

# Expected Performance

### Cytosol

3OC6-HSL turns on effector gene expression with increasing strength up to 10 µM. This system has only been validated in [spec](../s30-lysate/spec.md).  

:::{attention} Missing Characterization Data
- S30 lysate curves
- Nucleus Cytosol curves (Surendra is validating this module in Cytosol; pull data here)
:::

### Cells
3OC6-HSL can diffuse from outer solution across a lipid bilayer, meaning this module does not require transport. This module has been validated in [S30 Lysate Synthetic Cells](../../modules/london-chassis/spec) with extracellular target molecule at 10 µM.

:::{attention} Missing Characterization Data
Needs microscopy image of cells with (+) and without (-) target molecule.
:::

# Requirements

Requires sigma-70 promoter transcription (e.g., *E. coli* RNA Polymerase).

# Known Implementations

The synthetic-cell-encapsulated and hydrogel-embedded configurations described above are now documented as composed Module pages rather than as a standalone Implementation:

- [AHL Sensing Cell](../ahl-sensing-cell/spec.md): this Sensor Module encapsulated in the [London Chassis](../london-chassis/spec.md) driving GFP expression. 
- [London Cascade](../london-cascade/spec.md): this Sensor Module encapsulated in the [London Chassis](../london-chassis/spec.md) driving expression of [PLA1 Lysis Module](../../modules/effector-pla1/spec) used as part of a macroscopic colormetric reporter (@Claude: tag module page for that LacZ/CPRG reporter module if we have it).

# Credits

Developed by Ion Ioannou and Jonah McDonald (London node, Elani Lab).
