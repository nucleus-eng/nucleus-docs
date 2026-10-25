---
title: "Reporter: deGFP"
subtitle: "Module Specification"
thumbnail: schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The deGFP Reporter Module produces deGFP, a green fluorescent protein.

:::{figure} schematic.png
:width: 40%
:align: center

A schematic representation of PURE converting template DNA into a fluorescent reporter.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA
:::{table}
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pOpen-deGFP` | 2812 | [pOpen-deGFP.gbk](https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-deGFP.gbk) |
:::
::::

::::{tab-item} Cytosol

:::{table} This composition was evaluated in this [DevNote ](https://doi.org/10.63765/fppr8928)
![](xref:devnote-01#rc)
:::

::::

::::{tab-item} Cell

**Inner solution**

:::{table}
:label: comp-degfp-cell-inner

| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction (µL) |
| --- | --- | --- | --- | --- | --- |
| SMix | 3.33 | × | 1 | × | 12 |
| PMix | 15 | mg/mL | 1.80 | mg/mL | 4.8 |
| Ribosomes | 10 | µM | 1.8 | µM | 7.2 |
| `pOpen-deGFP` DNA | 124 | nM | 3 | nM | 0.95 |
| tRNA | 35 | mg/ml | 3.5 | mg/ml | 4 |
| Magnesium acetate | 200 | mM | 8 | mM | 1.6 |
| Optiprep | 1.32 | mg/µL | 0.043 | mg/µL | 1.33 |
| RNase Inhibitor | 40000 | U/mL | 2000 | U/mL | 2 |
| Water |  |  |  |  | 6.12 |
| Total volume (µL) |  |  |  |  | 40 |
:::

**Membrane**

:::{table}
:label: comp-degfp-cell-membrane

| Component    | Target (mmol/mol)     | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC         | 699.3                 | 760.076                  | 25                          | 162.01             |
| Cholesterol  | 299.7                 | 386.654                  | 50                          | 17.66              |
| Liss-Rhod PE | 1                     | 1301.71                  | 1                           | 9.92               |

:::

**Outer solution**

:::{table}
:label: comp-degfp-cell-outer

| Component | Concentration |
| --- | --- |
| Glucose | 850 mM |
:::

::::

:::::

# Expected Behavior

## Cytosols

<!-- :::::{tab-set}
::::{tab-item} Kinetics
:::{figure}
![](xref:devnote-01#fig:kinetics-exp1)
:::
::::

::::{tab-item} Endpoint
:::{figure}
![](xref:devnote-01#fig:endpoint-exp1)
:::
::::
::::: -->

:::::{tab-set}
::::{tab-item} Kinetics
:::{figure} cytosol-kinetics.png
Translation kinetics of Cytosol and PURExpress reactions using two different pOpen-deGFP DNA preps. Cytosol w/o DNA refers to the Cytosol reaction lacking the pOpen-deGFP template. Data in [DevNote](https://doi.org/10.63765/fppr8928).
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-endpoint.png
Final protein yields of the reactions measured at steady state. Data from [DevNote](https://doi.org/10.63765/fppr8928).
:::
::::
:::::

## Cells

:::::{tab-set}
::::{tab-item} Image 1
:::{figure} cell-image1.png
Combined green (488 nm) and red (561 nm) fluorescence channels. Timepoint 0 (t = 0) corresponds to 30 min after preparation of the inner solution, reflecting the time required to prepare liposomes.
:::
::::

::::{tab-item} Image 2
:::{figure} cell-image2.png
Combined green (488 nm) and red (561 nm) fluorescence channels. Timepoint 0 (t = 0) corresponds to 30 min after preparation of the inner solution, reflecting the time required to prepare liposomes.
:::
::::
:::::

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).

# Downloads

::::{grid} 1 1 1 2

:::{card}
:header: **Step-by-Step Cytosol Protocol**
:footer: *Implemented using Nucleus Cytosol*
{button}`Download <module-protocol-cytosol-degfp.pdf>`
:::

:::{card}
:header: **Cytosol Materials**
:footer: *Implemented using Nucleus Cytosol*
{button}`Download <module-bom-reporter-degfp.pdf>`
:::

:::{card}
:header: **Step-by-Step Cell Protocol**
:footer: *Implemented using Nucleus Cytosol*
{button}`Download <module-protocol-cells-degfp.pdf>`
:::

:::{card}
:header: **Cell Materials**
:footer: *Implemented using Nucleus Cytosol*
{button}`Download <module-bom-reporter-cells-degfp.pdf>`
:::

::::

# Credits

Developed by Surendra Yadav (b.next).

# Supported by

DevNotes that reference this spec, not curated attribution; see Credits for that.

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Characterizing the Limited Operational Lifetime of Cytosol Reactions
:link: https://devnotes.nucleus.engineering/articles/019ef6d5-3a27-787f-9ebd-fe80645b1068
:footer: Surendra Yadav · Nucleus Core

![](https://pub.curvenote.com/01a08cd1-0bda-777d-90ea-ef62ac077bf8/public/kinetics-normalized-8268e61917aa794a036d5761bad675cd.webp)
:::

:::{card} ClpXP Control Module: Deployment in Nucleus Cytosol
:link: https://devnotes.nucleus.engineering/articles/019f05cb-6be8-7189-8c0d-f8f51d170541
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a15336-ad4c-7145-b48c-b467190898c0/public/control-module-456a08ae6157de8014ea7b8b5895035f.webp)
:::

:::{card} ClpXP Control Module: Deployment in PURE
:link: https://devnotes.nucleus.engineering/articles/019b3969-570f-7d88-b998-48ca97f0306c
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a08cd1-0d1e-7663-b612-b11a47b09f60/public/clpXP-eeff4ebcb83656de9cf8c31ccc8ad782.webp)
:::

:::{card} First Nucleus Cytosol Testing
:link: https://devnotes.nucleus.engineering/articles/019a7511-0b68-702b-8909-0fe96ef8d5d2
:footer: Surendra Yadav · Nucleus Core

![](https://pub.curvenote.com/019fcdbd-d48a-7319-be07-15b772037c88/public/illustration2-63bd8a34b4a90292a066abf875d462eb.png)
:::

:::{card} Integrating PPK Module in PURE Cells
:link: https://devnotes.nucleus.engineering/articles/019926c4-3341-76fc-8f36-eb96fd77c170
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a04676-f2cb-77ef-be8a-94b6945522ba/public/Developer_Cell-PPK_M-0437e9bcfcc9583145022782575f6b7b.webp)
:::

:::{card} Nucleus Base Cell Testing
:link: https://devnotes.nucleus.engineering/articles/019b13f9-1ec6-757c-b5ed-68cdd8e91fb0
:footer: Surendra Yadav · Nucleus Core

![](https://pub.curvenote.com/01a04676-8d9d-7f8f-96e1-2eefb52a607d/public/Image1-97e36bb3a38f167a4409ef588837c5fa.webp)
:::

:::{card} What is a Cytosol Landscape?
:link: https://devnotes.nucleus.engineering/articles/01a08c2d-2898-7f60-8f62-6bee069fddca
:footer: Sharon Newman · Nucleus Core

![](https://pub.curvenote.com/01a14c37-92c9-709e-91b5-af7303081a95/public/thumbnail-223faeab72d3f8699de21fbcfcf44279.webp)
:::

::::
