---
name: farmer-waechter
description: "Kevin 27.10.: Waechter fuehrt den Farmer-Bau nach Limit-Abbruch weiter bis Farmer (mit Abschlusspruefung) + Server-Rezepte fertig sind, dann PAUSE; Ablauf in _docs/farmer_waechter.md"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-28T13:05:39.195Z
---

Kevin 27.10.2026 ~02:30: *"aktiviere einen waechter falls es abbricht wegen limit soll das weiter gefuehrt werden bis der farmer komplett fertig ist"*.

Gebaut als Sitzungs-Cron (stuendlich :17, Job 916b284e, nur diese Sitzung, max. 7 Tage). Ablauf, Kette (Farm-4b v3.14.8 -> Gesamtpruefung 1 ->
Farm-5a/5b/6/7/8 -> Gesamtpruefung 2 -> Ende) und Startbedingung (nur: kein ProjectZomboid-Prozess) stehen in
`_docs/farmer_waechter.md`, Zustand in `_docs/farmer_waechter_status.txt`.

Kevin 27.10. ~02:40 dazu: *"pruef den farmer am ende nochmal gut wenn alles fertig ist der soll sauber funktionieren"* -> Schritt 8 ist jetzt
die ABSCHLUSSPRUEFUNG (Werkzeuge, 8 Linsen + Widerleger + Kritiker, Fix-Version, Gegenpruefung, wiederholen bis nichts Toedliches/Ernstes,
hoechstens 3 Runden, sonst Kevin fragen); Ablauf in `_docs/farmer_waechter.md` Abschnitt 'Abschlusspruefung'.

Kevin 27.10. ~09:45: *"mach die regel weg mit 50% du sollst immer bauen egal wie viel"* -> keine Verbrauchsgrenze mehr fuer die
Farmer-Kette (weder 5 h noch Woche); Limit-Abbrueche holt der Waechter nach dem Reset nach. Gilt auch gegen die 'erst Pause'-Regel in
[[tests-sammeln-weiterbauen]] -- fuer diese Kette.

27.10. ~10:36: Cron 916b284e auf Kevins Anweisung GELOESCHT (Farm-5b v3.14.11 lief da noch). Kevin ~10:40: *"wenn der workflow durch ist erstmal pause machen"* -> Farm-5b
nur abschliessen, dann PAUSE; Farm-6 erst auf sein Wort. STAND 27.10. 11:25: v3.14.11 fertig (Tag b37-base-v3.14.11),
PAUSE. Naechstes: Farm-6 Pflege -- Skript FERTIG `_docs/nachtschicht/farm6_v3.14.12.js` (per Workflow scriptPath starten), danach
Farm-7/8 (Skripte daraus ableiten) und Abschlusspruefung (Schritt a fuer v3.14.11 schon ohne Treffer: _docs/farmer_abschluss/werkzeuge.md).

STAND 27.10. ~19:10: Farm-7 v3.14.13 laeuft (wf_4ced33bb-1d6, Tag-Basis b38-base-v3.14.12); Kevin macht spaeter den PC aus,
morgen 'normal weiter' -- Ablauf fuer morgen (auch bei abgebrochenem Farm-7) in _docs/uebergabe_2026-10-26.md Eintrag ~19:10.
Kevin ~19:15: nach Farm-7 nur abschliessen + merken, dann PAUSE; Farm-8 erst morgen auf sein Wort (Skript vorher vorbereiten).
STAND 27.10. ~20:15: Kevin faehrt den PC herunter, Farm-7 stand beim FIXER (Plan, Bau A/B, drei Pruefberichte fertig). MORGEN ZUERST:
Farm-7 fertig machen -- journal lesen, `git diff b38-base-v3.14.12 -- 42 common`, NEUER Workflow nur mit Fixer (prueft erst, was schon
geaendert ist), Gegenpruefer, ggf. Fixer2, Integrator; dann Abschluss + Maximal-Messung (beide Run-Ids) + Farm-8-Skript; Farm-8 nur
auf Kevins Wort. Einzelheiten _docs/uebergabe_2026-10-26.md Eintrag ~20:15.

STAND 27.10. ~23:15: Kevin 'okay weiter machen und mach den waechter an bei abbruch 5std limit etc automatisch weiter arbeiten' ->
NEUER Cron e03ad2c3 (stuendlich :17); Farm-7-Rest wf_cd7438bb-30a; Kette ohne Pause bis zum Ende (keine Verbrauchsgrenze). Stand in
_docs/farmer_waechter.md Abschnitt 'STAND 27.10. ~23:15'.

STAND 27.10. ~23:40: Kevin *"ok plan aenderung nach dem farmer + rezepte server seitig ist hier erstmal pause"* -> die Kette endet mit
Schritt 11 PAUSE (nach Schritt 10 Rezepte serverseitig): CronDelete e03ad2c3, Kevin melden, nichts Neues starten ([[weiterarbeiten-nach-farmer]]).

STAND 28.10. ~00:25: Farm-7 v3.14.13 fertig (Tag b39-base-v3.14.13, gespiegelt, Maximal-Messung gemeldet); Schritt 7 Farm-8 v3.14.14 laeuft als
wf_a3be91b2-4d5 (Skript _docs/nachtschicht/farm8_v3.14.14.js). Rezept-Recherche fertig (Bauplan _docs/rezepte_server/BAUPLAN_entwurf.md, Fragen an Kevin).

STAND 28.10. 04:20: Farm-8 v3.14.14 fertig (Tag b40-base-v3.14.14) -> Farmer gebaut. Schritt 8 Abschlusspruefung Runde 1 laeuft (wf_34959107-5a7);
danach A/B-Workflow mit HALTE-SCHRITT (Berichte nach backups/abschluss_hold verschieben) -- Ablauf in _docs/farmer_waechter.md b2 'SKRIPTE'.
Kevin 28.10. ~04:35: PC aus um ~08:20 -> heute nur noch Kurzes (A/B nur bei Start vor ~06:20), Fix-Version und Rezepte morgen; 'morgen zuerst'
steht in der Uebergabe 28.10. ~04:35. Morgen: Waechter neu anlegen, Hold-Ordner pruefen.
Kevin 28.10. ~04:45 (Woche 88 %): Pruefung zu Ende auf 'Extra hoch', danach NICHTS Neues bis zum Wochen-Reset Fr 30.10. 14:00 (A/B, Fix-Version,
Rezepte erst danach). Maximal mit 8 parallelen Agenten kostete ~0,4 % Woche je Minute -- vor grossen Laeufen get_usage pruefen und Kevin die Zahl nennen.

STAND 28.10. 05:25 (Woche 91 %, PAUSE): Runde 1 fertig -- 0 toedlich, 2 ernst (E1 Spieler-Saat verliert Samen, E2 Werkzeug-Fachkiste als
Zutatenkiste), 29 klein, Kritiker: Farmer vollstaendig, 9 Luecken (_docs/farmer_abschluss/runde1.md, runde1_kritiker.md). Waechter-Cron
e03ad2c3 GELOESCHT. AB FR 30.10. 14:00: Waechter neu, Hold-Schritt + A/B (abschluss_r1_ab.js), Fix-Version (E1-Variante: Warteschlange wie
playernear ohne Rueckfrage; Aufsatz auf Vanilla-complete nur mit Kevins Wort), Gegenpruefung, Runde 2; danach Rezepte serverseitig, dann PAUSE.
IN DIE FIX-VERSION AB FR AUCH: Magazin-Einordnung (RecipeResource -> literature, Waffen-Magazine -> ammo), Kevin: muss vor den Upload
([[vor-upload-pflicht]]).

STAND 30.10. 14:30 (Reset durch, Woche 0 %): Kevin *"du kannst jz weiter arbeiten an den schritten damit wir bald alles testen und danach
hochladen koennen"* -> Hold-Schritt erledigt, b2 A/B laeuft (wf_097a9a7e-b5b, 7 Agenten), Waechter-Cron NEU ee116e6d (stuendlich :17).
Ganze Kette bis zum Upload: `_docs/plan_upload_2026-10-30.md` (10 Schritte). NACH b2: Dateien aus backups/abschluss_hold zurueck.

STAND 30.10. 19:45: v3.14.15 (Farmer-Fix) + Runde 2 BESTANDEN (0/0) + v3.14.16 (Bugs vor Upload) FERTIG und gespiegelt; v3.14.17 (Tod im MP)
laeuft wf_c7968e1a-c75; dann fix18_v3.14.18.js (Tag b44-base-v3.14.18 vorher), dann v3.14.19 Baeume (Skript fehlt noch), Fields-Reiter (Entwurf an
Kevin), Server-Rezepte, Test, Upload. Waechter-Cron ee116e6d. Alle Kevin-Antworten in _docs/plan_upload_2026-10-30.md.

STAND 30.10. 21:50: v3.14.17 FERTIG + gespiegelt, PAUSE. Offene Fragen v3.14.17 in _docs/fix_v3.14.17/v3.14.17_integrator.md
'FRAGEN AN KEVIN' 1-4 (E1 Client-Anzeige bis Relog; Unsterblich-AN-Zweig; Identitaet gelockert; 'kept' baut neu). -- Zuvor: STAND 30.10. 21:20 -- PAUSE NACH v3.14.17 (Kevin: *"wenn der workflow durch ist muessen wir leider pausieren dann merkste dir den stand und
morgen gehts weiter"*). Waechter-Cron ee116e6d GELOESCHT. MORGEN ZUERST: (1) Status-Datei + diesen Eintrag lesen, v3.14.17 pruefen (gespiegelt?);
(2) Waechter neu anlegen (stuendlich :17, gleicher Prompt); (3) get_usage; (4) Tag b44-base-v3.14.18 setzen, _docs/nachtschicht/fix18_v3.14.18.js
starten; (5) v3.14.19 Baeume-Skript schreiben (Stamme bleiben liegen; plus Foerster 'notyours' -> Job mit Spruch beenden, Kevins Antwort offen);
(6) Kevin: Fields-Reiter-Entwurf zeigen + Server-Rezepte-Fragen Q1/Q5 + zwei offene Fragen aus v3.14.16 (Rezept-Magazine in den Posteingang;
notyours beenden); (7) Test, (8) Upload.

**Why:** Kevin will, dass der Farmer ohne sein Zutun fertig wird; Limits brechen Workflows ab.
**How to apply:** Sein Wort ersetzt fuer diese Kette die Rueckfrage bei Woche >= 75 %; 10-Agenten-Grenze je Workflow bleibt. Neue Sitzung = Waechter
weg -> Datei lesen und neu anlegen. Am Ende CronDelete und Kevin sagen. Siehe [[uebergabe-26-10]], [[tests-sammeln-weiterbauen]].
