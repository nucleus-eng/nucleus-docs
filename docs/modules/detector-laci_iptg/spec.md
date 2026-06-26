---
title: "Detector: LacI-IPTG"
subtitle: "Module Specification"
thumbnail: mechanism-schematic.png
site:
    hide-toc: true
    numbered_references: false
---
# Overview

The LacI-IPTG Detector Module is a set of two genetic constructs that encode IPTG-inducible gene expression. `pT7-lacI` encodes the lac operon repressor protein LacI. `pT7-lacO-plamGFP` is a GFP reporter construct under a T7 promoter controlled by a lacO operator site. In the absence of LacI, `pT7-lacO-plamGFP` expresses plamGFP. Adding LacI — either as a purified protein or by expressing it off of `pT7-lacI` — binds the lacO operator site and represses transcription by sterically occluding the promoter from its polymerase. Isopropyl β-d-1-thiogalactopyranoside (IPTG) recovers expression by allosterically binding LacI and causing it to release lacO. The `pT7-lacO` promoter is also a MoClo Level 0 'P' part and may be assembled into a Level 1 transcription unit with other MoClo-compatible genes.

:::::{tab-set}

::::{tab-item} Schematic
:::{figure} mechanism-schematic.png
Schematic of the LacI-IPTG detector module. IPTG relieves LacI repression of `pT7-lacO-plamGFP`, recovering GFP expression.
:::
::::

::::{tab-item} Designs
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-lacI` | 2877 | [pOpen-lacI.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/pOpen-lacI.gb) |
| `pT7-lacO-plamGFP` | 2958 | [pOpen-pT7-lacO.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/pOpen-pT7-lacO.gb) |
::::

:::::

## Cytosols

### Usage

Assemble `pT7-lacO-plamGFP` into a standard PURE reaction. Add purified LacI protein to a final concentration of 500 nM to 1000 nM, or include the `pT7-lacI` DNA construct. Add IPTG inducer at 500 nM to 2000 nM for effective induction. 

| **Component**              | **Master Mix (µL)** |
| -------------------------- | ------------------- |
| PURExpress Solution A      | 4                   |
| PURExpress Solution B      | 3                   |
| RNase Inhibitor            | 0.5                 |
| `pT7-lacO-plamGFP` (10 nM) | 0.5                 |
| LacI (10 µM)               | 0.5                 |
| **Master Mix Total**       | **9**               |

| **Component** | **Per Reaction (µL)** |
| ------------- | --------------------- |
| Master Mix    | 9                     |
| IPTG (10 µM)  | 1                     |
| **Total**     | **10**                |

### Expected Performance

We've validated the LacI-IPTG module in NEB PURExpress reactions by adding purified LacI repressor protein (MedChemExpress HY-P70247) at the final concentrations indicated, with `pT7-lacO-plamGFP` plasmid DNA at 5 nM to 10 nM.

We observe repression across a wide range of LacI concentrations (15.63 nM –1000 nM), with 1000 nM showing strong repression and suitable dynamic range for use in an inducible system. We saw a small increase in expression around 62.5 nM repressor; we saw a similar effect in TetR data and may reflect a shared mechanism (e.g., preserving PURE translational capacity under moderate transcriptional repression). The 250 nM datapoint is likely a technical failure. IPTG induction is effective across 500 nM to 2000 nM, consistent with concentrations used in cellular and cell-free systems ([Garamella et al., 2016](https://doi.org/10.1021/acssynbio.5b00296)). All induced samples show expression at or above the unrepressed positive control, a behavior that we've replicated across multiple experiments and is worth of further investigation.

***In vitro* repression with LacI**

:::::{tab-set}

::::{tab-item} Kinetics
:::{figure} cytosol-repression-kinetics.png
Repression kinetics of `pT7-lacO-plamGFP` by LacI at varying repressor concentrations. `pT7-lacO-plamGFP` plasmid DNA at 5 nM.
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-repression-endpoint.png
Repression of `pT7-lacO-plamGFP` by LacI at steady state. `pT7-lacO-plamGFP` plasmid DNA at 10 nM.
:::
::::

:::::

***In vitro* induction with IPTG**

:::::{tab-set}

::::{tab-item} Kinetics
:::{figure} cytosol-induction-kinetics.png
Induction kinetics of `pT7-lacO-plamGFP` by IPTG. LacI repressor protein present at 500 nM. Positive control is `pT7-lacO-plamGFP` without LacI repressor.
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-induction-endpoint.png
Induction of `pT7-lacO-plamGFP` by IPTG at steady state. LacI repressor protein present at 500 nM. Positive control is `pT7-lacO-plamGFP` without LacI repressor.
:::
::::

:::::

## Cells

:::{figure} cell-overview.png
The LacI-IPTG Detector module in the Base Cell.
:::

Cell performance data is not yet available for this module.

# Credits

- b.next
