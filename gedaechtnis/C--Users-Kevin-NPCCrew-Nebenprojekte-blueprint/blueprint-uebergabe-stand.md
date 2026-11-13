---
name: blueprint-uebergabe-stand
description: "Uebergabe Blueprint, Stand 13.11.2026 15:48: Bench auf Turret b9859e8 nachgezogen und in die Test-Mod kopiert (Test-Mod = Staging, ungespielt, alle Pruefer gruen); zuerst blueprint/UEBERGABE.md Abschnitt 0.0"
metadata:
  node_type: memory
  type: project
  originSessionId: 6e34c02d-c562-4c74-a7f8-6fe78bc56748
  modified: 2026-11-13T14:49:27.964Z
---

Kevin wechselt zwischen Claude-Accounts (10.11., 11.11. ~15:00: "der andere account soll alles wissen was ich noch testen
soll und wo es weiter geht"; 13.11. neue Blueprint-Sitzung auf dem zweiten Konto: "Ja, neue Sitzung"). Volle Uebergabe:
`C:\Users\Kevin\NPCCrew-Nebenprojekte\blueprint\UEBERGABE.md` **Abschnitt 0** (0.0 = Stand 13.11., darunter 11.11.), Belege
`blueprint\NAEHTE.md` 8, Verlauf `blueprint\leuchtfeuer\STAND.md`.

Stand 13.11. 15:48: Test-Mod NCBlueprintTest = Staging `b1\mod\NCBlueprintTest` (Festung 3b + Basis Leuchtfeuer + Burg Leuchtfeuer,
per `NCBlueprint_Wahl("basis"|"burg")` baubar, NICHTS gespielt). Am 13.11. 15:48 auf Kevins "Ja, kopieren" die nachgezogene Bench
kopiert (sha1 01b6b070, Sicherung `NCBlueprintTest_2026-11-13_154815_vorher/_nachher.zip`): Blickrichtung als 6. Argument an
`T.PlacePair(sq, lv, nil, nil, u, yaw)`, Hinweis liest die Turret-Mod (seit T3b zielen Turrets bis 3 Ebenen nach unten, der Befehl
stellt sie leer hin), Zeile zur Kollision. Fundstellen 433 / 0 / 0, alle Pruefer gruen
(`_arbeit\blueprint\turretnaht_1113\alles_pruefen.sh`). Kein Workflow, kein Timer offen. Die Turret-Sitzung kopiert bald T4d ein: danach
`alles_pruefen.sh` noch einmal. Kevin vor dem Test erinnern: NPC Crew "Base area size" 50, Burg "Turrets per base" >= 11
([[blueprint-leuchtfeuer-designs]]). Offene Fragen an Kevin: UEBERGABE 0.4 und 0.0 (Turrets geladen hinstellen? Sperr-Sprite in
die Verbotsliste?).

Zwei Lehren aus dem 13.11. (meine Deutung, nicht Kevins Wort):
- "verschoben (ok)" im Fundstellen-Pruefer heisst nur, dass die Zeile noch irgendwo steht. Sie kann inzwischen etwas anderes belegen
  (`if zs[i] == e.z then` nach Turret T3b). Nach einem Umbau der Nachbarn die Funktionskoerper per `git diff` gegen den letzten
  gruenen Stand vergleichen (Skripte `turret_funk_diff.py`, `stations_norm.py` in `_arbeit\blueprint\turretnaht_1113\`).
- `tools\blueprint_lua.py --pruefe` liest NPC Crews `BanditsNPCStations.lua` als TEXT (Katalogzeilen). Aendert NPC Crew die
  Schreibweise dort (13.11.: `label=` -> `lk=`/`ld=`), meldet der Selbsttest jedes Teil als fehlend, obwohl im Spiel nichts bricht.

**Why:** Ein anderer Account hat den Gespraechsverlauf nicht; ohne Uebergabe wuerde er Staende verwechseln oder mit einer
veralteten Naht testen lassen.

**How to apply:** Neue Sitzung im Blueprint-Projekt: zuerst UEBERGABE.md Abschnitt 0 lesen, `fundstellen_pruefen.py` laufen lassen,
dann Kevin nach seinen offenen Antworten fragen, nichts in die Test-Mod ohne sein Ja, vor jedem Workflow get_usage (hoechstens 10
Agenten). Siehe [[blueprint-kevins-zielbild]].
