---
name: workshop-waechter
description: "Kevin 02.11.: Desktop-App meldet neue Workshop-Kommentare und Diskussionsbeitraege per Fenster, Klick oeffnet Steam; bei 'was gibt's Neues' die Datei workshop_neu.txt lesen"
metadata:
  node_type: memory
  type: reference
  originSessionId: 8e7fd0ad-7592-45c0-90c1-5c2a73830a30
  modified: 2026-11-02T18:12:03.191Z
---

`C:\Users\Kevin\Tools\NPCCrew-Waechter\workshop_waechter.pyw`, Start ueber die Desktop-Verknuepfung 'NPC Crew Workshop-Waechter'. Oeffentliche Seiten, kein Login, kein API-Schluessel.
Kommentare jede Minute, Diskussionen alle 5 Minuten, kleines Fenster nur bei neuen Beitraegen anderer, Klick oeffnet `steam://openurl/...` in der Steam-App, Symbol unten rechts mit Rechtsklick-Menue.
Neue Beitraege stehen in `%LOCALAPPDATA%\NPCCrewTools\workshop_neu.txt`, Fehler in `workshop_waechter.log`, der Stand in `workshopwatch_stand.json` daneben.
Fragt Kevin nach neuen Meldungen: diese Datei lesen, bevor er etwas einfuegen muss. Autostart setzt er selbst per Rechtsklick 'Mit Windows starten' (Kevin 02.11., Form wie seine NetSpeedBar in `Desktop\Programme von Claude`), ich trage nichts ein ([[sicherheitsregeln]]).
