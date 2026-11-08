---
name: github-repo
description: "Kevin's mods are in a private GitHub repo AgentXTopSecret/Battle-Brothers-Mods; git lives in the project root with a whitelist .gitignore"
metadata:
  node_type: memory
  type: project
  originSessionId: 603c0cc3-65f8-4fca-8839-a46598c470ec
  modified: 2026-10-28T18:47:58.581Z
---

On 28.10.2026 Kevin asked to upload the mods to GitHub. His choices: both mods in one repo, private, code plus instructions only. He creates the empty repo on github.com himself because `gh` is not installed.

- Repo: `https://github.com/AgentXTopSecret/Battle-Brothers-Mods` (private). It is the remote `origin`, branch `main`. The first commit is 3caedf1 (Berater 0.10.0), pushed on 28.10.2026 and checked: the remote main matches the local HEAD. A push right after Kevin created the repo got "Repository not found"; a retry a few seconds later worked.
- Git runs in the project root. `.gitignore` is a whitelist: only `eigene-mod/`, `berater/`, `fix-uebersetzung/`, `werkzeuge/`, `README.md`, `.gitignore` and `.gitattributes` (`* -text`) are tracked.
- Kept out of the repo:
  - notes: CLAUDE.md, STAND.md, AUFGABEN.md, the WAECHTER files, `stand/`
  - `quellen/` and `downloads/`
  - `dist/` and the ZIPs
  - the Begleiter runtime folders: logs, exporte, plaene, work, labor, testmodus
- The git identity is AgentXTopSecret with a noreply email. Pushing goes through Git Credential Manager (account AgentXTopSecret). Never handle the token.

**Why:** Kevin's notes contain his email and internal plans. The `quellen/` folder holds third-party Legends and translation sources.

**How to apply:**
- Before each commit, run `git ls-files` and grep it for the excluded paths, and grep the files for email or tokens.
- Kevin decided on 28.10.2026 ("Ja, automatisch"): after installing each new version (VA 0.11.0, LS 0.12.0) and after the final docs, commit and push without asking. Then compare `git ls-remote origin main` with `git rev-parse HEAD`.
- If a login window opens, enter nothing and ask Kevin. The steps are in WAECHTER-ANLEITUNG.md, step 3.

Related: [[waechter-aufgabenliste]].
