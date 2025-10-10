---
title: Developer Notes
---

## Overview

This guide will introduce you to Developer Notes (DevNotes) as a way to quickly share ideas and results with the developer community. This guide assumes that you have familiarized yourself with Nucleus Hub Nucleus Hub..

## Using Curvenote Preview to view a DevNote

- [ ]  From the Launcher window, select the icon for Curvenote Preview.
- [ ]  You will see a window ({ref}`fig:01`) that says ‘Please set your Curvenote token:
- [ ]  After navigating to the Curvenote website ({ref}`fig:02`), create a Curvenote account
- [ ]  Create a new blank project and click ‘NEXT’
- [ ]  Go to personal settings ({ref}`fig:03`):
- [ ]  Select ‘API Access’ and click ‘Generate New Token’.
    - [ ]  Give the token a useful descrption and select Expiry for the maximum time allowed.
    - [ ]  Open a terminal window from the Launcher window and run the command `curvenote token set [my-token]`
    - [ ]  You should see a message that says: Token set for "[curvenote-username]" <curvenote-email-account> at https://api.curvenote.com/login”
- [ ]  You should now be able to view a DevNote by clicking Curvenote Preview from the Launcher window. Note: it may take up to a minute to populate the following viewer window if this is the first time you using the Preview feature.
- [ ]  click the `template/` directory.
- [ ]  Congratulations! You should now see a rendered DevNote file  ({ref}`fig:04`):


:::::{tab-set}

::::{tab-item} Tab Title 1
:sync: tab1-1
:::{figure} devnotes-figure-01.png
:label: fig:01
:::
::::

::::{tab-item} Tab Title 2
:sync: tab1-2
:::{figure} devnotes-figure-02.png
:label: fig:02
:::
::::

::::{tab-item} Tab Title 3
:sync: tab1-3
:::{figure} devnotes-figure-03.png
:label: fig:03
:::
::::

::::{tab-item} Tab Title 4
:sync: tab1-4
:::{figure} devnotes-figure-04.png
:label: fig:04
:::
::::

:::::


## Setting up your DevNote

- [ ]  In the File Directory (left panel), navigate to the `/devnotes/` directory and make a copy of the `/template/` directory and rename it. Note: we recommend that you always work off of a copy of the template file and never edit the template file itself so that it can serve as a working reference.
- [ ]  Inspect the output of the directory. In the Launcher Window (Main Panel), click Curvenote Preview and then select your renamed template file.
- [ ]  Change the title and author of your DevNote by opening the file `curvenote.yml` from the File Directory and modify the corresponding fields:

```markdown
# Ensure your title is the same as in your `main.md`
  title: "An Unexpected Enzyme in PURE"  
  subtitle: "The enzyme MTHFS is needed for 36 pot PURE"
  description:  
# Add any supporting files to the toc, but ensure that your main manuscript
# is first is the list. The title field is optional.
# Authors should have affiliations, emails and ORCIDs if available
  authors:
    - name: Sam Cell
      email: samcell@bnext.bio
      orcid: 0000-0001-1234-1234
      affiliations:
        - b.next
```

### **Connecting a Jupyer Notebook to a DevNote**

- [ ]  Navigate to your DevNote’s experimental directory `devnotes/my-devnote/experiments/`
- [ ]  In your current directory, open a Launcher Window by creating a new tab (”+” button) from the main panel. Click the Template icon, select `/analysis/platereader.ipynb`, and click GO. Note: there is a working analysis notebook already in the directory to serve as a reference: `20250220-analysis.ipynb`.
- [ ]  Link this notebook to your DevNote by including a reference to it in your `curvenote.yml` file as follows:

```markdown
# Add any supporting files to the toc, but ensure that your main manuscript
# is first is the list. The title field is optional.
  toc:
    - file: main.md
    - file: ./experiments/experiment-01/my-platereader.ipynb
      title: Analysis Notebook
```

- [ ]  In the newly created Jupyter Notebook, adjust the paths to your platemap and data file respectively.
- [ ]  Run the notebook cells.
- [ ]  The figure output of a cell can be referenced in two ways. We recommend using both.
    - [ ]  Option 1: save the output of a cell to the `/analysis/` directory by adding the following code to the end of the cell:
    
    ```python
    plt.savefig(./analysis/my-fig.png)
    ```
    
    - [ ]  Option 2: label the cell by adding the following syntax to the top of the cell:
    
    ```markdown
    #| label: fig:name-of-figure
    ```
    
    - **Note: complete documentation of MyST Markdown is available online**
        
        MyST specification: https://mystmd.org/spec
        
- [ ]  If the output of a cell is a table rather than a figure , it can be referenced as follows:
    - [ ]  Label the cell by adding the following syntax to the top of the cell:
    
    ```markdown
    #| label: tbl:name-of-table
    ```
    

### **Reference figures in `main.md`**

- [ ]  A figure can be generated in two ways depending on how you want to reference it:
    - [ ]  Option 1: reference the saved file:
    
    ```markdown
    :::{figure} ./experiments/experiment-01/my-fig.png
    :name: name-of-fig
    :align: center
    :width: 50%
    
    My caption
    :::
    ```
    
    - [ ]  Option 2: reference the output of a labelled jupyter cell:
    
    ```markdown
    :::{figure} #fig:name-of-figure
    :kind: table
    :name: name-of-fig
    :width: 50%
    
    My caption
    :::
    ```
    
    - [ ]  Multiple figures can be handled elegently by using tabs:
    
    ```markdown
    :::::{tab-set}
    
    ::::{tab-item} Tab Title 1
    :sync: tab1
    :::{figure} #fig:name-of-figure-1
    :name: name-of-fig-1
    :align: center
    :width: 50%
    
    My caption 1
    :::
    ::::
    
    ::::{tab-item} Tab Title 2
    :sync: tab2
    :::{figure} ./experiments/experiment-01/my-fig-2.png
    :name: name-of-fig-2
    :align: center
    :width: 50%
    
    My caption 2
    :::
    ::::
    
    :::::
    ```
    
    - [ ]  A table output can be included from a labelled jupyter cell as follows:
    
    ```markdown
    :::{figure} #tbl:name-of-table
    :kind: table
    :name: name-of-table
    
    My caption
    :::
    ```
    
    - [ ]  Figures and tables can be referenced in documents using the following syntax:
    
    ```markdown
    This point is illustrated in {ref}`name-of-fig`.
    ```
    
    - [ ]  Verify that the changes have been made by clicking Curvenote Preview.