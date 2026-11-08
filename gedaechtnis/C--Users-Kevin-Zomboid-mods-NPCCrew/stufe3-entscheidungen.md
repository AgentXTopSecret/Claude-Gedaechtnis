---
name: stufe3-entscheidungen
description: "Kevins Antworten zu Tierpfleger Stufe 3 vom 12.10. (Schlachten automatisch mit Hauptschalter AUS, Alter 99 %, 2 Tiere/Tag, eine Entsorgungsstelle je Basis, Fake-Feuer zuerst, Bestand zaehlt nur Erwachsene; UMSETZEN GESTRICHEN)"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7fd0ad-7592-45c0-90c1-5c2a73830a30
  modified: 2026-10-15T17:37:20.646Z
---

Kevin hat am 12.10.2026 (~17:05, zweites Konto) die Fragen zu Tierpfleger Stufe 3 beantwortet. Sie stehen auch im
Uebergabeblatt `_docs/uebergabe_2026-10-12.md` (Abschnitt "KEVINS ANTWORTEN ZU TIERPFLEGER STUFE 3"); der Bauplan entsteht in
`_docs/tierpfleger_stufe3_plan_2026-10-12.md`.

1. Schlachten laeuft AUTOMATISCH nach Regeln; Hauptschalter je Zone, Vorgabe AUS; die Liste "wuerde schlachten" ist immer sichtbar.
2. Alters-Regel Vorgabe **99 %** Lebensalter -- Kevin woertlich: "ich bin fuer ab 99% damit sie nicht sterben wegen dem alter und
   kein fleisch mehr bringen". Meine Empfehlung war 100 %, er hat sie geaendert.
3. Tempo: Regler je Zone, Vorgabe 2 Tiere pro Spieltag.
4. Entsorgungsstelle: EINE je Basis, Zuweisung im Animals-Reiter wie die Ertragskiste.
5. Entsorgungsart: Fake-Feuer zuerst (kein IsoFire; Bauform und Rauch siehe Punkt 11); Vergraben erlaubt, aber spaeter.
6. UMSETZEN IST GESTRICHEN (Kevin 12.10. ~17:15, "ja streich das mal raus"): er fragte "wofuer ist das gut?" -- der Punkt stammte
   nur aus seinem Verschreiber "verlegen" (gemeint "zerlegen", 07.10.). Stufe 3 = Schlachten, Zerlegen, Entsorgen. Nicht planen,
   nicht bauen, nicht wieder anbieten; nur Merkposten in [[moegliche-features]].
7. Hoechstbestand je Art zaehlt nur ERWACHSENE.

**Zweite Runde 12.10. ~21:50 (nach der Recherche):**
8. GROSSTIERE MIT HAKEN-ERTRAG -- Kevin woertlich: "ich will das die das mit den haken machen wie der spieler das man genauso viel
   bekommt". Seine Wahl "Haken zuweisen": Spieler baut einen Schlachthaken und weist ihn im Animals-Reiter zu, die Pflegerin bringt den
   Kadaver dorthin und zerlegt mit vollem Haken-Ertrag samt Leder; ohne zugewiesenen Haken ruehrt sie grosse Tiere nicht an. (Meine
   Empfehlung war ein Boden-Schalter mit kleinem Ertrag -- er hat sie geaendert.) Die Haken-Aktionen selbst brauchen einen IsoPlayer und
   bleiben tabu; unser Kern rechnet nur mit Vanillas Haken-Werten.
9. Mutterschutz nur fuer Saeuger (Kalb, Lamm, Ferkel); Hennen mit Kueken und befruchtete Hennen sind nicht geschuetzt.
10. Kein Stress fuer die Herde durch eine Schlachtung.
11. Feuer: Kevin will eigentlich eine ATTRAPPE; kann sie nicht flackern, dann die echte Feuerstelle (seine Wahl). Rauch entfaellt.

12. Rezept 'Forge Large Hook' beim Schmied mit Vanilla-Zutaten (Kevin: "genau nehm den mit als rezept"); den Schlachthaken baut der Spieler selbst.

13. (Kevin 13.10. ~00:10) WARNUNG BEIM ZEICHNEN EINER TIERZONE AUSSERHALB DER REICHWEITE: "beim tier zonen zeichnen ... eine warnung
    anzeigen 'outside of animal keeper' so maessig damit sie nicht enttaeuscht werden am ende". Eine Zone zaehlt nur, wenn ihr
    naechster Rand hoechstens 75 Kacheln vom Beacon liegt. Als Hinweis am Cursor/Fenster bauen, keine Sperre (Vanillas Werkzeug
    bleibt unberuehrt). Steht als Teil 3-9 im Vorgabenblatt `_docs/tierpfleger_stufe3_vorgaben_hauptsitzung.md` (Abschnitt 2c).
15. (Kevin 13.10. ~00:30) EIGENER SKILL DER PFLEGERIN: "den skill brauchen wir aber noch ;D der soll ja bewirken das wir mehr infos
    bekommen im ui ueber die tiere, und wenn moeglich dann auch stress mehr minus ... trotz das der spieler die xp und happyness
    bekommt". Heute hat die Crew acht Skills (kein Tier-Skill), beim Streicheln zaehlt der Tierhaltungs-Skill des SPIELERS. Machbar
    (statisch eingeschaetzt): neunter Crew-Skill, Zusatz-Stressabzug ueber changeStress nach Vanillas petAnimal. Teil 3-10 im
    Vorgabenblatt (Abschnitt 2d); beim Planen Kevin fragen: Infos VERSTECKEN bei niedriger Stufe oder NEUE Infos mit der Stufe?
    WIRKUNG WIE VANILLAS TIERHALTUNG (Kevin ~01:00 "ja mach das genauso wie das vorgesehn ist"): Infos im Reiter nach IHRER Stufe
    freigeschaltet (Alter/Gesundheit/Stress immer, ab 3 befruchtet/traechtig, ab 4 Gelege/Legeperiode/Deckung, ab 5 Gewicht/
    Paarungszeit/Euter dringend) -- die Frage 'verstecken oder neu' ist damit beantwortet: verstecken wie das Spiel. Melken/Scheren:
    unter Stufe 8 wie heute (ueber Stress 40 wartet sie), ab Stufe 8 auch bei Stress (von Kevin bestaetigt ~01:15); Scheren
    schneller mit der Stufe.
    STRESS BEIM STREICHELN (Kevin ~00:45, geht vor): "nur einmal abgezogen ... und zwar vom npc level abhaengig" -- EIN Abzug
    nach IHRER Stufe statt nach dem Level des Spielers, kein Zusatz obendrauf; Spieler behaelt XP und Stimmung. ENTSCHIEDEN
    (Kevin ~00:50 "ja mach das so"): Rand(7,11) + ihre Stufe; Bauform: Vanilla-Streicheln rufen, dann per changeStress auf den Zielwert ausgleichen.
    XP-Quellen (Kevin ~00:35): nur Handlungen direkt am Tier -- Melken, Scheren, Streicheln ("vllt hab ich noch was vergessen");
    dazu Schlachten und Zerlegen (Kevin ~00:40: "kann dazu zaehlen"). Abendruf und Troege fuellen: genannt, von ihm nicht bestaetigt -> zaehlen nicht.
14. (Kevin 12.10. spaet) Die Liste 'All stats' schoener: Bilder + mehr Abstand = Teil 3-8 im Vorgabenblatt (Abschnitt 2b).
15b. (Kevin 13.10. zwischen 17:20 und 18:00, Antworten auf die Vorplanung Teil 3-10 -- GELTEN) STREICHELN: "die stufe vom npc zaehlt und das soll
    ... ohne kick laufen" -- Form A (setDebugStress zum Zurueckstellen, dann EIN Abzug nach ihrer Stufe), BEDINGUNG kein Kick/keine
    Ablehnung fuer Rolle user mit AntiCheat 2; der Aufruf nur im Einzelspieler lokal und im Mehrspieler auf dem SERVER (6-Byte-
    Feldschreiber, die Admin-Sperre steckt nur in Vanillas Lua-Befehl, den wir nicht rufen); Pflicht-Test als user vor dem Upload.
    ZUSATZ-ZAHLEN im Tier-Reiter (Gesundheit %, Stress, Hunger/Durst %): erst ab Stufe 6 der Pflegerin (seine Zahl, mein Vorschlag war 5),
    MIT sichtbarem Hinweis, dass ab Stufe 6 mehr angezeigt wird; bei mehreren Pflegerinnen zaehlt die hoechste Stufe derer, die dort
    arbeiten (gebaut als: der Zone zugewiesen -- MEINE Auslegung, ihm genannt). ZONE OHNE ZUGEWIESENE PFLEGERIN (Kevin, selbe Runde: "ja wie stufe 0"): Grundanzeige wie
    Stufe 0, die Stufe des Spielers zaehlt dort nicht. XP-VERLUST ALLER CREW-SKILLS IM MP BEIM EINSTREAMEN (Kevin, selbe Runde: "ja beheb das da
    darf nichts verloren gehn"): wird behoben, als eigene kleine Version direkt nach der Kreis-Bug-Version und VOR Teil 3-2 (meine
    Reihenfolge, ihm genannt), erst belegen, dann bauen. Einzelheiten:
    _docs/tierpfleger_stufe3_vorgaben_hauptsitzung.md Abschnitt 2d-Nachtrag, Plan _docs/stufe3_bau/plan_teil_3-10_skill.md.
16. BAUSTAND 14.10.2026 00:45: Teil 3-1 (v3.13.30) und Teil 3-2 (v3.13.40, Kadaver/Zerlegen/Knochen im Einzelspieler) sind gebaut, beide
    ungespielt. Naechster Teil: 3-3 (Zerlegen im Mehrspieler) als v3.13.41, dann 3-4, 3-5, 3-7, 3-6, 3-8, 3-9, 3-10 -- Skript
    _docs/stufe3_bau/workflow_stufe3-teil-bauen.js (seit 13.10. ohne Workshop-Spiegel), Stand in _docs/stufe3_bau/STAND.md. Kevin testet am
    Ende alles; gebaut wird nur, solange sein PC laeuft (nicht ueber Nacht).
17. KEVINS ANTWORTEN 14.10.2026 ~13:10 (zu den Resten von v3.13.40): (a) Reste vom Zerlegen (Federn, Fleisch, das nicht passte) in einer
    Zone OHNE lebende Tiere: JA einsammeln -- danach ignoriert sie die Zone wieder; (b) gekochtes Fleisch in ihrer Tasche bleibt PROVIANT:
    sie darf es essen und liefert es NICHT ab (cropCarried/roomRule/yieldRun dieselbe Ausnahme wie der Ess-Riegel; nur rohes Fleisch und
    Knochen sind Ertrag). Teil 3-3 lief da schon (wf_e13ebcb9-ba0) -- beides als Pflicht in den naechsten Bau-Lauf (3-4) bzw. eine kleine
    Version davor, in SP und MP.
    Stand 14.10. ~14:55: 3-3 als v3.13.41 fertig (gesichert, Tag review-head-v3.13.41), 3-4 (Schlachten) laeuft als v3.13.42 mit beiden Antworten als Pflicht.

18. KEVINS ANTWORTEN 14.10.2026 ~19:50 (Fragen aus v3.13.43, Verbrennen): (a) TOTE BENANNTE TIERE wie alle anderen behandeln ("tot ist tot") --
    zerlegen, Knochen, verbrennen wie jeder Kadaver; der Name schuetzt nur das LEBENDE Tier vor dem Schlachten (so verstanden und ihm gesagt);
    (b) Kuh/Schaf/Schwein ohne Haken-Zerlegung erst VERROTTET verbrennen (wie gebaut); (c) Brennstelle IN Gebaeuden ERLAUBEN (gebaut war
    'indoors' ablehnen -> aendern); (d) Brennstelle im Hof eines fremden Safehouses erlaubt (wie gebaut). (a) und (c) als Pflicht in den
    naechsten Bau-Lauf (3-6, v3.13.45), weil 3-7 schon lief.
    (e) Kevin wusste nicht, dass benannte Tiere geschuetzt sind: SICHTBARE Zeile im Schlachtfenster (nicht nur Hover) + Satz in Patchnotes und
    Workshop-Beschreibung beim naechsten Upload ('Named animals are never slaughtered - give an animal a name to protect it').

19. KEVINS ANTWORTEN 14.10.2026 ~20:25 (vor der Nacht): Rezept 'Forge Large Hook' IMMER sichtbar, auch unter der Sperre SlaughterSoon
    (3-7 baute es hinter die Sperre -> im 3-6-Lauf aendern); Sammelstelle am Haken nimmt auch Kevins Stuecke mit (wie gebaut); Haken darf in
    Tierzone und Gebaeude (wie gebaut); beim Verbrennen hebt sie den Kadaver auch auf, wenn ein Spieler daneben steht (wie gebaut).

20. STUFE 3 KOMPLETT GEBAUT (15.10.2026 04:20): v3.13.30 (3-1) bis v3.13.48 (3-10), alle Teile mit Pruefern, ALLES UNGESPIELT seit v3.13.38.
    Kurze Testliste (Kevins Wunsch, nur das Noetigste): _docs/testliste_stufe3_kurz.md. Geparkte Fragen (14 Stueck) und naechste Schritte stehen im
    letzten Eintrag von _docs/stufe3_bau/STAND.md. Als ERSTES danach: MP-Luecke Populations-Waise ([[workshop-meldung-duplikate-14-10]]).

21. BRENNSTELLE (Kevin 15.10. im SP-Test): Flamme groesser -- TrueCompanions_PyreFx("k", 1.9) ist gut (Vorgabe war 0.7) -> neue Vorgabe 1.9
    (Lv.PYREFX_DEFAULTS in client/BanditsNPCLivestockHerdScan.lua UND DEFAULTS in client/ISUI/BanditsNPCLivestockPyreFx.lua). Dazu RAUCH
    DARUEBER, deutlich sichtbar (heute liegt Smoke_03 auf der Flamme mit Alpha 0,3): eigene Lage/Groesse/Deckkraft fuer den Rauch. Bauen als
    v3.13.52 NACH v3.13.51 (nicht parallel zum laufenden Bau).
    DAZU ASCHE AM BODEN (Kevin 15.10.): waehrend es brennt ein Aschehaufen auf der Brennkachel, verschwindet MIT der Flamme. Vanillas
    Aschebild ist die Kachel floors_burnt_01_1 (Vanilla client/Tests/TimedActionsTests.lua:593 'local ashes = newObject(..., "floors_burnt_01_1")';
    Varianten floors_burnt_01_0..2). Gezeichnet wie die Flamme (getTexture, lokal, kein Weltobjekt), unter der Flamme.
    KADAVER SICHTBAR IM FEUER (Kevin 15.10.: "das tier war da ja nie sichtbar an der feuerstelle das soll ... noch kurz [sichtbar sein] und dann
    der haufen asche"): heute entfernt Kern 1 den Kadaver schon beim AUFHEBEN (removeCorpse), sie traegt eine Zahl, an der Brennstelle nur Flamme.
    Mein Vorschlag (wie Haken B3): Kadaver bleibt liegen bis zur Ankunft an der Brennstelle, dann liegt er dort ECHT im Feuer (Engine-Weg pruefen:
    Vanilla square:createAnimalCorpseFromItem(item), ISButcherHookUI.lua:561, plus Korpus->Item wie ISGrabCorpseAction), brennt seine
    Lv.PYRE_H (0,5 Weltstunden), dann weg; Asche darunter bis die Flamme aus ist. Beim Schreiber (SP direkt, MP Server), nichts doppelt.
    Kevin: "jaa mach das" -> GEBAUT WIRD ES IN v3.13.52 (mit Feuer/Rauch/Asche).

23. FRISCHE FLEISCH-REZEPTE IN v3.13.52 (Kevin 15.10.: "ja sollst du", zusammen mit Feuer/Rauch/Asche): Befund: Gefluegel hat Roast Chicken/
    Roast Turkey (gekocht, NPCs essen), aber Steak/Beef/Pork/PorkChop/MuttonChop/Rabbitmeat/Venison/Smallanimalmeat/Smallbirdmeat haben nur
    'Cure Meat' (Jerky, Salz, Stufe 2); roh ist alles DangerousUncooked -> NPCs essen es nie (FoodRules rawPiece). Neu: (1) GRILL MEAT -- ein
    rohes Stueck wird DASSELBE Stueck gebraten (cooked = true, Kevins setCooked-Erweiterung 28.09. fuer Fleisch; keine UnhappyChange am rohen
    Fleisch, food.txt geprueft), Naehrwerte und Alter bleiben; (2) MEAT STEW -- 2 Fleisch + 2 Gemuese + Bowl -> Base.StewBowl (Form Vegetable
    Stew, Schuessel kommt beim Essen zurueck). Rezeptformat hat EINEN Ausgabetyp: Grill je Sorte oder 'Ausgabe = Eingabetyp' sauber bauen.

24. ALL STATS NEU GESTALTET IN v3.13.52 (Kevin 15.10., Entwurf C aus drei Vergleichsbildern): Animals-Reiter > All stats. LINKS kompakte Liste,
    nach GRUPPEN statt nach internem Schluessel: 'Water and feed' (Wasser gegossen, Futter in Troege), 'Coop and eggs' (Eier, Federn, Stallboden,
    Nester, Stalltueren, Abendruf), 'Pasture and manure' (Gras gemaeht, Grasbueschel, Mist), 'Wool, milk and care' (geschoren, Wolle gesammelt,
    Milch, gestreichelt), 'Slaughter and butchering' (geschlachtet, zerlegt, am Haken, Fleisch und Teile, Knochen, verbrannt); je Zeile feste
    Symbolspalte (auch ohne Bild), Text links, Zahl RECHTSBUENDIG in eigener Spalte, leichte Zebrastreifen, Gruppenkopf orange mit Linie.
    RECHTS 'Seen in this zone' als TABELLE Tier | Female | Male | Young, darunter Born/Died. Die echten Gegenstandsbilder bleiben. Neue
    Gruppenkoepfe/Spaltenkoepfe = neue UI-Texte in sieben Sprachen.

25. GEPARKTE FRAGEN BEANTWORTET (Kevin 15.10.): L7 HAKEN VERLEGEN/LOESCHEN, WAEHREND IHR TIER HAENGT -- "nein erst wenn keiner mehr dran ist":
    Zuweisen/Verlegen/Loeschen des Schlachthakens im Reiter abgelehnt (mit Satz), solange ein Tier daran haengt; erst wenn er leer ist.
    L8 HAKEN IN EINEM FREMDEN SAFEHOUSE -- "nein": ein Haken in einem fremden Safehouse darf nicht zugewiesen werden (Reiter lehnt ab, mit
    Satz; Server-Pruefung beim Schreiber, Form 'foreign' wie Ertragskiste/Wasserfass). (Anders als die Brennstelle, die dort erlaubt bleibt, Nr. 18.)
    L10 KEVIN NIMMT IHR TIER VOM HAKEN UND HAENGT ES SELBST WIEDER AUF -- "ja": sie zerlegt es trotzdem weiter (wie ein von ihr aufgehaengtes).
    HENNE STIRBT IM NEST -- "ja": wird heute nicht erkannt; nachbauen -- sie holt den toten Vogel aus dem Nest wie andere tote Voegel im Stall
    (Teil 3-6-Weg, v3.13.45), nichts verloren/doppelt, SP + MP.
    STATISTIKZEILE 'TOTE VOEGEL HERAUSGEHOLT' -- "ja": neue Zeile in All stats (Gruppe 'Coop and eggs' im Entwurf C, Nr. 24), zaehlt jeden aus Stall
    oder Nest geholten toten Vogel, sieben Sprachen.
    ZONE OHNE PFLEGERIN UNTER SANDBOX 'ALLE SKILLS AUF 10' (SkillsAllMaxed) -- "ja": die Zone zeigt dann alles wie Stufe 10 (bisher Stufe 0).
    XP-TEMPO ANIMAL CARE -- "es soll so bleiben" (Raten aus v3.13.48 unveraendert).
    GESCHLOSSENE STALLTUER BEI TOTEM VOGEL IM STALL -- Kevin waehlte "Sie oeffnet die Tuer selbst, holt den Vogel raus und schliesst sofort wieder"
    (IMMER, auch nachts; der Mittelweg 'nachts warten' wurde angeboten und NICHT gewaehlt). Bisher: Status/Spruch coopdeadclosed und warten.
    VERTEILUNG (mein Plan, Kevin genannt): v3.13.52 = Feuer/Rauch/Asche + Grill Meat/Meat Stew + All stats Entwurf C MIT Leder-Zeile, Zeile tote
    Voegel und SkillsAllMaxed-Zone; v3.13.53 = Haken gesperrt solange belegt, kein Haken im fremden Safehouse, selbst wieder aufgehaengtes Tier
    weiter zerlegen, tote Henne im Nest, Stalltuer selbst oeffnen/schliessen; v3.13.54 = Crew Backpack.
    EIGENE LEDER-ZEILE -- "ja": in All stats neben 'Meat and parts' eine Zeile 'Leather' (Gruppe 'Slaughter and butchering'), die Haeute zaehlt.

26. NACH v3.13.52 (Kevin 15.10. ~17:55, Auswahl): GRILL fuer ALLE 15 rohen Fleischsorten (die 9 roten aus v3.13.52 + die 6 Gefluegelstuecke
    Chicken, ChickenFillet, ChickenWings, TurkeyLegs, TurkeyFillet, TurkeyWings); CURE MEAT und MEAT STEW nehmen NUR ROHES Fleisch; Kadaver
    liegt 15 Spielminuten sichtbar im Feuer, dann 15 Minuten nur Asche (Lv.PYRE_BODY_H 0.25, so gebaut). E1/E4 kommen in v3.13.53.

27. NACH v3.13.53 (Kevin 15.10. ~19:40, alle drei 'Empfohlen' = wie gebaut): Haken in FREMDER Basis/fremdem Safehouse darf auch mit Tier
    verlegt/geloescht werden; alter Haken nicht geladen -> Absage 'geh naeher ran' bleibt; Stalltuer geht im selben Augenblick auf und zu (nur
    Pose + Toene). Damit ist v3.13.53 abgenommen, nichts mehr zu bauen vor dem Test.

22. ANIMAL CARE SCHER-TEMPO BLEIBT (Kevin 15.10.): erst "3 hab ich nie bestellt das soll nicht schneller gehn", dann nach meiner Antwort
    (Vanilla macht es beim Spieler genauso) "okay dann lass das doch einfach drinne ist ja egal jz". -> 'Scheren -2 % je Stufe' (v3.13.48,
    S.CareShearFactor) BLEIBT, nichts aendern, nicht neu fragen.

**Why:** Kevin wollte die Fragen vor dem Plan beantworten ("kannst mir die fragen stellen fuer stufe 3"); die aelteren
Schlacht-Entscheidungen (29.09./07.10.) stehen in [[moegliche-features]].

**How to apply:** Als Vorgabe in Plan und Bau fuehren, nicht neu fragen. Meine Annahmen dazu (nur erwachsene Maennchen zaehlen
fuer die Mindestzahl; ohne Platz in der Ertragskiste kein Schlachten; Hoechstbestand aus, bis eine Zahl gesetzt ist) sind MEINE
Auslegung, Kevin wurde sie genannt. Ungeprueft blieb am 12.10. abends: ob der Kadaver sichtbar am Haken haengen kann und ob die Attrappe flackern kann.
Siehe [[uebergabe-12-10]], [[kevins-zwei-rote-linien]].
