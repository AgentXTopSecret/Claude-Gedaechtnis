---
name: verdrehte-stationen
description: "30.09. gefunden, auf Kevins Wort NACH dem Upload v3.12.19 zu fixen: wood_bench/steel_bench (senkrecht) und chest_freezer haben verdrehte Sprite-Reihenfolgen -> Engine entfernt sie nicht (SP: altes Teil bleibt beim Aufwerten)"
metadata:
  type: project
---

**ERLEDIGT (geprueft 02.10.):** seit v3.12.20 repariert (S.RepairPairs + Entfernen mit Nachweis), Kevin hat D1-D3 am 01.10. im SP bestanden. Offen nur ein MP-Test mit einer ALTEN verdrehten Bank (server-console '[TC-STATION] Altlast Server ... berichtigt'). Nicht wieder als Bauauftrag fuehren.


Kevins SP-Test 30.09. 22:30: Reloading Bench aufgewertet, alte Holzwerkbank blieb unter der neuen stehen. Log: "Failed to find all parts of a multi-tile object!" (safelyRemoveTileObjectFromSquare). S.Pieces-Reihenfolgen widersprechen SpriteGridPos: wood_bench v muss {27,26}, steel_bench v {19,18}, chest_freezer h/v vertauscht.

**Why:** Kevin 30.09.: "ja dann merk dir das" -- erst hochladen, dann reparieren. SP: Duplikat-Teil (kein Gegenstandsverlust), MP: Ablehnung + Erstattung.

**How to apply:** Als ERSTES in der naechsten Sitzung bauen (Plan in _docs/offene_arbeit.md "VERDREHTE ZWEIFELD-STATIONEN"): Reihenfolgen korrigieren, verdrehte Altbestaende beim Entfernen per setSpriteFromName geraderuecken, SP nur setzen wenn Altes weg ist. Kevins SP-Stand hat bei 6336,5329/5330 Holz- UND Stahlwerkbank. Siehe [[leerer-chum]], [[moegliche-features]].
