---
name: reusen-pro-zone
description: "Kevins Entscheidungen 26.09.2026 zur Fischerzone: Reusen (E7) an/aus PRO ZONE; Fischkiste (E5) wird per Assign-Knopf aus beliebiger Kiste gewaehlt (wie Lagersystem), ohne Zuweisung = Intake, im Storage-UI mit eigener Farbe."
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-26T17:52:37.038Z
---

Reusen (Fischernetze, Etappe E7 des Fischer-Rework) werden **pro Zone** an/aus geschaltet, nicht pro Fischer (Kevin, 26.09.2026: "dann merk dir das du es per zone machst").

**Why:** Mehrere Fischer teilen sich eine Zone je Basis; mit einem Schalter je Fischer blieben Netze verwaist, wenn ein Fischer umgestellt wird oder stirbt, und ein neues Brain-Feld braeuchte Sync + CUSTOM_FIELDS (Zeitbomben-Familie). Die Zone liegt schon synchronisiert an der Site.

**How to apply:** Beim Bau von E7: ein Schalter im Fishing-Reiter des Beacons, gespeichert an der Zone; KEIN `brain.fishNetsOn`/`brain.fishNets`; jeder Fischer der Zone kontrolliert jedes Netz; AUS = keine neuen legen, liegende einsammeln; Sandbox `NetsPerFisher` heisst dann "Netze je Zone". Vermerk steht auch oben in Abschnitt (H) von `_docs/plan_angler_rework.md`. Siehe [[moegliche-features]].

**Fischkiste (E5), Kevin 26.09.2026:** kein Kistenbau -- im Fishing-Reiter ein Assign-Knopf, man waehlt IRGENDEINE vorhandene Kiste mit dem Auswahlweg des Lagersystems; ohne Zuweisung liefern die Fischer in den Intake, nie mehr in eine zufaellige Kiste im Umkreis (`F.FindDropBox` faellt weg); die Fischkiste erscheint im Storage-UI mit einer eigenen, noch unbenutzten Farbe. Gehoert der Zone. Steht oben in Abschnitt (E) von `_docs/plan_angler_rework.md`.
