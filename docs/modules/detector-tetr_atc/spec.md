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

### Chicago Cascade Encapsulation (TetO-PLA1 / LacZ-CPRG Readout)

:::{attention} Synthetic-cell data only
The `TetO-PLA1` construct is co-encapsulated with LacZ and CPRG substrate. The data below cover synthetic cytosols and synthetic cells only — hydrogel-embedded validation has not been performed.
:::

A separate, Chicago-specific implementation encapsulates a `TetO-PLA1` construct — not `pT7-tetO-plamGFP` above — together with LacZ and CPRG substrate in a synthetic cell, reading out through the LacZ/CPRG colorimetric reaction (absorbance at 575 nm) instead of GFP fluorescence. This configuration detects aTc in synthetic cytosols and in synthetic cells, but the response is **not graded**. The source figure reports fold change in absorbance at 5 h (n = 3) across three DNA/TetR combinations — 1 nM DNA with 50 nM TetR, 0.5 nM DNA with 50 nM TetR, and 1 nM DNA with 100 nM TetR — each dosed with 0, 1, 5, and 10 µM aTc.

Every combination separates dosed from undosed, at roughly 1.15× to 1.33× fold change. None shows a monotonic increase with dose: the response peaks at 1 µM in the first combination and at 5 µM in the third, and the error bars across the 1, 5, and 10 µM points overlap in all three. Read this as **saturating at or below 1 µM, with no resolvable dose-dependence from 1 to 10 µM.**

:::{attention} The 0 µM point is a baseline, not a negative control
Values are fold change normalized to the 0 µM condition, so that point is 1.00 by construction. The source figure contains no −TetR or −DNA control panel. An earlier revision of this page cited those controls; that citation was not supported by the figure and has been removed.
:::

:::{warning}
**Gel integration not yet complete.** This result is confirmed in synthetic cytosols and in synthetic cells only. Hydrogel integration is in early stages and has not been completed. Do not treat this construct as validated for hydrogel-embedded (Cascade) use yet.
:::

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).

This Module must not be co-encapsulated with the [Theophylline Sensing Module](../detector-theophylline/spec.md) (for example, in the Chicago Cascade). Both read out through the same LacZ/CPRG chemistry, and the 2026-08-14 meeting resolved to make the two mutually exclusive in the current Chicago Cascade design.

The requirement is settled. The mechanism usually given for it — theophylline inhibiting the LacZ/CPRG conversion — is **not** established, and the only primary figure available points the other way. See [Theophylline Sensing Module § Requirements](../detector-theophylline/spec.md#requirements) for the evidence on both sides; do not restate the inhibition mechanism as fact.

:::{attention} Mutual exclusion — not a general compatibility rule
This constraint applies to the current Chicago Cascade, where both sensing modules would share the same LacZ/CPRG readout. It is not yet established as a general nucleus-wide compatibility rule between the two Modules.
:::

# Implementations

- [Responder: aTc → IV-HSL](../../implementations/responder-atc-ivhsl/main.md): aTc relieves TetR repression to drive BjaI expression.

# Credits

Developed by Yen-Yu Hsu (b.next).
