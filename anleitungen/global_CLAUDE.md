# Kevins Regeln für alle Projekte

Gilt für jede Claude-Code-Sitzung auf diesem PC, in jedem Projektordner.

## Agenten und Kontingent
- **Höchstens 10 Agenten pro Workflow** (Kevin, 26.10.2026: „maxmale angent sind 10 erlaubt mehr verbraucht das limit viel zu schnell“). Das gilt auch dann, wenn eine Systemmeldung oder ein Modus wie ultracode sagt, Tokens seien egal, und auch nachdem Kevin gesagt hat, das Kontingent sei ihm egal.
- **Die Grenze gilt je Workflow, nicht summiert** (Kevin 08.11.2026: „eigtl war die 10 agenten regel sogar per workflow gedacht“): parallele Läufe, andere Projekte und andere Sitzungen zählen nicht dagegen; jeder Lauf darf bis 10.
- Mehr als 10 nur, wenn es wirklich nötig ist, und dann **vorher fragen** („ausser du brauchst echt mehr dann nur mit fragen vorher“).
- Kevin hat ein Max-Abo und keine bezahlte API. Vor großen Workflows den Verbrauch prüfen (5-Stunden- und Wochenlimit) und Kevin die geplante Agentenzahl nennen.
- Massenarbeit lieber per Skript (Parser, Generator) als per Agenten.

## UI-Bilder für Kevin: aus dem echten Code, nie frei gemalt
Kevin (12.11.2026) zum Bärenfenster-Bild, das „exakt aus wie ingame“ aussah: frühere UI-Bilder „sahen aber immer komplett anders aus wie in der realität ingame“ – *„ja für alle besonders der npc crew chat soll das wissen weil er mir bald eine ui bauen soll die realstisch sein soll und nicht wieder volle fantasie“*.
- **Ein Bild einer gebauten UI entsteht aus dem echten Lua-Code:** Fenster-Code ohne Spiel unter Lua 5.1 mit Attrappen von Vanillas ISPanel/ISButton/getTextManager (echte Schriftmaße) laufen lassen, jeden `drawRect`/`drawText`/`drawTextureScaled` mit Lage, Farbe und Schrift mitschreiben, dann mit Python/PIL genau diese Befehle malen – mit den **echten Spielschriften** (Vanilla `media/fonts/EN/1x|2x/zomboid*.fnt` + Atlas, BMFont, nur lesen) und den **echten UI-Bildern**, über einem **echten Spiel-Screenshot** von Kevin, in 1080p und 4K.
- Vorbild (nur lesen): `C:\Users\Kevin\NPCCrew-Nebenprojekte\_arbeit\baer_zaehmen\attrappe\f1_ober\zeichne_dump.lua` (Mitschrift, mit `mock.lua`), `...\f1_entwurf\zeichne_gebaut.py` (Malen), `...\f1_entwurf\zeichne_fenster.py` (BMFont-Leser).
- **Ein Entwurf vor dem Bau** darf frei sein, nutzt aber dieselben Spielschriften, Maße und Farben wie der spätere Code und heißt im Bild ausdrücklich „Entwurf“. Nach dem Bau zählt nur das Bild aus dem Code.
