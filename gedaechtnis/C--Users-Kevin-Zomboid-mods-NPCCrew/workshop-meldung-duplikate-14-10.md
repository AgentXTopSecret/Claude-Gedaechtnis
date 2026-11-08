---
name: workshop-meldung-duplikate-14-10
description: Workshop-Meldung 14.10.2026 -- Rekruten verdoppeln sich beim Verlassen der Basis; behoben in v3.13.50+.51 (ungespielt), Melder antwortet nicht mehr, abgeschlossen
metadata:
  type: project
---

Meldung (Workshop, 14.10.2026 abends, oeffentlicher Stand v3.13.31): "whenever I leave the base, some of my recruits duplicate ... 2, 3 or
sometimes 5 of them getting shredded by zombies. And once I'm back into my base, they are there, or they die (death option)."

Erste statische Einordnung (Hauptsitzung, ohne Agenten): Mechanismus Populations-Kopie (CLAUDE.md Abschnitt 5, Eintraege v3.9.46-.65:
Chunk-Entladen schreibt Companion-Koerper mit persistentOutfitID in die native Population, Bandits adoptiert Kopien mit Cluster-Eintrag).
Id-Netz seit v3.9.46 (Regeln A/B/C). Bekannte, dokumentierte Luecke im MP: Sweep-/Herholen-Neubau eines nicht geladenen Koerpers schreibt
die alte Id nur im SP nach parkedIds (client/BanditsNPCPersistence.lua ~7114-7117 und ~7380) -- im MP bleibt die Populations-Waise
adoptierbar; mehrere Neubauten waehrend einer Fahrt passen zu "2-5 Kopien". Nicht entschieden: SP oder MP, Folgende oder Basis-NPCs.

**Why:** Kevin fragte "kannst du nachgucken ob sowas echt passieren kann?"; Antwort: ja, Mechanismus belegt, Fall offen.
**How to apply:** Kevin hat einen Antworttext bekommen (fragt SP/MP, Folgen/Basis, console.txt). Kommen die Angaben: console.txt nach
[TC-COPY]/[TC-VANISH]/Kopie/Zwilling greppen, dann gezielt pruefen (rote Linie 2 von [[kevins-zwei-rote-linien]]). Erst nach Stufe 3 bauen.

Kevin 14.10. ~20:15: die bekannte MP-Luecke wird NACH STUFE 3 ALS ERSTES geschlossen (eigener Punkt, nicht wieder liegen lassen; STAND.md).

**15.10.2026 ~12:35:** keine Antwort des Melders; Kevin: "kannst du da diesen mp bug auch nach suchen und fixxen?" -> Lauf 'mp-kopien-fix'
(wf_aa12312b-d9a, 8 Agenten: Diagnose+Plan, Bauer, 2 Pruefer, Fixer, Gegenpruefer, Integrator) als v3.13.50, Basis-Tag dupfix-base-v3.13.50,
Berichte _docs/kopien_mp/. Vorstudie: der SERVER weiss im Bau-Zweig von doRestore, dass kein Koerper der uid geladen ist -> alte Eintraege
dort raeumen + NoteId, Regel A entfernt die spaetere Kopie. Davor am selben Tag v3.13.49 (Hold ground prueft alle Zombies, Workshop-Meldung Zaun).

**15.10.2026 13:50 GEBAUT als v3.13.50** (Tag review-head-v3.13.50 = 0c7806c1): BS.RetireOrphans(uid, keepId, label, keepId2) in
shared/BanditsNPCBaseSweep.lua, gerufen im Server-doRestore (Bau + alreadyhere) und im SP-BeginRestore; raeumt Cluster-Eintraege der uid ohne
geladenen Koerper + NoteId -> Regel A entfernt spaetere Kopien. Pruefer 0/1/3 und 0/1/7 (beide ernst = alreadyhere-Zweig, behoben), Gegenpruefung
0/0/4. UNGESPIELT. OFFEN (Kevins Wort): Folgende nicht neben dem FAHRENDEN Auto neu bauen (erst bei < 0,8 km/h) -- zweite Haelfte der Meldung
('shredded/die'). CLAUDE.md-Saetze v3.9.8 / v3.9.49(b) 'Client-Transmit erreicht Server-Cluster' laut Jar falsch -- Nachtrag offen.
Workshop-Antworttext in _docs/kopien_mp/v3.13.50_integrator.md.

**15.10.2026 ~18:00 ABGESCHLOSSEN VON UNSERER SEITE:** Kevin: "ich glaub zum bug mit den mehreren npc's wirds keine antwort mehr geben vom bug
reporter". Beide Haelften gebaut: v3.13.50 (MP-Waisen raeumen) und v3.13.51 (kein Neubau neben fahrendem Auto, Kevin "ja mach das so").
Nicht weiter nachfragen; nur wieder aufmachen, wenn eine neue Meldung oder Kevins MP-Test (testliste_stufe3_kurz.md Abschnitt v3.13.50) etwas zeigt.
