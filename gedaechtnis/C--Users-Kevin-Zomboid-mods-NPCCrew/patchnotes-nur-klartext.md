---
name: patchnotes-nur-klartext
description: "Patchnotes fuer Steam nur als Klartext schreiben, kein BBCode ([h2]/[list]); und vollstaendig -- alle Versionen seit dem letzten Upload"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-27T12:55:21.191Z
---

Kevin, 27.09.2026: "ich brauch nur klartext diese [H2] sachen bringen nix bei patch notes". Dazu am selben Tag:
"vergess nichts beim letzden mal hast du so einige patch notes vergessen".

**Why:** Steams Change-Notes-Feld zeigt BBCode nicht so, wie er es will; die BBCode-Fassung war doppelte Arbeit. Beim
letzten Upload fehlten mehrere Aenderungen in den Notes.

**How to apply:** Nur eine Klartext-Datei `_docs/patchnotes_vX_plain.txt` (Abschnittsueberschrift, darunter "- " Zeilen).
Vollstaendigkeit: jede Version seit dem letzten oeffentlichen Upload auslesen (Changelog in shared/BanditsNPC.lua) und
gegen die Versionsliste pruefen lassen; Zwischenstaende (Reviews) nur als Endverhalten. Siehe [[workshop-updates-nur-auf-ansage]].

**Nachtrag 27.09.:** die lange Fassung (19k Zeichen) passte nicht ins Steam-Feld ("hat den rahmen gesprengt"). Immer zusaetzlich eine Kurzfassung `_docs/patchnotes_vX_short.txt` unter ~4000 Zeichen schreiben -- alle Themen, knapp; die lange bleibt als Referenz.
