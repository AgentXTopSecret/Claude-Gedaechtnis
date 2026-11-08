---
name: bash-backslash-falle
description: In diesem Bash-Tool werden doppelte Backslashes im Befehl zu einfachen - Python mit Pfaden/Escapes immer als Datei schreiben
metadata:
  node_type: memory
  type: feedback
  originSessionId: 396dbd51-1f1a-4c90-b7eb-a21cbd5601c2
  modified: 2026-10-21T20:08:18.192Z
---

Im Bash-Tool dieser Umgebung (Git Bash unter Windows) kommen `\\` im Befehlstext als `\` an, auch in Heredocs mit `'EOF'`.
- Folge am 21.10.2026: Ein Python-Heredoc ersetzte `\x00` durch `b'\\0'`, geschrieben wurde aber wieder ein NUL-Zeichen.
- `printf '…\\tools…'` schrieb einen TAB statt `\tools` in `mod/notes/11-plan-20-10.md`.
- `'\\u…'` in einem Python-String ergab einen SyntaxError.

**Why:** Kaputte Steuerzeichen in Notizdateien (grep meldet „Binary file matches“). Außerdem sah die Reparatur erfolgreich aus, obwohl sie nichts geändert hatte.
**How to apply:**
- Python-Code, der Backslashes enthält (Windows-Pfade, Escapes wie `\0`, `\t`, `\u`), mit dem Write-Tool als `.py` in den Scratchpad schreiben und dann mit `python <datei>` starten.
- Bei Python-Heredocs nur raw-Strings mit EINEM Backslash nutzen.
- Kein `printf` mit Pfaden.
- Danach mit dem Prüfskript auf Steuerzeichen testen (Muster: `[\x00-\x08\x0b\x0c\x0e-\x1f]` und Tab vor Kleinbuchstaben).

Siehe [[swyf-claude-mod-status]].
