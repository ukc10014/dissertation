#!/usr/bin/env python3
"""
Convert Chicago Manual of Style bibliography entries from ch_03_combined.md
into BibTeX format. Output goes to bib/ch03_additions.bib.

Usage:
    python3 scripts/chicago_to_bibtex.py

Reads:  chapters/ch_03_combined.md (lines 358-727, the bibliography section)
Checks: bib/bibliography_ukc.bib (for duplicate detection)
Writes: bib/ch03_additions.bib (new entries only)
"""

import re
import sys
import os
from pathlib import Path
from collections import Counter


# ---------------------------------------------------------------------------
# 1. Read and split raw entries
# ---------------------------------------------------------------------------

def read_bibliography_section(path, start_line=358, end_line=727):
    """Read the bibliography section, return list of raw entry strings."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    bib_lines = lines[start_line - 1 : end_line]  # 0-indexed

    # Join into one blob, then split on blank-line boundaries
    # Each entry is separated by one or more blank lines
    entries = []
    current = []
    for line in bib_lines:
        stripped = line.strip()
        if stripped == "" or stripped == "## Bibliography {.unnumbered}":
            if current:
                entries.append(" ".join(current))
                current = []
        else:
            current.append(stripped)
    if current:
        entries.append(" ".join(current))
    return entries


# ---------------------------------------------------------------------------
# 2. Parse a single Chicago entry into structured fields
# ---------------------------------------------------------------------------

def clean_text(s):
    """Remove markdown formatting, escaped chars, etc."""
    # Normalize unicode whitespace (narrow no-break space, etc.) to regular space
    s = re.sub(r'[\u00a0\u202f\u2009\u200a\u2007\u2008]', ' ', s)
    s = s.replace("\\.", ".")
    s = s.replace("\\-", "-")
    s = s.replace("\\~", "~")
    s = s.replace("\\_", "_")
    s = re.sub(r"\\\)", ")", s)
    s = re.sub(r"\\\(", "(", s)
    s = re.sub(r"\\\[", "[", s)
    s = re.sub(r"\\\]", "]", s)
    # Remove markdown italics
    s = re.sub(r"\*([^*]+)\*", r"\1", s)
    return s.strip()


def extract_url(raw):
    """Extract URL from entry text."""
    # Match markdown links [text](url)
    urls = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', raw)
    if urls:
        # Return the URL part of the first link
        return urls[0][1]

    # Match bare URLs
    url_match = re.search(r'https?://\S+', clean_text(raw))
    if url_match:
        url = url_match.group(0).rstrip('.')
        # Clean trailing parentheses/punctuation
        url = re.sub(r'[)\].,;]+$', '', url)
        return url
    return None


def extract_doi(raw):
    """Extract DOI if present."""
    doi_match = re.search(r'(?:doi\.org/|doi:?\s*)(10\.[^\s\]\)]+)', raw, re.IGNORECASE)
    if doi_match:
        doi = doi_match.group(1).rstrip('.').rstrip(',')
        return doi
    return None


def extract_arxiv_id(raw):
    """Extract arXiv ID if present."""
    match = re.search(r'arxiv\.org/abs/([\d.]+)', raw, re.IGNORECASE)
    if match:
        return match.group(1)
    # Also check for arXiv:XXXX pattern
    match = re.search(r'arXiv[:\s]+(\d{4}\.\d+)', raw, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


def parse_authors(author_str):
    """Parse author string into list of (last, first) tuples.

    Chicago format: "LastName, F.N." or "LastName, F.N. and LastName2, F.N."
    Sometimes: "LastName, F.N., LastName2, F.N. and LastName3, F.N."
    """
    author_str = author_str.strip().rstrip(",").rstrip(".")
    # Handle "et al." / "et. al"
    has_etal = False
    if re.search(r'\bet\s*\.?\s*al\.?\b', author_str):
        has_etal = True
        author_str = re.sub(r',?\s*et\s*\.?\s*al\.?\s*,?', '', author_str).strip()

    # Split on " and " first
    parts = re.split(r'\s+and\s+', author_str)

    authors = []
    for part in parts:
        part = part.strip().rstrip(",")
        if not part:
            continue
        # Check for "Last, First" pattern
        # But also handle multiple authors separated by commas within one part
        # e.g. "Bai, Y., Kadavath, S., Kundu, S."
        # Heuristic: if there are multiple commas, try to split pairs
        comma_parts = [p.strip() for p in part.split(",")]
        if len(comma_parts) >= 2:
            # Try to pair them up: Last, First, Last, First, ...
            i = 0
            while i < len(comma_parts):
                last = comma_parts[i].strip()
                if i + 1 < len(comma_parts):
                    first = comma_parts[i + 1].strip()
                    # Check if 'first' looks like a first name (short, has initials or starts with uppercase)
                    if first and (len(first) <= 4 or first[0].isupper()) and not re.match(r'^[A-Z][a-z]{3,}$', first):
                        # Could be initials like "S." or "Y." or first name
                        # But also could be another last name
                        # Heuristic: if it's short (1-3 chars or has dots), treat as first name
                        if len(first) <= 4 or '.' in first or len(first.split()) == 1:
                            authors.append((last, first))
                            i += 2
                            continue
                # Single name without clear first/last split
                authors.append((last, ""))
                i += 1
        else:
            # Single name without comma
            name_parts = part.split()
            if len(name_parts) >= 2:
                authors.append((name_parts[-1], " ".join(name_parts[:-1])))
            else:
                authors.append((part, ""))

    if has_etal:
        authors.append(("others", ""))

    return authors


def parse_entry(raw):
    """Parse a single Chicago-style bibliography entry into a dict."""
    entry = {
        "raw": raw,
        "authors": [],
        "year": None,
        "title": None,
        "journal": None,
        "volume": None,
        "number": None,
        "pages": None,
        "publisher": None,
        "address": None,
        "booktitle": None,
        "editor": None,
        "url": None,
        "doi": None,
        "eprint": None,
        "note": None,
        "type": "misc",  # default
    }

    cleaned = clean_text(raw)
    entry["url"] = extract_url(raw)
    entry["doi"] = extract_doi(raw)
    entry["eprint"] = extract_arxiv_id(raw)

    # ---- Extract authors and year ----
    # Typical pattern: "Author, F., Year. 'Title...' or Author, F., Year. Title..."
    # Also: "Author, F. and Author2, G., Year."
    # Also: "Organization, Year."
    # Also: "Author, F., 2025a." or "Author, F., 2024b." (year with suffix)
    # Also: "Author, F. (2025) Title." (APA-style parenthesized year)

    year_match = None

    # Strategy 1: Look for comma-separated year (Chicago style)
    # Pattern: ", YYYY[a-c]. " where YYYY is a plausible year (1800-2099)
    year_match = re.search(r',\s*((?:1[89]|20)\d{2})[a-c]?\s*(?:\\\.|\.)?\s', cleaned)

    # Strategy 2: Look for parenthesized year (APA style)
    if not year_match:
        year_paren = re.search(r'\(((?:1[89]|20)\d{2})\)', cleaned)
        if year_paren:
            entry["year"] = year_paren.group(1)
            author_part = cleaned[:year_paren.start()].strip().rstrip(",").rstrip(".").rstrip("(").strip()
            rest = cleaned[year_paren.end():].strip()
            year_match = "done"  # sentinel

    # Strategy 3: Broader search — year at start or after whitespace
    if not year_match:
        year_match = re.search(r'((?:1[89]|20)\d{2})[a-c]?\s*(?:\\\.|\.)?\s', cleaned)

    if year_match and year_match != "done":
        entry["year"] = year_match.group(1)
        author_part = cleaned[:year_match.start()].strip().rstrip(",").rstrip(".").rstrip("(").strip()
        rest = cleaned[year_match.end():].strip()
    elif year_match != "done":
        author_part = ""
        rest = cleaned

    # Parse authors
    if author_part:
        entry["authors"] = parse_authors(author_part)

    # ---- Extract title ----
    # Title is usually in single quotes ('Title') or italics (*Title*)
    # For the raw text (before clean_text stripped italics), try to find title
    # Try quoted title first
    title_match = re.search(r"['\u2018\u2019]([^']+)['\u2018\u2019]", rest)
    if not title_match:
        # Try original raw for italicized title
        title_match_raw = re.search(r'\*([^*]+)\*', raw)
        if title_match_raw:
            entry["title"] = title_match_raw.group(1).strip().rstrip(".")
        else:
            # Take text up to first period or "Available at" as title
            title_end = re.search(r'\.\s+(?:Available|In:|New|Oxford|Cambridge|London|Berlin|Chicago|Princeton|Ithaca|Ann Arbor|Minneapolis|Falmouth|Dordrecht|Springer|Norton|Wiley|Penguin|MIT|Harvard|Bloomsbury|Hachette)', rest)
            if title_end:
                entry["title"] = rest[:title_end.start()].strip().rstrip(".")
            else:
                # Just take up to "Available at:" or first long pause
                avail = re.search(r'Available at:', rest, re.IGNORECASE)
                if avail:
                    entry["title"] = rest[:avail.start()].strip().rstrip(".")
                else:
                    entry["title"] = rest.split(".")[0].strip() if rest else None
    else:
        entry["title"] = title_match.group(1).strip().rstrip(".")

    # ---- Detect journal ----
    # Look for italicized text that comes after the title (in the raw text)
    # Journal usually appears as *Journal Name*, vol(issue), pp. XX-YY
    # Find all italic segments in raw
    italic_segments = re.findall(r'\*([^*]+)\*', raw)
    if italic_segments:
        # The first italic is usually the title (for books) or journal name (for articles)
        # If there's a second italic, it might be the journal
        for seg in italic_segments:
            seg_clean = seg.strip()
            # Skip if it matches the title
            if entry["title"] and seg_clean.rstrip(".") == entry["title"].rstrip("."):
                continue
            # Check if it looks like a journal (followed by volume/pages info)
            if re.search(re.escape(seg_clean) + r'\*\s*,\s*\d', raw):
                entry["journal"] = seg_clean
                break
            # Also check for journal patterns
            if any(kw in seg_clean.lower() for kw in ['journal', 'review', 'studies', 'proceedings',
                    'astrobiology', 'science', 'neuron', 'futures', 'psychology', 'bulletin',
                    'philosophical', 'policy', 'astronomy', 'today', 'monday', 'intelligence',
                    'autonomous', 'ieee', 'neurorobotics', 'frontiers', 'quarterly']):
                entry["journal"] = seg_clean
                break

    # ---- Extract volume, number, pages ----
    vol_match = re.search(r'(\d+)\((\d+)\)', cleaned)
    if vol_match:
        entry["volume"] = vol_match.group(1)
        entry["number"] = vol_match.group(2)
    elif entry.get("journal"):
        # Look for volume number after the journal name
        journal_escaped = re.escape(entry["journal"])
        vol_after_journal = re.search(journal_escaped + r'\*?\s*,\s*(\d+)', cleaned)
        if not vol_after_journal:
            # Try in raw text (journal might be in italics)
            vol_after_journal = re.search(journal_escaped + r'\*\s*,\s*(\d+)', raw)
        if vol_after_journal:
            vol_str = vol_after_journal.group(1)
            # Sanity check: volume should be < 1000
            if int(vol_str) < 1000:
                entry["volume"] = vol_str

    pages_match = re.search(r'pp?\.\s*([\d]+)\s*[-–—]\s*([\d]+)', cleaned)
    if pages_match:
        entry["pages"] = f"{pages_match.group(1)}--{pages_match.group(2)}"

    # ---- Extract publisher and address ----
    # Strategy: Find "City: Publisher" patterns where publisher contains known keywords
    # Scan for publisher names, then find the "City:" before them
    PUBLISHER_NAMES = [
        "Oxford University Press", "Cambridge University Press",
        "Cornell University Press", "Harvard University Press",
        "Princeton University Press", "Stanford University Press",
        "University of Minnesota Press", "University of Chicago Press",
        "MIT Press", "Edinburgh University Press", "Bristol University Press",
        "Farrar, Straus and Giroux", "Hill and Wang",
        "Springer", "Norton", "Wiley-Blackwell", "Wiley", "Penguin",
        "Macmillan", "Bloomsbury", "Urbanomic", "Urbanomic/Sequence Press",
        "Harper Perennial", "Harper & Row", "Harper",
        "Reidel", "Basic Books", "IOS Press",
        "Harcourt Brace Jovanovich", "Open Humanities Press",
        "Nelson Doubleday", "Viking", "Tor Books",
    ]
    CITY_NAMES = [
        "Cambridge, MA", "Ithaca, NY", "Stanford, CA", "Dordrecht, NL",
        "Ann Arbor", "New York", "Oxford", "Cambridge", "London", "Berlin",
        "Chicago", "Princeton", "Minneapolis", "Falmouth", "Dordrecht",
        "Boston", "Bristol", "Chichester", "Westport", "Brighton",
    ]
    for pub_name in PUBLISHER_NAMES:
        pub_idx = cleaned.find(pub_name)
        if pub_idx == -1:
            continue
        # Look backwards for "City: " pattern
        before = cleaned[:pub_idx].rstrip().rstrip(':').rstrip()
        for city_name in CITY_NAMES:
            if before.endswith(city_name):
                entry["address"] = city_name
                entry["publisher"] = pub_name
                break
        if entry.get("publisher"):
            break

    # ---- Extract editor / "In:" pattern ----
    in_match = re.search(r'In:\s*(.*?)\s*(?:eds?\.|ed\.)', cleaned)
    if in_match:
        entry["editor"] = in_match.group(1).strip().rstrip(",")

    # Also look for "In: ... *BookTitle*"
    in_book_match = re.search(r'In:.*?\*([^*]+)\*', raw)
    if in_book_match:
        entry["booktitle"] = in_book_match.group(1).strip()

    # Also check for editors after title: "ed. Name" or "Edited by"
    if not entry["editor"]:
        ed_match = re.search(r'(?:edited by|eds?\.)\s+([\w.\s,&]+?)(?:\.|,\s*\*)', cleaned, re.IGNORECASE)
        if ed_match:
            entry["editor"] = ed_match.group(1).strip()

    # ---- Classify entry type ----
    entry["type"] = classify_entry(entry, raw)

    # ---- Handle special note for accessed date ----
    accessed_match = re.search(r'\(Accessed:\s*([^)]+)\)', raw)
    if accessed_match:
        entry["note"] = f"Accessed: {accessed_match.group(1)}"

    return entry


def classify_entry(entry, raw):
    """Determine BibTeX entry type based on parsed fields."""
    cleaned = clean_text(raw)

    # Proceedings / inproceedings
    if entry.get("booktitle") and re.search(r'Proceedings|Conference', entry.get("booktitle", ""), re.IGNORECASE):
        return "inproceedings"

    # Incollection: has "In:" with editor and booktitle
    if entry.get("booktitle") and entry.get("editor"):
        return "incollection"

    # Has "In:" with a booktitle (even without explicit editor)
    if entry.get("booktitle"):
        return "incollection"

    # Article: has journal
    if entry.get("journal"):
        return "article"

    # Book: has publisher
    if entry.get("publisher"):
        return "book"

    # arXiv
    if entry.get("eprint"):
        return "misc"

    # Default
    return "misc"


# ---------------------------------------------------------------------------
# 3. Generate citation keys
# ---------------------------------------------------------------------------

def transliterate(s):
    """Convert accented characters to ASCII equivalents for citation keys."""
    TRANSLIT = {
        'Ć': 'C', 'ć': 'c', 'Č': 'C', 'č': 'c',
        'Š': 'S', 'š': 's', 'Ž': 'Z', 'ž': 'z',
        'ë': 'e', 'ë': 'e', 'ü': 'u', 'ö': 'o', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'É': 'E',
        'á': 'a', 'à': 'a', 'â': 'a',
        'í': 'i', 'ì': 'i', 'î': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u',
        'ñ': 'n', 'Ñ': 'N',
        '‑': '-', '–': '-', '—': '-',  # various hyphens
    }
    return ''.join(TRANSLIT.get(c, c) for c in s)


def make_surname(name_tuple):
    """Extract clean surname for citation key."""
    last = name_tuple[0]
    # Transliterate accented chars first
    last = transliterate(last)
    # Remove special chars, keep letters
    last = re.sub(r'[^A-Za-z]', '', last)
    # Handle prefixes like "de", "von" etc - capitalize
    if last and last[0].islower():
        last = last.capitalize()
    return last


def generate_key(entry):
    """Generate a citation key like AuthorYear, AuthorAuthorYear, etc."""
    authors = entry.get("authors", [])
    year = entry.get("year", "XXXX")

    if not authors:
        # Use first significant word of title
        title = entry.get("title", "Unknown") or "Unknown"
        word = re.sub(r'[^A-Za-z]', '', title.split()[0]) if title.split() else "Unknown"
        return f"{word}{year}"

    # Filter out "others"
    real_authors = [a for a in authors if a[0] != "others"]

    if len(real_authors) == 0:
        word = re.sub(r'[^A-Za-z]', '', (entry.get("title", "Unknown") or "Unknown").split()[0])
        return f"{word}{year}"
    elif len(real_authors) == 1:
        key = make_surname(real_authors[0])
    elif len(real_authors) == 2:
        key = make_surname(real_authors[0]) + make_surname(real_authors[1])
    else:
        key = make_surname(real_authors[0]) + "EtAl"

    # Handle "et al" in original
    if any(a[0] == "others" for a in authors) and len(real_authors) == 1:
        key = make_surname(real_authors[0]) + "EtAl"

    return f"{key}{year}"


def disambiguate_keys(entries):
    """Add a, b, c suffixes to duplicate keys."""
    key_counts = Counter(e["key"] for e in entries)
    key_indices = {}
    for e in entries:
        k = e["key"]
        if key_counts[k] > 1:
            idx = key_indices.get(k, 0)
            key_indices[k] = idx + 1
            e["key"] = k + chr(ord('a') + idx)


# ---------------------------------------------------------------------------
# 4. Format as BibTeX
# ---------------------------------------------------------------------------

def escape_bibtex(s):
    """Escape special BibTeX characters."""
    if not s:
        return s
    # Protect special chars
    s = s.replace("&", r"\&")
    # Don't double-escape existing LaTeX
    # Handle curly braces carefully
    return s


def format_bibtex(entry):
    """Format a parsed entry as a BibTeX string."""
    btype = entry["type"]
    key = entry["key"]

    # Format authors
    if entry["authors"]:
        author_strs = []
        for last, first in entry["authors"]:
            if last == "others":
                author_strs.append("others")
            elif first:
                author_strs.append(f"{last}, {first}")
            else:
                author_strs.append(last)
        author_field = " and ".join(author_strs)
    else:
        author_field = None

    lines = [f"@{btype}{{{key},"]

    def add_field(name, value):
        if value:
            value = escape_bibtex(str(value))
            lines.append(f"  {name} = {{{value}}},")

    add_field("author", author_field)
    add_field("title", entry.get("title"))
    add_field("year", entry.get("year"))

    if btype == "article":
        add_field("journal", entry.get("journal"))
        add_field("volume", entry.get("volume"))
        add_field("number", entry.get("number"))
        add_field("pages", entry.get("pages"))
    elif btype == "book":
        add_field("publisher", entry.get("publisher"))
        add_field("address", entry.get("address"))
    elif btype in ("incollection", "inproceedings"):
        add_field("booktitle", entry.get("booktitle"))
        add_field("editor", entry.get("editor"))
        add_field("publisher", entry.get("publisher"))
        add_field("address", entry.get("address"))
        add_field("pages", entry.get("pages"))

    if entry.get("eprint"):
        add_field("eprint", entry["eprint"])
        lines.append("  archivePrefix = {arXiv},")

    if entry.get("doi"):
        add_field("doi", entry["doi"])
    elif entry.get("url"):
        add_field("url", entry["url"])

    add_field("note", entry.get("note"))

    lines.append("}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 5. Duplicate detection against existing bib file
# ---------------------------------------------------------------------------

def load_existing_keys(bib_path):
    """Load existing citation keys and basic metadata from a .bib file."""
    text = Path(bib_path).read_text(encoding="utf-8")
    keys = set()
    entries = {}

    for match in re.finditer(r'@\w+\{([^,]+),', text):
        key = match.group(1).strip()
        keys.add(key)

        # Try to extract author/year/title for fuzzy matching
        # Find the entry text (up to the next @ or end)
        start = match.end()
        end = text.find('\n@', start)
        if end == -1:
            end = len(text)
        entry_text = text[start:end]

        author_m = re.search(r'author\s*=\s*\{([^}]+)\}', entry_text, re.IGNORECASE)
        year_m = re.search(r'year\s*=\s*\{?(\d{4})\}?', entry_text, re.IGNORECASE)
        title_m = re.search(r'title\s*=\s*\{([^}]+)\}', entry_text, re.IGNORECASE)

        author = author_m.group(1).lower() if author_m else ""
        year = year_m.group(1) if year_m else ""
        title = title_m.group(1).lower() if title_m else ""

        entries[key] = {
            "author": author,
            "year": year,
            "title": title,
            "title_words": set(re.findall(r'\w+', title))
        }

    return keys, entries


def is_duplicate(new_entry, existing_keys, existing_entries):
    """Check if a new entry is a duplicate of an existing one."""
    # Exact key match
    if new_entry["key"] in existing_keys:
        return True, new_entry["key"]

    # Fuzzy match by author + year + title words
    new_year = new_entry.get("year", "")
    new_title = (new_entry.get("title") or "").lower()
    new_title_words = set(re.findall(r'\w{4,}', new_title))  # words 4+ chars

    new_authors = new_entry.get("authors", [])
    new_surname = ""
    if new_authors:
        new_surname = new_authors[0][0].lower()

    for ekey, edata in existing_entries.items():
        # Year must match
        if edata["year"] != new_year:
            continue

        # Author surname must appear
        if new_surname and new_surname not in edata["author"]:
            continue

        # Check title word overlap
        if new_title_words and edata["title_words"]:
            overlap = new_title_words & edata["title_words"]
            if len(overlap) >= 3 or (len(overlap) >= 2 and len(new_title_words) <= 4):
                return True, ekey

    return False, None


# ---------------------------------------------------------------------------
# 6. Main
# ---------------------------------------------------------------------------

def main():
    base = Path(__file__).resolve().parent.parent
    ch03_path = base / "chapters" / "ch_03_combined.md"
    bib_path = base / "bib" / "bibliography_ukc.bib"
    output_path = base / "bib" / "ch03_additions.bib"

    if not ch03_path.exists():
        print(f"ERROR: {ch03_path} not found")
        sys.exit(1)
    if not bib_path.exists():
        print(f"ERROR: {bib_path} not found")
        sys.exit(1)

    # Load existing bib
    existing_keys, existing_entries = load_existing_keys(bib_path)
    print(f"Loaded {len(existing_keys)} existing keys from {bib_path.name}")

    # Read and parse ch03 bibliography
    raw_entries = read_bibliography_section(str(ch03_path))
    print(f"Found {len(raw_entries)} raw bibliography entries in ch_03_combined.md")

    parsed = []
    parse_errors = []
    for i, raw in enumerate(raw_entries):
        try:
            entry = parse_entry(raw)
            entry["key"] = generate_key(entry)
            parsed.append(entry)
        except Exception as e:
            parse_errors.append((i, raw[:80], str(e)))

    if parse_errors:
        print(f"\n--- Parse errors ({len(parse_errors)}) ---")
        for idx, snippet, err in parse_errors:
            print(f"  Entry {idx}: {snippet}... -> {err}")

    # Disambiguate keys
    disambiguate_keys(parsed)

    # Check for duplicates
    new_entries = []
    duplicates = []
    for entry in parsed:
        is_dup, match_key = is_duplicate(entry, existing_keys, existing_entries)
        if is_dup:
            duplicates.append((entry["key"], match_key, (entry.get("title") or "")[:60]))
        else:
            new_entries.append(entry)

    print(f"\nDuplicates found (skipped): {len(duplicates)}")
    for new_key, old_key, title in duplicates:
        print(f"  {new_key} matches existing {old_key}: {title}")

    print(f"New entries to write: {len(new_entries)}")

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"% Auto-generated from ch_03_combined.md bibliography section\n")
        f.write(f"% {len(new_entries)} new entries\n")
        f.write(f"% Review before appending to bibliography_ukc.bib\n\n")
        for entry in new_entries:
            f.write(format_bibtex(entry))
            f.write("\n\n")

    print(f"\nOutput written to {output_path}")

    # Summary of entry types
    type_counts = Counter(e["type"] for e in new_entries)
    print(f"\nEntry types: {dict(type_counts)}")

    # Flag entries that may need manual review
    print(f"\n--- Entries that may need manual review ---")
    review_count = 0
    for entry in new_entries:
        issues = []
        if not entry.get("title"):
            issues.append("missing title")
        if not entry.get("year"):
            issues.append("missing year")
        if not entry.get("authors"):
            issues.append("missing authors")
        if entry.get("title") and "unspecified" in entry["title"].lower():
            issues.append("placeholder title")
        if entry.get("title") and "pending" in (entry.get("note") or "").lower():
            issues.append("pending details")
        if issues:
            print(f"  {entry['key']}: {', '.join(issues)}")
            review_count += 1
    if review_count == 0:
        print("  (none)")


if __name__ == "__main__":
    main()
