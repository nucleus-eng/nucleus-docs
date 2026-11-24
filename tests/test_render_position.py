"""Tests for scripts/render-position.py.

Each case builds a small docs tree and checks the line it renders. The fixture
tree has one class page (`color-change`, the type `ColorReporter`), one Module
that refines it, one Module of a type with no page, and one Module with two
parents. A renderer that finds nothing wrong on main must be shown able to find
something wrong here.
"""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "render-position.py"
_spec = importlib.util.spec_from_file_location("render_position", SCRIPT)
rp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rp)

ORDER = """\
orders:
  type_refinement:
    nodes: [ColorReporter, Reporter, Fluorophore, Protein, Cell]
    edges:
      ColorReporter: [Reporter]
      Reporter: [Module]
module_slugs:
  color-change: ColorReporter
  reporter: Reporter
  cell: Cell
"""

SPECS = {
    "color-change": "module: color-change\ntitle: Color Change\ntype: ColorReporter\n",
    "lacz": "module: lacz\ntitle: 'Reporter: LacZ'\ntype: ColorReporter\nrefines: Protein\n",
    "degfp": "module: degfp\ntitle: deGFP\ntype: Reporter\nrefines: Fluorophore\n",
    "three": "module: three\ntitle: Three\ntype: Cell\nrefines: ['Vesicle[GUV]', 'Vesicle[liposome]']\n",
    "bare": "module: bare\ntitle: Bare\n",
}

PAGE = "---\ntitle: X\n---\n\n# Overview\n\nBody text.\n"


@pytest.fixture
def repo(tmp_path):
    (tmp_path / "docs" / "modules").mkdir(parents=True)
    (tmp_path / "docs" / "type-order.yml").write_text(ORDER)
    for slug, yml in SPECS.items():
        d = tmp_path / "docs" / "modules" / slug
        d.mkdir()
        (d / "spec.yml").write_text(yml)
        (d / "spec.md").write_text(PAGE)
    return tmp_path


def render(repo, slug):
    edges, node_of = rp.load_order(repo / "docs" / "type-order.yml")
    mods = rp.load_modules(repo / "docs" / "modules")
    return rp.line(slug, mods, edges, node_of)


def test_a_type_with_no_page_prints_as_code_not_a_link(repo):
    assert render(repo, "degfp").startswith("**Position.** Refines `Reporter` and `Fluorophore`.")


def test_a_type_with_a_page_links_to_it(repo):
    assert "[Color Change](../color-change/spec.md) and `Protein`" in render(repo, "lacz")


def test_a_class_page_refines_what_the_order_gives_its_node(repo):
    assert render(repo, "color-change").startswith("**Position.** Refines `Reporter`.")


def test_refined_by_lists_modules_under_the_class_node(repo):
    assert "Refined by [Reporter: LacZ](../lacz/spec.md)." in render(repo, "color-change")


def test_a_module_is_never_its_own_child(repo):
    d = repo / "docs" / "modules" / "cell"
    d.mkdir()
    (d / "spec.yml").write_text("module: cell\ntitle: Cell\ntype: Reporter\nrefines: Cell\n")
    refined_by = render(repo, "cell").split("Refined by")[1]
    assert "../cell/" not in refined_by
    assert "[Three](../three/spec.md)" in refined_by


def test_a_leaf_is_refined_by_nothing_declared(repo):
    assert render(repo, "lacz").endswith("Refined by nothing declared.")


def test_three_parents_read_as_a_list_with_one_and(repo):
    assert "Refines `Cell`, `Vesicle[GUV]` and `Vesicle[liposome]`." in render(repo, "three")


def test_a_module_with_no_type_is_placed_by_nothing(repo):
    assert render(repo, "bare").startswith("**Position.** Refines nothing declared.")


def test_no_link_points_at_a_page_that_does_not_exist(repo):
    import re
    pages = {p.parent.name for p in (repo / "docs" / "modules").glob("*/spec.md")}
    for slug in SPECS:
        for target in re.findall(r"\]\(\.\./([^/]+)/spec\.md\)", render(repo, slug)):
            assert target in pages


def test_insert_adds_the_block_under_overview_once(repo):
    page = repo / "docs" / "modules" / "degfp" / "spec.md"
    assert rp.insert(page, "LINE") is True
    text = page.read_text()
    assert "# Overview\n\n<!-- gen:position -->\nLINE\n<!-- /gen:position -->\n\nBody text." in text
    assert rp.insert(page, "LINE") is False


def test_embed_rewrites_a_stale_block_and_check_does_not_write(repo):
    page = repo / "docs" / "modules" / "degfp" / "spec.md"
    rp.insert(page, "OLD")
    assert rp.embed(page, "NEW", write=False) is True
    assert "OLD" in page.read_text()
    assert rp.embed(page, "NEW") is True
    assert "NEW" in page.read_text()
    assert rp.embed(page, "NEW") is False


def test_embed_reports_a_page_with_no_markers_as_none(repo):
    assert rp.embed(repo / "docs" / "modules" / "degfp" / "spec.md", "X") is None


def test_check_exits_1_on_a_stale_block_and_0_when_fresh(repo):
    page = repo / "docs" / "modules" / "degfp" / "spec.md"
    rp.insert(page, "OLD")
    assert rp.main(["--check", "docs/modules/degfp"], repo) == 1
    rp.main(["--embed", "docs/modules/degfp"], repo)
    assert rp.main(["--check", "docs/modules/degfp"], repo) == 0
