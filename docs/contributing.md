# Contributing Guide

> Help us keep this the most up-to-date VLA × Skill-RL paper collection!

## How to Add a New Paper

### Option A: Submit via Issue

1. Open a [New Issue](https://github.com/MXC66ai/vla-rl-Articles/issues/new)
2. Use the "New Paper" template
3. Fill in: title, authors, venue, arXiv ID, and a 2-3 sentence summary

### Option B: Submit via Pull Request

1. Fork this repository
2. Copy `papers/_template.md` to `papers/2026-paper-name.md`
3. Fill in all fields:

```yaml
---
title: "Full Paper Title"
year: 2026
venue: ICLR / ICRA / RSS / CoRL / AAAl / arXiv
authors: [Author1, Author2]
tags: [VLA, temporal-modeling]
code: https://github.com/author/repo
project: https://project-page.github.io
arxiv: "2608.26067"
open_source: true
---
## Key Idea          # One sentence
## Architecture      # Model structure
## Method            # Training / inference details
## Results           # Key numbers with benchmark
## Strengths         # 2-3 bullet points
## Limitations       # 2-3 bullet points
## Our Take          # Your critical assessment
```

4. Submit the PR — CI will validate format automatically

## Guidelines

- ✅ Papers must be from 2025–2026 (or earlier if foundational)
- ✅ Papers must relate to VLA / VLM / Skill-RL / Robot Learning
- ✅ Include at least `Key Idea` and `Results`
- ❌ No duplicate entries (check first!)
- ❌ No papers without verifiable source (arXiv, DOI, or conference page)

## Review Process

```
PR Submitted → CI Format Check → Human Review → Merged
    (auto)        (24-48h max)       
```

## Recognition

Contributors are listed in the [README](../README.md#contributors).  
Top contributors get write access to the repository.