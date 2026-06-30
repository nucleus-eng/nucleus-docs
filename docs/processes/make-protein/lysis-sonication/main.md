---
title: Lyse Bacteria by Sonication
---

# Overview

You have bacterial cultures and you want to extract something inside of them (e.g., overexpressed protein, plasmid DNA, tRNAs, total lysate, etc.). You're going to need to lyse this culture. You can use a sonicator to do so, disrupting bacterial walls and membranes using ultrasonic frequencies pumped into the bacterial culture. This protocol shows you how to use a sonicator to mechanically lyse cells.

This protocol is derived from the original PURE system ([Shimizu et al., 2001](https://doi.org/10.1038/90802)) and from the OnePot PURE method ([Lavickova & Maerkl, 2019](https://doi.org/10.1021/acssynbio.8b00427); [Grasemann et al., 2021](https://doi.org/10.3791/62625)). 

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

- [Prepare Protein Purification Buffers and Media](../prep-consumables/main.md)
- [Grow and Induce Expression Strains](../grow-bacteria/main.md)

::::::

:::::::

# Materials and Equipment


<!-- vale nucleus.magnitude-unit-spacing = NO -->
:::{table} Bill of Materials
:label: bom-lysis-sonication

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sonicator | Equipment | Q700 Sonicator | QSonica | Q700A-110 | $5500 | 4 °C to 30 °C | [link](https://www.sonicator.com/products/q700-sonicator?variant=36028875408) |
| Sonicator Probe | Equipment | Standard Probe, Replaceable Tip, 1/2" (12.7mm) diameter | QSonica | 4220 | $670 | 4 °C to 30 °C | [link](https://www.sonicator.com/collections/q700-probe-options/products/standard-probes-for-q700-and-q500?variant=36022579984) |
| Sound Enclosure | Equipment | Sound Enclosure | QSonica | 432B2 | $995 | 4 °C to 30 °C | [link](https://www.sonicator.com/collections/q700-sound-enclosure/products/sound-enclosure-for-q700-and-q500) |
| Lab Jack | Equipment | Fisherbrand™ Lab Jacks (15cmx15cm) | Fisher Scientific | 14-673-51 | $484 | 4 °C to 30 °C | [link](https://www.fishersci.com/shop/products/fisherbrand-lab-jacks-11/1467351) |
| 15 mL centrifuge tubes | Consumables | Corning® 15 mL PP Centrifuge Tubes, Rack Packed with CentriStar™ Cap, Sterile, 50/Rack, 500/Case | Corning | 430790 | $230.44 | 4 °C to 30 °C | [link](https://ecatalog.corning.com/life-sciences/b2b/UK/en/Liquid-Handling/Tubes%2C-Liquid-Handling/Centrifuge-Tubes/Corning%C2%AE-15mL-Centrifuge-Tubes/p/430790) |
| 10 mL Luer Lock Syringes | Consumables | Syringes with BD Luer-Lok® Tip, BD Medical, Syringe with Luer-Lok® Tip, Volume=10 mL | BD Industrial/Difco | 550-80620-PK | $102.40 | 4 °C to 30 °C | [link](https://www.spectrumchemical.com/bd-8482-sterile-luer-lok-8482-tip-general-purpose-syringes-320054) |
| 0.45 µm syringe filters | Consumables | PES Syringe Filter, 0.45μm, 30mm, Sterile | CELLTREAT Scientific Products | 229749 | $84 | 4 °C to 30 °C | [link](https://www.celltreat.com/product/229749/) |
| Potassium Hydroxide | Salts (for Buffers) | Potassium hydroxide - ACS reagent, ≥85%, pellets | Sigma-Aldrich | 221473-1KG | $99.90 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/221473) |
| HEPES | Salts (for Buffers) | HEPES, Crystalline Powder, ≥99.5% (titration), Poly bottle | Sigma-Aldrich | H3375-500G | $431 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/h3375) |
| Ammonium Chloride | Salts (for Buffers) | Ammonium chloride, ACS reagent, ≥99.5% | Sigma-Aldrich | 213330-500G | $73.50 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/213330) |
| Sodium Chloride | Salts (for Buffers) | Sodium Chloride, Redi-Dri™, anhydrous, free-flowing, ACS, ≥99% | Sigma-Aldrich | 746398-1KG | $133.00 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/746398) |
| Magnesium Chloride hexahydrate | Salts (for Buffers) | BioXtra Magnesium chloride, Hexahydrate, Powder or Crystals, ≥99.0% | Sigma-Aldrich | M2670-100G | $50.50 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sial/m2670) |
| Lysozyme | Supplements (for Buffers) | Lysozyme from chicken egg white, protein ≥90%, ≥40 000 units/mg protein, lyophilized powder | Sigma-Aldrich | L6876-1G | $76.90 | -25 °C to -15 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/l6876) |
| TCEP-HCl (0.5M; presuspended) | Supplements (for Buffers) | Thermo Scientific, Bond-Breaker® Tris[2-Carboxyethyl]phosphine Neutral Solution (TCEP), Application=Water-Soluble Reducing Agent, Molecular Weight=286.65, Size=5 mL | Thermo Scientific | 77720 | $175.65 | 4 °C to 30 °C | [link](https://www.thermofisher.com/order/catalog/product/77720) |
| cOmplete Protease Inhibitor | Supplements (for Buffers) | cOmplete™ Protease Inhibitor Cocktail, EDTA-Free, Tablets | Roche | 11873580001 | $472 | 1 °C to 4 °C | [link](https://www.sigmaaldrich.com/US/en/product/roche/coedtafro) |
:::
<!-- vale nucleus.magnitude-unit-spacing = YES -->

# Protocol

- [ ] **Prepare Stock Solutions.**

| Reagent | MW (g/mol) | Amount (g) | Final Volume (mL) | Storage | Needs pH adjustment? | Needs Sterilization? |
| --- | --- | --- | --- | --- | --- | --- |
| Potassium Hydroxide (1M) | 56.11 | 14.0 | 250 | 4 °C to 30 °C | no | no |
| HEPES-KOH (pH=7.6; 1M) | 238.3 | 59.5 | 250 | 4 °C to 30 °C; dark | yes | no |
| Ammonium Chloride (1M) | 53.49 | 13.4 | 250 | 4 °C to 30 °C | no | no |
| Sodium Chloride (5M) | 58.44 | 73.1 | 250 | 4 °C to 30 °C | no | no |
| Magnesium Chloride (1M) | 203.3 | 20.3 | 100 | 4 °C to 30 °C | no | no |
| Lysozyme (30 mg/mL) | 14320 | 1 | 33 | -25 °C to -15 °C | no | no |

- [ ] **Prepare Lysis Buffer** — used to resuspend bacterial pellets for mechanical lysis by sonication. Also chemically lyses cells with lysozyme (*G. gallus*). Contains protease inhibitor (cOmplete) to slow proteolysis. *Make fresh and use the same day!*

| Reagent | Final Concentration (mM) | Stock Concentration (mM) | Volume to Add (mL) |
| --- | --- | --- | --- |
| HEPES-KOH | 50 | 1000 | 5 |
| Ammonium Chloride | 100 | 1000 | 10 |
| Sodium Chloride | 500 | 5000 | 10 |
| Magnesium Chloride | 10 | 1000 | 1 |
| Lysozyme | 0.3 mg/mL | 30 mg/mL | 1 |
| TCEP | 1 | 500 | 0.2 |
| cOmplete Protease Inhibitor | 1 tablet / 50 mL | n/a | 2 tablets |
| water (milliQ) | — | — | 72.8 |
| **Total** | — | — | 100 |

- [ ] **Prepare centrifuge and Lysis Buffer.**
  - [ ] Pre-chill your centrifuge and Lysis Buffer to 4 °C.
  - [ ] Finish Lysis Buffer with TCEP (0.5M) (e.g., add 500 µL TCEP to 1 L Lysis Buffer).
- [ ] **Resuspend pellets in cold Lysis Buffer.**
  - [ ] Thaw bacterial pellets on ice.
  - [ ] Weigh 1 g dry cell mass per pellet.
  - [ ] Resuspend 1 g pellets in 10 mL Lysis Buffer by vortexing.
  - [ ] Keep lysate cold to prevent proteolysis.

  :::{hint} Note: Keep lysate cold to prevent proteolysis.
  :class: dropdown

  Lysis releases proteases from the cytosols and cell walls of your bacteria. These proteases can degrade your sample. To slow their activity, keep your samples cold (4 °C). We also recommend using protease inhibitors (e.g., cOmplete), or protease deficient expression strains to reduce protease activity further.

  To keep your samples cold during resuspension, return them to ice frequently as you resuspend them by vortexing. To check that your sample is fully suspended, vortex the pellet briefly, then hold the tube above your head and look up at the bottom of the tube. You may see either chunks or flecks of the pellet slowly float down to the bottom of the tube, or pellet gunk stuck to the bottom of the tube.
  :::

- [ ] **Lyse cells by sonication.**
  - [ ] Program your sonicator. We recommend 50% amplitude, 10 s on / 10 s off.
  - [ ] Always use a Sound Enclosure during sonication.

  :::{hint} Note: Always use a Sound Enclosure during sonication.
  :class: dropdown

  Sonicators produce an intense, high pitched noise during operation. This sound can be hazardous if standing next to the sonicator during operation, and at the very least unpleasant. Use sonicators in an appropriate sound enclosure, or make sure to use ear protection during use.
  :::

  - [ ] Place resuspended samples under the sonicator horn in an ice bucket on a lab jack.
  - [ ] Adjust your sample height using the sample jack until each sonicator tip is submerged by about one quarter (1/4) of the sample height (e.g., 2.5 mL into a 10 mL sample).
  - [ ] Lyse cells by sonication. Deliver 4.5 kJ for every 10 mL sample (e.g., a four-pronged sonicator horn lysing 4x 10 mL samples → 18 kJ).
  - [ ] Avoid foaming during sonication.

  :::{hint} Note: Avoid foaming during sonication.
  :class: dropdown

  Over-sonicating your lysates can damage your target proteins. Over-sonication forms foam at the top of your sample, presumably from lipids and proteins coagulating and trapping air. Avoid foaming!
  :::

- [ ] **Clarify lysates by centrifugation and filtration.**
  - [ ] Centrifuge lysates at 4 krcf / 4 °C / 45 min.
  - [ ] (Meanwhile) for each lysate, assemble a 10 mL Luer lock syringe and 0.22 µm syringe filter.
  - [ ] Carefully decant each supernatant into a syringe and filter into a fresh 15 mL centrifuge tube. Keep clarified lysate cold (4 °C).
  - [ ] Keep going! Don't take a break!

  :::{hint} Note: Keep going! Don't take a break!
  :class: dropdown

  Your target protein is not stable in clarified lysate, even if clarification reduces proteolytic activity. You should immediately proceed to purification. Your samples will only continue to degrade until they've been purified and stored at -80 °C. Work smoothly and quickly from here on out!
  :::

# Downloads

::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/lysis-sonication-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/lysis-sonication-bom.pdf>`
:::

::::

# Acknowledgments

Yan Zhang, Zoila Jurado, and Miki Yun (Richard Murray Lab, Caltech)
