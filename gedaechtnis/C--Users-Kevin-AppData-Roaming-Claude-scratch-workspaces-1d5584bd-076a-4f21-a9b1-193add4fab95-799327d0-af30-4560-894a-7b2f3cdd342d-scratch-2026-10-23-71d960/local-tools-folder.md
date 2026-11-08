---
name: local-tools-folder
description: "C:\\Users\\Kevin\\Tools holds the user's portable, verified tools (JDK 25, Vineflower, luacheck, Lua 5.1, AssetRipper)"
metadata:
  node_type: memory
  type: reference
  originSessionId: 56f6d77e-886c-43cd-be82-e0946090ef56
  modified: 2026-10-23T13:18:52.206Z
---

`C:\Users\Kevin\Tools` contains portable, already verified tools, one subfolder each: `jdk25` (Eclipse Temurin JDK 25, java/javap), `vineflower` (Java decompiler 1.12.0), `luacheck` (1.2.0), `lua51` (Lua 5.1.5), `assetripper`. Use these before downloading duplicates. They fit Java/Lua projects (e.g. Project Zomboid mods), not the Python-based EU5 advisor. New tools follow [[download-confirmation-rules]].

Added 2026-10-23 (user confirmed): `ruff\0.17.2\ruff.exe` — Python linter from the official astral-sh/ruff GitHub release, SHA-256 matched the vendor's .sha256 file. Used to lint the EU5 advisor code (`ruff check`), especially overlay/Win32 code paths that only run with the game live.
