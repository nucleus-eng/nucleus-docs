"""Tests for scripts/check-anchors.py — the anchor collision checker.

The failure mode this file exists to catch is a checker that finds nothing and
looks healthy doing it. `check-anchors.py` reported "no ambiguous anchors" on a
tree holding two duplicated labels, and it was right to: it validated *links*
against collected identifiers, and nothing linked to either label. A clean run
meant "no link is wrong today", which is not what a reader takes it to mean.

So every test here plants a known answer and asserts the checker reports it.
A test that only asserts exit 0 on a clean tree would have passed throughout
the bug.

Two kinds are reported, and they are kept apart on purpose:

  * an AMBIGUOUS LINK is a present defect — a reader clicking it lands on the
    wrong page today;
  * a DUPLICATE DEFINITION is a latent one — nothing links to it yet, so the
    rendered site is correct, and it goes wrong silently the day someone
    writes the link.

The end-to-end tests build a throwaway repo in tmp_path and point the script's
REPO at it, so they assert on real file scanning rather than on mocks.
"""

import importlib.util
import textwrap
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "check-anchors.py"


def _load():
    # The script is hyphenated, so it cannot be imported by name.
    spec = importlib.util.spec_from_file_location("check_anchors", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ca = _load()


def _write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).lstrip(), encoding="utf-8")
    return path


# --------------------------------------------------------------------------
# explicit_definitions — what counts as an author claiming a name
# --------------------------------------------------------------------------


def test_collects_directive_options_and_target_blocks(tmp_path):
    page = _write(tmp_path / "page.md", """
        # Title

        :::{table} Reaction setup.
        :name: rxn-setup
        :::

        :::{figure} a.png
        :label: fig-one
        :::

        (manual-target)=
        ## Section
    """)
    assert ca.explicit_definitions(page) == [
        ("rxn-setup", 4),
        ("fig-one", 8),
        ("manual-target", 11),
    ]


def test_headings_are_not_explicit_definitions(tmp_path):
    """Repeated headings are normal here and are the link pass's business.

    52 heading slugs collide across the TOC. Counting them as duplicate
    definitions would bury the two findings that are real.
    """
    page = _write(tmp_path / "page.md", """
        # Overview

        ## Expected Behavior
    """)
    assert ca.explicit_definitions(page) == []


def test_labels_inside_a_literal_fence_are_examples_not_definitions(tmp_path):
    """A syntax guide shows the same label twice — only the rendered one is real.

    guides/developer-note-syntax.md does exactly this: the label appears first
    inside a ``` block as the source a reader should copy, then again below it
    in a "Will appear as..." block. Counting both reports a duplicate on every
    page in the repo that teaches MyST syntax.
    """
    page = _write(tmp_path / "guide.md", """
        # How to write a figure

        ```
        :::{figure} ./my-fig.png
        :label: fig-my-fig
        :::
        ```

        :::{figure} ./my-fig.png
        :label: fig-my-fig
        :::
    """)
    assert ca.explicit_definitions(page) == [("fig-my-fig", 10)]


def test_a_braced_fence_is_a_directive_and_its_body_is_live(tmp_path):
    """```{note} is content, not an example. Labels inside it are real."""
    page = _write(tmp_path / "page.md", """
        ```{note}
        :::{table} T
        :name: inner-label
        :::
        ```
    """)
    assert ca.explicit_definitions(page) == [("inner-label", 3)]


def test_a_longer_fence_survives_an_inner_fence(tmp_path):
    """A ```` block quoting a ``` block closes on the ````, not the inner one."""
    page = _write(tmp_path / "page.md", """
        ````
        ```
        :label: not-a-definition
        ```
        ````

        :::{table} T
        :name: real-definition
        :::
    """)
    assert ca.explicit_definitions(page) == [("real-definition", 8)]


def test_same_page_duplicates_are_both_returned(tmp_path):
    """Returns a list, not a set — two claims on one page is still a finding."""
    page = _write(tmp_path / "page.md", """
        :::{table} First
        :name: twice
        :::

        :::{table} Second
        :name: twice
        :::
    """)
    assert ca.explicit_definitions(page) == [("twice", 2), ("twice", 6)]


# --------------------------------------------------------------------------
# End to end — the two planted known answers
# --------------------------------------------------------------------------


@pytest.fixture
def fake_repo(tmp_path, monkeypatch):
    """A throwaway repo with the real helper scripts and a TOC of its own."""
    (tmp_path / "scripts").mkdir()
    for helper in ("check-links.py", "check-toc.py"):
        (tmp_path / "scripts" / helper).write_text(
            (REPO / "scripts" / helper).read_text(encoding="utf-8"), encoding="utf-8"
        )
    monkeypatch.setattr(ca, "REPO", tmp_path)
    monkeypatch.setattr(ca, "MYST_YML", tmp_path / "myst.yml")
    monkeypatch.setattr(ca, "CONTENT_ROOTS", ("docs",))
    return tmp_path


def _toc(root: Path, *files: str) -> None:
    lines = ["version: 1", "project:", "  toc:"]
    lines += [f"    - file: ./{f}" for f in files]
    (root / "myst.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_clean_tree_exits_zero(fake_repo, monkeypatch, capsys):
    _write(fake_repo / "docs" / "a.md", """
        # A

        :::{table} T
        :name: unique-a
        :::
    """)
    _toc(fake_repo, "docs/a.md")
    monkeypatch.setattr("sys.argv", ["check-anchors.py"])
    assert ca.main() == 0
    assert "no ambiguous anchors, no duplicate definitions" in capsys.readouterr().out


def test_planted_duplicate_definition_is_reported(fake_repo, monkeypatch, capsys):
    """The os-prep case: one TOC page and one page outside the TOC.

    Nothing links to the label, and the page outside the TOC is not in the
    built site's cross-reference index — so the rendered site is correct and
    the link pass has nothing to say. This is the finding the checker used to
    miss entirely.
    """
    _write(fake_repo / "docs" / "assemble.md", """
        # Assemble

        :::{table} Preparation of outer solutions.
        :name: os-prep
        :::
    """)
    _write(fake_repo / "docs" / "protocol-cells.md", """
        # Protocol

        :::{table} Preparation of outer solutions.
        :name: os-prep
        :::
    """)
    _toc(fake_repo, "docs/assemble.md")  # protocol-cells.md deliberately omitted
    monkeypatch.setattr("sys.argv", ["check-anchors.py"])

    assert ca.main() == 1
    out = capsys.readouterr().out
    assert "1 identifier(s) defined more than once" in out
    assert "latent defect" in out
    assert "os-prep — defined at 2 sites" in out
    assert "docs/assemble.md:4  [TOC]" in out
    assert "docs/protocol-cells.md:4  [not in TOC]" in out
    # It must not be mistaken for the other kind.
    assert "bind to the wrong page" not in out


def test_planted_ambiguous_link_is_reported(fake_repo, monkeypatch, capsys):
    """The present-defect case: two TOC pages own `#overview`, and a link exists."""
    _write(fake_repo / "docs" / "one.md", """
        # Overview

        See [the other overview](./two.md#overview).
    """)
    _write(fake_repo / "docs" / "two.md", """
        # Overview
    """)
    _toc(fake_repo, "docs/one.md", "docs/two.md")
    monkeypatch.setattr("sys.argv", ["check-anchors.py"])

    assert ca.main() == 1
    out = capsys.readouterr().out
    assert "anchor(s) MyST will bind to the wrong page" in out
    assert "present defect" in out
    assert "docs/one.md:3" in out
    # A colliding *heading* is not reported as a duplicate definition.
    assert "defined more than once" not in out


def test_two_toc_pages_colliding_says_so(fake_repo, monkeypatch, capsys):
    """Severity wording turns on whether both sites are built into the site."""
    for name in ("one.md", "two.md"):
        _write(fake_repo / "docs" / name, """
            # Page

            :::{table} T
            :name: shared
            :::
        """)
    _toc(fake_repo, "docs/one.md", "docs/two.md")
    monkeypatch.setattr("sys.argv", ["check-anchors.py"])

    assert ca.main() == 1
    out = capsys.readouterr().out
    assert "2 of these are TOC pages — they collide in the built site now" in out


def test_naming_a_file_scopes_the_duplicate_report(fake_repo, monkeypatch, capsys):
    """Passing paths restricts findings to duplicates that involve those paths."""
    _write(fake_repo / "docs" / "a.md", """
        # A

        :::{table} T
        :name: shared
        :::
    """)
    _write(fake_repo / "docs" / "b.md", """
        # B

        :::{table} T
        :name: shared
        :::
    """)
    unrelated = _write(fake_repo / "docs" / "c.md", """
        # C

        :::{table} T
        :name: untouched
        :::
    """)
    _toc(fake_repo, "docs/a.md", "docs/b.md", "docs/c.md")
    monkeypatch.setattr("sys.argv", ["check-anchors.py", str(unrelated)])

    assert ca.main() == 0
