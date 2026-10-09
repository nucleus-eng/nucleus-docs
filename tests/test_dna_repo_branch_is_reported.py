"""Pin that check-dna-refs.py says which branch of nucleus-eng/DNA it read.

The index comes from `repo_root.rglob("*")` — the working tree, never a ref —
so the script finds the branch the checkout happens to be on. That cuts both
ways, and the quieter half is the false pass:

- A page saying a construct is ABSENT is reported wrong when a feature branch
  adds a file of that name. `detector-tetr-atc/spec.md:74-75` is reported this
  way today, and the page is correct: neither file is on `main`.
- A construct genuinely added to `main` is still "found" on a stale feature
  branch that lacks it, so a real absence claim goes unreported and nothing
  anywhere says so.

Resolving against `origin/main` instead would not fix it, because a page may
legitimately cite a construct that only exists on a branch. **Naming the tree
that was read is what lets a reader tell the two cases apart**, so that is what
is pinned here — the disclosure, not a verdict.
"""

import importlib.util
import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-dna-refs.py"


@pytest.fixture(scope="module")
def mod():
    spec = importlib.util.spec_from_file_location("check_dna_refs", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


@pytest.fixture
def repo(tmp_path):
    """A git checkout on a branch that is not `main`."""
    d = tmp_path / "DNA"
    d.mkdir()
    (d / "a.gb").write_text("LOCUS       thing  100 bp\n", encoding="utf-8")
    run = lambda *a: subprocess.run(["git", "-C", str(d), *a], capture_output=True, check=True)
    run("init", "-q", "-b", "main")
    run("-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "--allow-empty", "-m", "x")
    run("add", "a.gb")
    run("-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "-m", "y")
    return d, run


def test_it_reports_the_branch_and_the_commit(mod, repo):
    d, _ = repo
    branch, head = mod.dna_repo_state(d)
    assert branch == "main"
    assert head and len(head) >= 7
    assert str(d) in mod.describe_dna_repo_state(d, branch, head)
    assert head in mod.describe_dna_repo_state(d, branch, head)


def test_a_branch_that_is_not_main_says_so_and_says_why(mod, repo):
    """The warning must name BOTH failure modes, not only the one that bites today.

    A reader who is told only about the false fail will trust a clean run on a
    stale branch, which is the case nothing else in this script can catch.
    """
    d, run = repo
    run("checkout", "-q", "-b", "devcells/devstudio-constructs")
    branch, head = mod.dna_repo_state(d)
    out = mod.describe_dna_repo_state(d, branch, head)

    assert "devcells/devstudio-constructs" in out
    assert "NOT `main`" in out
    assert "absent" in out, "must name the false fail"
    assert "unreported" in out, "must name the false pass"


def test_main_is_not_warned_about(mod, repo):
    d, _ = repo
    branch, head = mod.dna_repo_state(d)
    assert "NOT `main`" not in mod.describe_dna_repo_state(d, branch, head)


def test_a_non_checkout_says_the_branch_is_unknown_and_does_not_crash(mod, tmp_path):
    """Absence of git must read as unknown, never as `main`.

    Silence here would be the worst outcome: a run with no branch line looks
    exactly like a run on `main`, which is the one state that needs no warning.
    """
    d = tmp_path / "plain"
    d.mkdir()
    branch, head = mod.dna_repo_state(d)
    assert branch is None and head is None
    out = mod.describe_dna_repo_state(d, branch, head)
    assert "unknown" in out
    assert "NOT `main`" not in out
