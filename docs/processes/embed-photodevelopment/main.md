---
title: "Embedding: Photodevelopment"
subtitle: "Process"
status: draft
---

# Overview

Photodevelopment crosslinks a light-sensitive polymer precursor into a gel only where light falls, so the gel's geometry comes from a projected image rather than from its container. It is the route Nucleus uses when populations have to be held apart in defined regions rather than dispersed through one matrix.

It is one of the three routes under [Embedding](../embed-hydrogel/main.md), and the only one that illuminates what it sets. Neither [Embedding: Ionic Crosslinking](../embed-ionic-crosslinking/main.md) nor [Embedding: Thermal Setting](../embed-thermal-setting/main.md) exposes its contents to light at all.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Two chemistries, and only one is used
PEG-norbornene is the route the aTc path uses. No DevCells demo uses PEGDA, because it "destroys the vesicles" (Group Meeting, Chicago Node, 2026-09-11).

The PEGDA material, protocol and bill of materials below are not maintained.
:::

:::{warning} The exposure bleaches CPRG, on both chemistries
This route exposes the payload to UV. The source is 405 nm, and a source in that range emits UV along with it, so [CPRG](../../modules/substrate-cprg-suv/spec.md) cannot be pre-loaded into liposomes present during crosslinking. The side-by-side comparison behind this — exposed sample visibly bleached against an unexposed control — was run on the PEG-norbornene chemistry.

The workaround inverts the order: pre-add LacZ to the gel, crosslink, then add CPRG as a free dye. That path does not use the Substrate SUV module, so it is a different cascade rather than the same one in a different gel.

The constraint does not apply to the ionic or thermal routes, which use no light.
:::

# Protocol

## Both chemistries

Both run the same four steps. What changes between them is what goes into step 1 and how long step 3 takes.

- [ ] Dissolve the precursor in an aqueous buffer, and add the PEG4SH crosslinker and the LAP photoinitiator. Both chemistries use PEG4SH.
- [ ] Protect the solution from light until the moment of patterning. A photocrosslinking precursor begins to react on ambient exposure.
- [ ] Expose the pattern through a digital light processing projector at 405 nm, for a time adjusted to the precursor concentration, layer thickness and target feature size.
- [ ] Confirm the pattern by microscopy against the intended design, and confirm structural integrity by visual or mechanical inspection.

:::{attention} Neither chemistry has a recorded precursor concentration
Exposure time depends on monomer concentration, layer thickness and feature size, and none of the three is established for either chemistry. Treat the exposure figures below as the conditions of one run rather than as a specification.
:::

# The two chemistries

| | PEG-Norbornene | PEGDA |
| --- | --- | --- |
| Status | **live**, the aTc path | **canceled**: PEGDA destroys the liposomes; the liposome class is not stated |
| Mechanism | step-growth thiol-ene | radical polymerization of acrylates |
| Oxygen inhibition at the surface | less prone | prone |
| Network uniformity | more uniform | more heterogeneous |
| Exposure | 60 s at 405 nm | (15–30) s at 405 nm |

## PEG-Norbornene, the live chemistry

Crosslinks a 4-arm PEG-norbornene precursor with a PEG4SH thiol crosslinker under UV, using lithium phenyl-2,4,6-trimethylbenzoylphosphinate (LAP) as photoinitiator. Precursor composition and preparation are on [Gel: PEG-Norbornene](../../modules/gel-peg-norbornene/spec.md). Patterning runs **60 s at 405 nm**.

:::{attention} No protocol for this chemistry
The four shared steps are above. The precursor recipe and the exposure conditions specific to thiol-ene crosslinking are not established. @Editor(chicago): add the precursor recipe and the exposure conditions for thiol-ene crosslinking.
:::

### Expected Behavior

One spatial-patterning result is recorded. A block-pattern color change, first produced in agarose, was repeated with a PEG-norbornene outer gel and LacZ added on top, with the color change still visible after roughly 1.5 h.

## PEGDA, the canceled chemistry

Crosslinks poly(ethylene glycol) diacrylate into spatially defined patterns using 405 nm light through a DLP projector. Precursor is 20 wt% PEGDA575, 0.3 wt% PEG4SH and 0.03 wt% LAP in PBS — see [Gel: PEGDA](../../modules/gel-pegda/spec.md). Patterning runs (15–30) s.

An alternative version combines PEGDA with alginate to produce a patterned frame around an alginate core, multiplexing PEGDA's patternability with alginate's mechanical and functional stability.

:::{attention} PEGDA → Readout was never demonstrated at macroscopic scale
DevCell component volumes are too small to produce macroscopically visible pattern changes. Photopatterning of the PEGDA hydrogel itself was demonstrated, with tunable feature sizes and a PEGDA frame with a structurally sound alginate core. The downstream link from a patterned, DevCell-embedded hydrogel to a visible colorimetric readout was not.
:::

### The PEGDA steps

- [ ] Dissolve PEGDA monomer in PBS or DI water.
- [ ] Add LAP photoinitiator to the precursor solution.
- [ ] Mix thoroughly, protecting the solution from light until ready to pattern.
- [ ] Load the precursor solution into the patterning setup.
- [ ] Expose the desired pattern using a 405 nm DLP projector for 15 s to 30 s, adjusting exposure time for monomer concentration, feature size and layer thickness.
- [ ] For multimaterial photodevelopment, combine 1.6 wt% alginate with the precursor solution to enable a combined ionic and photo-crosslinking system, producing a patterned PEGDA frame around an alginate core.

:::{attention} Two things were never established for this chemistry
@Editor(chicago): the mold or patterning-chamber setup is not established, and neither is the ionic-crosslinking step for the alginate component of the multimaterial variant. The frame recipe and exposure times are on [Gel: Alginate](../../modules/gel-alginate/spec.md).
:::

# Materials and Equipment

<!-- vale nucleus.magnitude-unit-spacing = NO -->
:::{table} Bill of Materials
:label: bom-embed-photodevelopment
:align: center

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4-arm PEG-norbornene | Chemical | not established | — | — | — | — | |
| PEG4SH | Chemical | thiol crosslinker, both chemistries; not established | — | — | — | — | |
| LAP photoinitiator | Chemical | Lithium phenyl-2,4,6-trimethylbenzoylphosphinate | Sigma-Aldrich | 900889-1G | $172.00 | 2 °C to 8 °C (dark, photosensitive) | [link](https://www.sigmaaldrich.com/US/en/product/aldrich/900889) |
| DLP projector (405 nm) | Equipment | PRO4500-92-405 optical engine | Wintech Digital Systems Technology | PRO4500-92-405 | $2150.00 | RT | [link](https://wintechdigital.com/products/pro4500-wintech-production-ready-optical-engine/) |
| PEGDA monomer | Chemical | Poly(ethylene glycol) diacrylate. **Canceled chemistry** | Sigma-Aldrich | 437441-500ML | $165.00 | 2 °C to 8 °C | [link](https://www.sigmaaldrich.com/US/en/product/aldrich/437441) |
| PBS or DI water | Chemical | Phosphate-buffered saline or deionized water | N/A | N/A | N/A | RT | |

:::
<!-- vale nucleus.magnitude-unit-spacing = YES -->

# Quality Control

- **Pattern fidelity**: confirm by microscopy, comparing patterned feature dimensions against the intended design. Tunable feature sizes were demonstrated on the PEGDA chemistry.
- **Structural integrity**: confirm by visual or mechanical inspection.
- **Dye integrity**: if the cascade involves CPRG, confirm the dye was added after crosslinking rather than pre-loaded. See the warning above.

:::{attention} Primary data not located
@Editor(chicago): no devnote with quantitative feature-size measurements, imaging methodology, or mechanical-integrity data is available for either chemistry, so the feature-size and structural-integrity results above are not independently verified.
:::

# Requirements

Requires a 405 nm light source, normally a DLP projector. **This is the only one of the three Embedding routes with an equipment requirement beyond ordinary labware.**

Requires the PEG4SH crosslinker and the LAP photoinitiator, on either chemistry.

**Requires that nothing UV-sensitive is present during crosslinking.** See the warning above.

# Modules

- [Gel: PEG-Norbornene](../../modules/gel-peg-norbornene/spec.md) — the live chemistry
- [Gel: PEGDA](../../modules/gel-pegda/spec.md) — canceled

# Credits

PEG-norbornene developed by the Chicago Node. PEGDA developed by Ojaswita Pant (Chicago Node, Truby Lab).
