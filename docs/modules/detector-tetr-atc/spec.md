---
title: "Detector: tetR-aTc"
subtitle: "Module Specification"
thumbnail: mechanism-schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The TetR inducible expression module is a set of two genetic constructs that encode tetracycline-inducible gene expression: `pT7-tetR`, encoding the TetR repressor protein, and `pT7-tetO-plamGFP`, encoding a reporter gene under an inducible T7 promoter.

`pT7-tetO-plamGFP` constitutively expresses the open reporter plamGFP in the absence of repressor protein. The inducible promoter is also a MoClo Level 0 'P' part and may be assembled into a Level 1 transcription unit with other MoClo-compatible genes. Addition of TetR protein — either as a purified protein or via constitutive expression of `pT7-tetR` — inhibits expression through steric occlusion of the tetO operator site. Addition of anhydrotetracycline (aTc) causes allosteric release of TetR from tetO, recovering expression. aTc is membrane-permeable, so the alpha-hemolysin membrane pore is not required for induction.

:::{figure} mechanism-schematic.png
Schematic of the TetR inducible expression module. TetR represses expression from `pT7-tetO-plamGFP`; aTc relieves repression by binding TetR and causing its release from the tetO operator.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA

:::{table}
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-tetR` | 2877 | [pOpen-tetR.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/pOpen-tetR.gb) |
| `pT7-tetO-plamGFP` | 2954 | [pOpen-pT7-tetO.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/pOpen-pT7-tetO.gb) |
| `T7-tetO-deGFP` | not documented | not yet in `nucleus-eng/DNA` |
| `TetO-PLA1` | not documented | not yet in `nucleus-eng/DNA` |
:::

The first two constructs are this Module's Reference Composition. The other two swap the reporter out and appear only in results: deGFP under [Replicated in Nucleus Cytosol](#replicated-in-nucleus-cytosol), and PLA1 driving a colorimetric readout under [TetO-PLA1 encapsulated with LacZ](#teto-pla1-encapsulated-with-lacz).

:::{attention} Two constructs are not yet in `nucleus-eng/DNA`
@Editor: neither `T7-tetO-deGFP` nor `TetO-PLA1` has a sequence file in [`nucleus-eng/DNA`](https://github.com/nucleus-eng/DNA), and neither has a recorded length. Both are distinct from `pT7-tetO-plamGFP`, so do not read either name as an identity claim against `pOpen-pT7-tetO.gb`. Flag for follow-up so both can be submitted before this page is used at the bench.
:::

::::

::::{tab-item} Cytosol

Assemble `pT7-tetO-plamGFP` into a standard PURE reaction. Add purified TetR protein to a final concentration of 500 nM, or include the `pT7-tetR` DNA construct. Add aTc inducer at 2.5 µM to 5 µM for effective induction. Volumes in µL.


| **Component** | **Master Mix (µL)** |
| --- | --- |
| PURExpress Solution A | 4 |
| PURExpress Solution B | 3 |
| RNase Inhibitor | 0.5 |
| `pT7-tetO-plamGFP` (10 nM) | 0.5 |
| TetR (10 µM) | 0.5 |
| **Master Mix Total** | **9** |

| **Component** | **Per Reaction (µL)** |
| --- | --- |
| Master Mix | 9 |
| Inducer | 1 |
| **Total** | **10** |

::::

:::::

# Expected Behavior

## Cytosols

The TetR module was validated in NEB PURExpress reactions. Purified repressor protein (MedChemExpress, HY-P71520A) and anhydrotetracycline inducer (Cayman Chemical, 10009542) were added at the final concentrations indicated. `pT7-tetO-plamGFP` plasmid DNA was added at 0.5 nM.

Repression follows a roughly linear trend between 125 and 750 nM TetR and saturates around 500 nM, though it can be further improved up to 2000 nM. An inducer concentration of 2.5 µM to 5 µM provides effective induction well below saturating or toxic aTc levels. Note that aTc's yellow color overwhelms GFP fluorescence at concentrations greater than 50 µM to 100 µM, and high concentrations may negatively affect expression generally.

***In vitro* repression with TetR**

:::::{tab-set}

::::{tab-item} Kinetics
:::{figure} cytosol-repression-kinetics.png
Repression kinetics of `pT7-tetO-plamGFP` by TetR at varying repressor concentrations.
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-repression-endpoint.png
Repression of `pT7-tetO-plamGFP` by TetR at steady state.
:::
::::

:::::

***In vitro* induction with aTc**

:::::{tab-set}

::::{tab-item} Kinetics
:::{figure} cytosol-induction-kinetics.png
Induction kinetics of `pT7-tetO-plamGFP` by aTc. TetR repressor protein is present at 500 nM. Positive control is `pT7-tetO-plamGFP` without TetR repressor protein.
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-induction-endpoint.png
Induction of `pT7-tetO-plamGFP` by aTc at steady state. TetR repressor protein is present at 500 nM. Positive control is `pT7-tetO-plamGFP` without TetR repressor protein.
:::
::::

:::::

### Replicated in Nucleus Cytosol

The results above are from NEB PURExpress. The Module has since been re-run in [Base Cytosol](../base-cytosol/spec.md), swapping the plamGFP reporter for deGFP, and both repression and aTc induction carry over.

Every condition plateaus within about 2 h. TetR at 500 nM holds the unregulated reporter to under a tenth of its plateau, and adding aTc recovers about two thirds of it — so repression is close to complete at this TetR concentration, while induction is substantial but partial.

:::{figure} cytosol-nucleus-degfp-kinetics.png
:name: fig-tetr-atc-nucleus-degfp
:align: center

`T7-tetO-deGFP` in Nucleus Cytosol: unregulated, repressed with 500 nM TetR, and induced with 500 nM TetR plus aTc, alongside a cytosol control reaction. Fluorescence is normalized to 1 µM fluorescein, and shaded bands are the spread across replicates.
:::

The same replication was also read out through catechol instead of fluorescence, using a TetR-gated catechol 2,3-dioxygenase construct. That result, and how it reconciles with the reference XylE reaction run at a lower TetR concentration, is on the [XylE / C23DO Reporter Module](../reporter-xyle/spec.md#reporter-xyle-expected-behavior) spec.

:::{attention} Inducer concentration not recorded
@Editor: the aTc concentration used for the induced condition is not recorded. Confirm it before this result is used at the bench. The construct gap is noted in the DNA tab under Reference Composition.
:::

## Cells

:::{figure} detector-overview.png
The TetR-aTc Detector module in the Base Cell.
:::

TetR detector synthetic cells were induced at multiple anhydrotetracycline concentrations and imaged over 12 h with approximately 22 min per timepoint.

:::::{tab-set}

::::{tab-item} Microscopy Images
:::{figure} cell-performance-montage.png
TetR detector synthetic cells induced at multiple anhydrotetracycline concentrations. 8 timepoints displayed per condition, approximately 22 min apart, over 12 h total. **First row:** induction using 625 nM, 312.5 nM, and 0 nM (fully repressed) aTc introduced into the outer buffer. **Second row:** induction with 2500 nM aTc in the inner solution and positive control without TetR repression.
:::
::::

::::{tab-item} Fluorescence Intensity
:::{figure} cell-performance-endpoint.png
GFP expression within synthetic cells when induced with 312.5 nM anhydrotetracycline.
:::
::::

:::::

The TetR detector cell functions when induced with low-nanomolar aTc concentrations. Higher concentrations begin to inhibit expression or confound analysis due to background aTc fluorescence and membrane localization.

### TetO-PLA1 encapsulated with LacZ

A second configuration replaces the plamGFP reporter with a `TetO-PLA1` construct and co-encapsulates LacZ protein at 20 U/mL, leaving 0.5 mM CPRG in the outer solution. aTc de-represses `TetO-PLA1`, PLA1 ruptures the membrane, and the released LacZ reaches the CPRG outside, so the readout is the [LacZ Reporter Module](../reporter-lacz/spec.md)'s color change at 575 nm rather than fluorescence. This configuration detects aTc in synthetic cells, but the response is **not graded**.

Three DNA/TetR pairs — 1 nM DNA with 50 nM TetR, 0.5 nM DNA with 50 nM TetR, and 1 nM DNA with 100 nM TetR — were each dosed at 0, 1, 5, and 10 µM aTc, and fold change in absorbance was measured at 5 h (n = 3). Every pair separates dosed from undosed by roughly 1.15× to 1.33×. None is monotonic in dose, and the spread across the 1, 5, and 10 µM points overlaps in all three. Expect the response to saturate at or below 1 µM, with no resolvable dose-dependence from 1 to 10 µM.

:::{figure} cell-lacz-readout-endpoint.png
:name: fig-tetr-atc-lacz-endpoint
:align: center

Fold change in absorbance at 575 nm after 5 h, relative to the undosed condition, for three DNA/TetR pairs dosed at 0, 1, 5, and 10 µM aTc. Points are the three replicates. LacZ is encapsulated at 20 U/mL, with CPRG at 0.5 mM outside. Figure by Mary Kelly (Chicago Node, Kamat Lab).
:::

**The 0 µM condition is the normalization baseline, not a negative control.** Fold change is taken against it, which is why every panel's 0 µM bar sits at exactly 1.0 with no spread — that bar reports the arithmetic, not a measurement. The controls that bound the assay are on the raw absorbance trace instead, where a reaction with no DNA template reaches nearly the same absorbance at 5 h as an undosed one. Most of the signal is therefore template-independent, and aTc recovers only part of the distance to a fully de-repressed reaction.

::::{hint} Most of the absorbance develops with no DNA template at all
:class: dropdown

:::{figure} cell-lacz-readout-kinetics.png
:name: fig-tetr-atc-lacz-kinetics
:align: center

Absorbance at 575 nm over 5 h, for 1 nM `TetO-PLA1` DNA with 50 nM TetR. The reaction without TetR is de-repressed throughout and reads highest; the three aTc-dosed conditions overlap one another; the undosed reaction and the no-DNA control run close together at the bottom. Figure by Mary Kelly (Chicago Node, Kamat Lab).
:::

::::

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).

# Implementations

- [Responder: aTc → IV-HSL](../../implementations/responder-atc-ivhsl/main.md): aTc relieves TetR repression to drive BjaI expression.

# Credits

Developed by Yen-Yu Hsu (b.next), with the encapsulated LacZ/CPRG configuration by Mary Kelly (Chicago Node, Kamat Lab).
