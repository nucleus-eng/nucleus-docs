---
title: Make Ribosomes
exports:
  - format: typst
    template: https://github.com/antonrmolina/nucleus-typst-test/archive/refs/heads/main.zip
    output: protocol-make_ribosomes.pdf
---

# Protocol

## Cell culture


- **Prepare overnight cultures.**
    - [ ] Add 5 mL Luria Broth (LB) under sterile conditions to two (2) 14 mL culture tubes.
    - [ ] Label one tube “(+)”. Add 10 uL of A19 glycerol stock to (+).
    - [ ] Label the other tube “(-)”. This will be your negative control, testing if your technique is sterile.
    - [ ] Incubate both tubes overnight shaking at 37C / (225-250) rpm / (12-16) hr.

- **Perform bulk outgrowth.**
    - [ ]  Check if (-) has growth. If not, continue.
    - [ ]  Back dilute overnight 1:250 - 1:1000 into 4x 450 mL fresh LB in 2 L baffled Erlenmeyer flasks (e.g., 1.8 mL overnight into 450 mL LB).
    - [ ]  Incubate back diluted cultures at 37C / (225-250) rpm to mid-log phase (OD600 between 0.6 and 0.8, typically ~3 hrs).

- **Pellet, wash, and store cells.**
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
        
:::{table}
:::

- **Set-up.**
    - [ ]  Connect the two Butyl column (5 mL) in tandem, totaling a column volume (CV) of 10 mL.
    - [ ]  Place A1 in Ribosome Wash Buffer and B1 in Ribosome Elution Buffer. Place sample line in A2. Set the default flow rate to 4 mL / min (except for pump washes: 10 mL/min).

- **Equilibrate HIC column.**
    - [ ]  Perform a pump wash with Ribosome Wash Buffer (without TCEP) and equilibrate the column with 4 CV of Ribosome Wash Buffer(without TCEP).
    - [ ]  Once you've equilibrated your columns, add TCEP to Ribosome Wash and Elution Buffer.
    - [ ]  Load your fraction collector with 15 mL conical tubes and set the fraction volume to 5 mL.
    - [ ]  If using a sample pump to load samples, place sample line (S1) into sample and load around 90% of sample volume onto the column. Once almost loaded, dilute the sample with Ribosome wash buffer (~5 mL) to load as much sample as possible. DO NOT allow air into the FPLC; make sure the sample line is always submerged.

- **Perform HIC**

    - [ ]  Wash step 1: wash with 3 CV of Ribosome Wash Buffer to remove unbound components .
    - [ ]  Wash step 2: wash with 5 CV of 80% Wash Buffer and 20% Ribosome Elution Buffer.
    - [ ]  Elution: elute the product by applying 3.5 CV (35 mL) of 50% Ribosome Wash Buffer and 50% Ribosome Elution Buffer. Ensure that the fraction collector captures these fractions separately.
    - [ ]  Wash step 3: Elute all strongly interacting contaminants with 5 CV of 100% Ribosome Elution Buffer.

- **Clean columns**
    - [ ]  Place inlet into a NaOH (0.5 M) and perform pump wash. Wash the column with 3 CV NaOH (0.5M).
    - [ ]  Place the inlet into water, perform pump wash, and then was column in 2 CV filtered Ultrapure water.
    - [ ]  Place the inlet into AcOH (0.1 M), perform pump wash, and subsequently wash column with 3 CV AcOH (0.1 M).
    - [ ]  Pump wash with water and wash column with 2 CV filtered MilliQ water.
    - [ ]  Place all inlets into EtOH (20% v/v). Perform a pump wash, then wash columns with 3 CV EtOH (20% v/v). Store columns at 4C in EtOH (20% v/v) until ready for use.

## Ultracentrifugation

- [ ]  Gently overlay recovered fractions (should correspond to second peak) onto 35 mL of Cushion Buffer in a polycarbonate ultracentrifuge bottle (70 mL).
- [ ]  Prepare another polycarbonate ultracentrifuge bottle as a balance. Measure 35 mL of Cushion Buffer, then add Ribosome Buffer until the balance mass is within 0.1 g of the sample bottle mass. **Make sure all bottles are well balanced (Δm ≤ 0.1 g) and have no cracks!**
- [ ]  Pellet ribosomes by ultracentrifugation at 100 000 rcf / 4C / 16 hrs. A translucent ribosome pellet will be formed at the bottom of the centrifuge bottle. It may be difficult to see.
- [ ]  Discard the supernatant. Carefully, wash each pellet with 0.5 mL cold ribosome buffer. Repeat this step twice.


- [ ]  Resuspend the clear pellets in 100 uL of Ribosome Buffer on ice using a magnetic stir bar (3 mm diameter, 10 mm length) on a magnetic stirrer set at the lowest possible speed. Collect resuspended ribosomes.
- [ ]  Wash tubes with an additional 50 uL of Ribosome Buffer to resuspend any remaining ribosomes.

## Quality Control

- [ ]  Determine the ribosome concentration by measuring the absorbance at 260 nm at a 100x dilution in Ribosome Buffer. 10 units of A260 from a 100x dilution corresponds to 23 uM of undiluted solution.
- [ ]  Dilute to final stock of 10 uM. To adjust the concentration, dilute the ribosomes with ribosome buffer or concentrate further via centrifugation at 4000 rcf in a 100 kDa centrifugal filter at 4C.
- [ ]  Protein gel: dilute 10 uM sample by 4x (Add 2.5 uL of sample with 7.5 uL water) and mix with 10 uL of 4x Laemmli with BME loading buffer. Boil samples at 90C for 10 minutes and load 5 uL and 2.5 uL onto 4-20% tris-glycine gel. Run gel at 200 V / 30-45 min or until the loading dye line reaches the bottom of the gel.

## Storage

- [ ] Aliquot your ribosomes to reduce freeze / thaw cycles and store at -80C.

