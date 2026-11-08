---
name: nach-dem-upload
description: "Kevins Auftraege fuer NACH dem naechsten Workshop-Upload (nicht vorher bauen): Foerster im Schichtplan vorhandene Zone waehlen, Leiche sichtbar ziehen"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-11-06T15:17:19.205Z
---

Gebaut wird erst NACH dem naechsten Upload (Kevin laedt hoch), jeweils auf sein Startwort:

1. **Foerster im Schichtplan: vorhandene Forstzone waehlen** (Kevin 29.10.: *"beim schedule plan muss man selbst zonen zum faellen markieren
   statt schon vorhandene zu uebernehmen und da weiter zu arbeiten, das soll aufjedenfall so sein das man da die forestery zone auswaehlt die es
   schon gibt wenn das moeglich ist"*). Heute verlangt der Schichtblock fuer den Foerster eine neu gezeichnete Faellzone; gewuenscht: im Block
   eine der vorhandenen Forstzonen der Basis auswaehlen (Pflanz-/Rodungsflaeche aus dem Forest-Reiter) und dort weiterarbeiten. Vor dem Bau
   nachlesen (ungeprueft): wie der Schichtblock die Zone heute speichert (shared/BanditsNPCSchedule.lua) und wie der Forest-Reiter Zonen fuehrt
   (TrueCompanionsForest-ModData); Form wie Tierpfleger-Block 'alle Tierzonen der Basis' (v3.12.46).
   DAZU Kevin 29.10.: *"bei der forster zone dann noch einen namen vergeben koennen ... damit man die unterscheiden kann wenn man
   mehrere hat und die forester zone muss dann natuerlich auch gespeichert werden das beim job wechsel die zone nicht geloescht wird"* ->
   (a) jede Forstzone bekommt einen NAMEN (umbenennbar im Forest-Reiter, Vorgabe z. B. 'Forest 1'), Auswahl im Schichtblock ueber den Namen;
   (b) Forstzonen gehoeren der BASIS, nicht der Figur -- ein Job-/Programmwechsel, Entlassen, Schichtwechsel oder Neubau loescht sie NIE;
   nur 'Delete' im Reiter. (Ausnahme bleibt die Rodungszone, die sich nach dem letzten Baum selbst loescht -- beim Bau mit Kevin klaeren, ob
   die bleiben soll.) Vor dem Bau pruefen, wo heute eine Zone beim Jobwechsel verschwindet (Fundstelle suchen, nicht raten).
2. **Leiche sichtbar ziehen: GESTRICHEN 02.11.** Pruefauftrag `_docs/leichen_ziehen/`, Kevin: *"dann lassen wir das einfach so"*. Nicht neu aufmachen.
3. **Pruefung 'was macht der Client noch selbst?'** (Workshop/Discord NaYceR 30.10.: moeglichst viel serverseitig, sicherer und stabiler;
   Kevin: *"erst nach dem upload gucken"*): gezielter Mod-Check -- (a) jede Client-Stelle, die noch selbst Gegenstaende erzeugt/entfernt oder
   die Welt aendert (AddItem/Remove/removeFromWorld/transmit/AddWorldInventoryItem in client/ und shared/ ohne isClient-Riegel), (b) jede
   Server-Tuer (OnClientCommand), die Besitz/Rolle/Plausibilitaet nicht prueft. NICHT moeglich: NPC-KI/Bewegung auf den Server (Bandits
   rechnet NPCs nur auf Clients, OnZombieUpdate feuert auf dem dedizierten Server nie -- CLAUDE.md v3.9.42). Mehr Server-Bitten = mehr
   Warten/Pakete, nur fuer Ware und Besitz lohnend.
4. **Barrikaden-Umweg** (Workshop Maxene Sita 31.10.: 'NPCs see a barricaded window and think that is a valid place to go through';
   Recherche + Gegenpruefung _docs/barrikaden/recherche.md, gegenpruefung.md). Ursache belegt: der Wegfinder schickt jeden gehenden IsoZombie
   ohne Aufpreis durch jedes Fenster (canThump fest an), kein Schalter je Figur; ClimbFix-Hop (v3.12.84 E35) bzw. passDoor (Tueren) setzen sie
   durch die Barrikade. KEVIN 31.10.: NACH dem Upload bauen; verbarrikadierte TUEREN auch (Umweg statt Durchgang); findet sie keinen Umweg:
   STEHEN BLEIBEN + SAGEN (kein Hop/Teleport durch die Barrikade mehr). Loesung (c) eigener Tuer-Umweg nur fuer unsere Crew, ohne Ausnahme --
   die Gegenpruefung nennt die Nachtraege (verschlossen = begehbar, verbarrikadiert = Wand; Wegpunkte auch an Richtungswechseln; alle Leser von
   task.x/y; Folgen mit wanderndem Ziel; alter Router v0.75.62 RouteWaypoint, N.ClassifyEdge benutzen). Eher 2 Versionen, eigener Test.

**Why:** Kevin will den Upload nicht mit neuen Baustellen verzoegern. **How to apply:** Nach dem Upload diese Liste mit Kevin durchgehen,
Reihenfolge von ihm. Siehe [[vor-upload-pflicht]], [[moegliche-features]].

Kevin 02.11. MP-Test: Mitspieler sieht den Farmer nur herumstehen, der Ton kommt an. Ursache: PS.POSES (shared/BanditsNPCPoseShow.lua) hat nur 10 Posen aus v3.12.60/.62; es fehlen Farmer (PourWateringCan, Forage, Loot, LootLow, LootHigh, BNGardenSpray, BNSeedPacket, DigShovel, ChopTree) und Pfleger (BNShear*, BNMilk*, BNPet*, BNSlaughter*). Endliche Posen sind ein Listeneintrag mit Cliplaenge; DigShovel/ChopTree/FillBucket sind m_Looped (Stufe 1b, Ende auf fremder Kopie ungeprueft, nur mit Waechter). ENTSCHIEDEN Kevin 02.11.: 'ja mach das nach dem upload' -> eigene Version direkt nach dem Upload, vor Pluendern; Pluendern rutscht entsprechend eine Nummer weiter.

Kevin 03.11. ~01:25: Fenster 'Boil water' (Liste der Regenfaenger: Dirty water from here / Clean water to here) braucht je Zeile einen Show-Knopf wie die Troege und das Wasserfenster. Gehoert in die Version direkt nach dem Upload, zusammen mit dem Posen-Spiegel (v3.14.39).

Kevin 03.11. ~01:25, Fenster 'Boil water', zweites Problem: 'Dirty water from here' nur auswaehlbar, wenn wirklich Dreckwasser drin ist; Ziel 'Clean water to here' nur leer oder mit sauberem Wasser (keine Milch usw.); sonst nicht auswaehlbar und eine Meldung, warum nicht. Zur Laufzeit lehnt der Koch eine Quelle mit Fremdinhalt schon ab (UI_BN_Boil_SrcNotWater, 'notwater'), die AUSWAHL prueft nichts; Ziel ungeprueft (W.PourInto kennt nur das Milchfass). Plan: mit Show-Knopf und Posen-Spiegel in v3.14.39, sieben Sprachen.

Kevin 03.11. ~01:35: Ist das Abkoch-Ziel das Milchfass einer Tierzone, lehnt W.PourInto ab (richtig, [TC-POUR]), NPCBoil beendet den Gang aber mit handBack('done') und der Koch sagt faelschlich 'Clean water's in.', immer wieder (Programs :7845). Gehoert zur Fenster-Pruefung in v3.14.39: Milchfass als Ziel gar nicht waehlbar, und ein abgelehnter Guss sagt den wahren Grund.

Kevin 03.11. ~01:55: die Taste, die die Felder anzeigt, soll auch zeigen, WAS in welchem Feld gepflanzt wird (Sortenname oder Bild am Feld). 'wenn ja mach das auch noch nach dem upload'. Gehoert in die Runde nach dem Upload.

Kevin 03.11. ~02:10: Kompost/Duenger geben: gleicher Clip wie beim Spieler (Vanilla ISFertilizeAction: Pour mit PourType Bucket, CompostBag und Fertilizer haben keinen eigenen PourType, also Bob_IdlePour_Bucket), die Baeuerin spielt PourBucket mit demselben Ton. Unterschied: der Spieler haelt den Sack in der Hand (setOverrideHandModels), die Baeuerin nicht. PourBucket steht schon im Posen-Spiegel. Kevin 03.11.: ja, nach dem Upload bauen: Sack beim Duengen sichtbar in der Hand, Fake-Waffe wie NPCCrew.BucketHand, das Modell braucht attachment Bip01_Prop1/Prop2 (CLAUDE.md v1.9.3).

Kevin 06.11. ~16:15 (SP-Test v3.14.51): Foerster-Zone 'Add' blendet die aktuelle Zone nicht ein -- man sieht nicht, wo man anbaut, und muss sie erst von Hand mit Show aufrufen. Gewuenscht: 'Add' zeigt die Zone beim Zeichnen von selbst. *"das muessen wir noch fixxen nach dem upload"*. Vor dem Bau pruefen, ob Rodungszone und Holzplatz dieselbe Luecke haben.

Ruckler gemessen 06.11. ~16:15 (SP, v3.14.51, Kevin: 'laggt jede 2 sec'): TrueCompanions_Profile(30) 8 Bildluecken 212-330 ms; ProfilePrograms(30): NPCLivestock.Main 115-198 ms JE AUFRUF, alle ~3 s (9 Aufrufe, 1408 ms), NPCHaul.Main 2911 ms in 51 Aufrufen (Spitzen 373 ms/s, SupplyNeed ~190 ms je Fehlgriff), dazu Basis-Scan 277 ms. Tierpfleger-Dateien seit v3.14.50 unveraendert, aber im Vorlauf (v3.14.49/.50) kostete derselbe Aufruf nur ~50-56 ms -- warum jetzt das Dreifache, ist OFFEN (ungeprueft: Zustand der Welt oder Laufzeit der Sitzung). Weg: Zeitmesser (nur Crew logging) in `guarded` in shared/BanditsNPCLivestockJob.lua (jede Runde laeuft dort durch), dann gezielt fixen; Nachschub-Speicher (auftrag_v3.14.51 Abschnitt 2) gehoert dazu. Kevins Wort, ob vor oder nach dem Upload, steht noch aus.

Kevin 03.11. ~02:40: der Foerster-Schichtblock (Punkt 1 oben: Zone waehlen, Name, Zonen gehoeren der Basis) MUSS noch VOR dem Pluenderer rein. Reihenfolge jetzt: Runde v3.14.39ff (Posen-Spiegel, Show-Knopf + Auswahl-Pruefung + wahrer Grund im Fenster Boil water, Namen fuer Tonnen, Sorte bei Show fields, Sack in der Hand, Foerster-Schichtblock), Holzfeuer-Test, erst DANN Pluendern. Start nur auf Kevins Wort.
