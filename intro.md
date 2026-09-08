---
title: Nucleus
description: Validated lab protocols, module specifications, and implementation guides for building synthetic cells with PURE system-based cytosol.
site:
  hide_outline: true
---

<a href="./about/release-notes/v060.md" class="version-badge">Nucleus v0.6.0</a> <a href="./about/license.md" class="version-badge">Open Source</a>

Nucleus is an open platform for synthetic cell development, maintained by [b.next](https://bnext.bio). It brings together validated protocols, modular biological components, digital tools, and physical materials — everything you need to start building synthetic cells in one place. Platform tools make it easy to contribute new capabilities back to the distribution, documented for reuse and interoperable with Nucleus specifications.

<a href="./start/first-guide.md" class="quick-link">Get started</a> <a href="./about/release-notes/v060.md" class="quick-link">🎊 What's new in v0.6.0</a> <a href="https://github.com/nucleus-eng" class="quick-link">GitHub</a> <a href="https://bnextbio.typeform.com/nucleus-signup" class="quick-link">Join the mailing list</a>

---

## Documentation

Nucleus Documentation is the protocol and specification library for the Nucleus Distribution. Here you'll find validated lab protocols, module specifications, and implementation guides for building synthetic cells using cytosol based on the PURE system. Documentation is built from [Developer Notes](https://devnotes.nucleus.engineering), the primary mechanism for contributing validated research to the Nucleus Distribution.


### ✨ Featured

::::{grid} 1 1 3 3

:::{card}
:header: 🧱 **Modules**
- [tetR-aTc Detector](docs/modules/detector-tetr_atc/spec.md)
- [ClpXP Control Module](docs/modules/control-clpxp/spec.md)
- [Cx43 Membrane Pore](docs/modules/membrane-pore-cx43/spec.md)
:::

:::{card}
:header: ⚙️ **Processes**
- [Encapsulation: Phase Transfer](docs/processes/assemble-base-cell/main.md)
- [Assemble Base Cytosol](docs/processes/assemble-base-cytosol/main.md)
- [Make Ribosomes](docs/processes/make-ribosomes/main.md)
:::

:::{card}
:header: 🔬 **Cells**
- [Responder Cell](docs/implementations/responder-atc-ivhsl/main.md)
- [Emitter Cell](docs/implementations/emitter-ivhsl/main.md)
- [Base Cell](docs/modules/base-cell/spec.md)
:::

::::

### How the Docs are structured

Nucleus Cytosol can be extended with Modules, assembled into Cells using Processes, and combined into Implementations. Supporting resources cover the DNA Distribution, software tools, and guides.

::::{grid} 1 1 3 3

:::{card}
:header: 🧱 **Modules**
:link: docs/modules/modules-main.md
Modules extend the functionality of Base Cytosol and Cells.
:::

:::{card}
:header: ⚙️ **Processes**
:link: docs/processes/processes-main.md
Processes are core protocols for implementing Base Cytosol and Cells.
:::

:::{card}
:header: 🏗️ **Implementations**
:link: docs/implementations/implementations-main.md
Implementations are useful combinations of Modules and Processes.
:::

::::

::::{grid} 1 1 3 3

:::{card}
:header: 🧬 **DNA Distribution**
:link: docs/dna-distro.md
Physical materials that are used to implement Processes and Modules.
:::

:::{card}
:header: 🛠️ **Cell Development Kit**
:link: https://pypi.org/project/nucleus-cdk/
Software tools for working with the Nucleus Distribution. Available via PyPI: `pip install nucleus-cdk`.
:::

:::{card}
:header: 📖 **Guides**
:link: guides/main.md
Tutorials, how-tos, and workshop materials for using the Nucleus Distribution and its digital tools.
:::

::::

Supported by the Astera Institute, National Science Foundation, Schmidt Sciences, and the Sloan Foundation. [Contact us](mailto:build@bnext.bio) to request access to materials or to get involved.
