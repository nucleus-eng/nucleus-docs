---
title: Developer Notes
---

# Overview

This guide will introduce you to Developer Notes (DevNotes) as a way to quickly share ideas and results with the developer community. This guide assumes that you have familiarized yourself with Nucleus Hub, see [Getting Started with Nucleus Hub](../nucleus-hub/nucleus-hub.md) for more information.

# Configuring Curvenote API Key

Most of the DevNote tools that appear in the Launcher require setting up API access to [Curvenote](https://editor.curvenote.com/) to work as expected. API access can be set up by following these steps:

- [ ] Navigate to the Curvenote [website](https://editor.curvenote.com/) ({ref}`curvenote-login`) and create an account.
- [ ] Create a new blank project and click ‘NEXT’
- [ ]  Go to personal settings ({ref}`curvenote-settings`)
- [ ]  Select ‘API Access’ and click ‘Generate New Token’.
  - [ ]  Give the token a useful description and select Expiry for the maximum time allowed.
- [ ]  From Nucleus Hub, open a terminal window from the Launcher and run the command `curvenote token set [my-token]`
- [ ]  You should see a message that says: Token set for "[curvenote-username]" <curvenote-email-account> at https://api.curvenote.com/login”

:::::{tab-set}

::::{tab-item} Curvenote Login
:::{figure} devnotes-figure-02.png
:label: curvenote-login
:::
::::

::::{tab-item} Curvenote Personal Settings
:::{figure} devnotes-figure-03.png
:label: curvenote-settings
:::
::::

:::::

# Create DevNote

A new DevNote project can be created in Nucleus Hub from the Launcher. The new project will appear in your `devnotes/` directory. This workflow is pulling in our DevNote [project template](https://github.com/nucleus-eng/devnote-template) from GitHub into Nucleus Hub. Follow these steps to create a new project:

- [ ] Create a new DevNote project
  - [ ] Select Create from the row of Nucleus tools on the Launcher.
  - [ ] You will be prompted for some basic information to initialize your project:
    - [ ] "Enter a directory name for your project" -> This is the name of the subdirectory in which your new project will appear, e.g. `devnotes/my-project`
    - [ ] "Add author(s)" -> You can safely skip this step and fill in author information later; however, the most efficient way would be to initialize the project using your ORCID.
    - [ ] "Would you like to start a local server now?" -> This step is unnecessary, press `n`
  - [ ] Find your new DevNote project by using the file browser to navigate to `devnotes/my-project`
  - [ ] Check to see if your author information was entered correctly by inspecting the file `curvenote.yml`.

**Notes**
- You must be in the directory of the project you want to preview.
- This tool can be used in any directory, not just `devnotes`.
- The first time you preview a project may take 10-20 seconds before showing a preview.

**Troubleshooting**

- N/A

# Live Preview

DevNotes are written using [MyST Markdown](https://mystmd.org/), a flavor of Markdown design for technical and scientific communication. DevNotes are built from Markdown (`.md`) and Jupyter Notebook (`.ipynb`) files. The built DevNotes can be inspected in live-preview mode. The following describes how to preview DevNotes in Nucleus Hub:

- [ ] Preview your DevNote.
  - [ ] Use the file browser to navigate to the DevNote directory `devnotes/my-project`. 
  - [ ] Open the file `main.md` in your directory.
  - [ ] Open a new Launcher window by clicking the "+" at the top of the screen.
  - [ ] Click the button "Preview" in the "Developer Notes" toolbar of the Launcher window. Note: you must be in `devnotes/my-project` directory.
  - [ ] You may see an [error message](hub-error). That’s ok.
  - [ ] Create a [split screen](hub-splitscreen) by dragging the "Preview" tab to the right corner of the screen.
  - [ ] Make an edit, say to the level 1 heading, e.g. `#Background - edited`. The preview window should automatically refresh and you should now be able to preview any updates to your DevNote in realtime.

**Notes**
- You must be in the directory of the project you want to preview.
- This tool can be used in any directory, not just `devnotes`.
- The first time you preview a project may take 10-20 seconds before showing a preview.

**Troubleshooting**
- The live-preview is no longer synced to my edits:
  - Refresh the window by right clicking and selecting "Reload Frame" from the context menu (this feature is not available on all browsers).
  - If the sync is still lost, this might signal that there is a fatal error in your project that prevents the document from compiling at all.
- There is a fatal error in my DevNote:

:::::{tab-set}

::::{tab-item} Error message
:::{figure} ./res-tutorial/error-loading-preview.png
:name: hub-error
:::
::::

::::{tab-item} Splitscreen
:::{figure} ./res-tutorial/splitscreen.png
:name: hub-splitscreen
:::
::::

:::::


# Draft Submit

DevNotes that are visible from the Developer Notes website (https://devnotes.nucleus.engineering/) are hosted on a deployment server. Some features of your DevNote may not be accurately represented by using the Preview tool alone. The Draft Submit tool allows you to preview your DevNote exactly as it will appear when hosted on the deployment server and viewed from the Developer Notes website. 

When your DevNote is ready for submission, you can preview how it will look on the Developer Notes site:

- [ ] Draft submit to deployment server.
  - [ ] While you're in the `devnotes/my-project` directory, click the button "Draft Submit" in the "Developer Notes" toolbar of the Launcher window.
  - [ ] Click the URL link at the end of the terminal output. 

**Notes**
- Specific things to keep in mind when inspecting your draft include:
  - Properly formatted thumbnail image.
  - Functional cross-referenced Jupyter cells.
  - All attachments and files are included.

**Troubleshooting**
- N/A

# Submit

If things look good after inspecting your DevNote using "Draft Submit", you can submit your draft to be posted by using the Publish tool. This will send the DevNote to the Nucleus Core development team.

- [ ] Submit DevNote
  - [ ] While you're in the `devnotes/template` directory, click the button "Publish" in the "Developer Notes" toolbar of the Launcher window.
  - [ ] Someone from the Nucleus Core development team will be in touch with you soon. 

**Notes**
- N/A

**Troubleshooting**
- N/A

<!-- # Using Curvenote Preview to view a DevNote





---
title: "Tutorial: submitting your first DevNote"
---

# Overview

This tutorial will walk you through the entire workflow for submitting a DevNote. This tutorial is broken into three sections.

- Creating a DevNote project from the standard template
- Populating the DevNote with content
- Reviewing and submitting the DevNote for display

This tutorial assumes the following:

- It assumes that you have access to Nucleus Hub and are familiar with its basic features.
- Have a Curvenote account
- Have an ORCID

If you do not have these things please see the [Tutorial: getting started with Nucleus Hub](../guides/nucleus-hub/nucleus-hub.md).

# Creating project from template

- [ ] From the Launcher window select the button "Create" in the "Developer Notes" toolbar and follow the dialogue:
  - [ ] Enter a directory name for the DevNote: `template`
  - [ ] Project title: `My first project`
  - [ ] Subtitle: `My first subtitle`
  - [ ] Description: `My first Description`
  - [ ] Add author(s): `[YOUR ORCID]`
  - [ ] Keywords: Hit `[Enter]` to skip
  - [ ] Would you like to start a local server now? `n`
  - [ ] Exit the terminal and return to the Launcher Window

- [ ] Preview your DevNote.
  - [ ] In your file directory, navigate to the directory `/devnotes/template` it should appear like [this]().
  - [ ] While you're in the `devnotes/template` directory, click the button "Preview" in the "Developer Notes" toolbar of the Launcher window.
  - [ ] You will likely see an [error message](fig:error). That's ok.
  - [ ] Open the file `main.md` in your directory
  - [ ] Create a [split screen](fig:splitscreen) by dragging the "Preview" tab to the right corner of the screen.
  - [ ] Make an edit, say to the level 1 heading, e.g. `#Background - edited`. The preview window should automatically refresh and you should now be able to preview any updates to your DevNote in realtime.

:::::{tab-set}

::::{tab-item} Error message
:::{figure} ./developer-notes/res-tutorial/error-loading-preview.png
:name: fig:error
:::
::::

::::{tab-item} Splitscreen
:::{figure} ./developer-notes/res-tutorial/splitscreen.png
:name: fig:splitscreen
:::
::::

:::::

# Authoring the DevNote

The DevNote template contains documentation describing how to author your first DevNote. Please take a look at the `README.md` and `main.md` which contains the markdown of a DevNote that describes how to make a DevNote.

# Review and submission

When your DevNote is ready for submission, you can preview how it will look on the Developer Notes site:

- [ ] Preview DevNote on deployment server
  - [ ] While you're in the `devnotes/template` directory, click the button "Preview" in the "Developer Notes" toolbar of the Launcher window.
  - [ ] Click the URL link at the end of the terminal output. 

- [ ] Submit DevNote for posting
  - [ ] While you're in the `devnotes/template` directory, click the button "Submit" in the "Developer Notes" toolbar of the Launcher window.
  - [ ] Someone from the Nucleus Core developer team will be in touch with you soon. 


# Setting up your DevNote

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

### **Connecting a Jupyter Notebook to a DevNote**

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
    plt.savefig("./analysis/my-fig.png")
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
    
    - [ ]  Multiple figures can be handled elegantly by using tabs:
    
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
    
    - [ ]  Verify that the changes have been made by clicking Curvenote Preview. -->