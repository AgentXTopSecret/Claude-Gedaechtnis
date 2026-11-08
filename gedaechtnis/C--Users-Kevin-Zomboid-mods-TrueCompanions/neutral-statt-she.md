---
name: neutral-statt-she
description: In Texten ueber Companions they/them benutzen, nie she/her als Vorgabe - Kevins Companions haben verschiedene Geschlechter.
metadata:
  type: feedback
---

**Nie "she" als Vorgabe fuer eine Companion.** Am 26.08.2026 stand auf demselben Bildschirm
`Male Wary` und *"She is out working the forest now."* Kevins Worte: *"du benutz fast immer
'she' als waere es eine frau dabei stimmt das ja garnicht ;D gibs da kein neutrales wort
fuer? das waere stimmiger."*

**Why:** Companions haben ein echtes Geschlecht (`brain.female`), und das UI spricht ueber
**irgendeine** von ihnen. Eine feste Form ist damit in der Haelfte der Faelle schlicht falsch.
Es waren 33 Schluessel in `UI.json` und 81 Zeichenketten in 18 Lua-Dateien.

**How to apply:**
1. **Englisch: singular they/them/their.** Verb dann im Plural — *they are*, *they take*,
   *they work*, nicht *they is/takes/works*.
2. **Die Hintergrund-Zeilen sind die Ausnahme.** `UI_BN_Bs_*_f` / `_m` und die Pronomen-Karte
   in `BanditsNPCBackstory.lua` waehlen ueber `brain.female` — dort ist das Geschlecht
   BEKANNT und die gegenderte Form richtig. Neutral gilt nur, wo ueber eine beliebige
   Companion geredet wird.
3. **Lua-Rueckfalltexte immer mitziehen.** Wer keine Sprachdatei hat, liest die; JSON und
   Lua duerfen nicht auseinanderlaufen.
4. **KEIN Blanko-Ersatz.** Zweimal an einem Tag Schaden angerichtet: englisches "her" ist
   Besitz UND Objekt (*her crate* -> their, *walk to her* -> **them**), und der Korrektor
   dagegen war zu breit und machte aus *on her way* ein *on them way*. Danach immer nach
   `them <Substantiv>` und `they <Verb>s` scannen. Siehe [[agenten-sparsam-einsetzen]] —
   selbst lesen, nicht blind ersetzen.
5. **PTBR und RU koennen das nicht.** Kein singular they, und Pronomen zeigen dort oft auf
   feminine SACHEN statt auf die Companion (*parte dela* = Teil der Flaeche). Dort nur pro
   Zeichenkette entscheiden oder das Pronomen umgehen — nie pauschal.
