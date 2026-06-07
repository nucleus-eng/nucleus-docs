---
title: DNA Distribution
---

# Overview

The Nucleus DNA Distribution is a free to use library of DNA without patent or material transfer restrictions. These DNA sequences are used to build the [Modules](./modules/modules-main.md) reported here in Nucleus Docs. Each module specification should describe how to use the DNA (and other components) comprising the module. Digital sequences are maintained in the companion [nucleus-eng/DNA](https://github.com/nucleus-eng/DNA) repository. The repository [README](https://github.com/nucleus-eng/DNA/blob/main/README.md) describes the structure and contents of the DNA distribution.

# Usage

Most sequences come in the `pOpen` plasmid (*E coli.* medium copy, ampicilin) and follow the naming pattern `pOpen-[part-name]`. `pOpen-pT7` constructs come with a T7 promoter and are appropriate DNA templates for reactions in [Nucleus Cytosol](./modules/base-cytosol/spec.md) and other PURE-derived systems. `pOpen` plasmids are NOT good expression vectors for protein production.

Expression vectors specifically for protein expression use the `pET28a` backbone (*E. coli* medium copy, kanamycin) and follow the naming pattern `pET28a-[protein-name]`. Most genes included in `pET28a` include 6xHis tags, making them ready for [Ni2+ Affinity Purification](./processes/make-protein/purify-proteins-grav-column/main.md). 

# Where to find things

| To find...                              | Look in...                                               |
| --------------------------------------- | -------------------------------------------------------- |
| Sequence files for a specific construct | the [DNA repository](https://github.com/nucleus-eng/DNA) |
| What a sequence does and how to use it  | [Modules](./modules/modules-main.md)                     |
| Lab protocols to handle DNA             | [Processes](./processes/processes-main.md)               |
