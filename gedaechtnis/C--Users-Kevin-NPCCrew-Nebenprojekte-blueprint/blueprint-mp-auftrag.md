---
name: blueprint-mp-auftrag
description: "Blueprint im Mehrspieler: 14.11.2026 16:17 FERTIG und in die Test-Mod kopiert (Lauf 2, 9 Agenten, Abnahme AUFFAELLIG 0), ungespielt; naechstes Kevins MP-Test, dann Version 1b; Stand blueprint/UEBERGABE.md 0.00"
metadata:
  node_type: memory
  type: project
  originSessionId: 4d678754-ad1e-4e32-b3c7-d96bab2275b2
  modified: 2026-11-14T15:18:58.659Z
---

Kevin 13.11.2026 ~15:52: *"ich will das es auch in mp funktioniert"* -- der Baubefehl `NCBlueprint_Bau()` der Test-Mod
NCBlueprintTest soll auch im Mehrspieler eine Basis hinstellen. Plan `blueprint\MP_PLAN.md` (Weg H, F1 **"nur admin"**, F2-F15
**"ja alles so"**). 14.11. ~12:15 Kevin: **"so mach die mod fertig"** = Startwort; ~13:30: *"du machst jz weiter bis alles komplett
fertig ist und dann spawn ich später mal eine burg im mp okay?"* = Auftrag bis zum Ende inkl. Kopieren (bei geschlossenem Spiel).

**14.11. 16:17 FERTIG:** Lauf 2 in drei Workflows (Teil 1 A1/A4/A5, Teil 2a A2/A3, Teil 2b P1/P2/N1/G1 `wf_83bc0e5a-646`), G1 gruen,
G1-01 von der Hauptsitzung eingebaut (eine Zeile `H.antwort`, Szenario `spaetzeile`). Abnahme `_arbeit\blueprint\mp\bau\alles_pruefen_mp.sh`:
AUFFAELLIG 0, MP-Attrappe 102/102, SP log-gleich (65 Szenarien), Fundstellen 625/0. In die Test-Mod kopiert (10/10 byte-gleich,
Sicherung `NCBlueprintTest_2026-11-14_161756_*`). **Ungespielt.** Kevins Anleitung `blueprint\b1\TEST_fuer_kevin_MP.md` (er aendert
selbst: Server-ini Mods + `NCBlueprintTest;NCTurretTest`, Sandbox "Base area size" 45 -> 50, Burg "Turrets per base" >= 11).
Neue Dateien: `shared\NCBlueprintBenchKern.lua`, `server\NCBlueprintBenchServer.lua`, `client\NCBlueprintBenchMP.lua` (alle Bench).

**Why:** Kevin will MP; er wechselt Claude-Konten, jedes muss den Stand ohne Gespraechsverlauf kennen.

**How to apply:** Neue Sitzung: UEBERGABE 0.00 lesen. Kevins MP-Testergebnis als Version 1b einarbeiten (Staging, dann
`alles_pruefen_mp.sh`, Kopieren nur bei geschlossenem Spiel); beim Test den Fehlerwaechter mitlaufen lassen. Die MP-Attrappe ordnet
Pakete je Kanal, das echte Spiel nicht (P1-02) -- Paket-Reihenfolge nie aus der Attrappe glauben. Siehe [[blueprint-uebergabe-stand]].
