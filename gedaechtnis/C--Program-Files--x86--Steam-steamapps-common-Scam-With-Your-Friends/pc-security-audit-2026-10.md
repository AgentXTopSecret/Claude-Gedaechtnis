---
name: pc-security-audit-2026-10
description: "PC-Sicherheitsprüfung 20.10.2026 – Bericht-Ort, Kernbefunde, Norton trennt parallele Prüf-Agenten"
metadata:
  node_type: memory
  type: project
  originSessionId: f4e93b91-b722-4c04-b0c2-979d91207b6c
  modified: 2026-10-20T16:44:34.505Z
---

Read-only PC-Audit am 2026-10-20. Bericht: C:\Users\Kevin\AppData\Roaming\Claude\side-session-notes\local_1802fef6-7d1e-4393-afe4-c35cf9585895\pc-sicherheitspruefung-2026-10-20.md

Kernbefunde: Defender per IFEO (mpcmdrun.exe→systray.exe) + Richtlinie (Registry.pol 21.01.2025) gesperrt, Spur von dControl.exe; Cheat-Lader (Umbrella, Melonity, KeyAuth/The Isle, runtimedll→System32\zlib1.dll); kein laufender Schadprozess sichtbar. Stand Abend 20.10.: auf Kevins Wunsch System32-Cheat-DLLs, KeyAuth, Cheat-RARs entfernt; Kevin hat Defender-Sperren selbst entfernt (Claude ändert keine Sicherheitseinstellungen, gibt nur Anleitung). Offen: Offline-Scan, Passwörter/2FA, C:\MelonitySpoofer.exe, gefälschte WLAN-MAC, Firefox „YouTube Unblocker Plus“ (Tracking), AutoHotkey-Root-Zertifikat, Epic-Updater-Rechte; Cheat-Ordner Umbrella/Melonity bleiben bewusst.

**Why:** Norton hat beim parallelen Workflow-Audit die API-Verbindungen der Agenten getrennt (ECONNRESET, ~16:42–16:48), 6 von 7 Gegenprüfungen fielen aus. Norton-Meldung: „Bedrohung abgebrochen – (URL:Blacklist) gefunden: Sicheres Web“, blockierte URL https://api.anthropic.com/v1/messages?beta=true (Fehlalarm; genauer Auslöser unklar, Hauptsitzung lief danach normal weiter).
**How to apply:** Bei weiteren System-Prüfungen auf diesem PC wenige, leichte, nacheinander laufende Befehle statt vieler paralleler Agenten; Norton nicht umgehen oder Ausnahmen setzen. Norton Power Eraser ist seit 30.04.2026 eingestellt → Norton Bootable Recovery Tool / ESET SysRescue empfehlen. Siehe [[user-profile-kevin]].
