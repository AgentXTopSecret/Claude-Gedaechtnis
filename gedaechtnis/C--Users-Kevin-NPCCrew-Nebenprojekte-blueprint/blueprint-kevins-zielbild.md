---
name: blueprint-kevins-zielbild
description: "Kevins Zielbild fuer die Blueprint-Starter-Basis (komplette ummauerte Basis, Turrets an den Eingaengen, Workshop-Werbebild)"
metadata:
  node_type: memory
  type: project
  originSessionId: 2c69e304-687f-40a4-a85b-6bb959366676
  modified: 2026-11-09T13:16:08.624Z
---

Kevin (09.11.2026) zeigte ein Project-Zomboid-Werbebild als Vorbild: komplette ummauerte Basis (Mauer ringsum, mehrere Gebaeude mit Flachdach, Hof, Parkplatz mit Autos, Felder, Gehege, Wald drumherum). Dazu: Turrets aus dem Turret-Projekt sollen die Eingaenge absichern, alles "mega nice", damit jeder beim ersten Workshop-Bild abonniert.

**Why:** Die Basis ist Werbung fuer NPC Crew (Workshop-Screenshots, spaeter Video); Optik zaehlt so viel wie Funktion.

**How to apply:** Entwuerfe wie eine Festung denken (hohe Steinmauer gewaehlt), hohe Teile hinten (Norden/Westen), Niedriges vorn. Turrets nur ebenerdig: das Turret zielt nur auf gleiche Ebene (NCTurretTest client/BanditsNPCTurretClient.lua:195/:299), Tuerme mit Turret brauchen erst eine Aenderung im Turret-Projekt. Entwurf 1 liegt in blueprint/entwurf/ (ENTWURF.md). Siehe [[blueprint-vorschau-renders]].
