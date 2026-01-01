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