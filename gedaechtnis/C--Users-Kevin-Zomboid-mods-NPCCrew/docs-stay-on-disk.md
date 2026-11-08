---
name: docs-stay-on-disk
description: "_docs/ bleibt absichtlich ungesichert und nur auf Kevins Platte - nicht erneut vorschlagen, es ins Repo aufzunehmen"
metadata:
  type: feedback
---

Der Ordner `_docs/` (mit `offene_arbeit.md`, `HANDOVER.md`, der Logistik-Spezifikation
und den Prüfwerkzeugen) steht in `.gitignore` Zeile 5 und liegt in **keiner** Sicherung.
Das ist Kevins ausdrückliche Wahl, nicht ein Versehen. Am 08.09.2026 gefragt, ob ich die
Übergabe-Datei in die Sicherung aufnehmen soll: *"nein das soll nur auf der platte
liegen"*.

**Why:** die Dateien sind interne Arbeitsunterlagen. Was in den Workshop und auf GitHub
geht, ist die Mod — nicht meine Notizen darüber.

**How to apply:**
* `.gitignore` an dieser Stelle **nicht anfassen**, und nicht erneut anbieten, `_docs/`
  zu versionieren oder in `backups\TrueCompanions\` zu kopieren.
* Die Folge bewusst mittragen: Änderungen an `_docs/offene_arbeit.md` sind nach dem
  Schreiben **fertig** — es kommt keine Wächter-Zeile dafür, und `git status` zeigt sie
  nie an. Wer dort nach einer Bestätigung sucht, sucht vergeblich.
* Die Datei bleibt trotzdem der erste Lesestoff jeder Sitzung (CLAUDE.md §8 verweist
  darauf).

Siehe auch [[probes-behind-sandbox-switch]], [[both-modes-always]].
