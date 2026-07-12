# Narrative Character Canon — Roadmap

## 1. Цель проекта

`narrative-character-canon` — единый источник правды для визуального канона персонажей Narrative / Voyage. Репозиторий нужен не просто как папка с красивыми изображениями, а как управляемая система, где у каждого персонажа есть утверждённая identity, стабильные reference sheets, промпты, результаты тестов и путь к будущему 3D/video production.

Репозиторий нужен для:

* стабильной генерации изображений;
* подготовки персонажей к видео;
* подготовки персонажей к анимации;
* подготовки 3D reference packs;
* будущего создания 3D-моделей;
* будущего локального AI pipeline;
* защиты от хаоса в файлах;
* повторяемости персонажей.

Главная формула проекта:

```text
2D canon → stable references → 3D reference pack → 3D model → rig → animation/video → local AI production
```

## 2. Почему проект разделён на две фазы

### Фаза 1 — текущий ноутбук + облачные сервисы

Текущий ноутбук слабый, поэтому он используется как control room, а не как тяжёлая production-станция. Локально делаются:

* структура репозитория;
* сортировка;
* документация;
* canon index;
* prompts;
* git;
* inventory;
* лёгкая проверка изображений;
* подготовка материалов.

Тяжёлые задачи делаются через:

* браузерные AI-сервисы;
* облачные генераторы изображений;
* облачные video tools;
* cloud ComfyUI / RunComfy / cloud GPU;
* внешние сервисы для рендера, апскейла и видео.

### Фаза 2 — новый мощный компьютер + локальный production pipeline

Когда появится новый мощный компьютер, проект переходит к локальному production pipeline:

* локальные нейросети для фото;
* локальные нейросети для видео;
* локальные LLM для текстов, сцен, промптов и диалогов;
* локальный ComfyUI;
* локальный Blender pipeline;
* локальные 3D-модели;
* локальный rig / animation / render;
* локальная приватная работа без необходимости начинать персонажей с нуля.

## 3. Главный принцип

Сейчас мы не пытаемся сделать всё локально. Сейчас мы создаём фундамент, который позже переедет в локальный AI/3D/video workflow:

* character identity;
* face canon;
* body canon;
* expression canon;
* outfit canon;
* prompt kits;
* control tests;
* 3D reference packs;
* 3D model specs;
* local storage backup.

Когда появится новый компьютер, мы не начинаем с нуля. Мы берём уже утверждённые материалы и переносим их в локальный AI/3D/video workflow.

## 4. Текущие документы проекта

* [PHASE_1_CURRENT_LAPTOP_CLOUD_PIPELINE.md](PHASE_1_CURRENT_LAPTOP_CLOUD_PIPELINE.md) — описание текущей работы на слабом ноутбуке с использованием облачных сервисов.
* [PHASE_2_LOCAL_AI_WORKSTATION_PIPELINE.md](PHASE_2_LOCAL_AI_WORKSTATION_PIPELINE.md) — описание будущей работы на мощном ПК с локальными нейросетями, Blender, видео, 3D и текстовыми моделями.

## 5. Текущий статус репозитория

* repository foundation: DONE;
* AI_CHARACTERS structure: DONE;
* Git / Git LFS: DONE;
* Universal visual-canon pipeline: ADOPTED (`docs/NCC_VISUAL_CANON_WORKFLOW.md`, `configs/visual_canon/pipeline_policy.json`, schemas);
* KIRA: `CANON_READY_2D` / `PROMPT_PIPELINE_ACTIVE_CORE`;
* ANDREY: `CANON_READY_2D` / `PROMPT_PIPELINE_ACTIVE`;
* ANDREY_JUNIOR: `BASE_CANON_APPROVED` / `CONTROL_TESTS_APPROVED` / `PROMPT_PIPELINE_ACTIVE` (public_filtered only);
* KIRA_ANDREY: `JOINT_CONTROL_TESTS_APPROVED` / `DUO_SCENE_PACKS_APPROVED`;
* OLGA: `BASE_CANON_APPROVED` / `CONTROL_TESTS_APPROVED` (Tests 01–09 published) / `PROMPT_PIPELINE_ACTIVE`;
* Group C (MARINA, NIKA, SERGEY, MAKSIM, EGOR): `TEXT_CANON_READY` / `CANON_PROMPTS_CREATED`;
* Next steps: implement validator MVP and deploy-tool MVP; pilot on OLGA Test10.

## 6. Приоритеты

### Priority 1 — ANDREY

Довести до 2D canon-ready и подготовить к 3D.

### Priority 2 — KIRA

Проверить репозиторий, обновить canon index и подготовить к 3D.

### Priority 3 — MARINA

Создать полный canon pack.

### Priority 4 — NIKA

Создать полный canon pack. Важно: adult, tasteful, cinematic, non-explicit base canon. Более откровенные сцены должны быть отделены от базового character canon.

### Priority 5 — OLGA

Создать полный canon pack.

### Priority 6 — EGOR

Создать полный canon pack. Важно: не допускать случайного drift в слишком взрослый / крупный / muscular тип, если это противоречит canon.

### Priority 7 — SERGEY / MAKSIM

Создать secondary character packs.

## 7. Долгосрочный путь

1. 2D canon.
2. Control tests.
3. 3D reference pack.
4. PureRef board.
5. Blender blockout.
6. Sculpt.
7. Retopology.
8. UV.
9. Textures.
10. Materials.
11. Rig.
12. Facial blendshapes.
13. Clothing setup.
14. Turntable renders.
15. Pose renders.
16. Animation tests.
17. AI image references.
18. AI video references.
19. Local production pipeline.

## 8. Definition of Done

### 2D canon-ready

* RAW_FILE_MAP;
* IDENTITY;
* CANON_INDEX;
* face Sheet A;
* face Sheet B;
* expression Sheet C;
* body canon;
* outfit canon;
* минимум 2 successful control tests;
* TEST_RESULTS;
* INVENTORY updated;
* git status clean.

### 3D-ready

* полный 2D canon;
* front/side/back body refs;
* front/side/profile head refs;
* neutral expression;
* expression refs;
* hair refs;
* outfit refs;
* 3D_REFERENCE_PACK.md;
* 3D_MODEL_SPEC.md.

### Animation-ready

* 3D model;
* clean topology;
* UV;
* textures;
* materials;
* body rig;
* facial rig;
* blendshapes;
* clothing compatibility;
* exports;
* turntables;
* animation tests.

## 9. Immediate next actions

1. Implement validator MVP (`tools/validate_visual_canon_pipeline.py`).
2. Implement deploy-tool MVP (`tools/deploy_visual_canon_result.py`).
3. Run OLGA Test10 (`neutral_height_scale_check`) as the first end-to-end pipeline pilot.
4. Prepare ANDREY 3D reference pack and model spec when requested.
5. Backfill KIRA_ANDREY joint prompt pipeline when requested.
6. Continue Group C base canon generation only after per-character `IDENTITY.txt` and `CANON_INDEX.md` skeletons are created.
