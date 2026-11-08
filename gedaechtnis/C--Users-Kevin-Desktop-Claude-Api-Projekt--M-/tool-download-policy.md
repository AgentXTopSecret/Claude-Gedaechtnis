---
name: tool-download-policy
description: "How the user wants extra tools downloaded – list first and wait for \"bestätigt\", official sources only, portable, checksum-verified"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 90bc59e6-c074-48ba-a483-209e9a8f239b
  modified: 2026-10-23T13:13:43.638Z
---

Before downloading any tool: show a list (file name, official source = vendor site or vendor's official GitHub release, size) and wait for the user's "bestätigt".
Only originals; prefer portable builds – no installer, no PATH / Windows settings / autostart changes. Each tool in its own subfolder of C:\Users\Kevin\Tools (see [[user-tools-folder]]).
After download: verify against the vendor's published checksum and report the result (say so if none is published), test that the tool runs, then record location and purpose in memory.
Only suggest tools that make a real difference for the project at hand – no wish lists. Reuse what is already in C:\Users\Kevin\Tools.

**Why:** The user wants control over what lands on their PC and only trusted, verifiable software.
**How to apply:** Any time a tool, SDK or binary would need to be fetched – including when a tool only exists as an installer, say that instead of quietly installing it.
