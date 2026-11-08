---
name: unstuck-liegende
description: "Kevin 21.10.: Unstuck muss eine niedergeschlagene (downed) Crew-Figur IMMER zum Spieler holen, auch aus einem ungeladenen Chunk -- nach dem Upload bauen."
metadata:
  type: project
---

Unstuck soll bei einer liegenden (downed) Figur immer wirken -- Kevin 21.10.: *"genau das soll echt immer gehn wenn die downed sind das hinlaufen waere ja nervig"*.

**Why:** Workshop-Melder Aurusine (21.10.): nach dem Wegtragen aus dem Kampf ("carried out of the fight") liegt die Figur oft in einem
entladenen Chunk, das Profil zeigt nur "Out of range - waiting where you left them", Unstuck holt sie nicht; man muss sie auf der Minimap suchen.

**How to apply:** Nach dem Upload bauen (Wochenlimit 92 % am 21.10.): Unstuck/Herholen holt eine liegende Figur zum Spieler (bleibt liegend,
dann Help up), auch wenn ihr Koerper nicht geladen ist; Profil sagt "liegt, in Sicherheit gebracht bei X,Y". Details in
_docs/fahrplan_2026-10-17.md (Abschnitt Aurusine). Rote Linie beachten: kein Verlust, kein Doppel-Koerper ([[kevins-zwei-rote-linien]]).

**Entschieden 21.10. (Kevin):** die 60 s Wartezeit nach dem Niederschlag (Sandbox UnstuckCooldown, P.StampUnstuckCooldown) BLEIBT -- *"jaa das hat schon einen grund"*. 'Immer' heisst also: nach Ablauf der Wartezeit muss Unstuck eine Liegende zuverlaessig holen, auch ungeladen.
