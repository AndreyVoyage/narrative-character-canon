# GitHub Reference Pack Workflow

> **Scope:** Reference-pack generation for Phase 1 cloud generation.
> **Parent authority:** `docs/NCC_VISUAL_CANON_WORKFLOW.md` — all future scene generation, selection, and deployment must follow the universal visual-canon pipeline.

## 1. Цель

Этот workflow нужен для быстрого подбора нужных reference images и канонических текстовых описаний персонажей перед генерацией сцены. Он превращает короткий запрос сцены в готовый reference pack: какие изображения загрузить вручную, какие GitHub/raw links соответствуют этим файлам, какой prompt вставить в генератор и как назвать результат.

## 2. Главная идея

```text
GitHub repository -> scene request -> reference selection -> embedded character canon -> output prompt -> manual image upload -> generation -> review -> save approved output
```

GitHub остаётся source of truth: все пути, raw links и текстовые каноны берутся из репозитория. Изображения пользователь загружает вручную, а текстовый canon инструмент встраивает прямо в итоговый prompt.

## 3. Что автоматизируется

* поиск подходящих references;
* подбор файлов по персонажу и типу сцены;
* сбор raw links;
* встроенный текстовый canon в итоговый prompt;
* suggested filename.

## 4. Что НЕ автоматизируется в Phase 1

* ChatGPT не загружает PNG напрямую из GitHub автоматически;
* пользователь вручную загружает указанные image references;
* текстовые canon files вручную загружать НЕ нужно, так как они встраиваются в prompt.

## 5. Типы сцен

Базовые типы сцен для v1:

* sauna;
* bar;
* evening_walk;
* yoga;
* beach;
* sports;
* formal;
* portrait;
* body_canon;
* expression_test.

Тип сцены не обязан идеально совпадать с папкой в репозитории. Для каждого персонажа `REFERENCE_PRESETS.json` хранит готовые наборы файлов, а инструмент при необходимости использует fallback на ближайший preset.

## 6. Что такое reference preset

Preset — заранее описанный набор лучших файлов для определённого персонажа и определённого типа сцены. Например, для sauna у персонажа могут использоваться face canon, body canon и нейтральные body/casual references, даже если отдельного sauna outfit ещё нет.

Preset содержит:

* описание сцены;
* список image references;
* prompt goal;
* ссылки на текстовые источники character canon.

## 7. Что создаёт инструмент

Инструмент создаёт pack в local storage:

```text
C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\scene_packs\...
```

Файлы pack:

* `SCENE_REFERENCE_PACK.md`;
* `SCENE_RAW_LINKS.md`;
* `SCENE_PROMPT.txt`;
* `SCENE_PACK.json`.

## 8. Как использовать

1. Запустить script.
2. Передать characters + scene + description.
3. Получить готовый pack.
4. Открыть `SCENE_REFERENCE_PACK.md`.
5. Загрузить только перечисленные изображения.
6. Скопировать `SCENE_PROMPT.txt`.
7. Сгенерировать изображение.
8. Проверить результат.
9. Сохранить approved output в repo.
10. Обновить inventory и commit/push.

Пример:

```powershell
python .\tools\build_scene_reference_pack.py --characters KIRA,ANDREY --scene sauna --description "Кира и Андрей в сауне разговаривают, укрытые по пояс полотенцем"
```

## 9. Роль программ

| Этап | Программа | Как используется | Результат |
|---|---|---|---|
| Source of truth | GitHub | Хранит canonical refs, markdown, prompts и историю изменений. | GitHub paths и raw links для ручной загрузки изображений. |
| Local editing | VS Code | Просмотр pack, правка presets, документация. | Обновлённые JSON/Markdown/Python files. |
| Automation | Python | Создаёт scene reference pack из presets и canon text. | `SCENE_REFERENCE_PACK.md`, raw links, prompt, JSON summary. |
| One-command launch | PowerShell | Wrapper для запуска Python script с удобными аргументами. | Тот же output folder без ручного набора Python-команды. |
| Generation control | ChatGPT | Получает вручную загруженные images и готовый prompt, помогает approve/regenerate. | Image generation result и review notes. |
| Repo agent | Kimi/Codex | Обновляет presets, docs, inventory, помогает безопасно коммитить. | Поддерживаемый workflow в репозитории. |
| Future node workflow | Future ComfyUI | Позже сможет использовать те же refs и prompt logic локально. | Reusable workflow JSON, seeds, local generations. |
| 3D references | Blender | Использует selected refs для blockout, pose refs, turntables и model checks. | 3D reference usage и renders. |
| Reference boards | PureRef | Собирает выбранные refs в доску перед 3D или сложной сценой. | PureRef board для персонажа/сцены. |

## 10. Phase 2

В Phase 2 этот же принцип можно подключить к локальному ComfyUI и Blender. Тогда presets будут использоваться не только для ручной загрузки в ChatGPT, но и для локальных workflows: image-to-image, pose/depth/normal pipelines, 3D pose renders, turntables и controlled video tests.

Ключевой принцип остаётся прежним: repository canon сначала, генерация потом.

## 11. Supported characters

Current character preset coverage:

* ANDREY — active GitHub-first presets with tracked face/expression/body/control-test references.
* ANDREY_JUNIOR — active son-version presets; public_filtered only.
* KIRA — active GitHub-first presets with tracked face/body/outfit/test references.
* OLGA — active presets with base canon, Tests 01–09, and DALL-E backend variant.
* MARINA — preset file exists, scene presets pending tracked image references.
* NIKA — preset file exists, scene presets pending tracked image references.
* SERGEY — preset file exists, scene presets pending tracked image references.
* MAKSIM — preset file exists, scene presets pending tracked image references.
* EGOR — preset file exists, scene presets pending tracked image references.

Presets are GitHub-first and should only use tracked files available on GitHub. Do not add untracked image files, guessed paths, placeholder names, or `.gitkeep` files as image references.

## 12. Правила для sensitive/adult scenes

* использовать только adult characters;
* core canon оставлять нейтральным;
* sensitive outputs хранить отдельно и не смешивать с base canon;
* manual approval обязателен;
* в публичный или потенциально публичный repo не коммитить private outputs;
* reusable face/body/outfit canon должен оставаться production-safe.

## 13. Immediate next step

Use the tool only for approved scenes. The sauna example below remains an **EXAMPLE / NOT REQUESTED** scene — see `.voyage/SCENE_REQUEST_RULES.md`.

When a scene is approved, build the reference pack first, then follow `docs/NCC_VISUAL_CANON_WORKFLOW.md` for generation, selection, and deployment.

```powershell
# Illustrative command only — do not treat as a generation request.
python .\tools\build_scene_reference_pack.py --characters KIRA,ANDREY --scene sauna --description "Кира и Андрей в сауне разговаривают, укрытые по пояс полотенцем"
```
