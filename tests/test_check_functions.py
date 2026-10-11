"""Pin scripts/check-functions.py: how it counts the signature, and how it reads the hub.

The count is the part that can go wrong silently. A parser that reads only the
one-line form `name : profile` misses hydrolyse[PPi] and hydrolyse[ATP], which put the
profile on the next line, and undercounts by exactly two. A parser that ignores the
"— undeclared" marker counts translocate and finds seventeen. Either way the check
would report a gap that is not there, or hide one that is. Each rule is pinned here by
a block whose answer is known.

The last two tests run on the real files. The signature test skips when no checkout of
compositional-biology-theory is found, and a skip is not a pass.
"""

import importlib.util
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-functions.py"


def _load():
    spec = importlib.util.spec_from_file_location("check_functions", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cf = _load()


def block(text):
    return textwrap.dedent(text).strip("\n")


# ---- COVERAGE --------------------------------------------------------------------

def test_the_one_line_form_is_counted():
    counted, _ = cf.declared(block("""
        alpha       : X ⟶ Y
    """))
    assert counted == ["alpha"]


def test_the_two_line_form_is_counted():
    # hydrolyse[PPi]'s form: the name alone, the profile indented on the next line.
    counted, _ = cf.declared(block("""
        beta[Q]
                    : X ⟶ Y
                      Δ(X) per event : Q −1
    """))
    assert counted == ["beta[Q]"]


def test_both_forms_together_count_two():
    counted, _ = cf.declared(block("""
        alpha       : X ⟶ Y
        beta[Q]
                    : X ⟶ Y
    """))
    assert counted == ["alpha", "beta[Q]"]


def test_a_name_with_a_comment_and_its_profile_below_is_one_declaration():
    # degrade[Protein]'s form. Its comment holds a colon, which is not its profile.
    counted, excluded = cf.declared(block("""
        gamma[P]                         — synonym: something
                    : X ⟶ Y
    """))
    assert counted == ["gamma[P]"] and excluded == {}


def test_undeclared_is_excluded_by_its_marker():
    text = """
        alpha       : X ⟶ Y
        translocate : Chaperone                   — undeclared
    """
    counted, excluded = cf.declared(block(text))
    assert counted == ["alpha"]
    assert excluded == {"translocate": "undeclared"}
    # The exclusion rests on the marker and nothing else.
    counted, _ = cf.declared(block(text.replace("— undeclared", "")))
    assert counted == ["alpha", "translocate"]


def test_a_composite_is_excluded():
    counted, excluded = cf.declared(block("""
        alpha       : X ⟶ Y
        beta        : Y ⟶ Z
        both        = beta ∘ alpha                composite, not a generator
    """))
    assert counted == ["alpha", "beta"]
    assert excluded == {"both": "composite"}


def test_a_refinement_is_excluded_by_its_stem():
    counted, excluded = cf.declared(block("""
        report      : R ⟶ R ⊞ S
        report_color: C ⊞ T ⟶ C ⊞ K
        transport   : P ⊗ M ⟶ M
        passive_transport
                    : P ⊗ M ⟶ M
        degrade     : D ⊞ X ⟶ D
        degrade[ssrA]
                    : C ⊞ P ⟶ C
        hydrolyse[PPi]
                    : C ⊞ PPi ⟶ C
        ::          : P ⊗ P ⟶ P
    """))
    # hydrolyse[PPi] counts: no bare `hydrolyse` is declared. `::` is its own name.
    assert counted == ["report", "transport", "degrade", "hydrolyse[PPi]", "::"]
    assert excluded == {"report_color": "refines report",
                        "passive_transport": "refines transport",
                        "degrade[ssrA]": "refines degrade"}


def test_indented_lines_are_never_declarations():
    counted, _ = cf.declared(block("""
        alpha       : X ⟶ Y
                      Δ(X) per residue : NTP −1, PPi +1
                      lone : something that looks like a profile
    """))
    assert counted == ["alpha"]


def test_the_interface_block_is_found_and_the_composition_block_is_not_read():
    text = textwrap.dedent("""\
        ### Composition — attested
        ```
        multiplex[Cascade]  ×0
        encapsulate : L ⊗ S ⟶ S
        ```
        ### Interface — derived
        ```
        alpha       : X ⟶ Y
        ```
        """)
    assert cf.declared(cf.interface_block(text))[0] == ["alpha"]


# ---- HUB -------------------------------------------------------------------------

HUB = """\
---
title: Functions
---

# Functions

| Function | What it does | Page |
| --- | --- | --- |
| Alpha | Does a. | [Alpha](./alpha/main.md) |
| Beta | Does b. | To be written |
| Gamma | Does c. | No Function page: it is something you do. |
{extra}
"""


def hub(tmp_path, extra=""):
    (tmp_path / "alpha").mkdir()
    (tmp_path / "alpha" / "main.md").write_text("# Overview\n")
    p = tmp_path / "functions-main.md"
    p.write_text(HUB.format(extra=extra))
    return p


def test_the_three_states_are_counted(tmp_path):
    rows, counts, fails = cf.check_hub(hub(tmp_path))
    assert len(rows) == 3 and fails == []
    assert counts == {"page": 1, "reason": 1, "to-write": 1}


def test_a_row_in_no_state_fails(tmp_path):
    _, _, fails = cf.check_hub(hub(tmp_path, "| Delta | Does d. | soon |"))
    assert len(fails) == 1 and "Delta" in fails[0]


def test_a_link_that_does_not_resolve_fails(tmp_path):
    _, _, fails = cf.check_hub(hub(tmp_path, "| Delta | Does d. | [Delta](./delta/main.md) |"))
    assert len(fails) == 1 and "./delta/main.md" in fails[0]


# ---- MEMBERS ---------------------------------------------------------------------

SOURCES = {
    "solution": {"module": "solution"},
    "cyto": {"module": "cyto", "refines": "solution"},
    "sensor": {"module": "sensor", "refines": "cyto"},
    "a": {"module": "a", "refines": "cyto"},
    "b": {"module": "b", "refines": ["sensor"]},
    "c": {"module": "c", "refines": ["other", "cyto"]},
}
PAGE = "# Routes\n\n| Route | Realized by |\n| --- | --- |\n| R | [A](../../modules/a/spec.md), [B](../../modules/b/spec.md) |\n"


def test_members_are_the_leaves_under_the_class():
    # sensor is refined by b, so it is a class and not a member.
    assert cf.class_members("cyto", SOURCES) == {"a", "b", "c"}


def test_a_member_left_out_is_reported_until_it_has_a_reason():
    _, _, out = cf.check_members("f", PAGE, "cyto", {}, SOURCES)
    assert out == ["f: c refines cyto and the page does not list it"]
    _, _, out = cf.check_members("f", PAGE, "cyto", {"c": "never runs it"}, SOURCES)
    assert out == []


def test_a_stale_exclusion_is_reported():
    page = PAGE.replace("[B](../../modules/b/spec.md)", "[C](../../modules/c/spec.md)")
    _, _, out = cf.check_members("f", page, "cyto", {"c": "never runs it", "b": "x"}, SOURCES)
    assert "f: c is excluded in function-members.yml but the page lists it" in out


# ---- the real files --------------------------------------------------------------

def test_the_real_signature_matches_the_hub():
    path, text, h = cf.find_theory(None, "HEAD")
    if path is None:
        pytest.skip("no checkout of compositional-biology-theory; a skip is not a pass")
    counted, excluded = cf.declared(cf.interface_block(text))
    rows, _, _ = cf.check_hub(cf.HUB)
    assert len(counted) == len(rows), (h, counted)
    assert excluded.get("translocate") == "undeclared"


def test_the_corpus_has_no_failing_finding():
    p = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert p.returncode == 0, p.stdout
