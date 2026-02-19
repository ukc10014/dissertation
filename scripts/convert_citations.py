#!/usr/bin/env python3
"""
Convert ch_03_combined.md citations from prose author-year format to Pandoc @key format.

Usage:
    python3 scripts/convert_citations.py

Reads:  chapters/ch_03_combined.md
        bib/bibliography_ukc.bib
        bib/ch03_additions.bib
Writes: chapters/ch_03_converted.md
        build/citation_conversion_log.txt
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE = Path(__file__).resolve().parent.parent
CHAPTER_PATH = BASE / "chapters" / "ch_03_combined.md"
BIB_PATHS = [
    BASE / "bib" / "bibliography_ukc.bib",
    BASE / "bib" / "ch03_additions.bib",
]
OUTPUT_PATH = BASE / "chapters" / "ch_03_converted.md"
LOG_PATH = BASE / "build" / "citation_conversion_log.txt"

# Where body text ends and footnote definitions begin
FOOTNOTE_DEF_START = None  # auto-detected

# Threshold for pure-citation classification (chars of non-cite residue)
PURE_CITE_THRESHOLD = 20

# ---------------------------------------------------------------------------
# Transliteration (reused from chicago_to_bibtex.py)
# ---------------------------------------------------------------------------

TRANSLIT = {
    'Ć': 'C', 'ć': 'c', 'Č': 'C', 'č': 'c',
    'Š': 'S', 'š': 's', 'Ž': 'Z', 'ž': 'z',
    'ë': 'e', 'ü': 'u', 'ö': 'o', 'ä': 'a',
    'é': 'e', 'è': 'e', 'ê': 'e', 'É': 'E',
    'á': 'a', 'à': 'a', 'â': 'a',
    'í': 'i', 'ì': 'i', 'î': 'i',
    'ó': 'o', 'ò': 'o', 'ô': 'o',
    'ú': 'u', 'ù': 'u', 'û': 'u',
    'ñ': 'n', 'Ñ': 'N',
    'ø': 'o', 'Ø': 'O',
    'å': 'a', 'Å': 'A',
    'ë': 'e',
    '‑': '-', '–': '-', '—': '-',
}

def transliterate(s):
    return ''.join(TRANSLIT.get(c, c) for c in s)


def normalize_surname(name):
    """Normalize a surname for matching: lowercase, transliterate, strip non-alpha."""
    name = transliterate(name)
    name = re.sub(r'[^a-zA-Z]', '', name)
    return name.lower()


def extract_surname_from_bib_author(author_str):
    """
    Extract surname from a bib author field entry.
    Handles both "Last, First" and "First Last" and "F. Last" formats.
    """
    author_str = author_str.strip()
    if ',' in author_str:
        # "Last, First" format
        return author_str.split(',')[0].strip()
    else:
        # "First Last" or "F. Last" format
        parts = author_str.split()
        if not parts:
            return author_str
        # Last word is the surname (handles "N. Bostrom", "R. Negarestani", etc.)
        return parts[-1].strip()


# ---------------------------------------------------------------------------
# Manual alias table
# ---------------------------------------------------------------------------
# Maps "Author Year" text forms (as they appear in the chapter) to bib keys.
# Used for non-standard key names, year mismatches, abbreviations, etc.

MANUAL_ALIASES = {
    # Abbreviations
    "ME 2022": "Bostrom2022",

    # Non-standard key names (key doesn't follow AuthorYear pattern)
    "Lem 1964": "LemST",
    "Lem  1964": "LemST",
    "Lem 1963": "Lem1963",
    "Lem 1961": "Lem1961",
    "Parfit 1984": "ParfitRP",
    "MacAskill 2022": "MacAskillWWO",
    "MacAskill 2024": "MacAskill2024",
    "MacAskill 2014": "MacAskill2014",

    # AAAI
    "AAAI 2025": "AAAI2025",

    # Year mismatches (text says one year, bib has another)
    "Sandberg et al 2017": "SandbergEtAl2018",
    "Sandberg et al. 2017": "SandbergEtAl2018",
    "Bostrom and Shulman 2022": "Shulman2021",
    "Bostrom & Shulman 2022": "Shulman2021",
    "Shulman & Bostrom 2022": "Shulman2021",
    "Shulman and Bostrom 2022": "Shulman2021",
    "Banks 1994": "Banks1994",
    "Banks 1998": "BanksE",

    # Multi-word or complex author names
    "De Lazari-Radek & Singer 2014": "DelazariradekSinger2014",
    "De Lazari-Radek and Singer 2014": "DelazariradekSinger2014",
    "de Cruz 2023": "Decruz2023",
    "De Cruz 2023": "Decruz2023",
    "Haqq-Misra and Baum 2009": "HaqqMisraBaum2009",
    "Haqq-Misra & Baum 2009": "HaqqMisraBaum2009",
    "Le Guin 1973": "LeGuin1973",
    "von Hoerner 1961": "VonHoerner1961",
    "Von Hoerner 1961": "VonHoerner1961",
    "Snyder-Beattie et al 2021": "SnyderBeattieEtAl2021",
    "Snyder-Beattie et al. 2021": "SnyderBeattieEtAl2021",
    "Godfrey-Smith 2016": "GodfreySmith2016",
    "Godfrey-Smith 2020": "GodfreySmith2020",
    "Zhi-Xuan et al 2024": "ZhiXuanEtAl2024",
    "Zhi-Xuan et al. 2024": "ZhiXuanEtAl2024",

    # Et al. forms
    "Hanson 2021": "HansonEtAl2021",
    "Hanson et al 2021": "HansonEtAl2021",
    "Greaves & MacAskill 2019": "GreavesMacAskill2019",
    "Greaves and MacAskill 2019": "GreavesMacAskill2019",
    "Greaves, MacAskill, Thornley 2021": "GreavesEtAl2021",
    "Greaves, MacAskill 2019": "GreavesMacAskill2019",
    "Kokotajlo et al 2025": "KokotajloEtAl2025",
    "Kokotajlo et al. 2025": "KokotajloEtAl2025",
    "Mills et al 2024": "MillsEtAl2024",
    "Mills et al. 2024": "MillsEtAl2024",
    "Long et al 2024": "LongEtAl2024",
    "Long et al. 2024": "LongEtAl2024",
    "Ćirković, Sandberg, Bostrom 2010": "CirkovicEtAl2010",
    "Greenblatt et al 2024": "GreenblattEtAl2024",
    "Greenblatt et al. 2024": "GreenblattEtAl2024",
    "Hubinger et al 2019": "HubingerEtAl2019",
    "Hubinger et al. 2019": "HubingerEtAl2019",
    "Shah et al 2022": "ShahEtAl2022",
    "Shah et al. 2022": "ShahEtAl2022",
    "Hong et al 2025": "HongEtAl2025",
    "Hong et al. 2025": "HongEtAl2025",
    "Phuong et al 2025": "PhuongEtAl2025",
    "Phuong et al. 2025": "PhuongEtAl2025",
    "Needham et al 2025": "NeedhamEtAl2025",
    "Needham et al. 2025": "NeedhamEtAl2025",
    "Schlatter et al 2025": "SchlatterEtAl2025",
    "Schlatter et al. 2025": "SchlatterEtAl2025",
    "Meinke et al 2024": "MeinkeEtAl2024",
    "Meinke et al. 2024": "MeinkeEtAl2024",
    "Ouyang et al 2022": "OuyangEtAl2022",
    "Ouyang et al. 2022": "OuyangEtAl2022",
    "Bai et al 2022": "BaiEtAl2022",
    "Bai et al. 2022": "BaiEtAl2022",
    "Rafailov et al 2023": "RafailovEtAl2023",
    "Rafailov et al. 2023": "RafailovEtAl2023",
    "Yuan et al 2023": "YuanEtAl2023",
    "Yuan et al. 2023": "YuanEtAl2023",
    "Sharma et al 2025": "SharmaEtAl2025",
    "Sharma et al. 2025": "SharmaEtAl2025",
    "Ji et al 2025": "JiEtAl2025",
    "Ji et al. 2025": "JiEtAl2025",
    "Ngo et al 2024": "NgoEtAl2024",
    "Ngo et al. 2024": "NgoEtAl2024",
    "Miller et al 2023": "MillerEtAl2023",
    "Miller et al. 2023": "MillerEtAl2023",
    "Sharkey et al 2025": "SharkeyEtAl2025",
    "Sharkey et al. 2025": "SharkeyEtAl2025",
    "Shreesha et al 2025": "ShreeshaEtAl2025",
    "Shreesha et al. 2025": "ShreeshaEtAl2025",
    "Zeng et al 2025": "ZengEtAl2025",
    "Zeng et al. 2025": "ZengEtAl2025",
    "Neuman, Coleman, Shah 2025": "NeumanEtAl2025",
    "Levin & Watson 2025": "LevinWatson2025",
    "Levin and Watson 2025": "LevinWatson2025",

    # Two-author forms
    "Armstrong and Sandberg 2012": "ArmstrongSandberg2012",
    "Armstrong & Sandberg 2012": "ArmstrongSandberg2012",
    "Armstrong and Sandberg": "ArmstrongSandberg2012",
    "Nguyen & Aldred 2024": "NguyenAldred2024a",
    "Nguyen and Aldred 2024": "NguyenAldred2024a",
    "Sotala & Gloor 2017": "SotalaGloor2017",
    "Sotala and Gloor 2017": "SotalaGloor2017",
    "Henrich & Muthukrishna 2021": "HenrichMuthukrishna2021",
    "Henrich and Muthukrishna 2021": "HenrichMuthukrishna2021",
    "Owe & Baum 2024": "OweBaum2024",
    "Owe and Baum 2024": "OweBaum2024",
    "Oesterheld & Conitzer 2022": "OesterheldConitzer2022",
    "Oesterheld and Conitzer 2022": "OesterheldConitzer2022",
    "Crawford & Schulze-Makuch 2024": "CrawfordSchulzeMakuch2024",
    "Crawford and Schulze-Makuch 2024": "CrawfordSchulzeMakuch2024",
    "Demski & Garrabrant 2019": "DemskiGarrabrant2019",
    "Demski and Garrabrant 2019": "DemskiGarrabrant2019",
    "Stanovich, Toplak, West 2021": "StanovichEtAl2021",
    "Stanovich, West & Toplak 2021": "StanovichEtAl2021",
    "Stanovich, West and Toplak 2021": "StanovichEtAl2021",
    "West & Toplak 2021": "StanovichEtAl2021",
    "West and Toplak 2021": "StanovichEtAl2021",
    "Perez & Long 2023": "PerezLong2023",
    "Perez and Long 2023": "PerezLong2023",
    "Herrmann & Levinstein 2024": "HerrmannLevinstein2024a",
    "Herrmann and Levinstein 2024": "HerrmannLevinstein2024a",
    "Kidd and Hayden 2015": "KiddHayden2015",
    "Kidd & Hayden 2015": "KiddHayden2015",
    "Oudeyer and Kaplan 2007": "OudeyerKaplan2007",
    "Oudeyer & Kaplan 2007": "OudeyerKaplan2007",
    "Balbi and Lingam 2025": "BalbiLingam2025",
    "Balbi & Lingam 2025": "BalbiLingam2025",
    "Maturana & Varela 1980": "MaturanaVarela1980",
    "Maturana and Varela 1980": "MaturanaVarela1980",
    "Arrow & Fisher 1974": "ArrowFisher1974",
    "Arrow and Fisher 1974": "ArrowFisher1974",

    # Negarestani (special key)
    "Negarestani 2018": "NegarestaniIS",

    # Oesterheld (special key)
    "Oesterheld 2017": "OesterheldECL",

    # Gebru & Torres
    "Gebru & Torres 2024": "GebruTorres2024",
    "Gebru and Torres 2024": "GebruTorres2024",

    # Fallenstein
    "Fallenstein & Soares 2015": "Fallenstein2015",
    "Fallenstein and Soares 2015": "Fallenstein2015",

    # Newberry
    "Newberry & Ord 2021": "NewberryOrd2021",
    "Newberry and Ord 2021": "NewberryOrd2021",

    # Ambiguous but with preferred resolution
    "Ćirković 2018": "Cirkovic2018a",
    "Cirkovic 2018": "Cirkovic2018a",

    # Specific footnote mentions
    "Ćirković 2018b": "Cirkovic2018b",
    "Cirkovic 2018b": "Cirkovic2018b",

    # RedwoodResearch special key
    "Redwood 2025": "RedwoodResearchJulianStastnyEtAl2025",

    # Stastny et al -> RedwoodResearch
    "Stastny, Järviniemi, and Shlegeris 2025": "RedwoodResearchJulianStastnyEtAl2025",

    # Yudkowsky & Soares 2025
    "Yudkowsky & Soares 2025": "YudkowskySoares2025",
    "Yudkowsky and Soares 2025": "YudkowskySoares2025",

    # Gigerenzer
    "Gigerenzer 1996": "GigerenzerGoldstein1996",

    # These have non-standard bib keys from older entries
    "Bostrom 2014": "Bostrom2014",

    # Likavčan with diacritics
    "Likavčan 2025": "Likavcan2025",

    # Dick 2006h (the "h" appears in original text, possibly a section reference)
    "Dick 2006h": "Dick2006",

    # Sebo (might be mis-parsed from context)
    "Sebo 2025": "Sebo2025",

    # Hayles
    "Hayles 2017": "hayles2017unthought",

    # Stastny et al in fn117
    "Stastny, Järviniemi, Shlegeris 2025": "RedwoodResearchJulianStastnyEtAl2025",

    # Bostrom 2003 (ambiguous, pick a for the sim argument)
    "Bostrom 2003": "Bostrom2003a",
    "Bostrom  2003": "Bostrom2003a",

    # Noë forms
    "Noë 2004": "Noe2004",
    "Noë 2015": "Noe2015",
    "Noe 2004": "Noe2004",
    "Noe 2015": "Noe2015",
}


# ---------------------------------------------------------------------------
# Parse bib files
# ---------------------------------------------------------------------------

def parse_bib_files(paths):
    """
    Parse .bib files. Returns:
      - key_set: set of all bib keys
      - key_to_meta: dict of key -> {authors: [(last,first)], year: str}
      - author_year_to_keys: dict of (normalized_surname, year) -> [keys]
    """
    key_set = set()
    key_to_meta = {}
    author_year_to_keys = defaultdict(list)

    for path in paths:
        if not path.exists():
            print(f"WARNING: {path} not found, skipping")
            continue
        text = path.read_text(encoding="utf-8")

        # Split into entries
        for match in re.finditer(r'@(\w+)\{([^,]+),', text):
            entry_type = match.group(1)
            key = match.group(2).strip()

            if key in key_set:
                continue  # skip duplicates across files
            key_set.add(key)

            # Extract entry text
            start = match.end()
            end = text.find('\n@', start)
            if end == -1:
                end = len(text)
            entry_text = text[start:end]

            # Extract author
            author_m = re.search(r'author\s*=\s*\{([^}]+)\}', entry_text, re.IGNORECASE)
            year_m = re.search(r'year\s*=\s*\{?(\d{4})\}?', entry_text, re.IGNORECASE)

            authors = []
            year = year_m.group(1) if year_m else ""

            if author_m:
                author_str = author_m.group(1)
                # Split on " and "
                for a in re.split(r'\s+and\s+', author_str):
                    a = a.strip()
                    if not a or a == "others":
                        continue
                    surname = extract_surname_from_bib_author(a)
                    if ',' in a:
                        first = a.split(',', 1)[1].strip()
                    else:
                        first = ' '.join(a.split()[:-1]) if len(a.split()) > 1 else ""
                    authors.append((surname, first))

            key_to_meta[key] = {"authors": authors, "year": year}

            # Build lookup by first author surname + year
            if authors and year:
                surname = normalize_surname(authors[0][0])
                author_year_to_keys[(surname, year)].append(key)

                # Also add with "et al" if 3+ authors
                if len(authors) >= 3:
                    author_year_to_keys[(surname + "etal", year)].append(key)

    return key_set, key_to_meta, author_year_to_keys


# ---------------------------------------------------------------------------
# Citation resolution
# ---------------------------------------------------------------------------

def resolve_citation(prose_text, key_set, author_year_to_keys, log):
    """
    Try to resolve a prose citation like "Bostrom 2024" to a bib key.
    Returns (key, confidence) or (None, reason).
    """
    original = prose_text.strip()

    # 1. Check manual alias table (exact match)
    if original in MANUAL_ALIASES:
        key = MANUAL_ALIASES[original]
        if key in key_set:
            return key, "alias"
        else:
            log.append(f"  WARNING: Alias '{original}' -> '{key}' but key not in bib")
            return None, f"alias key '{key}' not found"

    # 2. Try direct key match (e.g., "Bostrom2024" might be a key)
    direct = re.sub(r'\s+', '', original)
    if direct in key_set:
        return direct, "direct"

    # 2b. Try with whitespace normalization
    normalized = re.sub(r'\s+', ' ', original).strip()
    if normalized in MANUAL_ALIASES:
        key = MANUAL_ALIASES[normalized]
        if key in key_set:
            return key, "alias_normalized"

    # 3. Parse into author(s) + year
    # Pattern: Author(s) Year[suffix]
    m = re.match(
        r'^(.+?)\s+((?:19|20)\d{2})([a-c]?)\.?$',
        normalized
    )
    if not m:
        return None, "no year found"

    author_part = m.group(1).strip().rstrip(",").rstrip(".")
    year = m.group(2)
    suffix = m.group(3)

    # Normalize author part
    # Remove "et al.", "&", "and", etc. to get first author
    first_author = author_part
    first_author = re.sub(r'\s+et\s+al\.?$', '', first_author, flags=re.IGNORECASE)
    first_author = re.sub(r'\s*[&]\s*.+$', '', first_author)
    first_author = re.sub(r'\s+and\s+.+$', '', first_author, flags=re.IGNORECASE)
    first_author = re.sub(r',\s*.+$', '', first_author)  # remove after comma
    first_author = first_author.strip()

    surname_norm = normalize_surname(first_author)

    # Try exact (surname, year) lookup
    candidates = author_year_to_keys.get((surname_norm, year), [])

    if suffix and len(candidates) > 0:
        # Look for key ending with the suffix
        for c in candidates:
            if c.endswith(suffix):
                return c, "author_year_suffix"

    if len(candidates) == 1:
        return candidates[0], "author_year"
    elif len(candidates) > 1:
        log.append(f"  AMBIGUOUS: '{original}' matches {candidates}")
        return candidates[0], f"ambiguous({candidates})"

    # Try et al lookup
    candidates = author_year_to_keys.get((surname_norm + "etal", year), [])
    if len(candidates) == 1:
        return candidates[0], "author_year_etal"
    elif len(candidates) > 1:
        log.append(f"  AMBIGUOUS: '{original}' (et al) matches {candidates}")
        return candidates[0], f"ambiguous_etal({candidates})"

    # Try year ±1 (fuzzy)
    for delta in [-1, 1]:
        fuzzy_year = str(int(year) + delta)
        candidates = author_year_to_keys.get((surname_norm, fuzzy_year), [])
        if len(candidates) == 1:
            log.append(f"  YEAR FUZZY: '{original}' -> {candidates[0]} (year {fuzzy_year} in bib)")
            return candidates[0], f"year_fuzzy({year}->{fuzzy_year})"
        candidates = author_year_to_keys.get((surname_norm + "etal", fuzzy_year), [])
        if len(candidates) == 1:
            log.append(f"  YEAR FUZZY: '{original}' (et al) -> {candidates[0]} (year {fuzzy_year} in bib)")
            return candidates[0], f"year_fuzzy_etal({year}->{fuzzy_year})"

    return None, "no match"


# ---------------------------------------------------------------------------
# Regex patterns for finding citations in text
# ---------------------------------------------------------------------------

# Author name components
# Handles: Bostrom, Ćirković, de Cruz, Le Guin, Haqq-Misra, Snyder-Beattie, MacAskill, etc.
_AUTHOR_WORD = r"[A-ZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞĆČŠŽ][a-zàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþćčšžŸ]*(?:[A-Z][a-zàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþćčšžŸ]*)?"
_SURNAME = (
    r"(?:"
    r"(?:de|De|von|Von|van|Van|Le|le|Mac|Mc)\s*)?"  # optional prefix (no space needed for Mac/Mc)
    + _AUTHOR_WORD +
    r"(?:[‑\-]" + _AUTHOR_WORD + r")*"  # optional hyphenated parts
)

# Words that should NOT be treated as author names (false positives)
FALSE_POSITIVE_WORDS = {
    'however', 'the', 'this', 'that', 'these', 'those', 'but', 'and', 'or',
    'for', 'with', 'from', 'into', 'upon', 'about', 'after', 'before',
    'during', 'since', 'until', 'through', 'between', 'among',
    'january', 'february', 'march', 'april', 'may', 'june', 'july',
    'august', 'september', 'october', 'november', 'december',
    'chapter', 'section', 'appendix', 'table', 'figure',
    'see', 'also', 'note', 'research', 'ai',
    'particularly', 'specifically', 'precisely',
}

# Single author-year: "Bostrom 2024" or "Bostrom 2024a"
_SINGLE_AY = _SURNAME + r"\s+(?:19|20)\d{2}[a-c]?"

# Two authors: "Author and Author 2024" or "Author & Author 2024"
_TWO_AY = _SURNAME + r"\s+(?:and|&)\s+" + _SURNAME + r"\s+(?:19|20)\d{2}[a-c]?"

# Three+ listed authors: "Author, Author, Author 2024" or "Author, Author and Author 2024"
_THREE_AY = (
    _SURNAME + r"(?:,\s+" + _SURNAME + r")+(?:\s+and\s+" + _SURNAME + r")?"
    + r"\s+(?:19|20)\d{2}[a-c]?"
)

# Et al: "Author et al 2024" or "Author et al. 2024"
_ETAL_AY = _SURNAME + r"\s+et\s+al\.?\s+(?:19|20)\d{2}[a-c]?"

# Combined author-year pattern (order matters: try longer patterns first)
AUTHOR_YEAR_PATTERN = re.compile(
    r"(?:" + _THREE_AY + r"|" + _TWO_AY + r"|" + _ETAL_AY + r"|" + _SINGLE_AY + r")",
    re.UNICODE
)

# Year extraction from a matched author-year string
YEAR_RE = re.compile(r'((?:19|20)\d{2}[a-c]?)\s*$')

# Special abbreviation patterns
ABBREV_PATTERN = re.compile(r'\bME\s+2022\b')

# Already-converted Pandoc citations - skip these
PANDOC_CITE_RE = re.compile(r'@[A-Za-z][A-Za-z0-9]+')


# ---------------------------------------------------------------------------
# Footnote parsing
# ---------------------------------------------------------------------------

def parse_footnotes(lines):
    """
    Parse footnote definitions from lines.
    Returns dict: footnote_number -> {
        'text': full text of footnote definition,
        'start_line': line index (0-based),
        'end_line': line index (exclusive),
    }
    """
    footnotes = {}
    current_fn = None
    current_lines = []
    current_start = None

    for i, line in enumerate(lines):
        # Check for footnote definition start
        fn_match = re.match(r'^\[\\?\^(\d+)\]:\s*(.*)', line)
        if fn_match:
            # Save previous footnote if any
            if current_fn is not None:
                footnotes[current_fn] = {
                    'text': '\n'.join(current_lines),
                    'start_line': current_start,
                    'end_line': i,
                }
            current_fn = int(fn_match.group(1))
            current_lines = [fn_match.group(2)]
            current_start = i
        elif current_fn is not None:
            # Continuation of current footnote (indented or blank line between)
            if line.strip() == '':
                # Check if next non-blank line is a new footnote or continuation
                # For now, blank line might separate footnotes
                # Look ahead to see if next content line is a new footnote
                current_lines.append('')
            elif line.startswith('    ') or line.startswith('\t'):
                current_lines.append(line)
            else:
                # Not indented, might be a new footnote def on next iteration
                # Save current
                footnotes[current_fn] = {
                    'text': '\n'.join(current_lines),
                    'start_line': current_start,
                    'end_line': i,
                }
                current_fn = None
                current_lines = []
                current_start = None

    # Save last footnote
    if current_fn is not None:
        footnotes[current_fn] = {
            'text': '\n'.join(current_lines),
            'start_line': current_start,
            'end_line': len(lines),
        }

    return footnotes


def find_footnote_section_start(lines):
    """Find where footnote definitions begin."""
    for i, line in enumerate(lines):
        if re.match(r'^\[\^1\]:', line):
            return i
    # Fallback: find first footnote def
    for i, line in enumerate(lines):
        if re.match(r'^\[\^\d+\]:', line):
            return i
    return len(lines)


# ---------------------------------------------------------------------------
# Footnote classification
# ---------------------------------------------------------------------------

# Words/phrases to strip when testing for pure-citation
CITE_CONNECTORS = re.compile(
    r'\b(?:See|see|Cf\.|cf\.|Also|also|and|And|For|for|In|in|as\s+well\s+as|'
    r'e\.g\.|i\.e\.|particularly|especially|similarly|Relatedly|relatedly|'
    r'For\s+instance|for\s+instance|as\s+argued\s+in|as\s+discussed\s+in|'
    r'cited\s+works|See\s+also|see\s+also|Note\s+that|pp?\.|§|Ch\.|ch\.|'
    r'on\s+the|on\s+a|which|from|their|a\s+discussion|discussion)\b',
    re.IGNORECASE | re.UNICODE
)


def classify_footnote(fn_text, key_set, author_year_to_keys, log):
    """
    Classify footnote as 'pure_citation', 'discursive', or 'commentary'.
    Returns (classification, citations_found).
    """
    text = fn_text.strip()

    # Already a Pandoc citation?
    if re.match(r'^\s*\[?@[A-Za-z]', text):
        return 'pure_citation', []

    # Find all author-year citations in the footnote text
    citations = find_all_citations(text)

    if not citations:
        return 'commentary', []

    # Strip all citation matches from the text to see what remains
    residue = text
    for cite_text, _, _ in citations:
        residue = residue.replace(cite_text, '', 1)

    # Also strip ABBREV patterns
    residue = ABBREV_PATTERN.sub('', residue)

    # Strip connectors and punctuation
    residue = CITE_CONNECTORS.sub('', residue)
    residue = re.sub(r'[\s,;:.\-–—()\[\]\'\"]+', ' ', residue)
    residue = re.sub(r'\b(and|or|also|the|a|an|of|in|on|for|to|by|with|from|as|at)\b',
                     '', residue, flags=re.IGNORECASE)
    residue = residue.strip()

    # Count non-whitespace chars
    residue_chars = len(re.sub(r'\s+', '', residue))

    if residue_chars <= PURE_CITE_THRESHOLD:
        return 'pure_citation', citations
    else:
        return 'discursive', citations


def find_all_citations(text):
    """
    Find all author-year citation patterns in text.
    Returns list of (matched_text, author_part, year_part).
    """
    results = []

    # First check for ABBREV patterns
    for m in ABBREV_PATTERN.finditer(text):
        results.append((m.group(0), "ME", "2022"))

    # Find author-year patterns
    for m in AUTHOR_YEAR_PATTERN.finditer(text):
        matched = m.group(0)
        # Skip if it's inside an already-converted citation
        before = text[:m.start()]
        if before.endswith('@'):
            continue

        # Extract year
        ym = YEAR_RE.search(matched)
        if ym:
            year = ym.group(1)
            author_part = matched[:ym.start()].strip()

            # Filter out false positives
            first_word = re.sub(r'[^a-zA-Z]', '', author_part.split()[0]).lower() if author_part.split() else ""
            if first_word in FALSE_POSITIVE_WORDS:
                continue
            # Check ALL words in author_part for false positives
            all_words = [w.lower() for w in re.findall(r'[A-Za-z]+', author_part)]
            if all_words and all_words[0] in FALSE_POSITIVE_WORDS:
                continue
            # Skip single-letter "author" names (like "I")
            if len(author_part.strip()) <= 2 and not author_part.strip().isupper():
                continue
            # Skip if author_part is just an initial like "I" or "A"
            if re.match(r'^[A-Z]$', author_part.strip()):
                continue
            # Skip "de X" where X is not an author name but part of text
            if re.match(r'^de\s+[a-z]', author_part):
                continue

            results.append((matched, author_part, year))

    return results


# ---------------------------------------------------------------------------
# Citation conversion in text
# ---------------------------------------------------------------------------

def convert_citations_in_text(text, key_set, author_year_to_keys, log,
                              context="body", is_pure_fn_text=False):
    """
    Convert author-year citations in a text string to @key format.
    Returns (converted_text, changes_made).
    """
    changes = []

    # Skip if text contains TODO comments or is inside markdown links
    # Process the text, but protect certain regions

    # Protect markdown links, URLs, and already-converted citations
    protected = {}
    protect_counter = [0]

    def protect(m):
        key = f"__PROTECTED_{protect_counter[0]}__"
        protected[key] = m.group(0)
        protect_counter[0] += 1
        return key

    # Protect URLs and markdown links
    working = re.sub(r'\[([^\]]*)\]\([^)]+\)', protect, text)
    # Protect already-converted Pandoc citations
    working = re.sub(r'\[@[A-Za-z][A-Za-z0-9]+(?:,\s*[^]]+)?\]', protect, working)
    working = re.sub(r'(?<!\[)@[A-Za-z][A-Za-z0-9]+', protect, working)

    # Process parenthetical citations: (Author Year) or (Author Year, Author Year)
    def convert_paren_cite(m):
        inner = m.group(1)

        # Handle "Author Year, Year" pattern (same author, multiple years)
        multi_year_m = re.match(
            r'^(' + _SURNAME + r')\s+((?:19|20)\d{2}[a-c]?)(?:\s*,\s*((?:19|20)\d{2}[a-c]?))+$',
            inner.strip()
        )
        if multi_year_m:
            author = multi_year_m.group(1)
            years = re.findall(r'((?:19|20)\d{2}[a-c]?)', inner)
            multi_keys = []
            all_ok = True
            for y in years:
                cite_text = f"{author} {y}"
                key, conf = resolve_citation(cite_text, key_set, author_year_to_keys, log)
                if key:
                    multi_keys.append(key)
                else:
                    all_ok = False
                    log.append(f"  UNRESOLVED ({context}): '{cite_text}' in multi-year - {conf}")
            if all_ok and multi_keys:
                result = "[" + "; ".join(f"@{k}" for k in multi_keys) + "]"
                changes.append((m.group(0), result))
                return result

        # Find all citations inside the parentheses
        cites = find_all_citations(inner)
        if not cites:
            return m.group(0)

        # Check if the entire parenthetical is citations (possibly with locators)
        residue = inner
        cite_keys = []
        locators = []
        all_resolved = True

        for cite_text, author_part, year in cites:
            key, confidence = resolve_citation(cite_text, key_set, author_year_to_keys, log)
            if key:
                cite_keys.append(key)
                # Check for locator after this citation
                cite_pos = residue.find(cite_text)
                after_cite = residue[cite_pos + len(cite_text):] if cite_pos >= 0 else ""
                # Locator patterns: §X, pp. X-Y, Ch. X
                # For pp., allow commas within page ranges (e.g., "pp. 4, 6")
                loc_m = re.match(
                    r'\s*,\s*(§\s*[\d.,\s\-–]+|pp?\.\s*[\d,\s\-–]+|[Cc]h\.\s*[\d,\s]+)',
                    after_cite, re.IGNORECASE
                )
                if loc_m:
                    locators.append(loc_m.group(1).strip())
                else:
                    locators.append(None)
                residue = residue.replace(cite_text, '', 1)
            else:
                all_resolved = False
                log.append(f"  UNRESOLVED ({context}): '{cite_text}' - {confidence}")

        if not cite_keys:
            return m.group(0)

        # Clean residue
        clean_residue = re.sub(r'[\s,;.]+', '', residue)
        clean_residue = re.sub(r'§[^,;)]+|pp?\.\s*[^,;)]+', '', clean_residue)

        if not all_resolved:
            return m.group(0)  # Leave unconverted if any part failed

        # Build Pandoc citation
        parts = []
        for i, key in enumerate(cite_keys):
            if locators[i]:
                parts.append(f"@{key}, {locators[i]}")
            else:
                parts.append(f"@{key}")

        result = "[" + "; ".join(parts) + "]"
        changes.append((m.group(0), result))
        return result

    # Match parenthetical citations: (stuff with Author Year)
    paren_cite_re = re.compile(
        r'\((' + AUTHOR_YEAR_PATTERN.pattern + r'(?:\s*[,;]\s*(?:' +
        AUTHOR_YEAR_PATTERN.pattern + r'|§[^)]+|pp?\.\s*[^)]+|[^)]{0,30}))*' + r')\)',
        re.UNICODE
    )
    working = paren_cite_re.sub(convert_paren_cite, working)

    # Process narrative citations: Author Year at start of clause or after certain words
    def convert_narrative_cite(m):
        cite_text = m.group(0)

        # Don't convert if preceded by [ (already inside brackets) or @ (already converted)
        start = m.start()
        if start > 0 and working[start-1] in ('@', '['):
            return cite_text

        # Extract author part and filter false positives
        ym = YEAR_RE.search(cite_text)
        if ym:
            author_part = cite_text[:ym.start()].strip()
            first_word = re.sub(r'[^a-zA-Z]', '', author_part.split()[0]).lower() if author_part.split() else ""
            if first_word in FALSE_POSITIVE_WORDS:
                # The first word is a false positive, but there might be a valid
                # citation embedded within (e.g., "However, Bostrom 2024")
                # Try to find and convert a single-author citation within the text
                inner_m = re.search(
                    _SINGLE_AY,
                    cite_text,
                    re.UNICODE
                )
                if inner_m:
                    inner_text = inner_m.group(0)
                    inner_key, inner_conf = resolve_citation(
                        inner_text, key_set, author_year_to_keys, log
                    )
                    if inner_key:
                        # Replace just the inner citation within the full match
                        replacement = cite_text[:inner_m.start()] + f"@{inner_key}" + cite_text[inner_m.end():]
                        changes.append((inner_text, f"@{inner_key}"))
                        return replacement
                return cite_text
            # Skip single-character author names
            if re.match(r'^[A-Z]$', author_part.strip()):
                return cite_text

        key, confidence = resolve_citation(cite_text, key_set, author_year_to_keys, log)
        if key:
            replacement = f"@{key}"
            # Check if the character after this match is alphanumeric
            # If so, we need to prevent Pandoc from treating it as part of the key
            end_pos = m.end()
            if end_pos < len(working) and working[end_pos].isalpha():
                # The trailing letter would attach to the key; wrap in brackets
                replacement = f"[@{key}]"
            changes.append((cite_text, replacement))
            return replacement
        else:
            log.append(f"  UNRESOLVED ({context}): '{cite_text}' - {confidence}")
            return cite_text

    # Convert ME 2022 first (special abbreviation)
    def convert_abbrev(m):
        key = MANUAL_ALIASES.get(m.group(0))
        if key:
            changes.append((m.group(0), f"@{key}"))
            return f"@{key}"
        return m.group(0)

    working = ABBREV_PATTERN.sub(convert_abbrev, working)

    # Convert remaining author-year patterns (narrative)
    working = AUTHOR_YEAR_PATTERN.sub(convert_narrative_cite, working)

    # Restore protected regions
    for key, value in protected.items():
        working = working.replace(key, value)

    return working, changes


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

def main():
    log = []
    log.append("=" * 70)
    log.append("CITATION CONVERSION LOG")
    log.append("=" * 70)
    log.append("")

    # --- Parse bib files ---
    log.append("--- Parsing bib files ---")
    key_set, key_to_meta, author_year_to_keys = parse_bib_files(BIB_PATHS)
    log.append(f"Total unique keys: {len(key_set)}")
    log.append("")

    # --- Read chapter ---
    text = CHAPTER_PATH.read_text(encoding="utf-8")
    lines = text.split('\n')
    log.append(f"Chapter: {len(lines)} lines")

    # --- Find footnote section ---
    fn_section_start = find_footnote_section_start(lines)
    log.append(f"Footnote definitions start at line {fn_section_start + 1}")
    log.append("")

    body_lines = lines[:fn_section_start]
    fn_lines = lines[fn_section_start:]

    # --- Parse footnotes ---
    footnotes = parse_footnotes(fn_lines)
    log.append(f"Footnotes parsed: {len(footnotes)}")
    log.append("")

    # --- Classify footnotes ---
    log.append("--- Footnote classification ---")
    pure_citation_fns = {}
    discursive_fns = {}
    commentary_fns = {}

    for fn_num in sorted(footnotes.keys()):
        fn = footnotes[fn_num]
        classification, citations = classify_footnote(
            fn['text'], key_set, author_year_to_keys, log
        )
        if classification == 'pure_citation':
            pure_citation_fns[fn_num] = (fn, citations)
            log.append(f"  [^{fn_num}]: PURE CITATION")
        elif classification == 'discursive':
            discursive_fns[fn_num] = (fn, citations)
            log.append(f"  [^{fn_num}]: DISCURSIVE ({len(citations)} citations)")
        else:
            commentary_fns[fn_num] = fn
            log.append(f"  [^{fn_num}]: COMMENTARY")

    log.append("")
    log.append(f"Pure citation: {len(pure_citation_fns)}")
    log.append(f"Discursive: {len(discursive_fns)}")
    log.append(f"Commentary: {len(commentary_fns)}")
    log.append("")

    # --- Process pure citation footnotes ---
    log.append("--- Processing pure citation footnotes ---")
    body_text = '\n'.join(body_lines)
    fns_to_remove = set()

    for fn_num, (fn, citations) in sorted(pure_citation_fns.items()):
        fn_text = fn['text'].strip()
        log.append(f"\n  [^{fn_num}]: '{fn_text[:80]}...'")

        # Already a Pandoc citation? (like [^7]: [@Persson2021])
        pandoc_m = re.search(r'\[@([A-Za-z][A-Za-z0-9]+(?:,\s*[^]]+)?)\]', fn_text)
        if pandoc_m:
            replacement = pandoc_m.group(0)
            log.append(f"    Already Pandoc: {replacement}")
            # Check if the citation already exists adjacent to the footnote marker
            # Pattern: [@Key][^N] or [@Key].[^N]  -> just remove [^N], keep period
            adjacent_pattern = re.compile(
                re.escape(replacement) + r'(\s*\.?\s*)\[\^' + str(fn_num) + r'\](?!:)'
            )
            adj_m = adjacent_pattern.search(body_text)
            if adj_m:
                # Keep any period that was between citation and footnote marker
                sep = adj_m.group(1)
                # Preserve period if present
                period = '.' if '.' in sep else ''
                body_text = adjacent_pattern.sub(replacement + period, body_text)
                log.append(f"    Removed duplicate adjacent footnote marker")
            else:
                # Replace [^N] marker in body with the citation
                body_text = re.sub(
                    r'\[\^' + str(fn_num) + r'\](?!:)',
                    replacement,
                    body_text
                )
            fns_to_remove.add(fn_num)
            continue

        # Resolve citations in this footnote
        resolved_keys = []
        locator_info = None
        all_resolved = True

        if citations:
            for cite_text, author_part, year in citations:
                key, confidence = resolve_citation(
                    cite_text, key_set, author_year_to_keys, log
                )
                if key:
                    resolved_keys.append(key)
                    log.append(f"    Resolved: '{cite_text}' -> @{key} ({confidence})")
                else:
                    all_resolved = False
                    log.append(f"    UNRESOLVED: '{cite_text}' - {confidence}")
        else:
            # Try to parse the whole footnote text as a citation
            key, confidence = resolve_citation(
                fn_text.rstrip('.'), key_set, author_year_to_keys, log
            )
            if key:
                resolved_keys.append(key)
                log.append(f"    Resolved (whole): '{fn_text}' -> @{key} ({confidence})")
            else:
                all_resolved = False
                log.append(f"    UNRESOLVED (whole): '{fn_text}' - {confidence}")

        # Check for locator info (§, pp., ch.)
        loc_m = re.search(r'(§\s*[\d.,\s]+|pp?\.\s*[\d\-–]+|[Cc]h\.\s*[\d,\s]+)', fn_text)
        if loc_m:
            locator_info = loc_m.group(1).strip()

        if resolved_keys and all_resolved:
            # Build replacement
            if len(resolved_keys) == 1:
                if locator_info:
                    replacement = f"[@{resolved_keys[0]}, {locator_info}]"
                else:
                    replacement = f"[@{resolved_keys[0]}]"
            else:
                parts = [f"@{k}" for k in resolved_keys]
                replacement = "[" + "; ".join(parts) + "]"

            # Replace [^N] marker in body with the citation
            # But be careful: [^N] might appear with a space before it
            body_text = re.sub(
                r'\s*\[\^' + str(fn_num) + r'\](?!:)',
                ' ' + replacement,
                body_text
            )
            fns_to_remove.add(fn_num)
            log.append(f"    -> Replaced with {replacement}")
        else:
            log.append(f"    -> LEFT UNCONVERTED (unresolved)")

    log.append(f"\nPure citation footnotes removed: {len(fns_to_remove)}")
    log.append("")

    # --- Process in-text body citations ---
    log.append("--- Processing in-text body citations ---")
    body_text, body_changes = convert_citations_in_text(
        body_text, key_set, author_year_to_keys, log, context="body"
    )
    log.append(f"Body citations converted: {len(body_changes)}")
    for old, new in body_changes:
        log.append(f"  '{old}' -> '{new}'")
    log.append("")

    # --- Process discursive footnotes ---
    log.append("--- Processing discursive footnote citations ---")
    converted_fn_texts = {}
    total_fn_changes = 0

    for fn_num, (fn, citations) in sorted(discursive_fns.items()):
        fn_text = fn['text']
        converted, fn_changes = convert_citations_in_text(
            fn_text, key_set, author_year_to_keys, log,
            context=f"fn{fn_num}"
        )
        converted_fn_texts[fn_num] = converted
        total_fn_changes += len(fn_changes)
        if fn_changes:
            log.append(f"  [^{fn_num}]: {len(fn_changes)} changes")
            for old, new in fn_changes:
                log.append(f"    '{old}' -> '{new}'")

    log.append(f"\nDiscursive footnote citations converted: {total_fn_changes}")
    log.append("")

    # --- Rebuild footnote section ---
    # Collect all remaining footnotes with their (possibly converted) text
    remaining_fns = {}
    for fn_num in sorted(footnotes.keys()):
        if fn_num in fns_to_remove:
            continue
        if fn_num in converted_fn_texts:
            remaining_fns[fn_num] = converted_fn_texts[fn_num]
        elif fn_num in commentary_fns:
            remaining_fns[fn_num] = commentary_fns[fn_num]['text']
        elif fn_num in discursive_fns:
            remaining_fns[fn_num] = discursive_fns[fn_num][0]['text']
        else:
            remaining_fns[fn_num] = footnotes[fn_num]['text']

    # --- Renumber footnotes ---
    log.append("--- Renumbering footnotes ---")
    old_to_new = {}
    new_num = 1
    for old_num in sorted(remaining_fns.keys()):
        old_to_new[old_num] = new_num
        if old_num != new_num:
            log.append(f"  [^{old_num}] -> [^{new_num}]")
        new_num += 1

    log.append(f"\nRemaining footnotes: {len(remaining_fns)} (was {len(footnotes)})")
    log.append("")

    # Apply renumbering to body text
    # Sort by descending old number to avoid replacement conflicts
    for old_num in sorted(old_to_new.keys(), reverse=True):
        new_num = old_to_new[old_num]
        if old_num != new_num:
            # Replace [^old] with a temporary placeholder to avoid conflicts
            body_text = re.sub(
                r'\[\^' + str(old_num) + r'\]',
                f'[^__TEMP_{new_num}__]',
                body_text
            )

    # Now convert placeholders to final numbers
    for old_num in old_to_new:
        new_num = old_to_new[old_num]
        if old_num != new_num:
            body_text = body_text.replace(
                f'[^__TEMP_{new_num}__]',
                f'[^{new_num}]'
            )

    # Build new footnote definitions
    fn_section_lines = []
    fn_section_lines.append('')  # blank line before footnotes

    for old_num in sorted(remaining_fns.keys()):
        new_num = old_to_new[old_num]
        fn_text = remaining_fns[old_num]
        # The fn_text doesn't include the [^N]: prefix, we stripped that during parsing
        fn_section_lines.append(f'[^{new_num}]: {fn_text}')
        fn_section_lines.append('')

    # --- Assemble output ---
    output = body_text + '\n' + '\n'.join(fn_section_lines)

    # Clean up multiple blank lines
    output = re.sub(r'\n{4,}', '\n\n\n', output)

    # --- Write output ---
    OUTPUT_PATH.write_text(output, encoding="utf-8")
    log.append(f"Output written to {OUTPUT_PATH}")

    # --- Write log ---
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text('\n'.join(log), encoding="utf-8")
    print(f"Conversion complete.")
    print(f"  Output: {OUTPUT_PATH}")
    print(f"  Log: {LOG_PATH}")
    print(f"  Pure citation footnotes removed: {len(fns_to_remove)}")
    print(f"  Body citations converted: {len(body_changes)}")
    print(f"  Discursive footnote citations converted: {total_fn_changes}")
    print(f"  Remaining footnotes: {len(remaining_fns)}")


if __name__ == "__main__":
    main()
