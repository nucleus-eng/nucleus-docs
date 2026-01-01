---
title: Nucleus Documentation Style Guide
---

# Nucleus Documentation Style Guide

This guide establishes consistent formatting, structure, and naming conventions for all Nucleus documentation. Follow these standards to ensure clarity, professionalism, and maintainability across the platform.

---

## 1. YAML Front Matter

All Nucleus documentation pages must include YAML front matter with the following structure:

### Required Fields

```yaml
---
title: "Document Title"
---
```

### Optional Fields

```yaml
---
title: "Document Title"
subtitle: "Optional subtitle for context"
thumbnail: image.png
site:
    hide-toc: true
    numbered_references: false
---
```

### Guidelines

- **title**: Use title case, keep concise (5-7 words max)
- **subtitle**: Use for Module/Implementation Specifications to provide additional context
- **site.hide-toc**: Set to `true` for focused, single-purpose documents (Modules, Implementations)
- **site.numbered_references**: Set to `false` for consistency
- **thumbnail**: Optional image for visual reference; use for Modules/Implementations

---

## 2. Heading Hierarchy

Maintain a clear, consistent heading structure:

```markdown
# Main Title (H1)
Use only one per document; typically the opening section

## Major Sections (H2)
Overview, Protocol, Downloads, etc.

### Subsections (H3)
Steps, detailed categories, specific procedures

#### Details (H4)
Only when necessary for deeply nested content
```

### Guidelines

- Start with `# Overview` or `# Main Section` (never duplicate titles)
- Use `## Protocol`, `## Implementations`, `## Downloads` for major divisions
- Avoid more than 3 levels of nesting
- Use clear, descriptive headings (not "Step 1", use "Prepare Stock Buffers")

---

## 3. Admonition Styling

Nucleus uses MyST admonitions with a consistent styling approach.

### Standard Configuration

All admonitions should include:
```markdown
:::{type} Title
:icon: false
:class: dropdown
```

### Admonition Types & Colors

| Type | Color | Use Case | Example |
| --- | --- | --- | --- |
| `{note}` | Blue | General information, context | Notes, References |
| `{tip}` | Green | Helpful supplementary info | Composition, Tips |
| `{seealso}` | Green | Related documentation | Prerequisite Documentation |
| `{hint}` | Green | Practical guidance | Procedural hints |
| `{attention}` | Orange | Requires user attention | Critical Materials, Genetically Encoded Components |
| `{danger}` | Red | Safety critical | Hazardous Materials |
| `{warning}` | Orange | General caution | Site-wide warnings |

### Guidelines

- **Always use** `:icon: false` (cleaner aesthetic)
- **Use** `:class: dropdown` for optional/supplementary information
- **Use** `:class: simple` only for inline notices (not collapsible)
- Place safety-critical admonitions early in documents
- Color coding should be semantically consistent (orange = attention, red = danger)

### Examples

**Simple inline notice:**
```markdown
:::{note} Prerequisite
:class: simple
:icon: false

This requires admin approval.
:::
```

**Collapsible section:**
```markdown
:::{attention} Critical Materials
:icon: false
:class: dropdown

[Content here]
:::
```

---

## 4. Document Structures

### Module Specification Structure

```markdown
---
title: "Module Specification"
subtitle: "[Type]: [Name]"
site:
    hide-toc: true
    numbered_references: false
---

## Overview
[Brief description of module function]

:::{attention}

This Module has not been validated in Nucleus Cytosol $\ge$ v0.5. 
Documentation can be found on the legacy site [here](link).

:::
```

**Subtitle format:** `[Category]: [Component Name]`
- Examples: "Reporter: deGFP", "Detector: tetR-aTc", "Energy: PPK"

**Validation notice:** Use for modules not yet validated; link to legacy documentation.

### Process Document Structure

```markdown
---
title: "Process"
subtitle: "[Action]: [Component]"
---

## Overview
[Context and purpose]

::::::{card}
:header: **Important Information**

[Nested card with 7 standard dropdowns]
- Notes
- Composition
- Prerequisite Documentation
- Critical Materials
- Genetically Encoded Components
- Hazardous Materials
- References
::::::

# Protocol

## [First Major Section]
[Detailed steps with checklists]

# Downloads

:::::{card}
:header: **Resources**
[Download buttons for lab-ready protocol, worksheets, BOM]
:::::
```

**Key elements:**
- "Important Information" card is mandatory
- All 7 dropdown sections should be present (use "None" if not applicable)
- Use checklists (`- [ ]`) for procedural steps
- Group downloads at the end in a "Resources" card

### Implementation Document Structure

```markdown
---
title: "Implementation"
subtitle: "[Type]: [Description]"
site:
    hide-toc: true
---

## Overview
[Brief description combining modules]

:::{attention}

This Instance has not been validated in Nucleus Cytosol $\ge$ v0.5. 
Documentation can be found on the legacy site [here](link).

:::
```

---

## 5. Important Information Card Structure

The "Important Information" card is a standardized structure used in Process documents.

### Template

```markdown
::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, 
and safety information. Not all information included here is included in the 
lab-ready protocol.

:::{note} Notes
:icon: false
:class: dropdown

- [Bullet points with important information]

:::

:::::{tip} Composition
:icon: false
:class: dropdown

::::{card}
:header: **[Composition Title]**
:::{table} 
:label: tbl:[unique-label]

[Table content]
:::
::::
:::::

:::{seealso} Prerequisite Documentation
:icon: false
:class: dropdown

- [Links to prerequisite documents]

:::

::::{attention} Critical Materials
:icon: false
:class: dropdown

:::{table}
:label: tbl:[unique-label]

[Materials table]
::::

::::{attention} Genetically Encoded Components
:icon: false
:class: dropdown

:::{table}
:label: tbl:[unique-label]

[Components table]
::::

::::{danger} Hazardous Materials
:class: dropdown
:icon: false

- [Hazardous materials list]

::::

::::{note} References
:class: dropdown
:icon: false

- [Reference citations]

::::

::::::
```

### Key Rules

- **7 standard sections** in order: Notes → Composition → Prerequisites → Critical Materials → Genetically Encoded Components → Hazardous Materials → References
- **Unique table labels**: Use descriptive labels like `:label: tbl:critical-materials` and `:label: tbl:genetically-encoded-components` (never duplicate)
- **All 7 sections required**: Use "None" or empty lists if not applicable
- **Dropdown order matters**: Follow the sequence above for consistency

---

## 6. Tables

### Table Labels

All tables must have unique labels:

```markdown
:::{table}
:label: tbl:[descriptive-name]

| Column 1 | Column 2 |
| --- | --- |
| Data | Data |
:::
```

**Label naming convention:**
- Format: `tbl:[descriptive-name]` (lowercase, hyphens for spaces)
- Examples: `tbl:critical-materials`, `tbl:genetically-encoded-components`, `tbl:reaction-setup`
- **Never reuse labels** across a single document

### Table Content Guidelines

- Use bold headers: `| **Header** | **Header** |`
- Center align option-heavy tables: `:align: center`
- Include units in headers for numerical data
- Use LaTeX notation for units ($\mu$L, etc.)

---

## 7. Typography & Formatting

### Code/Component Names

Use backticks for:
- Plasmid names: `pOpen-deGFP`, `pT7-plamGFP`
- Protein names: `ClpXP`, `deGFP`
- Genetic sequences or files: `pT7-tetO-plamGFP`

```markdown
The `pOpen-deGFP` plasmid encodes...
```

### Mathematical & Scientific Notation

Use LaTeX for:
- Subscripts/superscripts: $\mu$L, $v \ge 0.5$
- Greek letters: $\alpha$-hemolysin
- Inequalities: $<$, $\le$, $\ge$, $>$

```markdown
Molecules < ~1000 kDa
Nucleus $v \ge$ v0.5
$\alpha$-hemolysin membrane pore
```

### Emphasis

- **Bold** for emphasis on important terms or headers: `**Critical Materials**`
- *Italic* for publication titles or non-English terms: *et al.*, *Nucleus Developer Notes*
- `Code` for technical terms and file names

### Lists

**Use bullet points** for unordered information:
```markdown
- First item
- Second item
- Third item
```

**Use numbered lists** only for sequential steps:
```markdown
1. First step
2. Second step
3. Third step
```

**Use checklists** for procedures:
```markdown
- [ ] Task 1
  - [ ] Subtask 1a
  - [ ] Subtask 1b
- [ ] Task 2
```

---

## 8. Links & Cross-References

### Internal Links

Use relative paths for internal documentation:

```markdown
[Link text](../path/to/document.md)
[Assemble Base Cytosol](../docs/processes/assemble-base-cytosol/main.md)
```

**Guidelines:**
- Use `../` for navigation between sections
- Always include `.md` extension
- Keep link text descriptive (not "click here")

### External Links

Include full URL with https:

```markdown
[Link text](https://example.com)
[GitHub Repository](https://github.com/bnext-bio/nucleus)
```

### Cross-References (MyST)

For internal references within the documentation system:

```markdown
[Reference text](xref:unique-label#target)
:::{figure} image.png
:label: fig:unique-name
:::
```

---

## 9. Figures & Media

### Figure Directive

```markdown
:::{figure} ./resources/image.png
:width: 50%
:align: center
:label: fig:descriptive-name

Caption describing the figure.
:::
```

**Guidelines:**
- Always include descriptive captions
- Use `:width:` to control sizing (common: 40%, 50%)
- Use `:align: center` for centered figures
- Use `:label:` for cross-referencing (format: `fig:descriptive-name`)
- Store images in `./resources/` directory

---

## 10. Common Patterns

### Warning/Under Development Banner

For pages still in development:

```markdown
:::{warning}
:class: simple

This page is still under heavy development and things may be incomplete, 
contain errors, or otherwise not work as expected.
:::
```

### Validation Status Notice

For modules/implementations not yet validated:

```markdown
:::{attention}

This [Module/Instance] has not been validated in Nucleus Cytosol $\ge$ v0.5. 
Documentation can be found on the legacy site [here](link).

:::
```

### Resources/Downloads Card

```markdown
:::::{card}
:header: **Resources**
::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**
:align: center

{button}`download <protocol-file.pdf>`
:::

:::{card}
:header: **Bill of Materials**
:align: center

{button}`download <bom-file.pdf>`
:::

::::
:::::
```

---

## 11. Common Mistakes to Avoid

| Mistake | Correct | Example |
| --- | --- | --- |
| Duplicate table labels | Use unique labels | `:label: tbl:genetically-encoded-components` |
| "imformation" in comments | "information" | `<!-- Important information here -->` |
| Inconsistent relative paths | Use `../` consistently | `(../docs/modules/spec.md)` |
| Icons in admonitions | Always use `:icon: false` | `:::{note}\n:icon: false` |
| Missing `{class: dropdown}` | Include on supplementary sections | `:::{tip}\n:class: dropdown` |
| Mixed backtick usage | Consistent for code/components | Always use backticks for plasmids |
| Absolute paths in links | Use relative paths | `(../path/to/doc.md)` not `(/docs/path)` |

---

## 12. Quick Reference Checklist

### Before Publishing Any Document

- [ ] YAML front matter is complete and correct
- [ ] All headings use proper hierarchy (H1 > H2 > H3)
- [ ] All admonitions use `:icon: false` and `:class: dropdown` (where applicable)
- [ ] All table labels are unique within the document
- [ ] All internal links use relative paths with `../`
- [ ] Plasmid names use backticks: `pOpen-deGFP`
- [ ] Units use LaTeX: $\mu$L, $\ge$, etc.
- [ ] No typos in comments ("information" not "imformation")
- [ ] Process docs include all 7 "Important Information" sections
- [ ] Module/Implementation docs include validation status notice
- [ ] Figures have captions and descriptive labels
- [ ] Grammar is correct and tone is professional
- [ ] All buttons/downloads have correct filenames

---

## 13. Questions or Additions?

This style guide is a living document. As patterns evolve or new needs arise, this guide should be updated to reflect best practices across Nucleus documentation.

For questions or suggestions, reach out to the documentation team at build@bnext.bio.
