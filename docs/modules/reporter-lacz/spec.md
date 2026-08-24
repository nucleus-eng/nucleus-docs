---
title: "Reporter: LacZ"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The LacZ Reporter Module produces β-galactosidase (LacZ), an enzyme that hydrolyzes the chromogenic substrate chlorophenol red-β-D-galactopyranoside (CPRG) from a yellow compound into a magenta/red product, giving a colorimetric readout visible to the naked eye. It is the shared colorimetric reporter behind both the Chicago and London DevCells cascades: Chicago pairs it with the Theophylline Sensing Module and the aTc Sensing Module, and London pairs it with a quorum-sensing input as one of two candidate reporter enzymes (alongside [XylE / C23DO](../reporter-xyle/spec.md)). This page covers the reporter enzyme and its LacZ/CPRG chemistry; sensor-specific behavior is documented on each sensing Module's own page and cited here rather than duplicated.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

Two source lines both use LacZ, at different levels of readiness, and should not be conflated:

1. **Chicago Node** — LacZ is used two ways: fused directly downstream of the theophylline riboswitch on a single bulk-cytosol validation construct (`pT7-theophylline-LacZ`, internally `pMN066`), and as a separate co-encapsulated reporter alongside a `TetO-PLA1` construct in the confirmed 2026-08-14 aTc Cascade synthetic cell result (see [tetR-aTc Detector](../detector-tetr_atc/spec.md) for that data). Sources: [`devnotes/chicago-theophylline-lacz`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-theophylline-lacz), [`devnotes/chicago-colorimetric-validation`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-colorimetric-validation).
2. **London Node** — LacZ is one of two candidate reporter enzymes (alongside XylE) for the London colour-change module, in two linear-DNA formats (`T7pro-LacZ-T7term` and a higher-expression `T7pro-UTR1-G10_leader_peptide-LacZ-T7term` variant). As of that devnote, LacZ was reported as synthesized, with templates prepared, but no synthetic-cell-encapsulated result had yet been reported. Source: [`devnotes/london-lacz-xyle-module`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/london-lacz-xyle-module).

Because both node lines use the same enzyme (LacZ) against the same substrate (CPRG), this page treats them as one shared Module, cited from each node's Implementation pages rather than duplicated across them.

:::{figure} cprg-color-change-agarose.png
:name: fig-lacz-cprg-agarose
:align: center
:width: 80%
Photograph of the LacZ/CPRG colorimetric reaction in an agarose hydrogel well, taken at t = 0, 30, and 60 min (left to right) after PLA1-triggered rupture of CPRG-loaded SUVs. CPRG starts yellow and turns magenta/purple as LacZ converts it. Source: 2026-08-14 DevCells status-meeting slide, "Color change in patterned agarose hydrogel can be spatially confined," Samuel Chen, Liu Lab.
:::

:::{note}
This photo shows the LacZ/CPRG reaction in the patterned-agarose demonstration, not the specific Chicago or London constructs on this page. It is included as a representative depiction of the underlying color-change mechanism (yellow → magenta/purple) shared by both node lines.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA

:::{attention} Not yet in `nucleus-eng/DNA`
No LacZ-encoding construct referenced by either node has a corresponding file in the [Nucleus DNA repository](https://github.com/nucleus-eng/DNA) as of this writing (checked `detectors/` and `reporters/`; none found). The Chicago bulk-cytosol construct `pT7-theophylline-LacZ` (`pMN066`) fuses LacZ downstream of the theophylline riboswitch rather than expressing it standalone, so even once submitted it would not represent a bare LacZ reporter part. The London constructs (`T7pro-LacZ-T7term`, `T7pro-UTR1-G10_leader_peptide-LacZ-T7term`) are reported as synthesized in the source devnote but no sequence file or DNA-repo submission is cited. Do not link to a placeholder or guess a filename — flag for follow-up so a standalone LacZ construct can be submitted to `nucleus-eng/DNA` before this table can cite a real sequence file.
:::

| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-theophylline-LacZ` (`pMN066`) | not verified | not yet in `nucleus-eng/DNA` |
| `T7pro-LacZ-T7term` | not verified | not yet in `nucleus-eng/DNA` |
| `T7pro-UTR1-G10_leader_peptide-LacZ-T7term` | not verified | not yet in `nucleus-eng/DNA` |

::::

::::{tab-item} Cytosol

The only bulk-cytosol reaction data available characterizes LacZ fused downstream of the theophylline riboswitch, not LacZ expressed standalone. In a 10 µL Nucleus Cytosol reaction with `pT7-theophylline-LacZ` (`pMN066`) at 5 nM sensor DNA and CPRG at 0.6 mg/mL final concentration, incubated at 37 °C in a platereader:

:::{table} Reaction composition (Chicago Node, bulk cytosol)
| Component | Stock Concentration | Final concentration | − theophylline [µL] | + 1.5 mM theophylline [µL] |
| --- | --- | --- | --- | --- |
| SMix | 3.33× | 1× | 3 | 3 |
| PMix | 15 mg/mL | 1.80 mg/mL | 1.2 | 1.2 |
| Ribosomes | 10 µM | 1.8 µM | 1.8 | 1.8 |
| tRNA | 35 mg/mL | 3.5 mg/mL | 1 | 1 |
| `pT7-theophylline-LacZ` (`pMN066`) DNA template | 49.55 nM | 5 nM | 1 | 1 |
| CPRG | 10 mg/mL | 0.6 mg/mL | 0.6 | 0.6 |
| Theophylline | 10 mM | 1.5 mM | 0.95 | 0.95 |
| RNase Inhibitor | 40000 U/mL | 2000 U/mL | 0.5 | 0.5 |
| Water | | | 0.54 | 0 |
:::

::::

:::::

## Substrate

CPRG (chlorophenol red-β-D-galactopyranoside, Roche 10884308001) is the substrate used in all confirmed LacZ results on this page. It is prepared fresh or stored at -20 °C in water at 10 mg/mL, and is converted by LacZ from a yellow compound into a magenta/red product, readable by absorbance near 570 nm to 575 nm or by eye.

# Expected Behavior

## Cytosols

Absorbance at 570 nm over time shows CPRG converts from yellow to a red product faster in the presence of 1.5 mM theophylline than without it, under the reaction above. This is a single preliminary experiment (one condition each, no replicates reported) demonstrating that the LacZ/CPRG reaction functions in Nucleus Cytosol — it is not a characterization of LacZ turnover independent of a switch, and no bulk-cytosol data exists yet for LacZ expressed standalone (without a sensor fused upstream).

:::{hint} Figure not yet migrated
:class: dropdown
The source devnote includes a kinetics figure (`pT7_theo_lacZ.png`, absorbance at 570 nm over time for the −/+ theophylline conditions). It has not been copied into this page — see [`devnotes/chicago-theophylline-lacz`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-theophylline-lacz) for the original.
:::

A separate devnote ([`chicago-colorimetric-validation`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-colorimetric-validation)) frames a broader goal of testing all sensor/reporter combinations (including LacZ) for at least 2-fold signal change with minimal leak, but reports no completed reaction data of its own — its DNA constructs are listed as "Awaiting from Twist." Treat it as milestone framing, not a second data point.

## Cells

:::{note}
See [tetR-aTc Detector](../detector-tetr_atc/spec.md) for the confirmed synthetic cell/hydrogel-relevant encapsulation data: `TetO-PLA1` co-encapsulated with LacZ and CPRG in a synthetic cell, showing a graded absorbance response (575 nm) to aTc dose across three DNA/TetR combinations. That result is the most advanced encapsulated use of this Module as of 2026-08-14 and is not duplicated here.
:::

For the London Node, LacZ encapsulation is still at the milestone-planning stage: the source devnote's Milestone 3 ("Encapsulate reporter system in synthetic cells") lists open risks — substrate/product interference with liposome generation, and encapsulation efficiency limiting visible pigment — with no success-criteria data reported yet. Do not read the London line as having reached the same readiness as the Chicago aTc Cascade result above.

# Requirements

**Requires a lysis effector to release the substrate.** LacZ and CPRG produce no signal while the substrate stays inside its liposome, so this Module does not function on its own — it needs an upstream effector that breaches the substrate compartment on cue. In every cascade documented here that effector is the [PLA1 Lysis Module](../effector-pla1/spec.md), and the substrate is the [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md).

This is a Requirement of the readout, not a component of any sensing cell. A Sensing Cell that expresses PLA1 satisfies this requirement; it does not thereby contain the reporter.

Because this Module supplies the shared LacZ/CPRG readout for both the [Theophylline Sensing Module](../detector-theophylline/spec.md) and the [aTc Sensing Module](../detector-tetr_atc/spec.md), those two sensing Modules must not be co-encapsulated in the same reaction. That requirement is settled — the 2026-08-14 meeting resolved to state it on each sensing Module page. A general Nucleus compatibility matrix covering other module pairs is out of scope here; the meeting scoped that as a platform-level decision.

:::{attention} The mechanism behind that requirement is not established
The constraint is usually explained as theophylline directly inhibiting the LacZ/CPRG conversion, "even at very low amounts." That explanation is unsupported and partly contradicted:

- The one bulk figure available shows 1 mM and 2 mM theophylline making the LacZ/CPRG reaction roughly **twice as fast**, not slower. Riboswitch activation producing more LacZ could mask direct enzyme inhibition, so both effects can coexist — but no figure showing inhibition has been located.
- @Editor: supporting titration data is reported to exist but has not been located. Confirm with the Chicago Node.
- Every verbal source is hedged, and one literature spot-check found only weak, millimolar-range inhibition, which is inconsistent with the "very low amounts" framing.

Cite the requirement and the decision behind it. Do not cite the inhibition mechanism as characterized. Full evidence on both sides is on [Theophylline Sensing Module § Requirements](../detector-theophylline/spec.md#requirements).
:::

:::{attention} PEG-norbornene hydrogel chemistry requires post-crosslinking CPRG addition
CPRG preloaded into liposomes photobleaches under the UV exposure used to crosslink PEG-norbornene (PEG4Nb) hydrogels — this does **not** affect agarose, alginate, or ULGA hydrogel embedding, where the standard two-liposome preloaded-CPRG method works as expected. This is a process-level incompatibility specific to the PEG-norbornene chemistry, not a defect in the LacZ/CPRG reaction itself.

**Confirmed workaround:** for PEG-norbornene hydrogels, add CPRG as a free dye *after* UV crosslinking, rather than preloading it into liposomes, and pre-add LacZ to the gel instead of encapsulating it. This gives a color change in PEG-4-NB where preloading does not. The gel it was demonstrated in is PEG4Nb 5 000 g/mol monomer, PEG4SH 2 000 g/mol crosslinker, and LAP 294.21 g/mol photoinitiator.
:::

:::{note} Exterior LacZ leakage — mitigation in progress, tracked separately
A related but distinct issue: LacZ (or LacZ/CPRG product) leaking to the exterior of a lysed liposome can confound readout, independent of the photobleaching issue above. A proteinase K treatment (50 °C for 10 min, then 40 °C for 1 h, then spin down) was proposed as a mitigation for exterior LacZ leakage after PLA1-triggered lysis. The protocol is documented at [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md). Treat it as proposed, not validated: no result from running it has been reported, and a standalone devnote is still an open action item from the 2026-08-14 meeting. See also the [PLA1 Lysis Module](../effector-pla1/spec.md).
:::

# Implementations

- [Chicago DevCell](../../implementations/chicago-devcell/main.md): supplies the colorimetric readout for the aTc, pH and theophylline cascades.
- [London DevCell](../../implementations/london-devcell/main.md): supplies the colorimetric readout for the AHL cascade.

# Credits

Developed by [Maram Naji](https://orcid.org/0000-0003-1409-4194) (Chicago Node, Lucks Lab) — bulk-cytosol validation.

Developed by [Charlie Newell](https://orcid.org/0000-0001-9208-7542) and Michael Booth (London Node, Booth Lab) — London colour-change module design.

Developed by Mary Kelly (Chicago Node, Kamat Lab) and Samuel Chen (Chicago Node, Liu Lab).
