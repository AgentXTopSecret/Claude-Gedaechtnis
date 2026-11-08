---
name: waffe-nicht-verlieren
description: "Das erprobte Muster, mit dem ein ausgerüstetes Werkzeug beim Wechsel NICHT verlorengeht — im Spiel bestätigt"
metadata: 
  node_type: memory
  type: reference
  originSessionId: bdc5780d-84d1-4dce-b9f1-6dca08a415d1
  modified: 2026-08-24T21:23:39.688Z
---

**So verliert eine Companion keine Waffe.** Am 24.08.2026 im Spiel bestätigt (Kevins
`[TC-TOOL]`-Log: drei Wechsel, jedes `takes up` mit seinem `puts back`, Verschleiß korrekt
mitgetragen). Kevin: *„speicher dir das fett in dein gedächniss wie man keine waffe verliert
damit du nicht immer denselben fehler machst."*

**Die Ausgangslage, die alles erklärt:** ein ausgerüstetes Werkzeug ist **kein Gegenstand**.
`Bandit.SetHands` baut es bei jedem Wechsel neu aus dem Typ-String — es lebt als
`brain.weapons.melee` (Typ) plus `brain.npcMeleeState` (Zustand). Der echte Gegenstand wurde
beim Ausrüsten gelöscht.

**Die vier Regeln, die daraus folgen:**

1. **Erst zurückgeben, dann ausrüsten.** Nie umgekehrt. `useTool` legt die bisherige Waffe mit
   `inv:AddItem(cur)` zurück, *bevor* `EquipWeapon` die neue setzt. Der Bruch-Pfad im Kampf
   macht es genauso: `putBrokenAway` zuerst, Ersatzwaffe danach.
2. **Der Zustand reist mit.** `back:setCondition(st.c)` aus `npcMeleeState`. Ohne das kommt
   eine abgenutzte Axt bei jedem Wechsel neuwertig zurück — der stille Reparatur-Exploit von
   v0.75.40.
3. **Niemals `brain.weapons.melee` leeren, ohne den Gegenstand vorher wiederherzustellen.**
   Jede Stelle, die den Slot auf `Base.BareHands` setzt, muss vorher zurückgeben.
4. **`Interact.HandBackOrDrop(chr, brain, typ)` ist der Boden** — erst die Tasche, sonst die
   eigene Kachel, nie ins Nichts. Ein Netz, kein Ersatz für Regel 1.

**Was NICHT die Ursache ist:** eine volle Tasche. `ItemContainer:AddItem` erzwingt keine
Kapazität (Vanilla: 205 Aufrufe, kein einziger prüft den Rückgabewert). Das habe ich am 24.08.
behauptet und in v0.91.24 zurücknehmen müssen. Siehe [[additem-nach-remove-regel]].

**Kontrolle statt Theorie:** jeder Wechsel druckt seit v0.91.21 eine `[TC-TOOL]`-Zeile mit
Zustand. Ein `takes up` ohne späteres `puts back` ist der Tatort.

Siehe [[werkzeugverlust-test]].
