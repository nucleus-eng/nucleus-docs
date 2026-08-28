---
title: "Reporter: XylE / C23DO"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The XylE / C23DO Reporter Module produces a visible color change by expressing catechol 2,3-dioxygenase (C23DO, the *xylE* gene product), which oxidises catechol (colorless) into 2-hydroxymuconate semialdehyde (yellow) and can be detectable by absorbance near (375–385) nm ([Kunz and Chapman, 1981](https://doi.org/10.1128/jb.146.1.179-191.1981)). 

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Proposed module requires validation
This module's chemistry is confirmed only at bulk-cytosol scale, with one construct, in one lab context (see Expected Behavior below). No synthetic cell/liposome encapsulation or hydrogel-embedded data exist for this reporter, and it is not part of any confirmed cascade result. Do not read this module as being at the same readiness level as its sibling [LacZ Reporter](../reporter-lacz/spec.md), which does have confirmed synthetic cell/hydrogel-level results.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA

:::{attention} Not yet in `nucleus-eng/DNA`
`pT7-TetO-catecholase` (`pMN067`) is not present in the [Nucleus DNA repository](https://github.com/nucleus-eng/DNA). A sequence file exists in the source devnote (`chicago-teto-catecholase/experiments/sequences/pMN067_T7_TetO_C23DO_entireconstruct.dna`), but per repository convention this page does not link to or copy it directly — flag for follow-up so the construct can be submitted to `nucleus-eng/DNA` before this page is used at the bench. The London-specific `T7pro-XylE-T7term` and `T7pro-UTR1-G10_leader_peptide-XylE-T7term` constructs are not yet designed at all (per the London devnote), so no equivalent DNA-table entry exists for them.
:::

| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-TetO-catecholase` (`pMN067`) | not verified | not yet in `nucleus-eng/DNA` |

::::

::::{tab-item} Cytosol

The Chicago-node construct was tested downstream of the tetR-aTc Detector at three conditions — unregulated (no TetR), regulated (TetR, no aTc), and derepressed (TetR + aTc) — in a 10 µL Nucleus Cytosol reaction with `pT7-TetO-catecholase` (`pMN067`) at 20 nM final concentration and 1 mM catechol.

:::{table} Reaction composition (Chicago Node)
| Component | Stock Concentration | Final concentration | Unregulated (µL) | Repressed (µL) | Activated (µL) |
| --- | --- | --- | --- | --- | --- |
| SMix | 3.33× | 1× | 3 | 3 | 3 |
| PMix | 15 mg/mL | 1.80 mg/mL | 1.2 | 1.2 | 1.2 |
| Ribosomes | 10 µM | 1.8 µM | 1.8 | 1.8 | 1.8 |
| tRNA | 35 mg/mL | 3.5 mg/mL | 1 | 1 | 1 |
| `pT7-TetO-catecholase` (`pMN067`) DNA template | 275.7 nM | 20 nM | 0.73 | 0.73 | 0.73 |
| Catechol | 100 mM | 1 mM | 0.2 | 0.2 | 0.2 |
| TetR | 1305.6 nM | 75 nM | 0 | 0.57 | 0.57 |
| Anhydrotetracycline (aTc) | 100 µM | 10 µM | 0 | 0 | 1 |
| RNase Inhibitor | 40 000 U/mL | 2000 U/mL | 0.5 | 0.5 | 0.5 |
| Water | | | 1.57 | 1 | 0 |
:::

:::{note} Two TetR scales, one construct
A later bulk-reaction replication re-runs the same TetR/aTc/C23DO-catechol chemistry and reports clean induced/repressed/unregulated separation, but at 500 nM and 1000 nM TetR against the 75 nM used in the reference reaction above. Both use the same construct, so these are two conditions of one design rather than two designs. The dependence of the readout on TetR concentration across that range has not been characterized.
:::

::::

:::::

(reporter-xyle-expected-behavior)=
# Expected Behavior

## Cytosols

The construct was validated in standard Nucleus Cytosol conditions with 20 nM sensor DNA, 1 mM catechol, in 10 µL reactions incubated at 37 °C in a platereader, monitored by absorbance at 385 nm. Color conversion (colorless to yellow) occurred faster and to a visually detectable level only in the activated condition (TetR + 10 µM aTc). The repressed condition (TetR, no aTc) remained visibly transparent relative to a priorly calibrated visual threshold (absorbance 1.0). 

:::{figure} cytosol-catecholase-kinetics.png
:label: fig-xyle-catecholase-kinetics
:width: 75%

Absorbance at 385 nm over time for the unregulated, regulated and derepressed conditions.
:::


## Cells

:::{caution} Missing Validation Data
No synthetic cell or hydrogel data exist for this module. 
:::

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)), and catechol as substrate.

When driven from `pT7-TetO-catecholase` (`pMN067`), additionally requires TetR and anhydrotetracycline (aTc) as the derepressing input — see the [tetR-aTc Detector](../detector-tetr-atc/spec.md).


# Implementations

- [Chicago DevCell](../../implementations/chicago-devcell/main.md): a proposed alternate colorimetric readout. The construct is `pT7-TetO-catecholase` (`pMN067`), expressing C23DO under a TetO/aTc promoter; it is validated in bulk Nucleus Cytosol and has no synthetic cell result. Source: [`chicago-teto-catecholase`](https://devnotes.nucleus.engineering/articles/019e0429-3749-72ce-a062-7d2a7cf18c20).
- [London DevCell](../../implementations/london-devcell/main.md): a proposed alternate to LacZ, in two linear-DNA formats — `T7pro-XylE-T7term` and a higher-expression `T7pro-UTR1-G10_leader_peptide-XylE-T7term` variant. The London XylE DNA is still to be designed. Source: [`london-lacz-xyle-module`](https://devnotes.nucleus.engineering/articles/019b1403-bfd4-7694-820f-9e9f0e732e13).

:::{attention} The two Nodes' constructs may not converge
@Editor(chicago): whether Chicago's `pMN067` and London's still-undesigned construct end up as the same DNA design is not established. Confirm with both Nodes before treating them as one construct.
:::

# Processes

- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) — the catechol conversion that produces the visible signal

# Credits

Developed by [Maram Naji](https://orcid.org/0000-0003-1409-4194) (Chicago Node, Lucks Lab), [Charlie Newell](https://orcid.org/0000-0001-9208-7542) and Michael Booth (London Node, Booth Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
