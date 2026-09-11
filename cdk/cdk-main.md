---
title: "Cell Development Kit"
---

# Overview

The Nucleus Cell Development Kit (CDK) is a Python library for analyzing synthetic cell experiments. It reads instrument output into a DataFrame and gives you population statistics, curve fits, and plots.

We currently assume cellular data uses microscopy and cytosol (bulk) data comes from plate readers. The CDK splits that up respectively. The APIs are found here:
:::::{card}

::::{grid} 1 1 2 2

:::{card}
:header: 🔬 **Cell**
:link: ./api/cell.md

Microscopy data. Segmented single-object measurements from a plate zarr: size, intensity, and how a population shifts over time.
:::

:::{card}
:header: 🧪 **Cytosol**
:link: ./api/cytosol.md

Plate reader data. Kinetic, endpoint, and spectral reads, with blanking, normalization to a standard, and fits for steady state and rate.
:::

::::
:::::

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

Worked analyses from load to figure. Start here if you are new to the CDK.
:::

:::{card}
:header: **API Reference**
:link: ./api/api-main.md

Every public function, grouped by analysis stage.
:::

::::
:::::

## Source

The CDK is open source under the MIT license. The package is published on [PyPI](https://pypi.org/project/nucleus-cdk/) as `nucleus-cdk`, and the source lives on [GitHub](https://github.com/bnext-bio/nucleus).
