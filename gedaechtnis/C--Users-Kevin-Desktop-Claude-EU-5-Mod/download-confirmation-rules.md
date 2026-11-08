---
name: download-confirmation-rules
description: Before downloading any tool, show filename + official source + size and wait for the user's "bestätigt"; portable originals only, verify checksums
metadata:
  type: feedback
---

Before downloading any tool or file: list filename, official source (vendor site or the vendor's official GitHub release only) and size, then wait for the user to reply "bestätigt". Only originals; portable versions preferred (no installer, no PATH/Windows settings/autostart changes). Each tool goes into its own subfolder of `C:\Users\Kevin\Tools` (see [[local-tools-folder]]). After download, verify every file against the vendor-published checksum and report the result (or say that none exists). Then test that it runs and note where it lives and what it is used for.

**Why:** The user wants full control over what lands on their PC and keeps a curated, verified tools folder.

**How to apply:** Applies to all downloads, including pip packages; ask first. The EU5 advisor's `.venv` (PySide6, numpy, Pillow from PyPI) was installed 2026-10-23 before this rule was stated and was later copied, not re-downloaded, into the project folder.
