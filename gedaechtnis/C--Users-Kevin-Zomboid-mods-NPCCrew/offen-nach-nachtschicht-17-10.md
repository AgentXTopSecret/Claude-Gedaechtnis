---
name: offen-nach-nachtschicht-17-10
description: "Alles, was nach der Nacht- und Tagschicht 16./17.10.2026 noch zu tun ist -- Reihenfolge (Fix F, dann TESTEN mit Selbsttest, dann Zeitraffer), Kevins offene Entscheidungen, offene Fix-Versionen E/G/H/C2, Mod-Check Teil 2, Features"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-17T08:38:59.694Z
---

Kevin 17.10.2026 ~10:30: *"okay gut dann stopp mal den endlos loop und merk dir was noch gemacht werden muss alles"*. Der Zeitgeber ist geloescht,
das Herunterfahren gestrichen (Kevin war wieder da). Gebaut seit 16.10. abends: v3.13.57 (Selbsttest 1) bis v3.13.62 (Fix C), dazu laeuft v3.13.63.
Alles UNGESPIELT, nichts hochgeladen seit v3.13.56 (Workshop-Ordner gespiegelt, geparkt). Status-Protokoll: `_docs/tagschicht_status.txt`,
`_docs/modcheck_2026-10-16/lauf2/nacht_status.txt`.

STAND 18.10. 15:51: v3.13.69 (Crew-Grenze) und v3.13.70 (Zahlenfeld) gebaut, alles getestet und HOCHGELADEN (v3.13.70 oeffentlich). Teil A des Fahrplans erledigt; weiter mit Teil B (_docs/fahrplan_2026-10-17.md).

STAND 18.10. ~01:55: v3.13.66 (Fix E), v3.13.67 (Zeitraffer), v3.13.68 (Release->Spieler im MP, Zeitraffer Feinde 30) FERTIG und gespiegelt, alle UNGESPIELT. Kevin: PAUSE, morgen weiter mit v3.13.69 Max Crew (Skript _docs/nachtschicht/mc.js, NICHT ohne Kevin starten), dann Test aller neuen Versionen (SP+MP, Selbsttest inkl. zeitraffer), Patchnotes ab v3.13.56, Upload. Ueberblick: _docs/fahrplan_2026-10-17.md.

STAND 17.10. ~18:10: v3.13.65 gebaut; TEST SP+MP BESTANDEN (Restliste _docs/testliste_rest_2026-10-17.md mit Ergebnissen). Kevin beantwortete Frage 1 (N01: vorher ablegen) und 2 (Altbestand: ja raeumen) -> Fix E = v3.13.66 laeuft (wf_8d4d36a0-053, Skript _docs/nachtschicht/fixe.js); parallel Zeitraffer-BAUPLAN (wf_c42f33ba-9aa, nur lesen, Ergebnis _docs/bauplaene_2026-10-17/zeitraffer.md + Fragen ZR-x). Danach: Zeitraffer-Version nach Kevins Antworten, kurzer Test, Patchnotes ab v3.13.56, UPLOAD (Kevins Plan).

**Reihenfolge (Kevins Wort 17.10. ~10:25: "ja dann danach erstmal dinge testen"):**
STAND 17.10. 14:11: v3.13.63 und v3.13.64 (Fix F) FERTIG und gespiegelt; v3.13.65 (vkadaver) laeuft als wf_d1dcf998-d51. Kevin 14:15: "wenn das fertig ist testen wir das und dann bauen wir noch den fast forward fix ein" -- Reihenfolge bestaetigt.
1. **Laeuft:** Selbsttest Teil 3 = v3.13.63 (Workflow wf_8489adac-afc, Tag stc-base-v3.13.62, Berichte `_docs/fix_v3.13.63/`). Nach der Meldung:
   Versionszeile pruefen, `workshop_sync.py`, Status-Zeile.
2. **Fix F = v3.13.64** (Skript `_docs/nachtschicht/fixf.js` fertig; vorher `git tag fixf-base-v3.13.63`, `mkdir -p _docs/fix_v3.13.64` +
   scratchpad/v3.13.64; Inhalt BERICHT 8.1/8.2: M01 Besorgungs-Marke im Cluster, M02 Dach-Anker, M05 Relax-Sitzen 3D, M07 Tierzonen ab Platz 13,
   M09 Quest nach Tod, M20 Taste, Sonde [TC-WANDER]). Ohne Zeitgeber: nach der V-C-Meldung von Hand starten.
2b. **Selbsttest-Zusatz 'alter Kadaver' = v3.13.65** (Kevin 17.10. ~10:40 'ja mach das'): Skript `_docs/nachtschicht/vkadaver.js` fertig; vorher
   `git tag std-base-v3.13.64`, `mkdir -p _docs/fix_v3.13.65` + scratchpad/v3.13.65. Todeszeit des Testkadavers zurueckstellen (setDeathTime belegt,
   ButcheringUtil.lua:594); 'verrottet/Skelett' nur, wenn der Planer den Engine-Weg im Jar belegt; Welt-Test kadaver_alt (Brennstelle, auch MP).
3. **TESTEN** (vor allem anderen): Kevin startet `NPCCrew-Spiel-Debug.bat`, laedt SP-Spielstand; ich starte bugwatch ([[bugwatch-bei-jedem-test]]) und
   `python -B _docs/tools/selftest.py wait-ready` / `checks` / Welt-Tests (sortieren, kadaver, lagerzaehlung; Basis braucht misc-Kiste, Tierzone mit
   Huehnern, Regel zerlegen, Messer im Lager). Danach MP (Testaccount Rolle user, AntiCheat 2). Kevins Teil: `_docs/testliste_upload_2026-10-15.md`
   Abschnitte v3.13.58 bis v3.13.64 (Waffenbruch mit Zielfernrohr, Task-Manager-Absturz, Logout-Parken auf dem Server usw.).
4. **Zeitraffer trotz Crew** -- noch KEIN Bauplan; Kevins Regel (16.10.): echte Zombies, feindliche Banditen und fremde Ueberlebende stoppen weiter, nur
   die eigene Crew nicht, Umkreis etwas groesser als Vanilla (Vanilla: IsoPlayer.updateLOS 935-1011, 4 bzw. 7 Kacheln, gleiche Ebene). Erst Bauplan, dann Version.

**Kevins offene Entscheidungen** -- alle in `_docs/fragen_2026-10-17.md`: 1 N01 Release mit voller Tasche (der EINZIGE toedliche offene Fund, Fix E),
2 N02/N06 Altbestand raeumen, 4 F1 (U24), 5 F2 (Foersterin Platz), 6 B11 Feuer im MP, 7 U01 Basis-Sperre, 8 U38-U42 Engine-Aufrufe, 9 XP im
Kadaver-Test, 11-13 N13/N15 fremde Basis, D14 U08 Teil 2, D15 U18, 14 M03 Schlafen, 15 M04, 16 M06 fremde Safehouses, 17 M08 Auto-Ausladezone,
18 M10 Wanderer toeten Companions, 19 M12; C1-C3 nur zur Kenntnis.

**Offene Fix-Versionen (BERICHT `_docs/modcheck_2026-10-16/BERICHT.md` 7.4/7.5/8.1/8.2):** E (N01/N02/N06/N17/N03/U04/U05/U26/N07/U03 -- braucht
Fragen 1+2), G (M04/M06/M03/M10-Fix -- braucht Kevin; M14/M16 gehen ohne ihn), H (nach C: M11/M24/M18/M19 ohne Kevin, M08 braucht ihn), C2 (uebrige
Kistengriffe ueber die Server-Tuer, U32), Restliste (U09, U11, U12, U19, U21, U23, U25, U27, U28, U33-U36, U43, U44, U46, U47, U49-U51, N08, N09,
N20, N21, N23-N38, M12, M13, M17, M21, M22 zuerst, M23, M25). Fix-Skript-Vorlage: `_docs/nachtschicht/fixd.js` (vier Bauer, 10 Agenten).

**Dritter Mod-Check Teil 2** (nach dem Wochen-Reset): R07 Produktion, R14 Wasser/Abkochen/Fischen, Persistence-Rest, Interact-Rest, Programs
6745-8133/8432-9100, StoragePanel-Rest, SelfTest-Dateien. Aufgaben-Form wie `_docs/modcheck_2026-10-16/lauf4/auftraege/f4_*.md`, Runner
`.../lauf2/runner.js` mit args {labels, base}.

**Features danach** ([[plan-upload-nach-v3-13-53]], [[moegliche-features]]): Stock-Reiter je Zustand (Bauplan 00, Kevins Antworten in UEBERSICHT),
Polsterung (fester Wert je Stoffart), Leichen (LE-1 offen), Wassertraeger mehrere Tonnen, Farmer, Crew-Rucksack, Pluendern, Streik, Max-Crew-Sandbox,
PvP-Sandbox; SlaughterSoon-Aufraeumen; Selbsttest V-D (Test 'auftrag'); MP-Brennstelle und Abendruf testen. Vor dem naechsten Upload: Patchnotes
ab v3.13.56 (Kurzfassung unter ~4000 Zeichen, Klartext, neutral formuliert).

**Why:** Kevin will nach der langen Bauphase zuerst testen; der Chat-Verlauf geht nicht mit, nur Dateien.
**How to apply:** Bei Sitzungsbeginn diese Liste und `_docs/fragen_2026-10-17.md` lesen; Punkt 1-3 in dieser Reihenfolge, Neues nur nach Kevins Wort.
