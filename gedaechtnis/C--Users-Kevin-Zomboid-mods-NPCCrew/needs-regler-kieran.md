---
name: needs-regler-kieran
description: "Workshop-Meldung KIERAN 22.10.: Beduerfnis-Regler (Sandbox NeedsRateMult) auf 0 wirkt nicht -- statisch geprueft: Regler stoppt den Anstieg, aber hohe Werte bleiben stehen und SP-Aenderung im laufenden Spiel wirkt erst nach Neuladen; Fix-Vorschlag fuer v3.13.96"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-22T21:47:08.202Z
---

Meldung KIERAN (Workshop, 22.10.2026): "Needs editor doesnt work at all. changed it to 0.00 = thirst still goes up ... they just constantly use
hunger/thirst dialog ... just make an option so they dont need to eat and drink." Kevin: "ohne agenten checken ... und wenn das stimmt merk dir das".

Ergebnis (selbst geprueft, statisch, nicht gespielt): "wirkt gar nicht" NICHT bestaetigt -- NeedsRateMult multipliziert in
`shared/BanditsNPCNeeds.lua` (Needs.Update) alle fuenf Anstiege, bei 0 steigt nichts. ABER zwei echte Luecken erklaeren den Bericht:
1. SP: Sandbox im LAUFENDEN Spiel geaendert (Debug-Menue) -> Vanilla ruft nur getSandboxOptions():set(), kein toLua (Jar); SandboxVars bleibt
   alt bis Speichern+Neuladen. Im MP wirkt das Admin-Fenster sofort (GameServer.receiveSandboxOptions -> toLua + an alle Clients).
2. Beide Modi: 0 stoppt nur den Anstieg, schon hohe Werte bleiben -> sie wollen weiter essen/trinken und sagen es immer wieder.
Dazu: Sandbox-Tooltip nennt Durst nicht (7 Sprachen).

**How to apply:** BESCHLOSSENER FIX (Kevin 22.10.: 'ja merk dir das als fix aber jz fixxen wir noch nichts') -> v3.13.96 Punkt d, erst ab Reset 25.10.: bei Regler 0 alle Beduerfnisse auf 0 halten, Regler
zusaetzlich ueber getSandboxOptions():getOptionByName lesen (Vanilla-belegt), Tooltip nennt Durst. Einzelheiten am Ende von
`_docs/uebergabe_2026-10-21.md`. Siehe [[uebergabe-19-10]].
