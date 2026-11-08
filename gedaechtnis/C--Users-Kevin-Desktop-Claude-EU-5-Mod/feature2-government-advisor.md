---
name: feature2-government-advisor
description: "Feature 2 (estate privileges, laws, government advisor) started 2026-10-23; findings on rule files, save format and OCR"
metadata:
  node_type: memory
  type: project
  originSessionId: 56f6d77e-886c-43cd-be82-e0946090ef56
  modified: 2026-10-30T20:55:55.832Z
---

The user wants an advisor shown on the left, next to the in-game government panel.

What it should suggest, all "really smart":
- which estate privileges to revoke and which to grant
- the best government form and reforms
- the best law policies

**The advisor must work for every country the user plays.** Böhmen (BOH) was only a test country (user, 2026-10-30: "der berater soll für jede fraktion laufen böhmen war nur eine teste fraktion"). Never hardcode a tag; detect the player's country from the save. The test save is `SP_BOH_1337_04_01_*.eu5`.

**Status 2026-10-30:** The generic rule overview is merged into main as `eu5advisor/government/`. It covers all governments, reforms, laws and privileges, base game plus DLCs, scored by goal. You open it with `Regierungs-Ratgeber.bat`, `run.py --ratgeber`, or the tray menu. Next step: read the player's own country state from the save and tailor the advice to it.

**Status 2026-10-30 (later):** Save reading (`eu5advisor/savegame/`) is merged into main (merge d2b48f7) and pushed.
- **Value tokens:**
  - 0x0d40 and 0x0d43 are 1-byte lookups; 0x0d3e is a 2-byte lookup.
  - Fixed-point numbers: 0x0d47 is zero, 0x0d48..0x0d4e are positive with 1..7 bytes, 0x0d4f..0x0d55 are negative. The value is divided by 100000.
- **Player country:** taken from the metadata coat-of-arms string `TAG={`.
- **Lookup strategy:** most fields are found by vocabulary. Only these are found by token: satisfaction 0x2ea5, gold 0x2875, religion 0x35c5, culture 0x35c4. Each is validated.
- **Estate power is not stored in the save.**
- **Verification:** only the 1.3.11 test save has been checked so far. After the big D009 update (build "ud009/release/next"), it still needs checking against a new save.

**Findings (2026-10-23, game 1.3.11):**
- **Privileges:** 261 in `in_game/common/estate_privileges/*_estate.txt`.
  - Attributes: estate, potential, allow, can_revoke, country_modifier, location_modifier, on_activate, on_deactivate.
  - Most common modifiers: `global_<estate>_power`, `<estate>_target_satisfaction`, `monthly_towards_<societal value>`, `<estate>_max_tax`.
- **Value tiers:** named values such as `medium_privilege_target_satisfaction = 0.05` live in `main_menu/common/script_values/default_values.txt`.
  - That file also holds the default satisfaction per estate: nobles 0.4, clergy 0.3, burghers 0.5, peasants 0.6.
- **Other rule folders:** `laws/` (30 files), `government_reforms/`, `government_types/`, `estates/00_default.txt`, `parliament_*`, `societal_values/`.
- **Save format:**
  - Header `SAV0203…`, then binary metadata, then a ZIP container holding `gamestate` (binary, about 174 MB) and `string_lookup`.
  - `string_lookup` contains identifier strings, including privilege keys, so the active privileges and laws are probably findable as lookup references.
  - Field names are binary tokens with no names. Do not read the game exe to get them.
- **Windows OCR:** the built-in engine (`Windows.Media.Ocr`, reachable from PowerShell 5.1) is available with de-DE and en-US. No download is needed. This is the fallback for reading the government panel.

**How to apply:** Start Feature 2 from these facts. Respect the fairness rule: read only the player's own country from the save.

Related: [[eu5-advisor-repo]], [[no-workflows-usage-limit]]
