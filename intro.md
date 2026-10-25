---
title: Nucleus
description: Validated lab protocols, module specifications, and implementation guides for building synthetic cells with PURE system-based cytosol.
site:
  hide_outline: true
---

<a href="./about/release-notes/v060.md" class="version-badge">Nucleus v0.6.0</a> <a href="./about/license.md" class="version-badge">Open Source</a>

Nucleus is an open platform for synthetic cell development, maintained by [b.next](https://bnext.bio). It brings together validated protocols, modular biological components, digital tools, and physical materials — everything you need to start building synthetic cells in one place. Platform tools make it easy to contribute new capabilities back to the distribution, documented for reuse and interoperable with Nucleus specifications. Contributions come from across the synthetic cell research community — see the full list of [contributors](about/contributors.md).

<a href="./start/first-guide.md" class="quick-link">Get started</a> <a href="./about/release-notes/v060.md" class="quick-link">🎊 What's new in v0.6.0</a> <a href="https://github.com/nucleus-eng" class="quick-link">GitHub</a> <a href="https://bnextbio.typeform.com/nucleus-signup" class="quick-link">Join the mailing list</a>

---

## Documentation

Nucleus Documentation is the protocol and specification library for the Nucleus Distribution. Here you'll find validated lab protocols, module specifications, and implementation guides for building synthetic cells using cytosol based on the PURE system. Documentation is built from [Developer Notes](https://devnotes.nucleus.engineering), the primary mechanism for contributing validated research to the Nucleus Distribution.


### ✨ Featured

::::{grid} 1 1 3 3

:::{card}
:header: 🧱 **Modules**
- [tetR-aTc Detector](docs/modules/detector-tetr-atc/spec.md)
- [ClpXP Control Module](docs/modules/control-clpxp/spec.md)
- [Cx43 Membrane Pore](docs/modules/membrane-pore-cx43/spec.md)

[See all Modules →](docs/modules/modules-main.md)
:::

:::{card}
:header: ⚙️ **Processes**
- [Encapsulation: Phase Transfer](docs/processes/assemble-base-cell/main.md)
- [Assemble Base Cytosol](docs/processes/assemble-base-cytosol/main.md)
- [Make Ribosomes](docs/processes/make-ribosomes/main.md)

[See all Processes →](docs/processes/processes-main.md)
:::

:::{card}
:header: 🔬 **Cells**
- [Responder Cell](docs/implementations/responder-atc-ivhsl/main.md)
- [Emitter Cell](docs/implementations/emitter-ivhsl/main.md)
- [Base Cell](docs/modules/base-cell/spec.md)

[See all Implementations →](docs/implementations/implementations-main.md)
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
Implementations are Cells, and other useful combinations of Modules and Processes.
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
:link: cdk/cdk-main.md
Python library for analyzing synthetic cell experiments, from raw instrument output to reportable statistics. Available via PyPI: `pip install nucleus-cdk`.
:::

:::{card}
:header: 📖 **Guides**
:link: guides/main.md
Tutorials, how-tos, and workshop materials for using the Nucleus Distribution and its digital tools.
:::

::::

### 🧪 Recent DevNotes

Modules, Processes, Implementations, and the resources above all grow from DevNotes the community contributes. The five most recent are shown here; browse the full collection at [DevNotes](https://devnotes.nucleus.engineering).

<!-- devnote-highlights:start -->

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Combining Class I & Class II PPK2 in Synthetic Cells
:link: https://devnotes.nucleus.engineering/articles/01a166a7-127b-7b5f-acc9-1a6d8b99ec8c
:footer: Jillian Yujuico, Zach Peterson · October 23, 2026

![](https://pub.curvenote.com/01a166b6-14c8-7d8b-a4f5-dd98fa087583/public/fig1-sds-page-6cf7f246878feb8843be6a87edea3d08.webp)
:::

:::{card} Supplementation and Encapsulation of PPK2 Enzymes in PURExpress Systems
:link: https://devnotes.nucleus.engineering/articles/01a166a8-645c-7748-aed7-b3e7ec381fc7
:footer: Sunayana Nguyen · October 23, 2026

![](https://pub.curvenote.com/01a166af-20f5-7f92-83aa-d75e2a12eb79/public/fig1-control-sfgfp-k-dc770221fc3c5fd1eb766e251a626867.webp)
:::

:::{card} Double Vesicle Lysis System Leveraging deGFP CFPE
:link: https://devnotes.nucleus.engineering/articles/01a16026-42c1-71ad-842a-463d52fae7d8
:footer: Mary Kelly, Madison Briggs · October 22, 2026

![](https://pub.curvenote.com/01a1659b-f37b-7cd9-ac05-7f491b920d6e/public/fig1-two-vesicle-kin-b2f2e21461dd910150fd25955247d4e8.webp)
:::

:::{card} TetO-Regulated PLA1 Sensor in Vesicles: aTc Titration and Spatial Patterning
:link: https://devnotes.nucleus.engineering/articles/01a1304b-1c56-7352-a082-ba84a2684f82
:footer: Mary Kelly, Madison Briggs · October 12, 2026

![](https://pub.curvenote.com/01a1659b-ebfe-71b5-b20a-66b33af95dfb/public/fig7-patterned-gel-5fc6273fa124c69e6d78ac4caafe3ce4.webp)
:::

:::{card} Implementing of a bulk color change module into bacterial quorum sensing
:link: https://devnotes.nucleus.engineering/articles/01a12e6c-b511-7d30-aa95-002d386f751e
:footer: Manuel Bibrowski, Charlie Newell, Jonah McDonald, Niall McIntyre, Julia Purrinos de Oliveira · October 12, 2026

![](https://pub.curvenote.com/01a1650a-90b4-729f-875b-e4f1ddce3bec/public/colorchange-overnigh-520d47ff723d53997b42c0e1c8c68cdc.webp)
:::

::::

<!-- devnote-highlights:end -->

Supported by the Astera Institute, National Science Foundation, Schmidt Sciences, and the Sloan Foundation. [Contact us](mailto:build@bnext.bio) to request access to materials or to get involved.
