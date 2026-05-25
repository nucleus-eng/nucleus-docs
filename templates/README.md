# How Modules, Processes, and Implementations Fit Together

Nucleus documentation is organized around three types of content. Each serves a different purpose, but they build on each other.

## Module Specifications

A Module spec describes a single biochemical component: a reporter protein, a membrane pore, an energy system. It covers what the component is, what it's made of (sequences, constructs), and its known properties. The data in a spec is typically sourced from existing databases or literature: an excitation/emission spectrum, a pore diameter, a substrate affinity. This is reference data intrinsic to the component, not empirical results from a particular experiment.

## Processes

A Process wraps a lab protocol: the step-by-step instructions someone follows at the bench. Processes also include an overview, a materials list, performance data from executing the protocol, and links to relevant DevNotes. A Process is self-contained. It describes how to make or prepare something (grow bacteria, purify a protein, assemble cytosol) without assuming which system the output ends up in.

## Implementations

An Implementation inherits from a Process but pulls in specific Module specs. It documents what happens when you assemble particular modules following a particular protocol: which modules, which process, and how the resulting system performed. Performance data (expression levels, yields, dose-response curves) lives here because it depends on the specific combination of modules and conditions.

## How they build on each other

Module specs provide the component definitions. Processes provide the protocols. Implementations combine both: they take a Process and populate it with specific Modules, then report what happened. The inheritance runs Spec + Process → Implementation.

In practice:

- A Module spec links to Processes that can produce it and to DevNotes that characterize it.
- A Process links to prerequisite Processes and to Module specs for any genetically encoded components involved.
- An Implementation links to its Modules and to the Process it follows.

## Where data goes

If the data describes an intrinsic property of a component (something you'd find in a database), it goes in the Module spec. If the data comes from executing a protocol, it goes in the Process. If the data comes from running a specific combination of modules together, it goes in an Implementation.