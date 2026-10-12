---
title: "Detector: tetR-aTc"
subtitle: "Module Specification"
thumbnail: mechanism-schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The TetR inducible expression module is a set of two genetic constructs that encode tetracycline-inducible gene expression: `pT7-tetR`, encoding the TetR repressor protein, and `pT7-tetO-plamGFP`, encoding a reporter gene under an inducible T7 promoter.

`pT7-tetO-plamGFP` constitutively expresses the open reporter plamGFP in the absence of repressor protein. The inducible promoter is also a MoClo Level 0 'P' part and may be assembled into a Level 1 transcription unit with other MoClo-compatible genes. Addition of TetR protein — either as a purified protein or via constitutive expression of `pT7-tetR` — inhibits expression through steric occlusion of the tetO operator site. Addition of anhydrotetracycline (aTc) causes allosteric release of TetR from tetO, recovering expression. aTc is membrane-permeable, so the alpha-hemolysin membrane pore is not required for induction.

:::{figure} mechanism-schematic.png
Schematic of the TetR inducible expression module. TetR represses expression from `pT7-tetO-plamGFP`; aTc relieves repression by binding TetR and causing its release from the tetO operator.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA
:::{table}
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-tetR` | 2877 | [pOpen-tetR.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/pOpen-tetR.gb) |
| `pT7-tetO-plamGFP` | 2954 | [pOpen-pT7-tetO.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/pOpen-pT7-tetO.gb) |
:::
::::

::::{tab-item} Cytosol

Assemble `pT7-tetO-plamGFP` into a standard PURE reaction. Add purified TetR protein to a final concentration of 500 nM, or include the `pT7-tetR` DNA construct. Add aTc inducer at 2.5 µM to 5 µM for effective induction. Volumes in µL.


| **Component** | **Master Mix (µL)** |
| --- | --- |
| PURExpress Solution A | 4 |
| PURExpress Solution B | 3 |
| RNase Inhibitor | 0.5 |
| `pT7-tetO-plamGFP` (10 nM) | 0.5 |
| TetR (10 µM) | 0.5 |
| **Master Mix Total** | **9** |

| **Component** | **Per Reaction (µL)** |
| --- | --- |
| Master Mix | 9 |
| Inducer | 1 |
| **Total** | **10** |

::::

:::::

# Expected Behavior

## Cytosols

The TetR module was validated in NEB PURExpress reactions. Purified repressor protein (MedChemExpress, HY-P71520A) and anhydrotetracycline inducer (Cayman Chemical, 10009542) were added at the final concentrations indicated. `pT7-tetO-plamGFP` plasmid DNA was added at 0.5 nM.

Repression follows a roughly linear trend between 125 and 750 nM TetR and saturates around 500 nM, though it can be further improved up to 2000 nM. An inducer concentration of 2.5 µM to 5 µM provides effective induction well below saturating or toxic aTc levels. Note that aTc's yellow color overwhelms GFP fluorescence at concentrations greater than 50 µM to 100 µM, and high concentrations may negatively affect expression generally.

***In vitro* repression with TetR**

:::::{tab-set}

::::{tab-item} Kinetics
:::{figure} cytosol-repression-kinetics.png
Repression kinetics of `pT7-tetO-plamGFP` by TetR at varying repressor concentrations.
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-repression-endpoint.png
Repression of `pT7-tetO-plamGFP` by TetR at steady state.
:::
::::

:::::

***In vitro* induction with aTc**

:::::{tab-set}

::::{tab-item} Kinetics
:::{figure} cytosol-induction-kinetics.png
Induction kinetics of `pT7-tetO-plamGFP` by aTc. TetR repressor protein is present at 500 nM. Positive control is `pT7-tetO-plamGFP` without TetR repressor protein.
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-induction-endpoint.png
Induction of `pT7-tetO-plamGFP` by aTc at steady state. TetR repressor protein is present at 500 nM. Positive control is `pT7-tetO-plamGFP` without TetR repressor protein.
:::
::::

:::::

### aTc titration in Nucleus Base Cytosol

`pT7-tetO-plamGFP` was titrated with aTc against purified His-tagged TetR (MedChemExpress, HY-P71520A) in [Nucleus Base Cytosol](../../processes/assemble-base-cytosol/main.md). Per 10 µL, the reaction holds 3.0 µL SMix, 1.0 µL tRNA, 1.2 µL PMix, 1.8 µL ribosomes and 0.5 µL RNase inhibitor. The plasmid is at 1 nM and TetR at 0, 500 or 1000 nM, before the aTc is added. Plasmid, TetR and water were incubated at 37 °C for 10 min so TetR could bind the operator, and the master mix was then added. Reactions were dispensed at 10 µL per well into a 384-well plate and 1 µL of aTc added, to final aTc concentrations of 0, 0.25, 0.35, 0.5, 1, 5 and 10 µM, with three wells per condition. A no-DNA reaction at each aTc concentration served as the background. Fluorescence (485 nm excitation, 528 nm emission, gain 75) was read every 5 min for 6 h at 37 °C on a BioTek Cytation 3.

Without aTc, TetR holds expression to 541 RFU at 500 nM (40-fold below the unrepressed reaction) and 399 RFU at 1000 nM (54-fold). The no-DNA background stays between 43 and 87 RFU across the titration and rises with aTc dose, from 47 RFU at 0 µM to 69 RFU at 5 µM and 87 RFU at 10 µM, which is under 0.5 % of the unrepressed signal. aTc does not change the unrepressed reaction: it reads between 21,662 and 22,871 RFU from 0 to 10 µM, so aTc neither quenches nor inhibits expression at these doses.

aTc relieves repression in both reactions, and the dose needed rises with the amount of TetR. At 500 nM TetR, expression reaches 30 % of the unrepressed level at 0.25 µM aTc, 86 % at 1 µM and 91 % at 5 µM. At 1000 nM TetR it is 4 % at 0.25 µM, 22 % at 0.5 µM, 63 % at 1 µM and 88 % at 5 µM. Half of the unrepressed level is reached at about 0.4 µM aTc with 500 nM TetR and about 0.8 µM with 1000 nM, so doubling TetR moves the induction curve about two-fold to higher aTc. Neither reaction reaches the unrepressed level by 10 µM, where they read 87 % and 93 %. The titration has no points between 1 and 5 µM, so these half-maximal doses are read from the measured points.

:::{figure} cytosol-nucleus-atc-titration-endpoint.png
:name: fig-tetr-atc-nucleus-cytosol-endpoint
:align: center

Endpoint GFP fluorescence at 6 h in Nucleus Base Cytosol, for 1 nM `pT7-tetO-plamGFP` with 0, 500 or 1000 nM TetR across 0 to 10 µM aTc, with a no-DNA control at each dose. Mean ± standard deviation of three wells; gain 75.
:::

## Cells

:::{figure} detector-overview.png
The TetR-aTc Detector module in the Base Cell.
:::

TetR detector synthetic cells were induced at multiple anhydrotetracycline concentrations and imaged over 12 h with approximately 22 min per timepoint.

:::::{tab-set}

::::{tab-item} Microscopy Images
:::{figure} cell-performance-montage.png
TetR detector synthetic cells induced at multiple anhydrotetracycline concentrations. 8 timepoints displayed per condition, approximately 22 min apart, over 12 h total. **First row:** induction using 625 nM, 312.5 nM, and 0 nM (fully repressed) aTc introduced into the outer buffer. **Second row:** induction with 2500 nM aTc in the inner solution and positive control without TetR repression.
:::
::::

::::{tab-item} Fluorescence Intensity
:::{figure} cell-performance-endpoint.png
GFP expression within synthetic cells when induced with 312.5 nM anhydrotetracycline.
:::
::::

:::::

The TetR detector cell functions when induced with low-nanomolar aTc concentrations. Higher concentrations begin to inhibit expression or confound analysis due to background aTc fluorescence and membrane localization.

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).

# Implementations

- [Responder: aTc → IV-HSL](../../implementations/responder-atc-ivhsl/main.md): aTc relieves TetR repression to drive BjaI expression.

# Credits

Developed by Yen-Yu Hsu (b.next).

Bulk titration in Nucleus Base Cytosol by Mary Kelly (Kamat Lab, Northwestern University, DevCells Chicago Node) and Madison Briggs (Kamat Lab, Northwestern University, DevCells Chicago Node).

GUV deGFP characterization by Mary Kelly (Kamat Lab, Northwestern University, DevCells Chicago Node).
