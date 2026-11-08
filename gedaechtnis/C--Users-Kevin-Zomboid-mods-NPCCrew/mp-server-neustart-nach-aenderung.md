---
name: mp-server-neustart-nach-aenderung
description: "Nach jeder Mod-Aenderung waehrend eines MP-Tests den Testserver per RCON save+quit neu starten, BEVOR Kevin sich neu verbindet (sonst Kick wegen Lua-Pruefsumme); Rollenwechsel admin->user nur ohne aktive Admin-Kraefte und ohne -debug."
metadata:
  node_type: memory
  type: feedback
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-28T18:06:21.735Z
---

28.09.: Zwei Kicks in 3 Minuten. (1) `setaccesslevel "admin" "user"` per RCON, waehrend Kevin noch eine Admin-Kraft an
hatte (God-Mode/Unsichtbar o. ae.) -> Anti-Cheat "Power" (PlayerPacketReliable: invalid mode). Und ein -debug-Client wird
ohne Admin-Rolle gar nicht erst eingelassen. (2) Ich hatte nach dem Serverstart Mod-Dateien geaendert (v3.11.81/.82), der
Server lief noch mit v3.11.80 -> "Lua/script checksums do not match" (AntiCheatChecksum).

**Why:** Anti-Cheat steht bei Kevin immer auf Kick ([[anticheat-immer-an]]); der Server prueft die Lua-Pruefsummen beim
Verbinden und laufend.

**How to apply:** Aendere ich Mod-Dateien, waehrend der Testserver laeuft: Kevin sagen, dass der Server neu muss, dann
`rcon.py save quit` (Scratchpad) und `NPCCrew-Testserver.bat` neu starten, erst danach verbinden. Vor einem Zurueckstufen
auf 'user': Kevin alle Admin-Kraefte ausschalten lassen und das Spiel OHNE -debug starten. Zurueck: `setaccesslevel "admin" "admin"`.

Praktisch (28.09.): der Fehlerwaechter meldet "[Client] VERSION: vX" bei jedem Spielstart -- steht dort eine andere
Version als beim Server, SOFORT den Server neu starten (bevor Kevin verbindet). Aenderungen an der Platte stoeren eine
laufende Sitzung nicht; die Pruefsummen werden beim Laden gebildet.

**Server stoppen = auch das cmd-Fenster schliessen** (Kevin 21.10.: *"und wenn ich das sage auch das cmd fenster dazu schliessen"*): nach `rcon.py save quit` und 'Shutdown handling finished' in server-console.txt den cmd.exe-Prozess mit NPCCrew-Testserver in der CommandLine beenden (PowerShell Get-CimInstance Win32_Process, nur ProcessId ausgeben -- die .bat enthaelt ein Passwort, CommandLine nie drucken).
