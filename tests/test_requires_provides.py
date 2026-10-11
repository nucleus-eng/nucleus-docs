"""Pin how a requirement meets a provider in scripts/collate-conditions.py.

A module-level `requires:` and a `provides:` meet by name. The rule that matters is
the direction of specificity: a bare `transcribe` is met by any provider of
`transcribe`, and `transcribe[pT7]` only by a provider with the same bracket. A
provider is never less specific than what it meets. Get that backwards and a T7-driven
construct is reported as served by S30 Lysate, which cannot transcribe it.

The last test runs on the real sources: the repressor detector's requirement is met,
and by the two cytosols that declare it.
"""

import importlib.util
import os
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "collate-conditions.py"


@pytest.fixture(scope="module")
def cc():
    # The script globs its sources relative to the working directory when it loads,
    # so load it from the repo root wherever pytest was started.
    here = os.getcwd()
    os.chdir(SCRIPT.parent.parent)
    try:
        spec = importlib.util.spec_from_file_location("collate_conditions", SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        os.chdir(here)
    return mod


def test_a_bare_requirement_is_met_by_any_restriction(cc):
    assert cc.meets("transcribe[pT7]", "transcribe")
    assert cc.meets("transcribe", "transcribe")


def test_a_restricted_requirement_needs_the_same_restriction(cc):
    assert cc.meets("transcribe[pT7]", "transcribe[pT7]")
    assert not cc.meets("transcribe[sigma70]", "transcribe[pT7]")


def test_a_bare_provider_does_not_meet_a_restricted_requirement(cc):
    # A provider that does not say which promoter cannot be assumed to read pT7.
    assert not cc.meets("transcribe", "transcribe[pT7]")


def test_a_different_operation_never_meets(cc):
    assert not cc.meets("translate", "transcribe")
    assert not cc.meets("transcribe-x", "transcribe")


def test_the_repressor_requirement_is_met_by_both_cytosols(cc, monkeypatch):
    monkeypatch.chdir(SCRIPT.parent.parent)  # load() opens the paths it globbed
    req, prov = cc.requirements()
    assert ("transcribe", "repressor-detector") in req
    met_by = {m for p, m in prov if cc.meets(p, "transcribe")}
    assert met_by == {"base-cytosol", "s30-lysate"}
    # S30 does not read a T7 promoter, so it must not meet a T7 requirement.
    assert {m for p, m in prov if cc.meets(p, "transcribe[pT7]")} == {"base-cytosol"}
