# Phase 2 — Local AI Workstation Pipeline

Phase 2 описывает будущий режим, когда появится новый мощный компьютер. В этот момент проект переходит от cloud-assisted preparation к локальному AI/3D/video/text production.

## 1. Цель Phase 2

Phase 2 начинается, когда есть новый ПК и уже подготовленные character canon materials.

Главная идея:

Мы не создаём персонажей с нуля. Мы берём готовый canon из Phase 1 и переносим его в локальный AI/3D/video production.

## 2. Что меняется после появления нового ПК

Появляется возможность:

* локальная генерация изображений;
* локальная генерация видео;
* локальный ComfyUI;
* локальные LLM;
* локальный Blender rendering;
* локальные 3D-модели;
* локальные rig/animation tests;
* локальный upscale;
* локальная приватность;
* повторяемые workflows.

## 3. Программы Phase 2 и где они используются

| Этап | Программа | Как использовать | Что сохранять |
|---|---|---|---|
| Repo control | VS Code | Repo control, markdown docs, prompt library, scripts, local automation. | Markdown, prompts, scripts, validation notes. |
| Version control | Git / Git LFS | Version control, visual asset tracking, milestone commits. | Commits, LFS assets, release-like milestones. |
| Strategic control | ChatGPT | Strategic control room, audit, prompt design, story/scene planning, quality decisions. | Decisions, prompts, scene briefs, approval notes. |
| Local agent | Kimi Code / Codex | Local repo changes, scripts, validation, documentation updates. | Repo edits, validation reports, commit hashes. |
| Local node generation | ComfyUI | Локальная node-based генерация изображений, image-to-image, ControlNet/pose/depth/normal workflows если доступны, character reference workflows, upscale workflows, video frame preparation. | Workflow JSON, seed/settings, input refs, output notes. |
| Image models | Stable Diffusion / SDXL / FLUX-style models | Локальная генерация персонажей, LoRA / embeddings / reference workflows, scene generation, controlled style tests. Конкретные модели не фиксируются как обязательные, потому что набор моделей может измениться. | Model notes, settings, seeds, approved outputs, rejected tests. |
| Text models | Local LLM tools | Написание сцен, диалогов, prompts, lore, character notes, negative prompts, batch prompt generation, translation/adaptation. | Drafts, prompt variants, lore notes, reviewed final text. |
| 2D cleanup | Krita | Paintover, mask editing, texture corrections, inpainting support, reference cleanup, frame corrections. | `.kra`, masks, corrected refs, texture notes. |
| Krita-local AI | Krita AI Diffusion | Использовать после появления мощного ПК для локальной генерации/редактирования внутри Krita, controlled edits, mask-based edits. | Krita files, settings, masks, approved edits. |
| 3D production | Blender | Полноценный 3D pipeline: blockout, sculpt, retopology, UV, materials, lighting, camera, render, rig, animation, turntables, pose references. | `.blend`, renders, rig files, turntables, pose refs. |
| Reference boards | PureRef | Reference boards для каждого персонажа, 3D reference boards, outfit boards, scene boards. | PureRef boards/exports, board notes. |
| Video editing | DaVinci Resolve или другой video editor | Монтаж, цвет, звук, preview renders, final clips. | Project files, preview renders, final clips, edit notes. |
| Upscale | Upscayl / local upscalers | Upscale images/video frames, compare before/after. Не заменять canon source без approval. | Upscaled outputs, comparison notes, approval status. |
| Fallback | Cloud services | Остаются optional fallback для задач, которые быстрее/лучше делать в облаке. Не заменяют локальный source of truth. | Cloud outputs, settings, notes, manual approval. |

## 4. Local image generation workflow

1. Взять character canon.
2. Взять face/body/outfit refs.
3. Создать ComfyUI workflow.
4. Подключить reference images.
5. Выставить seed/settings.
6. Сгенерировать draft.
7. Сравнить с canon.
8. APPROVE / REGENERATE.
9. Сохранить approved output.
10. Обновить test results.
11. Commit.

## 5. Local video workflow

1. Создать scene brief.
2. Взять character canon.
3. Взять 3D pose/turntable renders или reference frames.
4. Создать video workflow.
5. Генерировать короткими тестами.
6. Сохранять keyframes.
7. Проверять identity drift.
8. Reject плохие кадры.
9. Собирать удачные фрагменты в video editor.
10. Сохранять notes/settings.

## 6. Local text generation workflow

Локальные LLM используются для текстов:

* писать character scenes;
* писать диалоги;
* писать prompts;
* переводить;
* адаптировать;
* делать варианты;
* готовить negative prompts;
* собирать batch prompt generation.

Финальные решения принимает Андрей через ChatGPT control room. Локальная LLM помогает производить варианты, но не заменяет human approval.

## 7. 3D model pipeline

| Этап | Программа | Что делаем | Что сохраняем | Критерий готовности |
|---|---|---|---|---|
| 1. 3D reference pack | VS Code / PureRef | Собираем утверждённые face/body/outfit/expression refs. | `3D_REFERENCE_PACK.md`, PureRef board, refs. | Все ключевые ракурсы и notes собраны. |
| 2. PureRef board | PureRef | Раскладываем refs для моделинга и проверки пропорций. | `.pur`/export, board notes. | Board читается быстро и покрывает голову, тело, одежду. |
| 3. Blender blockout | Blender | Создаём грубую форму тела, головы, пропорций. | `.blend`, blockout screenshots. | Пропорции совпадают с canon. |
| 4. Sculpt | Blender | Уточняем формы лица, тела, волосы, детали. | Sculpt `.blend`, progress renders. | Силуэт и ключевые черты узнаваемы. |
| 5. Retopology | Blender | Создаём clean topology для анимации. | Retopo mesh, topology screenshots. | Mesh чистый, без лишней плотности и проблемных loops. |
| 6. UV | Blender | Разворачиваем модель под текстуры. | UV layout, `.blend`. | UV без критичных overlap и подходит для текстур. |
| 7. Textures | Krita / Blender | Создаём и правим текстуры кожи, волос, одежды. | Texture maps, source files. | Текстуры читаются при close-up и full body. |
| 8. Materials | Blender | Настраиваем материалы кожи, волос, ткани, глаз. | Material setup in `.blend`. | Материалы работают в тестовом освещении. |
| 9. Body rig | Blender | Делаем скелет, weights, базовые движения. | Rigged `.blend`, test poses. | Тело позируется без грубых деформаций. |
| 10. Facial rig | Blender | Настраиваем лицевое управление. | Facial rig, controllers. | Базовая мимика управляемая и узнаваемая. |
| 11. Blendshapes | Blender | Создаём expression targets. | Shape keys/blendshapes. | Neutral, smile, serious, surprise и другие expressions стабильны. |
| 12. Clothing | Blender / Krita | Готовим одежду, совместимость с rig, материалы. | Clothing meshes, materials, texture maps. | Одежда не ломается в базовых позах. |
| 13. Exports | Blender | Экспортируем нужные форматы для pipeline. | `.blend`, `.fbx`/`.glb` если нужны. | Экспорт открывается без потери rig/materials. |
| 14. Turntable renders | Blender | Рендерим круговой обзор. | Turntable frames/video. | Модель узнаваема со всех сторон. |
| 15. Pose renders | Blender | Рендерим позы для AI refs и проверки rig. | Pose renders, pose notes. | Позы читаются и не ломают character identity. |
| 16. Animation tests | Blender / video editor | Тестируем движение, мимику, камеры. | Test clips, notes. | Движение пригодно для дальнейших video workflows. |

## 8. Как 3D помогает фото

3D-модель используется не только для анимации. Она помогает:

* получать стабильные ракурсы;
* делать pose references;
* делать depth maps;
* делать normal maps;
* делать silhouette refs;
* делать lighting refs;
* делать scene blocking;
* сохранять рост и пропорции;
* уменьшать identity drift;
* ускорять генерацию фото.

## 9. Как 3D помогает видео

3D-модель используется для:

* turntable;
* pose animation;
* body motion;
* face expression refs;
* talking head;
* scene blocking;
* camera movement;
* video keyframes;
* AI video references.

## 10. Adult/private local workflow

Локальный ПК даст больше приватности, но это не отменяет дисциплину хранения. Adult/private scene generation должна быть отделена от core canon.

Правила:

* использовать только adult characters;
* не смешивать private scene outputs с base canon;
* хранить private workflow отдельно;
* сохранять prompts/settings локально;
* не публиковать случайно;
* не коммитить private outputs в публичный repo;
* core canon должен оставаться reusable, neutral и production-safe.

## 11. Phase 2 Definition of Done

Phase 2 для персонажа успешна, если есть:

* complete 2D canon;
* 3D reference pack;
* 3D model spec;
* Blender model;
* textures/materials;
* rig;
* facial expressions;
* turntables;
* pose renders;
* local AI workflows;
* video tests;
* clean repo;
* local backup.
