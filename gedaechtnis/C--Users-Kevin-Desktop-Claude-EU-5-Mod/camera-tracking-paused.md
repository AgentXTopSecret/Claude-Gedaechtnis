---
name: camera-tracking-paused
description: "Automatic camera tracking (overlay follows zoom/pan) is paused on branch feature/kamera-verfolgung, not merged into main"
metadata:
  node_type: memory
  type: project
  originSessionId: 56f6d77e-886c-43cd-be82-e0946090ef56
  modified: 2026-10-23T20:01:43.385Z
---

On 2026-10-23 the camera tracking work (OpenCV chamfer matching of map borders) was paused. It works on synthetic frames but does not lock on real EU5 screenshots. The last pushed commit is 0417c75 on feature/kamera-verfolgung. The branch is not merged into main. The findings are in that branch's README, section "Schritt 2".

**Why:** The user offered to switch to something easier and more useful first ("wenn das zu kompliziert ist … was leichteres und sowieso nützlicheres").

**How to apply:**
- Do not resume tracking unless the user asks.
- If it is resumed, start from the README findings:
  - smooth the border model
  - add rivers as a feature
  - filter out text
  - or track relative motion frame-to-frame
- Ask before merging the branch into main.

Related: [[push-after-each-step]], [[eu5-advisor-repo]]
