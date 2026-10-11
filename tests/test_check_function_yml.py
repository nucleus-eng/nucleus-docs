"""Pin scripts/check-function-yml.py: each rule against a block whose answer is known.

The checker compares a function.yml with the signature's Interface block. A comparison that
never fires reads the same as one that passes, so every rule here has a case that must fail
as well as one that must pass. The block below is a trimmed copy of the real one, in the
real forms: a one-line declaration, a two-line declaration, change lines under a heading and
continuation lines, a refinement stated in the profile, and a refinement implied by the stem.
"""

import importlib.util
import textwrap
from pathlib import Path

import yaml

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-function-yml.py"
_spec = importlib.util.spec_from_file_location("check_function_yml", SCRIPT)
fy = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fy)

BLOCK = textwrap.dedent("""\
    transcribe  : Cytosol ⊞ DNA[p]            ⟶ Cytosol′ ⊞ RNA  where p is a promoter
                  Δ(Cytosol) per residue : NTP −1, PPi +1
                             per chain   : RNA +1, PPi −1              the 5′ end keeps its triphosphate
    degrade     : D ⊞ X                       ⟶ D ; imposes degradation on every X mixed with D
    degrade[NucleicAcid]
                : D ⊞ NucleicAcid             ⟶ D                        refines degrade
    degrade[RNA]
                : D ⊞ RNA                     ⟶ D                        RNases; refines degrade[NucleicAcid]
    degrade[ssrA]
                : Control ⊞ Protein[ssrA]     ⟶ Control                  ClpXP
    passive_transport
                : Pore ⊗ Membrane            ⟶ Membrane[permeable]       see below
    transport   : Pore ⊗ Membrane            ⟶ Membrane                 abstract
    degrade[PPi]
                : Cytosol ⊞ PPi               ⟶ Cytosol′                inorganic pyrophosphatase; refines degrade
                  Δ(Cytosol) per event : PPi −1, Pi +2
    translocate : Chaperone                   — undeclared
    """)

COUNTED, EXCLUDED = fy.cf.declared(BLOCK)
VALID = set(COUNTED) | {n for n, w in EXCLUDED.items() if w.startswith("refines")}
SP = fy.spans(BLOCK)


def run(tmp_path, doc, modules=("m1",)):
    for m in modules:
        (tmp_path / "mods" / m).mkdir(parents=True, exist_ok=True)
        (tmp_path / "mods" / m / "spec.md").write_text("x")
    p = tmp_path / "op" / "function.yml"
    p.parent.mkdir(exist_ok=True)
    p.write_text(yaml.safe_dump(doc))
    out, untaken = fy.check_file(p, VALID, SP, tmp_path / "mods")
    return [m for mark, m in out if mark == "⛔️"], [m for mark, m in out if mark != "⛔️"], untaken


def op(**kw):
    return {"processes": [{"process": "transcribe", **kw}]}


def test_the_change_lines_are_read_in_both_forms():
    assert fy.change_lines(SP["transcribe"]) == {"residue": {"NTP": -1, "PPi": 1},
                                                 "chain": {"RNA": 1, "PPi": -1}}
    assert fy.change_lines(SP["degrade[PPi]"]) == {"event": {"PPi": -1, "Pi": 2}}


def test_a_matching_file_passes(tmp_path):
    bad, _, _ = run(tmp_path, op(species={"per_residue": {"NTP": -1, "PPi": 1},
                                          "per_chain": {"RNA": 1, "PPi": -1}}))
    assert bad == []


def test_a_wrong_count_fails(tmp_path):
    bad, _, _ = run(tmp_path, op(species={"per_residue": {"NTP": -1, "PPi": 2},
                                          "per_chain": {"RNA": 1, "PPi": -1}}))
    assert len(bad) == 1 and "differs from the signature" in bad[0]


def test_a_missing_species_fails(tmp_path):
    bad, _, _ = run(tmp_path, op(species={"per_residue": {"NTP": -1},
                                          "per_chain": {"RNA": 1, "PPi": -1}}))
    assert len(bad) == 1


def test_an_unknown_process_fails(tmp_path):
    bad, _, _ = run(tmp_path, {"processes": [{"process": "hydrolyse[PPi]"}]})
    assert len(bad) == 1 and "not a declared process" in bad[0]


def test_no_declared_change_is_unknown_and_never_zero(tmp_path):
    bad, info, _ = run(tmp_path, {"processes": [{"process": "degrade"}]})
    assert bad == []
    assert any("UNKNOWN, not zero" in m for m in info)


def test_species_stated_where_the_signature_has_none_fails(tmp_path):
    bad, _, _ = run(tmp_path, {"processes": [{"process": "degrade",
                                               "species": {"per_event": {"X": -1}}}]})
    assert len(bad) == 1 and "no change line" in bad[0]


def route(**kw):
    return {"processes": [{"process": "degrade", "routes": [{"id": "r", **kw}]}]}


def test_a_refinement_by_the_stem_passes(tmp_path):
    bad, _, _ = run(tmp_path, route(key="degrade[ssrA]", refines="degrade"))
    assert bad == []


def test_a_refinement_the_profile_states_passes(tmp_path):
    bad, _, _ = run(tmp_path, route(key="degrade[RNA]", refines="degrade[NucleicAcid]"))
    assert bad == []


def test_a_refinement_neither_stated_nor_stem_fails(tmp_path):
    bad, _, _ = run(tmp_path, route(key="degrade[ssrA]", refines="degrade[NucleicAcid]"))
    assert len(bad) == 1 and "neither states it nor implies it" in bad[0]


def test_a_route_change_is_compared(tmp_path):
    ok, _, _ = run(tmp_path, route(key="degrade[PPi]", refines="degrade",
                                   species={"per_event": {"PPi": -1, "Pi": 2}}))
    bad, _, _ = run(tmp_path, route(key="degrade[PPi]", refines="degrade",
                                    species={"per_event": {"PPi": -1, "Pi": 1}}))
    assert ok == [] and len(bad) == 1


def test_a_module_that_does_not_exist_fails(tmp_path):
    bad, _, _ = run(tmp_path, route(key="degrade[ssrA]", refines="degrade", realized_by=["nope"]))
    assert len(bad) == 1 and "not a Module here" in bad[0]


def test_match_name_and_docs_group_are_listed_and_not_checked(tmp_path):
    bad, _, untaken = run(tmp_path, {"processes": [{"process": "transcribe", "routes": [
        {"id": "T7", "match_name": "transcribe[pT7]", "docs_group": "g"}]}]})
    assert bad == []
    assert any("match_name" in u for u in untaken) and any("docs_group" in u for u in untaken)


NET_BLOCK = textwrap.dedent("""\
    regenerate  : R ⊞ X′                      ⟶ R ⊞ X                    abstract
    regenerate[rNTP]
                : R ⊞ rNMP|rNDP               ⟶ R ⊞ rNTP                 X ⊢ rNTP
                  Δν(R) per event : 0                                  both refinements below
                  free text under the net line
    regenerate[CP]
                : Cytosol ⊞ ADP               ⟶ Cytosol ⊞ ATP            refines regenerate[rNTP]
    """)


def run_net(tmp_path, doc):
    global VALID, SP
    saved = VALID, SP
    counted, excluded = fy.cf.declared(NET_BLOCK)
    VALID = set(counted) | {n for n, w in excluded.items() if w.startswith("refines")}
    SP = fy.spans(NET_BLOCK)
    try:
        return run(tmp_path, doc)
    finally:
        VALID, SP = saved


def test_a_net_line_is_read():
    assert fy.net_of(fy.spans(NET_BLOCK)["regenerate[rNTP]"]) == {"event": 0}


def test_species_that_sum_to_the_net_pass_and_others_fail(tmp_path):
    good = {"processes": [{"process": "regenerate[rNTP]", "net": {"per_event": 0}, "routes": [
        {"id": "cp", "key": "regenerate[CP]", "refines": "regenerate[rNTP]",
         "species": {"per_event": {"CP": -1, "ADP": -1, "creatine": 1, "ATP": 1}}}]}]}
    bad_route = {"processes": [{"process": "regenerate[rNTP]", "routes": [
        {"id": "cp", "key": "regenerate[CP]", "refines": "regenerate[rNTP]",
         "species": {"per_event": {"CP": -1, "ADP": -1, "ATP": 1}}}]}]}
    bad_net = {"processes": [{"process": "regenerate[rNTP]", "net": {"per_event": 1}}]}
    assert run_net(tmp_path, good)[0] == []
    assert any("sum to -1" in m for m in run_net(tmp_path, bad_route)[0])
    assert any("net change differs" in m for m in run_net(tmp_path, bad_net)[0])


def test_a_net_claim_where_the_signature_has_none_fails(tmp_path):
    bad, _, _ = run_net(tmp_path, {"processes": [{"process": "regenerate", "net": {"per_event": 0}}]})
    assert len(bad) == 1 and "no net line" in bad[0]


def test_a_refinement_implied_by_an_underscore_stem_passes(tmp_path):
    bad, _, _ = run(tmp_path, {"processes": [{"process": "transport", "routes": [
        {"id": "r", "key": "passive_transport", "refines": "transport"}]}]})
    assert bad == []
