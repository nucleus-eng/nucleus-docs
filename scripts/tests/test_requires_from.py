"""`from:` takes a requirement's bracket from an operand's type -- rulings.md D211.

THE CONTROL IS THE SECOND PROMOTER. Jon: "you can imagine systems requiring two
(or many) distinct promoters and have the modules match the correct `P1` vs
`P2`". So the test carries two constructs on two promoters against a cytosol
that drives one, and asserts the walker meets the first and not the second. A
resolver that ignored `from:` and compared bare `transcribe` would meet both.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_check_requirements as _t  # noqa: E402
from test_check_requirements import ORDER, mod  # noqa: E402
cr = _t.cr

ORDER2 = {**ORDER, "orders": {**ORDER["orders"], "type_refinement": {"edges": {
    **ORDER["orders"]["type_refinement"]["edges"],
    "Promoter": ["Component"], "pT7": ["Promoter"], "sigma70": ["Promoter"],
    "DNA[linear, pT7]": ["DNA"], "DNA[linear, sigma70]": ["DNA"], "DNA": ["Component"],
}}}}


def two_promoters(provides):
    return [
        mod("cytosol", type="Cytosol", provides=provides),
        mod("gate", type="Component",
            inputs={"dna-a": {"title": "A", "type": "DNA[linear, pT7]"},
                    "dna-b": {"title": "B", "type": "DNA[linear, sigma70]"}},
            requires=[{"id": "transcribe", "from": "dna-a", "why": "its own promoter"},
                      {"id": "transcribe", "from": "dna-b", "why": "its own promoter"}]),
        mod("system", type="Cascade",
            inputs={"cytosol": {"title": "C", "page": "../cytosol/spec.md"},
                    "gate": {"title": "G", "page": "../gate/spec.md"}},
            process_steps=[{"id": "mix", "process": {"title": "Mix", "page": None},
                            "operator": "mixing", "operands": ["cytosol", "gate"],
                            "produces": {"id": "system", "title": "S", "page": None}}]),
    ]


def _corpus(tmp_path, provides):
    import test_check_requirements as t
    return cr.Corpus.load(t.tree(tmp_path, modules=two_promoters(provides), order=ORDER2))


def test_the_bracket_comes_from_the_operand(tmp_path):
    """Each requirement resolves to ITS OWN operand's promoter."""
    c = _corpus(tmp_path, ["transcribe[pT7]"])
    ids = [e["id"] for e, _ in c.effective("gate", "requires")]
    assert ids == ["transcribe[pT7]", "transcribe[sigma70]"]


def test_an_unresolvable_from_leaves_the_id_bare(tmp_path):
    """THE CONTROL for silent dropping. A broken reference must not become a pass."""
    mods = two_promoters(["transcribe[pT7]"])
    mods[1]["requires"][0]["from"] = "nosuch"
    import test_check_requirements as t
    c = cr.Corpus.load(t.tree(tmp_path, modules=mods, order=ORDER2))
    ids = [e["id"] for e, _ in c.effective("gate", "requires")]
    assert ids[0] == "transcribe", "a bad `from` must leave the id bare, not drop it"


def test_a_type_with_no_promoter_axis_leaves_the_id_bare(tmp_path):
    """THE CONTROL for picking the wrong bracket member. `linear` is not a Promoter."""
    mods = two_promoters(["transcribe[pT7]"])
    mods[1]["inputs"]["dna-a"]["type"] = "DNA[linear]"
    import test_check_requirements as t
    c = cr.Corpus.load(t.tree(tmp_path, modules=mods, order=ORDER2))
    ids = [e["id"] for e, _ in c.effective("gate", "requires")]
    assert ids[0] == "transcribe", "only a member refining Promoter may fill the bracket"
