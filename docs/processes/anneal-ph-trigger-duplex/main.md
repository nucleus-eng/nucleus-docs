---
title: "Anneal pH Trigger Duplex"
subtitle: "Process"
status: draft
---

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Overview

Anneal pH Trigger Duplex hybridizes the pH-responsive strand (`pH-responsive-ssDNA-2`) and the trigger strand (`trigger-ssDNA-3`) in IDT duplex buffer, at a ratio of 3:1 by mole (pH-responsive : trigger). The design concentrations in the reaction are 14.4 µM pH-responsive strand and 4.8 µM trigger strand, so the pH-responsive strand is in excess ([Module Development Plan: DevCell-based pH sensor](https://devnotes.nucleus.engineering/articles/chicago-m1-5-1)). The duplex is the sensing element of the [pH-Sensing Detector](../../modules/detector-ph/spec.md), which the [pH Sensing Cell](../../modules/ph-sensing-cell/spec.md) carries: acidification releases the trigger strand, which activates a toehold switch RNA ([Hwang et al., 2025](https://doi.org/10.1101/2025.11.16.688650)). The cooling program runs from 95 °C to 25 °C in about 7 h. The pH Sensing Cell uses the annealed duplex at a stock concentration of 25 µM. This is the concentration of the trigger strand.

:::{attention}
@Developer: Give the concentration and volume of each strand in the annealing mix.
:::

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
    - [ ] Mix `pH-responsive-ssDNA-2` and `trigger-ssDNA-3` at a ratio of 3:1 by mole (pH-responsive : trigger). The design concentrations in the reaction are 14.4 µM pH-responsive strand and 4.8 µM trigger strand, so the pH-responsive strand is in excess ([Module Development Plan: DevCell-based pH sensor](https://devnotes.nucleus.engineering/articles/chicago-m1-5-1)).
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
