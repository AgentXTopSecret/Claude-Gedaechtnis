---
name: stand-18-09-nachmittag
description: "Stand 04.10. 22:50 -- bis v3.12.54 gebaut; SP grossteils bestanden; MORGEN: Testliste 2026-10-05 (SP-Nachtests + MP), parallel v3.12.55 Boden-Eier/Federn + Clear-Fix, dann P5"
metadata: 
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-04T15:57:16.687Z
---
**05.10. KEVIN ENTSCHIEDEN (Eieruhr, ersetzt die Erst-Wartezeit vom 30.09.):** keine Vorgeschichte = sicher. Erste Messung ohne Hahn und ohne befruchtete Henne -> Uhr sofort bereit (h = Schwelle); erst ein GESEHENER Hahn/befruchtete Henne setzt auf 0 und die volle Brutzeit laeuft ab dann ("merkt sich wann zuletzt ein Hahn da war"). Grund: die ersten Eier verdarben in 21 Tagen Wartezeit (DaysFresh 14, Rotten 21). Rest benannt: ein Ei, das VOR dem Einrichten von einer befruchteten Henne gelegt wurde, kann in der Kiste schluepfen (Kevin: egal). Altbestand: Datensatz ohne je gesehenes Risiko -> beim Laden bereit, wenn jetzt kein Risiko (neues Feld noetig, um Hahn-Faelle zu trennen). Gebaut zusammen mit:
**05.10. KEVIN WILL (nach v3.12.56, eigene kleine Version):** Warnung bei der Eier-Option -- ohne All eggs wartet die Pflegerin die ganze Brutzeit ohne Hahn (Normal ~21 Tage, h=6/506), bis dahin bleiben alle Eier liegen. Plan: Werte UI_BN_Herd_R_EggsTip + R_AllEggsTip in 7 Sprachen deutlich (Tage aus Lv.EggThreshold, Hahn setzt zurueck, All eggs = sofort), dazu gelbe Zeile im Regelfenster unter Collect eggs mit Restzeit (Lv.EggGate-Zustand, wie EggGateWait im Animals-Reiter). Nicht parallel zu v56 (dieselben UI.json). P5 rueckt dann auf v3.12.58.

**05.10. ~13:10 v3.12.56 BAUT** (Workflow w8fmi0pu5, Tag v56-base, Plan _docs/plan_v3.12.56_regentonne.md inkl. PRUEFER-EINARBEITUNG): Wasserfass je Tierzone. Kevins 4 Antworten = alle Empfehlungen: 45 von der TIERZONE, Brunnen/Leitung nicht zuweisbar, Koch-Tonne erlaubt ohne Warnung, Testbefehl TrueCompanions_LvBarrelTest(true) ja. Server laeuft noch v3.12.54 -- Kevin NICHT neu verbinden lassen, bis Neustart (v3.12.55+.56 zusammen). MP-Tests 05.10.: M1 M4 M5 M6 M8 M10 bestanden, M2/M9 teil (Neustart-Check offen), M12 ausgelassen; Eier nur mit All eggs = Eieruhr h=6/506, so gebaut.

**05.10. abends E3/E4 + KEVIN-ENTSCHEIDUNG:** Pflegerin laeuft im Kreis (Quellen/Warteplaetze alle 5-7 s "kein Fortschritt in 8 Durchlaeufen" gesperrt, festgehangen nach Zaunsprung ClimbFenceEnd) + falsche Sperre bei fremder Hoheit. Diagnose w4dlhkazd. KEVIN: lieber TELEPORT zum Ziel als Stall/Ziel sperren, falls nicht sauber fixbar (Ausnahme zu seiner Teleport-Linie, nur fuer diesen Fall). A3 A4 bestanden (Wasser ueber Server an Becken/Klo, Angel+Werkzeuge sichtbar).

**05.10. abends TEST v3.12.59 MP:** A1 A2 A5 bestanden, Tuer nachts (settle->zu) bestanden. Befunde fuer die naechste Fixversion (_docs/testliste_2026-10-06.md Abschnitt E): E1 Regelfenster-Luecken (Platz nur wenn Text da), E2 KEVIN: Zone ohne Tiere KOMPLETT ignorieren (keine Arbeit jeder Art, bis Tiere drin sind); Status zeigt laufende Arbeit statt alten Grund; Haenger in bumped auf dem Weg zum Trog (~4 min).

**05.10. ~20:15 v3.12.59 FERTIG (P5 Stall/Nester/Tuer + Schrubb-Posen + Eier/Federn echt tragen + Lager-Hinweis):** Bau + 4 Pruefer (10 Funde, 9 behoben, 1 mit Jar-Beleg abgelehnt) + Check ok + REVIEW2 von mir (Test R2, Rest zwei Pflegerinnen je Kiste). NAECHSTE SITZUNG: _docs/testliste_2026-10-06.md (A = MP Pflicht A1-A8, B = SP Pflicht B1-B10, C beobachten, D Frage SP-Rest R8). Server ist aus; Spiel+Server neu starten auf v3.12.59. Danach Tierpfleger P6 (Mist/Wolle/Maehen) und P7 (Tierliste).

**05.10. ~18:20 v3.12.58 FERTIG** (Bau + Review 10 Funde + Fix2 6 Funde [ernst: MP-Flaschen Sprudel+Wasser wurde Dreckwasser -> W.MixedWater kennt trinkbare Mischungen, W.WaterOnly] + REVIEW3 von mir: Testtexte). UI.json 2271. OFFEN an Kevin: SP-Rest R8 (Becken haengt an der Zieltonne des Wassertraegers -> Kreislauf im SP) auch im SP schliessen? (Empfehlung ja, eine Zeile). v3.12.59 (P5) BAUT: w707gzwlk, Tag v59-base.

**05.10. P5-PLAN FINAL:** _docs/plan_v3.12.59_tierpfleger_p5_final.md (konsolidiert + Kritiker Q1-Q11 + KEVINS ANTWORTEN: Spieler-Eier auch zur Kiste, max 40, Kiste voll = behalten+warten). 43 neue Texte. Bau startet nach v3.12.58 (w6x4udtnm).

**05.10. ~16:15 v3.12.57 FERTIG** (Bau+Review 7 kleine Funde behoben+Check; REVIEW2 von mir: Tests S8/R1/M2 + 2 Kommentare -- JAR: befruchtete Eier schluepfen NIE in Kiste/Kuehlschrank/Companion-Tasche, Food.checkEggHatch 286-300; nur Nest, Boden, Spielerinventar). Kevin 05.10.: Tonnensperre NUR die gezeichnete Basisflaeche, die 45er-Reservierung um einen fremden Beacon zaehlt NICHT (so lassen). v3.12.58 BAUT (w6x4udtnm, Tag v58-base): Wasser ueber Server an Hahn/Brunnen fuer alle + Hand sichtbar.

**05.10. ~16:10 SERVER GESTOPPT (RCON save quit).** MP-Runde v3.12.55/.56 durch: T1-T6, T8, T10-T13 bestanden, T7 ausgelassen, T9 + W1 -> v3.12.58; alte Liste 03.10.: A1, C1 bestanden, C2 entfaellt. Naechster Test erst mit neuer Version (v3.12.57 baut, wzljcgtut) und weiter gebautem Keeper -- dann T14 (Relog/Neustart), A2 Basisgroesse 60, v3.12.57-Tests. Testaccount hat 5000 Woodwork-XP per RCON.

**05.10. REIHENFOLGE NEU:** v3.12.57 (baut, wzljcgtut) -> v3.12.58 = Wassertraeger-MP-Fix (_docs/plan_wassertraeger_mp.md, Kevin: fremde Basis sperren, alle Wasserholer mit) + Hand fuer alle sichtbar (_docs/plan_v3.12.58_hand_sichtbar.md, Empfehlungen gelten) -> v3.12.59 = P5 Ausmisten/Nester/Tuer + Animationen/Toene + Eier/Federn echt tragen (befruchtbar: direkt + Schaugang) + Lager-Hinweis (Plan _docs/plan_v3.12.57_tierpfleger_p5.md, alle Zusatzabschnitte am Ende). Tests 05.10. MP: T1-T6, T10-T12 bestanden, T7 ausgelassen, T9 Eimer unsichtbar (-> v58), W1 Wassertraeger-Schleife (-> v58).

**05.10. KEVIN: Eier/Federn ECHT TRAGEN** (statt direkt Kiste) -- in v3.12.58 mit P5; Boden ueber GroundTake (Foerster-Weg, seit v3.12.15/16 MP-sicher -- mein Einwand "Boden-Aufheben offen" war FALSCH, die Notiz mp-boden-aufheben-4221 ist ueberholt), Nest neuer Server-Weg Nest->Tasche, Abliefern G.Deliver/PutGoods. Plan-Abschnitt in plan_v3.12.57_tierpfleger_p5.md.

**05.10. ~15:00 MP-BEFUND (Kevin):** Eimer in der Hand der Pflegerin ist NUR fuer den NPC-Besitzer sichtbar (T9/M3 durchgefallen). Ursache vermutlich: W.EquipCan/Bandit.SetHands nur auf dem Besitzer-Client, der Cluster-Poll fremder Companions holt nur das Programm (v3.9.8). Vorschlag: Handgegenstand ueber den Cluster teilen (fuer Eimer, Rute, Mopp) -- in v3.12.58 mit dem Mopp. Frage an Kevin offen: sieht der Testaccount die Angel deines Fischers?

**05.10. ~15:00 STAND:** v3.12.56 gebaut + Review (1 Fund behoben: Mischung im Eimer -> Dreckwasser), zweite Fixrunde laeuft (w7ba4x2cj: Testschritt, Changelog, SP/MP gleiche Regel, Verlustalarm). v3.12.57-Plan fertig (_docs/plan_v3.12.57_eieruhr_kuehlschrank.md + KEVINS ANTWORTEN: F1 ja, F2 alle Gruende, F3 so lassen, NEU fremde-Basis-Sperre fuer die Tonne gehoert in v3.12.57). Server ist per RCON gestoppt; Neustart erst nach v3.12.56-Fix2 (v55+v56 zusammen laden).

**05.10. STREICHELN GEPRUEFT (w55tv3y1q, Jar 42.21):** Companion kann nicht streicheln (petAnimal/Acceptance nur IsoPlayer); Vertrauen je Spieler, sinkt nie; Streicheln -2..12 Stress, dann Minuten Sperre; Melken: Vertrauen egal (ISMilkAnimal.lua:23 = 120), nur Stress < 40 zaehlt; Scheren ab Vertrauen 20 kein Abbruch; Eier unberuehrt. Empfehlung an Kevin: NICHT bauen, Stressquellen fernhalten (Futter/Wasser < 0,8, Dach bei Regen, nicht schiessen/rennen/schlachten nahe Tieren). Antwort Kevins offen. Kuehe zerlegen Zaeune bei Hunger/Durst > 0,9 oder Angriff (IsoAnimal.animalShouldThump) -- Kevins Test 05.10. bestaetigt.

**05.10. JAR-FUND KUEHLSCHRANK (gelesen, nicht gespielt):** Food.updateTemperature setzt isFertilized=false, sobald heat < 0.5; ItemContainer.getTemperature gibt 0.2 fuer einen LAUFENDEN Kuehlschrank/Gefrierschrank, Food.heat naehert sich dem (min 0.2). Food.update ruft checkEggHatch auch fuer Eier in Kisten/am Boden (schluepfen nach timeToHatch ab Befruchtung). Also: Eier im laufenden Kuehlschrank schluepfen nie. KEVIN 05.10.: "ja bau das ein" -> in v3.12.57 (Plan-Workflow wc3rigzxq, _docs/plan_v3.12.57_eieruhr_kuehlschrank.md): ist die Eierkiste ein laufender Kuehlschrank, sammelt sie sofort alle Eier, auch ohne All eggs. Food.isFertilized am Ei hat 0 Lua-Belege (braucht Kevins Wort), NestBox.removeEgg(i) ist belegt (ISHutchGrabEgg.lua:21), addEgg nicht -> befruchtete Eier koennen nicht zurueck ins Nest.

**05.10. P5 AUSMISTEN = v3.12.58 (Plan _docs/plan_v3.12.57_tierpfleger_p5.md inkl. PRUEFER-EINARBEITUNG K1-K22; Dateiname bleibt .57):** Kevin hat alle Empfehlungen gewaehlt: nachts zu sobald alle drin (immer wieder), morgens einmal auf, ausgesperrtes Huhn nachts reinlassen wenn Platz (letin), Handschliessen tags bleibt bis Morgen; Werkzeuge Mopp/Besen/Reisigbesen/Schwamm/Klo-/Grillbuerste, NICHT Handtuch/Spueltuch, Mopp bleibt in der Tasche; Ausmisten+Nester per Vorgabe AN; morgens ohne Pflegerin bleiben Voegel drin -> im Hinweis sagen. Ohne Antwort = Empfehlung: Schwellen fest (Schmutz 15, 30 min Ruhe), Gegenprobe mit der Uhr ja. Reihenfolge: v3.12.56 Tonne (baut) -> v3.12.57 Eieruhr ohne Erst-Wartezeit + Warnung -> v3.12.58 P5.

**05.10. FUTTERSACK GEKLAERT (wgyave49u, Widerleger):** Kuehe fressen das ERSTE passende Stueck im Trog (canEatFromTrough-Schleife) -- in 6046,5401 lagen vorn 100 Heubueschel + 2 Grassaecke, der Sack an Platz 103; je Bissen ein Bueschel, Hunger steigt nur 0,0035/h. Sack also wirklich voll = Vanilla, kein Fehler. LATENT (Jar): im MP frisst nur der Server; Use() am Trog-Sack schickt kein Paket (syncItemFields deckt keinen Trog-Behaelter) -> Clients sehen 100 bis zum leeren Sandsack (sendReplaceItemInContainer); unsere Pflegerin liest FeedInfo auf dem Besitzer-Client -> fuellt dann erst nach, wenn der Sack leer ist. Kein Verlust/Kopie; Rest benennen, evtl. Server-Fuellstand spaeter. Offen: wer nahm um 12:41:20 (admin) einen Sack aus 6046,5401 (Item-Log) -- vermutlich Kevin von Hand.

**05.10. ~12:05 v3.12.55 FERTIG** (Boden-Eier/Federn, Federn-Schalter Vorgabe an, Name produce crate, ParkedSupply, Clear-Fix;
Pruefer: nur minor, behoben). MP-Tests auf v3.12.54 laufen (Testaccount Rolle user seit 11:30): M1, M6, M8 bestanden; M2 Futter
ueber Server laut Log ok. OFFENE FRAGE an Kevin: Pflegerin soll Regentonnen als Wasserquelle nehmen (heute nur endlose Quellen
W.IsEndless, Regentonnen bewusst aus)? Empfehlung: nur als Rueckfall, nur Tonnen, die NICHT Ziel des Wassertraegers sind.
Testliste N1-N8 fuer v3.12.55 in testliste_2026-10-05.md; dafuer Server (rcon save quit + bat) UND beide Spiele neu.
**KEVIN 05.10. ENTSCHIEDEN (Regentonne):** je Tierzone eine zuweisbare Wassertonne (Animals-Reiter, Zeile "Water barrel:
[Assign] [Clear]", Zeiger wie Eierkiste), mit schoenem Hinweistext am Zuweis-Knopf. REIHENFOLGE: ERST endlose Quellen (See/Hahn wie
heute), DANACH die zugewiesene Tonne als Rueckfall; leer -> warten + Spruch. Dreckwasser ok. Wassertraeger darf dieselbe Tonne fuellen.
MP ueber WaterMove.RequestTake (Server, wie der Koch). -> v3.12.56 (Plan zuerst, Bau nach dem v3.12.55-Neustart).
**05.10. ~11:05 v3.12.55 BAUT** (wf_13314da9-540 / Task wovj7cth2, Tag v55-base, Skript scratchpad/keeper_v55.js): Boden-Eier/Federn nach
plan_v3.12.53_tierpfleger_p4c.md + Clear-Fix; offene Fragen mit Empfehlungen (Federn AN, produce crate, Verdorbenes ja, Brutzone=Collect
eggs aus, P13 benennen). Kevin testet MP M1-M12 auf v3.12.54 (Server + beide Clients geladen VOR dem Bau) -- NICHT neu verbinden.
S1-S4 SP-Nachtests nach dem Bau.
**05.10.2026 ~10:55 SITZUNGSBEGINN:** Bandits-Update seit 03.10. (3 Dateien): neues brain.permaInv (Bandit.lua UpdateItemsToSpawnAtDeath,
Spawner) -- unsere Brains haben es nicht, keine Wirkung; Body-Location "Satchel" neu in GetBodyLocationsOrdered (unsere Interact-Schleifen
nehmen sie mit -> getragene Umhaengetasche wird jetzt gezeichnet; kein Gear-Kasten dafuer, faellt unter "Also worn"). Verbrauch: Woche 54 %.
**04.10.2026 ~22:50 PAUSE BIS MORGEN (Kevin). v3.12.54 FERTIG** (Show zone eigene Rechtecke nur gewaehlte Zone, Taste KP_7
Vanilla alle; Eierkisten-Antwort im Eier-Block 30 s; Abstand N/45 am Zeiger; LootLow + GrabEggs; 2220 Schluessel; Pruefer nur
minor, behoben). MORGEN ZUERST: Kevin testet nach _docs/testliste_2026-10-05.md (S1-S4 Einzelspieler-Nachtests, dann M1-M12
Mehrspieler -- Testserver vorher starten, bugwatch mit; waehrend MP-Test KEIN Neuverbinden ohne Kevins/mein Okay, sonst
Pruefsummen-Kick). PARALLEL bauen: v3.12.55 = Eier+Federn vom Boden nach _docs/plan_v3.12.53_tierpfleger_p4c.md (Datei heisst
noch .53, inkl. PRUEFER-EINARBEITUNG P1-P15) + Clear-Knopf-Fix (DialogWindow.lua:1666 workstation ~= nil -> Wahrheitswert);
Tag v55-base vorher, brfc.js oder eigener Workflow mit 2 Bauern. Offene Fragen (ohne Antwort Empfehlung): Federn-Schalter AN,
Name produce crate, Verdorbenes einsammeln, Brutzone = Collect eggs aus. DANACH P5 (Stall ausmisten, Nester, Stalltuer, Plan
_docs/tierpfleger_bauplan_stufe1.md Abschnitt P5), dann P6/P7, dann Koch-Rezepte fuer Tierprodukte [[moegliche-features]].
Kevin mag das Zaunspringen der Pfleger (nicht aendern). Eier gehen direkt Nest->Kiste (Kevin ok, Grund MP-Tasche).
**04.10. ~22:20 Kevin-Meldung Job-Reiter:** Clear (Werkbank) bleibt sichtbar und 'tut nichts'. Ursache: ClearWorkstation setzt
lokal nil, synct workstation=false -- im SP dieselbe Tabelle, also steht false; DialogWindow.lua:1666 zeigt Clear bei
`workstation ~= nil` (false ~= nil). Fix klein (Wahrheitswert statt ~= nil) -> naechste kleine Version NACH v3.12.54.
Kevin gefragt: Sortiererin mit Beruf Builder zeigt roten Werkbank-Banner + Block im Production-Overview (Rezeptziele Cut
Planks usw.) -- ERLEDIGT: Kevin hat die Ziele geloescht, Block weg (gewollt seit v3.5.0). Bleibt NUR der Clear-Knopf-Fix.
**04.10. ~22:05 v3.12.53 FERTIG (Tor-Fix):** Ursache = Vanilla LOG GATE hat nur 2 Fluegel (N 1+2, W 3+4), mein v3.12.51-Code
verlangte Fluegel 4 + and/or-Falle im Beobachter (doubleGeom nil -> singleGeom). Jetzt Saetze 1-4/1+2/3+4, vergessen nur bei
nachweislich zu/weg. Offen (Bandits, fremd): Klettern ueber hoppable Log-Gate-Fluegel -> bumped/Teleport. v3.12.54 BAUT
(wf_066dcaf5-865 / Task wur6q6kf1, Tag v54-base): Show zone eigene Zeichnung, Eierkisten-Absage sichtbar, Abstand X/45,
GrabEggs-Ton + LootLow. Kevin NICHT neu starten lassen bis .54 fertig. Danach Neustart: G6, H1/H2, I3 nachtesten.
**04.10. ~21:15 G5 bestanden. G6 FEHLER: Show zone zeigt alle Tierzonen** -- Engine (FBORenderAreaHighlights.renderAnimalDesigationZones)
zeichnet bei setSeeDesignationZone(true) JEDE Zone, die gewaehlte nur tuerkis statt blau. Fix NACH dem Tor-Fix: Knopf zeichnet
die Gruppe selbst (Z.DrawRect-Form), Taste KP_7 bleibt Vanilla (alle). KEVIN 04.10. "ja mach das": Knopf nur gewaehlte Zone (eigene Zeichnung), Taste KP_7 zeigt weiter alle. Reihenfolge: v3.12.53 Tor-Fix (laeuft) -> v3.12.54 Show zone -> v3.12.55 Boden-Eier/Federn. v3.12.54 AUCH: Eierkisten-Absage unsichtbar (Fenster geht nach Kistenwahl auf und verdeckt den Spruch; Notiz rechts unten 6 s, gekuerzt) -> Absage im Eier-Block, laenger, umgebrochen; dazu Abstandsanzeige X / 45 am Zeiger (wie Fischzone). UND Eier-Ton: Vanilla ISHutchGrabEgg spielt "GrabEggs" (character:playSound, Loot-Pose LootPosition Low) -- beim Nest-Schritt der Pflegerin abspielen (Form pourSound in LivestockJob, WORK_SOUND_DIST, nie auf dem Server; Kevin 04.10. "ja waer cool").
**04.10.2026 ~21:00 KEVIN TESTET SP auf v3.12.52:** G1-G4 bestanden (Log bestaetigt). FEHLER: Doppeltore an der Tierzone, von
Dylan (Folgen) geoeffnet, bleiben OFFEN (TC-GATE 'Fluegel 1 nicht gefunden' + 'kein Tor mehr auf der Kachel -- vergessen', 5x).
-> v3.12.53 = Tor-Fix (wf_aa3880df-f2a / Task w5j449a0h, Tag v53-base). Boden-Eier/Federn werden v3.12.54 (Plan-Datei heisst
trotzdem plan_v3.12.53_tierpfleger_p4c.md). H2 erst nach v3.12.53 testen.
**04.10.2026 ~20:10 v3.12.52 FERTIG** (Ertragskiste je Basis site.storage.yieldCrate, Aufloeser Lv.EggCrate, Eier-Block im
Animals-Reiter, Schalter eggs/allEggs im Regelfenster; 9 Pruefer-Funde alle minor, behoben; Nachpruefung: KO-Artnamen von mir
nachgebessert, Rest Handwerks-Slot-Kiste benannt; 2219 Schluessel). v3.12.53 PLAN laeuft (wf_94d3231a-6ce / Task wnfqy90ti,
nur lesend -> _docs/plan_v3.12.53_tierpfleger_p4c.md). KEVIN ZUGESAGT: Bau von v3.12.53 erst, wenn er 'bin drin' sagt (dann
laeuft das Spiel schon) ODER 'bau weiter' (er testet nicht). Offene Frage an Kevin: Federn-Schalter Vorgabe AN? Vor dem Bau
Tag v53-base setzen, brfc.js nutzen.
**04.10.2026 ~17:50 v3.12.51 FERTIG** (Tore: Tierzonen-Tor spaetestens 5 s nach Oeffnen zu, nur die Pflegerin selbst auf der
Torkachel schiebt auf; Doppeltueren ueberall per toggleDoubleDoor; Futterfenster-Ursache = and/or-Falle in Lv.FeedRuleOf
(false -> nil), behoben; Holzplatz-Add-Text). Rest: Changelog-Ueberschrift verspricht noch 'auch mit Spieler daneben' (minor).
v3.12.52 BAUT (~17:55, wf_e3184369-bc3 / Task wzfxfmskp, Tag v52-base; Plan wird nach _docs/plan_v3.12.52_tierpfleger_p4b.md
geschrieben). DANACH v3.12.53 Boden (Eier/Federn vom Boden, Federn-Schalter) mit scratchpad/brfc.js + vorherigem Plan-Refresh,
dann Kevin eine Gesamt-Testliste (G + .51-.53 + MP-Block M) geben und Testserver neu starten.
**04.10.2026 ~17:35 KEVIN SPIELT ANDERES SPIEL -- ICH BAUE DURCH, ER TESTET SPAETER ALLES AUF EINMAL.** v3.12.50 FERTIG (1 ernster
Fund behoben). Testserver per RCON gespeichert + beendet (vor dem MP-Test wieder starten: NPCCrew-Testserver.bat). Generisches
Workflow-Skript scratchpad/brfc.js (args version/base/plan/task/lenses). v3.12.51 BAUT (wf_0ac6749d-61b / Task w89uu5rrl, Tag
v51-base): Tore, Futterfenster-Bug, Holzplatz-Add-Text, v50-Reste. DANACH: v3.12.52 = P4 Teil 2 (Ertragskiste PRO BASIS, Eier-UI,
Federn eigener Schalter) -- vorher Plan-Refresh gegen Stand nach .51; dann v3.12.53 = Boden (Eier/Federn). Testliste fuer Kevin:
_docs/testliste_2026-10-04.md (Block G = v3.12.49/.50, dann .51-.53 ergaenzen + MP-Block M).
**04.10.2026 ~14:50 SORTIERER 2x SCHNELL GEFUNDEN (Trace gemessen):** schnell = Engine-PathFindState + Bandits-Move gleichzeitig
(Doppel-Update, ~4 statt ~2 Kacheln/s), nur die 3 Sortierer im Stau am Posteingang. Kevin: 'in ordnung, aber bitte fehlerfrei'.
-> v3.12.50 = Sortierer-Fix (Doppeltempo + Stau: volle Kiste meiden, nicht aufnehmen ohne Ziel, eigene Stehkacheln, Loot-Pose
haengt) NACH v3.12.49; Plan laeuft (wf_cd5b10ca-889 / Task wxlycw7o8, nur lesend, scratchpad/plan_v3.12.50_sortierer.md).
P4-Teile verschieben sich: Ertragskiste+UI -> v3.12.51, Boden -> v3.12.52.
~17:50 REIHENFOLGE: v3.12.50 (laeuft) -> .51 Tore/Futterfenster/Holzplatz-Text -> .52 P4 Ertragskiste+Eier-UI -> .53 Boden.
Kevin zu P4 Teil 2/3 (unten im _docs/plan_v3.12.49_tierpfleger_p4.md): Ertragskiste PRO BASIS; Federn GETRENNTER Schalter;
Kueken-Rest so lassen. Kein Parallelbau (gleiche Dateien).
~17:40 TOR-PLAN FERTIG: _docs/plan_v3.12.51_tore.md (Ursache: Bandits' ManageCollisions oeffnet; Doppeltor nie gemerkt ODER
Einzeltor wartet ewig auf den Spieler; Fall war auf Stufe 2 stumm). KEVINS ENTSCHEIDUNGEN unten im Plan: sofort zu (auch mit Spieler
daneben) NUR Tore an Tierzonen; Doppeltueren/-tore ueberall jetzt auch schliessen (toggleDoubleDoor, normale Spieler-Warte-Regel);
nur was UNSERE oeffnen; keine Stufe 2/Option C. v3.12.51 = Tore + Futterfenster-Bug + Holzplatz-Add-Text -- BAUEN, SOBALD v3.12.50 FERTIG.
~17:20 MIT IN v3.12.51 AUCH: FUTTERFENSTER-BUG (Kevin SP, Bild): nach 'Ban all' ({@feed,@grass,@sheaf}=false, console f:1156 done)
zeigen die Gruppenkoepfe 'Allowed', alle Arten 'Banned' (0 of 58); Klick auf Heu pusht nur 'HayTuft = nil' (11x, f:1946-2083) ->
FW:onToggle haelt groupOn(grass) fuer true, FeedAllowed sagt false. Ursache beim Lesen NICHT gefunden (groupOn/FeedRuleOf/
FeedAllowed/Lv.Rule sehen gleich aus) -- Agent mit Beleg. Workaround an Kevin: 'Default'. client/ISUI/BanditsNPCLivestockFeedWindow.lua.
~17:00 MIT IN v3.12.51 (Tore): Holzplatz-Zeiger im ADD-Modus zeigt 'middle: X / 60' der Mitte des GANZEN Platzes (alt+neu),
waehrend daneben '1 x 1 tiles' steht -- Kevin verwirrt (Fischzone 48 vs Holzplatz 20 am selben Feld). Text im Add-Modus klarer
('middle of the whole yard: X / 60'), 7 Sprachen. ForestCursor.lua yardReach/self.extend ~212-232, ~319.
~16:30: Sortierer-Plan fertig (_docs/plan_v3.12.50_sortierer.md), v3.12.50 BAUT (wf_d4bae6da-a1a / Task wrju5ed1k, Tag v50-base:
Einzel-Fahrer, Stau 2a-2d, Show zone bleibt an, EggProbe). Tor-Plan laeuft noch -> danach v3.12.51 (Tore). Kevin testet SP v3.12.48:
A1-A6, B1-B3 bestanden, C uebersprungen (Kevin: auf Bugreports warten). Workshop-Meldung 'keine Moebel platzierbar' = fremde Mod
(wir greifen nur Aufheben/Zerlegen/Drehen von Beacons an), Antwort an Kevin gegeben.
v3.12.49 FERTIG (~15:20, Pruefer gruen, 5 Kleinigkeiten behoben; Rest: EggProbe zeigt den Live-Check nicht -> in .50 mitnehmen).
TOR-BUG (Kevin ~15:25, ROTE LINIE 'Tiere weg'): Pflegerin liess das Tor der Tierzone offen. Vermutung: Doors.lua closable() lehnt
Doppeltueren/-tore ab (alter Einfrier-Bug), keine [TC-DOOR]-Zeile. Kevin: Tor muss SOFORT zu, auch wenn er daneben steht. Plan
laeuft (wf_77f551dd-8be / Task w7kneaygm, scratchpad/plan_gates.md). Bau zusammen mit dem Sortierer-Plan als v3.12.50/.51.
ZUSATZ fuer v3.12.50 (Kevin ~15:10): Animals-Reiter 'Show zone' (LivestockPanel hlOn/hlOff Besitzer "tab", geht bei Reiterwechsel
:2120 / Fenster zu :2147 / Gruppe weg :752 aus) soll wie Trog-Show DAUERHAFT an bleiben bis Hide (gemeldet: 'geht direkt aus').
**04.10.2026 ~14:10:** v3.12.48 fertig (Fix+Check gruen), Kevin testet SP (A1-A3 bestanden, testliste_2026-10-04.md). P4-Plan
fertig (_docs/plan_v3.12.49_tierpfleger_p4.md, 3 Versionen: .49 Nest-Logik, .50 Ertragskiste+UI, .51 Boden). v3.12.49 BAUT
(Workflow wf_55430a82-152 / Task wriy50ghr, Basis-Tag v49-base; Variante B = Art zaehlt ab erster Sichtung, 21 Tage). VOR .50
Kevin fragen: Ertragskiste je Basis? Federn am selben Schalter? Kueken-Rest (S8)? Parallel: Untersuchung 'Sortierer laufen 2x
schnell + drehen sich im Kreis' (Workflow wf_0a6dcd37-4f9 / Task wts74kebs, nur lesend). Server laeuft v3.12.48.
**04.10.2026 ~12:20 KEVIN:** sobald v3.12.48 (Fix + Check) durch ist: Testliste geben, Kevin startet Spiel + Server neu und testet,
und ICH MACHE SOFORT MIT DEM NAECHSTEN TIERPFLEGER-PUNKT WEITER = P4 (Eier, Federn, Eieruhr, Ertragskiste; Bauplan
_docs/tierpfleger_bauplan_stufe1.md Abschnitt P4, alle Kevin-Entscheidungen dort Abschnitt 6 schon gefallen). Form: Plan gegen
den heutigen Code nachziehen -> Bau -> 4 Pruefer -> Fix -> Check (<= 10 Agenten). Kevin sagen: waehrend P4 gebaut wird NICHT neu
starten (laufendes Spiel bleibt auf v3.12.48, Lua laedt nur beim Start).
**04.10.2026 ~09:40:** v3.12.48 nach Plan gestartet (Workflow wf_66309f80-9c0 / Task wj8ailapt: Bauer, 4 Pruefer, Fix, Check; Basis-Tag v48-base). Danach: Kevin Spiel + Server (RCON) neu, bugwatch-Monitor, Testliste v3.12.41-.48 aus offene_arbeit zusammenstellen (testliste_2026-10-03.md erweitern/neu).
**03.10.2026 23:45 ALLES DURCH, PAUSE:** v3.12.47 (Fischzone 75 Kacheln Chebyshev, Holzplatz-Mitte 60, Client+Server-Tor) gebaut + geprueft (4 Kleinigkeiten behoben, ein kleiner Text-Rest steht als Nachtrag im Plan v3.12.48). Nichts laeuft mehr. Stand der Platte = v3.12.47, alles UNGESPIELT, nichts hochgeladen seit v3.12.19.
**03.10.2026 ~23:30 KEVIN: HEUTE NICHTS NEUES MEHR STARTEN.** Der Fischzonen/Holzplatz-Workflow (v3.12.47, wf_d55f5324-98d) und der v3.12.48-Planer duerfen fertig laufen, danach Pause. MORGEN (04.10.) ZUERST: Ergebnis v3.12.47 lesen (falls nicht schon gemeldet), Plan v3.12.48 aus `_docs/plan_v3.12.48_tierpfleger.md` bauen (Eimer beim Laufen, Tierblock nur wenn machbar + Spruch, Remove = alle ausser dieser, Show bleibt an bis Hide) mit Pruefern; dann Kevin Spiel+Server neu starten lassen und Testliste geben (v3.12.41-.48, Tests oben in offene_arbeit). Offen: Statistik-Tool Sterne + Bewertungsanzahl einbauen? (Kevin hat nicht geantwortet.)

**03.10.2026 ~20:30 ENTSCHEIDUNGEN:** (1) Workshop-Meldung 'Crew stirbt trotz Protect/Immortal' (Workflow wf_1fd3aee0-f12, Ergebnis im tasks/wuz2h23xq.output): Spieler-SCHUSS laeuft durch Bandits' OnHitZombie (BanditUpdate.lua:2349-2390) VOR unserem Schild, Kopf = Kill(nil); KEVIN: 'Voller Schutz' = Einmal-Riegel auf die globale instanceof im CheckFriendlyFire-Aufsatz (Compat.lua ~116), nur bei Fernwaffe, Entschaerfen zuoberst in HitShield onWeaponHitCharacter + OnTick-Netz. Dazu: Die/Zombify-Streifen auch auf Nicht-Besitzer-Clients (Guardian ~2982), UI_BN_Opt_Protect falsch beschriftet ('Zombies prefer the player'), Override-Markierung/Reset im Settings-Reiter, Tooltip ehrlich (Feuer/Fahrzeug). Antwort an den Melder hat Kevin bekommen. (2) Saecke + Restfutter zurueck ins Lager: KEVIN 'Ja, beides' (bestaetigt). (2b) Workshop-Meldung Fischzone zu weit (Kevin 'er hat recht'): Cursor prueft fuer kind fish keine Entfernung, Fischer scheitert am Ladefenster (Zone + Lagerkisten gleichzeitig) -> NACH dem Workflow post-p3-build bauen: Fischzone wie Basisflaeche (Live-Zeile X/75 vom Beacon, Absage, Server-Tor fuer neue Stuecke, Hinweis fuer alte zu weite Zonen); KEVIN 'ja nehm den mit': Holzplatz ebenso (Sortierer nutzt nur Mitte <= 60, H.YARD_RADIUS, Haul.lua ~1040). Befund des Lesers: ForestCursor.lua:233-245 ohne Pruefung, Interact.lua:4018+. (2c) v3.12.43-.46 gebaut+geprueft (nur 3 Kleinigkeiten, behoben). KEVINS ANTWORTEN auf die Bauer-Fragen (03.10. ~23:00) -> als v3.12.48 NACH dem Fischzonen-Workflow (v3.12.47) bauen: Eimer AUCH BEIM LAUFEN mit Wasser sichtbar (Schuetzen-Regel bleibt); Neutrale NICHT vor Schuessen schuetzen (so lassen); Tierblock: starten, wenn die Arbeit wirklich gemacht werden kann, sonst NICHT starten und den Grund als Spruch ueber dem Kopf (einmal je Aenderung, kein Spam); Remove einer Zone bei 'alle Tierzonen' = 'alle ausser dieser' (Ausschlussliste, neue Zonen kommen weiter dazu); Trog-SHOW (Kevin 03.10., gesehen: Fenster schliessen schaltet aus, Beacon verdeckt die Sicht) -> Show bleibt an, bis Hide gedrueckt wird, auch bei geschlossenem Fenster (Hover bleibt kurz). Nicht gefragt, so gelassen: Weide nur mit Jungtieren bekommt erlaubtes Futter; frueher als Posteingang zugewiesener Trog bleibt bis Neusetzen; nach Laden bleibt Geholtes bei ihr; Trog-Ansprueche zweier Besitzer im MP unabgestimmt. (3) Bandits still aktualisiert (virtuelle Banditen, noch ungenutzt), Sicherung 2026-10-03_2001.

**03.10.2026 00:15 P3 GEBAUT, PRUEFUNG OFFEN:** v3.12.41 (Logik) + v3.12.42 (UI) liegen auf der Platte und sind gesichert; Workflow auf Kevins Wunsch VOR den Pruefern angehalten. Ergebnisse beider Bauagenten in `_docs/tierpfleger_p3_build_ergebnis.json` (Zusammenfassung, offene Fragen). MORGEN ZUERST: drei Pruefer (mp-items, sp-logic, ui-langs) + Nachbesserung ueber den Diff ab dem Commit vor dem Titel v3.12.41 (Linsen wie im Script keeper-p3 der Sitzung c3f66696). Offene Kevin-Fragen aus dem Bau: Ausschuetten nur mit Spieler <= 6 Kacheln am Trog; Regen fuellt den geleerten Trog vor dem ersten Futter wieder; leere Saecke im Trog zurueck ins Lager?; uebriges Futter in der Tasche zurueckbringen?; Gruppe Other food einklappen?; Basisvorgabe fuer die Futterliste? KEVIN 03.10. ~00:20 auf die vier Fragen (6-Kachel-Naehe, Regen, leere Saecke zurueck, Restfutter zurueck): "ja klingt gut" -- als Ja zu allen vier gelesen; vor dem Bau von Saecke/Restfutter-zurueck kurz bestaetigen lassen.

**03.10.2026 TESTLISTE:** `_docs/testliste_2026-10-03.md` -- erst P3-Ergebnis lesen, dann die Fix-Liste unten (a-e + Knoepfe/Show) bauen, dann Server+Spiel neu, dann testen.

**02.10.2026 23:15 NACH P3 ZUERST FIXEN (Kevins SP-Test P2, Bild):** Im Animals-Reiter stehen die Trog-Rollenknoepfe Feed/Water/None am RECHTEN FENSTERRAND (4K-Fenster ~1900 px breit), weit weg von den Trogzeilen -- Kevin hat sie nicht gesehen. Sie gehoeren direkt hinter die Textspalte wie der Remove-Knopf der Pfleger (feste Spaltenbreite, Lehre v3.10.46 'Stop hinter der Textspalte'). Erst nach dem P3-Workflow (schreibt gerade LivestockPanel.lua). DAZU (Kevin 23:20): Trogzeilen zeigen nur Koordinaten -- ein normaler Spieler sieht keine Koordinaten; je Trog ein Knopf 'Show' (Trog leuchtet in der Welt, wie die Kachel-Hervorhebung beim Hover in der Lager-Zeile v3.12.28) und Hover ueber die Zeile hebt ihn auch hervor; KEVIN ENTSCHIEDEN: Koordinaten in den Trogzeilen GANZ RAUS ('Trough 1', 'Trough 2' bleiben), dafuer je Trog ein Umschaltknopf Show/Hide (Hervorhebung an/aus).
**DANACH (Kevin 23:30, 'ja sollst du ... sonst braucht man zich arbeiter'):** (a) Schichtplan-Block 'Tiere' wie der Fisch-Block -- die Zonen bleiben eine Einstellung aus dem Animals-Reiter (brain.livestock wie fishSite), der Block sagt nur WANN; (b) Zuweisung 'Alle Tierzonen dieser Basis' (auch spaeter neu angelegte), mehrere Pfleger teilen ueber die vorhandenen Trog-Ansprueche.
(c) (Kevin 23:35, P2 im SP bestanden: Pflegerin fuellt den Wassertrog) EIMER IN DER HAND beim Tragen/Giessen -- P2 hat W.EquipCan absichtlich weggelassen (Guardian-Tore 1797/1899 + tcWaterStash haengen an NPCWater/NPCBoil). Weg: Anzeige-Phantom NPCCrew.BucketHand ueber das WorkTool-Muster (Modultabelle, kein Gehirn-Stash, Schuetzen-Regel bleibt) oder die Tore um NPCLivestock erweitern -- Pruefer! Kevin 23:40: 'zumindest wenn er was reinschuettet' + TON: Vanilla hat eigens 'AnimalFeederAddWater' fuer Troege (ISAddFluidFromItemAction.lua:62, sonst PourWaterIntoObject :64) -- beim Giessen spielen, wie bei ihm ueber den Charakter-Emitter; nur hoerbar in der Naehe wie unsere anderen Arbeitstoene.
(d) BUG P2 (Kevin 23:40, Regel 'unter 50 %' -> sie fuellte bei angezeigten 50 %): Lv.WaterState (Livestock.lua ~2147-2152) vergleicht streng pct < low, die Anzeige rundet ab (math.floor, Panel ~362) -- also lag es NICHT an der Grenze, sondern am Nachfuell-Fenster Lv._refill (10 min): es wird nach dem Auffuellen auf waterHigh nicht geloescht ('full' raeumt es nicht), also fuellt sie 10 min lang jede Abweichung unter 100 % nach und ignoriert waterLow. Fix: Lv._refill[key] loeschen, sobald pct >= high (und am Ende des Gangs); gleiche Stelle fuer Futter (P3) pruefen. IM SPIEL BESTAETIGT (Kevin 23:55): nach etwas Warten fuellte sie bei 50 % NICHT mehr auf -- es ist das 10-min-Fenster.
(e) ANZEIGE (Kevin 23:50, Bild): Eimer mit Wasser zeigt im NPC-Fenster (beide Listen) immer Gewicht 1.0 -- client/ISUI/BanditsNPCItemList.lua:486-488 nimmt getWeight() (Leergewicht); Vanilla zeigt getUnequippedWeight() (ISInventoryPane.lua:569/612/1431, Lua-belegt). Kopfzeile 10.0/8.0 rechnet schon richtig. Fix: Zeilengewicht ueber getUnequippedWeight (mit Existenz-Riegel), Stapelsumme ebenso; Sortierung :404 pruefen.

**02.10.2026 vormittags:** v3.12.27 GEBAUT (MP: Neubau, der zweimal nicht ankommt, wird vom Server ersetzt statt 3 min zu warten; 3 Pruefer, nichts Schweres; UNGESPIELT, Test in offene_arbeit oben), gespiegelt, nicht hochgeladen. Ab 15:00 IN DIESER REIHENFOLGE: (1) Lager-Reiter-Zeile fehlende Zutatenkiste (7 Sprachen); (2) [[leerer-chum]]; (3) [[verdrehte-stationen]] -- WAR SCHON ERLEDIGT (v3.12.20); (4) Tierpfleger Stufe 1 nach _docs/tierpfleger_bauplan_stufe1.md. Kevins Feature-Reihenfolge danach: FARMER (Pflanzen pflegen/anpflanzen, B1-Beete-Test wartet darauf), DANN LEICHEN-JOB (Zone auch ausserhalb des Beacons ueber den NPC, alle Folgenden arbeiten mit, falsches Feuer ohne IsoFire, Beute-Entscheidung offen). Vor Upload: KeeperEnabled nur-debug, Patchnotes.

**01.10.2026 abends (Kevin bei 98 % Wochenlimit, Reset 02.10. 15:00):** v3.12.20-v3.12.26 gebaut (Essens-Tooltip, Tierpfleger-P0-Sonden, Konsole leise, Seitenleisten-Knoepfe, Sprechtext 100-300 %, dessen Fix), NICHTS hochgeladen seit v3.12.19, Ordner geparkt. Testliste _docs/testliste_2026-09-30.md: SP komplett bestanden (D, E1/E2, F, G, H), MP bestanden E3, G6, A8a; offen B1 (spaeter), C7c (Chum-Bug), A8b uebersprungen. Am 02.10. ab 15:00 IN DIESER REIHENFOLGE: (1) OFFENER BUG MP-Neubau nach dem Aussteigen -- Client erkennt den servergebauten Koerper nicht, 3 min bis das Kopien-Netz ihn entfernt und neu baut (Einzelheiten oben in _docs/offene_arbeit.md); (2) Lager-Reiter-Zeile fuer fehlende Zutatenkiste (Kevins Ja); (3) [[leerer-chum]]; (4) Tierpfleger Stufe 1 nach Bauplan (Trog-Entscheidung steht drin). Patchnotes fuer den naechsten Upload noch nicht geschrieben.

**30.09.2026 22:48:** v3.12.19 oeffentlich (Steam 11,8 MB, 3951 Abos), Ordner geparkt. Offen in dieser Reihenfolge: [[verdrehte-stationen]], [[leerer-chum]], Name/Zutatenliste im Manifest (Kevins Ja fuer den Setter nach Jar-Pruefung), Frische-Tooltip, Komposter-Auftrag ([[moegliche-features]]).


Stand 29.09.2026 21:40: v3.12.13 ist OEFFENTLICH (Kevin hat hochgeladen, Steam 21:39, 11,3 MB), Upload-Ordner wieder geparkt,
  Testserver per RCON sauber beendet. Heute gebaut: v3.12.5-.13 (zerstoerte Kisten + Knopf ueber den Server, Tueren/Fenster
  ueberall mit Spieler-Warten, Fernseher geht aus, Builder-Hammerton, Pruefer-Fixes). Bestanden: SP Tests 1-3, Fernseher,
  Posteingang zerschlagen; MP Kisten/Tueren/Fernseher. Nicht gespielt: v3.12.11-.13-Kleinteile (schlafender Spieler an der Tuer,
  Fernseher nach Essenspause, abgeschlossene Haustuer auf+zu, selbstgebaute Tuer behaelt Schloss). Excavation-Fehler beim
  Vorschlaghammer: fremd, Kevin will keine lokale Reparatur.
Stand 29.09.2026 17:50: v3.11.95 (Abgabe-Riegel), v3.11.96+.98 (PROJECT RV Interior: Mitfahrer bleiben im Raum geparkt,
  nur bei aktiver RV-Mod), v3.11.97 (Werkzeug in der Hand an allen Stationen, BanditsNPCWorkTool + 16 Fakes NPCCrew.*Hand,
  Saege-Knoten BNSawLog fuer Cut Planks), v3.11.99 (Heli/AviationCore: Rueckkehr-Kachel nicht im Rumpf, nur nach Fluggeraet;
  SP nach Figurentod steigen Mitfahrer aus). ALLES UNGESPIELT. Gegenpruefungen laufen (Werkzeug; RV+Heli inkl. ohne Mods).
  Server laeuft noch v3.11.95 -> vor dem Test neu starten. Uninstall-Helfer (eigene Mini-Mod) nur besprochen, nicht gebaut.
  B10, B11 bestanden, B12 auf Kevins Wort. MP-Teil B komplett. SP-Kurzliste (5 Punkte) an Kevin gegeben.
Stand 29.09.2026 mittags (Test v3.11.94 im MP): BESTANDEN A8-MP, B9, B13, B14, B15; A1-A6 + B3-B8 (Fischer) auf Kevins Wort
  abgehakt, nicht einzeln belegt. Offen im MP: B10 (M16), B11 (Auto-Beschuss), B12 (Waffe am Ruecken).
  v3.11.95 GEBAUT 12:21 nach dem Test (arriveAt nbSure + recon vor DropOff), ungespielt; Server per RCON aus.
  Offene Frage an Kevin: Saege-Bewegung fuer Cut Planks (eigener Knoten aus Vanillas Bob_IdleSawLog, ohne Ton)?
Stand 29.09.2026 11:32:
- Nachpruefung .92/.93 (Neustart als w6jhp6731, 4 Agenten, die Nacht-Pruefung starb mit der Sitzung): 1 ernst + 4 klein, alle
  als v3.11.94 gebaut (Wassertraeger pendelte an der Kletter-8-Kachel-Grenze -> Tonnen-Merkung zuerst; Charge-weg erst nach
  Abgleich; _dropUnreach raeumen; nbSure = ungeladene Nachbarn 20-s-Frist; Food-Deckel eine Regel, TooMany neu 6 Sprachen).
  UNGESPIELT, gesichert + gespiegelt. Server AUS -- vor dem Test starten (bat), Fehlerwaechter mit, beide Clients neu.
Stand 28.09.2026 22:05 (Kevin geht schlafen, morgen weiter):
- v3.11.90 (vier Stillstand-Stellen), v3.11.91 (Essensliste zaehlt alles Erreichbare, Forbid all jede Zeile -- Kevins Wahl
  'Alles Erreichbare'), v3.11.92 (7 Pruefer ueber .90: MP-Abgabe closeDrop, Koch skipCrate/BlockUnreach, nbLoaded, Wasser-
  Kletterbremse), v3.11.93 (5 Pruefer ueber .91: Handzuweisung spots.food, oberste Taschenebene, MP-Roster unsicher, Food_TooMany,
  1888 Keys). ALLE UNGESPIELT. Testserver per RCON beendet. Eine 5-Agenten-Nachpruefung ueber .92/.93 (Workflow wmrwj0z1n) lief
  beim Schlafengehen noch -- Ergebnis morgen zuerst lesen und ggf. v3.11.94.
- MP bestanden 28.09.: B1 (Testaccount 'user', Netz kontrolliert, kein Kick), B2 (Netze). Offen: B3-B15, A8 Stationen (MP:
  Schmied/Mechaniker/Bauer, Testaccount erst weiter weg, dann naeher), Testliste Stand v3.11.93.
- Beim Test: beide Clients + Server neu starten (Pruefsumme), Fehlerwaechter mitstarten.
Stand 28.09.2026 19:05:
- v3.11.78: Pruefer ueber .75 (Koeder am Haken kommt immer ab, Essens-Koeder nur beim Angeln festgehalten, Faenge nicht im Grund).
- v3.11.79: 156 Sonden (Crew logging 2) fuer die Testliste, Karte in `_docs/sonden_testliste.md`; Diagnose-Ladezeitwert AUS
  (war seit v3.7.99 an -- Kevin: keine Sonde bei aus); [TC-XFER] nur eingehaengt, wenn Stufe 2 beim Laden. Fehlerwaechter
  `_docs/tools/bugwatch.py` gebaut und laeuft als Monitor (siehe [[bugwatch-bei-jedem-test]]). Naechstes: Kevin testet.
Stand 28.09.2026 18:05:
- v3.11.73/.74: kein Gratis-Trinken am trockenen/Rest-Becken (useFluid, MP ueber den Server), Alter vor dem Verdorben-Test
  nachziehen, kein Nachschub-Kreis (Handauftrag wartet ganz, Dauerauftrag nicht bei Strom-/Arbeitspause).
- v3.11.75: Koederregel je Fischzone (site.fishBait, F.BaitVerdict fuer Rebait/BaitCount/BaitInStore), nutzloser/verbotener
  Koeder kommt ab, Essens-Koeder in Portionen (E13), Wild/Rind wieder essbar (BaitKind-Schwelle). v3.11.76: Koederfenster
  (Fishing-Reiter 'Bait rules...'). v3.11.77: Pruefer ueber .74 (Benzin-Becken, Wartegrund, Strom-Riegel, Beacon-Satz).
  Widerleger ueber .75 laeuft/lief -> ggf. v3.11.78. Danach offen: Canned-Veg-Deckel, Komposter-Auftrag (vorgemerkt).
Stand 28.09.2026 17:10:
- v3.11.66-.69: Chum 0 rot, Forbid all, Tagespruefung-Vorlauf, Crew isst nichts Verdorbenes/Verbranntes.
- v3.11.70: Tagespruefung (7 Agenten) -- trockene Becken nicht mehr waehlen, Texte, Cursor sagt warum.
- v3.11.71: KOCH nach Kevins drei Wahlen (Filet gekocht, Rezepte Koederfisch/Krebs/Frosch, Alter erben, Verdorbenes nie
  angefasst -- durch alle Leser: Planer, Nehmen, Sortierer, StockOf). v3.11.72: Pruefer ueber .70 (leeres Fass als Waschplatz).
  Vier Pruefer ueber .71/.72 laufen/liefen. OFFEN fuer Kevin: Trinken am trockenen Becken gilt als endlos; Deckel-Zustand
  Canned Veg + Dosen-Reste beim Kochen (naechste Version); danach Koederliste E9+E13/E10.
Stand 28.09.2026 15:35:
- v3.11.62: Beacon-Drehen/Aufheben/Zerlegen auch serverseitig gesperrt (4 Aufsaetze in NoSledge), Zonen-/Forst-Cursor R-Taste,
  MAX_PER_KIND 8 -> 64 (Kevin: 32 NPCs brauchen mehr Betten). Testliste A11, B15. Zwei Pruefer laufen/liefen.
- v3.11.63: 3D-Portraets bis 64 (Portrait.POOL_CEIL), TrueCompanions_Portraits() ohne Zahl warf (nil-Global pool).
- v3.11.64: NPC-Fenster merkt sich je Companion den letzten Reiter (NPCCrewClient.ini NPCWin.<uid>), nur eigene.
- v3.11.65: Fischer-Reiter Lagerzeile (Ruten/Koeder/Chum/Netze), Basis-Scan-Budget nur echte Kacheln, Uferplaetze max 8, 64+.
  Offen fuer Kevin: Building-Craft-CeroSec-Terminal gilt als Beacon. Pruefer ueber .63-.65 laufen/liefen.
- PZ-UPDATE 42.21 kam 28.09. 14:46 (685 Dateien). Geprueft: kein Bruch (apicheck.py, vier Agenten, Kevins SP-Runde ohne Fehler).
- v3.11.55-.61 gebaut, UNGESPIELT: Essensliste E11/E12 samt Pruefer-Korrekturen; Konserven (alle Glaeser/Dosen essbar, geschlossene
  von Haus aus Never, freischaltbar, leere Dose/Glas+Deckel zurueck, Canned Veg braucht Deckel); Waschen kostet Wasser (5x Trinken,
  Dreckwasser zuerst, nur Wasser, kein Teilen); TV-Sitz aus allen Stuehlen (Workshop-Meldung). Kevin hat das Essensfenster
  gesehen und gelobt (Stand .55-.57). Testliste `_docs/testliste_2026-09-28.md` A1-A10, B1-B14.
- Offen: Koeder-Kern E9+E13 und Koeder-UI E10 (plan_koeder_essen.md).
Stand 27.09.2026 16:27:
- v3.11.18 IST OEFFENTLICH (Steam updated 27.09. 16:26:55, 10,0 MB, 3824 Abonnenten; Beschreibung = geparktes workshop.txt,
  jetzt mit Chinesisch). Ordner GEPARKT. Ab hier zaehlt "nichts hochgeladen seit v3.11.18". Patchnotes: lang
  `_docs/patchnotes_v3.11.18_plain.txt` (19k Zeichen, zu lang fuer Steam), kurz `_short.txt` (3.940 Zeichen) -- Kevin hat
  die kurze benutzt. MP vor dem Upload gespielt: Kuechenfenster ueber Theke, Panik 0 neben Crew / echter Zombie Panik,
  Tuer-Schliessen in der Basis, Station unter Fenster. Server per RCON save + quit beendet.
  ERLEDIGT laut Kevin 27.09.: "Fighter Test 100 % Durst trotz Regenfaenger" ist schon gefixt -- nicht mehr als offen nennen.
Stand 27.09.2026 0:35:
- v3.10.97-v3.11.4 gebaut: Kick-Fix (removeItemOnServer fuer alle Rollen), Logout wartet auf den Sendepuffer (St.leaving), Fenster-Schalter, Heilen SP+MP (eine Tablette, Rundruf HealCompanion, Help up an alle), Kletterbremse (Ankunft nahe am Ziel, Folgen ohne Marke), Stehplatz ohne Sackgasse (v3.11.4; v3.11.5/.6 nach zwei Pruefrunden: Treppe nur vom Fuss/Absatz, Sackgasse als letzter Rueckfall, aktuelle Kachel zuerst, Treppenstufe nur Rueckfall). SP 1-4 bestanden (27.09. 0:20). Beide Pruefungen durch. Testplan: [[testplan-27-09]]. Nichts hochgeladen seit v3.10.70.
Stand 26.09.2026 mittags:
- v3.10.71 (Workshop-Meldung: Beacon-Rufen schaltet sich im MP wieder ein -- Objekt-ModData nie zum Server, jetzt B.SaveState + Seed aus dem Eintrag) und v3.10.72 (Chinesisch vereinfacht CN, nur Vanilla-CN-Zeichen; KO AmmoHUD_Load) GEBAUT, UNGESPIELT, NICHT HOCHGELADEN, geparkter Ordner gespiegelt + Chinesisch-Zeile in workshop.txt. Kick-beim-Anwerben-Meldung: Antwort geschrieben, wartet auf Log des Melders.
Stand 25.09.2026 spaetabends:
- 26.09. 0:18: v3.10.70 oeffentlich im Workshop (Building-Craft-Zonenfix v3.10.68-.70, Beacon-/Wasser-/MP-Fixes). Ordner geparkt.
- v3.10.66/.67: unerreichbare Wasserstelle beendet die Routine; Ufer-Overlays echter Seen fuellen nur den Rest der Wasserliste; Dreckwasser-Sperre gilt nicht fuers Waschen. GESPIELT 25.09. abends: Regentest, Wassertraeger trinkt, Kiste neben Beacon ueberlebt Ausbau+Abbau, Parken beim Sehen. v3.10.67 ungespielt.
- v3.10.60-.65: Pfuetzen keine Wasserstelle, Wasserregel wie das Spiel (Stellen streng, Flaschen 10 %), Scan legt echte Quellen vor Teichkacheln ab, Server parkt Companions abgemeldeter Spieler beim Laden ihres Chunks (Rueckkehr-Kachel vom Posten). MP-Tests Vorschlaghammer/Admin, Beacon-Abbau durch Admin, zweiter Beacon, Noah-Parken BESTANDEN.
- v3.10.59: Pruefer-Funde ueber .56-.58 (Deko-Uebernahme, ferne Routineplaetze, Folgen nur bei eigener Basis). Tests aa-ii.
- v3.10.58: Vorschlaghammer/Zerlegen fuer ALLE auf Beacons gesperrt (Kevins Ansage), Beacon-Regel nach shared (SR.IsBeaconObject). Tests aa-dd. Ungespielt, nicht hochgeladen.
- v3.10.50 (Punkt 1 der Workshop-Liste: Beacon-Ausbau frass Kuechenschraenke), v3.10.51 (vier Pruefer + Sandbox-Optionen
  OneBeaconPerPlayer/BeaconMinDistance + Koreanisch/Spanisch, fuenf Sprachen, Languages-Abschnitt im geparkten workshop.txt)
  und v3.10.52 (zweite Pruefrunde: radikal vereinfacht -- Theke/Funkgeraet nie Beacon, Basen mit Flaechen nie geraeumt,
  neuer Beacon nie <= 2 Kacheln an einem Eintrag, Aufheben am Objekt gefragt) GEBAUT, UNGESPIELT, NICHT HOCHGELADEN.
  v3.10.53: dritte Pruefrunde -- Alt-Schluessel ueber Koordinaten statt Thekenobjekt, einsamer toter Beacon wird
  wieder geraeumt, Zerlegen-Cursor ohne Fehler. Oeffentlich bleibt v3.10.49. Tests: `_docs/offene_arbeit.md`
  v3.10.50 a-f, v3.10.51 g-i, v3.10.52 j-m, v3.10.53 n-p, v3.10.54 q.
- Naechste Punkte der Workshop-Liste (Kevins Reihenfolge offen): Punkt 2 verwaister Eintrag / aktuelle Stufen-Sprites auf Sicht,
  Panik-Pendel, Forst-Cursor, Auto-Beschuss, Idle-Emote, Waffen-Aufsaetze in der Hand, Crew-Knopf verschiebbar.
Stand 20.09.2026, 21:10:
- v3.10.49 IST OEFFENTLICH (Item 3800132623, Steam updated 20.09. 21:04, 1573 Abonnenten). Upload-Ordner GEPARKT.
  Vor dem Upload gespielt: SP (Jacke 4/10 mit Loch ueber Wear/Take off/Speichern/Laden, Scope, Schaerfe) und MP
  (Jacke per Take ueber Server, Scope, Jacke ueber Posteingang -> Kleiderkiste mit Zustand). Patchnotes in _docs.
- Kevin bis Fr/Sa weg, 6 % Wochenlimit: KEINE Agenten ohne Not. Danach: Fischer E5 (Fischkiste), E7 (Reusen +
  Benutzen-Schalter), E8; M16 nicht per Rechtsklick aus der Kiste (Konsole beim Klick lesen); Durst/Regenfaenger
  (TrueCompanions_DrinkWhy); Fischer-SP-Test (v3.10.36-.46) weiter verschoben.
Stand 20.09.2026, 20:05 (aelter):
- v3.10.46 (Fischer-Reiter UI, Koeder 10), v3.10.47 (Fischer-Stacktrace + Widerleger-Fixes ueber .45: MAN_DEPTH-Verdopplung,
  SP-Take-Aufsaetze), v3.10.48 (Manifest Teil 2: wornRec je Slot, Kleidungszustand, Schaerfe/Kopf -- Kevins Wort fuer die Setter),
  v3.10.49 (Widerleger: MP-Faellverschleiss summiert sich) GEBAUT, UNGESPIELT, NICHT HOCHGELADEN. Server laeuft v3.10.47.
- KEVINS PLAN (20.09. abends): nur noch 6 % Wochenlimit bis Freitag, bis Fr/Sa nicht zuhause -> Rauchtest SP (Jacke/Scope/Laden) +
  MP (Jacke/Scope per Take), dann stage -> Upload -> park. Reusen (E7), Fischkiste (E5), E8 danach. KEINE weiteren Agenten ohne Not.
- Offen: Fighter Test 100 % Durst trotz nicht-rotem Regenfaenger (Sonde TrueCompanions_DrinkWhy, v3.10.48); Fischer-SP-Test verschoben.
Stand 20.09.2026, 19:05 (aelter):
- v3.10.42-.44 (Moebel: Muenze ueber instanceItem, zwei Familien) IM SPIEL BESTAETIGT SP + MP (20.09. 18:15). Melder-Fall zu.
- v3.10.45 (Manifest-Luecken Teil 1: Waffen-Aufsaetze, Schluessel-Id, eigener Name, Favorit, Tasche-in-Tasche Ebene 4,
  Server-Muenze mit Aussehen) und v3.10.46 (Fischer-Reiter rechts neben Unload cars, Stop hinter der Textspalte, Hotkey
  'Show fishing zone' F12 umlegbar, F.BAIT_STOCK 10) GEBAUT, UNGESPIELT, NICHT HOCHGELADEN (oeffentlich v3.10.35).
  Teil 2 der Manifest-Luecken offen: getragene Kleidung als Datensatz, Schaerfe (Setter braucht Kevins Wort), Kopfzustand.
  Testlisten `_docs/offene_arbeit.md` v3.10.45 a-g, v3.10.46 a-d; Fischer v3.10.36-.40 weiter ungespielt.
- Testserver lief am 20.09. abends noch (v3.10.44 geladen) -- vor dem naechsten MP-Test neu starten (v3.10.46).
Stand 20.09.2026, 16:00 (aelter):
- v3.10.36 (Fischer E4+E6: Fischzone je Basis als Beacon-Reiter 'Fishing', Zuweisung am NPC oder 'Assign...' nur Jobfreie, Dauerjob wartet auf Rute/Koeder/Platz/Zone und holt aus dem Lager, Portraet + Zustand je Fischer, All stats je Basis SP+MP) v3.10.37 (Korrekturen: tcFishSeenH ist Zahl nur waehrend sie wirft; ungeladene Zone = warten; Stop fragt zuerst; FishStat-Deckel) v3.10.38 (vier Widerleger: Stop bei Routine ueber Angeln; 'voll' = Ablieferung; F.ClockOff an der Park-Engstelle) v3.10.39 (drei Widerleger: Stop unter Handjob = Job-Ende; Uhr auch bei Handjobs; Lieferung mit leichtestem Fisch + Absage-Gedaechtnis) und v3.10.40 (zwei Widerleger: der Stop-Ausgang war falsch platziert; Absage je Kiste; Uferweg-Zaehler statt Teleport) GEBAUT, UNGESPIELT, NICHT HOCHGELADEN. Pruefkette beendet (10+4+3+2). Dazu v3.10.41 (Moebel-Sprite im Manifest, Workshop-Meldung). Testliste `_docs/offene_arbeit.md` (v3.10.36 1-7, .37 a-e, .38 f-i, .39 j-l, .40 m, .41 MP-Moebel). OFFEN fuer Kevin: Stationen gegen Aufheben riegeln? Offen im Rework: E5 Fischkiste, E7 Reusen, E8 Anzeigen -- Kevins Wahl.
- Oeffentlich im Workshop: v3.10.35 (Item 3800132623, hochgeladen 20.09. 14:25; davor v3.10.32 seit 20.09. 0:10, v3.9.88 seit 18.09.). Upload-Ordner geparkt.
- 20.09. mittags: v3.10.33-.35 (Frisur editierter NPCs ueberlebt neuen Koerper: Anblick-Vergleich statt Stempel, 30 Agenten in vier Runden) GEBAUT und am 20.09. nachmittags IM SPIEL BESTAETIGT (SP + MP, Konsolen belegen alle drei Wege); hochgeladen 14:25.
- GESPIELT 19.09.: SP-Kurzliste A1, B1, B5, B11 (A4 halb); v3.10.6/.7 (Holzplatz-Quelle, Seile);
  MP G2 (Axt zweimal + Magazin nach Client-Neustart mit v3.10.10) und G3 bestanden; G12 gestrichen
  (Bodenaufnahme durch Nicht-Admins im Bytecode belegt). v3.10.9 (leere Haende zeigten Axt-Icon)
  und v3.10.10 (Magazine je Fuellstand) dabei gebaut, v3.10.10 mitgespielt.
- Drei Workshop-Meldungen eines MP-Spielers (19.09.): Schuesseln aus dem Nichts, Feueraxt-Dupe,
  verdorben -> frisch. 22-Agenten-Pruefung + 5 + 3 Widerleger -> v3.10.11 (CaptureFood/ApplyFood,
  Bowl-Zutat, Rest vom Essen zurueck), v3.10.12 (reclaimStuckCopy vor dem npcMelee-Re-arm),
  v3.10.13 (Alter in Tagen, updateAge, Tor vor dem Remove, Parkzeit), v3.10.14 (zwei ernste
  Widerleger-Funde: Pp-nil-Global, Axt-Rueckholung nur vom Opfer), v3.10.15 (gekocht/verbrannt/
  gefroren im Manifest -- KEVINS AUSNAHME von Regel 3 fuer fuenf Setter, "ja bau", Jar-belegt,
  steht in CLAUDE.md Abschnitt 3), v3.10.16 (MP-Take aus einem Rucksack in ihrer Tasche abgelehnt --
  verdoppelte die Wurzel und vernichtete das Kind, Vorbestand seit v3.10.0; Frost-Projektion),
  v3.10.17 ('All' im MP war durch den Riegel tot -- nur Waisen ablehnen), v3.10.18 (Enkel einer
  Tasche in Tasche wandern vor dem MP-Take hoch). PRUEFKETTE BEENDET: acht Runden, ~50 Agenten,
  die letzte fand im frischen Code nichts mehr. ALLE UNGESPIELT. Testliste T0-T9 in `_docs/offene_arbeit.md` (Abschnitt WORKSHOP-MELDUNGEN 19.09.).
- 19.09. abends GESPIELT (MP): T0-T5 bestanden (gekocht/verdorben bleiben, Schuessel, Feueraxt via
  TrueCompanions_StuckAxe v3.10.20, Rucksack). v3.10.21 (Rute braucht Schnur+Haken) in v3.10.22
  ZURUECKGENOMMEN: Vanilla kann Schnur/Haken nicht abmontieren -- mein "ja" war unbelegt.
  v3.10.23-.25 = Workshop-Meldung Squabbithunter (Mod-Kleidung unsichtbar/unausziehbar): Zusatzkaesten
  + Exklusiv-Regel mit ItemBodyLocation-OBJEKTEN (v3.10.23 hatte Strings uebergeben -- toter Aufruf,
  Fehlerzeile je Stueck), Fenster waechst mit. Kevin hat Ruten-Heiler fuer alte Ruten
  abgelehnt ("nicht noetig"). GESPIELT 19.09. SP: Mod-Kleidung sichtbar, keine Fehler, Exklusivitaet
  greift -- aber Kaesten 'viel zu viel abstaende' -> v3.10.26 kompakte Liste -> '+5' und KEINE Zeile
  (die sc(560)-Reservierung erreichte bei seiner Schrift nie die Hoehe, railNeed setzt sie) ->
  v3.10.27: Hoehe aus der echten Puppenspalte (bnDollColumnNeed), Deckel gemessen, Kevins Knopf
  'take all off' in der Kopfzeile + klickbares '+N more', MP-Take-all als Kette je Stueck, Meldung in
  Spaltenbreite. Drei Widerleger -> v3.10.28: MP-Kette Record je Stueck + onFail an M.Grant (Logout-
  Dupe-Fenster zu), busy benannt, Deckel/Meldung nie unter contentBottom, Kopfzeile in UIFont.Small;
  1669 Keys. v3.10.27/.28 UNGESPIELT.
- OFFEN (spaeter): Server-Wahl innerhalb des passenden Behaelter-Eintrags beim MP-Take; Herholen-Text
  'ein Mitspieler haelt sie geladen', wenn der Server den Chunk haelt.
- Danach: MP-Serverwege (Faell-Verschleiss, Feuer, FillAt, WearTools sync, Logout-Parken mit
  Cluster-Programm), E4 Fischerzone.

**Why:** Kevin wollte die Workshop-Meldungen sofort geprueft haben ("kannst du das kurz untersuchen
wenn noetig auch mit 30 agenten"); die Antwort an den Melder steht noch aus, bis er die Versionen
gespielt und hochgeladen hat.
**How to apply:** vor dem Upload T1-T3 spielen lassen; im Antworttext an den Melder die drei
Ursachen und die Restgrenze (gekocht -> roh) nennen. Siehe [[kevins-zwei-rote-linien]].

**05.10. spaet:** A7 (Putzen beim Testaccount) BESTANDEN. Neu E4b: 'ground can't be reached' = gleicher Zaunsprung-Haenger (ClimbFenceEnd) wie E4, Ziel 10 min gesperrt, deshalb 'manchmal' -> Fix in v3.12.60 mit E4. Neu E5: Bump-Posen (setBumpType) reisen nicht uebers Netz (keine Netzklasse im Jar liest bumpType, Bandits synct nicht) -- der andere Spieler sieht Werkzeug, keine Pose; Rundruf wie HandShow moeglich, ungeprueft, Kevin fragen. P6-Plan fertig (_docs/plan_v3.12.60_tierpfleger_p6.md, 15 Fragen an Kevin, Empfehlung zwei Versionen); Fix-Version E1-E5 kommt zuerst, P6 rutscht auf v3.12.61+.
**05.10. spaet, Kevin zu E5:** Posen-Rundruf in v3.12.60 PROBIEREN -- nur wenn fehlerfrei, und abnehmbar gebaut (eigene Datei + Schalter, keine Umbauten an Bestehendem); klappt es nicht, sauber raus. E6: Show-Knopf fuer Ertragskiste (+ Wasserfass als mein Zusatz).
**05.10. ~21:55:** MP-Teil der Testliste 06.10. KOMPLETT bestanden (A1-A8; A6 im 2. Versuch: Logout mit 6 Eiern, Neubau, 6 in die Kiste, Kevin bestaetigt). Offen: SP B1-B10, Funde E1-E7 fuer v3.12.60 (E7 = Putzen stoppt bei 5 statt 0).
**05.10. ~22:15 Kevins Antworten E4 (Diagnose _docs/diag_v3.12.60_e4_kreis.md):** Wassersuche ab Arbeitsort max 45; lange MP-Gehbefehle (alle Berufe) mit Schalter VORGABE AUS; Zeitregel 15 s NUR Pflegerin (Fischer bleibt); Aufgeben = Teleport zum eigenen Ziel statt Sperre. E5 Posen-Spiegel: machbar nur als Schalter (_docs/plan_v3.12.60_e5_posen.md). v3.12.60 = E1-E7 + F1-F5 (F6 nur messen). P6 danach (v3.12.61+).
**05.10. ~23:00:** SP-Tests: B1 bestanden, B4/B7 halb (Schwamm TOP), B2 Hahn-Teil offen. Neu E8 (Eieruhr-Kopfzeile), E9 (SP-Sortierer im Kreis: Quell-Anspruch nie gelesen; Treppe direkt am Posteingang). Kevin: Teleport auch zu Kisten, leere Zonen -> Getragenes noch abliefern, 45 Kacheln beide Modi, grosse Haufen mehrere Sortierer, Warteplaetze verlegen. Plan _docs/plan_v3.12.60_fixversion.md (+Kritiker +Antworten). BAU v3.12.60 laeuft (wf_a72852bc-801, 8 Agenten: 3 Bauer, 3 Pruefer-Fixer, Integrator, Endpruefer). Danach P6 als v3.12.61+.
**05.10. spaet: P6-Fragen ALLE beantwortet** (alle Empfehlungen, Abschnitt KEVINS ANTWORTEN in _docs/plan_v3.12.60_tierpfleger_p6.md): P6 = v3.12.61 Wolle+Mist, v3.12.62 Maehen; Mist Vorgabe aus, Mistkiste je Basis (Komposter ok), ohne Kiste liegen lassen, nur Rechen/Laubrechen, leiser Ton; Wolle Schalter an; Geschenktes wegbringen; Gras erst Troege dann Posteingang, Maehen an, Ziel fest 20, Blumen stehen lassen, ueber Beete erlaubt, Sense echtes Modell sonst Sichel.
**05.10. 23:20: v3.12.60 GEBAUT** (8 Agenten, 3 Pruefer + Endpruefer, alle 13 Dateien Pruefer gruen, UI.json 2335 je Sprache inkl. 11 alter Luecken), gesichert, Workshop gespiegelt+geparkt, UNGESPIELT. Tests oben in offene_arbeit (T-A1..T-E9, T-M1..M5). Schalter: TrueCompanions_PoseShow (an), TrueCompanions_LongWalk (aus). Rest: Futter fuer leere Zone koennte gegessen werden (Endpruefer).
