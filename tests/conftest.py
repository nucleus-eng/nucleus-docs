import json
import shutil
import subprocess
from pathlib import Path

import pytest

VALE_BIN = "vale"
FIXTURE_DIR = Path(__file__).parent.parent / "styles" / "tests"


@pytest.fixture(scope="session")
def vale_available():
    if shutil.which(VALE_BIN) is None:
        pytest.skip("vale not installed; run setup.sh or see CI for install instructions")


@pytest.fixture(scope="session")
def vale_results(vale_available):
    return {p: _run_vale(p) for p in sorted(FIXTURE_DIR.glob("*.md"))}


def _run_vale(fixture_path):
    proc = subprocess.run(
        [VALE_BIN, "--output=JSON", str(fixture_path)],
        capture_output=True,
        text=True,
    )
    try:
        report = json.loads(proc.stdout or "{}")
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"vale produced non-JSON output for {fixture_path}:\n{proc.stdout[:200]}"
        ) from exc
    by_line = {}
    for entries in report.values():
        for entry in entries:
            by_line.setdefault(entry["Line"], set()).add(entry["Check"])
    return by_line
