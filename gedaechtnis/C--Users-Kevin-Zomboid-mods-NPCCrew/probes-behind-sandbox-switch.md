---
name: probes-behind-sandbox-switch
description: "Jede neue Sonde muss über die Sandbox-Einstellung abschaltbar sein, nie über ein nacktes print"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f31a6c60-393f-4384-a887-2468f35b6ab7
  modified: 2026-09-30T22:05:33.379Z
---

Jede Sonde und jede Diagnosezeile, die ich baue, muss über die Sandbox-Einstellung
**"Crew logging"** (`BanditsNPC.Diagnostics`) laufen — also `BanditsNPC.Log(...)`
statt `print(...)`. Kevins Ansage am 04.09.2026: *"merk dir auch das wenn du eine
sonde baust das die nur über die sandbox einstellung laufen soll"*.

**Why:** die Mod soll veröffentlicht werden. Vor dem Umbau in v3.7.98 liefen **362 von
605** `print`-Aufrufen automatisch bei **jedem Spieler**, davon nur ~72 gedrosselt —
jede Zeile ist ein Dateischreibvorgang, und auf einem vollen Server summiert sich das.
Die Diagnose ist für die Entwicklung da, nicht für den Spieler.

**How to apply:**
* Neue Diagnose → `BanditsNPC.Log(...)`. Sie hängt an der Stufe (1 aus / 2 Konsolenzeilen /
  3 zusätzlich das Trace-Protokoll), Vorgabe **aus**.
* **Ausnahme, bewusst:** echte Fehler → `BanditsNPC.Err(...)`, die laufen auf **jeder**
  Stufe. Ein stiller Fehlschlag ist in diesem Projekt teurer als jede Logzeile.
* `print(...)` bleibt nur in `TrueCompanions_*`-Konsolenbefehlen — die laufen ohnehin
  erst auf Zuruf.
* **VERSCHAERFT 01.10. (Tierpfleger-Sonden, Kevin: *"mess sonden aber wie gehabt nur wenn
  crew logging aktiv ist nicht bei aus"*):** auch NEUE Konsolenbefehl-Sonden messen und
  drucken nur bei Crew logging >= 2 (`BanditsNPC.DIAG`), Ausgabe über `BanditsNPC.Log`.
  Bei aus: nichts messen, nichts an den Server schicken, genau EINE Hinweiszeile, wie man
  es einschaltet (ein getippter Befehl darf nie stumm sein). Server-Echo ebenfalls nur über Log.
* **Und gleich danach, allgemein (01.10.):** *"sonden sollen immer nur laufen wenn crew logging aktiv
  ist sonst spammen sie die consolen zu unnoetig andere leute koennen damit eh nicht viel anfangen
  nur wir"* -- das kippt die v3.9.64-Begruendung ("Err, damit ein Fremdbericht es zeigt") fuer
  Mess-/Info-Zeilen. `Err` bleibt NUR fuer echte Fehler (Ausnahme, Verlust/Kopie-Alarm, kaputter
  Zustand, fehlgeschlagener Engine-Aufruf). Pruefung vom 01.10.: alle `print` lagen schon hinter
  Log oder in Konsolenbefehlen; 177 `Err`-Stellen wurden einzeln eingeordnet.
* Zur Laufzeit umschaltbar mit `TrueCompanions_Diag(1..3)`, ohne Neustart; das schlägt
  die Sandbox-Option.

Siehe auch [[both-modes-always]].
