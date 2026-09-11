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

This tutorial covers reading a **segmented measurement table** — one row per object per
timepoint — and turning it into population statistics you can interpret.

It assumes segmentation has already run. Producing that table from a plate zarr is a
separate, GPU-bound step (`process_dataset`, documented in the
[cell API reference](../api/cell.md)) that you run once per dataset. Everything here is
pandas and seaborn, fast enough to re-run freely in a notebook.

:::{note} What you need
:icon: false
:class: simple

A measurement table (`.parquet` or `.csv`) written by the segmentation step, and
optionally a **platemap** CSV describing what was in each well. The platemap is what
lets you split figures by experimental factor rather than by well.
:::

## Load

```python
from cdk.analysis import cell as m

data = m.load(PARQUET_URL, PLATEMAP_PATH)
```

`load` reads local paths or `https://` URLs, and accepts either format. The platemap is
merged on `Well`; wells that fail to match are named in a warning rather than silently
dropped.

What comes back is an ordinary `DataFrame`, so anything you already know about pandas
applies. Every plotting function below takes it directly.

### Real timepoints

By default the time axis is `Timepoint` — an integer frame index. Pass
`minutes_per_timepoint` to get real minutes, and every plot will use them automatically:

```python
data = m.load(PARQUET_URL, PLATEMAP_PATH, minutes_per_timepoint=10)
```

:::{attention} Check your acquisition interval
:icon: false
:class: simple

This multiplies the frame index by the interval you supply, so it is only correct if
acquisition actually held that interval. On the Cephla, sampling every well can take
longer than the requested `dt`, which shifts the real timing progressively later. Confirm
the interval your run actually achieved before relying on the axis. A proper per-frame
timestamp is planned; this argument is the current workaround.
:::

On a large dataset, `sample=` draws a random subset of objects, which makes iterating on
a figure much faster.

## Check the segmentation first

Before reading anything into the population statistics, look at what the segmenter
actually found. `plot_cell_grid` draws real image crops with the mask outline on top:

```python
m.plot_cell_grid(data, ZARR_URL, n=4)
```

:::{figure} ./resources/plot-cell-grid.png
:align: center
:label: fig:cell-grid

Segmented objects with mask outlines. **Red** is the selected object; **teal** are its
neighbours that were also segmented. Each object is shown once per channel — here
Alexa Fluor 647 and GFP — scaled to the same intensity range within a channel.
:::

Objects are picked at random unless you narrow the frame you pass in. To inspect a
specific well and timepoint, filter first:

```python
one = data[(data.Well == "M4") & (data.Timepoint == 0)]
m.plot_cell_grid(one, ZARR_URL, n=5, channels=["Alexa Fluor 647"])
```

Segmentation runs on the **membrane** channel, not the reporter — Alexa Fluor 647 or
Rhodamine by default. That is why the membrane channel is the one to check here.

:::{tip} This one is slow
:icon: false
:class: dropdown

`plot_cell_grid` is the only function on this page that reads the image data rather than
the measurement table, so it needs the zarr as well. Over a URL every frame is fetched
whole, which takes seconds per object. Pass `pyramid_level=2` to pull a coarser level, or
copy the zarr locally when you are iterating.
:::

## Did the acquisition hold up?

`plot_qc` answers a different question from the grid above: not "is segmentation
correct" but "did the *imaging* stay stable". It tracks membrane channel intensity and
object count across time.

```python
_ = m.plot_qc(data)
```

:::{figure} ./resources/plot-qc.png
:align: center
:label: fig:qc

Membrane channel intensity and object count over time.
:::

Both are things you want to know *before* interpreting a reporter trend, because either
one can manufacture a signal that looks biological.

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

The percentile view matters because the interesting population is often not the median
one. In the figure above — real data — the **99th percentile** carries the trend of cells
that actually turned on, while the median barely moves. A mean-intensity line would have
shown almost nothing.

### Turning on, or getting brighter?

When a reporter signal rises, two very different things could be happening: more objects
crossed threshold, or the same objects got brighter. `plot_positive_fraction` separates
them.

```python
m.plot_positive_fraction(data, facet="Name", hue="Osmolarity (mM)")
```

:::{figure} ./resources/plot-positive-fraction.png
:align: center
:label: fig:positive-fraction

Three rows, three questions. **Top:** what fraction of objects crossed their baseline
gate. **Middle:** how bright those positives got. **Bottom:** the size of the positive
and negative populations.
:::

The gate is per-well and self-referential: it is that well's own 99th-percentile
intensity at the first timepoint. Each well is therefore compared against its own
starting state rather than a global threshold, which keeps well-to-well brightness
offsets from being read as biology. Adjust it with `gate_quantile=`.

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
the figure above comes from a microscopy tile that was never collected, not from a real
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

When you leave one unset, it resolves:

| Argument | Unset behavior |
| --- | --- |
| `hue` | `Name` if a platemap was merged, otherwise `Well` |
| `time` | `Time (min)` if available, otherwise `Timepoint` |
| `value` | the first channel found among the `Intensity Mean (…)` columns — your reporter |
| `facet` | never guessed; no faceting unless you ask |

Any platemap column works for `hue` and `facet`, so the split is yours to choose:
`facet="Name"` gives one row per lipid mix while `hue="Osmolarity (mM)"` colours within
it. Numeric factors get a sequential colour ramp automatically; categorical ones get
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
