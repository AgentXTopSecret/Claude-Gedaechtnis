---
name: leerer-chum
description: "30.09. Kevins Entscheidung: leerer Chum (Staerke 0) zaehlt nicht als Koeder + Crew-Rezept macht echten Chum (plus 'Chum fuellen'); erst nach dem Upload v3.12.18 bauen"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-30T19:50:25.346Z
---

Vanilla-Chum aus Sand/Sandsack ist LEER (HungerChange 0, Name UI_Chum_Blank); Staerke kommt erst durch AddBaitToChum. Unser Rezept "Chum" (Production.lua, Sandbag -> 4x Base.Chum) macht nur leeren Chum, und die Fischerin legt Netze damit aus (C5-Test 30.09.: Koederstaerke 0, Chum-Rueckgabe korrekt 0).

Kevin 30.09.: "1 und 2 zusammen, aber erst nach dem Upload heute" -- (1) leerer Chum zaehlt nicht fuer "nur mit Chum", (2) Rezept macht echten Chum (Sandsack + Koeder); dazu "Chum fuellen" (leerer Chum + Koeder), damit alter leerer Chum nicht verloren ist. Nichts loeschen.

**Why:** Netze mit leerem Chum fangen wie ohne Koeder; die Fischerin taeuscht Koeder vor.

**How to apply:** Nach dem Upload v3.12.18 bauen (Details in _docs/offene_arbeit.md "LEERER CHUM"); beide Modi, Pruefer wie ueblich. Siehe [[reusen-pro-zone]].

**Stand 02.10.:** GEBAUT als v3.12.29 (ungespielt). **REVIEW 02.10.: das Why oben war falsch** -- jede Zahl im Netz wuerfelt, auch 0 (N.Roll = Vanilla checkTrap): leerer Chum gab 1/12 je Stunde Koederfang, Chum mit EINEM Koeder (Kraft 1 oder 10) 1/11; spuerbar erst ab Kraft 50/100/200 (1/10, 1/8, 1/4). Krebs aus den Chum-Koedern raus (Zutat Crayfish Stew). Offen fuer Kevin VOR dem Test: Koeder je Chum (Vanilla bis 10), leerer Chum bei Schalter AUS wieder nutzen (1/12)?, welche Koeder (Wurm ist auch Rutenkoeder/Rich Compost).

**NEUE ENTSCHEIDUNG 02.10. (Kevin, nach Pruefer-Fund):** 'Zurueck wie vorher'. Leerer Chum wirkt in Vanilla doch (checkTrap/N.Roll wuerfeln fuer jede Zahl, auch 0: 1 zu 12 je Stunde; 1 Koeder 1 zu 11, erst Kraft 100 = 1 zu 8). Also: leerer Chum zaehlt wieder als Chum, Rezept wieder nur Sandsack -> 4 Chum, 'Fill Chum' faellt weg. Bauen als v3.12.32 NACH Tierpfleger P1 (v3.12.30/.31), Changelog nennt die Ruecknahme von v3.12.29 und warum.

NICHT IN v3.12.32 GEBAUT, WEITER OFFEN (Review 02.10.; Kevin hatte 'das fixxed du aber oder?' gefragt -- ihm sagen, dass es fehlt): Name + Zutatenliste reisen nicht durchs Manifest (Chum mit Wurm kam nach dem Sortieren als 'Fischfutter-Basis' zurueck, Staerke blieb). Name ueber setName (Lua-belegt ISAddItemInRecipe.lua:139/156); Zutatenliste braucht addExtraItem ohne Lua-Beleg -> nur mit Jar-Beleg (Kevins Ja vom 30.09. gilt nach Jar-Pruefung). Gilt fuer alle Evolved-Recipe-Gerichte. Details offene_arbeit 'NAME UND ZUTATENLISTE REISEN NICHT'.

**Stand v3.12.32 (gebaut, ungespielt):** Chum wie vorher. Schalter 'nur mit Chum': AN holt Chum VOR dem Legen (jedes neue Netz gekoedert); AUS legt neue Netze erst blank und holt Chum danach -> erste Kontrolle je neuem Netz ~1,5 statt ~2,5, danach gleich; ohne Chum: AUS legt blank, AN legt keine. Offene Frage an Kevin: soll AUS Chum vor dem Legen holen?

**Stand v3.12.33 (gebaut, ungespielt):** Zutatenliste + Gewuerze reisen jetzt (rec.xi/rec.spc, addExtraItem/setSpices nach Jar-Beleg = Kevins Ja vom 30.09.); der Name reiste schon seit v3.10.45, der eigentliche Namensfehler war setCustomName(true) bei jeder Muenze (Vanilla benennt dann nie mehr um). Widerleger ueber die zwei Setter steht noch aus. Chum aus einem Netz kommt weiter nur mit Restkraft zurueck.
