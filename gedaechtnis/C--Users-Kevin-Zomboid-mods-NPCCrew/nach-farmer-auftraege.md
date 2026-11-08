---
name: nach-farmer-auftraege
description: "Kevin 27.10.: nach dem Farmer -- eigene Rezepte im MP serverseitig (Schritt 10, Bauplan fertig 28.10.; lokale Dateien abgelehnt, SP lokal weiter); offen: Quest-Luecke (Frage an Kevin), Bandits-Schaden-Regler"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-27T23:10:32.514Z
---

**AUFTRAG (Kevin 27.10.2026 ~12:30), nach dem Farmer bauen:** *"merk dir das für nach dem farmer das es serverseitig läuft und die selbst
eingestellten auf den pc werden dann abgelehnt weil man damit schummeln kann aber in sp sollen die lokalen natürlich noch laufen"*
- MP: die Rezeptdatei des SERVERS (`Zomboid\Lua\NPCCrew_recipes.txt` des Serverprozesses) ist die einzige Wahrheit; der Server schickt die
  Liste an alle Clients (Login + nach jeder Aenderung); die lokale Datei eines Clients wird im MP NICHT gelesen/benutzt (Schummel-Schutz).
- Editor im MP: Speichern schickt die Liste an den Server (nur Staff, Besitz-/Rollenpruefung auf dem Server), Vorlage `Editor.SaveSpawnConfig`
  -> sendClientCommand 'SetSpawnConfig' (`shared/BanditsNPCEditorData.lua` ~:771).
- SP: unveraendert die lokale Datei (beide Negationen, CLAUDE.md 0.7).
- Heute (Stand v3.14.11): `Editor.LoadRecipes` an OnGameBoot auf JEDEM Rechner aus der eigenen Datei; `SaveRecipes` schreibt nur lokal. Vor dem
  Bau klaeren: wo die Produktion im MP die Rezepte liest (Client/Server), Dialoge/Quests gleich mitnehmen?

**BESTAETIGT 27.10. ~23:25 (Kevin):** *"wenn der farmer komplett durch ist will ich noch das du das mit den rezepten einbaust, von mir aus kannst
du nebenbei ja schonmal recherche dafuer betreiben"* und *"also fuer singleplayer aendert sich nichts nur fuer server"* -> BAUEN direkt nach
dem Farmer (nach der Abschlusspruefung); Einzelspieler bleibt WOERTLICH unveraendert. Recherche laeuft seit 23:25 als wf_267c3fd4-9e4 (3 Agenten,
nur lesen), Ergebnis _docs/rezepte_server/BAUPLAN_entwurf.md (+ recherche_datenfluss.md, recherche_vertrauen_transport.md).

**RECHERCHE FERTIG 28.10. ~00:15:** Bauplan steht (9 Agenten, zwei Bauer mit getrennten Dateien). Nebenfund: QUESTS haben dasselbe Loch, groesser
(Server zahlt bis 10 Gegenstaende je Quest und XP ohne Deckel, `server/BanditsNPCPlayerTakeServer.lua`:397-413), Dialoge ein kleineres (Zuneigung).
Kevin gefragt: Q1 Quests/Dialoge als eigene Version noch vor der Pause? Q5 'cooked' in Handdateien auch im SP verwerfen? OHNE Antwort: Q1 NICHT
bauen, Q5 SP unveraendert, Q2-Q4 wie im Bauplan empfohlen. Antworten hier nachtragen.

**OFFEN, nur vorgeschlagen (Kevin fragte, kein Bauauftrag):** Sandbox-Regler 'Nahkampf-/Schuss-Schaden feindlicher Banditen' in % (0-500, Vorgabe
100), Aufsatz auf Bandits `PlayerDamageModel` (BulletHit/MeleeHit/BareHandHit) bzw. Engine-Treffer fuer die Crew; optional MP-Schalter 'PVP-Werte
des Servers'. Kevin: 'eigene werte rein machen waere am besten?' -> ja empfohlen. Braucht sein Wort (Eingriff in Bandits-Entscheidung).

**ERLEDIGT 27.10. ~16:45:** Bandits-Update 08:55 gegen unsere Aufsaetze geprueft (statisch, kein Code noetig; Zaun-Hops frueher -> im Test
beobachten). Ergebnis in _docs/uebergabe_2026-10-26.md Eintrag ~16:45.

**Why:** Kevin will Schummeln im MP verhindern, ohne SP-Spieler einzuschraenken. **How to apply:** Schritt 10 der Waechter-Kette: direkt nach
der Abschlusspruefung als eigene Version bauen (voller Ablauf); danach PAUSE (Kevin 27.10. ~23:40, [[weiterarbeiten-nach-farmer]]). Siehe [[farmer-waechter]], [[uebergabe-26-10]].
ANTWORTEN 31.10.: Q1 nach dem Upload; Q2 Moderatoren ja; Q3 warten (empfohlen); Q4 Datei des Servers; Q5 SP NICHT verwerfen. Rezepte MUESSEN in diesen Upload (Details _docs/plan_upload_2026-10-30.md).
