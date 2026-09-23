# Paper Database

> 27 structured papers, each in its own `.md` file with YAML front matter and standardized sections.

## Categories

- [**VLA Models**](vla.md) — 13 papers on Vision-Language-Action models
- [**Skill-based RL**](skill-rl.md) — 7 papers on skill-based reinforcement learning  
- [**Surveys**](surveys.md) — 7 survey papers covering the field

## Paper Template

Each paper follows this structure:

```yaml
---
title: Paper Title
year: 2026
venue: ICLR / ICRA / RSS / arXiv
authors: [Author1, Author2]
tags: [VLA, temporal-modeling]
code: https://github.com/xxx/xxx
arxiv: "2608.26067"
open_source: true/false
---
## Key Idea           # One-line summary
## Architecture       # Technical approach
## Results            # Key numbers
## Strengths          # What it does well
## Limitations        # What it doesn't address
## Our Take           # Critical assessment
```

## How to Add a Paper

1. Copy `papers/_template.md`
2. Fill in the fields
3. Submit a PR — the CI will validate the format automatically


[📥 Download all papers as JSON](https://github.com/MXC66ai/vla-rl-Articles/tree/main/papers)