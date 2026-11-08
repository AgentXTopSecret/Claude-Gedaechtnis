# Claude-Gedaechtnis (privat)

Sicherung von Claudes Notizen (Gedaechtnis) fuer alle Projekte auf Kevins PC und der Anleitungen, damit nach einem Plattenschaden
nichts verloren ist (Kevin 08.11.2026). Wird nach jeder Claude-Antwort automatisch aktualisiert (Stop-Hook in
`C:/Users/Kevin/.claude/settings.json`, Skript `sichern.py`).

## Zurueckspielen auf einem neuen PC
1. Repository klonen nach `C:/Users/Kevin/Claude-Gedaechtnis`.
2. `gedaechtnis/<projekt>/*.md` nach `C:/Users/Kevin/.claude/projects/<projekt>/memory/` kopieren (Ordnernamen sind die
   Projektpfade von Claude Code, z. B. `C--Users-Kevin-Zomboid-mods-NPCCrew` fuer `C:\Users\Kevin\Zomboid\mods\NPCCrew`).
3. `anleitungen/global_CLAUDE.md` nach `C:/Users/Kevin/.claude/CLAUDE.md`,
   `anleitungen/NPCCrew-Nebenprojekte_CLAUDE.md` nach `C:/Users/Kevin/NPCCrew-Nebenprojekte/CLAUDE.md`.
4. Die Projekte selbst kommen aus ihren eigenen Repositories (NPCCrew, NPCCrew-Turret, NPCCrew-Zweihaender, spaeter NPCCrew-Baer).

Nicht enthalten (Absicht): Zugangsdaten, Gespraechsprotokolle, die Arbeitsunterlagen `NPCCrew/_docs` (Kevins Entscheidung 08.09.:
nur auf der Platte).
