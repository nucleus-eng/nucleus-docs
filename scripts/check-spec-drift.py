#!/usr/bin/env python3
"""
check-spec-drift.py — does a spec.yml figure still appear on its own page?

The gap this fills. check-spec-schema.py validates shape and resolves
references and never looks at a figure. check-composition.py checks that the
prose names the constituents the source composes, and never looks at a figure
either. So a page can be edited — a concentration corrected, a volume changed —
and its spec.yml keeps the old number with nothing to notice.

What it does. For every number-with-unit in a source's `parameters`, look for
the same figure in that module's spec.md. A figure the page no longer states is
reported as drift.

What it CANNOT do, stated here because a checker that hides its blind spots is
worse than none.
  * It cannot tell which side is wrong. A figure on one side only means the two
    disagree, not that the source is stale.
  * It only reads `parameters`. Figures in `notes:`, `ratio:` and `headroom:`
    are not checked.
  * A page may state a figure in a form no normalisation reaches — inside an
    image, a linked DevNote, or computed rather than written. Those report as
    absent and are false positives.
  * It cannot always see the unit. The corpus's dominant page format is a table
    whose cells hold bare numbers and whose unit sits in the row label or the
    column head: "| NEB PURExpress Solution A | 4 | 4 |" against a source's
    "4 uL". So a match is reported in three tiers, and only the top one is
    evidence of agreement.
  * A bare-number match is weak on purpose. "0.5" occurs on many pages for many
    reasons, so a number-only hit cannot be told from a coincidence and is NOT
    counted as agreement.

Denominators are printed, always. A run that checks nothing must say so rather
than print a tick: see scripts/check-toc.py for the same discipline.

Advisory by default. --strict exits 1 on any drift.
"""
import glob, os, re, sys, unicodedata

try:
    import yaml
except ImportError:
    sys.exit("check-spec-drift.py needs PyYAML")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATTERN = os.path.join(ROOT, "docs", "modules", "*", "spec.yml")

# Case matters and getting it wrong conflates real units. nM is nanomolar and
# nm is nanometres; a case-insensitive match reported a 405 nm laser as a
# concentration. So units are matched case-SENSITIVELY, with both spellings
# named wherever the corpus uses both.
UNITS = (r"(?:nM|nm|uM|mM|mOsm|M|ng/uL|ug/uL|mg/mL|U/mL|KU|%|x|X|uL|mL|L"
         r"|degC|C|bp|kb|kDa|h|min|s)")
# Digits with an optional decimal part, and NOTHING else. Thousands separators
# are folded in normalise() before this runs, so they must not appear here:
# letting the number swallow a comma made "0.076 mL, 25 mg/mL" one figure.
NUMBER = r"\d+(?:\.\d+)?"
FIGURE = re.compile(r"(" + NUMBER + r")\s*(" + UNITS + r")(?![A-Za-z0-9/])")


def normalise(text):
    """Fold the spellings that mean one thing, so a match is about the figure."""
    t = unicodedata.normalize("NFKC", text)
    t = t.replace("µ", "u").replace("μ", "u")   # micro sign, greek mu
    t = t.replace("×", "x").replace("−", "-")   # times, minus
    t = t.replace("°", "")                            # degree sign
    t = re.sub(r"[ \u00a0,](?=\d{3}(?!\d))", "", t)      # 40 000 and 40,000 -> 40000
    return t                                               # case kept: nM is not nm


def _num(raw):
    raw = raw.strip().rstrip(".")
    if not raw:
        return None
    return raw.rstrip("0").rstrip(".") if "." in raw else raw


def figures(text):
    """Every (number, unit) in the text, normalised, as a set of strings."""
    out = set()
    for raw, unit in FIGURE.findall(normalise(text)):
        n = _num(raw)
        if n:
            out.add(n + unit)
    return out


def figures_with_number(text):
    """Same, but keep the bare number alongside, for the weak tier."""
    out = set()
    for raw, unit in FIGURE.findall(normalise(text)):
        n = _num(raw)
        if n:
            out.add((n + unit, n))
    return out


BARE = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)(?![\w])")


def numbers(text):
    """Every bare number on the page, for when the unit is in a row label."""
    return {n for n in (_num(m) for m in BARE.findall(normalise(text))) if n}


def main():
    strict = "--strict" in sys.argv
    sources = sorted(glob.glob(PATTERN))
    if not sources:
        print("searched: %s" % PATTERN)
        print("NO SOURCES FOUND. This is a failure, not a pass.")
        return 1

    n_sources = len(sources)
    no_params, no_page, checked_sources = [], [], []
    total_figs = agree = 0
    drift, weak = [], []

    for path in sources:
        module = os.path.basename(os.path.dirname(path))
        page_path = os.path.join(os.path.dirname(path), "spec.md")
        try:
            doc = yaml.safe_load(open(path, encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            drift.append((module, "-", "-", "spec.yml did not parse: %s" % exc))
            continue

        params = []
        for step in (doc.get("process_steps") or []):
            for key, val in (step.get("parameters") or {}).items():
                params.append((step.get("id", "?"), key, str(val)))
        if not params:
            no_params.append(module)
            continue
        if not os.path.exists(page_path):
            no_page.append(module)
            continue

        page_text = open(page_path, encoding="utf-8").read()
        page_figs = figures(page_text)
        page_nums = numbers(page_text)
        checked_sources.append(module)
        for step_id, key, val in params:
            for fig, num in figures_with_number(val):
                total_figs += 1
                if fig in page_figs:
                    agree += 1
                elif num in page_nums:
                    weak.append((module, step_id, key, fig))
                else:
                    drift.append((module, step_id, key, fig))

    print("searched: %s" % PATTERN)
    print("")
    print("POPULATIONS")
    print("  %3d source(s) found" % n_sources)
    print("  %3d carry no `parameters` at all, so nothing here can be checked" % len(no_params))
    print("  %3d carry `parameters` but have no spec.md beside them" % len(no_page))
    print("  %3d compared against their page" % len(checked_sources))
    print("  %3d figure(s) extracted from those" % total_figs)
    print("      %3d MATCH   number and unit both on the page" % agree)
    print("      %3d weak    number on the page, unit not beside it. Not agreement."
          % len(weak))
    print("      %3d ABSENT  the number is nowhere on the page" % len(drift))
    if total_figs:
        print("  %.0f%% match, %.0f%% weak, %.0f%% absent"
              % (100.0 * agree / total_figs, 100.0 * len(weak) / total_figs,
                 100.0 * len(drift) / total_figs))
    print("")

    if no_params:
        print("NOT CHECKED — no `parameters` (%d): %s" % (len(no_params), ", ".join(no_params)))
        print("")

    if weak:
        print("WEAK — the number is on the page and the unit is not beside it (%d)" % len(weak))
        print("  This is the corpus's normal table format, so most of these are fine.")
        print("  They are listed because this check cannot tell a real match from a coincidence.")
        for module, step_id, key, fig in weak[:12]:
            print("  %-26s %-26s %-22s %s" % (module, step_id, key, fig))
        if len(weak) > 12:
            print("  ... and %d more" % (len(weak) - 12))
        print("")

    if drift:
        print("ABSENT — the source states a figure its page does not carry at all (%d)" % len(drift))
        for module, step_id, key, fig in drift:
            print("  %-26s %-26s %-22s %s" % (module, step_id, key, fig))
        print("")
        print("A figure on one side only means the two disagree. It does not say which is wrong.")
    else:
        print("Nothing absent. Every extracted figure appears on its page in some form.")

    if total_figs == 0:
        print("")
        print("ZERO FIGURES EXTRACTED. Treat this as a failure of the check, not a pass.")
        return 1

    if drift and strict:
        return 1
    if drift:
        print("advisory: %d absent; pass --strict to fail on them. Weak never fails."
              % len(drift))
    return 0


if __name__ == "__main__":
    sys.exit(main())
