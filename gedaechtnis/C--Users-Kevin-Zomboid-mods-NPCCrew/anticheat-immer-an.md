---
name: anticheat-immer-an
description: "Kevin will den Anti-Cheat auf dem Testserver immer an (alle AntiCheat*=2 in NPCCrewTest.ini), damit Probleme sofort sichtbar werden"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-28T12:29:41.638Z
---

Kevin, 28.09.2026: *"ja stell anti-cheat immer an damit man direkt sieht wenn das probleme macht"*.
Seit 28.09. stehen alle zehn `AntiCheat*`-Zeilen in `Zomboid\Server\NPCCrewTest.ini` auf 2 (Kick). Vorher standen sie auf 4 (aus), nur Speed stand auf 2. Die Sicherung davor liegt in `backups\NPCCrewTest.ini.vor-anticheat-2026-09-28`.

**Why:** Mit Admin und abgeschaltetem Anti-Cheat blieb schon eine ganze Fehlerklasse unsichtbar: normale Spieler wurden beim ersten Kistengriff gekickt (v3.10.97). Der Testaccount spielt deshalb als Rolle 'user'. Siehe [[kevins-zwei-rote-linien]].

**How to apply:**
- Nicht zurückstellen, nur um einen Test durchzubringen.
- Wird Kevin oder der Testaccount gekickt, zuerst `server-console.txt` lesen: welcher Anti-Cheat hat angeschlagen, und bei welchem Paket.
- Beim Serverstart prüfen, ob das Spiel die ini wieder zurückgeschrieben hat.
- Der Engine-Standard für AntiCheatPermission ist 2 (belegt). Für die anderen neun Schalter ist er ungeprüft.
