---
title: "Substrate SUV: CPRG"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

A Substrate SUV is a small unilamellar liposome that carries a chemical substrate of interest and nothing else. The CPRG Substrate SUV is a subcomponent of a [LacZ colorimetric cascade](../../processes/colorimetric-readout/main.md).

This Substrate SUV carries chlorophenol red-β-D-galactopyranoside (CPRG). CPRG is yellow; β-galactosidase (LacZ) cleaves it to chlorophenol red, which is purple. Holding the substrate inside a liposome allows for substrate release using [PLA1](../effector-pla1/spec.md): as long as the SUV is intact, CPRG and LacZ never meet. When a neighboring Sensing Cell expresses PLA1 and lyses, it breaches these SUVs too, releasing CPRG into the surrounding LacZ solution and starting the color change.

This module is not a reporter in and of itself, requiring [LacZ Reporter Module](../reporter-lacz/spec.md) to produce an output.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::
# Reference Composition

:::::{tab-set}

::::{tab-item} Membrane

:::{table} Substrate SUV bilayer, as prepared for the Chicago colorimetric work.
:label: comp-substrate-cprg-bilayer

| Component   | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ----------- | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC        | 90                    | 760.076                  | 25                          | 208.51             |
| Cholesterol | 10                    | 386.654                  | 50                          | 6.00               |

:::

See [Chicago Membrane](../membrane-popc-chol-chicago/spec.md).

::::

::::{tab-item} Inner Solution

The luminal cargo is CPRG in hydration buffer. Two working concentrations are documented, for two different downstream uses.

:::{table} Inner solution.
:label: comp-substrate-cprg-lumen

| Use | CPRG concentration |
| --- | --- |
| SUV hydration (loading) | 50 mM (approx. 30 mg/mL) |
| Inner gel, patterned agarose | 15 mg/mL |

:::

::::

:::::

# Expected Behavior

Intact Substrate SUVs produce no signal. On PLA1-triggered lysis of a neighboring Sensing Cell, released CPRG reacts with LacZ in the surrounding matrix to give a yellow-to-purple change, measurable at 575 nm and visible by eye.

Quality control before combining with other components:

- **Size.** Confirm a mean diameter near 400 nm by dynamic light scattering. A single narrow peak indicates a homogeneous, well-extruded population.
- **Free substrate removed.** Measure absorbance at 575 nm of the purification flow-through, not the liposome fraction. A flat, low-absorbance flow-through indicates unencapsulated CPRG has been removed; residual absorbance means repeat the purification.

:::{attention} No primary data located
@Editor: the 400 nm target size and the 50 mM loading concentration have no DevNote behind them. No DLS traces or absorbance QC data has been located, so these values are not independently verified. Listed as a wanted module DevNote.
:::

## Gels

In ~1% alginate the yellow-to-purple change appears after about 16 h.

# Requirements

Requires an external β-galactosidase source in the surrounding matrix (e.g. [LacZ Reporter](../reporter-lacz/spec.md)), and a lysis trigger to breach the SUV membrane (e.g. [PLA1 Lysis Module](../effector-pla1/spec.md)).

Requires encapsulation within a lipid membrane (e.g. POPC, or POPC:cholesterol) until a lysis trigger is applied; released CPRG must not contact LacZ before that trigger.

:::{warning} Do not expose CPRG Substrate SUVs to UV light!
CPRG photobleaches under UV illumination, e.g., during PEG-norbornene crosslinking: side-by-side comparisons show UV exposure during PEG-norbornene crosslinking visibly bleaches the color while an unexposed control retains it.

The confirmed workaround for PEG-norbornene is to invert the order — pre-add LacZ to the gel, crosslink, then add CPRG as a free dye afterwards. That path does not use this module. Agarose, alginate, and ULGA embedding involve no UV step and are compatible with pre-loading as described here.
:::

# Implementations

- [Chicago DevCell](../../implementations/chicago-devcell/main.md): supplies the substrate for the theophylline and pH colorimetric readouts.
- [London DevCell](../../implementations/london-devcell/main.md): supplies the substrate for the AHL colorimetric readout.

# Processes

- [SUV Encapsulation](../../processes/encapsulate-suv/main.md) — lipid film, CPRG hydration, extrusion, purification.
- [Alginate Hydrogel Embedding](../../processes/embed-alginate-hydrogel/main.md) — co-embedding with Sensing Cells and LacZ.
- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) — the readout step itself.

:::{table} Standard preparation parameters.
:label: proc-substrate-cprg-parameters

| Parameter | Value | Notes |
| --- | --- | --- |
| Target diameter | 400 nm | Extruded through a 400 nm polycarbonate membrane |
| Extrusion passes | ≥21, odd number | Odd count avoids retaining unextruded material in the final syringe |
| Free-substrate removal | see the flag below | Two methods are recorded |
| Storage before use | on ice or at 4 °C | Hold until combining with Sensing Cells and LacZ |

:::

:::{attention} Two purification methods are recorded
@Editor: one record has the SUVs purified twice by size-exclusion chromatography to remove unencapsulated CPRG; another has them washed by centrifugation. Confirm with the Chicago Node which was used.

The two methods leave different residual-substrate profiles, and residual free CPRG is what produces background color.
:::

# Credits

Developed by the Chicago Node (Kamat Lab and Liu Lab).
