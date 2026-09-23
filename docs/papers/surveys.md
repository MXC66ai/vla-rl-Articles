# Surveys & Benchmarks

> 7 survey papers providing comprehensive coverage of the field. Last updated: September 2026.

| Survey | Venue | Focus |
|:---|---:|:---|
| [World Model for Robot Learning](https://arxiv.org/abs/2605.00080) | **IJRR 2026** | World models in robot learning |
| [Large VLM-based VLA Models](https://arxiv.org/abs/2508.13073) | arXiv Aug 2026 | VLM → VLA pathway |
| [Pure VLA Models](https://arxiv.org/abs/2509.19012) | arXiv Nov 2025 | VLA taxonomy and analysis |
| [VLA for Real-World Applications](https://arxiv.org/abs/2510.07077) | **IEEE Access 2025** | Real-world deployment |
| [From Human Videos to Robot Manipulation](https://arxiv.org/abs/) | **IJCAI 2026** | Human-centric data scaling |
| [mimic-video: Beyond VLAs](https://arxiv.org/abs/) | **RSS 2026** | Video-action models |
| [FluxVLA Engine](https://arxiv.org/abs/) | arXiv 2026 | VLA engineering platform |

## What the Surveys Tell Us

> 📌 **Consensus #1**: VLA is the dominant paradigm for generalist robot control
> 📌 **Consensus #2**: Temporal reasoning is the #1 unsolved challenge
> 📌 **Consensus #3**: Data scarcity remains the bottleneck — human videos are the key
> 📌 **Consensus #4**: Cross-embodiment transfer is feasible but not yet reliable

## Key Recommendations from Surveys

| Theme | Recommendation |
|:---|---:|
| Architecture | Start with flow-matching or diffusion for action representation |
| Data | Prioritize human video data over robot data for scaling |
| Training | Pre-train on diverse embodiments, fine-tune on target |
| Deployment | Use Real-Time Chunking + async inference |
| Evaluation | Report on at least 2 benchmarks + real-robot