---
name: sonden-muessen-sagen-was-sie-messen
description: "Eine Diagnose-Sonde muss dazuschreiben, WELCHEN Bereich und WELCHE Art Behälter sie gemessen hat"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bdc5780d-84d1-4dce-b9f1-6dca08a415d1
  modified: 2026-08-24T11:27:11.976Z
---

Am 24.08.2026 habe ich zweimal am selben Tag eine wahre Sondenausgabe falsch gelesen und
daraufhin Fehler gejagt, die es nicht gab.

1. Die Holz-Sonde durchsuchte **81×81 Kacheln um den Spieler**, die Arbeitszone war **12×26**.
   Ich habe die zwanzigfache Fläche gemessen und das Ergebnis als ihre Auslastung gelesen —
   zwei Versionen Jagd auf einen Seil-Fehler, den es nie gab.
2. Die Werkzeug-Sonde meldete „in a container at 6308,5373". Ich las „in seiner Lagerkiste".
   Sie durchsucht aber **jeden** Behälter — auch Autos, Ladenregale, Theken. Kevin: *„hä aber
   ich kann die garnicht finden wo soll das sein? hab meine ganze base abgesucht."* Der Fund
   lag 32 Kacheln westlich seiner Basis, in einem anderen Gebäude.

**Why:** Eine Sonde wird geglaubt. Misst sie das falsche Rechteck oder die falsche Art
Behälter, ist sie schlimmer als keine Sonde — sie liefert einen Beleg für eine falsche
Theorie.

**How to apply:** Jede Sonde schreibt dazu, **welchen Bereich** sie abgesucht hat (und bei
Companion-Verhalten ist das **deren Zone**, nicht ein Kreis um den Spieler), **was für ein
Behälter** ein Fund ist, und **wo** er relativ zu einem bekannten Punkt liegt (x wächst nach
Osten, y nach Süden). Vor dem Auswerten einer Sondenzeile prüfen, ob sie wirklich das
beantwortet, was ich gerade behaupten will.

Siehe [[additem-nach-remove-regel]].
