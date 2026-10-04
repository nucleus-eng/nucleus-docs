---
title: The type system
description: What a Component, a Module, a class and an Implementation are, how Modules compose, and the three levels at which a thing has an identity.
---

# Overview

Every page in this documentation describes one of a few kinds of thing. This page says what those kinds are and how they relate. It defines no material and no procedure. Read it when a page's shape is unclear, or before adding a page of a kind that does not exist yet.

# A Component and a Module

A **Component** is a thing that exists. It needs no purpose and no conditions. Agarose is a Component. So is a protein, a lipid and a buffer salt.

A **Module refines a Component.** It is a Component with a Function it performs and Requirements that must hold for that Function to be defined. The refinement adds the Function and the Requirements. It does not change the material.

That difference decides which pages exist:

- A Component with no stated Function gets no Module page. It is named where it is used.
- A Component that performs something, under conditions a reader must meet, gets a Module page.

One material can be both, at two levels. Catechol 2,3-dioxygenase is a protein, which is a Component. The XylE Reporter is a Module: the same protein with a Function, producing a visible color change, and a Requirement, that catechol is present and separated until the trigger.

**A composition of Modules is a Module.** A cytosol with a detector mixed into it is a Module. A cell made by closing that cytosol in a membrane is a Module. A cascade built from several cells is a Module. Composition does not produce a new kind of thing, which is why every one of those gets the same page shape.

# A class

A **class** is a Module that other Modules refine. It has no material of its own. It states the invariant its members share.

Color Change is a class. Its invariant is separation: an enzyme and its substrate held apart until a trigger. Every member holds them apart, so the invariant is stated once on the class rather than restated on each member.

A member states only what it adds. A sensitivity declared on a class is the member's sensitivity without being written again, and a member may narrow it but cannot silently widen it. This is why a class page carries conditions that look like they belong to its members: stating them once is the point.

# An Implementation

An **Implementation** is a set of Modules and Processes run together in one physical operating context, and what happened when it ran.

This is the one page kind where a report is the right genre. A Module page defines; an Implementation page records. A result belongs on an Implementation page. The claim that result supports belongs on the Module page.

# How Modules compose

Three operators build a Module from others. Which one applies follows from the process, and is not a choice made per step.

| Operator | Written | What it produces |
| --- | --- | --- |
| mixing | `⊞` | The operands end up in one compartment and share its resources |
| packing | `⊗` | Each operand keeps its own compartment |
| stitching | `::` | The operands join in order into one polymer |

**Mixing and packing differ by compartment, not by closeness.** A detector mixed into a cytosol shares that cytosol's energy and ribosomes. A cytosol packed inside a membrane does not share with what is outside it.

**Stitching is homogeneous.** Its operands and its product are the same kind of polymer: DNA stitched to DNA is DNA, and protein stitched to protein is protein. It joins in order, so the result depends on which operand comes first. It is realized by DNA assembly. A construct ordered as a single synthesized sequence is not assembled, so its page names the finished molecule as an input and declares no stitching step.

**Stitching makes new types.** A tag stitched to a protein gives a protein that a tag-specific enzyme can act on, where the untagged one is left alone. A regulatory element stitched to a coding sequence gives a construct that expresses only when that element allows it. In both cases the product is a different Module from either operand, not one of the operands in a different setting.

# Identity has three levels

A thing can be identified at three levels, and a page must be clear about which one it means.

| Level | Example | What it fixes |
| --- | --- | --- |
| Component | Agarose, by CAS number | The chemical identity |
| Grade | Low gelling against ultra low gelling | A property that changes what the thing can do |
| Part number | One supplier's catalog entry | The item that can be ordered |

**Two part numbers can share a Component and differ at the grade.** Those are not interchangeable, and a page that treats them as interchangeable states something false about the property the material was chosen for.

**Two part numbers can share everything but the quantity sold.** Those are the same part. A page names one, for the size usually ordered, and does not list the rest.

# A gene and its product are two objects

A gene and the protein it encodes are different things. They are related by expression, which is a step, not a kind. Neither refines the other, and no third kind sits above them: both are polymers, and that is all a shared parent could say about them.

What matters in practice is that holding one is not holding the other. DNA needs a cytosol able to read its promoter. The protein does not.

**So a Module named for a gene states three names together: the gene symbol, the name of the product, and the name of the construct that carries it.** Any one of the three then finds the other two. Without that, a reader searching for a gene symbol misses a construct filed under the enzyme's name, and may conclude a sequence is missing when it is present.

See [A shared identifier is a shared parent](../style-guide/principles.md) for the related rule on part numbers.
