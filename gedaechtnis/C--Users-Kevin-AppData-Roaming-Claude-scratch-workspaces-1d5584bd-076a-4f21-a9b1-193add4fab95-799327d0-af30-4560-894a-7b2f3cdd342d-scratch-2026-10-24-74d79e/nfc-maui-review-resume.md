---
name: nfc-maui-review-resume
description: "How to resume the NFC MAUI app review/fix workflow if it was cut off (usage limit) — runId, script path, git baseline"
metadata:
  node_type: memory
  type: project
  originSessionId: a104f454-ab6e-49be-b91d-1f8640487b46
  modified: 2026-10-24T17:06:09.312Z
---

NFC Tool (.NET 10 MAUI, Android/iOS/Windows-PC/SC) lives in this session's scratch folder (git repo, `NfcTool/`, `NfcTool.Tests/`, `NfcTool.slnx`). Baseline before review: commit 6205172 (all 4 TFMs build, 444 tests green).

Review/fix workflow started 2026-10-24 ~19:00: runId `wf_48c6605c-b4d`, script `C:\Users\Kevin\.claude\projects\C--Users-Kevin-AppData-Roaming-Claude-scratch-workspaces-1d5584bd-076a-4f21-a9b1-193add4fab95-799327d0-af30-4560-894a-7b2f3cdd342d-scratch-2026-10-24-74d79e\a104f454-ab6e-49be-b91d-1f8640487b46\workflows\scripts\nfc-maui-review-fix-wf_48c6605c-b4d.js`.

**Why:** the user (Kevin) expected their 5-hour usage window to run out mid-workflow and asked to be able to continue later.

**How to apply:** when the user says "weiter": read the journal `...\subagents\workflows\wf_48c6605c-b4d\journal.jsonl`, then `Workflow({scriptPath, resumeFromRunId: "wf_48c6605c-b4d"})` (same session only; finished agents replay from cache). If fixers were interrupted mid-edit, check `git diff 6205172` before resuming. Builds must use short output dirs (`-p:BaseIntermediateOutputPath=C:\Users\Kevin\AppData\Local\Temp\nfcb\<x>\obj\`), since the scratch path is too long for aapt2/MakePri. After it finishes: verify builds+tests, commit, offer to move the project to a short folder such as Desktop\NfcTool.
