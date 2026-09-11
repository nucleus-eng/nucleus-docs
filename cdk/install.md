---
title: "Installation"
---

# Overview

The CDK is published on PyPI as `nucleus-cdk`. It imports as `cdk`.

## Install with pip

```bash
pip install nucleus-cdk
```

```python
import cdk
print(cdk.__version__)
```

The package requires **Python 3.12 or newer**. It pulls in the scientific Python stack (numpy, pandas, scipy, scikit-learn, statsmodels, seaborn, matplotlib) plus `zarr`, `ome-zarr`, and `cellpose` for the microscopy path, so expect a large download into a fresh environment.

:::{tip} Installing only what you need
:icon: false
:class: dropdown

The microscopy dependencies (`cellpose`, `torch`, `zarr`) are the bulk of the install. If you only intend to analyze plate reader data, the plate reader modules import without touching them — but they are still installed as hard dependencies today. Splitting them into an optional extra is planned.
:::

## Nucleus Hub

If you work on the Nucleus Hub, the CDK is already installed and kept current; you do not need to pip install anything. Select the **b.next CDK** kernel in the top right of your notebook, and the analysis templates come preloaded.

See the [Nucleus Hub guide](../guides/nucleus-hub/nucleus-hub.md) for access.

## Templates

The package ships runnable notebook templates alongside the library, under `notebooks/templates/`. Run one to see a full analysis end to end. The [tutorials](./tutorials/tutorials-main.md) on this site cover the same ground with more explanation.
