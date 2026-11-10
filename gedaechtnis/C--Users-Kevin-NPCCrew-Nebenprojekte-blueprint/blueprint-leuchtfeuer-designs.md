---
name: blueprint-leuchtfeuer-designs
description: "Kevins zwei neue Basis-Designs vom 10.11.2026 (Basis Leuchtfeuer + Burg Leuchtfeuer, je 100x80 Kacheln) und wo Auftrag, Vorlagen und Vorschau liegen"
metadata:
  node_type: memory
  type: project
  originSessionId: 6e34c02d-c562-4c74-a7f8-6fe78bc56748
  modified: 2026-11-10T16:30:27.297Z
---

Kevin hat am 10.11.2026 (~17:10) zwei fertige Grundriss-Plaene mitgebracht ("ich hab noch 2 designs erstellen lassen", von jemand anderem gezeichnet): **Basis Leuchtfeuer** (normale Basis) und **Burg Leuchtfeuer** (Ritterburg mit Burggraben), beide 100 x 80 Kacheln, mit Durchfahrt West-Ost, Entladezone vor der Lagerhalle, 4 Standplaetzen fuer Sattelzuege, 12 PKW-Plaetzen, KFZ-Werkstatt, Tankstelle. Er will zuerst eine Vorschau, "wie es genaustens ingame aussehen wuerde", und sagt DANN, ob er es per Befehl im Spiel haben will.

**Why:** Die Plaene sind Kevins Vorgabe -- Plan-Treue geht vor eigenen Ideen; Abweichungen (z. B. Zusatz-Generator, fehlende 3 Stationen) werden gemeldet, nicht still geaendert.

**How to apply:** Alles liegt in `blueprint/leuchtfeuer/`: `AUFTRAG.md` (beide Plaene Kachel fuer Kachel + Regeln), `vorlage/` (Kevins Bilder + Raster-Ausschnitte, `raster.py`), `basis/` und `burg/` (Generator, JSON, Bilder, `BERICHT.md`), `FAHRZEUGE.md`. Bau per Befehl (Lua, Test-Mod) erst auf Kevins Ja. Bekannte Grenze: der Beacon steht in beiden Plaenen weit im Westen, NPC Crew `BaseAreaRadius` ist 45 (Sandbox bis 75). Uebergabe-Stand: [[blueprint-uebergabe-stand]], Zielbild: [[blueprint-kevins-zielbild]], Sattelzug: [[blueprint-sattelzug-plan]].
