"""Tests for scripts/check-materials-tables.py.

A CHECKER THAT HAS NEVER BEEN ABLE TO FAIL HAS NOT BEEN SHOWN TO WORK. This
corpus has about a dozen recorded instances of a green run that was never the
check -- a `--check` flag that did not exist and was ignored, a comparison that
agreed with its reference on every case where the thing under test did not
matter. So each job below gets a fixture that fails it and a control that
passes, and the clean fixture is the control for all three.

The inversion test is not hypothetical. The first run of the checker reported
`Part #` as off the allowlist in every file in the repo, templates included,
because ALLOWED_TITLES is keyed by FIELD and a header cell is a TITLE. It
passed `Name` and `Manufacturer`, where the two coincide. That is the exact
shape of a check that looks like it is working.
"""

import importlib.util
from pathlib import Path

import pytest

from bom_common import ALLOWED_TITLES, REQUIRED_FIELDS


def _load():
    """Import check-materials-tables.py by path (hyphen, so not importable)."""
    path = Path(__file__).resolve().parent.parent / "check-materials-tables.py"
    spec = importlib.util.spec_from_file_location("check_materials_tables", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cmt = _load()


CLEAN = """\
:::{table}
:label: critical-materials

| Name | Manufacturer | Part # |
| --- | --- | --- |
| Agarose | Sigma-Aldrich | A5030 |
:::
"""

NO_PART = """\
:::{table}
:label: critical-materials

| Name | Product | Manufacturer | Storage |
| --- | --- | --- | --- |
| deGFP | plamGFP | Addgene | -20 C |
:::
"""

RETIRED_TITLE = """\
:::{table}
:label: critical-materials

| Material | Manufacturer | Part # |
| --- | --- | --- |
| Agarose | Sigma-Aldrich | A5030 |
:::
"""

UNKNOWN_TITLE = """\
:::{table}
:label: critical-materials

| Name | Lot size | Manufacturer | Part # |
| --- | --- | --- | --- |
| Agarose | 5 g | Sigma-Aldrich | A5030 |
:::
"""

MISSING_REQUIRED = """\
:::{table}
:label: critical-materials

| Description | Manufacturer | Part # |
| --- | --- | --- |
| A gelling agent | Sigma-Aldrich | A5030 |
:::
"""

PROSE_PLACEHOLDER = """\
:::{table}
:label: critical-materials

| Name | Manufacturer | Part # |
| --- | --- | --- |
| ULGA | Sigma-Aldrich | Not stated |
| LGA | Sigma-Aldrich | A9414-5G |
:::
"""

EM_DASH = """\
:::{table}
:label: critical-materials

| Name | Manufacturer | Part # |
| --- | --- | --- |
| ULGA | Sigma-Aldrich | — |
:::
"""

RECIPE = """\
| Reagent | Volume |
| --- | --- |
| SMix | 3.0 uL |
"""

EQUIPMENT = """\
:::{table} Equipment.
| Item | Used for |
| --- | --- |
| Projector | Photocrosslinking |
:::
"""


def run(tmp_path, text, name="spec.md"):
    p = tmp_path / name
    p.write_text(text, encoding="utf-8")
    return cmt.check_file(p)


# --- the control ----------------------------------------------------------- #

def test_clean_table_has_no_findings(tmp_path):
    assert run(tmp_path, CLEAN) == []


# --- job 1: the header parses at all --------------------------------------- #

def test_job1_fires_on_a_table_with_no_part_column(tmp_path):
    found = run(tmp_path, NO_PART)
    assert [f.job for f in found] == [1]
    assert "no part column" in found[0].message


def test_job1_suppresses_jobs_2_and_3(tmp_path):
    """A table that does not parse has no column map, so the later jobs would
    be guessing. Exactly one finding, and it is the one that matters."""
    assert len(run(tmp_path, NO_PART)) == 1


# --- job 2: titles on the allowlist, required three present ---------------- #

def test_job2_fires_on_a_retired_spelling(tmp_path):
    found = [f for f in run(tmp_path, RETIRED_TITLE) if f.job == 2]
    assert len(found) == 1
    assert "retired spelling of 'Name'" in found[0].message


def test_job2_fires_on_an_unknown_title(tmp_path):
    found = [f for f in run(tmp_path, UNKNOWN_TITLE) if f.job == 2]
    assert len(found) == 1
    assert "'Lot size' is not on the allowlist" in found[0].message


def test_job2_fires_on_a_missing_required_column(tmp_path):
    found = [f for f in run(tmp_path, MISSING_REQUIRED) if f.job == 2]
    assert len(found) == 1
    assert "required column 'Name' is missing" in found[0].message


@pytest.mark.parametrize("field", REQUIRED_FIELDS)
def test_job2_every_allowed_title_passes(tmp_path, field):
    """The inverse map is built right -- every required title is a key in it.

    THIS IS NOT THE TEST THAT CATCHES THE INVERSION. Restoring the bug (look
    `key` up in ALLOWED_TITLES instead of _ALLOWED_BY_TITLE) leaves this test
    green, because it asserts on the map and the bug is in the use of it. What
    goes red is test_clean_table_has_no_findings and
    test_job2_passes_every_optional_title -- the two that run a real table
    through. Measured by mutation, not assumed.
    """
    assert ALLOWED_TITLES[field].lower() in cmt._ALLOWED_BY_TITLE


def test_job2_passes_every_optional_title(tmp_path):
    header = " | ".join(ALLOWED_TITLES[f] for f in ALLOWED_TITLES)
    text = (":::{table}\n:label: critical-materials\n\n"
            "| %s |\n| %s |\n| %s |\n:::\n"
            % (header,
               " | ".join("---" for _ in ALLOWED_TITLES),
               " | ".join("x" for _ in ALLOWED_TITLES)))
    assert [f for f in run(tmp_path, text) if f.job == 2] == []


# --- job 3: no prose placeholder where a value is indexed ------------------ #

def test_job3_fires_on_not_stated(tmp_path):
    found = [f for f in run(tmp_path, PROSE_PLACEHOLDER) if f.job == 3]
    assert len(found) == 1
    assert "Not stated" in found[0].message


def test_job3_accepts_an_em_dash(tmp_path):
    """The control for job 3. An em dash is a PLACEHOLDER and is skipped by the
    indexer; prose is not, and is keyed as a real material."""
    assert [f for f in run(tmp_path, EM_DASH) if f.job == 3] == []


# --- scope: what is and is not a materials table --------------------------- #

def test_a_recipe_table_is_not_audited(tmp_path):
    """`Reagent` is a retired alias for Name and appears in 21 headers on main,
    most of them recipe tables. Without a Manufacturer or Part # column and
    without a label, this is not a materials table and must not be reported."""
    assert run(tmp_path, RECIPE) == []


def test_an_unlabelled_equipment_table_is_not_audited(tmp_path):
    """Q5, ruled 2026-10-12: equipment stays out of the materials reference.
    It stays out structurally -- no materials label, no Manufacturer column --
    and not by spelling its headers defensively."""
    assert run(tmp_path, EQUIPMENT) == []


def test_a_labelled_table_is_audited_even_with_no_known_column(tmp_path):
    """The label is the other way in. Without it, `Item | Used for | Supplier
    and part number` is indistinguishable from a recipe table."""
    text = (":::{table}\n:label: materials-embed-thermal-setting\n\n"
            "| Item | Used for | Supplier and part number |\n"
            "| --- | --- | --- |\n| ULGA | Gel | Not stated |\n:::\n")
    found = run(tmp_path, text)
    assert [f.job for f in found] == [1]


# --- the header predicate -------------------------------------------------- #

def test_a_cell_value_is_not_read_as_a_header(tmp_path):
    """A sweep on 2026-10-12 counted every pipe row and reported `Reagent` 19
    times as a header when it is a Category value. A header is a row followed
    by a `| --- |` separator, and nothing else."""
    text = CLEAN.replace("| Agarose | Sigma-Aldrich | A5030 |",
                         "| Agarose | Sigma-Aldrich | A5030 |\n| Lot size | x | y |")
    assert run(tmp_path, text) == []
