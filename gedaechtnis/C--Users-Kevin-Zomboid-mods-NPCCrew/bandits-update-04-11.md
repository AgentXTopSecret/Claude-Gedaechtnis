---
name: bandits-update-04-11
description: Bandits-Update 03./04.11. (Waisen-Loeschung Naked*-Koerper, onSave nur bei sichtbarem ESC-Menue) -- geprueft 04.11., zwei ernste Funde, Kevins Entscheidung offen
metadata:
  type: project
---

Bandits hat sich zwischen 03.11. 17:03 und 04.11. 09:55 aktualisiert (6 Dateien; Snapshots `Zomboid/backups/snapshots/bandits/2026-11-03_1703` und `2026-11-04_0955`). Pruefung 04.11. (4 Agenten, nur lesen): Bericht `_docs/bandits_update_2026-11-04/BERICHT.md` (+ sp_cull/srv_cull/save_start.md).

Ergebnis: lebende Crew wird von Bandits' neuer Waisen-Loeschung (client BanditUpdate.lua ~:2161 SP je Bild; server BanditSave.lua cullOrphans EveryTenMinutes, SP+Server) NICHT getroffen -- jeder Neubau schreibt seinen Cluster-Eintrag im selben Schritt. Unsere zwei alten Netze (BanditBrain.Remove-Aufsatz, Guardian ANTI-ZOMBIFY) greifen im SP nicht mehr (Bandits loescht vorher), nur Randfaelle.
Zwei ernste Funde:
1. Nur bei 'Unsterblich' AUS: gezogene Leiche einer toten Companion (Griff-Zombie, Naked-Outfit, kein Eintrag) loescht cullOrphans samt Tasche -- Bandits-Fehler (Client-Fassung hat den Griff-Riegel, Server-Fassung nicht); trifft auch Bandits' eigene Leichen. Vorschlag: dem Bandits-Autor melden (IsReanimatedForGrappleOnly ueberspringen); bei uns kein sauberer Eingriff.
2. Nur SP: Bandits' onSave laeuft nur noch bei sichtbarem ESC-Menue -> Beenden per Fenster-X/Alt+F4 (Alt+F4 ungeprueft) oder Knoepfe nach dem Tod laesst die Crew in der Welt -> beim Laden wie nach Absturz (Zombie auf Crew-Platz, Crew nach 10-20 s), falsche ***-Zeile 'stand noch' je Mitglied. Kein Verlust/Teleport. Fix-Vorschlag: P.BanditSavePre dieselbe Frage stellen (ESC-Menue sichtbar?), sonst keine Kandidaten/***; ob wir die Crew dann selbst aus der Welt nehmen = Kevins Wahl.

**How to apply:** beim Testen ueber das ESC-Menue beenden; Zeile '[BANDITS] removed orphaned bandit body' mit Id melden. Fix fuer Fund 2 und die Bandits-Meldung nur nach Kevins Wort. Verwandt: [[bandits-snapshot]].

**ENTSCHIEDEN 04.11. (Kevin, 'ja dann so lassen'):** Beenden ohne ESC-Menue bleibt Variante C (v3.14.41): wir nehmen die Crew NIE selbst aus der Welt; nur die falschen ***-Zeilen sind weg, Laden wie nach Absturz, Liegende kommt liegend zurueck. Grund: kein neuer Entfernungs-Code, fremde Autosave-Mods anderer Spieler. Nicht neu aufmachen.
