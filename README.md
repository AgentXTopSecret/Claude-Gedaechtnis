# Claude-Gedaechtnis (privat)

Sicherung, damit nach einem Plattenschaden nichts verloren ist (Kevin 08.11.2026). Jedes Projekt fuehrt sein Gedaechtnis
(Claudes Notizen) im EIGENEN Repository mit (Kevin: "jedes projekt sein gedaechniss da gespeichert"):

| Projekt | Gedaechtnis liegt in | Repository |
|---|---|---|
| NPC Crew (+ alte TrueCompanions-Notizen) | `Zomboid/mods/NPCCrew/_gedaechtnis/` | NPCCrew (committet + laedt der Sicherungs-Waechter) |
| Turret | `NPCCrew-Nebenprojekte/turret/_gedaechtnis/` | NPCCrew-Turret, Zweig `unterlagen` |
| Zweihaender | `NPCCrew-Nebenprojekte/zweihaender/_gedaechtnis/` | NPCCrew-Zweihaender, Zweig `unterlagen` |
| Baer (nach dem Umzug) | `NPCCrew-Nebenprojekte/baer/_gedaechtnis/` | NPCCrew-Baer, Zweig `unterlagen` |
| alle anderen Projekte | `gedaechtnis/<projekt>/` hier | Claude-Gedaechtnis |

Dazu hier: `anleitungen/global_CLAUDE.md` (Kevins Regeln fuer alle Projekte) und `anleitungen/NPCCrew-Nebenprojekte_CLAUDE.md`.
Abgeglichen und hochgeladen wird mit `python sichern.py` nach jeder fertigen Mod-Version (Kevin 08.11.: "nach jeder version von
einer mod"), nicht nach jeder Antwort. Ein Projekt-Repo bekommt dabei nur Commits mit `_gedaechtnis/`, nie halbe Bau-Staende.

## Zurueckspielen auf einem neuen PC
1. Repositories klonen (NPCCrew nach `Zomboid/mods/NPCCrew`, die Nebenprojekte nach `NPCCrew-Nebenprojekte/<projekt>`, die Test-Mods
   vom Zweig `main` nach `Zomboid/mods/<TestMod>`, dieses nach `C:/Users/Kevin/Claude-Gedaechtnis`).
2. Je Projekt `_gedaechtnis/*.md` nach `C:/Users/Kevin/.claude/projects/<projektordner>/memory/` kopieren (Ordnernamen sind die
   Projektpfade von Claude Code, z. B. `C--Users-Kevin-Zomboid-mods-NPCCrew`, `C--Users-Kevin-NPCCrew-Nebenprojekte-turret`;
   die Zuordnung steht in `sichern.py`, Tabelle MAP).
3. `anleitungen/global_CLAUDE.md` nach `C:/Users/Kevin/.claude/CLAUDE.md`, `anleitungen/NPCCrew-Nebenprojekte_CLAUDE.md` nach
   `C:/Users/Kevin/NPCCrew-Nebenprojekte/CLAUDE.md`.

Nicht enthalten (Absicht): Zugangsdaten, Gespraechsprotokolle, die Arbeitsunterlagen `NPCCrew/_docs` (Kevins Entscheidung 08.09.:
nur auf der Platte).
