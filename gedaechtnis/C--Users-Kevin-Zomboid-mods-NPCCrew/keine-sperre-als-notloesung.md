---
name: keine-sperre-als-notloesung
description: "Kevin 21.10.: keine Feature-Sperre (CorpseSoon-Art) mehr als Reaktion auf einen Fehler einbauen -- nur im Sonderfall und nur nach Rueckfrage; stattdessen messen und reparieren."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8e7fd0ad-7592-45c0-90c1-5c2a73830a30
  modified: 2026-10-21T15:20:26.842Z
---

Keine Sperre (Feature fuer Modus/Rolle abschalten, z. B. `BanditsNPC.CorpseSoon`) als Antwort auf einen gemeldeten Fehler einbauen.
Kevin 21.10.: *"bau demnaechst keine sperre mehr ein das ist nur im sonderfall noetig"*.

**Why:** v3.13.89 hat Leichen entsorgen im MP gesperrt, weil v3.13.88 an 4 Spielerleichen falsch gemessen hatte ("MP-Client sagt immer
isZombie false"). Die Server-Sonde zeigte danach: Client und Server lesen richtig, die Sperre war unnoetig und hat eine Version gekostet.

**How to apply:** Bei einem Fehler zuerst messen (Sonde, frisches Gegenbeispiel), dann reparieren. Eine Sperre nur, wenn Kevin sie
ausdruecklich will oder es ein echter Sonderfall ist (z. B. unfertiges Feature vor einem Upload, siehe [[schlachten-coming-soon]]) --
dann vorher fragen, nicht selbst entscheiden.
