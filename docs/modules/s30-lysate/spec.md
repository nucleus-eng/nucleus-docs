---
title: "S30 Lysate"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

S30 Lysate is a commercially available *E. coli* cell-free expression system with undefined composition. S30 Lysate and [Base Cytosol](../base-cytosol/spec.md) are not drop-in replacements for one another. Base Cytosol supplies T7 RNA polymerase and transcribes T7-driven constructs; S30 Lysate carries *E. coli*'s native machinery and transcribes sigma-70-driven ones. A Module moves between the two only if its construct carries the matching promoter, which is the condition stated under Requirements.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. 
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
@Editor(london): no expected behavior is recorded — what the lysate expresses, in what assay, over what time and at what temperature (for example, "expresses X ng/µL deGFP over 6 h at 30 °C") — and no characterization data such as a positive-control cell-free reaction. Confirm with the London Node.
:::

# Requirements

Requires a circular DNA template driven by an *E. coli* sigma-70 promoter (e.g. [Detector: AHL](../detector-3oc6-hsl/spec.md)) and an RNase inhibitor.

:::{attention} Which DNA presentation goes into the reaction is not recorded
The kit is supplied for circular DNA, and this documentation calls the London constructs plasmids throughout. But the sequence files for those constructs are the linear presentation, supplied as G-blocks or clonal DNA, and the same parts also exist as glycerol stocks in a pET-Kan vector. That is one part in two physical forms, and only one of them matches what the kit asks for.

The distinction has bench consequences: linear DNA is exposed to exonuclease activity in an *E. coli* extract in a way circular DNA is not.

@Editor(london): confirm whether reactions receive the linear construct or the pET-Kan plasmid, and if linear, whether anything is done to protect it.
::: For encapsulated use, additionally requires a membrane (e.g. [London Membrane](../membrane-popc/spec.md)).

Not compatible with Optiprep in the inner solution above ~5%; use sucrose for density matching instead (e.g. [London Chassis](../london-chassis/spec.md)).

:::{caution} Optiprep may block expression. 
Optiprep-containing synthetic cells stayed round and abundant through 48 h (mean 80, then 66 synthetic cells per field at 1 h and 48 h) but gave no reporter signal at either timepoint. With membrane stability and plasmid dose (80 ng/µL) both ruled out as causes, the block appears to sit in expression itself. The leading interpretation is that Optiprep above ~5% of the inner solution suppresses cell-free expression, and both the 10% and 15% conditions tested exceed that threshold. Without Optiprep in the inner solution, the encapsulated AHL sensor expresses GFP on induction: green fluorescence appears in synthetic cells across all imaged fields, with liposome-associated puncta co-localizing with round liposomes, consistent with an active cell-free reaction inside the liposome.

**Not yet controlled.** The Optiprep-free expression result above has no minus-AHL or no-DNA negative controls yet, and no biological replicates. Treat the GFP signal as promising but unattributed until those controls are run.
:::

# Implementations

- [London DevCell](../../implementations/london-devcell/main.md): S30 Lysate is the cytosol of the London quorum-sensing demo.

# Processes

No process page builds this Module: S30 Lysate is supplied as a kit. See [Materials](#s30-lysate-materials) for the catalog entry.

(s30-lysate-materials)=
# Materials

:::{table} Kit and reagents used in the S30/POPC encapsulation experiment.
:label: comp-s30-materials

| Name            | Product                                       | Manufacturer | Part # | Price | Storage | Link                                                                                                                                     |
| --------------- | --------------------------------------------- | ------------ | ------ | ----- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| S30 Lysate      | *E. coli* S30 Extract System for Circular DNA | Promega      | L1020  | ~$650 | −80 °C  | [link](https://www.promega.com/products/protein-expression/cell-free-protein-expression/e_-coli-s30-extract-system-for-circular-dna/)   |
| RNase Inhibitor | Recombinant RNasin Ribonuclease Inhibitor     | Promega      | N2511  | ~$180 | −20 °C  | [link](https://www.promega.com/products/rna-analysis/rnase-inhibitor-rna-protection/rnasin-ribonuclease-inhibitor/)                     |

:::

# Credits

Developed by Ion Ioannou and Jonah McDonald (London Node, Elani Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
