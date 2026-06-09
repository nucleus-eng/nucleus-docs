---
title: Purify Proteins by Ni²⁺ Gravity Column
---

# Overview

You have a protein that you want to purify out of a complicated mixture. This protein has a 6xHis purification tag, which chelates Ni²⁺ ions. You can use a Ni-His resin to bind proteins with 6xHis tags. This resin is a suspension of microscopic gel beads with Ni ions covalently linked. Bound proteins can then be washed to remove non-tagged proteins, then eluted in a buffer with high concentration (~ 500 mM) Imidazole. Imidazole competes with 6xHis to bind the Ni ions, ultimately displacing your target proteins and releasing them from the affinity resin.

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

- [Prepare Protein Purification Buffers and Media](../prep-consumables/main.md)
- Prepare Columns
- [Lyse Bacteria by Sonication](../lysis-sonication/main.md)

::::::

:::::::

# Materials and Equipment


:::{table} Bill of Materials
:label: bom-purify-proteins-grav-column

| Name                           | Category    | Product                                                                                                                                                              | Manufacturer        | Part #      | Price   | Storage     | Link                                                                                                                                                                |
| ------------------------------ | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------- | ------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Columns                        | Columns     | Empty Disposable PD-10 Columns                                                                                                                                       | Cytiva              | 17043501    | $258.30 | 4°C to 30°C | [link](https://www.cytivalifesciences.com/en/us/shop/chromatography/columns/empty-columns-for-lab-scale/empty-disposable-pd-10-columns-p-06217)                     |
| Ni-His Resin                   | Resin       | NEBExpress Ni Resin                                                                                                                                                  | New England Biolabs | S1428S      | $358.00 | 1°C to 4°C  | [link](https://www.neb.com/en-us/products/s1428--nebexpress-ni-resin)                                                                                               |
| 15 mL centrifuge tubes         | Consumables | Corning® 15 mL PP Centrifuge Tubes, Rack Packed with CentriStar™ Cap, Sterile, 50/Rack, 500/Case                                                                     | Corning             | 430790      | $230.44 | 4°C to 30°C | [link](https://ecatalog.corning.com/life-sciences/b2b/UK/en/Liquid-Handling/Tubes%2C-Liquid-Handling/Centrifuge-Tubes/Corning%C2%AE-15mL-Centrifuge-Tubes/p/430790) |
| Potassium Hydroxide            | Buffers     | Potassium hydroxide - ACS reagent, ≥85%, pellets                                                                                                                     | Sigma-Aldrich       | 221473-1KG  | $99.90  | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/221473)                                                                                                    |
| Hydrochloric acid (1M)         | Buffers     | Hydrochloric acid 1 N, Reagent Grade, Packaging=Amber Bottle, Size=500 mL                                                                                            | VWR                 | E447-500L   | $72.46  | 4°C to 30°C | [link](https://us.vwr.com/store/catalog/static_catalog.jsp?catalog_number=97064-756)                                                                                |
| HEPES                          | Buffers     | HEPES, Crystalline Powder, ≥99.5% (titration), Poly bottle                                                                                                           | Sigma-Aldrich       | H3375-500G  | $431    | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/h3375)                                                                                                      |
| Imidazole                      | Buffers     | ReagentPlus® Imidazole, Crystalline, 99%                                                                                                                             | Sigma-Aldrich       | I202-500G   | $120    | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/213330)                                                                                                    |
| Ammonium Chloride              | Buffers     | Ammonium chloride, ACS reagent, ≥99.5%                                                                                                                               | Sigma-Aldrich       | 213330-500G | $73.50  | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/746398)                                                                                                    |
| Sodium Chloride                | Buffers     | Sodium Chloride, Redi-Dri™, anhydrous, free-flowing, ACS, ≥99%                                                                                                       | Sigma-Aldrich       | 746398-1KG  | $133.00 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sial/m2670)                                                                                                       |
| Potassium Chloride             | Buffers     | Potassium Chloride, ACS reagent, 99.0-100.5%                                                                                                                         | Sigma-Aldrich       | P3911-1KG   | $146.00 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/p3911)                                                                                                     |
| Magnesium Chloride hexahydrate | Buffers     | BioXtra Magnesium chloride, Hexahydrate, Powder or Crystals, ≥99.0%                                                                                                  | Sigma-Aldrich       | M2670-100G  | $50.50  | 4°C to 30°C | [link](https://www.thermofisher.com/order/catalog/product/77720)                                                                                                    |
| TCEP-HCl (0.5M; presuspended)  | Buffers     | Thermo Scientific, Bond-Breaker® Tris[2-Carboxyethyl]phosphine Neutral Solution (TCEP), Application=Water-Soluble Reducing Agent, Molecular Weight=286.65, Size=5 mL | Thermo Scientific   | 77720       | $175.65 | 4°C to 30°C | [link](https://www.thermofisher.com/order/catalog/product/77720)                                                                                                    |
:::

# Protocol

- [ ] **Prepare buffers:** Prepare the following buffers; chill at 4°C:
  - [ ] 50 mL Wash Buffer per sample.
  - [ ] 6 mL Elution Buffer per sample.
- [ ] **Assemble columns:** Assemble one (1) gravity column (2 mL resin bed) per sample.
- [ ] **Wash columns:** Wash each column with 5 CV of Ultrapure water. For this protocol, we will assume you are using a 2 mL resin bed.

:::{hint} Note: "CV" = Column Volume
:class: dropdown

One "Column Volume" is equal to the volume of affinity resin in your column. For example, "wash with 5 CV of Wash Buffer" means that for 2 mL of resin, wash with 10 mL of Wash Buffer. Specifying buffer volumes by CVs allows the user to increase or decrease the scale of the purification and still use the same protocol.

:::

- [ ] **Equilibrate columns:** Equilibrate each column with ≥ 5 CV (10 mL) cold Wash Buffer.
- [ ] **Load lysate:** Load up to 5 CV (10 mL) clarified lysate per column. Optionally capture flowthrough for later analysis.

:::{hint} Note: if you have >10 mL lysate, load in tranches.
:class: dropdown

If you have more than 10 mL of clarified lysate, you can load your sample in tranches of 10 mL at a time. At a point, your resin bed will saturate and you will stop binding more protein. You can determine this saturation point by analyzing the flowthrough of each tranche by protein gel. If you are saturating your columns, consider using a larger resin bed.

:::

- [ ] **Wash:** Wash column with ≥ 5 CV (10 mL) cold Wash Buffer. Allow buffer to flow through. Optionally capture flowthrough for later analysis.
- [ ] **Elute:** Elute sample with 3 CV (6 mL) cold Elution Buffer. Capture flow through in 15 mL centrifuge tube.

# Downloads

::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/purify-proteins-grav-column-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/purify-proteins-grav-column-bom.pdf>`
:::

::::

# References

- [Cell-free translation reconstituted with purified components](https://doi.org/10.1038/90802)
- [A Simple, Robust, and Low-Cost Method To Produce the PURE Cell-Free System](https://doi.org/10.1021/acssynbio.8b00427)
- [OnePot PURE Cell-Free System](https://dx.doi.org/10.3791/62625)

# Acknowledgements

Yan Zhang, Zoila Jurado, and Miki Yun (Richard Murray Lab, Caltech)
