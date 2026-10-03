"""Tests for scripts/check-reference-voice.py.

Each case is one line of page text and the rules it must raise. The firing
cases matter as much as the clean ones: a check that reports zero on main has to
be shown able to report non-zero, or the zero means nothing.
"""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-reference-voice.py"
_spec = importlib.util.spec_from_file_location("check_reference_voice", SCRIPT)
crv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(crv)

CONTRIBUTORS = """\
- Jon Calles — b.next
- Anton Jackson-Smith — b.next
- Anton Molina — b.next
- Yemo Ku — b.next
"""


@pytest.fixture
def contributors(tmp_path):
    path = tmp_path / "contributors.md"
    path.write_text(CONTRIBUTORS)
    return path


def rules_for(tmp_path, contributors, body):
    page = tmp_path / "page.md"
    page.write_text(body)
    person = crv.person_pattern(crv.read_contributors(contributors))
    return {rule for _, _, rule, _, _ in crv.check_file(page, person)}


@pytest.mark.parametrize("line, expected", [
    # Tier 1: who decided
    ("Jon ruled on 2026-09-29 that Gel refines by formation route.", {"person", "ruling", "date"}),
    ("**The rows above are filled**, on Jon's word.", {"person"}),
    ("Jon, 2026-09-21: *\"that's the right range.\"*", {"person", "date"}),
    ("Chicago Node, Mary, 2026-09-17: theophylline inhibits LacZ.", {"person", "date"}),
    ("Anton said the pore is passive.", {"person"}),
    ("An abstract Module carries an abstract Context, ruled 2026-09-17.", {"ruling", "date"}),
    ("That is why the membership ruling matters.", {"ruling"}),
    # Tier 1: working notes and review tags
    ("This is `open.md#O21` in the theory corpus.", {"working-notes"}),
    ("`compositional-biology-theory` declares Container in `signature.md`.", {"working-notes"}),
    ("Expand this (@Claude: merge LGA into ULGA).", {"review-tag"}),
    # Tier 2
    ("Written 2026-09-24 because three whiteboards reached for it.", {"date"}),
    ("It is the most general class this corpus names.", {"corpus-talk"}),
    ("`spec.yml` declares no `process_steps`.", {"tooling"}),
    ("`one_member_classes()` reported this class.", {"tooling"}),
    ("Applied at `6511b55`.", {"hash"}),
])
def test_fires(tmp_path, contributors, line, expected):
    assert rules_for(tmp_path, contributors, line + "\n") == expected


@pytest.mark.parametrize("line", [
    "Reformulated from the PURE system by Yemo Ku and Jon Calles (b.next).",
    "Anton Jackson-Smith and Anton Molina designed the pore.",
    "With membrane stability ruled out, the block sits in expression.",
    "@Editor(chicago): what temperature is the gel set at?",
    "@Editor: add the vendor page. @Developer: confirm the stock.",
    "Questions go to build@bnext.bio.",
    "See the [glossary](../glossary.md) and [DevNote](https://example.org/2026-09-24/open.md).",
    "Load the sample in tranches of 10 mL at a time.",
    "The 3.2 kDa cutoff is set by the pore, not the membrane.",
    "Chicago Node, Mary, 2026-09-17, personal communication: theophylline inhibits LacZ.",
])
def test_clean(tmp_path, contributors, line):
    assert rules_for(tmp_path, contributors, line + "\n") == set()


def test_skips_frontmatter_code_and_comments(tmp_path, contributors):
    body = (
        "---\n"
        "title: Jon ruled\n"
        "---\n"
        "```\n"
        "Jon ruled on 2026-09-29\n"
        "```\n"
        "<!-- Jon ruled\n"
        "on 2026-09-29 -->\n"
        "<!-- gen:position -->\n"
        "Refines nothing declared.\n"
        "<!-- /gen:position -->\n"
    )
    assert rules_for(tmp_path, contributors, body) == set()


def test_checks_text_between_gen_markers(tmp_path, contributors):
    body = "<!-- gen:position -->\nJon ruled this.\n<!-- /gen:position -->\n"
    assert rules_for(tmp_path, contributors, body) == {"person", "ruling"}


def test_reports_line_numbers(tmp_path, contributors):
    page = tmp_path / "page.md"
    page.write_text("---\ntitle: x\n---\n\nFine.\n\nJon ruled.\n")
    person = crv.person_pattern(crv.read_contributors(contributors))
    assert {n for n, *_ in crv.check_file(page, person)} == {7}


def test_exit_codes(tmp_path, contributors):
    page = tmp_path / "page.md"
    args = [str(page), "--contributors", str(contributors)]
    page.write_text("Written 2026-09-24.\n")
    assert crv.main(args) == 0                  # warnings alone pass
    assert crv.main(args + ["--strict"]) == 1   # unless --strict
    page.write_text("Jon ruled.\n")
    assert crv.main(args) == 1                  # errors fail


def test_no_contributors_is_not_a_pass(tmp_path):
    page = tmp_path / "page.md"
    page.write_text("Jon ruled.\n")
    empty = tmp_path / "contributors.md"
    empty.write_text("No list here.\n")
    assert crv.main([str(page), "--contributors", str(empty)]) == 2


def test_reads_the_real_contributors_list():
    names = crv.read_contributors(crv.CONTRIBUTORS)
    assert ("Jon", "Calles") in names
    assert len(names) > 10


def test_a_missing_path_is_not_a_pass(tmp_path, contributors):
    # The failure this guards: a shell passed several paths as one argument, the
    # one path did not exist, and the check reported 0 errors over 0 files.
    missing = tmp_path / "a.md\nb.md"
    assert crv.main([str(missing), "--contributors", str(contributors)]) == 2


def test_no_markdown_files_is_not_a_pass(tmp_path, contributors):
    empty = tmp_path / "empty"
    empty.mkdir()
    (empty / "notes.txt").write_text("Jon ruled.\n")
    assert crv.main([str(empty), "--contributors", str(contributors)]) == 2
