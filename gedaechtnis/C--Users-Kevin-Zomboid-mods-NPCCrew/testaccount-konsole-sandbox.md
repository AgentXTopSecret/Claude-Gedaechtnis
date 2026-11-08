---
name: testaccount-konsole-sandbox
description: Kevins zweiter Client (Testaccount) laeuft in Sandboxie; seine console.txt liegt unter C:\Sandbox\Kevin\steam2\user\current\Zomboid\ und ist lesbar -- aber NUR ueber den absoluten Pfad, nie per cd hinein (Sandboxie zwingt jeden Prozess mit Arbeitsverzeichnis in der Box in die Box).
metadata: 
  node_type: memory
  type: reference
  originSessionId: f31a6c60-393f-4384-a887-2468f35b6ab7
  modified: 2026-09-11T11:34:55.801Z
---

Der **Testaccount** (zweiter PZ-Client, Prozess `ProjectZomboid64.exe ... -debug`, Besitzer
"ANONYMOUS-ANMELDUNG") laeuft in einer **Sandboxie-Box** `steam2`. Seine Dateien liegen unter
`C:\Sandbox\Kevin\steam2\user\current\Zomboid\` — insbesondere `console.txt` dort.

**Why:** Bis zum 11.09. galt "der zweite Client schreibt nirgends" — er schrieb nur woanders.
Beide Konsolen benutzen dieselbe Uhr (`st:` in Millisekunden), die Zeilen beider Rechner
lassen sich zur selben Millisekunde nebeneinanderlegen. Genau so wurden v3.9.6 und v3.9.8
gefunden.

**How to apply:** Bei jeder Mehrspieler-Diagnose BEIDE Konsolen lesen:
`C:\Users\Kevin\Zomboid\console.txt` (Hauptclient `admin`) und die Sandbox-Konsole
(`Testaccount`). Den Sandbox-Prozess nie beenden — den startet und schliesst Kevin selbst.
Siehe auch [[logout-parken-offen]].

**NIE MIT cd IN DEN SANDBOX-ORDNER (11.09., gemessen).** Sandboxie zwingt jeden Prozess, dessen
Arbeitsverzeichnis unter `C:\Sandbox\Kevin\steam2\` liegt, in die Box -- Beweis: zwei identische
`cmd.exe`, eines mit CWD in der Box (`sandboxed = True`), eines mit CWD in `Zomboid` (`False`);
keine ForceProcess/ForceFolder-Regel in `Sandboxie.ini`. Folgen fuer meine Shell: die Kinder
kommen nicht mehr an die Pipes von `claude.exe` (Sandboxie-Meldung SBIE2112 fuer `bash.exe`/
`grep.exe`), Forks brechen ab (`fork_fixup: Win32 error 2`), und Schreibzugriffe ausserhalb von
`OpenFilePath=C:\Users\Kevin\Zomboid\mods\` wuerden in die Box-Kopie umgeleitet. Das
Bash-Werkzeug behaelt sein Arbeitsverzeichnis ueber Aufrufe hinweg -- ein einziges `cd` vergiftet
also alle folgenden Aufrufe. Also: `tail`/`grep` immer mit dem vollen Pfad, nie `cd`.
