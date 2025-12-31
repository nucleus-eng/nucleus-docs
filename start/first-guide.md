---
title: "Beginner's Guide" 
subtitle: "From Zero to DevNote: a Beginner's Guide to the Nucleus Technology Stack"
---

# Overview

The purpose of this tutorial is to guide a newcomer through the complete Nucleus technology stack and supporting workflows. 

:::{figure} ./resources/flowchart.png
**The Nucleus Development Cycle.** All components of the Nucleus platform work together to support the collaborative development of increasingly reliable and sophisticated synthetic cells contained within the Distribution. The **Documentation** (this site) is a knowledge base that contains protocols and  documentation for implementing validated synthetic cell modules. The **Hub** provides a resource for data sharing, analysis using standard digital tools. Useful results can be shared with the community as **DevNotes**. DevNotes can be viewed on the **Developer Note** website. Periodically, contributions made as Devnotes are integrated into the Distribution as validated protocols for others to use and build upon. All components of the platform can be discussed at the **Forum**, come say hello!
:::

At the end of this tutorial you will have used the Protocols in the Distribution to assemble Base Cytosol, characterize its performance using the Cell Development Kit (CDK) on Nucleus Hub, and finally post a Developer Note (DevNote) that reports on its performance. 

This tutorial assumes that you have the necessary components of Base Cytosol: small molecule mix, tRNA, protein mix, ribosomes, and a suitable reporter plasmid such as `pOpen-deGFP`. The components of Base Cytosol can be obtained in two ways: you can make them yourself from scratch, or you can acquire a premade reagent kit from b.next. 

If you are looking to get started quickly, we recommend acquiring a kit from b.next. If you prefer more control over the cytosolic system, the distribution contains materials, protocols, and documentation for making your own components from scratch. 

:::{note} Prerequisite
:class: simple
:icon: false

This tutorial assumes access to Nucleus Hub, which requires admin approval. Please reach out to build@bnext.bio.
:::

<!-- The purpose of this page is to guide a newcomer through the complete Nucleus technology stack and workflows, from assembling Base Cytosol and characterizing its performance using the Cell Development Kit (CDK) on Nucleus Hub, to finally posting a Developer Note (DevNote) that reports on its performance. -->


<!-- Since this is likely the first Nucleus Guide you have encourntered, it will walk through every step with a significant amount of detail. In general, guides tie together documentation from across the site into useful workflows. -->

# Using the Distribution as a knowledge base

The Distribution contains numerous validated protocols and other documentation organized across four different categories: DNA Distribution, Processes, Modules, and Implementations. Assembling Base Cytosol is regarded as a fundamental process in the Distribution, so protocols and documentation for its assembly can be found in the [Processes]() section. We recommend exploring the four Protocol category pages to get a sense for how the documentation is organized.

Now that we're more oriented in the documentation let's navigate to the protocol we'd like to implement:

- [Assemble Base Cytosol](../docs/processes/assemble-base-cytosol/main.md)

If you follow the steps on that page, you should find yourself with some data in hand ready to be analyzed. Rather than firing up Excel or opening a Google Sheet, we're going to sign into Nucleus Hub. 

<!-- TODO: talk about platemaps -->

<!-- In contrast, Modules extend the functionality of fundamental processes.  -->



<!-- The components of Base Cytosol can be obtained by either making them yourself or as a premade reagent kit. This distribution includes documentation for making Base Cytosol yourself from scratch. A same-formulation Base Cytosol can also be obtained as a kit from b.next.  -->

<!-- This tutorial assumes that you have the necessary components of Base Cytosol: small molecule mix, tRNA, protein mix, ribosomes, and a suitable reporter plasmid such as `pOpen-deGFP`. The components of Base Cytosol can be obtained in two ways: you can make them yourself from scratch, or you can purchase a premade reagent kit from b.next. This documentation includes instructions for making Base Cytosol yourself. 

This tutorial assumes that you have the necessary components of Base Cytosol: small molecule mix, tRNA, protein mix, ribosomes, and a suitable reporter plasmid such as `pOpen-deGFP`. These components can be obtained by making them yourself from scratch (as covered in this documentation) or by purchasing a premade reagent kit from b.next. -->



<!-- This distribution includes documentation for making it yourself from scratch. An open-formulation version can also be obtained from b.next. Since the goal of this guide is provide detailed introduction to the whole Nucleus Workflow, we'll start with the Base Cytosol Kit.  -->

<!-- - [Assemble Base Cytosol]() -->

<!-- If you follow the steps on that page, you shoud find yourself with some data in hand ready to be analyzed. Rather firing up Excel or opening a Google Sheet, we're going to sign into Nucleus Hub.  -->

## Analyzing Data with Nucleus Hub

Nucleus Hub is an interactive computing platform built on JupyterHub. Software tools are essential for getting work done and sharing results. Nucleus Hub provides a way of accessing software tools that just work. No installs, no compiling, no environmental management. Of course if you want to modify your own environments and build code, that's supported as well. The Nucleus CDK lives on [GitHub](), but the Hub is preconfigured to get you up and running without any additional work. And there's templates. 

Documentation for Nucleus Hub can be found in Guides. Guides are the place to find tutorials that walk you through different aspects of the documentation. This page is an example of one such tutorial. We recommend exploring the Guides pages to get a sense for how the documentation is organized.

You will find a Guide for getting started with Nucleus Hub. Be sure to take a look at that page and familiarize yourself with the platform. 

- [Getting Started with Nucleus Hub](../guides/nucleus-hub/nucleus-hub.md)

Now that you are setup and familiar with Nucleus Hub, we can use the CDK tools to analyze data in Nucleus Hub. You will also find a guide for that as well:

- [Tutorial: analyzing platereader data with the CDK](../guides/platereader_tutorial.md)

After working through these tutorials, you'll have a Nucleus Hub account and some compelling visualizations. Consider documenting your work by writing a DevNote to share with the Nucleus community.

## Sharing your results as a Developer Note

Nucleus is open source which means that we're building something together. Developer Notes are the key way to contribute to the Nucleus Distribution. Developer Notes are conveniently built on top of Jupyter Notebooks and MyST Markdown (a flavor of markdown designed for technical communication). Since you've done your analysis in a Jupyter Notebook, you've already half-written your DevNote and you didn't even know it. 

- [Writing your first Developer Note](../guides/devnote-tutorial.md)

If you followed the steps on that page, you should have successfully posted a Developer Note. 

<!-- Not only does your data help us understand how good you are preparing base cytosols (and how well our reagents are performing), it helps expand the largest on-going interlab study on the expression of deGFP. It also introduces you to the Developer Community, in a uniquely Nucleus Way.  -->

## Engage with the community on the Nucleus Forum

Once a DevNote goes live, a thread is opened on the Forum for others to discuss. People might ask you how to replicate what you did, tell you that you made an incredible mistake, or just say "hi". These "Hello, World!" DevNotes go into a special channel and provide a place for people to introduce themselves.

- [Nucleus Forum](https://forum.bnext.bio/)


## What's next?

<!-- Well, not quite. To be a proper Nucleus Developer, you should probably have developed something. But don't fret, you're well on your way.  -->

You are now in command of a growing collection of validated Modules that you can build on top of and equipped with the tools to analyze and share them. If you develop something useful or on the Nucleus Roadmap, you should keep in mind the Nucleus Contribution Standards so that your work can be shared on the distribution. 

- [Nucleus Distribution Contribution Guide](/guides/contribution-guide.md)

We look forward to hearing from you!

<!-- Once it's in the Distribution, you can safely call yourself a Developer.  -->

<!-- Getting Started with Nucleus
This guide walks you through the complete Nucleus workflow: from preparing base cytosol to analyzing results and sharing them with the community. By the end, you'll understand how the pieces fit together and be ready to contribute your own work.
Prerequisites

Basic lab skills for molecular biology
Familiarity with Python and Jupyter notebooks (helpful but not required)
A willingness to share your work openly

What You'll Learn

How to prepare base cytosol using the kit
How to analyze your data on Nucleus Hub
How to document your work as a Developer Note
How to engage with the Nucleus community

Step 1: Prepare Base Cytosol
The Nucleus Distribution includes multiple approaches for preparing base cytosol. For this tutorial, we'll use the Base Cytosol Kit, which provides a standardized starting point.
Follow the protocol: Making Base Cytosol from Kit
Once complete, you should have:

Prepared cytosol samples
Fluorescence measurements or other assay data
Raw data files ready for analysis

Step 2: Analyze Your Data
Nucleus Hub is a JupyterHub-based platform that provides pre-configured analysis environments. No installation required—just log in and start working.
Why use Nucleus Hub?

Pre-installed tools and libraries
Reproducible computational environments
Analysis templates for common workflows
Direct integration with the Nucleus Distribution

Get started: Introduction to Nucleus Hub
After completing the tutorial, you'll have:

A Nucleus Hub account
Analysis notebooks with your results
Plots and summary statistics

Step 3: Share Your Results
Developer Notes (DevNotes) are how we document and share work in Nucleus. They're built on Jupyter notebooks and MyST Markdown, so if you've already done your analysis in a notebook, you're halfway done.
What makes a good DevNote?

Clear documentation of methods
Reproducible analysis code
Discussion of results and limitations
Links to relevant protocols and modules

Write your first DevNote: Developer Note Guide
Your DevNote contributes to the community in two ways:

It documents real-world performance of Nucleus modules
It adds to our growing dataset of cell-free expression experiments

Step 4: Join the Discussion
When your DevNote is published, a forum thread opens automatically for discussion. Community members may ask questions, suggest improvements, or build on your work.
Learn more: Forum Guidelines
Next Steps
You've now completed the core Nucleus workflow. You know how to prepare reagents, analyze data, and share results. To become a more active contributor:
Build New Modules
Use existing validated components to create new functionality. Document your work thoroughly and test across conditions.
Improve Existing Protocols
Found a way to improve yield or reduce cost? Document your modifications and share the results.
Review the Contribution Standards
Before submitting work to the Distribution, review our standards for documentation, validation, and licensing: Contribution Standards
Questions?

Check the FAQ
Search the Forum
Open an issue on GitHub

Welcome to Nucleus. We're building this together. -->