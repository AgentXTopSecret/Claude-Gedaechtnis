---
name: workshop-meldungen-20-09
description: "Workshop-Meldungen 20.-25.09. -- STAND 04.10.: ALLE ERLEDIGT oder von Kevin gestrichen (Kevin: Zonen-Zeichnen und Weste 'haben wir schon behoben'); nur noch Archiv, nichts davon als offen melden"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-04T10:13:59.741Z
---

**STAND 04.10. (Kevin):** keine offenen Punkte mehr aus diesen Meldungen. Beacon-Ausbau/verwaister Eintrag (v3.10.50-.55), Durst-
Stillstand (v3.10.57), Zonen-Zeichnen (v3.10.68 laut Changelog), Panik (v3.11.14-.18), Schuss ins Auto (v3.11.19), Militaerweste
(laut Kevin behoben); Idle-Emote/Forst-Cursor/Waffenaufsaetze gestrichen bzw. erledigt. Wer nach offenen Bugs gefragt wird: diese
Liste NICHT als offen nennen (04.10. passiert, Kevin musste korrigieren).

Kevin (20.09. abends, 'nur sagen nix bauen' / 'merk dir das mal'): vier Punkte eines Workshop-Melders, ungespielt, Plaene oben in
`_docs/offene_arbeit.md` (Abschnitt WORKSHOP-MELDUNG 20.09. 22:00). Reihenfolge nach Kevins Wort, erst nach Fischer-Rework/Budget.

- **Schuss ins eigene Auto (Bug 3) -- Ursache gelesen:** Bandits' `IsShotClear` ist stillgelegt (`BanditUpdate.lua:114-116`,
  `if true then return true end`), `BanditUtils.ManageLineOfFire` beschaedigt jedes Fahrzeug auf der Linie (:516-535).
  FIX bei uns: Aufsatz auf `ZombieActions.Shoot.onWorking` (ZAShoot.lua:9) nur fuer Angeworbene, Bresenham-Linie, bei
  `square:getVehicleContainer()` auf einer Zwischenkachel Schuss ausfallen lassen; Wrapper-Form wie IsController (Claim.lua:634).
  Kleiner Aufwand, SP+MP gleich. Grenze: sie steht zielend, bis die Linie frei ist.
- **Idle-Emote (Bug 2) -- bestaetigt, unseres:** NPCCompanion.Main haengt bei Stillstand `BanditPrograms.Idle` ein (200 Ticks
  Smoke/ChewNails), Main laeuft erst bei leerer Liste -> folgt/reagiert erst nach dem Emote. Fix: kurzes Emote (Time braucht
  ein anim) + Guardian bricht es ab, wenn der Spieler ueber stopAt weg ist oder ein Gegner naht.
- **Militaerweste nicht im Gear-Reiter (Bug 1):** Slot kennt TorsoExtraVestBullet; Verdacht 'Also worn +N' eingeklappt oder
  Schluessel-Mismatch (`base:`-Praefix in NormalizeBodyLocation?). Rueckfrage an den Melder gestellt (Itemname, console.txt).
- **Fenster/Halbwaende als begehbar (Bug 4):** Engine-Zombie-Pfadfinder; Recherche noetig, kein schneller Fix.

**STAND 27.09. (Kevin):** (1) Beacon-Ausbau und (2) verwaister Eintrag sind behoben (v3.10.50-.55). GESTRICHEN von
Kevin: (7) Waffenaufsaetze an der Hand, (4) Forst-Cursor ('funktioniert doch alles'), (6) Idle-Emote ('konnte ich nicht
feststellen, vermutlich Mod-Konflikt' -- der Codeweg NPCCompanion.Main -> BanditPrograms.Idle ist gelesen, aber im Spiel
nie beobachtet; nicht wieder aufmachen ohne neue Meldung). OFFEN: (3) Panik-Pendeln (unser dampCompanionPanic,
client/BanditsNPCCompat.lua:213, zieht 12 je 300 ms ab statt ohne echte Zombies auf 0 zu setzen) und (5) Schuss ins Auto.

**ZU FIXEN, KEVINS ANSAGE 24.09. ('merkst du dir das auch das du das noch fixxen musst?') -- offene Reihenfolge, nichts
gebaut:** (1) Beacon-Ausbau frisst Nachbar-Behaelter [Verlust, rote Linie], (2) verwaister Beacon-Eintrag sperrt den Neubau,
Meldung ohne Koordinaten + kein Weg, ihn zu loeschen, (3) Panik-Pendeln (auf 0 setzen statt abziehen; Option PauseNearPlayer
wird vom Daempfer nicht gelesen), (4) Forst-Cursor anders bedienbar als Basis/Fisch (angleichen oder Hinweiszeile), (5) Schuss
ins eigene Auto (SetHands-/ZAShoot-Wrapper), (6) Idle-Emote blockiert Folgen und Reaktion, (7) Waffenaufsaetze wirken an der
Hand nicht. Dazu das Zonen-Zeichnen (vier Melder) untersuchen. Nach dem Fischer-Rework, mit Kevins Wort je Punkt.

**!! ERNSTESTER FUND (Meldung 24.09., KEVINS ROTE LINIE 1 -- Gegenstandsverlust):** der BEACON-AUSBAU frisst
  Nachbar-Behaelter. `LEGACY_SPRITES` enthaelt zwoelf gewoehnliche Vanilla-Kuechentheken (fixtures_counters_01_9..63, aus
  v0.66-v0.68) und wird in `SPRITE_INFO` gemischt (Beacon.lua:179-181); `B.PartsOf` scannt die Beacon-Kachel UND die vier
  Nachbarn (:386); `B.ApplyUpgrade` macht `parts.counter` zum ANKER und uebermalt ihn zur Konsole (die Theke des Spielers
  samt Inhalt) und entfernt jedes weitere Teil per transmitRemoveItemFromSquare (:1036-1050). Fix-Richtung: nur Objekte mit
  `getModData().tcBeacon` oder auf der eigenen Kachel als Teil zaehlen, Legacy-Sprites nur zur ERKENNUNG (:315/:1712 trennen
  das schon), nie etwas mit Behaelterinhalt uebermalen/entfernen; Alt-Beacons muessen erkennbar bleiben. Workaround fuer
  Spieler: Beacon mit einer Kachel Abstand zu Theken/Schraenken bauen.
- **'Upgrade-Kosten werden nicht abgezogen'** = BUILD-CHEAT (Stations.lua:284 `if S.BuildCheat(player) then return true`),
  rastet nach einem Druck auf 'Force craft' dauerhaft ein (v1.7.4); Vanilla hat keinen Ausschalter, wir haben den Befehl.

**Weitere Meldungen 21.-23.09. (alle gelesen, nichts gebaut, Fundstellen oben in offene_arbeit):**

- **'You already have a beacon', ohne je einen gebaut zu haben:** im SP sperrt in `SR.CheckBeacon` JEDER Registry-Eintrag
  (`foreignSite` ist dort immer false), und der Aufraeumer (Beacon.lua:640-655) raeumt nur bei GELADENER Kachel -- ein weit
  entfernt zerstoerter Beacon blockiert dauerhaft. Die Meldung nennt den Ort nicht, obwohl CheckBeacon ihn als detail 'x,y'
  liefert. Mini-Version: Koordinaten in den Text (3 Sprachen) + Weg, einen verwaisten Eintrag zu loeschen. Workaround: F8.
- **Panik 'geht hoch und runter' bei freundlichen NPCs:** unser `dampCompanionPanic` zieht alle 300 ms 12 Punkte ab, die Engine
  legt je Bild nach -> sichtbares Pendeln. Fix: ohne echte Zombies Panik auf 0 SETZEN. Nebenfund: der Daempfer liest die Option
  'Crew members calm the player's panic' (PauseNearPlayer) gar nicht -- die gilt nur fuers Pausieren (Programs.lua:2747).
- **Forstzone laesst nur 1 Kachel waehlen:** unsere zwei Cursor bedienen sich verschieden -- Basis/Fisch = Klick, bewegen, Klick;
  FORST = halten und ziehen, Loslassen beendet ('Mouse-up ends it'). Mini-Version: angleichen oder Hinweiszeile je Cursor.
- **Zonen-Zeichnen klappt nicht (vier Melder, Kevin spielt es fehlerfrei):** Verdacht Mod-Konflikt (fremdes UI-Panel schluckt den
  Weltklick, v0.91.6-Familie) ODER die Z-Ebene (pickSquare nimmt immer die Spieler-Ebene). Nach Kevins Rueckkehr mit Agenten
  untersuchen, nicht weiter einzeln beantworten.
- **Waffenaufsaetze wirken nicht an der Hand** (siehe oben, SetHands-Wrapper) und **eine Fraktionsbasis fuer zwei Spieler gibt es
  nicht** (Basis gehoert ihrem Erbauer, 90 Kacheln Abstand zwischen Beacons) -- beides gemeldet, beides moegliche Features.

- **25.09. 'Tending to needs', zwei stehen herum (Feuerwache):** 5 Pruefer -- Beduerfnisse toeten nie; wahrscheinlich
  Durst-Stillstand an leerer/dreckiger Tonne (NPCRoutine.Main gibt ohne Ausgang zurueck, Programs.lua:2429/:2446). Antwort an den
  Melder geschrieben, Fix-Kandidaten in offene_arbeit (Fortschritts-Waechter als Engstelle). NICHTS GEBAUT, Kevins Wort noetig.
- **Punkt 2 (verwaister Eintrag / Beacons in der Wildnis) GEBAUT als v3.10.55** (Kevins 'ja bau das'): Eintrag beim Bau,
  nur IsoThumpable zaehlt, Koordinaten in der Meldung, roter 'Forget this base', Abbau nur bis 5 Kacheln. Ungespielt.

**How to apply:** wenn Kevin 'bau' sagt, zuerst Bug 3 (kleinster Aufwand, klare Fundstelle) oder Bug 2 -- seine Wahl; vorher
die Fundstellen in offene_arbeit lesen, nicht aus dem Gedaechtnis bauen. Siehe [[moegliche-features]], [[kevins-zwei-rote-linien]].