"""Pin scripts/check-page-layering.py: which direction it reads, and what it exempts.

The rule is that a Module page may point downstream but must not depend
downstream (style-guide/principles.md). The check is only useful if it tells
the two axes apart: `refines:` is abstraction and `inputs:` is composition, and
a subclass that also takes its parent as an input is the abstraction axis, not
a finding. That case is live in the corpus, so it is pinned here.

These build their graphs in memory, so they need neither the corpus nor a
checkout of it.
"""

import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-page-layering.py"


def _load():
    spec = importlib.util.spec_from_file_location("check_page_layering", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cpl = _load()


def src(module, refines=None, inputs=()):
    """A source whose inputs name other modules by page."""
    doc = {"module": module, "title": module, "process_steps": [],
           "inputs": {i: {"title": i, "page": f"../{i}/spec.md"} for i in inputs}}
    if refines:
        doc["refines"] = refines
    return doc


def run(sources, pages, tmp_path):
    """Write the pages under a fake docs/modules/ and check them."""
    root = tmp_path / "docs" / "modules"
    for m in sources:
        (root / m).mkdir(parents=True, exist_ok=True)
        (root / m / "spec.md").write_text(pages.get(m, "# Overview\n"))
    cpl.MODULES = str(root)
    cpl.REPO = str(tmp_path)
    paths = [str(root / m / "spec.md") for m in pages]
    return cpl.findings(sources, *cpl.graph(sources), paths)


def test_a_link_to_a_consumer_outside_overview_is_reported(tmp_path):
    # cell takes membrane, so membrane must not explain itself through cell
    S = {"membrane": src("membrane"), "cell": src("cell", inputs=["membrane"])}
    out = run(S, {"membrane": "# Expected Behavior\n\nUsed in [Cell](../cell/spec.md).\n"}, tmp_path)
    assert len(out) == 1
    path, line, section, target, text = out[0]
    assert section == "Expected Behavior" and target == "cell" and text == "Cell"


def test_the_overview_pointer_sentence_is_exempt(tmp_path):
    S = {"membrane": src("membrane"), "cell": src("cell", inputs=["membrane"])}
    out = run(S, {"membrane": "# Overview\n\nComposes into [Cell](../cell/spec.md).\n"}, tmp_path)
    assert out == []


def test_implementations_and_credits_are_left_to_their_own_checks(tmp_path):
    S = {"membrane": src("membrane"), "cell": src("cell", inputs=["membrane"])}
    page = ("# Implementations\n\n- [Cell](../cell/spec.md)\n\n"
            "# Credits\n\nSee [Cell](../cell/spec.md).\n")
    assert run(S, {"membrane": page}, tmp_path) == []


def test_pointing_upstream_is_never_a_finding(tmp_path):
    # the consumer naming what it is built from is the right direction
    S = {"membrane": src("membrane"), "cell": src("cell", inputs=["membrane"])}
    out = run(S, {"cell": "# Reference Composition\n\nTakes [Membrane](../membrane/spec.md).\n"}, tmp_path)
    assert out == []


def test_a_class_listing_a_member_is_the_other_axis(tmp_path):
    S = {"gel": src("gel"), "gel-lga": src("gel-lga", refines="gel")}
    out = run(S, {"gel": "# Members\n\n- [Gel: LGA](../gel-lga/spec.md)\n"}, tmp_path)
    assert out == []


def test_a_subclass_that_also_consumes_its_parent_is_still_the_other_axis(tmp_path):
    # live in the corpus: sensor-cytosol refines cytosol AND takes it as an input.
    # Composition alone would call the class's Members row a downstream link.
    S = {"cytosol": src("cytosol"),
         "sensor-cytosol": src("sensor-cytosol", refines="cytosol", inputs=["cytosol"])}
    page = "# Reference Composition\n\n| [Sensor Cytosol](../sensor-cytosol/spec.md) | a Cytosol with a Detector |\n"
    assert run(S, {"cytosol": page}, tmp_path) == []


def test_it_reads_through_the_chain_not_just_one_hop(tmp_path):
    S = {"lipid": src("lipid"),
         "membrane": src("membrane", inputs=["lipid"]),
         "cell": src("cell", inputs=["membrane"])}
    out = run(S, {"lipid": "# Expected Behavior\n\nIn [Cell](../cell/spec.md).\n"}, tmp_path)
    assert len(out) == 1 and out[0][3] == "cell"


def test_a_generated_block_is_not_the_authors_prose(tmp_path):
    S = {"membrane": src("membrane"), "cell": src("cell", inputs=["membrane"])}
    page = ("# Reference Composition\n\n<!-- gen:composition-diagram -->\n"
            "[Cell](../cell/spec.md)\n<!-- /gen:composition-diagram -->\n")
    assert run(S, {"membrane": page}, tmp_path) == []


def test_a_cycle_in_refines_does_not_hang(tmp_path):
    S = {"a": src("a", refines="b"), "b": src("b", refines="a")}
    run(S, {"a": "# Overview\n"}, tmp_path)  # returns rather than looping


def test_it_never_blocks():
    """The exit code is 0 whatever it finds; the rule has a backlog behind it."""
    import inspect
    body = inspect.getsource(cpl.main)
    assert "return 1" not in body and body.rstrip().endswith("return 0")
