---
name: upload-v3-14-27
description: "v3.14.27 seit 01.11.2026 16:28 oeffentlich (Farmer fuer alle, Bandits-Kopien-Fix, Schild Vorgabe an); was ungespielt mitging; bei Meldungen zuerst hier"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-11-01T15:32:47.021Z
---

v3.14.27 ist seit 01.11.2026 16:28 im Workshop (Kevin hat hochgeladen; Steam 26,9 MB, 6513 Abonnenten; Tag `upload-v3.14.27`; Ordner wieder geparkt).
Ab hier zaehlt "nichts hochgeladen seit v3.14.27". Inhalt: Farmer fuer alle (v3.14.26 FarmerEnabled -> true), Fields-Reiter neu, Beet-Farben,
Taste Show fields (Numpad 0), Rezepte vom Server mit Sicherung, Wassertraeger bis 20 Gefaesse, Bandits-Update-30.10.-Fix (keine Kopien, Neubau
nach Laden auf jeder Ebene/ganzer Ladebereich, Speicher-Schild Vorgabe AN), MP-Leiche mit Tasche, Foerster-/Farm-Faell-Absagen, Herholen im Klettern.

Kevins Test 01.11. (SP + MP, Rolle user, AntiCheat 2) bestanden -- Ergebnisse in `_docs/testliste_2026-11-01.md`.
UNGESPIELT mitgegangen: Axtbruch im MP (Axt Zustand 1 brach nicht), Farm-Faell-10er-Regel im MP (nur statisch), Statustexte 'wartet auf die
Rezeptliste'/'norecipe', LootGuard (Bandits 42.21 hat WeaponLoot nicht -- ruht).
Gefunden beim Test, nicht gebaut (spaeter): 'Save to server' ohne vorheriges 'Apply' speichert die Aenderung nicht -- Save soll vor nicht
uebernommenen Aenderungen warnen; einmal 'container already has id' beim Testaccount beim Nachladen (kein Lua-Bezug) -- beobachten.
Patchnotes `_docs/patchnotes_v3.14.27_short.txt`; Guide aktualisiert (siehe [[steam-guide]]). Offene Kleinfragen des Integrators v3.14.27
(Sicherungs-Zeile nur Crew logging, 25er ohne Merker, norecipe bei fremder Station, Alt+F4 im Schlaf): Empfehlung 'so lassen', Kevin hat nicht
ausdruecklich geantwortet. Naechstes nach dem Upload: [[nach-dem-upload]].
