---
name: schlachten-coming-soon
description: "Zwischen-Upload vor fertiger Stufe 3: Schlachtregeln-Knopf sichtbar, aber 'Coming soon' und nicht anklickbar; NACH dem Upload (park) die Sperre sofort wieder herausnehmen (Kevin 12.10.)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8e7fd0ad-7592-45c0-90c1-5c2a73830a30
  modified: 2026-10-12T21:44:55.654Z
---

Kevin will den Tierpfleger (Stufe 1+2) schon hochladen, bevor Stufe 3 fertig ist. Fuer diesen Upload soll der Einstieg in die
Schlachtregeln (Tierpfleger Stufe 3, Teil 3-1 = v3.13.30) NICHT hinter -debug versteckt werden, sondern sichtbar bleiben mit dem
Zusatz "Coming soon" und NICHT ANKLICKBAR. Kevin woertlich (12.10.2026): "kann nicht dahinter stehn 'coming soon' und nicht
anklickbar statt -debug? aber das muesteste dir dann merken wieder raus zu nehmen nachdem es hochgeladen ist im workshop".

**Why:** Ein Regelfenster ohne Wirkung waere fuer fremde Spieler Halbfertiges; verstecken wollte er es aber nicht. Und er weiss aus
dem KeeperEnabled-Fall, dass eine Sperre am Ende vergessen werden kann.

**STAND 12.10.2026 23:45:** v3.13.31 (Sperre AN) ist hochgeladen und geparkt; v3.13.32 hat die Sperre wieder AUS
(`BanditsNPC.SlaughterSoon()` gibt false zurueck) und ist NICHT in den geparkten Ordner gespiegelt -- der bleibt auf dem
oeffentlichen Stand. Kevin ist informiert. Die Zusage ist damit eingeloest; es gilt nur noch die Regel fuer den NAECHSTEN Upload.

**How to apply:**
- Die Sperre ist EIN Schalter (`BanditsNPC.SlaughterSoon()` in shared/BanditsNPC.lua, Form wie `KeeperEnabled`). Vor dem
  Zwischen-Upload: AN (Knopf grau, Text "Coming soon", Vorschau-Liste und Schilder aus), Kevin testet DIESEN Zustand, dann
  `workshop_sync.py stage`, er laedt hoch, `park`.
- SOFORT NACH `park`: Schalter wieder AUS (im Entwicklungsstand ist das Fenster normal benutzbar), Version/Changelog-Zeile dazu,
  und Kevin sagen, dass es herausgenommen ist. Das ist die Zusage -- nicht vergessen.
- Vor JEDEM weiteren Upload, solange Stufe 3 nicht komplett ist: Schalter wieder AN und Kevin vorher sagen, was sichtbar ist.
- Beim Upload, der Stufe 3 veroeffentlicht: Schalter AUS bzw. ganz entfernen, zusammen mit der Pruefung von
  [[tierpfleger-schalter-upload]] (KeeperEnabled fuer alle an). Vor jedem `stage` beide Werte greppen und Kevin nennen.
- Der Text "Coming soon" braucht einen UI-Schluessel in allen sieben Sprachen ([[franzoesisch-uebersetzung]]).
- Workshop-Beschreibung (Kevin 12.10. spaet): der Tierpfleger bleibt unter "Planned features", die Zeile lautet nur noch
  "[*] [b]Animal keeper[/b] – about 80% done and already playable." (Kevin: Prozentzahl dahinter, den Erklaertext weglassen,
  "das sehn die ja dann eh was er kann"). Beim Upload, der Stufe 3 veroeffentlicht: Zeile aus "Planned" nehmen bzw. die Zahl
  anpassen -- Kevin vorher fragen, wie er sie haben will.
Siehe [[stufe3-entscheidungen]], [[workshop-updates-nur-auf-ansage]].

**Stand 15.10.2026:** Stufe 3 ist komplett (v3.13.48). BanditsNPC.SlaughterSoon() steht auf false und riegelt jetzt ALLE Wirkungen von 3-2 bis 3-7 (Ausnahmen: Rezept Forge Large Hook immer sichtbar, Zonen-Warnung 3-9 und Skill 3-10 gelten immer). Fuer den Veroeffentlichungs-Upload die Sperre ganz entfernen (grep SlaughterSoon), fuer jeden Zwischen-Upload vorher auf true und Kevin sagen.
