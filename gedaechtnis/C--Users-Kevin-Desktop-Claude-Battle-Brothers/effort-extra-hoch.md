---
name: effort-extra-hoch
description: "Kevin's effort choice for building here — session at \"extra hoch\" (xhigh); in workflows max only for spec/reviewers, high for simple steps"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 603c0cc3-65f8-4fca-8839-a46598c470ec
  modified: 2026-10-28T03:43:55.773Z
---

On 28.10.2026 Kevin chose "extra hoch" (xhigh) as the effort level for coding and building in this project, after I recommended it over "maximal" for everything.

In workflow scripts, set `effort` per agent:
- `max` for the spec author and the adversarial reviewers
- `xhigh` for builders and the correction step
- `high` for simple work: small features like the lab switch LS, and the docs

**Why:** With max inherited by every agent, TL cost about 23 % and GS about 10 % of the weekly quota. The multi-layer pipeline (spec → build → reviewers → correction → my own checks) catches the errors that extra thinking would avoid.

**How to apply:**
- Put explicit `effort` in new workflow scripts. The VA and LS scripts in `stand/workflow-scripts/` already have it.
- A session cannot change its own effort (the app refuses it), so Kevin sets the session level himself in the app's model/effort picker.

Related: [[max-10-agents]], [[waechter-aufgabenliste]].
