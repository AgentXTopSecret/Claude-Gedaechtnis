---
name: werkzeuge-tools
description: "Seit 23.10. liegen in C:\\Users\\Kevin\\Tools portable Originale: JDK 25 (javap), Vineflower-Decompiler, luacheck 1.2.0, Lua 5.1.5 -- statt der selbstgebauten Bytecode-Skripte benutzen"
metadata:
  node_type: memory
  type: reference
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-10-23T13:40:08.735Z
---

Kevin 23.10.2026: "lad die runter und installier die ... nur orginale ohne virus". Geladen von den offiziellen Quellen, Pruefsummen
gegen die Herstellerangaben geprueft (JDK + Vineflower SHA-256, Lua MD5; luacheck ohne veroeffentlichte Pruefsumme, offizielles GitHub-Release).
Portabel, kein Installer, nichts an PATH/Windows geaendert; entfernen = Ordner loeschen.

- `C:\Users\Kevin\Tools\jdk25\jdk-25.0.4.1+1\bin\` -- java/javap (Eclipse Temurin 25.0.4.1). Das Spiel-Jar ist Java 25 (Klassenversion 69).
  Klasse erst per Python-zipfile aus dem Jar in den Scratchpad holen, dann `javap -c -p X.class` (getestet an SandboxOptions.set).
- `C:\Users\Kevin\Tools\vineflower\vineflower-1.12.0.jar` -- Decompiler, `java -jar ... X.class <ausgabe>`; Ausgabe nur in den Scratchpad, nur lesen.
- `C:\Users\Kevin\Tools\luacheck\luacheck.exe` -- echter Lua-Pruefer; nur ueber `_docs/tools/luacheck_pz.py` aufrufen (baut die Namensliste selbst).
- `C:\Users\Kevin\Tools\lua51\lua5.1.exe` -- Lua 5.1.5 fuer reine Rechenlogik; Kahlua weicht ab (kein `next`).

**How to apply:** Bei jedem Jar-Beleg zuerst javap/Vineflower statt der Scratchpad-Parser (disasm_full.py, callers_generic.py). Agenten
den Pfad nennen (Suchorte festlegen). ERLEDIGT 23.10.: `python _docs/tools/luacheck_pz.py [dateien]` ist der VIERTE PRUEFER (CLAUDE.md Abschnitt 4 Punkt 4b): Whitelist aus
Vanilla+Bandits-Globalen, Java-Exposer-Klassen (javap) und eigenen Definitionen; meldet W113 (nil-Global). Erster Lauf: 5 Treffer, harmlos,
in Fahrplan B9. Nach PZ/Bandits-Update `--rebuild`.
Eintrag auch in CLAUDE.md Abschnitt 2 (Tabelle, Zeile 'Werkzeuge auf der Platte').

**Blender 5.2.3 LTS (06.11.2026, Kevin: 'ja lad runter'):** `C:\Users\Kevin\Tools\blender\blender-5.2.3-windows-x64\blender.exe`, ZIP von download.blender.org daneben, SHA256 gegen blender.org gleich (723f08a4...2fb), 405.839.452 Byte, entpackt 1,3 GB. Kein Installer, nichts an PATH oder Windows. Aufruf: `blender.exe --background --factory-startup --python skript.py`, Kopfloser Lauf mit `bpy` und FBX-Export geprueft. Skripte und Ausgaben nur im Scratchpad oder Projektordner, nie im Blender-Ordner. Zweck: Turret-Modell ([[turret-plan]]).
