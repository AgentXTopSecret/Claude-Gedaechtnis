---
name: pz-42-22-pre-release
description: "PZ 42.22 ist seit 27.10. nur auf dem Pre-Release-Zweig (Leitern, Brecheisen), Hotfixes 04.11./06.11.; Kevins Spiel ist noch 42.21 public -- bei Wechsel auf stable Pruefung laufen lassen"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-11-08T11:54:57.789Z
---

Kevin fragte 08.11.: "am 6 kam ein project zomboid update hast du das schon gecheckt?" Geprueft 08.11.: das war **42.22.2 Pre-Release Hotfix** (06.11.), davor 42.22.1 (04.11., Zertifikatspruefung, JRE-Integritaetspruefung) und 42.22 selbst am 27.10. ("Moving on Up", Leitern begehbar, Brecheisen fuer Tueren/Fenster/Tore; der Zweig "Pre-Release" ersetzt "Unstable"). Quelle: Steam-News-API (`ISteamNews/GetNewsForApp/v2/?appid=108600`, oeffentlich).

Kevins Installation: Zweig `public`, buildid 25485521, Jar vom 28.09.2026 = **42.21**, nichts Neues installiert (appmanifest_108600.acf, keine Datei unter media neuer als 05.11.).

**Why:** Ein PZ-Update hat schon `loadstring` entfernt (42.20.4) und Zeilen verschoben (42.21); NPC Crew haengt an Engine-Aufrufen, Aktionsautomaten (XML) und Bandits.
**How to apply:** Sobald 42.22 auf `public` kommt (oder Kevin den Pre-Release-Zweig waehlt): `snapshot.py` (`--diff pz`), `apicheck.py`, `luacheck_pz.py --rebuild`, geaenderte Vanilla-Lua gegen unsere Aufsaetze lesen (Timed-Action-Parameternamen!), `media/actiongroups/zombie` und AnimSets diffen (Leitern koennten Wegfindung/Klettern der Crew betreffen), Heap in ProjectZomboid64.json pruefen, Bandits-Update abwarten. Den Zweig wechselt nur Kevin. Verwandt: [[bandits-snapshot]].
