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

1. **Chicago node** — LacZ is used two ways: fused directly downstream of the theophylline riboswitch on a single bulk-cytosol validation construct (`pT7-theophylline-LacZ`, internally `pMN066`), and as a separate co-encapsulated reporter alongside a `TetO-PLA1` construct in the confirmed 2026-08-14 aTc Cascade GUV result (see [tetR-aTc Detector](../detector-tetr_atc/spec.md) for that data). Sources: [`devnotes/chicago-theophylline-lacz`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-theophylline-lacz), [`devnotes/chicago-colorimetric-validation`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-colorimetric-validation).
2. **London node** — LacZ is one of two candidate reporter enzymes (alongside XylE) for the London colour-change module, in two linear-DNA formats (`T7pro-LacZ-T7term` and a higher-expression `T7pro-UTR1-G10_leader_peptide-LacZ-T7term` variant). As of that devnote, LacZ was reported as synthesized, with templates prepared, but no GUV-encapsulated result had yet been reported. Source: [`devnotes/london-lacz-xyle-module`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/london-lacz-xyle-module).

Because both node lines use the same enzyme (LacZ) against the same substrate (CPRG), this page treats them as one shared Module, cited from each node's Implementation pages rather than duplicated across them.

:::::{tab-set}

::::{tab-item} Schematic

:::{figure} cprg-color-change-agarose.png
:align: center
:width: 80%
LacZ/CPRG colorimetric reaction in an agarose hydrogel well, photographed at t = 0, 30, and 60 min (left to right) after PLA1-triggered rupture of CPRG-loaded SUVs. CPRG starts yellow and turns magenta/purple as LacZ converts it. Source: 2026-08-14 DevCells status-meeting slide, "Color change in patterned agarose hydrogel can be spatially confined," Samuel Chen, Liu Lab.
:::

:::{note}
This photo shows the LacZ/CPRG reaction in the patterned-agarose demonstration, not the specific Chicago or London constructs on this page. It is included as a representative depiction of the underlying color-change mechanism (yellow → magenta/purple) shared by both node lines.
:::

::::

::::{tab-item} Designs

:::{attention} Not yet in `nucleus-eng/DNA`
No LacZ-encoding construct referenced by either node has a corresponding file in the [Nucleus DNA repository](https://github.com/nucleus-eng/DNA) as of this writing (checked `detectors/` and `reporters/`; none found). The Chicago bulk-cytosol construct `pT7-theophylline-LacZ` (`pMN066`) fuses LacZ downstream of the theophylline riboswitch rather than expressing it standalone, so even once submitted it would not represent a bare LacZ reporter part. The London constructs (`T7pro-LacZ-T7term`, `T7pro-UTR1-G10_leader_peptide-LacZ-T7term`) are reported as synthesized in the source devnote but no sequence file or DNA-repo submission is cited. Do not link to a placeholder or guess a filename — flag for follow-up so a standalone LacZ construct can be submitted to `nucleus-eng/DNA` before this table can cite a real sequence file.
:::

| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-theophylline-LacZ` (`pMN066`) | not verified | not yet in `nucleus-eng/DNA` |
| `T7pro-LacZ-T7term` | not verified | not yet in `nucleus-eng/DNA` |
| `T7pro-UTR1-G10_leader_peptide-LacZ-T7term` | not verified | not yet in `nucleus-eng/DNA` |

::::

:::::

## Substrate

CPRG (chlorophenol red-β-D-galactopyranoside, Roche 10884308001) is the substrate used in all confirmed LacZ results on this page. It is prepared fresh or stored at -20 °C in water at 10 mg/mL, and is converted by LacZ from a yellow compound into a magenta/red product, readable by absorbance near 570 nm to 575 nm or by eye.

## Cytosols

### Reference Composition

The only bulk-cytosol reaction data available characterizes LacZ fused downstream of the theophylline riboswitch, not LacZ expressed standalone. In a 10 µL Nucleus Cytosol reaction with `pT7-theophylline-LacZ` (`pMN066`) at 5 nM sensor DNA and CPRG at 0.6 mg/mL final concentration, incubated at 37 °C in a platereader:

:::{table} Reaction composition (Chicago node, bulk cytosol)
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

### Expected Performance

Absorbance at 570 nm over time shows CPRG converts from yellow to a red product faster in the presence of 1.5 mM theophylline than without it, under the reaction above. This is a single preliminary experiment (one condition each, no replicates reported) demonstrating that the LacZ/CPRG reaction functions in Nucleus Cytosol — it is not a characterization of LacZ turnover independent of a switch, and no bulk-cytosol data exists yet for LacZ expressed standalone (without a sensor fused upstream).

:::{hint} Figure not yet migrated
:class: dropdown
The source devnote includes a kinetics figure (`pT7_theo_lacZ.png`, absorbance at 570 nm over time for the −/+ theophylline conditions). It has not been copied into this page — see [`devnotes/chicago-theophylline-lacz`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-theophylline-lacz) for the original.
:::

A separate devnote ([`chicago-colorimetric-validation`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-colorimetric-validation)) frames a broader goal of testing all sensor/reporter combinations (including LacZ) for at least 2-fold signal change with minimal leak, but reports no completed reaction data of its own — its DNA constructs are listed as "Awaiting from Twist." Treat it as milestone framing, not a second data point.

## Cells

:::{note}
See [tetR-aTc Detector](../detector-tetr_atc/spec.md) for the confirmed GUV/hydrogel-relevant encapsulation data: `TetO-PLA1` co-encapsulated with LacZ and CPRG in a GUV, showing a graded absorbance response (575 nm) to aTc dose across three DNA/TetR combinations. That result is the most advanced encapsulated use of this Module as of 2026-08-14 and is not duplicated here.
:::

For the London node, LacZ encapsulation is still at the milestone-planning stage: the source devnote's Milestone 3 ("Encapsulate reporter system in GUVs") lists open risks — substrate/product interference with vesicle generation, and encapsulation efficiency limiting visible pigment — with no success-criteria data reported yet. Do not read the London line as having reached the same readiness as the Chicago aTc Cascade result above.

# Requirements

:::{attention} Theophylline interferes with the LacZ/CPRG reaction itself
Per the 2026-08-14 DevCells status meeting, theophylline interacts with and somewhat inhibits the LacZ/CPRG colorimetric reaction independent of whether a theophylline-responsive switch is present — described in the source transcript as affecting conversion "even at very low amounts" of theophylline. This is a hedged, source-quoted finding, not a fully characterized mechanistic claim, and it has not yet been written up in a formal devnote. Because this Module supplies the shared LacZ/CPRG readout for both the [Theophylline Sensing Module](../detector-theophylline/spec.md) and the [aTc Sensing Module](../detector-tetr_atc/spec.md), the two sensing Modules cannot be present together in the same cascade on the current Chicago Cascade design — see each sensing Module's own Requirements section for that mutual-exclusion decision. A general Nucleus compatibility matrix covering other module pairs is explicitly out of scope here.
:::

:::{attention} PEG-norbornene hydrogel chemistry requires post-crosslinking CPRG addition
CPRG preloaded into vesicles photobleaches under the UV exposure used to crosslink PEG-norbornene (PEG4Nb) hydrogels — this does **not** affect agarose, alginate, or ULGA hydrogel embedding, where the standard two-vesicle preloaded-CPRG method works as expected. This is a process-level incompatibility specific to the PEG-norbornene chemistry, not a defect in the LacZ/CPRG reaction itself.

**Confirmed workaround:** for PEG-norbornene hydrogels, add CPRG as a free dye *after* UV crosslinking, rather than preloading it into vesicles, and pre-add LacZ to the gel instead of encapsulating it. A 2026-08-14 status-meeting slide deck ("LacZ Induced Color Change in PEG-4-NB requires post UV light addition of CPRG," Mary Kelly, Kamat Lab) documents a controlled four-condition well comparison confirming this: +CPRG/+LacZ/−UV stays purple (baseline color intact); +CPRG/+LacZ/+UV goes clear (crosslinking bleaches the CPRG color); +LacZ/+UV/−CPRG is clear (no substrate, no color expected); +LacZ/+UV/+CPRG-added-after-crosslinking goes pink/red (the workaround recovers color). This directly confirms the transcript's photobleaching report with photographic evidence, and matches the PEG4Nb hydrogel composition described elsewhere in the same deck (PEG4Nb 5 000 g/mol monomer, PEG4SH 2 000 g/mol crosslinker, LAP 294.21 g/mol photoinitiator).
:::

:::{note} Exterior LacZ leakage — mitigation in progress, tracked separately
A related but distinct issue: LacZ (or LacZ/CPRG product) leaking to the exterior of a lysed vesicle can confound readout, independent of the photobleaching issue above. A proteinase K treatment (50 °C for 10 min, then 40 °C for 1 h, then spin down) was proposed as a mitigation for exterior LacZ leakage after PLA1-triggered lysis. This protocol is not yet written up as its own devnote — treat it as an action item, not a validated process, and see the PLA1 Lysis Module page (pending) for its eventual home rather than duplicating it here.
:::

# Implementations

- [tetR-aTc Detector](../detector-tetr_atc/spec.md) — confirmed GUV-level encapsulation of LacZ with `TetO-PLA1` and CPRG, the aTc Cascade's readout.
- [Theophylline Sensing Module](../detector-theophylline/spec.md) — bulk-cytosol validation of the LacZ/CPRG reaction fused downstream of the theophylline riboswitch.
- [XylE / C23DO Reporter](../reporter-xyle/spec.md) — sibling colorimetric reporter, used as an alternative or orthogonal readout in the same cascades.
- No Implementation page exists yet for the London LacZ/XylE colour-change module, the Chicago Cascade, or the London Cascade. Each is planned per the current DevCells documentation-authoring plan; link them here once authored.

# Credits

- Chicago node bulk-cytosol result: see [`devnotes/chicago-theophylline-lacz`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-theophylline-lacz) for contributor attribution.
- Chicago node GUV/hydrogel encapsulation result (Mary Kelly, Kamat Lab): see the 2026-08-14 DevCells status meeting materials.
- Schematic-tab photo of the LacZ/CPRG color change in patterned agarose (Samuel Chen, Liu Lab): see the 2026-08-14 DevCells status meeting materials.
- London node module design: see [`devnotes/london-lacz-xyle-module`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/london-lacz-xyle-module) for contributor attribution.
