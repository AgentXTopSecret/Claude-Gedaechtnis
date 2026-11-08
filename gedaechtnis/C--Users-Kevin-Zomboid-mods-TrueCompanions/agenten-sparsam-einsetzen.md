---
name: agenten-sparsam-einsetzen
description: HARTE REGEL - ueber 10 Agenten immer vorher fragen. Zweimal ist Kevins 5-Stunden-Fenster daran fast komplett draufgegangen.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bdc5780d-84d1-4dce-b9f1-6dca08a415d1
  modified: 2026-08-26T15:39:43.754Z
---

**Die Regel (26.08., wortwörtlich): „beim nächsten mal fragst du aber wenn du mehr als 10
benutzen willst merk dir das."**

Also: **bis 10 Agenten einfach machen. Ab 11 vorher fragen** — mit der Zahl und dem Grund,
nicht als vage Ankündigung. Kein „ich starte mal einen größeren Workflow".

**Vorgeschichte, zweimal derselbe Schaden:**
- 1. Mal: 130 Agenten für 5 Funde — *"das alleine hat 42% meines 5std fenster bei max 5x
  gekostet das war krank"*. Daraufhin: *"benutz nur soviele wie auch wirklich nötig sind"*
  und *"kannst du mir vorschlagen wenn du denkst das man mehr agenten benötigt"*.
- 2. Mal, trotz dieser Zusage: ein Workflow war auf „unter 15" geplant und verbrauchte **83**
  (8,3 Mio Token) — *"damit war meine 5x fast komplett weg in einen rutsch"*.

**Warum es zweimal passiert ist — die Mechanik, nicht Nachlässigkeit:** ein `parallel`
**innerhalb** einer `pipeline`-Stufe multipliziert sich mit der Fundzahl. Vier Suchrichtungen
× beliebig viele Funde × zwei Prüfer ist ein **Produkt**, keine Summe, und die Fundzahl steht
beim Schreiben des Skripts noch gar nicht fest. Eine geplante Zahl ist deshalb wertlos, wenn
sie nicht als Produkt gerechnet und **gedeckelt** wurde.

**Why:** Das Fenster ist eine harte, geteilte Ressource — eine Überschreitung kostet ihn
Stunden Arbeitszeit, nicht Geld. Und die Zusage nach dem ersten Mal habe ich quittiert und
dann gebrochen; das wiegt schwerer als der erste Verstoß.

**WAS SICH BEWAEHRT HAT (27.08., 12 Agenten):** die Form entscheidet, nicht die Zahl. Ein
Lauf mit **fester Agentenzahl, eine Suchrichtung je Agent, keine Verschachtelung** und einem
klar begrenzten Ziel (frisch geschriebener, ungespielter Code) hat fuer 1,8 Mio Token rund
zehn echte Fehler gefunden — darunter zwei, die Kevins Kisten leergeraeumt haetten, und
mehrere, die beim ersten Testlauf zugeschlagen haetten. Das war es wert, und er hat es
vorher ausdruecklich freigegeben.

Zum Vergleich: der 83-Agenten-Lauf am Vortag kostete 8,3 Mio Token und fand *einen* echten
Fehler, den ich vorher schon selbst im Log hatte. Unterschied: dort haengte eine Pruefstufe
an einer offenen Fundliste.

**Und die Rohzahl luegt:** 89 Befunde waren etwa zehn verschiedene Fehler — allein zehn
Meldungen beschrieben dieselbe Ursache aus verschiedenen Blickwinkeln. Vor dem Berichten
zusammenfassen, sonst klingt es nach mehr als es ist.

**How to apply:** Agentenzahl vor dem Start als **Produkt aller Fächerungen** ausrechnen und
hinschreiben. Fundlisten hart deckeln (`.slice(0, 3)`), bevor eine teure Prüfstufe darauf
läuft. Über 10 → fragen, mit Zahl und Nutzen. Er sagt zu, wenn der Grund stimmt — der
Workflow am 26.08. hat einen echten, munitionsvernichtenden Fehler gefunden. Und wenn es
trotzdem entgleist: **selbst ansprechen, bevor er es merkt.** Vorher gilt ohnehin
[[konsole-zuerst-nach-fehlern]]: erst billig selbst lesen, dann fächern.
