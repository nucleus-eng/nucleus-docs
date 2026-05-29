---
title: Contribution Guidelines
---

# Overview

This document provides guidelines for making a contribution to the Distribution. Since technical contributions are made by submitting a Developer Note, these contribution guidelines include both minimal requirements for submitting a DevNote and suggestions for increasing the likelihood that your contribution will be onboarded into the Distribution.

To clarify this distinction, we define several imperative phrases:

* **MUST.** This word means that something is an absolute requirement when submitting a Developer Note.
* **SHOULD.** This word means that including something will make it more likely that the submission will be onboarded into the Distribution by the Core Development Team.
* **IF POSSIBLE.** This phrase means that including something may prove technically challenging and situation dependent. Use good judgment, and post on the Forum if you need guidance on feasibility.
* **MAY.** This word means that something is optional and permissible. Inclusion or exclusion is fully at your discretion. 

> **Note:** Before reading the following guidelines, we highly recommend reading the document titled [*From Zero to DevNote*](../start/first-guide.md) which describes how to prepare your first Developer Note for inclusion into the Distribution. It provides a concrete description of the key components of a submission.

## General Considerations

### General

* SHOULD include Author(s) ORCID
* SHOULD include a schematic of the contribution

### Bill of Materials

* MUST have a section titled "Critical Reagents" that contains a table describing reagents that are critical for the experiment. The table MUST include the following columns and MAY include additional ones:

| Reagent     | **Product Name**                   | **Manufacturer** | **Part #** | **Price** | Storage Conditions | **Link**                                                      |
| ----------- | ---------------------------------- | ---------------- | ---------- | --------- | ------------------ | ------------------------------------------------------------- |
| Amino Acids | L-Amino acids, analytical standard | Sigma-Aldrich    | LAA21-1KT  | $558      | 1C to 4C           | [link](https://www.sigmaaldrich.com/US/en/product/sial/laa21) |

* SHOULD have a complete reagent list. In most circumstances, submissions will be modifying Processes with existing reagent lists. You are encouraged to reuse and modify these lists as appropriate and exercise good judgement when reagent substitutions should be regarded as "Critical"

### DNA Sequence Maps

* MUST include linear or plasmid DNA sequence maps.
* MUST include a statement attesting to sequence validity.
* MUST include a table containing names of sequences used and links to files in the project.
* SHOULD be in pOpen backbone
* SHOULD include sequence verification data.
* SHOULD follow DNA Distribution design guidelines

### Lab Notebook Entry

* MUST include a document (format as .pdf or .txt) that describes reaction preparation in sufficient detail to allow for their reproduction. At a minimum this includes the composition of stock solutions and master mixes.
* SHOULD include notes on handling or preparation that are non-obvious. For example, "preparing an aqueous stock solution of FITC requires first suspending in DMSO at 100 mM concentration" or "use of modified amino acid mixture requires extensive vortexing; do not use until solution is completely transparent".
* SHOULD include appropriate QC data on intermediate products (e.g., DNA and proteins).

## Considerations for Cytosols

### Testing and Experimental Design

* MUST be tested in reference to the PURE system, either from a commercial vendor or self-prepared. 
	* If using a self-prepared PURE system results MUST be tested across at least 2 batches. 
	* Data involving other systems such as lysates can be included but MUST be done in reference to the PURE system.
* MUST include at least >3 technical replicates for each reaction condition.
* MUST include an Appropriately Designed positive and negative control.
* SHOULD be tested in reference to version-specified Cytosol, the open-formulation flavor of PURE described on the Distribution.
* IF POSSIBLE measurements are made as timeseries, not just endpoints.

### Data

* MUST include raw data in a format that can be ingested by the Nucleus CDK
* MUST include a platemap in format that can be ingested by the Nucleus CDK
* IF POSSIBLE data is analyzed using Nucleus CDK tools

## Considerations for Cells

### Testing and Experimental Design

* MUST include appropriately designed controls
* MUST include >2 biological replicates to support each result

### Data

* MUST be possible to determine the size of liposomes
* MUST analyze >100 liposomes to support conclusions
* IF POSSIBLE, raw files of all images included in the DevNote should be included
* IF POSSIBLE, raw data files for all graphs in the DevNote should be included


# Find a typo? Want a feature?

If something is missing, lacking, or wrong on this site, [submit an issue!](https://github.com/nucleus-eng/nucleus-docs/issues/new) We use [GitHub](https://github.com/) to maintain our documentation and to track ongoing work. Just click the link above and describe what change you'd propose made to the site. If you are comfortable with git workflows, consider joining the core development team!

<!-- ---
title: Contribution Guidelines
---

# Cytosol

Requirement levels use key words as described in [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119)

- Data MUST extend an existing Module, Process, Implementation or MUST otherwise be aligned with the technical roadmap (more simply it should be tested against Nucleus PURE) or is of otherwise profound utility that ignoring the contribution would be detrimental to the well-being of the community. 
- Data MUST be included in a DevNote
- Data MUST be accompanied by a platemap compatible with the Nucleus CDK
- Data SHOULD be collected in at least technical triplicate
- Data SHOULD be collected in reference to an appropriate analytical standard

- Documentation MUST include a bill of materials
- Documentation MUST include design files for genetic constructs
- Documentation SHOULD include sequencing information for the genetic constructs
- Documentation MUST include a lab notebook entry detailing the final concentration of each component in the reactions.
- The lab notebook entry SHOULD include additional details that help others to reproduce the described work

# Cells

- Question: what is the equivalent of "Data SHOULD be collected in reference to an appropriate analytical standard"
- Question: how much data should be included? 
- Data should be processed using CDK -->
