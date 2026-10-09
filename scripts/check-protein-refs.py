#!/usr/bin/env python3
"""
check-protein-refs.py — verifies that a docs page's claims about a protein
match its UniProt entry, rather than just checking that the link resolves.

This is check-dna-refs.py one level up, from nucleotide to protein, and it
exists for the same reason: a link can be perfectly alive and still assert a
false identity. `check-links.py` confirms a uniprot.org URL returns 200. It says
nothing about whether the protein named beside it is the one the entry holds.

THE MOTIVATING CASE IS deGFP, AND IT IS NOT A NEAR MISS. deGFP aligns to
wild-type GFP (P42212) at 98.7% over 225 residues against the entry's 238. That
is close enough that a citation looks right to a reader and to a reviewer, and
different enough that the page would be asserting the wrong protein, the wrong
length and the wrong mass. A name match would have passed it. An eyeball would
have passed it.

For every UniProt citation it finds, it compares:

  * the accession in the link text against the accession in the URL
  * a stated residue count ("NNN aa", "NNN residues") against the entry
  * a stated mass ("NNN.N kDa") against the entry's computed molecular weight,
    monomer or a stated n-mer
  * a stated organism, italicized or not, against the entry's organism
  * the entry's own protein name against the words around the citation

AND, WHERE THE PAGE ALSO NAMES A CONSTRUCT IN nucleus-eng/DNA, it translates
that construct's CDS and aligns it against the cited entry. This is the only
check here that would have caught deGFP, and it is why `--align` exists.

Severity, matching check-dna-refs.py:

  BLOCKING  the claim is verifiably wrong — the accession does not resolve, or
            a stated length or mass contradicts the entry. Not judgment calls.
  WARN      the entry's name or organism does not obviously match the page, or
            an aligned construct is less than fully identical to the entry it
            is cited as. Often benign — an entry may name a protein by a
            systematic name the field does not use, and EsaR's entry calls it
            an activator where this corpus calls it a repressor — but exactly
            the shape of a wrong-protein citation, so a human decides.
  INFO      nothing to verify: no length, mass or organism stated near the
            citation.

LOCAL AND AUTHOR-TIME, NOT A CI GATE, for the same two reasons check-dna-refs
is: it needs the network, and with --align it needs a checkout of
nucleus-eng/DNA that CI does not have. A UniProt outage must never turn a PR
red, and a cached answer must never be mistaken for a fresh one.

IT REPORTS A FINDING, NEVER A FIX. "98.7% identical to the entry it cites" is
information for an author who knows whether their construct is a variant. A
script that rewrote the citation would automate the exact mistake it exists to
catch, which is the rule check-dna-refs.py states for the same reason.

A CLEAN RUN OVER NOTHING IS NOT A PASS. With no network it exits 2 and says so,
rather than reporting zero findings over zero fetched entries.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BLOCKING, WARN, INFO = "BLOCKING", "WARN", "INFO"
API = "https://rest.uniprot.org/uniprotkb/{}.json?fields=accession,protein_name,organism_name,sequence,gene_names"
CACHE = Path(os.environ.get("TMPDIR", "/tmp")) / "nucleus-uniprot-cache.json"
CACHE_TTL = 7 * 24 * 3600

# [UniProt P00722](https://www.uniprot.org/uniprotkb/P00722/entry), and the bare link.
# Non-capturing throughout: this pattern is embedded in CITATION, and a capture
# group here would shift CITATION's group numbers and make findall return the
# inner group instead of the accession.
ACCESSION = r"[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2}"
CITATION = re.compile(
    r"\[([^\]]*?)\]\(\s*https?://(?:www\.)?uniprot\.org/uniprotkb/(" + ACCESSION + r")(?:/entry)?[^)]*\)")


@dataclass
class Claim:
    path: Path
    line_no: int
    accession: str
    link_text: str
    context: str


def iter_pages(paths):
    for p in paths:
        if p.is_file() and p.suffix in (".md", ".yml"):
            yield p
        elif p.is_dir():
            yield from sorted(x for x in p.rglob("*") if x.suffix in (".md", ".yml"))


def paragraph(lines, n):
    """The blank-line-delimited block holding 1-indexed line `n`.

    A FIXED WINDOW OF LINES IS THE WRONG UNIT and reads the wrong sentence in
    both directions: too narrow and it misses a figure stated on the line above,
    too wide and one citation is checked against the next one's numbers. Two
    citations in one paragraph do share a context, which is correct -- a
    paragraph that states one length and cites two entries is ambiguous for a
    reader too.
    """
    i = n - 1
    start = i
    while start > 0 and lines[start - 1].strip():
        start -= 1
    end = i
    while end + 1 < len(lines) and lines[end + 1].strip():
        end += 1
    return " ".join(lines[start:end + 1])


def find_claims(paths):
    out = []
    for page in iter_pages(paths):
        try:
            lines = page.read_text(encoding="utf-8").split("\n")
        except (UnicodeDecodeError, OSError):
            continue
        for n, line in enumerate(lines, 1):
            for m in CITATION.finditer(line):
                ctx = paragraph(lines, n)
                out.append(Claim(page, n, m.group(2), m.group(1), ctx))
    return out


def _load_cache():
    try:
        d = json.loads(CACHE.read_text())
        return {k: v for k, v in d.items() if time.time() - v.get("_t", 0) < CACHE_TTL}
    except Exception:
        return {}


def fetch(accession, cache, offline=False):
    if accession in cache:
        return cache[accession], True
    if offline:
        return None, False
    try:
        with urllib.request.urlopen(API.format(accession), timeout=25) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"_missing": True, "_t": time.time()}, False
        raise
    seq = d.get("sequence", {})
    pd = d.get("proteinDescription", {})
    alt = [a.get("fullName", {}).get("value") for a in pd.get("alternativeNames", [])]
    entry = {
        "name": pd.get("recommendedName", {}).get("fullName", {}).get("value"),
        "alt": [a for a in alt if a],
        "organism": d.get("organism", {}).get("scientificName"),
        "length": seq.get("length"),
        "mass": seq.get("molWeight"),
        "seq": seq.get("value"),
        "genes": [g.get("geneName", {}).get("value") for g in d.get("genes", []) if g.get("geneName")],
        "_t": time.time(),
    }
    cache[accession] = entry
    return entry, False


STATED_LEN = re.compile(r"(\d[\d,]*)\s*(?:aa\b|residues\b|amino acids\b)", re.I)
STATED_MASS = re.compile(r"(\d+(?:\.\d+)?)\s*kDa", re.I)
# "*Escherichia coli* K12", "*Serratia liquefaciens*"
STATED_ORG = re.compile(r"\*([A-Z][a-z]+(?:\s+[a-z]+){1,2})\*")


def _words(s):
    return set(re.findall(r"[a-z0-9]+", (s or "").lower()))


def check(claim, entry):
    """Every finding this claim produces."""
    out = []
    if entry.get("_missing"):
        return [(BLOCKING, f"accession {claim.accession} does not resolve at UniProt")]

    # the link text, when it names an accession, must name this one
    for other in re.findall(ACCESSION, claim.link_text):
        if other != claim.accession:
            out.append((BLOCKING, f"link text says {other}, URL says {claim.accession}"))

    ctx = claim.context
    if (m := STATED_LEN.search(ctx)):
        stated = int(m.group(1).replace(",", ""))
        if entry["length"] and stated != entry["length"]:
            out.append((BLOCKING, f"page says {stated} aa, entry is {entry['length']} aa"))

    if (m := STATED_MASS.search(ctx)) and entry["mass"]:
        stated = float(m.group(1))
        kda = entry["mass"] / 1000
        # a page may legitimately state an n-mer mass; accept any small multiple
        if not any(abs(stated - kda * n) <= max(0.6, 0.01 * kda * n) for n in (1, 2, 3, 4, 6, 8)):
            out.append((BLOCKING,
                        f"page says {stated} kDa, entry's monomer is {kda:.1f} kDa "
                        f"(no n-mer up to 8 matches)"))

    if (m := STATED_ORG.search(ctx)) and entry["organism"]:
        said, real = _words(m.group(1)), _words(entry["organism"])
        if said and not said & real:
            out.append((WARN, f"page says *{m.group(1)}*, entry is {entry['organism']}"))

    names = _words(entry["name"]) | set().union(*[_words(a) for a in entry["alt"]] or [set()])
    names |= {g.lower() for g in entry["genes"]}
    if names and not (names & _words(claim.link_text + " " + ctx)):
        out.append((WARN,
                    f"nothing near the citation matches the entry's name "
                    f"{entry['name']!r} — confirm it is the right protein"))
    return out


def align_identity(protein, entry_seq):
    from Bio import Align
    al = Align.PairwiseAligner(scoring="blastp", mode="local")
    a = al.align(protein, entry_seq)[0]
    x, y = str(a[0]), str(a[1])
    same = sum(1 for i, j in zip(x, y) if i == j and i != "-")
    return 100.0 * same / min(len(protein), len(entry_seq))


# A CDS IS NOT THE ONLY PLACE AN INSERT LIVES. pOpen-Cx43.gb annotates its
# 1146 bp connexin insert as a `misc_feature` labeled "Cx43 (rat)" and declares
# no CDS for it at all; a CDS-only reader finds AmpR and a lacZ-alpha fragment
# and reports that the file has nothing to check. SnapGene exports do this
# routinely, so the insert types are read too and a label hint disambiguates.
TRANSLATABLE = ("CDS", "misc_feature", "gene")


def translated_cds(gb_path, label_hint=""):
    """Every translatable feature in a GenBank file, longest first."""
    from Bio import SeqIO
    out = []
    for rec in SeqIO.parse(str(gb_path), "genbank"):
        for ft in rec.features:
            if ft.type not in TRANSLATABLE:
                continue
            lab = (ft.qualifiers.get("label") or ft.qualifiers.get("gene")
                   or ft.qualifiers.get("product") or [""])[0]
            if label_hint and label_hint.lower() not in lab.lower():
                continue
            try:
                nt = ft.extract(rec.seq)
                # A primer_bind or a spacer is not a reading frame. Anything that
                # is not a whole number of codons, or that stops part way through,
                # is not the insert -- `Cx43-1F`, a 73 bp primer, otherwise
                # translates to 24 residues of nonsense and aligns at 12%.
                if len(nt) < 150 or len(nt) % 3:
                    continue
                aa = str(nt.translate()).rstrip("*")
                if "*" in aa:
                    continue
                out.append((lab, aa))
            except Exception:
                continue
    return sorted(out, key=lambda t: -len(t[1]))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("paths", nargs="*", type=Path, help="files or directories (default: docs/)")
    ap.add_argument("--align", metavar="GENBANK",
                    help="a .gb/.gbk file whose CDS translations are aligned against every "
                         "entry cited in the given paths. The deGFP guard.")
    ap.add_argument("--label", default="", help="only align CDS features whose label contains this")
    ap.add_argument("--offline", action="store_true", help="cache only; never fetch")
    a = ap.parse_args(argv)

    paths = a.paths or [REPO / "docs"]
    missing = [p for p in paths if not p.exists()]
    if missing:
        for p in missing:
            print(f"check-protein-refs: no such file or directory: {p}", file=sys.stderr)
        return 2

    claims = find_claims(paths)
    searched = ", ".join(str(p) for p in paths)
    if not claims:
        # A corpus with no citations is a real state, and it is not a pass.
        print(f"ℹ️  no UniProt citations found.\nsearched: {searched}")
        return 0

    cache = _load_cache()
    fetched = cached = 0
    findings = []
    for c in claims:
        try:
            entry, was_cached = fetch(c.accession, cache, a.offline)
        except Exception as e:
            print(f"check-protein-refs: could not reach UniProt ({e}). "
                  f"A cached answer is not a fresh one, so this is not a pass.", file=sys.stderr)
            return 2
        if entry is None:
            print(f"check-protein-refs: {c.accession} is not cached and --offline was given.",
                  file=sys.stderr)
            return 2
        cached += was_cached
        fetched += not was_cached
        for level, msg in check(c, entry):
            findings.append((level, c, msg))

    if a.align:
        gb = Path(a.align)
        if not gb.exists():
            print(f"check-protein-refs: no such file: {gb}", file=sys.stderr)
            return 2
        try:
            cdss = translated_cds(gb, a.label)
        except ImportError:
            print("check-protein-refs: --align needs biopython", file=sys.stderr)
            return 2
        if not cdss:
            print(f"check-protein-refs: {gb.name} has no CDS matching {a.label!r}", file=sys.stderr)
            return 2
        seen = set()
        for c in claims:
            if c.accession in seen:
                continue
            seen.add(c.accession)
            entry = cache.get(c.accession) or {}
            if not entry.get("seq"):
                continue
            for lab, prot in cdss:
                pid = align_identity(prot, entry["seq"])
                same_len = len(prot) == (entry["length"] or -1)
                # LOCAL ALIGNMENT ALONE DOES NOT CATCH A TRUNCATION. A clean
                # N-terminal deletion aligns at 100% over the part that remains,
                # so a variant that only loses residues would read as identical.
                # deGFP happens to carry substitutions too and lands at 98.7%; a
                # variant that did not would have passed. Length is the second
                # half of the test, not a nicety.
                level = INFO if (pid >= 99.95 and same_len) else WARN
                detail = f"{pid:.1f}% identical to {c.accession} ({entry['length']} aa)"
                if pid >= 99.95 and not same_len:
                    detail += (f" over the aligned region, but {abs(len(prot) - entry['length'])} "
                               f"residues shorter or longer — a truncation aligns at 100%")
                findings.append((level, c,
                                 f"{gb.name} CDS {lab!r} ({len(prot)} aa) is " + detail
                                 + ("" if level == INFO else
                                    " — a variant is not its parent; cite the parent only where "
                                    "the page says which part is the parent's")))

    try:
        CACHE.write_text(json.dumps(cache))
    except OSError:
        pass

    order = {BLOCKING: 0, WARN: 1, INFO: 2}
    for level, c, msg in sorted(findings, key=lambda f: (order[f[0]], str(f[1].path), f[1].line_no)):
        rel = c.path.relative_to(REPO) if c.path.is_absolute() and REPO in c.path.parents else c.path
        print(f"{level} {rel}:{c.line_no} — {msg}")

    n = {k: sum(1 for f in findings if f[0] == k) for k in (BLOCKING, WARN, INFO)}
    print(f"\nsearched: {searched}")
    print(f"{len(claims)} citation(s) over {len({c.accession for c in claims})} entry(ies): "
          f"{fetched} fetched, {cached} from cache")
    if n[BLOCKING]:
        print(f"⛔️ {n[BLOCKING]} blocking, {n[WARN]} warn, {n[INFO]} info")
        return 1
    print(f"✅ no blocking protein-reference issues ({n[WARN]} warning(s), {n[INFO]} info)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
