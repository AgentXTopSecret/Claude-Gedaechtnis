---
name: parallel-workflows
description: "Doku-Lauf neben Bau-Lauf ok; die 10-Agenten-Grenze gilt JE WORKFLOW, nicht summiert ueber parallele Laeufe (Kevin 08.11.)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8e7fd0ad-7592-45c0-90c1-5c2a73830a30
  modified: 2026-10-19T12:16:15.249Z
---

Ein Bauplan-/Lese-Workflow, der nur Dokumente schreibt, darf neben einem laufenden Bau-Workflow laufen (Kevin 19.10.: "beide wenn das nicht stört ;D").

**Why:** spart Wartezeit; Kevin fragte zuerst "stört der nicht beim aktuellen?" -- er will sicher sein, dass sich nichts in die Quere kommt.

**How to apply:** nur wenn die Dateien getrennt sind (kein Lua, keine UI.json im Doku-Lauf); gemeinsame Doku-Dateien (Fahrplan) danach pruefen. Zwei BAU-Versionen nie gleichzeitig. ~~Wenn beide zusammen ueber 10 Agenten kommen, VOR dem Start sagen und fragen.~~ **BERICHTIGT 08.11. (Kevin: 'meine regel ist 10 agenten pro projekt nicht aufgeteilt auf alles was ich grade mache'):** die Grenze gilt je Projekt bzw. Workflow; parallele Laeufe verschiedener Projekte (NPC Crew, Baer, Turret, Zweihaender) werden NICHT zusammengezaehlt. Den Verbrauch trotzdem nennen. **NOCHMAL GENAUER 08.11. (Kevin: 'eigtl war die 10 agenten regel sogar per workflow gedacht'):** die Grenze gilt je WORKFLOW -- auch zwei Laeufe im selben Projekt duerfen je 10 haben.
