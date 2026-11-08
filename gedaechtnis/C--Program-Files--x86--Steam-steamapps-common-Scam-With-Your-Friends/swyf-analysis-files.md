---
name: swyf-analysis-files
description: "Wo alle Arbeitsdateien der Scam-With-Your-Friends-Mod liegen (Arbeitsordner mit CLAUDE.md, Berichte, decompilierter Code, ilspycmd)"
metadata:
  node_type: memory
  type: reference
  originSessionId: aab284ab-c9db-4bc4-bdf3-26f404963264
  modified: 2026-10-23T13:11:47.042Z
---

Seit 2026-10-18 liegt alles dauerhaft in **`C:\Users\Kevin\Documents\SWYF-ClaudeMod\`** (gehört zu [[swyf-claude-mod-status]]):
- `CLAUDE.md`: vollständige Übergabe (Ziel, Regeln, Befunde, nächste Schritte)
- `analyse/1-spracheingabe.md` … `5-infrastruktur.md` + `analyst-reports.raw.json` + `workflow-journal.jsonl`
- `decompiled/<Assembly>/`: ILSpy-Ausgabe; die Belege in den Berichten sind relativ dazu. **Stand 19.10.** – das Spiel-Update vom 21.10. hat Teile geändert (z. B. Profilwerte wie Namensschild/Prestige liegen jetzt in `MetaSave.File` + Steam Cloud `metasave-1.json`, nicht mehr in der Registry). Vor Aussagen über Spiel-Verhalten die betroffene Klasse frisch decompilieren: `dotnet tools/ilspycmd/ilspycmd.dll -t <Typ> "<Spiel>\Scam With Your Friends_Data\Managed\ScriptsAssDef.dll"`
- `tools/ilspycmd/ilspycmd.dll`: ILSpy-CLI 9.1, Aufruf per `dotnet …/ilspycmd.dll` (kein `ilspycmd` im PATH)
- **AssetRipper 2.0.0** (seit 23.10., SHA256 geprüft): `C:\Users\Kevin\Tools\assetripper\app\AssetRipper.GUI.Free.exe --headless --port 51888` → http://127.0.0.1:51888. Für Unity-Assets (Szenen, Möbel-Anzahl, Schriften/Glyphen, UI). Nur lesen, Export außerhalb des Spielordners. Details `mod/notes/16-werkzeuge.md`. JDK/Vineflower/Lua in `C:\Users\Kevin\Tools` passen nicht zu diesem C#-Projekt.

Die alten Kopien im Temp-Scratchpad der ersten Session können gelöscht sein und werden nicht mehr gebraucht.
