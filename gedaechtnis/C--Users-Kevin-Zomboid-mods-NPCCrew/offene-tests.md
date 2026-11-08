---
name: offene-tests
description: "Vertagte Tests -- 26.09. vorgemerkt fuer 'gleich': Folgeabstand far/mid + Auto (v3.10.74), Beacon-Rufen bleibt aus (v3.10.71/.73), Chinesisch (v3.10.72); dazu der alte Tuer-Test aus v3.9.10/.11."
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-26T16:30:29.194Z
---

**Vorgemerkt am 26.09.2026 (Kevin: *"merk dir den test mal fuer gleich erst noch andere dinge"*):**

* **v3.10.74 Folgeabstand + Auto (SP und MP):** Folgeabstand auf "far" stellen, ins Auto
  steigen -> sie laeuft bis ans Auto heran und wird "riding"; aussteigen -> sie haelt wieder
  ihren Abstand. Dasselbe mit "mid". [MP "far" BESTANDEN 26.09. (v3.10.87): eingestiegen, Server
  'geparkt, Mitfahrt' x2; offen: "mid" und SP]
* **v3.10.71/.73 Beacon-Rufen (MP):** Rufen ausschalten, aus- und wieder einloggen (oder weit
  weg und zurueck) -> Knopf zeigt weiter "Broadcast for survivors", niemand kommt. Dasselbe mit
  einem AUSGEBAUTEN Beacon und mit weniger Plaetzen. SP: ausschalten, speichern/laden -> bleibt aus.
  [MP Grundfall BESTANDEN 26.09. (v3.10.87); offen: ausgebauter Beacon, Plaetze, SP]
* **v3.10.75 Regal-Fuellbild (SP + MP):** leeres Regal als Lagerkiste, Sortierer fuellt es ->
  Regal zeigt Ware; Companion leert es -> wieder leer gezeichnet; im MP auch beim Testaccount.
  [MP Einraeumen BESTANDEN 26.09. (Holz-Buecherregal/Regal); offen: Leeren, Testaccount-Blick, SP]
* **v3.10.76 Auto-Entladen + Steinbrocken (SP + MP):** Steinbrocken und normale Ware ins Auto in
  der Entladezone -> Ware kommt ins Lager, der Stein bleibt im Auto, sie laeuft nicht endlos hin.
  [MP BESTANDEN 26.09.: 5 Stueck entladen, LargeStone 'nicht ablegbar'; offen: Auto-Fenster-Anzeige, SP]
* **v3.10.77 Auto-Fenster:** Steinbrocken im Auto -> Fenster zeigt ihn grau mit "(too heavy - stays
  in the car)". MP-Regalbild: Sortierer nimmt aus einem Regal -> Bild passt, auch beim Testaccount.
* **v3.10.78 NPC Core Editor (SP, -debug):** Rechtsklick > NPC Core Editor, Station "smithing"
  (jetzt alle elf in der Liste), eigenes Rezept mit Tools "@hammer" anlegen, Apply, Save to file,
  Neustart -> Rezept da und verlangt den Hammer; `Zomboid\Lua\NPCCrew_recipes.txt` (seit v3.10.79)
  enthaelt nur `format=2` und dieses Rezept. Danach: Rezept Delete + Save -> Datei nur `format=2`;
  Knopf Default (v3.10.79) setzt ein eingebautes Rezept zurueck. Der Melder berichtet selbst (Kevins Ansage).
* **v3.10.82/.83 Munition (SP + MP):** Waffe + 3 volle Magazine geben, alles verschiessen, abnehmen -> insgesamt 3
  Magazine (nicht 6). [SP BESTANDEN 26.09. mit v3.10.87, Abnehmen ueber LHand; MP BESTANDEN 26.09. mit M16, 3/3] Waffe + 90 lose Patronen, sofort abnehmen -> 90 Patronen (in Schachteln), kein Magazin.
  M16 mit einem Magazin leerschiessen (Feuerstoss) -> 1 leeres Magazin. unlimited ammo [BESTANDEN 26.09. MP, nur ohne gegebene
  Magazine -- Kevin: gibt da keiner Munition]: lange kaempfen -> keine
  Magazinflut, beim Abnehmen die gegebenen Magazine voll zurueck. MP: weit weg und zurueck, dann abnehmen -> keine
  Verdopplung; Schrotflinte + 100 Schrot -> alles kommt an.
  v3.10.84 dazu: Flinte nachladen lassen und MITTEN drin 'Take weapon' bzw. 'Nur Nahkampf' -> sie friert nicht ein, keine
  roten Fehler. Nachladen, sofort >80 Kacheln weg und zurueck, abnehmen -> alle gegebenen Magazine da. MP: M16 + Magazin +
  Schachtel 5.56 abnehmen -> klappt (vorher abgelehnt); abnehmen waehrend sie schiesst -> keine Extra-Patronen.
  v3.10.85 dazu: [Tausch mitten im Nachladen GESTRICHEN, Kevin 26.09.: Abusing, im SP pausiert das Fenster; nur Harness-belegt].
  SP-Tests 1 + 2 BESTANDEN 26.09. (3 Magazine exakt; 90 lose -> Schachtel + 40). MP 1-3 BESTANDEN 26.09. (M16 3/3; M16+Magazin+
  Schachtel kommt an; weit weg + 3 Neubauten -> 3 Magazine, 47 Patronen). Offen nur noch optional: M16-Salve + 'Take weapon' -> keine
  [BANDITS][WARN]-Zeilen. MP: waehrend 'confirming' Magazin geben -> bleibt in ihrer Tasche; Equip -> 'transfer pending'.
* **v3.10.88 Dauerauftrag ueberspringt Zeilen ohne Lagerware (SP + MP):** [MP BESTANDEN 26.09.: Schmied uebersprang drei
  Zeilen und craftete Forge Bucket]. v3.10.89 dazu: Fenster misst seine Breite (Namen/Hinweise lesbar, Kevins Bild), Hinweis
  heisst 'too little in storage - skipped'; Zimmerer mit 'Burn Charcoal' ohne Holz/Holzplatz oben -> machbare Zeile darunter
  wird beliefert. Offen: SP.
* **v3.10.78 Editor im MP: BESTANDEN 26.09.** 'Test Nails' (smithing, Base.ScrapMetal:1 -> 5 Nails, @hammer) angelegt,
  gespeichert, vom Schmied hergestellt, nach Server-Neustart noch da (Datei + Log '1 eigene'). Nebenfund: im Namen stand ein
  TAB vor 'Test Nails' (Tab-Taste im Feld) -> onApply soll Name/Output trimmen (vorgemerkt fuer die Version nach der
  v3.10.89-Pruefung; beim Laden NICHT trimmen, sonst verwaist die Planzeile). Offen: Delete + Save, Knopf Default.
* **[GESTRICHEN 01.10. -- Sprachen testet Kevin nicht, siehe [[sprachen-testet-kevin-nicht]]] v3.10.72 Chinesisch:** Sprache auf Chinesisch -> F6, F8, V-Fenster, Sandbox-Seite: keine
  Kaestchen oder ?, nichts abgeschnitten.

**Vertagt am 11.09.2026 (Kevin: *"das kannste dir ja mal ins gedaechtnis schreiben als offene
tests fuer irgendwann mal"*):**

* **Tuer-Test (v3.9.10/v3.9.11):** Basis-Tuer abschliessen oder verbarrikadieren, Besitzer
  geht hinein, Testaccount steht draussen neben einer Folgenden (er hat die Hoheit). Sie darf
  die Tuer NICHT schlagen und keine Bretter abbauen; in seiner Konsole kein Destroy/BREACH.
  Nicht testbar, weil Kevins Basis komplett offen ist. Statisch geprueft: der Streifen im
  Guardian laeuft nur auf dem fremden Rechner (v3.9.11), der Besitzer behaelt `passDoor`.

**Why:** Der Rest der Acht-Pruefer-Liste (Magazin, Anwerbung, Entlassung, Uebergabe+Logout,
Login-Schleife, Waisen-Eintraege) ist am 11.09. gespielt und bestaetigt; nur dieser eine
Punkt fehlt und darf nicht stillschweigend als erledigt gelten.

**How to apply:** Wenn Kevin irgendwann eine Tuer verschliesst oder verbarrikadiert, den Test
vorschlagen; bis dahin in `_docs/offene_arbeit.md` (oben) als offen fuehren. Siehe auch
[[logout-parken-offen]].
