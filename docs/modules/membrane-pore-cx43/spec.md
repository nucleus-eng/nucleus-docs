---
title: "Membrane Pore: Cx43"
subtitle: "Module Specification"
site:
    hide-toc: true
    numbered_references: false
thumbnail: cell-insertion-sample.png
---
# Overview

The Cx43 Module expresses connexin 43 (Cx43), a mammalian gap junction protein, that self-assembles into hexameric hemichannels (connexons) that spontaneously integrate into the membrane of synthetic cells and permit the passage of molecules up to ~1 kDa. Cx43 provides an alternative to α-hemolysin: its status as a non-select agent makes it easier to distribute, and its capacity to form gap junctions between neighboring cells represents a new function that opens a path toward tissue-like assemblies.

This Module was contributed to the Nucleus Community by Ahmed Sihorwala (Belardi Lab, UT Austin), based on the construct design from the Stachowiak Lab and the publication [Sihorwala et al., 2023](https://doi.org/10.1021/jacs.2c12491). Validation data is presented in the DevNote [Cx43 Cell: DNA Validation](https://doi.org/10.63765/xvxu3274).

:::{attention}
This Module has not been validated in Nucleus Cytosol ≥ v0.5. Expected performance data below is from PURExpress cells.
:::

:::::{tab-set}

::::{tab-item} Schematic

:::{figure} xref:devnote-cx43#fig:scheme
Depiction of connexin and its relationship to a connexon: (left) Connexins are membrane-spanning proteins whose N- and C-termini are located in the cytoplasm; (right) connexons are complexes of six connexins. Figure by [Totland et al., 2023](https://doi.org/10.1016/j.bbadis.2023.166812) used under CC-BY-4.0 / cropped from original.
:::

::::

::::{tab-item} Designs

:::{attention}
Design files for the constructs below are available [Nucleus DNA repository](https://github.com/nucleus-eng/DNA) and in the [DevNote](https://doi.org/10.63765/xvxu3274).
:::

| Construct             | Size    | Description                                                            | **File**                                                                                 |
| --------------------- | ------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `pOpen-pT7-Cx43`      | 3320 bp | Expresses wild-type Cx43 under T7 promoter in pOpen backbone           | [pOpen-Cx43.gb](https://github.com/nucleus-eng/DNA/blob/main/pores/pOpen-Cx43.gb)        |
| `pOpen-pT7-Cx43-eGFP` | 3996 bp | Expresses Cx43-eGFP fusion protein under T7 promoter in pOpen backbone | [pOpen-Cx43-eGFP](https://github.com/nucleus-eng/DNA/blob/main/pores/pOpen-Cx43-eGFP.gb) |

::::

:::::

## Cytosol

Cx43 requires a lipid membrane environment for proper folding and pore assembly. To the best of our knowledge, this Module cannot be functionally deployed in Nucleus Cytosol alone.

## Cells

### Expected Performance

**Insertion Assay** — Liposomes encapsulating NEB PURExpress and `pOpen-pT7-Cx43-eGFP` were incubated at 37°C for 6 hrs. Green fluorescent rings around liposomes confirm membrane localization of Cx43-eGFP. Control liposomes lacking the Cx43 plasmid show no rings.

:::::{tab-set}

::::{tab-item} +Cx43

:::{figure} cell-insertion-sample.png
Liposomes expressing Cx43-eGFP. Green fluorescent rings surrounding liposomes indicate successful membrane localization of Cx43-eGFP hemichannels. 488 nm (green, Cx43-eGFP) and 561 nm (red, membrane label) channels overlaid.
:::

::::

::::{tab-item} -Cx43

:::{figure} cell-insertion-control.png
Control liposomes without Cx43 plasmid. No green fluorescent rings are observed. Faint green signal within liposomes is encapsulated PURE.
:::

::::

:::::

:::{note} Additional focus views
Higher-magnification views of individual Cx43-eGFP-expressing liposomes are available in the [DevNote](https://doi.org/10.63765/xvxu3274).
:::

**Leakage Assay** — Liposomes co-encapsulating NEB PURExpress, `pOpen-pT7-Cx43`, and Alexa Fluor 647 dye were incubated at 37°C for 6 hrs and imaged by confocal microscopy every 10 min.

:::{figure} cell-leakage-kinetics.png
Background-subtracted Alexa Fluor 647 fluorescence intensity over 6 hrs at 37°C. Liposomes containing Cx43 show a progressive decrease in encapsulated dye fluorescence relative to controls, consistent with pore-mediated dye leakage.
:::

:::::{tab-set}

::::{tab-item} +Cx43

:::{figure} cell-leakage-timeseries-sample.png
Time series of Cx43-reconstituted liposomes encapsulating Alexa Fluor 647 over 6 hrs at 37°C (images every 10 min, starting 40 min after preparation). Progressive loss of fluorescence is observed as dye leaks through Cx43 channels. Scale bar: 500 µm.
:::

::::

::::{tab-item} -Cx43

:::{figure} cell-leakage-timeseries-control.png
Time series of control liposomes encapsulating Alexa Fluor 647 over 6 hrs at 37°C. Dye fluorescence is maintained throughout, confirming that leakage requires Cx43 expression. Scale bar: 500 µm.
:::

::::

:::::

:::::{tab-set}

::::{tab-item} +Cx43 (start)

:::{figure} cell-leakage-startpoint-sample.png
Confocal image of Cx43-reconstituted liposomes at the start point, 40 min after preparation. Some liposomes already show reduced fluorescence, consistent with early dye leakage at room temperature. Scale bar: 500 µm.
:::

::::

::::{tab-item} +Cx43 (endpoint)

:::{figure} cell-leakage-endpoint-sample.png
Endpoint confocal image (6 hrs 40 min) of Cx43-reconstituted liposomes. A higher proportion of non-fluorescent liposomes is observed relative to controls. Scale bar: 500 µm.
:::

::::

::::{tab-item} -Cx43 (start)

:::{figure} cell-leakage-startpoint-control.png
Confocal image of control liposomes at the start point, 40 min after preparation. Liposomes remain fluorescent, confirming dye retention in the absence of Cx43. Scale bar: 500 µm.
:::

::::

::::{tab-item} -Cx43 (endpoint)

:::{figure} cell-leakage-endpoint-control.png
Endpoint confocal image (6 hrs 40 min) of control liposomes. Most liposomes remain fluorescent throughout the experiment. Scale bar: 500 µm.
:::

::::

:::::

# Credits

Module contributed by Ahmed Sihorwala (Belardi Lab, UT Austin). Validation data by Yen-Yu Hsu (b.next).
