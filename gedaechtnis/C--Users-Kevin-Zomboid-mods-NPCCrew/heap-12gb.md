---
name: heap-12gb
description: "Kevins Debug-Start (NPCCrew-Spiel-Debug.bat) laeuft seit 10.10. mit -Xmx12288m statt 8192m; 8 GB reichten nicht (nur 48 MB frei, Ruckler, OOM beim Neuladen)."
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-10T17:14:33.361Z
---

Am 10.10.2026 auf Kevins Ja ("ja mach") in `C:\Users\Kevin\Zomboid\NPCCrew-Spiel-Debug.bat` nur in der java-Zeile `-Xmx8192m` -> `-Xmx12288m` gesetzt (Kommentarzeile 11 nennt weiter 8192, historisch). Sicherung: `Zomboid\backups\NPCCrew-Spiel-Debug.bat.vor-12gb-2026-10-10`.

**Why:** Kevin mass bei 8 GB nur 48 MB frei (20 Portraets), mit 4 Portraets 114 MB -- die Portraets kosten nur ~4 MB je Stueck; der Bedarf seines Spiels liegt bei ~9 GB (Messung 07.10.: mit 12 GB ~3 GB frei). Zweimal OutOfMemory beim Neuladen im selben Prozess (B1 durchgefallen), Untersuchung laeuft (scratchpad oom/REPORT.md).

**How to apply:** Bei Ruckeln/OOM zuerst pruefen, mit welchem -Xmx gestartet wurde (Bat oder ProjectZomboid64.json nach PZ-Update). Siehe [[plan-freitag-09-10]], [[test-nur-noetigste]].

Auch Steam-Start: `ProjectZomboid64.json` am 10.10. auf Kevins Ja ('ja mach steam auf 12') von -Xmx8192m auf -Xmx12288m (Sicherung `Zomboid/backups/ProjectZomboid64.json.vor-12gb-2026-10-10`). Ein PZ-Update setzt die JSON zurueck -- nach Updates pruefen.
