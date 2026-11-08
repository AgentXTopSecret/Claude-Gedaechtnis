---
name: always-german
description: "The user wants every reply in German – including short status lines between tool calls, summaries and wrap-up texts"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 56f6d77e-886c-43cd-be82-e0946090ef56
  modified: 2026-10-23T19:14:38.596Z
---

Write everything the user reads in German: answers, short progress notes between tool calls, recaps, questions and button labels. Code comments, commit messages and README stay German as before.

**Why:** On 2026-10-23 several mid-turn status lines came out in English (e.g. during the review evaluation); the user asked explicitly: "merk dir mal das du deutsch schreiben sollst".

**How to apply:** Default to German from the first message of every session in this project, even when tool output or internal reasoning is English. Only switch if the user writes in another language.
