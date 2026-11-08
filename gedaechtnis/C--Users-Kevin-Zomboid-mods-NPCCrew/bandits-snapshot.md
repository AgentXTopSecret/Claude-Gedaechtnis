---
name: bandits-snapshot
description: "_docs/tools/snapshot.py sichert Bandits- und PZ-Stand (Text + Jar) nach Zomboid/backups/snapshots und meldet Aenderungen; bei Sitzungsbeginn und bei 'seit dem Update'-Meldungen laufen lassen"
metadata:
  node_type: memory
  type: reference
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-30T12:53:52.115Z
---

Kevins Vorschlag 30.09.2026: Sicherungskopien fremder Quellen, damit ein stilles Update verglichen werden kann. Anlass: Bandits hat sich am 29.09. 23:37 still aktualisiert (laut Steam-Aenderungsprotokoll nur "hidden feature for Month One mod"), PZ 42.21 kam am 28.09. -- fuer beide gab es keinen alten Stand.

Werkzeug: `python _docs/tools/snapshot.py` (Pruefen + bei Aenderung neue Sicherung mit Liste der geaenderten Dateien), `--list`, `--diff bandits|pz`. Ziel `C:\Users\Kevin\Zomboid\backups\snapshots\<quelle>\<datum>` (bandits ~5 MB, pz ~212 MB inkl. Jar). Erste Sicherung 30.09. 14:53. Aelterer Bandits-Lua-Stand zusaetzlich unter `backups\Bandits-lua-stand-2026-09-29_2337`.

**How to apply:** Bei Sitzungsbeginn einmal laufen lassen (13 s). Meldet es GEAENDERT, die geaenderten Dateien gegen unsere Aufsaetze pruefen (wie beim 42.21-Fund [[mp-boden-aufheben-4221]]). Aenderungsprotokoll von Bandits: steamcommunity.com/sharedfiles/filedetails/changelog/3268487204; PZ-Patchnotes: Steam-News-API appid 108600.
