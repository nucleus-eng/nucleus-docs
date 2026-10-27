---
title: "Detector: 3OC6-HSL (EsaR)"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The EsaR Detector Module senses the bacterial quorum signal 3-oxo-C6-HSL and starts transcription in response. EsaR is a repressor. It binds the EsaO operator, which sits between a T7 promoter and the gene behind it, and blocks T7 RNA polymerase from transcribing that gene. Adding 3-oxo-C6-HSL releases EsaR from the DNA, and expression recovers. The Module therefore detects its analyte by derepression: the regulator is bound by default, and the analyte removes it.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. Several quantities below are still open — see the note under Expected Behavior.
:::

**The analyte has three names.** `AHL`, `AHSL` and `3-oxo-C6-HSL` all name N-(3-oxohexanoyl)-L-homoserine lactone, the same ligand.

**EsaR is a repressor, despite what the database entry is called.** [UniProt P54293](https://www.uniprot.org/uniprotkb/P54293/entry) titles the entry "Transcriptional activator protein EsaR" for the *Pantoea stewartii* subsp. *stewartii* protein, 249 residues. The protein represses, and every result below is a repression result. Read the entry for the sequence, not for the mechanism.

# Reference Composition

The repressor reaches the reaction as protein, not as a template to transcribe. It is expressed first in its own cell-free reaction, 3 h at 37 °C, then held at 4 °C until use. It is then mixed with the reporter construct and held again before that mixture enters the working reaction. Occupying the operator before transcription can start is what makes the "off" state deep; co-expressing repressor and reporter together gives a much weaker switch.

:::::{tab-set}

::::{tab-item} DNA

:::{table} Linear templates. All three are amplified by PCR and cleaned up before use.
:label: comp-detector-esar-constructs

| **Name** | **Length (bp)** | **Role** | **File** |
| --- | --- | --- | --- |
| `T7-EsaR(D91G)-T7term` | 1118 | Expresses the repressor. The repressor is the point mutant D91G | [t7-esar-d91g-t7term.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/quorum-sensing/t7-esar-d91g-t7term.gb) |
| `T7-[EsaO]2-mNG-T7term` | 1118 | Reporter with two operator sites. The reference reporter | [t7-esao2-mng-t7term.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/quorum-sensing/t7-esao2-mng-t7term.gb) |
| `T7-[EsaO]-mNG-T7term` | 1098 | Reporter with one operator site. Run alongside the two-site construct for comparison | [t7-esao-mng-t7term.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/quorum-sensing/t7-esao-mng-t7term.gb) |

:::

The operator `[EsaO]2` is two EsaO sites in tandem, one base apart. Each site is the same 19 bp box, `CCTGTACTATAGTGCAGGT`, at positions 62–80 and 82–100. The single-site construct carries one copy of that box at 62–80. The two reporters carry the same mNeonGreen coding sequence, so the 20 bp of length between them is the second operator plus the base that separates the pair.

::::

::::{tab-item} Cytosol

The reference condition is the two-operator reporter at 0.1 nM against a fixed dose of pre-expressed repressor. Mix the repressor with the reporter template and hold the mixture at 37 °C for 1 h, then add it to the rest of the reaction. Split the assembled reaction in two and add 3-oxo-C6-HSL to one half, to 5 µM final.

:::{table} Composition of the Module in Nucleus Cytosol, per 65 µL before the reaction is split, from the reporter titration. That titration used a 15 min hold; 1 h is the reference and gives the fold changes under Expected Behavior. 3-oxo-C6-HSL is added after splitting, so it is not in this column.
:label: comp-detector-esar-cytosol

| Component | Stock concentration | Final concentration | Volume (µL) |
| --- | --- | --- | --- |
| Small molecule mix | 3.33-fold | 1-fold | 19.70 |
| tRNA | 35 µg/µL (10-fold) | 3.5 µg/µL (1-fold) | 6.50 |
| Protein mix | 8.33-fold | 1-fold | 7.80 |
| Ribosomes | 10 µM (5.55-fold) | 1.8 µM (1-fold) | 11.82 |
| RNase inhibitor | 40 U/µL | 1 U/µL | 1.62 |
| `T7-[EsaO]2-mNG-T7term` | 10 ng/µL | 0.1 nM | 0.43 |
| Pre-expressed EsaR(D91G) reaction | — | — | 14.00 |
| Nuclease-free water | — | — | 3.13 |
| **Total** | | | **65.00** |

:::

The repressor arrives as about a fifth of the reaction by volume, and that volume is not inert — see Expected Behavior.

::::

:::::

# Expected Behavior

:::{attention} Three quantities are open
- The pre-expressed repressor has **no measured protein concentration**, so the ratio of repressor to reporter — the parameter that decides whether the Module works — cannot be computed from any recorded number.
- The DevNote states the reporter dose two ways, as 12.2 nM (10 ng/µL) and as 320.5 ng in 65 µL, which differ about two-fold. Its own composition table gives 10 ng/µL, which is the figure used above.
- The source states the added repressor template as both an 87-fold and a 77-fold excess over the reporter.

@Developer: settle all three with the authors before this page leaves draft.
:::

## Cytosols

3-oxo-C6-HSL binds EsaR and relieves repression of the gene behind the operator. The Module was characterized on a fluorescent reporter, mNeonGreen, read against a fluorescein ladder.

:::{figure} xref:devnote-esar#fig-20260925-fold
:name: fig-detector-esar-fold
:align: center
:width: 70%

Steady-state fold change, plus against minus 3-oxo-C6-HSL, for the one-operator and two-operator reporters at 0.1, 0.5, 1 and 3 nM. At 0.5 nM the value is n = 2, after one low outlier in the induced wells was excluded for each construct.
:::

**Repression fails when the reporter template is in excess, not because the repressor is dead.** The first titration moved the repressor against a reporter held at 10 ng/µL and found no difference between the induced and uninduced states, at either operator count. Reversing the titration — moving the reporter against a fixed repressor dose — recovers repression. Above 1 nM reporter there is no repression. At 0.1 nM the two-operator reporter gives about 2-fold and the one-operator reporter about 1.5-fold. Each gives less at 0.5 nM than at 0.1 nM.

**Yield does not fall when the reporter is cut.** Reactions at roughly a tenth of the usual template reach fluorescence yields comparable to the constitutively expressed control. The likely reason is that each dose of pre-expressed repressor also carries over unspent energy and transcription and translation factors, so adding repressor adds capacity as well.

**The Module is expected to switch more deeply the longer the repressor and the reporter are held together before the reaction starts.** A 15 min hold gives about 2-fold. Extending it to 1 h gives about 3-fold, with individual replicates between 2.2 and 4.2.

**Magnesium is not expected to improve the dynamic range, and too much reduces it.** Supplementing the repressor–reporter hold with 0, 5 or 10 mM magnesium changes the dynamic range at none of those levels. At 20 mM the dynamic range roughly halves, and the loss falls almost entirely on the induced state.

**More repressor template deepens the "off" state and costs yield.** Carrying over pre-expressed repressor also carries over its template, to about 3.4 nM. Diluting the reporter stock in repressor template rather than water adds a further 5.3 nM, bringing the total to 8.7 nM. The fold change rises from 2.8 to about 3.8. Overall fluorescence falls roughly four-fold in the induced state, because expressing more repressor diverts resources away from the reporter.

**A lower reaction temperature gives the strongest switch recorded.** Running the reaction at 25 °C overnight in a thermocycler instead of at 37 °C gives about 5.8-fold, from 19,800 against 3,400 RFU. The reasoning is that a lower temperature both strengthens EsaR–DNA binding and slows T7, which limits expression from any template that is not fully repressed.

**How the repressor is prepared changes the result, so the two preparations are not interchangeable.** Expressing the repressor for 3 h at 37 °C and for 17 h at 30 °C give the same fold change at each reporter dose, but the longer preparation lowers overall yield. The likely cause is byproducts accumulating over the longer incubation, inorganic phosphate among them. The 3 h preparation is the reference.

## Cells

The Module works inside a synthetic cell. The two-operator reporter was encapsulated in GUVs at 0.1 nM with pre-expressed repressor, and 3-oxo-C6-HSL was supplied in the outer solution at 5 µM. GUVs in the induced wells are markedly brighter than the uninduced ones, so the encapsulated Module senses an analyte that starts outside the membrane.

GUVs were made by emulsion transfer. POPC was dried under nitrogen, dried further under vacuum for at least two hours, resuspended in 500 µL mineral oil and sonicated at room temperature for about 20 min. The inner solution was 20 µL. 200 µL of the lipid-in-oil mixture was added onto it and pipetted up and down nine times, and the emulsion was layered onto 250 µL of outer solution. GUVs were spun at 9000 g for 20 min at 15 °C.

For this run the repressor was pre-expressed from template at 24 nM, double the usual, giving a final repressor-reaction concentration of 5 nM. The reporter was held with the pre-expressed repressor for about 1 h at 37 °C before encapsulation.

:::{attention} Two values in the encapsulation method are open
The DevNote gives the imaging time as both a six-hour incubation and as overnight, and gives the pellet resuspension volume as 100 mL where every other volume in that method is in µL. @Developer: confirm both with the authors. This page states neither.
:::

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).

Requires the repressor to be supplied as protein, expressed in a separate reaction beforehand. Expressing the repressor and the reporter together in one reaction gives a much weaker switch, because the operator is not occupied before transcription begins.

Requires the repressor and the reporter template to be held together at 37 °C for 1 h before the reaction starts.

Requires the reporter template to be held at or below 0.5 nM. Above 1 nM the reporter is in excess of the repressor and no repression is seen.

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

# Credits

Developed by Charlie Newell, Manuel Bibrowski, Jonah McDonald, Niall McIntyre and Julia Purrinos De Oliveira.

Drawn from the DevNote [Quorum Sensing in Nucleus Cytosol using EsaO/EsaR Transcriptional Regulation](https://devnotes.nucleus.engineering/articles/01a108c6-4719-7833-92af-daf6f91ed06a).

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
