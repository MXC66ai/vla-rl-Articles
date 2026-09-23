# VLA/VLM & Skill-based RL Papers — Detailed Summaries

> Collected: September 2026 | Time window: ~1 month

---

## 1. StreamPI: Streaming Multimodal Temporal Modeling for VLA

**Link**: [arXiv 2608.26067](https://arxiv.org/abs/2608.26067)  
**Venue**: arXiv, Aug 2026

**Problem**: State-of-the-art VLA models (e.g., π₀.5) operate on single frames, limiting temporal reasoning and spatial perception.

**Solution**: StreamPI introduces **instruction-anchored temporal modeling** — each (visual observation, language instruction) pair is an atomic temporal unit. Bidirectional attention within each pair enables cross-modal fusion; causal attention across pairs preserves autoregressive streaming. A **random-interval streaming training** strategy bridges the gap between synchronous training and asynchronous real-robot deployment.

**Key Result**: Outperforms π₀.5 on memory-dependent and precise-perception tasks, as well as LIBERO simulation benchmark.

---

## 2. Qwen-VLA: Unifying VLA Across Tasks, Environments, and Robot Embodiments

**Link**: [arXiv 2605.30280](https://arxiv.org/abs/2605.30280)  
**Venue**: arXiv, Jun 2026 (Qwen Team, Alibaba)

**Problem**: Embodied intelligence models are fragmented across manipulation, navigation, and locomotion.

**Solution**: Extends Qwen's vision-language stack into a unified VLA model supporting heterogeneous embodied decision-making tasks.

**Key Result**: A single model works across diverse robot embodiments and tasks, demonstrating that VLA unification is feasible at scale.

---

## 3. Dexora: Open-source VLA for High-DoF Bimanual Dexterity

**Link**: [arXiv 2605.18720](https://arxiv.org/abs/2605.18720)  
**Venue**: **ICRA 2026 Best Conference Paper + Best Paper on Robot Manipulation and Locomotion**

**Problem**: No open-source VLA handles high-DoF bimanual dexterous manipulation (36 DoF).

**Solution**: First 36-DoF bimanual dexterous VLA model with interaction-graph-based contact reasoning and implicit MPC.

**Key Result**: Open-source; demonstrates dual-arm coordinated dexterous manipulation.

---

## 4. ProphRL: VLA + RL + World Model

**Link**: Fudan University  
**Venue**: arXiv 2026

**Problem**: VLA models lack trial-and-error improvement; RL requires prohibitive sample counts.

**Solution**: Train a **Prophet world model** as a differentiable simulator for online VLA fine-tuning via RL. The world model predicts action outcomes, allowing the VLA to practice virtually.

**Key Result**: 5–17% success rate improvement across VLA-adapter-0.5B, π₀.5-3B, and OpenVLA-OFT-7B on AgiBot, DROID, LIBERO, BRIDGE; 24–30% lift on real robots.

---

## 5. LaST₀: Latent Spatio-Temporal Chain-of-Thought for VLA

**Venue**: **ICLR 2026**

**Problem**: VLAs lack explicit spatial-temporal reasoning before acting.

**Solution**: Introduces latent chain-of-thought representations that encode future state evolution before predicting actions.

**Key Result**: Improved long-horizon manipulation performance through structured latent reasoning.

---

## 6. VLA-Reasoner: Empowering VLA with Online MCTS

**Link**: Tsinghua / Shanghai AI Lab  
**Venue**: arXiv 2026

**Problem**: VLAs produce actions autoregressively without explicit planning or search.

**Solution**: Monte Carlo Tree Search (MCTS) in action token space to explore multiple action trajectories before committing.

**Key Result**: VLA + search outperforms naive VLA rollout on complex manipulation.

---

## 7. SkillRL: Recursive Skill Evolution for RL Agents

**Link**: [Blog post](https://www.cnblogs.com/emergence/p/19740072)  
**Venue**: arXiv 2026

**Problem**: Standard RL (PPO, GRPO) treats all tasks from scratch; lacks structured skill reuse.

**Solution**: Three-stage pipeline: (1) **Skill distillation** from successful trajectories (teacher = o3), (2) **Skill retrieval** for task-specific K=6 skills, (3) **Recursive skill evolution** where the skill library and policy co-evolve via GRPO.

**Key Result**: 89.9% on ALFWorld (+12.3% over GRPO); 72.7% on WebShop; faster convergence (60 vs 90 steps).

---

## 8. Master Skill Learning with Policy-Grounded Synergy

**Venue**: **ICLR 2026**

**Problem**: Reward shaping + exploration for skill learning are typically decoupled.

**Solution**: Synergistic framework where LLM-based reward shaping and exploration policy co-evolve through grounded interaction.

**Key Result**: Effective language-instructed skill acquisition with better sample efficiency.

---

## 9. FlowDAgger: Human-in-the-Loop Adaptation of Generative Policies

**Link**: arXiv, Jul 2026  
**Venue**: arXiv

**Problem**: Generative robot policies (diffusion, flow matching) are hard to correct post-deployment.

**Solution**: Human corrections injected in latent space; DAgger-style iterative improvement without full retraining.

**Key Result**: Efficient online policy adaptation from human feedback.

---

## 10. Learning to Act While Waiting: RL Finetuning Under Inference Latency

**Link**: arXiv, Aug 2026  
**Venue**: arXiv

**Problem**: VLA models have high inference latency; robot idle time is wasted.

**Solution**: Use inference waiting periods for online RL fine-tuning via lightweight value updates.

**Key Result**: Simultaneous acting + learning with zero extra wall-clock time.

---

## 11. World Model for Robot Learning: A Comprehensive Survey

**Link**: [arXiv 2605.00080](https://arxiv.org/abs/2605.00080)  
**Venue**: IJRR 2026

**Content**: Comprehensive survey of world models for robot learning covering model-based RL, latent-space planning, video prediction, and sim-to-real transfer.

---

## 12. mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs

**Venue**: **RSS 2026**

**Problem**: VLAs rely on language conditioning; video demonstrations provide richer supervision.

**Solution**: Video-action models that directly map demonstration videos to robot actions without explicit language parsing.

**Key Result**: Better generalization than VLA on tasks where language instructions are ambiguous.

---

## 13. DynamicVLA: VLA for Dynamic Object Manipulation

**Link**: [arXiv 2601.22153](https://arxiv.org/abs/2601.22153)  
**Venue**: arXiv, Jan 2026

**Problem**: Standard VLAs assume static scenes.

**Solution**: VLA architecture with temporal dynamics modeling for moving/rearranging objects.

**Key Result**: Handles dynamic manipulation where object positions change during execution.

---

## Common Themes Across Papers

1. **Temporal is the next frontier**: Single-frame VLAs are hitting a wall; ~40% of recent papers focus on multi-frame temporal reasoning
2. **VLA + RL convergence**: The hybrid approach (VLA for priors + RL for fine-tuning) is emerging as the dominant paradigm
3. **Skill-based acceleration**: Skill libraries reduce RL sample complexity by 2–5×
4. **Cross-embodiment**: Foundation models are increasingly embodiment-agnostic
5. **Open-source momentum**: Dexora, RynnVLA-001, FluxVLA Engine are all open-source