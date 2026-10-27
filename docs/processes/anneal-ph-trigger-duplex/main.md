---
title: "Anneal pH Trigger Duplex"
subtitle: "Process"
status: draft
---

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Overview

Anneal pH Trigger Duplex hybridizes the pH-responsive strand (`pH-responsive-ssDNA-2`) and the trigger strand (`trigger-ssDNA-3`) in IDT duplex buffer. Each strand is dissolved to 100 µM in IDT duplex buffer, and the two stocks are mixed at a 3:1 volume ratio (pH-responsive : trigger), giving 75 µM pH-responsive strand and 25 µM trigger strand before annealing. An earlier design target called for 14.4 µM pH-responsive strand and 4.8 µM trigger strand ([Module Development Plan: DevCell-based pH sensor](https://devnotes.nucleus.engineering/articles/chicago-m1-5-1)); the executed protocol used the higher concentrations given here. The duplex is the sensing element of the [pH-Sensing Detector](../../modules/detector-ph/spec.md), which the [pH Sensing Cell](../../modules/ph-sensing-cell/spec.md) carries: acidification releases the trigger strand, which activates a toehold switch RNA ([Hwang et al., 2025](https://doi.org/10.1101/2025.11.16.688650)). The cooling program runs from 95 °C to 25 °C in about 7 h. The pH Sensing Cell uses the annealed duplex at a stock concentration of 25 µM. This is the concentration of the trigger strand.

::::{attention} Genetically Encoded Components
:class: dropdown
:icon: false

:::{table} The two oligonucleotides. Each is a single strand.
:label: tbl-anneal-ph-trigger-duplex-dna

| Name | Length (nt) | Sequence (5′ to 3′) | File |
| --- | --- | --- | --- |
| `pH-responsive-ssDNA-2` | 49 | TTCTCTTCTCGTTTGCTCTTCTCTTGTGTGGTATTGTCCAAGAGAAGAG | [pH-responsive-ssDNA-2.gb](https://github.com/nucleus-eng/DNA/blob/bf3d5aeea79c652b3f7af08f32409dbc7b3431b0/detectors/detector-ph/pH-responsive-ssDNA-2.gb) |
| `trigger-ssDNA-3` | 36 | TATGCAAACAAGACAATACCACACAATTTTTTTTTT | [trigger-ssDNA-3.gb](https://github.com/nucleus-eng/DNA/blob/bf3d5aeea79c652b3f7af08f32409dbc7b3431b0/detectors/detector-ph/trigger-ssDNA-3.gb) |
:::
::::

# Materials and Equipment

:::{table} Bill of Materials
:label: bom-anneal-ph-trigger-duplex
:align: center

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| ---- | -------- | ------- | ------------ | ------ | ----- | ------- | ---- |
| IDT duplex buffer | Reagent | Nuclease Free Duplex Buffer (10 x 2 mL) | IDT | 11-01-03-01 | $17.00 | -20 °C | [link](https://www.idtdna.com/site/order/stock/index/nfd) |
:::

The two oligonucleotides, a thermocycler, and nuclease-free tubes are also required.

# Protocol

## Anneal the Strands

- [ ] **Combine the strands in IDT duplex buffer.**
    - [ ] Dissolve `pH-responsive-ssDNA-2` and `trigger-ssDNA-3` separately to 100 µM each in IDT duplex buffer.
    - [ ] Mix the two stocks at a 3:1 volume ratio (pH-responsive : trigger). This gives 75 µM pH-responsive strand and 25 µM trigger strand.
- [ ] **Anneal in a thermocycler.** Cool in steps of 1 °C, with this program:

:::{table} Annealing program. Tm is the melting temperature of the duplex, 52 °C.
:label: tbl-anneal-ph-trigger-duplex-program

| Stage | From | To | Time per °C |
| --- | --- | --- | --- |
| Denature | 95 °C | 95 °C | 5 min hold |
| Cool to Tm | 95 °C | 52 °C (Tm) | 2 min |
| Slow cool | 52 °C (Tm) | 42 °C (Tm − 10 °C) | 30 min |
| Cool to room temperature | 42 °C | 25 °C | 2 min |
:::

- [ ] **Store the annealed duplex at −20 °C.**

# Credits

Developed by [Sung-Won Hwang](https://orcid.org/0000-0003-1686-7090), [Samuel Chen](https://orcid.org/0000-0001-8501-7175) and [Allen P. Liu](https://orcid.org/0000-0002-0309-7018) (University of Michigan).

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this page include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Two Vesicle Colorimetric pH Sensor System
:link: https://devnotes.nucleus.engineering/articles/01a0ea82-2101-7fed-82f9-1d8ef9258009
:footer: Sung-Won Hwang, Samuel Chen, Allen P. Liu · DevStudio 2026

![](https://pub.curvenote.com/01a1659e-fe19-7cd1-8542-37ff98753726/public/overview-schematic-a686967b8ee4691359ab0bc0bd9be620.webp)
:::

::::
