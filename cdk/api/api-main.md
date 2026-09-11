---
title: "CDK API Reference"
---

# Overview

The CDK splits along the measurement that produced your data. Both halves share the same
platemap conventions and the same plotting arguments, so what you learn on one transfers
to the other.

| | Data source | Import |
| --- | --- | --- |
| [**Cell**](./cell.md) | Microscopy — a segmented plate zarr | `from cdk.analysis import cell` |
| [**Cytosol**](./cytosol.md) | Plate reader — BioTek kinetic, endpoint, spectral | `from cdk.instruments import platereader` |

The names are the biology, not the instrument: *cell* analysis describes individual
objects imaged under a microscope, *cytosol* analysis describes bulk reactions read in a
plate. Most microscopy work is cell analysis and most plate reader work is cytosol
analysis, but the distinction that matters is what the numbers describe.

:::::{card}

::::{grid} 1 1 2 2

:::{card}
:header: 🔬 **Cell**
:link: ./cell.md

`load`, `plot_cell_grid`, `plot_qc`, `plot_quantile_ribbon`, `plot_positive_fraction`,
`plot_size_expression`, `plot_ecdf`, and the segmentation pipeline.
:::

:::{card}
:header: 🧪 **Cytosol**
:link: ./cytosol.md

`load_platereader_data`, `PlateReaderData` transforms, `Kinetics`, `StandardCurve`.
:::

::::
:::::

## Conventions shared by both

**Platemaps.** A platemap CSV maps wells to what was in them. Merging one is optional —
every function works without it, falling back to `Well` as the label — but supplying one
is what unlocks faceting by experimental factor.

**Transforms return new objects.** Nothing mutates in place. `data.blank()` gives you
blanked data; the original is untouched.

**Plots return their figure.** Every `plot_*` function returns the matplotlib figure or
seaborn grid it drew, so you can adjust and save it.
