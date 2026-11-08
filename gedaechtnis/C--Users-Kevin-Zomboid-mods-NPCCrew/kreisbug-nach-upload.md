---
name: kreisbug-nach-upload
description: "Kevin 12.10.2026 23:30: der Kreis-/Lauf-Fehler (NPC dreht sich auf der Stelle, Zaun-Pendeln, Minischritte) hat nach dem Upload v3.13.31 oberste Prioritaet, VOR Stufe 3 Teil 3-2; Messdaten liegen bereit"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7fd0ad-7592-45c0-90c1-5c2a73830a30
  modified: 2026-10-12T21:30:53.091Z
---

Kevin woertlich am 12.10.2026 um 23:30, nach drei Sichtungen an einem Tag (Schmied im Einzelspieler, Tierpfleger auf dem Weg zur
Kiste, Tierpfleger beim Melken am Zaun): "ja den kreis bug müssen wir nach dem upload UMGEDINKT finden und fixxen!!!"

**Why:** Der Fehler ist das Sichtbarste, was an der Mod gerade stoert, und trifft alle Arbeiter (Sortierer, Koch, Pfleger, Relax).
Gemessen seit 04.10. (Sonde [TC-MOVESTALL] ab v3.12.50), Ursache unbekannt. Kevin hat den Upload trotzdem freigegeben, weil ein
Sicherheitsnetz (Teleport zum eigenen Ziel nach ~20 s) den Stillstand beendet -- zufrieden ist er damit nicht.

**STAND 13.10.2026 ~01:45 -- DIAGNOSE FERTIG, DANN PAUSE (Kevin: "mach erstmal eine pause dann merk dir den rest fuer spaeter"):**
Ergebnis in `_docs/kreisbug/DIAGNOSE.md`. BELEGT: die Leichensuche der Engine schickt Companions zu Leichen toter Spielfiguren in
+-10 Kacheln (Ausfluege ohne Grund, Rucke in Posen, Zulieferer der Zaunspruenge); unser Zaehlfehler in der Kletterbremse. NICHT
geklaert: das haeufige Stehen mit Gehanimation ohne Kollision. Naechste Version (naechste freie Nummer, nach v3.13.36): Leichensuche
fuer Angeworbene abschalten (BRAUCHT KEVINS WORT: achte Ausnahme der eisernen Regel, `setBodyToEat(nil)`, Jar-belegt, kein Lua-Beleg),
Zaehlfehler beheben, drei Messungen. Fuenf Fragen an Kevin stehen in `_docs/uebergabe_2026-10-12.md` (oberster Block) -- BEIM
WEITERMACHEN ZUERST DIESE FRAGEN STELLEN, nichts ohne sein Wort fuer R1 bauen. Bandits hat sich am 13.10. 00:49 aktualisiert
(Sicherung 2026-10-13_0143) -- vor dem Bau gegen unsere Aufsaetze gegenlesen.

**KEVINS ANTWORTEN 13.10.2026 16:35 (AskUserQuestion, alle vier 'Empfohlen' gewaehlt) -- GELTEN, nicht neu fragen:**
(1) Leichensuche fuer die Crew abschalten: JA, bauen -- die ACHTE AUSNAHME der eisernen Regel (`IsoZombie.setBodyToEat(nil)`), mit
Schalter ohne Neustart; Bedingung wie bei der siebten: macht es im Test Fehler, kommt es wieder raus. (2) Spielerleichen in der
Testserver-Basis bleiben bis zum Test LIEGEN (Gegenprobe). (3) Versuchsschalter 'trotz Kollisionsmarke weiterfahren' fuer EINE
benannte Figur: mitbauen, Vorgabe aus. (4) Zwei unbelegte LESE-Aufrufe (Spielerleiche/Zombieleiche/Skelett unterscheiden) NUR in
der Konsolen-Sonde erlaubt. Noch offen: Meldung der drei Bandits-Stellen an den Bandits-Autor ja/nein. Gebaut wird das als
v3.13.37 (Workflow gestartet 13.10. ~16:40); danach Test durch Kevin (MP West-/Ost-Basis, SP Schmiede), dann Stufe 3 Teil 3-2.

**STAND 13.10.2026 19:40 -- v3.13.37 GEBAUT UND VON KEVIN GETESTET (MP + SP):** die Leichensuche der Engine ist als Ursache von Kreis UND
Schritt-Bug IM SPIEL BESTAETIGT (SP-Gegenprobe: Schutz aus -> ~1500 Eintritte ohne Gehbefehl in einer Minute + drei Kreis-Staende, Kevin: 'das buggt
jz hardcore rum die laufen im kreis + schritt bug'; Schutz an -> 'der schritt bug war direkt weg'; 10 min mit Schutz: null). Die achte Ausnahme
(setBodyToEat(nil)) bleibt drin, CLAUDE.md-Absatz eingetragen. ZWEITE URSACHE GEMESSEN: Haengen an Tonne/Kiste = Bandits' ZAMove kehrt bei
Kollisionsmarke vor update() zurueck (Store Keeper: Marke in 820 von 820 Bildern, update() lief 0); der Versuchsschalter
TrueCompanions_StallUpdate(Name) hat es bei Sortierer1 behoben (0 Staende gegen je 3 bei zwei Kollegen), Kevin: 'genau da ... hat der fast perfekt
gearbeitet'. NAECHSTER SCHRITT: StallUpdate als feste Reparatur fuer ALLE (zusammen mit dem XP-Fix als v3.13.38), danach Stufe 3 Teil 3-2. NOCH
OFFEN: Drehen auf der Stelle neben einem Hindernis im Relax (Dylan Collins), Staende mit Kollision 000 beim Folgen, MP-Engine-Warnung
'WalkTowardState but path2 != null'. Einzelheiten: _docs/kreisbug/bau/STAND.md, Konsolen _docs/diag_konsolen_2026-10-13_mp/ und _sp/.

**How to apply:**
- Reihenfolge nach dem Upload v3.13.31: park -> v3.13.32 (Sperre 'Coming soon' wieder heraus, siehe [[schlachten-coming-soon]]) ->
  DANN die Jagd auf diesen Fehler -> erst danach Stufe 3 Teil 3-2 ([[stufe3-entscheidungen]]).
- Messdaten und offene Fragen: `_docs/diag_2026-10-12_mp_kreisbug.md`; gesicherte Konsolen der MP-Sitzung unter
  `_docs/diag_konsolen_2026-10-12_mp/`; aeltere Befunde `_docs/diag_v3.13.28_fe_minischritte.md`.
- Drei Erscheinungen, vermutlich eine Familie: (1) Gaenge enden ohne Ankunft (walktoward + ZombieIdleState, moving=true),
  (2) ein alter Gehbefehl (bPathfind=true) wird spaeter in einer Pose aktiv = Minischritte, (3) Bandits greift am Tor nach Zaeunen
  neben dem Weg = Drehen/Pendeln. Erst messen, dann heilen (v0.98.8); ein Fix muss in Einzelspieler UND Mehrspieler laufen
  ([[both-modes-always]]).
- Kevin erwartet einen echten Fix, nicht ein weiteres Sicherheitsnetz. Wenn die Ursache in Bandits oder der Engine liegt und nur
  umgehbar ist: ihm das mit Beleg sagen.
