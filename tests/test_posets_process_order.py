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
    assert edges == dict(sorted(declared().items()))
    assert len(edges) >= 20


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
