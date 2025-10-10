---
title: Nucleus Hub
---

## Overview

This guide will introduce you to Nucleus Hub for accessing the Cell Development Kit (CDK) and collaborating with other Nucleus Developers. 

## Nucleus Hub Registration

Currently, access to Nucleus Hub is available by request to build@bnext.bio.

- [ ]  Navigate to hub.nucleus.engineering.
- [ ]  Follow the prompts to make an account.
- [ ]  After clicking `Create User` , send an email to build@bnext.bio to approve the account.

## Orientation

Upon entering Nucleus Hub you should the following screen:

:::{figure} nucleus-hub-image-01.png
:::

1. File directory.
2. Launcher window.
3. Make a new empty Jupyter Notebook.
4. Make a new template Jupyter Notebook.
5. Preview a Developer Note.
6. Open a terminal window.
7. View a draft of a Developer Note. 

## Accessing the Cell Development Kit

Nucleus Hub makes it easy to access the CDK to design and analyze experiments. This section will demonstrate a simple workflow for analyzing fluorescence time series data obtained from a microplate reader.  

- [ ]  Open the `/sample-data/` directory.
- [ ]  Click the Template icon, select `/analysis/platereader.ipynb`, and click GO.
- [ ]  Run the first cell to import the `platereader` library from the CDK.
- [ ]  Modify the variables `data_path` and `platemap_path` in the second cell to reference the corresponding files in the `/sample-data/` directory and run the cell to load the data.
- [ ]  Generate basic plots using the function `pr.plot_curves()`
- [ ]  These plots can then be incorporated into a Developer Note. See [Developer Notes](https://www.notion.so/Developer-Notes-22dae616eb5180bc9e76dc87f9af0e0e?pvs=21) for more information.

If you are a newcomer to Python and Jupyter the following links may be helpful:

- Beginner Python tutorial [[link](https://pythonspot.com/)].
- Introduction to the Pandas library [[link](https://tutswiki.com/pandas-cookbook/chapter2/)].
- Introduction to JupyterLab and Jupyter Notebooks [[link](https://jupyter.org/try-jupyter/notebooks/?path=notebooks/Intro.ipynb)].

## Collaboration options

Currently, Nucleus Hub supports two options for collaborating with other developers:

**Option 1:** share your entire workspace by generating a shared link. Any existing Nucleus Hub user will be able to read and write to documents in your workspace. 

- Click to the `Generate a Shared Link` icon at the top right corner of the workspace.

**Option 2:** create a collaborative workspace. This will create a special workspace to which a select group of authorized users will have read and write access to documents within that workspace. This option allows users to ensure that their personal workspace remains private. 

- Request a collaborative workspace by reaching out to build@bnext.bio.