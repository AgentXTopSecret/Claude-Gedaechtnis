---
name: copy-paste-in-npc-crew
description: "FESTE REGEL Kevin 08.11.: Nebenprojekte (Turret, Baer, Zweihaender) per Copy-Paste in NPC Crew einbaubar, KEINE Cheat-/Testmenues kommen mit"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-11-07T23:55:46.839Z
---

Kevin 08.11.2026: *"und ganz wichtig ist das was du alles baust soll spaeter einfach in npc crew einbaubar sein also im optimal fall einfach copy paste und direkt fertig"*.

**Why:** Turret und Baer sind fuer NPC Crew gedacht (Basisverteidigung, Begleiter); die Test-Mods sind nur die Werkbank, damit der Bau NPC Crew nicht stoert.

**How to apply:** Regeln wie beim Turret (`_docs/turret/PLAN.md` Kopf, Copy-Paste-Regeln a-f): Lua-Dateien heissen schon so, wie sie in NPC Crew heissen werden (`BanditsNPCTurret*`, `BanditsNPCBear*`), Module `BanditsNPC.Turret` / `BanditsNPC.Bear`, Texte `UI_BN_<Thema>_*` in sieben Sprachen, Sandbox `BanditsNPC.<Thema>*`, gleiche relative Pfade fuer Modelle, Texturen, Toene, Skripte; reine Testhilfen in getrennten Dateien (`NCTurretBench*`, `NCBearBench*`), die nie kopiert werden; Kollisionsprobe gegen NPC Crew (CLAUDE.md v3.8.38); ein Uebernahme-Skript je Thema unter `_docs/tools/` mit Trockenlauf und Probe an einer Kopie, `--echt` nur auf Kevins Wort. Der Baer braucht diesen Umbau noch (heute `NCBear*`-Dateien): in B1 mit erledigen. Zweihaender: Skript, Modell, Texturen sind uebernehmbar, `NCZweihaender.lua` ist nur Testhilfe. Verwandt: [[turret-plan]], [[baer-projekt]].

**FESTE REGEL fuer alle Nebenprojekte (Kevin 08.11.: 'ja mach das als feste regel bei den neben projekten und ja achte darauf das keine cheat menues davon rueber kommen am ende'):** Keine Cheat- oder Testhilfe kommt mit nach NPC Crew: kein Spawn-Menue, kein Bank-/Testmodus, keine Konsolenbefehle zum Erzeugen, Groesse-Setzen, Vorspulen oder Proben (`NCTurret_*`, `NCBear_*`), keine Debug-Rechtsklicks. Sie leben NUR in den Bench-Dateien. Jedes Uebernahme-Skript prueft das selbst: die kopierten Dateien duerfen keine dieser Befehle definieren und keinen Test-Menuepunkt anlegen, sonst bricht es ab. Was der Spieler im fertigen Spiel braucht (z. B. ein Junges finden statt spawnen), wird als echte Spielmechanik gebaut, nicht als Menue.

**UMGEZOGEN 08.11.2026:** Turret und Zweihaender liegen jetzt in `C:/Users/Kevin/NPCCrew-Nebenprojekte` (eigene CLAUDE.md, eigene Sitzung; Kevin: 'kannst du die die grade nicht laufen verschieben? das ich dann da weiter arbeiten kann'). Pfade `_docs/turret`, `_docs/modelle/turret_stufe3`, `_docs/tools/turret_*` und `_docs/modelle/zweihaender` gibt es hier nicht mehr (Notiz `_docs/UMGEZOGEN_nebenprojekte.md`). Turret-Entscheidungen fuehrt ab jetzt `NPCCrew-Nebenprojekte/turret/KEVIN_ENTSCHEIDUNGEN.md`. Der Baer folgt nach baer-anim. In dieser Sitzung Turret/Zweihaender nicht weiterbauen, ausser Kevin sagt es hier.
