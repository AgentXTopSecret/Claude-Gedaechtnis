---
name: moegliche-features
description: "Community-Wuensche und Kevins Merkposten als moegliche Features; Koch-Rezepte fuer alle Tierprodukte nach dem Tierpfleger (04.10.); Leichen entsorgen (nach Fischer-Rework), Crew-Knopf verschiebbar, Komposter-Auftrag fuer Verdorbenes (28.09.), Tierpfleger (Recherche fertig 29.09., 12 Entscheidungen offen); Liste in _docs/offene_arbeit.md ganz oben"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-11-06T21:55:51.083Z
---

Kevin (19.09.2026): "du kannst dir das ja mal merken als moegliche features" -- fuer Workshop-Fragen, die kein Fehler sind.
Die ausgearbeitete Liste steht ganz oben in `_docs/offene_arbeit.md` unter "MOEGLICHE FEATURES".

Eintraege bisher:
- **GESTRICHEN 02.11. (Kevin: 'dann lassen wir das einfach so'): Pruefauftrag _docs/leichen_ziehen zeigt, die Engine bewegt keine Leiche, im MP geht der Griff mit einem NPC nicht; nicht neu aufmachen.** LEICHE SICHTBAR ZIEHEN (Kevin 29.10.: 'zombie attrape ... ueber den boden schleifen beim corpse cleanup? nur zur show'): heute kniet
  die Figur und geht leer zum Feuer, die Leiche verschwindet erst dort. Plan mit drei Wegen (A echte Leiche per pickUpCorpse -- steht auf
  IsoGameCharacter, belegt nur am Spieler; B eigener Schein-Zombie; C nur Zieh-Pose) und Pruefauftrag (4 Agenten) in
  `_docs/plan_leichen_attrappe.md`. Kevin 29.10.: 'das kommt erst nach dem hochladen' -> erst NACH dem naechsten Upload (auch der Pruefauftrag); Bau nur auf Kevins Wort, B nur mit ausdruecklichem Wort.
- **PLUENDERN: ZEICHNEN UND 'THIS BUILDING' (Kevin 22.10., aus Workshop-Wunsch 'loot bodies/room/building on command'):** Grundlage bleibt die
  gezeichnete Lootflaeche; dazu ein Schnellknopf 'This building' = Gebaeude, in dem der Spieler steht, alle Stockwerke, danach erweiterbar.
  Leichen pluendern gibt es schon (Clean up corpses + Loot list). Einzelheiten Nachtrag am Ende von _docs/bauplaene_2026-10-16/05_pluendern.md.
- **SCHUSSWAFFEN NUR GEGEN BANDITEN (Kevin 22.10., Workshop-Wunsch, Fahrplan B15):** Einstellung JE SPIELER fuer alle eigenen Companions --
  gegen Zombies Nahkampf, Gewehre nur gegen Banditen/feindliche NPCs (sonst schiessen sie auf alles, Munition leer). Kevin wollte 'Sandbox fuer jeden
  Spieler' = meinte die Player settings im Beacon-Fenster. Wert am Gehirn (im MP kaempft der Hoheits-Rechner). BAUFORM ENTSCHIEDEN 22.10.:
  sperrt nichts -- bei feindlichen Banditen in Schussweite schaltet die Automatik Firearms AN fuer alle eigenen NPCs im Umkreis ~30 Kacheln,
  nach ~30 s ohne Banditen wieder AUS (gilt NUR fuer NPCs, deren Firearms-Schalter AUS steht; wer AN steht, bleibt immer AN und schiesst wie bisher).
  Einzelheiten offene_arbeit.md, MOEGLICHE FEATURES.
- **Leichen entsorgen -- VORGEMERKT FUER NACH DEM FISCHER-REWORK (Kevin 20.09.: 'merk dir das mal fuer nach den fisher
  rework')**, zweimal im Workshop gefragt (19.09. + 20.09.: Sammelzone, Haufen, beerdigen). KEVIN 06.10.: corpse cleanup laeuft
  UEBERALL, nicht nur in der Basis -- die Basis-Sammelzone unten ist damit nicht mehr die ganze Bauform. Heute nicht vorhanden; Bandits
  hat die Tasks (ZAPickUpBody/ZABuryCorpse/ZAFillGrave, Housekeeping nur in ZPCompanion). Bauform: BEFEHL (kein Beruf),
  gezeichnete Sammelzone/Haufen wie der Holzplatz, Leichen hintragen, Timer entfernt sie (sq:removeCorpse, MP ueber Server);
  Graeber vom Spieler gegraben. NICHT wie Vanilla verbrennen (burnCorpse = echtes IsoFire 100/700, breitet sich bei FireSpread
  aus, Bandits ManageOnFire toetet brennende Companions). Kosmetisches Feuer: Sprite + Licht wie Feuerstelle (empfohlen,
  kein IsoFire) oder Vanillas permanentes Campfire-IsoFire (kein Spread, aber brennt Betreter, ManageOnFire binnen 2
  Kacheln -> nur brennen, wenn niemand arbeitet). Details mit Fundstellen in _docs/offene_arbeit.md, Eintrag 'LEICHEN ENTSORGEN'.
  KEVIN 15.10.: "unsere soll ja ziemlich gleich laufen [wie A-Life] und ueberall laufen egal wo man grade ist in sp/mp mit leichen in der
  ausgewaehlten area zsm sammeln und dann verbrennen wie die tiere" -> dieselbe Brennstelle/Attrappe wie der Tierpfleger (v3.13.43ff).
  Er hat 'Project A-Life NPCs' abonniert (Workshop 3803984183, Aufraeum-Code server/ProjectALife/Admin/ALifeCleanup*.lua) zum Nachlesen --
  Mechanismus lernen, NICHT abschreiben. Recherche-Lauf wf_e954387f-d43 schreibt _docs/leichen/A_alife_cleanup.md, B_bausteine.md,
  C_plan.md, D_kritik.md. Danach Kevin Kurzfassung + Fragen (Leicheninventar!), Bau erst auf sein Wort.
  KLARSTELLUNG 15.10.: "die brennstelle von den leichen verbrennen geht ja UEBERALL auf der map sonst macht die option ja auch keinen sinn" --
  NICHT die Basis-Brennstelle; verbrannt wird dort, wo die gewaehlte Flaeche liegt. Wiederverwendet wird nur der CODE (Anzeige, Kadaver im Feuer,
  Tuer-Form). Reihenfolge (mein Vorschlag, Kevin nicht widersprochen): v3.13.51 -> .52 -> .53 Haken/Stall -> Leichen -> Crew Backpack.

- **EIGENER CREW-RUCKSACK -- VORGEMERKT FUER NACH TIERPFLEGER STUFE 3 (Kevin 13.10.2026: 'merk dir das auch fuer nach stufe 3'):** woertlich:
  "will ich einen eigenen rucksack den man craften kann 'eher teuer' weil der soll bei den npc's +100 traglast geben und nur fuer npc's
  ausruestbar sein aber ich muss mir noch das model aussuchen". Also: (1) eigener Gegenstand mit einem VORHANDENEN Vanilla-Modell (KEVIN
  SUCHT DAS MODELL AUS -- vor dem Bau fragen), NAME: EN 'Crew Backpack'; in den anderen Sprachen bleibt 'Crew' stehen und nur 'Backpack' wird uebersetzt (Kevin 13.10., erst: "soll 'Crew
  Backpack' heissen also in jeder sprache", dann: "ja okay Backpack darfst du schon uebersetzen"); (2) craftbar, Rezept 'eher teuer' (Zutaten und Station mit
  ihm klaeren, z. B. Schneider); (3) +100 Traglast fuer die NPC, die ihn traegt; (4) Spieler koennen ihn NICHT ausruesten (weder Ruecken
  noch Hand; Hinweistext), nur NPCs. Von mir am 13.10. eingeschaetzt: eine kleine Version (~2 h mit Pruefern); die Mod hat schon eigene
  Gegenstaende (42/media/scripts/tc_handitems.txt) und rechnet die Traglast aus der getragenen Tasche (H.CarryBag in
  shared/BanditsNPCHaul.lua, brain.bag.name). Im Jar gelesen (13.10.): die Gewichtsreduktion eines Behaelters zaehlt nur AUSGERUESTET
  (InventoryContainer.getEquippedWeight; InventoryItem.getUnequippedWeight = Eigengewicht + voller Inhalt) -- im Spielerinventar bringt
  er also nichts, eine zweite Sperre ist unnoetig (Kevin wusste das vorher). IM JAR GELESEN (13.10., ItemContainer.getCapacity): die Engine deckelt die Kapazitaet eines Behaelters, der ein GEGENSTAND ist, auf 50
  (Weltbehaelter 100, Fahrzeugteile 1000) -- die +100 koennen also NICHT aus dem Behaelterwert kommen, sie werden in UNSERER Traglast-
  Rechnung fuer genau diesen Typ addiert (H.CarryBag / paintedBagCap / bagTypeCap in shared/BanditsNPCHaul.lua; die Mod entscheidet
  ohnehin selbst ueber St.RoomFor, wie viel eine NPC traegt). Sortierer nehmen seit v3.12.50 nur, was ins Ziel passt (H.DstFree) --
  Kevins Bedingung 'nur nehmen, wenn im Lager Platz ist' ist damit schon gebaut. VOR DEM BAU NOCH NACHLESEN: und ob die Spieler-Sperre im MP auf
  allen Wegen haelt (Rechtsklick, Doppelklick, Ziehen, Schnellleiste). Nicht bauen ohne sein Startwort und sein Modell.
  MODELL GEWAEHLT (Kevin 15.10. im Debug-Gegenstandsfenster): "den millitaer rucksack will ich haben als neuen also das model" -- Vanillas
  Militaerrucksack (Bag_ALICEpack_Army bzw. Bag_ALICEpack_DesertCamo, beide 'Militaerrucksack'; sein Zeiger stand auf DesertCamo -- Farbe
  bei ihm erfragt). ENTSCHIEDEN 15.10. (Auswahl): FARBE Wueste = Modell von Bag_ALICEpack_DesertCamo; REZEPT Schneider-Station: 1
  Militaerrucksack + 2 grosse Tierhaeute (Kuh/Schwein/Schaf/Hirsch, *_Full-Leder vom Schlachten) + 4 Faden; WANN: als eigene Version NACH
  v3.13.52 (Startwort damit gegeben). Vor dem Bau noch klaeren lassen (Plan): welche Militaerrucksaecke als Zutat zaehlen (Army und Desert?),
  Typnamen der Haeute je Art (AnimalPartsDefinitions), Faden-Typ.

- **FARMER -- RECHERCHE BEAUFTRAGT (Kevin 13.10.2026 spaet: 'kannst du jz schon nachforschen wie wir den farmer bauen koennten?'), BAU NICHT:**
  seine Wuensche woertlich: Zonen-Markierung; Sandbox-Option 'farmer ignore seasons' ("damit er zu jeder zeit was anpflanzen kann ohne das die
  sachen kaputt gehn auch im winter nicht"); Sandbox-Option 'grow speed' ("weil vanilla dauert wohl ewig deswegen macht das kaum jemand");
  bewaessern, anpflanzen, ernten, krankheiten bekaempfen, "und was sonst noch alles moeglich ist". Lese-Workflow 'farmer-recherche'
  (wf_48427541-3cd, 2 Agenten nacheinander) schreibt nach _docs/farmer/A_vanilla_farming.md und B_bauform_farmer.md. Danach Kevin die
  Kurzfassung und die Fragen geben. Gebaut wird erst nach Tierpfleger Stufe 3 und nur auf sein Startwort; haengt mit dem Wassertraeger-
  Wunsch (mehrere Behaelter) zusammen.
  ERGEBNIS (14.10.2026 00:05, Berichte _docs/farmer/A_vanilla_farming.md und B_bauform_farmer.md -- B hat oben eine Kurzfassung fuer Kevin;
  statisch gelesen, nichts gespielt): (1) BEIDE Sandbox-Wuensche gibt es in Vanilla 42.21 schon WELTWEIT im Reiter Nature: 'Plant Growing
  Seasons' (aus = keine Monats-/Winterstrafen) und 'Farming Speed' (0,1-100; Vorgabe: Kartoffel/Tomate 90, Kohl 61 Spieltage; x10 = rund
  9 Tage). Eigene Optionen lohnen nur 'nur fuer Beete in einer Feld-Zone' -- machbar ueber Laufzeit-Aufsaetze auf Methoden der
  Server-Klasse SPlantGlobalObject, keine Vanilla-Datei. (2) Pflanzen sind Lua-Daten auf dem Server, wachsen auch ungeladen; alle
  Feldhandlungen ausser der ERNTE sind Vanilla-Methoden ohne Spieler, die Ernte muss nachgebaut werden (groesstes Verdopplungsrisiko);
  keine neue Ausnahme der eisernen Regel noetig. (3) MP: Vanillas Feld-Befehle pruefen nichts -> eigene Server-Tuer wie beim Tierpfleger.
  (4) In 42.21 entsteht praktisch nur Mehltau; Wasser ist die Hauptarbeit (ein Feld mit 96 Beeten ~144 l beim Saeen) -> der
  Wassertraeger-Umbau gehoert davor. (5) ENTWURF: Befehl wie der Tierpfleger (jede Companion), gezeichnete Feld-Zone, eine Sorte je Feld,
  sie graebt im Raster mit Wegen, saet, giesst, behandelt, erntet, liefert; 7 Teile + 1 Teil Wassertraeger, realistisch 10-13 Versionen.
  KEVINS ACHT ANTWORTEN (14.10.2026 kurz nach Mitternacht, alle 'Empfohlen' -- GELTEN, Datei _docs/farmer/ENTSCHEIDUNGEN.md): Optionen nur
  fuer Farmer-Felder; Vorgabe Jahreszeiten ignorieren AN und Wachstum x5; sie graebt selbst (zwei Reihen Beete, eine Reihe Weg) und pflegt
  seine eigenen Beete mit; eine Sorte je Feld; sie TRAEGT die Ernte; jede Companion als Befehl (eigene Fertigkeit spaeter); Duengen als
  Schalter mit Vorgabe aus (hoechstens einmal je Pflanze); Wassertraeger mit mehreren Behaeltern direkt nach dem ersten Farmer-Teil, VOR
  dem Giessen. DAZU (Kevin 14.10.): das Mehltau-Spritzmittel (leere Spruehflasche + 1 l Milch, wie Vanilla) stellt der BERUF Farmer an
  der Farmer-Station ab Stufe 3 her, 'genau wie der Spieler'. Bau erst nach Stufe 3 auf sein Startwort.

- **WASSERTRAEGER: MEHRERE BEHAELTER MIT PRIORITAET -- VORGEMERKT FUER NACH TIERPFLEGER STUFE 3 (Kevin 13.10.2026: 'merk dir das okay =)'):**
  Heute hat jeder Wassertraeger genau EIN Ziel (`brain.waterDest`; `W.Dest`/`W.SetDest` in shared/BanditsNPCWater.lua, Zuweisung
  client/BanditsNPCInteract.lua:995 -- am 13.10. im Code nachgelesen). Kevins Wunsch woertlich: "das der wassertraeger mehrere behaelter
  auffuellen kann mit prioritaet also welcher eimer oben steht fuellt er zuerst auf, und damit er den nicht permanent nachfuellt und die
  anderen nie, deshalb wie in der tierzone befuellen ab 75% z.b und bis 100% fuellen und danach naechster behaelter". Also: eine LISTE von
  Zielen mit Reihenfolge (oben = zuerst), je Ziel 'nachfuellen ab' (Beispiel 75 %) und 'fuellen bis' 100 % wie die Trog-Regeln der
  Tierzone, danach das naechste Ziel. Anlass (sein Satz): "wenn wir noch felder haben dann reicht nicht mehr nur ein gefaess" -- er
  denkt an einen FARMER (Felder anlegen, pflegen, giessen, ernten); dafuer hat er am 13.10. nur den AUFWAND erfragt (meine Schaetzung:
  wie Stufe 3, grob 16-24 h Bauzeit in 8-10 Teilen, ungelesen gegen Vanillas Farming-Code), NICHT beauftragt. Ebenso nur Aufwand
  erfragt, nicht beauftragt: Crew schiesst auf Spieler/PvP (meine Schaetzung 8-12 h, Unbekannte MP-Treffer/Anti-Cheat). MEINE Hinweise
  fuer den Bau: waterDest ist ein Gehirnfeld -- beim Umbau auf eine Liste JEDEN Leser mitziehen (W.FeedsDest, W.PourLocked, das
  Abkoch-Ziel, der Milchfass-Riegel v3.13.20, Sync-Pakete, CUSTOM_FIELDS) und alte Spielstaende migrieren (ein Ziel = Liste mit einem
  Eintrag). Nicht bauen ohne Kevins Startwort nach Stufe 3.

- **AMMO HUD UEBERARBEITEN (Kevin 15.10.2026: "das fenster gefaellt mir so garnicht aber alle versionen die mir claude geschickt hat damals sehn
  - NACHTRAG 20.10.: dazu ein Sammel-Knopf, der ALLE Folgenden auf einmal umschaltet (Haltung aggressiv/defensiv/passiv und weitere Einzel-Schalter) -- steht im Bauplan 09 am Ende und im Fahrplan B8b.
  ingame KOMPLETT anders aus"):** Lehre: Browser-Entwuerfe (HTML-Mockups) koennen, was PZ-UI nicht kann (weiche Schriften, runde Ecken, Schatten,
  freie Groessen) -- deshalb nie wieder nur Mockups. Vorgehen (mein Vorschlag): Kevin schickt Bild des heutigen HUD + was stoert; ich baue 2-3
  Varianten DIREKT IM SPIEL (client/ISUI/BanditsNPCAmmoHUD*.lua), umschaltbar ohne Neustart per Konsole/Regler (Form TrueCompanions_PyreFx), nur mit
  echten PZ-Mitteln (Spielschriften UIFont.*, Rechtecke, Gegenstandsbilder); Kevin waehlt per Screenshot, dann wird die Wahl fest. Position in der
  Reihenfolge: Kevin fragen.
  VORLAGE (Kevin 15.10. zeigte beide Bilder): sein damaliger Entwurf 'DEINE CREW / 6 FOLGEN' -- je NPC ein Block mit Trennlinie, Name gross/fett,
  Gesundheit als Balken + Zahl, Essen/Wasser-Symbol mit Balken, darunter Waffe, rechts Zustand % und Schaden bzw. 'N Schuss'; gebaut wurde damals
  eine enge Tabelle (Name abgeschnitten 'Fighter T...', Gesundheit im gruenen Kasten, Zeile 'Load', winzige Symbole). Nicht 1:1: Sperrschrift und
  runde Ecken. ZIEL (Kevin): "das fenster soll ja moeglichst klein [sein] das es nicht nervt und vllt der name hinpasst ohne dass das komplette
  fenster ultra gross wird" -> kompakt, Breite an den laengsten Namen angepasst mit Deckel, kein Abschneiden bei normalen Namen.

- **STRAFE BEI 100 % BEDUERFNIS OHNE ABHILFE -- ARBEITSVERWEIGERUNG (Kevin 15.10.2026, "merk dir auch das noch strafen kommen muessen"):**
  woertlich: "wenn die beduerfnisse auf 100% steigen und es keine moeglichkeit gibt die beduerfnisse zu befrieden also z.b kein essen (alles
  gesperrt) dann arbeiten die betroffenen npc's nichtmehr und es steht permanent ueber deren kopf das die nichtmehr arbeiten weil z.b hungrig ...
  das darf natuerlich erst passieren wenn der aktuelle auftrag durch ist, z.b wenn grad gecraftet wird und mitten im craften 100% essen erreicht ist
  wartet er bis der aktuelle auftrag durch ist und weigert sich dann zu arbeiten wenn kein essen da ist z.b und das bei allen beduerfnissen,
  (folgen + kaempfen geht immer)". Bauform-Gedanken (meine, Kevin genannt): KEIN gespeicherter Riegel (Zeitbomben autoTrip/haulJob), sondern bei
  jedem Arbeitsbeginn neu GERECHNET (Beduerfnis >= 100 UND keine erreichbare Abhilfe -- dieselbe Quelle, die die Routine fragt); EINE Engstelle,
  an der jedes Arbeitsprogramm seine naechste Einheit beginnt (MidJob/Programm-Main, Liste OUR_PROGRAMS), laufende Einheit/Charge endet zuerst;
  Folgen und Kampf nie betroffen; Anzeige dauerhaft ueber dem Kopf (Namensschild-Zeile, client/ISUI/BanditsNPCNameTags.lua) + Status im
  Fenster; sobald Abhilfe da ist, Routine laeuft und sie arbeitet wieder. ACHTUNG Needs.lua: Langeweile/Hygiene steigen nur und stehen dauerhaft
  hoch (CLAUDE.md 'Beduerfnisse heilen seit v0.90.52 nicht mehr von selbst') -- ohne TV/Waschgelegenheit wuerde dann die ganze Crew streiken; Kevin
  sagte 'alle Beduerfnisse' und BESTAETIGTE die Folge (15.10.: "ja das ist so gewollt dann muessen die sich das besorgen") -- also auch
  Langeweile/Hygiene/Muedigkeit streiken ohne TV/Waschen/Bett. SP + MP (Beduerfnisse rechnet der Besitzer-Rechner). Nicht vor dem Upload bauen.
  PRIORITAET NIEDRIG (Kevin 15.10.: "das feature hat aber keine hohe prioritaet die anderen sachen sollen davor kommen") -- erst nach Leichen
  entsorgen, Crew Backpack, Pluendern UND DEM FARMER (Kevin: "und auch der pflanzen dude ders ja wichtig dafuer das die leute ihr essen
  bekommen") einplanen -- der Streik setzt voraus, dass Essen selbst erzeugt werden kann.

- **PLUENDERN MIT FOLGENDEN INS AUTO (Kevin 15.10.2026: "das ich machen will das man mit npc's die einen folgen looten kann also einen bereich
  in einer stadt auswaehlt weit weg von der basis und dann items automatisch gelootet werden und ins auto eingeladen wird") -- bis 15.10. NIRGENDS
  als Plan notiert (offene_arbeit.md ~5320 lehnte 2024-08 'Pluendertouren' ab, weil eine Companion ALLEIN fern vom Spieler nicht geladen ist --
  hier ist der Spieler DABEI, also baubar). Bausteine: Flaeche ohne Beacon (dieselbe wie Leichen entsorgen, _docs/leichen/C_plan.md), Behaelter
  der Flaeche durchsuchen (Regal/Schrank/Leiche?), Filter was mitgenommen wird (Kategorien + Ausnahmeliste wie die Auto-Zone
  shared/BanditsNPCAutoZone.lua -- dort Gegenrichtung: Sortierer raeumt ein Auto IN der Basis aus), ins Auto tragen (Kofferraum/Sitze; im MP muss
  der SERVER einlegen -- sendAddItemToContainer ist client-seitig No-op, Form G.Deliver), Traglast, Gefahr (Zombies), Ende-Regel. Nur in der
  Naehe eines Spielers (76 Kacheln). Kein Auftrag zum Bauen -- nach Leichen/Backpack einordnen und mit Kevin planen.
  SONDERREGEL (Kevin 15.10.): "dass man bis zu 50 sich ueberladen kann als sonderregel bei dieser funktion damit es nicht ewig dauert und wenn die
  ziel auto's voll sind sollen die solange looten bis ihr rucksack + 50kg darueber KOMPLETT voll sind" -> waehrend des Pluenderns darf eine NPC bis
  zu +50 kg UEBER ihre normale Traglast tragen (nur in dieser Funktion; unsere Traglast-Rechnung St.RoomFor/H.CarryBag, die Engine deckelt
  Behaelter auf 50); MEHRERE Ziel-Autos; sind alle voll, pluendert sie weiter, bis Rucksack + 50 kg Ueberlast komplett voll sind, dann Ende.
  Vor dem Bau klaeren: Folgen der Ueberlast (Tempo? Vanilla-Malus gilt fuer Zombies nicht), was mit der Ueberlast nach Ende passiert (bei
  Rueckkehr in die Basis abliefern, Auto-Ablegen), Manifest/Speichern bei Ueberlast.
  ABLAUF (Kevin 15.10., gilt GLEICH fuer Leichen entsorgen -- "wie beim leichen entsorgen"): (a) per KNOPFDRUCK uebernehmen ALLE Companions, die
  gerade auf FOLGEN stehen und in der Naehe sind, den Job gemeinsam; (b) Ende, wenn kein Loot mehr da ist oder alles voll (Autos + Rucksack +50 kg)
  -> Job endet, alle laufen wieder zum Spieler (Folgen); (c) es gibt immer nur EINE aktive Lootzone gleichzeitig; sie laesst sich ERWEITERN (weitere
  Rechtecke), und sie wird ENTFERNT (beim Jobende bzw. von Hand), damit nicht 'am ende die ganze karte markiert' ist; (d) die ITEMLISTE (was
  mitgenommen wird) wird wie bei der Auto-Zone GESPEICHERT, aber GLOBAL fuer alle kuenftigen Lootzonen; sie WAECHST: jede neue Zone traegt die Typen,
  die dort liegen und noch nicht auf der Liste stehen, dazu, alte Haken/Ausnahmen bleiben ("wir die itemliste immer erweitert jenachdem was in der
  zone liegt"). LISTEN-BEDIENUNG (Kevin 15.10.): NEUE Typen stehen OBEN und LEUCHTEN (Hervorhebung), bis man sie einsortiert; es gibt ZWEI Listen,
  'Take' (mitnehmen) und 'Leave' (liegen lassen), man waehlt je Typ eine; beide Listen jederzeit aufrufbar und aenderbar (verschieben zwischen
  Take/Leave), aber NUR mit Typen, die schon auf der Liste stehen (kein freies Hinzufuegen beliebiger Gegenstaende). GEAENDERT 15.10.
  (Diskussion mit NaYceR, der eine feste 'nur das looten'-Liste wollte; Kevin waehlte meinen Kompromiss "ja klingt gut"): ZUERST NACH KATEGORIEN
  entscheiden (Kategorien wie im Storage-Reiter: Essen, Munition, Medizin, Werkzeug ... je Take/Leave), EINZELNE TYPEN koennen davon abweichen. Ein
  NEUER Typ uebernimmt automatisch die Einstellung SEINER KATEGORIE (die fruehere Regel 'Neues bleibt liegen, bis entschieden' ist damit
  ERSETZT), steht aber trotzdem LEUCHTEND oben -- und auch die KATEGORIE zeigt sichtbar, dass sie neue Typen hat ("das man direkt weiss in kategorie
  xy gibs jz neue items"), bis man sie angesehen hat. ESSEN (Kevin 15.10.: "bei essen muesste man aber auch entscheiden zwischen alles mitnehmen
  was nicht verdorben/verrottet ist"): fuer Essen ein Schalter 'Verdorbenes liegen lassen' -- je STUECK geprueft (FoodRules.Spoiled /
  Storage.FreshPiece, vorher updateAge), Verdorbenes bleibt liegen. PRAEZISIERT: "also mit son switch nur frisches oder alles" -> EIN Schalter
  mit zwei Stellungen 'Only fresh' / 'All'. Offen fuer den Plan: zaehlt angestandenes (stale, noch essbar) als frisch? Mein Vorschlag ja, Kevin
  beim Planen kurz bestaetigen lassen.
  FILTER (Kevin 15.10.: "und die liste soll auf eine filter liste haben damit man die items schnell findet und abaendern kann"): Suchfeld nach Name
  plus Kategorie-Filter (Form wie Vanillas Gegenstandsliste / unsere Kategorien), in beiden Listen.

- **ERLEDIGT seit v3.12.23 (Strg + Ziehen, client/BanditsNPCSideBtn.lua; Kevin 15.10.: "ist schon fertig") -- NICHT mehr als offen nennen.**
  **CREW-KNOPF VERSCHIEBBAR MACHEN (Kevins Ansage 24.09., Workshop-Wunsch):** Vorgabe bleibt wie JETZT -- fest an der
  Vanilla-Seitenleiste (Kind von `pd.equipped`, RosterPanel.lua:1076). Neu dazu: ENTSPERREN -> verschieben -> wieder SPERREN,
  Position pro Rechner in `NPCCrewClient.ini` (keine Weltregel, v3.7.30-Probe: wessen Ressource zahlt?). Vorlage steht fertig im
  Munitions-HUD (`BanditsNPCAmmoHUDButton`: `locked`, `_dragging`, DRAG_SLOP, moveWithMouse). FALLE v3.8.10: ausserhalb des
  Eltern-Rechtecks wird der Knopf gezeichnet, aber die Maus findet ihn nicht -- im entsperrten Zustand muss er frei im
  UI-Manager haengen, nicht als Kind der Seitenleiste.

- **KOMPOSTER-AUFTRAG FUER VERDORBENES (Kevin 28.09., 'merken wir uns fuer spaeter'):** der Sortierer sortiert
  Verdorbenes/Verbranntes weiter ganz normal unter Essen ein (so bleibt es). SPAETER bekommt der Komposter (Farming-Station,
  Hauptteil composter, Stations.lua:52/124) einen eigenen Auftrag: im Lager nach verdorbenem/verbranntem Essen suchen, es aus
  den Kisten holen und selbst in den Komposter legen. Frische-Frage = FoodRules.Spoiled / Storage.FreshPiece (v3.11.71).
  Auch die Zutatenkiste des Kochs einschliessen (dort bleibt Verdorbenes heute liegen). Vanilla-Komposter: ISCompost.lua
  (server/BuildingObjects) -- Mechanik vor dem Bau nachlesen. Nicht bauen ohne Kevins Auftrag.

- **TIERPFLEGER (Kevin 29.09.: 'fett recherche ... damit wir einen guten tierpfleger job einbauen koennen'):** Recherche
  FERTIG (29.09. 22:36, 7 Agenten inkl. Gegenpruefung), Bericht `_docs/tierpfleger_recherche.md`. Kern: Huhn/Truthahn/Kuh/
  Schaf/Schwein (+ Kaninchen); machbar Troege fuellen, Eier/Federn/Wolle/Mist sammeln, Stall ausmisten, Nester reinigen,
  Stalltuer (SP direkt, MP eigene Serverbefehle); NICHT machbar streicheln/fuehren/tragen/aus der Hand fuettern; Melken und
  Scheren nur als Nachbau (Vanillas Aufruf stuerzt mit Companion ab) = Kevins Wort. Falle: befruchtete Eier verlieren die
  Befruchtung im Manifest -> nie in die Tasche. Abschnitt 6 hat 12 offene Entscheidungen mit Empfehlung. NICHTS GEBAUT --
  erst Kevins Entscheidungen. ENTSCHIEDEN 29.09.: Streicheln unwichtig fuer den NPC (Vertrauen ist pro Spieler); MELKEN UND
  SCHEREN SIND GEWUENSCHT ('echt wichtige features') -> Nachbau-Plan per Workflow in `_docs/tierpfleger_melken_scheren.md`.
  ZONE ENTSCHIEDEN 29.09.: Vanilla-Tierzone (DesignationZoneAnimal, Lua-belegt getZone/getAnimalsConnected/
  getTroughsConnected/getHutchsConnected...), keine eigene Flaeche; MP-Sync der Zonen ungeprueft.
  MEHRERE ZONEN JE NPC + MEHRERE NPCS JE ZONE ENTSCHIEDEN 29.09. ('okay gut'): Reservierung je Trog/Nest/Tier (Modultabelle
  mit Frist); MP-Doppelgriff kann nichts verdoppeln (Server nimmt zuerst weg). Offen: Regeln je Zone oder global, eigener
  Tierpfleger-Reiter (meine Empfehlung: je Zone mit Basis-Vorgabe; Reiter wie Fishing).
  EIER-SCHALTER ENTSCHIEDEN 29.09.: je Zone 'Alle Eier sammeln' (Vorgabe AUS) -- an = alles sammeln trotz Hahn/Wartezeit;
  MP: befruchtete kommen als normale an; SP: koennten in der Kiste schluepfen (ungeprueft, in Stufe 1 testen, Tooltip sagt es).
  TOOLTIPS: jeder Regler/Schalter im Tierpfleger-UI bekommt einen Maus-Tooltip mit Wirkung und Folgen (Kevin 29.09.), 6 Sprachen;
  wo SP und MP sich unterscheiden, NUR den Satz des aktuellen Modus zeigen ('dann trenn das').
  BAU IN STUFEN ENTSCHIEDEN 29.09.: 1 = Zonen/Troege/Eier/Stall/Reiter, 2 = Melken+Scheren, 3 = Schlachten; jede Stufe
  einzeln bauen, pruefen, Kevin testet SP+MP, dann die naechste.
  UI-SKIZZE FREIGEGEBEN 29.09. ('ja so passt das'): links Zonenliste mit Warnungen, rechts Unterreiter Overview/Animals/
  All stats, Tierliste + Detailkarte; ECHTES TIERBILD statt Pfote (Liste: 2D-Bild, Detail: ein 3D-Portraet -- nur ein
  Renderer, v0.77.9). Beschrieben in _docs/tierpfleger_recherche.md Abschnitt 6.
  UI-PLAN 29.09.: eigener Reiter wie Fishing, Zonenauswahl oben nach Vanilla-Zonenname, Hauptseite nur Status, Regeln- und
  Futter-Fenster separat (wie Koederfenster), Regeln je Zone mit Basis-Vorgabe; ALL STATS je Zone gewuenscht (Eier, Milch,
  Wolle, Federn, Mist, Futter/Wasser, Ausmisten, Scheren, Schlachtungen, Geburten/Tode beobachtet). SCHLACHTEN: Kevin hofft
  darauf -- Recherche-Workflow w23djer73 -> _docs/tierpfleger_schlachten.md.
  KORREKTUREN 29.09. nachts (_docs/tierpfleger_alter.md), KEVIN MUSS NEU ENTSCHEIDEN: (a) Milch/Eier/Wolle hoeren im Alter
  NICHT auf, Tod schleichend (Gefluegel 10-14 d nach 'alt', Kuh/Schaf/Schwein 3-4,5 Monate) -> Alters-Vorgabe 100 % statt
  'knapp davor'; Hauptschalter Schlachten je Zone (Vorgabe aus) vorgeschlagen. (b) Eier: Stundenzaehler je Zone+Art statt
  fester 35/42 Tage. (c) befruchtete Eier schluepfen auch in Kisten als Kueken-Gegenstand (SP auch NPC-Tasche).
  Berichte fertig: tierpfleger_melken_scheren.md (13 Entsch.), tierpfleger_schlachten.md (10 Entsch.), tierpfleger_alter.md.
  SCHLACHT-REGELN ENTSCHIEDEN 29.09. ('bau die mit ein', falls Schlachten machbar): Hoechstbestand je Art (Maennchen+Aelteste
  zuerst), Hoechstzahl Maennchen je Art (Vorgabe 1), Alters-Regler (Vorgabe knapp vor 'alt'), geschuetzt: Jungtiere,
  Traechtige, Muetter mit Jungen, benannte Tiere. Alles je Zone. Bau erst nach den drei Berichten + Kevins Gesamt-OK.
  TROG-REGEL ENTSCHIEDEN 29.09. (Kevin: 'sonst laufen die ja nonstopp dahin'): Hysterese -- erst unter 75 % nachfuellen,
  dann bis 100 %, danach warten; Futter und Wasser getrennt, Vorgabe 75/100, einstellbar je Zone im Job-Reiter; ohne
  Nachschub nicht loslaufen, einmal sagen und warten.
  EIER ENTSCHIEDEN 29.09. (Kevin: 'ja mach das so'): steht ein Hahn (bzw. Truthahn-Hahn, je Art getrennt) in der
  (verbundenen) Zone, bleiben die Eier liegen und schluepfen wie in Vanilla; ohne Hahn sammelt der Pfleger sie in die
  Ertragskiste, ohne Zuweisung in den Posteingang -- von dort sortiert der Sortierer sie wie jedes Essen. Grund: Befruchtung
  ist aus Lua nicht belegt lesbar, MP-Ablieferung muenzt neu. 14-TAGE-REGEL ENTSCHIEDEN 29.09. (Kevin: 'ja plan das so
  ein'): nach Entfernen des Hahns sammelt der Pfleger erst 14 Spieltage spaeter wieder (Befruchtung haelt 336 h), sonst
  schluepft im SP ggf. ein Kueken in der Kiste. KORREKTUR (meine, 29.09.): 14 Tage reichen NICHT -- ein am 13. Tag gelegtes
  befruchtetes Ei bleibt befruchtet bis zum Schluepfen (21/28 d x Sandbox) -> sicher ~35/42 d, oder genau ueber das Ei-Alter
  (Workflow w2yn7470m -> _docs/tierpfleger_alter.md, auch Alters-/Nutzlos-Grenzen fuer die Schlacht-Regler). Der Zeitpunkt 'zuletzt Hahn gesehen' muss je Zone und Art GESPEICHERT sein
  (Site-Daten, keine Sitzungstabelle -- sonst beginnt die Frist nach jedem Laden neu bzw. gar nicht).

**How to apply:** Neue Community-Wuensche hier und in offene_arbeit.md anhaengen, nicht bauen, bis Kevin es beauftragt.
Wenn Kevin "was koennten wir als naechstes bauen" fragt, diese Liste nennen. Siehe [[kevins-zwei-rote-linien]].

- **Essens-Tooltip wie "Show Food Stats" mit Schalter** (Kevin 30.09., Bild: Naehrwerte, Koch-/Brennzeit, Frische in Tagen/Stunden; frueher "Frische-Tooltip"): beim Mouseover ueber jedes Lebensmittel "noch X Tage frisch" anzeigen; nach dem Upload v3.12.18. Dazu Name/Zutatenliste im Manifest (Name belegt, Zutatenliste braucht Kevins Wort). Details offene_arbeit "FRISCHE-TOOLTIP".

- **Stationen Stufe 4 mit schoeneren, grossen Modellen** (Kevin 02.10., Idee): alte Stationen NICHT umbauen (Platz, Mehrkachel-Fehler wie die verdrehten Werkbaenke, MP-Serverweg), sondern eine neue Ausbaustufe mit mehr Rezepten. Knackpunkte: Modelle viel groesser -> viele Kacheln; Bau aller Teile ganz oder gar nicht (Vorschau prueft alle Kacheln frei, Material zurueck bei Fehlschlag), Abbau mit Nachweis je Teil, SpriteGridPos-Reihenfolge je Teil pruefen (Lehre v3.12.20). Kevins Loesung fuer die Groesse (02.10.): Stufe 4 NICHT an Ort und Stelle ausbauen, sondern FREI PLATZIEREN wie eine neue Station; zum Umstellen ein eigener Befehl 'Station versetzen' (sauber abbauen -> Bausatz-Gegenstand mit Typ+Stufe -> wieder platzieren), NICHT Vanillas Aufheben freigeben (macht ein Moebelstueck, Stationsdaten weg).

- **KOCH-REZEPTE FUER ALLES AUS DER TIERHALTUNG -- NACH DEM TIERPFLEGER (Kevin 04.10.: "wir brauchen neue rezepte aber das kannste
  dir merken fuer wenn der animals keeper fertig ist, dann brauchen wir rezepte fuer alles was man bekommen kann, auch fleisch
  vom schlachten etc"):** Anlass: rohe Eier sind DangerousUncooked (food.txt Base.Egg) -> FoodRules erlaubt nur gekocht
  (FR.RawOnlyCooked/rawPiece), der Koch hat KEIN Ei-Rezept (grep Base.Egg in shared: 0). Umfang: Eier (Huhn/Truthahn: gekocht,
  Ruehrei/Omelett/Spiegelei -- Vanilla EggBoiled/EggScrambled/EggOmelette/EggPoached), Fleisch aus dem Schlachten (alle Tierarten),
  Milch (Kuh/Schaf), ggf. weitere Tierprodukte. Vorher Vanilla-Rezepte/Kochwege nachlesen (Alter erben, verdorben tabu --
  [[koch-rezepte-entscheidung]]). Erst NACH dem Tierpfleger bauen, mit Kevins Wort.

- **TOTE TIERE IN DER TIERZONE -- FUER STUFE 3 (Kevin 06.10. abends: "ja" auf meinen Vorschlag):** heute entfernt sie niemand,
  v3.12.63 zeigt nur die Tot-Warnung. Wunsch: die Pflegerin zerlegt FRISCHE Kadaver (Fleisch zur Ertragskiste), holt danach die
  Knochen vom Skelett, und vergraebt/entsorgt VERROTTETE. Vanilla-Wege (gelesen, nicht gespielt): ISButcherAnimal (Boden) bzw.
  Schlachthaken; ButcheringUtil.lua:153-156 macht aus dem zerlegten Kadaver ein blutiges Skelett, :91-92 + ISGetAnimalBones.lua
  holen die Knochen vom Skelett; animalRotStage > 0 -> Fleisch kommt verdorben (:299-308); Kueken/Huehner im Stall ueber
  ISHutchGrabCorpseAction; VERBRENNEN JA (Kevin 06.10.: "verbrennen geht ... fake feuer"), aber ueber dasselbe kosmetische Feuer
  ART wie beim Leichen-entsorgen (Sprite + Licht, kein IsoFire) -- verrottete Kadaver vergraben ODER verbrennen. Die Feuerstelle
  wird NICHT geteilt (Kevin 06.10.: "corpse cleanup macht man ueberall, nicht nur in der base"): die Tier-Brennstelle ist eine eigene
  an der Basis/Tierzone (genauer Ort noch offen). FAKE-FEUER = BILD + LICHT + RAUCH + TON, kein echtes Feuer (Kevin 06.10.).
  Rauch: Vanilla hat IsoFireManager.StartSmoke(getCell(), sq, true, 100, 500) (server/ClientCommands.lua:17, Debug-Befehl) --
  Lua-belegt, aber vermutlich ein IsoFire im Rauch-Modus: VOR dem Bau im Jar pruefen, ob er sich ausbreitet, Schaden macht oder
  Bandits' Feuer-Pruefung (ManageOnFire) ausloest; sonst eigener Rauch (Partikel/Sprite). Ton: Vanillas Feuerknistern, Name vor
  dem Bau nachschlagen. Gehoert zur Schlacht-Stufe
  (_docs/tierpfleger_schlachten.md), erst nach Kevins Tests von Stufe 1.

- **REZEPTE FUER ALLES, WAS DER TIERPFLEGER ZUM ARBEITEN BRAUCHT (Kevin 07.10.: "merk dir mal das wir noch rezepte einbauen muessen um
  alle dinge zu bauen die der animal keeper zum arbeiten braucht mit vanilla oder realistischen rezepten"):** Werkzeug und Verbrauch der
  Pflegerin aus unseren Stationen herstellbar machen: Harke/Laubharke (Base.Rake/LeafRake), Sense/Handsichel (Base.Scythe/HandScythe,
  geschmiedete Varianten), Putzzeug (Base.Mop, Base.Broom, Base.Broom_Twig, Base.Sponge, Bursten), Eimer, ggf. Futter/Heu und Troege.
  Vorlage: Vanillas eigene Rezepte (scripts/generated/recipes, craftRecipe) nachlesen und uebernehmen; wo Vanilla keins hat, ein
  realistisches bauen. Station je Rezept (Schmied fuer Metall, Zimmerer/Schneider fuer Holz/Stoff). Erst nach der Fix-Version, mit Kevins
  Wort zur Liste; Regel 'jedes Rezept braucht Animation + Ton' ([[animation-und-ton-je-arbeitsschritt]]).
- **TIERHALTUNGS-SKILL FUER NPCS (Kevin 07.10., Alternativvorschlag zu 'Karte zeigt immer alles'):** die Pflegerinnen bekommen einen Skill 'Tierhaltung' (neuer Schluessel in brain.skills, shared/BanditsNPCSkills.lua -- das System gibt es schon), XP je Arbeitsschritt; die Tierkarte zeigt so viel, wie die HOECHSTE Stufe der gerade zugewiesenen Pflegerinnen erlaubt (Vanillas Stufenregeln, ISAnimalUI). Aufwand maessig (ein Skill-Schluessel, XP-Stellen, Anzeige, 7 Sprachen, Karten-Riegel). ENTSCHIEDEN (Kevin 07.10.): der Skill bestimmt NUR, was die Karte zeigt -- kein Tempo-/Stress-Effekt ('arbeiten tut er schon schnell genug'). Erst nach Fix-Version + Stufe 2, bis dahin zeigt die Karte alles (E28).
- **STREICHELN DURCH DIE PFLEGERIN (Kevin 07.10.):** Pflegerin streichelt gestresste Tiere (Pose + Ton, wenn vorhanden), Stress sinkt UND das Vertrauen steigt fuer den NPC-BESITZER. Weg: Vanillas animal:petAnimal(character) ist Lua-belegt (shared/TimedActions/Animals/ISPetAnimal.lua:70/:88) und nimmt den Charakter als Parameter -> mit dem IsoPlayer des Besitzers aufrufen (MP: auf dem Server, Besitzer muss online sein; offline nur changeStress, Lua-belegt ISShearAnimal). JAR GELESEN 07.10. (42.21, disasm IsoAnimal.petAnimal(IsoPlayer)): auf einem MP-CLIENT laeuft nur player.petAnimal() (also SP/Server rufen); Riegel petTimer > 0 (Abklingzeit je Tier, gesetzt Rand(15000,25000) - Tierhaltung*200); changeStress(Rand(-11,-7) - Tierhaltung des Spielers); Vertrauen des Spielers + Rand(2,7) bis 100 (setDebugAcceptance, Lua-belegt ISAnimalContextMenu.lua:614); Spieler bekommt Tierhaltungs-XP Rand(5,10) (Server: GameServer.addXp); KEINE Abstandspruefung. Danach IsoPlayer.petAnimal(): hoechstens einmal je Spielstunde senkt es beim SPIELER Stress (0,15-0,35), Unglueck (15-35) und Schmerz (15-35) -- auch wenn er weit weg ist. ENTSCHIEDEN (Kevin 07.10., gegen meine Empfehlung 'nur fuers Tier'): VOLLE VANILLA-WIRKUNG -- animal:petAnimal(Besitzer) wie Vanilla, der Spieler bekommt XP und die Laune-Wirkung ('die NPCs nehmen dir das ja weg', und es geht ohnehin nur in der Naehe, weil die Pflegerin nur bei geladenem Bereich arbeitet); dazu levelt die PFLEGERIN selbst Tierhaltung (NPC-Skill, siehe Eintrag Tierhaltungs-Skill). Fuer Stufe 2 vorgemerkt.
  STREICHELN ANIMATION + TON (Kevin 07.10.: 'schoen mit Ton + Animation wie als ob der Spieler es tut'): Vanilla ISPetAnimal setzt am Spieler setVariable('petanimal', true) + setVariable('animal', <Tierart>) (Spieler-Animset, fuer einen Zombie nicht da) -> eigener Bump-Knoten aus Vanillas Streichel-Clip je Tierart wie BNScythe; am TIER Lua-belegt animal:setVariable('idleAction','petting') + getBehavior():setBlockMovement(true) (ISPetAnimal.lua:36/43), Ende clearVariable + setBlockMovement(false); Dauer 3000 ms (emulateAnimEventOnce 'pettingFinished'), danach petAnimal(Besitzer). Ton: in ISPetAnimal kein playSound -- im Clip/AnimSet nach Sound-Ereignissen suchen, sonst eigener passender Vanilla-Ton.
- **KEVINS RESTLISTE TIERPFLEGER (07.10.):** Schlachten, Tiere ZERLEGEN (Kevin 07.10. korrigiert: "verlegen" war ein Verschreiber, gemeint ist das Zerlegen nach dem Schlachten; beides mit Ton + Animation + Werkzeug) und die Schlacht-Einstellung 'ab Alter X' bzw. 'ab Bestand N, Aelteste zuerst' (Beispiel: ab 20 Huehnern). Deckt sich mit den Schlacht-Regeln vom 29.09. (Hoechstbestand je Art mit Maennchen+Aelteste zuerst, Hoechstzahl Maennchen, Alters-Regler, geschuetzt Jungtiere/Traechtige/Muetter/benannte; Bericht _docs/tierpfleger_schlachten.md). NEU zu klaeren: TIERE VERLEGEN -- die Recherche 29.09. hielt Fuehren/Tragen mit einem Companion fuer nicht machbar (Vanilla-Aktionen fuer Spieler) -> eigene Recherche wie beim Scheren-Nachbau. Reihenfolge: Fix-Version -> Stufe 2 (Melken, Scheren, Streicheln) -> Stufe 3 (Schlachten, tote Tiere, Verlegen) -> Rezepte fuer Pfleger-Werkzeuge -> Koch-Rezepte fuer Tierprodukte.
  ZUCHT-MAENNCHEN SCHUETZEN (Kevin 07.10.: 'man muss auch den Hahn z.B. schuetzen, ein maennliches Tier, das fuer die Paarung gebraucht wird'): neue Regel je Zone und Art 'mindestens N Maennchen behalten' (Vorgabe 1) -- das letzte zuchtfaehige Maennchen wird von KEINER Schlachtregel genommen (weder Hoechstbestand 'Maennchen zuerst' noch Alters-Regler). Sinnvoll dazu: ist ein jüngeres erwachsenes Maennchen da, darf das alte gehen (Vorschlag, Kevin fragen). Ergaenzt die Regeln vom 29.09. (Hoechstzahl Maennchen = Obergrenze, das hier = Untergrenze).
- **WORKSHOP-WUNSCH 10.10. (飞天。, spielt mit Week One):** (a) Sandbox-Einstellung fuer die ANWERBE-SCHWIERIGKEIT (heute reicht ein Essen/Wasser oder gar nichts), (b) OBERGRENZE fuer die Crew-Groesse, (c) Taste (z. B. V) zum Schliessen des Outfit-/Aussehen-Fensters, weil im First-Person-Modus (fremde Mod) die Maus das Fenster nicht schliessen kann. Heute gibt es weder (a) noch (b) als Option (sandbox-options.txt gegrept). Kevin 10.10.: "kannst du dir ja merken, aber ob wir das echt machen mal gucken" -- NICHT bauen ohne Auftrag; Antwort im Workshop ohne Zusage gegeben.
- **Schlachten/Zerlegen Recherche 07.10.:** `_docs/recherche_zerlegen_2026-10-07.md`. v1 nur Gefluegel/Kaninchen am Boden, Server toetet (setHealth 0) und zerlegt per Nachbau von ButcheringUtil, Ware direkt in die Ertragskiste; Grosstiere spaeter (Haken braucht IsoPlayer).

- **AUF DER LISTE SEIT 15.10.2026 (Kevin: "schreib auf die liste noch ..."): SANDBOX MAXIMALE ZAHL REKRUTIERTER NPCS, Vorgabe 30, einstellbar
  1-100.** Dazu der BEACON: heute rufen die Beacon-Stufen je eine Zahl NPCs herbei; kuenftig daraus ERRECHNEN -- die HOECHSTE Stufe ruft genau die
  Sandbox-Zahl (Vorgabe 30 -> 30 auf der Hoechststufe im Beacon-Fenster), niedrigere Stufen anteilig (Rechnung beim Planen vorschlagen; heutige
  Stufenzahlen vorher im Code nachlesen, client/BanditsNPCBeacon.lua, client/ISUI/BanditsNPCBeaconWindow.lua). Grenze beim Anwerben an der
  ENGSTELLE und im MP auf dem Server pruefen; Bestand ueber der Grenze wird nicht entlassen, nur keine neuen (vorgeschlagen, Kevin bestaetigen).
  Eintrag darunter (12.10.) ist dieselbe Sache -- jetzt mit Zahlen. Position: Platz 7, direkt vor PvP, ganz am Ende (Kevin 15.10.).
  **SANDBOX: HOECHSTZAHL CREW-NPCS JE SPIELER (Kevin 12.10., 'merk dir mal'):** neue Sandbox-Option, wie viele angeworbene NPCs ein
  Spieler hoechstens haben darf. Vor dem Bau: alle Anwerbe-Tueren finden (Interact.Recruit/FulfillWith, Claim, Spawn-Menue) und die Grenze
  an der ENGSTELLE pruefen, im MP auf dem Server (ein Client-Riegel reicht nicht); was mit Bestand ueber der Grenze passiert (nichts
  entlassen, nur keine neuen) mit Kevin klaeren. Sandbox-Regel aus CLAUDE.md 4.6: die Option muss im Lua gelesen werden.
- **AUF DER LISTE SEIT 15.10.2026, Platz 8 ganz am Ende, direkt nach 'Maximale Crew'; Sandbox-Schalter STANDARDMAESSIG AUS (Kevin 15.10.: "und pvp in sandbox standardmaessig deaktiviert") ("und danach kommt auf die liste PVP sandbox option wenn aktiviert schiessen
  die npc's alle anderen spieler ab die nicht in der gleichen gilde oder was es im spiel gibt ist"):** Sandbox-Schalter PvP; an = Companions greifen
  JEDEN anderen Spieler an, der nicht in derselben Gruppe wie ihr Besitzer ist -- im Spiel heisst das FRAKTION (Vanilla Faction, ggf. auch
  Safehouse-Mitglieder; beim Planen belegen, welche Abfrage es in Lua gibt). Nur MP sinnvoll. Details/Risiken im Eintrag darunter.
  **SANDBOX: PVP -- CREW SCHIESST AUF FREMDE SPIELER (Kevin 12.10., 'nur als idee, ka ob das so leicht geht'):** Option, dass Companions
  fremde Spieler (nicht Besitzer, nicht Verbuendete) angreifen, wenn PvP an ist. Ungeprueft, wie schwer: Bandits' Zielwahl laeuft ueber
  eigene Caches (BanditZombie.CacheLight) und hat fuer feindliche Banditen schon Spieler-Ziele; Schaden an Spielern im MP muss ueber den
  Server bzw. Vanillas PvP-Regeln (SafetySystem, Fraktionen) laufen; Friendly-Fire-Schild (Ausnahme 5) betrifft die Gegenrichtung.
  Erst Machbarkeit recherchieren, dann Kevin fragen.

- **TIERE UMSETZEN (Zone A -> Zone B) -- NUR MERKPOSTEN (Kevin 12.10.: aus Stufe 3 gestrichen, 'ja streich das mal raus'):** der Punkt
  stammte aus seinem Verschreiber 'verlegen' (gemeint 'zerlegen'). Moeglicher Nutzen: Maennchen trennen, Jungtiere in ein eigenes
  Gehege, ueberfuellte Zone entlasten. Riskantester Teil (Tier muss durch ein offenes Tor, keines darf entlaufen). Nicht bauen und
  nicht von mir aus anbieten; nur nennen, wenn Kevin fragt, was man noch bauen koennte. Recherche-Stand ggf. im Stufe-3-Plan
  (`_docs/tierpfleger_stufe3_plan_2026-10-12.md`) und in `_docs/plan_freitag_2026-10-09.md` (Stufe 3a/3b).

- **STORAGE-REITER: WELCHE KATEGORIE IST VOLL? -- OFFENER PUNKT (Kevin 12.10.2026 spaet, "was mich auch nervt das kannste dir noch
  merken als offenen punkt"):** wenn die NPCs sagen, es sei kein Platz mehr fuer etwas, soll im Storage-Reiter OBEN IN DER MITTE
  stehen, fuer welche Kategorie Lagerplatz fehlt, "damit man aufruesten kann ohne zu raetseln was fehlt". Kein Feature-Wunsch
  fuer irgendwann, sondern ein Aergernis -- nach Tierpfleger Stufe 3 einplanen und Kevin dann anbieten. Details zur Bauform im
  Uebergabeblatt `_docs/uebergabe_2026-10-12.md` Punkt 6b.

SELBSTTEST AUF KNOPFDRUCK (Kevin 16.10.2026 ~00:20: "das muessen wir mal testen das waer ja krank gut!!!" -- er testet ungern selbst,
"ich will lieber ergebnisse sehn"): Debug-Konsolenbefehl baut die Testlage selbst auf, Crew arbeitet, Konsole schreibt PASS/FAIL je Schritt,
Claude liest es. Nur Sichtpruefungen bleiben bei Kevin. Kommt in die Bauplan-Fabrik am 16.10. (_docs/uebergabe_2026-10-16.md Teil A Punkt 10). DAZU FERNSTEUERUNG (Kevin ~00:30 "jaa ... ich lass mich mal ueberraschen"): im Debug-Modus liest die Mod eine Befehlsdatei in
Zomboid\Lua\, die Claude schreibt -> Claude startet die Selbsttests selbst, Kevin laedt nur den Spielstand; nur feste Testbefehle, kein beliebiges Lua.

- **ZEITRAFFER TROTZ CREW (Kevin 16.10. ja, Workshop-Frage von 柒掌柜):** Vanilla setzt im SP den Zeitraffer zurueck, sobald ein sichtbarer IsoZombie <= 4 Kacheln (bei >4 sichtbaren Zombies 7) auf derselben Etage steht (Jar IsoPlayer.updateLOS Offset 935-1011: GameTime.setMultiplier(1) nur ohne GameClient.client, SpeedControls.SetCurrentGameSpeed(1) nur ohne GameServer.server; Abstand IsoUtils.DistanceTo, kein Quadrat). Crew zaehlt mit. Idee: wenn nur Crew und kein echter Zombie die Ursache ist, vorherigen Zeitraffer wiederherstellen (Form wie Panik-Korrektur shared/BanditsNPCPanic.lua). Nur SP relevant (MP-Zeit macht der Server). Platz: nach dem Selbsttest, Kevin hat keinen festen Platz genannt.
  KEVIN 16.10.: bei einem ECHTEN Zombie muss der Zeitraffer weiter stoppen (*"sonst stirbt man instant"*). Also nur die EIGENE angeworbene Crew ausnehmen; echte Zombies, feindliche Bandits und Neutrale zaehlen weiter, und die Pruefung nimmt eine OBERMENGE der Engine-Regel (groesserer Radius, ohne Sichtpruefung), damit im Zweifel gebremst wird.

- **POLSTERUNG ZAEHLT FUER CREW-SCHUTZ (Kevin 16.10. ja: *"wenn du das tun kannst mach es aber bugfrei sp/mp"*, Workshop-Frage eee):** heute rechnet armorTable/H.Mitigate (client/BanditsNPCSkillsHooks.lua ~1063-1160) ueber zombie:getBodyPartClothingDefense -- die Engine baut fuer Zombie-ItemVisuals ein FRISCHES Kleidungsstueck (InventoryItemFactory.CreateItem, Clothing.getDefForPart), Flicken/Polsterung fehlen. Die Flicken selbst sind seit v3.10.48 in brain.wornRec gespeichert (BanditsNPC.CaptureCloth). Ziel: Polsterung je Koerperteil in Anzeige UND Schadenswurf mitrechnen, Deckel 0,60 je Teil bleibt. Offen fuer den Plan: Schutzwert je Flicken (Vanilla haengt am Schneider-Wert des Aufnaehers, nicht auslesbar) -- z. B. fester Wert je Stoffart. Platz: nach dem Selbsttest (kann dann damit getestet werden).

- **JOB "CLEANER" (Kevin 17.10. abends, ans Ende des Fahrplans, B12):** um den Beacon so viele Kacheln wie gut machbar sauber halten -- Blut
  schrubben (wie Stall-Putzen, Mop/Putzzeug aus dem Lager) und Zombie-Leichen finden und an der Brennstelle der Tiere verbrennen. Kevin:
  *"der soll stueck fuer stueck die Umgebung scannen und nicht alle Felder aufeinmal das es ULTRA LAGGT! das ist wichtig, soll sp/mp funktionieren"*.
  NICHT mit Bauplan 01 zusammenlegen (Kevin: Leichen entsorgen macht man meist ausserhalb der Basis); eigener Basis-Job, nutzt aber 01s Bausteine, kommt nach 01.
- **GENERATOREN NACHFUELLEN UND REPARIEREN -- CLEANER WIRD "HAUSMEISTER" (Kevin 05.11.2026 waehrend des SP-Tests v3.14.48: *"merk dir mal was sehr gute idee fuer nen npc update. Generatoren Nachfuellen und reparieren. vllt fuer den cleaner job das man ihn irgentwie hausmeister oder so nennt der dann alles moegliche kann?"*):**
  der Cleaner-Job (Fahrplan B12/B12b) soll als Allround-Job der Basis gedacht werden (Arbeitsname Hausmeister/Caretaker, EN-Name noch offen): Blut schrubben, Leichen, Bodengegenstaende, Trash -- PLUS Generatoren der Basis mit Benzin aus dem Lager nachfuellen und reparieren (Zustand). Noch nichts entschieden oder recherchiert; vor dem Bau Vanilla-Wege belegen (Generator-Fuellen/Reparieren sind Spieler-TimedActions, MP ueber den Server), Kevins Wort zu Name und Umfang holen. Kommt nach dem Upload und nach Pluendern, nicht vorziehen.
- **UNABHAENGIG VON BANDITS (Kevin 05.11.2026 abends, nach dem Bandits-Update-Aerger: *"koennten wir wenn ich mit der mod komplett zufrieden bin probieren das wir von der bandits mod unabhaengig werden? irgentwie so eine interne version wo nur wir arbeiten und die leute bekommen weiterhin die abhaengige bis die andere klappt?"*):**
  gemessen 05.11.: 3361 Aufrufstellen in Bandits (132 verschiedene Funktionen), Bandits selbst ~24.500 Zeilen Lua + 200 eigene Animationsknoten (common/media/AnimSets/zombie/bumped). Bandits liefert Gehirn-Speicher + MP-Sync (Cluster), Aufgaben-Dispatcher + Gehen (ZAMove), Kampf, Spawnen, Aussehen, Waffen in der Hand. Nicht kopierbar (fremder Code, nur mit Erlaubnis des Autors) -> Nachbau. Weg wie Kevin vorschlaegt: interne Fassung (eigener git-Zweig, eigene mod id, nie hochgeladen), Spieler behalten die abhaengige. Schritt 1 Zwischenschicht TC.Engine.* (lohnt sich auch ohne Ende: ein Bandits-Update trifft dann nur eine Stelle), dann Stueck fuer Stueck ersetzen. Schaetzung (nicht gemessen): Monate, viele Wochenlimits. Erst wenn Kevin die Mod fertig findet (nach Pluendern usw.); vorher eine Lese-Analyse fuer einen echten Plan anbieten.
- **AUTOS REPARIEREN, AUTOMATISCH WIE VANILLA, MIT EIGENEM SKILL (Kevin 05.11.2026, direkt nach der Hausmeister-Idee: *"hab auch schon ueberlegt ob jemand autos reparieren koennen soll sowie in vanilia nur automatisch ;D und mit eigenen skill ^^"*):**
  eine Crew-Figur repariert Fahrzeuge der Basis selbststaendig (Teile tauschen/reparieren wie Vanillas Mechanik, Teile und Werkzeug aus dem Lager), mit eigenem Crew-Skill (wie Animal Care beim Tierpfleger). Offen: eigener Job oder Teil des Hausmeisters; Beruf nur, wenn es Station + Rezepte gibt (CLAUDE.md Abschnitt 5 "Ein Auftrag ist kein Beruf"). Vor dem Bau Vanilla-Mechanik belegen (ISInstallVehiclePart/ISRepairVehiclePart o. ae., MP ueber den Server), Kevins Wort zu Umfang. Nach Upload und Pluendern.

- **PERSOENLICHER MEDIZINER (Kevin 17.10. abends, "mein letzter Plan", Fahrplan B13):** je NPC Knopf ein/aus, Verbandszeug muss in IHREM
  Inventar sein; ist der Spieler verletzt, sagt sie GROESSER als normal ueber dem Kopf etwa "stand still, I'm patching you up", laeuft hin und
  behandelt ihn. Dazu neuer Skill Medizin mit echter Wirkung (hoeher = schneller und besser, so weit umsetzbar). SP und MP.
  NACHTRAG: auf Mediziner holt sie sich in Basis-Reichweite automatisch das Job-Zeug (je Sorte ~5-10, Tasche nie voll); Auto-Ablegen legt es nicht weg.

- **JOB "FORAGER" (Kevin 18.10., Fahrplan B14):** eine Crew-Figur sammelt wie Vanillas Foraging (Essen, Kraeuter, Beeren ...) in einer Flaeche und bringt es ins Lager; Anlass Workshop-Frage von CallMeBond (forger/forager). Noch kein Bauplan.
- NEU 21.10.: Leichen entsorgen mit echter SCHLEIF-Animation (Kevin; Vanilla pickUpCorpse(body,'BwdDrag') an der Crew = IsoZombie, ungeprueft; A-Life ist KEINE Vorlage -- erkennt nur vom Spieler gezogene Leichen). Nach dem Upload mit wenigen Lese-Agenten pruefen.
  - Kevin 21.10.: Schleifen BLEIBT ERSTMAL WEG (sicherer). Spaeter pruefen: (a) echtes Vanilla-Ziehen (Greif-Mechanik belebt Leiche kurz als Zombie -- Bandits/Crew greifen an, Abbruch-Risiko, MP ungeprueft), (b) reine Optik-Attrappe (Leiche bleibt liegen bis zum Verbrennen).

**Kevin 01.11.2026 (nach dem Upload v3.14.27), Farmer huebscher machen:** im Fields-Reiter je Feld-Kasten ein ICON der Saatpackung der angebauten Sorte (z. B. Karotten-Packung), damit man die Sorte sofort sieht. Machbar: Vanilla zeichnet Item-Icons in der UI (Textur des Gegenstands-Skripts); die Packungstypen je Sorte kennt Farm.lua (*BagSeed*). Noch nicht gebaut, Kevin sammelt weitere Ideen.

Kevin 04.11.: Strafe bei leerem Essen/Trinken -- HP-Verlust (auch Folgende), Niederschlag bis gefuettert, sterblich nur bis 1 HP, erst nach laufendem Auftrag und nur wenn Lager leer. Entwurf und Kevins Wortlaut als Nachtrag in `_docs/bauplaene_2026-10-16/06_streik.md` (unten). Noch NICHT entschieden; Bau nach dem Streik, auf sein Wort.
ENTSCHIEDEN 04.11. (Hunger-/Durst-Schaden): ZWEI Sandbox-Schalter (Streik + Schaden), beide Vorgabe AN; nur Unsterbliche liegen (bei 30 %, vorhandener Niederschlag), Sterbliche laufen mit 1 HP weiter (nichts Neues; weder Hunger noch Durst toeten je); Spruch + Kopfanzeige; Hunger/Durst nicht gestapelt; 100 % -> 1 HP in ~10 min Echtzeit. Einzelheiten im Nachtrag von 06_streik.md. Bau zusammen mit dem Streik.

**NEU 06.11.2026 (Kevin): NPC-Verlauf ("Log"-Reiter im NPC-Fenster).** Kevin: *"npc verlauf was hat er zuletzt gemacht alles protokoliert, hat ware abgeliefert etc ... vllt auch mit sowas wie 'wurde vom teleport waechter teleportiert' etc das man leichter bugs erkennt"*. Idee: je Figur die letzten ~30-50 Ereignisse mit Spielzeit -- Ware abgeliefert/geholt (Typ x Anzahl, Kiste), Job begonnen/beendet + Grund, gegessen/geschlafen, Kampf/niedergeschlagen/aufgeholfen, Waechter-Teleport/Unstuck/Herholen, Sprueche ('No room left' usw.). Nutzen: Spieler sieht, warum sie nichts tut; Fremdberichte koennen den Verlauf kopieren (Bugs leichter). Bauhinweise (ungeprueft): kleiner Ringpuffer in einer MODULTABELLE je uid (nicht am Gehirn -- kein Sync-Ballast, keine Zeitbombe v3.7.27), Quelle = die vorhandenen Stellen, die heute [TC-...]-Zeilen schreiben (eine Funktion BanditsNPC.History.Add), MP: lebt auf dem Rechner, der rechnet (Besitzer/Hoheit) -> fremde Rechner sehen nichts oder Server-Kopie; ueber Laden: nur Sitzung oder kleiner Teil im Roster. Text 7 Sprachen. Erst NACH dem Upload v3.14.51 einplanen.

**NEU Kevin 06.11. ~23:00, BAUAUFTRAG IM BLUEPRINT-MODUS:** *"man tut quasi in einen blueprint modus ein haus bauen das kostet keine resourcen ... so blau markiert und man kann es ausblenden und einblenden lassen, und dann wenn man einen arbeiter zuweisst faengt der an die resourcen zu holen und es genauso zu bauen wie der blueprint sagt geht das?"* Antwort: ja, vermutlich, grosses Feature (Schaetzung Farmer-Groesse, 6-10 Versionen, ungeprueft). Kevin dazu: *"merk dir das mal das kommt nicht direkt danach irgentwann aber mal waere cool"* -> KEIN fester Platz, NICHT direkt nach dem Pluenderer, nur auf sein Wort, nicht von mir aus vorschlagen. Belegt am 06.11.: blauer Geist `sprite:RenderGhostTileColor(x, y, z, r, g, b, a)` (Vanilla server/BuildingObjects/ISBuildCursorMouse.lua:23, ISBuildIsoEntity.lua:100); Weltobjekte setzen ueber unsere Server-Tuer PlaceObject (server/BanditsNPCBuildServer.lua); Bandits hat Bau-Aktionen (ZABuildFloor, ZAPlaceItem); Beruf Builder gibt es. Offen, vor dem Bau per Machbarkeitspruefung klaeren: ob eine Figur Vanillas Bau-Logik (ISBuildIsoEntity/BuildRecipe, an den Spieler gebunden) nutzen kann oder wie Waende identisch entstehen (Thumpable-Werte, Tuerrahmen), Reihenfolge und Erreichbarkeit (Boden vor Wand, Obergeschoss, Treppe, sich einmauern), Materialreservierung, halb fertiger Bau beim Speichern, MP.

**NEU Kevin 06.11. ~23:05, AUTO-TURRET (nur gefragt, wie schwer):** *"du gibst denen ein auto-turret ins inventar und die koennten das z.b unterwegs auf und abauen und im turret ist munition gespeichert ... ballert das alle zombies/bandits weg ... super base verteidigung, oder ein turret wo die npcs dran stehn muessen und es dann erst schiesst"*. Meine Einschaetzung (ungeprueft, kein Bau): BEMANNT rund 2-3 Versionen (Station plus Figur, nutzt Bandits-Kampf, Munition am Brain, BanditsNPCHoldGround); AUTOMATISCH rund 4-6 Versionen. Schwer daran: BanditUtils.Hit(shooter, item, victim, ...) braucht einen Schuetzen, im MP rechnet der Server keine Zombies (genau ein Client muss feuern), die Mod hat keine eigenen Kacheln oder Waffenmodelle (.pack fehlt, Bild/Modell noetig), laeuft nur im geladenen Bereich. Kevin bevorzugt die bemannte Variante: *"die variante mit npc der dran steht ist halt auch nicht so OP"*. Modell: keine Vanilla-Vorlage gefunden; technisch moeglich per Blender-Python (bpy) im Hintergrund, Vorschaubild rendern und selbst ansehen, Export fuer PZ; Blender portabel nach Tools, nur mit Kevins Ja zum Download; Massstab und Sitz im Spiel erst bei seinem Test. Kein fester Platz, nur auf sein Wort.

**TURRET MIT STUFEN UND RAKETEN, Kevin 06.11. ~23:15 (nur gefragt):** *"sentry-gun ... 2fach upgraden ... schiesst sogar raketen ... fliegendes projektil mit explosion + ton + AOE dmg + alle zombies die getroffen sind gehn in flammen auf ... ohne das der ganze server abrennt"*. Einschaetzung (ungeprueft, kein Bau): machbar, obendrauf rund 3-4 Versionen; eigenes Modell und eigene Toene, keine Team-Fortress-Assets. Jar-Beleg 06.11. (42.21): ein brennender Charakter LEGT FEUER, IsoGameCharacter.SpreadFire aus updateInternal (nur SP, FireSpread an, Rand(3000 je Bildrate) < fireSpreadProbability, Vorgabe 6 -> IsoFireManager.StartFire), auf dem Server SpreadFireMP ueber IsoFireManager. Gegenmittel: setFireSpreadProbability(int) ist public, 6 Byte, je Figur, KEINE Lua-Fundstelle -> braucht Kevins Wort als Ausnahme nach CLAUDE.md Abschnitt 3; SpreadFireMP vor dem Bau ganz lesen. SetOnFire belegt nur DebugContextMenu.lua:677. Nicht IsoFireManager.explode rufen (legt Feuer), sondern eigene Flaechenrechnung; Crew, Spieler, Neutrale aussparen; viele Brennende kosten FPS. Kein fester Platz, nur auf sein Wort.

**BAER ALS HAUSTIER, Kevin 06.11. ~23:30 (nur zum Ansehen):** *"einen baeren machen der laeuft und einen angriff macht einen krallenhieb ... wie das aussehn wuerde also der brauchbar waere fuer projekt zomboid als haustier"*. Probe aus Blender: Scratchpad der Sitzung `blender_test/baer/` (Skript baer.py, baer.blend, 2 GIFs). Reduziert 702 Punkte Koerper, dazu rund 2.400 Dreiecke Krallen, Zaehne, Augen. Noch nicht: gebackene Fell-Textur, Export, Spieltest, Kopf wirkt etwas nach Wombat, Auge steht in der reduzierten Fassung ab. Vanilla-Tiere 387-928 Punkte (Cow 670, Pig 928, Raccoon 387/726, Deer 624), eigenes Skelett und AnimSet je Art (`media/AnimSets/cow`, `media/anims_X/Cow`, `models_X/Skinned`). Companion Dogs (Workshop 3740052292) liefert eigene `Skinned/*_Body.glb`, also gehen eigene Tiermodelle; Tier-KI rechnet dort der Server. Kein fester Platz, keine Zusage, nur auf sein Wort. Gehoert nicht ohne Weiteres in NPC Crew.
