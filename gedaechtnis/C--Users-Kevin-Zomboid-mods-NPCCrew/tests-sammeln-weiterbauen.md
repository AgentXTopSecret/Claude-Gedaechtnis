---
name: tests-sammeln-weiterbauen
description: "Kevin 23.10.: nicht auf seine Tests warten -- Testlisten sammeln und merken, direkt die naechste Version bauen; Liste der offenen Tests hier"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-11-02T21:08:29.942Z
---

Kevin 23.10.2026: "nene das testen merkste dir du machst direkt den nächsten schritt" -- nach einer fertigen Version NICHT auf seinen Test
warten, sondern die Testliste merken und sofort den naechsten Fahrplan-Schritt starten (weiter: eine Bau-Version zur Zeit).

**Why:** Er will Tempo in der Bauwoche; getestet wird gesammelt, wenn er Zeit hat.

**How to apply:** Nach jedem Workflow: Testliste `_docs/testliste_vX.md` hier unten eintragen, dann direkt die naechste Version. Vor einem
Upload ALLE gesammelten Tests mit Kevin durchgehen (Upload nur nach seinem Wort). Wenn er "jetzt testen" sagt: Liste unten zusammenfassen,
nur das Noetigste ([[test-nur-noetigste]]), Bugwatch mitstarten.

Offene Tests (gesammelt):
- v3.13.96 -> `_docs/testliste_v3.13.96.md` (Crew-Leiche MP, Unstuck Liegende, Tuer-Schutz Feinde, Needs-Regler 0).
  SP-Test 24.10.: 'Liegende holen' (v3.13.96 Punkt 3, SP) BESTANDEN (Kevin: '1 hat geklappt').
  SP-Test 24.10.: 'Beduerfnis-Regler 0' (v3.13.96 Punkt 6, SP) BESTANDEN (Kevin: 'sofort alles auf 0').
  SP-Test 24.10.: Punkt 'gezogene Leiche' (v3.13.96 Punkt 4) von Kevin AUSGELASSEN ('kann ich nicht testen') -- bleibt ungespielt.
- v3.13.97 -> `_docs/testliste_v3.13.97.md` (Wassertraeger mehrere Tonnen, 6 Punkte).
  SP-Test 24.10.: alter Stand migriert als #1 75-100 % BESTANDEN; Reihenfolge BESTANDEN (Log: #2 bei 0 % gewaehlt, danach #3 bei 0 %,
  keine eigenen Fehler). Offen in SP: Tonne 1 waehrend der Arbeit unter 75 % -> dreht um (Punkt 2 Rest), Punkt 3 (90 % -> geht nicht los),
  Punkt 1 (Fenster speichern/laden), Koch-Tonne abgelehnt (Punkt 4 Rest). Kevin 24.10.: diese Reste testet er ERST NACH W1 (Show-Knopf),
  sonst weiss er nicht, welche Tonne #1 ist; W1 kommt nach dem Limit-Reset (Pause, Uebergabe 'PAUSE 24.10.').
  BEFUND SP-Test 24.10. W1: Wasserfenster braucht je Tonnen-Zeile einen Show-Knopf (wie Troege) -> naechste Fix-Version (Uebergabe 'BEFUNDE SP-TEST 24.10.').

**ABER (Kevin 23.10., gleicher Tag):** nach einer fertigen Version ERST PAUSE, wenn das 5-h-Fenster knapp wird -- *'du must doch danach
erstmal pause machen und dir merken was danach kommt das sprengt sonst das 5std fenster'*. Also: vor jeder neuen Version get_usage; ist
das 5-h-Fenster weit gefuellt, nicht starten, sondern naechste Schritte in _docs/uebergabe_2026-10-21.md ('PAUSE NACH ...') merken und
auf Kevins 'weiter' warten.

- v3.13.98 -> `_docs/testliste_v3.13.98.md` (Show je Tonne, Leichen neutral/angeworben, ID-Karte, Pflanzen MP, Schichtplan, Koehler).
  Damit sind die v3.13.97-Reste (Tonne <75 % dreht um, 90 % geht nicht los, speichern/laden, Koch-Tonne) jetzt testbar.
  UNBEDINGT: SP Punkt 1 (Show) + v3.13.97-Reste, SP Punkt 2 (Entlassene brennt, Angeworbene bleibt).

- v3.13.99 -> `_docs/testliste_v3.13.99.md` (MP Mischeimer als Dreckwasser, SP Becken ohne Wasser optional, normale Wasser-Runde SP+MP).
  UNBEDINGT: Punkt 3 (normale Runde SP: Hahn/Brunnen/See schoepfen und giessen wie bisher) -- B8d aendert die Quellenwahl in beiden Modi.

- v3.14.0 -> `_docs/testliste_v3.14.0.md` (3 MP: fremder Posteingang/Zutatenkiste/Fischkiste mit Testaccount user; 3 SP: Basis-Sperre
  Fisch/Wasser/Forst/Schlaf ueber 75 Kacheln, Foersterin ohne Rucksack, halb gegessenes Steak). UNBEDINGT: SP 4 und 6; MP 1 beim naechsten MP-Test.

- v3.14.1 -> `_docs/testliste_v3.14.1.md` (MP Koch: nachlegen/anzuenden/abkochen/loeschen ueber den Server, Testaccount user; MP Maehen mit
  fast voller Tasche; SP Regression Abkochen + Maehen). UNBEDINGT: SP 4 (Regression) beim naechsten SP-Test; MP 1+2 beim naechsten MP-Test.

- v3.14.2 -> `_docs/testliste_v3.14.2.md` (SP Hemdfarbe + Sitzen/Schlafen oben, SP Fenster/Kanten, MP Liegende beim Mitspieler, SP+MP
  Besorgung unterbrochen). UNBEDINGT: SP 1 (Farbe bleibt nach Speichern/Laden, Sitzen/Schlafen geht) und SP 2 (Kanten/Fenster).

- v3.14.3 FARMER TEIL 1 -> `_docs/testliste_v3.14.3.md` (SP Feld zeichnen, SP Jahreszeiten, SP Tempo + Strafe Frage 18, MP Server-Tor).
  TESTPUNKT 1 VON 3 FUER DEN FARMER (Kevins Antwort 15): kurz, ohne NPC, Fields-Reiter nur mit -debug. UNBEDINGT: SP 1-3.

- v3.14.4 FARMER TEIL 2 -> `_docs/testliste_v3.14.4.md` (Zuweisung, sie geht zum Feld und wartet, Logout behaelt sie an der Basis). Test erst
  nach Farm-4 (Farmer-Testpunkt 2).

- v3.14.5 FARMER TEIL 3 -> `_docs/testliste_v3.14.5.md` (Giessen SP/MP, Spieler am Beet, Beacon-Ablehnung, Alt+F4 mitten im Giessen). Test nach Farm-4.

- v3.14.6 FARMER TEIL 4a -> `_docs/testliste_v3.14.6.md` (Reichweiten-Warnung beim Feldzeichnen, Ertragskiste im Fields-Reiter, Eimer zurueck).
  Test zusammen mit Farm-4b (Farmer-Testpunkt 2).

- v3.14.7 -> `_docs/testliste_v3.14.7.md` (2 MP-Punkte: Pflegerin bringt Werkzeug/Saecke zurueck, Zaehltest; Eier/Futter wie bisher).
- v3.14.8 FARMER TEIL 4b -> `_docs/testliste_v3.14.8.md` (SP Ernte + Kiste mit Zaehltest, SP zu schwer (Wassermelone ohne Rucksack), MP Ernte
  als user, MP Alt+F4 mitten im Ernten/Abliefern). Test am Stueck, wenn der Farmer fertig ist (Kevin 27.10.: Abschlusspruefung vorher).
- v3.14.9 FARMER FIX (Gesamtpruefung 1) -> `_docs/testliste_v3.14.9.md` (SP zu schwere Ernte ein Gang je Sorte, MP dasselbe, MP Release
  waehrend Ernte-Bitte, eine Kiste fuer Eimer + Ernte). Test am Stueck mit dem Farmer.
- v3.14.10 FARMER TEIL 5a -> `_docs/testliste_v3.14.10.md` (SP graben/abraeumen mit Werkzeug + Haende, SP Sorte/Spieler daneben, MP als user,
  Werkzeug zurueck + keine Ersatzwaffe). Offene Fragen im Integrator: Farn als Busch, Werkzeug bleibt in der Tasche (beide 'so lassen').
- v3.14.11 FARMER TEIL 5b -> `_docs/testliste_v3.14.11.md` (SP Karotten-Zaehltest, MP Saeen + Alt+F4 mitten im Saeen, Behalten/Automatik/
  Ess-Sperre ohne Pendeln, Saison + Schalter im Sortenfenster).
- v3.14.12 FARMER TEIL 6 -> `_docs/testliste_v3.14.12.md` (SP Mehltau mit Zaehltest + Spruehpose -- steht sie nur da: melden, dann eine Zeile
  auf pourBottle; SP Duengen/Kompost; Unkraut; MP als user). Offen: Spieler saet selbst neu -> Duenger-Marke (G1, Abhilfe in Farm-7).
- v3.14.13 FARMER TEIL 7 -> `_docs/testliste_v3.14.13.md` (Regelfenster SP + MP als admin, Schichtblock 'Fields' SP + MP, Saat-Haken SP,
  Sonde FarmWhy/Netz-Rast). Reste: Assign-Menue prueft den Abstand nur beim Menuebau; MP-Client ohne Saat-Haken bis Neueinloggen.
- v3.14.14 FARMER TEIL 8 (letzter) -> `_docs/testliste_v3.14.14.md` (SP ganzer Kreis Mehltau-Rezept mit Speichern mitten in der Charge,
  MP als user, MP Neubau mitten in der Charge (Kritik 7), Raender: gemischte Milch/unter 1 l, Milchkarton, Wasserflasche mit Milch, volle Tasche).
  Das Rezept haengt NICHT am Farmer-Schalter. Frage R15 (volle Tasche haelt die Station an) offen, Empfehlung so lassen bis zum Test.

BANDITS-UPDATE 27.10. 08:55 (nicht unsere Version, beim naechsten Test nebenbei ansehen): Crew klettert frueher ueber niedrige Zaeune
(Farmer am Feldzaun, Pflegerin am Gehegezaun -- Zaun statt Tor?); an einer verschlossenen Tuer, durch die sie nicht durchgefuehrt wird,
Bildrate beobachten. Einzelheiten _docs/uebergabe_2026-10-26.md ~17:05.

MP-TESTS GESAMMELT (Kevin 24.10.: 'dafuer mp zu starten lohnt sich nicht ... das machen wir spaeter wenn mehr dazu kommt'):
1. Liegende holen aus der Ferne (v3.13.96 b): Testaccount Rolle user, Liegende 90-130 Kacheln weg, 'Bring here' -> liegt neben ihm, Tasche komplett,
   kein zweiter Koerper, kein Kick (Aurusines Fall, Serverteil fetchDowned).
2. Wassertraeger als user (v3.13.97): fuellt, kein Kick, Liste nach Aus-/Einloggen noch da; Tonne in fremder Basis wird abgelehnt.
3. Optional Crew-Leiche (v3.13.96 a): Immortal aus, Companion stirbt -> Server-Konsole [TC-CREWBODY], Clean up corpses laesst sie liegen.
Ausgelassen: Tuer-Schutz feindliche Schuetzen (kaum gezielt ausloesbar). Bei jedem MP-Test: bugwatch, Testaccount-Konsole nur per vollem Pfad.

**SP-TEST 29.10. (Kevin, v3.14.14, Konsole ausgezaehlt): BESTANDEN** -- Feld zeichnen, Sorte, Zuweisung; Graben mit Haenden (keine Schaufel
im Lager, richtig) und mit Schaufel (holt sie sofort, Pose); Saeen Karotten 14 Saat/14 Beete, Tomate 8/7 (1 Samen in der Tasche);
Giessen 21x; Kompost genau einmal je junger Pflanze (14x), leere Saecke zurueck; Ernte 63 Karotten, 63 abgeliefert, 0 Boden/0 verloren;
Abraeumen + Neu-Saeen nach der Ernte (12 Saat); Schaufel-Zaehltest 5 = 5 (Kevin: "es stimmt alles"). Kein ***/VERLUST, kein eigener Fehler.
Noch offen in SP: Mehltau-Spray (Pose!), zu schwer (Wassermelone), Mehltau-Rezept mit Speichern, Schichtblock Fields, Regelfenster-Raender.
- TEST 31.10. (v3.14.17 gestaged): E1 Warteschlange BESTANDEN (Kevin: Baeuerin meckert, dass ein Spieler zu nah ist, laesst das Beet aus).
- TEST 31.10.: Punkt 1 BESTANDEN (furrows-Texte, Fertilize off/fertilizer/compost/both im Regelfenster).
- TEST 31.10.: Punkt 4 Munitions-Schachtel UEBERSPRUNGEN (Kevin: schwer zu testen) -> geht ungespielt mit, in den Patchnotes nicht als bestaetigt nennen.
- TEST 31.10.: Punkt 3 Lager-Einordnung BESTANDEN (Log: M14Clip -> ammo, MetalworkMag2 + Ammo-Maker-Lesemagazin -> literature per Sortierer, TomatoBagSeed2 -> tools); leere Saatpackung GESTRICHEN (Kevin: wegen Fremd-Mod-Bug nicht testbar) -> ungespielt. Mini-Ruckler alle ~4 s: Profiler 0 Bilder > 200 ms, Diag(1) aendert nichts; Verdacht Farmerin-Scans (E2-Sperre v3.14.15), Kevin testet Farmerin auf Stay.
- 31.10.: Ruckler alle ~4 s auch mit Farmerin auf Stay und Logging aus (Diag 1) -> Kevin: 'wir gucken wegen den rucklern spaeter' -- OFFEN, spaeter mit TrueCompanions_Diag(2) + TrueCompanions_ProfilePrograms(30) messen (Profile(30) fand 0 Bilder > 200 ms); vor dem Upload klaeren, ob unsere Mod schuld ist.
- TEST 31.10.: Punkt 5 steckengebliebene Waffe BESTANDEN (Kevin: mehrere killen lassen, nichts doppelt).
  RUCKLER NUR IN DER BASIS (Kevin 31.10.). Log: 5 Sortierer (Test Crafter, Oliver Thomas, Bretter hersteller, Natalie Harris, Hazel Brooks) pruefen je ~500-600 Bilder die Entladezone ('[TC-CAR] Fahrzeuge in der Zone, aber nichts Nehmbares, 1 Fahrzeug, 0 Stueck') und planen Lagergaenge -- versetzt = alle 2-4 s ein Scan. Verdacht: Sortierer-Durchlaeufe (Lager-/Fahrzeug-Scan). Spaeterer Test: Sortierer 1 min auf Stay bzw. Auto aus der Entladezone fahren; dann TrueCompanions_ProfilePrograms(30) mit Diag(2).
- TEST 31.10.: Mehltau-Spray BESTANDEN laut Log (holt GardeningSprayMilk, 2 Beete je 1 Gabe 5.0 -> 0.0); Spruehpose NICHT beobachtet (Kevin hat es nicht gesehen) -> Pose ungeprueft. Fields-Warnung 'plants have mildew' von Kevin nicht gesehen (Pflanzen waren reif/schnell behandelt) -- ungeklaert, ob die Zeile erscheint.
- TEST 31.10. MP: Beacon-Ausbau Stufe 1 -> 2 als Testaccount BESTANDEN (Kevin: hat geklappt) -- Punkt 16 vor-upload erledigt.
- TEST 31.10. MP: Tod mit Unsterblich aus BESTANDEN (Kevin: nicht nackt, hatte alles an). Server-Log: OnZombieDead kommt auf dem dedizierten Server an (Testpunkt 1 v3.14.17 GEMESSEN), Urteil grave, Manifest 5/5, Kleidung 10/10, Waffen 3/3, Munition 6/6, Zufallsbeute gesperrt. E1 (Client-Anzeige bis Relog) noch offen -> Inhalt sofort/nach Relog.
- E1 GEMESSEN 31.10.: im MP sieht der Spieler Waffen/Munition/Taschen-Inhalt der toten Crew erst NACH RELOG (vorher Bandits' Leichen-Fassung); Server-Daten stimmen. Kevin entscheiden lassen: Bandits-Todes-Handler fuer unsere Crew-Kopie ausschalten (Eingriff) oder Patchnotes-Zusatz '(visible after relogging)'.
- v3.14.29 -> `_docs/testliste_v3.14.29.md`: Bilder BESTANDEN, Favoriten teils (01.11.). Kevin 01.11. ~19:30: 'test 4 und 5 noch merken das
  teste ich spaeter' -> OFFEN: Punkt 4 Ernte-Menge mit Skill 10, Punkt 5 MP als user (giesst/erntet, Skill steigt, kein Kick), dazu Punkt 3
  XP-Teil und Favoriten 'anheften + neu laden bleibt'.
- v3.14.30 -> `_docs/testliste_v3.14.30.md` (SP breit 2 Spalten + Karten oben rechts, SP schmal + Remove auf Karte, SP Storage-Hinweis
  neben/unter der Ueberschrift, MP als user Karten/Remove). Am Ende der Liste stehen die v3.14.29-Reste nochmal.
- v3.14.31 -> `_docs/testliste_v3.14.31.md` (Stock-Fenster 50.000, Zaehlung ueber mehrere Bilder): SP Normalfall, Ruckeln messen mit TrueCompanions_StockLoad(50000) bei Crew logging, Abbruch, MP als user. Offen auch Integrator-Fragen 1 (Wartezeit 'Counting...' beim Oeffnen) und 2 (Abstand der automatischen Zaehlungen).
- VOR-UPLOAD-LISTE: `_docs/testliste_vor_upload_v3.14.35.md` (19 Punkte, fasst v3.14.29-.35 zusammen, ersetzt die v3.14.32-Liste).
- v3.14.32 -> `_docs/testliste_v3.14.32.md` (lange Rezeptzeilen).
- v3.14.34 -> `_docs/testliste_v3.14.34.md` (Crew-Grenze haengt an der Beacon-Stufe). v3.14.35 -> `_docs/testliste_v3.14.35.md` (Login-Schild, Regel D).
- v3.14.36 -> `_docs/testliste_v3.14.36.md` (Entlassene am vollen Tor, Settings '100 (sandbox: 10)'; Absage nur UEBER der Grenze). SP-Test nicht nochmal verlangt, Kevin geht direkt in den MP: die 6 Punkte in `_docs/testliste_mp_v3.14.36.md` (Punkt 5 am 02.11. berichtigt).
  MP-TEST 02.11. abends: Punkt 1 BESTANDEN (4.005-Zeichen-Zeile gespeichert, nach Serverneustart geladen, 10.509 abgelehnt mit Rezeptnamen, Testrezept wieder geloescht, Datei wieder leer). Punkt 6 BESTANDEN ohne Zombie auf Crew-Platz (Melder-Fall NICHT nachgestellt): Herholen 6 s nach Login, 0,14 s bis Ankunft; Schild 16 s, Crew erst nach 22 s (Store Keeper 37 s, Outfit-0-Wiederholung), also 5 s Luecke; Patchnotes angepasst.
  MP-TEST 02.11. spaet: Punkt 2 BESTANDEN (Graben, Giessen, Ernte als user, Skill 76, Karten; Teilpunkt 'fremde Basis kein Remove' gestrichen, Fenster oeffnet nur fuer den Besitzer, statisch). Punkt 3 BESTANDEN (500 von 500 in 10 Paketen, 0,6 s; 490 von 500 Grund full beim Farmer richtig; nach Serverneustart 500 da). Punkt 4 BESTANDEN nur fuer Beenden 2 s NACH der Kette (Kette 0,6 s, von Hand nicht zu unterbrechen). Punkt 5 BESTANDEN: Ticket faellt sofort, Grenze 3, nach Entlassen 'crewfull (5/3, Stufe 1)', Gabe bleibt, kein Kick; Ausbau Stufe 1->2 BESTANDEN (Server 'Grenze 5 (Beacon-Stufe 2) -> full', Limit 10). MP-Liste v3.14.36 damit durch.
  MP-TEST 03.11. 02:18: Eimer-Fall BESTANDEN als user: Farmer mit Axt + Schaufel (5 kg) holte BucketForged aus der Kiste (Manifest), kein 'bag too full', kein Kick. Name SP bestanden, MP nicht geklickt. Holzfeuer (Punkte 4+5) UNGESPIELT, nach dem Upload.
- v3.14.38 -> `_docs/testliste_v3.14.38.md` (ersetzt v3.14.37: SP Eimer ueber 4 kg, SP Name auf der Karte, SP kaltes Holzfeuer samt Sperre, MP als user Eimer + Karte + Holzfeuer).
- v3.14.33 -> `_docs/testliste_v3.14.33.md` (MP als user 500 Naegel in einem Klick, 1.200 Bueroklammern Stopp bei 1.000 SP+MP, SP Patronen/Zaehler, MP Abbruch beim Beenden). Companion braucht grossen Rucksack, sonst stoppt das Gewicht zuerst.
- v3.14.39 -> `_docs/testliste_v3.14.39.md` (ersetzt v3.14.38: offen Holzfeuer SP+MP und Name-Klick MP; neu SP Auswahl-Pruefung Boil water + Show, SP alter Stand Milchfass-Ziel, SP Tonne benennen, MP als user Namen). Integrator-Fragen 1-7 (Brunnen/Milchfass als Quelle, Mischung, offene Regentonne, ein Name je Kachel, MP-Besitzregel, Name nur geladen) offen bei Kevin.

- v3.14.40 (03.11. 22:17, Foerster-Zonen der Basis + Namen + Zonenwahl im Schichtplan): `_docs/testliste_v3.14.40.md` (ENTHAELT alle offenen Punkte aus v3.14.38/.39 -> diese Liste reicht, 11 Punkte); 8 Fragen in `_docs/fix_v3.14.40/v3.14.40_integrator.md` (Vorgaben gebaut, nichts blockiert). Patchnotes `_docs/patchnotes_v3.14.40_short.txt` (3255 Z.) decken v3.14.39+.40 seit v3.14.38.

- SAMMELTEST NACH DEM PLUENDERER (Kevin 06.11. ~20:50): `_docs/testliste_v3.14.52.md`, `.53`, `.54`, `.55` und die kommende `_docs/testliste_pluendern.md`; dazu die Reste nach dem Upload v3.14.51. Bei v3.14.55 entscheidet die Sonde [TC-SENDHOME], ob eine Figur von fern laeuft.
