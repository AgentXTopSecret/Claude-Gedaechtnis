---
name: kevin-abo-statt-api
description: Kevin hat kein API-Guthaben; Claude-Anbindungen in seinen Tools laufen über claude -p mit dem Abo
metadata:
  node_type: memory
  type: user
  originSessionId: 63b062b8-75eb-4652-93cf-7fd3746d2234
  modified: 2026-10-26T21:54:33.783Z
---

Kevin nutzt nur sein Claude-Max-Abo und kein bezahltes API-Guthaben. Programme, die Claude aufrufen sollen (Oaken-Tower-Berater, SWYF-Mod, Battle-Brothers-Begleiter), rufen `claude.exe -p` mit Abo-Login auf (`C:\Users\Kevin\.local\bin\claude.exe`), nicht die API per Key.

**Why:** Kevins eigene Aussage vom 26.10.2026 („nur abo kein api guthaben“). Ein API-Key rechnet immer über Guthaben ab, nie übers Abo.

**How to apply:** Neue Claude-Anbindungen standardmäßig über `claude -p` bauen. Dabei ANTHROPIC_*-Variablen aus der Umgebung des Kindprozesses entfernen, sonst wird still über die API abgerechnet. Pro Tastendruck genau ein Aufruf, keine unbeaufsichtigten Schleifen (Grauzone der Abo-Bedingungen). Ein „Turbo“, bei dem claude.exe vorab startet und still wartet, spart ~4–5 s, Vorlage ist `SWYF-ClaudeMod/mod/ClaudeCaller/Vorstart.cs`. Siehe [[kevin-zwei-konten-uebergabe]].
