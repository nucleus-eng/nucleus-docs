---
title: "Protein Gel"
subtitle: "Process"
---

# Overview

You have samples and you want to see (1) what proteins are in that sample and (2) how much of each protein there is. You can use this protocol to semi-quantitate protein sizes and concentrations in your samples. You can use this information to roughly measure protein purity.

# Materials and Equipment

<!-- The lab-ready pipeline generates this process's Bill of Materials PDF and
     materials CSV from the table labeled `bom-protein-gel` below.
     Without this labeled table, no BOM artifacts are generated. See issue #10. -->

:::{table} Bill of Materials
:label: bom-protein-gel

| **Name** | **Category** | **Product** | **Manufacturer** | **Part #** | **Price** | **Storage** | **Link** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Tris-Glycine 4%–20% gels | Consumable | 4–20% Mini-PROTEAN® TGX™ Precast Protein Gels, 10-well, 50 µL | BioRad | 4561094 | $153.00 | 1°C to 4°C | [link](https://www.bio-rad.com/en-us/sku/4561094-4-20-mini-protean-tgx-precast-protein-gels-10-well-50-ul?ID=4561094) |
| Laemmli Buffer (6x) | Reagent | Laemmli SDS-Sample Buffer (6X, Reducing) | Boston BioProducts | BP-111R | $42.00 | 4°C to 30°C | [link](https://www.bostonbioproducts.com/products/laemmli-sds-sample-buffer-6x-reducing-bp-111r) |
| Rapid protein stain | Reagent | Pageblue™ Protein Staining Solution | Thermo Scientific | 24620 | $153.65 | 4°C to 30°C | [link](https://www.thermofisher.com/order/catalog/product/24620) |
| Thermocycler | Equipment | SimpliAmp™ Thermal Cycler | Applied Biosystems | A24811 | $6,580.00 | 4°C to 30°C | [link](https://www.thermofisher.com/order/catalog/product/A24811) |
| Gel Tank | Equipment | Criterion™ Cell | BioRad | 1656001 | $852.00 | 4°C to 30°C | [link](https://www.bio-rad.com/en-us/product/criterion-cell?ID=0d31b27f-e577-4e08-b552-8dc71e6105b7) |
| Gel Power Supply | Equipment | PowerPac™ Basic Power Supply | BioRad | 1645050 | $530.00 | 4°C to 30°C | [link](https://www.bio-rad.com/en-us/product/powerpac-basic-power-supply?ID=bea5dea1-cef0-43ad-8af5-b2c0287f6e07) |
| Gel Imager | Equipment | ChemiDoc™ Imaging System | BioRad | 12003153 | unlisted | 4°C to 30°C | [link](https://www.bio-rad.com/en-us/sku/12003153-chemidoc-imaging-system?ID=12003153) |

:::

:::{note}
**Missing materials — requires review.** The following items are referenced in the protocol but are absent from the materials table above. Add entries with product details before publishing:

- **Protein ladder** — referenced in the "Load protein ladder" step. Product and part number not specified in source.
- **Running buffer (Tris-Gly)** — referenced in the "Set up a gel box" step. Product and part number not specified in source.
:::

# Protocol

- [ ] **Denature samples.**
    - [ ] Label one tube per sample.
    - [ ] Add 4 µL of 6x Laemmli sample buffer and 20 µL of sample (~1 µg total protein) per tube. Mix by pipetting.
    - [ ] Incubate samples at 90°C / 10 min.
- [ ] **Set up a gel box.**
    - [ ] Open an individually wrapped protein gel (we use 10%–20% Tris Gly gels).
    - [ ] Remove plastic tape at the bottom of gel. This exposes a strip of the gel to the running buffer, allowing current to flow from one electrode through the gel to the other electrode.
    - [ ] Place gel in gel box and seal tightly. Check the seal by pouring running buffer (we use Tris Gly) into the front half of the reservoir and checking that no buffer leaks into the back half. If so, remove the gel, empty the reservoir and try again.
    - [ ] Pour running buffer into the back half of the reservoir.
    - [ ] Carefully, remove comb from top of gel.
- [ ] **Load 10 µL protein ladder onto the outermost lanes.**
- [ ] **Load each sample onto its own lane. Target between 1–2 µg purified protein and between 10 µL and 20 µL per lane.**
- [ ] **Run the gel at 200 V / 40–50 min, or until the dye front touches the bottom of the gel.**
- [ ] **Stain and destain the gel.**
    - [ ] Using a gel knife, crack open the plastic cassette holding the gel.
    - [ ] Remove the gel carefully into a waterproof container. We find this is easier if you cover the bottom of your container with Ultrapure water (≥ 3 mm).
    - [ ] Cover the gel with Ultrapure water (~40 mL), microwave for 30 seconds, and rock for 5 minutes. Decant and repeat this step twice, washing a total of three (3) times.
    - [ ] Cover gel in a rapid protein stain (~40 mL) in the same container. We use PageBlue Protein Staining Solution. Microwave for 30 seconds, then incubate at room temperature with rocking for ~30 minutes.
    - [ ] Decant staining solution, rinse gel at least once, then cover in Ultrapure water. Incubate gel at room temperature with rocking until you can see distinct protein bands (up to overnight).

:::{hint} Note: Use Kimwipes to speed up destaining
:class: dropdown

Knot 2–3 Kimwipes together and add to waterproof container with the gel while destaining. The Kimwipes absorbs the protein stain, reducing the number of times you need to exchange the destaining water and speeding up the process.

:::

- [ ] **Observe gel. High purity protein preps should have distinct bands at the correct molecular weight, with no unexpected additional bands.**

:::{hint} Note: You can use a gel imager to semi-quantitate your protein
:class: dropdown

You should now be able to see protein bands by naked eye, which is sufficient to get a qualitative understanding of your protein purity and concentration. Using a good imager will allow you to take high resolution photos of your gel. You can then calculate your sample purity by integrating the intensity of your target band and normalizing by the intensity of the whole lane. Further, you can semi-quantitate your sample if you use a protein ladder with known concentrations at specific bands.

:::

# Downloads

<!-- Protocol and BOM are generated by the lab-ready pipeline (issue #10) into a
     gitignored generated/ dir and published at deploy — never committed. -->

::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/protein-gel-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/protein-gel-bom.pdf>`
:::

::::
