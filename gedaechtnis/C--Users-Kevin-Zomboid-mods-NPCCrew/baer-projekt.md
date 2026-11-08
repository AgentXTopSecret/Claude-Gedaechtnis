---
name: baer-projekt
description: "Kevins Baer-Projekt (Test-Mod NCBearTest): steht, laeuft, Kampf gegen Zombies/feindliche Banditen in Arbeit; eigenes Projekt, bis 10 Agenten parallel erlaubt"
metadata:
  type: project
---

Test-Mod `Zomboid/mods/NCBearTest` (nicht NPC Crew, nicht Workshop). Stand 07.11.2026 abends: stehendes Modell und lebendes Tier "bear" (eigene Clips, animset buck, GLB) im Spiel von Kevin gesehen: *"kein meisterwerk aber auch nicht kacke"*, *"der andere geht voll klar"*; Reh-Variante bearstag aus dem Menue (Art bleibt definiert, sonst wirft sein Spielstand).

**Kampf (Lauf baer-kampf, 07.11. ~23:50 gestartet):** nur Zombies und FEINDLICHE Banditen als Ziel, aufrichten + bruellen, Prankenhieb mit Flaechenschaden und Umwerfen, Toene aus drei gemeinfreien Aufnahmen (Kevin hat jeden Download einzeln freigegeben, `_docs/modelle/baer/sound/roh/QUELLEN.txt`). Ablage `_docs/modelle/baer/spiel/kampf_*.md`.

**Agenten:** Kevin 07.11.: *"du darfst auch bis zu 10 agenten benutzen weil das ja hier quasi ein eigenes projekt ist"* -- fuer Baer (und Turret-Nebenlaeufe) bis 10 je Lauf neben den NPC-Crew-Versionen, ohne erneut zu fragen. Mehr als 10 in einem Lauf weiter nur nach Frage.

**Wegwerf-Spielstand:** ein gespeicherter Baer oder eine Baerenleiche ohne die Mod wirft beim Laden. Verwandt: [[turret-plan]], [[stand-07-11]].

**Groesse (Kevin 08.11.):** Erwachsen = setSizeForced **1,35** (Kevin 08.11. zuletzt: *'mach den finalen baeren doch auf 1,35'*, vorher 1,3 und 1,25). Modell bei 1,0: 1,96 m lang, 1,16 m Schulter. Jungtier 0,35 und Halbstark 0,75 entschieden (Stufen-Tabelle). Muss in `_docs/modelle/baer/begleiter/PLAN.md` (Lauf baer-begleiter-plan laeuft noch, danach nachziehen).

**Fell sieht 'wie Hubbel' aus (Kevin 08.11., Screenshot images/27.webp, Abendlicht):** Umriss hat grosse runde Beulen statt Fellzotteln, Koerpertextur nur 1024. NACH dem Lauf baer-kampf (der baut dieselbe GLB um) einen Lauf 'baer-fell' starten: Umriss mit vielen kleinen spitzen Zotteln statt Beulen, Textur 2048 mit staerkeren Haarstraehnen und Schatten in Falten, pruefen ob animalEffect Alpha-Haarkarten kann. Kevin hat das Startwort mit der Meldung gegeben.

**Stufen ENTSCHIEDEN (Kevin 08.11.: 'ja mach das so'):** Jungtier 0,35 kaempft nicht (versteckt sich hinter dem Besitzer); Halbstark ab 0,75 schwacher Einzelhieb, bruellt, richtet sich nicht auf, wirft nicht um; Erwachsen 1,35 alles (Aufrichten+Bruellen, Flaechenhieb, Umwerfen). Wachstum etwa 7 Spieltage bis Halbstark, weitere 14 bis Erwachsen, Sandbox-Tempo, Fuettern beschleunigt, Hunger bremst. Leben und Futter/Wasser skalieren mit der Stufe (Kevin: 'esssen/trinken muss auch skalieren'); Zahlen als Vorschlag im Chat, Antwort steht aus.

**Spaeter (Kevin 08.11.):** Faehigkeit Fischen: erst ab kampfbereit (Halbstark, dann schlecht), ausgewachsen effektiver; streift in See-/Flussnaehe herum, faengt Fische, legt sie in SEIN Inventar und frisst sie selbst. Eigenes Inventar zum Oeffnen, viel Traglast: Kevin fragte '500kg?'; mein Vorschlag im Chat: Jungtier 10, Halbstark 40, Erwachsen 100 (wie ein grosser Kofferraum), Packtaschen als Ausruestung +50, Sandbox-Faktor fuer mehr. Kevin 08.11.: 'ja das klingt gut' (Traglast 10/40/100, Packtaschen +50, Fischen als spaeterer Schritt nach Kampf, Wachsen, Fuettern).

**ALLE ENTSCHEIDUNGEN DAUERHAFT IN `_docs/modelle/baer/begleiter/ENTSCHEIDUNGEN.md`** (Groesse, Stufen, Leben 40/150/400, Futter 1/2/4, Wasser 1/2/3, Level +50 % Leben, unsterblich-Schalter, Gegner wehren sich, Inventar 10/40/100 +50, Fischen spaeter, Fell-Lauf). Die geht vor PLAN.md.

**Plan-Fragen beantwortet (08.11.):** Wald + Koeder, Downed mit Aufhelfen und allein nach 12 h, pathToLocation am Tier als Ausnahme erlaubt, Art umbenennen in `ncbear` (in B1). Nach baer-kampf: B1 und baer-fell starten (Kevin hat den Plan damit abgesegnet).
