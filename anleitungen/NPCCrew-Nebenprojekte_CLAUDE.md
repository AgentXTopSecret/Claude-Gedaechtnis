# NPC Crew Nebenprojekte -- Arbeitsanweisung

Lies das zuerst ganz. Dieser Ordner ist seit 08.11.2026 die Werkstatt fuer Kevins Nebenprojekte zur Mod **NPC Crew**
(Project Zomboid B42.21, auf der Mod "Bandits"). Die Mod selbst wird in einer ANDEREN Claude-Sitzung gebaut
(`C:\Users\Kevin\Zomboid\mods\NPCCrew`, dort steht ihre grosse `CLAUDE.md` mit allen Lehren). Hier wird NIE in NPC Crew
geschrieben -- ausser durch ein Uebernahme-Skript mit `--echt` auf Kevins ausdrueckliches Wort.

## 0. Die Grundregel (Kevin 08.11.2026)

> *"ganz wichtig ist das was du alles baust soll spaeter einfach in npc crew einbaubar sein also im optimal fall einfach copy paste
> und direkt fertig"* -- *"ja mach das als feste regel bei den neben projekten und ja achte darauf das keine cheat menues davon
> rueber kommen am ende"* -- *"mit unseren regeln die sollen da gelten also das die mods fuer die npc crew mod gemacht werden und
> das man die am ende leicht in die npc crew mod einfuegen koennen soll"*

Jedes Nebenprojekt wird FUER NPC Crew gebaut. Die Test-Mod ist nur die Werkbank, damit der Bau NPC Crew nicht stoert. Daraus:
1. **Namen schon wie in NPC Crew:** Lua-Dateien `BanditsNPC<Thema>*.lua` (z. B. `BanditsNPCTurret*`, `BanditsNPCBear*`), Module
   `BanditsNPC.<Thema>`, Texte `UI_BN_<Thema>_*` in SIEBEN Sprachen (EN, PTBR, RU, KO, ES, CN, FR; CN nur Zeichen, die Vanilla-CN
   selbst benutzt), Sandbox `BanditsNPC.<Thema>*`, gleiche relative Pfade fuer Modelle, Texturen, Toene, Skripte. Gegenstandsnamen
   bleiben fuer immer stabil (sonst verwaisen Gegenstaende in Spielstaenden). Vor jedem neuen Namen in NPC Crew greppen
   (`C:\Users\Kevin\Zomboid\mods\NPCCrew\42\media\lua`), ob er frei ist (NPC Crew CLAUDE.md, Kollisionsprobe v3.8.38).
2. **Keine Cheat- oder Testmenues nach NPC Crew:** Spawn-Menues, Bank-/Testmodus, Konsolenbefehle (`NCTurret_*`, `NCBear_*`,
   `NCZweihaender*`) und Debug-Rechtsklicks leben NUR in eigenen Bench-Dateien (`NCTurretBench*.lua`, `NCBearBench*.lua`, ...), die
   nie kopiert werden. Was der Spieler im fertigen Spiel braucht, wird als echte Spielmechanik gebaut, nicht als Menue.
3. **Je Thema ein Uebernahme-Skript** (`<thema>/tools/<thema>_uebernahme.py`): Trockenlauf (schreibt nichts), `--probe <ordner>`
   (echter Durchlauf an einer Kopie samt aller Pruefer), `--echt` nur auf Kevins Wort. Es prueft selbst: keine Bench-Datei, kein
   Testbefehl, kein Testmenue in den kopierten Dateien, sonst Abbruch; Texte sortiert in alle sieben `UI.json` zusammenfuehren
   (Round-Trip `json.dumps(data, indent=4, ensure_ascii=False) + "\n"`). Beruehrungen mit NPC Crew (Aufsaetze, Zeilen) stehen als
   "Naehte" in einer eigenen Liste (Vorbild `turret/NAEHTE.md`), jeder Aufsatz in `OnGameBoot`, keine NPC-Crew-Datei wird geaendert.
4. **NPC Crew bleibt optional, solange es eine Test-Mod ist:** alles hinter Existenz-Riegeln; mit und ohne NPC Crew darf nichts
   kaputtgehen.

## 1. Mit wem du arbeitest

**Kevin** (Steam `Agent X Top Secret`) programmiert nicht, er beschreibt, spielt und testet. Wenn er widerspricht, hat er
wahrscheinlich recht -- Screenshots mit roten Kreisen sind praezises Feedback.
- **Deutsch, KURZ (3 bis 6 Zeilen), Ergebnis zuerst.** Kein Code im Chat (ausser eine Zeile, die er eintippen soll).
- **"Statisch geprueft, nicht gespielt."** Du kannst das Spiel nicht starten; jede Laufzeit-Behauptung ist eine Vermutung. Lua laedt
  nur beim Spielstart: nach jeder Aenderung sagen, dass er das Spiel neu starten muss.
- **Schlechte Nachrichten mit Beleg, keine Behauptung ohne Fundstelle; sonst "ungeprueft".**
- Fertige Arbeit sofort auf die Platte. Crew-Figuren neutral (they/the keeper), englisch `singleplayer`/`multiplayer` zusammen.

## 2. Wo was liegt

| Was | Pfad |
|---|---|
| Diese Werkstatt | `C:\Users\Kevin\NPCCrew-Nebenprojekte` (`turret\`, `zweihaender\`, spaeter `baer\`; Arbeitsdaten `_arbeit\`) |
| Test-Mods (laedt das Spiel) | `C:\Users\Kevin\Zomboid\mods\NCTurretTest`, `...\NCZweihaender`, `...\NCBearTest` |
| NPC Crew (NUR LESEN) | `C:\Users\Kevin\Zomboid\mods\NPCCrew` -- Code `42\media\lua`, Landkarte `_docs\landkarte_index.txt` (greppen), Lehren `CLAUDE.md` (gross; nur den Abschnitt lesen, den du brauchst) |
| Vanilla-Lua (NUR LESEN) | `C:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid\media` (+ `projectzomboid.jar` daneben) |
| Bandits (NUR LESEN) | `C:\Program Files (x86)\Steam\steamapps\workshop\content\108600\3268487204\mods\Bandits\42.21` und `...\Bandits\common` |
| Konsole | `C:\Users\Kevin\Zomboid\console.txt`, Logs `C:\Users\Kevin\Zomboid\Logs` |
| Sicherungen | `C:\Users\Kevin\Zomboid\backups\<TestMod>\` (Zips mit Zeitstempel, nie in einen Mod-Ordner) |
| Werkzeuge | `C:\Users\Kevin\Tools\`: Blender 5.2.3 `blender\blender-5.2.3-windows-x64\blender.exe` (`--background --factory-startup --python skript.py -- args`), JDK 25 `jdk25\jdk-25.0.4.1+1\bin\javap.exe` (Jar-Klassen mit Python zipfile nach einem Ordner unter `C:/Users/...` ziehen, dann `javap -c -p`), Vineflower, Lua 5.1 `lua51\lua5.1.exe` (Attrappen; Kahlua ist kein echtes 5.1, z. B. kein `next`) |
| Lua-Pruefer (von NPC Crew, nur aufrufen) | `python C:\Users\Kevin\Zomboid\mods\NPCCrew\_docs\tools\luacheck.py`, `scopecheck.py`, `localcount.py` (aktiv UND insgesamt, Grenze 200, ab 180 aufteilen), `luacheck_pz.py` (nil-Globals) |
| Fehlerwaechter | `python C:\Users\Kevin\Zomboid\mods\NPCCrew\_docs\tools\bugwatch.py` -- bei JEDEM Test als Monitor mitlaufen lassen (30 min, dann neu) |

## 3. Die eiserne Regel fuer Engine-Aufrufe
Rufe nie eine Engine-Methode auf, die du nicht als echten Aufruf in Vanilla-Lua oder Bandits gesehen hast -- mit GLEICHEN
Argumenttypen. Erst die Fundstelle, dann der Aufruf; Fundstelle im Kommentar nennen. "Das steht da nicht" ist eine Behauptung ueber
eine Suche, die du gemacht haben musst. Eine Ausnahme (Jar-Beleg) braucht Kevins Wort je Methode. Ein `pcall` um einen unbelegten
Aufruf ist eine Tarnkappe, keine Absicherung.

## 4. Einzelspieler UND Mehrspieler
Jede Aenderung muss im SP und im MP laufen (oder im MP ehrlich als aus/offen markiert sein). SP-Test ist `not isServer() and not
isClient()` (beide Negationen; ein dedizierter Server ist auch "nicht Client"). Was der Server wissen muss, kommt nie aus einem
Client-Glauben. Kevins rote Linien: kein Gegenstand verloren oder verdoppelt, kein Kick (Rolle user, AntiCheat 2), nichts haengt
endlos, keine NPC-Crew-Figur wird gestoert. Changelog/Bericht nennt den SP-Zweig.

## 4a. Eine Sitzung je Projekt (Kevin 08.11.: "ich hab die jz einzelnd geoeffnet")
Kevin fuehrt je Nebenprojekt eine eigene Claude-Sitzung (Turret, Zweihaender, spaeter Baer). Daraus:
- **Jede Sitzung arbeitet nur in IHREM Unterordner** (`turret\`, `zweihaender\`, `baer\`) und IHRER Test-Mod. Fremde Unterordner nur lesen.
- **Diese `CLAUDE.md` gehoert allen:** aendern nur fuer eine Regel, die alle betrifft, und dann nur einen Absatz anhaengen (nie neu
  schreiben); projektbezogene Notizen gehoeren in den eigenen Unterordner (z. B. `turret\PLAN.md`).
- **Hoechstens 10 Agenten je WORKFLOW** (Kevin 08.11.: *"eigtl war die 10 agenten regel sogar per workflow gedacht"*): jeder Lauf
  fuer sich, andere Laeufe und Sitzungen zaehlen NICHT dagegen. Mehr als 10 in EINEM Workflow nur nach Frage mit Zahl und Grund.
- Gemeinsame Werkzeuge (Blender, javap, Pruefer) duerfen gleichzeitig laufen; Renders der Sitzungen nicht gleichzeitig auf die GPU
  legen, wenn eine Sitzung gerade rendert (kurz `tasklist | grep -i blender` pruefen).

## 5. Wie gebaut wird
- **Jede Version als Workflow:** Plan -> Bau -> Pruefer -> Nachbesserung -> Gegenpruefer -> Integrator (Kevin: "mir ist
  Zuverlaessigkeit wichtiger"). Zwei Bauer nur mit getrennten Dateien.
- **Hoechstens 10 Agenten je Workflow** (mehr nur nach Frage mit Zahl und Grund). Kevin hat ein Max-Abo: vor grossen Laeufen den
  Verbrauch pruefen (5-Stunden- und Wochenlimit) und ihm die Agentenzahl nennen. Die Grenze gilt je Workflow (4a), nicht summiert.
  Massenarbeit lieber per Skript.
- **Alles erst im Arbeitsordner bauen, dann in EINEM Zug in die Test-Mod kopieren** (Kevin kann jederzeit spielen), vorher und
  nachher sichern (Zip nach `Zomboid\backups\<TestMod>\`), byte-gleich nachzaehlen, nur hinzufuegen/ueberschreiben, nie loeschen.
- **Nicht bauen oder rendern, waehrend Kevin mit der betroffenen Mod spielt:** `tasklist | grep -i ProjectZomboid`; laeuft das
  Spiel, die Mod-Liste des GELADENEN Spielstands lesen (zweite `loading`-Liste in console.txt bzw. `mods.txt` des Spielstands; die
  erste `loaded OK`-Zeile kommt schon aus dem Hauptmenue). Renders nur auf der RTX 4090 (OPTIX, auch Denoiser), nie waehrend er spielt.
- Diagnose ueber Log-Zeilen hinter einem Schalter, echte Fehler immer melden; nichts Teures je Bild; Deckel fuer alles, was waechst;
  Mehrfachrueckgaben erst in Locals holen; Zeilenenden je Datei pruefen; Heredoc-Falle: keine Backslash-Escapes in Python-Heredocs.

## 6. Sicherheit (fest)
- Nie `cd` nach `C:\Sandbox`; nie rekursiv ueber `C:\Users\Kevin` oder ein Laufwerk suchen -- nur die Orte aus Abschnitt 2, und
  jeder Agenten-Auftrag nennt seine Suchorte ausdruecklich.
- Steam-API-Schluessel nie lesen, RCON-Passwort nie ausgeben, keine Zugangsdaten eingeben, keine Autostart-Eintraege oder
  versteckten Starts, PC nie herunterfahren, Spiel/Server nur Kevin starten, nie etwas hochladen.
- **Downloads nur mit Name, Quelle, Groesse und Kevins Ja je Datei.** Nichts aus fremden Mods kopieren (Kevin: nicht "wie ein Dieb");
  fremde Mods duerfen gelesen werden, um zu lernen.
- Nie von Hand in NPC Crews git committen; NPC Crew nicht anfassen.

## 7. Stand der Projekte (08.11.2026)
- **Turret** (`turret\`, Test-Mod `NCTurretTest`): T1 und T1b fertig und gespielt (dreht, schiesst, hunderte Zombies fluessig,
  Schweben behoben, Rauch, Reichweiten MK I 15 / MK II 30 / MK III 60). Plan `turret\PLAN.md` (T1..T10, am Ende Kevins neue
  Entscheidungen und die Umzugsnotiz), alle Entscheidungen `turret\KEVIN_ENTSCHEIDUNGEN.md`, Naehte `turret\NAEHTE.md`, Modelle und
  Blender-Skripte `turret\modell\`, Werkzeuge `turret\tools\` (`turret_uebernahme.py`, `turret_backup.py`). **Naechster Schritt T2
  (Figur am Turret)**, vorher im Uebernahme-Skript: Cheat-Pruefung einbauen und die Pluenderer-Naht (`SR.LootTypeRefused` nennt
  `NCTurret`) als erlaubte Fundstelle eintragen (PLAN.md 'Umzug').
- **Zweihaender** (`zweihaender\`, Test-Mod `NCZweihaender`): fertig nach Kevins Foto (Umriss 93 %), **ungespielt**. Quelle
  `zweihaender\zweihaender.py`, Vergleich `vergleich.py`. Skript `module NCSword`, Modell `NCZweihaender` (Prop2 wie Katana),
  `NCZweihaender.lua` ist nur Testhilfe (Rechtsklick-Spawn im SP) und darf nie mit nach NPC Crew. Uebernahme-Skript fehlt noch.
- **Baer** (Test-Mod `NCBearTest`): wird noch in der NPC-Crew-Sitzung gebaut (Lauf 'baer-anim' laeuft am 08.11.) und zieht
  danach hierher um (`baer\`). Bis dahin NICHTS an `NCBearTest` aendern.

## 8. Technik, die hier schon bezahlt wurde
- PZ-Modelle: `MaleBody.x` 0,98 Einheiten = 1,8 m (0,544 Einheiten je Meter). FBX ueber Assimp: Spiel-Einheiten = rohe Punkte x
  Lcl-Skalierung x Skript-`scale` (UnitScaleFactor wird ignoriert). Blender-Export `axis_forward="-Z", axis_up="Y"`,
  `apply_scale_options="FBX_SCALE_ALL"` -> Blender-Z = Spiel-Y. Waffen: Klinge entlang +Y, `attachment Bip01_Prop2` wie Katana.
- Bodengegenstaende drehen: `setWorldZRotation` (belegt `ISDropWorldItemAction.lua`), in 5-Grad-Schritten; ein Streupunkt erzwingt
  Direktzeichnen statt 3D-Atlas. Ein `attachment world`-Versatz hebt das Modell (T1b: -0.48 entfernt, sonst schwebt es).
- Tiere: AnimalDefinitions in Lua; das AnimSet muss eine Vanilla-Gruppe sein (z. B. `buck`), Clips heissen wie deren Knoten;
  `setSizeForced` (Vanilla `ButcheringUtil.lua:569`); Zombies greifen Tiere nie an (`AttackState`), Bandits zielt nie auf Tiere.
- Zeichnen ueber dem Bild (Leuchtspur, Laser, Muendungsfeuer): Bandits `client/BanditProjectile.lua` (`renderline`, `renderPoly`,
  `ISCoordConversion.ToScreen`); Sichtlinie `LosUtil.lineClear` (Bandits `BanditUtils.lua:1288`); Linie an der ersten Wand kappen.
- Zombie umwerfen: `knockDown` wirft in idle/walktoward/pathfind/attack/lunge um (die Engine sortiert Uebergaenge nach Prioritaet,
  dann nach Zahl der Bedingungen); `testDotSide` liefert FRONT/BEHIND/LEFT/RIGHT, die XML fragt FRONT/BACK.
- Blender: `hair_length` ist 4 x `normal_factor` (dasselbe Feld); ein schwarzes Bild zuerst an den Massen der Szene suchen.
- Das Spiel laedt 76 Kacheln um den Spieler; alles weiter weg existiert nicht. Reichweiten nie darueber.

## 9. Git (seit 08.11.2026, Kevin: "jedes als eigenes git")
Jedes Projekt hat ZWEI eigene, nur lokale Repositories (nie zusammengelegt, kein GitHub ohne Kevins Wort, kein push):
| Projekt | Unterlagen | Test-Mod (Git-Verzeichnis liegt in den Sicherungen, im Mod-Ordner nur die Zeigerdatei `.git`) |
|---|---|---|
| Turret | `turret/` | `Zomboid/mods/NCTurretTest` -> `Zomboid/backups/NCTurretTest/repo.git` |
| Zweihaender | `zweihaender/` | `Zomboid/mods/NCZweihaender` -> `Zomboid/backups/NCZweihaender/repo.git` |
| Baer (nach dem Umzug) | `baer/` | `Zomboid/mods/NCBearTest` -> `Zomboid/backups/NCBearTest/repo.git` |
- Je Repo `.gitattributes` mit `* -text` (Git schreibt keine Zeilenenden um) und `core.autocrlf false` -- nicht aendern.
- **Committen tut die Sitzung selbst** (hier gibt es keinen Sicherungs-Waechter wie bei NPC Crew): nach jeder fertigen Version
  bzw. jedem fertigen Lauf ein Commit je betroffenem Repo, Meldung kurz auf Deutsch (ASCII), was und warum; der Integrator macht es.
  Keine halben Staende committen, nie `--force`, nie Verlauf umschreiben.
- Uebernahme-Skripte kopieren nie `.git`/`.gitattributes` aus der Test-Mod nach NPC Crew.
- Die Wurzel `NPCCrew-Nebenprojekte` (diese CLAUDE.md, `_arbeit/`) ist absichtlich KEIN Repo.
