---
name: blueprint-vorschau-renders
description: "Wie man eigene 3D-Modelle (Turret) passend in die Blueprint-Vorschau rendert (Spielwinkel, Massstab)"
metadata:
  node_type: memory
  type: reference
  originSessionId: 2c69e304-687f-40a4-a85b-6bb959366676
  modified: 2026-11-09T13:16:13.921Z
---

3D-Modelle (nicht im Kachel-Pack) kommen per Blender-Render in die Vorschau: `blueprint/tools/turret_bild.py` importiert das Spiel-FBX + Textur aus der Test-Mod (nur lesen), Kamera orthografisch, 30 Grad ueber Horizont, Blick Nordwest (rotation_euler 60/0/45 Grad, Blender X = Osten, Y = Norden). Massstab bei 2x: 90,51 px je Einheit am Boden, 78,4 px je Einheit senkrecht (eine Ebene = 192 px = 2,449 Einheiten); gerendert doppelt (181 px/Einheit, 640x640), im Blueprint `bild_skala 0.5`, `anker [320,320]` = Drehachse am Boden. Hoehe je Turret-Stufe aus turret/T1_modelldaten.md Abschnitt 5. Autos: Lack kommt aus Shader-Tint (Textur-Alpha 0 = Lackflaeche), Raeder sind eigene Modelle -- fuer die Vorschau bisher weggelassen.

Verwandt: [[blueprint-kevins-zielbild]]
