---
name: bandits-unabhaengig-spaeter
description: "Kevin 05.11.2026 -- fuer GANZ SPAETER (wenn er mit der Mod zufrieden ist): interne Fassung unabhaengig von Bandits; Fakten, Grenzen (Server rechnet keine Zombies), offizielle NPCs B43 ohne Termin, Empfehlung Zwischenschicht TC.Engine"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7fd0ad-7592-45c0-90c1-5c2a73830a30
  modified: 2026-11-05T20:33:31.035Z
---

Kevin 05.11.2026 abends (nach dem Bandits-Update-Aerger): *"koennten wir wenn ich mit der mod komplett zufrieden bin probieren das wir von der bandits mod unabhaengig werden? irgentwie so eine interne version wo nur wir arbeiten und die leute bekommen weiterhin die abhaengige bis die andere klappt?"* -- danach: *"okay merk dir das mal fuer ganz spaeter aber das soll gespeichert sein das du das immer weisst"*.

**Wann:** erst wenn Kevin die Mod fertig findet (nach Pluendern, Hausmeister/Autos usw.). Dann zuerst eine Lese-Analyse mit echtem Plan und Zeitschaetzung anbieten, nicht drauflos bauen.

**Fakten (gemessen 05.11.2026):**
- Unser Code ruft Bandits an 3361 Stellen auf (132 verschiedene Funktionen); Bandits selbst ~24.500 Zeilen Lua.
- Bandits liefert: Gehirn-Speicher + MP-Abgleich (Cluster), Aufgaben-Dispatcher + Gehen (ZAMove), Kampf, Spawnen, Aussehen, Waffen in der Hand, ~200 AnimSet-XML-Knoten. **Die Animations-CLIPS sind Vanillas** (Kevin hat mich korrigiert) -- Bandits bringt nur die kleinen XML-Knoten, die einem Zombie die Spieler-Animation zuordnen; solche schreiben wir schon selbst (5 Stueck), dieser Teil waere leicht.
- Bandits-Code darf nicht kopiert werden (fremder Code, nur mit Erlaubnis des Autors) -> Nachbau.
- **Server-seitige NPCs gehen mit Zombie-Grundlage NICHT** (Kevins Folgefrage): ein dedizierter Server rechnet keine Zombies (MovingObjectUpdateScheduler nimmt kein IsoZombie in die Eimer, OnZombieUpdate feuert dort nie; CLAUDE.md Abschnitt 5, 13.09., v3.9.42). Das liegt am Spiel, nicht an Bandits. Server macht schon jetzt Zeit/Ablieferung/Lager/Speichern.
- Tiere (IsoAnimal) rechnet der Server -- NPCs darauf waeren ein Forschungsprojekt mit ungewissem Ausgang (eigenes Skelett/Modell/Animationen, vermutlich Java-Grenze). Meine Empfehlung an Kevin: kein Tier-Projekt.
- Offizielle NPCs: Build 43 soll die erste Stufe menschlicher NPCs bringen (Grundgeruest), KEIN Termin, haengt an der B42-Stabilitaet (B42 stabil seit 29.07.2026); realistisch 1-3 Jahre (Stand Websuche 05.11.2026).

**Weg (Kevins Idee + meine Empfehlung):** interne Fassung = eigener git-Zweig + eigene mod id, nie hochgeladen; Spieler behalten die abhaengige Fassung. Schritt 1: Zwischenschicht `TC.Engine.*` (unser Code spricht Bandits nur noch an einer Stelle an) -- lohnt sich auch ohne Ende: ein Bandits-Update trifft dann nur eine Stelle, und kommen offizielle NPCs, kann unsere Arbeitslogik darauf umziehen. Dann Stueck fuer Stueck ersetzen. Grobe Schaetzung: Monate, viele Wochenlimits.

Verwandt: [[moegliche-features]], [[bandits-update-04-11]].
