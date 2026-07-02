# .voyage Memory Layer

Эта папка — управленческий слой памяти проекта `narrative-character-canon`. Это не Voyage Framework и не автономный агент — только markdown-файлы, фиксирующие состояние, статусы и решения, чтобы разные сессии и инструменты (ChatGPT, Kimi, Codex, Claude Code) не теряли контекст.

## Файлы

* [PROJECT_STATE.md](PROJECT_STATE.md) — текущее состояние проекта.
* [CHARACTER_REGISTRY.md](CHARACTER_REGISTRY.md) — статус персонажей.
* [LOCATION_REGISTRY.md](LOCATION_REGISTRY.md) — статус локаций.
* [SCENE_REQUEST_RULES.md](SCENE_REQUEST_RULES.md) — правила статусов сцен.
* [DECISIONS.md](DECISIONS.md) — журнал решений.
* [CURRENT_TASK.md](CURRENT_TASK.md) — текущая активная задача.

Общий контекст и обоснование см. в [docs/VOYAGE_INTEGRATION_WORKFLOW.md](../docs/VOYAGE_INTEGRATION_WORKFLOW.md).

## Главное правило

Если информация в отчёте агента противоречит `git status` / `git log` / фактическим файлам в репозитории — source of truth это git и фактические файлы, а не текст отчёта.

Второе по важности правило: **пример сцены не равен задаче на генерацию**. Смотри [SCENE_REQUEST_RULES.md](SCENE_REQUEST_RULES.md).
