---
title: "ProphRL: VLA + RL + World Model"
year: 2026
venue: arXiv
authors: [Fudan University]
tags: [VLA, RL, world-model, fine-tuning]
code: ""
project: ""
dataset: [AgiBot, DROID, LIBERO, BRIDGE]
benchmark: [AgiBot, DROID, LIBERO, BRIDGE]
task: [manipulation]
robot: [multiple]
open_source: false
---
## Key Idea
Trains a Prophet world model as a differentiable simulator for online VLA fine-tuning via RL.

## Architecture
- **Paradigm**: VLA + World Model + Online RL
- **Key Innovation**: World model predicts action outcomes → VLA learns from imagined rollouts
- **Models Tested**: VLA-adapter-0.5B, Pi0.5-3B, OpenVLA-OFT-7B

## Results
| Benchmark | Improvement |
|:---|---:|
| AgiBot/DROID/LIBERO/BRIDGE | +5–17% SR |
| Real Robot | +24–30% SR |

## Our Take
Model-agnostic framework; world model as simulator is the key insight — addresses the fundamental limitation that VLAs cannot practice