---
name: koeder-regeln-essensliste
description: "Kevin's feature wish of 28.09.2026 - bait->fish list, allowed/forbidden baits per fishing zone, then a general list of which food the NPCs may eat"
metadata:
  node_type: memory
  type: project
  originSessionId: c3f66696-88e0-4da2-a026-3f8129d53368
  modified: 2026-09-28T10:19:04.699Z
---

Kevin, 28.09.2026: *"wir müssen noch eine liste machen, und gucken welche köder welche fische bringen und dann in der fischerzone eine auswahl welche köder alles erlaubt sind zum fischen und welche verboten sind die sollen dann pro fischerzone gelten die regeln und damit die leute nicht die köder essen brauchen wir danach noch eine liste wo man einstellt welches essen die npc´s essen dürfen allgemein"*

He wants three things, in this order:
1. A list of which bait brings which fish, based on the Vanilla fishing data.
2. A bait selection **per fishing zone**: which baits are allowed and which are forbidden for our fishers.
3. Afterwards, a **general** list of which food the NPCs may eat, so they do not eat the bait.

**Status 28.09., afternoon:**
- Research is done. The list is in `_docs/koeder_fische_liste.md`; the plan, with the critic's corrections and Kevin's decisions so far, is in `_docs/plan_koeder_essen.md`.
- Nothing is built yet.
- Four questions went to Kevin: food baits forbidden by default? never eat inedibles? food bait used portion-wise like Vanilla? crayfish/shrimp/baitfish unlockable in the food list?
- Key finding: our fisher ALREADY honours the bait when choosing the fish (F.EligibleFish/F.PickFish), so nothing needs building for that.
- Known gaps: a useless bait at her level means endless empty casts with rod wear; F.Rebait mounts the first piece, including cooked food, and uses it up whole.

**Kevin's answers of 28.09. afternoon (they win over the plan):**
- **Default:** everything edible may be eaten, including closed cans. The player marks what is forbidden. Worms, insects and other pure bait stay fixed-forbidden.
- **Never eat inedible items** (`isCantEat` without an OpeningRecipe), so closed cans stay edible.
- **Never eat raw food that is dangerous uncooked**, checked per piece (`isbDangerousUncooked and not isCooked`); cooked is fine.
- **Food bait is used up portion-wise**, as in Vanilla.
- **Crayfish, shrimp and baitfish:** the player decides; default edible.
- **Food bait as bait:** his answer to Q1 was about eating. I chose default NOT used as bait (as today), unlockable per zone, and told him.
- **Build order:** food list first, as workflow wjok5txkd (core, UI, 2 refuters), then bait core, then bait UI.

**Kevin's decision on the food list (28.09., with a screenshot):**
- Place: its own button in the Beacon **Settings** tab, in the section **"Player settings (only for you)"** (built in v3.11.50, below the divider).
- Default: everything may be eaten.
- A marked food turns **red** and is never eaten by the NPCs, whether it is in their bag or in a crate.
- The list shows **only food that is currently in our storage system** (Kevin 28.09.: "in der essenliste soll nur essen auftauchen das gerade in unseren lagersystem liegt"). My addition, to confirm with him: foods already marked forbidden stay listed even when none is in storage, so the mark can be undone.

**How to apply:**
- Defaults must keep today's behaviour for existing saves: all baits allowed, food as before.
- Already-held forbidden bait or food must never be lost or doubled. See [[kevins-zwei-rote-linien]].
- Everything must work in SP and MP. See [[both-modes-always]].
- Related: [[reusen-pro-zone]].
