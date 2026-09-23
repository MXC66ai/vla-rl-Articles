#!/usr/bin/env python3
"""
Search Recent Papers: VLA/VLM & Skill-based RL for Robot Learning.

This script queries arXiv and other sources for the latest papers
on Vision-Language-Action (VLA) models, Vision-Language Models (VLMs)
for robotics, and Skill-based Reinforcement Learning.

Usage:
    python search_recent_papers.py [--days 30] [--output papers.json]
"""

import json
import sys
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

ARXIV_API = "https://export.arxiv.org/api/query"

def search_arxiv(query: str, max_results: int = 20) -> list[dict]:
    """Search arXiv via the official API."""
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    print(f"[arXiv] Searching: {query[:60]}...")

    req = urllib.request.Request(url, headers={"User-Agent": "VLA-Paper-Search/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            xml_data = resp.read().decode("utf-8")
    except Exception as e:
        print(f"  Error: {e}")
        return []

    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_data)
    papers = []

    for entry in root.findall("a:entry", ns):
        title = entry.find("a:title", ns).text.strip().replace("\n", " ")
        abstract = entry.find("a:summary", ns).text.strip().replace("\n", " ")
        published = entry.find("a:published", ns).text[:10]
        link = entry.find("a:id", ns).text
        authors = [a.find("a:name", ns).text for a in entry.findall("a:author", ns)]

        papers.append({
            "title": title,
            "abstract": abstract[:500],
            "published": published,
            "url": link,
            "authors": authors[:5],  # keep first 5
        })

    return papers


def main():
    days = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1] == "--days" else 30
    output = sys.argv[3] if len(sys.argv) > 3 and sys.argv[1] == "--output" else "papers.json"

    queries = [
        # VLA queries
        ("VLA", '"vision language action" robot manipulation'),
        ("VLM-Robot", '"vision language model" robot manipulation'),
        ("Embodied VLA", '"embodied" "vision language action"'),
        # Skill-based RL queries
        ("Skill-RL", '"skill" "reinforcement learning" robot'),
        ("Skill-Learning", '"skill learning" robot manipulation'),
        ("RL-Acceleration", '"accelerated" "reinforcement learning" robot'),
    ]

    all_papers = []
    seen_titles = set()

    for category, query in queries:
        papers = search_arxiv(query, max_results=10)
        cutoff = datetime.now() - timedelta(days=days)

        for p in papers:
            try:
                pub_date = datetime.strptime(p["published"], "%Y-%m-%d")
            except ValueError:
                pub_date = datetime.now()

            if pub_date < cutoff:
                continue

            # Deduplicate
            title_key = p["title"][:80].lower()
            if title_key in seen_titles:
                continue
            seen_titles.add(title_key)

            p["category"] = category
            all_papers.append(p)

        time.sleep(3)  # arXiv API rate limit

    # Sort by date descending
    all_papers.sort(key=lambda x: x["published"], reverse=True)

    print(f"\n{'='*60}")
    print(f"Found {len(all_papers)} recent papers (last {days} days)")
    print(f"{'='*60}")

    for i, p in enumerate(all_papers, 1):
        print(f"\n[{i}] {p['title']}")
        print(f"    Date: {p['published']}  |  Category: {p['category']}")
        print(f"    URL:  {p['url']}")
        print(f"    Abstract: {p['abstract'][:200]}...")

    # Save to JSON
    with open(output, "w") as f:
        json.dump(all_papers, f, indent=2, ensure_ascii=False)
    print(f"\nSaved {len(all_papers)} papers to {output}")


if __name__ == "__main__":
    main()