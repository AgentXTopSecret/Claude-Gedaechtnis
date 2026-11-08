---
name: bekannte-fremdmod-konflikte
description: "Workshop-Meldungen, deren Ursache eine fremde Mod war (vom Melder bestaetigt) -- bei gleicher Meldung zuerst hier nachsehen"
metadata:
  node_type: memory
  type: reference
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-29T08:04:44.099Z
---

- **Crew haengt im 'surrender'-Zustand** (KevlinTallfellow, Workshop 29.10.2026): vom Melder bestaetigt behoben durch Entfernen der Mod
  'Bandits radio' (Bandits-Zusatzmod). Von uns nicht im Code nachgeprueft, Mechanismus ungeprueft. Kevin will dafuer nichts bauen.
- **CREW-/Uebersicht-Knoepfe nur im Debug sichtbar, verschwinden nach Minuten** (Jeion, 29.10.): unser Code hat keine Debug-Sperre (SideBtn,
  RosterPanel gelesen; Vanilla-Leiste unterscheidet sich nur durch den Debug-Knopf; Event-Handler werden je einzeln abgefangen, Jar Event.trigger).
  Vermutlich baut eine fremde Mod die linke Leiste um -- ungeprueft, console.txt angefragt. Kevin 29.10.: KEIN Selbstheiler bauen ('nur fuer
  einen user'); Ausweg F6.

**How to apply:** Bei einer gleichen Meldung die bekannte Ursache nennen, statt neu zu suchen; Kevins Entscheidung 'nichts bauen' gilt, bis
mehrere Spieler dasselbe melden.

**Knox Wildlife / Animals Attack Zombies (Kevin 08.11.):** AAZ-Bullen greifen Crew an, Knox-Kojoten fressen Leichen samt Inhalt -- *'ne wir bauen nichts gegen die mods weil wir die sowieso nicht nutzen also unnoetige arbeit'*. Nichts bauen. Kevin hat beide nur zum Nachlesen abonniert.
