---
name: upload-v3-13-95
description: "v3.13.95 seit 21.10.2026 20:32 oeffentlich (Steam 23.267.995 Byte, 5760 Abos); was gespielt/ungespielt mitging; bei Workshop-Meldungen zuerst hier."
metadata:
  type: project
---

v3.13.95 ist seit 21.10.2026 20:32 im Workshop (Kevin hat hochgeladen, Tag `upload-v3.13.95`, Ordner geparkt). Ab hier zaehlt "nichts hochgeladen seit v3.13.95".

Gespielt vor dem Upload: Leichen entsorgen im MP als Rolle user (4 verbrannt, kein Kick), T-4 (Fenster weicht beim Zeichnen aus), sauberes Laden v3.13.95 (SP-Client + Server).
UNGESPIELT mitgegangen: Tuer-Kick-Schutz im MP (Crew-Schuss schickt nie ein Tuer-Paket; Ursache per Sonde eingegrenzt, nicht 100 % bewiesen -- am selben Tor trat auch ein gewoehnlicher Zombie), Sonde v3.13.94 ([TC-THUMPWHO]/[TC-SRVPOS], nur bei Crew logging).
Bekannte offene Punkte: Crew-Leiche im MP kann als Kandidat zaehlen ([[uebergabe-19-10]], Fahrplan); Unstuck fuer Liegende ([[unstuck-liegende]]); Server sieht die Crew springen.

**Why:** Bei einer Kick- oder Leichen-Meldung aus dem Workshop zuerst wissen, was ungespielt mitging.
**How to apply:** Kommt ein Kick 'HitShortDistance ZombieHitThumpablePacket' wieder: [TC-THUMPWHO]-Zeilen lesen (Crew logging 2), nicht raten.
