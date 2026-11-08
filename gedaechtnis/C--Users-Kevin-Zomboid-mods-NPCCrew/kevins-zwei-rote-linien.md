---
name: kevins-zwei-rote-linien
description: "Kevins zwei harte Anforderungen an jede Version -- keine Gegenstandsverluste, keine zufaelligen Teleports (= Basis-NPC taucht beim Spieler unterwegs auf; Steckenbleib-Teleport zum eigenen Ziel ist ok); Massstab fuer jede Pruefung und jeden Changelog."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-18T19:12:43.894Z
---

Kevin am 18.09.2026 nachts, nach der Szenario-Pruefung ueber E1-E3: *"ja ich will keine item verluste und keine random teleports sehn"*.

**Why:** Das sind die zwei Fehlerklassen, die ihm Fehlerberichte von Workshop-Nutzern einbringen (Stay/Relax-Companions neben dem Spieler, Aexte/Ruten weg oder doppelt) und die er selbst am haeufigsten gemeldet hat (v0.75.40-Schaufel, 252 Kohle, Koch-Teleport, Melder-Faelle 17.09.).

**How to apply:** Jede Pruefung (Widerleger-Workflow) bekommt diese zwei Fragen als erste Linse: (1) wo wird ein Gegenstand vernichtet oder verdoppelt (AddItem/Remove-Reihenfolge, Typ-String am Brain, Manifest-Fenster, Sync-Pakete im MP), (2) welcher Weg baut einen Koerper neben dem Spieler oder setzt ihn um (Sweep-Neubau aus 'Folgen', Exil, prevProgram-Verlust, Rollback). Ein Fund in einer der beiden Klassen ist immer "ernst", auch wenn er selten ist. Im Changelog ausdruecklich sagen, welche der beiden Klassen eine Version beruehrt. Siehe [[both-modes-always]].

**KLARSTELLUNG Kevin 05.10.:** *"die regel keine zufaelligen teleports waren aber nur bezogen auf teleports von npc s die von der base aus zum spieler selbst teleportieren z.b wenn man grade unterwegs ist"*. Gemeint ist also NUR: ein Companion, der an der Basis arbeiten/bleiben soll, taucht beim Spieler unterwegs auf (Sweep-Neubau, Exil, Folgen-Verlust, Kopien). Ein Steckenbleib-Teleport einer Companion zu IHREM EIGENEN Arbeitsziel (Trog, Stall, Quelle) ist dagegen erlaubt -- Kevin zieht ihn sogar einer Sperre vor ("lieber teleport als dass der stall gesperrt wird", 05.10., E4).
