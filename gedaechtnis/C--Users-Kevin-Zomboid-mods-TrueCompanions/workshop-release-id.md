---
name: workshop-release-id
description: Vor der ersten Workshop-Veroeffentlichung an die Mod-id erinnern - danach ist sie fuer immer festgelegt.
metadata: 
  node_type: memory
  type: project
  originSessionId: bdc5780d-84d1-4dce-b9f1-6dca08a415d1
  modified: 2026-08-27T05:21:17.101Z
---

**Erinnerungsauftrag von Kevin (27.08.2026):** *"erinnere mich daran wenn ich mal frage was
noch benötigt wird die mod im steamworkshop zu veröffentlichen"*.

**Der Punkt:** Die Mod heisst seit v0.94.1 im Anzeigenamen **NPC Crew**, die interne
`id` in beiden `mod.info` steht aber weiter auf **`TrueCompanions`**. Er wollte sie
angleichen; ich habe abgeraten, solange sein laufender Spielstand daran haengt.

**Warum der Zeitpunkt vor der Veroeffentlichung liegt und nicht danach:** Nach dem ersten
Workshop-Release haengen die Spielstaende **aller Abonnenten** an der id. Eine spaetere
Aenderung braeche sie alle, nicht nur seine. Vorher ist es ein einmaliger, kontrollierter
Schnitt.

**Was an der id haengt — nachgemessen am 27.08. in `Saves/Sandbox/2026-08-17_04-15-25/`:**
- `mods.txt` — die Mod-Liste des Spielstands, Klartext, von Hand aenderbar.
- `global_mod_data.bin` — **ungefaehrlich**: die Schluessel dort (`TrueCompanionsRoster`,
  `TrueCompanionsBeacons`, `TrueCompanionsForest`, `TrueCompanionsOptions`,
  `TrueCompanionsFav`) sind feste Zeichenketten in unserem Code
  (`client/BanditsNPCPersistence.lua:28`), **keine Mod-id**. Companions, Beacons, Zonen und
  Optionen ueberleben eine id-Aenderung.
- `WorldDictionary.bin` / `WorldDictionaryLog.lua` — **das Risiko**: jedes platzierte
  `Base.TCAppearanceStation` und `Base.TCSurvivorBeacon` traegt dort `modID = "TrueCompanions"`
  neben Feldern `obsolete` / `removed` / `isLoaded`. Neue id = die Objekte gelten als aus
  einer entfernten Mod. **Ob das Spiel sie loescht, ist NICHT belegt** — nur die Feldnamen
  legen es nahe. Vor einer Empfehlung nachschlagen, nicht wiederholen.

**Wenn er nach der Veroeffentlichung fragt, dieses zuerst nennen** — dann Poster, Beschreibung,
Tags, `require=Bandits2`, und die drei Sprachen. Siehe [[kurz-antworten]]: kurz halten, die
id-Frage ist der einzige unumkehrbare Punkt der Liste.
