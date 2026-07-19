# NCC Project Boundary

- Workspace scope is only `narrative-character-canon`. Do not open, read for editing intent, or act on files outside this repository unless a task spec explicitly names an external source path.
- The Git repository at `C:\DEV\Narrative\narrative-character-canon` is authoritative. Tracked commits and `.voyage/` state win over any other memory of project facts.
- Other Narrative/Voyage repositories (e.g. `voyage-narrative-engine`) are read-only sources, and only when a task explicitly names them. Never edit them from this workspace.
- Never treat a report, prompt, or implementation task written for another project as a continuation of NCC work. If one appears, stop and warn the user instead of continuing it here.
- Only one write-capable agent operates in this repository at a time. Before any write, confirm no other agent session is mid-task.
- Preserve UTF-8 (no BOM) in every text/JSON file created or edited. Never introduce mojibake.
- Do not infer local filenames from ChatGPT attachment names, chat-pasted filenames, or assumed conventions. Require either an exact existing repository path or a task spec entry carrying a SHA-256 hash.
