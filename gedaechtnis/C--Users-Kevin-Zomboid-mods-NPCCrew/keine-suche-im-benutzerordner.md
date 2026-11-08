---
name: keine-suche-im-benutzerordner
description: Nie rekursiv im ganzen Benutzerordner oder Laufwerk suchen (grep -r ab C:\Users\Kevin oder C:\) -- Norton blockiert das als Datenabgriff (Firefox-Profil); Agenten-Prompts muessen die Suchorte festlegen
metadata:
  node_type: memory
  type: feedback
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-02T19:53:37.173Z
---

Suchen (grep/find/rg) nur in festen Orten: Mod-Ordner, Vanilla-media, Bandits, Scratchpad, Zomboid-Logs. NIE `cd /c/Users/Kevin && grep -r ... .` oder ab `C:\`.

**Why:** 02.10.2026 hat ein P2-Bauagent nach einem Entwurfstext im ganzen Benutzerordner gesucht; die Suche lief durchs Firefox-Profil, Norton meldete grep.exe als Datenabgriff und blockierte (Kevin: "norton hat ihn blockiert weil er daten abgreifen wollte in firefox"). Nichts gelesen/verschickt, aber es sieht aus wie Schadsoftware und ist langsam. Gleiche Familie wie die Sandbox-Regel (CLAUDE.md Abschnitt 2) und der Norton-Fund IDP.ALEXA.54 vom 27.08.

**How to apply:** In jeden Agenten-Prompt die erlaubten Suchorte schreiben ("search only in <repo>, vanilla media, Bandits; never recursive over C:/Users/Kevin or a drive root"). Nach dem laufenden Workflow die Regel auch in CLAUDE.md Abschnitt 2 eintragen. Siehe [[testaccount-konsole-sandbox]].
