---
name: blueprint-sattelzug-plan
description: "Kevins Sattelzug-Wunsch 10.11.2026 (W900 + Freightliner COE mit groesstem Auflieger in Festung und Ritterburg, gerade durchs Tor) -- Plan gespeichert, Start auf sein Wort"
metadata:
  node_type: memory
  type: project
  originSessionId: 2c69e304-687f-40a4-a85b-6bb959366676
  modified: 2026-11-10T00:24:46.582Z
---

Kevin 10.11.2026 frueh: mit "LKW + Anhaenger" meinte er ECHTE Sattelzuege aus seinen Mods, nicht Vanilla-Gespanne. Wahl: je Basis
(Festung 3b und Ritterburg V2) **einer W900 Semi-Truck** (Workshop 3409472393, Mod-ID rSemiTruck, braucht tsarslib) **und einer 1970
White Freightliner COE** (3409946507, `vehicle 1970whitefreightlinercoe`), beide mit dem W900-Auflieger mit dem **groessten
Kofferraum** (Kandidaten SemiTrailerContainer 3x1000? vs SemiTrailerVan 1500 -- belegen). Auflieger kuppeln ueber
`attachment trailerTruck`. Seine Frage "passt der Wagen durchs Ritterburg-Tor?": heutige kleine Gespanne nur knapp (gerechnet, 1-2 m),
ein ~15-m-Sattelzug nur mit Stellplatz auf der Torachse und gerader Ausfahrt -> so planen, Schleppkurve rechnen.

**Why:** Kevin wollte den Plan ausdruecklich gespeichert, "sodas ihn jeder account weiss" (er wechselt evtl. Konto/Sitzung wegen
Limits); Woche stand bei 72 %, darum noch nicht gestartet.

**How to apply:** Voller Plan `blueprint/SATTELZUG_PLAN.md`, fertiges Workflow-Skript `_arbeit/blueprint/wf_sattelzug.js` (6 Agenten;
zum Start in den Scratchpad kopieren, Workflow mit scriptPath). Nur auf Kevins Startwort, vorher get_usage pruefen und ihm die
Agentenzahl nennen. Mods bleiben optional (Rueckfall Vanilla-Gespanne), nichts aus den Mods kopieren, Kupplung nur mit belegten
Vanilla-Aufrufen (sonst Kevin fragen). Siehe [[blueprint-kevins-zielbild]].
