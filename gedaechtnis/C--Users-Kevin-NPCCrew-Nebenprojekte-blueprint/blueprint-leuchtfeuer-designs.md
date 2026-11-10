---
name: blueprint-leuchtfeuer-designs
description: "Kevins zwei neue Basis-Designs vom 10.11.2026 (Basis Leuchtfeuer + Burg Leuchtfeuer, je 100x80 Kacheln) und wo Auftrag, Vorlagen und Vorschau liegen"
metadata:
  node_type: memory
  type: project
  originSessionId: 6e34c02d-c562-4c74-a7f8-6fe78bc56748
  modified: 2026-11-10T21:11:52.774Z
---

Kevin hat am 10.11.2026 (~17:10) zwei fertige Grundriss-Plaene mitgebracht ("ich hab noch 2 designs erstellen lassen", von jemand anderem gezeichnet): **Basis Leuchtfeuer** (normale Basis) und **Burg Leuchtfeuer** (Ritterburg mit Burggraben), beide 100 x 80 Kacheln, mit Durchfahrt West-Ost, Entladezone vor der Lagerhalle, 4 Standplaetzen fuer Sattelzuege, 12 PKW-Plaetzen, KFZ-Werkstatt, Tankstelle. Er will zuerst eine Vorschau, "wie es genaustens ingame aussehen wuerde", und sagt DANN, ob er es per Befehl im Spiel haben will.

**Why:** Die Plaene sind Kevins Vorgabe -- Plan-Treue geht vor eigenen Ideen; Abweichungen (z. B. Zusatz-Generator, fehlende 3 Stationen) werden gemeldet, nicht still geaendert.

**ERINNERUNG, die Kevin bestellt hat (10.11.2026 ~20:55: "das bitte nochmal sagen wenn ich es teste ;D sonst vergess ich das"):** Sobald Kevin eine Leuchtfeuer-Basis im Spiel testen will, ihm ZUERST und unaufgefordert sagen: im Spielstand den NPC-Crew-Sandbox-Wert "Base area size" (`BanditsNPC.BaseAreaRadius`, Vorgabe 45, erlaubt bis 75) hochstellen -- etwa 50, genauer Wert je Design in `leuchtfeuer/<basis|burg>/BERICHT.md`. Sonst liegt der Rand der 98 Kacheln breiten Basis ausserhalb der Basiszone. Das gehoert auch als Punkt 1 in jede Testanleitung dazu. Entschieden am selben Abend: Turrets auf die Tuerme, Beacon in die Mitte ("hauptsache die ganze base ist eine basiszone und es funktioniert"), Rest des Laufs auf Fable.

**How to apply:** Zuerst `blueprint/leuchtfeuer/STAND.md` lesen (Vorschau beider Designs seit 10.11. 22:15 fertig: Basis gruen, Burg gelb mit 3 Datenfehlern; Fragen an Kevin; ein 10-Agenten-Lauf auf Fable kostete rund 80 Punkte der Fable-Woche -- kuenftig vorher mit Kevin das Modell klaeren). Alles liegt in `blueprint/leuchtfeuer/`: `AUFTRAG.md` (beide Plaene Kachel fuer Kachel + Regeln), `vorlage/` (Kevins Bilder + Raster-Ausschnitte, `raster.py`), `basis/` und `burg/` (Generator, JSON, Bilder, `BERICHT.md`), `FAHRZEUGE.md`. Bau per Befehl (Lua, Test-Mod) erst auf Kevins Ja. Bekannte Grenze: der Beacon steht in beiden Plaenen weit im Westen, NPC Crew `BaseAreaRadius` ist 45 (Sandbox bis 75). Uebergabe-Stand: [[blueprint-uebergabe-stand]], Zielbild: [[blueprint-kevins-zielbild]], Sattelzug: [[blueprint-sattelzug-plan]].
