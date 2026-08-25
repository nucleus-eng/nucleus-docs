"""Pin check-links.py's copy of MyST's slug rule.

`myst_html_id` is a hand port of `createHtmlId` in myst-common. MyST is not a
Python dependency, so nothing makes the two move together — this file is the
only thing that will notice if MyST changes the rule or someone "simplifies"
the port.

The case that matters is repeated hyphens. lychee slugs headings the GitHub
way and keeps them; MyST collapses them. Get that one wrong and the checker
reports working links as broken, which is worse than not checking at all.
"""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-links.py"

_spec = importlib.util.spec_from_file_location("check_links", SCRIPT)
check_links = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_links)

myst_html_id = check_links.myst_html_id
myst_anchors = check_links.myst_anchors


@pytest.mark.parametrize(
    "heading,expected",
    [
        # The regression case: " / " collapses to one hyphen under MyST, but
        # stays "--" under lychee. Seven real links depended on this.
        (
            "Chicago Cascade Encapsulation (TetO-PLA1 / LacZ-CPRG Readout)",
            "chicago-cascade-encapsulation-teto-pla1-lacz-cprg-readout",
        ),
        # Parentheses alone do not diverge — both tools agree here.
        ("Membrane (Base)", "membrane-base"),
        # Plain headings, the overwhelming majority.
        ("Expected Behavior", "expected-behavior"),
        ("Implementations", "implementations"),
        ("Reference Composition", "reference-composition"),
        ("Constituent Modules", "constituent-modules"),
        # Leading digit gets an "id-" prefix rather than an invalid HTML id.
        ("3 Step Protocol", "id-3-step-protocol"),
        # Trailing punctuation is stripped, not left as a hyphen.
        ("Downloads:", "downloads"),
        # Leading punctuation collapses to a hyphen, which then trips the
        # "must not start with a digit or hyphen" guard and picks up "id-".
        # Verified against myst-common, not derived from the port.
        ("— Credits —", "id-credits"),
        # Quotes are removed outright, not turned into hyphens.
        ("The “Base” Cell", "the-base-cell"),
        # Chemistry and units survive as-is once lowercased.
        ("Mg²⁺ Requirements", "mg-requirements"),
    ],
)
def test_myst_html_id(heading, expected):
    assert myst_html_id(heading) == expected


def test_anchors_from_headings_labels_and_targets(tmp_path):
    page = tmp_path / "spec.md"
    page.write_text(
        "\n".join(
            [
                "# Overview",
                "",
                "## Expected Behavior",
                "",
                "### Chicago Cascade Encapsulation (TetO-PLA1 / LacZ-CPRG Readout)",
                "",
                ":::{table} A composition",
                ":label: comp-ph-sensor",
                ":::",
                "",
                ":::{figure} x.png",
                ":name: fig-schematic",
                ":::",
                "",
                "(my-explicit-target)=",
                "## Materials",
                "",
                "## Using `pOpen-deGFP` and **bold** and [a link](http://x)",
            ]
        ),
        encoding="utf-8",
    )

    anchors = myst_anchors(str(page))

    assert "overview" in anchors
    assert "expected-behavior" in anchors
    assert (
        "chicago-cascade-encapsulation-teto-pla1-lacz-cprg-readout" in anchors
    )
    assert "comp-ph-sensor" in anchors
    assert "fig-schematic" in anchors
    assert "my-explicit-target" in anchors
    # Inline markdown is stripped before slugging. MyST slugs a heading's
    # rendered text (mdast toText), not its source, so the link URL does not
    # appear. Feeding the raw source to myst-common's normalizeLabel gives
    # "...-a-link-http-x" instead — that is not what a MyST build produces.
    assert "using-popen-degfp-and-bold-and-a-link" in anchors
    # The lychee/GitHub spelling must NOT be present, or the divergence check
    # silently stops suppressing anything.
    assert (
        "chicago-cascade-encapsulation-teto-pla1--lacz-cprg-readout"
        not in anchors
    )


def test_missing_file_yields_no_anchors():
    assert myst_anchors("/nonexistent/spec.md") == frozenset()
