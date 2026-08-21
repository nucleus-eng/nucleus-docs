---
title: "S30 Lysate"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

S30 Lysate is a commercially available *E. coli* cell-free expression system with undefined composition. S30 Lysate may be used in place of [Base Cytosol](../base-cytosol/spec.md) for compatible modules.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. Composition and performance data below come from a single internal encapsulation experiment (London Module 3) and have not been independently replicated or validated.
:::

# Reference Composition

S30 Lysate itself is supplied as a kit (premix + extract + amino acid mix) rather than formulated from individual reagents ([Promega *E. coli* S30 Extract System for Circular DNA](https://www.promega.com/products/protein-expression/cell-free-protein-expression/e_-coli-s30-extract-system-for-circular-dna/), Cat. No. L1020).

:::{table} Composition of the S30 Lysate.
:label: comp-s30-inner-solution

| Component               | Stock Concentration | Final Concentration | Volume to add (µL) |
| ----------------------- | ------------------- | ------------------- | ------------------ |
| S30 premix              | 2.5x (kit)          | 1×                  | 10                 |
| S30 extract             | 3.33x (kit)         | 1×                  | 7.5                |
| Amino acid mix (pooled) | 10x (kit)           | 1×                  | 2.5                |
| RNase inhibitor         | 40 000 U/mL         | 2000 U/mL           | 1.25               |
| DNA Template            | —                   | 37 ng/µL            | —                  |
| Nuclease-free water     | —                   | —                   | to 25              |

:::

# Expected Behavior

S30 Lysate's expected behavior is characterized by expressing a reporter module (e.g., [deGFP](../reporter-degfp/spec.md)).

:::{attention} Needs more detail
No verbal description of expected behavior is recorded — what the lysate expresses, in what assay, over what time and at what temperature (for example, "expresses X ng/µL deGFP over 6 h at 30 °C") — and no characterization data such as a positive-control cell-free reaction. Raised with the London Node (London questionnaire, Q9).
:::

# Requirements

Requires a circular DNA template driven by an *E. coli* sigma-70 promoter (e.g. [Detector: AHL](../detector-ahl/spec.md)) and an RNase inhibitor. For encapsulated use, additionally requires a membrane (e.g. [London Membrane](../membrane-popc/spec.md)).

Not compatible with Optiprep in the inner solution above ~5%; use sucrose for density matching instead (e.g. [London Chassis](../london-chassis/spec.md)).

**Optiprep blocks expression.** Optiprep-containing synthetic cells stayed round and abundant through 48 h (mean 80, then 66 synthetic cells per field at 1 h and 48 h) but gave no reporter signal at either timepoint. With membrane stability and plasmid dose (80 ng/µL) both ruled out as causes, the block appears to sit in expression itself. The leading interpretation is that Optiprep above ~5% of the inner solution suppresses cell-free expression, and both the 10% and 15% conditions tested exceed that threshold. Without Optiprep in the inner solution, the encapsulated AHL sensor expresses GFP on induction: green fluorescence appears in synthetic cells across all imaged fields, with liposome-associated puncta co-localizing with round liposomes, consistent with an active cell-free reaction inside the liposome.

:::{caution}
**Not yet controlled.** The Optiprep-free expression result above has no minus-AHL or no-DNA negative controls yet, and no biological replicates. Treat the GFP signal as promising but unattributed until those controls are run — the source document explicitly lists both as outstanding ("Controls ... are still needed to attribute the signal, and biological replicates remain to be added").
:::

# Implementations

S30 Lysate is used, encapsulated in POPC, as the chassis for the London demo's AHL-sensing liposome and downstream London Cascade. See [London Chassis](../london-chassis/spec.md) and [London Cascade](../london-cascade/spec.md).

# Materials

:::{table} Kit and reagents used in the S30/POPC encapsulation experiment.
:label: comp-s30-materials

| Name            | Product                                       | Manufacturer | Part # | Price | Storage | Link                                                                                                                                     |
| --------------- | --------------------------------------------- | ------------ | ------ | ----- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| S30 Lysate      | *E. coli* S30 Extract System for Circular DNA | Promega      | L1020  | ~$650 | −65 °C  | [link](https://www.promega.com/products/protein-expression/cell-free-protein-expression/e_-coli-s30-extract-system-for-circular-dna/)   |
| RNase Inhibitor | Recombinant RNasin Ribonuclease Inhibitor     | Promega      | N2511  | ~$180 | −20 °C  | [link](https://www.promega.com/products/rna-analysis/rnase-inhibitor-rna-protection/rnasin-ribonuclease-inhibitor/)                     |

:::

:::{warning} S30 kit storage temperature is inconsistent between sources
Two source materials tables give different storage temperatures for the same Promega L1020 kit: **−65 °C** in the Chicago-side table and **−80 °C** in the London-side table. The table above carries the −65 °C figure as transcribed. Confirm against the current Promega product page before relying on either (London questionnaire, Q9).
:::
