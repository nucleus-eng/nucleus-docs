#!/usr/bin/env python3
"""Walk `requires:` and `provides:` through the orders, and report what the walk finds.

    python3 scripts/check-requirements.py            # report; always exits 0
    python3 scripts/check-requirements.py --strict   # exit 1 if there is any finding
    python3 scripts/check-requirements.py --json     # the same, as data
    python3 scripts/check-requirements.py --root DIR # a tree laid out like this repo

REPORT ONLY, BY RULING. Jon ruled on 2026-10-12: "report. write a memory that we may
want to raise that later." No workflow runs the schema checkers, so a walker that fails
would turn every open PR red over findings nobody is assigned. The count that matters is
`findings` in the last line. Drive it toward zero. `--strict` exists for the day that
ruling is raised again, and nothing runs it.

WHY THIS FILE EXISTS. scripts/spec-yml-schema.yml states rules about `requires` and
`provides`, argues for them at length, and nothing ran them. The only matcher was string
equality. String equality gets four of the schema's five worked examples right, and those
four do not need an order at all. The fifth, `requires degrade[linearDNA]` met by
`degrade[DNA]`, is the only one that does. A check that never meets the case it exists for
looks the same as one that works. So tests/test_check_requirements.py runs the real code
and a broken copy against the same assertions, and the broken copy must fail.

ONE DISPATCHER, NOT FIVE CHECKS. A requirement names an order, and `dispatch()` compares
in that order:

    operation   same operation word, then the bracket type, contravariant: a provider
                meets a requirer when the provider's type is at least as WIDE
    type        one type refines another, in the published type order
    interval    a provider's band contains the interval asked for
    within      two readings differ by a setpoint, within a tolerance

THE RULES. Each one has its own section in the report, and every section always prints.

    R1  CONTRAVARIANCE ON THE BRACKET. Every requirement is compared with every provider.
        An operation id cannot nest a bracket, so a type whose own name has one, such as
        `DNA[linear]`, is written flat, `linearDNA`. The published order's `bracket_aliases`
        says which node a flat name means, and the verdict says when an alias decided it.
    R2  INHERITANCE DOWN `refines:`. A member has what its classes require and provide.
        The walk is cycle-safe. It reports each `refines:` that ends at a node with no
        source, because nothing can flow across one.
    R3  DISCHARGE IN A COMPOSITE. A requirement is met in a composite only by a provider
        that shares its compartment. Compartments come from each step's `operator`:
        `mixing` puts the operands in one compartment, `packing` leaves each in its own.
        The answer is computed and never written down, as the schema says.
    R4  THE OTHER GUARD KINDS. `transcribe`'s guard, `p in P(cytosol)`, is `provides` and
        `requires` already, so R1 and R3 carry it. The numeric kinds are the `interval`
        and `within` comparators. This section says what the sources can reach.
    R5  A CHILD MUST NOT CONTRADICT ITS PARENT. It fires on a DENIAL and never on a
        SILENCE. A child that says nothing inherits. A stated value that differs from the
        nearest one stated above it is a contradiction, for the keys whose absence the
        schema calls undeclared. It looks up the whole chain, not only one level. For
        TYPES it reads `type_declares` in the published order: a type that is ABSENT from
        that map is silent and inherits, and `kind: none` is a claim that it declares
        nothing, so a type that claims it below a type that declares is a contradiction.
    R6  AN ENCAPSULATION'S PRODUCT STATES A VESICLE SIZE CLASS. A step whose process refines
        `encapsulate` yields a product whose `type`, or an axis it `refines`, reaches
        `Vesicle[GUV]`, `Vesicle[LUV]` or `Vesicle[SUV]`. It checks for the CLASS and never for
        a diameter: no diameter is characterized for anything in this corpus, so a rule that
        demanded one would fire on every vesicle and nothing could fix it. `Vesicle[liposome]`
        is a material, not a size. The report says whether the size came through `type` or
        through `refines`. A product with no page is a gap, because only a page can fix it.
        An abstract class, one that another source refines, is open on purpose and is skipped.

THREE ANSWERS, NEVER TWO. Every comparison returns `met`, `unmet` or `undetermined`.
`undetermined` is never a pass and never a failure. It names what was missing. A provider
that might meet a requirement is reported as undetermined, and is never read as absent.

FINDINGS AND GAPS ARE DIFFERENT. A FINDING is something wrong in the sources: a cycle, a
contradiction, a requirement that no constituent of its composite meets, a malformed id or
interval, a source that does not parse. A source that makes the walk crash is also a
finding, and the walk goes on with the rest. A GAP is something this walk could not
decide, or a fact the schema says to report and never fail, such as a requirement with no
provider anywhere in the corpus. Gaps carry their denominators, so a clean count is never
read as a clean corpus.

WHERE THE SCHEMA IS SILENT, AND WHAT THIS WALKER CHOSE. Each choice is open to a ruling.
  - A provider of a finer operation meets a bare requirement for a coarser one:
    `emit_fluorescence` meets `emit_color`, and the converse fails. The schema's own
    reason for contravariance is that the bracket sits in input position. The operation
    sits in output position, so it is covariant: capability is covariant and the argument
    is contravariant. The schema says "the same word", written before an operation order
    existed. The report labels these `operation order`, so the two readings can be told apart.
  - A list of types in a bracket is undetermined. The schema does not say whether it means
    all of them or any of them, and no source uses one. A provider with no bracket against a
    requirer with one is undetermined too: the schema does not make a bare requirement the top
    type, and a bare provider is not the top capability either. It has claimed no width.
  - `stitching` puts its operands in one compartment, as `mixing` does. That is sound, since
    one molecule is more joined than one compartment. No source uses it, the report says so,
    and so that branch has no source to test it on.
  - Compartments are the state after the last step, and no operator separates what is
    already together. A step whose process refines `purify` does separate, and one that
    refines `transport` moves cargo across a boundary that persists. Both are outside the
    model, and the report says so where they apply and does not assume otherwise. `lyse` is
    inside it: a compartment destroyed by merging upward is a join.
  - An id that two steps use is two portions of one stock, as a membrane that feeds two
    encapsulations is. The first use is the one the report asks about.
  - `operator_pairs` that contradict through the other pairs of one step are undetermined
    and not a finding. It is not ruled whether a source that lists too few pairs is wrong,
    or the shorthand is. The one real instance is `atc-cascade`, step
    `embed-photocrosslinking`, which lists 2 of the 3 pairs its own exceptions imply.
    The report names the pair.
  - A requirer that is an optional input is a gap when it is not discharged, because the
    condition applies only if it is present.
  - A requirement that nothing in the corpus can meet is one gap in R1, and R3 counts the
    composites it touches. The cause is one missing kind of source: `observe` is met by an
    assay, and this repo has no assay sources. Many findings would be one absence, copied.

WHAT IT CANNOT REACH, and the report says it each time:
  - The numeric kinds have no source to read. The schema has no key for a provider's
    band, and none for which operand of an encapsulation is the lumen.
  - A bracket type that the published order has no node for compares only to itself.
    That is the schema's own decision. The report lists each such type, and names a node
    made of the same words, as a hint it never uses.
  - A `mixing` step whose operand is already several compartments does not say which one
    joins. The walk reports it as undetermined and does not guess.
  - R6 finds a size that is missing and cannot find one that is wrong. A product that says
    `guv` while its page describes a freeze-thaw LUV passes, because the class is stated. A
    check that a process page describes the method its product's class implies would need
    more than names, and is not built.
  - A `refines:` that names a parent under docs/functions/ is reported as having no
    source, because only docs/modules and docs/processes are read.
  - An order with no `type_declares` cannot say what a type declares. R5 says so in a gap
    and finds nothing for types.

READS docs/modules/*/spec.yml, docs/processes/*/spec.yml and docs/type-order.yml, under
`--root`. It prints the files it read, because a walker that reports no findings over no
files looks the same as a clean run. It exits 2 if it finds no module source.
"""
import argparse
import contextlib
import dataclasses
import itertools
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("needs pyyaml: pip install pyyaml")

REPO = Path(__file__).resolve().parent.parent

MET, UNMET, UNDETERMINED = "met", "unmet", "undetermined"

# The schema's own pattern for an id, from `requires.items.id` and `provides.items.id`.
ID_RE = re.compile(r"^([a-z0-9]+(?:[-_][a-z0-9]+)*)(?:\[([A-Za-z0-9]+(?:,[A-Za-z0-9]+)*)\])?$")

# PROCESSES THE COMPARTMENT MODEL DOES NOT COVER. The model has three operators, and each only
# joins or keeps apart. A step whose process refines one of these does something else, so its
# operands' compartments are unknown and the report says so. Each is a named branch, and a
# branch with no source in the corpus has nothing to test it on.
OUTSIDE_THE_MODEL = {
    "purify": "separates a product from waste, which separates what was together",
    "transport": "moves cargo across a boundary that persists, so nothing merges and something ends up in another compartment",
}

# THE SIZE CLASSES OF A VESICLE. `Vesicle[liposome]` is a material, not a size, so it is not here.
# The rule checks for a class and never for a diameter: no diameter is characterized for anything in
# this corpus, so a rule that demanded one would fire on every vesicle and nothing could fix it.
VESICLE_SIZES = ("GUV", "LUV", "SUV")
ENCAPSULATE = "encapsulate"

# A DIFFERENT KIND OF CONSTANT. This one is not outside the model. `observe` names a family whose
# provider is an assay, and the provider class has no source file in this repo.
ASSAY = "observe"

# Lengths, in meters. Bands in this corpus are wavelengths, so this is all the interval
# comparator needs. A unit that is not here makes the answer undetermined.
LENGTH_UNITS = {
    "pm": 1e-12,
    "picometer": 1e-12,
    "picometers": 1e-12,
    "å": 1e-10,
    "angstrom": 1e-10,
    "angstroms": 1e-10,
    "nm": 1e-9,
    "nanometer": 1e-9,
    "nanometers": 1e-9,
    "µm": 1e-6,
    "um": 1e-6,
    "micron": 1e-6,
    "microns": 1e-6,
    "micrometer": 1e-6,
    "micrometers": 1e-6,
    "mm": 1e-3,
    "millimeter": 1e-3,
    "millimeters": 1e-3,
    "cm": 1e-2,
    "centimeter": 1e-2,
    "centimeters": 1e-2,
    "m": 1.0,
    "meter": 1.0,
    "meters": 1.0,
}


# --------------------------------------------------------------------------- #
# Verdicts, and the four comparators
# --------------------------------------------------------------------------- #


@dataclasses.dataclass(frozen=True)
class Verdict:
    status: str
    via: str
    why: str = ""
    hint: str = ""


@dataclasses.dataclass(frozen=True)
class Op:
    word: str
    types: tuple
    raw: str


def parse_op(raw):
    """`transcribe[pT7]` -> Op('transcribe', ('pT7',)). A bare name has no types.

    Returns None where the id does not match the schema's pattern.
    """
    m = ID_RE.match(str(raw))
    if not m:
        return None
    types = tuple(m.group(2).split(",")) if m.group(2) else ()
    return Op(m.group(1), types, str(raw))


def norm(name):
    """Lowercase, drop hyphens and underscores. The schema's rule for matching a name."""
    return re.sub(r"[-_\s]", "", str(name)).lower()


def words(name):
    """The words of a CamelCase or bracketed name, lowercase. Used for hints only."""
    return frozenset(w.lower() for w in re.findall(r"[A-Z]+(?![a-z])|[A-Z]?[a-z]+|\d+", str(name)))


class Order:
    """The published type order and process order, from docs/type-order.yml.

    A type that is not a node compares only to itself. That is the schema's decision for
    a bracket type with no node, so `below` never guesses a relation it was not given.
    """

    def __init__(
        self,
        type_edges=None,
        proc_edges=None,
        type_nodes=None,
        proc_nodes=None,
        slugs=None,
        aliases=None,
        declares=None,
    ):
        self.type_edges = {str(k): [str(x) for x in as_list(v)] for k, v in as_dict(type_edges).items()}
        self.proc_edges = {str(k): [str(x) for x in as_list(v)] for k, v in as_dict(proc_edges).items()}
        self.slugs = {str(k): str(v) for k, v in as_dict(slugs).items() if v}
        self.error = ""
        self.aliases = {str(k): str(v) for k, v in as_dict(aliases).items() if isinstance(v, str)}
        # What each type declares. A type that says nothing is ABSENT from this map, which is how
        # silence is told from `kind: none`, a claim that the type declares nothing.
        self.declares = {str(k): as_dict(v) for k, v in as_dict(declares).items()}
        self.has_declares = bool(declares) if isinstance(declares, dict) else False
        self.type_nodes = self._nodes(self.type_edges, type_nodes)
        self.proc_nodes = self._nodes(self.proc_edges, proc_nodes)
        # Whether the file listed its nodes, or they were read off the edges. A node with
        # no edges is only visible when the file lists it.
        self.nodes_listed = isinstance(type_nodes, list)

    @staticmethod
    def _nodes(edges, listed):
        nodes = set(str(n) for n in as_list(listed))
        for child, parents in edges.items():
            nodes.add(child)
            nodes.update(parents)
        return nodes

    @classmethod
    def from_file(cls, path):
        path = Path(path)
        if not path.is_file():
            return cls(), f"{path} (absent: every bracket type compares only to itself)"
        try:
            data = as_dict(yaml.safe_load(path.read_text()))
        except yaml.YAMLError as e:
            order = cls()
            order.error = str(e).splitlines()[0]
            return order, f"{path} (unreadable: every bracket type compares only to itself)"
        orders = as_dict(data.get("orders"))
        t, p = as_dict(orders.get("type_refinement")), as_dict(orders.get("process_refinement"))
        order = cls(
            t.get("edges"),
            p.get("edges"),
            t.get("nodes"),
            p.get("nodes"),
            data.get("module_slugs"),
            data.get("bracket_aliases"),
            data.get("type_declares"),
        )
        how = "nodes listed" if order.nodes_listed else "nodes read off the edges"
        extra = f"; {len(order.aliases)} bracket aliases, {len(order.declares)} type declarations"
        return (
            order,
            f"{path} ({len(order.type_nodes)} type nodes, {len(order.proc_nodes)} process nodes; {how}{extra})",
        )

    @staticmethod
    def _below(edges, a, b):
        """a refines b: reflexive, transitive, and safe on a cycle."""
        seen, stack = set(), [a]
        while stack:
            n = stack.pop()
            if n == b:
                return True
            if n in seen:
                continue
            seen.add(n)
            stack.extend(edges.get(n, []))
        return False

    def type_below(self, a, b):
        return self._below(self.type_edges, a, b)

    def proc_below(self, a, b):
        return self._below(self.proc_edges, a, b)

    def resolve_type(self, name):
        """The node a type name stands for, or None.

        An exact node first, then a page slug, then the schema's normalized match
        (lowercase, no hyphens) if exactly one node answers to it.
        """
        name = str(name)
        if name in self.type_nodes:
            return name
        if self.aliases.get(name) in self.type_nodes:
            return self.aliases[name]
        if self.slugs.get(name) in self.type_nodes:
            return self.slugs[name]
        hits = {n for n in self.type_nodes if norm(n) == norm(name)}
        return hits.pop() if len(hits) == 1 else None

    def hint(self, name):
        """A node made of the same words as `name`, in another order. A hint only."""
        w = words(name)
        hits = sorted(n for n in self.type_nodes if n != name and words(n) == w)
        return hits[0] if len(hits) == 1 else ""

    def cycles(self):
        return _cycles(self.type_edges, "type order") + _cycles(self.proc_edges, "process order")

    def denials(self):
        """[(type, ancestor, names)]: a type that claims it declares nothing, below one that declares.

        `kind: none` is a claim. A type that says nothing is not in the map and inherits.
        The nearest declaring ancestor on each line above the type is the one reported.
        """
        out = []
        for t, entry in sorted(self.declares.items()):
            if entry.get("kind") != "none":
                continue
            for parent in self.type_edges.get(t, []):
                seen, frontier = {t}, [parent]
                found = None
                while frontier and not found:
                    nxt = []
                    for n in frontier:
                        if n in seen:
                            continue
                        seen.add(n)
                        if as_dict(self.declares.get(n)).get("kind") == "declares":
                            found = n
                            break
                        nxt.extend(self.type_edges.get(n, []))
                    frontier = nxt
                if found:
                    out.append((t, found, as_list(self.declares[found].get("names"))))
        return sorted(set((t, a, tuple(n)) for t, a, n in out))


def _cycles(edges, label):
    """One example cycle per strongly connected loop, as a list of names."""
    found, color = [], {}

    def visit(n, path):
        color[n] = 1
        for m in edges.get(n, []):
            if color.get(m) == 1:
                found.append((label, path[path.index(m) :] + [m] if m in path else [n, m]))
            elif color.get(m) is None:
                visit(m, path + [m])
        color[n] = 2

    for n in list(edges):
        if color.get(n) is None:
            visit(n, [n])
    return found


def cmp_operation(provided, required, order):
    """Does a provider of `provided` meet a requirement for `required`?

    Same operation word, and then the bracket, CONTRAVARIANT: the provider's type must be
    at least as wide as the requirer's. A bare requirement demands nothing and is met by
    any provider of the operation. It is not the top type.
    """
    p, r = parse_op(provided), parse_op(required)
    if p is None or r is None:
        bad = provided if p is None else required
        return Verdict(UNDETERMINED, "malformed id", f"`{bad}` does not match the schema's id pattern")
    if p.word != r.word:
        # A provider of a finer operation does the coarser one: emit_fluorescence is an
        # emit_color. The schema says "the same word", so this is reported as its own `via`.
        if order.proc_below(p.word, r.word):
            if not r.types:
                return Verdict(MET, "operation order", f"`{p.word}` refines `{r.word}`")
            return Verdict(
                UNDETERMINED,
                "operation order",
                f"`{p.word}` refines `{r.word}`, and the schema does not say how a bracket crosses that",
            )
        return Verdict(UNMET, "different operation", f"`{p.word}` is not `{r.word}`")
    if not r.types:
        return Verdict(MET, "same operation", "a bare requirement demands nothing")
    if not p.types:
        return Verdict(
            UNDETERMINED, "provider names no type", f"`{provided}` states no type, so how wide it is is not stated"
        )
    if len(p.types) > 1 or len(r.types) > 1:
        return Verdict(
            UNDETERMINED,
            "type list",
            "the schema does not say whether a list of types means all of them or any of them",
        )
    pt, rt = p.types[0], r.types[0]
    if pt == rt:
        return Verdict(MET, "same type", f"both name `{pt}`")
    # The operation order spells the same relation with the operation in front.
    if order.proc_below(f"{p.word}[{rt}]", f"{p.word}[{pt}]"):
        return Verdict(MET, "operation order", f"`{p.word}[{rt}]` refines `{p.word}[{pt}]`: the provider is wider")
    pn, rn = order.resolve_type(pt), order.resolve_type(rt)
    if pn and rn:
        by = "".join(f" ({t} is {n} by alias)" for t, n in ((pt, pn), (rt, rn)) if t != n and t in order.aliases)
        if order.type_below(rn, pn):
            return Verdict(MET, "type order", f"`{rt}` refines `{pt}`: the provider is wider{by}")
        return Verdict(UNMET, "type order", f"`{rt}` does not refine `{pt}`: the provider is not wide enough{by}")
    missing = [t for t, n in ((pt, pn), (rt, rn)) if n is None]
    hints = [f"`{t}` has the words of `{order.hint(t)}`" for t in missing if order.hint(t)]
    return Verdict(
        UNMET,
        "no node",
        "no node in the published order for "
        + ", ".join(f"`{t}`" for t in missing)
        + ", so a type compares only to itself",
        "; ".join(hints),
    )


def length_factor(unit):
    """Meters per `unit`, or None. U+03BC (Greek mu) and U+00B5 (micro sign) are the same unit."""
    if not isinstance(unit, str):
        return None
    return LENGTH_UNITS.get(unit.strip().replace("\u03bc", "\u00b5").lower())


def is_number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _length(value, unit):
    f = length_factor(unit)
    return None if f is None or not is_number(value) else value * f


def cmp_interval(provided, required):
    """Does the provider's band contain the interval asked for? Closed intervals.

    Both are `{low, high, unit}`. Units are converted, so 0.5 µm contains 480 to 520 nm.
    """
    lo_p, hi_p = _length(provided.get("low"), provided.get("unit")), _length(provided.get("high"), provided.get("unit"))
    lo_r, hi_r = _length(required.get("low"), required.get("unit")), _length(required.get("high"), required.get("unit"))
    if None in (lo_p, hi_p, lo_r, hi_r):
        return Verdict(UNDETERMINED, "interval", "a bound is missing, or its unit is not a length this walker reads")
    if lo_p > hi_p or lo_r > hi_r:
        return Verdict(UNDETERMINED, "interval", "an interval has low above high")
    if lo_p <= lo_r and hi_r <= hi_p:
        return Verdict(MET, "interval", "the provider's band contains the interval asked for")
    return Verdict(UNMET, "interval", "the interval asked for is not inside the provider's band")


def cmp_within(bound, lumen, outer):
    """|(lumen - outer) - setpoint| <= tolerance, for a `within` bound.

    `bound` is `{setpoint, value, unit}`. The readings are `{value, unit}`. Units are
    compared literally, as the schema says, so mOsm/kg and mOsm/L never meet. A bound with
    no setpoint or no tolerance cannot be computed and is never a pass.
    """
    setpoint, tol, unit = bound.get("setpoint"), bound.get("value"), bound.get("unit")
    if setpoint is None or tol is None:
        return Verdict(UNDETERMINED, "within", "the bound has no setpoint or no tolerance, so it cannot be computed")
    if lumen.get("unit") != unit or outer.get("unit") != unit:
        return Verdict(
            UNDETERMINED, "within", f"the readings are not both in `{unit}`, and units are compared literally"
        )
    gap = lumen["value"] - outer["value"]
    off = abs(gap - setpoint)
    if off <= tol:
        return Verdict(MET, "within", f"lumen minus outer is {gap:g} {unit}, {off:g} from the setpoint, inside {tol:g}")
    return Verdict(UNMET, "within", f"lumen minus outer is {gap:g} {unit}, {off:g} from the setpoint, outside {tol:g}")


def cmp_within_unoriented(bound, a, b):
    """The `within` check when it is not stated which reading is the lumen.

    If both orientations agree, the answer holds either way. If they differ, which one is
    the lumen decides it, and that is not stated, so the answer is undetermined.
    """
    one, two = cmp_within(bound, a, b), cmp_within(bound, b, a)
    if one.status == two.status:
        return one
    return Verdict(
        UNDETERMINED,
        "within",
        "the two readings pass in one orientation and fail in the other, " "and which one is the lumen is not stated",
    )


def cmp_type(sub, sup, order):
    """Does `sub` refine `sup` in the published type order? A type is its own refinement, node or not."""
    if sub == sup:
        return Verdict(MET, "same type", f"both are `{sub}`")
    sn, un = order.resolve_type(sub), order.resolve_type(sup)
    if sn is None or un is None:
        miss = [t for t, n in ((sub, sn), (sup, un)) if n is None]
        return Verdict(UNDETERMINED, "type order", "no node for " + ", ".join(f"`{t}`" for t in miss))
    if order.type_below(sn, un):
        return Verdict(MET, "type order", f"`{sub}` refines `{sup}`")
    return Verdict(UNMET, "type order", f"`{sub}` does not refine `{sup}`")


def dispatch(kind, *args, **kw):
    """Compare in the order the requirement names. The one entry point for every rule."""
    try:
        fn = {
            "operation": cmp_operation,
            "type": cmp_type,
            "interval": cmp_interval,
            "within": cmp_within,
            "within-unoriented": cmp_within_unoriented,
        }[kind]
    except KeyError:
        raise ValueError(f"no comparator for `{kind}`") from None
    return fn(*args, **kw)


# --------------------------------------------------------------------------- #
# Reading the sources
# --------------------------------------------------------------------------- #


@dataclasses.dataclass
class Item:
    rule: str
    kind: str  # "finding" or "gap"
    code: str
    where: str
    text: str


@dataclasses.dataclass
class Source:
    slug: str
    kind: str  # "module" or "process"
    path: str
    doc: dict


def as_list(value):
    if value is None:
        return []
    return list(value) if isinstance(value, (list, tuple)) else [value]


def as_dict(value):
    return value if isinstance(value, dict) else {}


def page_slug(page):
    """`../base-cytosol/spec.md` -> `base-cytosol`. None where there is no page."""
    if not page:
        return None
    parts = [p for p in str(page).replace("\\", "/").split("/") if p and p not in (".", "..")]
    if parts and parts[-1].endswith(".md"):
        parts = parts[:-1]
    return parts[-1] if parts else None


class Corpus:
    def __init__(self, sources, order):
        self.sources = {(s.kind, s.slug): s for s in sources}
        self.order = order

    @classmethod
    def load(cls, root, order_path=None):
        root = Path(root)
        sources, unreadable = [], []
        for kind, sub in (("module", "modules"), ("process", "processes")):
            for f in sorted((root / "docs" / sub).glob("*/spec.yml")):
                if not f.is_file():
                    continue
                try:
                    doc = yaml.safe_load(f.read_text()) or {}
                except yaml.YAMLError as e:
                    unreadable.append((str(f), str(e).splitlines()[0]))
                    continue
                if not isinstance(doc, dict):
                    unreadable.append((str(f), "not a mapping"))
                    continue
                sources.append(Source(f.parent.name, kind, str(f.relative_to(root)), doc))
        order, how = Order.from_file(order_path or root / "docs" / "type-order.yml")
        corpus = cls(sources, order)
        corpus.order_note, corpus.unreadable = how, unreadable
        return corpus

    def of(self, kind):
        return [s for (k, _), s in sorted(self.sources.items()) if k == kind]

    def get(self, kind, slug):
        return self.sources.get((kind, slug))

    def class_source(self, entry):
        """The module source a `refines:` entry stands for, or None.

        By slug, then by a slug the order maps to that type, then by the schema's
        normalized match. A type with no page has no source, which is not an error.
        """
        entry = str(entry)
        if ("module", entry) in self.sources:
            return entry
        for slug, t in self.order.slugs.items():
            if t == entry and ("module", slug) in self.sources:
                return slug
        hits = [s.slug for s in self.of("module") if norm(s.slug) == norm(entry)]
        return hits[0] if len(hits) == 1 else None

    def parents(self, kind, slug):
        """(source slugs, entries with no source) for one source's `refines:`."""
        doc = self.get(kind, slug).doc
        found, dead = [], []
        for entry in as_list(doc.get("refines")):
            target = (
                self.class_source(entry)
                if kind == "module"
                else (str(entry) if ("process", str(entry)) in self.sources else None)
            )
            (found if target else dead).append(target or str(entry))
        return found, dead

    def ancestors(self, kind, slug):
        """Every source this one refines, nearest first and each once. Safe on a cycle."""
        order, seen, frontier = [], {slug}, [slug]
        while frontier:
            nxt = []
            for s in frontier:
                for p in self.parents(kind, s)[0]:
                    if p not in seen:
                        seen.add(p)
                        order.append(p)
                        nxt.append(p)
            frontier = nxt
        return order

    def refines_graph(self, kind):
        return {s.slug: self.parents(kind, s.slug)[0] for s in self.of(kind)}

    def effective(self, slug, key):
        """Entries of `requires` or `provides` this module has: its own, then its classes'.

        Each is (entry, origin slug). A member inherits through `refines:` and does not
        restate. `optional` is carried on the entry.
        """
        ok = lambda e: isinstance(e, dict) and isinstance(e.get("id"), str)
        out = [(e, slug) for e in as_list(self.get("module", slug).doc.get(key)) if ok(e)]
        for ancestor in self.ancestors("module", slug):
            out += [(e, ancestor) for e in as_list(self.get("module", ancestor).doc.get(key)) if ok(e)]
        return out

    def stated_above(self, kind, slug, get):
        """What each parent line states for a key: [(source, value)], one per direct parent.

        Walks up each line to the nearest source that states the key, so a child is held to
        what it inherits through a silent middle, and not only to its direct parent.
        """
        out = []
        for parent in self.parents(kind, slug)[0]:
            for up in [parent] + self.ancestors(kind, parent):
                value = get(self.get(kind, up).doc)
                if value is not None:
                    out.append((up, value))
                    break
        return out


# --------------------------------------------------------------------------- #
# R3: compartments
# --------------------------------------------------------------------------- #


class _Blocks:
    def __init__(self):
        self.parent = {}

    def add(self, x):
        self.parent.setdefault(x, x)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)


@dataclasses.dataclass
class Unit:
    id: str
    slug: str
    leaves: frozenset
    optional: bool = False


class Composite:
    """The compartments of one module's own steps, from `operator` alone.

    A unit is an input or a step's product. `mixing` puts its operands in one compartment.
    `packing` leaves each in its own. A pair that differs from the step's label is in
    `operator_pairs`. `stitching` joins operands into one object, so it counts as `mixing`
    here. The answer is the state after the last step, and nothing can separate what is
    already together. An id that two steps use is two portions of one stock.

    Where the steps cannot say, the answer is `unknown` and the walk does not guess: a
    `mixing` step whose operand is already several compartments, a `packing` step whose
    operands are already together, an operand that names nothing, a product that reuses an
    id, a shape that is not a mapping or a list.
    """

    def __init__(self, slug, doc, outside=None):
        self.slug, self.units, self.notes, self.all = slug, {}, [], []
        self.outside = outside or (lambda step: None)
        self.stitching = 0
        self.outside_steps = {}
        self.uses = {}
        self.blocks, self.tainted = _Blocks(), set()
        inputs, steps = doc.get("inputs"), doc.get("process_steps")
        if inputs is not None and not isinstance(inputs, dict):
            self.notes.append("`inputs` is not a mapping, so its constituents are unknown")
            inputs = {}
        if steps is not None and not isinstance(steps, list):
            self.notes.append("`process_steps` is not a list, so its steps are unknown")
            steps = []
        for iid, spec in (inputs or {}).items():
            spec = as_dict(spec)
            self._add(Unit(str(iid), page_slug(spec.get("page")), frozenset([str(iid)]), bool(spec.get("optional"))))
        for step in steps or []:
            self._step(step)

    def _add(self, unit):
        self.units[unit.id] = unit
        self.all.append(unit)
        for leaf in unit.leaves:
            self.blocks.add(leaf)

    def _roots(self, unit):
        return {self.blocks.find(leaf) for leaf in unit.leaves}

    def _taint(self, *units):
        for u in units:
            self.tainted |= u.leaves

    def _portion(self, unit):
        """The unit as one step consumes it.

        An id that two steps use is two portions of one stock, such as a membrane that feeds two
        encapsulations. Treating them as one object would put their products in one compartment
        because they share a leaf. The first use takes the unit itself, and the one the report
        asks about. A later use takes a copy with new leaves and the same compartments among them.
        """
        n = self.uses.get(unit.id, 0)
        self.uses[unit.id] = n + 1
        if n == 0:
            return unit
        copy = {leaf: f"{leaf}#{n + 1}" for leaf in unit.leaves}
        groups = {}
        for leaf, new in copy.items():
            self.blocks.add(new)
            groups.setdefault(self.blocks.find(leaf), []).append(new)
        for group in groups.values():
            for other in group[1:]:
                self.blocks.union(group[0], other)
        if unit.leaves & self.tainted:
            self.tainted |= set(copy.values())
        return Unit(unit.id, unit.slug, frozenset(copy.values()), unit.optional)

    def _step(self, step):
        if not isinstance(step, dict):
            self.notes.append("a step is not a mapping, so it is skipped and its compartments are unknown")
            return
        prod = as_dict(step.get("produces"))
        sid = prod.get("id") or step.get("id")
        ops = [str(o) for o in as_list(step.get("operands"))]
        resolved = [None if self.units.get(o) is None else self._portion(self.units[o]) for o in ops]
        known = [u for u in resolved if u is not None]
        operator = step.get("operator")
        self.stitching += operator == "stitching"
        named = self.outside(step)
        if named:
            self.outside_steps[named] = self.outside_steps.get(named, 0) + 1
            self.notes.append(
                f"step `{step.get('id')}`: its process refines `{named}`, which {OUTSIDE_THE_MODEL[named]}. "
                "The compartment model covers operators only, so the compartments of its operands are unknown"
            )
            self._taint(*known)
        elif any(u is None for u in resolved) or operator not in ("mixing", "packing", "stitching"):
            self.notes.append(
                f"step `{step.get('id')}`: an operand or the operator is not stated, so its compartments are unknown"
            )
            self._taint(*known)
        else:
            exceptions = {}
            for pair in as_list(step.get("operator_pairs")):
                names = as_dict(pair).get("operands")
                if isinstance(names, list) and all(isinstance(n, str) for n in names):
                    exceptions[frozenset(names)] = as_dict(pair).get("operator")
            apart = []
            for a, b in itertools.combinations(known, 2):
                how = exceptions.get(frozenset((a.id, b.id)), operator)
                if how in ("mixing", "stitching"):
                    ra, rb = self._roots(a), self._roots(b)
                    if len(ra) == 1 and len(rb) == 1:
                        self.blocks.union(next(iter(ra)), next(iter(rb)))
                    else:
                        self.notes.append(
                            f"step `{step.get('id')}`: `mixing` of a unit that is already several compartments; "
                            "which one joins is not stated"
                        )
                        self._taint(a, b)
                elif how == "packing":
                    apart.append((a, b))
            for a, b in apart:
                if self._roots(a) & self._roots(b):
                    self.notes.append(
                        f"step `{step.get('id')}`: its label `packing` keeps `{a.id}` and `{b.id}` apart, "
                        "and the other pairs of this step already put them in one compartment"
                    )
                    self._taint(a, b)
        if sid:
            leaves = frozenset().union(*[u.leaves for u in known]) if known else frozenset()
            product = Unit(str(sid), page_slug(prod.get("page")), leaves, bool(step.get("optional")))
            earlier = self.units.get(product.id)
            if earlier is not None:
                self.notes.append(f"step `{step.get('id')}`: its product reuses the id `{product.id}`")
                self._taint(earlier, product)
            self.units[product.id] = product
            self.all.append(product)

    def shares(self, a, b):
        """'yes', 'no' or 'unknown': do two units end in one compartment?

        A unit that is several compartments (a packed product) shares one with another unit
        if their sets overlap, but which of its compartments is its own is not stated, so
        that is `unknown`. If the sets do not overlap at all, the answer is `no` however
        many compartments there are.
        """
        if (a.leaves | b.leaves) & self.tainted:
            return "unknown"
        ra, rb = self._roots(a), self._roots(b)
        if not ra & rb:
            return "no"
        return "yes" if len(ra) == 1 and len(rb) == 1 else "unknown"


# --------------------------------------------------------------------------- #
# The walk
# --------------------------------------------------------------------------- #


class Result:
    def __init__(self):
        self.items, self.counts, self.sections, self.read = [], {}, {}, []

    def add(self, rule, kind, code, where, text):
        self.items.append(Item(rule, kind, code, where, text))

    def line(self, rule, text):
        self.sections.setdefault(rule, []).append(text)

    @property
    def findings(self):
        return [i for i in self.items if i.kind == "finding"]

    @property
    def gaps(self):
        return [i for i in self.items if i.kind == "gap"]


@contextlib.contextmanager
def guard(res, rule, where):
    """One bad source must not stop the report. A crash becomes a finding and never silence."""
    try:
        yield
    except Exception as e:  # report-only: say what broke, and go on with the rest
        res.add(rule, "finding", "walk-error", where, f"could not be walked: {type(e).__name__}: {e}")


def _entries(corpus, key, res):
    """Every own entry of `requires` or `provides`: (entry, slug). A malformed one is a finding."""
    out = []
    for s in corpus.of("module"):
        value = s.doc.get(key)
        if value is None:
            continue
        if not isinstance(value, list):
            res.add("R1", "finding", "malformed-entry", s.slug, f"`{key}` is not a list")
            continue
        for e in value:
            if not isinstance(e, dict):
                res.add("R1", "finding", "malformed-entry", s.slug, f"a `{key}` entry is not a mapping")
            elif not isinstance(e.get("id"), str):
                res.add("R1", "finding", "malformed-id", s.slug, f"a `{key}` entry has no id that is a string")
            else:
                out.append((e, s.slug))
    return out


def walk(corpus):
    res = Result()
    modules, processes = corpus.of("module"), corpus.of("process")
    reqs, provs = _entries(corpus, "requires", res), _entries(corpus, "provides", res)
    res.counts.update(modules=len(modules), processes=len(processes), requires=len(reqs), provides=len(provs))
    res.read = [f"{len(modules)} module sources, {len(processes)} process sources", f"order: {corpus.order_note}"]
    for path, why in corpus.unreadable:
        res.add("read", "finding", "unreadable", path, f"could not be read: {why}")
    if corpus.order.error:
        res.add("read", "finding", "unreadable", "type-order.yml", f"could not be read: {corpus.order.error}")

    for label, found in corpus.order.cycles():
        res.add("R2", "finding", "order-cycle", label, "cycle in the " + label + ": " + " -> ".join(found))

    _r1(corpus, res, reqs, provs)
    _r2(corpus, res)
    _r3(corpus, res, provs)
    _r4(corpus, res, reqs)
    _r5(corpus, res)
    _r6(corpus, res)
    return res


def _providers(provs, rid, order):
    """Split providers by how they compare with `rid`: (those that meet it, those that might)."""
    met, maybe = [], []
    for pentry, pslug in provs:
        if parse_op(pentry.get("id")) is None:
            continue
        v = dispatch("operation", pentry["id"], rid, order)
        if v.status == MET:
            met.append((pentry, pslug, v))
        elif v.status == UNDETERMINED:
            maybe.append((pentry, pslug, v))
    return met, maybe


def _who(found):
    return "; ".join(f"{slug} `{entry['id']}` ({v.via})" for entry, slug, v in found)


def _r1(corpus, res, reqs, provs):
    order = corpus.order
    for entry, slug in reqs:
        with guard(res, "R1", slug):
            rid = entry["id"]
            if parse_op(rid) is None:
                res.add(
                    "R1", "finding", "malformed-id", slug, f"requires `{rid}` does not match the schema's id pattern"
                )
                continue
            met, maybe = _providers(provs, rid, order)
            if met:
                extra = f"; undetermined: {_who(maybe)}" if maybe else ""
                res.line("R1", f"requires `{rid}` ({slug}): met by {_who(met)}{extra}")
            elif maybe:
                res.line("R1", f"requires `{rid}` ({slug}): UNDETERMINED by {_who(maybe)}")
                res.add(
                    "R1",
                    "gap",
                    "provider-undetermined",
                    slug,
                    f"requires `{rid}`; a provider may meet it, and the answer is not decided: {maybe[0][2].why}",
                )
            else:
                res.line("R1", f"requires `{rid}` ({slug}): NO PROVIDER declared in this corpus")
                cause = ""
                if order.proc_below(parse_op(rid).word, ASSAY):
                    cause = f". An assay provides `{ASSAY}`, and this repo has no assay sources"
                res.add("R1", "gap", "no-provider", slug, f"requires `{rid}` and no source provides it{cause}")
    for entry, slug in provs:
        if parse_op(entry.get("id")) is None:
            res.add(
                "R1",
                "finding",
                "malformed-id",
                slug,
                f"provides `{entry.get('id')}` does not match the schema's id pattern",
            )
    # The bracket types the order has no node for. The schema measured this itself.
    types = {t for e, _ in reqs + provs for t in (parse_op(e["id"]).types if parse_op(e["id"]) else ())}
    bare = sorted(t for t in types if order.resolve_type(t) is None)
    res.counts["bracket_types"] = len(types)
    res.counts["bracket_types_without_node"] = len(bare)
    res.line(
        "R1",
        f"bracket types: {len(types)}; with a node in the published order: {len(types) - len(bare)}; "
        f"with none, so they compare only to themselves: {len(bare)}",
    )
    for t in bare:
        h = order.hint(t)
        res.add(
            "R1",
            "gap",
            "type-without-node",
            t,
            f"bracket type `{t}` has no node in the published order" + (f" (it has the words of `{h}`)" if h else ""),
        )
    valid = lambda e: parse_op(e["id"]) is not None
    idle = [
        e
        for e, _ in provs
        if valid(e)
        and not any(valid(r) and dispatch("operation", e["id"], r["id"], order).status != UNMET for r, _ in reqs)
    ]
    res.counts["providers_nobody_requires"] = len(idle)
    res.line("R1", f"providers nobody requires: {len(idle)} of {len(provs)}")


def _r2(corpus, res):
    edges = ended = dead_total = 0
    for kind in ("module", "process"):
        for s in corpus.of(kind):
            with guard(res, "R2", s.slug):
                found, dead = corpus.parents(kind, s.slug)
                edges += len(found) + len(dead)
                ended += len(found)
                dead_total += len(dead)
                for d in dead:
                    where = "docs/processes or docs/modules"
                    res.add(
                        "R2",
                        "gap",
                        "refines-no-source",
                        s.slug,
                        f"{kind} `{s.slug}` refines `{d}`, which has no source under {where}: nothing can flow across it",
                    )
    for kind in ("module", "process"):
        for _, cyc in _cycles(corpus.refines_graph(kind), kind):
            res.add("R2", "finding", "refines-cycle", cyc[0], f"{kind} `refines:` is a cycle: " + " -> ".join(cyc))
    res.counts.update(refines_edges=edges, refines_with_source=ended, refines_without_source=dead_total)
    res.line(
        "R2", f"refines edges: {edges}; ending at a source: {ended}; ending at a node with no source: {dead_total}"
    )
    inherited = 0
    for s in corpus.of("module"):
        with guard(res, "R2", s.slug):
            for key in ("requires", "provides"):
                got = [(e, o) for e, o in corpus.effective(s.slug, key) if o != s.slug]
                if got:
                    inherited += len(got)
                    res.line("R2", f"{s.slug} inherits {key}: " + ", ".join(f"`{e['id']}` from {o}" for e, o in got))
    res.counts["inherited_entries"] = inherited


def _process_names(corpus, step):
    """The names a step's process goes by: its abstract, its page, and what that page's source refines."""
    proc = as_dict(step.get("process"))
    names = [n for n in (proc.get("abstract"), page_slug(proc.get("page"))) if isinstance(n, str)]
    for n in list(names):
        if ("process", n) in corpus.sources:
            for up in [n] + corpus.ancestors("process", n):
                names += corpus.parents("process", up)[1]
    return names


def _outside(corpus):
    """A function: which process outside the model does this step's process refine, if any?

    By its abstract, its page, or that page's source and what that source refines.
    """
    order = corpus.order

    def check(step):
        names = _process_names(corpus, step)
        return next((o for o in OUTSIDE_THE_MODEL if any(order.proc_below(n, o) for n in names)), None)

    return check


def _r3(corpus, res, provs):
    order = corpus.order
    composites = [s for s in corpus.of("module") if s.doc.get("process_steps")]
    res.counts["composites"] = len(composites)
    checked = discharged = no_provider_anywhere = stitching = 0
    outside_steps = {name: 0 for name in OUTSIDE_THE_MODEL}
    outside = _outside(corpus)
    for s in composites:
        with guard(res, "R3", s.slug):
            comp = Composite(s.slug, s.doc, outside)
            stitching += comp.stitching
            for name, n in comp.outside_steps.items():
                outside_steps[name] += n
            for note in comp.notes:
                res.add("R3", "gap", "compartment-unknown", s.slug, note)
            units = [u for u in comp.all if u.slug and u.slug != s.slug and corpus.get("module", u.slug)]
            for u in units:
                # Two inputs can name one page. Say which one, only when the slug alone would not.
                who = f"{u.slug} (`{u.id}`)" if sum(1 for x in units if x.slug == u.slug) > 1 else u.slug
                for rentry, _origin in corpus.effective(u.slug, "requires"):
                    rid = rentry["id"]
                    if parse_op(rid) is None:
                        continue
                    checked += 1
                    cands = []  # (status, where, tag, provider is optional)
                    for v in units:
                        if v is u:
                            continue
                        for pentry, _ in corpus.effective(v.slug, "provides"):
                            if parse_op(pentry["id"]) is None:
                                continue
                            verdict = dispatch("operation", pentry["id"], rid, order)
                            if verdict.status != UNMET:
                                cands.append(
                                    (verdict.status, comp.shares(u, v), f"{v.slug} `{pentry['id']}`", v.optional)
                                )
                    same = [t for st, w, t, opt in cands if st == MET and w == "yes" and not opt]
                    unsure = [
                        t
                        for st, w, t, opt in cands
                        if (st == UNDETERMINED and w != "no")
                        or (st == MET and (w == "unknown" or (w == "yes" and opt)))
                    ]
                    elsewhere = [t for st, w, t, opt in cands if st == MET and w == "no"]
                    here = f"{s.slug}: {who} requires `{rid}`"
                    if same:
                        discharged += 1
                        res.line("R3", here + ": DISCHARGED by " + "; ".join(same))
                    elif unsure:
                        res.line("R3", here + ": UNDETERMINED, " + "; ".join(unsure))
                        res.add(
                            "R3",
                            "gap",
                            "discharge-undetermined",
                            s.slug,
                            f"{who} requires `{rid}`; a provider may share its compartment, and the compartment, "
                            "the provider's type or its presence is not stated",
                        )
                    elif u.optional:
                        res.line("R3", here + ": not discharged, and the requirer is optional")
                        res.add(
                            "R3",
                            "gap",
                            "requirer-optional",
                            s.slug,
                            f"{who} is an optional constituent and its requirement `{rid}` is not discharged; "
                            "the condition applies only if it is present",
                        )
                    elif rentry.get("optional"):
                        res.line("R3", here + ": not discharged, and the requirement is optional")
                    elif elsewhere:
                        res.line(
                            "R3",
                            here + ": NOT DISCHARGED. A provider is in another compartment: " + "; ".join(elsewhere),
                        )
                        res.add(
                            "R3",
                            "finding",
                            "provider-in-another-compartment",
                            s.slug,
                            f"{who} requires `{rid}`; " + "; ".join(elsewhere) + " is in another compartment",
                        )
                    elif not any(_providers(provs, rid, order)):
                        # Nothing in the corpus can meet it, so no composite could discharge it. That is
                        # one fact, reported once by R1, and not one finding for every composite.
                        no_provider_anywhere += 1
                    else:
                        res.line("R3", here + ": NOT DISCHARGED. Nothing in the composite provides it")
                        res.add(
                            "R3",
                            "finding",
                            "undischarged",
                            s.slug,
                            f"{who} requires `{rid}` and nothing in this composite provides it",
                        )
    res.counts.update(
        requirements_in_composites=checked,
        discharged_in_composites=discharged,
        no_provider_anywhere_in_composites=no_provider_anywhere,
        stitching_steps=stitching,
        outside_model_steps=sum(outside_steps.values()),
        **{f"steps_{name}": n for name, n in outside_steps.items()},
    )
    branches = {"stitching": stitching, **outside_steps}
    res.line(
        "R3",
        "branches the model names, and the steps that use each: "
        + ", ".join(f"{name} {n}" for name, n in branches.items())
        + ". "
        + (
            "No source uses "
            + ", ".join(f"`{name}`" for name, n in branches.items() if not n)
            + ", so each has nothing to test it on: the model's coverage is bounded by the corpus and not by the model."
            if not all(branches.values())
            else ""
        ),
    )
    res.line(
        "R3",
        f"composites (modules with steps): {len(composites)}; requirements a constituent carries: {checked}; "
        f"discharged: {discharged}; with no provider anywhere in the corpus, so none could be (see R1): "
        f"{no_provider_anywhere}",
    )


def _carried_size(corpus, slug):
    """(size class, route, source) a module reaches, or (None, None, None).

    The route is `type` or `refines`: the size can arrive through the module's own type, or through an
    axis it refines, such as `Vesicle[GUV]` or the slug `guv`. A source it refines can carry it too.
    """
    order = corpus.order
    for source in [slug] + corpus.ancestors("module", slug):
        doc = corpus.get("module", source).doc
        for route, names in (("type", [doc.get("type")]), ("refines", as_list(doc.get("refines")))):
            for name in names:
                node = order.resolve_type(name) if isinstance(name, str) else None
                for size in VESICLE_SIZES:
                    if node and order.type_below(node, f"Vesicle[{size}]"):
                        return size, route, source
    return None, None, None


def _r6(corpus, res):
    """A step that encapsulates must yield a product that states a vesicle size class.

    A product with no page states nothing, which is a gap and not a finding, since only a page can fix it.
    An abstract class, one that another source refines, is open on purpose and is skipped.
    """
    order = corpus.order
    classes = {corpus.class_source(e) for s in corpus.of("module") for e in as_list(s.doc.get("refines"))} - {None}
    found = {"type": 0, "refines": 0}
    steps = missing = unknown = skipped = 0
    for s in corpus.of("module"):
        with guard(res, "R6", s.slug):
            for step in as_list(s.doc.get("process_steps")):
                if not isinstance(step, dict) or not any(
                    order.proc_below(n, ENCAPSULATE) for n in _process_names(corpus, step)
                ):
                    continue
                steps += 1
                pslug = page_slug(as_dict(step.get("produces")).get("page"))
                if not pslug or corpus.get("module", pslug) is None:
                    unknown += 1
                    res.add(
                        "R6",
                        "gap",
                        "size-product-unknown",
                        s.slug,
                        f"step `{step.get('id')}` encapsulates, and its product has no source, so no size class is stated",
                    )
                    continue
                if pslug in classes:
                    skipped += 1
                    continue
                size, route, origin = _carried_size(corpus, pslug)
                if size is None:
                    missing += 1
                    res.add(
                        "R6",
                        "finding",
                        "encapsulation-no-size",
                        s.slug,
                        f"step `{step.get('id')}` encapsulates, and its product `{pslug}` states no vesicle size class "
                        f"({', '.join(VESICLE_SIZES)}) in its `type` or its `refines`",
                    )
                else:
                    found[route] += 1
    res.counts.update(
        encapsulations=steps,
        size_via_type=found["type"],
        size_via_refines=found["refines"],
        size_missing=missing,
        size_product_unknown=unknown,
        size_classes_skipped=skipped,
    )
    res.line(
        "R6",
        f"steps that encapsulate: {steps}. Product states a size class: {found['type'] + found['refines']} "
        f"(through its type: {found['type']}; through a `refines`: {found['refines']}). "
        f"States none: {missing}. Product has no source: {unknown}. Abstract class, skipped: {skipped}.",
    )
    res.line(
        "R6", "This checks for a size class and never for a diameter. No diameter is characterized for anything here."
    )


def _band(doc, key):
    """A member's stated number for `key`. A value stated in a step wins over one on the module."""
    sources = [as_dict(as_dict(s).get("parameters")) for s in as_list(doc.get("process_steps"))]
    sources.append(as_dict(doc.get("parameters")))
    for params in sources:
        if key in params:
            m = re.match(r"\s*~?\s*(-?\d+(?:\.\d+)?)", str(params[key]))
            if m:
                return float(m.group(1))
    return None


def _r4(corpus, res, reqs):
    res.line(
        "R4",
        "transcribe's guard, `p in P(cytosol)`, is `requires` and `provides`. R1 compares it and R3 discharges it.",
    )
    asked = resolved = missing = bad = 0

    def malformed(slug, entry, name, text):
        res.add("R4", "finding", "malformed-interval", slug, f"`{entry['id']}` parameter `{name}`: {text}")

    for entry, slug in reqs:
        with guard(res, "R4", slug):
            params = entry.get("parameters")
            if params is None:
                continue
            if not isinstance(params, dict):
                asked += 1
                bad += 1
                malformed(slug, entry, "parameters", "is not a mapping")
                continue
            for name, spec in params.items():
                asked += 1
                if not isinstance(spec, dict):
                    bad += 1
                    malformed(slug, entry, name, "is not an interval")
                    continue
                unit = spec.get("unit")
                if "peak" in spec:
                    if not (is_number(spec.get("bandwidth")) and spec["bandwidth"] > 0):
                        bad += 1
                        malformed(slug, entry, name, "has no usable bandwidth")
                        continue
                else:
                    lo, hi = spec.get("low"), spec.get("high")
                    if not (is_number(lo) and is_number(hi)) or lo > hi:
                        bad += 1
                        malformed(slug, entry, name, "low and high must be numbers, with low not above high")
                        continue
                if not isinstance(unit, str):
                    bad += 1
                    malformed(slug, entry, name, "has no unit")
                    continue
                if length_factor(unit) is None:
                    res.add(
                        "R4",
                        "gap",
                        "unit-unknown",
                        slug,
                        f"`{entry['id']}` parameter `{name}` is in `{unit}`, which this walker does not read as a length",
                    )
                    continue
                if "peak" not in spec:
                    continue
                carriers = [slug] + [m.slug for m in corpus.of("module") if slug in corpus.ancestors("module", m.slug)]
                for c in carriers:
                    if _band(corpus.get("module", c).doc, spec["peak"]) is None:
                        if c != slug:
                            missing += 1
                            res.add(
                                "R4",
                                "gap",
                                "peak-not-stated",
                                c,
                                f"{c} refines {slug}, whose `{entry['id']}` asks for `{spec['peak']}`, and states none",
                            )
                    else:
                        resolved += 1
    res.counts.update(intervals_asked=asked, intervals_resolved=resolved, intervals_peak_missing=missing)
    res.line(
        "R4",
        f"intervals asked by requirements: {asked}; resolved to a band for a member: {resolved}; "
        f"a member that states no peak: {missing}; malformed: {bad}",
    )
    res.line(
        "R4",
        "provider bands to compare them with: 0. The schema has no key for a provider's band, so the "
        "`interval` comparator has nothing in the sources to meet.",
    )
    within = []
    for s in corpus.of("module"):
        with guard(res, "R4", s.slug):
            for sens in as_list(s.doc.get("sensitivities")):
                sens = as_dict(sens)
                b = as_dict(sens.get("bound"))
                if b.get("sense") == "within":
                    within.append((s.slug, sens.get("id"), b))
    res.counts["within_bounds"] = len(within)
    for slug, sid, b in within:
        res.line(
            "R4",
            f"`within` bound {slug}/{sid}: setpoint {b.get('setpoint')}, tolerance {b.get('value')} {b.get('unit')}. "
            "No source states a reading for the lumen or the outer solution, and none says which operand is which.",
        )
        res.add("R4", "gap", "within-no-readings", slug, f"`within` bound `{sid}` has no readings to compare with")


def _r5_types(corpus, res):
    """A type that says it declares nothing, below a type that declares something."""
    order = corpus.order
    if not order.has_declares:
        res.line(
            "R5",
            "the published order carries no `type_declares`, so a type that denies what its ancestor declares cannot be found",
        )
        res.add("R5", "gap", "type-declares-absent", "type-order.yml", "no `type_declares` in the published order")
        return
    kinds = {}
    for t, entry in order.declares.items():
        kind = entry.get("kind")
        kinds[kind] = kinds.get(kind, 0) + 1
        if kind not in ("declares", "none", "position"):
            res.add(
                "R5",
                "gap",
                "declares-kind-unknown",
                t,
                f"type `{t}` has kind `{kind}`, which this walker does not read",
            )
    res.counts["type_declarations"] = len(order.declares)
    res.counts["types_claiming_none"] = kinds.get("none", 0)
    res.line(
        "R5",
        f"type declarations: {len(order.declares)} ("
        + ", ".join(f"{n} {k}" for k, n in sorted(kinds.items(), key=lambda kv: str(kv[0])))
        + "). "
        "A type absent from the map is silent and inherits.",
    )
    for t, ancestor, names in order.denials():
        res.add(
            "R5",
            "finding",
            "type-denies-ancestor",
            t,
            f"type `{t}` claims it declares nothing, and its ancestor `{ancestor}` declares "
            + (", ".join(f"`{n}`" for n in names) or "something"),
        )


def _r5(corpus, res):
    compared = 0
    for s in corpus.of("process"):
        with guard(res, "R5", s.slug):
            for key in ("operator", "keeps_boundary", "conserves"):
                for up, p in corpus.stated_above("process", s.slug, lambda d, k=key: d.get(k)):
                    c = s.doc.get(key)
                    if c is None:
                        continue  # silence inherits. Absence is undeclared, never false.
                    compared += 1
                    if c != p:
                        res.add(
                            "R5",
                            "finding",
                            "contradiction",
                            s.slug,
                            f"process `{s.slug}` says `{key}: {c}` and `{up}` above it says `{p}`",
                        )
            produced = lambda d: as_dict(as_dict(d.get("signature")).get("produces")).get("type")
            pc = produced(s.doc)
            for up, pp in corpus.stated_above("process", s.slug, produced):
                if not pc:
                    continue
                compared += 1
                v = dispatch("type", pc, pp, corpus.order)
                if v.status == UNMET:
                    res.add(
                        "R5",
                        "finding",
                        "contradiction",
                        s.slug,
                        f"process `{s.slug}` produces `{pc}` and `{up}` above it produces `{pp}`; {v.why}",
                    )
                elif v.status == UNDETERMINED:
                    res.add(
                        "R5",
                        "gap",
                        "type-undetermined",
                        s.slug,
                        f"`{s.slug}` produces `{pc}`, `{up}` above it produces `{pp}`: {v.why}",
                    )
    for s in corpus.of("module"):
        with guard(res, "R5", s.slug):
            for key in ("requires", "provides", "impositions"):
                if s.doc.get(key) == []:
                    for a in corpus.ancestors("module", s.slug):
                        if as_list(corpus.get("module", a).doc.get(key)):
                            res.add(
                                "R5",
                                "gap",
                                "empty-list",
                                s.slug,
                                f"`{s.slug}` writes `{key}: []` and its class `{a}` has `{key}`; "
                                "the schema does not say an empty list is a claim",
                            )
    _r5_types(corpus, res)
    res.counts["inherited_declarations_compared"] = compared
    res.line(
        "R5",
        f"stated values compared with what is above them: {compared}. A key the child does not state is silence and inherits.",
    )


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #

TITLES = {
    "R1": "R1  every requirement, and what meets it (contravariant on the bracket)",
    "R2": "R2  inheritance down refines:",
    "R3": "R3  discharge in a composite (compartments from mixing and packing)",
    "R4": "R4  the other guard kinds",
    "R5": "R5  a child must not contradict its parent (a denial, never a silence)",
    "R6": "R6  an encapsulation's product states a vesicle size class (never a diameter)",
}


def render(res):
    out = ["check-requirements.py: walks requires: and provides: (report only)", "", "READ"]
    out += [f"  {x}" for x in res.read]
    c = res.counts
    out.append(f"  requires: {c['requires']} entries; provides: {c['provides']} entries")
    for rule in ("R1", "R2", "R3", "R4", "R5", "R6"):
        out += ["", TITLES[rule]]
        out += [f"  {x}" for x in res.sections.get(rule, ["(nothing to report)"])]
        for it in res.items:
            if it.rule == rule and it.kind == "finding":
                out.append(f"  FINDING [{it.code}] {it.where}: {it.text}")
    out += ["", "GAPS (not failures: what this walk could not decide, with the schema's own reasons)"]
    by = {}
    for g in res.gaps:
        by.setdefault((g.rule, g.code), []).append(g)
    for (rule, code), items in sorted(by.items()):
        out.append(f"  {rule} {code}: {len(items)}")
        out += [f"      {g.where}: {g.text}" for g in items[:8]]
        if len(items) > 8:
            out.append(f"      ... and {len(items) - 8} more")
    if not by:
        out.append("  none")
    out += ["", f"findings={len(res.findings)} gaps={len(res.gaps)} (report only: exit 0 unless --strict)"]
    return "\n".join(out)


def to_data(res):
    return {
        "read": res.read,
        "counts": res.counts,
        "findings": [dataclasses.asdict(i) for i in res.findings],
        "gaps": [dataclasses.asdict(i) for i in res.gaps],
        "sections": res.sections,
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
        "--root", default=str(REPO), help="a tree with docs/modules, docs/processes and docs/type-order.yml"
    )
    ap.add_argument("--order", help="a type order file, instead of <root>/docs/type-order.yml")
    ap.add_argument("--strict", action="store_true", help="exit 1 if there is any finding. Nothing runs this.")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    args = ap.parse_args(argv)
    corpus = Corpus.load(args.root, args.order)
    if not corpus.of("module"):
        print(
            f"no module source under {args.root}/docs/modules. A walk over no files is not a clean run.",
            file=sys.stderr,
        )
        return 2
    res = walk(corpus)
    print(json.dumps(to_data(res), indent=2) if args.json else render(res))
    return 1 if args.strict and res.findings else 0


if __name__ == "__main__":
    sys.exit(main())
