---
name: fortschritt-mod-ort
description: Kevins Fortschrittsbalken-Mod laeuft aus C:\Users\Kevin\Desktop\Claude Mods\fortschritt (CLAUDE_CODE_PLUGIN_DIRS), NICHT aus dev-mods -- dort aendern
metadata:
  type: reference
---

Kevins Claude-App-Mod "fortschritt" (Fortschrittsbalken + Limits ueber dem Eingabefeld) wird ueber `CLAUDE_CODE_PLUGIN_DIRS` in
`~/.claude/settings.json` aus **`C:\Users\Kevin\Desktop\Claude Mods\fortschritt`** geladen, mit `CLAUDE_CODE_PLUGIN_DIR_WATCH=1` (laedt neu bei
Aenderung). Kopien unter `~/.claude/dev-mods/<session>/fortschritt` laufen NICHT -- am 31.10. habe ich die ETA-Reparatur zuerst nur dort gebaut,
und Kevin sah weiter "laeuft seit 139 min" (alter Code). Seit 31.10. ~20:30 liegt die Reparatur (Zeit ab Workflow-Start, Verlauf frueherer Laeufe
aus `<session>/workflows/*.json`, Plattenabgleich `subagents/workflows/<runId>/`) auch im Desktop-Ordner; Sicherung des alten Stands im
Scratchpad `fortschritt_desktop_vorher`. Pruefen: `claude.exe plugin test <ordner>` (Binary unter
`%APPDATA%\Claude\claude-code\<version>\<hash>\claude.exe`), 12 Tests.

**How to apply:** Jede Aenderung an der Mod im Desktop-Ordner machen (und ggf. die dev-mods-Kopien angleichen).
