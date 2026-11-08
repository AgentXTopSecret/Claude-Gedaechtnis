---
name: uebergabe-konto-02-11
description: 02.11.2026 Kevin switched to his other Claude account (old one at 98 % weekly); UEBERGABE.md in project root is the entry point
metadata:
  node_type: memory
  type: project
  originSessionId: 603c0cc3-65f8-4fca-8839-a46598c470ec
  modified: 2026-11-02T19:42:15.606Z
---

On 02.11.2026 Kevin asked to hand the work over to his other Claude account ("mach alles bereit dafür das mein anderer account weiter machen kann wo wir aufgehört haben"). The old account was at 98 % of its weekly limit (reset 06.11. ~14:00).

**Why:** a new session on the other account cannot resume the old session's workflows or scratchpad, so everything needed was moved into the project folder.

**Update 02.11. ~17:15:** Berater 0.13.3 is installed and pushed (`5f14312`), still untested in the game. Everything Kevin ordered is built; open are only his game tests, lab runs and his decisions (ANLEITUNG chapter 8, questions 17-26). Lab runs only on Kevin's word.

**Update 02.11. ~20:42:** Fair Autopilot series done (5 S / 8 N / 7 U, by survivors 11 : 9, report `stand/labor-autopilot-20-fair.md`), round limit 40 for both series. Opus probe stopped after 1 fight (no count, 100-call cap at round 20, 65 min, 6 vs 1, about like Autopilot; quota is not the problem, time is: report `stand/labor-opus-probe-0211.md`). Any full Opus series only on Kevin's word. The game can only be minimized by script (`stand/spiel-minimieren.py`), by hand it jumps back.

**Update 03.11.:** Berater 0.14.0 (local range display, Kevin plays fights himself) is installed and pushed (`b97dbde`), untested in the game; 0.13.4 was cancelled. The movement bug found then is fixed in 0.14.1.

**Update 04.11.:** Berater 0.14.1 is installed and pushed (`cb4f71e`), untested in the game. It fixes the dog freeze after a kill with "Ziel vorgeben" (our `setForcedOpponent(null)` stored `WeakTableRef(null)`; never call it with null, set `agent.m.ForcedOpponent = null`) and the movement bug (`_int_list` now takes 9 values). Kevin's test: ANLEITUNG list Q.

**How to apply:** Start with `UEBERGABE.md` (project root). Scratchpad leftovers are in `stand/sitzung-603c0cc3/`. Nothing is running. The Begleiter uses whichever account `claude.exe` is logged into, so check `claude auth status`. See [[github-repo]], [[max-10-agents]], [[fragen-deutsch]].
