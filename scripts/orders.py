#!/usr/bin/env python3
"""The published orders, read once, by every checker that needs them.

WHY THIS EXISTS. Four sites across two checkers opened docs/type-order.yml and
each decided for itself what membership meant. Two of them read `edges` alone,
which is keyed by child, so a node that refines nothing and is refined by
nothing was invisible -- nine of forty-one Processes at the time. Two of them
read the GENERATED docs/type-system.posets.yml, which is built from the very
`refines:` values they were checking, so a typo invented its own node and
passed. Both defects were found on 2026-10-12, one of them twice, because the
fix landed in one file and not in the other.

THE AUTHORITY IS docs/type-order.yml, published from the theory corpus by
scripts/publish-type-order.py. It is not derived from these sources, which is
the whole point: a checker must not validate a source against a file generated
from that source.

MEMBERSHIP IS `nodes` UNION THE EDGE ENDPOINTS. `nodes` states it; the union is
belt and braces for an order published before `nodes` existed.

WHAT IS DELIBERATELY NOT HERE: anything that decides whether a REQUIREMENT is
discharged in a composite. That depends on what shares a compartment and is
computed from the step graph, never written down -- scripts/spec-yml-schema.yml
says so under `provides:`, and says there must be no key for it. This module
answers questions about the ORDER. Dispatch is the caller's.
"""
import os

import yaml

_CACHE = {}
_ALIAS_CACHE = {}


def load(repo):
    """The parsed docs/type-order.yml for `repo`, or an empty order if absent.

    AN ABSENT ORDER FILE DEGRADES TO ACCEPTING ANYTHING, which is stated rather
    than silent: callers that care should check `is_empty`.
    """
    repo = os.path.abspath(repo)
    if repo not in _CACHE:
        path = os.path.join(repo, "docs", "type-order.yml")
        try:
            with open(path, encoding="utf-8") as fh:
                doc = yaml.safe_load(fh) or {}
        except FileNotFoundError:
            doc = {}
        _CACHE[repo] = doc.get("orders", {}) or {}
    return _CACHE[repo]


def aliases(repo):
    """Flat spellings for type nodes whose own name carries a bracket.

    AN OPERATION ID CANNOT SPELL A BRACKETED TYPE. scripts/spec-yml-schema.yml
    matches a bracket against `[A-Za-z0-9]+(,[A-Za-z0-9]+)*`, so `degrade[DNA[linear]]`
    is invalid by construction and a type named `DNA[linear]` has no spelling inside
    an operation id. Three sources write `degrade[linearDNA]`; the order publishes
    `DNA[linear]`. docs/type-order.yml carries the map that joins them.

    Absent in an order published before the map existed, which degrades to the old
    behaviour: the flat name resolves to nothing and the caller reports no node.
    """
    repo = os.path.abspath(repo)
    if repo not in _ALIAS_CACHE:
        path = os.path.join(repo, "docs", "type-order.yml")
        try:
            with open(path, encoding="utf-8") as fh:
                doc = yaml.safe_load(fh) or {}
        except FileNotFoundError:
            doc = {}
        _ALIAS_CACHE[repo] = {str(k): str(v) for k, v in (doc.get("bracket_aliases") or {}).items()}
    return _ALIAS_CACHE[repo]


def _one(orders, key):
    return (orders.get(key) or {}) if orders else {}


def nodes(orders, key):
    """Every member of one order: `nodes`, plus both ends of every edge."""
    o = _one(orders, key)
    out = {str(x) for x in (o.get("nodes") or [])}
    for child, ps in (o.get("edges") or {}).items():
        out.add(str(child))
        out.update(str(x) for x in (ps or []))
    return out


def type_nodes(orders):
    return nodes(orders, "type_refinement")


def process_nodes(orders):
    return nodes(orders, "process_refinement")


def parents(orders, key, child):
    return [str(x) for x in ((_one(orders, key).get("edges") or {}).get(child) or [])]


def ancestors(orders, key, t, _seen=None):
    """Every type `t` refines, transitively. `t` itself is not included."""
    seen = set() if _seen is None else _seen
    for p in parents(orders, key, t):
        if p not in seen:
            seen.add(p)
            ancestors(orders, key, p, seen)
    return seen


def refines(orders, key, a, b):
    """True when `a` is `b` or refines it, transitively."""
    return a == b or b in ancestors(orders, key, a)


def operation(name):
    """`transcribe[pT7]` -> (`transcribe`, `pT7`); a bare name has no restriction."""
    op, _, rest = str(name).partition("[")
    return op, (rest.rstrip("]") or None)


def meets(orders, provided, required, alias=None):
    """Whether a provider of `provided` meets a requirement for `required`.

    SATISFACTION IS CONTRAVARIANT, and this is the rule scripts/spec-yml-schema.yml
    states under `provides:`: the bracket sits in INPUT position, so a provider
    meets a requirer when the operations are the same word AND the provider's
    type is at least as WIDE as the requirer's. Narrowing a bracket makes a
    capability do LESS, never more.

    A BARE REQUIREMENT DEMANDS NOTHING and is met by any provider of that
    operation. It is not the top type: `requires: degrade` is met by
    `degrade[RNA]`, while `requires: degrade[NucleicAcid]` is not.

    THE PREVIOUS IMPLEMENTATION WAS STRING EQUALITY. collate-conditions.py's
    own meets() compared brackets with `==`, and of the five worked examples the
    schema gives, four agreed with it and the fifth did not -- the fifth being
    the only one that needs the order at all. The four that passed are decidable
    without ever opening a poset. A green run that was never the check.
    """
    alias = alias or {}
    pop, pr = operation(provided)
    rop, rr = operation(required)
    if pop != rop:
        return False
    if rr is None:
        return True
    if pr is None:
        return False
    # A FLAT SPELLING IS RESOLVED BEFORE THE LOOKUP, 2026-10-12. `linearDNA` is how
    # three sources write the node the order calls `DNA[linear]`, because an
    # operation id may not nest a bracket. Resolving here rather than in each caller
    # is the same argument this module exists for: four readers of one file each
    # decided membership for itself and two of them were wrong.
    pr, rr = alias.get(pr, pr), alias.get(rr, rr)
    return refines(orders, "type_refinement", rr, pr)
