---
name: bugwatch-bei-jedem-test
description: "Kevins Ansage 28.09. -- den Fehlerwaechter (_docs/tools/bugwatch.py) bei JEDEM Test mitstarten (Spiel-/Serverstart), per Monitor, alle 30 min neu anmelden."
metadata:
  node_type: memory
  type: feedback
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-28T16:54:26.297Z
---

Sobald Kevin etwas testen soll (Spielstart, Serverstart, MP mit Testaccount), wird der Fehlerwaechter
`C:\Users\Kevin\Zomboid\mods\NPCCrew\_docs\tools\bugwatch.py` ueber das Monitor-Werkzeug mitgestartet
(`python "C:/Users/Kevin/Zomboid/mods/NPCCrew/_docs/tools/bugwatch.py"`, timeout 1800000) und nach jedem
30-min-Ablauf neu angemeldet, solange er testet. Aus nur, wenn Kevin es sagt oder nicht mehr testet.

**Why:** Kevin, 28.09.: "den waechter must du dir jz merken das du den bei jeden server start und so mit
startest wenn ich was testen soll". Der Waechter laeuft lokal (kostet keine Tokens), weckt nur bei echten
Fehlern -- Kevin muss dann nicht selbst die Konsole abschreiben.

**How to apply:** Vor/mit jeder Testansage pruefen, ob ein Monitor laeuft; wenn nicht, starten. Bei einer
Meldung zuerst den Vorfall lesen (console.txt / server-console.txt / Testaccount-Kopie), dann Kevin kurz
sagen. Testaccount-Konsole nur ueber den vollen Pfad, nie cd (siehe [[testaccount-konsole-sandbox]]).
NOISE-Liste im Skript nur nach `--noise`-Pruefung erweitern.

**Nie im Mod-Ordner schreiben (28.09.):** der Waechter schrieb anfangs alle 5 s seinen Stand nach mods/NPCCrew/_docs --
das Hauptmenue las darauf die Mod-Liste immer wieder neu und laggte (Kevin hat es erkannt: "weil du die dateien in das
verzeichniss geschoben hast wo mods geladen werden"). Stand/Verlauf/Messpunkte liegen seither unter
%LOCALAPPDATA%/NPCCrewTools und werden nur bei Aenderung geschrieben. Gemessen: ohne Schreiben kein Neu-Einlesen mehr.
