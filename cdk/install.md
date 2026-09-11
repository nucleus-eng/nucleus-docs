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

## Nucleus Hub

If you work on the Nucleus Hub, the CDK is already installed and kept current; you do not need to pip install anything. Select the **b.next CDK** kernel in the top right of your notebook, and the analysis templates come preloaded.

See the [Nucleus Hub guide](../guides/nucleus-hub/nucleus-hub.md) for access.

## Templates

The package ships runnable notebook templates alongside the library, under `notebooks/templates/`. Run one to see a full analysis end to end. The [tutorials](./tutorials/cdk-tutorials-main.md) on this site cover the same ground with more explanation.
