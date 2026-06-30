"""Executable tests for Vale style rules.

Each annotated line in styles/tests/*.md becomes one pytest case.
Annotation grammar (trailing HTML comments):

  <!-- vale-expect: rule1, rule2 -->  — exactly these rules must fire (set equality)
  <!-- vale-clean -->                  — no rule may fire
  <!-- vale-xfail: rule (reason) -->  — rule fires today but SHOULD be clean (known false positive)
  <!-- vale-miss: rule (reason) -->   — rule SHOULD fire but doesn't today (known detection gap)

vale-xfail and vale-miss both compile to xfail(strict=True): if the rule is later fixed, the
unexpected pass (XPASS) fails CI, prompting the fixture annotation to be updated.
"""

import re
from pathlib import Path

import pytest

FIXTURE_DIR = Path(__file__).parent.parent / "styles" / "tests"

_ANNOTATION_RE = re.compile(r"<!--\s*vale-(expect|clean|xfail|miss)[:\s]")
_RULES_REASON_RE = re.compile(r"^(.+?)(?:\s*\(([^)]*)\))?\s*$")


def _parse_rules_and_reason(text):
    m = _RULES_REASON_RE.match(text.strip())
    if not m:
        return frozenset(), None
    rules = frozenset(r.strip() for r in m.group(1).split(","))
    return rules, m.group(2)


def _collect_cases():
    cases = []
    for path in sorted(FIXTURE_DIR.glob("*.md")):
        for lineno, line in enumerate(path.read_text().splitlines(), start=1):
            m = re.search(r"<!--\s*vale-expect:\s*(.+?)\s*-->", line)
            if m:
                rules, _ = _parse_rules_and_reason(m.group(1))
                cases.append(pytest.param(
                    path, lineno, rules,
                    id=f"{path.name}:{lineno}:expect",
                ))
                continue

            if re.search(r"<!--\s*vale-clean\s*-->", line):
                cases.append(pytest.param(
                    path, lineno, frozenset(),
                    id=f"{path.name}:{lineno}:clean",
                ))
                continue

            m = re.search(r"<!--\s*vale-xfail:\s*(.+?)\s*-->", line)
            if m:
                rules, reason = _parse_rules_and_reason(m.group(1))
                reason = reason or "known false positive"
                cases.append(pytest.param(
                    path, lineno, frozenset(),
                    id=f"{path.name}:{lineno}:xfail:{'+'.join(sorted(rules))}",
                    marks=pytest.mark.xfail(
                        strict=True,
                        reason=f"{reason} — fix rule then change annotation to vale-clean",
                    ),
                ))
                continue

            m = re.search(r"<!--\s*vale-miss:\s*(.+?)\s*-->", line)
            if m:
                rules, reason = _parse_rules_and_reason(m.group(1))
                reason = reason or "known detection gap"
                cases.append(pytest.param(
                    path, lineno, rules,
                    id=f"{path.name}:{lineno}:miss:{'+'.join(sorted(rules))}",
                    marks=pytest.mark.xfail(
                        strict=True,
                        reason=f"{reason} — fix rule then change annotation to vale-expect",
                    ),
                ))

    return cases


@pytest.mark.parametrize("fixture_path,lineno,expected", _collect_cases())
def test_vale_line(fixture_path, lineno, expected, vale_results):
    actual = vale_results[fixture_path].get(lineno, set())
    assert expected == actual


def test_all_content_lines_annotated():
    """Every non-blank, non-header line in each fixture must carry a vale annotation."""
    issues = []
    for path in sorted(FIXTURE_DIR.glob("*.md")):
        for lineno, line in enumerate(path.read_text().splitlines(), start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if not _ANNOTATION_RE.search(line):
                issues.append(f"  {path.name}:{lineno}: {stripped[:70]}")
    assert not issues, (
        "Unannotated content lines — add vale-expect/vale-clean/vale-xfail/vale-miss:\n"
        + "\n".join(issues)
    )
