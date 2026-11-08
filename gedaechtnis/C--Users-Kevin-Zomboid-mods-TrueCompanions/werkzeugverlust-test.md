---
name: werkzeugverlust-test
description: "Der Werkzeugverlust hat eine belegte Ursache - zwei Werkzeuge desselben Typs; gefunden im Log, nicht durch Nachdenken."
metadata: 
  node_type: memory
  type: project
  originSessionId: bdc5780d-84d1-4dce-b9f1-6dca08a415d1
  modified: 2026-08-25T07:50:17.731Z
---

**Stand 25.08.2026: gefunden, behoben (v0.91.43) und IM SPIEL BESTAETIGT — mit zwei Aexten in der Tasche wechselt er sauber, nichts verschwindet.** Die Ursache stand im Log, ungelesen.

Kevin meldete den Werkzeug-Test als bestanden („das hab ich schon getestet das ging").
Ich habe trotzdem die `[TC-TOOL]`-Zeilen gelesen, und die widersprechen:
`takes up Base.WoodAxe cond=15`, vier Minuten später `takes up Base.WoodAxe cond=14`,
**ohne `puts back` dazwischen** — genau das Muster, für das die Zeilen seit v0.91.21 gedruckt werden.

**Der Mechanismus:** `useTool` übersprang die Rücknahme, wenn das gefundene Werkzeug
denselben Typ hatte wie das ausgerüstete — entfernte das gefundene Item danach aber trotzdem
aus der Tasche. Axt A lebt nur als Typ-String am Brain, `EquipWeapon` überschreibt den Slot
mit Axt B, B verschwindet aus der Tasche. Zwei rein, eine raus, keine Meldung.
Dasselbe Loch steckte im Profilfenster (`ctxEquip`) unter dem Kommentar „no dupes, nothing lost".

**Nicht bewiesen:** dass das Kevins Schaufel war — dafür hätte sie zwei Schaufeln tragen müssen,
und das hat niemand gezählt. Es ist das erste Loch der richtigen Form, das man im Code
**zeigen** statt bereden kann.

**Why:** Zwei Versionen lang wurde über eine falsche Theorie gestritten (volle Tasche, in
v0.91.24 zurückgenommen), während der Beweis auf der Platte lag.

**How to apply:** **Wenn ein Test als grün gemeldet wird, lies trotzdem das Log.** Und für den
Nachtest: er feuert nur mit **zwei Werkzeugen desselben Typs** in der Tasche — mit je einem
kann er gar nicht auslösen. Ein `[TC-TOOL] ... already has ...` heisst, der Schutz greift.
Siehe [[additem-nach-remove-regel]] und [[waffe-nicht-verlieren]].
