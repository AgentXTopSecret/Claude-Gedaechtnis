---
name: sicherheitsregeln
description: "Feste Sicherheitsregeln: Steam-API-Schluessel nie lesen, RCON-Passwort nie ausgeben, Sandbox-Konsole nur per cp, keine Zugangsdaten, kein Upload/Start ohne Kevin"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-11-01T23:42:45.558Z
---

- Den Steam-API-Schluessel (C:\Users\Kevin\NPCCrew-Statistik\steam_api_key.txt) NIE lesen oder ausgeben.
- Das RCON-Passwort nie ausgeben -- `_docs/tools/rcon.py` liest es selbst aus NPCCrewTest.ini.
- Testaccount-Konsole nur per `cp` mit vollem Pfad in den Scratchpad kopieren, nie `cd` nach C:\Sandbox; Agenten bekommen den Sandbox-Pfad nie.
- Keine Zugangsdaten eingeben (Kevin loggt sich bei Steam selbst ein), keine Autostart-Eintraege oder versteckten Starts, PC nie herunterfahren.
- Nie hochladen; Steam-Inhalte oeffentlich nur nach Kevins ausdruecklichem Ja; Spiel/Server nur auf sein Wort starten; Downloads nur mit Name/Quelle/
  Groesse und seinem Ja.

**Why:** Kevins Vorgaben ueber viele Sitzungen (Norton-Vorfaelle, Sandboxie-Popups, Schutz seiner Schluessel). **How to apply:** bei jeder Sitzung,
auch nach Kontowechsel. Siehe [[keine-suche-im-benutzerordner]], [[testaccount-konsole-sandbox]].
