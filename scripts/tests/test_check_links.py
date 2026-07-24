"""Tests for scripts/check-links.py — the link-failure classifier.

These lock down the behavior that issues #193 and #199 were about: a failure is
judged by what it says about the *link*, never by which vendor served it. Before
this classifier the wrapper matched a hand-maintained domain list against the
literal string "HTTP/2 protocol error", so every newly crawler-hostile vendor
turned the PR gate red until someone landed a config change.

The JSON fixtures below are real shapes captured from lychee 0.24.2, including
the two that are easy to get wrong:

  * A mistyped hostname and a vendor resetting the connection produce the
    *identical* code-less "Connection failed" status. Only a DNS lookup
    separates them, which is why host_resolves exists.
  * When a URL repeats across files, lychee reports the repeats from its in-run
    cache with the status detail stripped ("Error (cached)"). Those entries carry
    no evidence of their own and must inherit the URL's established verdict.

Every test runs offline: socket.getaddrinfo is monkeypatched, and _run_lychee is
stubbed for the end-to-end exit-code tests.
"""

import importlib.util
import socket
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "check-links.py"


def _load_module():
    # The script is hyphenated, so it cannot be imported by name.
    spec = importlib.util.spec_from_file_location("check_links", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cl = _load_module()


# Hosts the fake resolver knows about. Anything else raises gaierror, standing
# in for NXDOMAIN.
RESOLVABLE = {
    "www.cytivalifesciences.com",
    "www.sigmaaldrich.com",
    "www.sonicator.com",
    "github.com",
    "doi.org",
}


@pytest.fixture(autouse=True)
def fake_dns(monkeypatch):
    """Resolve only known hosts, and never touch the network."""

    def getaddrinfo(host, *args, **kwargs):
        if host in RESOLVABLE:
            return [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (host, 0))]
        raise socket.gaierror(socket.EAI_NONAME, "Name or service not known")

    monkeypatch.setattr(socket, "getaddrinfo", getaddrinfo)
    cl.host_resolves.cache_clear()
    yield
    cl.host_resolves.cache_clear()


# --- fixture builders -------------------------------------------------------


def entry(url, status, line=1):
    return {"url": url, "status": status, "span": {"line": line, "column": 1}}


def coded(url, code, line=1):
    return entry(url, {"text": f"Rejected status code: {code}", "code": code}, line)


def network(url, detail, line=1):
    return entry(
        url,
        {"text": f"Network error: {detail} (error sending request)", "details": detail},
        line,
    )


def cached(url, line=1):
    """lychee's detail-stripped repeat of a URL seen earlier in the same run."""
    return entry(url, {"text": "Error (cached)"}, line)


H2_DETAIL = "HTTP/2 protocol error. Server may not support HTTP/2 properly"
CONN_DETAIL = "Connection failed. Check network connectivity and firewall settings"

CYTIVA = "https://www.cytivalifesciences.com/en/us/products/items/hitrap-butyl-hp-p-05631"
DEAD_PAGE = "https://github.com/nucleus-eng/nucleus-docs/definitely-not-a-real-page"
TYPO_HOST = "https://www.sigmaaldrichh.com/US/en/product/sial/a2939"


def report(error_map=None, timeout_map=None, **totals):
    base = {
        "total": 0,
        "successful": 0,
        "errors": 0,
        "excludes": 0,
        "error_map": error_map or {},
        "timeout_map": timeout_map or {},
    }
    base.update(totals)
    return base


def verdicts(rep):
    """URL -> verdict, for a report with one entry per URL."""
    return {f["url"]: f["verdict"] for f in cl.collect_findings(rep)}


# --- classification: the link is wrong -------------------------------------


@pytest.mark.parametrize("code", [404, 410])
def test_gone_status_is_a_hard_failure(code):
    """404/410 is the one signal that reliably means the link itself is wrong."""
    v = verdicts(report({"a.md": [coded(DEAD_PAGE, code)]}))
    assert v[DEAD_PAGE] == cl.HARD_FAIL


def test_unresolvable_host_is_a_hard_failure():
    """A mistyped domain is the most common real authoring error.

    It arrives as a code-less "Connection failed", identical to vendor noise, so
    tolerating all network errors would silently swallow it.
    """
    v = verdicts(report({"a.md": [network(TYPO_HOST, CONN_DETAIL)]}))
    assert v[TYPO_HOST] == cl.HARD_FAIL


def test_missing_local_file_is_a_hard_failure():
    """A broken relative link is what 404s the deployed site."""
    url = "file:///repo/docs/modules/modules-main.html"
    v = verdicts(report({"a.md": [network(url, "Cannot find file")]}))
    assert v[url] == cl.HARD_FAIL


def test_url_with_no_host_is_a_hard_failure():
    v = verdicts(report({"a.md": [network("https://", CONN_DETAIL)]}))
    assert v["https://"] == cl.HARD_FAIL


# --- classification: tolerated noise ---------------------------------------


def test_http2_reset_on_a_live_host_is_tolerated():
    """Issue #199: Cytiva behaves exactly like Sigma, with no config entry."""
    v = verdicts(report({"a.md": [network(CYTIVA, H2_DETAIL)]}))
    assert v[CYTIVA] == cl.TOLERATED


def test_no_domain_allowlist_exists():
    """The fix is structural: nothing in the script names a vendor.

    If a domain list creeps back in, #193/#199 recur for the next vendor.
    """
    source = SCRIPT.read_text()
    for vendor in ("sigmaaldrich", "cytivalifesciences", "sonicator"):
        assert vendor not in source.lower().replace("#193", "").replace("#199", "")


@pytest.mark.parametrize("code", [401, 403, 429, 500, 502, 503, 504])
def test_refused_and_hiccup_statuses_are_tolerated(code):
    """Issue #193: a 503 says the server had a bad moment, not that we are wrong."""
    url = "https://www.sonicator.com/products/q700-sonicator"
    v = verdicts(report({"a.md": [coded(url, code)]}))
    assert v[url] == cl.TOLERATED


@pytest.mark.parametrize("code", [400, 405, 406, 451])
def test_other_4xx_are_tolerated(code):
    """Bot-shaped rejections. Only 404/410 speak to the link's validity."""
    url = "https://doi.org/10.1126/science.274.5294.1859"
    v = verdicts(report({"a.md": [coded(url, code)]}))
    assert v[url] == cl.TOLERATED


def test_403_is_reported_not_silently_accepted():
    """403 used to sit in .lychee.toml's accept list, making it invisible.

    It is still non-blocking, but it must now show up as a finding so a vendor
    quietly refusing every request is at least visible.
    """
    url = "https://doi.org/10.1126/science.274.5294.1859"
    findings = cl.collect_findings(report({"a.md": [coded(url, 403)]}))
    assert len(findings) == 1
    assert findings[0]["verdict"] == cl.TOLERATED
    assert "403" in findings[0]["reason"]


def test_timeouts_are_reported_and_tolerated():
    """Regression test: timeouts live in timeout_map, absent from error_map.

    The previous wrapper read only error_map, so every timeout vanished without
    a word while the summary line still claimed success.
    """
    url = "https://www.sonicator.com/products/q700-sonicator"
    findings = cl.collect_findings(
        report(timeout_map={"a.md": [entry(url, {"text": "Timeout"})]})
    )
    assert len(findings) == 1
    assert findings[0]["verdict"] == cl.TOLERATED


# --- cached repeats inherit their URL's verdict -----------------------------


def test_cached_repeat_of_tolerated_url_is_tolerated():
    rep = report(
        {
            "a.md": [network(CYTIVA, H2_DETAIL)],
            "b.md": [cached(CYTIVA)],
        }
    )
    findings = cl.collect_findings(rep)
    assert len(findings) == 2
    assert {f["verdict"] for f in findings} == {cl.TOLERATED}


def test_cached_repeat_of_dead_url_still_fails():
    """The dangerous direction: a stripped repeat must not launder a 404."""
    rep = report(
        {
            "a.md": [coded(DEAD_PAGE, 404)],
            "b.md": [cached(DEAD_PAGE)],
        }
    )
    findings = cl.collect_findings(rep)
    assert len(findings) == 2
    assert {f["verdict"] for f in findings} == {cl.HARD_FAIL}


def test_cached_repeat_seen_before_its_source_still_inherits():
    """Order must not matter — lychee does not guarantee file ordering."""
    rep = report(
        {
            "a.md": [cached(DEAD_PAGE)],
            "b.md": [coded(DEAD_PAGE, 404)],
        }
    )
    assert {f["verdict"] for f in cl.collect_findings(rep)} == {cl.HARD_FAIL}


def test_orphan_cached_entry_defaults_to_tolerated():
    """With no evidence anywhere for the URL, do not invent a failure."""
    rep = report({"a.md": [cached(CYTIVA)]})
    assert verdicts(rep)[CYTIVA] == cl.TOLERATED


# --- end-to-end exit codes -------------------------------------------------


@pytest.fixture
def stub_lychee(monkeypatch):
    """Stub _run_lychee, returning a different report per pass."""

    def install(internal=None, external=None):
        def fake(args, offline):
            return (internal if offline else external) or report()

        monkeypatch.setattr(cl, "_run_lychee", fake)

    return install


def test_clean_run_exits_zero(stub_lychee, capsys):
    stub_lychee()
    assert cl.main() == cl.EXIT_OK
    assert "no broken links" in capsys.readouterr().out


def test_tolerated_only_run_exits_zero(stub_lychee, capsys):
    """The whole point: 87 vendor failures must not fail the build."""
    stub_lychee(external=report({"a.md": [network(CYTIVA, H2_DETAIL)]}))
    assert cl.main() == cl.EXIT_OK
    out = capsys.readouterr().out
    assert "tolerated" in out
    assert "no broken links" in out


def test_dead_link_exits_one(stub_lychee):
    stub_lychee(external=report({"a.md": [coded(DEAD_PAGE, 404)]}))
    assert cl.main() == cl.EXIT_FAILURES


def test_broken_internal_link_exits_one(stub_lychee):
    """Internal links block unconditionally — they break the deployed site."""
    url = "file:///repo/docs/modules/gone.md"
    stub_lychee(internal=report({"a.md": [network(url, "Cannot find file")]}))
    assert cl.main() == cl.EXIT_FAILURES


def test_offline_only_skips_the_network_pass(stub_lychee, monkeypatch):
    """--offline-only must not fetch anything, even if externals would fail."""
    calls = []

    def fake(args, offline):
        calls.append(offline)
        return report({"a.md": [coded(DEAD_PAGE, 404)]}) if not offline else report()

    monkeypatch.setattr(cl, "_run_lychee", fake)
    monkeypatch.setattr("sys.argv", ["check-links.py", "--offline-only", "docs/"])
    assert cl.main() == cl.EXIT_OK
    assert calls == [True]


def test_unparseable_output_exits_two(monkeypatch):
    """Tooling breakage must be distinguishable from a link failure.

    Both used to exit 1, so a broken lychee install read as broken docs.
    """

    def boom(args, offline):
        raise cl.CannotRun("lychee is not installed")

    monkeypatch.setattr(cl, "_run_lychee", boom)
    assert cl.main() == cl.EXIT_CANNOT_RUN


def test_blame_changed_requires_a_ref(monkeypatch):
    monkeypatch.setattr("sys.argv", ["check-links.py", "--blame-changed"])
    assert cl.main() == cl.EXIT_CANNOT_RUN


# --- blame partitioning ----------------------------------------------------


def test_rot_in_an_untouched_file_does_not_block(stub_lychee, monkeypatch, capsys):
    stub_lychee(external=report({"docs/old.md": [coded(DEAD_PAGE, 404)]}))
    monkeypatch.setattr(cl, "changed_files", lambda ref: {"docs/mine.md"})
    monkeypatch.setattr(
        "sys.argv", ["check-links.py", "--blame-changed", "origin/main", "docs/"]
    )
    assert cl.main() == cl.EXIT_OK
    out = capsys.readouterr().out
    assert "pre-existing" in out
    assert DEAD_PAGE in out  # still reported, just not blocking


def test_rot_in_a_touched_file_blocks(stub_lychee, monkeypatch):
    stub_lychee(external=report({"docs/mine.md": [coded(DEAD_PAGE, 404)]}))
    monkeypatch.setattr(cl, "changed_files", lambda ref: {"docs/mine.md"})
    monkeypatch.setattr(
        "sys.argv", ["check-links.py", "--blame-changed", "origin/main", "docs/"]
    )
    assert cl.main() == cl.EXIT_FAILURES


def test_internal_failure_blocks_even_when_unblamed(stub_lychee, monkeypatch):
    """Blame partitioning applies to external rot only.

    A broken relative link in an untouched file still breaks the built site, so
    it must block regardless.
    """
    url = "file:///repo/docs/modules/gone.md"
    stub_lychee(internal=report({"docs/old.md": [network(url, "Cannot find file")]}))
    monkeypatch.setattr(cl, "changed_files", lambda ref: {"docs/mine.md"})
    monkeypatch.setattr(
        "sys.argv", ["check-links.py", "--blame-changed", "origin/main", "docs/"]
    )
    assert cl.main() == cl.EXIT_FAILURES


def test_undiffable_ref_falls_back_to_blocking_everything(stub_lychee, monkeypatch):
    """If git cannot answer, fail closed rather than silently passing rot."""
    stub_lychee(external=report({"docs/old.md": [coded(DEAD_PAGE, 404)]}))
    monkeypatch.setattr(cl, "changed_files", lambda ref: None)
    monkeypatch.setattr(
        "sys.argv", ["check-links.py", "--blame-changed", "origin/main", "docs/"]
    )
    assert cl.main() == cl.EXIT_FAILURES
