---
title: "Cell Development Kit"
---

# Overview

The Nucleus Cell Development Kit (CDK) is the Python library for analyzing synthetic
cell experiments. It turns raw instrument output into tidy, plottable data — and then
into the population statistics and kinetic parameters you actually report.

The CDK is organized around the two measurements that dominate synthetic cell work:

:::::{card}

::::{grid} 1 1 2 2

:::{card}
:header: 🔬 **Cell**
:link: ./api/cell.md

Microscopy. Segmented single-object measurements from a plate zarr — size,
intensity, and how a population shifts over time.
:::

:::{card}
:header: 🧪 **Cytosol**
:link: ./api/cytosol.md

Plate reader. Kinetic, endpoint, and spectral reads — blanked, normalized to a
standard, and fit for steady state and rate.
:::

::::
:::::

Both live under the same package and share the same conventions: a platemap describes
your wells, every plot takes the same faceting arguments, and every transform returns
new data rather than mutating what you passed in.

## Install

```bash
pip install nucleus-cdk
```

See [Installation](./install.md) for Python version requirements and the JupyterHub route.

## Where to go next

:::::{card}

::::{grid} 1 1 2 2

:::{card}
:header: **Tutorials**
:link: ./tutorials/tutorials-main.md

Worked analyses from load to figure. Start here.
:::

:::{card}
:header: **API Reference**
:link: ./api/api-main.md

Every public function, grouped by what you are trying to do.
:::

::::
:::::

## Source

The CDK is open source under the MIT license. The package is published on
[PyPI](https://pypi.org/project/nucleus-cdk/) as `nucleus-cdk`, and the source lives on
[GitHub](https://github.com/bnext-bio/nucleus).
