---
title: DNA Distribution
---

# Overview

The Nucleus DNA Distribution is a library of OpenMTA genetic constructs used to engineer synthetic cells. It includes the protein-coding genes of the [PURE](https://doi.org/10.1038/90802) cell-free expression system, a level-matched T7 promoter library, ribosome binding sites, terminators, fluorescent reporters, and regulatory circuit components.

These constructs are the physical materials referenced throughout the [Modules](./modules/modules-main.md) and [Processes](./processes/processes-main.md) sections of this site. To request access to the distribution, join the [mailing list](https://bnextbio.typeform.com/nucleus-signup) or [contact us](mailto:build@bnext.bio).

# The DNA repository

All sequences are maintained in the companion [nucleus-eng/DNA](https://github.com/nucleus-eng/DNA) repository as GenBank (`.gb`) files, which open in [Benchling](https://benchling.com), [SnapGene](https://www.snapgene.com/), or any sequence editor that supports the format.

Most parts use the MoClo-compatible `pOpen` entry-vector backbone and follow the naming pattern `pOpen-[part-name]`; PURE protein expression constructs use the `pET28a` backbone and follow `pET28a-[protein-name]`. The repository [README](https://github.com/nucleus-eng/DNA/blob/main/README.md) is the canonical description of its structure and contents.

# Where to find things

This page orients you to the distribution; the details live in three places.

| To find... | Look in... |
| --- | --- |
| Sequence files for a specific construct | the [DNA repository](https://github.com/nucleus-eng/DNA) |
| What a component does and how it behaves | [Modules](./modules/modules-main.md) |
| Lab protocols that use these constructs | [Processes](./processes/processes-main.md) |
