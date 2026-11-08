---
name: download-confirmation-rules
description: "Before downloading any tool, show filename + official source + size and wait for the user's \"bestätigt\"; portable originals only, verify checksums"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 56f6d77e-886c-43cd-be82-e0946090ef56
  modified: 2026-10-23T13:16:37.395Z
---

Before downloading any tool or file: list filename, official source (vendor site or the vendor's official GitHub release only) and size, then wait for the user to reply "bestätigt". Only originals; portable versions preferred (no installer, no PATH/Windows settings/autostart changes). Each tool goes into its own subfolder of `C:\Users\Kevin\Tools` (see [[local-tools-folder]]). After download, verify every file against the vendor-published checksum and report the result (or say that none exists). Then test that it runs and note where it lives and what it is used for.

**Why:** The user wants full control over what lands on their PC and keeps a curated, verified tools folder.

**How to apply:** Applies to all downloads, including pip packages for new projects; ask first, and mention when something was already installed earlier (e.g. the PySide6/numpy/Pillow venv for the EU5 advisor, installed 2026-10-23 before this rule was stated).
