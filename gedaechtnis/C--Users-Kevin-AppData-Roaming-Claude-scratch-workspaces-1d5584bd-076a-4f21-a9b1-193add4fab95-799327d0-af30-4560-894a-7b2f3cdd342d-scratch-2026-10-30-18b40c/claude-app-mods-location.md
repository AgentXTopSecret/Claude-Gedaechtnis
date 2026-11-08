---
name: claude-app-mods-location
description: Kevins Claude-App-Mods liegen in C:\Users\Kevin\Desktop\Claude Mods und laden in jedem Chat über CLAUDE_CODE_PLUGIN_DIRS
metadata:
  node_type: memory
  type: project
  originSessionId: f4b54466-1f8b-441a-a3f8-0ad50ed7ea4d
  modified: 2026-10-30T15:38:10.507Z
---

Kevins eigene Mods für die Claude-App (Function-Hook-Plugins) liegen je in einem Unterordner von `C:\Users\Kevin\Desktop\Claude Mods\` (Stand 30.10.2026: nur `fortschritt` — Fortschrittsbalken + Limit-Anzeige über dem Eingabefeld, `/limits`-Seitenleiste).

Geladen werden sie in jedem Chat über `~/.claude/settings.json` → `env.CLAUDE_CODE_PLUGIN_DIRS` (ein Pfad pro Mod-Ordner, unter Windows mit `;` getrennt) plus `CLAUDE_CODE_PLUGIN_DIR_WATCH=1`, damit offene Chats Änderungen von selbst nachladen.

**Why:** Kevin will, dass seine Mods in jedem offenen und jedem neuen Chat laufen, und hat diesen Ordner ausdrücklich als Ablageort bestimmt.

**How to apply:** Neue Mods dort anlegen (nicht nur im sitzungseigenen dev-mods-Ordner) und ihren Ordner an `CLAUDE_CODE_PLUGIN_DIRS` anhängen; Änderungen an bestehenden Mods direkt dort machen. Chats, die vor einer Pfadänderung gestartet wurden, brauchen einen App-Neustart.

Erkenntnisse zur Desktop-App: Mod-Panes landen im rechten Seitenbereich; die Fußzeile (SessionMode) schneidet nach ~25 Zeichen ab; die Hinweiszeile (PromptHint) zeichnet die Desktop-App nicht; das Band über dem Eingabefeld (AbovePrompt) weicht, solange ein Frage-Kasten offen ist. Die Kevin-Vorgaben zur Agentenzahl stehen in [[kevin-agent-limit]].
