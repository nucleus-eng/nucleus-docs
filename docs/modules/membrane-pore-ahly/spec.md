---
title: "Membrane Pore: α-Hemolysin"
subtitle: "Module Specification"
site:
    hide-toc: true
    numbered_references: false
thumbnail: cell-gfp-quench.png
---
# Overview

The α-Hemolysin (aHly) Module produces a self-inserting membrane pore that allows passive transport of small molecules between the cytosol of a synthetic cell and its external environment. The pore is assembled from seven monomers (33.2 kDa each, 293 amino acids) with an outer diameter of 10 nm and an inner diameter of (1.6–4.6) nm — sufficient for molecules up to ~3 kDa. The height of the 3 nm hydrophobic patch along the pore matches the thickness of the non-polar layer of a typical phospholipid membrane, making aHly a useful tool for confirming bilayer (as opposed to multilayer) formation in synthetic cells.

aHly is a toxin derived from *Staphylococcus aureus* and requires BSL-2 handling. The [Cx43 Module](../membrane-pore-cx43/spec.md) provides a functionally comparable alternative that does not.

:::{attention}
This Module is not actively supported. At this time, the Nucleus Distribution does not support BSL-2 reagents. For new implementations, we recommend the [Cx43 Module](../membrane-pore-cx43/spec.md).
:::

aHly can be used in two ways: expressed directly from `pT7-aHly` within the PURE system, or added as purified protein from an external source. We recommend the purified protein approach for most applications.

:::::{tab-set}

::::{tab-item} Schematic

:::{note}
A schematic for this module is not yet available.
:::

::::

::::{tab-item} Designs

:::{attention}
`pT7-aHly` is not in the [Nucleus DNA repository](https://github.com/nucleus-eng/DNA).
:::

| Construct  | Description                                                 |
| ---------- | ----------------------------------------------------------- |
| `pT7-aHly` | Expresses α-hemolysin under T7 promoter for PURE expression |

::::

:::::

## Cytosols

### Usage

We recommend purchasing aHly as purified protein (e.g., MedChemExpress Cat. No. HY-P2967) and resuspending to 10 µM in milliQ water. Introduce purified protein to the outer solution of synthetic cells rather than expressing from DNA to avoid variability in expression efficiency.

Alternatively, aHly can be expressed directly in PURE by including `pT7-aHly` as a template. Reactions are assembled following the [Assemble Base Cytosol](../../processes/assemble-base-cytosol/main.md) protocol.

| Component          | Volume (µL) |
| ------------------ | ----------- |
| Solution A         | 4           |
| Solution B         | 3           |
| RNase Inhibitor    | 1           |
| `pT7-aHly` (10 nM) | 1           |
| Nucleus-Free Water | 1           |
| **Total**          | **10**      |

:::{hint} Note: aggregation at high concentrations
:class: dropdown
High concentrations of purified aHly (>100 nM) are more likely to aggregate. Keep your working concentrations below this threshold.
:::

### Expected Performance

We validated aHly expression in cytosol by protein gel. Bands at ~33 kDa (red arrows) confirm successful expression of aHly monomer from `pT7-aHly` in PURE. Two loading volumes are shown (5 µL and 2.5 µL) alongside a no-template control (-).

:::{figure} cytosol-protein-gel.png
Protein gel showing aHly expression in PURE. Lanes labeled "hly" and "(-)" correspond to reactions with and without `pT7-aHly`. Red arrows indicate the aHly band at ~33 kDa. Left pair: 5 µL; right pair: 2.5 µL per lane.
:::

## Cells

### Usage

To demonstrate functional pore insertion, co-express aHly is with a reporter (`pT7-eGFP`) in synthetic cells using an osmolarity-matched buffer without energy molecules (10 mM HEPES, 790 mM glucose) as the outer solution. As aHly inserts into the membrane, small molecules required for transcription and translation leak out into the outer solution, quenching GFP production. 

Prepare master mix for 3 reactions to account for dead volume.

| Component | Per Reaction (µL) | Master Mix ×3 (µL) |
| --- | --- | --- |
| *Master Mix* | | |
| NEB Solution A | 4 | 12 |
| NEB Solution B | 3 | 9 |
| RNase Inhibitor | 0.5 | 1.5 |
| Sucrose (2 M) | 1.5 | 4.5 |
| **Subtotal** | **9** | **27** |
| | | |
| | +aHly | −aHly |
| Master Mix | 9 | 9 |
| `pT7-aHly` | 0.5 | 0 |
| `pT7-eGFP` | 0.5 | 0.5 |
| Nucleus-Free Water | 0 | 0.5 |
| **Total** | **10** | **10** |

### Expected Performance

GFP production is quenched in synthetic cells expressing aHly, confirming functional pore insertion and membrane permeabilization. In the absence of `pT7-aHly`, GFP is produced in a subpopulation of cells. Samples incubated at 37°C for 7.5 hrs.

:::{figure} cell-gfp-quench.png
Epifluorescence microscopy of synthetic cells. (Left) GFP+aHly: GFP production is quenched when aHly is co-expressed, as small molecules leak through the inserted pores. (Right) GFP only: GFP is produced in a subpopulation of cells in the absence of aHly. Red channel: membrane label; green channel: GFP. Scale bar: 100 µm.
:::

## References

- Song, L., et al. (1996). Structure of staphylococcal α-hemolysin, a heptameric transmembrane pore. *Science*, [10.1126/science.274.5294.1859](https://doi.org/10.1126/science.274.5294.1859)
- Noireaux, V., and Libchaber, A. (2004). A vesicle bioreactor as a step toward an artificial cell assembly. *PNAS*, [10.1073/pnas.0408236101](https://doi.org/10.1073/pnas.0408236101)
- Harjung, A., Fracassi, A., and Devaraj, N. K. (2023). Modular engineering of α-hemolysin for synthetic cell construction. *bioRxiv*, [10.1101/2023.10.06.561148](https://doi.org/10.1101/2023.10.06.561148)
- Nishimura, K., et al. (2012). Cell-free protein synthesis inside giant unilamellar vesicles analyzed by flow cytometry. *Langmuir*, [10.1021/la3001703](https://doi.org/10.1021/la3001703)

# Credits

Module developed by the [Devaraj Lab](https://www.devarajgroup.com/).
