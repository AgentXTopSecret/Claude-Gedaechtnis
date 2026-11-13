---
name: programme-fuer-kevin-losgeloest-starten
description: "Dauerlaeufer fuer Kevin (TempBar, NetSpeedBar) nie einfach per Start-Process aus der Claude-Shell starten -- sie haengen sonst an der Sitzung; wo die Taskleisten-Programme liegen"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 07ffa84a-cac3-4eab-97fc-6a0ec3eb3d8f
  modified: 2026-11-13T20:08:05.959Z
---

Kevins Taskleisten-Programme liegen in `C:\Users\Kevin\Desktop\Programme von Claude\` (`TempBar` = CPU-/GPU-Temperatur, `NetSpeedBar` = Up-/Download), Anleitung und Verlauf in `LIES MICH.txt` dort. Seit 13.11.2026 dort auch `PZStart` (Steam-Startoption vor Project Zomboid: Fenster nach vorn, ein Klick ins Bild, maximieren; Protokoll `PZStart\PZStart.log`, bei Klagen ueber den Spielstart zuerst lesen). Norton CyberCapture haelt jede neu gebaute .exe beim ersten Start ~15 s an. Den Namen "TempBar" wusste Kevin am 13.11.2026 selbst nicht mehr ("die anzeige unten in der taskleiste ... gpu und cpu temperatur").

Ein Programm, das aus einer Claude-Shell mit `Start-Process` gestartet wird, liegt im Job-Objekt der Sitzung (gemessen 13.11.2026: `IsProcessInJob` = ja, Job erlaubt Breakaway). TempBar 1.1 war so gestartet worden und war weg, nachdem jene Sitzung beim Kontowechsel zuging -- kein Absturz-Eintrag in Windows.

**Why:** Kevin 13.11.2026: "beheb das mal die wart heute schon 2x weg -.-". Dass die Sitzung das Programm mitgenommen hat, ist meine Deutung (kein Protokoll beweist es); gemessen ist nur der Job und das Verschwinden ohne Absturz.

**How to apply:** Ein Programm, das fuer Kevin weiterlaufen soll, losgeloest starten: per `CreateProcess` mit `CREATE_BREAKAWAY_FROM_JOB` (getestet: danach in keinem Job). `explorer.exe "<pfad>"` loest NICHT (getestet: Kopie bleibt im Job). TempBar ab Version 1.2 loest sich selbst und startet nach einem Absturz neu (hoechstens 3-mal in 10 Minuten); zum Ersetzen der Datei deshalb sauber beenden (WM_APP_EXIT 0x8001 an das Top-Level-Fenster "TempBar" oder alle `TempBar.exe` zugleich), nicht nur die Anzeige abschiessen. Nach dem Start pruefen: Fenster "TempBar" unter `Shell_TrayWnd` sichtbar. Siehe [[wo-der-stand-steht]].
