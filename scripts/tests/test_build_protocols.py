"""Tests for the link handling in scripts/build-protocols.py.

The lab-ready PDF copied checklist lines as written, so a relative link such as
`../assemble-base-cytosol/main.md` became a PDF link to a path on the reader's
own disk (#277). These pin the rewrite: a page link becomes its published URL,
any other relative target is reduced to its text, and absolute links and
anchors are left alone.
"""

import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "build-protocols.py"
_spec = importlib.util.spec_from_file_location("build_protocols", SCRIPT)
bp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bp)

BASE = "https://docs.nucleus.engineering"
PAGE = Path("docs/processes/assemble-base-cell/main.md")


def rewrite(text, base_url=BASE, page=PAGE):
    return bp.absolutize_links(text, page, base_url)


def test_relative_page_link_becomes_its_published_url():
    text = "(see [Assemble Base Cytosol](../assemble-base-cytosol/main.md) for an example)"
    assert rewrite(text) == (
        f"(see [Assemble Base Cytosol]({BASE}/docs/processes/assemble-base-cytosol/main) "
        "for an example)"
    )


def test_root_relative_link_and_anchor():
    text = "[deGFP](/docs/modules/reporter-degfp/spec.md#reference-composition)"
    assert rewrite(text) == (
        f"[deGFP]({BASE}/docs/modules/reporter-degfp/spec#reference-composition)"
    )


def test_link_into_a_module_from_a_process():
    text = "[Base Cytosol](../../modules/base-cytosol/spec.md)"
    assert rewrite(text) == f"[Base Cytosol]({BASE}/docs/modules/base-cytosol/spec)"


def test_absolute_links_anchors_and_images_are_untouched():
    text = ("[vendor](https://www.stemcell.com/x) [mail](mailto:build@bnext.bio) "
            "[here](#protocol) ![fig](schematic.png)")
    assert rewrite(text) == text


def test_relative_target_that_is_not_a_page_keeps_only_its_text():
    assert rewrite("[the PDF](generated/x-protocol.pdf)") == "the PDF"


def test_without_a_site_url_every_relative_link_keeps_only_its_text():
    text = "[Assemble Base Cytosol](../assemble-base-cytosol/main.md)"
    assert rewrite(text, base_url=None) == "Assemble Base Cytosol"


def test_absolute_page_path_resolves_like_a_relative_one(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    page = tmp_path / PAGE
    text = "[Assemble Base Cytosol](../assemble-base-cytosol/main.md)"
    assert rewrite(text, page=page) == (
        f"[Assemble Base Cytosol]({BASE}/docs/processes/assemble-base-cytosol/main)"
    )


def test_site_url_reads_site_dot_url(tmp_path):
    config = tmp_path / "site.yml"
    config.write_text(
        "version: 1\n"
        "project:\n"
        "  url: https://wrong.example\n"
        "site:\n"
        "  url: https://docs.nucleus.engineering/\n"
        "  nav:\n"
        "    - url: https://also.wrong\n",
        encoding="utf-8",
    )
    assert bp.site_url(config) == "https://docs.nucleus.engineering"


def test_site_url_is_none_without_the_key(tmp_path):
    config = tmp_path / "site.yml"
    config.write_text("site:\n  template: book-theme\n", encoding="utf-8")
    assert bp.site_url(config) is None
    assert bp.site_url(tmp_path / "absent.yml") is None


def test_protocol_markdown_carries_no_relative_link():
    checklist = ["- [ ] Assemble it (see [Assemble Base Cytosol](../assemble-base-cytosol/main.md))."]
    md = bp.build_protocol_markdown("Encapsulation: Phase Transfer", None, checklist,
                                    "assemble-base-cell", page=PAGE, base_url=BASE)
    assert "](../" not in md
    assert f"{BASE}/docs/processes/assemble-base-cytosol/main" in md
