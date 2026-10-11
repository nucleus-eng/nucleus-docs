"""Pin what a link-check failure is allowed to say about the corpus.

The axis this script claims is "what the response says about the *link*, not
which vendor served it". A 404 comes from the authoritative server and is about
the link. A refused crawler is about the crawler. A hostname that does not
resolve is about the RESOLVER, and no response was received at all.

That last one used to be a hard failure. On 2026-09-29 four correct links were
the only red on this check for days, because `ecgrc.net` returned NXDOMAIN on
this machine while google.com, github.com, sigmaaldrich.com and doi.org all
resolved on the same resolver, and the host resolves on the internet.
"""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-links.py"


@pytest.fixture(scope="module")
def mod():
    spec = importlib.util.spec_from_file_location("check_links", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_a_404_is_still_a_hard_failure(mod):
    """It comes from the authoritative server, so it is about the link."""
    verdict, reason = mod.classify({"url": "https://example.com/gone", "status": {"code": 404}})
    assert verdict == mod.HARD_FAIL
    assert "gone" in reason


def test_a_refused_crawler_is_tolerated(mod):
    """A 403 says the bot was refused, not that the link is wrong."""
    verdict, _ = mod.classify({"url": "https://example.com/x", "status": {"code": 403}})
    assert verdict == mod.TOLERATED


def test_an_unresolvable_host_is_tolerated_not_a_hard_failure(mod, monkeypatch):
    """A resolver failure is a fact about this machine. It must not read as a
    statement about the corpus, and it must not turn the gate red."""
    monkeypatch.setattr(mod, "host_resolves", lambda h: False)
    verdict, reason = mod.classify(
        {"url": "https://ecgrc.net/index.php/product/a19/", "status": {"details": "dns error"}}
    )
    assert verdict == mod.TOLERATED
    assert "did not resolve from here" in reason
    assert "DNS, not the link" in reason


def test_a_link_with_no_host_is_still_a_hard_failure(mod):
    """Deterministic and local: the URL itself is malformed."""
    verdict, reason = mod.classify({"url": "https:///nowhere", "status": {"details": "bad"}})
    assert verdict == mod.HARD_FAIL
    assert "no host" in reason
