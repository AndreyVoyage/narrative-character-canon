# Phase 1 — Current Laptop + Cloud Pipeline

Phase 1 описывает текущую реальность: ноутбук слабый, поэтому нельзя рассчитывать на тяжёлый локальный AI/render/video pipeline. Ноутбук используется как control room, репозиторий является центром управления, а тяжёлые задачи выполняются в облаке. Главная задача сейчас — создать материалы, которые не придётся переделывать после покупки нового ПК.

## 1. Цель Phase 1

Phase 1 — это не временная ерунда, а подготовительный production pipeline. Его результатом должны стать проверенные character canon materials, которые можно будет перенести в локальный pipeline Phase 2.

Цель Phase 1:

* собрать персонажей;
* утвердить visual canon;
* сделать face/body/outfit/expression sheets;
* сделать prompt kits;
* провести control tests;
* подготовить 3D reference packs;
* подготовить документы для будущего 3D;
* использовать облачные сервисы для тяжёлой генерации фото/видео;
* не создавать персонажей с нуля в будущем.

## 2. Роль ноутбука

Ноутбук используется для:

* VS Code;
* Git;
* Git LFS;
* Kimi Code / Codex;
* ChatGPT;
* просмотра изображений;
* сортировки файлов;
* документации;
* prompt writing;
* inventory;
* лёгкой правки;
* подготовки и проверки результата.

Ноутбук НЕ используется для:

* тяжёлой локальной генерации видео;
* тяжёлого локального Stable Diffusion;
* тяжёлого Blender rendering;
* больших локальных LLM;
* сложной 3D-анимации;
* production render.

## 3. Программы Phase 1 и где они используются

| Этап | Программа | Как использовать | Что сохранять |
|---|---|---|---|
| Repo control | VS Code | Редактирование markdown, работа с repo, запуск Kimi/Codex, проверка структуры. | Markdown-документы, prompts, notes, результаты проверок. |
| Version control | Git | Commits, push, контроль истории, фиксация этапов canon-ready. | Осмысленные commits, чистый `git status`, история milestones. |
| Large assets | Git LFS | Хранение PNG/JPG/WEBP/MP4/MOV/PSD. Не хранить большие визуальные файлы как обычный git blob. | LFS-tracked visual assets, проверенные указатели LFS. |
| Control room | ChatGPT | Штаб управления, анализ изображений, генерация prompts, аудит отчётов Kimi/Codex, проектирование roadmap, решения APPROVE / REGENERATE. | Решения, критерии approval, prompts, замечания к тестам. |
| Local agent | Kimi Code / Codex | Локальные изменения файлов, создание markdown, обновление inventory, безопасные commits, repo checks. | Изменённые markdown-файлы, отчёты, commit hash. |
| Heavy generation | Browser / cloud AI services | Генерация изображений, видео, тестовых сцен. Более чувствительные adult/private experiments делать только в разрешённых сервисах и только с adult characters. | Скачанные результаты, notes, approval status, seed/settings если доступны. |
| Node workflows | RunComfy / Comfy Cloud / cloud GPU | Тяжёлые node workflows, image-to-image, pose/reference workflows, upscale, video experiments. | Workflow notes, workflow JSON если доступен, результаты, параметры. |
| Reference boards | PureRef | Собрать reference board персонажа: face, profile, body, outfit, expression refs. Использовать перед Blender/3D этапом. | Board/export в `09_blender/01_reference_pack/` или local storage. |
| Image review | XnView MP | Быстрый просмотр, сравнение изображений, сортировка, bulk rename, проверка дубликатов. | Переименованные файлы, отобранные approved/rejected кандидаты. |
| Light 2D edit | Krita | Лёгкая ручная правка, paintover, маски, пометки, исправление мелких дефектов, clean reference sheets. Не использовать как тяжёлую AI-станцию на слабом ноутбуке. | `.kra` или экспортированные clean sheets только после approval. |
| Light 3D check | Blender | Только лёгкий просмотр, basic blockout, проверка пропорций, простые turntable/reference tests, если ноутбук тянет. | Простые `.blend`, screenshots/notes, reference checks. |
| Upscale | Upscayl | Использовать только если ноутбук тянет; иначе делать upscale в облаке. | Upscaled candidates, comparison notes. |
| Transfer archives | 7-Zip | Временные архивы для переноса. ZIP не коммитить и не считать source of truth. | Временные локальные архивы вне canon flow. |
| Video tests | Cloud video tools | Короткие video tests, character motion experiments, scene mood tests. Видео не считается canon без reference frames и notes. | Keyframes, notes/settings, rejected/approved flags. |

## 4. File workflow Phase 1

1. Сгенерировать изображение в облаке.
2. Скачать локально.
3. Сохранить во временную папку.
4. Проверить в ChatGPT.
5. Если APPROVE — переименовать правильно.
6. Положить в нужную папку character.
7. Обновить canon index/test results.
8. Обновить inventory.
9. Commit.
10. Push.
11. Скопировать важные документы в local storage.

## 5. Adult/private scenes policy

Базовый character canon должен оставаться нейтральным, reusable и clean. Более откровенные/adult сцены не должны загрязнять базовые face/body/outfit canon files.

Правила:

* такие сцены должны храниться отдельно как private scene workflow;
* использовать только adult characters;
* не смешивать adult scene outputs с core canon;
* не коммитить sensitive/private outputs в публичный репозиторий;
* если репозиторий private, всё равно хранить adult/private scene experiments отдельно;
* использовать только сервисы, где такие сцены разрешены правилами;
* в canon index отмечать только reusable neutral references.

Рекомендуемая локальная структура вне repo, которую можно создать позже:

```text
C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\private_scene_workflow\
├── drafts\
├── approved_refs\
├── rejected\
├── prompts\
└── notes\
```

Эти папки сейчас не создаются. Они описаны как будущая безопасная зона для private workflow.

## 6. Phase 1 character workflow

1. Raw intake.
2. RAW_FILE_MAP.
3. IDENTITY.
4. CANON_INDEX.
5. FACE Sheet A.
6. FACE Sheet B.
7. EXPRESSION Sheet C.
8. BODY canon.
9. OUTFIT canon.
10. Control tests.
11. TEST_RESULTS.
12. 3D_REFERENCE_PACK.md.
13. 3D_MODEL_SPEC.md.
14. Ready for Phase 2.

## 7. Phase 1 3D preparation

В Phase 1 мы не обязаны делать полноценную 3D-модель локально. Задача Phase 1 — подготовить всё, что нужно 3D-этапу, чтобы в Phase 2 Blender pipeline мог стартовать не с поиска identity, а с уже утверждённого canon.

Нужно подготовить:

* front face;
* side face;
* 3/4 face;
* front body;
* side body;
* back body;
* neutral expression;
* expression sheet;
* hair refs;
* outfit refs;
* PureRef board;
* 3D reference pack document;
* 3D model spec document.

Папка для reference pack:

```text
AI_CHARACTERS/<CHARACTER>/09_blender/01_reference_pack/
```

Документы:

```text
AI_CHARACTERS/<CHARACTER>/10_notes/<CHARACTER>_3D_REFERENCE_PACK.md
AI_CHARACTERS/<CHARACTER>/10_notes/<CHARACTER>_3D_MODEL_SPEC.md
```

## 8. Phase 1 Definition of Done

Phase 1 считается успешной для персонажа, если:

* 2D canon готов;
* control tests пройдены;
* 3D reference pack подготовлен;
* 3D model spec подготовлен;
* все активные файлы указаны в canon index;
* inventory обновлён;
* repo clean;
* local storage имеет копии ключевых документов.
