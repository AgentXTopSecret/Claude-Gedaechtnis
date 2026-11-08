---
name: waechter-aufgabenliste
description: "Kevin's hourly \"Wächter\" that works through AUFGABEN.md until empty and resumes broken runs; how to resume or recreate it"
metadata:
  node_type: memory
  type: project
  originSessionId: 603c0cc3-65f8-4fca-8839-a46598c470ec
  modified: 2026-10-30T19:35:58.313Z
---

A watcher (CronCreate job) works through `AUFGABEN.md` top-down until "Offen" is empty. History:
- 27.10.2026 02:33: first watcher, job e2ef9782.
- 27.10. ~11:20: Kevin cancelled it.
- 27.10. ~23:12: Kevin had it recreated: "okay weiter machen und mach den wächter an bei abbruch 5std limit etc automatisch weiter arbeiten". This is job 597fc86f, hourly at :47, in session 603c0cc3.
- 28.10. ~04:15: Kevin paused everything ("erstmal Pause bis ich sage du darfst weiter arbeiten"), and job 597fc86f was deleted. Recreate it only when Kevin says to continue.
- 30.10. ~15:10: Kevin said "weiter". The new job is 0e345b91, hourly at :47, in session 603c0cc3, and expires on 06.11. VA started as run wf_71efec18-182; LS and the docs follow.
- 30.10. ~20:46: VA (0.11.0), LS (0.12.0) and the final docs (`berater/ANLEITUNG.md`) are done, installed and pushed. "Offen" is empty, and jobs 0e345b91 and cb369658 were deleted. No watcher is active now. Recreate one only if Kevin gives new tasks and asks for it.

Per-step state goes in `WAECHTER-STATUS.md`. The full rules and the exact cron prompt are in `WAECHTER-ANLEITUNG.md`. Those rules include:
- resuming interrupted runs (reset half-finished build files first, then resume the script unchanged)
- installing 0.9.0 after TL, 0.10.0 after GS, 0.11.0 after VA and 0.12.0 after LS, each only after our own check and only if the game is closed (Kevin's yes, 27.–28.10.)

**Why:** Kevin wants the list finished even if runs break (5h limit, API errors, power loss). Cron jobs die when the app or Claude exits, and after 7 days.

**How to apply:**
- If the app was restarted, the job is gone. Recreate it from `WAECHTER-ANLEITUNG.md` when Kevin says "weiter" or asks for the watcher.
- Resume a broken run when the 5h window is under 75 % and the week is under 97 %. Start a new task only when the 5h window is under 50 %.
- Max 10 agents per workflow.
- Never run the real claude.exe without Kevin's word.

Related: [[checkpoint-before-heavy-steps]], [[max-10-agents]], [[github-repo]].
