---
name: blueprint-mp-auftrag
description: "Blueprint im Mehrspieler: Plan fertig, alle Fragen entschieden (nur admin), Bau-Lauf 2 startbereit -- Kevin hat ihn am 13.11.2026 auf spaeter verschoben; Start nur auf sein neues Wort"
metadata:
  node_type: memory
  type: project
  originSessionId: 4d678754-ad1e-4e32-b3c7-d96bab2275b2
  modified: 2026-11-13T20:05:33.113Z
---

Kevin 13.11.2026 ~15:52: *"ich will das es auch in mp funktioniert"* -- der Baubefehl `NCBlueprint_Bau()` der Test-Mod
NCBlueprintTest soll auch im Mehrspieler eine Basis hinstellen.

Stand 13.11. ~21:15:
- Lauf 1 (Forschung + Plan, 6 Agenten) fertig -> `blueprint\MP_PLAN.md` (Weg H: Server baut Welt/Beacon/Turrets/Fahrzeuge, der
  Client des Admins macht die NPC-Crew-Schritte; Bench-Kern nach `shared\NCBlueprintBenchKern.lua`, neue `server\NCBlueprintBenchServer.lua`
  und `client\NCBlueprintBenchMP.lua`). Alle 15 Fragen entschieden: F1 **"nur admin"** (16:35), F2-F15 **"ja alles so"** (Vorgaben).
- Alle drei Entwuerfe im SP gespielt und abgenommen -> Bedingungen fuer Lauf 2 erfuellt (auch Turret T4d eingebaut, Pruefer gruen).
- Kevin fragte ~21:10 "kannst du jz machen das es im mutliplayer auch geht?", bekam Dauer und Versionen genannt (eine Bau-Version in
  zwei Teilen, 9 Agenten, ~4-5 h; danach sein MP-Test und realistisch Version 1b, 2-4 Agenten, 1-2 h) und sagte dann: **"ne so wichtig
  ist das jz nicht merk dir das einfach fuer ein anders mal sodas jeder claude account das weiss"**. Verbrauch da: Woche alle Modelle
  72 %, Fable 100 % (Reset 20.11. ~14:00).
- Einzelheiten und Startanleitung: `blueprint\UEBERGABE.md` Abschnitt 0.0 (Absatz "MP-BAU AUF SPAETER VERSCHOBEN").

**Why:** Kevin will MP, aber nicht um den Preis, dass sein Wochenkontingent fuer die anderen Projekte knapp wird. Er wechselt Claude-Konten;
jedes muss den Stand ohne Gespraechsverlauf kennen.

**How to apply:** Den MP-Bau nicht von selbst starten und nicht draengen. Fragt Kevin wieder danach (oder nach dem Reset), vorher
`get_usage`, ihm Agentenzahl (9) und Dauer nennen, `alles_pruefen.sh` neu laufen lassen (NPC Crew aendert sich weiter), dann Lauf 2
nach `MP_PLAN.md` Abschnitt 9 als zwei Workflows (Teil 1 drei Agenten, Zwischenabnahme in der Hauptsitzung, Teil 2 sechs Agenten).
Rote Linien im MP (kein Kick, nichts doppelt, nichts haengt) gelten. Siehe [[blueprint-uebergabe-stand]].
