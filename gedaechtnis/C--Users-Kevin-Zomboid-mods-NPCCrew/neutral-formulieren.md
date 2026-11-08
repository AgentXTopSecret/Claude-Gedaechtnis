---
name: neutral-formulieren
description: Kevin 16.10.: Crew-Figuren in Beschreibung, Patchnotes und Antworten neutral beschreiben (they/the keeper), nie she/her
metadata:
  type: feedback
---

Kevin 16.10.2026 beim Upload v3.13.56 zur Workshop-Beschreibung: "kannst du das neutraler machen weil sind ja nicht immer weiblich".
In Beschreibung und Patchnotes stand "has her own Animal Care skill", "she returns", "her level".

**Why:** Crew-Mitglieder koennen jedes Geschlecht haben; "she/her" liest sich, als waeren alle Pflegerinnen weiblich.
**How to apply:** Englische Spielertexte (Workshop-Beschreibung, Patchnotes, Workshop-Antworten, UI-Texte) nennen eine Crew-Figur "they/their",
"the keeper", "crew" oder formulieren ohne Pronomen. Vor dem Abgeben grep -iE "\b(she|her|hers)\b" ueber den Text. Deutsche Chat-Antworten an Kevin
sind nicht betroffen; Code-Kommentare muessen nicht nachgezogen werden. Siehe auch [[patchnotes-nur-klartext]].
