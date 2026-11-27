---
title: "Detector: 3OC6-HSL (EsaR)"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

(detector-esar-overview)=
# Overview

The EsaR Detector Module initiates transcription of a target gene in response to the bacterial quorum signal 3-oxo-C6-HSL. EsaR is a repressor that binds the EsaO operator, which when placed sits between a promoter and the target gene can reversibly repress transcription. When EsaR binds the operator sequence, it blocks T7 RNA polymerase from transcribing. When EsaR allosterically binds 3-oxo-C6-HSL, it releases from the DNA and derepresses transcription of the target gene. 

:::{figure} xref:devnote-esar#fig-esar-sensing
:name: fig-detector-esar-mechanism
:align: center
:width: 70%

Schematic representation of EsaO/EsaR-dependent transcriptional regulation. EsaR binds the EsaO box and blocks T7 RNA polymerase from transcribing an mNeonGreen reporter. When 3-oxo-C6-HSL binds, EsaR leaves the DNA and transcription resumes. Figure from [Quorum Sensing in Nucleus Cytosol using EsaO/EsaR Transcriptional Regulation](https://devnotes.nucleus.engineering/articles/01a108c6-4719-7833-92af-daf6f91ed06a).
:::

:::{note} EsaR is a repressor, despite its entry in UniProt.
[UniProt P54293](https://www.uniprot.org/uniprotkb/P54293/entry) titles the entry for EsaR "Transcriptional activator protein EsaR" for the *Pantoea stewartii* subsp. *stewartii* protein, 249 residues. Despite this, EsaR is a repressor; refer to the UniProt entry for the sequence, not for the mechanism.
:::

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. Several quantities below are still open — see the note under Expected Behavior.
:::

(detector-esar-reference-composition)=
# Reference Composition

EsaR is added to the reaction as a protein. It is first expressed from DNA in its own cell-free reaction (3 h at 37 °C, held at 4 °C until use) then pre-incubated with the EsaO-containing DNA template before being added to the working reaction to allow the repressor to bind the operator site. 

:::::{tab-set}

::::{tab-item} DNA

:::{table} Linear templates. All three are amplified by PCR and cleaned up before use.
:label: comp-detector-esar-constructs

The operator `[EsaO]2` is two EsaO sites in tandem, one base apart. Each site is the same 19 bp box, `CCTGTACTATAGTGCAGGT`, at positions 62–80 and 82–100. The single-site construct carries one copy of that box at 62–80. 

| **Name** | **Length (bp)** | **Role** | **File** |
| --- | --- | --- | --- |
| `T7-EsaR(D91G)-T7term` | 1118 | Expresses EsaR. Contains a single amino acid substitution (D91G) shown to give stronger repression than wild type. | [pT7-EsaR-D91G-linear.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/detector-esar/pT7-EsaR-D91G-linear.gb) |
| `T7-[EsaO]2-mNG-T7term` | 1118 | Reporter with two operator sites. The reference reporter | [pT7-EsaO-EsaO-mNG-linear.gb](https://devnotes.nucleus.engineering/articles/01a108c6-4719-7833-92af-daf6f91ed06a#seq-esao2-mng) |
| `T7-[EsaO]-mNG-T7term` | 1098 | Reporter with one operator site. | [pT7-EsaO-mNG-linear.gb](https://devnotes.nucleus.engineering/articles/01a108c6-4719-7833-92af-daf6f91ed06a#seq-esao-mng) |

:::

:::{note} mNeonGreen may be patented
The reporter used in the templates above, mNeonGreen, may be covered by a United States patent.
:::

Annotated sequence maps are in the DevNote: [T7-EsaR(D91G)-T7term](https://devnotes.nucleus.engineering/articles/01a108c6-4719-7833-92af-daf6f91ed06a#seq-esar-d91g), [T7-[EsaO]2-mNG-T7term](https://devnotes.nucleus.engineering/articles/01a108c6-4719-7833-92af-daf6f91ed06a#seq-esao2-mng) and [T7-[EsaO]-mNG-T7term](https://devnotes.nucleus.engineering/articles/01a108c6-4719-7833-92af-daf6f91ed06a#seq-esao-mng).

::::

::::{tab-item} Cytosol

:::{table} Composition of the Module in Nucleus Cytosol, per 65 µL. 

:label: comp-detector-esar-cytosol

| Component | Stock concentration | Final concentration | Volume (µL) |
| --- | --- | --- | --- |
| [Protein Mix (PMix)](../pmix/spec.md) | 15 µg/µL (8.33×) | 1.8 µg/µL | 7.80 |
| [Small Molecule Mix (SMix)](../smix/spec.md) | 3.33× | 1× | 19.70 |
| Ribosomes | 10 µM (5.55×)       | 1.8 µM                 | 11.82 |
| tRNA      | 35 µg/µL (10×)      | 3.5 µg/µL              |6.50 |
| RNase Inhibitor | 40 000 U/mL (20×) | 2000 U/mL | 1.62 |
| `T7-[EsaO]2-mNG-T7term` | 14.5 nM (10 ng/µL) | 0.1 nM | 0.43 |
| Pre-expressed EsaR(D91G) reaction | — | — | 14.00 |
| Nuclease-free water | — | — | 3.13 |
| **Total** | | | **65.00** |

:::

::::

:::::

(detector-esar-expected-behavior)=
# Expected Behavior

## Cytosols

3-oxo-C6-HSL binds EsaR and turns on expression of the target gene. This module was characterized using a fluorescent reporter, mNeonGreen.

:::{figure} xref:devnote-esar#fig-20260925-fold
:name: fig-detector-esar-fold
:align: center
:width: 70%

Steady-state fold change (with versus without 3-oxo-C6-HSL), for the one-operator and two-operator DNA templates at (0.1, 0.5, 1, and 3) nM. At 0.5 nM the ON state is ~ 1.8-fold higher than the OFF state.
:::

**Repression fails when the reporter template is in excess.** Titrating repressor (volume of pre-reaction) with a fixed DNA template (10 ng/µL) found no difference in output signal (mNeonGreen) between the ON and OFF states. Reversing the titration, i.e., varying the DNA template concentration with a fixed repressor, recovers repression below 1 nM DNA template. At 0.1 nM the two-operator reporter gives about 2-fold and the one-operator reporter about 1.5-fold.

**Expression level does not fall when the DNA template is reduced.** Sensor DNA at (0.5, 1 and 3) nM matches or exceeds the fluorescence of the constitutive mNeonGreen control at 15.6 nM, a 5- to 30-fold lower template concentration. Carryover of unspent energy components and transcription and translation factors from the pre-expressed repressor reaction may supply the extra capacity.

**Longer pre-incubation of the repressor and the DNA template increases difference in ON and OFF states.** A 15 min pre-incubation gives about 2-fold dynamic range between states in the titration experiments, whereas a 1 h pre-incubation gives about 3-fold, with individual replicates between 2.2- and 4.2-fold (see [below](#fig-detector-esar-mg-fold)).

**Magnesium does not improve dynamic range, and too much reduces it.** Supplementing the repressor–reporter pre-incubation step with (0, 5, or 10) mM magnesium does not change the dynamic range of the detector. At 20 mM, the dynamic range roughly halves due almost entirely to a lower induced state.

:::{figure} xref:devnote-esar#fig-20261001-mg-sweep-fold
:name: fig-detector-esar-mg-fold
:align: center
:width: 55%

Fold change (+3-oxo-C6-HSL / −3-oxo-C6-HSL) for the two-operator reporter at (0, 5 and 10) mM added magnesium, after a 1 h pre-incubation of repressor and DNA at 37 °C. Error bars show standard deviation across two replicate wells.
:::

@Editor: the 20 mM arm was run but is not plotted, and the DevNote text says Mg did not alter the dynamic range at any concentration tested. Plot the 20 mM arm and correct that sentence. The raw file gives a fold change of 1.75-fold at 20 mM against 3.0- to 3.4-fold at (0, 5 and 10) mM.

**More repressor template lowers the OFF state but costs yield in the ON state.** Pre-expressed repressor carries over its own template at about 3.4 nM. Adding 5.3 nM more EsaR template, for 8.7 nM in total, raises the fold change from 2.8 to about 3.8. The induced state falls roughly four-fold, likely because expressing more repressor diverts resources away from expressing the reporter.

:::{figure} xref:devnote-esar#fig-20261007-fold
:name: fig-detector-esar-template-competition
:align: center
:width: 65%

Fold change (+3-oxo-C6-HSL / −3-oxo-C6-HSL) at 0.1 nM sensor DNA, with and without 5.3 nM added EsaR template (n = 3 wells). Error bars show standard deviation.
:::

**A lower reaction temperature increases the dynamic range.** Running the final cytosol reaction at 25 °C overnight in a thermocycler instead of at 37 °C for 3 h gives about 5.8-fold, using a 1 h pre-incubation of repressor and DNA. Likely both EsaR–DNA binding is strengthened and T7 transcription is slowed at a lower temperature, which would lower the OFF state.

:::{figure} xref:devnote-esar#fig-20261008-overnight
:name: fig-detector-esar-overnight
:align: center
:width: 55%

Background-corrected fluorescence for 0.1 nM two-operator reporter DNA after overnight incubation at 25 °C, with and without 5 µM 3-oxo-C6-HSL (n = 3 wells).
:::

**How the repressor is prepared changes the total yield.** Pre-expressing the repressor for 3 h at 37 °C versus for 17 h at 30 °C give the same fold change at each reporter dose, but the longer preparation lowers yield for both ON and OFF states. The likely cause is byproducts accumulating over the longer incubation (e.g., inorganic phosphate).

## Cells

The two-operator reporter was encapsulated in GUVs at 0.1 nM with pre-expressed repressor. 3-oxo-C6-HSL was supplied in the outer solution at 5 µM. GUVs in the induced wells are noticeably brighter than the uninduced ones.

The repressor was pre-expressed from 24 nM DNA template, double the typical concentration. The reporter DNA template was then added and the mixture was incubated for about 1 h at 37 °C before encapsulation.

GUVs were made by emulsion transfer. POPC was dried under nitrogen, dried further under vacuum for at least 2 h, resuspended in 500 µL mineral oil and sonicated at room temperature for about 20 min. 200 µL of the lipid-in-oil mixture was added onto 20 µL inner solution and mixed by pipetting (9x) to emulsify. The emulsion was layered onto 250 µL of outer solution and centrifuged at 9000 g for 20 min at 15 °C.


# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).

Requires the repressor to be supplied as protein, e.g., expressed in a separate reaction beforehand.

Requires the DNA template at or below 0.5 nM. Above 1 nM the reporter is in excess of the repressor and no repression is seen.

Requires the analyte to reach the repressor. 3-oxo-C6-HSL crosses a POPC membrane well enough to induce an encapsulated reaction from the outer solution, so no membrane pore is needed.

# Processes

- [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md): makes the GUVs by emulsion transfer.

# Materials

:::{table}
:label: critical-materials

| Name | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- |
| AHSL | N-(3-Oxohexanoyl)-L-homoserine lactone | Sigma-Aldrich | K3007 | — | — | [link](https://www.sigmaaldrich.com/US/en/product/aldrich/k3007) |
| Magnesium acetate | Magnesium acetate tetrahydrate | Sigma-Aldrich | M0631-100G | $34.80 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/m0631) |
| POPC | 16:0-18:1 PC (POPC), 25 mg/mL | Avanti Research | A80557 | $435.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc) |
| Mineral oil | Mineral oil, light, BioReagent, for molecular biology | Sigma-Aldrich | M5904 | — | Room temperature | [link](https://www.sigmaaldrich.com/US/en/product/sigma/m5904) |
| RNase Inhibitor, Murine | RNase Inhibitor, Murine | NEB | M0314S | $87.00 | -25 °C to -15 °C | [link](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| Fluorescein | Fluorescein, NIST-Traceable Standard (50 µM nominal) | Invitrogen | F36915 | $554.00 | 2 °C to 8 °C, protect from light | [link](https://www.thermofisher.com/order/catalog/product/F36915) |

:::

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this specification include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Quorum Sensing in Nucleus Cytosol using EsaO/EsaR Transcriptional Regulation
:link: https://devnotes.nucleus.engineering/articles/01a108c6-4719-7833-92af-daf6f91ed06a
:footer: Charlie Newell, Manuel Bibrowski, Jonah McDonald, Niall McIntyre, Julia Purrinos de Oliveira · DevStudio 2026

![](https://pub.curvenote.com/01a1650a-b201-7bf1-8f59-f37bce646feb/public/EsaR-sensing-6354ffdd322f6b6aca0909ed8f894e30.png)
:::

::::
