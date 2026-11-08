---
name: konsole-zuerst-nach-fehlern
description: Bei JEDER Fehlersuche zuerst console.txt nach ERROR/Exception durchsuchen - vor allen eigenen Theorien und vor den eigenen Log-Zeilen.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bdc5780d-84d1-4dce-b9f1-6dca08a415d1
  modified: 2026-08-25T11:15:19.415Z
---

**Erster Schritt jeder Fehlersuche, ohne Ausnahme:** `console.txt` nach `ERROR`, `Exception`
und `OutOfMemory` durchsuchen — **bevor** ich eine Theorie aufstelle und **bevor** ich nach
meinen eigenen Diagnosezeilen greppe.

```
grep -a -n "ERROR\|Exception\|OutOfMemory" console.txt | tail -30
```

**Why:** Am 25.08.2026 habe ich Kevins Einfrieren über **acht Versionen** (v0.91.44–.58) als
Rechenzeit-Problem gejagt: Wächter gedrosselt, Baum-Scan gemerkt, drei Messgeräte gebaut.
Die Antwort stand die ganze Zeit in `console.txt` — **vier `java.lang.OutOfMemoryError`**,
das Spiel lief mit `-Xmx3072m` auf 24 GB RAM. Ich habe gezielt nach `[TC-FOREST]`,
`[TC-PROF]`, `unfroze` und `[TC-TOOL]` gesucht, also nach **meinen eigenen** Zeilen — und
einmal `ERROR` gegrept, die Treffer wegen `f:0` als Startrauschen abgetan.
Kevins Bitte danach: *„das würde einiges erleichtern."*

**How to apply:**
1. **Fremde Fehler zuerst, eigene Zeilen zweitens.** Meine Log-Zeilen sagen nur, was ich
   erwartet habe; ein Java-Stacktrace sagt, was wirklich passiert ist.
2. **Frame-Nummern sind kein Filter.** `f:0` heisst Hauptmenü — aber ein OOM beim Rendern
   trägt auch eine hohe Nummer, und ich habe die Liste zu früh weggeworfen.
3. **Nicht nur nach Zeit suchen.** Ich habe vier Messgeräte auf die Achse *Rechenzeit*
   gelegt; knapp war der *Speicher*. Alle Messungen waren richtig und alle irrelevant.
4. **Zwei Sätze des Autors sind Diagnosen, keine Färbung:** „plötzlich" (= eine Klippe,
   typisch Speicher) und „auch in der Pause" (= schliesst alles aus, was nur bei laufender
   Zeit arbeitet). Siehe [[sonden-muessen-sagen-was-sie-messen]].
