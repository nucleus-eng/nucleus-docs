---
title: "Parts of a Developer Note"
subtitle: "Reference"
---

# Overview

This page provides reference documentation describing the basic properties of files that compose a Developer Note (DevNote). It assumes that you have familiarized yourself with the basics of [Nucleus Hub](../nucleus-hub/nucleus-hub.md) and have made a [DevNote](../developer-notes/developer-notes.md). If you are looking for examples of useful MyST Markdown syntax please refer to the relevant documentation [page](../developer-note-syntax.md). 

# Filestructure

A DevNote can be thought of as a repository of research artifacts that can include Markdown text, code, datasets, design files, and any other supporting documents. A minimal DevNote project might have the following file structure:

<!-- :::::{tab-set}

::::{tab-item} Code -->
```
# As seen in the file browser in Nucleus Hub

devnotes/my-project/
├── _build/
├── experiments/
├── general/
├── banner.webp
├── thumbnail.png
├── curvenote.yml
├── base.yml
├── environment.yml
├── main.md
└── README.md

```
<!-- ::::

::::{tab-item} figure
:::{figure} devnotes-figure-01.png
:::
::::


::::: -->

## Key Files

- `main.md` - this MyST Markdown file is main document of your DevNote.
- `curvenote.yml` - this [YAML](https://en.wikipedia.org/wiki/YAML) file defines the structure, content, and settings of the DevNote including its authors and title.
- `base.yml` - this YAML file extends the curvenote.yml with additional settings that a typical DevNote author would normally not need to interact with. 
- `environment.yml` - this YAML file describes the computational environment, enabling reproducibility and portability of the project's code. This file is for advanced users who want to include additional software dependencies in their DevNote.
- `thubnail.png` - this file defines the gallery image describing the DevNote. You can think of it as a Table of Contents figure. It defaults to the first figure of your DevNote.
- banner.webp - this file defines the banner image rendered at the top of the DevNote.
- `README.md` - this is the DevNote's [README](https://en.wikipedia.org/wiki/README). It can be used to provide additional context for people who will access the project files directly.

## Directories

- `_build/` - this directory contains the [build files](https://en.wikipedia.org/wiki/Software_build) that are used to render your DevNote for the web. These are automatically generated and you do not need to interact with them. 
- `experiments/` - this directory can be used to contain files associated with individual experiments. A useful pattern involves creating sub-directories self-contained experiments in this experiment that include things like relevant datasets, design files, analysis notebooks, and other experiment specific files.
- `general/` - this directory can be used to contain files do not pertain to a specific experiment such as schematics that provide an overview of an experimental arc, instrument documentation, lab notebook entries that may span multiple experiments, DNA sequence maps, and any other resources that are not associated with any single experiment.

<!-- **Notes**

- additional directories can be added
  
**Troubleshooting**
- files don't appear in Draft Submit -->

<!-- # curvenote.yml



# main.md

# Jupyter Notebooks

# Supplementary Files -->