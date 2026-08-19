---
title: "Detector: AHL"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The AHL Detector module is a LuxR/pLux genetic sensor that detects the quorum-sensing molecule AHL (N-(β-ketocaproyl)-L-homoserine lactone, also referred to in source material as 3-oxohexanoyl-L-homoserine lactone or 3OC6-HSL) and turns on expression of a downstream reporter. LuxR binds AHL and activates the pLux promoter, driving expression of GFP or, in a related colorimetric configuration, PLA1 (see Caveats).

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Not related to the α-Hemolysin membrane pore module
This page is unrelated to [Membrane Pore: α-Hemolysin](../membrane-pore-ahly/spec.md), which documents a self-inserting protein pore (aHly) used for passive small-molecule transport across a membrane. That module is a structural/transport component; this one is a genetic AHL quorum-sensing detector. The two share no components, mechanism, or data, and this page does not extend, link to, or otherwise build on `membrane-pore-ahly/spec.md`.
:::

:::{attention} Not the same molecule as the IV-HSL Emitter module
[Emitter: IV-HSL](../emitter-ivhsl/spec.md) documents a *different* acyl-homoserine lactone system: it produces N-isovaleryl-L-homoserine lactone (IV-HSL, a branched-chain HSL detected by BjaR) rather than detecting it, and IV-HSL is chemically distinct from the AHL (3-oxo-C6-HSL) detected by this module. The two are not interchangeable and this page makes no claim about compatibility between them.
:::

:::{attention} Not yet validated in PURExpress or Nucleus Cytosol
All data below comes from bacterial S30 lysate (Promega) and POPC synthetic cells built from S30 lysate, not from PURExpress or Nucleus Cytosol. This module has not yet been characterized in either cytosol platform used elsewhere in this Distribution.
:::

:::::{tab-set}

::::{tab-item} Schematic
:::{figure} mechanism-schematic.png
LuxR, constitutively expressed from P70, binds AHL as it diffuses in from outside the synthetic cell; the resulting LuxR–AHL complex activates the pLux promoter, driving GFP expression inside the liposome. Cropped from the DevCell Project Meeting slide deck (14 Aug 2026, p. 13, "Sensor GFP SynCells with lysate (in gel)"); the source panel's phospholipid-bilayer inset has been cropped out as unrelated to the sensing mechanism itself.
:::
::::

::::{tab-item} Designs

:::{attention} Construct not in `nucleus-eng/DNA`
The LuxR/pLux AHL sensor plasmid used in the synthetic cell encapsulation work below is referred to as `pLux-GFP` (in-house stock, Elani lab) and has no catalog number or sequence file in the source material. It is not present in [`nucleus-eng/DNA`](https://github.com/nucleus-eng/DNA) and does not appear to have originated from a prior repository either — it needs to be submitted before this Designs table can cite a real sequence file. Do not treat the name `pLux-GFP` as a stable identifier: the bacterial-lysate characterization below (Module 1) references only an unnamed "sensing plasmid" and does not confirm it is the same construct as the synthetic cell encapsulation plasmid (Module 3). Flagging this rather than assuming identity.
:::

**DNA**

| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pLux-GFP` (LuxR/pLux AHL sensor) | not available | not yet in `nucleus-eng/DNA` |

::::

:::::

## Cytosols

### Usage

The sensor was characterized in Promega bacterial S30 lysate (not PURExpress or Nucleus Cytosol). A representative reaction (`Demo Status - London.docx`, Module 1) combines lysate premix, extract, amino acids, an unnamed sensing plasmid, and AHL at final concentrations of 1x, 1.80 mg/mL, 1.8 µM, 40 ng/µL, and 10 µM respectively, against a no-AHL negative control. Volumes in µL.

| **Component** | **Stock** | **Final** | **Condition 1 (− AHL)** | **Condition 2 (+ 10 µM AHL)** |
| --- | --- | --- | --- | --- |
| Premix | 3.33x | 1x | 20 | 20 |
| Extract | 15 mg/mL | 1.80 mg/mL | 15 | 15 |
| Amino acids | 10 µM | 1.8 µM | 5 | 5 |
| Sensing plasmid | 2000 ng/µL | 40 ng/µL | 1 | 1 |
| AHL | 50 mM | 0.01 mM | 0.5 | 0 |
| RNase inhibitor | 40000 U/mL | 800 U/mL | 1 | 1 |
| Water | — | — | 7.5 | 8 |

### Expected Performance

AHL turns on GFP expression from the sensing plasmid in bacterial S30 lysate. The source material describes this system as fully characterized in bacterial lysate for detecting bacteria that produce quorum-sensing molecules, with expression increasing across a range of AHL concentrations and plateauing around 10 µM.

:::{attention} Caveats from the source material
- The sensor works well only when the expression system supplied lacks T7 polymerase.
- No figure data or replicate counts were included alongside this reaction table in the source document — treat the "fully characterized" framing as the source's own claim, not independently re-verified here.
:::

## Cells

### Usage

The sensor plasmid was encapsulated in POPC synthetic cells together with S30 lysate by mineral-oil phase transfer (Elani-lab protocol), forming synthetic cells that report AHL exposure by expressing GFP inside the liposome. AHL is supplied in the outer solution and diffuses across the POPC membrane to activate the encapsulated sensor.

| **Component** | **Concentration** |
| --- | --- |
| Potassium L-glutamate (outer) | 578 mM |
| HEPES, pH 7.4 (outer) | 72 mM |
| Glucose (outer) | 300 mM |
| AHL (3OC6-HSL), + condition only (outer) | 10 µM |

### Expected Performance

Without Optiprep in the inner solution, encapsulated sensor synthetic cells express GFP on AHL induction: green fluorescence appears across all imaged fields, with liposome-associated puncta co-locating with round liposomes, consistent with an active encapsulated reaction. The source material notes that minus-AHL and no-DNA controls, plus biological replicates, were still needed at the time of writing to formally attribute the signal — this result should be read as directional, not a fully controlled positive.

Separately, the LuxR sensor was embedded in POPC synthetic cells within 1% ultra-low-gelling-temperature agarose (ULGA) hydrogel. These hydrogel-embedded synthetic cells produced a GFP response after 2.5 h incubation with either overnight bacterial culture or bacterial culture supernatant, confirmed by Z-stack imaging; an LB-only control showed no signal at matched imaging settings.

:::{attention} Caveats from the source material
- Optiprep above ~5% of the inner solution broadly suppresses cell-free expression (not AHL-specific); encapsulate without Optiprep to preserve expression.
- Plasmid dosing is critical: early failures traced to roughly seven-fold under-dosing; use ~1000 ng per reaction (~37–80 ng/µL in-reaction, per the encapsulation protocol).
- Sensor fold-induction is strongest near 25 °C and drops at 37 °C; incubate at 25 °C when minimal background matters.
- Encapsulation is stochastic — expect a GFP-positive subpopulation rather than uniform signal across liposomes.
:::

### Related colorimetric configuration and known leakiness

A separate configuration couples this sensor to a PLA1-based colorimetric readout (CPRG → chlorophenol red), documented on the PLA1 Lysis Module page rather than duplicated here. In S30 lysate, that configuration showed only a slight discernible color-change difference between +AHL and −AHL conditions after 16 h (15 ng/µL DNA, 5 µM AHL), and the source material states directly: "AHL sensing is currently not proven in nucleus cytosol, and in lysate, the sensor is leaky." Treat sensor leakiness as an open, unresolved caveat on this module, not something specific to the colorimetric readout alone.

### Expected Performance by Configuration

AHL sensing has been tested across nine distinct configurations spanning solution, gel, and bulk formats, and cytosol, lysate, and live-bacteria expression systems (deck pp. 12–21). Selected results, cited as reported — reproducibility across the set is uneven, and none of it is presented as fully validated:

- GFP synthetic cells with lysate in gel (synthetic cell + AHL) were confirmed on a plate reader, with a reproducible signal over a 1000-minute time course (deck pp. 13–14).
- A constitutive (non-AHL-gated) PLA1/CPRG two-liposome colorimetric configuration in cytosol/gel showed a measurable, reportedly reproducible color change by UV-Vis after 3 h (deck p. 15).
- The AHL-gated colorimetric sensor in lysate was tested in both solution and gel; the gel version was reported as repeated across two different labs, but is described as "temperamental... sometimes SynCells do not rupture" (deck pp. 16–17).
- The sensor was also tested as a GFP readout in cytosol/bulk, alongside a low-cost spectrometer build for quantifying the output (deck pp. 18–20).
- A lysate-synthetic cell-plus-live-bacteria (agar-pad AHL diffusion) test was attempted once and produced no observable GFP (deck p. 21).
- The target demo is colorimetric readout in a gel-based cytosol system (deck p. 12); GFP currently outperforms the colorimetric readout, and solution/bulk formats currently outperform gel formats.
- The deck itself flags "leaky expression [as] a bigger issue than first thought" (p. 13), consistent with the leakiness caveat above.

Separately, and more provisionally, meeting notes describe a distinct, very recent AHL Sensing Cell + [CPRG-loaded SUV](../../processes/encapsulate-suv/main.md) + AHL result, not yet reproduced; negative controls in that specific test turned purple, attributed to leaky old-stock liposomes rather than to AHL response. This is a separate, more nascent data point from the nine configurations above and should not be conflated with them — it is cited here as an active lead, not a result.

:::{attention} Net characterization
Taken together, the AHL Detector module has real, multi-format experimental traction — GFP and colorimetric readouts have both worked in at least one lysate/synthetic cell/gel configuration, in some cases repeated across labs or over long time courses. It has not, however, reached the point of established reproducibility: leakiness (signal in the absence of AHL) is a recurring, explicitly unresolved caveat across multiple configurations, and the most recent reported result is both unreproduced and subject to a known false-positive risk from old-stock liposome leakage. Treat this module as demonstrating feasibility, not as a validated detector.
:::

# Known Implementations

The synthetic-cell-encapsulated and hydrogel-embedded configurations described above are now documented as composed Module pages rather than as a standalone Implementation:

- **AHL Sensing Cell.** See the [AHL Sensing Cell](../ahl-sensing-cell/spec.md) spec: this Detector's `pLux-GFP` plasmid encapsulated in a POPC synthetic cell built on the [London Chassis](../london-chassis/spec.md). Same GFP readout, same caveats (leakiness, unreproduced recent Sensing Cell + CPRG-loaded SUV result) as documented above — not duplicated here.
- **London Cascade.** See the [London Cascade](../london-cascade/spec.md) spec: the same LuxR/pLux sensing mechanism, but gating a `P70lux-PLA1-term` construct instead of GFP, so that AHL exposure triggers a two-liposome PLA1/LacZ colorimetric handoff.

Both pages still ultimately trace back to `devnotes/london-quorum-sensing-polymersome/main.md`, which is a template stub — milestones and risks only, no primary data.

:::{attention} That devnote is not just a stub, it is dropped
As of 2026-08-19, London is **not** pursuing polymersomes. So this module's nominal source document covers abandoned work *and* contains no data. The AHL Detector currently has no backing document at all, and needs a module DevNote written against the S30/POPC work it actually uses.
:::

# Credits

- Ion Ioannou (synthetic cell encapsulation)
- Jonah McDonald (synthetic cell encapsulation)
