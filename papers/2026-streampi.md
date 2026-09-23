---
title: "StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models"
year: 2026
venue: arXiv
authors: []
tags: [VLA, temporal-modeling, streaming]
code: ""
project: "https://happinesslz.github.io/projects/StreamPI/"
dataset: []
benchmark: [LIBERO, Real-robot]
task: [memory-dependent-manipulation, precise-perception]
robot: []
open_source: true
arxiv: "2608.26067"
---
## Key Idea
Equips single-frame VLAs (π₀.5) with temporal reasoning capability via instruction-anchored causal attention — zero additional parameters.

## Architecture
- **Backbone**: π₀.5
- **Innovation**: Instruction-anchored temporal modeling treats (image, text) as atomic units: bidirectional attention within pairs, causal across pairs
- **Training**: Random-interval streaming training bridges sync training → async deployment gap

## Results
| Benchmark | Metric | Score |
|:---|---:|---:|
| LIBERO | Success Rate | Outperforms π₀.5 |
| Real-robot (memory) | Success Rate | Superior |
| Real-robot (precise perception) | Success Rate | Superior |

## Strengths & Limitations
| Strengths | Limitations |
|:---|:---|
| Zero additional parameters | Requires pre-trained single-frame VLA |
| Async deployment support | Limited to VLA models with LLM backbone |
| Inherits pre-trained weights | |

## Our Take
An elegant solution to the temporal bottleneck — key innovation is treating the instruction as a persistent semantic anchor