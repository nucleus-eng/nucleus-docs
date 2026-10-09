---
title: "Encapsulation: Freeze-Thaw"
subtitle: "Process"
status: draft
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

Encapsulation: Freeze-Thaw makes large unilamellar vesicles (LUVs) that carry an aqueous payload. An inner solution hydrates a dried lipid film. Sonication and five freeze-thaw cycles break up the film. Ten centrifugation washes in outer solution then remove the payload that stays outside the liposomes. The payload in use is chlorophenol red-β-D-galactopyranoside (CPRG), the substrate half of the [LacZ Reporter](../../modules/reporter-lacz/spec.md): the liposome keeps CPRG away from LacZ until a lysis event releases it.

This is an instance of [Encapsulation](../encapsulate/main.md). It uses no extrusion and no oil phase.

:::{attention} Size and lamellarity are not measured
@Editor: no diameter, size distribution or lamellarity has been measured for this route. The name LUV is not yet confirmed by a measurement. Record at least a diameter distribution before this page is published.
:::

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

- [Assemble Outer Solution](../assemble-outer-solution/main.md) — the wash solution. Which formulation is the implementation's choice.
- [Substrate: CPRG](../../modules/substrate-cprg/spec.md) — the payload.

::::::

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

**Chloroform** — irritant, possible carcinogen. Lipid stocks are supplied in chloroform. Work in a fume hood and wear gloves.

**Liquid nitrogen** — causes cold burns, and displaces oxygen in a closed space. Wear cryogenic gloves and eye protection, and work in a ventilated area.

::::::

::::::{note} Composition
:class: dropdown
:icon: false

:::{table} Inner solution, 500 µL.
:label: comp-encapsulate-luv-inner

| Component | Stock | Final concentration | Volume (µL) |
| --- | --- | --- | --- |
| CPRG | 30 mg/mL | 14.25 mg/mL | 237.5 |
| OptiPrep | 100% (v/v) | 10% (v/v) | 50 |
| Tris-HEPES buffer (1 M Tris, 1.15 M HEPES) | ≈2520 mOsm | 1071 mOsm, this buffer's share by dilution | 212.5 |
| Total | | | 500 |

:::

@Editor: 1 M Tris with 1.15 M HEPES adds to about 2150 mOsm/L as written. The page gives 2520. The 1071 is 0.425 of 2520, so it moves with it. Which is right?

Every wash is into the outer solution the implementation uses. Its formulations are on [Assemble Outer Solution](../assemble-outer-solution/main.md).

:::{table} Membrane, 2 µmol of lipid in 0.5 mL (4 mM). Volumes are of the lipid stocks.
:label: comp-encapsulate-luv-membrane

| Component | Stock | Final (mol%) | Volume (µL) | Amount (µmol) |
| --- | --- | --- | --- | --- |
| POPC | 25 mg/mL | 89.9 | 54.66 | 1.798 |
| Cholesterol | 50 mg/mL | 10 | 1.547 | 0.2 |
| Liss Rhod PE | 1 mg/mL | 0.1 | 2.603 | 0.002 |
| Total | | 100 | | 2 |

:::

:::{attention} The lipid film is only partly specified
@Editor: record the vessel the film is made in and how it is dried.
:::

::::::

:::::::

# Materials and Equipment

:::{table}
:label: bom-encapsulate-luv
:align: center

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| POPC | Lipid | 16:0-18:1 PC 25 mg/mL | Avanti Lipids | A80557 | $435.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc) |
| Cholesterol | Lipid | Cholesterol | Avanti Research | A80100 | $261.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/700100-cholesterol-plant) |
| Liss Rhod PE | Lipid | Liss Rhod PE | Avanti Lipids | A81179 | $273.47 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/810179-180-liss-rhod-pe) |
| Chloroform | Chemical | Chloroform, suitable for HPLC, ≥99.8%, contains 0.5-1.0% ethanol as stabilizer | Sigma-Aldrich | 366927 | $94.30 | RT (flammables cabinet) | [link](https://www.sigmaaldrich.com/US/en/product/sigald/366927) |
| CPRG | Reagent | Chlorophenol red-β-D-galactopyranoside | Roche | 10884308001 | $160.00 | -20 °C | [link](https://www.sigmaaldrich.com/US/en/product/roche/10884308001) |
| OptiPrep | Reagent | OptiPrep | STEMCELL Technologies | 07820 | $289.00 | RT | [link](https://www.stemcell.com/products/optipreptm.html) |
| Tris base | Chemical | Tris base | — | — | — | RT | — |
| HEPES | Chemical | HEPES | — | — | — | RT | — |
| Liquid nitrogen | Consumable | Liquid nitrogen | — | — | — | Dewar | — |
| Sonicator | Equipment | — | — | — | — | RT | — |
| Water bath | Equipment | Set to 35 °C | — | — | — | RT | — |
| Microcentrifuge | Equipment | Reaches 10,000 × g | — | — | — | RT | — |
| Vortex mixer | Equipment | — | — | — | — | RT | — |

:::

# Protocol

## Prepare the Lipid Film

:::{attention} Film preparation is only partly recorded
@Editor: record the vessel and how the film is dried.
:::

- [ ] Combine the three lipid stocks in the volumes in the membrane table, and dry them to a thin film.

:::{warning} Warning
:class: simple
:icon: false
Work inside a fume hood when handling chloroform.
:::

## Hydrate

- [ ] Add the inner solution directly to the dried lipid film.
- [ ] Vortex until the film is no longer visible on the bottom of the vessel.
- [ ] Sonicate for 10 min.

:::{attention} Sonication is not specified
@Editor: record the sonicator type (bath or probe), the power and the temperature.
:::

## Freeze and Thaw

- [ ] **Do five freeze-thaw cycles.** For each cycle:
    - [ ] Freeze the suspension in liquid nitrogen.
    - [ ] Thaw it in a 35 °C water bath.
    - [ ] Vortex for 30 s.

## Pellet

- [ ] Add 200 µL outer solution to each 50 µL portion of liposomes. One batch is 12 portions.

:::{attention} The batch does not add up
@Editor: one hydration makes 500 µL, but 12 portions of 50 µL need 600 µL. Record whether a batch is more than one hydration, and where the suspension is split into portions.
:::

- [ ] Centrifuge at 10,000 × g for (10–20) min.
- [ ] **Pool the pellets into two tubes.** For each pooled tube:
    - [ ] Collect 15 µL of pellet from each of six tubes, 90 µL in total.
    - [ ] Add 160 µL outer solution, for 250 µL in total.

:::{admonition} The wash spin and the pellet spin are different speeds
:class: warning

The wash spins at **4,000 × g**. The single pellet spin above runs at **10,000 × g**,
which is also what the equipment list gives as the microcentrifuge's maximum.

[Substrate: CPRG LUV](../../modules/substrate-cprg-luv/spec.md) carried 10,000 × g for
the wash, which is the pellet figure in the wrong row. That page now points here
instead of repeating a speed.

@Editor: confirm 4,000 × g is the wash speed actually run. If it is not, this page is
the one to correct, because it is the one a bench user follows.
:::

## Wash

- [ ] **Wash each pooled tube 10 times.** For each wash:
    - [ ] Centrifuge at 4,000 × g for 10 min.
    - [ ] Remove 200 µL of supernatant. Do not disturb the pellet.
    - [ ] Add 200 µL fresh outer solution.
    - [ ] Turn the tube 180° in the rotor before the next spin.

:::{hint} Turn the tube at every wash
:class: simple
:icon: false
Turning the tube makes the pellet form on the opposite wall at each spin. Moving the pellet releases unencapsulated solution that is trapped between the liposomes.
:::

## Resuspend

- [ ] After the last wash, keep the tubes on ice for at least 30 min.
- [ ] Tap each tube gently to resuspend the pellet. Do not pipette.

One batch gives two tubes of 250 µL each.

# Quality Control

:::{attention} No quality control is recorded
@Editor: no measurement of size, lamellarity or free CPRG after the last wash is recorded for this route. Add at least a diameter distribution, and a check that the final supernatant holds no free CPRG.
:::

# Credits

Developed by Manuel and Sung-Won.

# Downloads

::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/encapsulate-luv-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/encapsulate-luv-bom.pdf>`
:::

::::
