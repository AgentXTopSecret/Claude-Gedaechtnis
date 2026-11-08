---
name: tierpfleger-schalter-upload
description: "Tierpfleger-Schalter BanditsNPC.KeeperEnabled(): Zwischen-Uploads nur-debug, nach Park zurueck AN; beim VEROEFFENTLICHUNGS-Upload unbedingt fuer alle AN (Kevin 07.10.)"
metadata:
  type: feedback
---

Alle Einstiege des Tierpflegers (Befehl, Reiter, Ausloeser) laufen ueber EINE Abfrage (BanditsNPC.KeeperEnabled()), beim Bauen AN.

**Why:** Kevin 30.09.: ein wichtiger Bugfix muss mitten im Tierpfleger-Bau hochladbar sein, ohne dass Spieler Halbfertiges sehen -- aber eine Dauer-Sperre wird am Ende vergessen ("oder du baust das erst ein wenn es wirklich noetig ist das waere eigtl besser").

**How to apply:** Bei jedem Upload, solange Stufe 1 nicht fertig und von Kevin getestet ist: VOR `workshop_sync.py stage` die Abfrage auf "nur mit -debug" stellen (Changelog-Zeile), hochladen lassen, nach `park` wieder auf AN. Siehe [[workshop-updates-nur-auf-ansage]], [[moegliche-features]].

**FINALER RELEASE (Kevin 07.10.: "merk dir unbedingt das du das -debug rausnimmst fuer den tierpfleger nicht das ich es hochlade und keiner sieht es"):** beim Upload, der den Tierpfleger VEROEFFENTLICHT (Stufe 1-3 fertig), MUSS `BanditsNPC.KeeperEnabled()` (shared/BanditsNPC.lua, Stand 07.10.: `return true`) fuer ALLE an sein -- keine -debug-Sperre. Vor jedem `stage` den Wert pruefen (`grep -n -A2 "function BanditsNPC.KeeperEnabled"`) und Kevin VOR dem Hochladen ausdruecklich sagen, ob der Tierpfleger in diesem Upload sichtbar ist oder nicht. Nach einem Zwischen-Upload mit Sperre: sofort nach `park` wieder auf `return true`.
