---
name: swyf-claude-mod-status
description: "Stand der privaten Claude-Mod (ClaudeCaller) für \"Scam With Your Friends\"; nächste Schritte in Documents\\SWYF-ClaudeMod\\UEBERGABE.md"
metadata:
  node_type: memory
  type: project
  originSessionId: aab284ab-c9db-4bc4-bdf3-26f404963264
  modified: 2026-11-02T13:07:56.736Z
---

Private Mod „ClaudeCaller“ für „Scam With Your Friends“: Claude führt die Anrufe (Modus Auto = maximal Geld, Auto + Sprechen = mit Stimme), liest Anruferdaten und füllt Apps aus.

**Bei neuer Sitzung zuerst lesen:** `C:\Users\Kevin\Documents\SWYF-ClaudeMod\UEBERGABE.md` – ganz oben der Block „START NACH DEM RESET (Fr 23.10. 15:00)“ mit der Reihenfolge. Danach `CLAUDE.md`, `mod/notes/14-0.8.3.md` (0.8.3-Liste) und `mod/notes/11-plan-20-10.md` (alle Entscheidungen/Ideen mit Wortlaut).

**Stand 02.11. ~14:10:** Installiert 0.9.9 (Tag v0.9.9, ClaudeCaller.dll 0814ba58…; A18 Prestige-Prüfer + als Host halten, beides ab Werk AUS, Einfg → Host → Namen). Liste notes/20 leer, nichts läuft, kein Cron, weitere Arbeit nur auf Kevins Wort. 0.9.6–0.9.9 im Spiel noch ungetestet. Nachtest: 12 Gesamtläufe, 11× 11484/0, 1× 11479/1 einmalig und nicht nachstellbar; Hauptverdacht `TestBudgetEchtFs` nicht bewiesen (UEBERGABE oberster Block). Testläufe immer vollständig in eine Datei schreiben, nie mit `Select-Object -Last` kürzen, sonst fehlt die Zeile `FEHLER: <Name>`. Last-Prozesse nur niedrig priorisiert starten: auf dem PC laufen parallel andere Projekte von Kevin. Limit 02.11.: Woche 9 %, Reset So 08.11. 22:59 (nicht mehr Freitag 14:00).

**Stand 01.11. 02:54:** Installiert 0.9.8 (Tag v0.9.8; A15 Noclip nur Host, A16 Teleport/Hinlaufen immer automatisch, A17 Claude im Clip lauter). PAUSE auf Kevins Wunsch; A18 Prestige-Prüfer + als Host halten (0.9.9) nur auf sein Wort. Weiter-Stand: WAECHTER-ANLEITUNG.md oberster Block.

**Stand 30.10. ~18:50:** Installiert 0.9.7 (A13 mehrere Jumpscare-Videos, enthält A12 Clip-Garantie; Tag v0.9.7). Aufgabenliste notes/20 LEER, Wächter-Cron gelöscht. Neue Aufgaben nur auf Kevins Wunsch. Davor 17:07: 0.9.6 eingespielt (Kevin: Pause vor Claudes Zeile 2 s, mod/notes/34). A13 (mehrere Jumpscare-Videos) läuft als wf_56050adc-696 → 0.9.7. A14 (Prestige) VERWORFEN. Wächter-Cron 9adf3005.

**Stand 28.10. ~15:35:** 0.9.3 eingespielt und vom User im Spiel abgenommen (nur Geist-Stimme verständlich, Tag v0.9.3, Commit 7e3f879, Sicherung backup/2026-10-28_vor-0.9.3 = 0.9.2). Lauf wf_3a76d026-e93 baut A9 → 0.9.4, danach A11 → 0.9.5 (Grusel-Art je Zweck ohne Hauptschalter, Jumpscare lauter wirken lassen (User „Ja, beides“: Clip davor leiser + Schreck härter, Schalter [Jumpscare] Maximal), Regler Leistungsprüfung härter, Regel Nicht am PC). Wächter-Cron 00c7244f. Details WAECHTER-STATUS.md + notes/20.

**Stand 27.10. ~19:45 – MORGEN WEITER (User: „wenn der workflow durch ist erstmal merken und pausieren morgen gehts dann weiter“):**
- **27.10. ~23:15 WEITER + WÄCHTER AN** (User: „okay weiter machen und mach den wächter an bei abbruch 5std limit etc automatisch weiter arbeiten“): Cron `d61adb5a` (stündlich :23, nur in Sitzung 89a9b429, max. 7 Tage). Lauf `wf_252d4479-d84` = Fix 3 fertig (auf UNFERTIG 9f6168e) → Teleport-Bau → 2 Gegenprüfer → Fix → Einspielen 0.9.0. Danach A8 und A9 ohne Pause. Die „Pause“-Hinweise unten sind damit überholt.
- **28.10. ~07:15 PAUSE:** A8 fertig, 0.9.1 eingespielt + Tag v0.9.1 + gepusht (selbst nachgeprüft: SHA Spiel = releases/0.9.1). Keine Crons mehr. Nächstes Mal: A9 (Bild drucken + Namensschild + Kleinkram, notes/20), vorher Wochenlimit prüfen (Reset Fr 30.10. 14:00). Grusel-Stimme einschalten: Einfg → „Modus + Sprechen“ → „Grusel-Stimme (Halloween)“.
- **28.10. ~04:40 PLANÄNDERUNG** (User: „du machst nur noch den aktuellen workflow fertig und danach schon pause und merkste dir dann alles fürs nächste mal“ – Limit geht zu schnell weg): Wächter-Cron `d61adb5a` gelöscht, A9 auf PAUSE. Nur noch A8 fertig machen; danach nichts starten, bis der User sich meldet. Nächstes Mal: Stand in notes/20 (A8/A9) und WAECHTER-STATUS.md lesen; ist A8 nicht fertig → fehlende Schritte nachholen (notes/31-a8-zwischenstand.md, falls angelegt); dann A9 (Bild drucken + Namensschild + Kleinkram), Woche vorher prüfen (Reset Fr 30.10. 14:00).
- **28.10. ~04:30:** A8 läuft als `wf_ce0d41df-b94` (→ 0.9.1: F-B ganze Lobby + Grusel-Stimme). User macht den PC ca. **08:20** aus → bis dahin nichts Neues; ab 07:40 Abschalt-Vorbereitung laut WAECHTER-ANLEITUNG.md (Block „ABSCHALTUNG“): ggf. stoppen, „UNFERTIG 0.9.1“ committen, Agenten-Ergebnisse als notes/31 sichern. Danach (neue Sitzung) zuerst A8 fertig machen, dann A9.
- **28.10. ~03:40:** 0.9.0 eingespielt + Tag v0.9.0 + gepusht (selbst nachgeprüft). A8 startet, sobald das 5-h-Fenster < 50 %; A9 = Bild drucken + **Namensschild schön beschriften** (User 28.10. ~03:55) + Kleinkram (Wackel-Tests, Wächter-Test-Kodierung), Details notes/20 unter A9. Woche 82 % → A9 vermutlich erst nach dem Reset Fr 30.10. 14:00.
- **Antworten 27.10. ~23:35** („du sollst jz alles feritg bauen am stück“), Details in notes/20 (Zeile nach „Wächter-Cron wieder AN“): Grusel Dämon + im Anruf volle Stärke; Druck-Bild beides; Teleport Host sofort, Client RENNEN; Beleidigungen ganze Lobby; Kurs-Ticker bleibt (Geld geht vor); Telefon-Platzsparen passt. Nachtrag „rennen/ganze Lobby“ im A8-Lauf prüfen bzw. erledigen.
- **27.10. ~20:15 GESTOPPT** (User: „speicher das ab ich muss jz ins bett“): `wf_c76879cb-1e4` = Fix 3 (Befunde notes/29d) + A7 Teleport → 0.9.0. Fertig: Teleport-Bauplan notes/30 (71b4f76/167acae). Fix 3 halb = Commit 9f6168e „UNFERTIG 0.9.0“ (nicht gebaut/getestet). Morgen zuerst: Fix 3 fertig → Teleport-Bau → 2 Gegenprüfer → Fix → Einspielen 0.9.0 (Weitermachen-Text in notes/20 bei A7; resumeFromRunId nur in Sitzung 89a9b429). Installiert bleibt 0.8.9. Nichts starten, bis der User weitermacht.
- Morgen (28.10.) zuerst **A8 „Grusel-Stimme“** für Halloween (Sa 31.10.; User 27.10. ~20:00: „vor dem Bild-Drucken (wegen Halloween am Samstag)“): Plan in notes/11 direkt nach der JW-Paint-Idee – Effekt auf die eigene Mod-Stimme (Dämon/Geist/Gruft), im Anruf nur leicht (Spracherkennung des KI-Anrufers), auch als Client.
- Danach **A9 „Bild drucken (JW Paint)“** (User-Wahl 27.10. ~19:40): Plan in notes/11 Zeile ~388 + notes/17 „JW-Paint-Poster“: Bild aus Ordner (z. B. `ClaudeCaller\bilder\`) in die JW-Paint-Malfläche laden, der User druckt selbst über den normalen Druck-Knopf; nie `CmdPrint` mit fremden Bytes. Nicht gewählt: Sprengmeister, Song global, mehr als 8 Spieler.
- notes/20 „Aufgaben ab 27.10.“ bekommt A8/A9 erst nach dem 0.9.0-Lauf (Agenten schreiben dort gerade).
- Wächter-Cron bleibt AUS (User: „Nein, aus lassen“). Teleport als Client nur echtes Auto-Laufen (feste Grenze, dem User angekündigt).
- Offene Fragen an den User: F3/F4 (notes/20), F-A bis F-E (notes/29). Seit 0.8.7 nichts im Spiel getestet.

**JOB NACH DEM RESET (User 23.10. ~04:25: „merk dir, was morgen dein Job ist“), in frischer Sitzung, Versionen nacheinander:**
0. `decompiled/` ist vom 19.10. und veraltet (Spiel-Update 21.10.) → betroffene Klassen frisch decompilieren, alten Stand behalten.
1. **Sprachbereich-Bug = WICHTIGSTER PUNKT** (User: „sehr wichtig, dass wir gezeigt werden“): nach Beitritt in laufende Lobbys gehen Sprech-Zeilen ohne Sprachbereich raus → nicht als Meeting-Room-Clip wählbar. Fix im Log nachweisen.
2. Blink-Fix Aufnahme-Schutz. 3. Jumpscare-Anzeiger + STAT `typ: "meeting"` (gezeigt ja/nein). 4. Kleinpunkte (u. a. Zeitlimit/ohne Zeitlimit trennen). 5. User testet → 0.8.3 einfrieren (Tag v0.8.3). 6. Dann 0.8.4 Mithören (inkl. Sprachwahl DE/EN).
- Workflow nur nach OK des Users; kleine Teile mit Sonnet.

**Stand 26.10. ~21:00:** Neue Sitzung/anderer Account: zuerst den Block „WEITERMACHEN (anderer Account / neue Sitzung)“ ganz oben in UEBERGABE.md lesen. Installiert 0.8.6 (Tag v0.8.6), kein Workflow läuft. Nächste Schritte: Zusatz aus notes/11 (26.10. ~19:00) als 0.8.7, dann Bann-Liste, dann Teleport. Azure pausiert. Nachtwache-Cron aus. Max. 10 Agenten pro Workflow.

**Stand 26.10. ~17:55 (Nachtwache):** 0.8.5 (Mithören, Reichweite, Sprachwahl, Host-Force, Video-Wartezeit) eingespielt + Tag v0.8.5. Läuft: 0.8.6 (Host-Rache zuerst, Limit-Anzeige + Konto-Wechsel per CLAUDE_CONFIG_DIR, Chat-Bot, Troll) als wf_d816ff2b-46e; danach Teleport.

**Stand 26.10. ~13:10 (Nachtwache):** 0.8.4 eingefroren (Tag v0.8.4) und eingespielt: neue Scams, Lautsprecher-Tonweg, deutsche Durchsagen, Halloween-Modus (nur Host), Anpassung an Spiel 0.1.92 (Build 26208975 akzeptiert, Anti-Cheat GRÜN, L2 geprüft). Läuft: 0.8.5 Mithören + Host-Werkzeuge (wf_b03cae58-3df), danach 0.8.6 Chat-Bot/Troll. Status: mod/notes/20-nachtwache.md.

**Stand 26.10. ~06:20 (Nachtwache):** 0.8.4 Teil 1 neue Scams eingespielt (IP Geolocation, Money Mule, Frenzy). Halloween-Bau läuft danach.

**Stand 26.10. ~01:20 (Nachtwache):** 0.8.3 eingefroren (Tag v0.8.3) und eingespielt; Spiel 0.1.91 (Build 26194293) nach Prüfung akzeptiert (GELB harmlos: Frenzy-Modus-Kaufsperre). Nächster Bau: neue Scams, dann Halloween. Status: mod/notes/20-nachtwache.md.

**DAUERAUFTRAG 25.10. ~23:20 (User: „das baust du alles direkt danach … und spielst immer direkt die neue Version ein“):** Nach dem Feinschliff alle Versionen nacheinander ohne Rückfrage bauen, selbst prüfen und sofort einspielen. Nur bei geschlossenem Spiel, sonst warten. Immer mit Sicherung, Doku und push. Reihenfolge: Feinschliff → v0.8.3 → neue Scams → Halloween bis 31.10. → 0.8.4 Mithören → 0.8.5 Chat-Bot/Troll. Azure erst mit Schlüssel. Details oben in UEBERGABE.md.

**Stand 25.10.:** `0.8.3-zwischenstand-update` eingespielt (Anpassung an Spiel 0.1.84 + Jumpscare 2; vorher waren Meeting Room und Headset-Ton nach dem Spiel-Update abgeschaltet). Offen: Flacker-Fix (uncommittet im Arbeitsordner, nicht verwerfen), Kleinpunkte, Prüfung → neue Scams → Halloween bis 31.10. → 0.8.4.

**Stand 23.10. abends:** 0.8.3 Rest-Endstand EINGESPIELT (rest-final, Commit 28ca094, Tests 5072/0), gepusht, PAUSE bis morgen. Morgen: User-Test nach LIESMICH „IM SPIEL TESTEN“ → Logs → 0.8.3 einfrieren → dann Lautsprecher-Tonweg + deutsche Durchsagen + Halloween-Modus bis Sa 31.10. → dann 0.8.4 Mithören. Details oben in UEBERGABE.md.

**Stand 23.10. ~04:25:** Installiert 0.8.3-Zwischenstand „jumpscare“ (A+A2+B+Aufnahme-Schutz+Jumpscare). config: `Lustiger = true`, `KurzeSaetze = true` (A/B beendet: kurz +50 $/min). Alles gepusht. Force-Modus nur als Host (als Client abgelehnt, User hat es mehrfach gefordert – dabei bleiben, freundlich). Namensschild per Registry wirkungslos (Profil liegt seit 21.10. in MetaSave/Steam Cloud) und rückgängig gemacht.

**Limit:** Account Max x5, Woche 99 % am 23.10. nachts, **Reset Fr 23.10. 15:00**. Auto-Spielen verbraucht mit (claude -p). Gemessen: Workflow mit 6 Opus-Agenten ≈ 4 % Woche / 30 % 5-h-Fenster; Sonnet-Einzelagent ≈ 1 %.
**Technik:** .NET SDK 10 ist installiert (Visual Studio 2026) → `global.json` pinnt SDK 8.0.426, dotnet aus dem Projektordner starten. Git-Repo `main`, privates GitHub-Repo, nach jedem Schritt pushen, Spielcode nie hochladen.

Kernbefunde: Unity 6.3 Mono, kein Anti-Cheat, Doorstop 4.5 statt BepInEx. Die Mod läuft auch als Client.

**23.10. ~13:05:** Der User hat die Comedy-Erhöhung als Client erneut verlangt (Begründung „nur private Lobbys mit Freunden, wir manipulieren den Clip ja schon“), verärgert. Claude hat kurz einen Client-Modus mit Freundes-Sperre erwogen. Der Sicherheitscheck von Claude Code hat das als „Third-Party Attack“ blockiert → verworfen. Es bleibt bei: Force nur als Host. Nicht umgehen, nicht neu verhandeln, freundlich bleiben. Befund und Bauplan: `mod/notes/15-comedy-auswahl.md`. Kernpunkt: Bei ≤ 5 Spielern kommt jeder sicher dran, der eine aufgenommene Zeile mit comedy > 0,75 hat → Sprachbereich-Bug zuerst. `decompiled-26097532` = aktueller Build.

**Why:** Der User macht nach dem Limit-Reset in einer neuen Sitzung weiter; der nächste Schritt soll nahtlos anschließen.
**How to apply:**
- UEBERGABE.md lesen und dort weitermachen.
- Am Spielordner nichts ohne OK ändern; vor Änderungen prüfen, ob das Spiel läuft (Prozess per Pfad suchen, nicht per Name).
- Workflows mit höchstens 10 Agenten.
- Nie den echten Namen nennen, nur den Spielnamen „Agent X Top Secret“.
- Zum User siehe [[user-profile-kevin]], zu den Dateien [[swyf-analysis-files]].
