---
title: "pH Demo"
subtitle: Implementation
status: draft
site:
    hide-toc: true
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

The pH Demo turns acidic pH into a color change in a gel. [SensorCell[pH ⟶ PLA1]](../../modules/ph-sensing-cell/spec.md) synthetic cells and CPRG-loaded large unilamellar vesicles (LUVs) are set together in low-gelling agarose. At pH 6.0 to 6.5 the synthetic cells express phospholipase A1 (PLA1), which breaks the LUVs' membranes and releases CPRG into the gel. A basic buffer carrying [Reporter: LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) then goes into the gel, and LacZ turns the released CPRG from yellow to purple.

LacZ is added only after the sensing step, because it works poorly at the acidic pH the sensor needs. What the gel embedding builds is [pH Cascade](../../modules/ph-cascade/spec.md).

This page carries two formats of the same cascade, and **both have run**. The solution-phase arm is under Observed Performance. The gel demo has run **four times**, and this page does not yet carry its data.

# Modules

| Role | Module | How each format uses it |
| --- | --- | --- |
| Cascade | [pH Cascade](../../modules/ph-cascade/spec.md) | gel: what the embedding builds. Solution: what the co-incubation builds |
| Sensing cell | [SensorCell[pH ⟶ PLA1]](../../modules/ph-sensing-cell/spec.md) | gel: set in the gel. Solution: suspended in the well, with Cy5 at 2 µM in the lumen |
| Detector | [Detector: pH-Sensing](../../modules/detector-ph/spec.md) | the pH-responsive and trigger strands, annealed 3:1 |
| Lysis | [Lysis: PLA1](../../modules/effector-pla1/spec.md) | expressed from the `pT7-toehold9-PLA1` template |
| Cytosol | [Base Cytosol](../../modules/base-cytosol/spec.md) | inside the synthetic cells |
| Membrane | [Membrane: POPC/Chol (9:1)](../../modules/membrane-popc-chol-9-1/spec.md) | with 0.1 mol% Liss Rhod PE, on both the synthetic cells and the LUVs |
| Substrate | [Substrate: CPRG](../../modules/substrate-cprg/spec.md) | 14.25 mg/mL inside the LUVs |
| Gel | [Gel: LGA](../../modules/gel-lga/spec.md) | 0.7% (w/v) in the set gel for the first three attempts, 0.35% for the fourth |
| Reporter | [Reporter: LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) | gel only: in the basic buffer, added after the sensing step |
| Substrate carrier | [Substrate LUV: CPRG](../../modules/substrate-cprg-luv/spec.md) | solution only: the payload population, carrying no Cy5 |
| Outer solution | [Outer Solution: Tris-HEPES](../../modules/outer-solution-tris-hepes/spec.md) | solution only: both arms are built on it |

Both formats use the same membrane on both populations, so the membrane label does not tell them apart. In the solution format, Cy5 in the sensing population's lumen does.

# Processes

The two formats share their parts and differ in their operations, so this section splits where the Modules table did not.

**The gel demo.**

| Step | Process | In the demo |
| --- | --- | --- |
| 1 | [Anneal pH-Responsive Trigger Duplex](../../processes/anneal-ph-trigger-duplex/main.md) | pH-responsive strand to trigger, 3:1 |
| 2 | [Assemble Cytosol](../../processes/assemble-cytosol/assemble-cytosol-main.md) | the trigger duplex and the PLA1 template, into Base Cytosol |
| 3 | [Encapsulation: Freeze-Thaw](../../processes/encapsulate-luv/main.md) | the CPRG-loaded LUVs |
| 4 | [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) | the synthetic cells |
| 5 | [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md) | synthetic cells and LUVs set in LGA, then incubated at 37 °C |
| 6 | [Color Development](../../processes/color-development/main.md) | the basic buffer carrying LacZ Enzyme goes into the gel |
| 7 | [Colorimetric Readout](../../processes/colorimetric-readout/main.md) | the color is read |

**The solution-phase arm.** No gel, no LacZ step, and the readout is fluorescence rather than color.

| Step | Process | In the run |
| --- | --- | --- |
| 1 | [Anneal pH-Responsive Trigger Duplex](../../processes/anneal-ph-trigger-duplex/main.md) | pH-responsive strand to trigger, 3:1 |
| 2 | [Assemble Cytosol](../../processes/assemble-cytosol/assemble-cytosol-main.md) | the trigger duplex and the PLA1 template, into Base Cytosol |
| 3 | [Encapsulation: Freeze-Thaw](../../processes/encapsulate-luv/main.md) | the CPRG-loaded LUVs |
| 4 | [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) | the sensing cells |
| 5 | [Assemble Outer Solution](../../processes/assemble-outer-solution/main.md) | both arms |

The sensing cells were made by an inverted-emulsion variant of phase transfer — a different lipid prep, a layered interface and a slower, colder spin. That variant is now written up as [Protocol: Inverted Emulsion](../../processes/assemble-base-cell/protocol-guv.md), a second protocol under Phase Transfer. The readout is [Microscopy Readout](../../processes/microscopy-readout/main.md).

**How the gel is brought to acidic pH.** The gel route takes the same buffer mix as the solution arm, at the same 12% (v/v), and names its two arms **pH 7.4 and pH 6.5**. The neutral arm is the Tris-HEPES stock alone. The acidic arm is the four-component mix under Protocol as run below, and its figures are identical to the solution arm's.

:::{attention} The same mix is labeled with two different pH pairs
The solution arm calls these arms pH 7.6 and pH 6.3. The gel route calls them pH 7.4 and pH 6.5, from the same stock and the same 1200 µL recipe. @Editor(chicago): one meter reading of an assembled well settles both pairs. See the note under Protocol as run.
:::

**The amounts in the gel.** The vesicles are 12% (v/v) of the set gel, 7.2 µL in 60 µL, which is the same fraction the solution arm gives them.

:::{attention} What the demo does not yet specify
- **The split between the two populations.** The 12% (v/v) above is the sensing cells and the LUVs together. @Editor: record the two separately, and the LacZ Enzyme in the basic buffer.
- **The color development conditions in the gel.** @Editor: confirm them. The one test on record ran in solution: pH 9.9 buffer, 37 °C, 3 h.
:::

# Protocol as run

The protocol below is the solution-phase arm. The gel attempts ran to a protocol that is not transcribed here yet.

**The solution-phase arm.** Two vesicle populations co-incubated in one 60 µL well, at two pH values, for 13 h at 37 °C.

:::{table} The assembled well, 60 µL.
:label: comp-ph-demo-solution-well

| Component | Volume (µL) | Fraction |
| --- | --- | --- |
| Energy solution | 30 | 50% (v/v) |
| Ultra-pure distilled water | 15.6 | 26% (v/v) |
| Tris-HEPES buffer stock | 7.2 | 12% (v/v) |
| Vesicle suspension | 7.2 | 12% (v/v) |
| Total | 60 | 100% |
:::

**Two liquids are called the outer solution and they are not the same.** The first is what the vesicles are washed into and suspended in: Tris-HEPES stock in water, about 1180 mOsm, which is the composition on [Outer Solution: Tris-HEPES](../../modules/outer-solution-tris-hepes/spec.md). The second is the assembled well above, where that suspension is 12% of the volume and the energy solution is half of it.

The acidic arm replaces the Tris-HEPES buffer stock row with a separate buffer mix, at the same 7.2 µL.

:::{table} Buffer mix for the acidic arm. The mix is 1200 µL and it replaces the Tris-HEPES stock at the same 12% (v/v).
:label: comp-ph-demo-solution-acid

| Component | Stock | Volume (µL) |
| --- | --- | --- |
| Tris-HEPES buffer stock | — | 466.67 |
| HEPES | 2 M | 576.19 |
| HCl | 37% | 80 |
| Ultra-pure distilled water | — | 77.14 |
| Total | | 1200 |
:::

:::{attention} The arm pH figures are intended, not measured
@Editor(chicago): the arms are recorded at pH 7.6 and pH 6.3 on the build sheet's column headers. Confirm with a meter reading of an assembled well, or state that the headers are the target rather than the result.
:::

# Observed Performance

**The gel demo, read by eye across four attempts.** The first gel attempt gave an acid-responsive color change, and so did its control: CPRG-loaded LUVs with β-galactosidase and no PLA1-expressing cells colored as well. The only difference from the solution arm was the agarose, so gel embedding releases CPRG from the LUVs with no PLA1 present. Extruding the carriers through 400 nm membranes lowered the background only slightly, and cut the yield of both populations. The fourth attempt worked: a visible color difference in gel and in solution, after a larger starting volume, more washes, and the gel reduced from 0.7% to 0.35% (w/v).

**The readout is the eye.** Attempts two and three are reported as not distinguishable by eye, and the fourth as a visible difference. No plate-reader or imaging figure is recorded for any of the four.

:::{attention} The gel attempts have no data on this page
@Editor: record each attempt's date, its conditions and its photograph or trace. The fourth attempt changed three things at once, so nothing here can attribute the fix to one of them.
:::

**The solution-phase arm, read by fluorescence microscopy at both pH values.**

Cy5 stays in the sensing population at both pH values, so the two populations remain distinguishable for the length of the run. The fraction of sensing cells still holding Cy5 is markedly lower at pH 6.3 than at pH 7.6, which is lysis gated by pH.

Acquisition is a two-channel z-stack, 1.5 µm between planes and 0.333 µm pixels, written as one OME-Zarr 0.5 store per well. The channel named for Alexa Fluor 647 reports the Cy5 signal; the microscope names a channel after a representative dye, not after the dye in the sample.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
