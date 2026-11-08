---
name: kein-bau-waehrend-test
description: Waehrend Kevin spielt/testet keine Lua-Dateien im Mod-Ordner aendern -- jeder Neustart und jedes Hauptmenue->Laden liest halbfertigen Code
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8e7fd0ad-7592-45c0-90c1-5c2a73830a30
  modified: 2026-10-20T16:44:27.216Z
---

Am 20.10. lief der Bau von v3.13.83 im Mod-Ordner, waehrend Kevin v3.13.82 testete. Sein Spielstart um 18:30 las die Dateien, die Bauer A schon geaendert hatte (Client-Teil fehlte): neue Leichen-Aufgabe im Zustand BEREIT ohne Start-Knopf, Crew 0, nach einer Minute vom Besitzer-Waechter mit 'nocrew' beendet -- Kevin meldete es als Fehler ("die machen nichts und die zone war einfach wieder weg"). Die Versionszeile sagte noch v3.13.82.

**Why:** Lua laedt bei JEDEM Spielstart UND bei Hauptmenue -> Laden im Einzelspieler neu (IngameState.exit -> LuaManager.init, CLAUDE.md Abschnitt 5). Ein Bau im Mod-Ordner ist waehrend eines Tests also nie "unsichtbar", sobald Kevin neu laedt (z. B. fuer einen Speichern/Laden-Testpunkt).

**How to apply:** Waehrend Kevin testet: nur Lese-Laeufe (Pruefung, Plan) oder den Bau in einer git-Worktree/Kopie ausserhalb von mods\NPCCrew; erst nach seinem Test (oder mit seinem Wort "ich starte jetzt nicht neu") in den Mod-Ordner. Wenn doch gebaut wird: VORHER sagen "bis Version X fertig ist nicht neu starten/laden". Verwandt: [[mp-server-neustart-nach-aenderung]], [[zuverlaessigkeit-vor-tempo]].
