---
title: "Detector: 3OC6-HSL (EsaR)"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The EsaR Detector Module senses the bacterial quorum signal 3-oxo-C6-HSL and starts transcription of a downstream gene in response. EsaR is a repressor that binds the EsaO operator, which sits between a T7 promoter and the target gene. EsaR blocks T7 RNA polymerase from transcribing. Adding 3-oxo-C6-HSL releases EsaR from the DNA, initiating gene expression by derepressing transcription. 

:::{figure} xref:devnote-esar#fig-esar-sensing
:name: fig-detector-esar-mechanism
:align: center
:width: 70%

Schematic representation of EsaO/EsaR-dependent transcriptional regulation. EsaR binds the EsaO box and blocks T7 RNA polymerase from transcribing an mNeonGreen reporter. When 3-oxo-C6-HSL binds, EsaR leaves the DNA and transcription resumes.
:::

:::{note} EsaR is a repressor, despite its entry in UniProt.
[UniProt P54293](https://www.uniprot.org/uniprotkb/P54293/entry) titles the entry for EsaR "Transcriptional activator protein EsaR" for the *Pantoea stewartii* subsp. *stewartii* protein, 249 residues. Despite this, EsaR is a repressor; refer to the UniProt entry for the sequence, not for the mechanism.
:::

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. Several quantities below are still open — see the note under Expected Behavior.
:::

# Reference Composition

EsaR is added to the reaction as a protein. It is first expressed in its own cell-free reaction (3 h at 37 °C, held at 4 °C until use) then pre-incubated with the EsaO-containing template before being added to the working reaction. 

:::::{tab-set}

::::{tab-item} DNA

:::{table} Linear templates. All three are amplified by PCR and cleaned up before use.
:label: comp-detector-esar-constructs

The operator `[EsaO]2` is two EsaO sites in tandem, one base apart. Each site is the same 19 bp box, `CCTGTACTATAGTGCAGGT`, at positions 62–80 and 82–100. The single-site construct carries one copy of that box at 62–80. 

| **Name** | **Length (bp)** | **Role** | **File** |
| --- | --- | --- | --- |
| `T7-EsaR(D91G)-T7term` | 1118 | Expresses the repressor. The repressor is the point mutant D91G which is shown to have stronger repression than wild type. | [pT7-EsaR-D91G-linear.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/detector-esar/pT7-EsaR-D91G-linear.gb) |
| `T7-[EsaO]2-mNG-T7term` | 1118 | Reporter with two operator sites. The reference reporter | [pT7-EsaO-EsaO-mNG-linear.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/detector-esar/pT7-EsaO-EsaO-mNG-linear.gb) |
| `T7-[EsaO]-mNG-T7term` | 1098 | Reporter with one operator site. | [pT7-EsaO-mNG-linear.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/detector-esar/pT7-EsaO-mNG-linear.gb) |

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
| `T7-[EsaO]2-mNG-T7term` | 10 ng/µL | 0.1 nM | 0.43 |
| Pre-expressed EsaR(D91G) reaction | — | — | 14.00 |
| Nuclease-free water | — | — | 3.13 |
| **Total** | | | **65.00** |

:::

::::

:::::

# Expected Behavior

## Cytosols

3-oxo-C6-HSL binds EsaR and turns on expression of the target gene. This module was characterized using a fluorescent reporter ([mNeonGreen](../reporter-mneongreen/spec.md)).

:::{figure} xref:devnote-esar#fig-20260925-fold
:name: fig-detector-esar-fold
:align: center
:width: 70%

Steady-state fold change (with versus without 3-oxo-C6-HSL), for the one-operator and two-operator DNA templates at (0.1, 0.5, 1, and 3) nM. At 0.5 nM the ON state is ~ 1.8-fold higher than the OFF state.
:::

**Repression fails when the reporter template is in excess.** Titrating repressor (volume of pre-reaction) with a fixed DNA template (10 ng/µL) found no difference between the induced and uninduced states. Reversing the titration, i.e., titrating the DNA template with a fixed repressor, recovers repression. This system does not show repression above 1 nM DNA template. At 0.1 nM the two-operator reporter gives about 2-fold and the one-operator reporter about 1.5-fold.

**Yield does not fall when the DNA template is reduced.** Reactions at roughly a tenth of the usual DNA template concentration reach fluorescence yields comparable to the constitutively expressed control. The likely reason is that each dose of pre-expressed repressor also carries over unspent energy and transcription and translation factors, so adding repressor adds capacity as well.

**Longer pre-incubation of the repressor and the DNA template increases difference in ON and OFF states.** A 15 min incubation gives about 2-fold in the titration experiments. Extending it to 1 h gives about 3-fold in the magnesium sweep, with individual replicates between 2.2 and 4.2 (see [the magnesium figure](#fig-detector-esar-mg-fold)).

**Magnesium does not improve dynamic range, and too much reduces it.** Supplementing the repressor–reporter incubation step with (0, 5, or 10) mM magnesium does not change the dynamic range of the detector. At 20 mM, the dynamic range roughly halves due almost entirely to a lower induced state.

:::{figure} xref:devnote-esar#fig-20261001-mg-sweep-fold
:name: fig-detector-esar-mg-fold
:align: center
:width: 55%

Fold change (+3-oxo-C6-HSL / −3-oxo-C6-HSL) for the two-operator reporter at 0, 5 and 10 mM added magnesium, after a 1 h pre-incubation of repressor and DNA at 37 °C. Error bars show standard deviation across two replicate wells.
:::

@Editor: the 20 mM arm was run but is not plotted, and the DevNote text says Mg did not alter the dynamic range at any concentration tested. Plot the 20 mM arm and correct that sentence. The raw file gives a fold change of 1.75 at 20 mM against 3.0 to 3.4 at 0, 5 and 10 mM.

**More repressor template lowers the OFF state but costs yield in the ON state.** Pre-expressed repressor carries over its own template at about 3.4 nM. Adding 5.3 nM more EsaR template, for 8.7 nM in total, raises the fold change from 2.8 to about 3.8. The induced state falls roughly four-fold, because expressing more repressor diverts resources away from the reporter.

:::{figure} xref:devnote-esar#fig-20261007-fold
:name: fig-detector-esar-template-competition
:align: center
:width: 65%

Fold change (+3-oxo-C6-HSL / −3-oxo-C6-HSL) at 0.1 nM sensor DNA, with and without 5.3 nM added EsaR template (n = 3 wells). Error bars show standard deviation.
:::

@Editor: the DevNote's figure and platemap name the single-operator reporter, and its composition table names the two-operator one. State which construct this result is for.

**A lower reaction temperature increases the dynamic range.** Running the reaction at 25 °C overnight in a thermocycler instead of at 37 °C for 3 h gives about 5.8-fold, after a 1 h pre-incubation of repressor and DNA. The likely reason is that at a lower temperature both EsaR–DNA binding is strengthened and T7 transcription is slowed, which limits expression from any repressed template.

:::{figure} xref:devnote-esar#fig-20261008-overnight
:name: fig-detector-esar-overnight
:align: center
:width: 55%

Background-corrected fluorescence for 0.1 nM two-operator reporter DNA after overnight incubation at 25 °C, with and without 5 µM 3-oxo-C6-HSL (n = 3 wells).
:::

@Editor: the three replicate values behind this figure are typed into the notebook cell and no raw file for the overnight read is in the DevNote folder. Add the raw file.

**How the repressor is prepared changes the result, so the two preparations are not interchangeable.** Expressing the repressor for 3 h at 37 °C and for 17 h at 30 °C give the same fold change at each reporter dose, but the longer preparation lowers yield in both ON and OFF states. The likely cause is byproducts accumulating over the longer incubation (e.g., inorganic phosphate).

## Cells

This module works inside a synthetic cell. The two-operator reporter was encapsulated in GUVs at 0.1 nM with pre-expressed repressor, and 3-oxo-C6-HSL was supplied in the outer solution at 5 µM. GUVs in the induced wells are noticeably brighter than the uninduced ones.

GUVs were made by emulsion transfer. POPC was dried under nitrogen, dried further under vacuum for at least two hours, resuspended in 500 µL mineral oil and sonicated at room temperature for about 20 min. The inner solution was 20 µL. 200 µL of the lipid-in-oil mixture was added onto it and pipetted up and down nine times, and the emulsion was layered onto 250 µL of outer solution. GUVs were spun at 9000 g for 20 min at 15 °C.

For this run the repressor was pre-expressed from template at 24 nM, double the usual, giving a final repressor-reaction concentration of 5 nM. The reporter was held with the pre-expressed repressor for about 1 h at 37 °C before encapsulation.

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).

Requires the repressor to be supplied as protein, e.g., expressed in a separate reaction beforehand.

Requires the DNA template at or below 0.5 nM. Above 1 nM the reporter is in excess of the repressor and no repression is seen.

Requires the analyte to reach the repressor. 3-oxo-C6-HSL crosses a POPC membrane well enough to induce an encapsulated reaction from the outer solution, so no membrane pore is needed.

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
