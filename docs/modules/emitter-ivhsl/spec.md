---
title: "Emitter: IV-HSL"
subtitle: "Module Specification"
thumbnail: mechanism-schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The IV-HSL Emitter module produces and releases N-isovaleryl-L-homoserine lactone (IV-HSL), a branched acyl-homoserine lactone, enabling enzymatic small-molecule production, molecule release as a reporter output, inter-cell communication, and co-culture of synthetic cells with living bacteria. The module is based on work by [Smith, Hartmann, and Booth](https://doi.org/10.1038/s41589-023-01374-7).

IV-HSL offers several advantages: it crosses synthetic cell membranes; its uncommon branched-chain structure makes it orthogonal from many other HSLs [[Lindemann, 2011](https://www.pnas.org/doi/full/10.1073/pnas.1114125108)]; and it activates expression in receiver cells at picomolar concentrations. The module encodes the BjaI enzyme under a constitutive T7 promoter. BjaI converts S-adenosylmethionine (SAM) and isovaleryl coenzyme A (IV-CoA) into IV-HSL, which diffuses out of the cell through the lipid bilayer. A companion *E. coli* receiver construct (`bjaR-GFP-native`) detects IV-HSL and produces a fluorescent output.

:::::{tab-set}

::::{tab-item} Schematic
:::{figure} mechanism-schematic.png
Design schematic of the IV-HSL Emitter module. `pT7-bjaI` expresses the BjaI enzyme, which converts SAM and IV-CoA substrates into IV-HSL. IV-HSL diffuses across the lipid bilayer and activates GFP expression in *E. coli* receiver cells via the BjaR transcription factor.
:::
::::

::::{tab-item} Designs
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-bjaI` | N/A | Nucleus v0.3.0 Distribution Plate *(upcoming)* |
| `bjaR-GFP-native` | N/A | Nucleus v0.3.0 Distribution Plate *(upcoming)* |
::::

:::::

## Cytosols

### Usage

Add equimolar amounts of SAM and IV-CoA at 0.3 µM and 0.08 µM final concentration, respectively, to a standard PURE reaction containing `pT7-bjaI`. Volumes in µL.

| **Component** | **Sample** | **Negative Control** | **Positive Control** | **Notes** |
| --- | --- | --- | --- | --- |
| PURE Solution A | 12 | 12 | 0 | Energy solution: small molecules |
| PURE Solution B | 9 | 9 | 0 | Proteins and ribosomes |
| RNase Inhibitor | 1.5 | 1.5 | 0 | Prevents RNase activity |
| `pOpen-pT7-bjaI` (~200 ng/µL) | 1.5 | 0 | 0 | DNA encoding BjaI |
| SAM (5 mM) | 1.8 | 1.8 | 0 | Substrate for IV-HSL production |
| IV-CoA (5 mM) | 0.48 | 0.48 | 0 | Substrate for IV-HSL production |
| OptiPrep | 1.5 | 1.5 | 1.5 | Adds density for phase-transfer |
| IV-HSL (10 µM) | 0 | 0 | 0.3 | Commercial IV-HSL for positive control |
| 3M Glucose | 0 | 0 | 8.46 | |
| ddH₂O | 2.22 | 3.72 | 19.74 | |
| **Total** | **30** | **30** | **30** | |

### Expected Performance

PURE reactions were incubated for 4 hours, then added to log-phase *E. coli* receiver cell cultures containing `bjaR-GFP-native`. GFP fluorescence was measured over 6 hours at 5-minute timepoints using a BioTek Cytation 5 plate reader. Expression in XL-10 Gold cells containing `bjaR-GFP-native` is equivalent for bulk PURE reactions with `pT7-bjaI` and substrates and for emitter cells containing IV-HSL without plasmid DNA — both show a significant response over the negative control.

:::::{tab-set}

::::{tab-item} Kinetics
:::{figure} cytosol-performance-kinetics.png
Expression kinetics of *E. coli* receiver cells modified with `bjaR-GFP-native` in response to IV-HSL produced by PURE reactions.
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-performance-endpoint.png
Expression of *E. coli* receiver cells modified with `bjaR-GFP-native` at steady state.
:::
::::

:::::

## Cells

:::{figure} emitter-overview.png
The IV-HSL Emitter module in the Base Cell.
:::

### Expected Performance

Emitter Cells were constructed and co-cultured with *E. coli* containing `bjaR-GFP-native`. Time-series confocal microscopy (Revvity Operetta CLS) was performed over 8 hours collecting red (Rhodamine-B), green (GFP), and brightfield images at 40× magnification across multiple fields per well at approximately 15-minute intervals.

:::{figure} cell-performance-endpoint.png
**Emitter Cell Endpoint Montage.** Single field of view at t = 8 hours. **(green)** *E. coli* producing GFP in response to IV-HSL emitted by the Emitter Cells. **(red)** Emitter cells with rhodamine-labeled membrane. **(grey)** Brightfield. **(rgb)** Merged image.
:::

::::{hint} The Emitter Cell causes E. coli to express GFP in response to IV-HSL.
:class: dropdown

:::{figure} cell-liposome-exclusion.png
**Emitter Cell Timeseries. (Positive)** Liposomes contain PURE and 100 nM IV-HSL. **(Negative)** Liposomes contain PURE supplemented with SAM and IV-HSL, but no DNA encoding BjaI. **(Emitter)** Liposomes contain PURE expressing BjaI from `pT7-bjaI`. Exposures are matched between wells. Each field of view is 167 µm wide.
:::

::::

## References

- Smith, J. M., Hartmann, D. & Booth, M. J. Engineering cellular communication between light-activated synthetic cells and bacteria. *Nature Chemical Biology* **19**, 1138–1146 (2023). [10.1038/s41589-023-01374-7](https://doi.org/10.1038/s41589-023-01374-7)
- Lindemann, A. et al. Isovaleryl-homoserine lactone, an unusual branched-chain quorum-sensing signal from the soybean symbiont *Bradyrhizobium japonicum*. *Proceedings of the National Academy of Sciences* **108**, 16765–16770 (2011). [10.1073/pnas.1114125108](https://www.pnas.org/doi/full/10.1073/pnas.1114125108)
