---
title: "Photodevelopment, PEG-Norbornene"
status: draft
---

# Overview

Photodevelopment, PEG-Norbornene crosslinks a 4-arm PEG-norbornene precursor with a PEG4SH thiol crosslinker under UV, using lithium phenyl-2,4,6-trimethylbenzoylphosphinate (LAP) as photoinitiator. It is one of the two routes under [Photodevelop Gel](../photodevelop-gel/photodevelop-gel-main.md); see that page for the steps the two share, and [Photodevelopment, PEGDA](../photodevelop-pegda/main.md) for the other.

Step-growth thiol-ene addition gives a more uniform network than PEGDA's chain-growth acrylate polymerization and is less prone to oxygen inhibition at the gel surface.

:::{attention} 🚧 Draft
This page is a stub. The chemistry and its one confirmed incompatibility are recorded; the procedure is not. It cannot be run from this page.
:::

:::{warning} This route bleaches CPRG
CPRG pre-loaded into liposomes photobleaches during this gel's UV crosslinking step. A side-by-side comparison shows the exposed sample visibly bleached against an unexposed control. The effect is confirmed for PEG-norbornene and is stated **not** to apply to PEGDA, agarose, alginate or ULGA — see [LacZ Reporter](../../modules/reporter-lacz/spec.md).

The confirmed workaround inverts the order: pre-add LacZ to the gel, crosslink, then add CPRG as a free dye afterwards. That path does not use the [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md) module at all, so it is a different cascade rather than the same one in a different gel.
:::

# Materials and Equipment

:::{attention} Not established
No precursor concentration, arm ratio, crosslinker ratio, photoinitiator concentration, exposure time or light source is recorded for this route. PEG4SH has no sourced entry on any page — it is the crosslinker for both routes and is missing from the [Photodevelopment, PEGDA](../photodevelop-pegda/main.md) bill of materials as well.

@Editor(chicago): supply the precursor composition and exposure conditions before this page is used at the bench.
:::

| Name | Category | Product | Manufacturer | Part # |
| --- | --- | --- | --- | --- |
| 4-arm PEG-norbornene | Chemical | not established | — | — |
| PEG4SH | Chemical | thiol crosslinker, shared with the PEGDA route; not established | — | — |
| LAP photoinitiator | Chemical | Lithium phenyl-2,4,6-trimethylbenzoylphosphinate | Sigma-Aldrich | 900889-1G |

# Protocol

:::{attention} No protocol is recorded
The four shared steps are on [Photodevelop Gel](../photodevelop-gel/photodevelop-gel-main.md). What this page would add — the precursor recipe and the exposure conditions specific to thiol-ene crosslinking — does not exist in any source available to this documentation.
:::

# Quality Control

- **Pattern fidelity**: confirm by microscopy, comparing patterned feature dimensions against the intended design.
- **Structural integrity**: confirm by visual or mechanical inspection.
- **Dye integrity**: if the cascade involves CPRG, confirm the dye was added after crosslinking rather than pre-loaded. See the warning above.

# Expected Behavior

One spatial-patterning result is recorded. A block-pattern color change, first produced in agarose, was repeated with a PEG-norbornene outer gel and LacZ added on top, with the color change still visible after roughly 1.5 h.

# Modules

- [Gel: PEG-Norbornene](../../modules/gel-peg-norbornene/spec.md)

# Credits

Developed by the Chicago Node.
