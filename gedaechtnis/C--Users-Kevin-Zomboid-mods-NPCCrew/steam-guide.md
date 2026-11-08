---
name: steam-guide
description: "Steam-Guide \"How to use NPC Crew\" (id 3822355628); REGEL Kevin 31.10.: bei JEDEM Upload auf den neuesten Stand bringen; Quelle _docs/guide/guide_en.txt"
metadata:
  node_type: memory
  type: reference
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-18T16:03:13.461Z
---

Steam-Guide "How to use NPC Crew", id 3822355628, Link https://steamcommunity.com/sharedfiles/filedetails/?id=3822355628.
Veroeffentlicht 18.10.2026 auf Kevins Ja (13 Abschnitte, Bild _docs/guide/guide_bild.png). Quelltext: `_docs/guide/guide_en.txt`
(je Abschnitt `=== SECTION: ... ===`), Abschnitts-Ids und Stand in `_docs/guide/guide_steam_id.txt`.

Verlinkt in der Workshop-Beschreibung direkt unter dem REQUIRES-Absatz -- live auf Steam UND in der geparkten
`backups/Workshop-Upload/NPCCrew/workshop.txt` (sonst ueberschreibt der naechste Upload den Link).

**How to apply:** Aendert sich etwas an Bedienung/Tasten/Berufen, den Guide-Abschnitt mitpflegen (Steam: manageguide > Abschnitt
bearbeiten, Speichern ist Ajax). Kevin meldet sich im eingebauten Browser selbst an. Siehe [[upload-v3-13-70]].

21.10.: Abschnitt 'Clean up corpses' (zwischen Water carrier and cook und Settings) + 2 FAQ-Eintraege vor 'Reporting a bug' von Claude im eingebauten Browser eingetragen (Kevin angemeldet, sein Auftrag). Stil der Abschnitte: [h2], [olist] fuer Schritte, [list] fuer Punkte. Bearbeiten: steamcommunity.com/sharedfiles/manageguide/?id=3822355628; Speichern-Knopf unten per Koordinate, Erfolg per fetch der Guide-Seite pruefen. Vorlage _docs/guide_abschnitt_leichen.txt.

**REGEL (Kevin 31.10.2026: *"du must dir noch merken irgentwie das wenn wir etwas hochladen das unser guide aktualsiiert werden muss damit
es auf neusten stand ist"*): JEDER Upload bringt den Guide mit auf den neuesten Stand.** Ablauf vor dem `stage`: (1) alles, was sich seit dem
letzten Upload an Bedienung, Knoepfen, Reitern, Berufen, Tasten, Sandbox-Optionen geaendert hat (Patchnotes-Entwurf + Changelogs), gegen
`_docs/guide/guide_en.txt` halten; (2) neue/geaenderte Abschnitte als Entwurf in `_docs/guide/` schreiben (Stil [h2]/[olist]/[list], neutral
'they', singleplayer/multiplayer zusammen, nur was der Code heute tut); (3) Kevin zeigen; (4) nach seinem Ja im eingebauten Browser eintragen
(er ist angemeldet) -- zeitgleich mit seinem Upload, nicht vorher (sonst beschreibt der Guide Dinge, die noch nicht live sind); (5)
guide_en.txt nachziehen. Steht auch in `_docs/plan_upload_2026-10-30.md` Schritt 10 und in [[vor-upload-pflicht]].
Fuer den naechsten Upload (nach v3.13.95) fehlt im Guide mindestens: der ganze FARMER (Fields-Reiter, Feld zeichnen, Sorte, Regeln, Stats,
Next harvest, Wasserfass, Ertragskiste), Saatpackungen, Buesche/Baeume auf Beeten, Duengen 'both', Rezepte im multiplayer vom Server
(Save to server nur admin/moderator), Leiche im multiplayer mit Tasche.

01.11.2026 (Upload v3.14.27): Farmer-Abschnitt (sectionid 9454733, hinter Animal keeper) + Wasser/Berufe/MP/FAQ live eingetragen; guide_en.txt nachgezogen. Neuer Abschnitt: AddNewSubSection, dann Reihenfolge per Seiten-Funktion OnSubSectionReorder; Bearbeiten: Textarea #description setzen, ValidateEditSubSectionForm (Speichern-Link), Erfolg per fetch der Guide-Seite pruefen.

03.11.2026 (Upload v3.14.38): zehn Abschnitte live eingetragen, guide_en.txt nachgezogen (jetzt mit Clean up corpses). Der eingebaute Browser war nicht angemeldet, Kevin hat sich selbst eingeloggt. Bearbeiten: je editguidesubsection-Seite #description setzen, ValidateEditSubSectionForm(), Laenge per fetch pruefen; Sektions-Ids: Getting started 9401092, Building 9401099, Recruiting 9401106, Orders 9401107, Professions 9401109, Storage 9401110, Forester 9401111, Fisher 9401116, Animal keeper 9401119, Water carrier 9401124, Settings 9401126, Multiplayer 9401127, FAQ 9401129, Clean up corpses 9421131, Farmer 9454733.

06.11.2026 (Upload v3.14.51): elf Abschnitte live eingetragen, je per Pruefsumme bestaetigt (Fragment: fetch der editguidesubsection-Seite, #description lesen, gegen den lokalen Hash halten); guide_en.txt nachgezogen. Vorher Hash-Vergleich Steam gegen guide_en.txt: alle gleich, also ueberschreibt man nichts Fremdes. Der Browser war nicht angemeldet, Kevin hat sich selbst eingeloggt. FAQ mit 7997 Zeichen angenommen. Offen: `_docs/guide_abschnitt_leichen.txt` ist eine alte Kopie des Leichen-Abschnitts.
