#!/usr/bin/env python3
"""Build a hierarchical argument graph JSON from dissertation markdown files.

The output is designed for web mind-map tools (e.g. React Flow, Cytoscape,
D3 force trees):

- level 0: dissertation root
- level 1: chapter/document nodes
- level 2: section/subsection nodes (from markdown headings)
- level 3: source nodes (citation keys found in each section)

Usage:
    python3 scripts/build_argument_graph.py
    python3 scripts/build_argument_graph.py --output mindmap/argument_graph.json
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Set, Tuple


DEFAULT_INPUTS = [
    "chapters/ch_01_upg.md",
    "chapters/ch_03_combined.md",
    "chapters/ch_04.md",
    "chapters/outline/upgrade_outline_v9.md",
]
DEFAULT_BIB = "bib/bibliography_ukc.bib"
DEFAULT_OUTPUT = "mindmap/argument_graph.json"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
CITE_RE = re.compile(r"@([A-Za-z0-9_:\-./]+)")
BIBKEY_RE = re.compile(r"@\w+\{([^,\s]+)")


@dataclass
class Node:
    id: str
    label: str
    node_type: str
    level: int
    meta: Dict[str, str] = field(default_factory=dict)


def slugify(value: str) -> str:
    s = value.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") or "node"


def parse_bib_keys(path: Path) -> Set[str]:
    if not path.exists():
        return set()
    keys = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = BIBKEY_RE.search(line)
        if m:
            keys.add(m.group(1))
    return keys


def extract_sections(path: Path) -> List[Tuple[int, str, List[str]]]:
    """Return list of (heading_level, heading_title, paragraph_lines_until_next_heading)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    sections: List[Tuple[int, str, List[str]]] = []
    current_level = 0
    current_title = "Document"
    buffer: List[str] = []

    for line in lines:
        h = HEADING_RE.match(line)
        if h:
            # flush previous section
            if buffer or current_title != "Document":
                sections.append((current_level, current_title, buffer))
            current_level = len(h.group(1))
            current_title = h.group(2).strip()
            buffer = []
        else:
            buffer.append(line)

    if buffer or current_title != "Document":
        sections.append((current_level, current_title, buffer))

    return sections


def citations_in_lines(lines: List[str], known_keys: Set[str]) -> List[str]:
    found: List[str] = []
    seen = set()
    for line in lines:
        for raw_key in CITE_RE.findall(line):
            key = raw_key.lstrip("-")  # handles forms like -@Bostrom2014
            if key in seen:
                continue
            if not known_keys or key in known_keys:
                seen.add(key)
                found.append(key)
    return found


def build_graph(input_files: List[Path], bib_keys: Set[str]) -> Dict[str, object]:
    nodes: List[Node] = []
    edges: List[Dict[str, str]] = []

    root_id = "thesis"
    nodes.append(Node(id=root_id, label="PhD Thesis Argument", node_type="root", level=0))

    for file_path in input_files:
        doc_id = f"doc:{slugify(file_path.stem)}"
        nodes.append(
            Node(
                id=doc_id,
                label=file_path.stem,
                node_type="document",
                level=1,
                meta={"path": str(file_path)},
            )
        )
        edges.append({"source": root_id, "target": doc_id, "type": "contains"})

        sections = extract_sections(file_path)
        parents_by_level: Dict[int, str] = {0: doc_id}

        for idx, (h_level, title, lines) in enumerate(sections, start=1):
            section_id = f"sec:{slugify(file_path.stem)}:{idx}:{slugify(title)}"
            section_level = min(h_level + 1, 4) if h_level > 0 else 2
            nodes.append(
                Node(
                    id=section_id,
                    label=title,
                    node_type="section",
                    level=section_level,
                    meta={"source_file": str(file_path), "heading_level": str(h_level)},
                )
            )

            parent_key = max((lvl for lvl in parents_by_level if lvl < h_level), default=0)
            parent_id = parents_by_level[parent_key]
            edges.append({"source": parent_id, "target": section_id, "type": "contains"})
            parents_by_level[h_level] = section_id

            for ckey in citations_in_lines(lines, bib_keys):
                cite_id = f"cite:{ckey}"
                if not any(n.id == cite_id for n in nodes):
                    nodes.append(Node(id=cite_id, label=ckey, node_type="source", level=5))
                edges.append({"source": section_id, "target": cite_id, "type": "cites"})

    return {
        "meta": {
            "documents": [str(p) for p in input_files],
            "description": "Hierarchical argument graph with citation leaves",
        },
        "nodes": [n.__dict__ for n in nodes],
        "edges": edges,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--bib", default=DEFAULT_BIB)
    parser.add_argument("--inputs", nargs="*", default=DEFAULT_INPUTS)
    args = parser.parse_args()

    in_paths = [Path(p) for p in args.inputs]
    missing = [str(p) for p in in_paths if not p.exists()]
    if missing:
        raise SystemExit(f"Missing input files: {', '.join(missing)}")

    bib_keys = parse_bib_keys(Path(args.bib))
    graph = build_graph(in_paths, bib_keys)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Wrote graph JSON: {output_path}")
    print(f"Nodes: {len(graph['nodes'])}")
    print(f"Edges: {len(graph['edges'])}")


if __name__ == "__main__":
    main()