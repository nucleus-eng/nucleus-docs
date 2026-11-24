"""Tests for scripts/add-heading-labels.py.

Known-answer fixture: a page in a directory called `widget` with one labeled
heading, one bare heading, a duplicate heading, a heading inside a code fence,
a tab-set and an admonition, a generated "Supported by" section, and a
heading with punctuation. The expected output is written out by hand.
"""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "add-heading-labels.py"
spec = importlib.util.spec_from_file_location("add_heading_labels", SCRIPT)
ahl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ahl)

PAGE = """\
---
title: Widget
---

(widget-overview)=
# Overview

Text.

# Requirements

## Assay (5 mM).

```markdown
# Not a heading
```

::::{tab-set}
:::{tab-item} A
# Inside a tab
:::
::::

:::{note}
# Inside a note
:::

# Credits

# Supported by

Cards.
"""

EXPECTED = """\
---
title: Widget
---

(widget-overview)=
# Overview

Text.

(widget-requirements)=
# Requirements

(widget-assay-5-mm)=
## Assay (5 mM).

```markdown
# Not a heading
```

::::{tab-set}
:::{tab-item} A
# Inside a tab
:::
::::

:::{note}
# Inside a note
:::

(widget-credits)=
# Credits

# Supported by

Cards.
"""


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """Point the script at a throwaway repo so it never touches real pages."""
    (tmp_path / "docs" / "widget").mkdir(parents=True)
    monkeypatch.setattr(ahl, "REPO", tmp_path)
    monkeypatch.setattr(ahl, "DOCS", tmp_path / "docs")
    return tmp_path


def page_path(repo):
    return repo / "docs" / "widget" / "spec.md"


def test_known_answer(repo, capsys):
    p = page_path(repo)
    p.write_text(PAGE, encoding="utf-8")
    assert ahl.main([str(p)]) == 0
    assert p.read_text(encoding="utf-8") == EXPECTED


def test_idempotent(repo):
    p = page_path(repo)
    p.write_text(PAGE, encoding="utf-8")
    ahl.main([str(p)])
    first = p.read_text(encoding="utf-8")
    assert ahl.main([str(p)]) == 0
    assert p.read_text(encoding="utf-8") == first


def test_check_fails_then_passes(repo):
    p = page_path(repo)
    p.write_text(PAGE, encoding="utf-8")
    assert ahl.main(["--check", str(p)]) == 1
    assert p.read_text(encoding="utf-8") == PAGE  # --check writes nothing
    ahl.main([str(p)])
    assert ahl.main(["--check", str(p)]) == 0


def test_existing_label_kept(repo):
    p = page_path(repo)
    p.write_text("(custom-name)=\n# Overview\n", encoding="utf-8")
    ahl.main([str(p)])
    assert p.read_text(encoding="utf-8") == "(custom-name)=\n# Overview\n"


def test_duplicate_heading_reports_and_writes_nothing(repo, capsys):
    p = page_path(repo)
    body = "# Notes\n\ntext\n\n# Notes\n"
    p.write_text(body, encoding="utf-8")
    assert ahl.main([str(p)]) == 1
    assert p.read_text(encoding="utf-8") == body
    assert "(widget-notes)=" in capsys.readouterr().out


def test_collision_with_existing_label_elsewhere(repo):
    other = repo / "docs" / "widget" / "other.md"
    other.write_text("(widget-notes)=\n# Notes\n", encoding="utf-8")
    p = page_path(repo)
    p.write_text("# Notes\n", encoding="utf-8")
    assert ahl.main([str(p)]) == 1
    assert p.read_text(encoding="utf-8") == "# Notes\n"


def test_excluded_hub_untouched(repo, monkeypatch):
    hub = repo / "docs" / "widget" / "hub-main.md"
    hub.write_text("# Overview\n", encoding="utf-8")
    monkeypatch.setitem(ahl.EXCLUDED_PAGES, "docs/widget/hub-main.md", "hub")
    assert ahl.main([str(hub)]) == 0
    assert hub.read_text(encoding="utf-8") == "# Overview\n"


def test_leading_digit_heading(repo):
    p = page_path(repo)
    p.write_text("## 1. Prepare Lipids\n", encoding="utf-8")
    ahl.main([str(p)])
    assert p.read_text(encoding="utf-8").startswith("(widget-1-prepare-lipids)=\n")
