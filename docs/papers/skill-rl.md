# Skill-based Reinforcement Learning

> 7 recent papers on skill-based RL for accelerated robot learning. Last updated: September 2026.

## 🤖 Methods

| Paper | Venue | Skill Source | RL Algorithm |
|:---|---:|:---|:---|
| [SkillRL](../papers/2026-skillrl.md) | arXiv | LLM distillation (o3) | GRPO |
| [Master Skill Learning](../papers/2026-master-skill.md) | **ICLR 2026** | LLM reward shaping | PPO |
| [FlowDAgger](../papers/2026-flowdagger.md) | arXiv | Human correction (latent) | DAgger |
| [Act While Waiting](../papers/2026-act-while-waiting.md) | arXiv | None (online) | Value-based |
| [Residual RL](../papers/2026-residual-rl.md) | arXiv | Pre-trained skill prior | SAC |
| [Robot Self-Improve](../papers/2026-robot-self-improve.md) | arXiv | Human video dynamics | Model-based |
| [Efficient Skill Acq.](../papers/2025-efficient-skill.md) | **AAAI 2025 🎙** | LLM reward shaping | PPO |

## 🏆 Top Performers

| Method | Benchmark | Score | vs Baseline |
|:---|---:|---:|---:|
| **SkillRL** | ALFWorld | 89.9% | +12.3% over GRPO |
| **SkillRL** | WebShop | 72.7% | +10.5% |
| **Residual RL** | Manipulation Suite | 3× faster | vs from-scratch RL |

## 💡 Key Insights

1. **Skills accelerate RL 2–5×** — SkillRL, Residual RL
2. **LLM can replace human reward design** — Master Skill, Efficient Skill Acq.
3. **Co-evolution beats static libraries** — SkillRL, Master Skill
4. **Inference latency can be repurposed for learning** — Act While Waiting

## Comparison Table

See [Skill-RL Comparison](../tables/skill-rl-comparison.md) for method × performance × design matrix.