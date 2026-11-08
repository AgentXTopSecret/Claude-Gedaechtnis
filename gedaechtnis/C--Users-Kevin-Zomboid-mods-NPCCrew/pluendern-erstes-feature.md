---
name: pluendern-erstes-feature
description: "Kevin 01.11.: Reihenfolge Icon -> Farming-Skill -> Pluendern; mit Folgenden ins Auto (Flaeche + This building) ist das ERSTE grosse Feature nach v3.14.27, neben den Fixes; 19 Fragen beantwortet"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-11-02T11:47:29.820Z
---

Kevin 01.11.2026 (nach Upload v3.14.27): *"Pluendern mit den Folgenden ins Auto, mit Flaechenwahl und This building -- das haette ich gern als
erstes grosses Feature neben den Fixes"*, und: *"das sollte ja eigtl nicht so schwer sein wir haben ja schon aehnliche funktionen"*.

Reihenfolge: v3.14.28 Saatpackungs-Icon (klein, schon zugesagt) -> Pluendern; die Liste [[nach-dem-upload]] laeuft als Fix-Versionen daneben.
Bauplan `_docs/bauplaene_2026-10-16/05_pluendern.md` (16.10., VOR Clean up corpses -- veraltet: vor dem Bau gegen heutigen Code nachziehen und
wiederverwenden: Flaeche zeichnen/erweitern, Beute-Liste-Fenster, Server-Tuer, Auto-Zugriff des Sortierers). Plan sagte 3-4 Versionen / 24-32
Agenten; durch die Wiederverwendung vermutlich weniger (Schaetzung, ungeprueft). 19 Fragen mit Empfehlung in
`_docs/fragen_pluendern_2026-11-01.md`, Antworten dort eintragen. Bau erst nach den Antworten und mit Blick aufs Wochenlimit (01.11.: 91 %,
Reset Fr 06.11. 14:00).

**Why:** Kevins Prioritaet. **How to apply:** naechste grosse Arbeit nach dem Icon; vor dem Bau Fragen klaeren, Plan nachziehen. Siehe
[[moegliche-features]], [[fahrplan-ab-17-10]].

**NACHTRAG 01.11. ~17:00 (Kevin):** zwischen Icon und Pluendern kommt der FARMING-SKILL fuer die Crew: *"ne das soll nach dem icon noch kommen aber mit den saeen bonus fuer leute die jahreszeiten nicht ignorieren"*. Heute uebergibt die Crew ueberall skill 0 (shared/BanditsNPCFarmOps.lua: fertilize skill = 0, Ernte-Nachbau skill 0, Cure je Gabe 10). Vanilla-Wirkung (_docs/farmer/A_vanilla_farming.md 3.7, Tabelle Zeile 151-157): Ernte +skill mit Chance skill/10, Cure je Gabe 10+skill, Duengen Bonus ZombRand(20) < 9+skill, Saeen Startgesundheit +skill und Monats-Risiko/Bonus (11-skill bzw. 9+skill) -- der Monatsteil wirkt nur, wenn das Feld Jahreszeiten NICHT ignoriert (Sandbox-Option der Farmer-Felder). Bauform BESTAETIGT (Kevin 01.11. 'ja der vorschlag von dir ist gut'): Skill 0-10 je NPC wie Animal Care v3.13.48 (shared/BanditsNPCSkills.lua), XP je Feldschritt, Wirkung aus dem Skill der Figur, die den Schritt tut, Skill-Leiter im Skills-Reiter, 7 Sprachen. Woche 01.11. 92 % mit laufendem Icon -> Kevin arbeitet AB 02.11. AUF EINEM ZWEITEN ACCOUNT weiter (der hat 0-100 % frei): dort zuerst der Farming-Skill, dann Pluendern (nach den 19 Antworten). Vorher: Kevin testet das Icon kurz, dann Uebergabe schreiben.

**REIHENFOLGE ENDGUELTIG (Kevin 01.11. ~17:10: 'und danach kommen die fixxes dran die noch anstehn'):** 1 Icon v3.14.28 -> 2 Farming-Skill -> 3 Pluendern -> 4 die anstehenden Fixes: Liste [[nach-dem-upload]] (Foerster-Zonen waehlen/benennen/behalten, Leiche sichtbar ziehen, Pruefung 'was macht der Client noch selbst', Barrikaden-Umweg, Tuer statt Fenster B16) plus Kleinkram aus [[upload-v3-14-27]] ('Save to server' warnt ohne Apply, Axtbruch/Farm-Faell-Regel im MP ungespielt, 'container already has id' und Ruckeln ~3,75 s beobachten).

**19 FRAGEN BEANTWORTET (01.11. ~17:20)** -- Antworten in `_docs/fragen_pluendern_2026-11-01.md` unten. Abweichungen von den Empfehlungen: AUTO-ZONE statt Einzel-Auto (alle Fahrzeuge/Anhaenger in einem gezeichneten Rechteck, Start-Knopf im Loot-Fenster, MP: Autos mit fremdem Insassen auslassen); AUCH VOM BODEN pluendern; Leine 60 statt 40; Radios normal in der Take/Leave-Liste; MP-Abstand 10 Kacheln (Kevin erst 3, nach Hinweis auf Kopie-Risiko zurueck auf 10) MIT Text ueber dem Kopf.

**NEUE REIHENFOLGE (Kevin 01.11. ~17:30: 'ich will nach farming skill noch die attrape habe beim corpse cleanup oder halt die echte zombie leiche bewegen jenachdem was besser und risikoaermer geht'):** 1 Icon v3.14.28 -> 2 Farming-Skill -> 3 LEICHE SICHTBAR ZIEHEN beim Corpse cleanup -> 4 Pluendern -> 5 restliche Fixes. Zu 3: Plan `_docs/plan_leichen_attrappe.md` (Wege A echte Leiche pickUpCorpse, B Schein-Zombie, C nur Zieh-Pose) -- Kevin gibt die Wahl frei: der Pruefauftrag aus dem Plan (Lese-Agenten) entscheidet, welcher Weg BESSER UND RISIKOAERMER ist (rote Linien: keine Kopie/kein Verlust, keine Leiche, die als Zombie aufsteht und angreift, nichts haengt, SP+MP); Kevin bekommt die Empfehlung kurz vor dem Bau. Notiz 21.10.: echtes Ziehen belebt die Leiche kurz als Zombie (Bandits/Crew greifen an, MP ungeprueft).

**STAND 01.11. ~19:00:** v3.14.28 (Bild) und v3.14.29 (Agriculture-Skill, Erntegut-Bild, Favoriten-Fix) gebaut; Kevin: 'die icons sind richtig gut' (v3.14.29 Punkt 2 bestanden, Rest der Testliste _docs/testliste_v3.14.29.md offen). NEU vor 'Leiche ziehen': v3.14.30 = Fields-Reiter Kaesten in Spalten nebeneinander bei breitem Fenster (Auftrag _docs/auftrag_v3.14.30.md). Reihenfolge: v3.14.30 -> Leiche ziehen -> Pluendern -> Fixes.

**STAND 02.11.:** Leiche ziehen ist GESTRICHEN (Kevin nach dem Pruefauftrag: 'dann lassen wir das einfach so'). v3.14.31 Stock-Fenster 50.000 fertig und geparkt gespiegelt, ungespielt (`_docs/testliste_v3.14.31.md`). Kevin 02.11. ~12:45: *'ja bau pluendern'* = STARTWORT fuer das ganze Feature. Ablauf: zuerst Plan-Nachzug gegen den heutigen Code (nur lesen, Ergebnis `_docs/pluendern/PLAN.md`), dann die Bauversionen einzeln. Vor jedem Bau pruefen, dass Kevin nicht spielt ([[kein-bau-waehrend-test]]).

**OFFENE TESTS v3.14.29 (Kevin 01.11. ~19:30 'test 4 und 5 noch merken das teste ich spaeter'):** XP steigt bei Feldarbeit (Punkt 3), Ernte-Menge mit Stufe 10 (Punkt 4), MP als user (Punkt 5), Favorit anheften + neu laden bleibt -- in _docs/testliste_v3.14.29.md unten. Bestanden: Bilder, Favoriten leer, Skill-Zeile sichtbar. v3.14.30 (Felder in Spalten, Farmer-Karten oben rechts, Storage-Ueberlappung) gestartet ~19:35.
