---
title: "Responder: aTc → IV-HSL"
subtitle: Implementation
status: unvalidated-published
site:
    hide-toc: true
---
# Overview

The aTc → IV-HSL Responder Implementation combines the TetR-aTc Detector Module and the IV-HSL Emitter Module ([Smith, Hartmann, and Booth., 2023](https://doi.org/10.1038/s41589-023-01374-7)) to produce a synthetic cell that generates isovaleryl-l-homoserine lactone (IV-HSL; [Lindemann et al., 2011](https://doi.org/10.1073/pnas.1114125108)) in response to anhydrotetracycline (aTc; [Lutz and Bujard, 1997](https://doi.org/10.1093/nar/25.6.1203)). The module is implemented as a single genetic construct encoding the BjaI enzyme under control of the tet operator. A co-cultured *E. coli* receiver strain carrying `bjaR-GFP-native` reports IV-HSL production by expressing GFP.

:::{attention} Not yet validated
This implementation has not been validated in Nucleus Cytosol.
:::

:::{figure} mechanism-schematic.png
:align: center
:width: 75%

aTc activates BjaI expression by relieving TetR repression. BjaI converts SAM and IV-CoA into IV-HSL, which diffuses to co-cultured *E. coli* receiver cells and induces GFP expression.
:::

:::{figure} cell-schematic.png
:align: center
:width: 75%

The aTc → IV-HSL Responder in the Base Cell. aTc enters the cell and releases TetR from the tetO operator, allowing BjaI expression. BjaI produces IV-HSL from SAM and IV-CoA; IV-HSL diffuses to neighboring *E. coli* receiver cells.
:::

# Protocol

Three construct variants were evaluated: `pT7-tetO-bjaI` (single operator), `tetO-pT7-tetO-bjaI` (sandwich operator), and `pT7-tetO-tetO-bjaI` (train operator). `pT7-tetO-bjaI` has poor dynamic range — leaky expression in the off state produces sufficient IV-HSL to induce receiving *E. coli* cells. `tetO-pT7-tetO-bjaI` and `pT7-tetO-tetO-bjaI` resolve this by providing tight repression in the off state ([Lutz and Bujard, 1997](https://doi.org/10.1093/nar/25.6.1203)). We chose to move forward with `pT7-tetO-tetO-bjaI`.

The IV-HSL Emitter Module may be implemented by assembling the `pT7-tetO-tetO-bjaI` responder construct within a standard PURE reaction, following [Assemble Base Cytosol](../../processes/assemble-base-cytosol/main.md). Add equimolar amounts of the substrates SAM and IV-CoA at 0.3 µM and 0.08 µM final concentration, respectively.

**DNA Parts**

| **Name**             | **Length (bp)** | **File**                                                                                                                   |
| -------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `pT7-tetO-tetO-bjaI` | 908             | [pT7-tetO-tetO-bjaI.gb (linear)](https://github.com/nucleus-eng/DNA/blob/main/emitters/pT7-tetO-tetO-bjaI-linear.gb)       |
| `bjaR-GFP-native`    | 3877            | [pOpen-bjaR-GFP-native.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/quorum-sensing/pOpen-bjaR-GFP-native.gb) |

**Protein Components**

- TetR purified protein — MedChemExpress HY-P71520, resuspended to 30 µM.

**Cell Components**

- XL-10 Gold

**Primers and PCR**

| **Name**        | **Sequence**                                                 | **Tm full (°C)** | **Ta binding (°C)** |
| --------------- | ------------------------------------------------------------ | ---------------- | ------------------- |
| tetO-pT7-tetO F | gacggccagttccctatcagtgatagagagcatgagacggtctcag               | 72               | 64                  |
| pT7-tetO-tetO F | aggagtaatacgactcactatagggtccctatcagtgatagagattgacaggtccctatc | 72               | 70                  |
| M13 Reverse     | caggaaacagctatgaccatg                                        | 63               | 63                  |

| **Name** | **Vector** | **Primer F** | **Primer R** | **Anneal (°C)** | **Extension time (s)** |
| --- | --- | --- | --- | --- | --- |
| tetO-pT7-tetO | pT7-tetO-bjaI | tetO-pT7-tetO F | M13 R | 64 | 25 |
| pT7-tetO-tetO | pT7-tetO-bjaI | pT7-tetO-tetO F | M13 R | 64 | 25 |

**Reaction Construction**

| **Component**       | **Samples (each) (µL)** | **Positive controls (each) (µL)** | **Negative control (µL)** | **Notes**                                 |
| ------------------- | ----------------------- | --------------------------------- | ------------------------- | ----------------------------------------- |
| PURE Solution A     | 4                       | 4                                 | 4                         | PURE energy solution: small molecules     |
| PURE Solution B     | 3                       | 3                                 | 3                         | PURE proteins and ribosomes               |
| RNase Inhibitor     | 0.5                     | 0.5                               | 0.5                       | Prevents RNase activity                   |
| Linear DNA (30 nM)  | 0.2                     | 0.2                               | 0                         | `pT7-tetO-tetO-bjaI` or variant           |
| SAM (5 mM)          | 0.6                     | 0.6                               | 0                         |                                           |
| IV-CoA (5 mM)       | 0.16                    | 0.6                               | 0                         |                                           |
| TetR (30 µM)        | 1.54                    | 0                                 | 0                         | Represses tetO-controlled BjaI expression |
| Nuclease-free water | 0                       | 1.54                              | 2.5                       |                                           |
| **Total**           | **10**                  | **10**                            | **10**                    |                                           |

**Experimental Method**

- [ ] Prepare M9 media containing cells and antibiotics:
    - [ ] Prepare M9 Media containing 1× M9 salts, 0.34 mg/mL 1-thiamine hydrochloride, 0.2% casamino acids, 2 mM MgSO₄, 100 µM CaCl₂ and 0.4% (wt/vol) glucose.
    - [ ] Use a pipette tip to scrape some of the frozen bacteria off of the top and inoculate a 1.5 mL eppendorf containing the M9 media with 100 µg/mL carbenicillin.
    - [ ] Gently mix the tube by inverting 5 times. The solution in the tube will be named **M9-cell solution** in the following part.
- [ ] Incubate samples and controls containing PURE reactions at 37°C for 1.5 hrs.
- [ ] Mix varying amounts of samples or controls (1 or 2 µL) with 100 µL of the M9-cell solution.

# Performance

**Induction of receiver *E. coli***

:::{figure} performance-induction.png
:align: center
:width: 75%

GFP induction kinetics in *E. coli* receiver cells carrying `bjaR-GFP-native` after addition of PURE reaction sample or control.
:::

:::{note}
Excessive addition of PURE reaction to the M9-cell solution negatively impacts GFP induction in *E. coli*, with 1 µL proving more effective than 2 µL. As a result, the figures below focus on the outcomes observed with the addition of 1 µL of samples or controls.
:::

**Repression Validation**

:::::{tab-set}

::::{tab-item} Comparison
:::{figure} performance-repression-comparison.png
:align: center
:width: 75%

Repression of BjaI expression across three tetO construct variants. Positive controls contain no TetR.
:::
::::

::::{tab-item} Endpoint
:::{figure} performance-repression-endpoint.png
:align: center
:width: 75%

Endpoint GFP expression in *E. coli* receiver cells for each construct variant with and without TetR repressor.
:::
::::

:::::

**Observations:**

- Positive controls (samples without any TetR) exhibited similar GFP fluorescence, indicating that all DNA constructs (`pT7-tetO-tetO-bjaI`, `tetO-pT7-tetO-bjaI`, and `pT7-tetO-bjaI`) are effective for BjaI expression.
- Repression efficiency follows the order: `pT7-tetO-tetO-bjaI` > `tetO-pT7-tetO-bjaI` > `pT7-tetO-bjaI`. Based on this, `pT7-tetO-tetO-bjaI` was selected for use in the subsequent liposome experiment to construct the responder cells.

# Process

- [Assemble Base Cytosol](../../processes/assemble-base-cytosol/main.md)

# Modules

- [Detector: TetR-aTc](../../modules/detector-tetr_atc/spec.md)
- [Emitter: IV-HSL](../../modules/emitter-ivhsl/spec.md)

# Credits

- Jefferson Smith & Michael Booth (Oxford / UCL)
- b.next
