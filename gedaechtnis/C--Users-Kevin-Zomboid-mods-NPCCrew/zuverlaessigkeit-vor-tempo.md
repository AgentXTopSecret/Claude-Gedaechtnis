---
name: zuverlaessigkeit-vor-tempo
description: "Kevin will Bau -> Pruefer -> Nachbesserung je Version beibehalten, auch wenn es langsamer ist; Zuverlaessigkeit vor Tempo"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-02T18:54:35.508Z
---

Jede Version laeuft als Workflow: Bau-Agent, unabhaengiger Pruefer, bei Funden Nachbesserung -- nacheinander, weil alle in Versionszeile und UI.json schreiben. Nicht zugunsten von Tempo abkuerzen.

**Why:** Kevin 02.10.2026 auf meine Frage, ob kleine Sachen wieder direkt ohne Pruefer gehen sollen: *"nein so lassen mir ist zuverlaessigkeit wichtiger, besser als wenn du das 10x nachbessern musst"*. Am selben Tag fanden die Pruefer ueber 20 echte Fehler vor seinem Test.

**How to apply:** Auch fuer kleine Aenderungen mindestens einen Pruefer; Wartezeit ansagen statt Pruefung weglassen. Grenze bleibt: ueber 10 Agenten je Auftrag vorher fragen. Siehe [[kevins-zwei-rote-linien]], [[both-modes-always]].

Kevin 15.10.2026 ~23:00 (auf meinen Vorschlag 'zwei Bauer gleichzeitig'): "aber nur wenn das genauso zuverlaessig ist ansonsten so lassen".
Also: parallele Bauer NUR, wenn ihre Dateien vollstaendig getrennt sind (kein gemeinsames UI.json, keine gemeinsame Lua-Datei, Versionszeile
nur der Integrator) und jeder seine Pruefer selbst laeuft; Pruefrunde danach unveraendert. Sonst nacheinander wie bisher.
Kevin ~23:05 "jaa klingt gut": UEBERSETZUNGEN SIND KEIN HINDERNIS mehr -- parallele Bauer schreiben neue/geaenderte UI-Texte NICHT in die
UI.json, sondern je in eine eigene Liste (_docs/fix_vX/vX_texte_<bauer>.json, sieben Sprachen); erst der Integrator traegt sie einmal sortiert in alle
sieben UI.json ein (Round-Trip, Paritaet, CN-Zeichen). Gemeinsame Lua-Dateien bleiben ein Grund fuer 'nacheinander' (lost update).
