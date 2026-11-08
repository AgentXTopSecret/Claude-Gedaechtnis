---
name: agenten-lauf-16-10
description: "Kevin 15.10.2026: am 16.10. um 15 Uhr mit dem zweiten Account Bauplan-Fabrik + grosser Mod-Check, so viele Agenten, dass das 5-h-Limit knapp erreicht wird"
metadata:
  type: project
---

Kevin 15.10.2026 ~23:20 woertlich: "okay dann machen wir morgen 15 uhr mit dem anderen acccount deine 2 dinge ... bauplan fabrik + grosser
mod-check und da ballern wir soviele agenten fuer raus das wir knapp am 5std limit sind am ende merk dir das und schreib das auch so in die
uebergabe damit der andere account das auch weiss".

Details (Feature-Liste, Linsen, Agentenzahl ~80-90 nach Messung 15.10.: 1 Agent ~1 % des 5-h-Limits, ~0,3 % Woche) in
_docs/uebergabe_2026-10-16_nachmittag.md Abschnitt 3 (aktuell, mit Landkarte des Codes; aelter: _docs/uebergabe_2026-10-16.md Abschnitt 3). Beide Teile aendern keinen Code. Freigabe fuer >10 Agenten liegt fuer DIESEN Lauf vor; vor dem
Start trotzdem die Zahl in einem Satz nennen, get_usage zuerst, nicht ueber ~90 % des 5-h-Fensters.

**Why:** Der zweite Account endet am 17.10. (Samstag); Kevin will sein Limit vorher sinnvoll fuer die Mod nutzen.
**How to apply:** Am 16.10. ab 15 Uhr als Workflow starten (Teil A Bauplan-Fabrik ~30, Teil B Mod-Check ~40-50), Upload-Tests haben Vorrang,
falls Kevin gerade testet -- der Lauf stoert sie nicht. Siehe [[plan-upload-nach-v3-13-53]], [[moegliche-features]].

**GESTARTET 16.10. ~15:25** (Sitzung c3f66696, zweiter Account): Workflow wf_851ba69a-0ae, 80 Agenten (Teil A: 11 Features x Planer/Kritiker/Pruefer + Sammler; Teil B: 17 Regionen-Finder, Top 14 Funde x 2 Widerleger, Berichtsschreiber). Ergebnisse: _docs/bauplaene_2026-10-16/ (je Feature NN_*.md + UEBERSICHT.md) und _docs/modcheck_2026-10-16/ (BERICHT.md, funde.json). Verbrauch vorher: 5h 2 %, Woche 0 % (usage.py --snap gesetzt). Nach dem Lauf: get_usage + --snap, Kevin kurz berichten.

**16.10. ~16:15: 5h-Fenster schon bei 80 % nach 37 von 80 Agenten** (je Agent ~1,5-2 %, nicht 1 %). Kevin: Wochenlimit darf bis 17.10. ganz aufgebraucht werden (Abo laeuft ab, neues Abo = Wochen-Reset); er schreibt "weiter", wenn das 5h-Fenster wieder frei ist (Reset 18:40). DANN: Journal pruefen (subagents/workflows/wf_851ba69a-0ae/journal.jsonl: started vs result), ist der Lauf nicht fertig -> Workflow({scriptPath: ".../workflows/scripts/bauplan-fabrik-und-modcheck-wf_851ba69a-0ae.js", resumeFromRunId: "wf_851ba69a-0ae"}) MIT DENSELBEN args (Features + Regionen stehen im Script-Aufruf; regions.json im Scratchpad lauf1610); vorher evtl. TaskStop. Danach Kevin kurz berichten und als ERSTE Bau-Version den Selbsttest (Bauplan 10_selbsttest_fernsteuerung.md) bauen.
  Die args fuer das Fortsetzen liegen WORTGLEICH in scratchpad (Sitzung c3f66696)/lauf1610/args.json -- genau dieses JSON uebergeben, sonst Cache-Fehlschlag.

**FERTIG 16.10. ~20:10** (Rest als neuer Workflow wf_36a5d4d3-431, 13 Agenten): 11 Bauplaene, 10 BAUREIF (Leichen nicht: LE-1 + Fragen offen), 144 Fragen in _docs/bauplaene_2026-10-16/UEBERSICHT.md (Kevin kann "alles nach Empfehlung" sagen, EINZELN nur LE-1 isZombie und SR-12 Zustands-Setter fuer Teststuecke). Mod-Check _docs/modcheck_2026-10-16/BERICHT.md: 66 Funde, 14 bestaetigt (2 fatal MP-Kopien B01/B02, 8 ernst inkl. Teleporte B06/B07, 4 mittel), 52 ungeprueft; Vorschlag Fix-Versionen A-D. Verbrauch: 5h 61 %, Woche 43 % (nach ~93 Agenten + Wiederholungen). Naechster Schritt: Selbsttest V-A bauen (Bauplan 10, 3 Versionen) nach Kevins Antworten ST-1..13/SR-12.

**16.10. ~20:20 BAU GESTARTET: v3.13.57 Selbsttest Teil 1 (V-A)** -- Workflow wf_f60d5a9c-4e0 (Planer, Bauer A/B parallel, 2 Pruefer, Fixer, Gegenpruefer, ggf. Fixer2, Integrator), Basis-Tag sta-base-v3.13.56, Berichte _docs/fix_v3.13.57/. Schreibprobe C:/Users/Kevin/Zomboid/Lua/NPCCrewSelfTest_schreibprobe.txt ok. Nach dem Lauf: Ergebnis pruefen, workshop_sync (geparkt), Kevin kurz sagen, wie er es einschaltet; bricht der Lauf ab: NICHT resumeFromRunId, sondern Journal lesen (siehe workflow-fortsetzen-falle).

**16.10. ~21:50 v3.13.57 FERTIG** (Selbsttest Teil 1): Laeufer client/BanditsNPCSelfTest.lua, Checks client/BanditsNPCSelfTestCases.lua, _docs/tools/selftest.py (wait-ready, checks, send, run, scan); Pruefer 2 ernst + 10 klein behoben, Gegenpruefer 0/0/3 klein; Integrator gruen, gesichert, gespiegelt (geparkt). Versionszeile jetzt Zeile 1229. Kevin muss: Spiel neu mit NPCCrew-Spiel-Debug.bat, einmal TrueCompanions_SelfTestRemote(true); dann teste ich mit selftest.py (Testpunkte _docs/testliste_upload_2026-10-15.md Abschnitt v3.13.57). UNGESPIELT.

**16.10. ~22:05 v3.13.57 IM SP GETESTET (Selbsttest Teil 1): 6 PASS, 0 FAIL, keine Mod-Fehler** -- Kevin tippte TrueCompanions_SelfTestRemote(true); ich lief selftest.py wait-ready + checks. Einschraenkung: basisnpc konnte nur 1 von 18 messen (17 ohne Ankerfeld, z. B. Arbeiter an Werkbank) -> in Teil 2 Werkbank als Anker. Danach Kevin: *"dann bau jz weiter"* -> **Fix A v3.13.58 GESTARTET** (Workflow wf_ac7ee3dc-860, 10 Agenten, Tag fixa-base-v3.13.57, Berichte _docs/fix_v3.13.58/, Funde B01 B03 B04 B05). Termin c7222bd3 (23:47) startet danach den zweiten Mod-Check (wartet, falls Fix A noch laeuft). Nach Fix A: workshop_sync, Kevin berichten, selftest.py checks laufen lassen (Spiel laeuft im SP mit -debug).

**NACHTSCHICHT 16./17.10. EINGERICHTET (~22:20):** Anleitung _docs/nachtschicht_2026-10-16.md; zweiter Mod-Check abbruchfest ueber _docs/modcheck_2026-10-16/lauf2/lauf2.py (status/next/mark/top) + runner.js (Agent liest auftraege/<label>.md, schreibt ergebnisse/<label>.json); ~47 Agenten (13 Widerleger alt, 10 Finder, bis 24 Widerleger neu, 1 Bericht); Termin 4bdcdcde (alle 30 min, :17/:47, wiederkehrend, nur Sitzung c3f66696) startet nur Fehlendes, ab 75 % 5h nichts. Ausnahme >10 Agenten NUR fuer diesen Lauf (Kevin 16.10.). Ohne Kevins Wort keine weitere Version in der Nacht.

**NACHTBAU (Kevin 16.10. ~22:30):** nach dem Check NUR Fix B (v3.13.59, Skript _docs/nachtschicht/fixb.js) und Selbsttest Teil 2 (v3.13.60, _docs/nachtschicht/vb.js), ohne 25-%-Grenze (Kevin 16.10. ~22:40: bis ans Limit arbeiten, nach Abbruch nur fehlende Stufen fortsetzen; Start bis 90 % 5h); Anleitung _docs/nachtschicht_2026-10-16.md (Abschnitt NACHTBAU, Abbruch-Regeln). Termin jetzt 70a70334 (alle 30 min, Minute 17/47; ersetzt cf16e8db). Kevins Antworten: Stock-Reiter alles nach Empfehlung (SR-2 gefroren ja, SR-3 kaputt ja, SR-1/SR-9 nein, SR-10/11 spaeter); Polsterung fester Wert je Stoffart (mittlerer Schneider-Wert); Zeitraffer: Zombies, Feinde, Fremde stoppen weiter -- alles in UEBERSICHT.md unten. Diese drei NICHT in der Nacht bauen.

**ERGEBNIS NACHTSCHICHT (17.10. ~04:30):** alles durch, Zeitgeber 70a70334 geloescht. v3.13.58 Fix A, zweiter Mod-Check (23 + 24 + 1 Agenten, ~20 % 5h je 23 Agenten -- billiger als geschaetzt, ~0,9 % je Agent), v3.13.59 Fix B (Umfang nach BERICHT 7.4, N02 bewusst raus), v3.13.60 Selbsttest Teil 2. Kein Limit-Abbruch. Fragen in `_docs/fragen_2026-10-17.md`.
