---
title: "Dye Liposomes"
subtitle: "Module Specification"
status: validated-published
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Dye Liposomes encapsulate HPTS dye in  [Membrane: POPC/Chol (7:3)](/docs/modules/membrane-popc-chol/spec.md) and use a simple, glucose outer solution. Dye Liposomes are a fast debugging tool and positive control for liposome encapsulation and microscopy. This protocol is adapted from the [Build a Cell liposome kit](https://github.com/BuildACell/liposome-kit) ([Fujii et al., 2014](https://doi.org/10.1038/nprot.2014.107)).

# Reference Composition

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    OUTER_SOLUTION["Outer solution"]
    HPTS["HPTS dye solution"]
    MEMBRANE_POPC_CHOL["Membrane: POPC/Chol (7:3)"]

    P1_ENCAPSULATE_0(["Encapsulation: Phase Transfer (packing)"])
    DYE_LIPOSOMES["Dye Liposomes"]

    HPTS --> P1_ENCAPSULATE_0
    MEMBRANE_POPC_CHOL --> P1_ENCAPSULATE_0
    OUTER_SOLUTION --> P1_ENCAPSULATE_0
    P1_ENCAPSULATE_0 --> DYE_LIPOSOMES


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class OUTER_SOLUTION,HPTS,MEMBRANE_POPC_CHOL leaf;
    class DYE_LIPOSOMES composed;
    class P1_ENCAPSULATE_0 process;

    click OUTER_SOLUTION "/docs/modules/outer-solution/spec"
    click MEMBRANE_POPC_CHOL "/docs/modules/membrane-popc-chol/spec"
    click P1_ENCAPSULATE_0 "/docs/processes/assemble-base-cell/main"
    click DYE_LIPOSOMES "/docs/modules/dye-liposomes/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} Inner Solution

:::{table}
:label: comp-inner-solution

| Component         | Stock concentration | Final concentration | Volume for one reaction (µL) |
| ----------------- | ------------------- | ------------------- | ---------------------------- |
| HPTS              | 4 mM                | 0.2 mM              | 5                            |
| Optiprep          | 1.32 mg/µL          | 0.043 mg/µL         | 0.98                         |
| Water             |                     |                     | 24.02                        |
| Total volume (µL) |                     |                     | 30                           |
:::

:::{admonition} Two corrections to this table
:class: warning

**The Optiprep volume was 1.33 µL and is now 0.98 µL.** The row `1.32 mg/µL / 0.043 mg/µL
/ 1.33 µL` appears identically on four pages. On [Base Cell](../base-cell/spec.md) and
[Reporter: deGFP](../reporter-degfp/spec.md) the reaction is **40 µL**, where 1.33 µL of a
1.32 mg/µL stock gives 0.0439 mg/µL and the row closes. This reaction is **30 µL**, where
the same volume gives 0.0585 mg/µL. The row was copied without rescaling the volume.
0.98 µL is what 0.043 mg/µL requires at 30 µL, and water absorbs the difference.

**The HPTS row still does not close and is left as written.** 5 µL of a 4 mM stock in
30 µL gives 0.667 mM, not the 0.2 mM stated. 0.2 mM would need 1.5 µL, or a 1.2 mM stock.
No other page carries this row, so there is nothing to compare it against.

@Editor: confirm the HPTS stock and volume against the working-solution prep. One of the
three numbers is wrong and the page cannot say which.
:::

::::

::::{tab-item} Membrane

:::{table}
:label: comp-dye-liposomes-membrane

| Component    | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC         | 70                    | 760.076                  | 25                          | 162.17             |
| Cholesterol  | 29.95                 | 386.7                  | 50                          | 17.65              |
| Liss-Rhod PE | 0.05                  | 1301.71                  | 1                           | 4.96               |

:::

See [Membrane: POPC/Chol (7:3)](../membrane-popc-chol/spec.md) for the full membrane spec.
::::

::::{tab-item} Outer Solution

:::{table}
:label: comp-outer-solution

| Component | Concentration |
| --------- | ------------- |
| Glucose   | 800 mM        |
:::

::::

:::::

# Expected Behavior

Liposomes are visible in the green channel (interior, HPTS, 480 nm ex / 520 nm em) and in the red channel (membrane, Liss-Rhodamine-PE, 540 nm ex / 580 nm em) under fluorescence microscopy.

# Processes

Dye Liposomes are assembled and encapsulated using [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md).

# Materials

:::{table}
:label: bom-dye-liposomes
:align: center

| Name                     | Category   | Product                                    | Manufacturer          | Part #      | Price   | Storage | Link                                                                                                    |
| ------------------------ | ---------- | ------------------------------------------- | ---------------------- | ----------- | ------- | ------- | --------------------------------------------------------------------------------------------------------- |
| HPTS                     | Reagent    | HPTS (Pyranine)                             | Thermo Scientific      | L11252-06   | $92.60  | RT      | [link](https://www.thermofisher.com/order/catalog/product/L11252-06)                                       |
| HEPES pH 7.6             | Chemical   | HEPES, Free Acid                            | Fisher BioReagents     | NC1584172   | $85.90  | RT      | [link](https://www.fishersci.com/shop/products/hepes-free-acid-fisher-bioreagents-3/NC1584172)             |
| Optiprep                 | Reagent    | OptiPrep™                                   | STEMCELL Technologies  | 07820       | $289.00 | RT      | [link](https://www.stemcell.com/products/optipreptm.html)                                                  |
| POPC                     | Lipid      | 16:0-18:1 PC 25 mg/mL                       | Avanti Lipids          | A80557      | $435.00 | -20 °C   | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc)                       |
| Liss-Rhod PE             | Lipid      | 18:0 Liss Rhod PE 1 mg/mL                   | Avanti Lipids          | A81179      | $273.47 | -20 °C   | [link](https://www.avantiresearch.com/en-gb/products/product/810179-180-liss-rhod-pe)                      |
| Glucose                  | Chemical   | D-(+)-Glucose, 99%                          | Thermo Scientific      | A16828-36   | $41.65  | RT      | [link](https://www.thermofisher.com/order/catalog/product/A16828.36)                                       |
| Mineral oil              | Chemical   | Mineral oil, mixed weight                   | Thermo Scientific      | AC415080010 | $53.40  | RT      | [link](https://www.thermofisher.com/order/catalog/product/AC415080010)                                     |
| Glass syringe 250 µL     | Equipment  | Hamilton glass syringe                      | Hamilton               | 14-815-238  | $150.15 | RT      | [link](https://www.fishersci.com/shop/products/800-microliter-syringes-rn-termination/14815238)            |
| 18-well imaging slide    | Consumable | µ-Slide 18 Well glass bottom                | ibidi                  | 80826       | $178.00 | RT      | [link](https://ibidi.com/chambered-coverslips/237--slide-18-well-glass-bottom.html)                        |

:::

:::{hint} Note
:class: simple
:icon: false
Sucrose is used in the original [Build a Cell liposome kit](https://github.com/BuildACell/liposome-kit) protocol for the inner solution, but is replaced by Optiprep here to match the Base Cell inner-solution formulation. It is not included in the BOM above.
:::

# Constituent Modules

- [Membrane: POPC/Chol (7:3)](../membrane-popc-chol/spec.md) — 70:30 POPC:cholesterol bilayer encapsulating the HPTS dye solution

# Credits

Adapted from the [Build a Cell liposome kit](https://github.com/BuildACell/liposome-kit) ([Fujii et al., 2014](https://doi.org/10.1038/nprot.2014.107)).
