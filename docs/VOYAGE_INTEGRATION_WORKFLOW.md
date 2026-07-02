# Voyage Integration Workflow

## 1. Цель

Voyage-lite слой нужен для сохранения контекста проекта `narrative-character-canon` между сессиями, инструментами и агентами. Он помогает не путать:

* example scene и real task;
* draft image и approved image;
* active canon и raw reference;
* local-only file и GitHub-tracked file;
* public repo content и private/local-only content;
* персонажа, сцену и локацию как разные сущности.

## 2. Что такое Voyage-lite в этом проекте

* это не автономный агент;
* это не генератор изображений;
* это не замена Git;
* это memory/control layer — набор markdown-файлов и правил;
* он совместим по идее с Framework-voyage-mvp, но сейчас не требует установки самого framework.

## 3. Главная проблема, которую решаем

В проекте будут десятки персонажей, локаций, outfit-паков, сцен, 3D-файлов и private/local outputs. Без слоя памяти легко перепутать пример и задачу.

Пример:

> "Кира и Андрей в сауне разговаривают, укрытые по пояс полотенцем"

Должна сначала быть записана как:

```
SCENE EXAMPLE / TOOL TEST IDEA
```

А не как:

```
APPROVED GENERATION TASK
```

## 4. Статусы сцен

* **EXAMPLE** — идея или пример команды. Ничего не генерировать.
* **REQUESTED** — пользователь явно попросил подготовить сцену.
* **REFERENCE_PACK_READY** — инструмент подготовил refs и prompt.
* **GENERATED_DRAFT** — изображение сгенерировано, но не утверждено.
* **APPROVED_AS_TEST** — можно сохранить в canon_tests.
* **APPROVED_AS_CANON** — можно использовать как active canon или strong reference.
* **REJECTED** — не использовать.
* **PRIVATE_LOCAL_ONLY** — хранить только вне public repo.

## 5. Статусы файлов

* **RAW** — исходный reference.
* **CANDIDATE** — потенциально полезный файл.
* **ACTIVE_CANON** — утверждённый active canon.
* **APPROVED_TEST** — утверждённый тестовый output.
* **REFERENCE_ONLY** — можно смотреть, но нельзя использовать как основной canon.
* **REJECTED** — не использовать.
* **LOCAL_ONLY** — есть только локально, не использовать для GitHub-first raw links.
* **GITHUB_TRACKED** — можно использовать в GitHub-first workflow.

## 6. Статусы персонажей

* **EMPTY_STRUCTURE** — есть папка, но почти нет данных.
* **RAW_BASED** — есть raw refs, но нет canon.
* **TEXT_CANON_READY** — есть identity/canon text.
* **FACE_CANON_ACTIVE** — есть active face canon.
* **BODY_PENDING** — body canon ещё не готов.
* **CANON_READY_2D** — персонаж готов в 2D.
* **READY_FOR_3D_REFERENCE_PACK** — можно готовить 3D reference pack.
* **READY_FOR_3D_MODEL** — можно начинать 3D model.

## 7. Где что хранится

* `AI_CHARACTERS/` — хранит assets персонажей.
* `docs/` — хранит workflow documentation.
* `tools/` — хранит automation scripts.
* `.voyage/` — хранит project memory/control files.
* Local storage вне repo — хранит private outputs, scene packs, backups, adult/private workflows.

## 8. Как фиксировать решения

Решения фиксируются в [.voyage/DECISIONS.md](../.voyage/DECISIONS.md).

Формат:

```
Дата:
Decision ID:
Context:
Decision:
Affected files:
Reason:
Next action:
```

## 9. Как фиксировать активную задачу

Активная задача фиксируется в [.voyage/CURRENT_TASK.md](../.voyage/CURRENT_TASK.md). Там указывается: task id, status, scope, files allowed to edit, forbidden actions, next expected report.

## 10. Как фиксировать персонажей

Персонажи фиксируются в [.voyage/CHARACTER_REGISTRY.md](../.voyage/CHARACTER_REGISTRY.md). Для каждого: character id, folder, current status, active canon files, missing canon files, reference preset status, next step.

## 11. Как фиксировать локации

Локации фиксируются в [.voyage/LOCATION_REGISTRY.md](../.voyage/LOCATION_REGISTRY.md). Для каждой: location id, description, status, refs folder if exists, related characters/scenes, next step.

## 12. Как использовать с локальными агентами (Kimi/Codex и др.)

Перед каждым запуском локального агента:

1. Проверить `PROJECT_STATE`.
2. Проверить `CURRENT_TASK`.
3. Сформировать prompt.
4. После отчёта обновить `DECISIONS`/`PROJECT_STATE`.
5. Не считать отчёт правдой без проверки git/files.

## 13. Как использовать с ChatGPT

ChatGPT используется как control room:

* анализирует отчёты;
* формирует prompts;
* проверяет сцены;
* принимает APPROVE/REGENERATE/HOLD;
* помогает фиксировать решения.

## 14. Защита от путаницы

* если сцена была приведена как пример, она не становится задачей;
* если файл не tracked в git, он не используется для GitHub raw links;
* если output не approved, он не canon;
* если private/adult output, он не попадает в public canon;
* если agent report противоречит git/files, верить git/files;
* если сомневаемся, сначала read-only audit.

## 15. Immediate next workflow

1. Зафиксировать Voyage-lite docs.
2. Проверить KIRA_REFERENCE_PRESETS.json.
3. Не генерировать KIRA + ANDREY sauna scene, пока пользователь явно не попросит.
4. Продолжить развитие GitHub-first reference tool.
