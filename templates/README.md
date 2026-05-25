# How Modules, Processes, and Implementations Fit Together

Nucleus documentation is organized around three types of content that build on each other.

**Module specs** are abstract descriptions of a single biochemical component: a reporter protein, a membrane pore, an energy system. A spec covers what the component is, what it's made of (sequences, constructs), and its known properties. The data in a spec is typically sourced from databases or literature: an excitation/emission spectrum, a pore diameter, a substrate affinity. A spec does not include a protocol, a materials list, or performance data from a particular experimental context.

**Processes** wrap lab protocols: the step-by-step instructions someone follows at the bench. A Process also includes an overview, materials, QC data that characterize the final product (e.g., protein purity on a gel, ribosome concentration by absorbance), and links to relevant DevNotes. Processes are self-contained. They describe how to make or prepare something (grow bacteria, purify a protein, assemble cytosol) without assuming which modules or system the output ends up in.

**Implementations** inherit from Processes but pull in specific Module specs. An Implementation documents what happens when you put particular modules into a particular system following a particular protocol. Performance data (expression levels, yields, dose-response curves) lives here because it depends on the specific combination of modules and conditions. Implementations can also document interesting combinations of multiple modules.

The inheritance runs Module Spec + Process → Implementation. Module specs provide the component definitions. Processes provide the protocols and materials. Implementations combine both, then report what happened.

## Where data goes

If the data describes an intrinsic property of a component (something you'd find in a database), it goes in the Module spec. If the data characterizes the quality of a product made by a protocol (purity, concentration, integrity), it goes in the Process. If the data comes from running specific modules in a specific context, it goes in an Implementation.