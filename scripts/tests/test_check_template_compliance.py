"""Tests for scripts/check-template-compliance.py — page shape against template.

The planted fixture is PLANTED below, and it is the point of the file. The
corpus number this check replaces was swept by hand, and a hand sweep that
finds nothing and a checker that cannot report anything look identical from
the outside. PLANTED is a page carrying one of each failure the script claims
to catch; `test_the_planted_fixture_fails` asserts a non-zero exit on it and
`test_a_clean_corpus_passes` asserts zero on a corpus built to the templates.
Together they are the evidence that a clean run on docs/ means something.

Two things here are easy to get wrong and are locked down on purpose:

  * A page whose top-level sections are `##` must still have its sections
    read. Reporting only "these are H2" and stopping would hide every other
    finding on the page behind one cosmetic line — which is the shape of the
    bug that let docs/implementations/emitter-ivhsl/main.md read as clean.
  * A `#` inside a fenced code block, a `:::{directive}` or an HTML comment is
    not a heading. The templates are full of all three, so a parser that
    counted them would invent sections and then complain about their order.

Every test runs against a corpus written into tmp_path. Nothing reads docs/.
"""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "check-template-compliance.py"


def _load_module():
    # The script is hyphenated, so it cannot be imported by name.
    spec = importlib.util.spec_from_file_location("check_template_compliance", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ctc = _load_module()


# --- fixture builders -------------------------------------------------------


def page(title: str, sections: list[str], level: int = 1) -> str:
    """A page with frontmatter and one body paragraph under each section."""
    marker = "#" * level
    body = "\n\n".join(f"{marker} {s}\n\nBody text for {s}." for s in sections)
    return f'---\ntitle: "{title}"\n---\n\n{body}\n'


FORMULATION = ["Overview", "Reference Composition", "Expected Behavior", "Credits"]
FUNCTIONAL = ["Overview", "Reference Composition", "Requirements", "Credits"]
PROCESS = ["Overview", "Materials and Equipment", "Protocol", "Credits", "Downloads"]
IMPLEMENTATION = ["Overview", "Modules", "Processes", "Credits"]


# The planted failing fixture. One page, four failures, one of each kind:
#   LEVEL   — its sections are H2 where the template puts H1.
#   ORPHAN  — `Acknowledgments` is in no template and on no allowlist.
#   SHAPE   — Credits sits above Reference Composition.
#   MISSING — there is no Overview.
# It also carries a `#` inside a code fence and inside a directive, so a
# parser regression shows up here as invented sections rather than silently.
PLANTED = """---
title: "Reporter: Planted"
---

## Credits

Developed by nobody.

## Reference Composition

```bash
# this is a shell comment, not a section
```

:::{note}
# nor is this
:::

<!--
# nor is this
-->

## Acknowledgments

Thanks to nobody.
"""


def corpus(tmp_path: Path, files: dict[str, str]) -> Path:
    docs = tmp_path / "docs"
    for name in ("modules", "processes", "implementations"):
        (docs / name).mkdir(parents=True, exist_ok=True)
    for rel, text in files.items():
        path = docs / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return docs


def findings(tmp_path: Path, files: dict[str, str]) -> list[str]:
    found, _notes, _checked = ctc.run(corpus(tmp_path, files))
    return found


def notes(tmp_path: Path, files: dict[str, str]) -> list[str]:
    _found, notes_, _checked = ctc.run(corpus(tmp_path, files))
    return notes_


def matching(found: list[str], needle: str) -> list[str]:
    return [f for f in found if needle in f]


# --- scope item 1: shape against the page's own template --------------------


def test_a_page_in_template_order_is_clean(tmp_path):
    assert findings(
        tmp_path,
        {
            "modules/base-membrane/spec.md": page("Base Membrane: POPC", FORMULATION),
            "processes/make-trna/main.md": page("Make tRNA", PROCESS),
            "implementations/atc-demo/main.md": page("aTc Demo", IMPLEMENTATION),
        },
    ) == []


def test_a_section_out_of_template_order_is_a_finding(tmp_path):
    found = findings(
        tmp_path,
        {
            "modules/base-membrane/spec.md": page(
                "Base Membrane: POPC",
                ["Overview", "Credits", "Reference Composition"],
            )
        },
    )
    assert matching(found, "'Reference Composition' comes after 'Credits'")
    assert len(found) == 1


def test_the_genre_comes_from_the_title_and_directory(tmp_path):
    """A pore is functional even though it is named after a membrane."""
    pore = tmp_path / "docs/modules/membrane-pore-ahly/spec.md"
    membrane = tmp_path / "docs/modules/membrane-popc-chol/spec.md"
    corpus(
        tmp_path,
        {
            "modules/membrane-pore-ahly/spec.md": page("Membrane Pore: aHly", FUNCTIONAL),
            "modules/membrane-popc-chol/spec.md": page("Base Membrane: POPC", FORMULATION),
        },
    )
    assert ctc.module_template(pore, pore.read_text()) is ctc.MODULE_FUNCTIONAL
    assert ctc.module_template(membrane, membrane.read_text()) is ctc.MODULE_FORMULATION


def test_an_unclassifiable_module_is_checked_against_the_union_and_said_so(tmp_path):
    files = {"modules/ulga/spec.md": page("ULGA", FORMULATION)}
    assert findings(tmp_path, files) == []
    assert matching(notes(tmp_path, files), "genre not inferable")


def test_a_module_section_on_an_implementation_page_is_a_finding(tmp_path):
    """The page's own template is the authority, not the Module one."""
    found = findings(
        tmp_path,
        {
            "implementations/atc-demo/main.md": page(
                "aTc Demo", ["Overview", "Reference Composition", "Credits"]
            )
        },
    )
    assert matching(found, "orphan section 'Reference Composition'")
    assert matching(found, "implementation-template.md")


# --- scope item 2: heading level, not only sequence -------------------------


def test_a_page_written_entirely_at_h2_is_reported(tmp_path):
    found = findings(
        tmp_path,
        {"implementations/emitter/main.md": page("Emitter Cell", ["Overview"], level=2)},
    )
    assert matching(found, "top-level sections are H2")


def test_an_h2_page_still_has_its_sections_read(tmp_path):
    """The failure item 2 exists to prevent: one cosmetic line, nothing else.

    A checker that counts H1s sees no sections here and reports the page
    clean. A checker that stops at the level finding hides the rest. Both the
    orphan and the missing section must survive the demotion.
    """
    found = findings(
        tmp_path,
        {
            "modules/reporter-degfp/spec.md": page(
                "Reporter: deGFP",
                ["Reference Composition", "Acknowledgments"],
                level=2,
            )
        },
    )
    assert matching(found, "top-level sections are H2")
    assert matching(found, "orphan section 'Acknowledgments'")
    assert matching(found, "missing required section 'Overview'")
    assert matching(found, "missing required section 'Credits'")


def test_a_template_section_sitting_too_deep_is_reported(tmp_path):
    found = findings(
        tmp_path,
        {
            "processes/make-trna/main.md": (
                page("Make tRNA", ["Overview", "Protocol", "Credits", "Downloads"])
                + "\n## Quality Control\n\nRun a gel.\n"
            )
        },
    )
    assert matching(found, "'Quality Control' is a top-level section")
    assert matching(found, "sits at H2")


def test_the_wrong_level_is_found_whatever_the_casing(tmp_path):
    """`## Quality control` and `## Quality Control` are the same mistake."""
    found = findings(
        tmp_path,
        {
            "processes/make-trna/main.md": (
                page("Make tRNA", ["Overview", "Protocol", "Credits", "Downloads"])
                + "\n## Quality control\n\nRun a gel.\n"
            )
        },
    )
    assert matching(found, "'Quality control' is a top-level section")


def test_a_page_with_no_headings_is_reported(tmp_path):
    found = findings(
        tmp_path, {"modules/base-cell/spec.md": '---\ntitle: "Base Cell"\n---\n\nText.\n'}
    )
    assert matching(found, "no headings")


# --- scope item 3: orphan headings against a declared allowlist -------------


def test_materials_and_downloads_are_allowed_where_the_template_omits_them(tmp_path):
    """Both are legitimate optional sections; the formulation template has
    neither Downloads nor a page-level reason to forbid Materials."""
    assert findings(
        tmp_path,
        {
            "modules/base-membrane/spec.md": page(
                "Base Membrane: POPC",
                [
                    "Overview",
                    "Reference Composition",
                    "Materials",
                    "Downloads",
                    "Credits",
                ],
            )
        },
    ) == []


def test_the_allowlist_holds_exactly_the_two_ruled_entries(tmp_path):
    assert ctc.ALLOWED_EXTRA == frozenset({"Materials", "Downloads"})


def test_an_undocumented_heading_is_a_finding(tmp_path):
    found = findings(
        tmp_path,
        {
            "processes/grow-bacteria/main.md": page(
                "Grow Bacteria",
                ["Overview", "Protocol", "Credits", "Acknowledgments"],
            )
        },
    )
    assert matching(found, "orphan section 'Acknowledgments'")
    assert matching(found, "ALLOWED_EXTRA")


def test_sub_headings_are_not_orphans(tmp_path):
    """Protocol steps and Expected Behavior contexts are free text."""
    assert findings(
        tmp_path,
        {
            "modules/reporter-degfp/spec.md": (
                page("Reporter: deGFP", ["Overview", "Expected Behavior"])
                + "\n## Cytosols\n\nText.\n\n## Cells\n\nText.\n\n# Credits\n\nText.\n"
            )
        },
    ) == []


# --- scope item 4: required sections present --------------------------------


def test_a_module_page_requires_overview_and_credits(tmp_path):
    found = findings(
        tmp_path,
        {"modules/reporter-degfp/spec.md": page("Reporter: deGFP", ["Requirements"])},
    )
    assert matching(found, "missing required section 'Overview'")
    assert matching(found, "missing required section 'Credits'")


def test_a_process_page_requires_credits(tmp_path):
    found = findings(
        tmp_path,
        {
            "processes/make-trna/main.md": page(
                "Make tRNA", ["Overview", "Protocol", "Downloads"]
            )
        },
    )
    assert matching(found, "missing required section 'Credits'")
    assert not matching(found, "missing required section 'Quality Control'")


def test_the_missing_section_message_says_where_to_put_it(tmp_path):
    found = findings(
        tmp_path,
        {"modules/reporter-degfp/spec.md": page("Reporter: deGFP", ["Requirements"])},
    )
    assert matching(found, "add it at the top of the page")  # Overview
    assert matching(found, "add it after 'Constituent Modules'")  # Credits


def test_only_the_ruled_sections_are_required(tmp_path):
    """Omitting a template section is normally correct, so absence alone is
    not a finding — style-guide/sections.md: "Omit a section rather than
    stubbing it empty"."""
    assert findings(
        tmp_path, {"modules/reporter-degfp/spec.md": page("Reporter: deGFP", ["Overview", "Credits"])}
    ) == []
    assert ctc.REQUIRED["implementation"] == ()


# --- scope item 5: it must be able to report non-zero -----------------------


def test_the_planted_fixture_fails(tmp_path, monkeypatch, capsys):
    corpus(tmp_path, {"modules/reporter-planted/spec.md": PLANTED})
    monkeypatch.chdir(tmp_path)

    assert ctc.main([]) == 1

    out = capsys.readouterr().out
    assert "top-level sections are H2" in out
    assert "orphan section 'Acknowledgments'" in out
    assert "'Reference Composition' comes after 'Credits'" in out
    assert "missing required section 'Overview'" in out
    assert "1 page(s) checked" in out


def test_a_clean_corpus_passes(tmp_path, monkeypatch, capsys):
    corpus(
        tmp_path,
        {
            "modules/base-membrane/spec.md": page("Base Membrane: POPC", FORMULATION),
            "processes/make-trna/main.md": page("Make tRNA", PROCESS),
            "implementations/atc-demo/main.md": page("aTc Demo", IMPLEMENTATION),
        },
    )
    monkeypatch.chdir(tmp_path)

    assert ctc.main([]) == 0
    assert "✅ 3 page(s) match their templates." in capsys.readouterr().out


# --- the fence-aware parser -------------------------------------------------


@pytest.mark.parametrize(
    "block",
    [
        "```bash\n# not a heading\n```",
        "~~~\n# not a heading\n~~~",
        ":::{note}\n# not a heading\n:::",
        "<!--\n# not a heading\n-->",
        "<!-- # not a heading -->",
    ],
    ids=["backticks", "tildes", "directive", "comment-block", "comment-line"],
)
def test_a_hash_inside_a_block_is_not_a_heading(block):
    text = f'---\ntitle: "T"\n---\n\n# Overview\n\n{block}\n\n# Credits\n\nText.\n'
    assert [t for _, _, t in ctc.headings(text)] == ["Overview", "Credits"]


def test_nested_directive_fences_close_by_colon_count(tmp_path):
    """`:::::{tab-set}` holds `::::{tab-item}` holds `:::{table}`.

    A boolean instead of a stack closes the tab-set on the first inner `:::`
    and leaves the rest of the page being read inside no fence at all.
    """
    text = (
        '---\ntitle: "T"\n---\n\n'
        "# Overview\n\n"
        ":::::{tab-set}\n"
        "::::{tab-item} DNA\n"
        ":::{table}\n"
        "| # | x |\n"
        "| --- | --- |\n"
        ":::\n"
        "::::\n"
        ":::::\n\n"
        "# Credits\n\nText.\n"
    )
    assert [t for _, _, t in ctc.headings(text)] == ["Overview", "Credits"]


def test_frontmatter_is_not_read_as_headings():
    text = (
        "---\n"
        'title: "Reporter: deGFP"\n'
        '# Title format: "Category: Name"\n'
        "---\n\n"
        "# Overview\n\nText.\n"
    )
    assert [t for _, _, t in ctc.headings(text)] == ["Overview"]


def test_a_heading_carries_its_line_number():
    text = '---\ntitle: "T"\n---\n\n# Overview\n\nText.\n\n# Credits\n'
    assert ctc.headings(text) == [(5, 1, "Overview"), (9, 1, "Credits")]


# --- what is skipped, and visibly ------------------------------------------


def test_a_class_page_is_skipped_with_a_reason(tmp_path):
    """spec-class.md is not in this tree, so there is nothing to check against.

    Both signals: a `spec.yml` declaring `abstract:`, and a `# Members`
    heading. Checking a class page against the functional or formulation
    template would manufacture findings from the wrong authority.
    """
    by_yml = {
        "modules/detector/spec.md": page("Detector", ["Overview", "Credits"]),
        "modules/detector/spec.yml": "abstract: true\nname: Detector\n",
    }
    found, notes_, _ = ctc.run(corpus(tmp_path, by_yml))
    assert found == []
    assert matching(notes_, "skipped: class page")

    by_members = {
        "modules/gel/spec.md": page("Gel", ["Overview", "Members", "Credits"])
    }
    found, notes_, _ = ctc.run(corpus(tmp_path / "b", by_members))
    assert found == []
    assert matching(notes_, "skipped: class page")


def test_a_parent_process_page_is_skipped_with_a_reason(tmp_path):
    files = {
        "processes/make-protein/make-protein-main.md": page(
            "Make Protein", ["Overview", "Make Protein Processes"]
        ),
        "processes/make-protein/grow-bacteria/main.md": page("Grow Bacteria", PROCESS),
    }
    found, notes_, checked = ctc.run(corpus(tmp_path, files))
    assert found == []
    assert matching(notes_, "skipped: parent page")
    assert checked == 2  # skipped, not dropped from the count


def test_a_modules_non_spec_page_is_not_a_module_page(tmp_path):
    """protocol-cells.md and bom-cytosol.md sit beside a spec and are not specs."""
    found, _notes, checked = ctc.run(
        corpus(
            tmp_path,
            {
                "modules/reporter-degfp/spec.md": page(
                    "Reporter: deGFP", ["Overview", "Credits"]
                ),
                "modules/reporter-degfp/protocol-cells.md": "# Overview\n\nText.\n",
            },
        )
    )
    assert found == []
    assert checked == 1


def test_a_hierarchy_index_page_is_not_a_page_in_the_hierarchy(tmp_path):
    found, _notes, checked = ctc.run(
        corpus(tmp_path, {"processes/processes-main.md": "# Overview\n\nText.\n"})
    )
    assert found == []
    assert checked == 0


# --- the CLI ----------------------------------------------------------------


def test_a_path_argument_scopes_the_run(tmp_path, monkeypatch, capsys):
    corpus(
        tmp_path,
        {
            "modules/reporter-degfp/spec.md": page("Reporter: deGFP", ["Requirements"]),
            "processes/make-trna/main.md": page("Make tRNA", PROCESS),
        },
    )
    monkeypatch.chdir(tmp_path)

    assert ctc.main(["docs/processes"]) == 0
    assert "1 page(s) match their templates." in capsys.readouterr().out

    assert ctc.main(["docs/modules"]) == 1
    assert "reporter-degfp" in capsys.readouterr().out
