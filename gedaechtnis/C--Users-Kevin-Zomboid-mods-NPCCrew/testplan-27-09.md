---
name: testplan-27-09
description: "Kevins Testplan 27.09.: Fischer-Rework E1-E8 + Netze/Toene/Chum bis v3.11.44, alles ungespielt; Tests in offene_arbeit (a-w, N1-N10, X1-X4, K1/K2, v3.11.28-.44); Kevin testet alles am Ende"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-27T21:58:58.505Z
---

Kevin, 27.09.2026 ~0:35: *"merk dir was ich nacher alles testen soll sp und dann multiplayer tests und dann
testen wir das morgen wenn das die pruefer durch sind"*.

**ZUERST:** erledigt am 27.09. vormittags. Pruefung ueber v3.11.4: der Fix haette nicht gewirkt (Suednachbarin
6342,5321,1 ist ein oberes Treppenende) und machte ein nil-Loch -> v3.11.5. Gegenpruefung ueber v3.11.5 (3 Agenten): haelt,
Messort aus dem Spielstand nachgerechnet; ein kleiner Fund (Treppenstufe gewann den Ring) -> v3.11.6. Nichts mehr offen vor den
Tests. Kevin: Spiel UND Server neu starten, Zeile `[BanditsNPC] v3.11.6 loaded OK` pruefen (Server: server-console.txt).
Die fruehere Messzeile fuer 6342,5320,1 ist GESTRICHEN (Spielstand-Dekodierung hat es beantwortet).

**SP -- schon BESTANDEN (27.09. ~0:20, auf v3.11.2):** 1 Normalbetrieb (Sortierer/Koch/Crafter/Geben/Anwerben/Treat),
2 Selbstheilung (Pills: eine Dose 0.80, LIVE = MANIFEST), 3 Help up + sofort Treat, 4 Folgen ueber Zaun.
Konsole: 0 VERLUST, 9 TC-POOL-Leerungen (gewollt), keine Lua-Fehler.

**NEU 27.09. mittags:** v3.11.7 (Pause zaehlt nicht als Stillstand: Test = 2 min ESC, danach kein [TC-WATCH]) und
v3.11.8 (echter Fenstersprung, Ortsgedaechtnis statt Teleport; Test an Sherrifs Restaurantfenster 6345,5340 -> Zeilen
'Fenstersprung Schritt 1/2/angenommen/gelandet'). Gegenpruefung ueber v3.11.8 lief (Workflow wtsepqq1i) -- Ergebnis
einbauen, BEVOR Kevin das Fenster testet. Zaun = naechster Schritt (Kevins Wahl). Pillen-Test (b) laut Kevin bestanden
(Bag(2) zur Bestaetigung vorgeschlagen).

**NEU 27.09. 13:20:** v3.11.9 + v3.11.10 gebaut (Pruefer-Funde zum Fenstersprung, v3.11.10 = ernster Fund in meinem
v3.11.9: Kampf waehrend Schritt 1 sperrte das Fenster). Tod-Test MP gemacht: Respawn weit weg (10936,6645), Server nur
Vanilla-Fehler (MOWoodenWallFrame); 41 Fehler in der Testaccount-Konsole UNGELESEN (Classifier sperrt meine Kopie --
Kevin muss Zeilen zeigen). Sortierer-weiterarbeiten nach Respawn offen (er ist 4900 Kacheln weg). Zaun laeuft (springt).
13:40: MP-Tests DURCH -- Sortierer arbeitet nach Respawn weiter (Kevin), Zaun: springt. v3.11.11 = die 41 Fehler
(40x phantomSweep ohne Spieler beim Respawn, 1x MarkRemoved auf Leiche). AntiCheatPermission ZURUECK AUF 4 (Datei;
nach dem naechsten Serverstart pruefen, ob sie 4 bleibt). Testaccount-Rolle 14:25 per RCON wieder admin. Server laeuft v3.11.12, AntiCheat 4 bestaetigt.

**SP 27.09. nachmittags (v3.11.11/.12):** Fenstersprung 2x BESTANDEN, Pause ohne Teleport BESTANDEN, Foerster ohne
Spam BESTANDEN (Kevin). Zombie-im-Sprung ungetroffen (ungetestet gelassen). TREPPE FAELLT: Sortierer '2etage test' kommt
oben an, liefert ab, will runter zu 6345,5328,0, steht auf 6343,5321,1 ohne Hindernis, Teleport nach 20 s -- zweimal
reproduziert (Workflow stairs-down-stuck weevqrp2u). 'BLOCKED NEW X' ueber dem Kopf = Bandits ZAMove.lua:13.

**27.09. ~16:15 (v3.11.18, MP):** Kuechenfenster mit Theke BESTANDEN (Kevin: "mehrfach durch gesprungen ohne
probleme"; Log 2x 'UEBER DIE THEKE' -> 'gelandet', kein Teleport). NB: gemeldet 'gelandet auf 6166,5411' = der
Thekenkachel selbst, danach idle und weitergelaufen -- die Engine hat sie nicht auf 6167 gesetzt, schadet aber nicht.
Tueren offen im SP = Absicht (nur in Basisflaechen). PANIK MP BESTANDEN (Testaccount 0 Panik neben Crew, vorher
staendig; Server nahm 100/14/7 zurueck; echter Zombie -> Panik normal; Kevin: "sehr starker fix"). Tuer-Schliessen in
der Basiszone im MP BESTANDEN (Kevin: "das haben die echt grade gemacht"). Station unter Fenster BESTANDEN.
v3.11.18 OEFFENTLICH. NAECHSTE TESTS: v3.11.19 (Auto-Beschuss, keine Missing-arguments-Warnung) und der M16-TEST (MP: M16 in
Posteingang, Sortierer bringt sie in die Waffenkiste, dann Rechtsklick > Grab; Details offene_arbeit 'M16-TEST').
Danach Upload (stage -> Kevin -> park), Patchnotes `_docs/patchnotes_v3.11.18_plain.txt`.

**27.09. ~17:30:** v3.11.19/.20 (Auto-Beschuss, Missing arguments) und v3.11.21 FISCHKISTE (E5) gebaut, ungespielt.
Kevin: Sortierer nimmt aus der Fischkiste ALLES mit (nicht nur Fisch), nur in Reichweite. Tests a-k in offene_arbeit
(Block v3.11.21). Drei Pruefer liefen (Workflow wf_dcb20292-f87) -- Ergebnis einbauen, bevor Kevin testet.

**27.09. ~18:30:** v3.11.22 (Pruefer ueber .21: Lieferweg gibt auf statt Teleport, nur eigenes Lager, MP alle Arten in einem
Gang) und v3.11.23 (zwei Pruefer ueber .22: drei ernste Funde in MEINEN .22-Reparaturen -- Tuerwarten nur bei echter Anfrage,
Aufgabe-Zaehler am Plan und nur bei Stillstand, keine falsche Absage nach Sammellieferung; dazu crategone, weggeraeumter
Posteingang benannt) und v3.11.24 (zwei Pruefer ueber .23: Aufgabe-Zaehler misst wie der Waechter, Favoriten-Fisch ohne
Planschleife). Alle ungespielt. Fischkisten-Tests: a-k (.21), l-p (.22), q-u (.23), v-w (.24) in offene_arbeit.
Danach E7 (Reusen je Zone) -- Kevin wollte warten, bis die Pruefer durch sind.

**27.09. ~19:30:** v3.11.25 = E7 REUSEN gebaut (shared/BanditsNPCFishNet.lua, server/BanditsNPCFishNetServer.lua, Schalter je
Zone im Fishing-Reiter, Sandbox NetsPerZone/NetCheckHours), zwei Pruefrunden (3+2) eingearbeitet (u. a. toedlich im MP: Server
schrieb tcNetTS nicht). Dazu Pruefer ueber v3.11.24: Waechter gibt Fisch-Lieferung/Netz-Gang auf statt zu teleportieren. Ungespielt.
Tests N1-N10 in offene_arbeit. Offen fuer Kevin: Schalter 'Crew weicht nie zurueck' (Bandits-Ueberzahl-Flucht) -- nur angeboten.

**27.09. ~20:15:** v3.11.26 = E8 (Crew-Netze im Fischzonenbild, Netzstatus auf Crew-Karte/Survivor-Reiter) + Kevins
XP-Option SkillXPNeedMult 0.1..10 (Vorgabe 1.0; Gewinn gleich, Bedarf mal Faktor; gespeichert ungeteilt) + Pruefer-Korrekturen
(2 ueber E8, 2 ueber XP: kein Verlust/Teleport; veralteter Netz-Gang, Fangzahl, Scan aus dem Render, Spieler-Netze genannt,
Reset loescht Overrides). DAMIT IST DAS FISCHER-REWORK E1-E8 FERTIG. Kevin: "danach teste ich alles" -- Tests X1-X4 zusaetzlich.
Offen fuer Kevin: Schalter 'Crew weicht nie zurueck' (nur angeboten).
**27.09. ~20:45:** v3.11.27 = Koch-Geraeusch (AddItemInRecipe an der Kochstation, gedrosselt; Jar: kein Zombie-Anlocken, MP-Paket nur LoginOnServer). Test K1/K2.

**27.09. ~21:30:** v3.11.28-.35 (Netze-Schalter gruen/rot, kein Netzabstand + 20/40, Live-Restzeit, Netze AUS = einsammeln
+ heimbringen, Schmied-/Stations-Toene, Netz-Statistik, Farben) und v3.11.36/.37 (Netz-Ton, ALLE Netze der Zone gehoeren der
Crew ausser gueltig fremd markierten, Netze bis 4 Kacheln ins Wasser mit Stehkachel nur am Ufer, Vanilla-Netzaktionen gegen
weggeholte Netze gesichert, zwei Netze je Kachel). Pruefer liefen ueber alles (wkua03bxb), eingebaut. Ungespielt, Tests
in offene_arbeit (v3.11.28-.37, K1/K2).

**27.09. ~23:15:** v3.11.38-.44 gebaut, alle ungespielt. v3.11.44 = Neun-Agenten-Fischerpruefung umgesetzt (Netze nur fuer
freie Kacheln, kein Teleport bei Lagergang/Warteplatz/Ufer, Angeluhr bei Ablieferung aus, Netzalter in Weltstunden, Chum-Schalter
rot mit Grund, ES 'engodo') + Halfter-Pruefer-Funde. Tests v3.11.44 a-j in offene_arbeit. Drei Pruefer ueber v3.11.44 laufen
(Workflow wf_89ae61d5-127) -- Ergebnis einbauen, bevor Kevin testet. PFLICHTTEST MP bleibt v3.11.39 (Netz per Rechtsklick
kontrollieren, kein 'NetTimedAction rejected').

**27.09. ~23:50 (Kevin geht schlafen, PC aus):** v3.11.45 + v3.11.46 gebaut und gesichert (Pruefer-Funde ueber .44/.45:
Stehplatz je Ring, Teleport nach Stop im Reiter, eigene Lagermarke, wachsende Sperre, 07-Uhr-Fenster). Der EINE Pruefer ueber
v3.11.46 ist FERTIG (27.09. ~23:55): nichts Toedliches, ein ernster Vorbestand (Warteplatz-Gang nach Stop -> Teleport) +
drei kleine -- als v3.11.47 GEBAUT am 28.09. 12:12 (Pruefer w9umvcf5w lief danach), dann Kevin testen
lassen: Testliste _docs/testliste_2026-09-28.md (A = SP, B = MP).
Nebenbei am 27.09. erledigt: Spenden-Recherche (Antwort gegeben), Bandits-Abhaengigkeit (~40 %, Adapter-Datei angeboten,
Kevins Antwort offen), mod.info author=Agent X Top Secret (siehe [[kevin-steam-name]]).

**SP -- offen:**
- v3.11.5/.6 (ersetzt v3.11.4): vorher `TrueCompanions_Diag(2)`; Sortierer im Obergeschoss laufen lassen. Beweis = Abwesenheit:
  kein `[TC-WATCH] ... 6342,5320,1`. Hoechstens einmal `[TC-STAND] ... 6342,5320,1 ... Sackgasse`; NIE `keine andere Stehkachel
  -- die Sackgasse 6342,5320,1 bleibt`. Positiv: `TrueCompanions_WalkWhy(true)` -> `steh=6343,5321` (oder 6344,5321).
- v3.11.3: Fensterfall / Relax am Zaun mit wechselnden Zielen -> `[TC-CLIMBLOOP] ... aufgegeben` kommt, kein Pendel;
  Folgen: ueber Zaun hin und zurueck -> sie bleibt hoechstens kurz stehen.
- v3.11.2 (b): Pillendose, heilen lassen, SOFORT weit wegfahren und zurueck -> Dose 0.9, nicht 1.0.

**MP (Server + Testaccount) -- offen:**
5. Kick-Test: BESTANDEN 27.09. 12:50 (v3.11.8, AntiCheatPermission=2 von mir gesetzt -- Sicherung
   scratchpad/NPCCrewTest.ini.vor-kicktest; NACH den MP-Tests wieder auf 4!; Testaccount per RCON 'user'): kein Kick,
   Anwerben als user, SSOrtiertest lieferte 20 Schrauben + 5 + 4 Blech, nach Server-Neustart genau 20 + 9. Offen nur noch
   'Treat wounds' als user (Verband). Alter Text: Kevin stellt in NPCCrewTest.ini SELBST AntiCheatPermission=2 (danach zurueck auf 4), Testaccount ohne -debug,
   Rolle user; Sortierer sortiert, geben, Treat -> kein Kick, nach Server-Neustart nichts doppelt.
6.-8. BESTANDEN 27.09. (v3.11.8, Serverlog): Logout 12:56 geparkt, Login 12:58 Neubau an der Parkkachel; genau EINE
   Entnahme (item.txt 12:59:12 'container -20 Screws' am Intake 6070,5401) und EINE Ablage (12:59:43, 20 in 6073,5397) --
   der Griff fiel NACH den Relog, die Logout-Wartefrist (Griff < 3,5 s vor dem Klick) wurde also nicht getroffen. Test 7
   (Mitfahrt Mason, Neubau bei Rueckkehr) und Test 8 (Help up + Treat, laut Kevin) bestanden.
   ALTER TEXT: 6. Logout: Sortierer greift, sofort Hauptmenue-Exit -> Klickton, Ende nach <= 4 s, Stueck genau einmal da; auch Quit to desktop.
7. Wegfahren > 80 Kacheln waehrend der Sortierer arbeitet, zurueck -> nichts fehlt, nichts doppelt.
8. Help up mit Testaccount daneben -> bleibt stehen (v3.11.2 Rundruf mit keep); Help up + 0,5 s spaeter Treat -> 100 %.
- dazu v3.11.1 (d): sterben, im Todesbildschirm Exit -> wartet, keine doppelte Ware; v3.11.3: Exit, ESC, Respawn ->
  Sortierer arbeiten danach weiter.
- v3.11.3 (b): Sortierer ueber niedrigen Zaun zwischen zwei Kisten, 5 min -> kein "I can't reach that crate".

**Nebenbei gemerkt:** Kevins Spieler hatte am 27.09. Unsichtbar + Geist-Modus an (Aegis/Debug) -- deshalb griffen
gespawnte Zombies nicht an. Vor Kampf-/Biss-Tests abschalten.

**Why:** Kevin will erst testen, wenn die Pruefer durch sind; die Liste darf beim Neustart der Sitzung nicht fehlen.
**How to apply:** Beim naechsten Start zuerst das Workflow-Ergebnis holen (Journal unter
subagents/workflows/wf_f6c2c041-573), einbauen, dann diese Liste in dieser Reihenfolge anbieten. Details in
`_docs/offene_arbeit.md` (v3.11.0-v3.11.4). Siehe [[kevins-zwei-rote-linien]], [[both-modes-always]].
