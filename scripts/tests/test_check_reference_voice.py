"""Tests for scripts/check-reference-voice.py — the who-decided net.

Both defects pinned here were found the same way: by running the checker over a
corpus it had already passed. The case defect is why `d6cd78eb` and `9dd612b5`
exist, two commits that fixed by hand what this script was built to catch —
`RULED` and `THE THEORY CORPUS` went straight through a pattern spelled
`[Rr]ul` and `[Tt]heory`. The branch defect ran the other way: `check-pins.py`
reported `roll/refinement-rulings` as a recorded decision, which is a place.

ONE THING PER CASE. The first draft of this fixture labeled its own rows
`rulings-lower` and `rulings-caps`, so three of them fired on the annotation
rather than on the text under test and the run looked like a pass of a
different question. A fixture needs the same known-answer check as the
instrument it tests.
"""

import importlib.util
import re
from pathlib import Path

import pytest


def _load_module():
    """Import check-reference-voice.py by path (hyphenated filename)."""
    path = Path(__file__).resolve().parent.parent / "check-reference-voice.py"
    spec = importlib.util.spec_from_file_location("check_reference_voice", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


crv = _load_module()


def _fires(rule: str, text: str) -> bool:
    """True when `rule` matches `text` after the blanking the checker applies."""
    pattern = (crv.TIER1 | crv.TIER2)[rule][0]
    blanked = crv._blank_branch(crv._URL.sub(" ", crv._LINK_TARGET.sub("]()", text)))
    return bool(pattern.search(blanked))


# --- the `ruling` rule is case-insensitive, and its `out` exemption with it ---

@pytest.mark.parametrize("text", [
    "the team ruled on this",
    "Ruled by the group",
    "RULED by the group",            # d6cd78eb, 9dd612b5: capitals went through
    "the RuLiNg stands",
])
def test_ruling_fires_in_any_case(text):
    assert _fires("ruling", text)


@pytest.mark.parametrize("text", [
    "that option was ruled out",
    "that option was RULED OUT",     # the exemption is case-insensitive too
])
def test_ruled_out_is_not_a_ruling(text):
    assert not _fires("ruling", text)


def test_rulings_md_is_an_address_not_a_ruling():
    """`(?!\\.md)` keeps the filename out; `working-notes` is what catches it."""
    assert not _fires("ruling", "cited in rulings.md today")
    assert _fires("working-notes", "cited in rulings.md today")


# --- working-notes and corpus-talk are case-insensitive too ---

@pytest.mark.parametrize("text", [
    "see the theory corpus for detail",
    "see THE THEORY CORPUS for detail",
    "recorded in RULINGS.MD today",
])
def test_working_notes_fires_in_any_case(text):
    assert _fires("working-notes", text)


@pytest.mark.parametrize("text", ["this corpus", "THIS CORPUS", "The Corpus"])
def test_corpus_talk_fires_in_any_case(text):
    assert _fires("corpus-talk", text)


# --- a branch or directory name is an address, not a record of a decision ---

@pytest.mark.parametrize("text", [
    "merged from branch roll/refinement-rulings yesterday",
    "the branch docs/who-ruled-what carries it",
    "see docs/processes/colorimetric-readout for the method",
])
def test_a_branch_name_is_not_a_ruling(text):
    assert not _fires("ruling", text)


def test_blanking_a_branch_keeps_the_true_positive_beside_it():
    """The blanker must not swallow prose that happens to sit near a path."""
    assert _fires("ruling", "on branch fix/dna-repo-path the group ruled that it holds")


@pytest.mark.parametrize("text, rule", [
    ("quoted from rulings.md:97", "working-notes"),
    ("see scripts/check-foo.py:12 for the pattern", "tooling"),
])
def test_a_path_with_an_extension_stays_visible(text, rule):
    """Only a last segment with no dot is blanked, so a filename still reports."""
    assert _fires(rule, text)


# --- the rules that must stay case-SENSITIVE ---

def test_review_tag_stays_case_sensitive():
    """`@claude` lowercase is not a review tag; the rule wants a capital."""
    assert _fires("review-tag", "@Claude: please look")
    assert not _fires("review-tag", "an @editor note")


def test_blank_branch_preserves_line_length():
    """Columns stay true, unlike the URL blanker beside it."""
    line = "see roll/refinement-rulings here"
    assert len(crv._blank_branch(line)) == len(line)
