---
name: user-tools-folder
description: "Portable dev tools the user keeps in C:\\Users\\Kevin\\Tools (JDK 25, Vineflower, luacheck, Lua 5.1, AssetRipper) and what they suit"
metadata:
  node_type: memory
  type: reference
  originSessionId: 90bc59e6-c074-48ba-a483-209e9a8f239b
  modified: 2026-10-23T13:24:29.935Z
---

C:\Users\Kevin\Tools holds portable, user-checked tools, each in its own subfolder (none on PATH):
- `jdk25` – Eclipse Temurin JDK 25 (java, javap)
- `vineflower` – Vineflower 1.12.0 Java decompiler
- `luacheck` – luacheck 1.2.0 Lua linter
- `lua51` – Lua 5.1.5 interpreter
- `assetripper` – AssetRipper (Unity asset extraction; seen 2026-10-23, not described by the user)

They fit the user's game-modding work (Project Zomboid mods are Lua on a Java engine). Not useful for .NET / C# work.
New tools go here too, following [[tool-download-policy]].

State of this PC on 2026-10-23: .NET SDK 8.0.426 + 10.0.402 and Visual Studio Community 2026 (18.11.1) installed; no full SQL Server, no Docker.
LocalDB (SQL Server 2025 LocalDB 17.0.4025.3) was added on 2026-10-23 with the user's "bestätigt", via the VS Installer component `Microsoft.VisualStudio.Component.SQL.LocalDB.Runtime` (SHA-256 and Microsoft signature verified). It lives in `C:\Program Files\Microsoft SQL Server\170\Tools\Binn\` (SqlLocalDB.exe, on the system PATH), instance `(localdb)\MSSQLLocalDB`; used to test SQL Server code. Side effect: it also installed the auto-start service "SQL Server VSS Writer". Remove via VS Installer.
