---
title: "Membrane Pore: Cx43"
subtitle: "Module Specification"
status: unvalidated-published
site:
    hide-toc: true
    numbered_references: false
thumbnail: cell-insertion-sample.png
---
# Overview

The Cx43 Module expresses connexin 43 (Cx43), a mammalian gap junction protein, that self-assembles into hexameric hemichannels (connexons) that spontaneously integrate into the membrane of synthetic cells and permit the passage of molecules up to ~1 kDa. Cx43 provides an alternative to α-hemolysin: its status as a non-select agent makes it easier to distribute, and its capacity to form gap junctions between neighboring cells represents a new function that opens a path toward tissue-like assemblies.

The construct design is from the Stachowiak Lab ([Sihorwala et al., 2023](https://doi.org/10.1021/jacs.2c12491)). Validation data is presented in the DevNote [Cx43 Cell: DNA Validation](https://doi.org/10.63765/xvxu3274).

:::{attention} Not yet validated
This Module has not been validated in Nucleus Cytosol. Expected performance data below is from PURExpress cells.
:::

:::::{tab-set}

::::{tab-item} Schematic

:::{figure} xref:devnote-cx43#fig:scheme
Depiction of connexin and its relationship to a connexon: (left) Connexins are membrane-spanning proteins whose N- and C-termini are located in the cytoplasm; (right) connexons are complexes of six connexins. Figure by [Totland et al., 2023](https://doi.org/10.1016/j.bbadis.2023.166812) used under CC-BY-4.0 / cropped from original.
:::

::::

:::::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA

:::{attention}
Design files for the constructs below are available in the [Nucleus DNA repository](https://github.com/nucleus-eng/DNA) and in the [DevNote](https://doi.org/10.63765/xvxu3274).
:::

| Construct | Size | Description | File |
| --------------------- | ------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `pOpen-pT7-Cx43` | 3320 bp | Circular plasmid that expresses wild-type Cx43 under T7 promoter in pOpen backbone | [pOpen-Cx43.gb](https://github.com/nucleus-eng/DNA/blob/main/pores/pOpen-Cx43.gb) |
| `pOpen-pT7-Cx43-eGFP` | 3996 bp | Circular plasmid that expresses Cx43-eGFP fusion protein under T7 promoter in pOpen backbone | [pOpen-Cx43-eGFP.gb](https://github.com/nucleus-eng/DNA/blob/main/pores/pOpen-Cx43-eGFP.gb) |

::::

::::{tab-item} Cytosol

The Insertion Assay reaction in NEB PURExpress, 20 µL.

| Component | Volume (µL) |
| --- | --- |
| NEB PURExpress Solution A | 8 |
| NEB PURExpress Solution B | 6 |
| RNase inhibitor | 1 |
| `pOpen-pT7-Cx43-eGFP` (100 ng/µL) | 2 |
| (Optional) OptiPrep | 0.67 |
| Nuclease-free water | 2.33 |

:::{attention}
@Editor: the pore passes cargo down its gradient (Pore ⊗ Membrane ⊗ Cargo[φₚ] ⟶ Membrane[permeable]); this member's cutoff φₚ is ~1 kDa. State the outer solution as a requirement: it holds every species of Cargo[φₚ] the interior needs at working concentration.
:::

::::

::::{tab-item} Membrane

[Base Membrane: POPC/Chol](../membrane-popc-chol/spec.md) at its default composition.

| Component | Target (mmol/mol) |
| --- | --- |
| POPC | 699.3 |
| Cholesterol | 299.7 |
| (Optional) Fluorescent lipid label | 1 |

::::

:::::

# Expected Behavior

## Cells

**Insertion Assay** — The Cx43 Module is expected to localize to the membrane of the synthetic cells that express it. Synthetic cells encapsulating NEB PURExpress and `pOpen-pT7-Cx43-eGFP`, incubated at 37 °C for 6 h, show green fluorescent rings around the synthetic cells, which confirm membrane localization of Cx43-eGFP. Control synthetic cells lacking the Cx43 plasmid show no rings. Imaging used a Squid+ (Cephla) with an Olympus UPLXAPO40X 40x objective, at 80 ms for the 561 channel and 200 ms for the 488 channel ([Hsu, 2025](https://doi.org/10.63765/xvxu3274)).

| Component | +Cx43 (µL) | -Cx43 (µL) |
| --- | --- | --- |
| NEB PURExpress Solution A | 8 | 8 |
| NEB PURExpress Solution B | 6 | 6 |
| RNase inhibitor | 1 | 1 |
| `pOpen-pT7-Cx43-eGFP` (100 ng/µL) | 2 | 0 |
| (Optional) OptiPrep | 0.67 | 0.67 |
| Nuclease-free water | 2.33 | 4.33 |

:::::{tab-set}

::::{tab-item} +Cx43

:::{figure} cell-insertion-sample.png
Fluorescence micrograph of synthetic cells expressing Cx43-eGFP. Green fluorescent rings surrounding the synthetic cells indicate successful membrane localization of Cx43-eGFP hemichannels. 488 nm (green, Cx43-eGFP) and 561 nm (red, membrane label) channels overlaid.
:::

::::

::::{tab-item} -Cx43

:::{figure} cell-insertion-control.png
Fluorescence micrograph of control synthetic cells without Cx43 plasmid. No green fluorescent rings are observed. Faint green signal within the synthetic cells is encapsulated PURE.
:::

::::

:::::

:::{note} Additional focus views
Higher-magnification views of individual Cx43-eGFP-expressing synthetic cells are available in the [DevNote](https://doi.org/10.63765/xvxu3274).
:::

**Leakage Assay** — The Cx43 Module is expected to let encapsulated dye leave the synthetic cells that express it. Synthetic cells co-encapsulating NEB PURExpress, `pOpen-pT7-Cx43`, and Alexa Fluor 647 dye, incubated at 37 °C for 6 h and imaged by confocal microscopy every 10 min, lose encapsulated fluorescence over time. Control synthetic cells without the Cx43 plasmid retain it. Imaging used an Operetta confocal microscope at 40x, at 80 ms for the 561 channel and 20 ms for the 647 channel ([Hsu, 2025](https://doi.org/10.63765/xvxu3274)).

| Component | +Cx43 (µL) | -Cx43 (µL) |
| --- | --- | --- |
| NEB PURExpress Solution A | 8 | 8 |
| NEB PURExpress Solution B | 6 | 6 |
| RNase inhibitor | 1 | 1 |
| `pOpen-pT7-Cx43` (100 ng/µL) | 2 | 0 |
| Alexa Fluor 647 (1 mM) | 0.1 | 0.1 |
| (Optional) OptiPrep | 0.67 | 0.67 |
| Nuclease-free water | 2.23 | 4.23 |

:::{attention}
@Editor: the imaging readout has no Process page to link. Link the readout.
:::

:::{figure} cell-leakage-kinetics.png
Plot of background-subtracted Alexa Fluor 647 fluorescence intensity over 6 h at 37 °C. Synthetic cells containing Cx43 show a progressive decrease in encapsulated dye fluorescence relative to controls, consistent with pore-mediated dye leakage.
:::

:::::{tab-set}

::::{tab-item} +Cx43

:::{figure} cell-leakage-timeseries-sample.png
Confocal time series of synthetic cells expressing Cx43 and encapsulating Alexa Fluor 647 over 6 h at 37 °C (images every 10 min, starting 40 min after preparation). Progressive loss of fluorescence is observed as dye leaks through Cx43 channels. Scale bar: 500 µm.
:::

::::

::::{tab-item} -Cx43

:::{figure} cell-leakage-timeseries-control.png
Confocal time series of control synthetic cells encapsulating Alexa Fluor 647 over 6 h at 37 °C. Dye fluorescence is maintained throughout, confirming that leakage requires Cx43 expression. Scale bar: 500 µm.
:::

::::

:::::

:::::{tab-set}

::::{tab-item} +Cx43 (start)

:::{figure} cell-leakage-startpoint-sample.png
Confocal image of synthetic cells expressing Cx43 at the start point, 40 min after preparation. Some synthetic cells already show reduced fluorescence, consistent with early dye leakage at room temperature. Scale bar: 500 µm.
:::

::::

::::{tab-item} +Cx43 (endpoint)

:::{figure} cell-leakage-endpoint-sample.png
Confocal endpoint image (6 h 40 min) of synthetic cells expressing Cx43. A higher proportion of non-fluorescent synthetic cells is observed relative to controls. Scale bar: 500 µm.
:::

::::

::::{tab-item} -Cx43 (start)

:::{figure} cell-leakage-startpoint-control.png
Confocal image of control synthetic cells at the start point, 40 min after preparation. The synthetic cells remain fluorescent, confirming dye retention in the absence of Cx43. Scale bar: 500 µm.
:::

::::

::::{tab-item} -Cx43 (endpoint)

:::{figure} cell-leakage-endpoint-control.png
Confocal endpoint image (6 h 40 min) of control synthetic cells. Most synthetic cells remain fluorescent throughout the experiment. Scale bar: 500 µm.
:::

::::

:::::

# Requirements

- Requires a membrane (e.g. [Base Membrane: POPC/Chol](../membrane-popc-chol/spec.md)).
- Requires pT7 transcription and translation, when expressing from DNA (e.g. [Base Cytosol](../base-cytosol/spec.md)).
- Requires that molecules passing through the pore be about 1 kDa or smaller ([Sihorwala et al., 2023](https://doi.org/10.1021/jacs.2c12491); [Hsu, 2025](https://doi.org/10.63765/xvxu3274)).
- Requires, when the interior reaction must keep running after the pore is open, that the outer solution hold every species the pore passes that the interior needs, at working concentration: SMix at 1x for a [Base Cytosol](../base-cytosol/spec.md) interior, or NEB Solution A at 1x (the stock is 2.5x) for an NEB PURExpress interior. Ribosomes, polymerase and plasmid stay in. An assay that reads what leaks out of the interior needs no outer-solution supply ([Sihorwala et al., 2023](https://doi.org/10.1021/jacs.2c12491); [Hsu, 2025](https://doi.org/10.63765/xvxu3274)).

# Processes

- [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) — prepares synthetic cells by encapsulating an inner solution in a membrane.

# Credits

Module contributed by Ahmed Sihorwala (Belardi Lab, UT Austin). Validation data by Yen-Yu Hsu (b.next).
