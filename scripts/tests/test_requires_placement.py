"""A Module that is not a class may state a requirement -- rulings.md D209.

THE CONTROL IS THE OLD RULE. Until 2026-10-20 check-spec-schema.py rejected a
module-level `requires:` on anything no other source refines. These assert the
rejection is gone AND that the rest of the entry is still validated, because a
rule removed too widely looks exactly like a rule removed correctly.
"""
import importlib.util as _u
import subprocess
import sys
import textwrap
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
_s = _u.spec_from_file_location("css", REPO / "scripts" / "check-spec-schema.py")
css = _u.module_from_spec(_s)
_s.loader.exec_module(css)

LEAF = """\
    module: leaf
    type: ColorReporter
    title: Leaf
    inputs: {}
    process_steps: []
    requires:
      - id: transcribe[pT7]
        why: It is transcribed only where this promoter is driven.
    """


def _run(tmp_path, body, slug="leaf"):
    d = tmp_path / "docs" / "modules" / slug
    d.mkdir(parents=True)
    (d / "spec.yml").write_text(textwrap.dedent(body))
    for f in ("check-spec-schema.py", "orders.py", "spec-yml-schema.yml"):
        (tmp_path / "scripts").mkdir(exist_ok=True)
        (tmp_path / "scripts" / f).write_text((REPO / "scripts" / f).read_text())
    (tmp_path / "docs" / "type-order.yml").write_text(
        (REPO / "docs" / "type-order.yml").read_text())
    r = subprocess.run([sys.executable, str(tmp_path / "scripts" / "check-spec-schema.py")],
                       capture_output=True, text=True, cwd=tmp_path)
    return r.stdout + r.stderr


def test_a_leaf_may_require_an_operation(tmp_path):
    """Nothing refines `leaf`, and that is no longer a reason to reject it."""
    out = _run(tmp_path, LEAF)
    assert "requires-on-a-non-class" not in out
    assert "strengthens nothing" not in out


def test_the_placement_function_is_gone(tmp_path):
    assert not hasattr(css, "requires_placement_findings")


def test_the_entry_is_still_validated(tmp_path):
    """THE CONTROL. A malformed id must still be rejected -- the rule was removed,
    not the key's validation."""
    out = _run(tmp_path, LEAF.replace("transcribe[pT7]", "Transcribe Badly!"))
    assert "requires" in out and ("⛔️" in out or "does not match" in out)
