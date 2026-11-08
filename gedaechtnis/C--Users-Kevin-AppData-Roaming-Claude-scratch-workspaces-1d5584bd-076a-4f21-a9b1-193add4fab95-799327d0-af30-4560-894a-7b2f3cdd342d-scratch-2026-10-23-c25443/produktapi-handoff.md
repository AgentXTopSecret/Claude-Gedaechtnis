---
name: produktapi-handoff
description: ProduktApi (.NET 10 REST API + SQL Server) is built for another person and is handed over as a ZIP with a German README
metadata:
  node_type: memory
  type: project
  originSessionId: 90bc59e6-c074-48ba-a483-209e9a8f239b
  modified: 2026-10-23T15:17:01.913Z
---

The ProduktApi project (ASP.NET Core .NET 10, EF Core 10, SQL Server/LocalDB, started 2026-10-23) is not for the user themself: it gets forwarded to another person who opens it in Visual Studio 2026.
It looks like a numbered training assignment; task 1 (2026-10-23) was "REST API in eine .NET 10 MAUI-App einbinden" → solution now also has ProduktApp (MAUI, CommunityToolkit.Mvvm, Windows + Android). Project lives in C:\Users\Kevin\Desktop\Claude Api Projekt (M), ZIP = ProduktApi.zip there. Task 1 finished 2026-10-23: two review rounds, all confirmed findings fixed, final ZIP handed over (API 48/48, app client 24/24, Windows UI checks passed; Android only built, not run – no emulator image on this PC).

**Why:** The recipient only gets the ZIP, so everything they need must be inside it and explained in the German README.md.
**How to apply:** Keep the ZIP free of bin/obj/.vs and personal data, rebuild it after every change, and keep README.md in sync with the code. Since 2026-10-23 LocalDB is on the PC (see [[user-tools-folder]]); end-to-end tests run against throwaway DBs named ProduktApiTest_*, never against ProduktApiDb.
