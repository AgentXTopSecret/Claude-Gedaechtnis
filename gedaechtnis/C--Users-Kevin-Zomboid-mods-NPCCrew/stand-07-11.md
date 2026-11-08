---
name: stand-07-11
description: "Stand 07.11. nachts: v3.14.55 fertig, kein neuer Workflow ohne Kevins Wort; naechster Schritt Send-home-Nachbesserung, dann Auto-Tuer; Baer-Entwuerfe gesichert, Rest auf sein Wort"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-11-08T11:37:07.603Z
---

Kevin 07.11.2026 nachts: kein neuer Workflow, bis er es sagt -- AUFGEHOBEN 07.11. abends ('so weiter gehts'). PC auf sein Wort heruntergefahren. Ausfuehrlich in `_docs/uebergabe_2026-11-07.md`, ZUERST lesen.

**Wenn er 'weiter' sagt:** v3.14.56 kleine Nachbesserung Send home (seine vier Entscheidungen), danach Auto-Tuer als v3.14.57 und der Pluenderer (Nummern schieben um eins). Tests und Upload erst nach dem Pluenderer.

**Baer:** drei Entwuerfe unter `_docs/modelle/baer/entwuerfe/`, Rest (Urteil, Zusammenbau, Kritik, Feinschliff) als neuer kleiner Workflow auf sein Wort, kein Resume, siehe [[workflow-fortsetzen-falle]].

**Turret:** Plan in [[turret-plan]] ist laut Kevin abgedeckt, Bau erst nach dem Pluenderer. Vorschau-Video `_docs/modelle/turret_stufe3/feuer_vorschau.mp4`.

**ABENDS 07.11. (Kevin 'so weiter gehts'):** v3.14.56 laeuft, danach Auto-Tuer v3.14.57 (Tag b72-base-v3.14.57, Plan umnummeriert bis .63). Daneben auf sein Wort, alles parallel erlaubt (Antwort auf meine Frage, rund 23 Agenten zusammen): Baer Entwurf C 'stehend und lebend' in eigener Test-Mod `Zomboid/mods/NCBearTest` (Ablage `_docs/modelle/baer/spiel/`), Turret T1 in `NCTurretTest` nach Copy-Paste-Regeln (Ablage `_docs/turret/`, Uebernahme-Skript `_docs/tools/turret_uebernahme.py`, `--echt` nur auf sein Wort). Kevin: 'irgentwie so das wir das am ende einfach copy paste in npc crew uebernehmen koennen'.

**22:40 07.11.:** v3.14.56 fertig (Gegenpruefer 0/0/5, UI 3683, gespiegelt geparkt, ungespielt). Sieben kleine Fragen an Kevin in `_docs/fix_v3.14.56/v3.14.56_integrator.md` (Satz ueber seinem Kopf ab 30 Kacheln, Langeweile-Handplatz erst wenn B fuer TV/Stuhl/Lesen nichts hat, Info-Box 'works anywhere' veraltet u. a.), nichts blockiert, beim Sammeltest mit ihm durchgehen. v3.14.57 Auto-Tuer laeuft (Tag b72-base-v3.14.57, Ablage `_docs/fix_v3.14.57/`). Zweihaender fertig als Mod `Zomboid/mods/NCZweihaender` (Quelle `_docs/modelle/zweihaender/zweihaender.py`, Umriss 93 % gegen sein Foto, ungespielt). Baer stehend fertig in `NCBearTest`, lebend laeuft (Lauf baer-lebend).

**STOPP 08.11. nachts (Kevin: 'starte ab jz keine neuen workflows mehr wenn die aktuellen durch ist merkst du dir dann fuer morgen was ansteht'):** keine neuen Workflows, bis er es wieder sagt (auch nicht v3.14.59, B1, baer-fell). Laufende Laeufe beenden lassen (v3.14.58, baer-kampf, baer-zombie-angriff, baer-spionage), danach nur Nacharbeit (spiegeln, Lehren, Gedaechtnis) und den Plan fuer morgen in `_docs/uebergabe_2026-11-08.md` 'Morgen' eintragen.

**02:15 08.11.: ALLES DURCH.** v3.14.58 fertig (Commit 206c5be6, geparkt gespiegelt, ungespielt), Baerenkampf fertig und in NCBearTest kopiert (Kevin testet ab 02:08, bugwatch lief). knockDown wirft doch um (Jar: Uebergaenge nach Bedingungszahl sortiert), K1 nicht gebaut. Plan fuer morgen steht in `_docs/uebergabe_2026-11-08.md` Abschnitt 'MORGEN' -- dort weitermachen, STOPP gilt bis Kevins Wort.

**~03:00 Kevins Baerentest + Wuensche (alle in `_docs/modelle/baer/begleiter/ENTSCHEIDUNGEN.md`, Ende):** Umwerfen klappt, Schaden zu hoch (Wert per NCBear_Tune, dann fest). ALLE Kampfclips neu (Arm/Gelenke knicken, ganzer Koerper muss mitarbeiten; Aufrichten bleibt 3 s, nur schoener), Biss im Wechsel auch gegen Stehende, Knockback (erst Beleg klaeren), Schnauben auch ausserhalb des Kampfs, KEIN Scheinangriff, Sitzen nach `kevin_sitzvorlage.png` MORGEN mit Vergleich zum Bild, Kopf bleibt so, Rumpf/Beine weniger eckig. Kevin hat 'morgen mit agenten' gesagt -> Lauf 'baer-anim' ist von ihm gewollt, trotzdem kurz Bescheid geben vor dem Start.

**STOPP AUFGEHOBEN 08.11. 12:30 (Kevin: 'mach bei allem weiter').** Laufen: v3.14.59 (Workflow wf_b7c3ffc8-c1a, Tag b74-base-v3.14.59, Ablage _docs/fix_v3.14.59) und baer-anim (wf_82f926ca-a1e, Bau unter scratchpad/baer_anim/mod, Berichte _docs/modelle/baer/spiel/anim_*.md, Testhilfen nur NCBearBench.lua). Wochenlimit 49 % bei Start (letzte 16 h: ~2,4 Agenten je 1 %). Turret und Zweihaender sind 08.11. ~13:00 nach `C:/Users/Kevin/NPCCrew-Nebenprojekte` umgezogen (eigene Sitzung, NICHT mehr hier bauen). Danach hier: Baer-Umzug nach baer-anim (dann B1 dort), Baer B1 erst NACH baer-anim (Umbenennen beruehrt dieselben Dateien), dann v3.14.60.

**BAER-UMZUG NACH baer-anim (Kevin 08.11.: 'wenn der baer workflow durch ist dann machste den auch berreit zum verschieben mit unseren regeln fuer npc crew und das er alles weiss was noch ansteht'):** sobald wf_82f926ca-a1e fertig ist und Video/Anleitung bei Kevin sind: `_docs/modelle/baer` (spiel/, begleiter/, sound/, entwuerfe/, Skripte) nach `C:/Users/Kevin/NPCCrew-Nebenprojekte/baer/` wie Turret/Zweihaender (Sicherung als Zip vorher, Kopie byte-gleich, Pfade in Skripten/Berichten nachziehen, Arbeitsdaten aus scratchpad baer_* nach `_arbeit/`, Originale weg, Notiz in `_docs/UMGEZOGEN_nebenprojekte.md`). Dazu `baer/STAND.md`: ALLES, was ansteht (B1 Wachsen/Groessen 0.35/0.75/1.35/Art ncbear/Umbenennen nach BanditsNPCBear*/Bench-Dateien/baer_uebernahme.py mit Cheat-Pruefung; Fell/Hubbel/Textur; Sitzen-Ergebnis; B5a Biss der Zombies (Weg 2); Befehle Folgen/Bleiben/Sitz/Frei herumlaufen in Basisflaeche/Komm her, Passiv, Unstuck; Fressen/Trinken skaliert; Leben/Level/Downed/Unsterblich-Sandbox; Jungtier finden statt spawnen; Inventar; Fischen; MP offen; offene Funde aus anim_review_gegen.md und kampf_fix.md; Banditen-Kugel-Nebenfund), mit Verweis auf ENTSCHEIDUNGEN.md. CLAUDE.md der Nebenprojekte Abschnitt 7 'Baer' aktualisieren (nur diesen Absatz). Memory baer-projekt.md bekommt die Umzugsnotiz.
