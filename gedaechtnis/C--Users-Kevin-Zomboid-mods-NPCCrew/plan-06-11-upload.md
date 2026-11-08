---
name: plan-06-11-upload
description: "Kevin 06.11.2026 ~01:10 -- Ablauf fuer den zweiten Account: v3.14.51 (nur Auto-Frist 30 s + Foerster Pflanzplatz/Boden reservieren), kurzer Test SP+MP, Patchnotes+Guide, Upload; Rest NACH dem Upload"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-11-06T15:55:02.019Z
---

Kevin 06.11.2026 ~01:10 auf meine Empfehlung: *"ja dann merk dir das und mach das es der andere account auch weiss"*.

**Ablauf (zweiter Account, ab 06.11.):** Uebergabe `_docs/uebergabe_2026-11-06.md` ZUERST lesen.
1. v3.14.51 bauen, NUR: (a) Auto-Frist `H.CAR_AIM_MS` 30 s fest -> Sortierer drehen vor fernem Auto um + falsches 'No room left.'; (b) Foerster reservieren Pflanzplatz und Bodenarbeit (FJ.claims).
2. Kevin testet kurz SP (3 Punkte) + MP-Test von v3.14.50 (5 Punkte).
3. Patchnotes + Guide, Live-Beschreibung vergleichen.
4. stage -> Kevin laedt hoch -> park.

**Why:** oeffentlich ist v3.14.38; das Bandits-Update 05.11. laesst bei allen Spielern die Crew an Kisten haengen, v3.14.49/.50 beheben das -- Upload nicht lange aufschieben.

**How to apply:** alle anderen Funde aus dem SP-Test (Sortierer-Anlaeufe, Farmer-Objektkachel, turnalerted, Nachschub-Speicher, F2, F4) erst NACH dem Upload; sie stehen in `_docs/auftrag_v3.14.51.md`. Verwandt: [[naechste-sitzung-03-11]], [[sicherheitsregeln]].

**NACHTRAG 06.11. ~01:20 (Kevin):** *"wir haben aber noch 6% uebrig ... morgen erstmal hier weiter machen am besten multiplayer tests aber nur die anders laufen als im sp"* -> ZUERST auf DIESEM Account (6 %) der MP-Test mit 4 Punkten (Geldboersen, Sortierer-Rueckweg, Koch/Folgende bei Hoheitswechsel, Unstuck+Relog-Kick-Probe; Liste in der Uebergabe), KEIN Bau hier. Danach zweiter Account: v3.14.51 bauen, 3 SP-Punkte, Patchnotes/Guide, Upload.

**MP-Test 06.11. mittags:** Boersen, Sortierer-Rueckweg, Koch bestanden. Folgende im MP haengt IN pathfind (F4, Waechter-Teleport nach 25 s) -- Kevin: in die Uebergabe; Einordnung nach dem Upload, ausser er zieht es vor. Einzelheiten `_docs/uebergabe_2026-11-06.md` unten.

**MP-TEST FERTIG 06.11.:** alle 4 bestanden (Kick-Probe ok), nur F4 offen. Weiter auf dem zweiten Account mit v3.14.51.

**STAND 06.11. ~17:00:** v3.14.51 gebaut (Reviews 0 toedlich, 0 ernst), SP gespielt: Punkt 1 und 2 bestanden, 0 Fehler in der Sitzung; Punkt 3 ohne Ergebnis (nur Spruch-Risiko), MP-Teil von .51 ungespielt. Patchnotes `_docs/patchnotes_v3.14.51_short.txt` (3991 Zeichen) und Guide-Entwurf `_docs/guide/guide_entwurf_v3.14.51.txt` (11 Abschnitte; Kopfzeilen `=== SECTION` und `--- GEAENDERT` nicht eintragen) gegen den Code geprueft. **UPLOAD-ORDNER IST GESTAGED** (`Zomboid/Workshop/NPCCrew`, Kandidat-Tag upload-kandidat-v3.14.51): NACH Kevins Upload SOFORT `python _docs/tools/workshop_sync.py park`, Tag upload-v3.14.51, Steam-Groesse pruefen, Guide nach seinem Ja eintragen (Ids in [[steam-guide]]), guide_en.txt nachziehen, CLAUDE.md Abschnitt 8 und stand_historie fortschreiben. Offen bei Kevin: Guide-Warnung F14 (gezogene Crew-Leiche, Bandits-Fehler; Empfehlung weglassen). Danach Liste [[nach-dem-upload]]; Ruckler zuerst.

**ERLEDIGT 06.11. ~17:30:** hochgeladen 16:57, geparkt, Tag upload-v3.14.51, Guide live. Weiter: [[nach-dem-upload]], auf Kevins Wort.
