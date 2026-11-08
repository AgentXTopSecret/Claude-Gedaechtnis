---
name: logout-parken-offen
description: "Logout-Parken der Companions: am 11.09.2026 als v3.9.9 GEBAUT und bestaetigt (Server-Poll + Hauptmenue-Haken, Mitfahrt-Mechanik); Testliste in offene_arbeit.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: f31a6c60-393f-4384-a887-2468f35b6ab7
  modified: 2026-09-10T22:59:56.534Z
---

**Verabredet in der Nacht auf den 11.09.2026, vertagt auf den 11.09. ab 15 Uhr** (Kevins
Limit war aufgebraucht): das **Logout-Parken** der Companions wird dann gebaut.

**Die Entscheidung steht schon** (Kevin, 10.09.): Companions sollen beim Ausloggen ihres
Besitzers **mitgehen** — Schnappschuss schreiben, Körper aus der Welt nehmen, beim
nächsten Login zurückholen.

**Und die Reihenfolge ist der ganze Punkt** — Kevin hat den Verlustfall selbst
vorhergesehen, bevor eine Zeile gebaut war:

1. **Zuerst die schwebende Ware zurückgeben.** Während einer Ablieferung liegt sie weder
   in der Tasche noch in der Kiste, sondern in `G.pending[uid].held`
   (`client/BanditsNPCGoodsMove.lua`) und wartet auf die Serverantwort. Ein Schnappschuss
   speichert die **Tasche** — diese Ware wäre also nicht dabei, und mit dem Körper wäre
   sie weg. `G.SweepHeld` gibt sie zurück, aber erst nach einer Minute; das muss erzwungen
   werden.
2. **Dann** `P.Record` — jetzt ist die Ware im Manifest.
3. **Erst dann** den Körper parken.

**NICHT bauen: "die Arbeit vorher instant abschließen".** Eine Charge fertigzustellen,
ohne dass die Zutaten verbraucht wurden, erzeugt Ware aus dem Nichts — die Richtung, die
dieses Projekt am 31.08. 252 Gegenstände gekostet hat.

**Der häufigste Fall ist ungefährlich, im Spiel gemessen:** eine laufende Produktion hängt
an der **Weltzeit**, nicht am Programm ("die arbeitszeit läuft trotzdem weiter"). Kritisch
ist nur das schmale Fenster einer Ablieferung, die gerade beim Server liegt.

**Die teure Hälfte ist der Rückweg:** der automatische Sweep holt eine Entfernte
ausdrücklich **nicht** zurück (`farAway`). Ohne eigenen Auslöser beim Login müsste jede
Companion von Hand hergeholt werden — schlimmer als das Problem.

Siehe auch [[both-modes-always]] und [[probes-behind-sandbox-switch]].

**Stand 11.09. mittags, vor dem Bau:** v3.9.3–v3.9.8 sind gebaut und gespielt — Folgen läuft
auf dem Rechner mit Hoheit, fremde Companions holen ihr Programm aus dem Cluster. Fürs Parken
heißt das: beim Ausloggen des Besitzers kann ein **fremder** Rechner gerade eine Folgende
führen; der Parkvorgang muss vom Besitzer-Client ausgehen (Schnappschuss, Serverbitte) und
darf nicht voraussetzen, dass er selbst die Hoheit hat. Server läuft nicht; alles ist
heruntergefahren. Kevins Wochenlimit war bei 1 %, Reset 15 Uhr.

**GEBAUT als v3.9.9 und IM SPIEL BESTAETIGT (11.09.): Hauptmenue-Weg 9 geparkt, 9 zurueck. Alt+F4-Weg (nur Poll) noch ungespielt.** Serverseitig (kein Logout-Ereignis
existiert): Poll alle 5 s ueber `getOnlinePlayers()`, parken wie die Mitfahrt (`riding`),
Rueckweg ueber `onPlayerUpdate` neben den Spieler. Client-Haken am Hauptmenue-Ausgang fuer
frische Schnappschuesse. **Schritt 1 der alten Reihenfolge (schwebende Ware zurueckholen)
war falsch** -- die Server-Bitte geht im selben Schritt wie das Halten raus, der Server
schliesst ab; Zurueckholen haette verdoppelt. Testliste: `_docs/offene_arbeit.md` oben.

**Einschraenkung, aus der Gegenpruefung (v3.9.10):** der Server-Poll sieht nur Koerper, die
ein ANDERER Spieler geladen haelt -- die Zellen des gegangenen Spielers entlaedt der Server im
selben Bild wie die Verbindung faellt. Allein auf dem Server bleibt bei Alt+F4 alles in der
Chunk-Datei (kein Verlust). Der Hauptmenue-Haken ist der belastbare Weg. Und: v3.9.9 macht
jeden harten Abbruch zu einem Roster-Neubau -- jede lokale Gehirnaenderung braucht seither
sofort ein `Persistence.Record` (v3.9.10 fuer Waffenuebergabe und Zutatennahme nachgezogen).
