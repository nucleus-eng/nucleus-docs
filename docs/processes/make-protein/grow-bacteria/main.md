---
title: Grow and Induce Expression Strains
---

# Overview

You want to purify proteins. First, you're going to have to make some. We make proteins using bacterial strains that carry our protein of interest on an expression plasmid (here: pET28a). These expression plasmids put a gene of interest under the transcription of an inducible promoter (e.g., pT7). This allows us to first (1) grow our bacteria quickly to a high density, without the metabolic load of making a lot of proteins, then to (2) induce the overexpression of our protein of interest. Making so much protein is toxic to the cells, so we only want to induce expression once our culture is grown out (OD600 ~0.5).

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

- [Prepare Protein Purification Buffers and Media](../prep-consumables/main.md)

::::::

:::::::

# Materials and Equipment

| **Name** | **Category** | **Product** | **Manufacturer** | **Part #** | **Price** | **Storage** | **Link** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LB | Media | Luria Broth (Miller's LB Broth), Non-Sterile, pH 6.8-7.2, Molecular Biology Grade, Powder | Sigma-Aldrich | L3522-1KG | $221 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/l3522) |
| IPTG | Media | Isopropyl β-D-thiogalactoside (IPTG), Powder, ≥99% (TLC), ≤0.1% Dioxane | Sigma-Aldrich | I6758-1G | $89.90 | -25°C to -15°C | [link](https://www.sigmaaldrich.com/US/en/product/sial/i6758) |
| Kanamycin | Media | Kanamycin sulfate, BioReagent, ≥750 ug/mg, Suitable for cell culture, Powder | Sigma-Aldrich | K1377-1G | $47.70 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/k1377) |
| Culture tubes | Consumables | Culture Tube, PS, 14mL, 18x95mm, Sterile, TC Treated, w/ Snap (Vent) Cap | Greiner Bio-One | 191160 | $258.15 | 4°C to 30°C | — |
| 50 mL conical tubes | Consumables | Corning® 50 mL Polypropylene Centrifuge Tubes, Sterile, Racked, CentriStar™ Cap | Corning | 430828 | $436.88 | 4°C to 30°C | [link](https://ecatalog.corning.com/life-sciences/b2b/US/en/Liquid-Handling/Tubes%2C-Liquid-Handling/Centrifuge-Tubes/Corning%C2%AE-50-mL-Centrifuge-Tubes/p/430828) |
| 250 mL baffled flasks | Flasks | PYREX® 250 mL Delong Shaker Erlenmeyer Flask with Baffles | Pyrex | 4444-250 | $188.26 | 4°C to 30°C | [link](https://ecatalog.corning.com/life-sciences/b2c/US/en/Bioprocess-and-Scale-up/Erlenmeyer-Flasks/Erlenmeyer-Flasks,-Glass/PYREX%C2%AE-Flask-with-Baffles/p/4444-250) |
| Flask closures | Flasks | Chemglass Life Sciences Closure, 38mm, Stainless Steel | Chemglass Life Sciences | CG-1320-01 | $100.75 | 4°C to 30°C | [link](https://www.fishersci.com/shop/products/sst-closure-38mm-lanced-1/501215156) |
| Shaking incubator | Equipment | New Brunswick Innova 4430 Incubator Shaker | New Brunswick | — | discontinued | — | discontinued |
| Microvolume spectrophotometer | Equipment | DeNovix DS-11+ Spectrophotometer | DeNovix | DS-11+ | unlisted | 4°C to 30°C | [link](https://www.denovix.com/products/ds-11-fx-spectrophotometer-fluorometer/) |
| Bench centrifuge | Equipment | Sorvall X4R Pro-MD, IVD Certified | Sorvall | 75009521 | $18,270.00 | 4°C to 30°C | [link](https://www.thermofisher.com/order/catalog/product/75009521) |
| -20°C Freezer | Equipment | TSX Series High-Performance -20°C Manual Defrost Freezers | Thermo Scientific | TSX2320FA | unlisted | 4°C to 30°C | [link](https://www.thermofisher.com/order/catalog/product/TSX2320FA) |
| -80°C Freezer | Equipment | TSX Series Ultra-Low Freezers | Thermo Scientific | TSX60086A | unlisted | 4°C to 30°C | [link](https://www.thermofisher.com/order/catalog/product/TSX60086A) |

# Protocol

- [ ] **Prep overnight cultures.**
    - [ ] Add 5 mL LB + Kanamycin (50 µg/mL) to 15 mL culture tubes and label.
    - [ ] Inoculate your tubes with your expression strain working stock using a pipette tip.
    - [ ] Incubate cultures overnight at 37°C / 225 rpm for between 12 hrs and 16 hrs.

:::{hint} Note: you can use glycerol stocks OR fresh colonies as working stocks.
:class: dropdown
We first need to prepare bacterial cultures to induce. We will work from 5 mL overnight cultures of our expression strains and backdilute them the next day. In order to prepare these overnight cultures, we need stocks of bacteria.

We work from 100 µL aliquots of our glycerol stocks, frozen in PCR strip tubes. When seeding our overnights with bacteria, we poked each glycerol stock with a pipette tip and ejected the tip into culture tubes.

Optionally, you can work from individual colonies by streaking out your bacterial stocks onto selective plates (here: Kanamycin at 50 µg/mL). Working from colonies assures that your bulk outgrowth will have come from a single colony forming unit, which may improve plasmid stability over the course of protein expression.
:::

- [ ] **Perform bulk outgrowth.**
    - [ ] Back dilute overnight cultures 1:1000 into fresh media (e.g., add 100 µL of overnight and 100 mL LB with Kanamycin to 250 mL Erlenmeyer flasks).
    - [ ] Incubate back diluted cultures at 37°C / 225 rpm to mid-log phase (OD600 between 0.4 and 0.6, ~3.5 hrs).

:::{hint} Note: leave ≥ 2.5x culture volume in headroom!
:class: dropdown
Bacteria need breathing room! Oxygenation matters, plus shaking can spill overfilled flasks. Make sure to leave at least 2.5 culture volumes worth of headroom. For example:

- 100 mL culture in a 250 mL flask
- 500 mL culture in a 2 L flask
:::

- [ ] **Induce protein expression.**
    - [ ] At mid-log phase, induce your cultures with IPTG to 500 µM (e.g., add 100 µL of IPTG (0.5M) to a 100 mL culture).
    - [ ] Incubate induced cultures at 37°C / 225 rpm / 4 hr to allow cells to express proteins.

- [ ] **Centrifuge cells and freeze pellets.**
    - [ ] While incubating your induced cultures, pre-chill your centrifuge and rotor to 4°C.
    - [ ] Harvest your cultures by centrifuging at 3200 rcf / 4°C / 30 min.
    - [ ] Decant supernatant and reserve pellets.
    - [ ] Weigh pellets to calculate your biomass yield (gDCM / L).
    - [ ] Store pellets at -80°C and allow to freeze (at least overnight).

:::{hint} Note: take a break!
:class: dropdown
Frozen bacterial pellets can be stored at -80°C for extended periods (up to at least 3 months). There is no need to rush directly into purifying proteins from these pellets. We find that a nice workflow for making PURE proteins is to take two weeks to make 36 bacterial pellets, then purify those pellets at a later point.
:::

# References

- [Cell-free translation reconstituted with purified components](https://doi.org/10.1038/90802)
- [A Simple, Robust, and Low-Cost Method To Produce the PURE Cell-Free System](https://doi.org/10.1021/acssynbio.8b00427)
- [OnePot PURE Cell-Free System](https://dx.doi.org/10.3791/62625)

# Acknowledgements

Yan Zhang, Zoila Jurado, and Miki Yun (Richard Murray Lab, Caltech)
