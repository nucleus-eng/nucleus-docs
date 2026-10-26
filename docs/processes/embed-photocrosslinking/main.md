---
title: "Embedding: Photocrosslinking"
subtitle: "Process"
status: draft
---

# Overview

Embedding: Photocrosslinking holds a sample in a PEG-nb gel that sets under 405 nm light. The precursor stays liquid until it is exposed, so the sample can be loaded and checked before the gel forms. This page covers [Gel: PEG-nb](../../modules/gel-peg-nb/spec.md). A digital light processing (DLP) projector exposes the plate at 405 nm for 60 s.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{figure} ./resources/photopatterning-setup.jpg
:label: fig-photopatterning-setup
:width: 40%
:align: center

Photograph of photopatterning in a 96-well plate: a digital light processing projector on a stand exposes the plate to 405 nm light.
:::

:::{table} Precursor, per 1 mL.
| Component | Concentration | Amount |
| --- | --- | --- |
| 4-arm PEG-norbornene | 80 mM | 0.4 g |
| 4-arm PEG-thiol | 20 mM | 0.04 g |
| LAP | 16.9 mM | 4.97 mg |
:::

# Materials and Equipment

The precursor materials are listed under Materials on [Gel: PEG-nb](../../modules/gel-peg-nb/spec.md).

:::{table} Equipment.
| Item | Used for |
| --- | --- |
| DLP projector (Zwants Supplies Engineering, PRO4500-92-405) | Exposure |
| 96-well or 384-well plate | Plating |
:::

:::{attention} Plate vendor and exposure dose are not stated
@Editor: give the vendor of the plate and the irradiance of the projector at the sample.
:::

# Protocol

## Prepare the Precursor

:::{hint} The precursor is photosensitive
:class: dropdown
Prepare the precursor in a dark room, and wrap the vial in foil for storage.
:::

- [ ] **Dissolve the components.**
    - [ ] Dissolve the PEG-nb, the PEG-thiol and the LAP in 1 mL of the outer solution the liposomes were prepared in.
- [ ] **Mix until clear.**
    - [ ] Vortex at 2000 rpm for 1 min, then leave at room temperature for 3 to 5 min.
    - [ ] Vortex again for 2 to 4 min and check that every component has dissolved.
    - [ ] Repeat until the solution is clear.

:::{attention} Best starting solvent is not settled
@Editor: state which solvent is the best starting point for the precursor. The choice being flexible is not enough. The protocol step allows PBS, deionized water or any buffer. A stock-sheet note records that PBS did not work in one set of GUVs. The reagent table instead names glucose in 50 mM HEPES. Name every solvent that was tried, what happened with each, and recommend one.
:::

## Mix with the Sample and Plate

- [ ] **Mix the sample with the precursor.**
    - [ ] Combine 15 µL of sample with 15 µL of precursor.
- [ ] **Plate the mixture.**
    - [ ] Dispense 30 µL per well into a 96-well or 384-well plate. Plate each sample in duplicate.
    - [ ] Plate the sample in its outer solution, with no gel, as a reference.

## Expose

- [ ] **Photopattern the gel.**
    - [ ] Expose the plate for exactly 60 s at 405 nm with a DLP projector.

:::{hint} The precursor can be diluted in the well
:class: dropdown
When a lower concentration is needed, dilute the precursor 1:1 in the well, for example 50 µL of precursor with 50 µL of buffer.
:::

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this page include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Understanding Liposome Behaviour in Hydrogel Matrices
:link: https://devnotes.nucleus.engineering/articles/01a10dfe-c1df-7c2d-ba5a-035280a349f7#hydrogel-preparation
:footer: Ojaswita Pant, Manuel Bibrowski · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-f2a7-7372-93d6-8ea9f387f61d/public/schematic-hydrogel-o-d7d3affce66c5490e22c9a76d4696445.webp)
:::

:::{card} TetO-Regulated PLA1 Sensor in Vesicles: aTc Titration and Spatial Patterning
:link: https://devnotes.nucleus.engineering/articles/01a1304b-1c56-7352-a082-ba84a2684f82
:footer: Mary Kelly, Madison Briggs · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-ebfe-71b5-b20a-66b33af95dfb/public/fig1-guv-gfp-gel-vs--e6f9429ea276453e88a78e854168033e.png)
:::

::::
