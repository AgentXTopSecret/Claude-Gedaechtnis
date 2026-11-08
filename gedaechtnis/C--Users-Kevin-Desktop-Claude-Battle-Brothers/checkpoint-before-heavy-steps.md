---
name: checkpoint-before-heavy-steps
description: Save STAND.md + stand/ after every workflow; since 2026-10-26 no pause needed for the 5-hour window
metadata:
  node_type: memory
  type: feedback
  originSessionId: 603c0cc3-65f8-4fca-8839-a46598c470ec
  modified: 2026-10-26T13:38:09.803Z
---

Save the current state to a checkpoint file (STAND.md in the project folder, plus results under `stand/`) as soon as a workflow finishes and before starting the next heavy step, so a new session (or a crash — Kevin's PC went off once on 2026-10-26) can resume without redoing work.

Update 2026-10-26: Kevin said "das 5std fenster ist kein problem mehr" — do NOT pause after workflows to wait for his decision anymore; just save state and continue. The weekly limit was not mentioned; if Kevin says a limit is tight again, go back to pausing.

**Why:** originally the workflows blew his 5-hour usage window; the checkpoint habit still protects against crashes and session restarts.
**How to apply:** after each workflow, write results to `C:\Users\Kevin\Desktop\Claude Battle Brothers\stand\` and update STAND.md (done / where / next), then carry on. Related: [[bb-legends-custom-mod-goals]].
