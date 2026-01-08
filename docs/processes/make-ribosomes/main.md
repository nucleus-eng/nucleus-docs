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

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

- None

::::::

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

- None

::::::

::::::{attention} Critical Materials
:class: dropdown
:icon: false

- A19 *E. coli*

::::::

::::::{attention} Genetically Encoded Components
:class: dropdown
:icon: false

- None

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

::::::{note} References
:class: dropdown
:icon: false

- None

::::::

:::::::

# Protocol

## Cell culture

:::{hint} Note: you can work from glycerol stocks OR colonies.
:icon: false
:class: dropdown
We first need to prepare bacterial cultures. We will work from 6 mL overnight cultures of our expression strains and backdilute them the next day. In order to prepare these overnight cultures, we need stocks of bacteria.

We worked from 100 uL aliquots of our glycerol stocks, frozen in PCR strip tubes. When seeding our overnights with bacteria, we poked one glycerol aliquot with a pipette tip and ejected the tip into culture tubes (more details below).

Optionally, you can work from individual colonies by streaking out your bacterial stocks. Working from colonies assures that your bulk outgrowth will have come from a single colony forming unit.
:::

**Prepare overnight cultures.**
- [ ] Add 5 mL Luria Broth (LB) under sterile conditions to two (2) 14 mL culture tubes.
- [ ] Label one tube “(+)”. Add 10 uL of A19 glycerol stock to (+).
- [ ] Label the other tube “(-)”. This will be your negative control, testing if your technique is sterile.
- [ ] Incubate both tubes overnight shaking at 37C / (225-250) rpm / (12-16) hr.

**Perform bulk outgrowth.**
- [ ]  Check if (-) has growth. If not, continue.
- [ ]  Back dilute overnight 1:250 - 1:1000 into 4x 450 mL fresh LB in 2 L baffled Erlenmeyer flasks (e.g., 1.8 mL overnight into 450 mL LB).
- [ ]  Incubate back diluted cultures at 37C / (225-250) rpm to mid-log phase (OD600 between 0.6 and 0.8, typically ~3 hrs).

**Pellet, wash, and store cells.**
- [ ]  Fill 1 L centrifuge bottles with culture. Balance centrifuge bottles against each other and centrifuge cultures at 16 000 rcf / 4C / 10 min.
- [ ]  Decant supernatant, add fresh culture, and repeat centrifugation as above, working through the remaining culture. You should end up with large pellets at the bottom of each centrifuge bottle.
- [ ]  Wash the pellets by resuspending (4C) NaCl (0.9%) in about 50 mL and transfer the resuspended cells to a single centrifuge bottle. Dilute to ~500 mL and re-pellet at 16 000 rcf / 4C / 10 min.
- [ ]  Transfer pellets by spatula into a tared bag weigh and record the mass.
- [ ]  Flash freeze pellet in liquid nitrogen and store at -80C.

## Lysis

- [ ]  Resuspend (2-5) g cell pellet in 25 mL of Ribosome Lysis buffer & lyse cells using 130-watt probe sonicator (probe tip diameter: 6 mm) on ice with following parameters: 50% amplitude, 15s on/ 30s off for 2 minutes on-time. The amount of energy delivered via sonication will vary depending on the amount of cells resuspended.
- [ ]  Clarify lysate by centrifugation at 16 000 rcf / 4C / 10 min.
- [ ]  Aspirate supernatant and measure volume. Add an equal volume of Salting Out buffer to adjust the concentration of ammonium sulfate to 1.5 M and mix well. Incubate at 4C / 10 min.
- [ ]  Remove precipitate by centrifugation at 16 000 rcf / 4C / 10 min.
- [ ]  Filter supernatant using a 0.22 um syringe filter and keep cold (4C).

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
- [ ]  Place all inlets into EtOH (20% v/v). Perform a pump wash, then wash columns with 3 CV EtOH (20% v/v). Store columns at 4C in EtOH (20% v/v) until ready for use.

## Ultracentrifugation

- [ ]  Gently overlay recovered fractions (should correspond to second peak) onto 35 mL of Cushion Buffer in a polycarbonate ultracentrifuge bottle (70 mL).
- [ ]  Prepare another polycarbonate ultracentrifuge bottle as a balance. Measure 35 mL of Cushion Buffer, then add Ribosome Buffer until the balance mass is within 0.1 g of the sample bottle mass. **Make sure all bottles are well balanced (Δm ≤ 0.1 g) and have no cracks!**
- [ ]  Pellet ribosomes by ultracentrifugation at 100 000 rcf / 4C / 16 hrs. A translucent ribosome pellet will be formed at the bottom of the centrifuge bottle. It may be difficult to see.
- [ ]  Discard the supernatant. Carefully, wash each pellet with 0.5 mL cold ribosome buffer. Repeat this step twice.

::::{hint} Note: Don’t disturb the ribosome pellet during washing.
:class: dropdown
:icon: false

The ribosome pellet is fairly compact and stable, but some ribosomes can get resuspended during washing and be lost in the process. Be careful! 

First, find the pellet. Next, wash the pellet by gently pipetting Ribosome Buffer down the sides of the tube, allowing the buffer to run over the pellet. Tilt the ultracentrifuge bottle gently so that the buffer falls away from the pellet, aspirate the buffer, add fresh buffer as before, and repeat.
::::

- [ ]  Resuspend the clear pellets in 100 uL of Ribosome Buffer on ice using a magnetic stir bar (3 mm diameter, 10 mm length) on a magnetic stirrer set at the lowest possible speed. Collect resuspended ribosomes.
- [ ]  Wash tubes with an additional 50 uL of Ribosome Buffer to resuspend any remaining ribosomes.

## Quality Control

- [ ]  Determine the ribosome concentration by measuring the absorbance at 260 nm at a 100x dilution in Ribosome Buffer. 10 units of A260 from a 100x dilution corresponds to 23 uM of undiluted solution.
- [ ]  Dilute to final stock of 10 uM. To adjust the concentration, dilute the ribosomes with ribosome buffer or concentrate further via centrifugation at 4000 rcf in a 100 kDa centrifugal filter at 4C.
- [ ]  Protein gel: dilute 10 uM sample by 4x (Add 2.5 uL of sample with 7.5 uL water) and mix with 10 uL of 4x Laemmli with BME loading buffer. Boil samples at 90C for 10 minutes and load 5 uL and 2.5 uL onto 4-20% tris-glycine gel. Run gel at 200 V / 30-45 min or until the loading dye line reaches the bottom of the gel.

## Storage

- [ ] Aliquot your ribosomes to reduce freeze / thaw cycles and store at -80C.

# Downloads

:::::{card}
:header: **Resources**
::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**
{button}`download <protocol-make_ribosomes.pdf>`
:::

:::{card}
:header: **Bill of Materials**
{button}`download <protocol-Make_tRNAs.pdf>`
:::

::::
:::::