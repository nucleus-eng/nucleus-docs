"""Pin that check-functions.py says WHICH ref its coverage count was taken against.

The count compares declared operations in `compositional-biology-theory`'s signature
against rows in the Functions hub. It reads `git show REF:signature.md`, and REF
defaults to HEAD — **which is whatever branch that checkout happens to sit on**.

Measured 2026-10-08: the only theory checkout on this machine was on a feature branch
behind `origin/main`, so every count taken that day was against a tree no reader
shares. It came out right by luck; that branch had not touched the Interface block.

**This is `check-dna-refs.py`'s defect in a second script**, found the same day and
fixed the same way. Resolving against `origin/main` unconditionally would be wrong:
counting against your own unpushed branch is exactly what you want while checking an
edit before pushing it. There is no ref that is right for every run, so the script
says which one it used.

What is pinned is the disclosure and its silence on main — not the count, which moves.
"""

import importlib.util
import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-functions.py"


@pytest.fixture(scope="module")
def mod():
    spec = importlib.util.spec_from_file_location("check_functions", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


@pytest.fixture
def repo(tmp_path):
    """A checkout with `origin/main` and a feature branch that diverges from it."""
    d = tmp_path / "theory"
    d.mkdir()
    g = lambda *a: subprocess.run(["git", "-C", str(d), *a], capture_output=True, check=True)
    g("init", "-q", "-b", "main")
    (d / "signature.md").write_text("x\n", encoding="utf-8")
    g("add", "signature.md")
    g("-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "-m", "one")
    # a local ref standing in for the remote-tracking branch
    g("update-ref", "refs/remotes/origin/main", "HEAD")
    return d, g


def test_main_is_not_warned_about(mod, repo):
    d, _ = repo
    assert mod.ref_warning(d, "HEAD") == ""


def test_a_diverged_branch_is_named_and_counted(mod, repo):
    """The branch name and the distance both matter: one says what, one says how stale."""
    d, g = repo
    g("checkout", "-q", "-b", "claude/some-feature")
    (d / "signature.md").write_text("y\n", encoding="utf-8")
    g("add", "signature.md")
    g("-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "-m", "two")

    out = mod.ref_warning(d, "HEAD")
    assert "claude/some-feature" in out
    assert "NOT `origin/main`" in out
    assert "--ref origin/main" in out, "must say how to get the reader's count"


def test_no_remote_is_silent_rather_than_wrong(mod, tmp_path):
    """With no origin/main there is nothing to compare against, so claim nothing.

    A warning here would fire on every fresh clone of a repo that has no remote,
    which trains a reader to ignore it.
    """
    d = tmp_path / "bare"
    d.mkdir()
    subprocess.run(["git", "-C", str(d), "init", "-q"], check=True)
    assert mod.ref_warning(d, "HEAD") == ""
