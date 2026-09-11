---
title: "Analyzing Microscopy Data"
subtitle: "Cell population analysis with the CDK"
---

:::{attention}
:icon: false
:class: simple

The interface described here is not yet in the released `nucleus-cdk` package. Version
0.6.0 exposes only `cdk.analysis.cell.microscopy`; the functions below ship in the next
release and are available now on the Nucleus Hub.
:::

# Overview

This tutorial covers reading a **segmented measurement table**. Producing this table from a plate zarr is a
separate step (`process_dataset`, documented in the
[cell API reference](../api/cell.md)) that must be run once per dataset. 

:::{note} What you need
:icon: false
:class: simple

A measurement table (`.parquet` or `.csv`) written by the segmentation step, and a **platemap** CSV describing what was in each well. The platemap is what
lets you split figures by experimental factor rather than by well.
:::

## Load

```python
from cdk.analysis import cell as m

data = m.load(PARQUET_URL, PLATEMAP_PATH)
```

`load` reads local paths or `https://` URLs, and accepts either format. The platemap is
merged on `Well`; wells that fail to match are named in a warning. This returns an `DataFrame` that can be processed by pandas.

### Real timepoints

By default the time axis is `Timepoint` — an integer frame index. Pass
`minutes_per_timepoint` to get real minutes. If you do this, every plot will use them automatically. 

```python
data = m.load(PARQUET_URL, PLATEMAP_PATH, minutes_per_timepoint=10)
```

:::{attention} Check your acquisition interval
:icon: false
:class: simple

This multiplies the frame index by the interval you supply, so it is only correct if
acquisition followed that interval. On the Cephla, sampling every well can take
longer than the requested `dt`, which shifts the real timing progressively later. Confirm
the interval your run actually achieved before relying on the axis. A proper per-frame
timestamp is planned; this argument is the current workaround.
:::

On a large dataset, `sample=` draws a random subset of objects, which makes iterating on
a figure much faster.

## Check the segmentation first

Before reading anything into the population statistics, look at what got segmented. `plot_cell_grid` draws real image crops with the mask outline on top:

```python
m.plot_cell_grid(data, ZARR_URL, n=4)
```

:::{figure} ./resources/plot-cell-grid.png
:align: center
:label: fig:cell-grid

Segmented objects with mask outlines. **Red** is the selected object; **teal** are its
neighbours that were also segmented. Each object is shown once per channel (here Alexa Fluor 647 and GFP) scaled to the same intensity range within a channel.
:::

Objects are picked at random unless you narrow the frame you pass in. To inspect a
specific well and timepoint, filter first:

```python
example_subset = data[(data.Well == "M4") & (data.Timepoint == 0)]
m.plot_cell_grid(example_subset, ZARR_URL, n=5, channels=["Alexa Fluor 647"])
```

:::{tip} This one is slow
:icon: false
:class: dropdown

`plot_cell_grid` reads the image data rather than
the measurement table, so it needs the zarr as well. Doing this for many cells could take quite some time. 
:::

## How did general cells and segementation channel come out?

`plot_qc` tracks membrane channel intensity and
object count across time.

```python
_ = m.plot_qc(data)
```

:::{figure} ./resources/plot-qc.png
:align: center
:label: fig:qc

Membrane channel intensity and object count over time.
:::

## How did the population shift?

`plot_quantile_ribbon` is the main population view: the median as a solid line, with
the inter-quartile range and P10–P90 as shaded bands.

```python
m.plot_quantile_ribbon(data, hue="Osmolarity (mM)", facet="Name")
```

:::{figure} ./resources/plot-quantile-ribbon.png
:align: center
:label: fig:quantile-ribbon

Population percentiles over time. The solid line is the median; bands are the percentile
ranges named in the legend.
:::

We split up into percentiles here because we noticed that there are oftentimes two separate populations: one that is actually turned on and others that practically do not turn on. 
In the figure above from real data, the **99th percentile** carries the trend of cells
that actually turned on, while the median barely shifts in intensity. 

### Turning on, or getting brighter?

Here we track how the changes in the population at the upper percentile (positive) compare to the lower percentile (negative).

```python
m.plot_positive_fraction(data, facet="Name", hue="Osmolarity (mM)")
```

:::{figure} ./resources/plot-positive-fraction.png
:align: center
:label: fig:positive-fraction

**Top:** what fraction of objects crossed their baseline
gate. **Middle:** how bright those positives got. **Bottom:** the size of the positive
and negative populations.
:::

% of objects above their well's baseline threshold (set at t=0), the median brightness of those positives, and the median size of each population. 
Adjust the baseline percentage threshold with `gate_quantile=`.

### Does size correlate with expression?

```python
_ = m.plot_size_expression(data, facet="Name")
```

:::{figure} ./resources/plot-size-expression.png
:align: center
:label: fig:size-expression

Per-object reporter intensity against volume, as a hexbin with a fit line per panel.
:::

:::{warning} Two things to know about this figure
:icon: false
:class: dropdown

**The low-intensity population is an artifact.** The band of objects at very low GFP in
the figure above comes from a dropped microscopy tile, and not from a real
dim subpopulation. If you see a suspiciously clean low-intensity cluster, check your tiles
before interpreting it, we noticed in earlier versions of microscopy hardware, tiles could be dropped. 

**The fit line is fit to everything.** It is not split by percentile, so a skewed
population pulls it. Read it as an eyeline, not an estimate. Updates forthcoming. 
:::

## Splitting figures by experimental factor

Every plotting function takes the same four arguments — `hue`, `facet`, `time`, and
`value` — and all four default to `None`. This is where a platemap is very useful. 

```python
m.plot_quantile_ribbon(data)                                       # groups by well
m.plot_quantile_ribbon(data, hue="Osmolarity (mM)", facet="Name")  # crosses two factors
```

The default values are: 

| Argument | Default behavior                                                             |
| --- |------------------------------------------------------------------------------|
| `hue` | `Name` if a platemap was merged, otherwise `Well`                            |
| `time` | `Time (min)` if available, otherwise `Timepoint`                             |
| `value` | the first channel found among the `Intensity Mean (…)` columns — your reporter |
| `facet` | None                                           |

Numeric factors get a sequential colour ramp automatically; categorical ones get
distinct colours.

## Caveats 

:::{danger} `Label` is not stable across timepoints
:icon: false
:class: simple

Each frame is segmented independently and objects are renumbered `1..N` every time.
The object called `Label 7` at timepoint 0 is almost certainly **not** the object called
`Label 7` at timepoint 1.

Grouping by `Label` produces smooth, convincing single-object traces that are fiction.
On a measured dataset, a label's centroid moves 190–1600 µm between consecutive frames
while the nearest real object sits 13–21 µm away — and that nearest object carries the
same id only 0–15% of the time.

Until a tracking step exists, **every time-series view must be a population aggregate**.
That is exactly what the functions on this page do.
:::

## Other views

`plot_ecdf` gives the empirical CDF at a few timepoints — the full distribution rather
than summary percentiles. `plot_summary`, `plot_size`, `plot_intensity`, `plot_fogplot`,
and `plot_fogplot_compare` are the earlier generation of overview plots; they still work
and are slated for deprecation in favour of the quantile and gated views above.

Full signatures for all of them are in the [cell API reference](../api/cell.md).
