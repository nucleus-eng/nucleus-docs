---
title: "Reporter: LacZ"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The LacZ Reporter Module produces β-galactosidase (LacZ), an enzyme that hydrolyzes the chromogenic substrate chlorophenol red-β-D-galactopyranoside (CPRG) from a yellow compound into a magenta/red product, giving a colorimetric readout visible to the naked eye. It is the shared colorimetric reporter across the DevCells cascades, paired with a different sensing Module in each; sensor-specific behavior is on that Module's own page.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{figure} cprg-color-change-agarose.png
:name: fig-lacz-cprg-agarose
:align: center
:width: 80%
Photograph of the LacZ/CPRG colorimetric reaction in an agarose hydrogel well, taken at t = 0, 30, and 60 min (left to right) after PLA1-triggered rupture of CPRG-loaded SUVs. CPRG starts yellow and turns magenta/purple as LacZ converts it. Samuel Chen, Liu Lab (Chicago Node).
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

:::{table} Composition of the LacZ Reporter Module in Base Cytosol at reaction concentration.
:label: comp-lacz-cytosol

| Component | Stock Concentration | Final Concentration |
| --- | --- | --- |
| [Base Cytosol](../base-cytosol/spec.md) | — | 1× |
| LacZ DNA template (`T7pro-LacZ-T7term`) | prep-specific | 5 nM |
| CPRG | 10 mg/mL | 0.6 mg/mL |
| RNase inhibitor | 40 000 U/mL | 2000 U/mL |

LacZ may also be added as a purified protein rather than expressed from DNA to 20 U/mL final.
:::

:::{attention} Imputed from the theophylline-gated reaction
@Editor(chicago): no reaction expressing LacZ standalone is on record. Every value above is taken from the theophylline-gated reaction on the [Theophylline Detector](../detector-theophylline/spec.md#detector-theophylline-reference-composition) spec with the analyte removed — that reaction is this Module plus a riboswitch, so what remains when theophylline is dropped is this Module. Two things that follow are assumptions, not measurements: that a constitutive LacZ construct wants the same 5 nM as a riboswitch-gated one, and that the London constructs (`T7pro-LacZ-T7term`, `T7pro-UTR1-G10_leader_peptide-LacZ-T7term`) behave like the Chicago one at that concentration. Confirm both with the Node that runs it.

In the synthetic cells documented here LacZ is not expressed at all — it is added as purified enzyme at 20 U/mL. Where the two sit relative to each other is the composing system's choice; see the [aTc Sensing Cell](../atc-sensing-cell/spec.md), which encapsulates the enzyme and keeps 0.5 mM CPRG outside.
:::

::::

:::::

## Substrate

CPRG (chlorophenol red-β-D-galactopyranoside, Roche 10884308001) is the substrate used in all confirmed LacZ results on this page. It is prepared fresh or stored at -20 °C in water at 10 mg/mL, and is converted by LacZ from a yellow compound into a magenta/red product, readable by absorbance near 570 nm to 575 nm or by eye.

# Expected Behavior
LacZ converts CPRG on contact, so a reaction colocalizing both is in the ON state.

## Cytosols

Absorbance at 570 nm over time shows CPRG converts from yellow to a red product faster in the presence of 1.5 mM theophylline than without it, under the reaction on the [Theophylline Detector](../detector-theophylline/spec.md#detector-theophylline-reference-composition) spec. This is a single preliminary experiment (one condition each, no replicates reported) demonstrating that the LacZ/CPRG reaction functions in Nucleus Cytosol — it is not a characterization of LacZ turnover independent of a switch, and no bulk-cytosol data exists yet for LacZ expressed standalone (without a sensor fused upstream).

:::{figure} cytosol-theophylline-kinetics.png
:label: fig-lacz-theophylline-kinetics
:width: 75%

Kinetics for colorimetric conversion of CPRG into a red product, absorbance at 570 nm, with and without theophylline.
:::


## Cells

See [tetR-aTc Detector](../detector-tetr-atc/spec.md) for the confirmed synthetic cell/hydrogel-relevant encapsulation data: `TetO-PLA1` co-encapsulated with LacZ, CPRG outside, in a synthetic cell, showing a graded absorbance response (575 nm) to aTc dose across three DNA/TetR combinations. 

(reporter-lacz-requirements)=
# Requirements

A system that has to *switch* ON requires that LacZ protein is not colocalized with CPRG until the reporter is turned ON, and the trigger must be the only route for these components to come in contact. 

How to achieve this requirement is a design choice. Here are three example solutions:

- **Enclose the enzyme.** The [aTc Cascade](../atc-cascade/spec.md) encapsulates LacZ and leaves CPRG outside. LacZ can then be released upon lysis using [PLA1 Lysis Module](../effector-pla1/spec.md).
- **Enclose the substrate.** The [pH Cascade](../ph-cascade/spec.md) and [London Cascade](../london-cascade/spec.md) load CPRG into a [Substrate SUV](../substrate-cprg-suv/spec.md) and leave LacZ in the exterior. CPRG can then be released upon lysis using [PLA1 Lysis Module](../effector-pla1/spec.md).
- **Supply no enzyme at all.** The [Theophylline Sensing Cell](../theophylline-sensing-cell/spec.md) co-encapsulates CPRG and DNA encoding LacZ rather than LacZ protein.

LacZ activity MAY be inhibited by theophylline, thus do not use with [Theophylline Sensing Module](../detector-theophylline/spec.md). 

:::{attention} The mechanism behind LacZ and theophylline incompatibility is not established.
The constraint is usually explained as theophylline directly inhibiting the LacZ/CPRG conversion, "even at very low amounts." That explanation is unsupported and partly contradicted:

- The one bulk figure available shows 1 mM and 2 mM theophylline making the LacZ/CPRG reaction roughly **twice as fast**, not slower. Riboswitch activation producing more LacZ could mask direct enzyme inhibition, so both effects can coexist — but no figure showing inhibition has been located.
- @Editor(chicago): supporting titration data is reported to exist but has not been located. Confirm with the Chicago Node.
- Every verbal source is hedged, and one literature spot-check found only weak, millimolar-range inhibition, which is inconsistent with the "very low amounts" framing.

See [Theophylline Sensing Module § Requirements](../detector-theophylline/spec.md#detector-theophylline-requirements) for more details.
:::

:::{warning} Gels requiring UV crosslinking require post-exposure addition of CPRG
CPRG is UV-sensitive: preloaded into liposomes it photobleaches under the UV exposure used to crosslink a photodeveloped gel, by either route — this does **not** affect agarose, alginate, or ULGA hydrogel embedding, where the standard two-liposome preloaded-CPRG method works as expected. This is a process-level incompatibility specific to the PEG-norbornene chemistry, not a defect in the LacZ/CPRG reaction itself.

**Confirmed workaround:** for PEG-norbornene hydrogels, add CPRG as a free dye *after* UV crosslinking, rather than preloading it into liposomes, and pre-add LacZ to the gel instead of encapsulating it. This gives a color change in PEG-4-NB where preloading does not. The gel it was demonstrated in is PEG4Nb 5 000 g/mol monomer, PEG4SH 2 000 g/mol crosslinker, and LAP 294.21 g/mol photoinitiator.
:::

:::{caution} Exterior LacZ leakage confounds the readout
LacZ (or LacZ/CPRG product) leaking to the exterior of a lysed liposome can confound readout, independent of the photobleaching issue above. A proteinase K treatment (50 °C for 10 min, then 40 °C for 1 h, then spin down) was proposed as a mitigation for exterior LacZ leakage after PLA1-triggered lysis. The protocol is documented at [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md). Treat it as proposed, not validated: no result from running it has been reported.
:::

# Implementations

- [Chicago DevCell](../../implementations/chicago-devcell/main.md): supplies the colorimetric readout for the aTc and pH cascades. LacZ is encapsulated as purified enzyme alongside the sensing construct rather than expressed from DNA, and converts CPRG released from a neighboring Substrate SUV. Sources: [`chicago-theophylline-lacz`](https://devnotes.nucleus.engineering/articles/019e0431-5045-7f14-a4f9-d3795e22bcdd), [`chicago-colorimetric-validation`](https://devnotes.nucleus.engineering/articles/019b140b-4888-74fd-b8c9-c2b79a64601e).
- [London DevCell](../../implementations/london-devcell/main.md): supplies the colorimetric readout for the AHL cascade. LacZ is the enzyme in use and XylE/C23DO is the proposed alternative, not yet run. Both linear-DNA formats have been synthesized and templates prepared; no encapsulated result has been reported. Source: [`london-lacz-xyle-module`](https://devnotes.nucleus.engineering/articles/019b1403-bfd4-7694-820f-9e9f0e732e13).

# Processes

- [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) — reduces background from LacZ outside the liposome, before the readout
- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) — the CPRG conversion this Module performs

- [ULGA Hydrogel Embedding](../../processes/embed-ulga-hydrogel/main.md) — the London hydrogel format

# Credits

Developed by [Maram Naji](https://orcid.org/0000-0003-1409-4194) (Chicago Node, Lucks Lab), [Charlie Newell](https://orcid.org/0000-0001-9208-7542) and Michael Booth (London Node, Booth Lab), Mary Kelly (Chicago Node, Kamat Lab), and Samuel Chen (Chicago Node, Liu Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
