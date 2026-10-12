---
title: "Detector: tetR-aTc"
subtitle: "Module Specification"
status: validated-published
thumbnail: mechanism-schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The TetR inducible expression module is a set of two genetic constructs that encode tetracycline-inducible gene expression: `pT7-tetR`, encoding the TetR repressor protein, and `pT7-tetO-plamGFP`, encoding a reporter gene under an inducible T7 promoter.

`pT7-tetO-plamGFP` constitutively expresses the open reporter plamGFP in the absence of repressor protein. The inducible promoter is also a MoClo Level 0 'P' part and may be assembled into a Level 1 transcription unit with other MoClo-compatible genes. Addition of TetR protein — either as a purified protein or via constitutive expression of `pT7-tetR` — inhibits expression through steric occlusion of the tetO operator site. Addition of anhydrotetracycline (aTc) causes allosteric release of TetR from tetO, recovering expression. aTc is membrane-permeable.

:::{figure} mechanism-schematic.png
Schematic of the TetR inducible expression module. TetR represses expression from `pT7-tetO-plamGFP`; aTc relieves repression by binding TetR and causing its release from the tetO operator.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA
:::{table}
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-tetR` | 2877 | [pOpen-tetR.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/pOpen-tetR.gb) |
| `pT7-tetO-plamGFP` | 2954 | [pOpen-pT7-tetO.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/pOpen-pT7-tetO.gb) |
:::

:::{attention} `pOpen-TetO-deGFP` is not in `nucleus-eng/DNA`
The titration and GUV results below use `pOpen-TetO-deGFP`, a 2855 bp plasmid that places the tetO operator between the T7 promoter and deGFP. No file in `nucleus-eng/DNA` has this sequence. The closest is [pOpen-deGFP](https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-deGFP.gbk), the same plasmid without the 43 bp operator region (2812 bp).

@Editor: Submit the sequence file to `nucleus-eng/DNA`, then add a row to the table above.
:::
::::

::::{tab-item} Cytosol

The reference composition is [Base Cytosol](../base-cytosol/spec.md), with `pT7-tetO-plamGFP` at 1 nM and purified TetR at 500 nM or 1000 nM, induced with aTc at 0.25 µM to 10 µM; the titration is under [aTc titration in Nucleus Base Cytosol](#atc-titration-in-nucleus-base-cytosol). The useful aTc range in Base Cytosol is 0.25 µM to 1 µM at either TetR concentration ([Expressing Cell-Free TetO-GFP in Solution with aTc Titration](https://github.com/nucleus-eng/devstudio-board/pull/12)). The NEB PURExpress build follows.

In NEB PURExpress, assemble `pT7-tetO-plamGFP` into a standard PURE reaction. Supply TetR in one of three ways: as purified protein, added to a final concentration of 500 nM; expressed in situ from the `pT7-tetR` plasmid, used as a DNA template in the same reaction; or expressed in a separate Cytosol reaction, whose total reaction is added as a component of this one. Add aTc inducer at 2.5 µM to 5 µM for effective induction. Volumes in µL.


| **Component** | **Master Mix (µL)** |
| --- | --- |
| PURExpress Solution A | 4 |
| PURExpress Solution B | 3 |
| RNase Inhibitor | 0.5 |
| `pT7-tetO-plamGFP` (10 nM) | 0.5 |
| TetR (10 µM) | 0.5 |
| Water | 0.5 |
| **Master Mix Total** | **9** |

| **Component** | **Per Reaction (µL)** |
| --- | --- |
| Master Mix | 9 |
| aTc inducer (25 µM to 50 µM) | 1 |
| **Total** | **10** |

::::

:::::

# Expected Behavior

## Cytosols

### aTc titration in Nucleus Base Cytosol

`pT7-tetO-plamGFP` was titrated with aTc against purified His-tagged TetR (MedChemExpress, HY-P71520A) in [Nucleus Base Cytosol](../../processes/assemble-base-cytosol/main.md). Per 10 µL, the reaction holds 3.0 µL SMix, 1.0 µL tRNA, 1.2 µL PMix, 1.8 µL ribosomes and 0.5 µL RNase inhibitor. The plasmid is at 1 nM and TetR at 0, 500 or 1000 nM, before the aTc is added. Plasmid, TetR and water were incubated at 37 °C for 10 min so TetR could bind the operator, and the master mix was then added. Reactions were dispensed at 10 µL per well into a 384-well plate and 1 µL of aTc added, to final aTc concentrations of 0, 0.25, 0.35, 0.5, 1, 5 and 10 µM, with three wells per condition. A no-DNA reaction at each aTc concentration served as the background. Fluorescence (485 nm excitation, 528 nm emission, gain 75) was read every 5 min for 6 h at 37 °C on a BioTek Cytation 3.

Without aTc, TetR holds expression to 541 RFU at 500 nM (40-fold below the unrepressed reaction) and 399 RFU at 1000 nM (54-fold). The no-DNA background stays between 43 and 87 RFU across the titration and rises with aTc dose, from 47 RFU at 0 µM to 69 RFU at 5 µM and 87 RFU at 10 µM, which is under 0.5 % of the unrepressed signal. aTc does not change the unrepressed reaction: it reads between 21,662 and 22,871 RFU from 0 to 10 µM, so aTc neither quenches nor inhibits expression at these doses.

aTc relieves repression in both reactions, and the dose needed rises with the amount of TetR. At 500 nM TetR, expression reaches 30 % of the unrepressed level at 0.25 µM aTc, 86 % at 1 µM and 91 % at 5 µM. At 1000 nM TetR it is 4 % at 0.25 µM, 22 % at 0.5 µM, 63 % at 1 µM and 88 % at 5 µM. Half of the unrepressed level is reached at about 0.4 µM aTc with 500 nM TetR and about 0.8 µM with 1000 nM, so doubling TetR moves the induction curve about two-fold to higher aTc. Neither reaction reaches the unrepressed level by 10 µM, where they read 87 % and 93 %. The titration has no points between 1 and 5 µM, so these half-maximal doses are read from the measured points.

:::{figure} cytosol-nucleus-atc-titration-endpoint.png
:name: fig-tetr-atc-nucleus-cytosol-endpoint
:align: center

Endpoint GFP fluorescence at 6 h in Nucleus Base Cytosol, for 1 nM `pT7-tetO-plamGFP` with 0, 500 or 1000 nM TetR across 0 to 10 µM aTc, with a no-DNA control at each dose. Mean ± standard deviation of three wells; gain 75.
:::

### aTc titration at 1000 nM TetR

`pOpen-TetO-deGFP` is a plasmid, purified by maxiprep, that places the tetO operator between the T7 promoter and deGFP. Each 10 µL reaction is in the same cytosol as the section above and holds the plasmid at 1 nM, purified His-tagged TetR at 1000 nM, and the OnePot sub-mixes (Smix, tRNA, Pmix, ribosomes and RNase inhibitor). aTc was added in a further 1 µL at 0, 0.25, 0.5 and 1 µM. Fluorescence was read every 5 min for 6 h at 37 °C (485/20 nm excitation, 528/20 nm emission, gain 50), with two wells per condition.

@Editor: No Process page documents the plate reader kinetic read. Link one here when it exists.

TetR at 1000 nM holds deGFP to about a tenth of the unrepressed level, and the no-DNA floor is under 1 % of it. aTc at 0.25 µM raises expression about 3.3-fold over the repressed reaction, to about a third of the unrepressed level. Above 0.25 µM the titration is not monotonic: 1 µM reads below 0.25 µM, and the two wells at 0.5 µM differ 2.3-fold, the widest disagreement of any condition. aTc does not inhibit the reaction: unrepressed wells at 1 µM aTc read within 6 % of unrepressed wells at 0 µM. Every condition reaches 95 % of its 6 h value within about 4 h.

:::{figure} cytosol-degfp-atc-titration-kinetics.png
:name: fig-tetr-atc-titration-kinetics
:align: center

Kinetics of deGFP expression from `pOpen-TetO-deGFP` in bulk reactions: no DNA, unrepressed (1 nM plasmid), and 1 nM plasmid with 1000 nM TetR across 0 to 1 µM aTc. Fluorescence at gain 50, read every 5 min for 6 h at 37 °C. n = 2 wells per condition.
:::

:::{figure} cytosol-degfp-atc-titration-endpoint.png
:name: fig-tetr-atc-titration-endpoint
:align: center

Endpoint deGFP fluorescence at 6 h, from the run in the kinetics figure. Individual replicates are shown; n = 2 wells per condition.
:::

### NEB PURExpress

The TetR module is validated in NEB PURExpress reactions. Purified repressor protein and anhydrotetracycline inducer are added at the final concentrations indicated. `pT7-tetO-plamGFP` plasmid DNA is added at 0.5 nM.

Repression follows a roughly linear trend between 125 and 750 nM TetR and saturates around 500 nM, though it can be further improved up to 2000 nM. An inducer concentration of 2.5 µM to 5 µM provides effective induction well below saturating or toxic aTc levels. Note that aTc's yellow color overwhelms GFP fluorescence at concentrations greater than 50 µM to 100 µM, and high concentrations may negatively affect expression generally.

### *In vitro* repression with TetR

:::::{tab-set}

::::{tab-item} Kinetics
:::{figure} cytosol-repression-kinetics.png
Repression kinetics of `pT7-tetO-plamGFP` by TetR at varying repressor concentrations.
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-repression-endpoint.png
Repression of `pT7-tetO-plamGFP` by TetR at steady state.
:::
::::

:::::

### *In vitro* induction with aTc

:::::{tab-set}

::::{tab-item} Kinetics
:::{figure} cytosol-induction-kinetics.png
Induction kinetics of `pT7-tetO-plamGFP` by aTc. TetR repressor protein is present at 500 nM. Positive control is `pT7-tetO-plamGFP` without TetR repressor protein.
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-induction-endpoint.png
Induction of `pT7-tetO-plamGFP` by aTc at steady state. TetR repressor protein is present at 500 nM. Positive control is `pT7-tetO-plamGFP` without TetR repressor protein.
:::
::::

:::::

## Cells

:::{figure} detector-overview.png
Schematic representation of the TetR-aTc Detector Module in the Base Cell.
:::

TetR detector synthetic cells are induced at multiple anhydrotetracycline concentrations and imaged over 12 h with approximately 22 min per timepoint.

:::::{tab-set}

::::{tab-item} Microscopy Images
:::{figure} cell-performance-montage.png
TetR detector synthetic cells induced at multiple anhydrotetracycline concentrations. 8 timepoints displayed per condition, approximately 22 min apart, over 12 h total. **First row:** induction using 625 nM, 312.5 nM, and 0 nM (fully repressed) aTc introduced into the outer buffer. **Second row:** induction with 2500 nM aTc in the inner solution and positive control without TetR repression.
:::
::::

::::{tab-item} Fluorescence Intensity
:::{figure} cell-performance-endpoint.png
GFP expression within synthetic cells when induced with 312.5 nM anhydrotetracycline.
:::
::::

:::::

The TetR detector cell functions when induced with aTc at 312.5 nM to 2500 nM. Higher concentrations begin to inhibit expression or confound analysis due to background aTc fluorescence and membrane localization.

### `pOpen-TetO-deGFP` in GUVs

Giant unilamellar vesicles (GUVs) were formed by inverted emulsion transfer ([Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md)) from POPC and cholesterol at 9:1 with 18:1 Liss Rhod PE at 1 mmol/mol. Sucrose, at 8.8 % of the reaction, is the density agent in the inner solution, and glucose is the outer solution. The inner solution is the reaction in the previous section plus that sucrose: no DNA, unrepressed (`pOpen-TetO-deGFP` at 1 nM), or repressed (1 nM plasmid with 1000 nM TetR). aTc was added outside the vesicles at 0, 0.25, 0.5 and 1 µM. The vesicles were imaged over 4 h in a BSA-blocked 384-well glass-bottom plate on a Cephla Squid microscope, in a GFP channel and an Alexa Fluor 647 channel. GFP was scored only inside objects with a continuous membrane label.

@Editor: The membrane label is a rhodamine dye, and the stored channels are GFP and Alexa Fluor 647, with no rhodamine channel. Give the channel that imaged the vesicles. Also give the objective, exposure, gain and laser power of the fluorescence readout. No Process page documents it.

In solution, no-DNA vesicles stayed dark throughout, unrepressed vesicles became strongly fluorescent, the 0 µM aTc condition remained repressed, and lumen deGFP increased with aTc concentration up to 1 µM, the highest dose tested. aTc is autofluorescent in the GFP channel and raises background in proportion to dose, so the second figure subtracts the matched no-DNA control at each dose from every condition.

GUVs embedded in PEG-NB hydrogel were imaged alongside. Light scattering from the gel dominates those images, and expression could not be read from them.

:::{figure} cell-guv-degfp-atc-raw.png
:name: fig-tetr-atc-guv-raw
:align: center

Lumen deGFP fluorescence in solution-phase GUVs over 4 h, by aTc dose. Bands show the median, interquartile range, 10th to 90th percentile and 99th percentile of the mean intensity of each vesicle. Two technical replicates per condition.
:::

:::{figure} cell-guv-degfp-atc-background-subtracted.png
:name: fig-tetr-atc-guv-subtracted
:align: center

The same data after subtracting the matched no-DNA control at each aTc dose.
:::

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).

# Implementations

- [Responder: aTc → IV-HSL](../../implementations/responder-atc-ivhsl/main.md): aTc relieves TetR repression to drive BjaI expression.

# Processes

- [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md): makes the GUVs by inverted emulsion transfer.

# Materials

:::{table}
:label: critical-materials

| Material | Description | Manufacturer | Part # | Link |
| --- | --- | --- | --- | --- |
| Purified TetR protein | His-tagged TetR repressor, lyophilized from a solution containing 0.2 mg/mL Tween 80 | MedChemExpress | HY-P71520A | |
| Anhydrotetracycline (aTc) | Inducer | Cayman Chemical | 10009542 | |
:::

# Credits

Developed by Yen-Yu Hsu (b.next).

Bulk titration in Nucleus Base Cytosol by Mary Kelly (Kamat Lab, Northwestern University, DevCells Chicago Node).

GUV deGFP characterization by Mary Kelly (Kamat Lab, Northwestern University, DevCells Chicago Node).
