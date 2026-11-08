# -*- coding: utf-8 -*-
"""Sichert Claudes Gedaechtnis JE PROJEKT in das Repository des Projekts und die Anleitungen nach GitHub (privat).

Kevin 08.11.2026: "inklusive unserem gedaechniss damit claude immer weiss was er noch machen soll selbst wenn mal meine
festplatte kaputt waere" und "ja genau so hab ich mir das gedacht das jedes projekt sein gedaechniss da gespeichert hat".

Ziele (sonst NICHTS -- keine Zugangsdaten, keine Gespraechsprotokolle):
  NPC Crew        memory -> C:/Users/Kevin/Zomboid/mods/NPCCrew/_gedaechtnis/      (committet + laedt der Sicherungs-Waechter)
  (alt: TrueCompanions-Gedaechtnis -> NPCCrew/_gedaechtnis/alt_TrueCompanions/)
  Turret          memory -> C:/Users/Kevin/NPCCrew-Nebenprojekte/turret/_gedaechtnis/       (Repo NPCCrew-Turret, Zweig unterlagen)
  Zweihaender     memory -> C:/Users/Kevin/NPCCrew-Nebenprojekte/zweihaender/_gedaechtnis/  (Repo NPCCrew-Zweihaender, Zweig unterlagen)
  Baer            memory -> C:/Users/Kevin/NPCCrew-Nebenprojekte/baer/_gedaechtnis/         (Repo NPCCrew-Baer, sobald der Ordner existiert)
  alle anderen Projekte + global CLAUDE.md + Nebenprojekte-CLAUDE.md -> dieses Repo (Claude-Gedaechtnis)
Ein Projekt-Repo bekommt dabei nur einen Commit, der ausschliesslich `_gedaechtnis/` enthaelt (nie halbe Bau-Staende).
Laeuft als Stop-Hook nach jeder Claude-Antwort oder von Hand:  python sichern.py   |   python sichern.py --pruefen
"""
import os, shutil, subprocess, sys, time, filecmp

HERE = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
HOME = "C:/Users/Kevin"
PROJ = HOME + "/.claude/projects"
NEB = HOME + "/NPCCrew-Nebenprojekte"
NPCCREW = HOME + "/Zomboid/mods/NPCCrew"
LOG = HERE + "/sichern.log"
DRY = "--pruefen" in sys.argv

# Projektordner von Claude Code -> (Ziel-Ordner, Repo-Wurzel, commit_selbst)
MAP = {
    "C--Users-Kevin-Zomboid-mods-NPCCrew": (NPCCREW + "/_gedaechtnis", NPCCREW, False),
    "C--Users-Kevin-Zomboid-mods-TrueCompanions": (NPCCREW + "/_gedaechtnis/alt_TrueCompanions", NPCCREW, False),
    "C--Users-Kevin-NPCCrew-Nebenprojekte-turret": (NEB + "/turret/_gedaechtnis", NEB + "/turret", True),
    "C--Users-Kevin-NPCCrew-Nebenprojekte-zweihaender": (NEB + "/zweihaender/_gedaechtnis", NEB + "/zweihaender", True),
    "C--Users-Kevin-NPCCrew-Nebenprojekte-baer": (NEB + "/baer/_gedaechtnis", NEB + "/baer", True),
}
SINGLE = [
    (HOME + "/.claude/CLAUDE.md", HERE + "/anleitungen/global_CLAUDE.md"),
    (NEB + "/CLAUDE.md", HERE + "/anleitungen/NPCCrew-Nebenprojekte_CLAUDE.md"),
]


def log(msg):
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S ") + msg + "\n")
    except Exception:
        pass


def mirror(src_dir, dst_dir):
    """Spiegelt *.md aus src_dir nach dst_dir; Unterordner von dst_dir bleiben unberuehrt."""
    changed = []
    files = [f for f in os.listdir(src_dir) if f.endswith(".md") and os.path.isfile(os.path.join(src_dir, f))]
    for f in files:
        s, d = os.path.join(src_dir, f), os.path.join(dst_dir, f)
        if not os.path.isfile(d) or not filecmp.cmp(s, d, shallow=False):
            changed.append(d)
            if not DRY:
                os.makedirs(dst_dir, exist_ok=True)
                shutil.copy2(s, d)
    if os.path.isdir(dst_dir):
        for f in os.listdir(dst_dir):
            p = os.path.join(dst_dir, f)
            if os.path.isfile(p) and f.endswith(".md") and f not in files:
                changed.append("(weg) " + p)
                if not DRY:
                    os.remove(p)
    return changed


def git(root, *args):
    return subprocess.run(["git", "-C", root] + list(args), capture_output=True, text=True, timeout=60)


def push_bg(root):
    if not git(root, "remote").stdout.strip():
        return
    flags = 0x00000008 | 0x00000200 if os.name == "nt" else 0  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    with open(LOG, "a", encoding="utf-8") as lf:
        subprocess.Popen(["git", "-C", root, "push", "-q"], stdout=lf, stderr=lf, stdin=subprocess.DEVNULL, creationflags=flags)


def main():
    report = []
    commit_roots = {}
    other = set()
    for p in sorted(os.listdir(PROJ)):
        mem = os.path.join(PROJ, p, "memory")
        if not os.path.isdir(mem) or not any(f.endswith(".md") for f in os.listdir(mem)):
            continue
        if p in MAP:
            dst, root, selbst = MAP[p]
            if not os.path.isdir(root):
                continue  # Projekt noch nicht umgezogen (z. B. baer)
            ch = mirror(mem, dst)
            report += ch
            if ch and selbst:
                commit_roots[root] = os.path.relpath(dst, root).replace("\\", "/")
        else:
            other.add(p)
            ch = mirror(mem, HERE + "/gedaechtnis/" + p)
            report += ch
            if ch:
                commit_roots[HERE] = "."
    # Projekte, die hier nicht (mehr) hingehoeren oder verschwunden sind, aus dem Sammel-Repo entfernen
    gd = HERE + "/gedaechtnis"
    if os.path.isdir(gd):
        for p in os.listdir(gd):
            if p not in other:
                report.append("(weg) " + gd + "/" + p)
                if not DRY:
                    shutil.rmtree(os.path.join(gd, p))
                commit_roots[HERE] = "."
    for s, d in SINGLE:
        if os.path.isfile(s) and (not os.path.isfile(d) or not filecmp.cmp(s, d, shallow=False)):
            report.append(d)
            commit_roots[HERE] = "."
            if not DRY:
                os.makedirs(os.path.dirname(d), exist_ok=True)
                shutil.copy2(s, d)
    if DRY:
        print("\n".join(report) or "nichts zu tun")
        return
    for root, path in commit_roots.items():
        git(root, "add", "-A", "--", path)
        r = git(root, "commit", "-q", "-m", "Gedaechtnis gesichert", "--", path)
        if r.returncode != 0 and "nothing" not in (r.stdout + r.stderr):
            log("commit %s fehlgeschlagen: %s" % (root, (r.stderr or r.stdout).strip()[:300]))
            continue
        log("gesichert: " + root)
        push_bg(root)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # ein Hook darf Claude nie stoeren
        log("Fehler: %r" % (e,))
