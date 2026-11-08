---
name: both-modes-always
description: "Kevins Regel vom 30.08.2026 - jede Aenderung muss im Einzelspieler UND im Mehrspieler funktionieren, und das ist vor dem Ausliefern zu pruefen"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f31a6c60-393f-4384-a887-2468f35b6ab7
  modified: 2026-08-30T08:15:03.945Z
---

Jede Aenderung an NPC Crew muss **im Einzelspieler UND im Mehrspieler** funktionieren.
Kevin am 30.08.2026: *"kannst du dir ins gedächniss schreiben das du jedes mal durchlädst
das alle sachen die du einbaust im singleplayer und multiplayer funktionieren sollen?"* —
kurz zuvor gefragt: *"nicht das danach singleplayer wieder kaputt ist"*.

**Why:** Er spielt ueberwiegend Einzelspieler; der Mehrspieler-Umbau ist neu. Ein
Rueckschritt im Einzelspieler waere fuer ihn teurer als jeder offene Mehrspieler-Fehler.
Die Sorge ist berechtigt: die Pruefung, die diese Regel ausgeloest hat, fand sofort einen
echten Fehler — `BanditsNPC.IsStaff` fragte `getAccessLevel()` ohne `isClient()` und haette
im Einzelspieler jedem die Debug-Oberflaeche geoeffnet (v2.9.19).

**How to apply:** Vor dem Ausliefern jede neue oder geaenderte Stelle einmal aus beiden
Richtungen durchgehen und im Changelog ausdruecklich sagen, was im Einzelspieler passiert —
nicht "sollte unveraendert sein", sondern welcher Zweig dort laeuft. Merkposten:

* Im Einzelspieler sind `isClient()` **und** `isServer()` falsch. Vanillas eigener Test
  lautet woertlich `not isServer() and not isClient()` (`ISPlowAction.lua:185`).
* `isAdmin()` ist im Einzelspieler falsch, `getAccessLevel()` ist dort **unzuverlaessig** —
  Vanilla setzt an allen sechs Fundstellen ein `isClient()` davor.
* ModData eines Mehrspieler-Clients erreicht nie eine Platte; im Einzelspieler schon.
  Deshalb liegen reine Client-Einstellungen in `NPCCrewClient.ini` — siehe
  [[client-settings-in-file]] falls angelegt.
* Ein Riegel gehoert an die **Engstelle**, nicht an einen Aufrufer: `BeginRestore` hat
  sieben Aufrufer, und ein Riegel bei einem davon war zweimal zu wenig (v2.9.13/v2.9.14).

Siehe auch [[kevin-tests-by-playing]].
