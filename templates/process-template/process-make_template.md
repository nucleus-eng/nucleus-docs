---
title: TODO: Process Name
---

# Overview

One paragraph. State what the process does and why one would want to do it. If this process makes an output, describe what it is used for. Include key parameters needed to execute the protocol. Use precise terms. Don't open with preamble. Just start with the thing:

"Make tRNA purifies transfer RNAs from E. coli A19 by acid-phenol extraction and isopropanol precipitation, yielding a mixed tRNA preparation for use in cell-free translation reactions."

"Make Ribosomes produces 70S ribosomes from E. coli A19 by Hydrophobic Interaction Chromatography (HIC) and sucrose cushion ultracentrifugation for use in PURE-based cell-free systems."

When in doubt, read the existing Process pages.

<!-- Delete any dropdown whose only content is "- None" before publishing.
     If all dropdowns are removed, delete this entire card block. -->
:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{note} Notes
:class: dropdown
:icon: false

- None

::::::

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

- None

::::::

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

- None

::::::

::::::{attention} Critical Materials
:class: dropdown
:icon: false

- None

::::::

::::::{attention} Genetically Encoded Components
:class: dropdown
:icon: false

- None

::::::

::::::{note} Composition
:class: dropdown
:icon: false

- None

::::::

::::::{note} References
:class: dropdown
:icon: false

<!-- List DevNotes and literature that informed this process.
DevNotes are the primary source for protocol development history and QC data. -->

- None

::::::

:::::::

# Materials and Equipment

<!-- The lab-ready pipeline generates this process's Bill of Materials PDF and
     materials CSV from EITHER the inline table labeled `bom-<process-slug>`
     below OR an uploaded `resources/<process-slug>-bom.csv` beside this page.
     Replace <process-slug> with this process's directory name (e.g.
     `bom-make-trna`). Without one of those, no BOM artifacts are generated. If
     you provide both, they must agree (CI enforces it). Reuse existing part
     numbers/vendors via the Materials Reference page. See issues #10 and #108. -->

:::{table} Bill of Materials
:label: bom-<process-slug>

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| ---- | -------- | ------- | ------------ | ------ | ----- | ------- | ---- |
| TODO | TODO     | TODO    | TODO         | TODO   | TODO  | TODO    | [link](TODO) |
:::

# Protocol

### TODO: Step 1 (e.g., "Cell Culture")

:::{hint} Note: TODO: Note title (e.g., "You can work from glycerol stocks OR colonies.")
:class: dropdown
TODO: Extended note or background information for this step. Delete this block if not needed.
:::

- [ ] **TODO: Top-level step (e.g., "Prepare overnight cultures.")**
    - [ ]  TODO: Substep 1 (e.g., "Add 6 mL LB to two 14 mL culture tubes under sterile conditions.")
    - [ ]  TODO: Substep 2 (e.g., "Incubate overnight shaking at 37°C / 225 rpm / 12 hr.")
- [ ] **TODO: Top-level step (e.g., "Perform bulk outgrowth.")**
    - [ ]  TODO: Substep 1 (e.g., "Back-dilute overnight 1:500 into fresh LB in baffled Erlenmeyer flasks.")
    - [ ]  TODO: Substep 2 (e.g., "Incubate at 37°C / 225 rpm to mid-log phase (OD600 0.6–0.8).")

### TODO: Step 2 (e.g., "Nucleic Acid Extraction")

- [ ] **TODO: Top-level step (e.g., "First extraction.")**
    - [ ]  TODO: Substep 1 (e.g., "Resuspend 2 g biomass in 18 mL extraction buffer by vortexing.")
    - [ ]  TODO: Substep 2 (e.g., "Add 18 mL acid phenol and incubate at 37°C / 225 rpm / 30 min.")
- [ ] **TODO: Top-level step (e.g., "Precipitate nucleic acids.")**
    - [ ]  TODO: Substep 1 (e.g., "Add isopropanol to one volume and incubate at RT / 10 min.")
    - [ ]  TODO: Substep 2 (e.g., "Pellet by centrifugation at 14 500 rcf / 25°C / 15 min.")

# Quality Control

Describe the QC checks that confirm the process produced a usable output. Name the assay, the acceptance criterion, and the instrument or method used. Include representative data (gel image, absorbance spectrum, concentration measurement) so a reader can judge their own result against a reference. For example:

"Assess RNA integrity by denaturing PAGE. A single band at the expected size with no visible degradation products indicates acceptable quality. Typical yield is 2–5 mg/mL at OD260."

"Confirm ribosome concentration by absorbance at OD260 (1 A260 unit = 23 pmol/mL 70S ribosomes). A correctly prepared batch should yield 5–15 µM 70S ribosomes."

:::{figure} TODO: qc-gel.png
:name: fig-qc
:align: center
:width: 75%

TODO: Describe the QC result shown — assay type, lane contents, expected band or signal, and acceptance criterion. Example: "Denaturing PAGE of tRNA preparation. Lane 1: ladder; Lane 2: product. A single band at ~75 nt indicates acceptable integrity."
:::

# Downloads

<!-- These artifacts are generated by the lab-ready pipeline (issue #10) into a
     gitignored generated/ dir and published at deploy — never committed. Replace
     <process-slug> with this process's directory name. The BOM button only works
     if the page has a `bom-<process-slug>` labeled table (see Materials above);
     delete the BOM card otherwise. -->

::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/<process-slug>-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/<process-slug>-bom.pdf>`
:::

::::
