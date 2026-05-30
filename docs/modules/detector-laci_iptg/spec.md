---
title: "Detector: LacI-IPTG"
subtitle: "Module Specification"
thumbnail: mechanism-schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The LacI-IPTG detector module is a set of two genetic constructs that encode IPTG-inducible gene expression. `pT7-lacI` encodes the lac operon repressor protein LacI. `pT7-lacO-plamGFP` is a GFP reporter construct under a T7 promoter containing the lacO operator site. In the absence of LacI, `pT7-lacO-plamGFP` constitutively expresses plamGFP. Addition of LacI — either as a purified protein or via constitutive expression from `pT7-lacI` — represses expression through steric occlusion of the lacO operator site. Addition of isopropyl β-d-1-thiogalactopyranoside (IPTG) causes allosteric release of LacI from lacO, recovering expression. The `pT7-lacO` promoter is also a MoClo Level 0 'P' part and may be assembled into a Level 1 transcription unit with other MoClo-compatible genes.

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

Assemble `pT7-lacO-plamGFP` into a standard PURE reaction. Add purified LacI protein to a final concentration of 500–1000 nM, or include the `pT7-lacI` DNA construct. Add IPTG inducer at 500–2000 nM for effective induction. Volumes in µL.

:::{warning}
**Concentration discrepancy — requires review.** The reaction table lists LacI stock as `10 mM`, but the target final concentration stated in the text is 500–1000 nM. At 10 mM stock with 0.5 µL in 10 µL total, the calculated final concentration would be 500 µM — a 1000× discrepancy. The stock concentration is likely `10 µM` (yielding 500 nM final). Please verify before use.
:::

| **Component** | **Master Mix (µL)** |
| --- | --- |
| PURExpress Solution A | 4 |
| PURExpress Solution B | 3 |
| RNase Inhibitor | 0.5 |
| `pT7-lacO-plamGFP` (10 nM) | 0.5 |
| LacI (10 mM) | 0.5 |
| **Master Mix Total** | **9** |

| **Component** | **Per Reaction (µL)** |
| --- | --- |
| Master Mix | 9 |
| Inducer | 1 |
| **Total** | **10** |

### Expected Performance

The LacI-IPTG module was validated in NEB PURExpress reactions. Purified LacI repressor protein (MedChemExpress HY-P70247) was added at the final concentrations indicated. `pT7-lacO-plamGFP` plasmid DNA was added at 5–10 nM.

Repression is observed across the range of 15.63–1000 nM LacI, with 1000 nM providing strong repression and suitable dynamic range for induction. A small increase in expression is observed around 62.5 nM repressor; a similar effect has been observed in TetR data and may reflect preserved PURE translational capacity under moderate transcriptional repression. The 250 nM datapoint is likely a technical failure. IPTG induction is effective across 500–2000 nM, consistent with concentrations used in cellular and cell-free systems. All induced samples show expression at or above the unrepressed positive control, a behavior that replicates across experiments and is under further investigation.

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

## References

- Garamella J, Marshall R, Rustad M, Noireaux V. (2016). The All E. coli TX-TL Toolbox 2.0: A Platform for Cell-Free Synthetic Biology. *ACS Synthetic Biology*. [https://doi.org/10.1021/sb400131a](https://doi.org/10.1021/sb400131a)

# Credits

- b.next
