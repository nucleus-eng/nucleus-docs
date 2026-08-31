---
title: "Photodevelopment, PEGDA"
subtitle: "Process"
status: draft
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

Photodevelopment, PEGDA crosslinks poly(ethylene glycol) diacrylate (PEGDA) hydrogel precursor into spatially defined patterns using 405 nm light, delivered through a digital light processing (DLP) projector. In the Chicago colorimetric readout system, this process is used to fabricate hydrogel-embedded micro-patterns (e.g., QR-code-style test patterns) intended to house DevCells with precise spatial control and low phototoxicity relative to traditional UV crosslinking. An alternative version combines PEGDA with alginate to produce a patterned frame around an alginate core, multiplexing PEGDA's patternability with alginate's mechanical and functional stability.

:::{attention} PEGDA → Readout is not yet demonstrated at macroscopic scale
DevCell component volumes are currently too small to produce macroscopically visible QR-code pattern changes. Photopatterning of the PEGDA hydrogel itself has been demonstrated (tunable feature sizes, and a PEGDA frame with a structurally sound alginate core), but the downstream link from a patterned, DevCell-embedded hydrogel to a visible colorimetric readout has not. This matches the dashed PEGDA → Readout edge in `process-dependency-diagram.md`.
:::

:::{attention} PEG-norbornene: a related, newer hydrogel chemistry — not yet a diagram node
A separate, more recently explored hydrogel chemistry, PEG-norbornene, is sometimes discussed alongside PEGDA but is chemically distinct and **not the subject of this page**:

- **PEGDA** crosslinks by chain-growth radical polymerization of the acrylate groups directly (no separate crosslinker), which is prone to oxygen inhibition at the gel surface and produces more heterogeneous networks.
- **PEG-norbornene** crosslinks by step-growth thiol-ene chemistry — 4-arm PEG-norbornene plus a PEG4SH crosslinker, with lithium phenyl-2,4,6-trimethylbenzoylphosphinate (LAP) as photoinitiator — which is less prone to oxygen inhibition.

**PEG-norbornene has no corresponding node in `process-dependency-diagram.md`** — the diagram only represents PEGDA. This is a diagram-maintenance gap, not a decision to fold PEG-norbornene into this page.

PEG-norbornene also has a real, confirmed incompatibility that does not apply to PEGDA: chlorophenol red-β-D-galactopyranoside (CPRG) pre-loaded into liposomes photobleaches during PEG-norbornene's UV crosslinking step. The confirmed workaround is to add CPRG as a free dye after crosslinking rather than pre-loading it, with LacZ pre-added to the gel. Separately, a spatial-patterning demonstration (a block-pattern color change in agarose) was repeated with a PEG-norbornene outer gel and LacZ added on top, with the color change still observed after roughly 1.5 h — relevant context for spatial patterning work generally, but it is a PEG-norbornene result, not a PEGDA one, and should not be cited as PEGDA data.
:::

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{note} Notes
:class: dropdown
:icon: false

- Exposure time (15 s to 30 s at 405 nm) needs to be adjusted based on other experimental conditions (e.g., monomer concentration, layer thickness, feature size) — no single fixed value is established.
- PEG-4SH, a step-growth thiol-ene crosslinker used with PEG-norbornene, is excluded from the Bill of Materials below — it does not belong to PEGDA's chain-growth acrylate polymerization chemistry.

::::::

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

- **PEGDA monomer (poly(ethylene glycol) diacrylate)** — Irritant to skin, eyes, and respiratory tract. Acrylates are also sensitizers with repeated exposure. Wear gloves and eye protection.
- **LAP photoinitiator (lithium phenyl-2,4,6-trimethylbenzoylphosphinate)** — Irritant; photosensitive. Handle under reduced ambient light and store in the dark.
- **405 nm light source** — Not traditional UV, but still capable of eye and skin exposure at close range from a DLP projector. Avoid direct viewing of the light path.

::::::

:::::::

# Materials and Equipment

<!-- vale nucleus.magnitude-unit-spacing = NO -->
:::{table} Bill of Materials
:label: bom-photodevelop-pegda
:align: center

| Name             | Category    | Product                                              | Manufacturer  | Part #                     | Price   | Storage                  | Link                                                                                                                                                                                                                   |
| ---------------- | ----------- | ----------------------------------------------------- | -------------- | --------------------------- | ------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PEGDA monomer     | Chemical    | Poly(ethylene glycol) diacrylate                      | Sigma-Aldrich | 437441-500ML                | $165.00 | 2 °C to 8 °C                | [link](https://www.sigmaaldrich.com/US/en/product/aldrich/437441)                                                                                                                                                    |
| LAP photoinitiator | Chemical    | Lithium phenyl-2,4,6-trimethylbenzoylphosphinate      | Sigma-Aldrich | 900889-1G                   | $172.00 | 2 °C to 8 °C (dark, photosensitive) | [link](https://www.sigmaaldrich.com/US/en/product/aldrich/900889)                                                                                                                                                    |
| DLP projector (405 nm) | Equipment | PRO4500-92-405 optical engine                        | Wintech Digital Systems Technology | PRO4500-92-405 | $2150.00 | RT                       | [link](https://wintechdigital.com/products/pro4500-wintech-production-ready-optical-engine/)                                                                                                                          |
| PBS or DI water   | Chemical    | Phosphate-buffered saline or deionized water          | N/A           | N/A                          | N/A     | RT                        |                                                                                                                                                                                                                        |

:::
<!-- vale nucleus.magnitude-unit-spacing = YES -->

:::{attention} Materials list incomplete
Patterning runs at 405 nm for (15–30) s, adjusted for the other conditions; multimaterial patterning combines PEGDA with 1.6 wt% alginate. @Editor(chicago): the PEGDA and LAP *working* concentrations and the mold or patterning-chamber setup are still not established. Only the reagents themselves and the 405 nm exposure window (15 s to 30 s) are documented.
:::

# Protocol

## Prepare PEGDA Hydrogel Precursor Solution

- [ ] Dissolve PEGDA monomer in PBS or DI water.
- [ ] Add LAP photoinitiator to the precursor solution.

:::{hint} Note
:class: simple
:icon: false
Working concentrations for PEGDA monomer and LAP in this precursor solution are not yet established — see the flag above.
:::

- [ ] Mix thoroughly, protecting the solution from light until ready to pattern.

## Photopattern with 405 nm Light

- [ ] Load the PEGDA precursor solution into the patterning setup.
- [ ] Expose the desired pattern using a 405 nm DLP projector for 15 s to 30 s, adjusting exposure time based on your specific experimental conditions (e.g., monomer concentration, feature size, layer thickness).

## Multimaterial Patterning with Alginate (optional)

- [ ] For multimaterial photopatterning, combine 1.6 wt% alginate with the PEGDA precursor solution to enable a combined ionic/photo-crosslinking system, producing a photopatterned PEGDA frame around an alginate core.

:::{hint} Note
:class: simple
:icon: false
This combined system has been used to demonstrate a PEGDA frame–alginate core construct with reasonable structural integrity. The ionic-crosslinking step for the alginate component (e.g., CaCl₂ concentration and exposure time) is not yet established.
:::

# Quality Control

- **Pattern fidelity and feature size**: Confirm by microscopy imaging, comparing patterned feature dimensions against the intended design. Tunable feature sizes have been demonstrated for PEGDA hydrogels photopatterned by this process.
- **Structural integrity (multimaterial constructs)**: For PEGDA frame–alginate core constructs, confirm structural integrity by visual and/or mechanical inspection.

:::{attention} Primary data not located
@Editor(chicago): no devnote with quantitative feature-size measurements, imaging methodology, or mechanical-integrity data for this process is available yet, so the feature-size and structural-integrity results above are not independently verified. This process's link to a macroscopically visible colorimetric readout has likewise not been demonstrated (see the dashed-edge note in the Overview).
:::

# Credits

Developed by Ojaswita Pant (Chicago Node, Truby Lab).

# Downloads

::::{grid} 1 1 1 1

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/photodevelop-pegda-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/photodevelop-pegda-bom.pdf>`
:::

::::

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
