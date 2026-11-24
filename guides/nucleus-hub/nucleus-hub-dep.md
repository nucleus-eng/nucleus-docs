---
title: "Getting Started with Nucleus Hub"
subtitle: "Archived Tutorial"
---

:::{note} Archived
:class: simple
:icon: false

Nucleus Hub is retired. This page is a record of how it worked, kept for reference. See [Nucleus Hub](./nucleus-hub.md) for its current status.
:::

# Overview

This guide introduces Nucleus Hub for accessing the Cell Development Kit (CDK) and collaborating with other Nucleus Developers. For Developer Notes (DevNotes), see [Getting Started: Developer Notes](../developer-notes/developer-notes.md).

# Nucleus Hub Registration

Currently, access to Nucleus Hub is available by request. If you are a Nucleus Contributor, you can gain access by following these steps:

- [ ] Make sure you have a [GitHub Account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github). Take note of your GitHub username.
- [ ] Send an email to the Nucleus team (build@bnext.bio) asking for access to the Nucleus Hub. Please include your GitHub username. They will invite you through GitHub to join the Nucleus Engineering Hub Access GitHub Team. Please watch your email for the invite.
- [ ] Once you accept the invitation, go to https://hub.nucleus.engineering/ and log in with your GitHub credentials.

# Orientation

Upon entering Nucleus Hub you see the Nucleus Hub [landing page](#hub-landing). This section describes a few key interfaces used in common workflows. Nucleus Hub builds on JupyterLab. For a full description of the interface, see the [JupyterLab Docs](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#main-area).

:::::{tab-set}

::::{tab-item} Landing Page
:::{figure} hub-landing.png
:name: hub-landing
Nucleus Hub landing page. 
:::
::::

::::{tab-item} File Browser
:::{figure} hub-file-browser.png
:name: hub-file-browser
The file browser shows your home directory, where notebooks, scripts, datasets, and other files can be saved.
:::
::::

::::{tab-item} Launcher
:::{figure} hub-launcher.png
:name: hub-launcher
The Launcher allows you quickly start a new activity such as creating a new template notebook or creating a new Developer Note.
:::
::::

:::::

## File Browser

Nucleus Hub allows you with a home directory that allows you to save files. To learn more about your home directory and your filesystem, please refer to this documentation [page](https://2i2c.org/community-showcase/user/topics/data/filesystem.html) from 2i2c. The [file browser](#hub-file-browser) is the main interface for managing notebooks, scripts, datasets, and other file types. A few directories exist by default:

:::{table}

| Directory | Access | Permissions | Usage |
| --- | --- | --- | --- | 
| `devnotes/` | private | read/write | A directory to organize DevNotes. When using the Create button from the Launcher, new DevNotes will appear here. |
| `projects/` | shared | read/write | A directory to that provides access to files for specific projects. |
| `sample-data/` | private | read/write | A directory that contains sample data for testing purposes. |
| `shared/` | shared | read | A shared directory that allows Nucleus Hub admins to make files available to all Hub users. |
| `work/` | private | read/write | A private directory to collect your individual work. |

:::


## Launcher

Common Nucleus Hub workflows can be initiated from the [Launcher](#hub-launcher). The button on the Launcher window are organized into the following categories:

:::{table}

| Launcher Category | Function |
| --- | --- |
| Notebook | Create new blank or template notebooks associated with a specific kernel. |
| Console | Initiate an interactive console session associated with a specific kernel. |
| Other | Miscellaneous tools including the ability to initiate a terminal session. |
| Developer Notes | Tools for working with DevNotes. Some features will require setting API access, see [Getting Started: Developer Notes](../developer-notes/developer-notes.md) for more details. |
| Nucleus | Links to other Nucleus resources. |

:::


# Accessing the Cell Development Kit

Nucleus Hub makes it easy to access the CDK to design and analyze experiments. This section will demonstrate a simple workflow for analyzing fluorescence time series data obtained from a microplate reader.  

- [ ]  From the Launcher, click the Template button and select `/analysis/platereader_tutorial.ipynb`, and click GO.
- [ ]  Run the first cell to import the `platereader` library from the CDK.
- [ ]  Check the variables `data_path` and `platemap_path` in the second cell. Update them to the matching files in the `/sample-data/` directory.
- [ ]  Run the cell to load the data.
- [ ]  Generate basic plots using the function `pr.plot_curves()`
- [ ]  These plots can then be incorporated into a Developer Note. See [Developer Notes](../developer-notes/developer-notes.md) for more information.

For a closer look into the workflows supported by the CDK, take a look at the following tutorials:

- [Cytosol Kinetics Analysis Tutorial](../platereader_tutorial.md)

If you are a newcomer to Python and Jupyter, the following links can help:

- Beginner Python tutorial [[link](https://pythonspot.com/)].
- Introduction to the Pandas library [[link](https://tutswiki.com/pandas-cookbook/chapter2/)].
- Introduction to JupyterLab and Jupyter Notebooks [[link](https://jupyter.org/try-jupyter/notebooks/?path=notebooks/Intro.ipynb)].

# Uploading data into the hub

Small datasets (>25 MB) can be uploaded [directly](#hub-upload) into the hub. You can also drag and drop them into the file browser, for example typical plate reader datasets or individual PNGs. We recommend organizing your data by experiment in a directory in your home directory. For example: `/home/work/2026-04-02_my-experiment`.

:::{figure} hub-upload-data.png
:name: hub-upload
Data can directly uploaded into the hub.
:::

<!-- # Collaboration options

Currently, Nucleus Hub supports two options for collaborating with other developers:

**Option 1:** share your entire workspace by generating a shared link. Any existing Nucleus Hub user will be able to read and write to documents in your workspace. 

- Click to the `Generate a Shared Link` icon at the top right corner of the workspace.

**Option 2:** create a collaborative workspace. This will create a special workspace to which a select group of authorized users will have read and write access to documents within that workspace. This option lets users check that their personal workspace stays private. 

- Request a collaborative workspace by reaching out to build@bnext.bio. -->