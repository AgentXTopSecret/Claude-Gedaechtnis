---
name: mp-boden-aufheben-4221
description: "GELOEST in v3.12.15/16 (Server-Tuer GroundTake, BundleLogs, RemoveStump). Hintergrund: seit PZ 42.21 (28.09.) wirkt transmitRemoveItemFromSquare auf einem MP-Client nur lokal -- Foerster/Sortierer/Beacon-Abbau u. a. verdoppeln oder entfernen nichts beim Server; gefunden 29.09. nachts, ungespielt, nicht gefixt"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-30T11:27:49.797Z
---

**GELOEST (05.10. nachgelesen):** v3.12.15/16 bauten die Server-Tueren (GroundTake, BundleLogs, RemoveStump), Kevin hat danach getestet und v3.12.19 hochgeladen. Neue Boden-Aufnahmen (z. B. Tierpfleger) nehmen GroundTake -- nicht mehr als offenes Risiko nennen.

42.20 hatte in IsoGridSquare.transmitRemoveItemFromSquare einen GameClient-Zweig mit RemoveItemFromSquarePacket (scratchpad igs_all.txt vom 25.09., Offset 17-85). Im 42.21-Jar (28.09.) ist der weg: Client = nur lokales RemoveTileObject, Paket-Annotation handlingType 3 -> 2. Selbst per disasm.py nachgelesen am 29.09. nachts.

Folge im MP: jede Client-Stelle, die vom Boden aufhebt oder ein Weltobjekt entfernt, wirkt nur lokal -> Tasche + Server-Boden = Verdopplung (rote Linie, siehe [[kevins-zwei-rote-linien]]). Betroffen u. a. ForestJob (Setzling/Stamm/Buendel/Beute), Haul takeFromYard, Combat.lua:403, Production ~884/899, Forestry Stumpf/Baum, Beacon.lua:1520 (Abbau), WorkstationBuild 297/521. SP nicht betroffen. Server-Aufrufe (ForestServer, FishNetServer, BuildServer) sind ok.

**Why:** Der apicheck nach dem Update prueft nur, ob Methoden existieren, nicht ihr Verhalten -- so rutschte das durch. Alte Changelog-Saetze "hat einen Client-Zweig" gelten nur fuer 42.20.

**AUDIT FERTIG 30.09. (_docs/mp_boden_4221.md): Fund echt; 6 Verdopplungs-Stellen (Foerster 5, Sortierer 1; Foerster-Aufraeumen = Exploit), 5 Schein-Entfernungen; Fix = eigene Server-Tueren; 2 Verlustfenster im Entwurf, eines davon (Antwort beim Mitfahren) steckt heute schon im Netz-Einsammeln. Wartet auf Kevins Schnelltest (3 Pfannen) und sein Go.** **30.09. mittags NEU GESTARTET (Run wf_46cac520-05e, Skriptkopie im Scratchpad mp-ground-pickup-4221.js) -- Ergebnis nach _docs/mp_boden_4221.md.** Frueher: **NEU STARTEN BEI KEVINS NAECHSTER NACHRICHT (seine Ansage 29.09. ~23:45):** der Pruef-Workflow 'mp-ground-pickup-4221' (Inventar aller Client-Stellen + Server-Tuer-Plan + Gegenpruefung + deutscher Bericht nach _docs/mp_boden_4221.md) wurde gestoppt, bevor ein Agent fertig war. Skript: ~/.claude/projects/C--Users-Kevin-Zomboid-mods-NPCCrew--docs/c3f66696-88e0-4da2-a026-3f8129d53368/workflows/scripts/mp-ground-pickup-4221-wf_c7a5dfe6-b78.js (Run wf_c7a5dfe6-b78; nichts im Cache). Neu starten per Workflow({scriptPath}) -- oder in neuer Sitzung das Skript neu schreiben.

**How to apply:** Eintrag ganz oben in _docs/offene_arbeit.md ('42.21-FUND'). Erst Kevins MP-Test (Stamm aufheben, relog), dann Fix: Server-Tuer 'vom Boden nehmen' (Server entfernt zuerst, Client bucht auf Antwort). Nach jedem PZ-Update zusaetzlich die Paket-Annotationen (pkt_annots) und die transmit*-Methoden gegen die Vorversion vergleichen.
