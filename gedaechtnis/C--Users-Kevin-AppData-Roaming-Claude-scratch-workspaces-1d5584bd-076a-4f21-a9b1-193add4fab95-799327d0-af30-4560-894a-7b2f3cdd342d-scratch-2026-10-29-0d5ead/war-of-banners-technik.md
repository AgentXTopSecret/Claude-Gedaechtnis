---
name: war-of-banners-technik
description: "Technische Befunde zur War-of-Banners-Demo (UE 5.5, unverschlüsselte Paks, Kampf-Funktionen in C++, UE4SS experimental nötig) – Stand 29.10.2026"
metadata:
  node_type: memory
  type: project
  originSessionId: 41b17b5b-8001-44fb-a552-8f6e81864a7c
  modified: 2026-10-30T18:22:58.333Z
---

Befunde vom 29.10.2026 (Demo-Build 26292740, wird fast wöchentlich gepatcht – vor Nutzung neu prüfen):

- Demo: Steam-App 3912710 (Vollversion 3869940), installiert unter `C:\Program Files (x86)\Steam\steamapps\common\War of Banners Demo`. Spiel-Exe: `WOB\Binaries\Win64\WOB-Win64-Shipping.exe`. Auf D: liegt ein leerer gleichnamiger Ordner.
- Engine: Unreal Engine 5.5 (`++UE5+Release-5.5-CL-40574608`), IoStore (`pakchunk0-Windows.utoc/.ucas/.pak`), **nicht verschlüsselt, nicht signiert**. Kein Anti-Cheat gefunden, Sentry-Plugin für Absturzberichte vorhanden.
- Spielwerte in DataTables unter `WOB/Content/_Data/` (z. B. DT_Mercenary, DT_Trait_*, DT_Training, DT_Equipment, DT_Store, DT_Settlement*, DT_Event*). Liste aller Dateien: `Manifest_UFSFiles_Win64.txt` im Spielordner.
- Kampflogik in C++ mit reflektierten Namen: GetGlobalTurnManager, GetGlobalTileManager, GetActorOnTile, GetIsMyTurn, CalcValidMovePathByStamina, CalculateSkillUseRangeTiles, CalculateSkillAccuracyPreview, CalcBestSkillAndTarget, CalcBestMoveTilePath, TryUseSkillOnBestTarget, EndTurn, ProgressAutoBattle. Klassen ABattleActor, AMercenaryBattleActor, ABattleAIController, UGlobalTurnManager. „TurnTimer“ ist die Zugreihenfolge (Initiative), keine ablaufende Uhr.
- Inventar: gewichtsbasiert (DefaultInventoryWeight, InventoryMaxWeightPerMember, InventoryOverweightPercent, GetPlayerSquadMaxInventoryWeight), Lehen-Lager mit Slots, Stack-Limits.
- Fortschritt: Talente je Attribut (teils verborgen: IsMercenaryTalentHidden), Level-up mit AttributePoint, Trainings-Auswahl je Stufe (GetTrainingCandidatesByTypeAndLevel), Berufe, Traits, Gunst/Favor.
- Grafik: Figuren sind 2D-Papierfiguren aus Einzelteilen (Paper2D, PaperZD-Plugin), kein 3D. Jede Waffe hat Icon `_Art/UI/Icon/Equipment/Weapon/.../T_Icon_*`, Bild in der Hand `_Art/Equipment/Weapon/.../T_Weapon_*` und Sprite `_Art/Sprites/Character/Weapon/.../SP_Equip_Weapon_*`. Rüstung/Helme haben Male/Female-Sprites. Kein passender Leucht-/Aura-Niagara-Effekt im Spiel gefunden.
- Demo-Grenze: 100 Spieltage, angemeldete Playtester 300 (Dev Note #34, Okt. 2026; Freischaltung über Steam-Account, Anmeldung geschlossen). Liegt fest im Programmcode, nicht in einer ini. Kevin fragte am 30.10.2026 nach Umgehung – abgelehnt, weil die Entwickler die Grenze bewusst gesetzt haben. Für Mod-Tests heißt das: pro Durchlauf nur 100 Tage.
- Mod-Lader: UE4SS experimental v3.0.1-1185 **läuft** in der Demo (getestet 30.10.2026, Build 26319068). Reflektiert sind 216 Klassen in `/Script/WOB`. Die KI-Funktionen (CalcBestSkillAndTarget, TryUseSkillOnBestTarget, ProgressAutoBattle, GetActorOnTile, GetIsMyTurn) sind **nicht** aufrufbar, nur Text in der Exe. Aufrufbar: WOBFunctionLibrary.GetGlobal*Manager, Kampfleisten-Knöpfe (BattleHUDWidget.On*Clicked), SetMercenaryOrderingByPlayer (Söldner an Spiel-KI abgeben), IsMercenaryTalentHidden. Details im PLAN im Projektordner.
- Vorbild: Kevins Battle-Brothers-Begleiter (`C:\Users\Kevin\Desktop\Claude Battle Brothers\berater\begleiter\`, Python, Port 47811, `claude.exe -p`).

Gehört zu [[war-of-banners-mod-umfang]].
