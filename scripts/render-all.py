#!/usr/bin/env python3
"""Run every generator in this repository, in one command.

THE LIST WAS A MEMORY AND THAT IS WHY THIS EXISTS. Four scripts generate
content here. Two write into markers on pages and two write review material
that lives outside `docs/`. Nothing named all four, so a regeneration was
whatever loops the last person remembered, and `render-meet.py` was left out of
every sweep because it has no `--embed` and therefore no page to go stale.

    python3 scripts/render-all.py           # regenerate everything, report changes
    python3 scripts/render-all.py --check   # change nothing, exit 1 if stale

WHAT EACH ONE WRITES, AND WHY TWO OF THEM WRITE TO tmp/.

  render-composition.py  gen:composition-diagram markers, one module per page
  render-position.py     gen:position markers, one module per page

Both of those grew a `--check` for this driver. `--check` is `--embed` without
the write: same comparison, same tri-state, no file touched. Without it this
driver could only check the two artifacts under tmp/, which is the smaller half
of what it generates and the half least likely to go stale.
  render-meet.py         tmp/generated/, because a meet spans several modules
  render-posets.py       tmp/generated/, because the orders span the whole corpus

A MEET HAS NO PAGE AND MUST NOT BE GIVEN ONE HERE. The cross-demo meet's
outcome slot reports NO COMMON ANCESTOR over aTc Cascade, London Cascade and pH
Cascade: the class that would hold them is not written, deliberately. Embedding
the figure on a page would need that page to exist, and creating it would settle
a modeling question by making a generator convenient. So the meet is review
material next to the poset draft, regenerated on every run and diffable.

WHICH MEETS ARE WORTH RENDERING, MEASURED RATHER THAN LISTED. A meet over one
leg is the composition diagram restated, and three of the four cascades have
exactly one leg. Only chicago-cascade is multi-leg on its own. The set below is
Jon's, 2026-09-21: the two Chicago integration paths plus the London demo, which
is three legs and every detector in the corpus.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MODULES = REPO / "docs" / "modules"
OUT = REPO / "tmp" / "generated"

# Each entry is an output file and the arguments that produce it. A meet over one
# leg is omitted: it restates that module's own composition diagram.
MEETS = [
    ("meet-chicago-london.md", ["chicago-cascade", "london-cascade"],
     "The two Chicago integration paths and the London demo. Three legs, "
     "one per detector in the corpus."),
    ("meet-chicago.md", ["chicago-cascade"],
     "Chicago alone. Two legs, the pH path and the aTc path."),
]


def run(args: list[str]) -> tuple[int, str, str]:
    p = subprocess.run([sys.executable, *args], cwd=REPO,
                       capture_output=True, text=True)
    return p.returncode, p.stdout, p.returncode and p.stderr or p.stderr


def main() -> int:
    check = "--check" in sys.argv
    stale: list[str] = []

    # --- the two that write into page markers
    for script, label in (("render-composition.py", "composition diagram"),
                          ("render-position.py", "position line")):
        counts: dict[str, int] = {}
        mode = "--check" if check else "--embed"
        if script == "render-composition.py":
            # One file at a time, because this script's input is one module.
            # rc 1 means STALE and is not a failure; anything else is.
            for yml in sorted(MODULES.glob("*/spec.yml")):
                rc, out, err = run(["scripts/render-composition.py",
                                    str(yml.relative_to(REPO)), mode])
                if rc not in (0, 1):
                    print(f"FAILED: {yml}\n{err}", file=sys.stderr)
                    return 2
                verdict = out.strip().splitlines()[-1].split(":")[0]
                counts[verdict] = counts.get(verdict, 0) + 1
        else:
            rc, out, err = run(["scripts/render-position.py", mode])
            if rc not in (0, 1):
                print(f"FAILED: {script}\n{err}", file=sys.stderr)
                return 2
            for line in out.strip().splitlines():
                n, _, k = line.strip().partition("  ")
                counts[k.strip()] = int(n)
        print(f"{label}: " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())))
        for word in ("updated", "STALE"):
            if counts.get(word):
                stale.append(f"{counts[word]} {label}(s)")

    # --- the two that write review material
    # A CHECK MUST NOT TOUCH THE FILESYSTEM, INCLUDING BY MAKING A DIRECTORY.
    # This line ran unconditionally and created tmp/generated/ during --check,
    # which then swallowed a `mv` of the real directory into itself.
    if not check:
        OUT.mkdir(parents=True, exist_ok=True)
    jobs = [(name, ["scripts/render-meet.py", *args], note) for name, args, note in MEETS]
    jobs.append(("posets.md", ["scripts/render-posets.py"],
                 "Every order this corpus generates, and the relations that are not orders."))
    for name, args, note in jobs:
        rc, out, err = run(args)
        if rc:
            print(f"FAILED: {' '.join(args)}\n{err}", file=sys.stderr)
            return 2
        body = (f"<!-- Generated by scripts/render-all.py. Do not edit. -->\n"
                f"<!-- {' '.join(args)} -->\n\n{note}\n\n"
                + ("```mermaid\n" + out.rstrip() + "\n```\n" if out.lstrip().startswith("flowchart")
                   else out.rstrip() + "\n")
                + "\n<!-- diagnostics -->\n```\n" + err.rstrip() + "\n```\n")
        dest = OUT / name
        was = dest.read_text() if dest.is_file() else None
        if was == body:
            print(f"{name}: unchanged")
        elif was is None and check:
            # tmp/ IS GITIGNORED, SO A MISSING FILE IS NOT STALENESS. On a fresh
            # checkout none of these exist, and reporting three stale artifacts
            # there would make --check fail everywhere and mean nothing. A file
            # that exists and disagrees with its source is the real finding.
            print(f"{name}: absent, not generated here")
        elif check:
            print(f"{name}: STALE")
            stale.append(name)
        else:
            dest.write_text(body)
            print(f"{name}: {'written' if was is None else 'updated'}")
            stale.append(name)

    if check and stale:
        print(f"\n{len(stale)} generated artifact(s) are stale: " + ", ".join(stale),
              file=sys.stderr)
        return 1
    print(f"\n4 generators run. "
          + (f"{len(stale)} artifact group(s) changed: " + ", ".join(stale) if stale
             else "Nothing changed; every generated artifact was already current."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
