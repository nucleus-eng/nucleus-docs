---
title: FAQs
---

### What problem is Nucleus trying to solve?

The synthetic cell field has a simple problem: how does the field build synthetic cells together? More specifically, how do we reduce the time for Technology A developed in one lab to work together with Technology B developed in another lab, or make it possible at all. This matters because no single lab or company has the full range of expertise needed to build a working synthetic cell — progress depends on being able to combine work done in different labs, rather than each one reinventing the same components alone. Nucleus contains the tools, designs, specifications, methods, and materials required to do integrative synthetic cell engineering. 

### Where does Nucleus live?

Nucleus tools, designs, specifications, methods, and DevNotes all live on the [Nucleus Homepage](https://docs.nucleus.engineering) website. Content is contributed by b.next and the wider synthetic cell community. All source code for the site and content is available in the [nucleus-eng GitHub organization](https://github.com/nucleus-eng). Plasmids are available upon request to b.next and Addgene (beginning September, 2026). Nucleus is currently sponsored by b.next, which supports the infrastructure, staff, and materials that keep the platform running.

### Why is Nucleus open source?

We believe that building sophisticated, useful synthetic cells requires integrating capabilities that live beyond any single institution — no one lab or company has all the expertise needed. We want to encourage many approaches to innovation in this space, including proprietary ones. But biotech today defaults to proprietary: open approaches are often dismissed or unfamiliar to those developing and managing technology. We believe that if the field defaults to closed approaches, it will be difficult to realize its full potential. Open source provides the ethos and licensing framework to help correct that default.

### What is open source?

Open source describes content — of any kind, not just software — that is documented and made publicly available in enough detail to be reproduced, and released under a license that grants terms allowing others to use, modify, reuse, and build on it, rather than restricting that activity. At Nucleus, that includes designs, protocols, specifications, datasets, and documentation, alongside code; each is released under a license appropriate to its type (see our [License page](./license.md)). Open source is sometimes assumed to mean unsupported or informal — a hobbyist effort without real backing. That's not the case here. Nucleus is actively stewarded by a dedicated core development team at b.next, with defined processes for review, release, and quality control, a role we expect to evolve as the community matures (see ["Who decides what content lives on Nucleus?"](#who-decides-what-content-lives-on-nucleus)). Being open source is a licensing and access model, not a statement about how seriously a project is maintained. Open source is necessary to realize the kind of networked engineering this field needs — see ["Why is Nucleus open source?"](#why-is-nucleus-open-source) for more.

### How do I get started with Nucleus?

Most people will contribute to Nucleus by submitting a Developer Note (DevNote), a way to share ideas, specifications, processes, and results with the developer community. This can ultimately result in changes to Nucleus Docs including the introduction of new modules. Nucleus Docs and technical tools are maintained in several repositories across GitHub. We use GitHub’s pull request system to support review and acceptance of changes to these systems. For more information see our Get Started guide. 

### What license applies to my DevNote?

A DevNote’s license depends on what it contains, not on the fact that it’s a DevNote. Narrative text, figures, and characterization data are released under CC-BY-4.0. Protocols, module/cell designs, or sequence maps included in the same DevNote are released under CERN-OHL-P-2.0, provided the underlying IP can be cleared for that license (see ["What if my contribution is patented?"](#what-if-my-contribution-is-patented) for options when it can’t be). A single DevNote can therefore carry both licenses simultaneously, applying to the corresponding parts of its content. All of these licenses are what are known as permissive: you are free to use the tools, designs, specifications, methods conveyed in the DevNote as long as you acknowledge the project when you do.

### Who decides what content lives on Nucleus?

Anyone can contribute to Nucleus today — submitting a DevNote or opening a pull request doesn't require any special status. Currently, the core development team at b.next serves as the primary maintainer of Nucleus, responsible for merging and approving DevNote releases, submitting pull requests against Nucleus repositories, making key architectural decisions, and identifying enabling partnerships to support the community. The core team works closely with the broader community and takes their feedback seriously in shaping these decisions. As Nucleus matures and its architecture and practices stabilize, the goal is to open up decision-making and governance to a dedicated community of cell builders outside of b.next — including inviting others to take on maintainer roles themselves. To learn more about how b.next and Nucleus relate, read here.

### How do I contact the core development team?

For general comments or if you'd like to be a contributor, please send an email to [build@bnext.bio](mailto:build@bnext.bio). For general discussion with the Nucleus community, please check out the [Nucleus Forum](https://forum.nucleus.engineering/). For specific technical comments, suggestions, or bug-fixes please leave an issue on the relevant Nucleus repository.  

### Who owns contributions on Nucleus?

Contributions to Nucleus aren’t owned by any single entity; each contribution is owned by the contributing individual or organization. By contributing to Nucleus you agree to give users of the project a license to use and modify your contribution for any purpose, even commercial.

### What if my contribution is patented?

Nucleus uses the CERN Open Hardware License to handle patented subject matter. If you are the rights holder, or your institution grants permission, we can make your contribution accessible under CERN-OHL-P-2.0 — a license that allows others to practice the claims of the patent that would necessarily be infringed by implementing your contribution. This patent license is narrowly scoped, covering only what's needed to use the contribution as intended.

If clearance can't be obtained — for example, if your institution won't grant even this narrow license — nobody can practice your contribution without risking infringement. We can still publish your DevNote under CC-BY-4.0 as a citable record of the work, but the design or protocol itself won't be released under CERN-OHL-P-2.0, and it won't be integrated into the core Nucleus Docs until clearance is resolved. We discourage this path where possible.

### What if I want to patent something built using Nucleus?

The Nucleus licensing scheme does not require you to open source or license back modifications or improvements you build on top of Nucleus. As such, downstream patenting of modified or improved Nucleus content is not blocked. We want Nucleus to encourage sustainable innovation broadly; this may include patenting. It's best to consult legal counsel when considering patenting strategies.

### How does Nucleus handle physical materials?

Nucleus is scoped to handle plasmids. Currently, b.next may receive digital designs of plasmids and synthesize them such that they can be redistributed to the Nucleus community under the terms of the OpenMTA. We expect distribution of these plasmids to be mediated by Addgene beginning in September, 2026.

### What does the OpenMTA allow me to do?

The OpenMTA governs transfer and use of the physical material itself, including for commercial purposes, but does not include any license — separate rights may need to be obtained for any use. For plasmids distributed through Nucleus, this isn't the whole picture: the underlying design is separately released under CERN-OHL-P-2.0, which does grant a license to practice it where necessary. The OpenMTA and CERN-OHL-P-2.0 work together: the OpenMTA covers the physical transfer of the material, while CERN-OHL-P-2.0 covers the rights to use the design it embodies.

---

### How does b.next currently support Nucleus?

Since launching Nucleus in 2023, b.next has driven its core development: technical contributions, community support, and the infrastructure that makes both possible.

- **Technical content.** We make ongoing contributions of plasmids, methods, and reference specifications, including the full set that defines Nucleus Cytosol, as well as the protocols for liposome encapsulation. We regularly document our own work for reuse as Nucleus content and help others who want to build alongside us.
- **Community building.** We work as the dedicated team to help ensure that the community can build synthetic cells together. This means we respond to questions about protocol details and will hop on a call if the Cytosol protocol is not working. We also organize Developer workshops to bring the community together to share engineering best practices and increasingly help each other out.
- **Core infrastructure.** We maintain and develop the underlying technical infrastructure that makes Nucleus possible. This includes technical partnerships to sustain the infrastructure that runs [Developer Notes](https://devnotes.nucleus.engineering) and the legal work to ensure that Nucleus and its community have freedom to operate as a permissively licensed project (learn more about Nucleus [licensing](./license.md)).

### How does b.next benefit from Nucleus?

Our core thesis for investing in and contributing to Nucleus is that the sooner people can build cells, the sooner b.next (and others) can develop cells to solve problems. Short term, we benefit by building products like b.next Cytosol and services like contract R&D on top of Nucleus. Long term, b.next will benefit by using foundational technology developed on Nucleus to build valuable applications. Just as important, we'll need to develop capabilities to operate at speed and scale, and to make those applications robust enough for real-world deployment, capabilities we expect other organizations building on Nucleus will need to develop too. Growing this alongside Nucleus is core to how we plan to turn the open foundation into deployed, real-world impact. We benefit from working closely with today's synthetic cell pioneers, and we want that group to grow. The synthetic cell specifications, methods, and protocols on Nucleus will remain permissively licensed so that anyone can use and modify them for any purpose, even commercial.

### How does b.next intend to make money?

We see Nucleus as core technology for synthetic cells. By creating this technological foundation, we believe we'll be able to pursue application development, and so can anyone else. We believe there's more opportunity here than any one organization, b.next included, could realize alone. The specifications, protocols, and reference designs are open, and b.next builds commercial work on top of that open platform rather than by restricting it. Per our contribution rubric, what's broadly enabling for others (e.g. specifications, protocols, plasmids) goes back into Nucleus; what's specific to deploying a particular application is what we build our business on. Short term, that means supporting researchers working to make synthetic cell technology reliable and reproducible, through products like Cytosol and services like contract R&D. Long term, as that groundwork matures, we want to build applications ourselves and enable others to do the same. We also reserve the right to pursue work that isn't related to Nucleus at all.

### What is b.next’s long term vision for Nucleus?

Our long term vision for Nucleus is that it becomes the platform synthetic cell researchers reach for by default: the specifications, protocols, and tools that let people build without reinventing the basics. This means that Nucleus should always strive to meet the needs of its user community and grow in whatever direction best addresses those needs while remaining sustainable. We recognize this might require Nucleus to become its own independent organization, governed by the community it serves, or it might take some other form. What matters is that the structure serves the community building on it, not b.next alone. In all scenarios, we see ourselves as a core user and contributor to Nucleus, since enabling the synthetic cell community is core to our mission.

### What is b.next currently doing to realize its long term vision for Nucleus?

Currently, b.next’s core team decides which contributions appear on Nucleus sites and enter its repositories, and sets the specifications and quality bar content has to meet. While Nucleus is still in its infancy, we believe it is important for b.next to retain this role. However, we know that our long term vision requires us to create a shared governance with the community. We collaborate with an increasing number of labs; those interactions inform our thinking about Nucleus. In parallel, we worked with an independent third party, [Conscience](https://bnext.bio/conscience), to survey how the community sees itself engaging with Nucleus. We are using this feedback to define a set of criteria and a timeline for opening up greater governance to the community. 

### How does b.next decide what to contribute to Nucleus?

Our rubric is simple: if something is broadly enabling for others building alongside us, it belongs on Nucleus. Capabilities that are more specific to deploying a particular application such as the speed, scale, and hardened engineering needed to bring a product to market, for instance, are more likely to stay with b.next.

### How is Nucleus sustainable?

Nucleus doesn't depend on any single source of support. Today, Nucleus's early promise has attracted financial support that has gone directly back into developing Nucleus itself, including support from Schmidt Sciences (which funds the DevCells program, supporting multiple labs building together on Nucleus to expand its collection of reusable content and modules), the Astera Institute, and the Sloan Foundation. As more labs build on and contribute to Nucleus, we expect that base of support to broaden further, reducing reliance on any one funder or organization, including b.next. Right now, that support is largely grant-funded, which isn't a permanent model on its own — but the number of institutions and funders willing to back this work has grown steadily, and we expect that momentum to continue as the field matures.