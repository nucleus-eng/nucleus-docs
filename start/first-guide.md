---
title: "Beginner's Guide" 
subtitle: "From Zero to DevNote: a Beginner's Guide to the Nucleus Technology Stack"
---

# Overview

The purpose of this tutorial is to guide a newcomer through the complete Nucleus technology stack and supporting workflows. 

At the end of this tutorial you will have used the Protocols in the Distribution to assemble Base Cytosol, characterized its performance using the Cell Development Kit (CDK) on Nucleus Hub, and finally posted a Developer Note (DevNote) that reports on its performance. 

:::{figure} ./resources/flowchart.png
**The Nucleus Development Cycle.** All components of the Nucleus platform work together to support the collaborative development of increasingly reliable and sophisticated synthetic cells contained within the Distribution. The **Documentation** (this site) is a knowledge base that contains protocols and  documentation for implementing validated synthetic cell modules. The **Hub** provides a resource for data sharing, analysis using standard digital tools. Useful results can be shared with the community as **DevNotes**. DevNotes can be viewed on the **Developer Note** website. Periodically, contributions made as Devnotes are integrated into the Distribution as validated protocols for others to use and build upon. All components of the platform can be discussed at the **Forum**, come say hello!
:::

This tutorial assumes that you have the necessary components of Base Cytosol: small molecule mix, tRNA, protein mix, ribosomes, and a suitable reporter plasmid such as `pOpen-deGFP`. The components of Base Cytosol can be obtained in two ways: you can make them yourself from scratch, or you can acquire a premade reagent kit from b.next. 

If you are looking to get started quickly, we recommend acquiring a kit from b.next. If you prefer more control over the cytosolic system, the distribution contains materials, protocols, and documentation for making your own components from scratch. 

# Using the Distribution as a knowledge base

The Distribution contains numerous validated protocols and other documentation organized across four different categories: DNA Distribution, Processes, Modules, and Implementations. Assembling Base Cytosol is regarded as a fundamental process in the Distribution, so protocols and documentation for its assembly can be found in the [Processes](../docs/processes/processes-main.md) section. We recommend exploring the four Protocol category pages to get a sense for how the documentation is organized.

Now that we're more oriented in the documentation let's navigate to the protocol we'd like to implement:

- [Assemble Base Cytosol](../docs/processes/assemble-base-cytosol/main.md)

If you follow the steps on that page, you should find yourself with some data in hand ready to be analyzed. Rather than firing up Excel or opening a Google Sheet, we're going to sign into Nucleus Hub. 

<!-- TODO: talk about platemaps -->

<!-- In contrast, Modules extend the functionality of fundamental processes.  -->

## Analyzing Data with Nucleus Hub

:::{note} Prerequisite
:class: simple
:icon: false

This remainder tutorial assumes access to Nucleus Hub, which requires admin approval. Please reach out to build@bnext.bio.
:::

Nucleus Hub is an interactive computing platform built on JupyterHub. Software tools are essential for getting work done and sharing results. Nucleus Hub provides a way of accessing software tools that just work. No installs, no compiling, no environmental management. Of course, if you want to modify your own environments and build code, that's supported as well. The Nucleus CDK lives on [GitHub](https://github.com/bnext-bio/nucleus/tree/main/cdk), but the Hub is preconfigured to get you up and running without any additional work. And there's templates. 

Documentation for Nucleus Hub can be found in Guides. Guides is the place to find tutorials and how-tos that walk you through different aspects of the documentation. This page is an example of a tutorial. We recommend exploring the Guides pages to get a sense for how the documentation is organized.

You will find a Guide for getting started with Nucleus Hub. Be sure to take a look at that page and familiarize yourself with the platform. 

- [Getting Started with Nucleus Hub](../guides/nucleus-hub/nucleus-hub.md)

Now that you are setup and familiar with Nucleus Hub, we can use the CDK tools to analyze data in Nucleus Hub. You will also find a guide for that as well:

- [Tutorial: analyzing platereader data with the CDK](../guides/platereader_tutorial.md)

After working through these tutorials, you'll have a Nucleus Hub account and a visualization of your data. Consider documenting your work by writing a DevNote to share with the Nucleus community.

## Sharing your results as a Developer Note

Nucleus is open source which means that we're building something together. DevNotes are the key way to contribute to the Nucleus Distribution. DevNotes are conveniently built on top of Jupyter Notebooks and MyST Markdown (a flavor of markdown designed for technical communication). Since you've done your analysis in a Jupyter Notebook, you've already half-written your DevNote and you didn't even know it. 

- [Writing your first DevNote](../guides/devnote-tutorial.md)

If you followed the steps on that page, you should have successfully posted a DevNote. 

## Engage with the community on the Nucleus Forum

Once a DevNote goes live, a thread will be opened on the Forum for others to discuss. People might ask you how to replicate what you did, tell you that you made an incredible mistake, or just say "hi". These "Hello, World!" DevNotes go into a special channel and provide a place for people to introduce themselves.

- [Nucleus Forum](https://forum.nucleus.engineering/)


## What's next?

You are now in command of a growing collection of validated Modules that you can build on top of and equipped with the tools to analyze and share them. If you develop something useful or on the Nucleus Roadmap, you should keep in mind the Nucleus Contribution Standards so that your work can be shared on the distribution. 

- [Nucleus Distribution Contribution Guide](../guides/contribution-guide.md)

We look forward to hearing from you!