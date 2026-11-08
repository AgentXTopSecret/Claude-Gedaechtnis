---
name: koch-rezepte-entscheidung
description: Kevins Entscheidungen 28.09. zu Koch-Rezepten (gekochte Filets, Koederfisch/Flusskrebs/Frosch, verdorbene Zutaten) -- gebaut wird nach der Tagespruefung, vor/neben der Koederliste
metadata:
  type: project
---
Kevin, 28.09. (AskUserQuestion):
- "Fillet Fish" gibt direkt GEKOCHTE Filets (Rezeptfeld cooked = true; setCooked-Ausnahme damit erweitert, steht in CLAUDE.md §3).
- Neue Rezepte: Koederfisch -> Fried Fish; Flusskrebs und Frosch -> Eintopf-Schuessel (StewBowl).
- Ergebnisse erben das Alter der Zutaten (wie Vanilla InheritFoodAge), UND verdorbene Zutaten fasst der Koch gar nicht an
  ("bringt ja eh nichts"). Verbranntes ebenso (meine Ergaenzung, Kevin gesagt).

**Why:** Kevin will, dass der Koch die rohe Ware der Crew essbar macht; v3.11.69 sperrt Verdorbenes fuers Essen, und
die Produktion machte bisher aus verdorbenem Fisch frische Filets (Loch).
**How to apply:** Bestandsbegriff "brauchbare Zutat" muss durch ALLE Leser (StockOf/PickNext/SupplyNeed/removeItem/
Hauler-Griff) -- Lehre v3.9.97/.98 (Werkzeug-Laufband). Sushi nimmt dann gekochte Filets (Vanilla: roh) -- benennen.
Siehe [[koeder-regeln-essensliste]] fuer die Koederliste, die danach kommt.
