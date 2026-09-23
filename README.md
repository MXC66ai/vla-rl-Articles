# VLA/VLM & Skill-based RL for Accelerated Robot Learning — Recent Papers

> **Collected**: September 2026  
> **Scope**: Vision-Language-Action (VLA) models, Vision-Language Models (VLMs) for robotics, and Skill-based Reinforcement Learning for accelerated robot learning  
> **Time window**: August–September 2026 (last month)

---

## 📋 Overview

This repository contains a curated collection of **recent papers** at the intersection of:

1. **VLA / VLM for Robotics** — Models that unify vision, language, and action for end-to-end robot control
2. **Skill-based Reinforcement Learning** — Using skills as reusable primitives to accelerate RL for complex, long-horizon robot tasks

The collection covers papers from top venues (ICLR 2026, ICRA 2026, RSS 2026, CoRL 2025, IJRR 2026, CVPR 2026, AAAI 2026) and recent arXiv preprints.

---

## 📑 Paper Collection

### 🏆 VLA Models (Vision-Language-Action)

| # | Paper | Venue | Date | Key Contribution |
|---|-------|-------|------|------------------|
| 1 | **StreamPI: Streaming Multimodal Temporal Modeling for VLA** | arXiv Aug 2026 | 2608.26067 | Instruction-anchored temporal modeling for single-frame VLAs; random-interval streaming training for async deployment |
| 2 | **Qwen-VLA: Unifying VLA Across Tasks, Environments, and Robot Embodiments** | arXiv Jun 2026 | 2605.30280 | Unified embodied foundation model extending Qwen's VL stack to manipulation, navigation, and locomotion |
| 3 | **Dexora: Open-source VLA for High-DoF Bimanual Dexterity** | ICRA 2026 | 2605.18720 | First 36-DoF bimanual dexterous manipulation VLA; **best paper award** |
| 4 | **ProphRL: VLA + RL + World Model** | arXiv 2026 | — | World model as simulator for VLA training; online RL fine-tuning; 24–30% real-robot success lift |
| 5 | **LaST₀: Latent Spatio-Temporal Chain-of-Thought for VLA** | ICLR 2026 | — | Latent chain-of-thought reasoning for spatial-temporal VLA |
| 6 | **VLA-Reasoner: VLA with Online MCTS** | arXiv 2026 | — | Combines VLA with Monte Carlo Tree Search for reasoning during action generation |
| 7 | **MemoryVLA++: Temporal Modeling via Memory and Imagination** | arXiv 2026 | — | Memory-augmented VLA with imagination-based planning |
| 8 | **DynamicVLA: VLA for Dynamic Object Manipulation** | arXiv Jan 2026 | 2601.22153 | Handles dynamic/rearranging objects in VLA |
| 9 | **XR-1: Unified Vision-Motion Codes for VLA** | ICRA 2026 | — | Three-stage training: multimodal pre-train → cross-embodiment → scenario fine-tune |
| 10 | **RynnVLA-001: VLA Foundation Model** | ICRA 2026 | 2602.14979 | Open-source VLA foundation model with strong cross-embodiment generalization |
| 11 | **OTTER: Text-Aware Visual Feature Extraction for VLA** | arXiv 2026 | — | Decoupled text-aware visual features for better language grounding |
| 12 | **MAP-VLA: Memory-Augmented Prompting for VLA** | ICLR 2026 | — | Prompt-based memory retrieval for long-horizon VLA |

### 🎯 Skill-based RL for Robot Learning

| # | Paper | Venue | Date | Key Contribution |
|---|-------|-------|------|------------------|
| 13 | **SkillRL: Recursive Skill Evolution for RL Agents** | arXiv 2026 | — | LLM-based skill distillation + GRPO; 12.3% absolute gain over standard GRPO on ALFWorld; skill library co-evolves with policy |
| 14 | **Master Skill Learning with Policy-Grounded Synergy of LLM-based Reward Shaping** | ICLR 2026 | — | LLM-guided reward shaping + exploration synergy for skill acquisition |
| 15 | **Efficient Language-instructed Skill Acquisition via Reward-Policy Co-Evolution** | AAAI 2025 (Oral) | — | Co-evolution of reward functions and policies for instruction-following skills |
| 16 | **FlowDAgger: Human-in-the-Loop Adaptation of Generative Policies** | arXiv Jul 2026 | — | Latent-space human correction for generative robot policies |
| 17 | **Robot Self-Improvement via Human-Video Dynamics Models** | arXiv Jun 2026 | — | Robots improve their own policies by watching human demonstration videos |
| 18 | **Learning to Act While Waiting: RL Finetuning of Generalist Policies Under Inference Latency** | arXiv Aug 2026 | — | Uses inference idle time for real-time RL fine-tuning |
| 19 | **Accelerating Residual Reinforcement Learning** | arXiv 2026 | — | Residual RL with skill priors for fast policy adaptation |
| 20 | **Master Skill Learning with Policy-Grounded Synergy** | ICLR 2026 | — | Synergistic LLM reward shaping and policy exploration for skill mastery |

### 📚 Surveys & Benchmarks

| # | Paper | Venue | Date | Key Contribution |
|---|-------|-------|------|------------------|
| 21 | **World Model for Robot Learning: A Comprehensive Survey** | IJRR 2026 | 2605.00080 | Comprehensive survey of world models in robot learning |
| 22 | **Large VLM-based VLA Models for Robotic Manipulation: A Survey** | arXiv Aug 2026 | 2508.13073 | Large VLM → VLA survey covering architecture, training, deployment |
| 23 | **Pure VLA Models: A Comprehensive Survey** | arXiv Nov 2025 | 2509.19012 | Pure VLA model taxonomy and analysis |
| 24 | **VLA for Robotics: A Review Towards Real-World Applications** | IEEE Access 2025 | 2510.07077 | Real-world deployment survey of VLA |
| 25 | **From Human Videos to Robot Manipulation: Scalable VLA Learning** | IJCAI 2026 | — | Human-centric data scaling for VLA |
| 26 | **mimic-video: Video-Action Models Beyond VLAs** | RSS 2026 | — | Video-action models as alternative to VLA for robot control |
| 27 | **FluxVLA Engine: One-Stop VLA Engineering Platform** | arXiv 2026 | — | End-to-end VLA engineering platform with simulation, deployment, RTC |

---

## 🧠 Key Insights

### Trend 1: Temporal Reasoning for VLA
**StreamPI** and **MemoryVLA++** address the key weakness of current VLAs (π₀.5, OpenVLA): they operate on single frames. StreamPI introduces instruction-anchored causal attention across frames with zero additional parameters, while MemoryVLA++ uses explicit memory buffers.

### Trend 2: VLA + RL Hybridization
**ProphRL** and **SkillRL** represent a convergence: VLAs provide semantic priors, while RL provides trial-and-error fine-tuning. ProphRL trains a world model as a simulator for the VLA, then fine-tunes with online RL. SkillRL distills successful trajectories into a skill library and uses GRPO to evolve both skills and policy.

### Trend 3: Cross-Embodiment & Unification
**Qwen-VLA** and **RynnVLA-001** demonstrate that a single VLA can handle manipulation, navigation, and locomotion across different robot morphologies, moving toward general-purpose embodied intelligence.

### Trend 4: Skill as Accelerator for RL
The recurring theme across SkillRL, Master Skill Learning, and Residual RL is: **pre-learned skills + online RL** outperform either approach alone. Skills provide structured exploration priors that drastically reduce the sample complexity of RL for long-horizon tasks.

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/vla-rl-papers.git
cd vla-rl-papers

# View the collection
cat papers_summary.md

# Run the paper search script
python scripts/search_recent_papers.py
```

---

## 📄 File Structure

```
vla-rl-papers/
├── README.md                  # This file
├── papers_summary.md          # Detailed paper summaries
├── scripts/
│   └── search_recent_papers.py  # Automated paper search script
└── vla-rl-survey.md           # Extended survey writeup
```

---

## 🔗 Links

- [Awesome-VLA](https://github.com/KwanWaiPang/Awesome-VLA) — Comprehensive VLA paper collection
- [VLA Survey Project](https://vla-survey.github.io) — Interactive VLA survey
- [Pi₀.5: VLA Flow Model](https://arxiv.org/abs/2410.24164) — Physical Intelligence
- [NVIDIA Isaac Lab](https://developer.nvidia.com/isaac/lab) — GPU-accelerated robot RL framework

---

*Maintained by AI Research Assistant — automatically collected and summarized.*