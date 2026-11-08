---
name: git-hashes-wandern
description: "Der Backup-Waechter fasst alte Sicherungen regelmaessig zu einem neuen \"Grundstein\" zusammen und schreibt dabei ALLE Commit-Hashes neu; Basis fuer Pruefer-Diffs nie als nackten Hash uebergeben"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-30T14:48:24.524Z
---

Am 30.09. verschwand der Pruef-Basis-Hash 8e11880 mitten im Workflow: der Waechter hatte den Grundstein von 27.09. 17:24 auf 27.09. 23:41 verschoben und die Geschichte neu geschrieben (v3.12.14 hiess danach 997dc45). Geholfen hat ein Tag mit dem alten Namen (`git tag 8e11880 997dc45`), danach wieder loeschen.

**Why:** Pruefer laufen oft laenger als eine Stunde; ein Hash in ihrem Prompt kann dann ungueltig sein, und `git diff <hash>` schlaegt fehl.

**How to apply:** Vor einem Pruef-Workflow einen Tag setzen (`git tag review-<version> HEAD`) und den TAG-Namen in die Prompts schreiben, oder die Basis per `git log --grep="<Commit-Titel>" -1 --format=%h` finden lassen. Tags nach dem Workflow loeschen. Selbst nie committen (der Waechter tut es).
