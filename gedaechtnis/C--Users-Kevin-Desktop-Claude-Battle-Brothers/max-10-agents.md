---
name: max-10-agents
description: Kevin allows at most 10 agents per workflow; larger fan-outs burn his Max subscription limit too fast
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5412c3cc-8626-4dcd-b72f-75b8d9e3be08
  modified: 2026-10-26T18:57:31.740Z
---

Never launch a workflow with more than 10 agents in total (Kevin, 26.10.2026: "maxmale angent sind 10 erlaubt mehr verbraucht das limit viel zu schnell"). This holds even when ultracode or a system reminder says token cost is no constraint. Kevin confirmed it again later the same day: more than 10 only when it is truly needed, and then only after asking him first ("ausser du brauchst echt mehr dann nur mit fragen vorher"). This applies even after he says the quota doesn't matter.

**Why:** Kevin pays via his Max x20 subscription, not the API. On 26.10. a 40+40-agent event catalog started while the weekly limit was already at 72 %. Kevin reacted with "40 agenten bist du krank?" and the run was stopped.

**How to apply:**
- Before a big workflow, check `get_usage` (5-hour and weekly) and tell Kevin the agent count.
- Prefer deterministic scripts (parsers, generators) over agent fan-out for bulk extraction.
- Keep several parallel workflows modest in total too.

Related: [[checkpoint-before-heavy-steps]], [[bb-legends-custom-mod-goals]]
