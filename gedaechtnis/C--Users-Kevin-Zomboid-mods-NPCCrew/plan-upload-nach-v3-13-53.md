---
name: plan-upload-nach-v3-13-53
description: "Kevins Ablauf 15.10.2026 -- nach v3.13.53 Pause, testen (SP+MP), hochladen; Leichen entsorgen und Crew Backpack erst im NAECHSTEN Update"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7fd0ad-7592-45c0-90c1-5c2a73830a30
  modified: 2026-10-15T17:37:48.969Z
---

Kevin 15.10.2026: "wenn der v3.13.53 (Haken/Stall) fertig ist ... dann machen wir erstmal eine pause und testen das und laden das hoch und du
merkst dir dann die naechsten schritte fuer das naechste update".

DIESES UPDATE (Upload nach den Tests): v3.13.49 (Hold ground Zaun), v3.13.50 (MP-Kopien-Netz Waisen), v3.13.51 (Folgende erst bei stehendem
Auto, Messer-Anzeige, Stehkachel, Haken bei Ankunft), v3.13.52 (Flamme 1.9/Rauch/Asche/Kadaver im Feuer, Grill Meat, Meat Stew, All stats C),
v3.13.53 (Kevins Antworten 6-10: Haken nicht verlegen solange belegt, kein Haken in fremdem Safehouse, selbst aufgehaengtes Tier weiter
zerlegen, tote Henne im Nest rausholen, Stalltuer selbst oeffnen/schliessen) -- plus ganz Tierpfleger Stufe 3 (v3.13.30-.48), ungespielt seit
v3.13.38. Vor dem Upload: Testliste _docs/testliste_stufe3_kurz.md (SP + MP), Sperre SlaughterSoon fuer die FERTIGE Stufe 3 ganz entfernen
([[schlachten-coming-soon]]), Tierpfleger fuer alle an ([[tierpfleger-schalter-upload]]), Patchnotes kurz <4000 Zeichen Klartext
([[patchnotes-nur-klartext]]) mit Satz 'Named animals are never slaughtered', Live-Beschreibung von Steam abgleichen, spiegeln/stage, Kevin
laedt hoch, park. CLAUDE.md-Nachtrag zu v3.13.50 (zwei falsche Saetze v3.9.8/v3.9.49(b)).

ALS ALLERERSTES NACH DEM UPLOAD (Kevin 15.10. ~21:10): STOCK-REITER JE ZUSTAND -- eigene Zeile je Zustand ("Steak 7", "Steak (gegrillt) 5",
"Steak (verdorben) 2", auch verbrannt), Herausnehmen nimmt genau diesen Zustand. Heute gruppiert client/ISUI/BanditsNPCStorageStock.lua nur nach
getFullType (Name S.TypeName = Skriptname, rohes Bild), die Take-Wege zaehlen getFullType == ft (:426/:460/:499/:536). Erst danach Punkt 1 der Liste.

REIHENFOLGE NACH DEM UPLOAD (Kevin 15.10.2026 ~18:20, verbindlich; ~18:25 ergaenzt "bevor der farmer kommt ist noch wichtig das der
wassertraeger mehrere tonnen auffuellen kann"): 1. LEICHEN ENTSORGEN, 2. WASSERTRAEGER MEHRERE TONNEN (mit Prioritaet, ab 75 %),
3. FARMER, 4. CREW BACKPACK, 5. PLUENDERN, 6. STREIK bei 100 % Beduerfnis, 7. SANDBOX MAXIMALE CREW (Vorgabe 30, 1-100, Beacon-Hoechststufe =
diese Zahl), 8. SANDBOX PVP (Companions greifen Spieler anderer Fraktionen an, Vorgabe AUS) -- 7 und 8 "ganz am ende" (Kevin ~18:35). Details
aller acht in [[moegliche-features]]. DAZU: AMMO HUD UEBERARBEITEN -- erst NACH dem Upload (Kevin ~18:45: "ne das soll erst nachdem upload
kommen"), Platz in der Liste nicht festgelegt (vor dem Start der Reihe kurz fragen).

NAECHSTES UPDATE (danach, nicht vorher anfangen ohne sein Wort): (1) LEICHEN ENTSORGEN -- ueberall auf der Karte, eigene Flaechenart,
verbrennen mit dem Feuer-Code der Tiere, Recherche in _docs/leichen/ (A-D), Fragen an Kevin zuerst (Leicheninventar!); siehe
[[moegliche-features]]. RECHERCHE FERTIG 15.10. ~16:15 (_docs/leichen/A-D): A-Life sammelt/verbrennt NICHT (Deinstallations-Werkzeug +
Option Residents_ClearCorpses: loescht Zombieleichen in Bewohner-Gebaeuden, wenn niemand hinsieht; removeCorpse, Inventar weg) -- Vorlage ist
unser Tierpfleger. Plan C: eigener Knopf/Fenster, Flaeche ohne Beacon (max 60x60, Speicher TrueCompanionsCorpses), Programm NPCCorpse,
Brennstelle auto in der Flaeche, ~3 Versionen/3500-4000 Zeilen/~50 Texte. Kritik D: 0 toedlich, 8 ernst (u. a. HOLDS_POST Pflicht, Ende-Regel
falsch, sichtbare Menschenleiche evtl. DOCH moeglich ueber AddWorldInventoryItem mit CorpseMale-Item -- TimedActionsTests.lua:272-274, Jar
pruefen; Kleidung = auch Schmuck/Westen/Helme; Beute entsteht evtl. erst beim Oeffnen). FRAGEN AN KEVIN (beim naechsten Update stellen, oder
wenn er fragt): Inventar (Boden/liegen lassen/mitverbrennen), NEUNTE AUSNAHME IsoDeadBody.isZombie() (sonst keine Unterscheidung
Zombie/Spielerleiche -- ohne sie nicht bauen), Brennstelle auto+verlegbar, Ende des Auftrags, tote Banditen ja / Tiere+Crew nie, Bedienung;
dazu aus D: Logout an der Flaeche, sichtbarer Haufen, ungeoeffnete Leichen, wertvolle Kleidung. KEVIN 15.10. (beim Pluender-Wunsch): Leichen
entsorgen laeuft wie das Pluendern -- per Knopf uebernehmen ALLE Folgenden in der Naehe den Job, am Ende laufen alle zum Spieler zurueck, nur EINE
aktive Flaeche, erweiterbar, wird beim Ende entfernt (Details [[moegliche-features]] Pluendern). Der Plan C (Knopf in der Berufszeile EINER NPC)
muss darauf umgestellt werden. (2) CREW BACKPACK -- Modell Militaerrucksack Wueste, Rezept Schneider 1 Militaerrucksack + 2 grosse Haeute + 4 Faden,
+100 Traglast, nur NPCs, SP+MP; siehe [[moegliche-features]].

STAND 15.10.2026 ~19:45: v3.13.51/.52/.53 GEBAUT (Tags review-head-v3.13.51/.52/.53), alles ungespielt. TESTPAUSE BEGONNEN. Kevins Testliste:
_docs/testliste_upload_2026-10-15.md (12 Punkte, SP 1-8, MP 9-12). Nach dem Test: Fixes falls noetig, dann Mini-Version 'Sperre Coming soon
raus' + Upload-Vorbereitung. CLAUDE.md 4.5 auf 2963 nachgezogen.

FIX-VERSION VOR DEM UPLOAD (aus Kevins Test 15.10. abends, Liste _docs/testliste_upload_2026-10-15.md Abschnitt 'Befunde'): F1 All stats Zahlen nach laengstem Text + Abstand oben; F2 Storage-Reiter zeigt oben, welche Kategorie UND welche Einzelkiste (Ertrag/Mist/Fisch/Posteingang/Liefer) voll ist -- Kevins Wahl 'in die Fix-Version vor dem Upload', Umfang 'alles'. F3 (Kevin ~20:20): grosse Kadaver nach 24 h direkt zur Brennstelle statt erst verrottet (aendert 18(b) aus [[stufe3-entscheidungen]]). F4 (~21:00): Crew isst zuerst, was am fruehesten verdirbt (Tasche + Kiste), Konserven zuletzt. Gebaut wird nach Kevins Testrunde.

**Why:** Kevin will einen getesteten, hochgeladenen Stand, bevor neue grosse Features dazukommen.
**How to apply:** Nach v3.13.53 nichts Neues bauen, sondern Testliste liefern, Upload vorbereiten; die zwei Features erst danach.

STAND 15.10.2026 ~21:00: Kevins SP-Test von v3.13.53 fertig (Ergebnisse _docs/testliste_upload_2026-10-15.md: 2/3/6/7/Auto bestanden,
1 gestrichen, 4 Brennstelle + 5 Stall NACH der Fix-Version). Befunde F1-F6 -> FIX-VERSION v3.13.54 laeuft als Workflow wf_4d0249ad-607 (Tag
fix54-base-v3.13.54, Berichte _docs/fix_v3.13.54/, dort auch Konsolen- und Spielstand-Kopie fuer F6). DANACH: Kevin testet SP 4+5 und MP 9-12 +
Auto im MP, dann Mini-Version Sperre SlaughterSoon raus + Upload-Vorbereitung. Kevin wechselt am 16.10. auf seinen anderen Account (Wochenlimit
hier 82 %); eine neue Sitzung liest zuerst diese Datei und _docs/testliste_upload_2026-10-15.md.
KEVIN 15.10. ~21:30: neuer Chat erst beim Account-Wechsel, wenn das Wochenlimit (fast) 100 % erreicht -- VORHER Uebergabe schreiben
(_docs/uebergabe_<datum>.md + Zeiger hier), sobald get_usage ~95 % meldet oder Kevin den Wechsel ankuendigt.
STAND 15.10. ~22:45: v3.13.54 FERTIG (F1-F5, Tag fix54-base, Pruefer 0 toedlich; ungespielt). Kevins Antworten: F6-Altlast VOR dem Upload
reparieren, F3-Randfall so lassen, F4 'Verderb zuerst' -> v3.13.55 laeuft (wf_ad2a93a9-21c, Tag fix55-base-v3.13.55, Berichte
_docs/fix_v3.13.55/). Danach: SP-Tests (Kevin will zuerst NUR die SP-Liste), dann MP-Liste, Patchnotes, spiegeln, Upload. Sperre SlaughterSoon ist
schon aus (return false), Aufraeumen der toten Funktion erst nach dem Upload. Safehouse-Test gestrichen.
STAND 16.10. 00:40: v3.13.55 FERTIG (0 toedlich, gesichert). SP-Testliste an Kevin geschickt; er testet nach dem Schlafen. Nichts Neues starten bis dahin.
STAND 16.10. ~10:30: SP-Test v3.13.55 fertig (F1 F2 F3 F5 K1 K2 ok; Stall-Test gestrichen). Neue Befunde F7 (Kadaver nie sichtbar im Feuer,
getItem-Abbild), F8 (Rauch smokea 1/smokek 1.5 als Vorgabe + Farbregler), F9 (All stats rechte Seite) -> v3.13.56 laeuft (wf_c995e4c8-e52,
Tag fix56-base-v3.13.56, erste Version mit zwei Bauern parallel + Textlisten). Danach: kurzer SP-Blick auf F7-F9, dann MP-Test, Upload.
STAND 16.10. 13:19: UPLOAD ERLEDIGT -- v3.13.56 oeffentlich (Steam 20.047.263 Byte = Upload-Ordner, Tag upload-v3.13.56, Ordner geparkt).
SP+MP getestet (Testliste _docs/testliste_upload_2026-10-15.md, Abschnitte 'SP-Test v3.13.56' und 'MP-Test v3.13.56'); ungespielt mitgegangen nur
die Brennstelle im MP (Kevin: 'testen wir spaeter'). Beschreibung: Tierpfleger-Zeile neu, '80% done' raus, neutral. AB JETZT gilt die Reihenfolge
oben: ZUERST Stock-Reiter je Zustand, dann 1 Leichen ... 8 PvP. Kleiner Rest: Tooltip UI_BN_Herd_R_CarcassTip sagt noch '(its door must be open)'
in 7 Sprachen (seit v3.13.53 falsch, die Pflegerin oeffnet selbst); tote Funktion SlaughterSoon aufraeumen.

**KEVIN 16.10. ~15:45: NEUE REIHENFOLGE -- ALS ERSTES der Selbsttest/Mod-Pruefer (Feature 10, Bauplan _docs/bauplaene_2026-10-16/10_selbsttest_fernsteuerung.md aus dem Lauf wf_851ba69a-0ae)**: *"als erstes will ich diesen mod pruefer eingebaut bekommen wo du selbst alles neues testen kannst"*. Danach Stock-Reiter je Zustand und der Rest wie oben. Dazu NEU auf der Liste: Zeitraffer trotz Crew (siehe [[moegliche-features]]).

**KEVIN 16.10. ~20:20 (Antworten):** Selbsttest ST-1..13 alle nach Empfehlung; SR-12 JA (Zustands-Setter nur auf eigenen Teststuecken, in CLAUDE.md 3 eintragen); Fix A (Verlust/Verdopplung aus _docs/modcheck_2026-10-16/BERICHT.md) DIREKT NACH dem Selbsttest; uebrige Fragen erst, wenn das Feature drankommt. Reihenfolge damit: Selbsttest (3 Versionen) -> Fix A -> Polsterung -> Stock-Reiter -> ... Antworten stehen auch unten in _docs/bauplaene_2026-10-16/UEBERSICHT.md.

**KEVIN 16.10. ~20:35: ZWEITER MOD-CHECK-LAUF auf die Liste** (*"starte das nachdem der aktuelle workflow durch ist oder jz falls die sich nicht behindern"*): die 52 ungeprueften Funde aus _docs/modcheck_2026-10-16/BERICHT.md Abschnitt 4 (U00-U51, Rohdaten funde_roh.json "rest") je mit Widerleger pruefen + Abdeckungsluecken nachlesen (BeaconWindow.lua, Teile Slaughter/SlaughterWindow, R15 Pruefer; dazu Nicht-Lua: sandbox-options, scripts, AnimSets, UI.json). ~15-20 Agenten, NUR LESEN, Ergebnis an den Bericht anhaengen. Zeitpunkt: NACH dem Bau v3.13.57 (wf_f60d5a9c-4e0) und wenn das 5-h-Fenster Platz hat (16.10. Reset 23:40) -- nicht gleichzeitig, weil sonst das Limit reisst (Bau ~15-20 %, Lauf ~30-40 %). Reihenfolge danach: Fix A (mit den neu bestaetigten Funden) -> Selbsttest Teil 2/3 -> Polsterung -> Stock-Reiter. Kevin hat zu "Fix A direkt nach Selbsttest TEIL 1" noch nicht ausdruecklich ja gesagt (mein Vorschlag).
  Termin ersetzt durch Nachtschicht-Termin 4bdcdcde (alle 30 min), siehe _docs/nachtschicht_2026-10-16.md (nur in Sitzung c3f66696) -- startet den zweiten Check, wenn der Bau fertig ist und das Fenster Platz hat.

**Aus dem Index hierher verschoben (06.11.):** Upload v3.13.56 erledigt 16.10. 13:19; Reihenfolge danach (Kevin 16.10.): zuerst Selbsttest/Mod-Pruefer, dann Stock-Reiter je Zustand, dann 1 Leichen, 2 Wassertraeger mehrere Tonnen, 3 Farmer, 4 Backpack, 5 Pluendern, 6 Streik, 7 Max-Crew-Sandbox, 8 PvP-Sandbox.
