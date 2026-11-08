---
name: maximal-verbrauch-messen
description: "Kevin 27.10.: Wochen-% der ersten Farmer-Version komplett auf Aufwand 'Maximal' messen und ihm sagen (Vergleich ~9 % je Version auf 'Extra hoch') -- NICHT VERGESSEN"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-28T03:38:29.142Z
---

Kevin 27.10.2026 ~18:00: *"ja mach das aber nicht vergessen"* -- auf meine Zusage, den Verbrauch der naechsten Version auf Aufwand
'Maximal' zu messen und ihm zu sagen.

Hintergrund (in den Protokollen gezaehlt, 27.10.): ALLES in diesem Projekt lief bis 27.10. ~17:40 auf Aufwand 'Extra hoch' (xhigh) --
Hauptsitzungen seit 22.08., Agenten seit 27.08. (einzelne Agenten zeitweise 'Hoch'). Die alte App-Stufe 'Ultracode' war intern
'Extra hoch' + Workflows; die App trennt jetzt Aufwand (bis 'Maximal', laut App "3,5x oder mehr Nutzung") und den Schalter Ultracode.
Kevin hat am 27.10. ~17:40 auf 'Maximal' gestellt; Workflow-Agenten uebernehmen die Einstellung SOFORT (der Fixer von Farm-6 wechselte
mitten im Lauf; Beleg: "effort":"max" in agent-*.jsonl).

**Vergleichswerte 'Extra hoch' (27.10., Kevin: "mit farm 5 vergleichen oder vorher"; Woche inkl. Hauptsitzung):**
v3.14.9 Fix 8 Agenten ~6 % (15-9), 3,93 Mio. Agenten-Tokens; Farm-5a 8 Agenten ~7 % (22-15), 4,64 Mio.; Farm-5b 10 Agenten ~9 %
(31-22), 5,78 Mio. -> je Agent ~0,8-0,9 % Woche bzw. ~0,5-0,6 Mio. Tokens. Farm-4b nicht messbar (Kontowechsel 27.10. nachts).
**Farm-6 v3.14.12** = gemischt (fast alles xhigh, ab Fixer max) -- zaehlt NICHT als Messung.
**Farm-6 (gemischt) kostete Woche 34 -> 47 % (~13 %, inkl. viel Hauptsitzungs-Arbeit auf max) -- keine Messung.**
**FARM-7 GESTARTET 27.10. 18:42 (wf_4ced33bb-1d6), START-WERT Woche 47 %, 5h 52 % (usage.py --snap 47 52).**
**Farm-7 melden:** Woche-% UND Tokens je Agent (aus der Workflow-Benachrichtigung 'subagent_tokens' / agent_count), gegen diese Tabelle.
**MESSUNG:** die erste Version KOMPLETT auf 'Maximal' (geplant Farm-7 v3.14.13): get_usage (Woche %, 5 h %) direkt VOR dem Start und
direkt NACH dem Integrator notieren (auch `python _docs/tools/usage.py --snap W F RESET`), Differenz Kevin in 1-2 Zeilen sagen, mit
dem Vergleich ~9 %. Pruefen, dass die Agenten wirklich auf max liefen (grep '"effort":"max"' in den agent-*.jsonl des Workflows).

**KORREKTUR 27.10. ~19:00 (Kevin):** *"den wochenstand der bringt nix weil ich ja grade an 3 mods arbeite mit dem account also du must schon
echt gucken was der workflow verbraucht"* -> Wochen-% ist KEIN Mass (andere Sitzungen auf demselben Konto). Gemessen wird nur noch aus den
Agenten-Protokollen des Workflows: `python _docs/tools/wfcost.py <run-id> ...` (zaehlt je message.id einmal: Ausgabe inkl. Denken,
Cache-Schreiben, Cache-Lesen; je Agent und je Rolle; Aufwand-Eintraege je Stufe). Gewichtung fuers Limit unbekannt -> Arten getrennt zeigen.
Vergleichswerte 'Extra hoch' (je Agent): v3.14.9 Ausgabe 62k (Denken 35k), Cache-Schr. 0,48 Mio, Cache-Lesen 23 Mio; Farm-5a 82k (42k),
0,57 Mio, 38 Mio; Farm-5b 92k (55k), 0,56 Mio, 34 Mio. Rollen auf xhigh: Planer Denken 49k/66k/99k, Integrator 13k/13k/7k,
Gegenpruefer 61k/31k/61k. Farm-6 (gemischt): Integrator auf max 41k Denken, Gegenpruefer auf max 111k -- nur Hinweis (andere Aufgabe).
Farm-7 = wf_4ced33bb-1d6: nach Abschluss wfcost.py laufen lassen und je Agent/Rolle gegen diese Werte melden.
ACHTUNG: Farm-7 wurde am 27.10. ~20:15 beim Fixer abgebrochen (PC aus) -> die Restschritte laufen morgen in einem NEUEN Workflow;
Messung = wfcost.py ueber BEIDE Run-Ids (wf_4ced33bb-1d6 + der neue), Abbruch-Agent (Fixer ohne Ergebnis) gesondert nennen.

**GEMESSEN UND GEMELDET 28.10. ~00:25 (Farm-7 = wf_4ced33bb-1d6 + wf_cd7438bb-30a, 10 Agenten inkl. abgebrochenem Fixer, alle Eintraege 'max'):**
je Agent Ausgabe 149k (Denken 89k), Cache-Schreiben 0,73 Mio, Cache-Lesen 68 Mio, 121 Antworten. Gegen Farm-5b (xhigh): 1,6x / 1,6x / 1,3x /
2,0x; gegen Farm-5a: 1,8x / 2,1x / 1,3x / 1,8x; nach API-Preisen gewichtet (Ausgabe 5, Cache-Schr. 1,25, Cache-Lesen 0,1) ~1,7-1,9x je Agent.
Groesste Spruenge: Integrator Denken 48k gegen 7-13k, Bauer A Ausgabe 215k gegen 73-105k. Vorbehalt: Farm-7 groesser (13 Dateien, 42 Texte) und
Fixer-Neustart. Baseline-Run-Ids: v3.14.9 wf_ea0da046-cd1, Farm-5a wf_435113f3-e06, Farm-5b wf_83df038c-25f. KOSTEN-TEIL ERLEDIGT; offen nur noch
der A/B-Test unten.

**Kevin 28.10. ~04:40:** *"maximal frisst wohl echt viel limit deswegen brauchen wir spaeter echte ergebnisse ob sich das lohnt"* -> A/B
verstaerkt: je Linse ZWEI Laeufe auf 'xhigh' (Streuung derselben Stufe) gegen den Maximal-Lauf, blinder Richter ueber drei Listen (7 Agenten).
Melden: echte Funde je Stufe nach Schwere, Fehlalarme, Funde nur einer Stufe, Kosten je echtem Fund; Maximal lohnt nur, wenn der Abstand
M gegen X deutlich groesser ist als X gegen X2. Grenze dazusagen: drei Linsen auf einem Code-Stand sind ein Hinweis, kein Beweis.

**QUALITAETS-TEST (Kevin 27.10.: "ja mach den test"):** A/B in der Abschlusspruefung Runde 1 -- Linsen Ware, Teleport, SP/MP je auf
'max' und 'xhigh' (opts.effort ausdruecklich), blinder Richter, Ergebnis `_docs/farmer_abschluss/ab_test.md`; Ablauf
`_docs/farmer_waechter.md` Abschnitt Abschlusspruefung b2). Kevin danach beides melden: Kosten (Farm-7) und Funde (A/B).

**A/B ERLEDIGT 30.10. 15:20 (wf_097a9a7e-b5b, Bericht _docs/farmer_abschluss/ab_test.md):** echte (alle kleinen) Funde M 5 / X 4 / X2 3,
Abstand M-X = Streuung X-X2, kein ernster Fund in keinem Arm; M ~1,75x Kosten je Agent. Empfehlung an Kevin: Extra hoch als Regel, max nur
fuer hartnaeckige Bugs. Kevins Entscheidung offen.

**Why:** Kevin entscheidet danach, ob 'Maximal' den Mehrverbrauch wert ist. **How to apply:** bei jedem Versionsabschluss hier
nachsehen, bis die Zahl gemeldet ist; danach diesen Eintrag als ERLEDIGT markieren. Siehe [[farmer-waechter]], [[verbrauch-messen]].
