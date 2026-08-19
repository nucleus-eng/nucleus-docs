---
title: "S30 Lysate"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

S30 Lysate is a commercial *E. coli* cell-free expression system used as the cytosol-equivalent Module for the London chassis. It plays the same role that [Base Cytosol](../base-cytosol/spec.md) plays for the Nucleus/PURE-based chassis: a ready-to-use transcription-translation mix that, once combined with a POPC membrane, produces a functional synthetic cell. Unlike Base Cytosol, S30 Lysate is not assembled in-house from purified components — it is a supplied crude lysate (Promega E. coli S30 Extract System for Circular DNA, catalog `L1020`), used together with the kit's own premix and amino acid mix.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. Composition and performance data below come from a single internal encapsulation experiment ([London Module 3](#source-note)) and have not been independently replicated or validated.
:::

(source-note)=
:::{note}
**Source of this page.** All data below is drawn from `Demo Status - London.docx` (London Module 3, "Encapsulation" — contributors Ion Ioannou, Jonah McDonald), the internal London demo-status writeup covering S30/POPC encapsulation. No dedicated S30 Lysate DevNote exists yet in `2026-CERN-OHL-P/devnotes/`.
:::

```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart LR
    S30Premix["S30 Premix<br/>(kit, supplied)"]
    S30Extract["S30 Extract<br/>(kit, supplied)"]
    AAMix["Amino Acid Mix<br/>(kit, supplied)"]
    SensorPlasmid(["Sensor Plasmid<br/>Module Spec"])
    S30Premix & S30Extract & AAMix --> J(( ))
    SensorPlasmid -.-> J
    J -->|"Combine"| S30Lysate["S30 Lysate"]

    style S30Premix fill:#6B7280,color:#ffffff,stroke:#4B5563
    style S30Extract fill:#6B7280,color:#ffffff,stroke:#4B5563
    style AAMix fill:#6B7280,color:#ffffff,stroke:#4B5563
    style SensorPlasmid fill:#6B7280,color:#ffffff,stroke:#4B5563
    style S30Lysate fill:#6B7280,color:#ffffff,stroke:#4B5563
    style J fill:none,stroke:none
```

*S30 Lysate is combined from three supplied kit components — premix, extract, and amino acid mix — rather than assembled from individually-purified parts. A sensor plasmid (e.g. `pLux-GFP` from the [AHL Sensing Module](../ahl-sensing-cell/spec.md)) is added per experiment; it is not part of the kit. This is the same role that Base Cytosol's PMix/SMix/ribosome/tRNA assembly plays for the Nucleus/PURE chassis — see [Base Cytosol](../base-cytosol/spec.md).*

:::{attention}
No published schematic exists for this mechanism; the diagram above is a simplified summary, not a reproduction of a lab figure. Replace with a proper schematic once one is available, following [Base Cytosol](../base-cytosol/spec.md)'s `schematic.png` as the precedent.
:::

## Reference Composition

S30 Lysate itself is supplied as a kit (premix + extract + amino acid mix) rather than formulated from individual reagents, so there is no analog to Base Cytosol's PMix/SMix breakdown. The table below reproduces the one documented reaction recipe: the synthetic cell **inner solution** used in the S30/POPC encapsulation experiment, which includes sucrose for osmotic matching to the outer buffer and RNase inhibitor. It is not a general-purpose bulk-reaction recipe — no bulk (non-encapsulated) S30 composition has been documented yet.

:::{table} Composition of the S30/POPC synthetic cell inner solution, as used in the encapsulation experiment.
:label: comp-s30-inner-solution

| Component | Stock Concentration | Final Concentration | Condition 1 (− DNA, µL) | Condition 2 (+ DNA, µL) |
| --- | --- | --- | --- | --- |
| S30 premix | supplied (kit) | 1× | 10 | 10 |
| S30 extract | supplied (kit) | 1× | 7.5 | 7.5 |
| Amino acid mix (pooled) | supplied (kit) | 1× | 2.5 | 2.5 |
| Sensor plasmid (pLux-GFP DNA) | 1056 ng/µL | 37 ng/µL | 0 | 0.95 |
| Sucrose | 2 M | 276 mM | 3.75 | 3.75 |
| RNase inhibitor | 40 000 U/mL | 1840 U/mL | 1.25 | 1.25 |
| Nuclease-free water | — | — | 2.2 | 1.25 |

:::

:::{attention}
The `pLux-GFP` sensor plasmid is part of the AHL Sensing Module, not S30 Lysate itself — it is included here only because it is what the source encapsulation experiment used to read out expression. It is listed as an in-house Elani-lab construct with no DNA-repo file reference yet; treat any future Designs table for the AHL Sensing Module as the authoritative source for that construct.
:::

## Materials

:::{table} Kit and reagents used in the S30/POPC encapsulation experiment.
:label: comp-s30-materials

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage |
| --- | --- | --- | --- | --- | --- |
| S30 lysate | E. coli S30 Extract System for Circular DNA | [Promega](https://www.promega.com/products/protein-expression/cell-free-protein-expression/e_-coli-s30-extract-system-for-circular-dna/) | L1020 | ~$650 | −65 °C |
| RNase inhibitor | Recombinant RNasin Ribonuclease Inhibitor | [Promega](https://www.promega.com/products/rna-analysis/rnase-inhibitor-rna-protection/rnasin-ribonuclease-inhibitor/) | N2511 | ~$180 | −20 °C |

:::

## Expected Behavior

S30 Lysate's expected behavior is characterized by encapsulation in the [London Membrane](../membrane-popc/spec.md) as a synthetic cell, read out with the AHL Sensing Module (LuxR/pLux → GFP). This S30 + POPC combination is the confirmed chassis-assembly step for the London chassis (per the module-integration status tracking: both the POPC-membrane and S30-lysate legs of that assembly are marked confirmed, as of the 2026-08-14 integration review).

**synthetic cell encapsulation route.** Three phase-transfer protocols for encapsulating S30 lysate in POPC synthetic cells were compared: the Elani-lab protocol with Optiprep, the same protocol without Optiprep, and the Schroeder protocol (JoVE, 2020). The Elani protocol with Optiprep gave the cleanest, highest-yield encapsulation; without Optiprep it gave fewer synthetic cells; the Schroeder protocol gave very low yield and was dropped. Adding 5 mg/mL BSA and raising Optiprep to 15% increased yield by roughly 1.5× (~42 vs. ~27 synthetic cells ≥5 µm per field). synthetic cell counts held steady through 37 °C incubation, so membrane stability was not the yield bottleneck.

**Optiprep blocks expression.** Optiprep-containing synthetic cells stayed round and abundant through 48 h (mean 80, then 66 synthetic cells per field at 1 h and 48 h) but gave no reporter signal at either timepoint. With membrane stability and plasmid dose (80 ng/µL) both ruled out as causes, the block appears to sit in expression itself. The leading interpretation is that Optiprep above ~5% of the inner solution suppresses cell-free expression, and both the 10% and 15% conditions tested exceed that threshold.

**Dropping Optiprep restores expression.** Without Optiprep in the inner solution, the encapsulated AHL sensor expresses GFP on induction: green fluorescence appears in synthetic cells across all imaged fields, with liposome-associated puncta co-localizing with round liposomes, consistent with an active cell-free reaction inside the liposome.

:::{caution}
**Not yet controlled.** The Optiprep-free expression result above has no minus-AHL or no-DNA negative controls yet, and no biological replicates. Treat the GFP signal as promising but unattributed until those controls are run — the source document explicitly lists both as outstanding ("Controls ... are still needed to attribute the signal, and biological replicates remain to be added").
:::

## Protocols

synthetic cell fabrication follows an Elani-lab mineral-oil phase-transfer protocol (per the source document). The shared method is documented in [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md), and the London-specific lipid composition on [London Membrane](../membrane-popc/spec.md). A dedicated encapsulation DevNote is still outstanding.

:::{tip}
**Possible protocol citations — unconfirmed.** The devnote at `2026-CERN-OHL-P/devnotes/london-quorum-sensing-polymersome/main.md` (a related but distinct London effort using diblock-copolymer polymersomes, not S30 lysate) cites Elani-lab phase-transfer literature that plausibly underlies the "Elani-lab phase-transfer protocol" referenced above:

- Contini, C., Hu, W. & Elani, Y. (2022) Manufacturing polymeric porous capsules. *Chemical Communications*. 58 (28), 4409–4419. [doi:10.1039/D1CC06565C](https://doi.org/10.1039/D1CC06565C)
- Ioannou, I.A., Monck, C., Ceroni, F., Brooks, N.J., Kuimova, M.K. & Elani, Y. (2024) Nucleated synthetic cells with genetically driven intercompartment communication. *PNAS*. 121 (36), e2404790121. [doi:10.1073/pnas.2404790121](https://doi.org/10.1073/pnas.2404790121)

This link is inferred from shared authorship (Elani lab) and shared phase-transfer method, not a citation stated in the S30 encapsulation source document itself. Confirm with the contributors (Ion Ioannou, Jonah McDonald) before treating either DOI as the citation for this protocol.

**Additional reason to confirm directly:** as of 2026-08-19 London is no longer pursuing polymersomes, so the devnote these citations were found in covers abandoned work. The papers may still be the right method references — but source them from the contributors, not from that devnote.
:::

## Implementations

S30 Lysate is used, encapsulated in POPC, as the chassis for the London demo's AHL-sensing liposome and downstream London Cascade. See [London Chassis](../london-chassis/spec.md) and [London Cascade](../london-cascade/spec.md).
