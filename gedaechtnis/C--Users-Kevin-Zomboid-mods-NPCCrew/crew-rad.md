---
name: crew-rad
description: "Kevin 22.10.: eigenes Crew-Rad auf einer Taste (nur NPC-Crew-Schalter, alle Folgenden auf einmal) als Hauptweg statt HUD-Knopfleiste; Taste in der Tastenbelegung 'NPC Crew', nicht Sandbox; gehoert zu Fahrplan B8b"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-22T13:53:37.656Z
---

Entschieden 22.10.2026 (Anlass: Workshop-Vorschlag von SovietStevey, "crew command wheel on a hotkey"):

- Ein EIGENES Radmenue nur mit NPC-Crew-Eintraegen (Vanillas Q-/V-Rad unberuehrt), wirkt auf ALLE eigenen Folgenden gleichzeitig:
  Haltung (aggressiv/defensiv/passiv), Abstand, Stellung halten, Schusswaffen an/aus, evtl. Stay/Relax fuer alle, Crew-Fenster.
  Jeder Eintrag zeigt den Gruppenstand ('Passive (3/5)' / 'Mixed'). "Greif dieses Ziel an" ist ein neuer Befehl, nicht in dieser Version.
- Das Rad ist der HAUPTWEG; das Ammo-HUD bekommt keine Knopfleiste, nur eine Zustandszeile. Die Funktion "auf alle Folgenden anwenden" steht
  einmal da (dieselben Tueren wie die Einzelknoepfe), ein HUD-Knopf koennte spaeter ohne zweite Antwort dazu.
- Taste: Optionen > Tastenbelegung, Abschnitt "NPC Crew" -- NICHT Sandbox. Kevin wollte Sandbox ("dann wissen die das"); erklaert: Sandbox gilt
  fuer die Welt, keine Taste je Spieler; er war einverstanden. Auffindbar machen: Mod-Optionen-Hinweis, HUD-Tooltip, Guide-Abschnitt Orders.
- Jobs im Rad (Kevin 22.10.): Unterrad 'Jobs' mit den vorhandenen Auftraegen (Sortieren, Fischen, Wasser, Abkochen, Tierpfleger,
  Leichen, Foerster/Werkstatt, Stay/Relax/Guard/Hide), gleiche Tueren und Tore wie die Knoepfe. Offen: Person waehlen dann Job, oder 'alle zurueck
  an die Arbeit', oder beides (Vorschlag beides).
- Vorlage Vanilla `ISEmoteRadialMenu.lua` (halten 450 ms, Umschalt-Option, Unterraeder mit Zurueck).

**How to apply:** Gehoert zu Fahrplan B8b (Sammel-Knopf / Crew-Uebersicht), Einzelheiten in `_docs/bauplaene_2026-10-16/09_ammo_hud.md`
(zweiter Nachtrag + "ENTSCHIEDEN KEVIN 22.10."). Der Planer fragt Kevin vor dem Bau nach Vorgabetaste und Inhalt. Nichts gebaut. Siehe
[[uebergabe-19-10]], [[moegliche-features]].
