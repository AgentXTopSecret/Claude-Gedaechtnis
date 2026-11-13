---
name: wo-der-stand-steht
description: "Wo Kevins Projektstaende stehen, wenn er im Benutzerordner fragt \"was steht an\" (NPC Crew + Nebenprojekte) -- Uebergabe-Dateien je Projekt, nichts raten"
metadata:
  node_type: memory
  type: reference
  originSessionId: 07ffa84a-cac3-4eab-97fc-6a0ec3eb3d8f
  modified: 2026-11-13T14:13:21.980Z
---

Kevin fragt in der Sitzung im Benutzerordner (`C:\Users\Kevin`) "weisst du was ansteht?" (13.11.2026). Diese Sitzung hat kein eigenes Projekt; der Stand steht je Projekt auf der Platte, weil Kevin zwischen zwei Claude-Accounts wechselt und jede Projektsitzung eine Uebergabe pflegt:

- **NPC Crew** (Hauptmod, Project Zomboid): Gedaechtnis `C:\Users\Kevin\.claude\projects\C--Users-Kevin-Zomboid-mods-NPCCrew\memory\` -- zuerst `stand-07-11.md` (oberster Block), dann `nach-dem-upload.md` (Reihenfolge der naechsten Auftraege) und `upload-v3-14-*.md` (was oeffentlich ist).
- **Turret**: `C:\Users\Kevin\NPCCrew-Nebenprojekte\turret\STAND.md` (Block "UEBERGABE ... HIER ANFANGEN"), Kevins Tests `turret\TESTLISTE_fuer_kevin.md`.
- **Baer**: `...\baer\STAND.md` (oberster Block), `baer\UEBERGABE_ACCOUNT2.md`.
- **Modelle** (Zweihaender, Crew Backpack, Ruestung/Schwertkampf): `...\zweihaender\STAND.md`.
- **Blueprint**: `...\blueprint\UEBERGABE.md` Abschnitt 0.

Laufende Sitzungen zeigt `mcp__ccd_session_mgmt__list_sessions`. Nie rekursiv ueber `C:\Users\Kevin` suchen (Glob dort laeuft in den Timeout, und Kevins Regel in den Projekten verbietet es) -- gezielt diese Pfade lesen. Antwort an Kevin: Deutsch, kurz, Ergebnis zuerst.
