---
title: "S30 Lysate"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

S30 Lysate is a commercially available *E. coli* cell-free expression system with undefined composition. S30 Lysate may be used in place of [Base Cytosol](/docs/mo/base-cytosol/spec) for compatible modules.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. Composition and performance data below come from a single internal encapsulation experiment ([London Module 3](#source-note)) and have not been independently replicated or validated.
:::

# Reference Composition

S30 Lysate itself is supplied as a kit (premix + extract + amino acid mix) rather than formulated from individual reagents (Promega, Cat. No. N2511 @Claude link to product inline).

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

## Materials

:::{table} Kit and reagents used in the S30/POPC encapsulation experiment.
:label: comp-s30-materials

| Name            | Product                                     | Manufacturer (@Claude: move links to separate link column; see [main](../../processes/make-trna/main.md) for an example well formatted table) | Part # | Price | Storage                                 |
| --------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ----- | --------------------------------------- |
| S30 Lysate      | E. coli S30 Extract System for Circular DNA | [Promega](https://www.promega.com/products/protein-expression/cell-free-protein-expression/e_-coli-s30-extract-system-for-circular-dna/)      | L1020  | ~$650 | −65 °C @Claude: check this. likely -80C |
| RNase Inhibitor | Recombinant RNasin Ribonuclease Inhibitor   | [Promega](https://www.promega.com/products/rna-analysis/rnase-inhibitor-rna-protection/rnasin-ribonuclease-inhibitor/)                        | N2511  | ~$180 | −20 °C                                  |

:::

## Expected Behavior

S30 Lysate's expected behavior is characterized by expressing a reporter module (e.g., [deGFP](../reporter-degfp/spec.md)).

:::{attention} Needs more detail
@Claude: pull out for London Questionnaire
Verbal description of expected behavior (i.e., does what with what assay; e.g., "expresses X ng/uL deGFP over 6 hrs at 30 C")
characterization data (e.g., positive control cell-free reaction)
:::

@Claude: these two blocks should be pulled out to a Requirements section (this is an incompatibility, not Expected Behavior, thus captured as requirements)

**Optiprep blocks expression.** Optiprep-containing synthetic cells stayed round and abundant through 48 h (mean 80, then 66 synthetic cells per field at 1 h and 48 h) but gave no reporter signal at either timepoint. With membrane stability and plasmid dose (80 ng/µL) both ruled out as causes, the block appears to sit in expression itself. The leading interpretation is that Optiprep above ~5% of the inner solution suppresses cell-free expression, and both the 10% and 15% conditions tested exceed that threshold. Without Optiprep in the inner solution, the encapsulated AHL sensor expresses GFP on induction: green fluorescence appears in synthetic cells across all imaged fields, with liposome-associated puncta co-localizing with round liposomes, consistent with an active cell-free reaction inside the liposome.

:::{caution}
**Not yet controlled.** The Optiprep-free expression result above has no minus-AHL or no-DNA negative controls yet, and no biological replicates. Treat the GFP signal as promising but unattributed until those controls are run — the source document explicitly lists both as outstanding ("Controls ... are still needed to attribute the signal, and biological replicates remain to be added").
:::

# Requirements
@Claude: pull requirements into here.

## Implementations

S30 Lysate is used, encapsulated in POPC, as the chassis for the London demo's AHL-sensing liposome and downstream London Cascade. See [London Chassis](../london-chassis/spec.md) and [London Cascade](../london-cascade/spec.md).
