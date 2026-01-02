---
title: Make Template
exports:
  - format: typst
    template: https://github.com/antonrmolina/nucleus-typst-test/archive/refs/heads/main.zip
    output: protocol-make_template.pdf
---

# Protocol

## Cell culture


- **Prepare overnight cultures.**
    - [ ]  Add 6 mL Luria Broth (LB) under sterile conditions to two (2) 14 mL culture tubes. 6 mL is enough to innoculate 4 x 900 mL bulk outgrowths.
    - [ ]  Label one tube “(+)”. Add 10 uL of A19 glycerol stock to (+).
    - [ ]  Label the other tube “(-)”. This will be your negative control, testing if your technique is sterile.
    - [ ]  Incubate both tubes overnight shaking at 37C / (225 - 250) rpm / (10 - 16) hr.

- **Perform bulk outgrowth.**
    - [ ]  Check if (-) has growth. If not, continue.
    - [ ]  Back dilute overnight 1:500 - 1:1000 into 4x 900 mL fresh LB in 2 L baffled Erlenmeyer flasks (e.g., 900 uL overnight into 900 mL LB).
    - [ ]  Incubate back diluted cultures at 37C / (225-250) rpm to mid-log phase (OD600 between 0.6 and 0.8). This took us ~3 hrs.

- **Pellet, wash, and store cells.**
    - [ ]  Fill 500 mL centrifuge bottles with culture. Balance centrifuge bottles against each other and centrifuge cultures at 16 000 rcf / 4C / 10 min.
    - [ ]  Decant supernatant, add fresh culture, and repeat centrifugation as above, working through the remaining culture. You should end up with large pellets at the bottom of each centrifuge bottle.
    - [ ]  Wash the pellets by resuspending in 500 mL cold (4C) NaCl (0.9%) then re-pelleting at 16 000 rcf / 4C / 10 min.
    - [ ]  Transfer pellets by spatula into a tared bag weigh and record the mass.
    - [ ]  Flash freeze pellet in liquid nitrogen and store at -80C.

## Nucleus acid extraction by precipitation

- **First Nucleic Acid Extraction:**
    - [ ]  Set centrifuge to 4C and set shaking incubator to 37C.
    - [ ]  Resuspend 2 g of biomass into 18 mL of Extraction Buffer: NaOAc (50 mM), Mg(OAc)2 (10 mM), pH 5.0 in a 50 mL centrifuge tube by vortexing.
    - [ ]  Add 18 mL of Acid Phenol (pH 4.5) using a glass serological pipette in a fume hood.
    - [ ]  Cap the 50 mL centrifuge tube and seal with parafilm to prevent spillage.
    - [ ]  Incubate at 37C / 225 rpm / 30 min in a shaking incubator. Tape tubes against the bottom plate of the shaking incubator horizontally so that samples are shaking laterally.
    - [ ]  Centrifuge at 4000 rcf / 4C / 15 min. You should observe three (3) layers: the aqueous (top) fraction, the organic (lower) fraction, and a middle fraction of cell debris separating them.
    - [ ]  Carefully collect the aqueous fraction by serological pipette, without disturbing the cell debris fraction, and transfer to a fresh 50 mL centrifuge tube.

- **Second Nucleic Acid Extraction:**
    - [ ]  Add 14 mL of Extraction Buffer to Acid Phenol, parafilm the 50 mL centrifuge tube, and incubate at 37C / 225 rpm / 15 min.
    - [ ]  Centrifuge at 4000 rcf / 4C / 15 min.
    - [ ]  Collect the aqueous fraction and combine with the first nucleic acid extraction (total volume between 30 mL and 32 mL).

- **Phenol Clean-up:**
    - [ ]  Split aqueous layer into 2x 50 mL centrifuge tubes and add one volume chloroform (~16 mL) to each tube using a glass serological pipette. Vortex for 5 minutes at RT.
    - [ ]  Centrifuge at 4000 rcf  / 4C /  15 min. You should see two (2) fractions: the aqueous (top) fraction and the organic (lower) fraction. The aqueous fraction should be more clear after washing with chloroform.
    - [ ]  Collect the aqueous fraction and transfer to a fresh 50 mL centrifuge tube.

- **Precipitate Nucleic Acids (RNA & DNA):**
    - [ ]  Set centrifuge to 25C.
    - [ ]  Add NaCl (5 M) to the aqueous phase to a final concentration of 0.2 M (~1.5 mL). Mix by inversion and split evenly into 2x 50 mL centrifuge tubes.
    - [ ]  Precipitate nucleic acids by adding one volume of isopropanol (~17 mL) to each tube and incubate at RT for 10 min. The mixture should turn cloudy.
    - [ ]  Pellet nucleic acid precipitate via centrifugation at 14 500 rcf / 25C / 15 min.
    - [ ]  Wash the pellet with EtOH (70%):
        - [ ]  Decant supernatant and wash nucleic acid pellet with 10 mL cold (-20C) EtOH (70%).
        - [ ]  Re-pellet nucleic acid pellet by centrifugation at 14 500 rcf / 25C / 5 min.
        - [ ]  Decant the supernatant and allow the pellet to air dry for 10 minutes.

- **Remove rRNA by precipitation:**
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


## Concentrate

- [ ]  Pipette dialyzed tRNAs to the upper chamber of an Amicon® Ultra-0.5 mL Centrifugal Filter, 3 kDa MWCO.
- [ ]  Centrifuge at 14 000 rcf / 10 min and check the remaining volume in the upper chamber. Repeat until you hit your target volume.


## Quality control

- **Estimate concentration by UV-Vis Spectroscopy (Nanodrop).**
    - [ ]  Prepare a 1:1000 dilution of your tRNAs in water.
    - [ ]  Measure absorbance at 260 nm, 280 nm, and 230 nm.
    - [ ]  Estimate your yield by A260 ([tRNA] = A260 * 40 mg/mL). Typical yield of tRNA is ~ (4-20) mg per gram of cell mass.
    - [ ] Estimate your purity by A260/A230 and A260/A280 (both should be ≥1.8).


- **Visualize purity by TBE-Urea 10% Gel.**
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


- **(Optional) Measure RNase contamination using Ambion RNaseAlert Lab Test Kit.**
    - [ ] We recommend diluting your tRNAs by adding 2 uL to 40 uL of provided sample buffer. 

## Formulation

- [ ] Dilute your tRNA stocks in nuclease-free water to your working concentration, depending on your application. We recommend 50 ug / uL to use as a component in Energy Mix, or 35 ug / uL as a 10x stock for PUREΔtRNA reactions (add 1 uL to 10 uL reactions).

## Storage

- [ ] Aliquot your tRNAs to reduce freeze / thaw cycles and store at -80C.

