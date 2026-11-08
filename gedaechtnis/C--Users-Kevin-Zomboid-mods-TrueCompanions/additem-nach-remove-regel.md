---
name: additem-nach-remove-regel
description: "Die Regel, die ich in diesem Projekt ständig breche — ein AddItem nach einem Remove ohne Prüfung vernichtet Ware"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bdc5780d-84d1-4dce-b9f1-6dca08a415d1
  modified: 2026-08-24T11:26:55.966Z
---

Kevin am 24.08.2026: *„falls ja schreib dir das mal fett in dein gedächniss .md datei rein du
machst den fehler ja ständig."* Er hat recht.

**Ein `AddItem`, das fehlschlagen kann, darf nie auf ein bereits erfolgtes `Remove` folgen.**
`AddItem` liefert bei voller Tasche `nil`. Steht der Gegenstand dann nirgends mehr, ist er
vernichtet.

**Why:** In TrueCompanions war die Regel streng auf **Kisten-Transfers** angewandt
(`St.MoveItem` zählt vorher/nachher und entfernt nur bei bewiesener Ankunft) und **nie aufs
Ausrüsten** — dabei ist das dieselbe Sache: eine getragene Waffe, ein Rucksack, ein
Kleidungsstück existieren nur als Typ-String am Brain, der echte Gegenstand ist gelöscht. Am
24.08. steckte das an **sieben** Stellen gleichzeitig und hat Kevin vermutlich eine Schaufel
gekostet. An einer stand sogar der Kommentar „no dupes, nothing lost".

**How to apply:** Vor jedem Ship laufen lassen:
`grep -rn "getInventory():AddItem(" 42/media/lua` — jeder Treffer, der nicht durch
`Interact.HandBackOrDrop` geht oder einen *neuen* Gegenstand erzeugt, ist ein Verdächtiger.
`HandBackOrDrop(chr, brain, typ)` ist der Boden: erst die Tasche, sonst die eigene Kachel, nie
ins Nichts.

Die Regel steht auch als hervorgehobener Kasten ganz oben in Abschnitt 5 von `CLAUDE.md`.

Siehe [[werkzeugverlust-test]], [[sonden-muessen-sagen-was-sie-messen]].
