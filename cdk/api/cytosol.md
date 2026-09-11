---
title: "Cytosol API"
subtitle: "cdk.instruments.platereader — plate reader"
---

:::{warning}
:class: simple
:icon: false

This page is an outline awaiting content. The structure mirrors the
[cell API reference](./cell.md); the sections below name the entry points but do not yet
describe them. The code itself is released and working — see the
[kinetics tutorial](../tutorials/cytosol-kinetics.md) for usage.
:::

# Overview

Loading, transforming and fitting plate reader data.

```python
from cdk.instruments.platereader import load_platereader_data
```

The plate reader half of the CDK is built around an **immutable object API**: loading
gives you an object that knows what it contains, and every transform returns a new object
rather than mutating the one you have. Provenance travels with the data, so a plot can
label its own axes from the transforms that produced it.

| Module | Role |
| --- | --- |
| `loader` / `loaders` | File → `PlateReaderResult`. Loaders self-register by extension; BioTek is currently the only one. |
| `result` | `PlateReaderResult` and `PlateReaderData` — the core objects. |
| `transforms` | The pure reference-application core behind `blank` and `normalize`. |
| `kinetics` | `Kinetics` — per-group curve fits and their plots. |
| `standardcurve` | `StandardCurve` — a fitted, invertible calibration curve. |
| `legacy` | The pre-refactor function-based pipeline, preserved verbatim. |

## Loading

`load_platereader_data(data_file, platemap_file=None, platereader=None)`

## The data objects

`PlateReaderResult` — a sequence of read blocks.

`PlateReaderResult.take(which=None, *, modality=None)`

`PlateReaderData` — one read block: a long-form frame, a format, and a lineage.

## Transforms

`PlateReaderData.blank(blank_name="Blank", *, window=...)`

`PlateReaderData.normalize(standard_name, *, window=..., group_by=())`

`PlateReaderData.ratio(numerator_read, denominator_read, *, name=None)`

`PlateReaderData.standardize(curve)`

## Selecting rows

`PlateReaderData.select(*, well=None, read=None, read_name=None, modality=None, name=None, type=None)`

## Fitting

`PlateReaderData.fit_kinetics(data_column=None, fit_function_name="sigmoid_drift", group_by=..., completion_threshold=0.95)`

`PlateReaderData.fit_standard_curve(*, known, standard_name="Standard", model="linear", data_column=None)`

## Kinetics results

`Kinetics.plot(...)`, `Kinetics.plot_data(...)`, `Kinetics.plot_summary(...)`,
`Kinetics.plot_response(x, y, ...)`

## Plotting data

`PlateReaderData.plot(...)`, `PlateReaderData.plot_plate(...)`

## Platemaps

`load_platemap(path, sep=",")`, `validate_platemap(df)`, `merge_platemap(data, platemap)`

## Legacy API

`cdk.instruments.platereader.legacy` — DataFrame-in / DataFrame-out. Reach for it when
you need the rolling-window steady-state analysis or the wider instrument set (Envision,
Glomax) that the object API does not cover yet.

:::{note} Migrating an old notebook
:icon: false
:class: simple

Notebooks written before the refactor start with:

```python
from cdk.analysis.cytosol import platereader as pr
```

That module no longer exists. Replace the line with:

```python
import cdk.instruments.platereader.legacy as pr
```
:::
