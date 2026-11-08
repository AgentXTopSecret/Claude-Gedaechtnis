# -*- coding: utf-8 -*-
"""Sichert Claudes Gedaechtnis (Notizen aller Projekte) und die Anleitungen nach GitHub (privat).

Kevin 08.11.2026: "inklusive unserem gedaechniss damit claude immer weiss was er noch machen soll selbst wenn mal
meine festplatte kaputt waere". Laeuft als Stop-Hook von Claude Code nach jeder Antwort (schnell: nur kopieren und
lokal committen; das Hochladen laeuft losgeloest im Hintergrund, damit nichts wartet).

Was gesichert wird (sonst NICHTS -- keine Zugangsdaten, keine Gespraechsprotokolle):
  C:/Users/Kevin/.claude/CLAUDE.md                         -> anleitungen/global_CLAUDE.md
  C:/Users/Kevin/NPCCrew-Nebenprojekte/CLAUDE.md          -> anleitungen/NPCCrew-Nebenprojekte_CLAUDE.md
  C:/Users/Kevin/.claude/projects/<projekt>/memory/*.md    -> gedaechtnis/<projekt>/*.md   (nur Projekte mit Notizen)
Die Anleitung von NPC Crew liegt schon in dessen eigenem Repository.
Zurueckspielen: die Dateien von Hand an ihre Orte kopieren (siehe README.md).
Aufruf von Hand:  python sichern.py           (kopieren, committen, hochladen)
                  python sichern.py --pruefen (nur zeigen, was sich aendern wuerde)
"""
import os, shutil, subprocess, sys, time, filecmp

HERE = os.path.dirname(os.path.abspath(__file__))
HOME = r"C:/Users/Kevin"
CLAUDE = HOME + "/.claude"
SINGLE = [
    (CLAUDE + "/CLAUDE.md", "anleitungen/global_CLAUDE.md"),
    (HOME + "/NPCCrew-Nebenprojekte/CLAUDE.md", "anleitungen/NPCCrew-Nebenprojekte_CLAUDE.md"),
]
LOG = os.path.join(HERE, "sichern.log")
DRY = "--pruefen" in sys.argv


def log(msg):
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S ") + msg + "\n")
    except Exception:
        pass


def sync():
    changed = []
    for src, rel in SINGLE:
        dst = os.path.join(HERE, rel)
        if os.path.isfile(src) and (not os.path.isfile(dst) or not filecmp.cmp(src, dst, shallow=False)):
            changed.append(rel)
            if not DRY:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
    proj_root = os.path.join(CLAUDE, "projects")
    keep = set()
    for p in sorted(os.listdir(proj_root)):
        mem = os.path.join(proj_root, p, "memory")
        if not os.path.isdir(mem):
            continue
        files = [f for f in os.listdir(mem) if f.endswith(".md") and os.path.isfile(os.path.join(mem, f))]
        if not files:
            continue
        for f in files:
            rel = "gedaechtnis/" + p + "/" + f
            keep.add(rel)
            src = os.path.join(mem, f)
            dst = os.path.join(HERE, rel)
            if not os.path.isfile(dst) or not filecmp.cmp(src, dst, shallow=False):
                changed.append(rel)
                if not DRY:
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.copy2(src, dst)
    gd = os.path.join(HERE, "gedaechtnis")
    if os.path.isdir(gd):
        for root, _, files in os.walk(gd):
            for f in files:
                rel = os.path.relpath(os.path.join(root, f), HERE).replace("\\", "/")
                if rel not in keep:
                    changed.append("(weg) " + rel)
                    if not DRY:
                        os.remove(os.path.join(root, f))
    return changed


def git(*args):
    return subprocess.run(["git", "-C", HERE] + list(args), capture_output=True, text=True, timeout=60)


def main():
    changed = sync()
    if DRY:
        print("\n".join(changed) or "nichts zu tun")
        return
    if not changed:
        return
    git("add", "-A")
    r = git("commit", "-q", "-m", "Gedaechtnis gesichert: %d Datei(en)" % len(changed))
    if r.returncode != 0:
        log("commit fehlgeschlagen: " + (r.stderr or r.stdout).strip()[:300])
        return
    log("gesichert: %d Datei(en)" % len(changed))
    # Hochladen losgeloest, damit Claude nicht wartet. Ohne Remote passiert nichts.
    if git("remote").stdout.strip():
        flags = 0x00000008 | 0x00000200 if os.name == "nt" else 0  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
        with open(LOG, "a", encoding="utf-8") as lf:
            subprocess.Popen(["git", "-C", HERE, "push", "-q", "origin", "main"], stdout=lf, stderr=lf,
                             stdin=subprocess.DEVNULL, creationflags=flags)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # ein Hook darf Claude nie stoeren
        log("Fehler: %r" % (e,))
