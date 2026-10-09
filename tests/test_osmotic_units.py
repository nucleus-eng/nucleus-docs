"""Known answers for scripts/check-osmotic-units.py."""
import importlib.util
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "check-osmotic-units.py"
spec = importlib.util.spec_from_file_location("check_osmotic_units", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def make(tmp_path, text, ledger):
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "a.md").write_text(text)
    led = tmp_path / "ledger.yml"
    led.write_text(ledger)
    return ["--root", str(tmp_path), "--ledger", str(led)]


LISTED = 'unrecorded:\n  - {file: docs/a.md, figure: "920", count: 1}\n'


def test_a_listed_figure_passes(tmp_path, capsys):
    assert mod.main(make(tmp_path, "About 920 mOsm.\n", LISTED)) == 0


def test_a_new_bare_figure_fails(tmp_path, capsys):
    assert mod.main(make(tmp_path, "About 920 mOsm and 1180 mOsm.\n", LISTED)) == 1
    assert "1180" in capsys.readouterr().out


def test_a_second_copy_of_a_listed_figure_fails(tmp_path, capsys):
    assert mod.main(make(tmp_path, "920 mOsm here, 920 mOsm there.\n", LISTED)) == 1


def test_a_figure_with_a_denominator_is_not_bare(tmp_path, capsys):
    assert mod.main(make(tmp_path, "920 mOsm/L and 100 mOsm/kg.\n", "unrecorded: []\n")) == 0


def test_a_stale_entry_is_reported_and_does_not_fail(tmp_path, capsys):
    assert mod.main(make(tmp_path, "920 mOsm/L.\n", LISTED)) == 0
    assert "Remove or lower" in capsys.readouterr().out


def test_another_denominator_fails(tmp_path, capsys):
    assert mod.main(make(tmp_path, "920 mOsm/mL.\n", "unrecorded: []\n")) == 1


def test_reading_no_files_is_not_a_pass(tmp_path, capsys):
    (tmp_path / "docs").mkdir()
    led = tmp_path / "ledger.yml"
    led.write_text("unrecorded: []\n")
    assert mod.main(["--root", str(tmp_path), "--ledger", str(led)]) == 2


def test_the_corpus_is_listed():
    assert mod.main([]) == 0
