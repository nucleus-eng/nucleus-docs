"""Pin the SKIPPABLE rule in scripts/check-composition.py, and the one case it exempts.

No module source marks a step optional, so on the corpus the rule has never fired and
a run over the corpus cannot tell a working rule from one that never fires. These
tests make it fire on purpose, then plant the case it must not fire on.

The exempt case is a wash. Skipping an optional step hands its consumer the step's
operands instead of its product. Under a packing consumer that is usually several
loose things where one bounded thing was expected, which is the finding. A wash keeps
its vesicles' boundary and only replaces the solution outside, so skipping it hands
the consumer the unwashed vesicles: still one bounded thing. A process that says so
declares `keeps_boundary: true` in its own source, and the rule reads it there.

The module sources are built in memory. The process sources are written to disk,
because the rule finds them through each step's `process.page`, as a real source does.
"""

import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-composition.py"


def _load():
    spec = importlib.util.spec_from_file_location("check_composition", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cc = _load()


def tree(tmp_path, processes):
    """A fake docs/ with one module directory and the named process sources.

    `processes` maps a process directory to the text of its spec.yml, or to None for a
    directory with a page and no source.
    """
    for name, text in processes.items():
        d = tmp_path / "docs" / "processes" / name
        d.mkdir(parents=True)
        (d / "main.md").write_text("# Overview\n")
        if text is not None:
            (d / "spec.yml").write_text(text)
    mod = tmp_path / "docs" / "modules" / "m"
    mod.mkdir(parents=True)
    return mod


def page(name):
    return {"title": name, "page": f"../../processes/{name}/main.md"}


def source(wash_process, consumer_operator="packing", **consumer):
    """An optional step whose product the next step consumes."""
    return {"module": "m", "title": "M", "process_steps": [
        {"id": "wash", "optional": True, "process": wash_process,
         "operator": "packing", "operands": ["vesicles", "fresh"],
         "produces": {"id": "washed", "title": "Washed"}},
        {"id": "embed", "process": page("embed"), "operator": consumer_operator,
         "operands": ["washed", "gel"], "produces": {"id": "m", "title": "M"},
         **consumer},
    ]}


KEEPS = "process: wash\ntitle: Wash\nkeeps_boundary: true\n"
PLAIN = "process: wash\ntitle: Wash\n"


def test_the_rule_fires_on_a_packing_consumer(tmp_path):
    # The known answer the corpus cannot give: an optional step under packing.
    mod = tree(tmp_path, {"wash": PLAIN, "embed": None})
    out = cc.skippable(source(page("wash")), mod)
    assert len(out) == 1
    assert "embed packs its product 'washed'" in out[0]
    assert "2 loose operands" in out[0]


def test_a_step_that_keeps_the_boundary_does_not_fire(tmp_path):
    mod = tree(tmp_path, {"wash": KEEPS, "embed": None})
    assert cc.skippable(source(page("wash")), mod) == []


def test_false_is_not_true(tmp_path):
    mod = tree(tmp_path, {"wash": "process: wash\ntitle: Wash\nkeeps_boundary: false\n",
                          "embed": None})
    assert len(cc.skippable(source(page("wash")), mod)) == 1


def test_a_process_with_no_source_still_fires(tmp_path):
    # Not finding the declaration is not the same as finding it true.
    mod = tree(tmp_path, {"wash": None, "embed": None})
    assert len(cc.skippable(source(page("wash")), mod)) == 1


def test_a_chain_keeps_the_boundary_only_if_every_link_does(tmp_path):
    mod = tree(tmp_path, {"wash": KEEPS, "spin": "process: spin\ntitle: Spin\n",
                          "embed": None})
    chain = {"title": "Wash, then spin",
             "composed_of": [page("wash"), page("spin")]}
    assert len(cc.skippable(source(chain), mod)) == 1
    both = tree(tmp_path / "b", {"wash": KEEPS, "spin": KEEPS, "embed": None})
    assert cc.skippable(source(chain), both) == []


def test_an_abstract_with_no_page_is_followed(tmp_path):
    mod = tree(tmp_path, {"wash": KEEPS, "embed": None})
    assert cc.skippable(source({"title": "Wash", "page": None, "abstract": "wash"}),
                        mod) == []


def test_a_mixing_consumer_does_not_fire(tmp_path):
    mod = tree(tmp_path, {"wash": PLAIN, "embed": None})
    assert cc.skippable(source(page("wash"), consumer_operator="mixing"), mod) == []


def test_operator_pairs_decide_for_the_product(tmp_path):
    # The step is labeled mixing, but the pair holding the product is packed.
    mod = tree(tmp_path, {"wash": PLAIN, "embed": None})
    pairs = [{"operands": ["washed", "gel"], "operator": "packing"}]
    out = cc.skippable(source(page("wash"), consumer_operator="mixing",
                              operator_pairs=pairs), mod)
    assert len(out) == 1
