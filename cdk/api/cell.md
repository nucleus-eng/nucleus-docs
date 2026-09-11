---
title: "Cell API"
subtitle: "cdk.analysis.cell — microscopy"
---

:::{attention}
:icon: false
:class: simple

The interface described here is not yet in the released `nucleus-cdk` package. Version
0.6.0 exposes only `cdk.analysis.cell.microscopy`; the functions below ship in the next
release and are available now on the Nucleus Hub.
:::

# Overview

Segmentation and single-object analysis of high-content microscopy data.

```python
from cdk.analysis import cell as m
```

The package has three modules, one per pipeline stage:

| Module | Role                                                                                               |
| --- |----------------------------------------------------------------------------------------------------|
| `raw_image_process` | Per-object measurements, appended to a CSV beside the dataset.                                     |
| `analysis` | Segmented data CSV → population plots                                                            |
| `segmentation_qc` | Segmented CSV and zarr → per-object image crops with mask outlines, for checking the segmentation. |

`raw_image_process` and `analysis` communicate only through the file on disk. `segmentation_qc` needs both: it reads the table to pick objects and the zarr to get pixels.

```python
from cdk.analysis.cell import analysis as m
```


## Loading

:::{card} `load(data_path, platemap_path=None, sample=None, minutes_per_timepoint=None)`

Read a measurement table, optionally merged with a platemap.

- **`data_path`** — `.csv` or `.parquet`, a local path or an `https://` URL. An unrecognized extension returns `None`; no exception is raised.
- **`platemap_path`** — CSV merged on `Well`. Unmatched wells are named in a warning.
- **`sample`** — draw a random subset of objects. Speeds up figure iteration on a large dataset.
- **`minutes_per_timepoint`** — derive a `Time (min)` column that every plot then uses as its x axis. See the [caveat in the tutorial](../tutorials/cell-microscopy.md#real-timepoints).

Returns a `DataFrame`.
:::

## Checking the data

Two QC functions, which check different things:

:::{card} `plot_qc(data, membrane=None, hue=None, facet=None, time=None)`

**Acquisition** QC. Tracks membrane channel intensity and object count over time, which catches photobleaching and object loss. Reads the measurement table only.
:::

:::{card} `plot_cell_grid(data, image_path, n=12, channels=None, info=None, crop_um=None, ncols=4, pyramid_level=None, field=0, segment_channel=None, mask_source="auto", contrast="shared", random_state=None, tile_size=2.2)`

**Segmentation** QC. A grid of segmented objects with mask outlines drawn on the image crops. Red is the selected object and teal are its neighbors.

Needs the zarr as well as the table, so it is much slower than anything else on this page. `image_path` accepts a local path or a URL. `pyramid_level` defaults to the level the run was measured at.
:::

## Population views

These are the current plotting functions. All of them take `hue`, `facet`, `time`, and `value`, and all four default to `None`. See [splitting figures by factor](../tutorials/cell-microscopy.md#splitting-figures-by-experimental-factor) for how each one resolves when unset.

:::{card} `plot_quantile_ribbon(data, value=None, quantiles=None, hue=None, facet=None, time=None, channel=None, show_p99=True, logy=True)`

Median, IQR, and P10–P90 of `value` over time, per condition. This is the main population view.
:::

:::{card} `plot_positive_fraction(data, value=None, y=VOLUME_COLUMN, hue=None, facet=None, time=None, channel=None, gate_quantile=0.99, logy=True)`

Three rows: how many objects cross their well's baseline gate, how bright those positives are, and how big each population is. Use it to tell whether more objects turned on or the same objects got brighter.

The gate is per-well — that well's own `gate_quantile` of `value` at the first timepoint.
:::

:::{card} `plot_size_expression(data, x=VOLUME_COLUMN, y=None, timepoints=None, facet=None, time=None, channel=None, logx=True, logy=True)`

`y` against `x` as a hexbin, with a fit line in each panel. Answers whether size changes concentration. The fit covers all objects and is not split by percentile.
:::

:::{card} `plot_ecdf(data, value=None, timepoints=None, hue=None, facet=None, time=None, channel=None, gate_quantile=0.99, logx=True, show_gate=True)`

Empirical CDF at a few timepoints: what fraction of objects are dimmer than a given value. Shows the full distribution, where the quantile views show summary percentiles.
:::

## Earlier views

Still supported. These will likely be deprecated. 

| Function | Output |
| --- | --- |
| `plot_summary(data, value=None, hue=None, time=None, channel=None)` | Intensity, object count and size in one three-panel figure |
| `plot_intensity(data, value=None, hue=None, time=None, channel=None, **kwargs)` | Mean intensity over time, one line per condition |
| `plot_size(data, timepoints=None, hue=None, time=None)` | Diameter histograms, one column per condition and row per timepoint |
| `plot_fogplot(data, value=None, hue=None, time=None, channel=None)` | Per-object intensity against time, one row per condition |
| `plot_fogplot_compare(data, value=None, hue=None, time=None, channel=None)` | The fogplot with conditions overlaid rather than stacked |

## Segmentation

Run this once per dataset. Everything above reads its output. A GPU makes it faster.

:::{card} `process_dataset(dataset_path, pyramid_level=0, write_labels=False, segment_channel=None, target_wells=None, target_timepoints=None)`

Walks an OME-NGFF plate zarr (wells → fields → timepoints), segments each frame with Cellpose, measures every channel, and appends the result to `<dataset_name>.csv` **relative to the current working directory**. If that CSV already exists it is renamed with a timestamp; nothing is overwritten.

`segment_channel` defaults to the first match among `Rhodamine` and `Alexa Fluor 647`. Both are membrane dyes, so segmentation runs on the membrane channel and not on the reporter. If neither is present, the function logs an error and skips the dataset.

`pyramid_level` is the only segmentation parameter that has much effect. Measurements stay in real units at any level, but object size *in pixels* changes fourfold per level, and pixel size is what Cellpose responds to.
:::

| Function | Role |
| --- | --- |
| `process_datasets(dataset_paths, pyramid_level=2)` | Wrap a list of datasets. Note the differing default. |
| `process_frame(data, segment_channel, model, spacing, pbar)` | Segment and measure a single frame. |
| `write_label_zarr(group, labels, coordinateTransformations, axes="tyx", name="Labels")` | Write a label array back into the plate zarr. |
| `release_model()` | Drop the cached model so its GPU memory can be reclaimed. |

:::{danger} `Label` is not stable across timepoints
:icon: false
:class: simple

Each frame is segmented independently and objects are renumbered `1..N`. Grouping by `Label` produces single-object traces that look smooth and are not real. Until a tracking step exists, every time-series view has to be a population aggregate, which is what all the plotting functions above do.
:::

## Naming and axis helpers

The plotting functions call these to resolve their defaults. Call them directly to check what a plot will pick, or to build a column name.

| Name | Returns |
| --- | --- |
| `label_column(data)` | `Name` if a platemap was merged, else `Well` |
| `time_column(data)` | `Time (min)` when real minutes are available, else `Timepoint` |
| `channels(data, stat="Mean")` | Channel labels present, in the order they were written |
| `intensity_column(data, channel=None, stat="Mean")` | The `Intensity {stat} ({channel})` column name |
| `factor_levels(data, column)` | Values of `column`, ascending |
| `factor_palette(data, column)` | One color per level of `column` |
| `quantile_table(data, value, by)` | Median, IQR, P10–P90 and P99 of `value` per group |
| `positive_gate(data, value, quantile=0.99, time=None)` | Per-well threshold from that well's own baseline quantile |

## Column constants

| Constant | Value |
| --- | --- |
| `WELL_COLUMN` | `Well` |
| `TIMEPOINT_COLUMN` | `Timepoint` |
| `TIME_COLUMN` | `Time (min)` |
| `DIAMETER_COLUMN` | `Diameter (Equivalent) (um)` |
| `VOLUME_COLUMN` | `Volume (um^3)` |
| `LABEL_COLUMNS` | `("Name", "Well")` |
| `INTENSITY_COLUMN` | pattern matching `Intensity {stat} ({channel})` |
| `GATE_QUANTILE` | `0.99` |
| `PYRAMID_LEVEL_COLUMN` | `Pyramid Level` |
| `CENTROID_COLUMNS` | the centroid column names |
| `DEFAULT_CROP_INFO` | default per-object annotations in `plot_cell_grid` |
