---
name: workshop-updates-nur-auf-ansage
description: "Workshop-Upload-Ordner darf ich nach jeder Version spiegeln -- HOCHLADEN zu Steam tut nur Kevin selbst im Spiel. Der Ordner parkt zwischen zwei Uploads AUSSERHALB von Zomboid/Workshop (backups/Workshop-Upload), weil das Spiel ihn sonst statt des Entwicklungsstands laedt."
metadata:
  node_type: memory
  type: feedback
  originSessionId: f31a6c60-393f-4384-a887-2468f35b6ab7
  modified: 2026-09-12T12:05:27.271Z
---

Kevin (12.09.2026, zwei Ansagen): erst *"ich will keine updates nach jeder version ... das will
ich selbst entscheiden wann ich updates auf steam veroeffentliche"*, dann die Klarstellung
*"du kannst die workshop mod ruhig immer aktualisieren nach jeder veraenderung ich will nur
nicht das du sie selbst staendig hochlaedst fuer alle das soll nur ich selbst tun"*.

**Why:** ein Steam-Update zwingt jeden Spieler und Server zum Neustart -- die Kadenz ist seine
Entscheidung. Der lokale Upload-Ordner ist dagegen nur Vorbereitung; den aktuell zu halten
stoert niemanden. Hochladen geht ohnehin nur im Spiel (Hauptmenue > Workshop), und das tut
er. **Gemessen (12.09.):** das Spiel -- Client UND dedizierter Server -- laedt jeden Ordner
`Zomboid\Workshop\*\Contents\mods\*` als Mod und die Kopie dort GEWANN gegen
`Zomboid\mods\NPCCrew` (Server lud v3.9.30 statt v3.9.31; Beweis: `[BanditsNPC] vX loaded
OK`). Kevin will immer den Entwicklungsstand spielen ("Ordner beiseite legen", seine Wahl).

**How to apply:** nach jeder Version `python _docs\tools\workshop_sync.py` -- spiegelt in den
GEPARKTEN Ordner `Zomboid\backups\Workshop-Upload\NPCCrew` (fuers Spiel unsichtbar, `id=3800132623`
bleibt stehen). Will Kevin veroeffentlichen: `workshop_sync.py stage` (legt ihn nach
`Zomboid\Workshop`, dort sieht ihn das Spiel unter Upload), er laedt hoch, danach SOFORT
`workshop_sync.py park`. Nach jedem Start die `loaded OK`-Zeile lesen. Kevin darf sein eigenes
Item nicht abonnieren. Nie selbst etwas zu Steam schicken. Siehe auch [[docs-stay-on-disk]].

LEHRE 31.10.: `workshop_sync.py stage` spiegelt VORHER den aktuellen Stand aus mods/NPCCrew -- waehrend ein Bau-Workflow laeuft, kopiert es
halbfertige Dateien in den Testordner (passiert: 18 Dateien v3.14.18). Zum Testen eines aelteren Stands neben einem laufenden Bau den Testordner
aus einem git-Tag fuellen (scratchpad restage.py-Form: git show <tag>:<datei> fuer 42/ und common/, Ueberzaehliges loeschen, 0 Abweichungen pruefen).
