# VLA Model Comparison Table

> **Legend**: ✅ = supported/publicly available | ❌ = not supported | — = not reported

## Architecture & Action

| Model | Year | Venue | Backbone | Action Repr. | Temporal | Param | Open-Source |
|:---|---:|:---|:---|:---|---:|---:|:---:|
| StreamPI | 2026 | arXiv | π₀.5 | Continuous (flow) | ✅ Instruction-anchored | — | ✅ |
| Qwen-VLA | 2026 | arXiv | Qwen VL | Token + Continuous | ❌ Single-frame | — | ✅ |
| Dexora | 2026 | ICRA🏅 | Custom | Continuous (MPC) | ✅ Interaction graph | — | ✅ |
| ProphRL | 2026 | arXiv | Varies (model-agnostic) | Continuous | ✅ World model rollout | 0.5B–7B | ❌ |
| LaST₀ | 2026 | ICLR | Custom | Latent CoT | ✅ Spatio-temporal CoT | — | ❌ |
| VLA-Reasoner | 2026 | arXiv | Custom | Token (MCTS) | ✅ MCTS search | — | ❌ |
| MemoryVLA++ | 2026 | arXiv | Custom | Continuous | ✅ Memory + imagination | — | ❌ |
| DynamicVLA | 2026 | arXiv | Custom | Continuous | ✅ Temporal dynamics | — | ❌ |
| XR-1 | 2026 | ICRA | PaliGemma+Gemma | UVMC token | ❌ Single-frame | — | ❌ |
| RynnVLA-001 | 2026 | ICRA | Custom | Continuous | ❌ Single-frame | — | ✅ |
| OTTER | 2026 | arXiv | Custom | Continuous | ❌ Single-frame | — | ❌ |
| MAP-VLA | 2026 | ICLR | Custom | Continuous | ✅ Memory prompting | — | ❌ |
| π₀.5 | 2025 | CoRL | Custom | Continuous (flow) | ❌ Single-frame | 3B | ✅ |
| OpenVLA | 2024 | CoRL | Prismatic-7B | Token | ❌ Single-frame | 7B | ✅ |
| RT-2 | 2023 | arXiv | PaLI-X | Token | ❌ Single-frame | 55B | ❌ |

## Benchmark Performance

| Model | LIBERO | CALVIN | ALFWorld | Real-Robot | Cross-Embodiment |
|:---|---:|---:|---:|---:|:---:|
| StreamPI | **92.1%** | — | — | **82.0%** | ❌ |
| ProphRL | 90.5% | **89.2%** | — | **88.0%** | ✅ (3 models) |
| Dexora | — | — | — | Dexterous 36-DoF | ❌ |
| Qwen-VLA | — | — | — | 78.5% | ✅ (multi) |
| π₀.5 | 87.3% | 82.1% | — | 76.0% | ✅ |
| OpenVLA | 72.0% | 65.0% | — | 58.0% | ✅ |
| RT-2 | — | — | — | 62.0% | ❌ (single) |

## Key Dimensions Score (1–5 ★)

| Model | Temporal | Generalization | Sample Eff. | Deployability | Novelty |
|:---|---:|---:|---:|---:|---:|
| StreamPI | ★★★★★ | ★★★★ | ★★★★ | ★★★★★ | ★★★★★ |
| Qwen-VLA | ★★ | ★★★★★ | ★★★ | ★★★★ | ★★★★ |
| Dexora | ★★★★ | ★★★ | ★★ | ★★ | ★★★★★ |
| ProphRL | ★★★★★ | ★★★★ | ★★★★★ | ★★★ | ★★★★★ |
| LaST₀ | ★★★★★ | ★★★ | ★★★ | ★★★ | ★★★★ |
| VLA-Reasoner | ★★★★ | ★★★★ | ★★★ | ★★ | ★★★★ |
| MemoryVLA++ | ★★★★★ | ★★★ | ★★★ | ★★★ | ★★★★ |
| DynamicVLA | ★★★★ | ★★★ | ★★★ | ★★★ | ★★★★ |
| XR-1 | ★★ | ★★★★★ | ★★★ | ★★★★ | ★★★★ |
| RynnVLA-001 | ★★ | ★★★★★ | ★★★ | ★★★★★ | ★★★ |
| OTTER | ★★ | ★★★★ | ★★★ | ★★★ | ★★★ |
| MAP-VLA | ★★★★ | ★★★ | ★★★ | ★★★★ | ★★★ |
| SkillRL | ★★★★★ | ★★★★★ | ★★★★★ | ★★★ | ★★★★★ |
| Master Skill | ★★★ | ★★★★ | ★★★★★ | ★★★ | ★★★★ |
| Act-While-Wait | ★★★ | ★★★ | ★★★★★ | ★★★★★ | ★★★★★ |