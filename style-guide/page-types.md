# Page types

Four content types. The distinction that matters is **definition versus report**.

| Type | Location | Genre | Definition or report? |
| --- | --- | --- | --- |
| Module | `docs/modules/<name>/spec.md` | Specification | Definition |
| Process | `docs/processes/<name>/main.md` | Specification of a procedure | Definition |
| Implementation | `docs/implementations/<name>/main.md` | Worked example | **Report** |
| Guide | `guides/` | Tutorial, reference, contribution | Varies |

`about/`, `start/`, `templates/`, `styles/` and `assets/` are the other allowed roots. They are site furniture, not content types.

## Modules

A Module is a component with specified Composition and Function, given certain Requirements. Compositions of Modules — chassis, sensing cells, cascades — are still Modules, and get a Module page.

## Processes

A Process is a step-by-step protocol. Method detail belongs here rather than in a spec.

**With exceptions.** Some facts serve both: "fluoresces at 488 nm emission" is part of the Process *and* part of the Expected Behavior. The test is not where the fact was measured, but which claim it supports. When a fact plausibly serves both, ask the editor rather than guessing.

## Implementations

An Implementation is a specific set of Modules and Processes integrated for one example, and what happened when it ran. DevStudio demos are the clearest case.

**This is the one page type where a report is the correct genre.** The rules against past-tense reporting and against hosting experimental narrative do not apply here — they exist to keep reports out of specifications, and this is where those reports belong.

## Guides

Not yet examined. `guides/` currently holds a contribution guide, a DevNote syntax reference, tutorials, and workshops — plausibly several genres rather than one. No rule in this style guide was derived from a guide page. Expect this section to grow.

## Where displaced content goes

When content is on the wrong page, the destination depends on what it is evidence for.

| Content | Destination |
| --- | --- |
| Evidence that a Module's Function holds | That Module's Expected Behavior |
| A result produced by several Modules together | The composed Module's page, or an Implementation |
| A specific demo run, with its conditions and outcome | The Implementation page |
| Step-by-step method | The Process page |
| A constraint on what the Module can compose with | Requirements |
| Status, provenance of internal sources, open questions | `tmp/`, not the repo |

A result does not belong on a constituent's page merely because the constituent was physically in the tube.
