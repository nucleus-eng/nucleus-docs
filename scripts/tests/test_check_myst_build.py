"""Tests for scripts/check-myst-build.py: the exit code is part of the contract.

The script used to read only the ⛔️ lines and ignore myst's exit code. The
local `myst` shim was curvenote 0.13.1, which prints an "Upgrade Required"
banner, builds nothing and exits 1. That output has no ⛔️ line, so the script
printed "✅ myst build: no unfiltered ⛔️ errors" and exited 0 for a build that
never ran.

The fixtures below are real output, captured from the two binaries:

  * CURVENOTE_BANNER: curvenote 0.13.1 on this repo, exit 1.
  * STRICT_ERROR: mystmd 1.9.1, `build --html --strict`, a missing image, exit 1.
  * STRICT_WARNING_ONLY: the same command on a page whose only issue is an
    unrecognized frontmatter key, exit 0. `--strict` fails on a ⛔️ error and
    not on a ⚠️ warning, so a non-zero exit with no ⛔️ line means "did not run".

Every test runs offline: shutil.which and subprocess.run are stubbed.
"""

import importlib.util
import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "check-myst-build.py"


def _load_module():
    # The script is hyphenated, so it cannot be imported by name.
    spec = importlib.util.spec_from_file_location("check_myst_build", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cmb = _load_module()

CURVENOTE_BANNER = """\
(node:29311) ExperimentalWarning: localStorage is not available because --localstorage-file was not provided.
(Use `node --trace-warnings ...` to show where the warning was created)

   ╭───────────────────────────────────────────────────╮
   │                                                   │
   │   Upgrade Required! v0.13.1 ≫ v0.14.2 (minimum)   │
   │                                                   │
   │    Run `npm i -g curvenote@latest` to update.     │
   │                                                   │
   ╰───────────────────────────────────────────────────╯
"""

STRICT_ERROR = """\
🌎 Building MyST site
📖 Built index.md in 2.13 ms.
⛔️ index.md:7 Cannot find image "does-not-exist.png" in /tmp/probe-err
⛔️ index.md Cannot find image "does-not-exist.png" in /tmp/probe-err
📚 Built 1 page for project in 5.55 ms.

index.md
  - ⛔ Cannot find image "does-not-exist.png" in /tmp/probe-err
  - ⛔ Cannot find image "does-not-exist.png" in /tmp/probe-err

Site has 2 errors and 0 warning, stopping build.
"""

STRICT_WARNING_ONLY = """\
🍡 Execution parallelism set to: 9
⚠️  index.md 'frontmatter' extra key ignored: status (at index.md)
🌎 Building MyST site
📖 Built index.md in 2.38 ms.
📚 Built 1 page for project in 5.89 ms.
"""

CX43_LINE = (
    '⛔️ docs/modules/membrane-pore-cx43/spec.md '
    'Cannot find image "./Figure/connexin-scheme.png" in /repo/docs/modules/membrane-pore-cx43'
)
FALSE_POSITIVES = [
    {
        "file": "docs/modules/membrane-pore-cx43/spec.md",
        "substring": 'Cannot find image "./Figure/connexin-scheme.png"',
    }
]


# --- parse_errors ------------------------------------------------------------


def test_parse_errors_finds_the_error_lines_and_not_the_summary():
    genuine, filtered = cmb.parse_errors(STRICT_ERROR, [])
    assert len(genuine) == 2
    assert all(line.startswith("⛔️ index.md") for line in genuine)
    assert filtered == 0


def test_parse_errors_reports_nothing_for_a_warning_only_run():
    assert cmb.parse_errors(STRICT_WARNING_ONLY, []) == ([], 0)


def test_parse_errors_reports_nothing_for_the_curvenote_banner():
    assert cmb.parse_errors(CURVENOTE_BANNER, []) == ([], 0)


def test_parse_errors_filters_a_known_false_positive():
    assert cmb.parse_errors(CX43_LINE, FALSE_POSITIVES) == ([], 1)


def test_parse_errors_keeps_the_same_message_in_another_file():
    other = CX43_LINE.replace("membrane-pore-cx43", "membrane-pore-ahly")
    genuine, filtered = cmb.parse_errors(other, FALSE_POSITIVES)
    assert genuine == [other]
    assert filtered == 0


# --- verdict: one row per case ----------------------------------------------


@pytest.mark.parametrize(
    ("returncode", "genuine", "filtered", "expected"),
    [
        pytest.param(0, [], 0, 0, id="clean-build"),
        pytest.param(0, [], 0, 0, id="warnings-only-strict-exits-0"),
        pytest.param(1, ["⛔️ a.md x"], 0, 1, id="strict-error"),
        pytest.param(0, ["⛔️ a.md x"], 0, 1, id="error-with-exit-0-still-fails"),
        pytest.param(1, [], 0, 2, id="nonzero-exit-no-error-line-did-not-run"),
        pytest.param(137, [], 0, 2, id="killed-process-did-not-run"),
        pytest.param(1, [], 1, 0, id="strict-exit-1-from-a-filtered-false-positive"),
        pytest.param(1, ["⛔️ b.md y"], 1, 1, id="false-positive-does-not-hide-another-error"),
    ],
)
def test_verdict(returncode, genuine, filtered, expected):
    assert cmb.verdict(returncode, genuine, filtered) == expected


# --- main(): the whole script on the captured output --------------------------


def _run_main(monkeypatch, capsys, *, which, returncode=0, output=""):
    monkeypatch.setattr(cmb.shutil, "which", lambda name: which)
    monkeypatch.setattr(
        cmb.subprocess,
        "run",
        lambda *a, **k: subprocess.CompletedProcess(a, returncode, stdout=output, stderr=""),
    )
    monkeypatch.setattr(cmb, "_load_false_positives", lambda: FALSE_POSITIVES)
    with pytest.raises(SystemExit) as exc:
        cmb.main()
    return exc.value.code, capsys.readouterr().out


def test_main_curvenote_banner_is_not_a_pass(monkeypatch, capsys):
    code, out = _run_main(
        monkeypatch, capsys, which="/usr/bin/myst", returncode=1, output=CURVENOTE_BANNER
    )
    assert code == 2
    assert "did not run" in out
    assert "Upgrade Required" in out  # the reader sees why
    assert "✅" not in out


def test_main_strict_error_fails(monkeypatch, capsys):
    code, out = _run_main(
        monkeypatch, capsys, which="/usr/bin/myst", returncode=1, output=STRICT_ERROR
    )
    assert code == 1
    assert "2 genuine myst build error(s)" in out


def test_main_warning_only_passes(monkeypatch, capsys):
    code, out = _run_main(
        monkeypatch, capsys, which="/usr/bin/myst", returncode=0, output=STRICT_WARNING_ONLY
    )
    assert code == 0
    assert "✅" in out


def test_main_known_false_positive_passes_even_though_myst_exited_1(monkeypatch, capsys):
    code, out = _run_main(
        monkeypatch, capsys, which="/usr/bin/myst", returncode=1, output=CX43_LINE + "\n"
    )
    assert code == 0
    assert "Filtered 1 known false positive" in out


def test_main_missing_myst_is_could_not_run_not_build_failure(monkeypatch, capsys):
    code, out = _run_main(monkeypatch, capsys, which=None)
    assert code == 2
    assert "myst is not installed" in out
