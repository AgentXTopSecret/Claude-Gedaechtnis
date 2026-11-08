---
name: stand-18-10-abend
description: "ZUERST LESEN (Stand 18.10.2026 abends): v3.13.71 (Fahrplan B1) im Workflow, was danach zu tun ist, naechste Schritte; 5-h-Fenster war knapp"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-18T16:30:32.962Z
---

Stand 18.10.2026 ~18:30 (Kevin: "stand so merken und die naechsten schritte auch weil das 5std fenster reicht nichtmehr aus").

**Heute erledigt:** Upload v3.13.70 (15:51, [[upload-v3-13-70]]); Steam-Guide veroeffentlicht und verlinkt ([[steam-guide]]);
Statistik-Seite `C:\Users\Kevin\NPCCrew-Statistik` misst jetzt NPC Crew UND True Companions (3751199292) in EINEM Sammler
(kein zweiter Autostart), Umschalter, Bewertungs-Spalten, "Deabonniert", Aufrufe-Karte ganz links. Nach Skript-Aenderung den
Sammler neu starten: pythonw-Prozess beenden, sammler.lock loeschen, Autostart-Verknuepfung starten.

**v3.13.71 FERTIG 18.10. ~18:45** (Integrator durch, Pruefer gruen, Gegenpruefer 0 toedlich/0 ernst), gespiegelt (geparkt,
Guide-Link in workshop.txt erhalten), Statuszeile + Fahrplan B1 nachgetragen. UNGESPIELT. NAECHSTER SCHRITT: Kevin testet
`_docs/testliste_v3.13.71.md` (5 Punkte, 1 SP + 4 MP; Bugwatch mitstarten, Server per NPCCrew-Testserver.bat). Neue offene Fragen
F71-1..F71-3 (fragen_2026-10-17.md, nicht blockierend). Danach B2 Stock-Reiter.

**v3.13.72 (B2 Stock-Reiter je Zustand + Kadaver-Tooltip) LAEUFT** seit 18.10. ~21:10, run wf_16ba4c1d-e8c, Basis-Tag b2-base-v3.13.71,
Berichte _docs/fix_v3.13.72/. Kevin konnte v3.13.71 noch nicht testen ('bau erstmal weiter'). Nach Abschluss: wie bei .71 (Versionszeile, sync, Status,
Fahrplan B2, Testliste _docs/testliste_v3.13.72.md); abgebrochen -> nur fehlende Stufe neu. Danach B3 Fix G + die vier Spieltexte -- Kevins Antworten 14/15/16/18 liegen vor (18.10. ~21:15, in fragen_2026-10-17.md ganz unten), Fix G direkt nach .72 starten (nicht parallel: Versionszeile/UI.json/Diff).

(Alt:) v3.13.71 = Fahrplan B1 (zwei gleiche Taschen gleich voll -> Take-Abdruck; Fix C2 Kistengriffe ueber Server-Tuer;
Kleinkram), Workflow wf_432c4bb6-35f, Basis-Tag b1-base-v3.13.70. Stand 18:30: Plan, 4 Bauer, 2 Pruefer, Fixer fertig,
Gegenpruefer lief, Integrator fehlte.

**Wenn er fertig ist (oder abgebrochen):**
1. Versionszeile `42/media/lua/shared/BanditsNPC.lua:1229` muss 3.13.71 sein; Pruefer-Ergebnis lesen.
2. Abgebrochen (Limit/Kontowechsel)? Journal `subagents/workflows/wf_432c4bb6-35f/journal.jsonl` lesen und NUR die fehlende Stufe
   neu starten (Vorbild `_docs/nachtschicht/fixe_integ.js`), NIE resumeFromRunId ([[workflow-fortsetzen-falle]]).
3. `python _docs\tools\workshop_sync.py` (geparkt), Statuszeile `_docs/tagschicht_status.txt`, Fahrplan-Zeile B1 abhaken.
4. Kevin kurz berichten + Testliste `_docs/testliste_v3.13.71.md` (nur das Noetigste, SP+MP, Bugwatch mitstarten).

**Danach (Fahrplan `_docs/fahrplan_2026-10-17.md`, abwechselnd Feature/Fix):** B2 Stock-Reiter je Zustand, B3 Fix G, B4 Leichen
entsorgen, B5 Fix H MIT Polsterung (Kevin 18.10.: Polsterung ist ein Bug, kein Feature), B7 Mod-Check 2, ... B14 Forager.

**In die naechste Fix-Version (Nebenfunde des Guide-Workflows, Spieltexte):** "Your crew is full" raet zu Dismiss (loescht endgueltig)
-> Release nennen; "P1" in einem Lager-Text; "she" im Tipp zum Schlachthaken; UI_BN_Fish_NoFishers nennt noch den alten
Fish-Knopf im Job-Reiter. Offene Fragen R1/R2/Z1 (v3.13.68) weiter unbeantwortet, nicht blockierend.

**Montag:** x20-Konto; vor dem Kontowechsel darf KEIN Workflow laufen (Agenten brechen ab).

**Stand 18.10. ~22:20:** v3.13.72 (B2 Stock-Reiter) FERTIG + gespiegelt, ungespielt (Test _docs/testliste_v3.13.72.md; Pruefer 1 ernst behoben, Gegenpruefer
0/0/2; offen F72-1 Setter-Selbsttest, F72-2 Kistenlisten vereinheitlichen; Zaehldauer auf Kevins Lager ungemessen). v3.13.73 (B3 Fix G mit Kevins Antworten
14/15/16/18 + vier Spieltexte) LAEUFT, run wf_3e540376-e0d, Tag b3-base-v3.13.72, Berichte _docs/fix_v3.13.73/. Kevin testet .71/.72/.73 spaeter zusammen.
Danach laut Fahrplan B4 Leichen entsorgen (3 Teilversionen V-A1/V-A2/V-B je ~9 Agenten; Kevins Antworten liegen vor 18.10. ~22:35, fragen_2026-10-17.md ganz unten: LE-1 JA = neunte Ausnahme isZombie -> CLAUDE.md Abschnitt 3 beim Bau eintragen; LE-2 Schalter JE SPIELER im Spiel mit 3 Stellungen inkl. alles verbrennen; LE-12 a; LE-13 a; AL-1 ja; Rest nach Empfehlung), dann B5 Fix H mit Polsterung (Frage 17 M08 vorher).

**Stand 18.10. ~23:55:** v3.13.73 (B3 Fix G) FERTIG + gespiegelt, ungespielt (Test _docs/testliste_v3.13.73.md; 1 ernster Pruefer-Fund behoben:
fremde Altflaeche in eigener Basis sperrte Teleports -> eigene Zone gewinnt; Gegenpruefer 0/0/3; offen F73-1..F73-4 nicht blockierend).
UNGESPIELT JETZT: v3.13.71, .72, .73 -- Kevin testet die drei Testlisten zusammen (SP+MP, Bugwatch). NICHTS LAEUFT.
Budget: 5h 89 % (Reset 02:00), WOCHE 77 % (Reset Fr 23.10. 15:00). Leichen entsorgen = 3 Teilversionen (~20 % Woche) -> NICHT auf diesem
Konto anfangen; ab Montag x20-Konto (vorher kein Workflow laufen lassen). Reihenfolge danach: B4 Leichen V-A1/V-A2/V-B (Antworten liegen vor),
B5 Fix H mit Polsterung (Frage 17 M08 vorher stellen).
