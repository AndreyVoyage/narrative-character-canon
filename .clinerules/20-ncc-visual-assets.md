# NCC Visual Assets

- Never generate an image unless the user has explicitly authorized that specific generation request.
- Never edit source image pixels during a reference import or any other file operation. Imports are byte-for-byte copies only.
- Copy external originals into the repository; never move or delete the external source file.
- Verify SHA-256 of the source before copying and of the destination immediately after copying. A mismatch is a hard failure.
- Never overwrite an existing repository file with different content. If a target path already exists with different bytes than the requested source, stop and report the conflict instead of overwriting.
- If a target path already exists with the *same* content (identical SHA-256), reuse the existing tracked file instead of creating a duplicate.
- Role assignment (`FACE_MAIN`, `BODY_MAIN`, `SUPPORT`, `MAIN`/`ALT`, etc.) is a human decision recorded in the task spec or a later approval step. Do not infer or upgrade a role.
- In duo/joint scenes, a person appearing alongside the target character must not be merged into or treated as the target character's identity.
- Reference imports are a copy-only operation. They do not create prompt attempts, canon-test registrations, or approvals by themselves — those remain separate, explicitly requested steps.
- SQLite (`LOCAL_STORAGE/.../voyage_memory/*.sqlite`) and other local/private assets stay outside normal reference-import flow; never read, write, or reference them from an import task.
