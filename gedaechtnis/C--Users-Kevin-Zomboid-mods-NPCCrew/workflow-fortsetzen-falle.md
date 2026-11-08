---
name: workflow-fortsetzen-falle
description: "Fortsetzen (resumeFromRunId) eines parallelen Workflows nach Limit-Abbruch startet fast alles neu -- stattdessen Ergebnisse aus journal.jsonl ziehen und nur die fehlenden Agenten in einem neuen kleinen Workflow laufen lassen"
metadata:
  type: feedback
---

Am 16.10. (Lauf wf_851ba69a-0ae, 80 Agenten) brachen 13 Agenten am 5-h-Limit ab. Das Fortsetzen mit resumeFromRunId
uebernahm nur die Planer aus dem Zwischenspeicher; Kritiker und Finder liefen NEU (der Cache gilt nur fuer den
unveraenderten VORDERSTEN Teil der agent()-Aufrufe, und bei parallelen Aufrufen ist die Reihenfolge nicht fest).
Kevin bemerkte es: *"bis auf die bauplaene hat gefuehlt alles neu gestartet"*. Kosten: rund 34 % eines 5-h-Fensters.

**Why:** Agenten-Laeufe sind teuer (je Agent 1,5-2 % des 5-h-Fensters bei grossen Dateien); doppelte Arbeit
kostet Kevin Limit und liefert abweichende Ergebnisse.

**How to apply:** Nach einem Abbruch NICHT resumeFromRunId bei parallelen Workflows. Stattdessen:
journal.jsonl lesen (je Label das erste 'result'), die fertigen Ergebnisse in eine Datei schreiben
(Vorlage: scratchpad c3f66696/lauf1610/extract.py) und einen NEUEN kleinen Workflow nur fuer die fehlenden
Agenten starten, der die Datei liest. Grosse Laeufe vorher kleiner schneiden (Agentenzahl x ~2 % gegen das
freie 5-h-Fenster rechnen). Siehe [[agenten-lauf-16-10]].
