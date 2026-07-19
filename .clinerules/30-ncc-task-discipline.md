# NCC Task Discipline

- One task equals one phase. Discovery, import, metadata closeout, verification, staging, commit, and push are separate tasks — never collapse two of them into one unless the user explicitly asks for that combined scope.
- Use Plan mode when the scope of a request is uncertain or exploratory. Switch to Act mode only once the operation is deterministic and approved.
- Stop immediately when a required input is missing (a task spec path, an expected hash, an explicit approval). Do not guess a substitute and continue.
- Do not keep reasoning or acting past a defined stop condition (a failed gate, a missing input, an unexpected repository state). Report and wait.
- End every task with a short, machine-readable summary plus the path to any handoff file written, instead of a long narrative.
- Use `@` file/folder mentions only for the specific files a task actually needs. Do not pull in unrelated context.
- Avoid reading the entire repository. Read only the files a task's scope requires.
- Do not use a browser tool or MCP server for local NCC file work — this repository's operations are local filesystem and Git operations only.
