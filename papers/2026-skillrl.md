---
title: "SkillRL: Recursive Skill Evolution for Reinforcement Learning Agents"
year: 2026
venue: arXiv
authors: []
tags: [skill-RL, LLM, GRPO, skill-evolution]
code: ""
project: ""
benchmark: [ALFWorld, WebShop]
task: [long-horizon-reasoning]
base_model: Qwen2.5-7B-Instruct
open_source: false
---
## Key Idea
Three-stage pipeline: skill distillation (teacher=o3) → skill retrieval (K=6) → recursive skill evolution via GRPO. Skill library and policy co-evolve.
## Results
| Benchmark | Score | vs GRPO |
|:---|---:|---:|
| ALFWorld | 89.9% | +12.3% |
| WebShop | 72.7% | +10.5% |
## Our Take
The co-evolution mechanism is the key insight — static skill libraries plateau, evolving ones don't
