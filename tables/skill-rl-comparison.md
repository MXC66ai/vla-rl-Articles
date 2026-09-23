# Skill-based Reinforcement Learning Comparison Table

## Method Taxonomy

| Method | Year | Venue | Skill Source | RL Algorithm | Skill Reuse | Co-Evolution |
|:---|---:|:---|:---|:---|---:|:---:|
| **SkillRL** | 2026 | arXiv | LLM distillation (o3) | GRPO | ✅ Retrieval (K=6) | ✅ Recursive |
| **Master Skill Learning** | 2026 | ICLR | LLM reward shaping | PPO | ✅ Policy-grounded | ✅ Reward-policy |
| **FlowDAgger** | 2026 | arXiv | Human correction (latent) | DAgger | ❌ | ❌ |
| **Act While Waiting** | 2026 | arXiv | None (online) | Value-based | ❌ | ❌ |
| **Residual RL** | 2026 | arXiv | Pre-trained skill prior | SAC | ✅ Residual | ❌ |
| **Robot Self-Improve** | 2026 | arXiv | Human video dynamics | Model-based | ❌ | ❌ |
| **Efficient Skill Acq.** | 2025 | AAAI🎙 | LLM reward shaping | PPO | ✅ Co-evolution | ✅ |

## Performance

| Method | Benchmark | Metric | Score | vs Baseline |
|:---|---|:---|---:|---:|
| **SkillRL** | ALFWorld | Success Rate | **89.9%** | +12.3% over GRPO |
| | WebShop | Success Rate | **72.7%** | +10.5% |
| **Act While Waiting** | Simulated Robot | Task Completion | Comparable | Zero extra time |
| **Residual RL** | Manipulation Suite | Sample Efficiency | **3× faster** | vs from-scratch RL |
| **FlowDAgger** | Real Robot | Correction Efficiency | **2×** | vs full retraining |

## Key Design Decisions

| Decision | SkillRL | Master Skill | Residual RL | FlowDAgger |
|:---|:---|:---|:---|:---|
| Skill representation | Natural language + trajectory | Reward function parameters | Policy parameters | Latent codes |
| Skill library growth | Continuous evolution | Co-evolution | Static prior | N/A |
| Human involvement | None (LLM teacher) | None (LLM teacher) | None | ✅ Active |
| Base model | Qwen2.5-7B | — | — | Diffusion policy |
| Open-source | ❌ | ❌ | ❌ | ❌ |

## Insights Summary

| Insight | Supporting Methods |
|:---|---:|
| Skills accelerate RL convergence 2–5× | SkillRL, Residual RL |
| LLM can replace human reward design | Master Skill, Efficient Skill Acq. |
| Co-evolution beats static libraries | SkillRL, Master Skill |
| Inference latency can be repurposed for learning | Act While Waiting |
| Human correction in latent space is efficient | FlowDAgger |
| Video-only (no language) skill learning works | Robot Self-Improve |