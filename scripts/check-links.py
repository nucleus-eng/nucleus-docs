#!/usr/bin/env python3
"""
check-links.py — lychee wrapper that classifies link failures by what they
actually tell you about the link.

Two passes, both over the whole corpus:

  Pass A (internal)  lychee --offline. Relative and root-relative links only, no
                     network. Deterministic and fast (~20 ms for all of docs/).
                     A broken internal link 404s the deployed site, so any
                     failure here blocks unconditionally.

  Pass B (external)  Network check. Every failure is classified as either a HARD
                     FAIL (the link is wrong) or TOLERATED noise (our bot was
                     blocked, or the server hiccuped).

The classification axis is what the response says about the *link*, not which
vendor served it:

  * A 404/410, or a hostname that does not resolve, means the link is wrong.
    Deterministic and actionable — hard failure.
  * A 403/429/5xx/timeout/TLS error/HTTP-2 reset means the crawler was refused
    or the server had a bad moment. It says nothing about whether the link is
    valid, and it is not reproducible — tolerated, but reported.

This replaces an earlier per-domain allowlist keyed on the literal string
"HTTP/2 protocol error", which meant every newly crawler-hostile vendor turned
the PR gate red until someone landed a config change (issues #193, #199).

Blame partitioning: with --blame-changed, only hard failures in files the branch
modified affect the exit status. Pre-existing rot elsewhere is still found and
reported, but does not block a PR that did not cause it. The scheduled link-rot
sweep runs without the flag, so there every hard failure counts.

Usage:
    python3 scripts/check-links.py                    # both passes over docs/
    python3 scripts/check-links.py docs/ templates/   # both passes, given paths
    python3 scripts/check-links.py <file.md>          # both passes, one file
    python3 scripts/check-links.py --offline-only     # Pass A alone (no network)
    python3 scripts/check-links.py --blame-changed origin/main docs/

Exit codes:
    0  no blocking failures (tolerated noise and non-blocking rot may be listed)
    1  blocking link failures found
    2  the check could not run (lychee missing, or unparsable output)
"""

import json
import shutil
import socket
import subprocess
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from urllib.parse import urlsplit

LYCHEE_CONFIG = ".lychee.toml"

EXIT_OK = 0
EXIT_FAILURES = 1
EXIT_CANNOT_RUN = 2

# Status codes that mean the resource is gone — the link itself is wrong.
DEAD_CODES = {404, 410}

# Verdicts
HARD_FAIL = "hard_fail"
TOLERATED = "tolerated"


class CannotRun(Exception):
    """lychee could not be run, or produced output we cannot interpret."""


def _run_lychee(args: list[str], offline: bool) -> dict:
    """Run lychee and return its parsed JSON report."""
    if not shutil.which("lychee"):
        raise CannotRun(
            "lychee is not installed. Run ./setup.sh or: brew install lychee"
        )

    cmd = ["lychee", "--config", LYCHEE_CONFIG, "--format", "json", "--no-progress"]
    if offline:
        cmd.append("--offline")
    cmd += args

    result = subprocess.run(cmd, capture_output=True, text=True)

    # lychee appends free-text hints after the JSON document, so decode just the
    # first JSON value rather than depending on the exact hint wording.
    start = result.stdout.find("{")
    if start == -1:
        raise CannotRun(
            "lychee produced no JSON output.\n"
            f"exit={result.returncode}\n"
            f"stdout: {result.stdout[:500]}\n"
            f"stderr: {result.stderr[:500]}"
        )
    try:
        report, _ = json.JSONDecoder().raw_decode(result.stdout[start:])
    except json.JSONDecodeError as exc:
        raise CannotRun(
            f"could not parse lychee JSON output: {exc}\n"
            f"stdout: {result.stdout[:500]}"
        ) from exc
    return report


@lru_cache(maxsize=None)
def host_resolves(host: str) -> bool:
    """Whether a hostname resolves in DNS.

    lychee reports a mistyped hostname and a vendor closing the connection with
    the *same* code-less "Connection failed" error, so the JSON alone cannot
    tell "this domain does not exist" (a real authoring mistake) from "this
    server hung up on our crawler" (noise). Resolving the name settles it.
    """
    if not host:
        return False
    try:
        socket.getaddrinfo(host, None)
    except socket.gaierror:
        return False
    except OSError:
        # Anything other than a resolution failure (e.g. no network at all) is
        # not evidence that the domain is dead — do not blame the link for it.
        return True
    return True


def classify(entry: dict) -> tuple[str, str]:
    """Classify one lychee error entry as (verdict, reason).

    Entries whose status carries no code and no recognizable detail — lychee's
    "Error (cached)" repeats — return a verdict of None so the caller can make
    them inherit the verdict already established for that URL.
    """
    status = entry.get("status", {})
    code = status.get("code")

    if code is not None:
        if code in DEAD_CODES:
            return HARD_FAIL, f"HTTP {code} — resource is gone"
        return TOLERATED, f"HTTP {code}"

    url = entry.get("url", "")
    split = urlsplit(url)

    if split.scheme == "file":
        # A relative or root-relative link that resolves to nothing on disk.
        # This is the failure that 404s the deployed site.
        return HARD_FAIL, "local file not found"

    host = split.hostname or ""
    if not host:
        return HARD_FAIL, "no host in URL"

    if not host_resolves(host):
        return HARD_FAIL, f"{host} does not resolve"

    detail = status.get("details") or status.get("text") or "network error"
    return TOLERATED, detail


def _is_detail_less(entry: dict) -> bool:
    """True for lychee's stripped 'Error (cached)' repeats.

    When the same URL appears in several files, lychee reports the repeats from
    its in-run cache with the status detail removed. Those entries carry no
    information of their own and must inherit the verdict established for the
    URL elsewhere in the report.
    """
    status = entry.get("status", {})
    if status.get("code") is not None:
        return False
    text = (status.get("text") or "").strip()
    return "cached" in text.lower() and not status.get("details")


def collect_findings(report: dict) -> list[dict]:
    """Flatten a lychee report into classified findings.

    Reads error_map and timeout_map. Timeouts live in their own bucket and are
    absent from error_map, so a wrapper that reads only error_map drops them
    silently — which is what happened before this rewrite.
    """
    raw = []
    for filepath, entries in report.get("error_map", {}).items():
        for entry in entries:
            raw.append((filepath, entry, None))
    for filepath, entries in report.get("timeout_map", {}).items():
        for entry in entries:
            raw.append((filepath, entry, "request timed out"))

    # First pass: classify everything that carries its own information.
    verdict_by_url: dict[str, str] = {}
    classified = []
    for filepath, entry, forced_reason in raw:
        url = entry.get("url", "")
        if forced_reason is not None:
            verdict, reason = TOLERATED, forced_reason
        elif _is_detail_less(entry):
            verdict, reason = None, "cached repeat"
        else:
            verdict, reason = classify(entry)

        if verdict == HARD_FAIL:
            # A hard verdict for a URL applies to every occurrence of that URL,
            # including detail-less repeats in other files.
            verdict_by_url[url] = HARD_FAIL
        elif verdict == TOLERATED:
            verdict_by_url.setdefault(url, TOLERATED)

        classified.append((filepath, entry, verdict, reason))

    # Second pass: resolve inheritance, then apply URL-level hard verdicts.
    findings = []
    for filepath, entry, verdict, reason in classified:
        url = entry.get("url", "")
        known = verdict_by_url.get(url)
        if verdict is None:
            # Unknown on its own; inherit. Default to tolerated rather than
            # inventing a failure from an entry that carries no evidence.
            verdict = known or TOLERATED
            reason = f"{reason} (inherited: {verdict})"
        elif known == HARD_FAIL:
            verdict = HARD_FAIL
        findings.append(
            {
                "file": filepath,
                "url": url,
                "line": entry.get("span", {}).get("line", "?"),
                "verdict": verdict,
                "reason": reason,
            }
        )
    return findings


def changed_files(ref: str) -> set[str]:
    """Files modified relative to ref. Empty set if git cannot answer."""
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=d", f"{ref}...HEAD"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(
            f"⚠️  could not diff against {ref} "
            f"({result.stderr.strip()}) — treating every failure as blocking",
            file=sys.stderr,
        )
        return None
    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


@lru_cache(maxsize=1)
def _repo_root() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def _relative(path: str) -> str:
    """lychee reports absolute paths for some inputs; git reports repo-relative."""
    root = _repo_root()
    if root and path.startswith(root + "/"):
        return path[len(root) + 1 :]
    return path


def _print_group(heading: str, findings: list[dict]) -> None:
    print(f"\n{heading}\n")
    by_file = defaultdict(list)
    for f in findings:
        by_file[f["file"]].append(f)
    for filepath, entries in sorted(by_file.items()):
        print(f"  {_relative(filepath)}")
        for f in sorted(entries, key=lambda e: str(e["line"])):
            print(f"    [{f['line']}] {f['url']} — {f['reason']}")


def _print_tolerated(findings: list[dict]) -> None:
    """Summarize tolerated noise by host and reason rather than listing all of it."""
    if not findings:
        return
    grouped = Counter(
        (urlsplit(f["url"]).hostname or "?", f["reason"].split(" (inherited")[0])
        for f in findings
    )
    total = len(findings)
    print(f"\nℹ️  {total} tolerated failure(s) — blocked crawler or server hiccup,")
    print("   not evidence of a broken link:\n")
    for (host, reason), count in sorted(grouped.items(), key=lambda kv: -kv[1]):
        print(f"    {count:4d}  {host}  —  {reason}")


def _is_web(url: str) -> bool:
    return urlsplit(url).scheme in ("http", "https")


def run_pass(label: str, paths: list[str], offline: bool) -> list[dict]:
    report = _run_lychee(paths, offline=offline)
    findings = collect_findings(report)

    # The two passes overlap: the network pass also resolves internal links, so
    # without this a broken relative link would be reported by both. Pass A owns
    # internal links; Pass B owns web links only.
    if offline:
        findings = [f for f in findings if not _is_web(f["url"])]
    else:
        findings = [f for f in findings if _is_web(f["url"])]

    successful = report.get("successful", 0)
    total = report.get("total", 0)
    excludes = report.get("excludes", 0)
    hard = sum(1 for f in findings if f["verdict"] == HARD_FAIL)
    print(
        f"{label}: {successful}/{total} OK, {hard} broken, "
        f"{len(findings) - hard} tolerated, {excludes} excluded"
    )
    return findings


def main() -> int:
    argv = sys.argv[1:]

    offline_only = "--offline-only" in argv
    argv = [a for a in argv if a != "--offline-only"]

    blame_ref = None
    if "--blame-changed" in argv:
        i = argv.index("--blame-changed")
        if i + 1 >= len(argv):
            print("ERROR: --blame-changed requires a git ref", file=sys.stderr)
            return EXIT_CANNOT_RUN
        blame_ref = argv[i + 1]
        del argv[i : i + 2]

    paths = argv or ["docs/"]

    try:
        internal = run_pass("internal (offline)", paths, offline=True)
        external = [] if offline_only else run_pass("external", paths, offline=False)
    except CannotRun as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return EXIT_CANNOT_RUN

    # Internal links are ours to get right, so a failure blocks no matter which
    # files the branch touched.
    blocking = [f for f in internal if f["verdict"] == HARD_FAIL]
    tolerated = [f for f in internal + external if f["verdict"] == TOLERATED]
    external_broken = [f for f in external if f["verdict"] == HARD_FAIL]

    unblamed = []
    if blame_ref is None:
        blocking += external_broken
    else:
        touched = changed_files(blame_ref)
        if touched is None:
            blocking += external_broken
        else:
            for f in external_broken:
                if _relative(f["file"]) in touched:
                    blocking.append(f)
                else:
                    unblamed.append(f)

    _print_tolerated(tolerated)

    if unblamed:
        _print_group(
            f"⚠️  {len(unblamed)} pre-existing broken link(s) in files this branch "
            "did not modify — not blocking, but they need fixing:",
            unblamed,
        )

    if blocking:
        _print_group(f"❌ {len(blocking)} broken link(s):", blocking)
        return EXIT_FAILURES

    if unblamed:
        print("\n✅ nothing broken in the files this branch modified")
    else:
        print("\n✅ no broken links")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
