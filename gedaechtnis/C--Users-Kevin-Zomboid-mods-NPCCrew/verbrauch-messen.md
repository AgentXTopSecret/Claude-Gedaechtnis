---
name: verbrauch-messen
description: "Kevins Wunsch 28.09. -- Token-/Agentenverbrauch bis 100 % Wochenlimit mitschreiben: get_usage lesen + `_docs/tools/usage.py --snap W F RESET` bei Sitzungsbeginn, vor/nach grossen Workflows und auf Nachfrage."
metadata:
  node_type: memory
  type: feedback
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-28T17:09:15.335Z
---

Kevin will wissen, wie viele Tokens und Agenten bis 100 % Wochenlimit gebraucht werden. Das Limit selbst kann ich
NICHT aendern (auch nicht auf 0 setzen -- er hat am 28.09. danach gefragt; es liegt bei Anthropic, Reset Fr 15:00
Ortszeit laut get_usage), nur lesen: Werkzeug `mcp__ccd_session_mgmt__get_usage` (5h, Woche, Reset-Zeit).

**Why:** Kevin, 28.09.: "ein tool ... der den tokens verbrauch trackt ... und wie viel agenten gelaufen sind, sodass ich
weiss wie viele agenten und token ich verbraucht hatte bis ich bei 100% wochenlimit angekommen bin".

**How to apply:** Messpunkt = get_usage lesen, dann
`python C:/Users/Kevin/Zomboid/mods/NPCCrew/_docs/tools/usage.py --snap <Woche%> <5h%> <resetsAt>` -- bei Sitzungsbeginn,
vor und nach jedem Workflow mit mehr als ~5 Agenten, und wenn Kevin fragt. Bericht: `usage.py` (Woche) oder
`usage.py --since DATUM`; er rechnet aus den Messpunkten "je 1 % Wochenlimit". Grenze: Agenten-Protokolle speichern die
AUSGABE nur vom Antwortanfang (zu klein) -- Anzahl, Cache-Schreiben/-Lesen der Agenten sind vollstaendig. Erster Messpunkt:
28.09. 19:09, Woche 23 %, 384 Agenten seit Fr 25.09. 15:00. Siehe [[bugwatch-bei-jedem-test]].

**05.10. Kevin:** "wenns vorher verbraucht ist warten wir halt" -- ein Wochenlimit, das vor dem Reset leer ist, ist fuer ihn in Ordnung. Also NICHT an Pruefern oder Gruendlichkeit sparen, um bis zum Reset zu kommen ([[zuverlaessigkeit-vor-tempo]]); nur Rechnung offen sagen und ueber 10 Agenten weiter vorher fragen.

**12.10. zweites Konto (Max, neu):** zwei Workflows GLEICHZEITIG (6 + 9 Agenten, zusammen 8,3 Mio Subagenten-Tokens, rund 1.200
Werkzeugaufrufe) haben das 5-Stunden-Fenster dieses Kontos in unter einer Stunde geleert -- sieben der fuenfzehn Agenten starben mit
"You've hit your session limit", die Arbeit stand bis 21:30. Faustregel fuer dieses Konto: ein lesender Recherche-/Pruef-Agent kostet
rund 0,8 Mio Tokens, das Fenster traegt etwa ZEHN davon. Also Workflows NACHEINANDER, je Fenster hoechstens etwa acht Agenten einplanen,
und Kevin die Rechnung vorher sagen. Fortsetzen geht ohne Verlust: `Workflow({scriptPath, resumeFromRunId})` spielt fertige Agenten aus
dem Zwischenspeicher ab, solange ihr Prompt bytegleich bleibt -- neue Vorgaben deshalb NUR in die Prompts der noch offenen Stufen
schreiben (eigene Konstante), nie in den gemeinsamen Vorspann. Das Skript muss dazu in einem lesbaren Ordner liegen (Scratchpad).
