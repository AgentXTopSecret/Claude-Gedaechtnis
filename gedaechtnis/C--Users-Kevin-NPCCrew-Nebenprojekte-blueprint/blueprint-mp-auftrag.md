---
name: blueprint-mp-auftrag
description: "Kevin 13.11.2026: der Blueprint-Baubefehl soll auch im Mehrspieler funktionieren -- noch nicht gebaut, Vorschlag Forschungs-Lauf dann Bau-Lauf, Start nur auf sein Wort"
metadata:
  node_type: memory
  type: project
  originSessionId: 4d678754-ad1e-4e32-b3c7-d96bab2275b2
  modified: 2026-11-13T16:16:59.972Z
---

Kevin am 13.11.2026 ~15:52, direkt nachdem die Bench in die Test-Mod kopiert war: *"ich will das es auch in mp funktioniert"*.
Gemeint (meine Lesart): der Baubefehl `NCBlueprint_Bau()` der Test-Mod NCBlueprintTest soll auch im Mehrspieler eine Basis
hinstellen. Bis dahin war MP bewusst aus (`tor()` in `NCBlueprintBench.lua`).

Stand 13.11. ~17:25: Lauf 1 (Forschung + Plan, 6 Agenten) fertig -> `blueprint\MP_PLAN.md` (Weg H, Bench-Kern nach shared, neue
Server- und MP-Client-Datei, Bau-Lauf 2 mit 9 Agenten, Fragen F2-F15 mit Vorgaben). Nichts gebaut. Lauf 2 erst nach Kevins SP-Test,
nach dem Turret-T4d-Einbau und auf sein Startwort.
(Frueherer Stand 15:55: nichts gebaut, kein Lauf gestartet.) Vorschlag an Kevin: Lauf 1 "MP-Forschung und Plan" (3 Agenten auf Opus,
nur lesen + `blueprint\MP_PLAN.md`), danach Lauf 2 "MP-Bau" (etwa 7 Agenten). Meine Vorgaben, solange Kevin nichts anderes sagt:
gebaut wird auf dem Server (Host-Spiel und dedizierter Server), nur Admins loesen aus, der SP-Weg bleibt unveraendert, alles bleibt
Testhilfe. Erste Sichtung und offene Punkte: `blueprint\UEBERGABE.md` 0.0 (Absatz "NEUER AUFTRAG"). Siehe [[blueprint-uebergabe-stand]].

Kevins Entscheidung 13.11. ~16:35 auf "Wer soll im Mehrspieler den Baubefehl nutzen duerfen?": **"nur admin"** -- moderator und alle
anderen Rollen still ablehnen (kein Kick), der Server prueft. Fuer alle Spieler gedacht ist spaeter nur Phase 2 (Builder-Job mit Material).

**Why:** Kevin betreibt NPC Crew auch auf einem MP-Server (13.11.); seine Regel ist "SP UND MP" (Werkstatt-CLAUDE.md Abschnitt 4).

**How to apply:** MP nie nebenbei einschalten -- rote Linien (kein Kick bei Rolle user/AntiCheat 2, nichts doppelt, nichts haengt)
gelten; vor dem Lauf `get_usage` und Kevin die Agentenzahl nennen (am 13.11.: Woche alle Modelle 33 %, Woche Fable 64 %, darum Opus).
