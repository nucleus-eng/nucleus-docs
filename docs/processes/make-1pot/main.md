---
title: "Make OnePot Protein Mix"
subtitle: "Process"
---

# Overview

Making PURE requires making Protein Mix, which contains the thirty-six (36) proteins in the PURE system. If you want to purify each protein individually, you can follow our [36-pot protocol](../make-36pot/main.md). However, if you want working protein mix with less time and effort, you can co-express and co-purify all 36 proteins at once in OnePot. This protocol shows you how. This protocol has been established to grow, purify, and characterize OnePot PURE proteins following [Lavickova’s OnePot PURE protocol](https://doi.org/10.3791/62625) with a few deviations. 

::::::{note} Genetically Encoded Components
:class: dropdown
:icon: false

All thirty-six PURE system expression constructs (pET28a backbone, T7 promoter, kanamycin resistance) are maintained in the Nucleus DNA repository:

- [nucleus-eng/DNA/PURE/expression/](https://github.com/nucleus-eng/DNA/tree/main/PURE/expression)

::::::

::::::{note} Composition
:class: dropdown
:icon: false

| **Component** | **Stock Concentration** | **Reaction Concentration** |
| --- | --- | --- |
| OnePot Protein Mix | 15 mg/mL | 2.4 mg/mL |

::::::

# Protocol

*E. coli* BL21(DE3) was used as the expression strain for all 36 PURE proteins in this protocol.

## Starter Plate Preparation

- [ ] Prepare a OnePot PURE starter plate containing each of the 36 strains, stored as 25% glycerol stocks at an OD₆₀₀ of 0.5. Each well of the starter glycerol stock plate should contain 40 µL of the corresponding strain at OD₆₀₀ = 0.5 and be stored at −80 °C.

:::{figure} ./platemap.jpg
:label: fig:OnePotPURE-platemap
:width: 75%
Plate layout of 40 µL PCR plate aliquots for the Nucleus OnePot PURE protocol.
:::


## Buffer Preparation

The following stock buffers are required for preparing the working buffers used in PURE production. At this stage, the solutions are not pH-adjusted, as pH adjustment will be performed during preparation of the working buffers (see below).

### 1M HEPES (250 mL)

- [ ] Dissolve 59.6 g HEPES (MW 238.3 g/mol) in 200 mL dH₂O.
- [ ] Adjust to a final volume of 250 mL.
- [ ] Sterilize by autoclaving or filter sterilization.
- [ ] Store at 4 °C with the bottle wrapped in foil to protect from light. Avoid storing HEPES for longer than one week; prepare only the amount required for the intended number of preparations.

### 1M Magnesium Chloride (250mL)

- [ ] Dissolve 23.8 g MgCl₂ (MW 95.21 g/mol) in 200 mL dH₂O.
- [ ] Adjust to a final volume of 250 mL.
- [ ] Sterilize by autoclaving or filter sterilization.
- [ ] Store at 4 °C for up to 6 months.

### 2M Potassium Chloride (250 mL)

- [ ] Dissolve 37.3 g KCl (MW 74.55 g/mol) in 200 mL dH₂O.
- [ ] Adjust to a final volume of 250 mL.
- [ ] Sterilize by autoclaving or filter sterilization.
- [ ] Store at 4 °C for up to 6 months.

Following are the working buffers required for PURE protein production:

### Buffer A (1 L)

- [ ] Add 53.5 g NH₄Cl to a 1 L Duran bottle and dissolve in 500 mL dH₂O.
- [ ] Add 50 mL of 1 M HEPES.
- [ ] Add 10 mL of 1 M MgCl₂.
- [ ] Bring the volume up to 1 L with dH₂O.
- [ ] Adjust pH to ~7.6 using KOH pellets.
- [ ] Filter sterilize.
- [ ] Store at 4 °C, wrapped in foil to protect from light; suitable for multiple preparations.

### Buffer B (500 mL)

- [ ] Add 17 g imidazole to a 500 mL Duran bottle and dissolve in 300 mL dH₂O.
- [ ] Add 25 mL of 1 M HEPES.
- [ ] Add 5 mL of 1 M MgCl₂.
- [ ] Add 25 mL of 2 M KCl.
- [ ] Bring the volume to 490 mL with dH₂O.
- [ ] Adjust pH to ~7.6 using HCl.
- [ ] Bring the final volume to 500 mL with dH₂O.
- [ ] Filter sterilize.
- [ ] Store at 4 °C, wrapped in foil to protect from light; suitable for multiple preparations.

### Buffer HT (2 L)

- [ ] Use a sterile 2 L Duran bottle and sterile (filtered) HEPES, MgCl₂, KCl, and water to avoid the need for filter sterilization.
- [ ] Add 100 mL of 1 M HEPES.
- [ ] Add 20 mL of 1 M MgCl₂.
- [ ] Add 100 mL of 2 M KCl.
- [ ] Add 1780 mL sterile dH₂O.
- [ ] Store at 4 °C, wrapped in foil to protect from light; suitable for multiple preparations.

### Stock 60 (100 mL)

- [ ] Add 5 mL of 1 M HEPES (filtered) to a sterile 100 mL Duran bottle.
- [ ] Add 1 mL of 1 M MgCl₂ (filtered).
- [ ] Add 5 mL of 2 M KCl (filtered).
- [ ] Add 60 mL of 100% sterile glycerol.
- [ ] Add 29 mL sterile dH₂O.
- [ ] Store at 4 °C, wrapped in foil to protect from light; suitable for multiple preparations.
- [ ] Prepare Stock 30 using Stock 60 before adding any reducing agent to Stock 60.

### Stock 30 (50 mL)

- [ ] Add 25 mL of filtered Buffer HT (without reducing agent) to a sterile 100 mL Duran bottle.
- [ ] Add 25 mL of filtered Stock 60 (without reducing agent).
- [ ] Store at 4 °C, wrapped in foil to protect from light; suitable for multiple preparations.

## Procedure

A single OnePot PURE system preparation requires processing 500 mL of liquid culture. It is recommended to process two 500 mL cultures simultaneously to generate two independent PURE batches in a single run. These can be quantified separately and combined if their activity levels are comparable.

This protocol processes two 500 mL OnePot PURE cultures, yielding ~600 µL purified PURE proteins per batch. The final stock concentration is 15 mg/mL.


### Day 1: Starter Culture

- [ ] Starter culture incubation needs to begin at 6 pm. As such begin subsequent steps at 5 pm to allow sufficient time to start incubation at 6pm. 
- [ ] Thaw a PURE Starter Plate on ice. This starter plate contains each of the 36 strains frozen in 25% glycerol at OD 0.5.
- [ ] Add 50 µL 1000X Kanamycin (50 mg/mL) to 50 mL of sterile LB in a sterile falcon tube.
- [ ] Label 1.5 mL sterile tubes from 1 to 36 (except number 25) and add 1 mL of LB+KAN to each tube.
- [ ] Add 10 µL of each of the 36 glycerol stocks (except number 25) to the corresponding labeled tubes and mix well by vortexing.
- [ ] Add 300 µL of innoculated cuture from each tube into the corresponding well of a sterile 96 deep well plate. Seal the plate using a Breath-easy sealing membrane. 
- [ ] Innoculate 3 mL of LB+KAN in 15 mL falcon tubes with 10 µL of EF-Tu glycerol stock. Do this in duplicate.
- [ ] Incubate deep well culture plate and 15 mL falcon tubes at 260 RPM 37°C for 16 hours.
- [ ] Start incubation at 6pm. Check OD₆₀₀ at 10 am the next day (16 hours incubation).
- [ ] Place 1.5 L of sterile LB in 37°C static incubator to prewarm overnight.

### Day 2: Main Growth

- [ ] The next day, measure the OD₆₀₀ of the starter plate using a 96 well plate by adding 30 µL of each starter  to the bottom of each well and 270 µL of LB+KAN on top (10X dilution). Measure EF-Tu culture density at this time too. Expected OD₆₀₀ with 10X dilution is 0.2 - 0.3.
- [ ] After 16 hours of incubation, all strains should be at OD 2-3. If a strain is growing very slowly, remove the starter volume from the 96-deep well plate and place it into a 2 mL sterile tube, and shake at 260 RPM 37°C independently until desired OD is reached. The remaining starters can be left in the deep well plate on the bench. If a starter has overgrown above OD₆₀₀, dilute the starters to OD₆₀₀ = 3 using LB+KAN in a sterile tube.
- [ ] Once all starter strains have been equilibrated to OD₆₀₀ 2-3, proceed to main growth by adding 500 mL of prewarmed LB+KAN into a 2.5 L baffled flask (2X flasks).
- [ ] Into a sterile 5 mL tube add 55 µL of each starter culture (excluding EF-Tu), and 1675 µL of EF-Tu starter culture. Mix well by vortexing and add entire content to 500 mL of LB+KAN in 2.5 L baffled flask. Repeat for the second culture flask.
- [ ] Incubate the cultures at 37°C 260 RPM for 1.5 to 2 hours (until OD₆₀₀ reaches 0.2 - 0.3). Check OD after 1 hour as baffled flask may cause cells to grow faster.
- [ ] Once OD₆₀₀ of 0.2- 0.3 is reached, innoculate each culture flask with 500 µL of 100 mM IPTG to achieve a final induction concentration of 0.1 mM IPTG.
- [ ] Incubate cultures for a further 3 hours at 37°C 260 RPM.
- [ ] During incubation periods of main growth, prepare protein purification buffers as described below and store at 4°C until use. Don't add TCEP at this point.

:::{table} Protein Purification Buffers
:label: protein-buffers
:align: center
:width: 75%

| Buffer Type | Buffer A (mL) | Buffer B (mL) | Total (mL) | 0.5 M TCEP (µL) |
| --- | --- | --- | --- | --- |
| Resuspension/Equilibration Buffer | 200 | 0 | 200 | 400 |
| Wash Buffer  | 99 | 1 | 100 | 200 |
| Elution Buffer | 2 | 18 | 20 | 40 |  
:::

- [ ] 15 minutes before the end of the incubation, cool table top centrifuge to 4°C and prepare an ice bucket and cool centrifuge bottles.
- [ ] At the end of the 3 hour incubation, place baffled flask into ice bucket and remove samples for OD₆₀₀ measurement. Final expected OD₆₀₀ is 2-3.
- [ ] Fill each centrifuge bottle with 500 mL of culture from each flask and spin at 5000g, 4°C, 15 minutes and discard supernatant.
- [ ] Add 20 mL of sterile LB into each bottle and resuspend the cell pellet thoroughly and move resuspension into labelled sterile 50 mL falcon tubes.
- [ ] Centrifuge the Falcon tubes at 4°C, 2000g for 8 minutes, remove the supernatant by decanting.
- [ ] Centrifuge Falcon tubes at 4°C, 2000g again for 2 minutes, remove residual supernatant by pipetting.
- [ ] The pellets can be flash frozen in liquid nitrogen and stored at -80 °C for up to 3 days until protein purification.

### Day 3: Protein Purification

- [ ] Thaw cell pellets on ice.
- [ ] Add 2 mL of fresh cOmplete resin to chromotography column. Wash column with 30 mL dH20 twice to remove ethanol.
- [ ] Add TCEP to Resuspension/Equilibration buffer to a final concentration of 1 mM (see {ref}`protein-buffers`).
- [ ] Equilibrate column with 30 mL of Resuspension/Equilibration buffer+TCEP and close vavle on the column with 5 mL of buffer remaining in the column.
- [ ] Add 7.5 mL of Resuspension/Equilibration buffer+TCEP to each falcon tube containing cell pellet and resuspend thorougly and store on ice.
- [ ] Lyse cells via sonication at 70% amplitude, 10s on 10s off with 2000 J of energy in a ice water bath. Use a clamp stand to hold the falcon tube in place such that the cell suspension is submerged in the ice water bath and place the probe deep enough into the solution without touching the tube. If a large amount of foam is generated, the energy transfer will be damped. In that case, let the foam settle, lower the probe deeper into the solution, and extend the sonication time. If sonication is successful, the solution will turn darker.
- [ ] Aliquot the sonicated sample in 2 mL tubes (1 mL per tube) and spin at 15923g, 4°C, 20 minutes.
- [ ] Collate all clarified pellet free supernatant into a fresh 50 mL falcon tube on ice.
- [ ] Resuspend the resin in the remaining 5 mL of Resuspension/Equilibration buffer+TCEP within the column and collate buffer+resin into falcon tube containing supernatant. Seal the lid with parafilm and incubate in a rotisseriie shaker at 4°C for a minimum of 3 hours.
- [ ] After incubation of sample with resin, briefly spin the falcon tubes in a table top centrifuge using pulse mode to collate the resin to the bottom of the tube.
- [ ] Resuspend the sample with resin using a pipette and add the mixture back into the protein purification column.
- [ ] Label three 15 mL falcon tubes as 'flow through', 'wash' and 'elution', respectively. Replicate as required for the number of purifications you are doing.
- [ ] Add TCEP at a final concentration of 1 mM to wash and elution buffers (see {ref}`protein-buffers`) and store at 4°C until use.
- [ ] Once the resin has settled into a bed at the bottom of the column, let the buffer run through and collect samples from the middle of the flow through into 15 mL falcon tube labelled 'flow through'.
- [ ] Wash column with wash buffer+TCEP and collect flow through in 15 mL falcon tube labelled 'wash'.
- [ ] Add 5 mL elution buffer+TCEP into the column and resuspend the resin a few times with pipette and incubate for 10 minutes before elution into tube labelled 'elution'. During this incubation, add 1 L of Buffer HT into a 1L beaker and soak 2kDA dialysis cassette in buffer with magnetic stirir in cold room/fridge.
- [ ] Store eluted protein on ice.
- [ ] Remove dialysis cassette from beaker and add 5 mL of eluted protein into the dialysis casssette. Remove as much air as possible from cassette before putting the lid back on. Dialyse according to protocol stated below to remove imidazole. 5 mL of eluted protein is dialysed against 1L of buffer HT (without TCEP) for 12 hours/overnight at 4°C. In instances when elutions can be combined, 10 mL of elution can be dialysed against 2L of buffer HT.

### Day 4: Protein Concentration

- [ ] After dialysis is complete, remove dialysed sample from cassette and add to a 3K MWCO Amicon Ultra 15 and top up volume with 10 mL of fresh buffer HT+TCEP.
- [ ] Spin at 3220 g for 60 mins at 4°C. The sample volume will reduce down to 1.5 mL.
- [ ] Remove sample from amicon tube and split into 2 mL sterile tubes in 500 µL aliquots. Spin to pellet any precipitated proteins at 14,000g for 10 minutes at 4°C.
- [ ] Collate pellet free supernantant into a fresh 1.5 mL tube on ice.
- [ ] Add TCEP to a 1 mL aliquot of Stock-60 to achieve a final concentration of 1 mM.
- [ ] Add equal volume of Stock-60+TCEP to collated sample. Proceed to determine protein concentration using [Pierce660 Assay](../pierce660/main.md) in triplicate with a calibration curve spanning 0 - 2 mg/mL.
- [ ] Concentrate protein down using 0.5 mL 3K amicon columns and spin at 14862g for 15 minutes at 4°C until desired volume is reached to obtain a final concentration of 15 mg/mL. 
- [ ] Spin to pellet any precipitated proteins at 14,000g for 10 minutes at 4°C.
- [ ] Determine final protein concentration using [Pierce660 Assay](../pierce660/main.md) and dilute samples with Stock 30+TCEP as required to reach correct final concentration of 15 mg/mL.
- [ ] Aliquot 50 µL into PCR tubes, snap freeze using liquid nitrogen, and store at -80°C.

# Downloads

::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**
{button}`download <generated/make-1pot-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**
{button}`download <generated/bom-1onepot.pdf>`
:::

::::