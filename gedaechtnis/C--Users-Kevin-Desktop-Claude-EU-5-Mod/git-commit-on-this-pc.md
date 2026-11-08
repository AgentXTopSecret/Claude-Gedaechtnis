---
name: git-commit-on-this-pc
description: How to pass multi-line commit messages to git on this Windows PC without breaking (use Bash stdin, not PowerShell here-strings)
metadata:
  type: reference
---

On this PC, `git commit -m @'…'@` from Windows PowerShell 5.1 silently breaks on double quotes inside the message (part of it becomes a pathspec, nothing is committed), and `git commit -F <scratchpad file>` fails with "Filename too long" because the session scratchpad path exceeds git's 260-character limit. What works: write the message to a file, then in the Bash tool run `cat <file> | git commit -F -`. Always check `git log --oneline -1` after committing. PowerShell also reports git's normal stderr output (e.g. "Switched to branch", push progress) as a red NativeCommandError, which is harmless. Related: [[eu5-advisor-repo]], [[push-after-each-step]].
