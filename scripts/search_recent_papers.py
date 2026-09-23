#!/usr/bin/env python3
"""
Weekly arXiv Paper Scanner for VLA × Skill-based RL.

Usage:
    # Simple search (last 30 days)
    python search_recent_papers.py

    # Weekly scan with dedup against existing papers
    python search_recent_papers.py --days 7 --check-existing ../papers/

    # Full scan + auto-generate paper files
    python search_recent_papers.py --days 7 --check-existing ../papers/ --generate ../papers/
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

ARXIV_API = "https://export.arxiv.org/api/query"
QUERIES = [
    ("VLA", '"vision language action" robot'),
    ("VLA", '"vision-language-action" robot'),
    ("VLM-Robot", '"vision language model" robot manipulation'),
    ("Skill-RL", '"skill" "reinforcement learning" robot manipulation'),
    ("Skill-RL", '"skill learning" robot'),
    ("RL-Accel", '"accelerated" robot learning'),
    ("World-Model", '"world model" robot learning'),
    ("Embodied", '"embodied" VLA robot'),
]


def search_arxiv(query, max_results=15):
    """Search arXiv API for papers matching the query."""
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "VLA-Paper-Scanner/2.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            xml_data = resp.read().decode("utf-8")
    except Exception as e:
        print(f"[WARN] arXiv query failed: {e}", file=sys.stderr)
        return []

    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_data)
    papers = []
    for entry in root.findall("a:entry", ns):
        title = entry.find("a:title", ns).text.strip().replace("\n", " ").strip()
        abstract = entry.find("a:summary", ns).text.strip().replace("\n", " ")
        published = entry.find("a:published", ns).text[:10]
        link = entry.find("a:id", ns).text
        authors = [a.find("a:name", ns).text for a in entry.findall("a:author", ns)]

        # Extract arXiv ID from link
        arxiv_id = ""
        m = re.search(r"(\d{4}\.\d{4,5})", link)
        if m:
            arxiv_id = m.group(1)
        m2 = re.search(r"abs/(\d{4}\.\d{4,5})", link)
        if m2:
            arxiv_id = m2.group(1)

        papers.append({
            "title": title,
            "abstract": abstract[:300],
            "published": published,
            "url": link,
            "arxiv_id": arxiv_id,
            "authors": authors[:3],
        })
    return papers


def load_existing_papers(papers_dir):
    """Load arXiv IDs from existing paper files for dedup."""
    existing = set()
    if not papers_dir or not os.path.isdir(papers_dir):
        return existing
    for fname in os.listdir(papers_dir):
        if not fname.endswith(".md") or fname.startswith("_"):
            continue
        fpath = os.path.join(papers_dir, fname)
        with open(fpath) as f:
            content = f.read()
        m = re.search(r'^arxiv:\s*"([^"]+)"', content, re.MULTILINE)
        if m:
            existing.add(m.group(1))
        # Also match title as fallback
        m2 = re.search(r'^title:\s*"([^"]+)"', content, re.MULTILINE)
        if m2:
            existing.add(m2.group(1)[:80].lower())
    return existing


def generate_paper_file(paper, output_dir):
    """Generate a structured .md file for a new paper."""
    arxiv_id = paper.get("arxiv_id", "")
    year = paper["published"][:4]
    title_short = paper["title"].split(":")[0].split(".")[0][:40]
    safe_name = re.sub(r'[^a-zA-Z0-9\- ]', '', title_short).strip().lower().replace(" ", "-")[:30]
    if arxiv_id:
        safe_name = arxiv_id.split(".")[-1][:10]
    fname = f"{year}-{safe_name}.md"
    fpath = os.path.join(output_dir, fname)

    if os.path.exists(fpath):
        print(f"  Skipping (exists): {fname}")
        return None

    tags = []
    title_lower = paper["title"].lower()
    abstract_lower = paper["abstract"].lower()
    if any(kw in title_lower or kw in abstract_lower for kw in ["vla", "vision-language-action", "vision language action"]):
        tags.append("VLA")
    if any(kw in title_lower or kw in abstract_lower for kw in ["skill", "reinforcement learning", "rl"]):
        tags.append("skill-RL")
    if "world model" in title_lower or "world model" in abstract_lower:
        tags.append("world-model")
    if "survey" in title_lower or "review" in title_lower:
        tags.append("survey")

    content = f"""---
title: "{paper['title']}"
year: {year}
venue: arXiv
authors: {json.dumps(paper['authors'])}
tags: {json.dumps(tags)}
arxiv: "{arxiv_id}"
open_source: false
---
## Key Idea
<!-- Auto-generated from abstract --> {paper['abstract'][:200]}

## Architecture
<!-- Add architecture details after review -->

## Results
<!-- Add key results after review -->

## Strengths & Limitations
| Strengths | Limitations |
|:---|:---|
| | |

## Our Take
<!-- Add your assessment after reading the paper -->
"""
    with open(fpath, "w") as f:
        f.write(content)
    print(f"  Created: {fname}")
    return fname


def main():
    # Parse args
    days = 30
    check_dir = None
    gen_dir = None
    output = "new_papers.json"

    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--days" and i + 1 < len(args):
            days = int(args[i + 1])
        elif a == "--check-existing" and i + 1 < len(args):
            check_dir = args[i + 1]
        elif a == "--generate" and i + 1 < len(args):
            gen_dir = args[i + 1]
        elif a == "--output" and i + 1 < len(args):
            output = args[i + 1]

    existing_ids = load_existing_papers(check_dir) if check_dir else set()
    print(f"[INFO] Existing: {len(existing_ids)} papers loaded")
    print(f"[INFO] Window: {days} days")

    all_papers = []
    seen_titles = set()
    cutoff = datetime.now() - timedelta(days=days)

    for category, query in QUERIES:
        papers = search_arxiv(query)
        for p in papers:
            try:
                pub_date = datetime.strptime(p["published"], "%Y-%m-%d")
            except ValueError:
                pub_date = datetime.now()
            if pub_date < cutoff:
                continue

            # Dedup by arXiv ID + title
            dedup_key = p.get("arxiv_id", "") or p["title"][:80].lower()
            if not dedup_key or dedup_key in seen_titles:
                continue
            seen_titles.add(dedup_key)

            # Skip if already exists in papers/
            if dedup_key in existing_ids or p["title"][:80].lower() in existing_ids:
                continue

            p["category"] = category
            all_papers.append(p)
        time.sleep(3)

    # Sort by date
    all_papers.sort(key=lambda x: x["published"], reverse=True)

    print(f"[RESULT] New papers found: {len(all_papers)}")

    for i, p in enumerate(all_papers, 1):
        print(f"\n  [{i}] {p['title']}")
        print(f"       Date: {p['published']} | arXiv: {p.get('arxiv_id','?')}")

    # Save JSON output
    with open(output, "w") as f:
        json.dump(all_papers, f, indent=2, ensure_ascii=False)
    print(f"\n[OUTPUT] Saved to {output}")

    # Generate paper files
    if gen_dir and all_papers:
        os.makedirs(gen_dir, exist_ok=True)
        print(f"\n[GEN] Generating paper files in {gen_dir}...")
        for p in all_papers:
            generate_paper_file(p, gen_dir)

    # Exit with code for CI
    if all_papers:
        print(f"\n✅ {len(all_papers)} new paper(s) — ready for PR")
    else:
        print("\n✅ No new papers found")

    return 0


if __name__ == "__main__":
    sys.exit(main())