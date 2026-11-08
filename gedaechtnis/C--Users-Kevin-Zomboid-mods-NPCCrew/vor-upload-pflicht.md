---
name: vor-upload-pflicht
description: "Kevin 28.10.: was VOR dem naechsten Upload noch rein muss -- Magazin-Einordnung (Stock-Reiter/Sortierer); Liste fuer jeden Upload pruefen"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-11-01T11:33:30.662Z
---

**ERLEDIGT 01.11.2026 16:28: v3.14.27 hochgeladen -- alle Punkte dieser Liste (inkl. 21 a-f) sind drin und getestet bzw. benannt (siehe [[upload-v3-14-27]]). Fuer den naechsten Upload eine NEUE Liste beginnen.**

Kevin 28.10.2026: *"gut dann merk dir das noch bevor wir hochladen das es noch kommen wird am freitag arbeiten wir ja weiter"*.

MUSS VOR DEM NAECHSTEN UPLOAD REIN (Kevin laedt hoch, nie ich):
1. **Magazin-Einordnung** (Meldung NaYceR 28.10., zwei Bilder des Stock-Reiters):
   (a) `shared/BanditsNPCStorage.lua` DISPCAT `RecipeResource = "materials"` -> `"literature"` (alle 150 Vanilla-Gegenstaende mit
   DisplayCategory RecipeResource sind ItemType base:literature = Rezept-Magazine; betrifft Anzeige UND Sortierer).
   (b) Waffen-Magazine einer Waffen-Mod (STANAG 30Rds, M92FS 15Rds, Bakelite 30Rds ...) ohne DisplayCategory Ammo fallen auf die
   Wort-Heuristik LITERATURE_WORDS 'magazine' (~:3633) -> 'literature'; Fix: Wort-Heuristik nur fuer echte Literatur, Magazine mit
   Munitionstyp/Kapazitaet -> 'ammo' (Getter mit Lua-Fundstelle belegen). Kommt in die Fix-Version ab Fr 30.10. (mit E1/E2 der Abschlusspruefung).

2. **Tote Crew im MULTIPLAYER verliert Tasche (und ist nackt)** (Meldung NaYceR 28.10., Kevin: *"kannste das fixxen auch noch fuer
   multiplayer?"*): mit 'Unsterblich' AUS legt `stashManifestForCorpse` (client/BanditsNPCPersistence.lua ~:6556) die Tasche nur im SP in die
   Leiche (`if not sp then return 0 end`); im MP wird sie mit P.Forget vergessen = Verlust (rote Linie 1). Fix: im MP legt der SERVER die Tasche
   aus seinem Roster-Manifest in die Leiche (OnDeadBodySpawn auf dem Server, nie BanditBrain.Get; Form wie Crew-Leiche v3.13.96 markCrewBody in
   shared/BanditsNPCBaseSweep.lua), Zwilling/Kopie/geparkt/Neubau wie im SP ausschliessen (nie doppelt). Dazu vorher LESEN, warum die Leiche
   nackt ist (Vermutung, ungeprueft: Kleidung wird nur clientseitig von Bandits angezogen, der Server-Koerper hat keine ItemVisuals) und die
   Kleidung aus brain.clothing mitgeben. Kommt in die Fix-Version ab Fr 30.10. (eigene Pruefer-Linse 'Tasche doppelt/verloren beim Tod').

3. **Munitions-Schachteln werden nicht geoeffnet** (Meldung NaYceR 28.10.; Kevin: *"ja mach das"*): client/BanditsNPCInteract.lua ~:4341 oeffnet
   eine Schachtel nur, wenn ihr GANZER Inhalt in das Fehlende passt (rounds + n <= budget; Vorrat Vorgabe 3 Magazine) -> 9mm-Schachtel 50 >
   45 bei 15er-Pistole, Schrot 25 > Vorrat: nie geoeffnet, nur ins Inventar. Fix: oeffnen, sobald ihr ueberhaupt Munition fehlt (rounds < budget);
   Ueberschuss bleibt in ihrem virtuellen Vorrat (Zaehler am Gehirn), KEIN neuer Gegenstand -> SP und MP gleich; Rueckgabe (refundGunAmmo)
   packt weiter in Schachteln. Dazu nachlesen, ob Schachteln aus Waffen-Mods erkennbar sind (AMMO_BOXES kennt nur 9 Vanilla-Schachteln;
   Vanilla-Auspack-Rezepte OpenBoxOfBullets* als Quelle?), ungeprueft. Pruefer-Linse Ware: keine Patrone doppelt/verloren (Schachtel -> Zaehler,
   Rueckgabe, Logout, Neubau, Manifest).

4. **Steckengebliebene Waffe verdoppelt sich** (Workshop Deixide 28.10.: 'every zombie it hits leaves a full condition bolt cutter'): Bandits
   ZASmack.lua:434 haengt mit 1/4 je Treffer auf einen Zombie das HANDOBJEKT (volle Kopie) ans Opfer (Liste stuckItemLocations, auch
   Base.BoltCutters :192, Aexte, Messer, Brecheisen ...); unser Guardian (reclaimStuckCopy, client/BanditsNPCGuardian.lua:155, Aufruf ~:2049)
   ruestet sie aus dem Schatten npcMelee neu aus und nimmt die Kopie nur vom LEBENDEN Opfer; toetet der Treffer sofort, liegt die Kopie in der
   Leiche (Leichen-Suche seit v3.10.14 entfernt) -> Verdopplung, rote Linie 1, vermutlich nur SP (MP laut v3.10.14 nicht, ungeprueft).
   Fix ab Fr: beim Tod genau DIESES Opfers (getAttackedBy == unsere Companion) nur das steckengebliebene Stueck entfernen, nie eigene Beute des
   Zombies (vorher im Jar lesen: Reihenfolge onKilled/DoZombieInventory/OnZombieDead, wo das angehaengte Stueck dann liegt). Kevin noch nicht
   ausdruecklich gefragt -- als Pflicht eingetragen, er kann widersprechen.

5. **'beds' -> Vanilla-Wort 'furrows'** (Kevin 29.10., Screenshot Sandbox-Tooltip Field growth speed: *"wieso steht da BEDS?"* -> *"ja aendere
   das noch bevor wir es hochladen aber nicht jz"*): alle FARMER-Texte, die die Pflanzkacheln 'bed(s)' nennen, auf Vanillas Wort umstellen
   (EN 'furrow(s)', Vanilla Farming_Tooltip_FurrowNeedsSeed / SurvivalGuide_dig_furrow_*; in den anderen sechs Sprachen das jeweilige
   Vanilla-Wort aus deren Farming-Texten nachschlagen, nicht raten). In UI.json UND Sandbox.json, alle 7 Sprachen, per Skript. NUR Feld-Texte --
   Schlafbetten (Routine, 'My bed is gone', Bett zuweisen) bleiben 'bed'. Werte aendern, Schluesselnamen bleiben. Erst nach Kevins Test und
   wenn Limit frei ist (nicht vor dem Reset Fr 30.10. 14:00).

6. **Feld-Tempo: NUR den Sandbox-Hinweis klarer machen, KEIN Umbau** (Kevin 29.10. zuerst *"eigtl wollte ich das es unabhaengig ist"*,
   dann: *"ne lass das einfach so wie es ist stell nur sicher das in den sandbox einstellung da steht das es mit den wert der eingestellt ist
   bei vanillia skaliert okay"*): FarmGrowSpeed multipliziert weiter auf Vanillas FarmingSpeedNew. Nur der Tooltip
   Sandbox_BanditsNPC_FarmGrowSpeed_tooltip (7 Sprachen) sagt ausdruecklich: die beiden Werte multiplizieren sich; das Beispiel '5 = Kartoffeln
   in ~18 statt 90 Tagen' gilt fuer Farming Speed 1,0 (Vanilla-Vorgabe), bei 2,0 ~9 Tage. Zusammen mit Punkt 5 (beds -> furrows) im selben
   Skriptlauf, gleiche Bedingungen (nach Kevins Test, nach dem Reset).

7. **VORSCHLAG (Kevins Ja fehlt noch): Fields-Reiter wie Animals-Reiter** (Kevin 29.10., Screenshot: *"wieso steht move produce crate ganz
   rechts und wieso gibs kein show button wie in den anderen ui's?"*): client/ISUI/BanditsNPCFarmPanel.lua ~:1516-1529 setzt Assign/Move +
   Clear der Ertragskiste RECHTSBUENDIG und hat KEIN Show/Hide; der Animals-Reiter (BanditsNPCLivestockPanel.lua ~:6827) legt sie links unter
   den Text und hat Show/Hide (v3.12.60 E6, win.onLvObjShow). Dasselbe fehlt an der Wasserfass-Zeile der Felder. Fix: gleiche Anordnung +
   Show/Hide fuer Ertragskiste und Wasserfass, Form des Animals-Reiters wiederverwenden.

8. **Duengen: dritte Wahl 'both'** (Kevin 29.10.: *"wieso gibs nur compost oder fertilizer? waere es nicht gut es gaeb auch nimm beides?"*):
   Regel Fertilize off -> fertilizer -> compost -> both -> off; bei 'both' nimmt sie, was im Lager liegt, Kompost zuerst (Vanilla
   SPlantGlobalObject.lua:520-560: beide rufen fertilize2 = dieselbe Wirkung; Kompost hat eigenen Merker je Stufe und schadet nie, Duenger zaehlt
   hoch: 2. Gabe in einer Stufe -25 Gesundheit, 3. verflucht). Weiter EINE Gabe je Pflanze (unsere Regel). Regelfenster, Sortenfenster,
   Server-Tuer (Art pruefen), Texte 7 Sprachen. KEVIN BESTAETIGT 29.10.: *"ja merk dir noch both das es noch rein muss"* -- MUSS vor den Upload.

9. **Fields-Reiter neu ordnen** (Kevin 29.10., Screenshot: *"das ui ist noch echt scheisse, viel zu viel abstand und man muss schneller
   felder erkennen also die dinge die zu einen feld gehoeren"*): Ursache: BanditsNPCFarmPanel.lua reserviert fuer JEDE moegliche Warn-/Hinweis-
   zeile einen festen Platz (Regel 'Kasten, der nur manchmal erscheint, schiebt alles' zu woertlich genommen) -> grosse Luecken; die Feld-Bloecke
   haben keine Grenze. Plan: (a) je Feld ein KASTEN (Rahmen + leicht anderer Hintergrund), Kopfzeile 'Field N' mit Knoepfen, Inhalt
   eingerueckt; (b) nur Zeilen mit Inhalt, kein reservierter Leerraum -- neu gelayoutet nur, wenn sich die MENGE der Zeilen aendert (Refresh ruft
   layout, nie je Bild); (c) im Kasten Gruppen: Zustand (Planted/ripe/water/dead, Tended by, Now) | Sorte + Regeln + Saat-Hinweise | Wasserfass |
   Statistik klein unten; (d) basisweite Dinge (Weltregeln-Zeile, Ertragskiste mit Knoepfen + Show, Saat-Hinweis) oben in EINEM Kopfblock.
   Punkt 7 (Knoepfe links + Show/Hide) geht hier mit auf. Vor dem Bau Kevin einen Entwurf zeigen (Bild/Mockup).

10. **Je Feld: Statistik wie bei den Tieren + 'naechste Ernte in ...'** (Kevin 29.10.: *"ich will noch wie bei den animals stats haben zu
   jeden feld und ich will noch sehn koennen in welcher zeit etwas fertig ist zum ernten ... soll er einfach pro feld anzeigen was als erstes
   fertig ist zum ernten"*). (a) KEVIN 29.10.: *"also einfach bei jeden feld noch einen stats knopf"* -> in der Kopfzeile JEDES Feldes ein Knopf 'Stats' (neben Show/Add/
   Delete/Assign/Remove), oeffnet die Statistik NUR dieses Feldes (Fensterform wie Animals 'All stats' v3.13.46): geerntet je Sorte, gegossen, gegraben,
   gesaet, abgeraeumt, Mehltau behandelt, geduengt, Unkraut, verfault/gestorben -- die Zaehler gibt es teils schon (UI_BN_Farm_St_*, 'Crew work').
   (b) Zeile 'Next harvest: <Sorte> in about N h' (sichtbar im Feld-Kasten, nicht erst im Stats-Fenster) = die Pflanze des Feldes, die als erste erntereif wird. Rechnung: Vanilla speichert je Pflanze
   nextGrowing (Stunde des NAECHSTEN Wachstumsschritts, ISFarmingInfo.lua:527-545 liest es auch auf dem Client) -- genau nur fuer den
   naechsten Schritt; weitere Stufen geschaetzt (timeToGrow / FarmingSpeedNew + unser Tempo, Vanilla wuerfelt +-12 h je Stufe) -> 'about',
   ehrlich als Schaetzung beschriften; eine Pflanze, die gerade nicht beschleunigt wird (trocken/Mehltau), mit Vanilla-Tempo. Teil des Umbaus
   Punkt 9; Entwurf vorher zeigen.
   -> STAND 31.10.: Entwurf (Kasten je Feld, Kopfblock, Stats-Knopf, Next harvest, Show fuer Kiste+Fass, Mehltau sichtbar) von Kevin
   ABGENOMMEN ("ja du kannst das ja erstmal so machen") -> Bau als v3.14.21 (Skript _docs/nachtschicht/fix21_v3.14.21.js). Punkte 7, 9, 10.
11. **Vorschlag (Kevins Ja fehlt): 'Show' faerbt Beete nach Zustand** (braucht Wasser / reif / krank / tot), angeboten 29.10.

12. **Saatpackungen selbst oeffnen -- KEVIN BESTAETIGT 29.10.: *"ja merk dir das das soll er tun"*, MUSS vor den Upload** (Kevin 29.10.: *"ich habe seed packungen in den kisten die ruehrt er wohl
   garnicht an wenn man die nicht auspackt?"* -- stimmt: kein Farmer-Code kennt *BagSeed*). Vanilla recipes_farming.txt:185-202
   OpenPacketOfSeeds: 1 Packung (z. B. Base.CarrotBagSeed2, ItemType literature) -> 5 Samen + leere Packung (*_Empty). Vorschlag: fehlt Saat,
   oeffnet die Farmerin eine Packung der Sorte (wie Munitions-Schachteln, Punkt 3); leere Packung zur Abgabe; im Sortenfenster 'seeds in storage'
   Packungen x5 mitzaehlen; MP ueber die Server-Tuer (Server muenzt), Zaehltest Packung -> 5 Samen, nie doppelt.

13. **Hindernisse auf Beeten entfernen** (Kevin 29.10.: *"kann man da noch hinzufuegen das die mod noch anbieten das was im weg ist zu
   entfernen? also ohne cheat sondern nur was wirklich entfernbar ist und nur wenn das tool dazu im lager ist"*): heute zaehlt der Reiter
   'N beds have a tree or bush on them - the crew leaves those to you'. Neu: Regel im Regelfenster (Vorschlag Vorgabe AUS, beim Bau mit Kevin
   klaeren). NUR Vanilla-Wege: (a) Busch/Gestruepp = Objekt mit IsoFlagType.canBeCut, Vanilla ISRemoveBush (shared/TimedActions/
   ISRemoveBush.lua:118-160, complete auf dem Server: transmitRemoveItemFromSquare, 50 % Base.TreeBranch2 + Base.Twigs auf den Boden) -- nur
   mit einem Werkzeug mit Tag base:cutplant (predicateCutPlant, ISWorldObjectContextMenu.lua:69) aus dem Lager (Vanilla erlaubt auch Haende --
   Kevin will Werkzeug); (b) Baum = Faellen mit Axt aus dem Lager ueber den Foerster-Weg (BanditsNPC.ChopBlow, MP-Server), danach Stumpf
   raeumen wie der Foerster; (c) alles ohne Flag / ohne Vanilla-Weg bleibt stehen und wird weiter gezaehlt. Aeste/Zweige zur Ertragskiste
   bzw. Posteingang (Zaehltest), Werkzeug zurueck wie die Schaufel. Wanddeko/Ranken (wallVine) NICHT. KEVIN 29.10.: *"alles dann mit animation + sound falls moeglich"* -- gilt fuer 12 und 13 (Regel
   [[animation-und-ton-je-arbeitsschritt]]): Vanilla ISRemoveBush spielt RemoveBush/RemoveBushKnife/-LongBlade/-Axe (Spieler-Sets, fuer den
   Zombie ggf. eigener bumped-Knoten mit Clip aus Vanilla anims_X/Bob noetig, vor dem Bau pruefen); Bandits hat zschoptree.xml (Faellen) und
   zsforage.xml; Ton = Vanillas Ton der Aktion. Wo es keine Pose gibt: im Plan sagen warum.

14. **Klein (Log-Text):** Rueckgabe leerer Kompostsaecke druckt '[TC-FARM] ... bringt 1 Typ(en) ungenutzter leerer Eimer zurueck (zuerst
   Base.EmptySandbag)' / 'N ungenutzte(n) leere(n) Eimer ... zurueckgebracht' -- 'Eimer' ist falsch, wenn es Saecke sind (Kevins SP-Test
   29.10., Konsole). Text nach Gegenstandsart. Ergebnis desselben Tests: Kreislauf Karotten komplett, alle Zaehlungen stimmen (14 Saat/14
   gesaet, 63 geerntet/63 abgeliefert, 14x Kompost einmal je Pflanze); Tomate 8 Saat geholt, 7 gesaet -- 1 Samen muss in ihrer Tasche sein.

15. **Vorschlag (rote Linie 1, klein): Loch beim Boden-Loeschen des Servers** (Workshop-Frage 29.10. zu 'automatisch Items vom Boden
   loeschen' = Vanillas WorldItemRemovalList/HoursForWorldItemRemoval): Holzplatz-BUENDEL sind geschuetzt (setIgnoreRemoveSandbox(true) wie
   Vanilla ISDropWorldItemAction.lua:85 -- SP ForestJob ~:3340/:4142, MP ForestServer layOnTile ~:411). OHNE Schutz: einzelne Staemme auf dem
   Haufen im SP (ForestJob ~:4269 'Base.Log'), das Rueckfall-Neulegen relayLogs im MP (ForestServer ~:600) und ein abgelegtes Werkzeug
   (ForestJob ~:755). Nur ein Verlust, wenn der Server genau diese Typen auf der Loeschliste hat. Fix: dieselbe Zeile setIgnoreRemoveSandbox
   an den drei Stellen; dabei alle AddWorldInventoryItem der Mod (FarmOps, Livestock*, CorpseClean, SkillsHooks, WorkstationBuild) gegenlesen.

16. **MP: Beacon-Ausbau scheitert mit 'The server did not take it -- it stays with you.' -- URSACHE GEFUNDEN 30.10.:** PT.Request
   (client/BanditsNPCPlayerTake.lua ~:89-92) schickt im sendClientCommand KEIN `key` (nur rid, purpose, ids, types, uid, id, pieceId, stage,
   n, genAt); der Server liest args.key (server/BanditsNPCPlayerTakeServer.lua ~:307 beaconAtKey) -> nil -> 'nokey' -> refuse('nobeacon').
   JEDER MP-Beacon-Ausbau ueber den Server scheitert seit v3.13.66 (oeffentlich seit v3.13.70), fuer jede Rolle; 'als admin geht es' =
   Build-Cheat an (isBuildCheat -> kein Paket, gratis). Fix: `key = req.key` ins Paket (eine Zeile), Pruefer drueber. Kevin 30.10.:
   *"ja das soll auch noch mit hoch"* -> KEIN eigener Hotfix, kommt MIT dem naechsten Upload (MUSS rein). -- Urspruengliche Notiz: (Spieler-Meldungen, Kevin 30.10. mit Bild:
   Scrap Radio Stufe 1, Material vollstaendig). client/BanditsNPCBeacon.lua ~:1485-1535 zeigt DENSELBEN Text fuer VIER Faelle: Modul
   PlayerTake fehlt; Request nicht gesendet (nicht 'busy'); Server lehnt 'nobeacon' ab; Antwort findet den Beacon nicht auf der erwarteten
   Stufe (Undo). Wahrscheinlichster Fall (UNGEPRUEFT, kein Server-Log): 'nobeacon' -- seit v3.13.66 (N07, oeffentlich seit v3.13.70) prueft
   der Server mit beaconAtKey (server/BanditsNPCPlayerTakeServer.lua) + SR.IsBeaconObject (shared/BanditsNPCSiteRules.lua ~:1428), fail-closed;
   der Grund steht nur per BanditsNPC.Log (Crew logging) in der Server-Konsole: '... Beacon-Ausbau von X: an beacon|x|y|z steht kein Beacon
   (unloaded/none/nokey/norules/err)'. Verdacht: ein Beacon, der auf dem Server KEIN IsoThumpable mit heutigem Bild ist (Karten-Objekt oder
   Alt-Bild), braucht SiteUsed (Zonen/Lager/adopted) -- ein frischer Stufe-1-Beacon ohne Zonen faellt durch. Fix-Version: (1) Server-Grund als
   Err/ErrEvery (immer an), (2) je Fall ein eigener Text am Client (Regel 'eine Meldung fuer sechs Zustaende ist keine'), (3) Ursache im MP
   nachstellen (Testaccount user, frischer Beacon Stufe 1 ohne Zonen -> Upgrade) und beheben. Rote Linie: nichts darf genommen werden ohne Ausbau.

18. **Server-Rezepte** (Kevin 31.10. muss mit): Bau als v3.14.22 (_docs/nachtschicht/fix22_v3.14.22.js), Antworten Q1-Q5 in plan_upload_2026-10-30.md.

20. **BANDITS-UPDATE 30.10. -- Companions nach dem Laden doppelt (TOEDLICH, oeffentlich betroffen)** (Workshop Aglio e Olio 31.10., SP 42.21):
   Bandits server/BanditSave.lua neu: onSave nimmt jeden NPC mit Cluster-Eintrag (auch unsere Crew) aus der Welt + needRestore; onGameStart baut
   per spawnRestore eine Bandits-Kopie (anderer Name/Kleidung, gleiches Aussehen) und loescht gmd[id]; unser Restore baut das Original nach.
   Kevin 31.10.: KEIN Eilfix auf v3.13.95, sondern in die grosse Version direkt nach v3.14.20 -> v3.14.21 (Skript fix21_v3.14.21.js), mit den
   bestaetigten Funden des Bandits-Abgleichs (_docs/bandits_update_3110/). Kopien schon betroffener Spieler: nicht ohne Kevins Wort loeschen.

19. **Steam-Guide auf den neuesten Stand** (Kevin 31.10., gilt fuer JEDEN Upload): Abschnitte fuer Farmer/Fields, Rezepte vom Server,
   Saatpackungen, Buesche/Baeume, both-Duenger, MP-Leiche entwerfen, Kevin zeigen, mit dem Upload eintragen -- Ablauf in [[steam-guide]].

17. **Wassertraeger und Eimer** (Kevin 30.10.): mehrere Gefaesse weiter erlaubt, aber immer EINEN im Lager lassen; nach der Arbeit alle
   Gefaesse zurueckbringen, Restwasser vorher ins Ziel giessen bzw. ausschuetten -- keine halb vollen Eimer im Lager. In v3.14.18.
   ALLE ANTWORTEN KEVINS vom 30.10. (F1-F4 v3.14.16, Leiche/Munition v3.14.17, both/Ernte/Packungen/Buesche/Baeume) stehen in
   _docs/plan_upload_2026-10-30.md Abschnitt 'KEVINS ANTWORTEN 30.10.'.

21. **FIX-VERSION NACH KEVINS TEST (Kevin 01.11. ~00:15, 'alles wie du es gesagt hast' auf die Fragen v3.14.24):** (a) Zeile
   [TC-LOOTGUARD] *** (Bandits WeaponLoot fehlt) nur bei Crew logging, nicht bei jedem Start (client/BanditsNPCCrewLootGuard.lua);
   (b) Farm-Faellregel 'fell' bei dauerhafter Server-Absage: dieselbe 10er-Regel wie der Foerster (v3.14.24: kurz warten, nach ~10 Absagen
   in Folge Arbeit dort beenden + Spruch) und eine immer-an-Konsolenzeile (ErrEvery, 10 min); (c) Speicher-Schild BanditsNPC.SAVE_SHIELD
   Vorgabe AN, sobald Kevins Schlaftest mit TrueCompanions_SaveShield(true) gut war. ENTSCHIEDEN NEIN: Profil-Waffen einer Bandits-Kopie
   hinlegen; leerer Ersatz fuer Bandits WeaponLoot. (d) v3.14.23: der Server legt vor JEDEM 'Save to server' eine Sicherungskopie der Rezeptdatei an (Kevin 01.11.: 'ja'; Testserver und
   SP teilen Zomboid/Lua/NPCCrew_recipes.txt). (e) v3.14.23 (Kevin 01.11.: 'nein davor damit alles fertig ist'): Status der Baeuerin, solange die Server-Rezeptliste
   noch fehlt, sagt 'wartet auf die Rezeptliste' (heute 'reserved in an ingredient crate'), und ein eigener Grund 'norecipe', wenn das einzige
   Rezept im Plan eines Crafters gestrichen wurde (heute 'All targets met') -- beides VOR dem Upload, Fix-Version nach dem Test, 7 Sprachen.
   (f) BUG aus Kevins SP-Test 01.11. (Punkt 2): seit Bandits' BanditSave (30.10.) nimmt JEDES Speichern alle Crew-Koerper aus der Welt;
   der Sweep (P.Tick, client/BanditsNPCPersistence.lua ~:8654 RESTORE_NEAR = 25 und farAway ~:8802-8806: andere Ebene ODER > 25 Kacheln
   vom Spieler) baut eine Vermisste nur neu, wenn der Spieler binnen 25 Kacheln auf DERSELBEN Ebene steht -- gebaut fuer 'streamt mit dem
   Chunk von selbst zurueck', was seit dem Update nicht mehr gilt. Folge: Basis-NPCs weiter weg oder im 1. Stock ('2etage test', Asher,
   Aubrey) bleiben 'away / Out of range', obwohl die Basis geladen ist; Koch/Fischer kamen erst nach ~3 min. Fix: im Speicher-Vorlauf (SP,
   v3.14.21-Bilanz) je von Bandits genommenem Crew-Koerper einen Merker am Roster-Eintrag (z. B. entry.bsTaken, mit Loescher bei live/
   Neubau); fuer diese baut der Sweep, sobald die Posten-KACHEL geladen ist (jede Ebene, ohne 25er-Grenze), und ohne lange Wartezeit
   (Kevin wollte es schneller: 14 kamen nach 19 s, 3 nach 33 s). Zwillings-Schutz: findLoadedReal bleibt, nie neben einem lebenden Koerper.
   Kevin 01.11.: 'das muss doch ein bug sein ... der bereich ist zu 100% geladen' -- ja, MUSS vor den Upload.
   Kevin 01.11. dazu: 'auch auf anderen etagen ... radius erhoehen, 25 kacheln ist zu wenig -- soviele kacheln wie geladen sind bzw. die
   base radius maximal hergibt'. Also: fuer die von Bandits genommenen (Merker) JEDE Ebene und der ganze geladene Bereich (Posten-Kachel
   geladen; Basisflaeche bis 75, Ladebereich 76). Fuer den Fall OHNE Merker (in der Sitzung entladen, Koerper liegt in der Population) die
   Ebenen-Bedingung ebenfalls weg (das Risiko 'Kachel geladen, Koerper noch nicht da' haengt an der Entfernung, nicht an der Ebene); die
   Entfernungsgrenze dort nur mit Beleg erhoehen (Zwillings-Gefahr v0.77/29.07.) -- im Plan pruefen und Kevin sagen.

**Why:** Kevin will den Fix im naechsten Upload sehen; der Melder wurde vertroestet ("wird im naechsten Update korrigiert").
**How to apply:** Vor jedem Upload diese Liste durchgehen und Kevin sagen, ob alles drin ist; erledigte Punkte hier abhaken. Siehe
[[farmer-waechter]], [[workshop-updates-nur-auf-ansage]].
