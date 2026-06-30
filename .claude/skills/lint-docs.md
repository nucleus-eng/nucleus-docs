---
description: Commands and interpretation guide for Vale, codespell, and lychee — run these before opening a PR or committing content.
---

### Prose linting (Vale)

**Run `git ls-files docs/ | grep -E '\.(md|csv)$' | xargs vale` before opening a PR or committing a content migration.** This command lints only committed source files (skipping gitignored `generated/` artifacts). Vale lints both `.md` and `.csv` files and runs as part of the `qa` CI workflow (`.github/workflows/qa.yml`).

```bash
git ls-files docs/ | grep -E '\.(md|csv)$' | xargs vale          # lint all committed docs (skips generated/)
vale --glob='!**/generated/**' docs/                              # lint full docs/ tree, excluding generated/
vale <file.md>                                                     # lint a single file
```

Vale rules live in `styles/nucleus/`. Current rules enforce temperature unit formatting (`°C`), micro symbol usage (`µ`), chemical notation (subscripts and ion superscripts), and unit spacing. Executable tests for these rules live in `tests/` (pytest, not content — run `python -m pytest` from the repo root).

**Interpreting temperature-related errors.** Temperature formatting is enforced by two overlapping rules: `nucleus.units` flags spelled-out forms (`degC`, `degrees C`, `degrees Celsius`, `deg C`) via substitution; `nucleus.degrees-symbol` flags bare digit+C patterns (`95C`, `72 C`) via a raw regex. Both fire as `error` level. In practice, `nucleus.degrees-symbol` currently has a known detection gap — bare `\d+C` patterns are not reliably detected (tracked by `vale-miss` annotations in `styles/tests/temperature.md`). Rely on `nucleus.units` for spelled-out forms; flag bare patterns manually until the gap is fixed.

**Interpreting `nucleus.degrees-symbol` errors.** When Vale flags a `nucleus.degrees-symbol` error, check the surrounding context:

- **Real error** — the token is a temperature value. Fix it by adding the degree symbol (e.g., `37C` → `37 °C`, `4 C` → `4 °C`).
  - Signals: preceded by "at", "to", "of", or a verb like "incubate", "store", "heat"; followed by "for X minutes/hours"; in a reaction table or thermocycler step.
  - **Table cells**: a bare value (e.g., `37C`) in a table column whose header indicates temperature (e.g., "Temperature", "Incubation temp", "Storage") is always a real error, even without surrounding signal words.
- **False positive** — the token is a label, not a temperature. Leave it alone.
  - Signals: preceded by "Figure", "Fig.", "Step", "Lane", "Panel", "Tube", "Option", or a similar structural label word.

**Interpreting `nucleus.chemical-notation` errors.** This rule flags molecular formulae and wavelength labels written with bare ASCII digits and suggests the correct Unicode subscript form. Always a real error — replace `OD600` → `OD₆₀₀`, `A260` → `A₂₆₀`, `H2O` → `H₂O`, `ddH2O` → `ddH₂O`, `MgSO4` → `MgSO₄`, etc. The rule is a substitution rule — the error message shows the exact correct form to use. There are no known false positives (the rule uses an explicit curated list of formulae rather than a generic pattern, so construct names like `pET28a` and labels like `A19` are unaffected).

**Interpreting `nucleus.ion-charges` errors.** This rule flags ion charges written with inline numbers rather than Unicode superscripts. Always a real error — replace `Mg2+` → `Mg²⁺`, `Ni2+` → `Ni²⁺`, `Na+` → `Na⁺`, `K+` → `K⁺`, `Mg++` → `Mg²⁺`, etc. Superscript characters: ⁺ (U+207A), ² (U+00B2), ³ (U+00B3).

**Interpreting `nucleus.micro-symbol` errors.** This rule flags patterns like `10 uL`, `500 uM`, or `2 um` that use an ASCII `u` instead of the micro symbol `µ`. Always a real error — replace with `µL`, `µM`, or `µm` respectively.

**Vale `TokenIgnores` limitation on CSV files.** Vale's `TokenIgnores` setting (used to suppress URL matches) works for `.md` files but is silently ignored for `.csv` files. This means URL-encoded sequences like `%2C` in CSV cells can trigger rules even when URLs are listed in `TokenIgnores`. The workaround is to bake URL safety directly into the rule pattern (e.g., `(?<!%)\d+\s*C\b` instead of `\d+\s*C\b`).

**Applying fixes programmatically.** When using a script (e.g., perl/sed) to bulk-apply degrees-symbol fixes, always use a negative lookbehind for `%` to avoid corrupting URL-encoded sequences like `%2C` (comma):

```perl
# Safe — won't corrupt %2C, %3C, etc. in URLs
s/(?<!%)(\d+)C\b/$1°C/g

# Unsafe — will corrupt URL-encoded sequences
s/(\d+)C\b/$1°C/g
```

Do not add Vale inline suppression comments (`<!-- vale off -->`) without confirming with the developer first. When suppressing only a specific rule (e.g., to silence BOM product-name false positives), prefer rule-scoped suppression over a blanket `<!-- vale off -->`:

```html
<!-- vale nucleus.magnitude-unit-spacing = NO -->
:::{table} Bill of Materials
...
:::
<!-- vale nucleus.magnitude-unit-spacing = YES -->
```

Additionally, some rules (e.g., nucleus.range-styles) will require unit consistency which may require negative lookbehinds, capture groups, and semantic parsing in extreme cases (e.g., 50-2000 ng/mL -> 50 ng/mL to 2000 ng/mL, equivlant to 50 ng/mL to 2 ug/mL). Perl scripts will often generate errors that Vale does not catch (e.g., 50-2000 ng/mL -> 50 ng to 2000 ng/mL; inconsistent units). Before applying changes like these repo-wide, assess how complicated the search-and-replace job is and whether simple regex will suffice. After making such changes, cherry pick a few example substitutions and check for semantic correctness (e.g., consistent units).

**Canonical unit list.** Several Vale rules share an overlapping set of recognised units. Vale rule files are self-contained YAML and have no native include or variable mechanism, so the lists are duplicated by design — the rules differ slightly because false-positive risk varies by context. The canonical reference list (for human consistency checks, not machine enforcement) is:

| Domain | Units |
| --- | --- |
| Length | `nm`, `µm`, `mm`, `cm`, `km` |
| Volume | `nL`, `µL`, `mL`, `L` |
| Mass | `nL`, `µg`, `mg`, `g`, `kg` |
| Concentration | `nM`, `µM`, `mM`, `M` |
| Molecular weight | `Da`, `kDa` |
| Time | `s`, `min`, `h`, `d` (SI); `yr`, `mo` (non-SI, no SI symbol exists) |
| Centrifugation | `rcf`, `rpm` |
| Temperature | `°C` |

When adding a new unit to one rule, check whether the other rules (magnitude-unit-spacing, range-style, ousands-separator) should also be updated.

**Known NIST SP 811 divergences.** The following are deliberate departures from NIST SP 811, documented here so they read as decisions rather than oversights:

| NIST rule | NIST says | Our style | Rationale |
| --- | --- | --- | --- |
| §7.10.2 — percent | `25 %` (space before `%`) | `25%` | Universal convention; `25 %` reads as unusual to bench scientists |
| §7.10.3 — ppm/ppb/ppt | Not acceptable; use `µL/L` etc. | `ppm` permitted, as is `µL/L` etc.| Accessible shorthand; rarely appears in docs |
| Time abbreviations | `h`, `min`, `s`, `d` | `yr`, `mo` also used | Year and month have no SI symbol; `yr`/`mo` are the accepted non-SI forms |

### Spell checking (codespell)

**Run `codespell docs/` before opening a PR or committing content.** codespell catches real typos and enforces American English spelling.

```bash
codespell docs/          # check all docs
codespell <file.md>      # check a single file
```

Configuration lives in `.codespellrc` at the repo root. It uses the `en-GB_to_en-US` builtin dictionary, which flags British spellings as errors (`labelled` → `labeled`, `grey` → `gray`, `Acknowledgements` → `Acknowledgments`, `homogenous` → `homogeneous`). The `ignore-words = .codespell-ignore` option suppresses known false positives — add a **lowercased** word on its own line to suppress it (e.g., `ser` suppresses the amino acid abbreviation Ser which codespell misreads as a typo for "set").

codespell only flags words in its curated misspelling dictionary, so niche technical terms (`PURExpress`, `plamGFP`, `PURET7`) are not flagged.

### Link checking (lychee)

**Run `python3 scripts/check-links.py docs/` before opening a PR if you have added, edited, or removed any links or URLs.** This is slower than Vale and doesn't need to run on every commit — focus on PRs that touch links.

```bash
python3 scripts/check-links.py docs/       # check all docs
python3 scripts/check-links.py <file.md>   # check a single file
```

The script wraps `lychee` and filters known false positives before reporting. **What it catches:** dead internal links, 404 external links, empty URLs. **What it does not catch:** product catalog changes on vendor sites (e.g. Sigma-Aldrich discontinuing a part number) — those require manual review.

**Interpreting output.** The script will note how many HTTP/2 false positives were filtered from `sigmaaldrich.com` — these are valid URLs on a server that blocks automated crawlers at the protocol level and can be ignored. Any remaining errors are genuine and should be fixed before opening a PR.
