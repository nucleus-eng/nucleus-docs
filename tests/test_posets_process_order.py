"""Pin the published process order to what each process says about itself.

The order was built from module steps' `process.abstract`, which are one Module's statement about
one use. It listed 9 edges while 22 processes declare `refines:` in their own spec.yml, and it put
`express` under `assemble-solution` from a single craic-cascade step while express's own spec says
`make`. The order now reads each process's own `refines:`. Two tests keep it that way.
"""
import importlib.util
import re
from pathlib import Path

import yaml

REPO = Path(__file__).parent.parent
_spec = importlib.util.spec_from_file_location("render_posets", REPO / "scripts" / "render-posets.py")
rp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rp)


def declared():
    out = {}
    for f in (REPO / "docs" / "processes").glob("*/spec.yml"):
        r = (yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("refines")
        if r:
            out[f.parent.name] = [r] if isinstance(r, str) else list(r)
    return out


def test_every_declared_process_edge_is_in_the_published_order(tmp_path):
    rp.emit_orders(tmp_path / "p.yml")
    edges = yaml.safe_load((tmp_path / "p.yml").read_text(encoding="utf-8"))["orders"]["process_refinement"]["edges"]
    for child, parents in declared().items():
        assert edges[child] == parents
    assert len(edges) >= 20


def test_function_routes_sit_in_the_same_order_and_no_name_is_in_both(tmp_path):
    rp.emit_orders(tmp_path / "p.yml")
    doc = yaml.safe_load((tmp_path / "p.yml").read_text(encoding="utf-8"))["orders"]
    assert "function_refinement" not in doc
    edges = doc["process_refinement"]["edges"]
    assert edges["degrade[ssrA]"] == ["degrade"] and edges["regenerate[CP]"] == ["regenerate[rNTP]"]
    assert edges["express"] == ["make"]
    pages = set(declared())
    routes = {k for k in edges if k not in pages}
    assert routes and not (routes & pages)


def test_no_module_step_names_a_parent_its_process_does_not():
    spec = declared()
    bad = []
    for f in (REPO / "docs" / "modules").glob("*/spec.yml"):
        for st in (yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("process_steps") or []:
            pr = st.get("process") or {}
            ab, page = pr.get("abstract"), pr.get("page") or ""
            if ab and page:
                child = re.sub(r"/[^/]+$", "", page).rsplit("/", 1)[-1]
                if spec.get(child, [None])[0] != ab:
                    bad.append((f.parent.name, st["id"], child, ab, spec.get(child)))
    assert bad == []


def test_encapsulate_and_embed_refine_hold(tmp_path):
    rp.emit_orders(tmp_path / "p.yml")
    edges = yaml.safe_load((tmp_path / "p.yml").read_text(encoding="utf-8"))["orders"]["process_refinement"]["edges"]
    assert edges["encapsulate"] == ["hold"] and edges["embed-gel"] == ["hold"]


# ---- the module order ---------------------------------------------------------------

def _orders(tmp_path):
    rp.emit_orders(tmp_path / "p.yml")
    return yaml.safe_load((tmp_path / "p.yml").read_text(encoding="utf-8"))["orders"]


def test_every_module_root_is_under_component(tmp_path):
    edges = _orders(tmp_path)["module_refinement"]["edges"]
    for root in ("analyte", "detergent", "substrate", "membrane-components", "container", "vesicle"):
        assert edges[root] == ["component"], root
    assert edges["pore"] == ["membrane-components"]
    assert edges["cell"] == ["vesicle"]     # a Cell is a type of Vesicle


def test_a_planned_module_is_in_the_order_and_stops_the_generator_when_it_gains_a_source(tmp_path, monkeypatch):
    import pytest
    assert _orders(tmp_path)["module_refinement"]["edges"]["chaperone"] == ["component"]
    real = rp.sources
    monkeypatch.setattr(rp, "sources", lambda: {**real(), "chaperone": {}})
    with pytest.raises(SystemExit):
        rp.emit_orders(tmp_path / "q.yml")
