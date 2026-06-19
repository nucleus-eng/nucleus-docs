---
title: Make Ribosomes
subtitle: Process
---

# Overview

Ribosomes are large complexes of RNA and proteins (MW ~2.7 MDa) that are the sites of protein synthesis. Ribosomes coordinate the decoding of mRNA transcripts by tRNA and catalyze the formation of each peptide bond in new proteins, making ribosomes a key component of any protein synthesis system. Ribosomes can be purified from E. coli biomass by a variety of methods (e.g., His-tagged ribosomes can be purified by Ni-His chromatography), but we recommend a two step process: (1) initial, tag-free purification by hydrophobic interaction chromatography (HIC) and (2) size-selective precipitation by ultracentrifugation. This protocol will show you how to grow E. coli A19 biomass and purify ribosomes by HIC followed by ultracentrifugation.

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{note} Notes
:class: dropdown
:icon: false

- We purify RNAs and Riboproteins from *E. coli* A19 biomass ([CGSC 5997](https://ecgrc.net/index.php/product/a19/)), a strain with a mutation in RNase I that improves RNA yields. You can use other RNase deficient strains with this protocol, but you may need to optimize this protocol to achieve high yield and purity.

- ‼️All reagents and materials must be prepared RNase-free. Use RNaseZap or 10% bleach to decontaminate plastic and glassware and rinse with nuclease-free water. We find ultrapure water (18.2 MOhm) is often sufficient for RNase-free work.

::::::

::::::{attention} Critical Materials
:class: dropdown
:icon: false

- A19 *E. coli*

::::::

::::::{note} Composition
:class: dropdown
:icon: false

:::{table} 
:label: tbl:comp-ribo
:align: center

| **Component** | **Stock Concentration** | **Reaction Concentration** |
| --- | --- | --- |
| Ribosomes | 10 $\mu$M (5.55x) | 1.8 $\mu$M |

:::

::::::

:::::::

# Materials and Equipment

:::{table} Bill of Materials
:label: bom-make-ribosomes

| Name                                          | Category    | Product                                                                                                                                                              | Manufacturer       | Part #      | Price   | Storage     | Link                                                                                                                                                                                 |
| --------------------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------- | ------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| HEPES                                         | Salts       | HEPES, Crystalline Powder, ≥99.5% (titration), Poly bottle                                                                                                           | Sigma-Aldrich      | H3375-500G  | $431    | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/h3375)                                                                                                                       |
| Ammonium Chloride                             | Salts       | Ammonium chloride, ACS reagent, ≥99.5%                                                                                                                               | Sigma-Aldrich      | 213330-500G | $73.50  | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/213330)                                                                                                                     |
| Ammonium Sulfate                              | Salts       | Ammonium sulfate,BioXtra, ≥99.0%                                                                                                                                     | Sigma-Aldrich      | A2939-1KG   | $188.00 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sial/a2939)                                                                                                                        |
| Potassium Chloride                            | Salts       | Potassium Chloride, ACS reagent, 99.0-100.5%                                                                                                                         | Sigma-Aldrich      | P3911-1KG   | $146.00 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/p3911)                                                                                                                      |
| Magnesium Acetate                             | Salts       | Magnesium acetate tetrahydrate                                                                                                                                       | Sigma-Aldrich      | M0631-100G  | $34.80  | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/m0631)                                                                                                                      |
| Potassium Hydroxide                           | Salts       | Potassium hydroxide - ACS reagent, ≥85%, pellets                                                                                                                     | Sigma-Aldrich      | 221473-1KG  | $99.90  | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/221473)                                                                                                                     |
| Sodium Chloride                               | Salts       | Sodium Chloride, Redi-Dri™, anhydrous, free-flowing, ACS, ≥99%                                                                                                       | Sigma-Aldrich      | 746398-1KG  | $133.00 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/746398)                                                                                                                     |
| Sodium Hydroxide (pellets)                    | Salts       | Sodium hydroxide, ACS Reagent Grade, Pellets, ≥97.0%, Poly bottle                                                                                                    | Sigma-Aldrich      | 221465-1KG  | $137.00 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/221465)                                                                                                                     |
| Acetic Acid (glacial)                         | Supplements | Acetic Acid, Glacial (Certified ACS), Fisher Chemical                                                                                                                | Fisher Scientific  | A38-212     | $458    | 4°C to 30°C | [link](https://www.fishersci.ca/shop/products/acetic-acid-glacial-certified-acs-fisher-chemical-9/A38212)                                                                            |
| Sucrose                                       | Supplements | Sucrose, bioultra, for molecular biology, ≥99.5% (HPLC)                                                                                                              | Sigma-Aldrich      | 84097-1KG   | $170.00 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/84097)                                                                                                                       |
| TCEP                                          | Supplements | Thermo Scientific, Bond-Breaker® Tris[2-Carboxyethyl]phosphine Neutral Solution (TCEP), Application=Water-Soluble Reducing Agent, Molecular Weight=286.65, Size=5 mL | Thermo Scientific  | 77720       | $175.65 | 4°C to 30°C | [link](https://www.thermofisher.com/order/catalog/product/77720)                                                                                                                     |
| Ethanol                                       | Supplements | Ethanol, HPLC/Spectrophotometric Grade, Liquid, ≥99.5%, Glass bottle, 200 Proof                                                                                      | Sigma-Aldrich      | 459828-4L   | $493.00 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/459828)                                                                                                                     |
| Laemmli Buffer (6x)                           | Supplements | Laemmli SDS-Sample Buffer (6x, Reducing)                                                                                                                             | Boston BioProducts | BP-111R     | $42.00  | 4°C to 30°C | [link](https://www.bostonbioproducts.com/products/laemmli-sds-sample-buffer-6x-reducing-bp-111r)                                                                                     |
| LB                                            | Media       | Luria Broth (Miller's LB Broth), Non-Sterile, pH 6.8-7.2, Molecular Biology Grade, Powder                                                                            | Sigma-Aldrich      | L3522-1KG   | $221    | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/l3522)                                                                                                                       |
| A19 *E. coli*                                 | Strains     | A19 (RNase I mutant)                                                                                                                                                 | CGSC               | 5997        | $130.00 | -80°C       | [link](https://ecgrc.net/index.php/product/a19/)                                                                                                                                     |
| Culture tubes (14 mL)                         | Consumables | 14mL Culture Tube and Dual Cap, PP, Sterile                                                                                                                          | CELLTREAT          | 230439      | $190.00 | 4°C to 30°C | [link](https://www.celltreat.com/product/230439/)                                                                                                                                    |
| 2 L baffled Erlenmeyer flasks                 | Consumables | PYREX® 2L Delong Shaker Erlenmeyer Flask with Baffles                                                                                                                | Corning            | 4444-2L     | $96.44  | 4°C to 30°C | [link](https://ecatalog.corning.com/life-sciences/b2c/US/en/Bioprocess-and-Scale-up/Erlenmeyer-Flasks/Erlenmeyer-Flasks%2C-Glass/PYREX%C2%AE-Flask-with-Baffles/p/pyrexFlaskBaffled) |
| 1 L centrifuge bottles                        | Consumables | Thermo Scientific™ # Fiberlite 1000mL Bottles                                                                                                                        | Thermo Scientific  | 010-1491    | $326.84 | 4°C to 30°C | [link](https://www.thermofisher.com/order/catalog/product/010-1491)                                                                                                                  |
| 0.22 µm syringe filters                       | Consumables | PES Syringe Filter, 0.22µm, 30mm, Sterile                                                                                                                            | CELLTREAT          | 229747      | $84.00  | 4°C to 30°C | [link](https://www.celltreat.com/product/229747/)                                                                                                                                    |
| Butyl HIC columns (5 mL)                      | Columns     | HiTrap Butyl HP Column                                                                                                                                               | Cytiva             | 28-4110-05  | $679.00 | 4°C to 30°C | [link](https://www.cytivalifesciences.com/en/us/products/items/hitrap-butyl-hp-p-05631?selectedProduct=28411005)                                                                     |
| 15 mL centrifuge tubes                        | Consumables | Corning® 15 mL PP Centrifuge Tubes, Rack Packed with CentriStar™ Cap, Sterile, 50/Rack, 500/Case                                                                     | Corning            | 430790      | $230.44 | 4°C to 30°C | [link](https://ecatalog.corning.com/life-sciences/b2b/UK/en/Liquid-Handling/Tubes%2C-Liquid-Handling/Centrifuge-Tubes/Corning%C2%AE-15mL-Centrifuge-Tubes/p/430790)                  |
| Polycarbonate ultracentrifuge bottles (70 mL) | Consumables | 70 mL Polycarbonate Bottle Assembly, 38 x 102mm - 6Pk                                                                                                                | Beckman Coulter    | 355622      | $687.60 | 4°C to 30°C | [link](https://www.beckman.com/supplies/tubes-and-bottles/bottles/355622)                                                                                                            |
| 100 kDa centrifugal filter                    | Consumables | Amicon® Ultra Centrifugal Filter, 100 kDa MWCO                                                                                                                       | EMD Millipore      | UFC910008   | $141.00 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/mm/ufc9100)                                                                                                                        |
| Tris-Glycine 4–20% gels                       | Consumables | 4–20% Mini-PROTEAN® TGX™ Precast Protein Gels, 10-well, 50 µL                                                                                                        | BioRad             | 4561094     | $153.00 | 1°C to 4°C  | [link](https://www.bio-rad.com/en-us/sku/4561094-4-20-mini-protean-tgx-precast-protein-gels-10-well-50-ul?ID=4561094)                                                                |

:::

# Protocol

## Prepare Stock Buffers

- [ ] Make the following stock solutions. Use ultrapure water (18.2 MΩ, e.g., Milli-Q) and keep everything RNase-free.

| **Stocks**         | Final Concentration (mM) | MW (g/mol) | Mass to add (g) | Final Vol (mL) | Storage (°C) |
| ------------------ | ------------------------ | ---------- | --------------- | -------------- | ------------ |
| HEPES-KOH (pH 7.6) | 1000                     | 238.3      | 238.3           | 1000           | room temp    |
| Ammonium Chloride  | 1000                     | 53.49      | 53.49           | 1000           | room temp    |
| Potassium Chloride | 1000                     | 74.55      | 74.55           | 1000           | room temp    |
| Magnesium Acetate  | 1000                     | 214.45     | 214.45          | 1000           | room temp    |
| Sodium Hydroxide   | 500                      | 40.00      | 20              | 1000           | room temp    |

- [ ] Adjust the pH of HEPES-KOH to 7.6 with Potassium Hydroxide.
- [ ] Prepare Sodium Hydroxide (0.5 M) from pellets (used to clean the HIC column).

:::{hint} Note: components added dry or purchased
:class: dropdown

Ammonium sulfate and sucrose are **added dry** directly to the buffers (masses given in each recipe below), not prepared as stock solutions. TCEP is used from a purchased **0.5 M (500 mM)** neutral stock (Bond-Breaker) and added fresh on the day of use.

:::

## Prepare Stable Buffers

Make these buffers *in advance* and store at 4°C. Add all components **except TCEP**, which you must add fresh on the day of use.

- [ ] **Ribosome Lysis Buffer** — used to resuspend the cell pellet for sonication.

| Reagent            | Final Concentration (mM) | Stock Concentration (mM) | Volume to Add (mL) |
| ------------------ | ------------------------ | ------------------------ | ------------------ |
| HEPES-KOH (pH 7.6) | 10                       | 1000                     | 15                 |
| Magnesium Acetate  | 10                       | 1000                     | 15                 |
| Potassium Chloride | 50                       | 1000                     | 75                 |
| TCEP               | 1                        | 500                      | 3                  |
| Ultrapure water    | —                        | —                        | 1392               |
| **Total**          |                          |                          | **1500**           |

- [ ] **Ribosome Salting Out Buffer** — added 1:1 to clarified lysate to bring ammonium sulfate to 1.5 M and precipitate contaminants.

| Reagent            | Final Concentration (mM) | Stock Concentration (mM) | Volume to Add (mL) |
| ------------------ | ------------------------ | ------------------------ | ------------------ |
| Ammonium Sulfate   | 3000                     | n/a (dry)                | 198.21 g           |
| HEPES-KOH (pH 7.6) | 10                       | 1000                     | 5                  |
| Magnesium Acetate  | 10                       | 1000                     | 5                  |
| Potassium Chloride | 50                       | 1000                     | 25                 |
| TCEP               | 1                        | 500                      | 1                  |
| Ultrapure water    | —                        | —                        | ~265.8             |
| **Total**          |                          |                          | **500**            |

- [ ] **Ribosome Wash Buffer** — HIC running/wash buffer; high ammonium sulfate drives hydrophobic binding.

| Reagent            | Final Concentration (mM) | Stock Concentration (mM) | Volume to Add (mL) |
| ------------------ | ------------------------ | ------------------------ | ------------------ |
| Ammonium Sulfate   | 1500                     | n/a (dry)                | 396.42 g           |
| HEPES-KOH (pH 7.6) | 20                       | 1000                     | 40                 |
| Magnesium Acetate  | 10                       | 1000                     | 20                 |
| TCEP               | 1                        | 500                      | 4                  |
| Ultrapure water    | —                        | —                        | ~1539.6            |
| **Total**          |                          |                          | **2000**           |

- [ ] **Ribosome Elution Buffer** — HIC elution buffer; low salt releases bound ribosomes.

| Reagent            | Final Concentration (mM) | Stock Concentration (mM) | Volume to Add (mL) |
| ------------------ | ------------------------ | ------------------------ | ------------------ |
| HEPES-KOH (pH 7.6) | 20                       | 1000                     | 20                 |
| Magnesium Acetate  | 10                       | 1000                     | 10                 |
| TCEP               | 1                        | 500                      | 2                  |
| Ultrapure water    | —                        | —                        | 968                |
| **Total**          |                          |                          | **1000**           |

- [ ] **Cushion Buffer** — dense sucrose cushion through which ribosomes are pelleted during ultracentrifugation.

| Reagent            | Final Concentration (mM) | Stock Concentration (mM) | Volume to Add (mL) |
| ------------------ | ------------------------ | ------------------------ | ------------------ |
| Sucrose            | 30% (w/v)                | n/a (dry)                | 300 g              |
| HEPES-KOH (pH 7.6) | 20                       | 1000                     | 20                 |
| Ammonium Chloride  | 30                       | 1000                     | 30                 |
| Magnesium Acetate  | 10                       | 1000                     | 10                 |
| TCEP               | 1                        | 500                      | 2                  |
| Ultrapure water    | —                        | —                        | ~638               |
| **Total**          |                          |                          | **1000**           |

- [ ] **Ribosome Buffer** — final resuspension and storage buffer for purified ribosomes.

| Reagent            | Final Concentration (mM) | Stock Concentration (mM) | Volume to Add (mL) |
| ------------------ | ------------------------ | ------------------------ | ------------------ |
| HEPES-KOH (pH 7.6) | 20                       | 1000                     | 10                 |
| Magnesium Acetate  | 6                        | 1000                     | 3                  |
| Potassium Chloride | 30                       | 1000                     | 15                 |
| TCEP               | 1                        | 500                      | 1                  |
| Ultrapure water    | —                        | —                        | 471                |
| **Total**          |                          |                          | **500**            |

## Prepare Working Buffers

Make these column-cleaning solutions as needed for the FPLC step.

- [ ] **Acetic Acid (0.1 M)** — prepared by diluting glacial acetic acid; used to clean the HIC column.

| Reagent               | Final Concentration (mM) | Stock Concentration (mM) | Volume to Add (mL) |
| --------------------- | ------------------------ | ------------------------ | ------------------ |
| Acetic Acid (glacial) | 100                      | 17 400                   | 5.75               |
| Ultrapure water       | —                        | —                        | 994.25             |
| **Total**             |                          |                          | 1000               |

- [ ] **Ethanol (20% v/v)** — used to wash and store the HIC column.

| Reagent         | Final Concentration | Stock Concentration | Volume to Add (mL) |
| --------------- | ------------------- | ------------------- | ------------------ |
| Ethanol         | 20% (v/v)           | 100% (v/v)          | 200                |
| Ultrapure water | —                   | —                   | 800                |
| **Total**       |                     |                     | **1000**           |

## Cell culture

:::{hint} Note: you can work from glycerol stocks OR colonies.
:icon: false
:class: dropdown
We first need to prepare bacterial cultures. We will work from 6 mL overnight cultures of our expression strains and backdilute them the next day. In order to prepare these overnight cultures, we need stocks of bacteria.

We worked from 100 µL aliquots of our glycerol stocks, frozen in PCR strip tubes. When seeding our overnights with bacteria, we poked one glycerol aliquot with a pipette tip and ejected the tip into culture tubes (more details below).

Optionally, you can work from individual colonies by streaking out your bacterial stocks. Working from colonies assures that your bulk outgrowth will have come from a single colony forming unit.
:::

**Prepare overnight cultures.**
- [ ] Add 5 mL Luria Broth (LB) under sterile conditions to two (2) 14 mL culture tubes.
- [ ] Label one tube “(+)”. Add 10 µL of A19 glycerol stock to (+).
- [ ] Label the other tube “(-)”. This will be your negative control, testing if your technique is sterile.
- [ ] Incubate both tubes overnight shaking at 37°C / (225-250) rpm / (12-16) hr.

**Perform bulk outgrowth.**
- [ ]  Check if (-) has growth. If not, continue.
- [ ]  Back dilute overnight 1:250 - 1:1000 into 4x 450 mL fresh LB in 2 L baffled Erlenmeyer flasks (e.g., 1.8 mL overnight into 450 mL LB).
- [ ]  Incubate back diluted cultures at 37°C / (225-250) rpm to mid-log phase (OD₆₀₀ between 0.6 and 0.8, typically ~3 hrs).

**Pellet, wash, and store cells.**
- [ ]  Fill 1 L centrifuge bottles with culture. Balance centrifuge bottles against each other and centrifuge cultures at 16 000 rcf / 4°C / 10 min.
- [ ]  Decant supernatant, add fresh culture, and repeat centrifugation as above, working through the remaining culture. You should end up with large pellets at the bottom of each centrifuge bottle.
- [ ]  Wash the pellets by resuspending (4°C) NaCl (0.9%) in about 50 mL and transfer the resuspended cells to a single centrifuge bottle. Dilute to ~500 mL and re-pellet at 16 000 rcf / 4°C / 10 min.
- [ ]  Transfer pellets by spatula into a tared bag weigh and record the mass.
- [ ]  Flash freeze pellet in liquid nitrogen and store at -80°C.

## Lysis

- [ ]  Resuspend (2-5) g cell pellet in 25 mL of Ribosome Lysis buffer & lyse cells using 130-watt probe sonicator (probe tip diameter: 6 mm) on ice with following parameters: 50% amplitude, 15s on/ 30s off for 2 min on-time. The amount of energy delivered via sonication will vary depending on the amount of cells resuspended.
- [ ]  Clarify lysate by centrifugation at 16 000 rcf / 4°C / 10 min.
- [ ]  Aspirate supernatant and measure volume. Add an equal volume of Salting Out buffer to adjust the concentration of ammonium sulfate to 1.5 M and mix well. Incubate at 4°C / 10 min.
- [ ]  Remove precipitate by centrifugation at 16 000 rcf / 4°C / 10 min.
- [ ]  Filter supernatant using a 0.22 µm syringe filter and keep cold (4°C).

## FPLC purification
        
::::{hint} Note: line configuration on FPLC.
:icon: false
:class: dropdown
:::{table}
| Line | Buffer |
| --- | --- |
| A11 | Ribosome Wash Buffer |
| B1 | Ribosome Elution Buffer |
| A12 | Water |
| A13 | 0.5 M NaOH |
| A14 | 0.1 M Acetic Acid |
:::
::::

**Set-up**
- [ ]  Connect the two Butyl column (5 mL) in tandem, totaling a column volume (CV) of 10 mL.
- [ ]  Place A1 in Ribosome Wash Buffer and B1 in Ribosome Elution Buffer. Place sample line in A2. Set the default flow rate to 4 mL / min (except for pump washes: 10 mL/min).

**Equilibrate HIC column**
- [ ]  Perform a pump wash with Ribosome Wash Buffer (without TCEP) and equilibrate the column with 4 CV of Ribosome Wash Buffer(without TCEP).
- [ ]  Once you've equilibrated your columns, add TCEP to Ribosome Wash and Elution Buffer.
- [ ]  Load your fraction collector with 15 mL conical tubes and set the fraction volume to 5 mL.
- [ ]  If using a sample pump to load samples, place sample line (S1) into sample and load around 90% of sample volume onto the column. Once almost loaded, dilute the sample with Ribosome wash buffer (~5 mL) to load as much sample as possible. DO NOT allow air into the FPLC; make sure the sample line is always submerged.

**Perform HIC**
- [ ]  Wash step 1: wash with 3 CV of Ribosome Wash Buffer to remove unbound components .
- [ ]  Wash step 2: wash with 5 CV of 80% Wash Buffer and 20% Ribosome Elution Buffer.
- [ ]  Elution: elute the product by applying 3.5 CV (35 mL) of 50% Ribosome Wash Buffer and 50% Ribosome Elution Buffer. Ensure that the fraction collector captures these fractions separately.
- [ ]  Wash step 3: Elute all strongly interacting contaminants with 5 CV of 100% Ribosome Elution Buffer.

**Clean columns**
- [ ]  Place inlet into a NaOH (0.5 M) and perform pump wash. Wash the column with 3 CV NaOH (0.5M).
- [ ]  Place the inlet into water, perform pump wash, and then wash column in 2 CV filtered Ultrapure water.
- [ ]  Place the inlet into AcOH (0.1 M), perform pump wash, and subsequently wash column with 3 CV AcOH (0.1 M).
- [ ]  Pump wash with water and wash column with 2 CV filtered MilliQ water.
- [ ]  Place all inlets into EtOH (20% v/v). Perform a pump wash, then wash columns with 3 CV EtOH (20% v/v). Store columns at 4°C in EtOH (20% v/v) until ready for use.

## Ultracentrifugation

- [ ]  Gently overlay recovered fractions (should correspond to second peak) onto 35 mL of Cushion Buffer in a polycarbonate ultracentrifuge bottle (70 mL).
- [ ]  Prepare another polycarbonate ultracentrifuge bottle as a balance. Measure 35 mL of Cushion Buffer, then add Ribosome Buffer until the balance mass is within 0.1 g of the sample bottle mass. **Make sure all bottles are well balanced (Δm ≤ 0.1 g) and have no cracks!**
- [ ]  Pellet ribosomes by ultracentrifugation at 100 000 rcf / 4°C / 16 hrs. A translucent ribosome pellet will be formed at the bottom of the centrifuge bottle. It may be difficult to see.
- [ ]  Discard the supernatant. Carefully, wash each pellet with 0.5 mL cold ribosome buffer. Repeat this step twice.

::::{hint} Note: Don’t disturb the ribosome pellet during washing.
:class: dropdown
:icon: false

The ribosome pellet is fairly compact and stable, but some ribosomes can get resuspended during washing and be lost in the process. Be careful! 

First, find the pellet. Next, wash the pellet by gently pipetting Ribosome Buffer down the sides of the tube, allowing the buffer to run over the pellet. Tilt the ultracentrifuge bottle gently so that the buffer falls away from the pellet, aspirate the buffer, add fresh buffer as before, and repeat.
::::

- [ ]  Resuspend the clear pellets in 100 µL of Ribosome Buffer on ice using a magnetic stir bar (3 mm diameter, 10 mm length) on a magnetic stirrer set at the lowest possible speed. Collect resuspended ribosomes.
- [ ]  Wash tubes with an additional 50 µL of Ribosome Buffer to resuspend any remaining ribosomes.

## Quality Control

- [ ]  Determine the ribosome concentration by measuring the absorbance at 260 nm at a 100x dilution in Ribosome Buffer. 10 units of A₂₆₀ from a 100x dilution corresponds to 23 µM of undiluted solution.
- [ ]  Dilute to final stock of 10 µM. To adjust the concentration, dilute the ribosomes with ribosome buffer or concentrate further via centrifugation at 4000 rcf in a 100 kDa centrifugal filter at 4°C.
- [ ]  Protein gel: dilute 10 µM sample by 4x (Add 2.5 µL of sample with 7.5 µL water) and mix with 2 µL of 6x Laemmli loading buffer. Boil samples at 90°C for 10 min and load 5 µL and 2.5 µL onto 4-20% tris-glycine gel. Run gel at 200 V / 30-45 min or until the loading dye line reaches the bottom of the gel.

## Storage

- [ ] Aliquot your ribosomes to reduce freeze / thaw cycles and store at -80°C.

# Downloads

:::::{card}
:header: **Resources**
::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**
{button}`download <generated/make-ribosomes-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**
{button}`download <generated/make-ribosomes-bom.pdf>`
:::

::::
:::::