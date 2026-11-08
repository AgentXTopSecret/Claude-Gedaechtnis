---
name: ungetestet-upload-v3-13-31
description: Was mit dem Zwischen-Upload v3.13.31 (Tierpfleger Stufe 1+2 oeffentlich) UNGESPIELT mitgeht -- Kevins bewusste Entscheidung vom 12.10.; bei Workshop-Meldungen zuerst hier nachsehen
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7fd0ad-7592-45c0-90c1-5c2a73830a30
  modified: 2026-10-12T21:44:51.650Z
---

Kevin laedt den Tierpfleger (Stufe 1+2) als Zwischen-Upload hoch, bevor Stufe 3 fertig ist. Dabei gehen bewusst ungespielt mit
(Kevin 12.10.2026 ~23:05: "die rezepte wollte ich erst testen wenn auch stufe 3 fertig ist weil dann braucht man die erst richtig
ich weiss dadurch koennte ich bugs hochladen aber das risiko geh ich einfach mal ein vllt melden sich ja dann welche"):

- v3.13.25 / v3.13.26: die 13 Rezepte fuer Tier- und Schlachtprodukte (Ruehrei, gekochte Eier, Roast Chicken/Turkey, Cure Meat,
  Smash Bones, Bone Hooks, Spin Yarn/Wool Thread, Forge Shears/Scythe, Mist-Duenger je Art) und Forge Rake; neues Rezeptfeld inheritFood.
- v3.13.24: Koch geht nicht mehr zur eigenen Kachel (T3, MP-Messung offen).
- v3.13.29: Entscheide-Sonde der Minischritte und die zwei Versuchs-Schalter (beide aus) -- T8 offen.
- v3.13.30 / v3.13.31: Schlachtregeln und Vorschau, im Upload gesperrt ("Coming soon"), also fuer Spieler nicht erreichbar.
- Aus der alten Liste: Abendruf der Voegel.

Am 12.10. spaet im Einzelspieler auf v3.13.30 BESTANDEN (Kevin): Forge Rake, Forge Scythe und Forge Shears (Konsole: Zutaten je Charge genau abgebucht, je 1 Stueck abgeliefert), Melken samt Pose ("diesmal war die pose perfekt"), Scheren
("sieht auch gut aus"), Streicheln ("perfekt bei jeden tier").

HOCHGELADEN am 12.10.2026 um 23:40 (v3.13.31, Steam-Groesse = Upload-Ordner auf das Byte, Tag `upload-v3.13.31`). Davor im
Mehrspieler bestanden (Kevin + Testaccount, 23:15-23:30): Laden, Melken ueber den Server samt Milchfass (vier Runden, Buchungen
lueckenlos), gesperrter Schlachtregeln-Knopf. In derselben Sitzung dreimal der Kreis-/Lauf-Fehler gesehen -- der ging mit hoch
und ist der naechste Auftrag ([[kreisbug-nach-upload]]).

**Why:** Die Rezepte braucht man erst richtig mit Stufe 3 (Schlachtprodukte); Kevin nimmt Fehlermeldungen aus dem Workshop in Kauf.

**How to apply:** Kommt eine Workshop-Meldung zu Rezepten, Koch-Wegen oder Tierprodukten: zuerst diese Liste -- die Stelle war nie
gespielt, also nicht "kann nicht sein" sagen. Die Tests T4-T6 und T8 stehen in `_docs/testliste_2026-10-11.md` und laufen mit dem
Stufe-3-Test. Nicht vorher einzeln danach fragen ([[test-nur-noetigste]]). Siehe [[schlachten-coming-soon]], [[uebergabe-12-10]].
