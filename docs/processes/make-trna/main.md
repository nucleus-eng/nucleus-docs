---
title: "Make tRNAs"
subtitle: "Process"
---

# Overview

Transfer RNAs (tRNAs) are small RNA molecules (76 - 90) nt that carry amino acids to ribosomes during protein synthesis. They are essential for translation and can be easily purified following this protocol, which covers bacterial growth, purification, dialysis, and quality assurance. You can use these tRNAs in Make Energy Mix.


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

- **Acid Phenol**
    - Corrosive, toxic, rapidly absorbed through skin, & respiratory irritant
    - Use in fume hood, wear neoprene gloves, & PPE

- **Acetic Acid**
    - Corrosive to skin and eyes
    - Use appropriate PPE and handle under fume-hood

- **Chloroform**
    - Irritant, possible carcinogen
    - Work in fume hood & appropriate gloves

- **Ethanol**
    - Highly flammable, toxic, and irritant
    - Wear PPE, use in well-ventilated areas, and keep away from open flames

::::::

::::::{attention} Critical Materials
:class: dropdown
:icon: false

- None

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
:label: tbl:composition-table
:align: center

| **Component** | **Stock Concentration** | **Reaction Concentration** |
| --- | --- | --- |
| tRNA | 35 $\mu$g/$\mu$L (10x) | 3.5 $\mu$g/$\mu$L |

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

:::{tip} Note: you can work from glycerol stocks OR colonies.
:class: dropdown
We first need to prepare bacterial cultures. We will work from 6 mL overnight cultures of our expression strains and backdilute them the next day. In order to prepare these overnight cultures, we need stocks of bacteria.

We worked from 100 uL aliquots of our glycerol stocks, frozen in PCR strip tubes. When seeding our overnights with bacteria, we poked one glycerol aliquot with a pipette tip and ejected the tip into culture tubes (more details below).

Optionally, you can work from individual colonies by streaking out your bacterial stocks. Working from colonies assures that your bulk outgrowth will have come from a single colony forming unit.
:::

**Prepare overnight cultures.**
  - [ ]  Add 6 mL Luria Broth (LB) under sterile conditions to two (2) 14 mL culture tubes. 6 mL is enough to inoculate 4 x 900 mL bulk outgrowths.
  - [ ]  Label one tube “(+)”. Add 10 uL of A19 glycerol stock to (+).
  - [ ]  Label the other tube “(-)”. This will be your negative control, testing if your technique is sterile.
  - [ ]  Incubate both tubes overnight shaking at 37C / (225 - 250) rpm / (10 - 16) hr.

**Perform bulk outgrowth.**
  - [ ]  Check if (-) has growth. If not, continue.
  - [ ]  Back dilute overnight 1:500 - 1:1000 into 4x 900 mL fresh LB in 2 L baffled Erlenmeyer flasks (e.g., 900 uL overnight into 900 mL LB).
  - [ ]  Incubate back diluted cultures at 37C / (225-250) rpm to mid-log phase (OD600 between 0.6 and 0.8). This took us ~3 hrs.

**Pellet, wash, and store cells.**
  - [ ]  Fill 500 mL centrifuge bottles with culture. Balance centrifuge bottles against each other and centrifuge cultures at 16 000 rcf / 4C / 10 min.
  - [ ]  Decant supernatant, add fresh culture, and repeat centrifugation as above, working through the remaining culture. You should end up with large pellets at the bottom of each centrifuge bottle.
  - [ ]  Wash the pellets by resuspending in 500 mL cold (4C) NaCl (0.9%) then re-pelleting at 16 000 rcf / 4C / 10 min.
  - [ ]  Transfer pellets by spatula into a tared bag weigh and record the mass.
  - [ ]  Flash freeze pellet in liquid nitrogen and store at -80C.

## Nucleus acid extraction by precipitation

**First Nucleic Acid Extraction:**
  - [ ]  Set centrifuge to 4C and set shaking incubator to 37C.
  - [ ]  Resuspend 2 g of biomass into 18 mL of Extraction Buffer: NaOAc (50 mM), Mg(OAc)2 (10 mM), pH 5.0 in a 50 mL centrifuge tube by vortexing.
  - [ ]  Add 18 mL of Acid Phenol (pH 4.5) using a glass serological pipette in a fume hood.
  - [ ]  Cap the 50 mL centrifuge tube and seal with parafilm to prevent spillage.
  - [ ]  Incubate at 37C / 225 rpm / 30 min in a shaking incubator. Tape tubes against the bottom plate of the shaking incubator horizontally so that samples are shaking laterally.
  - [ ]  Centrifuge at 4000 rcf / 4C / 15 min. You should observe three (3) layers: the aqueous (top) fraction, the organic (lower) fraction, and a middle fraction of cell debris separating them.
  - [ ]  Carefully collect the aqueous fraction by serological pipette, without disturbing the cell debris fraction, and transfer to a fresh 50 mL centrifuge tube.

**Second Nucleic Acid Extraction:**
  - [ ]  Add 14 mL of Extraction Buffer to Acid Phenol, parafilm the 50 mL centrifuge tube, and incubate at 37C / 225 rpm / 15 min.
  - [ ]  Centrifuge at 4000 rcf / 4C / 15 min.
  - [ ]  Collect the aqueous fraction and combine with the first nucleic acid extraction (total volume between 30 mL and 32 mL).

**Phenol Clean-up:**
  - [ ]  Split aqueous layer into 2x 50 mL centrifuge tubes and add one volume chloroform (~16 mL) to each tube using a glass serological pipette. Vortex for 5 minutes at RT.
  - [ ]  Centrifuge at 4000 rcf  / 4C /  15 min. You should see two (2) fractions: the aqueous (top) fraction and the organic (lower) fraction. The aqueous fraction should be more clear after washing with chloroform.
  - [ ]  Collect the aqueous fraction and transfer to a fresh 50 mL centrifuge tube.

**Precipitate Nucleic Acids (RNA & DNA):**
  - [ ]  Set centrifuge to 25C.
  - [ ]  Add NaCl (5 M) to the aqueous phase to a final concentration of 0.2 M (~1.5 mL). Mix by inversion and split evenly into 2x 50 mL centrifuge tubes.
  - [ ]  Precipitate nucleic acids by adding one volume of isopropanol (~17 mL) to each tube and incubate at RT for 10 min. The mixture should turn cloudy.
  - [ ]  Pellet nucleic acid precipitate via centrifugation at 14 500 rcf / 25C / 15 min.
  - [ ]  Wash the pellet with EtOH (70%):
      - [ ]  Decant supernatant and wash nucleic acid pellet with 10 mL cold (-20C) EtOH (70%).
      - [ ]  Re-pellet nucleic acid pellet by centrifugation at 14 500 rcf / 25C / 5 min.
      - [ ]  Decant the supernatant and allow the pellet to air dry for 10 minutes.

**Remove rRNA by precipitation:**
  - [ ]  Resuspend each pellet into 15 mL of cold (4C) NaCl (1 M) by vortexing or pipetting. Ensure the pellet is fully dissolved. Allow NaCl (1 M) solution to hydrate pellet for ~(10 - 15) min at RT to help the pellet dissolve.
  - [ ]  Precipitate rRNA by centrifugation at 9500 / 4C / 20 min.
  - [ ]  Decant the supernatant to a new 50 mL centrifuge tube.

- **Precipitate remaining DNA and tRNA nucleic acids:**
    - [ ]  Add 2 volumes (~30 mL) of cold (-20C) EtOH (100%) to the supernatant and incubate at -20C / >30 min to precipitate remaining nucleic acids. You can perform this step overnight.
    - [ ]  Centrifuge at 14 500 rcf / 4C / 5 min.
    - [ ]  Wash the pellet with EtOH (70%) as above.

- **Remove DNA by precipitation:**
    - [ ]  Set centrifuge to 25C.
    - [ ]  Dissolve the pellet in 6 mL of NaOAc (300 mM, pH 5.0). As needed to ensure the pellet is fully dissolved, heat samples up to 60C, pipette mix, and/or vortex. If the pellet is visibly small, you can dissolve each pellet in 3 mL of NaOAc (0.3 M, pH 5.0) and pool together, totaling 6 mL.
    - [ ]  Add 0.56 volumes of isopropanol (~3.4 mL) to each nucleic acid solution and incubate at RT / 10 min.
    - [ ]  Centrifuge at 14 500 rcf / RT / 5 min. Decant the supernatant to a 15 mL centrifuge tube.

- **Precipitate tRNAs:**
    - [ ]  Set the centrifuge to 4C.
    - [ ]  Add 2.3 mL of isopropanol to the supernatant (supernatant:isopropanol is 100:95) and incubate at -20C / >30 min. This step can be performed overnight.
    - [ ]  Centrifuge the suspension at 14 500 rcf / 4C / 15 min.
    - [ ]  Wash the pellet with EtOH (70%) as above.
    - [ ]  Resuspend tRNA pellet in 1.5 mL of nuclease-free water and keep on ice.

## Dialysis

  - [ ]  Hydrate membrane: Remove the cassette from its protective pouch and hydrate the membrane by immersing the cassette in nuclease-free water for 2 minutes.
  - [ ]  Add Sample:
      - [ ]  Open the cassette by twisting the cap counter-clockwise (~45 degrees) and pull out the cap.
      - [ ]  Carefully pipette 1.5 mL of resuspended tRNAs into the cassette without puncturing the membrane.
      - [ ]  Remove the excess air in the cassette by simultaneously pressing the membrane gently on both sides and inserting the cap and locking it into place.
  - [ ]  Dialyze Sample:
      - [ ]  Float cassette in 500 mL nuclease-free water in a large (>600 mL) beaker and gently stir at 4C / 45 min. We do this by putting our beaker in a bucket of ice on a stir plate.
      - [ ]  Change the dialysis buffer and dialyze for another 45 minutes.

:::{tip} Note: you can dialyze overnight.
:class: dropdown
Dialysis can be done overnight after changing the dialysis buffer at least once. The manufacturer of Slide-A-Lyzer chips recommends dialyzing for 2 hours, then changing the buffer and dialyzing for another two hours. We have found 2 x 45 min sufficient. 

For more detailed instructions on using the Slide-A-Lyzer, please look at manufacturer’s [manual](https://assets.thermofisher.com/TFS-Assets/LSG/manuals/MAN0027985-SAL-G3-Cassettes-UG-EN.pdf).
:::

## Concentrate

  - [ ]  Pipette dialyzed tRNAs to the upper chamber of an Amicon® Ultra-0.5 mL Centrifugal Filter, 3 kDa MWCO.
  - [ ]  Centrifuge at 14 000 rcf / 10 min and check the remaining volume in the upper chamber. Repeat until you hit your target volume.

:::{tip} Note: estimate your target volume at 100 uL per 1 g biomass.
:class: dropdown
From our experience, a good rule of thumb is to target a final volume around 100 uL per 1g of biomass used (e.g., 3.6 gDCM → concentrate to ~360 uL (~40 ug/uL tRNAs)).
:::

## Quality control

**Estimate concentration by UV-Vis Spectroscopy (Nanodrop).**
  - [ ]  Prepare a 1:1000 dilution of your tRNAs in water.
  - [ ]  Measure absorbance at 260 nm, 280 nm, and 230 nm.
  - [ ]  Estimate your yield by A260 ([tRNA] = A260 * 40 mg/mL). Typical yield of tRNA is ~ (4-20) mg per gram of cell mass.
  - [ ] Estimate your purity by A260/A230 and A260/A280 (both should be ≥1.8).

:::{tip} Note: [tRNA] = A260 * 40 mg / mL
:class: dropdown
A260 units (*a.k.a.* “absorbance units”, or “OD260”) are defined as the amount of light (wavelength = 260 nm) absorbed by a sample resuspended in 1 mL of water as said light passes through 1 cm of said sample. 

Typically, this value is measured by diluting a sample until it’s absorbance is in the linear range (0.5 is acceptable), then multiplying the measured absorbance by the dilution factor.

These units are annoying to design experiments around, but easy to measure. If you want to report mass concentration of your samples instead, you can approximate as ~40 mg/mL per A260 unit of tRNA.

NEB has a great [tool](https://nebiocalculator.neb.com/#!/od260) for converting absorbance units to concentrations. Make sure to select “ssRNA”
:::

**Visualize purity by TBE-Urea 10% Gel.**
  - [ ]  (optional) Prepare TBE-Urea 10% Gel
      - [ ]  Load gel into gel dock with running buffer.
      - [ ]  Pre-run gels at 100 V / 30 min.
      - [ ]  Wash wells with running buffer by syringe. You should be able to see urea displaced from the well by change in refractive index.
  - [ ]  Prepare tRNA samples:
      - [ ]  Dilute tRNAs to 40 ng / uL tRNA in nuclease-free water.
      - [ ]  Prepare 20 ng / uL sample by adding 10 uL of 40 ng / uL tRNA to 10 uL 2x TBE-Urea sample buffer.
      - [ ]  Prepare an ssRNA ladder. We use the NEB low range ssRNA (2 uL ladder + 2 uL 2x sample buffer).
      - [ ]  Incubate sample and and ladder at 65C / 3 min → 4C / hold using a thermal cycler.
  - [ ]  Load 200 ng of tRNA (10 uL at 20 ng / uL) onto the TBE-Urea gel and run at 125V / 2.5 hr.
  - [ ]  Meanwhile, prepare SYBR-Green stain (4 uL in 40 mL water) to stain gel.
  - [ ]  Soak gel in SYBR-Green stain and visualize gel using UV or blue-light transilluminator. You should see multiple distinct bands around 75-90 nt.

:::{tip} Note: RNases digesting your tRNA → smear on gel
:class: dropdown
If your sample is contaminated with RNases, your sample quality will decrease as the RNases degrade the tRNAs. A clear sign of tRNA degradation are poorly defined, smeared bands. A clean tRNA prep should have distinct bands.

If your samples appear as a smear on your gel, consider testing your input buffers and final prep for RNase activity (see below).
:::

**(Optional) Measure RNase contamination using Ambion RNaseAlert Lab Test Kit.**
- [ ] We recommend diluting your tRNAs by adding 2 uL to 40 uL of provided sample buffer. 

## Formulation

  - [ ] Dilute your tRNA stocks in nuclease-free water to your working concentration, depending on your application. We recommend 50 ug / uL to use as a component in Energy Mix, or 35 ug / uL as a 10x stock for PUREΔtRNA reactions (add 1 uL to 10 uL reactions).

## Storage

  - [ ] Aliquot your tRNAs to reduce freeze / thaw cycles and store at -80C.

# Downloads

:::::{card}
:header: **Resources**
::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**
{button}`download <protocol-make_trnas.pdf>`
:::

:::{card}
:header: **Bill of Materials**
{button}`download <protocol-Make_tRNAs.pdf>`
:::

::::
:::::