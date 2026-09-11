---
title: "CDK API Reference"
---

# Overview

The CDK is split by the instrument that produced your data. Both halves use the same platemap conventions and the same plotting arguments.

| | Data source | Import |
| --- | --- | --- |
| [**Cell**](./cell.md) | Microscopy — a segmented plate zarr | `from cdk.analysis import cell` |
| [**Cytosol**](./cytosol.md) | Plate reader — BioTek kinetic, endpoint, spectral | `from cdk.instruments import platereader` |

The modules are named for the biology rather than the instrument. *Cell* analysis describes individual objects imaged under a microscope; *cytosol* analysis describes bulk reactions read in a plate. In practice most microscopy work is cell analysis and most plate reader work is cytosol analysis.

:::::{card}

::::{grid} 1 1 2 2

:::{card}
:header: 🔬 **Cell**
:link: ./cell.md

`load`, `plot_cell_grid`, `plot_qc`, `plot_quantile_ribbon`, `plot_positive_fraction`, `plot_size_expression`, `plot_ecdf`, and the segmentation pipeline.
:::

:::{card}
:header: 🧪 **Cytosol**
:link: ./cytosol.md

`load_platereader_data`, `PlateReaderData` transforms, `Kinetics`, `StandardCurve`.
:::

::::
:::::


