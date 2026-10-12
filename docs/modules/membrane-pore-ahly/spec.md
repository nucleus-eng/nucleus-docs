---
title: "Membrane Pore: α-Hemolysin"
subtitle: "Module Specification"
status: unvalidated-published
site:
    hide-toc: true
    numbered_references: false
thumbnail: cell-gfp-quench.png
---
# Overview

The α-Hemolysin (aHly) Module produces a self-inserting membrane pore that allows passive transport of small molecules between the cytosol of a synthetic cell and its external environment ([Noireaux and Libchaber, 2004](https://doi.org/10.1073/pnas.0408236101), [Harjung et al., 2023](https://doi.org/10.1101/2023.10.06.561148)). The pore is assembled from seven monomers (33.2 kDa each, 293 amino acids) with an outer diameter of 10 nm and an inner diameter of (1.6–4.6) nm — sufficient for molecules up to ~3 kDa. The height of the 3 nm hydrophobic patch along the pore matches the thickness of the non-polar layer of a typical phospholipid membrane, making aHly a useful tool for confirming bilayer (as opposed to multilayer) formation in synthetic cells ([Song et al., 1996](https://doi.org/10.1126/science.274.5294.1859)).

aHly is a toxin derived from *Staphylococcus aureus* and requires controlled material handling.

:::{attention}
This Module is not actively supported. At this time, the Nucleus Distribution does not support controlled material reagents. For new implementations, we recommend the [Membrane Pore: Cx43](../membrane-pore-cx43/spec.md) Module, which does not require controlled material handling. Cx43 passes molecules up to ~1 kDa, so it replaces aHly only where the cargo is below that.
:::

:::{attention} Not yet validated
This Module has not been validated in Nucleus Cytosol. Expected performance data below is from PURExpress cells.
:::

aHly can be used in two ways: expressed directly from `pT7-aHly` within the PURE system, or added as purified protein from an external source.

:::{attention}
The working concentration of purified aHly is not specified. The Reference Composition below covers the expression route.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA

:::{attention}
`pT7-aHly` is not in the [Nucleus DNA repository](https://github.com/nucleus-eng/DNA).
:::

| Construct  | Description                                                 | Length (bp)    | Supply route   |
| ---------- | ----------------------------------------------------------- | -------------- | -------------- |
| `pT7-aHly` | Expresses α-hemolysin under T7 promoter for PURE expression | Not documented | Not documented |

::::

::::{tab-item} Cytosol

aHly is expressed in PURE by including `pT7-aHly` as a template. Reactions use the NEB PURExpress In Vitro Protein Synthesis Kit (E6800) and are assembled as in Assemble Solution, following the [Assemble Base Cytosol](../../processes/assemble-base-cytosol/main.md) protocol.

| Component                 | Volume (µL) | Working concentration |
| ------------------------- | ----------- | --------------------- |
| NEB Solution A            | 4           | Not specified         |
| NEB Solution B            | 3           | Not specified         |
| RNase inhibitor           | 1           | 4000 U/mL             |
| `pT7-aHly` (10 nM)        | 1           | 1 nM                  |
| Nuclease-free water       | 1           | n/a                   |
| **Total**                 | **10**      |                       |

::::

::::{tab-item} Membrane

[Base Membrane: POPC/Chol](../membrane-popc-chol/spec.md) at its default composition.

| Component | Target (mmol/mol) |
| --- | --- |
| POPC | 699.3 |
| Cholesterol | 299.7 |
| (Optional) Fluorescent lipid label | 1 |

:::{attention}
@Editor: the pore passes cargo down its gradient (Pore ⊗ Membrane ⊗ Cargo[φₚ] ⟶ Membrane[permeable]); this member's cutoff φₚ is ~3 kDa. State the outer solution as a requirement: it holds every species of Cargo[φₚ] the interior needs at working concentration.
:::

::::

:::::

# Expected Behavior

## Cytosols

aHly Module is expected to be expressed from `pT7-aHly` in PURE as a monomer band at ~33 kDa (red arrows), read by [Protein Gel](../../processes/protein-gel/main.md), which shows expression of the product, not leakage. Two loading volumes are shown (5 µL and 2.5 µL) alongside a no-template control (-).

:::{figure} cytosol-protein-gel.png
Protein gel showing aHly expression in PURE. Lanes labeled "hly" and "(-)" correspond to reactions with and without `pT7-aHly`. Red arrows indicate the aHly band at ~33 kDa. Left pair: 5 µL; right pair: 2.5 µL per lane.
:::

## Cells

aHly Module is expected to quench GFP production in synthetic cells that co-express it with `pT7-eGFP`: inserted pores let the small molecules needed for transcription and translation leak into the outer solution. In the absence of `pT7-aHly`, GFP is produced in a subpopulation of cells. Samples were incubated at 37 °C for 7.5 h and imaged by epifluorescence microscopy, which shows the leakage. @Editor: the epifluorescence imaging readout has no Process page to link. Link or name the readout.

The outer solution is an osmolarity-matched buffer without energy molecules (10 mM HEPES, 790 mM glucose). Prepare master mix for 3 reactions to account for dead volume.

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
| Nuclease-free water | 0 | 0.5 |
| **Total** | **10** | **10** |

:::{figure} cell-gfp-quench.png
Epifluorescence microscopy of synthetic cells. (Left) GFP + aHly: GFP production is quenched when aHly is co-expressed, as small molecules leak through the inserted pores. (Right) GFP only: GFP is produced in a subpopulation of cells in the absence of aHly. Red channel: membrane label; green channel: GFP. Scale bar: 100 µm.
:::

# Requirements

Requires a membrane (e.g. [Base Membrane: POPC/Chol](../membrane-popc-chol/spec.md)).

Requires pT7 transcription and translation, when using `pT7-aHly` (e.g. [Base Cytosol](../base-cytosol/spec.md)).

Requires that molecules crossing the pore are no larger than ~3 kDa.

Requires controlled material handling.

Requires, when the interior reaction must keep running after the pore is open, that the outer solution holds, at working concentration, every species the pore passes that the interior needs. For a PURExpress interior these are the small substrates; ribosomes, polymerase and plasmid stay in. An assay that reads what leaks out of the interior needs no outer-solution supply.

# Processes

- [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) — prepares synthetic cells by encapsulating an inner solution in a membrane.

# Materials

We recommend purchasing aHly as purified protein and resuspending to 10 µM in ultrapure water. Introduce purified protein to the outer solution of synthetic cells rather than expressing from DNA to avoid variability in expression efficiency.

| Material | Description | Manufacturer | Part # |
| --- | --- | --- | --- |
| α-Hemolysin | Purified α-hemolysin protein, resuspended to 10 µM in ultrapure water | MedChemExpress | HY-P2967 |

:::{hint} Aggregation at high concentrations
:class: dropdown
High concentrations of purified aHly (>100 nM) are more likely to aggregate. Keep your working concentrations below this threshold.
:::

# Credits

Module developed by the [Devaraj Lab](https://www.devarajgroup.com/).
