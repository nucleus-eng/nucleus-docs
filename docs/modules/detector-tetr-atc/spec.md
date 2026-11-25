---
title: "Detector: tetR-aTc"
subtitle: "Module Specification"
status: validated-published
thumbnail: mechanism-schematic.png
site:
    hide-toc: true
    numbered_references: false
---

(detector-tetr-atc-overview)=
# Overview

The TetR Detector Module module senses the small molecule anhydrotetracycline (aTc) and starts transcription in response. TetR is a repressor that binds the TetO operator, which when placed between a T7 promoter and the gene behind it blocks T7 RNA polymerase from transcribing that gene. Adding aTc releases TetR from the DNA, and initiates transcription.

Nucleus includes a set of two DNA sequences that implement this module in DNA: `pT7-tetR`, encoding the TetR repressor protein, and `pT7-tetO-plamGFP`, encoding a reporter gene under control of TetO. `pT7-tetO-plamGFP` constitutively expresses the open reporter plamGFP in the absence of repressor protein. Addition of TetR, either as a purified protein or expressed from `pT7-tetR`, represses transcription. aTc is membrane-permeable, so this Module does not require membrane transport

(detector-tetr-atc-reference-composition)=
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

| Component | Stock concentration | Final concentration | Volume (µL) |
| --- | --- | --- | --- |
| Small molecule mix | 3.33-fold | 1-fold | 10.50 |
| tRNA | 35 µg/µL (10-fold) | 3.5 µg/µL (1-fold) | 3.50 |
| Protein mix | 8.33-fold | 1-fold | 4.20 |
| Ribosomes | 10 µM (5.55-fold) | 1.8 µM (1-fold) | 6.30 |
| RNase inhibitor | 40 U/µL | 1 U/µL | 0.88 |
| `pT7-tetO-plamGFP` | 10 nM | 1 nM | 3.50 |
| TetR (protein) | 10 µM | 500 nM | 1.75 |
| aTc inducer | — | 250 nM | — | 
| Nuclease-free water | — | — | 4.37 |
| **Total** | | | **35.00** |
::::

:::::

(detector-tetr-atc-expected-behavior)=
# Expected Behavior

(detector-tetr-atc-cytosols)=
## Cytosols

(detector-tetr-atc-atc-titration-in-nucleus-base-cytosol)=
### aTc titration in Nucleus Base Cytosol

Purified His-tagged TetR (MedChemExpress, HY-P71520A) at (0, 0.5, and 1) µM and aTc at (0, 0.25, 0.35, 0.5, 1, 5 and 10) µM were titrated against fixed `pT7-tetO-plamGFP` (1 nM) in [Nucleus Base Cytosol](../../processes/assemble-base-cytosol/main.md). Plasmid, TetR and water were first pre-incubated at 37 °C for 10 min so TetR could bind the operator, then added to the reaction master mix. A no-DNA reaction at each aTc concentration was included for background correction. Fluorescence (485 nm excitation, 528 nm emission, gain 75) was read every 5 min for 6 h at 37 °C on a BioTek Cytation 3.

Without aTc induction, TetR represses expression 40-fold below the unrepressed reaction at 500 nM TetR and 54-fold at 1000 nM TetR. The no-DNA background stays under 0.5 % of the unrepressed signal in all conditions. aTc does not change the unrepressed reaction, so aTc neither quenches nor inhibits expression at these doses.

aTc induces expression in all repressed conditions. The required aTc concentration rises with the increasing TetR. At 500 nM TetR, expression reaches 30 % of the unrepressed level at 0.25 µM aTc, 86 % at 1 µM and 91 % at 5 µM. At 1000 nM TetR, expression reaches 4 % at 0.25 µM, 22 % at 0.5 µM, 63 % at 1 µM and 88 % at 5 µM. Half of the unrepressed level is reached at about 0.4 µM aTc with 500 nM TetR and about 0.8 µM with 1000 nM, so doubling TetR moves the induction curve about two-fold to higher aTc. Neither reaction reaches the unrepressed level by 10 µM, where they read 87 % and 93 %. The titration has no points between 1 and 5 µM, so these half-maximal doses are read from the measured points.

:::::{tab-set}
::::{tab-item} Endpoint Fluorescence (graph)
:::{figure} cytosol-nucleus-atc-titration-endpoint.png
:name: fig-tetr-atc-nucleus-cytosol-endpoint
:align: center

Endpoint GFP fluorescence at 6 h in Nucleus Base Cytosol, for 1 nM `pT7-tetO-plamGFP` with (0, 500 or 1000) nM TetR across (0 to 10) µM aTc, with a no-DNA control at each dose. Mean ± standard deviation of three wells; gain 75.
:::
::::

::::{tab-item} Endpoint Fluorescence (table)
:::{table} Endpoint GFP at 6 h as a percentage of the unrepressed reaction without aTc (0 nM TetR and 0 µM aTc), which reads 21,662 RFU at gain 75. Mean ± standard deviation of three wells.
:label: tbl-tetr-atc-nucleus-cytosol-pct

| aTc (µM) | 0 nM TetR | 500 nM TetR | 1000 nM TetR |
| --- | --- | --- | --- |
| 0 | (100.0 ± 1.9) % | (2.5 ± 0.2) % | (1.8 ± 0.1) % |
| 0.25 | (100.2 ± 0.3) % | (30.4 ± 1.6) % | (4.0 ± 0.1) % |
| 0.35 | (103.3 ± 0.7) % | (43.7 ± 4.7) % | (5.0 ± 0.7) % |
| 0.5 | (103.9 ± 1.7) % | (75.0 ± 2.8) % | (22.9 ± 3.2) % |
| 1 | (105.6 ± 0.6) % | (90.5 ± 2.0) % | (66.7 ± 4.1) % |
| 5 | (104.8 ± 3.3) % | (95.2 ± 4.9) % | (92.5 ± 2.0) % |
| 10 | (103.8 ± 2.0) % | (89.8 ± 2.9) % | (96.1 ± 1.8) % |
:::
::::


:::::

(detector-tetr-atc-atc-titration-at-1000-nm-tetr)=
### aTc titration at 1000 nM TetR

aTc at (0, 0.25, 0.5 and 1) µM was titrated again against fixed `pOpen-TetO-deGFP` (1 nM) and His-tagged TetR (1000 nM). Fluorescence was read every 5 min for 6 h at 37 °C (485/20 nm excitation, 528/20 nm emission, gain 50), with two replicates per condition.

1000 nM TetR holds deGFP expression to about 10 % of the unrepressed level. 0.25 µM aTc induces expression about 3.3-fold over the repressed reaction, to about 33% of the unrepressed level. Above 0.25 µM aTc, the titration does not monotonically increase expression: 1 µM aTc shows lower expression than 0.25 µM aTc. The two replicates at 0.5 µM aTc differ by 2.3-fold. Again, we found that aTc does not inhibit the reaction. Unrepressed wells at 1 µM aTc showed expression within 6 % of unrepressed wells at 0 µM. Every reaction with DNA reaches 95 % of its expression level at endpoint (6 h) within (2.4 to 3.8) h. The no-DNA conditions read under 1 % of the unrepressed level and drift upward by about 0.4 % of it over 6 h.

:::::{tab-set}
::::{tab-item} aTc titration at 1000 nM TetR (kinetics)
:::{figure} cytosol-degfp-atc-titration-kinetics.png
:name: fig-tetr-atc-titration-kinetics
:align: center

Kinetics of deGFP expression from `pOpen-TetO-deGFP` in bulk reactions: no DNA, unrepressed (1 nM plasmid), and 1 nM plasmid with 1000 nM TetR across (0 to 1) µM aTc. Fluorescence at gain 50, read every 5 min for 6 h at 37 °C. n = 2 replicates per condition.
:::
::::

::::{tab-item} aTc titration at 1000 nM TetR (endpoint)
:::{figure} cytosol-degfp-atc-titration-endpoint.png
:name: fig-tetr-atc-titration-endpoint
:align: center

Endpoint deGFP fluorescence at 6 h, from the run in the kinetics figure. Individual replicates are shown; n = 2 replicates per condition.
:::
::::
::::{tab-item} Endpoint Fluorescence (table)
:::{table} Endpoint deGFP at 6 h as a percentage of the unrepressed reaction without aTc (0 nM TetR and 0 µM aTc), which reads 41,763 RFU at gain 50. Each cell gives the mean of two wells, then the two wells in parentheses. The unrepressed reaction was not run at 0.25 or 0.5 µM aTc.
:label: tbl-tetr-atc-titration-pct

| aTc (µM) | 0 nM TetR | 1000 nM TetR |
| --- | --- | --- |
| 0 | 100.0 % (98.3 %, 101.7 %) | 9.9 % (9.8 %, 10.0 %) |
| 0.25 | not run | 32.2 % (29.5 %, 34.9 %) |
| 0.5 | not run | 36.8 % (51.0 %, 22.6 %) |
| 1 | 94.6 % (107.9 %, 81.4 %) | 21.4 % (22.3 %, 20.5 %) |
:::
::::


:::::

(detector-tetr-atc-neb-purexpress)=
### NEB PURExpress

Purified TetR was titrated at (0.125, 0.25, 0.5, 0.75, 1, and 2) µM against `pT7-tetO-plamGFP` (0.5 nM) in NEB PURExpress, without aTc. In a separate experiment, aTc was also titrated at (0, 1.25, 2.5, 5, 7.5, 10, 15, and 20) µM against fixed TetR (500 nM) and `pT7-tetO-plamGFP` (0.5 nM).

Repression follows a roughly linear trend between (125 and 750) nM TetR and saturates around 500 nM, though repression does increase up to 2000 nM. An inducer concentration of 2.5 µM to 5 µM provides effective induction. Note that aTc's yellow color overwhelms GFP fluorescence at concentrations greater than 50 µM to 100 µM, and high concentrations may negatively affect expression generally.

(detector-tetr-atc-in-vitro-repression-with-tetr)=
### *In vitro* repression with TetR

:::::{tab-set}

::::{tab-item} Kinetics
:::{figure} cytosol-repression-kinetics.png
Repression kinetics of `pT7-tetO-plamGFP` (0.5 nM) by TetR at (0.125, 0.25, 0.5, 0.75, 1 and 2) µM in NEB PURExpress.
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-repression-endpoint.png
Repression of `pT7-tetO-plamGFP` (0.5 nM) by TetR at (0.125, 0.25, 0.5, 0.75, 1 and 2) µM in NEB PURExpress at steady state.

:::
::::

:::::

(detector-tetr-atc-in-vitro-induction-with-atc)=
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

(detector-tetr-atc-cells)=
## Cells

Synthetic cells with TetR and `pT7-tetO-plamGFP` were induced at (0, 312.5, 625, and 2500) nM aTc and imaged over 12 h at 37 °C with approximately 22 min between timepoints. For the 2500 nM aTc condition, aTc was added directly to the inner solution of the synthetic cells.

:::::{tab-set}

::::{tab-item} Microscopy Images
:::{figure} cell-performance-montage.png
TetR detector synthetic cells induced at multiple aTc concentrations. 8 timepoints displayed per condition, approximately 22 min apart, over 12 h total. **First row:** induction using 625 nM, 312.5 nM, and 0 nM (uninduced) aTc introduced into the outer buffer. **Second row:** induction with 2500 nM aTc in the inner solution and positive control without TetR repression.
:::
::::

::::{tab-item} Fluorescence Intensity
:::{figure} cell-performance-endpoint.png
GFP expression within synthetic cells when induced with 312.5 nM aTc.
:::
::::

:::::

aTc at 312.5 nM to 2500 nM induces expression in synthetic cells. Higher concentrations begin to inhibit expression or confound analysis due to background aTc fluorescence and membrane localization.

(detector-tetr-atc-popen-teto-degfp-in-guvs)=
### `pOpen-TetO-deGFP` in GUVs

Giant unilamellar vesicles (GUVs) were formed by ([Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md)) from POPC:cholesterol at 9:1 with Liss Rhod PE at 1 mmol/mol final. Sucrose was used as the density reagent at 136 mg/mL (about 400 mM) final reaction concentration. Glucose was used the outer solution to match osmolarity. The following conditions were tested: no DNA, unrepressed (`pOpen-TetO-deGFP` at 1 nM), or repressed (1 nM plasmid with 1000 nM TetR). aTc was added outside the vesicles at (0, 0.25, 0.5 and 1) µM. The vesicles were imaged over 4 h in a BSA-blocked 384-well glass-bottom plate on a Cephla Squid microscope, in a GFP channel and an Alexa Fluor 647 channel. GFP expression was scored only inside objects with a continuous membrane.

Unrepressed synthetic cells became strongly fluorescent and the 0 µM aTc condition remained repressed. aTc is autofluorescent in the GFP channel, so no-DNA vesicles also brighten with aTc concentration: their median intensity at 4 h is 14.7 %, 22.3 %, 31.5 % and 46.4 % of the unrepressed control at 0, 0.25, 0.5 and 1 µM aTc. The unrepressed control is the unrepressed vesicles at 0 µM aTc, with a median intensity of 9,557 before subtraction. After subtracting the matched no-DNA control at each dose, the repressed vesicles read 3.2 %, 22.5 %, 22.8 % and 23.4 % of the unrepressed control subtracted the same way (median intensity 8,156). The signal steps up at 0.25 µM, then rises about 1 percentage point more up to 1 µM, the highest dose tested.

:::::{tab-set}
::::{tab-item} TetR and `pOpen-TetO-deGFP` in GUVs (raw)
:::{figure} cell-guv-degfp-atc-raw.png
:name: fig-tetr-atc-guv-raw
:align: center

deGFP fluorescence in GUVs over 4 h, by aTc dose. Bands show the median, interquartile range, 10th to 90th percentile and 99th percentile of the mean intensity of each vesicle. Two technical replicates per condition.
:::
::::

::::{tab-item} TetR and `pOpen-TetO-deGFP` in GUVs (background subtracted)
:::{figure} cell-guv-degfp-atc-background-subtracted.png
:name: fig-tetr-atc-guv-subtracted
:align: center

The same data after subtracting the matched no-DNA control at each aTc dose. deGFP fluorescence in GUVs over 4 h, by aTc dose. Bands show the median, interquartile range, 10th to 90th percentile and 99th percentile of the mean intensity of each vesicle. Two technical replicates per condition.
:::
::::
:::::

(detector-tetr-atc-requirements)=
# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).

(detector-tetr-atc-implementations)=
# Implementations

- [Responder: aTc → IV-HSL](../../implementations/responder-atc-ivhsl/main.md): aTc relieves TetR repression to drive BjaI expression.

(detector-tetr-atc-processes)=
# Processes

- [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md): makes the GUVs by inverted emulsion transfer.

(detector-tetr-atc-materials)=
# Materials

:::{table}
:label: critical-materials

| Material | Description | Manufacturer | Part # | Link |
| --- | --- | --- | --- | --- |
| Purified TetR protein | His-tagged TetR repressor, lyophilized from a solution containing 0.2 mg/mL Tween 80 | MedChemExpress | HY-P71520A | |
| Anhydrotetracycline (aTc) | Inducer | Cayman Chemical | 10009542 | |
:::

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this specification include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Expressing Cell-Free TetO-GFP in Solution with aTc Titration
:link: https://devnotes.nucleus.engineering/articles/01a12d61-686f-7790-8068-f3638be6d7d2
:footer: Mary Kelly, Madison Briggs · DevStudio 2026

![](https://pub.curvenote.com/01a1650b-08b5-76a5-a679-ac13b0944c15/public/fig2-endpoint-gfp-at-09c04f5579c52340f211668c43f87209.webp)
:::

:::{card} GUV Encapsulation of a TetR/aTc-Inducible deGFP Cell-Free Sensor
:link: https://devnotes.nucleus.engineering/articles/01a12ce3-b57e-7986-8786-d64ff5b6e936
:footer: Mary Kelly · DevStudio 2026

![](https://pub.curvenote.com/01a1650b-081a-7258-a515-7ca0766174f5/public/fig1-bulk-kinetics-abc1dc43cd2229418420caf2908bdad1.webp)
:::

:::{card} IV-HSL Emitter Cell
:link: https://devnotes.nucleus.engineering/articles/01945265-b728-7938-aab0-1ce134f4dffa
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a08cd1-0fa0-703d-902e-ade36c88739c/public/emitter-cell-schemat-41d2837d97b57df934b8bf6cbf9f0d3b.webp)
:::

:::{card} Implementing of a bulk color change module into bacterial quorum sensing
:link: https://devnotes.nucleus.engineering/articles/01a12e6c-b511-7d30-aa95-002d386f751e
:footer: Manuel Bibrowski, Charlie Newell, Jonah McDonald, Niall McIntyre, Julia Purrinos de Oliveira · DevStudio 2026

![](https://pub.curvenote.com/01a1650a-90b4-729f-875b-e4f1ddce3bec/public/colorchange-overnigh-520d47ff723d53997b42c0e1c8c68cdc.webp)
:::

:::{card} TetO-Regulated PLA1 Sensor in Vesicles: aTc Titration and Spatial Patterning
:link: https://devnotes.nucleus.engineering/articles/01a1304b-1c56-7352-a082-ba84a2684f82
:footer: Mary Kelly, Madison Briggs · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-ebfe-71b5-b20a-66b33af95dfb/public/fig7-patterned-gel-5fc6273fa124c69e6d78ac4caafe3ce4.webp)
:::

::::
