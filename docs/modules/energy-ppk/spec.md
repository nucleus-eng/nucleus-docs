---
title: "Energy: PPK"
subtitle: "Module Specification"
thumbnail: reaction-schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The PPK energy Module generates ATP and  GTP from AMP and GDP, respectively, using inorganic polyphosphate (100mer) as a phosphate donor. This module complements the default energy module in Nucleus Cytosol.

:::{attention}

This Module has not been validated in Nucleus Cytosol $\ge$ v0.5. Documentation can be found here and in the following DevNotes:

- [Integrating PPK Module in PURE Cells](https://doi.org/10.63765/mwur3749)
- [PPK Module testing in PURE](https://doi.org/10.63765/djnv7772)

:::

:::{figure} header.png
:align: center
:width: 60%
:::

The PPK Energy module consists of a purified protein, the bifunctional polyphosphate kinase (PPK2), and its substrate, the 100mer polyphosphate (PolyP). Here, bifunctionality refers to the module's ability to direct the synthesis of ATP and GTP from AMP and GDP, respectively

When used alongside PURE's standard energy regeneration module based on creatine kinase and creatine phosphate (CP/CK), significant increases in protein expression yields can result.

:::{figure} reaction-schematic.png
:align: center
:width: 50%
:::

## Usage

The PPK energy module is implemented by preparing a custom energy mix and adding in purified PPK2 protein. This module is highly sensitive to amount of Mg²⁺ contained in Cytosol since PolyP acts as a magnesium chelator

**DNA Parts**

:::{attention}
Design files for the constructs below are available [Nucleus DNA repository](https://github.com/nucleus-eng/DNA).
:::

| Construct   | Size    | Description                                                | **File**                                                                                    |
| ----------- | ------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `pOpen-PPK` | 2915 bp | Contains PPK2 in pOpen backbone. Does NOT have a promoter. | [pOpen-PPK-CHis.gb](https://github.com/nucleus-eng/DNA/blob/main/energy/pOpen-PPK-CHis.dna) |

**Protein components**

- PPK2

**Cell components**

This module is implemented using purified PPK2 protein; no additional cell components are required.

### Reaction Construction

**Custom SMix.** The construction SMix without creatine phosphate (SMixΔCP) is as follow. Note that normal SMix contains all of the following plus 20 mM CP.

| Component             | Stock concentration (mM) | Concentration of components in reaction (mM) | Concentration in Energy solution  (mM) | Final volume to add (µL) |
| --------------------- | ------------------------ | -------------------------------------------- | -------------------------------------- | ------------------------ |
| HEPES                 | 1000                     | 50                                           | 150                                    | 30.0                     |
| Potassium glutamate   | 2500                     | 100                                          | 300                                    | 24.0                     |
| Magnesium acetate     | 1000                     | 11.8                                         | 35.4                                   | 7.1                      |
| NTP                   | 100                      | 2                                            | 6                                      | 12.0                     |
| tRNA                  | 35 (mg/mL)               | 3.5 (mg/mL)                                  | 10.5 (mg/mL)                           | 60.0                     |
| Creatine phosphate    | 1000                     | 0                                            | 0                                      | 0.0                      |
| TCEP                  | 500                      | 1                                            | 3                                      | 1.2                      |
| Folinic acid          | 5                        | 0.02                                         | 0.06                                   | 2.4                      |
| Spermidine            | 200                      | 2                                            | 6                                      | 6.0                      |
| Amino acid solution   | 3.25                     | 0.3                                          | 0.9                                    | 55.4                     |
| Water                 |                          |                                              |                                        | 1.9                      |
|                       |                          |                                              |                                        |                          |
| Energy solution total |                          | Final concentration (fold)                   |                                        | Final volume             |
|                       |                          | 3                                            |                                        | 200                      |

The following reaction table is a self-contained experiment for evaluating the performance of the PPK energy module. Details about the stock solutions and detailed reaction descriptions are available in the toggle list below.

:::{hint} Note: Concentration of Stock Solutions
:class: dropdown

| Component                                                                                   | Input concentration | Unit  |
| ------------------------------------------------------------------------------------------- | ------------------- | ----- |
| Sol A                                                                                       | 2.50                | fold  |
| Energy solution-CP                                                                          | 3.00                | fold  |
| Sol B                                                                                       | 3.33                | fold  |
| [plamGFP DNA](https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-plamGFP-PURE.gb) | 120                 | ng/µL |
| Mg-Acetate                                                                                  | 200                 | mM    |
| Creatine phosphate                                                                          | 1000                | mM    |
| PEG4K 40%                                                                                   | 40                  | %     |
| PolyP                                                                                       | 500                 | mM    |
| PPK2                                                                                        | 57.5                | uM    |

:::

:::{hint} Note: Description of Reactions
:class: dropdown

| Name in Reaction Table     | Description                                                      |
| -------------------------- | ---------------------------------------------------------------- |
| **CP/CK**                  | PURE with CP and 8 mM Mg²⁺                                       |
| **PPK/PolyP**              | PURE with PolyP, PPK and 18 mM Mg²⁺                              |
| **CP/CK + PPK/PolyP**      | PURE with CP, PolyP, PPK and 18 mM Mg²⁺                          |
| **+ DNA Positive Control** | PURExpress Positive control (PC) reaction                        |
| **- DNA Negative Control** | PURExpress Negative control (NC) reaction (without DNA template) |

:::

| **Component**                                                                               | **CP/CK (µL)** | **PPK/PolyP (µL)** | **CP/CK + PPK/PolyP (µL)** | **+ DNA Positive Control (µL)** | **-DNA Negative Control (µL)** |
| ------------------------------------------------------------------------------------------- | -------------- | ------------------ | -------------------------- | ------------------------------- | ------------------------------ |
| Sol A                                                                                       |                |                    |                            | 14.00                           | 14.00                          |
| Energy solution-CP                                                                          | 11.67          | 11.67              | 11.67                      |                                 |                                |
| Sol B                                                                                       | 10.51          | 10.51              | 10.51                      | 10.51                           | 10.51                          |
| [plamGFP DNA](https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-plamGFP-PURE.gb) | 1.67           | 1.67               | 1.67                       | 1.67                            | 0.00                           |
| Mg-Acetate                                                                                  | 1.40           | 3.15               | 3.15                       | 0.00                            | 0.00                           |
| Creatine phosphate                                                                          | 0.70           | 0.00               | 0.70                       | 0.00                            | 0.00                           |
| PEG4K 40%                                                                                   | 1.75           | 1.75               | 1.75                       | 0.00                            | 0.00                           |
| PolyP                                                                                       | 0.00           | 2.10               | 2.10                       | 0.00                            | 0.00                           |
| PPK2                                                                                        | 0.00           | 1.22               | 1.22                       | 0.00                            | 0.00                           |
| Water                                                                                       | 7.30           | 2.93               | 2.23                       | 8.82                            | 10.49                          |

## Performance Data

:::::{tab-set}

::::{tab-item} Kinetics
:::{figure} kinetics.png
Translation kinetics of PURE reactions using different energy modules. The PPK2 module performed approximately 77% lower than the CP/CK module. However, the combination of PPK2 and CP/CK modules resulted in approximately 96% higher final protein yield than the CP/CK module alone.
:::
::::

::::{tab-item} Endpoint
:::{figure} endpoint.png
Final protein yields of the reactions measured at steady state. The PPK2 module performed approximately 77% lower than the CP/CK module. However, the combination of PPK2 and CP/CK modules resulted in approximately 96% higher final protein yield than the CP/CK module alone.
:::
::::

::::{tab-item} Mg Sensitivity
:::{figure} mg-sensitivity.png
The PPK energy module is highly sensitive to [Mg²⁺]. Final protein yields of PPK2-powered PURE reactions at different Mg²⁺ concentrations. PPK2 enzyme and polyP were added at a final concentration of 2 µM and 30 mM, respectively.
:::
::::

:::::

## Credits

- Surendra Yadav
