---
title: "Pierce660 Assay"
subtitle: "Process"
---

# Overview

Pierce660 is a quick (5 min) colorimetric method for total protein quantitation. Compared to other quantitation assays, we find Pierce660 to be simple and reproducible, with a wide dynamic range (50–2000 µg/mL), and robust to buffer composition, including detergents and reducing agents.

# Materials and Equipment

<!-- The lab-ready pipeline generates this process's Bill of Materials PDF and
     materials CSV from the table labeled `bom-pierce660` below.
     Without this labeled table, no BOM artifacts are generated. See issue #10. -->

:::{table} Bill of Materials
:label: bom-pierce660

| **Name** | **Category** | **Product** | **Manufacturer** | **Part #** | **Price** | **Storage** | **Link** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pierce660 Reagent | Reagent | Pierce™ 660nm Protein Assay Reagent | Thermo Scientific | 22660 | $176.65 | 4°C to 30°C | [link](https://www.thermofisher.com/order/catalog/product/22660) |
| BSA Protein Standard | Reagent | Pierce™ Bovine Serum Albumin Standard Ampules, 2 mg/mL | Thermo Scientific | 23209 | $81.65 | 4°C to 30°C | [link](https://www.thermofisher.com/order/catalog/product/23209) |
| 96-well optical plate | Consumable | Microplate, 96 well, PS, U-bottom, clear | Greiner | 650101 | $156.14 | 4°C to 30°C | [link](https://shop.gbo.com/en/usa/products/bioscience/microplates/96-well-microplates/96-well-microplates-clear/650101.html) |
| Plate Reader | Equipment | BioTek Cytation 5 Cell Imaging Multimode Reader | Agilent | CYT5MFAWSN | Quote required | 4°C to 30°C | [link](https://www.fishersci.com/shop/products/cytation-5-cell-imaging-multi-mode-reader-28/BTCYT5MFAW) |

:::

# Protocol

- [ ] Prepare a standard curve within the assay's working range (125 µg/mL to 2000 µg/mL). Remember to dilute the BSA stock in the same buffer used for your sample. The standards can be stored at −20°C for future assays.

:::{hint} Note: Standard curve dilution table
:class: dropdown

| **Concentration** | **Volume of BSA Stock (2 mg/mL)** | **Volume of Buffer** |
| --- | --- | --- |
| 2 mg/mL | 200 µL | 0 µL |
| 1.5 mg/mL | 150 µL | 50 µL |
| 1 mg/mL | 100 µL | 100 µL |
| 0.75 mg/mL | 75 µL | 125 µL |
| 0.50 mg/mL | 50 µL | 150 µL |
| 0.25 mg/mL | 25 µL | 175 µL |
| 0.125 mg/mL | 12.5 µL | 187.5 µL |
| 0 mg/mL | 0 | 200 µL |

:::

- [ ] Prepare a dilution series of your samples in the same buffer.

:::{hint} Note: We do 2x serial dilutions
:class: dropdown

We like to prepare eight (8) dilutions of our samples in a twofold (2x) dilution series (1x, 2x, …, 128x) by diluting 15 µL of each sample + 15 µL of sample buffer. This range of dilutions (~100x) fits on a single column of a 96-well plate for each sample and tends to give us at least two dilutions that are in the linear range of the assay.

:::

- [ ] Mix Pierce660 Reagent well by inverting the bottle before use.
- [ ] Array 150 µL of Pierce660 Reagent on a 96-well optical plate by reverse pipetting.
- [ ] Add 10 µL of each sample (BSA standard series and sample concentration series) column-wise (e.g., BSA standard in Column 12, Sample 1 series in column 1, …) to the optical plate.

:::{hint} Note: use a single channel pipette, or reverse pipette with a multichannel, to transfer samples.
:class: dropdown
Pierce660 is quite naturally sensitive to input volumes. Typically, multichannel pipetting volume is too high variance to reliably measure protein concentrations. One simple way to reduce pipetting volume is to use the same single channel pipette to transfer _every sample,_ including preparing the 2x dilution series in the first place. This takes time, but works. 

An effective alternative is to _always_ reverse pipette your samples when using a multichannel pipette. Push your pipette plunger past the aspiration point to the blow-out point, as far as you can, and aspirate the full volume. You may see variance in the pipetted volume, but don't worry. When dispensing sample, dispense to the first point (aspiration) instead of all the way (blow-out). This ensures each sample is equally dispensed, in spite of variance in aspirated volume.
:::

- [ ] Cover your plate with aluminum foil and mix on a plate shaker at medium speed for 1 minute.
- [ ] Incubate your plate at 25°C / 5 min. Samples should turn from brown to green.
- [ ] Using a plate reader, measure the absorbance of the samples at 660 nm.
- [ ] Analyze results.
    - [ ] Subtract the absorbance of blank samples (i.e., BSA standard = 0 mg/µL) from all other samples ("background subtracted absorbance").
    - [ ] Plot the standard curve by plotting the background subtracted absorbance vs. concentration for each BSA standard. Fit a line to your standard curve.
    - [ ] For each sample dilution series, choose a well with a background subtracted absorbance in the linear range of the standard curve.
    - [ ] Using the linear fit of your standard curve, calculate the concentration of the sample.

# Downloads

<!-- Protocol and BOM are generated by the lab-ready pipeline (issue #10) into a
     gitignored generated/ dir and published at deploy — never committed. -->

::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/pierce660-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/pierce660-bom.pdf>`
:::

:::{card}
:header: **Manufacturer's Manual**

<!-- TODO: host this PDF externally (e.g. S3 or vendor link) rather than
     serving from the repo. Manufacturer PDFs should not be committed to
     nucleus-docs. See Issue #87. -->
{button}`download <resources/Private & Shared/Pierce660 Assay/Pierce660_Manual.pdf>`
:::

::::
