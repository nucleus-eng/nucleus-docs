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

:::::{tab-set}

::::{tab-item} Schematic
:::{figure} mechanism-schematic.png
Schematic of the TetR inducible expression module. TetR represses expression from `pT7-tetO-plamGFP`; aTc relieves repression by binding TetR and causing its release from the tetO operator.
:::
::::

::::{tab-item} Designs
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-tetR` | N/A | Nucleus v0.1.0 Distribution Plate, well G1 |
| `pT7-tetO-plamGFP` | N/A | Nucleus v0.1.0 Distribution Plate, well G3 |
::::

:::::

## Cytosols

### Usage

Assemble `pT7-tetO-plamGFP` into a standard PURE reaction. Add purified TetR protein to a final concentration of 500 nM, or include the `pT7-tetR` DNA construct. Add aTc inducer at 2.5–5 µM for effective induction. Volumes in µL.

:::{warning}
**Concentration discrepancy — requires review.** The reaction table lists TetR stock as `10 mM`, but the target final concentration stated in the text is 500 nM. At 10 mM stock with 0.5 µL in 10 µL total, the calculated final concentration would be 500 µM — a 1000× discrepancy. The stock concentration is likely `10 µM` (yielding 500 nM final). Please verify before use.
:::

| **Component** | **Master Mix (µL)** |
| --- | --- |
| PURExpress Solution A | 4 |
| PURExpress Solution B | 3 |
| RNase Inhibitor | 0.5 |
| `pT7-tetO-plamGFP` (10 nM) | 0.5 |
| TetR (10 mM) | 0.5 |
| **Master Mix Total** | **9** |

| **Component** | **Per Reaction (µL)** |
| --- | --- |
| Master Mix | 9 |
| Inducer | 1 |
| **Total** | **10** |

### Expected Performance

The TetR module was validated in NEB PURExpress reactions. Purified repressor protein (MedChemExpress, HY-P71520A) and anhydrotetracycline inducer (Cayman Chemical, 10009542) were added at the final concentrations indicated. `pT7-tetO-plamGFP` plasmid DNA was added at 0.5 nM.

Repression follows a roughly linear trend between 125 and 750 nM TetR and saturates around 500 nM, though it can be further improved up to 2000 nM. An inducer concentration of 2.5–5 µM provides effective induction well below saturating or toxic aTc levels. Note that aTc's yellow color overwhelms GFP fluorescence at concentrations greater than 50–100 µM, and high concentrations may negatively affect expression generally.

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

## Cells

:::{figure} detector-overview.png
The TetR-aTc Detector module in the Base Cell.
:::

### Expected Performance

TetR detector synthetic cells were induced at multiple anhydrotetracycline concentrations and imaged over 12 hours with approximately 22 minutes per timepoint.

:::{warning}
**Concentration discrepancy — requires review.** The figure caption for the encapsulated endpoint image states `312.5 uM` anhydrotetracycline, but the montage caption for the same experiment reports `312.5 nM`. Given the in vitro data showing toxicity above 50–100 µM, the intended concentration is almost certainly `312.5 nM`. Please verify before use.
:::

:::::{tab-set}

::::{tab-item} Montage
:::{figure} cell-performance-montage.png
TetR detector synthetic cells induced at multiple anhydrotetracycline concentrations. 8 timepoints displayed per condition, approximately 22 minutes apart, over 12 hours total. **First row:** induction using 625 nM, 312.5 nM, and 0 nM (fully repressed) aTc introduced into the outer buffer. **Second row:** induction with 2500 nM aTc in the inner solution and positive control without TetR repression.
:::
::::

::::{tab-item} Endpoint
:::{figure} cell-performance-endpoint.png
GFP expression within synthetic cells when induced with 312.5 µM anhydrotetracycline.
:::
::::

:::::

The TetR detector cell functions when induced with low-nanomolar aTc concentrations. Higher concentrations begin to inhibit expression or confound analysis due to background aTc fluorescence and membrane localization.
