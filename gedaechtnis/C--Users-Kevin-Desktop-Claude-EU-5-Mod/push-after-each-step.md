---
name: push-after-each-step
description: Standing permission: commit and push to the private GitHub repo after every finished and tested work step, then tell the user briefly what is in it
metadata:
  type: feedback
---

For the EU5 advisor repo ([[eu5-advisor-repo]]): after every finished AND tested work step, commit and `git push` without asking again, then tell the user in a few lines what the new version contains. Never push half-finished or untested states. Larger milestones may get a version tag like `v0.1.0`.

**Why:** The user explicitly asked for this on 2026-10-23 ("lade nach jedem fertigen und getesteten Schritt selbst hoch und sag mir kurz, was drin ist"), so they can follow each version in GitHub Desktop.

**How to apply:** Run tests and ruff before each commit; one commit per logical step; keep the repo private and free of personal names.
