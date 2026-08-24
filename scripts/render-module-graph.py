#!/usr/bin/env python3
"""
render-module-graph.py — Layer 4 of the module-integration-map pipeline.

Merges Layer 1+2 (generate-module-graph.py's JSON: composition structure +
modules-main.md metadata) with Layer 3 (module-graph-annotations.yaml:
curated status/requires/conflict/disambiguation data) and emits the
Mermaid diagram blocks the artifact needs: one system map plus one per
family, however many families FAMILY_CONFIG declares.

Node ids are UPPER_SNAKE, mechanically derived from the slug (same rule as
the vendored skill's node_id()) -- never from prose, so a text sweep can't
silently break a diagram by substituting into an id.

Colour follows the skill's own rule (references/palettes.md): colour
encodes exactly one distinction. Here that's family membership, using the
Okabe-Ito colourblind-safe palette. Status (unsupported / shelved) is
carried by a dashed border, not a second hue on the same node -- mixing
the two was a real mistake in this map's first hand-built version.

Usage:
    python3 scripts/render-module-graph.py --out-dir tmp/mermaid-blocks/
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).parent

# Okabe-Ito, from .claude/skills/mermaid-diagrams/references/palettes.md.
# One hue per family -- the single distinction colour is allowed to encode
# here (references/palettes.md: "colour encodes exactly one distinction").
# Status (unsupported/shelved) is a dashed border, never a hue.
#
# Assigned by position, not by family name, so this script carries zero
# knowledge of which families exist in any given repo -- that's entirely
# generate-module-graph.py's FAMILY_CONFIG. Six families is the practical
# ceiling: past that, a diagram is asking for hue as a second distinction
# anyway (see the skill's own "if you need more than three shades" note).
OKABE_ITO_ORDER = [
    {"fill": "#f2e6f2", "stroke": "#CC79A7", "text": "#5c2a4a"},  # purple
    {"fill": "#fbe8dc", "stroke": "#D55E00", "text": "#7a2d00"},  # orange
    {"fill": "#def5ee", "stroke": "#009E73", "text": "#00402e"},  # green
    {"fill": "#e3f0f8", "stroke": "#0072B2", "text": "#063a57"},  # blue
    {"fill": "#fdf3d9", "stroke": "#E69F00", "text": "#6b4a00"},  # yellow
    {"fill": "#f1efe8", "stroke": "#5f5e5a", "text": "#2c2c2a"},  # neutral
]
EXTERNAL_STYLE = {"fill": "none", "stroke": "#5f5e5a", "text": "#5f5e5a"}  # neutral, dashed


def family_palette(family_names) -> dict:
    ordered = sorted(family_names)
    if len(ordered) > len(OKABE_ITO_ORDER):
        sys.exit(
            f"{len(ordered)} families but only {len(OKABE_ITO_ORDER)} "
            "colourblind-safe hues -- that many families in one map is "
            "asking hue to carry a second distinction; split the map "
            "instead of adding a seventh colour."
        )
    return dict(zip(ordered, OKABE_ITO_ORDER))


def node_id(slug: str) -> str:
    return re.sub(r"[^A-Za-z0-9]", "_", slug).upper()


def run_generator(repo: Path) -> dict:
    out = subprocess.run(
        [sys.executable, str(HERE / "generate-module-graph.py")],
        cwd=repo,
        capture_output=True,
        text=True,
    )
    if out.returncode != 0:
        sys.exit(f"generate-module-graph.py failed:\n{out.stderr}")
    return json.loads(out.stdout)


def load_annotations() -> dict:
    return yaml.safe_load((HERE / "module-graph-annotations.yaml").read_text())


def title_for(slug: str, modules: dict, overrides: dict) -> str:
    if slug in overrides:
        return overrides[slug]
    return modules.get(slug, {}).get("title", slug)


class FamilyDiagram:
    """One family's flowchart -- its own members, plus any external node
    pulled in only because a requires/extra/conflict edge points at it."""

    def __init__(self, family_name: str, members: set, report: dict, ann: dict, palette: dict):
        self.family = family_name
        self.members = set(members)
        self.external = set()
        self.report = report
        self.ann = ann
        self.modules = report["modules"]
        self.palette = palette
        self.lines = []

    def _label(self, slug: str) -> str:
        return title_for(slug, self.modules, self.ann["title_overrides"]).replace('"', "'")

    def _touch_external(self, slug: str):
        if slug not in self.members and slug in self.modules:
            self.external.add(slug)

    def composition_edges(self):
        overrides = {(e["from"], e["to"]): e["status"] for e in self.ann["edge_status"]}
        edges = []
        for slug in sorted(self.members):
            for c in self.modules.get(slug, {}).get("constituents", []):
                if c not in self.members:
                    continue
                status = overrides.get((c, slug), "confirmed")
                arrow = "-.->" if status == "proposed" else "-->"
                edges.append(f"    {node_id(c)} {arrow} {node_id(slug)}")
        return edges

    def requires_edges(self):
        """Only edges whose declared `family` is this one. Membership
        alone would double-count: a module can be a real member of more
        than one family (base-cytosol is required by PURExpress modules
        but lives in the Shared family), and inferring from "either side
        is a member" pulled unrelated edges into diagrams that had
        nothing to do with them."""
        edges = []
        for r in self.ann["requires"]:
            if r["family"] != self.family:
                continue
            left, right = r["left"], r["right"]
            self._touch_external(left)
            self._touch_external(right)
            edges.append(f'    {node_id(right)} -.->|requires| {node_id(left)}')
        return edges

    def extra_edges(self):
        edges = []
        for e in self.ann["extra_edges"]:
            if e["family"] != self.family:
                continue
            self._touch_external(e["from"])
            self._touch_external(e["to"])
            style = e["style"]
            label = e["label"]
            if style == "implementation":
                edges.append(
                    f'    {node_id(e["from"])} =="{label}"==> {node_id(e["to"])}'
                )
            else:  # substitute, assay -- both read as a soft dotted claim
                edges.append(
                    f'    {node_id(e["from"])} -. "{label}" .-> {node_id(e["to"])}'
                )
        return edges

    def conflict_edges(self):
        edges = []
        for c in self.ann["conflicts"]:
            if c["family"] != self.family:
                continue
            self._touch_external(c["a"])
            self._touch_external(c["b"])
            edges.append(f'    {node_id(c["a"])} --x|"{c["label"]}"| {node_id(c["b"])}')
        return edges

    def render(self, direction="TD") -> str:
        comp = self.composition_edges()
        req = self.requires_edges()
        extra = self.extra_edges()
        conf = self.conflict_edges()

        lines = [
            "```mermaid",
            "%%{init: {'theme': 'base', 'themeVariables': "
            "{'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%",
            f"flowchart {direction}",
        ]
        for slug in sorted(self.members):
            lines.append(f'    {node_id(slug)}["{self._label(slug)}"]')
        for slug in sorted(self.external):
            lines.append(f'    {node_id(slug)}(("{self._label(slug)}"))')
        lines.append("")
        lines += comp + req + extra + conf
        lines.append("")

        pal = self.palette[self.family]
        lines.append(
            f'    classDef fam fill:{pal["fill"]},stroke:{pal["stroke"]},color:{pal["text"]};'
        )
        lines.append(
            f'    classDef ext fill:{EXTERNAL_STYLE["fill"]},'
            f'stroke:{EXTERNAL_STYLE["stroke"]},color:{EXTERNAL_STYLE["text"]},'
            f'stroke-dasharray:5 5;'
        )
        if self.members:
            lines.append("    class " + ",".join(node_id(s) for s in sorted(self.members)) + " fam;")
        if self.external:
            lines.append("    class " + ",".join(node_id(s) for s in sorted(self.external)) + " ext;")

        # Status: a dashed border on top of the family fill -- never a
        # second hue on the same node (see references/palettes.md).
        node_status = self.ann["node_status"]
        for slug in sorted(self.members | self.external):
            if slug in node_status:
                lines.append(f"    style {node_id(slug)} stroke-dasharray: 4 3")

        lines.append("```")
        return "\n".join(lines)


def render_system_map(report: dict, ann: dict, palette: dict) -> str:
    families = list(report["families"].keys())
    counts = {f: len(report["families"][f]["members"]) for f in families}
    lines = [
        "```mermaid",
        "%%{init: {'theme': 'base', 'themeVariables': "
        "{'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%",
        "flowchart LR",
    ]
    for f in families:
        name = report["families"][f]["display_name"]
        lines.append(f'    {f.upper()}["{name} &mdash; {counts[f]} module(s)"]')
    lines.append("")
    for e in ann["system_map_edges"]:
        lines.append(f'    {e["from"].upper()} -- "{e["label"]}" --> {e["to"].upper()}')
    lines.append("")
    for f in families:
        pal = palette[f]
        lines.append(
            f'    classDef {f} fill:{pal["fill"]},stroke:{pal["stroke"]},color:{pal["text"]};'
        )
        lines.append(f"    class {f.upper()} {f};")
    lines.append("```")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out-dir", type=Path, default=Path("tmp/mermaid-blocks"))
    ap.add_argument(
        "--repo-root",
        type=Path,
        default=Path(
            subprocess.run(
                ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True
            ).stdout.strip()
            or "."
        ),
    )
    args = ap.parse_args()

    report = run_generator(args.repo_root)
    ann = load_annotations()
    palette = family_palette(report["families"].keys())

    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "system-map.md").write_text(render_system_map(report, ann, palette) + "\n")

    for family, data in report["families"].items():
        direction = data.get("direction", "TD")
        diagram = FamilyDiagram(family, set(data["members"]), report, ann, palette)
        text = diagram.render(direction)
        (args.out_dir / f"{family}.md").write_text(text + "\n")
        print(f"{family}: {len(diagram.members)} member(s), {len(diagram.external)} external ref(s)")

    print(f"\nwritten to {args.out_dir}")


if __name__ == "__main__":
    main()
