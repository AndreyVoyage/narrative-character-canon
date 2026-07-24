# INVENTORY.md

Repository:

C:\DEV\Narrative\narrative-character-canon

Generated:

2026-07-24 14:00:07

---

# Folder and file tree

```text
├── .claude/
│   └── settings.json
├── .cline/
│   └── skills/
│       └── ncc-reference-import/
│           ├── scripts/
│           │   ├── __pycache__/
│           │   │   └── import_references.cpython-314.pyc
│           │   └── import_references.py
│           ├── templates/
│           │   └── reference-import-task.example.json
│           └── SKILL.md
├── .clinerules/
│   ├── 00-ncc-project-boundary.md
│   ├── 10-ncc-git-safety.md
│   ├── 20-ncc-visual-assets.md
│   └── 30-ncc-task-discipline.md
├── .voyage/
│   ├── CHARACTER_REGISTRY.md
│   ├── CHARACTER_REGISTRY.md.backup_20260703_124946
│   ├── CHARACTER_REGISTRY.md.backup_20260703_155641
│   ├── CHARACTER_REGISTRY.md.backup_20260704_151046
│   ├── CHARACTER_REGISTRY.md.backup_20260704_160529
│   ├── CHARACTER_REGISTRY.md.backup_20260705_162559
│   ├── CHARACTER_REGISTRY.md.backup_20260705_234357
│   ├── CHARACTER_REGISTRY.md.backup_20260706_083029
│   ├── CHARACTER_REGISTRY.md.backup_20260706_115144
│   ├── CHARACTER_REGISTRY.md.backup_20260707_154019
│   ├── CONTEXT_SNAPSHOT.md
│   ├── CURRENT_TASK.md
│   ├── CURRENT_TASK.md.backup_20260703_124946
│   ├── CURRENT_TASK.md.backup_20260703_155641
│   ├── CURRENT_TASK.md.backup_20260704_151046
│   ├── CURRENT_TASK.md.backup_20260704_160529
│   ├── CURRENT_TASK.md.backup_20260705_162559
│   ├── CURRENT_TASK.md.backup_20260705_234423
│   ├── CURRENT_TASK.md.backup_20260706_083029
│   ├── CURRENT_TASK.md.backup_20260706_115144
│   ├── CURRENT_TASK.md.backup_20260707_154019
│   ├── DECISIONS.md
│   ├── DECISIONS.md.backup_20260702_231625
│   ├── DECISIONS.md.backup_20260703_124946
│   ├── DECISIONS.md.backup_20260703_155641
│   ├── DECISIONS.md.backup_20260704_151046
│   ├── DECISIONS.md.backup_20260704_160529
│   ├── DECISIONS.md.backup_20260705_162559
│   ├── DECISIONS.md.backup_20260705_234423
│   ├── DECISIONS.md.backup_20260706_083029
│   ├── DECISIONS.md.backup_20260706_115144
│   ├── DECISIONS.md.backup_20260707_154019
│   ├── EVENTS_EXPORT.jsonl
│   ├── LOCATION_REGISTRY.md
│   ├── PROJECT_STATE.md
│   ├── README.md
│   ├── SCENE_REQUEST_RULES.md
│   ├── SQLITE_MEMORY_STATUS.md
│   └── STATE_EXPORT.json
├── .vscode/
│   └── settings.json
├── AI_CHARACTERS/
│   ├── _JOINT_SCENES/
│   │   └── KIRA_ANDREY/
│   │       ├── 06_prompts/
│   │       │   └── KIRA_ANDREY_DUO_SCENE_PACK_PROMPTS.txt
│   │       ├── 07_generated/
│   │       │   ├── canon_tests/
│   │       │   │   ├── 01_neutral_studio_duo/
│   │       │   │   │   ├── .gitkeep
│   │       │   │   │   └── KIRA_ANDREY_joint_test01_neutral_studio_duo_v2_APPROVED.png
│   │       │   │   ├── 02_evening_embankment_duo/
│   │       │   │   │   ├── .gitkeep
│   │       │   │   │   └── KIRA_ANDREY_joint_test02_evening_embankment_duo_v1_APPROVED.png
│   │       │   │   ├── 03_warm_bar_conversation/
│   │       │   │   │   ├── .gitkeep
│   │       │   │   │   └── KIRA_ANDREY_joint_test03_warm_bar_conversation_v1_APPROVED.png
│   │       │   │   └── 04_sea_yacht_mood_duo/
│   │       │   │       ├── .gitkeep
│   │       │   │       └── KIRA_ANDREY_joint_test04_sea_yacht_mood_duo_v1_APPROVED.png
│   │       │   └── scene_packs/
│   │       │       ├── 01_evening_embankment_walk/
│   │       │       │   ├── .gitkeep
│   │       │       │   └── KIRA_ANDREY_scene01_evening_embankment_walk_v1_APPROVED.png
│   │       │       ├── 02_warm_bar_dialogue/
│   │       │       │   ├── .gitkeep
│   │       │       │   └── KIRA_ANDREY_scene02_warm_bar_dialogue_v1_APPROVED.png
│   │       │       ├── 03_yacht_sunset/
│   │       │       │   ├── .gitkeep
│   │       │       │   └── KIRA_ANDREY_scene03_yacht_sunset_v1_APPROVED.png
│   │       │       ├── 04_studio_character_poster/
│   │       │       │   ├── .gitkeep
│   │       │       │   └── KIRA_ANDREY_scene04_studio_character_poster_v1_APPROVED.png
│   │       │       ├── 05_rainy_city_street/
│   │       │       │   ├── .gitkeep
│   │       │       │   └── KIRA_ANDREY_scene05_rainy_city_street_v1_APPROVED.png
│   │       │       ├── 06_cozy_interior_conversation/
│   │       │       │   ├── .gitkeep
│   │       │       │   └── KIRA_ANDREY_scene_pack06_cozy_interior_conversation_v4_APPROVED.png
│   │       │       ├── candidates/
│   │       │       │   └── .gitkeep
│   │       │       └── rejected/
│   │       │           └── .gitkeep
│   │       └── 10_notes/
│   │           ├── KIRA_ANDREY_DUO_SCENE_PACK_INDEX.md
│   │           ├── KIRA_ANDREY_DUO_SCENE_PACK_INDEX.md.backup_20260703_124946
│   │           ├── KIRA_ANDREY_DUO_SCENE_PACK_RESULTS.md
│   │           ├── KIRA_ANDREY_DUO_SCENE_PACK_RESULTS.md.backup_20260703_124946
│   │           ├── KIRA_ANDREY_DUO_SCENE_PACKS.json
│   │           ├── KIRA_ANDREY_DUO_SCENE_PACKS.json.backup_20260703_124946
│   │           ├── KIRA_ANDREY_JOINT_CANON_INDEX.md
│   │           ├── KIRA_ANDREY_JOINT_TEST_RESULTS.md
│   │           ├── KIRA_ANDREY_REFERENCE_PRESETS.json
│   │           └── KIRA_ANDREY_REFERENCE_PRESETS.json.backup_20260703_124946
│   ├── ANDREY/
│   │   ├── 01_refs_raw/
│   │   │   ├── ANDREY_RAW_01_face_closeup_blue_shirt.png
│   │   │   ├── ANDREY_RAW_02_yacht_sunset_blue_shirt.png
│   │   │   ├── ANDREY_RAW_03_fullbody_studio_blue_shirt.png
│   │   │   ├── ANDREY_RAW_04_bar_portrait_blue_shirt.png
│   │   │   ├── ANDREY_RAW_05_main_identity_sheet_blue_shirt.png
│   │   │   ├── ANDREY_RAW_06_formal_suit_walking.png
│   │   │   ├── ANDREY_RAW_07_formal_suit_standing.png
│   │   │   ├── ANDREY_RAW_08_expressions_sheet_A.png
│   │   │   ├── ANDREY_RAW_09_expressions_sheet_B.png
│   │   │   ├── ANDREY_RAW_10_sports_gym_black.png
│   │   │   ├── ANDREY_RAW_11_body_identity_sheet_blue_shirt.png
│   │   │   └── ANDREY_RAW_12_kling_face_closeup_REFERENCE_ONLY.jpg
│   │   ├── 02_best_refs/
│   │   │   └── ANDREY_best_main_identity_sheet_v1.png.png
│   │   ├── 03_face_sheet/
│   │   │   ├── expressions/
│   │   │   │   └── ANDREY_expressions_v1_sheet_C_refined.png
│   │   │   ├── ANDREY_face_canon_v1_sheet_A_basic.png
│   │   │   └── ANDREY_face_canon_v1_sheet_B_angles.png
│   │   ├── 04_body_sheet/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   ├── ANDREY_body_canon_v1_sheet_A_front_side_back.png
│   │   │   └── ANDREY_body_canon_v1_sheet_B_pose_variations.png
│   │   ├── 05_outfits/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   ├── casual/
│   │   │   │   └── .gitkeep
│   │   │   ├── evening_dress/
│   │   │   │   └── .gitkeep
│   │   │   ├── formal/
│   │   │   │   └── .gitkeep
│   │   │   ├── scene_outfits/
│   │   │   │   └── .gitkeep
│   │   │   └── sports_look/
│   │   │       └── .gitkeep
│   │   ├── 06_prompts/
│   │   │   ├── ANDREY_BODY_CANON_NEGATIVE_PROMPT.txt
│   │   │   ├── ANDREY_BODY_CANON_PROMPT.txt
│   │   │   ├── ANDREY_CONTROL_TEST_PROMPTS.txt
│   │   │   ├── ANDREY_FACE_CANON_NEGATIVE_PROMPT.txt
│   │   │   ├── ANDREY_FACE_CANON_PROMPT.txt
│   │   │   ├── ANDREY_KIRA_JOINT_CONTROL_TEST_PROMPTS.txt
│   │   │   ├── ANDREY_PROMPT_INDEX.md
│   │   │   ├── ANDREY_PROMPT_RUN_LOG.jsonl
│   │   │   └── ANDREY_WORKING_SCENE_PROMPTS.md
│   │   ├── 07_generated/
│   │   │   ├── canon_tests/
│   │   │   │   ├── 01_evening_embankment/
│   │   │   │   │   └── .gitkeep
│   │   │   │   ├── 01_neutral_studio_portrait/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── ANDREY_test01_neutral_studio_portrait_v1.png
│   │   │   │   ├── 02_full_body_blue_shirt/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── ANDREY_test02_full_body_blue_shirt_studio_v1.png
│   │   │   │   ├── 02_sports_yoga/
│   │   │   │   │   └── .gitkeep
│   │   │   │   ├── 03_portrait_expression/
│   │   │   │   │   └── .gitkeep
│   │   │   │   ├── 03_warm_bar_portrait/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── ANDREY_test03_warm_bar_portrait_v1.png
│   │   │   │   ├── 04_formal_evening_look/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── ANDREY_test04_formal_evening_look_v1.png
│   │   │   │   ├── 05_sports_gym_identity/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── ANDREY_test05_sports_gym_identity_v1.png
│   │   │   │   └── 06_sea_yacht_mood/
│   │   │   │       ├── .gitkeep
│   │   │   │       └── ANDREY_test06_sea_yacht_mood_scene_v1.png
│   │   │   ├── drafts/
│   │   │   │   └── .gitkeep
│   │   │   └── rejected/
│   │   │       └── .gitkeep
│   │   ├── 08_masks/
│   │   │   └── .gitkeep
│   │   ├── 09_blender/
│   │   │   └── .gitkeep
│   │   └── 10_notes/
│   │       ├── ANDREY_CANON_APPROVAL_WORKSHEET.md
│   │       ├── ANDREY_CANON_INDEX.md
│   │       ├── ANDREY_CANON_INDEX.md.backup_20260630_085458
│   │       ├── ANDREY_CANON_INDEX.md.backup_20260706_115144
│   │       ├── ANDREY_IDENTITY.txt
│   │       ├── ANDREY_RAW_FILE_MAP.md
│   │       ├── ANDREY_REFERENCE_PRESETS.json
│   │       ├── ANDREY_REFERENCE_PRESETS.json.backup_20260706_115144
│   │       ├── ANDREY_REFERENCE_PRESETS.json.backup_20260709_092657
│   │       ├── ANDREY_TEST_RESULTS.md
│   │       └── ANDREY_TEST_RESULTS.md.backup_20260706_115144
│   ├── ANDREY_JUNIOR/
│   │   ├── 01_refs_raw/
│   │   │   └── .gitkeep
│   │   ├── 02_refs_selected/
│   │   │   └── .gitkeep
│   │   ├── 03_face_sheet/
│   │   │   ├── expressions/
│   │   │   │   ├── .gitkeep
│   │   │   │   └── ANDREY_JUNIOR_expressions_v2_sheet_A_APPROVED.png
│   │   │   ├── .gitkeep
│   │   │   └── ANDREY_JUNIOR_face_canon_v1_sheet_A_APPROVED.png
│   │   ├── 04_body_sheet/
│   │   │   ├── .gitkeep
│   │   │   ├── ANDREY_JUNIOR_body_canon_v2_sheet_A_front_side_back_APPROVED.png
│   │   │   └── ANDREY_JUNIOR_body_canon_v2_sheet_B_pose_variations_APPROVED.png
│   │   ├── 05_outfits/
│   │   │   └── .gitkeep
│   │   ├── 06_prompts/
│   │   │   ├── .gitkeep
│   │   │   ├── ANDREY_JUNIOR_CANON_GENERATION_PROMPTS.txt
│   │   │   ├── ANDREY_JUNIOR_CANON_GENERATION_PROMPTS.txt.backup_20260704_150852
│   │   │   ├── ANDREY_JUNIOR_CANON_GENERATION_PROMPTS.txt.backup_20260706_083029
│   │   │   ├── ANDREY_JUNIOR_PROMPT_INDEX.md
│   │   │   ├── ANDREY_JUNIOR_PROMPT_RUN_LOG.jsonl
│   │   │   └── ANDREY_JUNIOR_WORKING_SCENE_PROMPTS.md
│   │   ├── 07_generated/
│   │   │   ├── canon_tests/
│   │   │   │   ├── 01_neutral_studio_portrait/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── ANDREY_JUNIOR_test01_neutral_studio_portrait_v1_APPROVED.png
│   │   │   │   ├── 02_full_body_studio/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── ANDREY_JUNIOR_test02_full_body_studio_v1_APPROVED.png
│   │   │   │   ├── 03_athletic_gym_identity/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── ANDREY_JUNIOR_test03_athletic_gym_identity_v1_APPROVED.png
│   │   │   │   ├── 04_casual_outfit/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── ANDREY_JUNIOR_test04_casual_outfit_v1_APPROVED.png
│   │   │   │   ├── 05_scale_compact_body_check/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── ANDREY_JUNIOR_test05_scale_compact_body_check_v1_APPROVED.png
│   │   │   │   ├── 06_father_son_scale_check/
│   │   │   │   │   └── ANDREY_JUNIOR_test06_father_son_scale_check_v2_APPROVED.png
│   │   │   │   ├── 07_father_son_casual_outdoor/
│   │   │   │   │   └── ANDREY_JUNIOR_test07_father_son_casual_outdoor_v1_APPROVED.png
│   │   │   │   ├── 08_father_son_home_conversation/
│   │   │   │   │   └── ANDREY_JUNIOR_test08_father_son_home_conversation_v1_APPROVED.png
│   │   │   │   ├── 09_father_son_training_coaching/
│   │   │   │   │   └── ANDREY_JUNIOR_test09_father_son_training_coaching_v1_APPROVED.png
│   │   │   │   └── .gitkeep
│   │   │   ├── drafts/
│   │   │   │   └── .gitkeep
│   │   │   ├── rejected/
│   │   │   │   └── .gitkeep
│   │   │   └── .gitkeep
│   │   ├── 08_video_refs/
│   │   │   └── .gitkeep
│   │   ├── 09_blender/
│   │   │   └── .gitkeep
│   │   ├── 10_notes/
│   │   │   ├── .gitkeep
│   │   │   ├── ANDREY_JUNIOR_CANON_INDEX.md
│   │   │   ├── ANDREY_JUNIOR_CANON_INDEX.md.backup_20260704_150852
│   │   │   ├── ANDREY_JUNIOR_CANON_INDEX.md.backup_20260706_083029
│   │   │   ├── ANDREY_JUNIOR_IDENTITY_DRAFT.md
│   │   │   ├── ANDREY_JUNIOR_IDENTITY_DRAFT.md.backup_20260704_150852
│   │   │   ├── ANDREY_JUNIOR_IDENTITY_DRAFT.md.backup_20260706_083029
│   │   │   ├── ANDREY_JUNIOR_REFERENCE_PRESETS.json
│   │   │   ├── ANDREY_JUNIOR_REFERENCE_PRESETS.json.backup_20260704_150852
│   │   │   ├── ANDREY_JUNIOR_REFERENCE_PRESETS.json.backup_20260706_083029
│   │   │   ├── ANDREY_JUNIOR_REFERENCE_PRESETS.json.backup_20260709_092657
│   │   │   ├── ANDREY_JUNIOR_TEST_RESULTS.md
│   │   │   ├── ANDREY_JUNIOR_TEST_RESULTS.md.backup_20260704_150852
│   │   │   └── ANDREY_JUNIOR_TEST_RESULTS.md.backup_20260706_083029
│   │   └── .gitkeep
│   ├── EGOR/
│   │   ├── 01_refs_raw/
│   │   │   ├── .gitkeep
│   │   │   ├── EGOR_RAW_01_body_multiangle_burgundy.png
│   │   │   ├── EGOR_RAW_02_face_bar_burgundy.jpg
│   │   │   ├── EGOR_RAW_03_duo_couch.png
│   │   │   ├── EGOR_RAW_04_duo_pillar.png
│   │   │   └── EGOR_RAW_05_duo_close.png
│   │   ├── 02_best_refs/
│   │   │   └── .gitkeep
│   │   ├── 03_face_sheet/
│   │   │   ├── expressions/
│   │   │   │   ├── .gitkeep
│   │   │   │   └── EGOR_expressions_v1_sheet_A_APPROVED.png
│   │   │   └── EGOR_face_canon_v1_sheet_A_APPROVED.png
│   │   ├── 04_body_sheet/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   └── EGOR_body_canon_v1_sheet_A_front_side_back_APPROVED.png
│   │   ├── 05_outfits/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   ├── casual/
│   │   │   │   └── .gitkeep
│   │   │   ├── evening_dress/
│   │   │   │   └── .gitkeep
│   │   │   ├── formal/
│   │   │   │   └── .gitkeep
│   │   │   ├── scene_outfits/
│   │   │   │   └── .gitkeep
│   │   │   └── sports_look/
│   │   │       └── .gitkeep
│   │   ├── 06_prompts/
│   │   │   ├── .gitkeep
│   │   │   ├── EGOR_CANON_GENERATION_PROMPTS.txt
│   │   │   ├── EGOR_PROMPT_INDEX.md
│   │   │   ├── EGOR_PROMPT_RUN_LOG.jsonl
│   │   │   └── EGOR_WORKING_SCENE_PROMPTS.md
│   │   ├── 07_generated/
│   │   │   ├── canon_tests/
│   │   │   │   ├── 01_evening_embankment/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── EGOR_test02_evening_embankment_v1_APPROVED.png
│   │   │   │   ├── 02_sports_yoga/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── EGOR_test03_sports_yoga_v1_APPROVED.png
│   │   │   │   └── 03_portrait_expression/
│   │   │   │       ├── .gitkeep
│   │   │   │       └── EGOR_test01_neutral_portrait_v1_APPROVED.png
│   │   │   ├── drafts/
│   │   │   │   └── .gitkeep
│   │   │   └── rejected/
│   │   │       └── .gitkeep
│   │   ├── 08_masks/
│   │   │   └── .gitkeep
│   │   ├── 09_blender/
│   │   │   └── .gitkeep
│   │   └── 10_notes/
│   │       ├── .gitkeep
│   │       ├── EGOR_CANON_INDEX.md
│   │       ├── EGOR_REFERENCE_PRESETS.json
│   │       └── EGOR_TEST_RESULTS.md
│   ├── KIRA/
│   │   ├── 01_refs_raw/
│   │   │   └── .gitkeep
│   │   ├── 02_best_refs/
│   │   │   └── .gitkeep
│   │   ├── 03_face_sheet/
│   │   │   ├── expressions/
│   │   │   │   ├── KIRA_expressions_v1_sheet_A_emotional.png
│   │   │   │   └── KIRA_expressions_v1_sheet_B_emotional.png
│   │   │   ├── KIRA_face_canon_sheet_A.png
│   │   │   └── KIRA_face_canon_sheet_B.png
│   │   ├── 04_body_sheet/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   ├── KIRA_BODY_CANON_v4_sheet_A_4views.png
│   │   │   └── KIRA_BODY_CANON_v4_sheet_B_4views.png
│   │   ├── 05_outfits/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   ├── casual/
│   │   │   │   └── .gitkeep
│   │   │   ├── evening_dress/
│   │   │   │   ├── candidates/
│   │   │   │   │   ├── KIRA_evening_dress_v2_sheet_A_fullbody_4plus_candidate.png
│   │   │   │   │   └── KIRA_evening_dress_v2_sheet_B_portraits_4plus_candidate.png
│   │   │   │   ├── KIRA_evening_dress_FINAL_sheet_A_fullbody.png
│   │   │   │   ├── KIRA_evening_dress_FINAL_sheet_B_portraits.png
│   │   │   │   ├── KIRA_evening_dress_v1_sheet_A_fullbody.png
│   │   │   │   └── KIRA_evening_dress_v1_sheet_B_fullbody.png
│   │   │   ├── formal/
│   │   │   │   └── .gitkeep
│   │   │   ├── scene_outfits/
│   │   │   │   └── .gitkeep
│   │   │   └── sports_look/
│   │   │       ├── KIRA_sports_look_v1_sheet_A_front_side_back.png
│   │   │       └── KIRA_sports_look_v1_sheet_B_3q_action_portrait.png
│   │   ├── 06_prompts/
│   │   │   ├── create_kira_prompt_kit.ps1.txt
│   │   │   ├── KIRA_BASE_PROMPT.txt
│   │   │   ├── KIRA_BASE_PROMPT.txt.backup_20260707_153812
│   │   │   ├── KIRA_EVENING_SCENE_PROMPT.txt
│   │   │   ├── KIRA_EVENING_SCENE_PROMPT.txt.backup_20260707_153812
│   │   │   ├── KIRA_NEGATIVE_PROMPT.txt
│   │   │   ├── KIRA_NEGATIVE_PROMPT.txt.backup_20260707_153812
│   │   │   ├── KIRA_PROMPT_INDEX.md
│   │   │   ├── KIRA_PROMPT_RUN_LOG.jsonl
│   │   │   ├── KIRA_SPORTS_SCENE_PROMPT.txt
│   │   │   ├── KIRA_SPORTS_SCENE_PROMPT.txt.backup_20260707_153812
│   │   │   └── KIRA_WORKING_SCENE_PROMPTS.md
│   │   ├── 07_generated/
│   │   │   ├── canon_tests/
│   │   │   │   ├── 01_evening_embankment/
│   │   │   │   │   ├── KIRA_test01_evening_embankment_v1.png
│   │   │   │   │   ├── KIRA_test01_evening_embankment_v2_MAIN.png
│   │   │   │   │   └── KIRA_test01_evening_embankment_v3_ALT_cinematic.png
│   │   │   │   ├── 02_sports_yoga/
│   │   │   │   │   ├── KIRA_test02_sports_yoga_v1.png
│   │   │   │   │   ├── KIRA_test02_sports_yoga_v2_MAIN.png
│   │   │   │   │   └── KIRA_test02_sports_yoga_v3_ALT_stretch.png
│   │   │   │   └── 03_portrait_expression/
│   │   │   │       └── KIRA_test02_bar_romance_v1_APPROVED.png
│   │   │   ├── drafts/
│   │   │   │   └── .gitkeep
│   │   │   ├── rejected/
│   │   │   │   └── .gitkeep
│   │   │   ├── 317946af-4d80-4e9a-8b97-c469551e0235.png
│   │   │   ├── 9f28dfea-0aaa-4dee-831a-0a18004e2a7e.png
│   │   │   └── f7d3091b-c9ce-4ccc-878a-596980ce5231.png
│   │   ├── 08_masks/
│   │   │   └── .gitkeep
│   │   ├── 09_blender/
│   │   │   └── .gitkeep
│   │   └── 10_notes/
│   │       ├── KIRA_APPROVAL_CRITERIA.md.txt
│   │       ├── KIRA_APPROVAL_CRITERIA_ENG.md.txt
│   │       ├── KIRA_CANON_APPROVAL_WORKSHEET.md
│   │       ├── KIRA_CANON_INDEX.md.txt
│   │       ├── KIRA_CANON_INDEX.md.txt.backup_20260707_153909
│   │       ├── KIRA_IDENTITY.txt.txt
│   │       ├── KIRA_IDENTITY.txt.txt.backup_20260707_154006
│   │       ├── KIRA_REFERENCE_PRESETS.json
│   │       ├── KIRA_REFERENCE_PRESETS.json.backup_20260707_153832
│   │       ├── KIRA_REFERENCE_PRESETS.json.backup_20260709_092657
│   │       ├── KIRA_TEST_RESULTS.md.txt
│   │       ├── KIRA_TEST_RESULTS.md.txt.backup_20260702_231620
│   │       └── KIRA_TEST_RESULTS.md.txt.backup_20260707_153909
│   ├── MAKSIM/
│   │   ├── 01_refs_raw/
│   │   │   └── .gitkeep
│   │   ├── 02_best_refs/
│   │   │   └── .gitkeep
│   │   ├── 03_face_sheet/
│   │   │   └── expressions/
│   │   │       └── .gitkeep
│   │   ├── 04_body_sheet/
│   │   │   └── candidates/
│   │   │       └── .gitkeep
│   │   ├── 05_outfits/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   ├── casual/
│   │   │   │   └── .gitkeep
│   │   │   ├── evening_dress/
│   │   │   │   └── .gitkeep
│   │   │   ├── formal/
│   │   │   │   └── .gitkeep
│   │   │   ├── scene_outfits/
│   │   │   │   └── .gitkeep
│   │   │   └── sports_look/
│   │   │       └── .gitkeep
│   │   ├── 06_prompts/
│   │   │   ├── .gitkeep
│   │   │   └── MAKSIM_CANON_GENERATION_PROMPTS.txt
│   │   ├── 07_generated/
│   │   │   ├── canon_tests/
│   │   │   │   ├── 01_evening_embankment/
│   │   │   │   │   └── .gitkeep
│   │   │   │   ├── 02_sports_yoga/
│   │   │   │   │   └── .gitkeep
│   │   │   │   └── 03_portrait_expression/
│   │   │   │       └── .gitkeep
│   │   │   ├── drafts/
│   │   │   │   └── .gitkeep
│   │   │   └── rejected/
│   │   │       └── .gitkeep
│   │   ├── 08_masks/
│   │   │   └── .gitkeep
│   │   ├── 09_blender/
│   │   │   └── .gitkeep
│   │   └── 10_notes/
│   │       ├── .gitkeep
│   │       └── MAKSIM_REFERENCE_PRESETS.json
│   ├── MARINA/
│   │   ├── 01_refs_raw/
│   │   │   └── .gitkeep
│   │   ├── 02_best_refs/
│   │   │   └── .gitkeep
│   │   ├── 03_face_sheet/
│   │   │   ├── expressions/
│   │   │   │   ├── .gitkeep
│   │   │   │   ├── MARINA_expressions_v1_sheet_A_APPROVED.png
│   │   │   │   ├── MARINA_expressions_v1_sheet_B_SUPPORT.png
│   │   │   │   ├── MARINA_expressions_v1_sheet_C_SUPPORT.png
│   │   │   │   ├── MARINA_expressions_v1_sheet_D_SUPPORT.png
│   │   │   │   ├── MARINA_expressions_v1_sheet_E_SUPPORT.png
│   │   │   │   └── MARINA_expressions_v1_sheet_F_SUPPORT.png
│   │   │   └── MARINA_face_canon_v1_sheet_A_APPROVED.png
│   │   ├── 04_body_sheet/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   └── MARINA_body_canon_v1_sheet_A_APPROVED.png
│   │   ├── 05_outfits/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   ├── casual/
│   │   │   │   └── .gitkeep
│   │   │   ├── evening_dress/
│   │   │   │   └── .gitkeep
│   │   │   ├── formal/
│   │   │   │   └── .gitkeep
│   │   │   ├── scene_outfits/
│   │   │   │   └── .gitkeep
│   │   │   ├── sports_look/
│   │   │   │   └── .gitkeep
│   │   │   ├── MARINA_outfit_evening_peach_v1_portrait_SUPPORT.png
│   │   │   ├── MARINA_outfit_evening_peach_v1_sheet_A_APPROVED.png
│   │   │   └── MARINA_outfit_warm_evening_v1_portrait_SUPPORT.png
│   │   ├── 06_prompts/
│   │   │   ├── .gitkeep
│   │   │   ├── MARINA_CANON_GENERATION_PROMPTS.txt
│   │   │   ├── MARINA_PROMPT_INDEX.md
│   │   │   ├── MARINA_PROMPT_RUN_LOG.jsonl
│   │   │   └── MARINA_WORKING_SCENE_PROMPTS.md
│   │   ├── 07_generated/
│   │   │   ├── canon_tests/
│   │   │   │   ├── 01_evening_embankment/
│   │   │   │   │   └── .gitkeep
│   │   │   │   ├── 02_sports_yoga/
│   │   │   │   │   └── .gitkeep
│   │   │   │   ├── 03_portrait_expression/
│   │   │   │   │   └── .gitkeep
│   │   │   │   ├── MARINA_test01_rainy_cafe_v1_APPROVED.png
│   │   │   │   ├── MARINA_test02_theater_melancholy_v1_APPROVED.png
│   │   │   │   ├── MARINA_test03_evening_city_balcony_v1_APPROVED.png
│   │   │   │   ├── MARINA_test04_autumn_street_portrait_v1_APPROVED.png
│   │   │   │   ├── MARINA_test05_morning_pajamas_v1_APPROVED.png
│   │   │   │   ├── MARINA_test06_white_garden_formal_v1_APPROVED.png
│   │   │   │   └── MARINA_test07_pool_sunset_v1_APPROVED.png
│   │   │   ├── drafts/
│   │   │   │   └── .gitkeep
│   │   │   └── rejected/
│   │   │       └── .gitkeep
│   │   ├── 08_masks/
│   │   │   └── .gitkeep
│   │   ├── 09_blender/
│   │   │   └── .gitkeep
│   │   └── 10_notes/
│   │       ├── .gitkeep
│   │       ├── MARINA_CANON_INDEX.md
│   │       ├── MARINA_REFERENCE_PRESETS.json
│   │       └── MARINA_TEST_RESULTS.md
│   ├── NIKA/
│   │   ├── 01_refs_raw/
│   │   │   ├── .gitkeep
│   │   │   ├── NIKA_RAW_01_face_main_burgundy_expressions.png
│   │   │   ├── NIKA_RAW_02_body_main_burgundy_multiview.png
│   │   │   ├── NIKA_RAW_03_body_support_gym_multiview.png
│   │   │   ├── NIKA_RAW_04_style_main_burgundy_bar.png
│   │   │   ├── NIKA_RAW_05_formal_support_burgundy_sheet.png
│   │   │   └── NIKA_RAW_06_sports_support_gym_leggings.png
│   │   ├── 02_best_refs/
│   │   │   └── .gitkeep
│   │   ├── 03_face_sheet/
│   │   │   ├── expressions/
│   │   │   │   ├── .gitkeep
│   │   │   │   ├── NIKA_expressions_v1_sheet_A_APPROVED.png
│   │   │   │   └── NIKA_expressions_v1_sheet_A_attempt03_REVISE.png
│   │   │   └── NIKA_face_canon_v1_sheet_A_APPROVED.png
│   │   ├── 04_body_sheet/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   ├── NIKA_body_canon_v1_sheet_A_front_side_back_APPROVED.png
│   │   │   └── NIKA_body_canon_v1_sheet_B_pose_variations_APPROVED.png
│   │   ├── 05_outfits/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   ├── casual/
│   │   │   │   └── .gitkeep
│   │   │   ├── evening_dress/
│   │   │   │   └── .gitkeep
│   │   │   ├── formal/
│   │   │   │   └── .gitkeep
│   │   │   ├── scene_outfits/
│   │   │   │   └── .gitkeep
│   │   │   └── sports_look/
│   │   │       └── .gitkeep
│   │   ├── 06_prompts/
│   │   │   ├── .gitkeep
│   │   │   ├── NIKA_CANON_GENERATION_PROMPTS.txt
│   │   │   ├── NIKA_PROMPT_INDEX.md
│   │   │   ├── NIKA_PROMPT_RUN_LOG.jsonl
│   │   │   └── NIKA_WORKING_SCENE_PROMPTS.md
│   │   ├── 07_generated/
│   │   │   ├── canon_tests/
│   │   │   │   ├── 01_evening_embankment/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── NIKA_test02_evening_embankment_v1_APPROVED.png
│   │   │   │   ├── 02_sports_yoga/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── NIKA_test03_sports_yoga_v1_APPROVED.png
│   │   │   │   └── 03_portrait_expression/
│   │   │   │       ├── .gitkeep
│   │   │   │       ├── NIKA_test01_neutral_portrait_v1_APPROVED.png
│   │   │   │       └── NIKA_test01_neutral_portrait_v2_APPROVED.png
│   │   │   ├── drafts/
│   │   │   │   ├── .gitkeep
│   │   │   │   ├── NIKA_body_canon_v1_attempt01_REVISE.png
│   │   │   │   └── NIKA_body_canon_v1_attempt02_REVISE.png
│   │   │   └── rejected/
│   │   │       └── .gitkeep
│   │   ├── 08_masks/
│   │   │   └── .gitkeep
│   │   ├── 09_blender/
│   │   │   └── .gitkeep
│   │   └── 10_notes/
│   │       ├── .gitkeep
│   │       ├── NIKA_CANON_INDEX.md
│   │       ├── NIKA_REFERENCE_PRESETS.json
│   │       └── NIKA_TEST_RESULTS.md
│   ├── OLGA/
│   │   ├── 01_refs_raw/
│   │   │   └── .gitkeep
│   │   ├── 02_best_refs/
│   │   │   └── .gitkeep
│   │   ├── 02_refs_selected/
│   │   │   ├── .gitkeep
│   │   │   └── OLGA_ref_face_primary_v1_SELECTED.jpg
│   │   ├── 03_face_sheet/
│   │   │   ├── expressions/
│   │   │   │   ├── .gitkeep
│   │   │   │   └── OLGA_expressions_v1_sheet_A_APPROVED.png
│   │   │   ├── .gitkeep
│   │   │   └── OLGA_face_canon_v1_sheet_A_APPROVED.png
│   │   ├── 04_body_sheet/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   ├── .gitkeep
│   │   │   ├── OLGA_body_canon_v1_sheet_A_front_side_back_APPROVED.png
│   │   │   └── OLGA_body_canon_v1_sheet_B_pose_variations_APPROVED.png
│   │   ├── 05_outfits/
│   │   │   ├── candidates/
│   │   │   │   └── .gitkeep
│   │   │   ├── casual/
│   │   │   │   └── .gitkeep
│   │   │   ├── evening_dress/
│   │   │   │   └── .gitkeep
│   │   │   ├── formal/
│   │   │   │   └── .gitkeep
│   │   │   ├── scene_outfits/
│   │   │   │   └── .gitkeep
│   │   │   ├── sports_look/
│   │   │   │   └── .gitkeep
│   │   │   └── .gitkeep
│   │   ├── 06_prompts/
│   │   │   ├── .gitkeep
│   │   │   ├── OLGA_CANON_GENERATION_PROMPTS.txt
│   │   │   ├── OLGA_POOL_SCENE_PROMPT.md
│   │   │   ├── OLGA_PROMPT_INDEX.md
│   │   │   ├── OLGA_PROMPT_INDEX.md.backup_20260705_234153
│   │   │   ├── OLGA_PROMPT_RUN_LOG.jsonl
│   │   │   ├── OLGA_PROMPT_RUN_LOG.jsonl.backup_20260705_234153
│   │   │   ├── OLGA_WORKING_SCENE_PROMPTS.md
│   │   │   ├── OLGA_WORKING_SCENE_PROMPTS.md.backup_20260705_234153
│   │   │   └── OLGA_WORKING_SCENE_PROMPTS_V2.md
│   │   ├── 07_generated/
│   │   │   ├── canon_tests/
│   │   │   │   ├── 01_evening_embankment/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── OLGA_test01_evening_embankment_v1_APPROVED.png
│   │   │   │   ├── 02_sports_yoga/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── OLGA_test02_sports_yoga_v1_APPROVED.png
│   │   │   │   ├── 03_portrait_expression/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── OLGA_test03_portrait_expression_v1_APPROVED.png
│   │   │   │   ├── 04_outdoor_walk_with_andrey_junior/
│   │   │   │   │   └── OLGA_test04_outdoor_walk_with_andrey_junior_v1_APPROVED.png
│   │   │   │   ├── 05_business_interior/
│   │   │   │   │   └── OLGA_test05_business_interior_v1_APPROVED.png
│   │   │   │   ├── 06_indoor_lounge_conversation_with_andrey_junior/
│   │   │   │   │   └── OLGA_test06_indoor_lounge_conversation_with_andrey_junior_v1_APPROVED.png
│   │   │   │   ├── 07_pool_wellness_solo/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── OLGA_test07_pool_wellness_solo_v1_APPROVED.png
│   │   │   │   ├── 08_dalle_evening_embankment/
│   │   │   │   │   ├── .gitkeep
│   │   │   │   │   └── OLGA_test08_dalle_evening_embankment_v1_APPROVED.png
│   │   │   │   ├── 09_formal_elegant/
│   │   │   │   │   └── OLGA_test09_formal_elegant_v4_APPROVED.png
│   │   │   │   ├── 10_neutral_height_scale_check/
│   │   │   │   │   └── OLGA_test10_neutral_height_scale_check_v1_APPROVED.png
│   │   │   │   └── .gitkeep
│   │   │   ├── drafts/
│   │   │   │   └── .gitkeep
│   │   │   ├── rejected/
│   │   │   │   └── .gitkeep
│   │   │   └── .gitkeep
│   │   ├── 08_masks/
│   │   │   └── .gitkeep
│   │   ├── 08_rejected/
│   │   │   ├── .gitkeep
│   │   │   └── OLGA_business_interior_raw_1_unlabeled_REJECTED.png
│   │   ├── 09_blender/
│   │   │   └── .gitkeep
│   │   ├── 09_exports/
│   │   │   └── .gitkeep
│   │   ├── 10_notes/
│   │   │   ├── .gitkeep
│   │   │   ├── OLGA_CANON_INDEX.md
│   │   │   ├── OLGA_CANON_INDEX.md.backup_20260705_162431
│   │   │   ├── OLGA_CANON_INDEX.md.backup_20260705_234259
│   │   │   ├── OLGA_IDENTITY_DRAFT.md
│   │   │   ├── OLGA_IDENTITY_DRAFT.md.backup_20260705_162431
│   │   │   ├── OLGA_REFERENCE_PRESETS.json
│   │   │   ├── OLGA_REFERENCE_PRESETS.json.backup_20260705_162431
│   │   │   ├── OLGA_REFERENCE_PRESETS.json.backup_20260705_234259
│   │   │   ├── OLGA_REFERENCE_PRESETS.json.backup_20260709_092657
│   │   │   ├── OLGA_TEST_RESULTS.md
│   │   │   ├── OLGA_TEST_RESULTS.md.backup_20260705_162431
│   │   │   └── OLGA_TEST_RESULTS.md.backup_20260705_234259
│   │   └── .gitkeep
│   └── SERGEY/
│       ├── 01_refs_raw/
│       │   └── .gitkeep
│       ├── 02_best_refs/
│       │   └── .gitkeep
│       ├── 03_face_sheet/
│       │   └── expressions/
│       │       └── .gitkeep
│       ├── 04_body_sheet/
│       │   └── candidates/
│       │       └── .gitkeep
│       ├── 05_outfits/
│       │   ├── candidates/
│       │   │   └── .gitkeep
│       │   ├── casual/
│       │   │   └── .gitkeep
│       │   ├── evening_dress/
│       │   │   └── .gitkeep
│       │   ├── formal/
│       │   │   └── .gitkeep
│       │   ├── scene_outfits/
│       │   │   └── .gitkeep
│       │   └── sports_look/
│       │       └── .gitkeep
│       ├── 06_prompts/
│       │   ├── .gitkeep
│       │   └── SERGEY_CANON_GENERATION_PROMPTS.txt
│       ├── 07_generated/
│       │   ├── canon_tests/
│       │   │   ├── 01_evening_embankment/
│       │   │   │   └── .gitkeep
│       │   │   ├── 02_sports_yoga/
│       │   │   │   └── .gitkeep
│       │   │   └── 03_portrait_expression/
│       │   │       └── .gitkeep
│       │   ├── drafts/
│       │   │   └── .gitkeep
│       │   └── rejected/
│       │       └── .gitkeep
│       ├── 08_masks/
│       │   └── .gitkeep
│       ├── 09_blender/
│       │   └── .gitkeep
│       └── 10_notes/
│           ├── .gitkeep
│           └── SERGEY_REFERENCE_PRESETS.json
├── configs/
│   └── visual_canon/
│       ├── character_bootstrap.schema.json
│       ├── character_manifest.schema.json
│       ├── deployment_request.schema.json
│       ├── pipeline_policy.json
│       └── prompt_record.schema.json
├── docs/
│   ├── GITHUB_REFERENCE_PACK_WORKFLOW.md
│   ├── NCC_DEPLOY_CHECKLIST.md
│   ├── NCC_FOLDER_MAP.md
│   ├── NCC_VISUAL_CANON_WORKFLOW.md
│   ├── PROJECT_DOCUMENTATION_INDEX.md
│   ├── VOYAGE_INTEGRATION_WORKFLOW.md
│   └── VOYAGE_SQLITE_MEMORY_WORKFLOW.md
├── tests/
│   └── visual_canon/
│       ├── __pycache__/
│       │   ├── deploy_test_support.cpython-314.pyc
│       │   ├── test_bootstrap_character.cpython-314.pyc
│       │   ├── test_cline_reference_import_skill.cpython-314.pyc
│       │   ├── test_deploy_visual_canon_apply.cpython-314.pyc
│       │   ├── test_deploy_visual_canon_authority.cpython-314.pyc
│       │   ├── test_deploy_visual_canon_cli.cpython-314.pyc
│       │   ├── test_deploy_visual_canon_concurrency.cpython-314.pyc
│       │   ├── test_deploy_visual_canon_dry_run.cpython-314.pyc
│       │   ├── test_deploy_visual_canon_rollback.cpython-314.pyc
│       │   ├── test_validator_cli.cpython-314.pyc
│       │   ├── test_validator_discovery.cpython-314.pyc
│       │   ├── test_validator_legacy_compatibility.cpython-314.pyc
│       │   └── test_validator_prompt_records.cpython-314.pyc
│       ├── fixtures/
│       │   ├── invalid_duplicate_id/
│       │   │   └── prompt_run_log.jsonl
│       │   ├── invalid_empty_prompt/
│       │   │   └── prompt_run_log.jsonl
│       │   ├── invalid_jsonl/
│       │   │   └── prompt_run_log.jsonl
│       │   ├── invalid_local_only_leak/
│       │   │   └── prompt_run_log.jsonl
│       │   ├── invalid_missing_reference/
│       │   │   └── prompt_run_log.jsonl
│       │   ├── invalid_mojibake/
│       │   │   └── prompt_run_log.jsonl
│       │   ├── invalid_multiple_main/
│       │   │   └── prompt_run_log.jsonl
│       │   ├── invalid_selected_without_approval/
│       │   │   └── prompt_run_log.jsonl
│       │   ├── invalid_variant_in_id/
│       │   │   └── prompt_run_log.jsonl
│       │   ├── valid_legacy/
│       │   │   └── prompt_run_log.jsonl
│       │   └── valid_strict/
│       │       └── prompt_run_log.jsonl
│       ├── deploy_test_support.py
│       ├── test_bootstrap_character.py
│       ├── test_cline_reference_import_skill.py
│       ├── test_deploy_visual_canon_apply.py
│       ├── test_deploy_visual_canon_authority.py
│       ├── test_deploy_visual_canon_cli.py
│       ├── test_deploy_visual_canon_concurrency.py
│       ├── test_deploy_visual_canon_dry_run.py
│       ├── test_deploy_visual_canon_rollback.py
│       ├── test_validator_cli.py
│       ├── test_validator_discovery.py
│       ├── test_validator_legacy_compatibility.py
│       └── test_validator_prompt_records.py
├── tools/
│   ├── __pycache__/
│   │   ├── bootstrap_character.cpython-314.pyc
│   │   ├── deploy_visual_canon_result.cpython-314.pyc
│   │   └── validate_visual_canon_pipeline.cpython-314.pyc
│   ├── bootstrap_character.py
│   ├── build_scene_reference_pack.ps1
│   ├── build_scene_reference_pack.py
│   ├── deploy_visual_canon_result.py
│   ├── generate_inventory.py
│   ├── validate_visual_canon_pipeline.py
│   ├── voyage_memory_export.py
│   ├── voyage_memory_init.py
│   ├── voyage_memory_record.py
│   └── voyage_memory_status.py
├── .gitattributes
├── .gitignore
├── AGENTS.md
├── INVENTORY.md
├── INVENTORY.md.backup_20260703_125505
├── INVENTORY.md.backup_20260703_160011
├── INVENTORY.md.backup_20260704_151411
├── INVENTORY.md.backup_20260704_160831
├── INVENTORY.md.backup_20260705_163018
├── INVENTORY.md.backup_20260709_101916
├── INVENTORY.md.backup_20260710_123336
├── INVENTORY.md.backup_20260710_152700
├── INVENTORY.md.backup_20260711_082946
├── INVENTORY.md.backup_20260712_183037
├── INVENTORY.md.backup_20260719_141209
├── PHASE_1_CURRENT_LAPTOP_CLOUD_PIPELINE.md
├── PHASE_2_LOCAL_AI_WORKSTATION_PIPELINE.md
├── README.md
├── repo_audit.txt
├── ROADMAP.md
└── UNIFIED_CANON_TESTS_TEMPLATE.md
```

# Total file count

574

# File type summary

| Extension | Count |
|---|---:|
| (no extension) | 190 |
| .backup_20260630_085458 | 1 |
| .backup_20260702_231620 | 1 |
| .backup_20260702_231625 | 1 |
| .backup_20260703_124946 | 7 |
| .backup_20260703_125505 | 1 |
| .backup_20260703_155641 | 3 |
| .backup_20260703_160011 | 1 |
| .backup_20260704_150852 | 5 |
| .backup_20260704_151046 | 3 |
| .backup_20260704_151411 | 1 |
| .backup_20260704_160529 | 3 |
| .backup_20260704_160831 | 1 |
| .backup_20260705_162431 | 4 |
| .backup_20260705_162559 | 3 |
| .backup_20260705_163018 | 1 |
| .backup_20260705_234153 | 3 |
| .backup_20260705_234259 | 3 |
| .backup_20260705_234357 | 1 |
| .backup_20260705_234423 | 2 |
| .backup_20260706_083029 | 8 |
| .backup_20260706_115144 | 6 |
| .backup_20260707_153812 | 4 |
| .backup_20260707_153832 | 1 |
| .backup_20260707_153909 | 2 |
| .backup_20260707_154006 | 1 |
| .backup_20260707_154019 | 3 |
| .backup_20260709_092657 | 4 |
| .backup_20260709_101916 | 1 |
| .backup_20260710_123336 | 1 |
| .backup_20260710_152700 | 1 |
| .backup_20260711_082946 | 1 |
| .backup_20260712_183037 | 1 |
| .backup_20260719_141209 | 1 |
| .jpg | 3 |
| .json | 20 |
| .jsonl | 19 |
| .md | 65 |
| .png | 130 |
| .ps1 | 1 |
| .py | 23 |
| .pyc | 17 |
| .txt | 26 |

# File list

| Path | Size bytes | Modified |
|---|---:|---|
| .claude/settings.json | 157 | 2026-07-13 23:03:10 |
| .cline/skills/ncc-reference-import/scripts/__pycache__/import_references.cpython-314.pyc | 28524 | 2026-07-19 14:14:56 |
| .cline/skills/ncc-reference-import/scripts/import_references.py | 18790 | 2026-07-19 14:04:58 |
| .cline/skills/ncc-reference-import/SKILL.md | 2968 | 2026-07-19 14:03:41 |
| .cline/skills/ncc-reference-import/templates/reference-import-task.example.json | 770 | 2026-07-19 14:05:35 |
| .clinerules/00-ncc-project-boundary.md | 1176 | 2026-07-19 14:02:49 |
| .clinerules/10-ncc-git-safety.md | 1388 | 2026-07-19 14:02:58 |
| .clinerules/20-ncc-visual-assets.md | 1518 | 2026-07-19 14:03:08 |
| .clinerules/30-ncc-task-discipline.md | 1165 | 2026-07-19 14:03:16 |
| .gitattributes | 303 | 2026-07-21 18:18:06 |
| .gitignore | 147 | 2026-07-12 22:06:08 |
| .voyage/CHARACTER_REGISTRY.md | 4410 | 2026-07-24 13:58:57 |
| .voyage/CHARACTER_REGISTRY.md.backup_20260703_124946 | 2920 | 2026-07-03 12:49:47 |
| .voyage/CHARACTER_REGISTRY.md.backup_20260703_155641 | 2956 | 2026-07-03 15:56:41 |
| .voyage/CHARACTER_REGISTRY.md.backup_20260704_151046 | 3142 | 2026-07-04 15:10:46 |
| .voyage/CHARACTER_REGISTRY.md.backup_20260704_160529 | 3189 | 2026-07-04 16:05:29 |
| .voyage/CHARACTER_REGISTRY.md.backup_20260705_162559 | 3394 | 2026-07-05 16:25:59 |
| .voyage/CHARACTER_REGISTRY.md.backup_20260705_234357 | 3423 | 2026-07-05 23:43:57 |
| .voyage/CHARACTER_REGISTRY.md.backup_20260706_083029 | 3219 | 2026-07-06 08:30:30 |
| .voyage/CHARACTER_REGISTRY.md.backup_20260706_115144 | 3268 | 2026-07-06 11:51:44 |
| .voyage/CHARACTER_REGISTRY.md.backup_20260707_154019 | 3312 | 2026-07-07 15:40:19 |
| .voyage/CONTEXT_SNAPSHOT.md | 3182 | 2026-07-07 15:44:38 |
| .voyage/CURRENT_TASK.md | 42210 | 2026-07-20 21:39:08 |
| .voyage/CURRENT_TASK.md.backup_20260703_124946 | 6168 | 2026-07-03 12:49:47 |
| .voyage/CURRENT_TASK.md.backup_20260703_155641 | 6572 | 2026-07-03 15:56:41 |
| .voyage/CURRENT_TASK.md.backup_20260704_151046 | 7311 | 2026-07-04 15:10:46 |
| .voyage/CURRENT_TASK.md.backup_20260704_160529 | 8013 | 2026-07-04 16:05:29 |
| .voyage/CURRENT_TASK.md.backup_20260705_162559 | 8743 | 2026-07-05 16:25:59 |
| .voyage/CURRENT_TASK.md.backup_20260705_234423 | 9571 | 2026-07-05 23:44:23 |
| .voyage/CURRENT_TASK.md.backup_20260706_083029 | 11000 | 2026-07-06 08:30:29 |
| .voyage/CURRENT_TASK.md.backup_20260706_115144 | 12381 | 2026-07-06 11:51:44 |
| .voyage/CURRENT_TASK.md.backup_20260707_154019 | 13548 | 2026-07-07 15:40:19 |
| .voyage/DECISIONS.md | 78477 | 2026-07-20 21:38:34 |
| .voyage/DECISIONS.md.backup_20260702_231625 | 9474 | 2026-07-02 23:16:26 |
| .voyage/DECISIONS.md.backup_20260703_124946 | 14008 | 2026-07-03 12:49:47 |
| .voyage/DECISIONS.md.backup_20260703_155641 | 15978 | 2026-07-03 15:56:41 |
| .voyage/DECISIONS.md.backup_20260704_151046 | 16517 | 2026-07-04 15:10:46 |
| .voyage/DECISIONS.md.backup_20260704_160529 | 19455 | 2026-07-04 16:05:29 |
| .voyage/DECISIONS.md.backup_20260705_162559 | 20295 | 2026-07-05 16:25:59 |
| .voyage/DECISIONS.md.backup_20260705_234423 | 22526 | 2026-07-05 23:44:23 |
| .voyage/DECISIONS.md.backup_20260706_083029 | 24849 | 2026-07-06 08:30:30 |
| .voyage/DECISIONS.md.backup_20260706_115144 | 27453 | 2026-07-06 11:51:44 |
| .voyage/DECISIONS.md.backup_20260707_154019 | 30636 | 2026-07-07 15:40:19 |
| .voyage/EVENTS_EXPORT.jsonl | 36829 | 2026-07-07 15:44:38 |
| .voyage/LOCATION_REGISTRY.md | 871 | 2026-07-02 09:08:58 |
| .voyage/PROJECT_STATE.md | 7946 | 2026-07-24 13:59:12 |
| .voyage/README.md | 1635 | 2026-07-02 09:08:52 |
| .voyage/SCENE_REQUEST_RULES.md | 2099 | 2026-07-02 09:08:54 |
| .voyage/SQLITE_MEMORY_STATUS.md | 4577 | 2026-07-07 15:44:38 |
| .voyage/STATE_EXPORT.json | 93915 | 2026-07-07 15:44:38 |
| .vscode/settings.json | 4 | 2026-07-09 09:27:48 |
| AGENTS.md | 21043 | 2026-07-19 14:10:35 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/06_prompts/KIRA_ANDREY_DUO_SCENE_PACK_PROMPTS.txt | 7932 | 2026-07-03 02:16:30 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/01_neutral_studio_duo/.gitkeep | 0 | 2026-07-02 22:42:54 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/01_neutral_studio_duo/KIRA_ANDREY_joint_test01_neutral_studio_duo_v2_APPROVED.png | 2148429 | 2026-07-03 00:05:04 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/02_evening_embankment_duo/.gitkeep | 0 | 2026-07-02 22:42:55 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/02_evening_embankment_duo/KIRA_ANDREY_joint_test02_evening_embankment_duo_v1_APPROVED.png | 2259795 | 2026-07-03 00:24:35 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/03_warm_bar_conversation/.gitkeep | 0 | 2026-07-02 22:42:56 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/03_warm_bar_conversation/KIRA_ANDREY_joint_test03_warm_bar_conversation_v1_APPROVED.png | 2145535 | 2026-07-03 00:41:53 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/04_sea_yacht_mood_duo/.gitkeep | 0 | 2026-07-02 22:42:57 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/04_sea_yacht_mood_duo/KIRA_ANDREY_joint_test04_sea_yacht_mood_duo_v1_APPROVED.png | 2108540 | 2026-07-03 01:06:45 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/01_evening_embankment_walk/.gitkeep | 0 | 2026-07-03 02:15:48 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/01_evening_embankment_walk/KIRA_ANDREY_scene01_evening_embankment_walk_v1_APPROVED.png | 2266427 | 2026-07-03 07:20:27 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/02_warm_bar_dialogue/.gitkeep | 0 | 2026-07-03 02:15:50 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/02_warm_bar_dialogue/KIRA_ANDREY_scene02_warm_bar_dialogue_v1_APPROVED.png | 2082012 | 2026-07-03 07:37:27 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/03_yacht_sunset/.gitkeep | 0 | 2026-07-03 02:15:51 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/03_yacht_sunset/KIRA_ANDREY_scene03_yacht_sunset_v1_APPROVED.png | 2136480 | 2026-07-03 07:48:11 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/04_studio_character_poster/.gitkeep | 0 | 2026-07-03 02:15:52 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/04_studio_character_poster/KIRA_ANDREY_scene04_studio_character_poster_v1_APPROVED.png | 1893562 | 2026-07-03 08:38:13 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/05_rainy_city_street/.gitkeep | 0 | 2026-07-03 02:15:53 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/05_rainy_city_street/KIRA_ANDREY_scene05_rainy_city_street_v1_APPROVED.png | 2450287 | 2026-07-03 08:49:12 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/06_cozy_interior_conversation/.gitkeep | 0 | 2026-07-03 02:15:54 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/06_cozy_interior_conversation/KIRA_ANDREY_scene_pack06_cozy_interior_conversation_v4_APPROVED.png | 2126855 | 2026-07-03 11:41:24 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/candidates/.gitkeep | 0 | 2026-07-03 02:15:56 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/rejected/.gitkeep | 0 | 2026-07-03 02:15:55 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/10_notes/KIRA_ANDREY_DUO_SCENE_PACK_INDEX.md | 3366 | 2026-07-03 12:50:29 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/10_notes/KIRA_ANDREY_DUO_SCENE_PACK_INDEX.md.backup_20260703_124946 | 2367 | 2026-07-03 12:49:46 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/10_notes/KIRA_ANDREY_DUO_SCENE_PACK_RESULTS.md | 4033 | 2026-07-03 12:50:08 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/10_notes/KIRA_ANDREY_DUO_SCENE_PACK_RESULTS.md.backup_20260703_124946 | 1521 | 2026-07-03 12:49:46 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/10_notes/KIRA_ANDREY_DUO_SCENE_PACKS.json | 3971 | 2026-07-03 12:50:53 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/10_notes/KIRA_ANDREY_DUO_SCENE_PACKS.json.backup_20260703_124946 | 2849 | 2026-07-03 12:49:47 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/10_notes/KIRA_ANDREY_JOINT_CANON_INDEX.md | 2457 | 2026-07-03 01:21:35 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/10_notes/KIRA_ANDREY_JOINT_TEST_RESULTS.md | 3694 | 2026-07-03 01:21:20 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/10_notes/KIRA_ANDREY_REFERENCE_PRESETS.json | 4398 | 2026-07-03 12:51:20 |
| AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/10_notes/KIRA_ANDREY_REFERENCE_PRESETS.json.backup_20260703_124946 | 3093 | 2026-07-03 12:49:47 |
| AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_01_face_closeup_blue_shirt.png | 2169748 | 2026-06-25 21:12:14 |
| AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_02_yacht_sunset_blue_shirt.png | 2050416 | 2026-06-25 21:51:52 |
| AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_03_fullbody_studio_blue_shirt.png | 1908427 | 2026-06-25 20:54:30 |
| AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_04_bar_portrait_blue_shirt.png | 1983592 | 2026-06-26 08:11:40 |
| AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_05_main_identity_sheet_blue_shirt.png | 2058537 | 2026-06-20 22:19:34 |
| AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_06_formal_suit_walking.png | 1762429 | 2026-06-25 21:08:30 |
| AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_07_formal_suit_standing.png | 1785612 | 2026-06-25 20:54:36 |
| AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_08_expressions_sheet_A.png | 2352290 | 2026-06-25 21:24:00 |
| AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_09_expressions_sheet_B.png | 2392642 | 2026-06-25 21:31:18 |
| AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_10_sports_gym_black.png | 2195467 | 2026-06-26 12:43:12 |
| AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_11_body_identity_sheet_blue_shirt.png | 2023706 | 2026-06-25 21:02:34 |
| AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_12_kling_face_closeup_REFERENCE_ONLY.jpg | 98452 | 2026-06-20 20:20:44 |
| AI_CHARACTERS/ANDREY/02_best_refs/ANDREY_best_main_identity_sheet_v1.png.png | 2023706 | 2026-06-25 21:02:34 |
| AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_A_basic.png | 2365284 | 2026-06-30 22:22:05 |
| AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_B_angles.png | 2366781 | 2026-06-30 23:12:12 |
| AI_CHARACTERS/ANDREY/03_face_sheet/expressions/ANDREY_expressions_v1_sheet_C_refined.png | 2372255 | 2026-07-01 12:36:42 |
| AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_A_front_side_back.png | 1752758 | 2026-07-02 13:49:29 |
| AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_B_pose_variations.png | 1807220 | 2026-07-02 14:00:01 |
| AI_CHARACTERS/ANDREY/04_body_sheet/candidates/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/05_outfits/candidates/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/05_outfits/casual/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/05_outfits/evening_dress/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/05_outfits/formal/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/05_outfits/scene_outfits/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/05_outfits/sports_look/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/06_prompts/ANDREY_BODY_CANON_NEGATIVE_PROMPT.txt | 975 | 2026-07-02 10:19:06 |
| AI_CHARACTERS/ANDREY/06_prompts/ANDREY_BODY_CANON_PROMPT.txt | 6139 | 2026-07-02 10:18:54 |
| AI_CHARACTERS/ANDREY/06_prompts/ANDREY_CONTROL_TEST_PROMPTS.txt | 6948 | 2026-07-02 17:23:15 |
| AI_CHARACTERS/ANDREY/06_prompts/ANDREY_FACE_CANON_NEGATIVE_PROMPT.txt | 1016 | 2026-06-30 21:47:29 |
| AI_CHARACTERS/ANDREY/06_prompts/ANDREY_FACE_CANON_PROMPT.txt | 3934 | 2026-06-30 21:47:29 |
| AI_CHARACTERS/ANDREY/06_prompts/ANDREY_KIRA_JOINT_CONTROL_TEST_PROMPTS.txt | 4628 | 2026-07-02 22:43:27 |
| AI_CHARACTERS/ANDREY/06_prompts/ANDREY_PROMPT_INDEX.md | 4335 | 2026-07-06 11:55:05 |
| AI_CHARACTERS/ANDREY/06_prompts/ANDREY_PROMPT_RUN_LOG.jsonl | 8646 | 2026-07-06 11:55:05 |
| AI_CHARACTERS/ANDREY/06_prompts/ANDREY_WORKING_SCENE_PROMPTS.md | 16600 | 2026-07-06 11:55:05 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/01_evening_embankment/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/01_neutral_studio_portrait/.gitkeep | 0 | 2026-07-02 17:22:37 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/01_neutral_studio_portrait/ANDREY_test01_neutral_studio_portrait_v1.png | 2095075 | 2026-07-02 18:46:10 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/02_full_body_blue_shirt/.gitkeep | 0 | 2026-07-02 17:22:37 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/02_full_body_blue_shirt/ANDREY_test02_full_body_blue_shirt_studio_v1.png | 1781088 | 2026-07-02 19:35:32 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/02_sports_yoga/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/03_portrait_expression/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/03_warm_bar_portrait/.gitkeep | 0 | 2026-07-02 17:22:37 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/03_warm_bar_portrait/ANDREY_test03_warm_bar_portrait_v1.png | 2141345 | 2026-07-02 20:34:52 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/04_formal_evening_look/.gitkeep | 0 | 2026-07-02 17:22:37 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/04_formal_evening_look/ANDREY_test04_formal_evening_look_v1.png | 1846194 | 2026-07-02 20:51:29 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/05_sports_gym_identity/.gitkeep | 0 | 2026-07-02 17:22:37 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/05_sports_gym_identity/ANDREY_test05_sports_gym_identity_v1.png | 1920059 | 2026-07-02 21:03:32 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/06_sea_yacht_mood/.gitkeep | 0 | 2026-07-02 17:22:37 |
| AI_CHARACTERS/ANDREY/07_generated/canon_tests/06_sea_yacht_mood/ANDREY_test06_sea_yacht_mood_scene_v1.png | 2097881 | 2026-07-02 21:14:57 |
| AI_CHARACTERS/ANDREY/07_generated/drafts/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/07_generated/rejected/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/08_masks/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/09_blender/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_APPROVAL_WORKSHEET.md | 5495 | 2026-07-09 09:26:57 |
| AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_INDEX.md | 12170 | 2026-07-06 12:02:11 |
| AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_INDEX.md.backup_20260630_085458 | 9425 | 2026-06-30 08:48:46 |
| AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_INDEX.md.backup_20260706_115144 | 11601 | 2026-07-06 11:51:44 |
| AI_CHARACTERS/ANDREY/10_notes/ANDREY_IDENTITY.txt | 9304 | 2026-06-30 08:23:04 |
| AI_CHARACTERS/ANDREY/10_notes/ANDREY_RAW_FILE_MAP.md | 6599 | 2026-06-30 08:14:52 |
| AI_CHARACTERS/ANDREY/10_notes/ANDREY_REFERENCE_PRESETS.json | 8220 | 2026-07-09 09:26:57 |
| AI_CHARACTERS/ANDREY/10_notes/ANDREY_REFERENCE_PRESETS.json.backup_20260706_115144 | 7232 | 2026-07-06 11:51:44 |
| AI_CHARACTERS/ANDREY/10_notes/ANDREY_REFERENCE_PRESETS.json.backup_20260709_092657 | 7562 | 2026-07-09 09:26:57 |
| AI_CHARACTERS/ANDREY/10_notes/ANDREY_TEST_RESULTS.md | 5038 | 2026-07-06 12:02:51 |
| AI_CHARACTERS/ANDREY/10_notes/ANDREY_TEST_RESULTS.md.backup_20260706_115144 | 4739 | 2026-07-06 11:51:44 |
| AI_CHARACTERS/ANDREY_JUNIOR/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/01_refs_raw/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/02_refs_selected/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/ANDREY_JUNIOR_face_canon_v1_sheet_A_APPROVED.png | 2261340 | 2026-07-03 21:15:18 |
| AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/expressions/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/expressions/ANDREY_JUNIOR_expressions_v2_sheet_A_APPROVED.png | 2334285 | 2026-07-03 23:31:01 |
| AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/ANDREY_JUNIOR_body_canon_v2_sheet_A_front_side_back_APPROVED.png | 1797398 | 2026-07-04 06:30:22 |
| AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/ANDREY_JUNIOR_body_canon_v2_sheet_B_pose_variations_APPROVED.png | 1768630 | 2026-07-04 07:51:53 |
| AI_CHARACTERS/ANDREY_JUNIOR/05_outfits/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/06_prompts/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/06_prompts/ANDREY_JUNIOR_CANON_GENERATION_PROMPTS.txt | 9297 | 2026-07-06 08:37:21 |
| AI_CHARACTERS/ANDREY_JUNIOR/06_prompts/ANDREY_JUNIOR_CANON_GENERATION_PROMPTS.txt.backup_20260704_150852 | 3933 | 2026-07-04 15:08:52 |
| AI_CHARACTERS/ANDREY_JUNIOR/06_prompts/ANDREY_JUNIOR_CANON_GENERATION_PROMPTS.txt.backup_20260706_083029 | 8806 | 2026-07-06 08:30:29 |
| AI_CHARACTERS/ANDREY_JUNIOR/06_prompts/ANDREY_JUNIOR_PROMPT_INDEX.md | 5962 | 2026-07-06 08:36:51 |
| AI_CHARACTERS/ANDREY_JUNIOR/06_prompts/ANDREY_JUNIOR_PROMPT_RUN_LOG.jsonl | 11607 | 2026-07-06 08:36:51 |
| AI_CHARACTERS/ANDREY_JUNIOR/06_prompts/ANDREY_JUNIOR_WORKING_SCENE_PROMPTS.md | 13810 | 2026-07-06 08:36:51 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/.gitkeep | 0 | 2026-07-03 15:56:33 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/01_neutral_studio_portrait/.gitkeep | 0 | 2026-07-03 15:56:33 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/01_neutral_studio_portrait/ANDREY_JUNIOR_test01_neutral_studio_portrait_v1_APPROVED.png | 2097235 | 2026-07-03 21:16:26 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/02_full_body_studio/.gitkeep | 0 | 2026-07-03 15:56:33 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/02_full_body_studio/ANDREY_JUNIOR_test02_full_body_studio_v1_APPROVED.png | 1990651 | 2026-07-03 21:51:03 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/03_athletic_gym_identity/.gitkeep | 0 | 2026-07-03 15:56:33 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/03_athletic_gym_identity/ANDREY_JUNIOR_test03_athletic_gym_identity_v1_APPROVED.png | 1929235 | 2026-07-03 22:01:40 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/04_casual_outfit/.gitkeep | 0 | 2026-07-03 15:56:33 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/04_casual_outfit/ANDREY_JUNIOR_test04_casual_outfit_v1_APPROVED.png | 2285922 | 2026-07-03 22:07:30 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/05_scale_compact_body_check/.gitkeep | 0 | 2026-07-03 15:56:33 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/05_scale_compact_body_check/ANDREY_JUNIOR_test05_scale_compact_body_check_v1_APPROVED.png | 2074779 | 2026-07-03 23:00:11 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/06_father_son_scale_check/ANDREY_JUNIOR_test06_father_son_scale_check_v2_APPROVED.png | 1892311 | 2026-07-04 08:34:37 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/07_father_son_casual_outdoor/ANDREY_JUNIOR_test07_father_son_casual_outdoor_v1_APPROVED.png | 2286466 | 2026-07-04 09:47:55 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/08_father_son_home_conversation/ANDREY_JUNIOR_test08_father_son_home_conversation_v1_APPROVED.png | 2274479 | 2026-07-04 11:27:52 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/09_father_son_training_coaching/ANDREY_JUNIOR_test09_father_son_training_coaching_v1_APPROVED.png | 1917670 | 2026-07-04 12:11:18 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/drafts/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/07_generated/rejected/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/08_video_refs/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/09_blender/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/.gitkeep | 0 | 2026-07-03 15:55:31 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_CANON_INDEX.md | 1707 | 2026-07-06 08:39:54 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_CANON_INDEX.md.backup_20260704_150852 | 684 | 2026-07-04 15:08:52 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_CANON_INDEX.md.backup_20260706_083029 | 1093 | 2026-07-06 08:30:29 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_IDENTITY_DRAFT.md | 1656 | 2026-07-06 08:41:05 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_IDENTITY_DRAFT.md.backup_20260704_150852 | 1261 | 2026-07-04 15:08:52 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_IDENTITY_DRAFT.md.backup_20260706_083029 | 1508 | 2026-07-06 08:30:29 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_REFERENCE_PRESETS.json | 7603 | 2026-07-09 09:26:57 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_REFERENCE_PRESETS.json.backup_20260704_150852 | 602 | 2026-07-04 15:08:52 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_REFERENCE_PRESETS.json.backup_20260706_083029 | 6295 | 2026-07-06 08:30:29 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_REFERENCE_PRESETS.json.backup_20260709_092657 | 6755 | 2026-07-09 09:26:57 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_TEST_RESULTS.md | 3515 | 2026-07-06 08:40:42 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_TEST_RESULTS.md.backup_20260704_150852 | 903 | 2026-07-04 15:08:52 |
| AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_TEST_RESULTS.md.backup_20260706_083029 | 2982 | 2026-07-06 08:30:29 |
| AI_CHARACTERS/EGOR/01_refs_raw/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/01_refs_raw/EGOR_RAW_01_body_multiangle_burgundy.png | 2590598 | 2026-07-19 19:20:10 |
| AI_CHARACTERS/EGOR/01_refs_raw/EGOR_RAW_02_face_bar_burgundy.jpg | 83723 | 2026-07-19 19:20:10 |
| AI_CHARACTERS/EGOR/01_refs_raw/EGOR_RAW_03_duo_couch.png | 3068480 | 2026-07-19 19:20:10 |
| AI_CHARACTERS/EGOR/01_refs_raw/EGOR_RAW_04_duo_pillar.png | 2666182 | 2026-07-19 19:20:10 |
| AI_CHARACTERS/EGOR/01_refs_raw/EGOR_RAW_05_duo_close.png | 2998637 | 2026-07-19 19:20:10 |
| AI_CHARACTERS/EGOR/02_best_refs/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/03_face_sheet/EGOR_face_canon_v1_sheet_A_APPROVED.png | 2138235 | 2026-07-20 17:54:13 |
| AI_CHARACTERS/EGOR/03_face_sheet/expressions/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/03_face_sheet/expressions/EGOR_expressions_v1_sheet_A_APPROVED.png | 2224466 | 2026-07-20 17:56:59 |
| AI_CHARACTERS/EGOR/04_body_sheet/candidates/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/04_body_sheet/EGOR_body_canon_v1_sheet_A_front_side_back_APPROVED.png | 1807653 | 2026-07-20 17:57:52 |
| AI_CHARACTERS/EGOR/05_outfits/candidates/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/05_outfits/casual/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/05_outfits/evening_dress/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/05_outfits/formal/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/05_outfits/scene_outfits/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/05_outfits/sports_look/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/06_prompts/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/06_prompts/EGOR_CANON_GENERATION_PROMPTS.txt | 5794 | 2026-07-20 21:37:55 |
| AI_CHARACTERS/EGOR/06_prompts/EGOR_PROMPT_INDEX.md | 2323 | 2026-07-20 21:37:22 |
| AI_CHARACTERS/EGOR/06_prompts/EGOR_PROMPT_RUN_LOG.jsonl | 4041 | 2026-07-20 20:54:09 |
| AI_CHARACTERS/EGOR/06_prompts/EGOR_WORKING_SCENE_PROMPTS.md | 5539 | 2026-07-20 21:37:37 |
| AI_CHARACTERS/EGOR/07_generated/canon_tests/01_evening_embankment/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/07_generated/canon_tests/01_evening_embankment/EGOR_test02_evening_embankment_v1_APPROVED.png | 2107059 | 2026-07-20 20:14:28 |
| AI_CHARACTERS/EGOR/07_generated/canon_tests/02_sports_yoga/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/07_generated/canon_tests/02_sports_yoga/EGOR_test03_sports_yoga_v1_APPROVED.png | 1726201 | 2026-07-20 20:15:05 |
| AI_CHARACTERS/EGOR/07_generated/canon_tests/03_portrait_expression/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/07_generated/canon_tests/03_portrait_expression/EGOR_test01_neutral_portrait_v1_APPROVED.png | 1939280 | 2026-07-20 19:13:49 |
| AI_CHARACTERS/EGOR/07_generated/drafts/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/07_generated/rejected/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/08_masks/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/09_blender/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/10_notes/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/EGOR/10_notes/EGOR_CANON_INDEX.md | 1846 | 2026-07-20 21:37:10 |
| AI_CHARACTERS/EGOR/10_notes/EGOR_REFERENCE_PRESETS.json | 5464 | 2026-07-20 21:37:50 |
| AI_CHARACTERS/EGOR/10_notes/EGOR_TEST_RESULTS.md | 1808 | 2026-07-20 21:37:15 |
| AI_CHARACTERS/KIRA/01_refs_raw/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/KIRA/02_best_refs/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/KIRA/03_face_sheet/expressions/KIRA_expressions_v1_sheet_A_emotional.png | 2257262 | 2026-06-29 18:03:58 |
| AI_CHARACTERS/KIRA/03_face_sheet/expressions/KIRA_expressions_v1_sheet_B_emotional.png | 2251489 | 2026-06-29 18:04:20 |
| AI_CHARACTERS/KIRA/03_face_sheet/KIRA_face_canon_sheet_A.png | 2445177 | 2026-06-29 13:23:22 |
| AI_CHARACTERS/KIRA/03_face_sheet/KIRA_face_canon_sheet_B.png | 2272821 | 2026-06-29 13:23:34 |
| AI_CHARACTERS/KIRA/04_body_sheet/candidates/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/KIRA/04_body_sheet/KIRA_BODY_CANON_v4_sheet_A_4views.png | 1768955 | 2026-06-29 13:15:08 |
| AI_CHARACTERS/KIRA/04_body_sheet/KIRA_BODY_CANON_v4_sheet_B_4views.png | 1911966 | 2026-06-29 13:15:32 |
| AI_CHARACTERS/KIRA/05_outfits/candidates/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/KIRA/05_outfits/casual/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/KIRA/05_outfits/evening_dress/candidates/KIRA_evening_dress_v2_sheet_A_fullbody_4plus_candidate.png | 2000189 | 2026-06-29 20:28:02 |
| AI_CHARACTERS/KIRA/05_outfits/evening_dress/candidates/KIRA_evening_dress_v2_sheet_B_portraits_4plus_candidate.png | 2563239 | 2026-06-29 20:57:22 |
| AI_CHARACTERS/KIRA/05_outfits/evening_dress/KIRA_evening_dress_FINAL_sheet_A_fullbody.png | 2000189 | 2026-06-29 20:28:02 |
| AI_CHARACTERS/KIRA/05_outfits/evening_dress/KIRA_evening_dress_FINAL_sheet_B_portraits.png | 2563239 | 2026-06-29 20:57:22 |
| AI_CHARACTERS/KIRA/05_outfits/evening_dress/KIRA_evening_dress_v1_sheet_A_fullbody.png | 2036585 | 2026-06-29 17:47:14 |
| AI_CHARACTERS/KIRA/05_outfits/evening_dress/KIRA_evening_dress_v1_sheet_B_fullbody.png | 2276573 | 2026-06-29 17:47:32 |
| AI_CHARACTERS/KIRA/05_outfits/formal/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/KIRA/05_outfits/scene_outfits/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/KIRA/05_outfits/sports_look/KIRA_sports_look_v1_sheet_A_front_side_back.png | 1912030 | 2026-06-29 15:37:52 |
| AI_CHARACTERS/KIRA/05_outfits/sports_look/KIRA_sports_look_v1_sheet_B_3q_action_portrait.png | 2072557 | 2026-06-29 15:38:18 |
| AI_CHARACTERS/KIRA/06_prompts/create_kira_prompt_kit.ps1.txt | 8785 | 2026-06-29 19:00:54 |
| AI_CHARACTERS/KIRA/06_prompts/KIRA_BASE_PROMPT.txt | 1845 | 2026-07-07 15:38:19 |
| AI_CHARACTERS/KIRA/06_prompts/KIRA_BASE_PROMPT.txt.backup_20260707_153812 | 1662 | 2026-07-07 15:38:12 |
| AI_CHARACTERS/KIRA/06_prompts/KIRA_EVENING_SCENE_PROMPT.txt | 1756 | 2026-07-07 15:38:21 |
| AI_CHARACTERS/KIRA/06_prompts/KIRA_EVENING_SCENE_PROMPT.txt.backup_20260707_153812 | 1573 | 2026-07-07 15:38:12 |
| AI_CHARACTERS/KIRA/06_prompts/KIRA_NEGATIVE_PROMPT.txt | 1836 | 2026-07-07 15:38:25 |
| AI_CHARACTERS/KIRA/06_prompts/KIRA_NEGATIVE_PROMPT.txt.backup_20260707_153812 | 1653 | 2026-07-07 15:38:12 |
| AI_CHARACTERS/KIRA/06_prompts/KIRA_PROMPT_INDEX.md | 3732 | 2026-07-07 15:35:06 |
| AI_CHARACTERS/KIRA/06_prompts/KIRA_PROMPT_RUN_LOG.jsonl | 4323 | 2026-07-07 15:37:45 |
| AI_CHARACTERS/KIRA/06_prompts/KIRA_SPORTS_SCENE_PROMPT.txt | 1616 | 2026-07-07 15:38:23 |
| AI_CHARACTERS/KIRA/06_prompts/KIRA_SPORTS_SCENE_PROMPT.txt.backup_20260707_153812 | 1433 | 2026-07-07 15:38:12 |
| AI_CHARACTERS/KIRA/06_prompts/KIRA_WORKING_SCENE_PROMPTS.md | 17631 | 2026-07-07 15:37:08 |
| AI_CHARACTERS/KIRA/07_generated/317946af-4d80-4e9a-8b97-c469551e0235.png | 2097050 | 2026-06-29 20:28:22 |
| AI_CHARACTERS/KIRA/07_generated/9f28dfea-0aaa-4dee-831a-0a18004e2a7e.png | 2433253 | 2026-06-29 17:03:04 |
| AI_CHARACTERS/KIRA/07_generated/canon_tests/01_evening_embankment/KIRA_test01_evening_embankment_v1.png | 2333289 | 2026-06-29 23:04:46 |
| AI_CHARACTERS/KIRA/07_generated/canon_tests/01_evening_embankment/KIRA_test01_evening_embankment_v2_MAIN.png | 1949984 | 2026-06-29 23:19:38 |
| AI_CHARACTERS/KIRA/07_generated/canon_tests/01_evening_embankment/KIRA_test01_evening_embankment_v3_ALT_cinematic.png | 2245912 | 2026-06-29 23:20:02 |
| AI_CHARACTERS/KIRA/07_generated/canon_tests/02_sports_yoga/KIRA_test02_sports_yoga_v1.png | 1915994 | 2026-06-29 23:49:46 |
| AI_CHARACTERS/KIRA/07_generated/canon_tests/02_sports_yoga/KIRA_test02_sports_yoga_v2_MAIN.png | 2021939 | 2026-06-29 23:50:12 |
| AI_CHARACTERS/KIRA/07_generated/canon_tests/02_sports_yoga/KIRA_test02_sports_yoga_v3_ALT_stretch.png | 1963790 | 2026-06-29 23:50:32 |
| AI_CHARACTERS/KIRA/07_generated/canon_tests/03_portrait_expression/KIRA_test02_bar_romance_v1_APPROVED.png | 2185958 | 2026-06-30 06:12:28 |
| AI_CHARACTERS/KIRA/07_generated/drafts/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/KIRA/07_generated/f7d3091b-c9ce-4ccc-878a-596980ce5231.png | 2202047 | 2026-06-29 17:03:10 |
| AI_CHARACTERS/KIRA/07_generated/rejected/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/KIRA/08_masks/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/KIRA/09_blender/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_APPROVAL_CRITERIA.md.txt | 13560 | 2026-06-29 21:03:18 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_APPROVAL_CRITERIA_ENG.md.txt | 4209 | 2026-06-29 21:08:48 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_CANON_APPROVAL_WORKSHEET.md | 5827 | 2026-07-09 09:26:57 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_CANON_INDEX.md.txt | 10703 | 2026-07-07 15:43:12 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_CANON_INDEX.md.txt.backup_20260707_153909 | 10102 | 2026-07-07 15:39:09 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_IDENTITY.txt.txt | 13272 | 2026-07-07 15:40:13 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_IDENTITY.txt.txt.backup_20260707_154006 | 13022 | 2026-07-07 15:40:06 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_REFERENCE_PRESETS.json | 6421 | 2026-07-09 09:26:57 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_REFERENCE_PRESETS.json.backup_20260707_153832 | 4217 | 2026-07-07 15:38:32 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_REFERENCE_PRESETS.json.backup_20260709_092657 | 4536 | 2026-07-09 09:26:57 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_TEST_RESULTS.md.txt | 3581 | 2026-07-07 15:39:57 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_TEST_RESULTS.md.txt.backup_20260702_231620 | 2916 | 2026-07-02 23:16:20 |
| AI_CHARACTERS/KIRA/10_notes/KIRA_TEST_RESULTS.md.txt.backup_20260707_153909 | 2752 | 2026-07-07 15:39:09 |
| AI_CHARACTERS/MAKSIM/01_refs_raw/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/02_best_refs/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/03_face_sheet/expressions/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/04_body_sheet/candidates/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/05_outfits/candidates/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/05_outfits/casual/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/05_outfits/evening_dress/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/05_outfits/formal/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/05_outfits/scene_outfits/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/05_outfits/sports_look/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/06_prompts/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/06_prompts/MAKSIM_CANON_GENERATION_PROMPTS.txt | 4485 | 2026-07-09 10:15:21 |
| AI_CHARACTERS/MAKSIM/07_generated/canon_tests/01_evening_embankment/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/07_generated/canon_tests/02_sports_yoga/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/07_generated/canon_tests/03_portrait_expression/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/07_generated/drafts/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/07_generated/rejected/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/08_masks/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/09_blender/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/10_notes/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MAKSIM/10_notes/MAKSIM_REFERENCE_PRESETS.json | 2402 | 2026-07-09 09:26:57 |
| AI_CHARACTERS/MARINA/01_refs_raw/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MARINA/02_best_refs/.gitkeep | 0 | 2026-06-30 20:37:52 |
| AI_CHARACTERS/MARINA/03_face_sheet/expressions/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_A_APPROVED.png | 2793679 | 2026-06-24 12:16:13 |
| AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_B_SUPPORT.png | 2507724 | 2026-06-24 13:21:29 |
| AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_C_SUPPORT.png | 2609441 | 2026-06-24 13:08:17 |
| AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_D_SUPPORT.png | 2492855 | 2026-06-24 13:26:07 |
| AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_E_SUPPORT.png | 2393971 | 2026-06-24 12:46:29 |
| AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_F_SUPPORT.png | 2461808 | 2026-06-24 12:22:38 |
| AI_CHARACTERS/MARINA/03_face_sheet/MARINA_face_canon_v1_sheet_A_APPROVED.png | 2300259 | 2026-06-20 10:26:04 |
| AI_CHARACTERS/MARINA/04_body_sheet/candidates/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/04_body_sheet/MARINA_body_canon_v1_sheet_A_APPROVED.png | 1964738 | 2026-06-24 10:15:32 |
| AI_CHARACTERS/MARINA/05_outfits/candidates/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/05_outfits/casual/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/05_outfits/evening_dress/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/05_outfits/formal/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/05_outfits/MARINA_outfit_evening_peach_v1_portrait_SUPPORT.png | 1983655 | 2026-06-20 10:25:54 |
| AI_CHARACTERS/MARINA/05_outfits/MARINA_outfit_evening_peach_v1_sheet_A_APPROVED.png | 2045753 | 2026-06-24 08:16:29 |
| AI_CHARACTERS/MARINA/05_outfits/MARINA_outfit_warm_evening_v1_portrait_SUPPORT.png | 1899586 | 2026-06-24 11:54:11 |
| AI_CHARACTERS/MARINA/05_outfits/scene_outfits/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/05_outfits/sports_look/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/06_prompts/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/06_prompts/MARINA_CANON_GENERATION_PROMPTS.txt | 4923 | 2026-07-18 13:39:06 |
| AI_CHARACTERS/MARINA/06_prompts/MARINA_PROMPT_INDEX.md | 5842 | 2026-07-19 06:42:00 |
| AI_CHARACTERS/MARINA/06_prompts/MARINA_PROMPT_RUN_LOG.jsonl | 15056 | 2026-07-19 06:42:00 |
| AI_CHARACTERS/MARINA/06_prompts/MARINA_WORKING_SCENE_PROMPTS.md | 16149 | 2026-07-19 06:42:00 |
| AI_CHARACTERS/MARINA/07_generated/canon_tests/01_evening_embankment/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/07_generated/canon_tests/02_sports_yoga/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/07_generated/canon_tests/03_portrait_expression/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test01_rainy_cafe_v1_APPROVED.png | 2244661 | 2026-06-24 11:00:14 |
| AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test02_theater_melancholy_v1_APPROVED.png | 1742251 | 2026-06-24 11:08:00 |
| AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test03_evening_city_balcony_v1_APPROVED.png | 1768025 | 2026-06-24 10:55:19 |
| AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test04_autumn_street_portrait_v1_APPROVED.png | 2172369 | 2026-06-20 10:25:58 |
| AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test05_morning_pajamas_v1_APPROVED.png | 1970323 | 2026-06-24 11:21:46 |
| AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test06_white_garden_formal_v1_APPROVED.png | 2294626 | 2026-06-24 10:42:02 |
| AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test07_pool_sunset_v1_APPROVED.png | 2020204 | 2026-06-24 11:17:34 |
| AI_CHARACTERS/MARINA/07_generated/drafts/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/07_generated/rejected/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/08_masks/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/09_blender/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/10_notes/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/MARINA/10_notes/MARINA_CANON_INDEX.md | 7339 | 2026-07-19 06:42:00 |
| AI_CHARACTERS/MARINA/10_notes/MARINA_REFERENCE_PRESETS.json | 5053 | 2026-07-19 06:42:00 |
| AI_CHARACTERS/MARINA/10_notes/MARINA_TEST_RESULTS.md | 5359 | 2026-07-19 06:42:00 |
| AI_CHARACTERS/NIKA/01_refs_raw/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_01_face_main_burgundy_expressions.png | 2066529 | 2026-07-21 18:15:44 |
| AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_02_body_main_burgundy_multiview.png | 1935430 | 2026-07-21 18:15:44 |
| AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_03_body_support_gym_multiview.png | 2177150 | 2026-07-21 18:15:44 |
| AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_04_style_main_burgundy_bar.png | 1639183 | 2026-07-21 18:15:44 |
| AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_05_formal_support_burgundy_sheet.png | 1927825 | 2026-07-21 18:15:44 |
| AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_06_sports_support_gym_leggings.png | 1805654 | 2026-07-21 18:15:44 |
| AI_CHARACTERS/NIKA/02_best_refs/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/03_face_sheet/expressions/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/03_face_sheet/expressions/NIKA_expressions_v1_sheet_A_APPROVED.png | 2258718 | 2026-07-22 09:04:34 |
| AI_CHARACTERS/NIKA/03_face_sheet/expressions/NIKA_expressions_v1_sheet_A_attempt03_REVISE.png | 2314676 | 2026-07-22 08:00:32 |
| AI_CHARACTERS/NIKA/03_face_sheet/NIKA_face_canon_v1_sheet_A_APPROVED.png | 2258699 | 2026-07-21 21:17:17 |
| AI_CHARACTERS/NIKA/04_body_sheet/candidates/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/04_body_sheet/NIKA_body_canon_v1_sheet_A_front_side_back_APPROVED.png | 1809583 | 2026-07-22 11:24:25 |
| AI_CHARACTERS/NIKA/04_body_sheet/NIKA_body_canon_v1_sheet_B_pose_variations_APPROVED.png | 1871552 | 2026-07-22 12:20:31 |
| AI_CHARACTERS/NIKA/05_outfits/candidates/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/05_outfits/casual/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/05_outfits/evening_dress/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/05_outfits/formal/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/05_outfits/scene_outfits/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/05_outfits/sports_look/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/06_prompts/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/06_prompts/NIKA_CANON_GENERATION_PROMPTS.txt | 6634 | 2026-07-24 13:58:02 |
| AI_CHARACTERS/NIKA/06_prompts/NIKA_PROMPT_INDEX.md | 3162 | 2026-07-24 13:56:27 |
| AI_CHARACTERS/NIKA/06_prompts/NIKA_PROMPT_RUN_LOG.jsonl | 6691 | 2026-07-24 13:57:07 |
| AI_CHARACTERS/NIKA/06_prompts/NIKA_WORKING_SCENE_PROMPTS.md | 6706 | 2026-07-24 13:57:40 |
| AI_CHARACTERS/NIKA/07_generated/canon_tests/01_evening_embankment/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/07_generated/canon_tests/01_evening_embankment/NIKA_test02_evening_embankment_v1_APPROVED.png | 2084220 | 2026-07-22 15:20:28 |
| AI_CHARACTERS/NIKA/07_generated/canon_tests/02_sports_yoga/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/07_generated/canon_tests/02_sports_yoga/NIKA_test03_sports_yoga_v1_APPROVED.png | 1965291 | 2026-07-24 08:32:14 |
| AI_CHARACTERS/NIKA/07_generated/canon_tests/03_portrait_expression/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/07_generated/canon_tests/03_portrait_expression/NIKA_test01_neutral_portrait_v1_APPROVED.png | 1763077 | 2026-07-22 13:05:11 |
| AI_CHARACTERS/NIKA/07_generated/canon_tests/03_portrait_expression/NIKA_test01_neutral_portrait_v2_APPROVED.png | 1800546 | 2026-07-22 14:41:44 |
| AI_CHARACTERS/NIKA/07_generated/drafts/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/07_generated/drafts/NIKA_body_canon_v1_attempt01_REVISE.png | 1906582 | 2026-07-22 10:02:33 |
| AI_CHARACTERS/NIKA/07_generated/drafts/NIKA_body_canon_v1_attempt02_REVISE.png | 1876834 | 2026-07-22 10:21:27 |
| AI_CHARACTERS/NIKA/07_generated/rejected/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/08_masks/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/09_blender/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/10_notes/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/NIKA/10_notes/NIKA_CANON_INDEX.md | 2987 | 2026-07-24 13:55:38 |
| AI_CHARACTERS/NIKA/10_notes/NIKA_REFERENCE_PRESETS.json | 8511 | 2026-07-24 13:58:40 |
| AI_CHARACTERS/NIKA/10_notes/NIKA_TEST_RESULTS.md | 3131 | 2026-07-24 13:56:00 |
| AI_CHARACTERS/OLGA/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/01_refs_raw/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/02_best_refs/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/02_refs_selected/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/02_refs_selected/OLGA_ref_face_primary_v1_SELECTED.jpg | 130813 | 2026-07-04 21:54:10 |
| AI_CHARACTERS/OLGA/03_face_sheet/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/03_face_sheet/expressions/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/03_face_sheet/expressions/OLGA_expressions_v1_sheet_A_APPROVED.png | 2289464 | 2026-07-04 21:21:04 |
| AI_CHARACTERS/OLGA/03_face_sheet/OLGA_face_canon_v1_sheet_A_APPROVED.png | 2261807 | 2026-07-04 19:03:41 |
| AI_CHARACTERS/OLGA/04_body_sheet/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/04_body_sheet/candidates/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/04_body_sheet/OLGA_body_canon_v1_sheet_A_front_side_back_APPROVED.png | 1839620 | 2026-07-04 21:33:10 |
| AI_CHARACTERS/OLGA/04_body_sheet/OLGA_body_canon_v1_sheet_B_pose_variations_APPROVED.png | 1753854 | 2026-07-04 21:46:26 |
| AI_CHARACTERS/OLGA/05_outfits/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/05_outfits/candidates/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/05_outfits/casual/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/05_outfits/evening_dress/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/05_outfits/formal/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/05_outfits/scene_outfits/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/05_outfits/sports_look/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/06_prompts/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/06_prompts/OLGA_CANON_GENERATION_PROMPTS.txt | 4546 | 2026-07-05 16:24:20 |
| AI_CHARACTERS/OLGA/06_prompts/OLGA_POOL_SCENE_PROMPT.md | 5069 | 2026-07-09 09:26:57 |
| AI_CHARACTERS/OLGA/06_prompts/OLGA_PROMPT_INDEX.md | 5779 | 2026-07-17 14:08:29 |
| AI_CHARACTERS/OLGA/06_prompts/OLGA_PROMPT_INDEX.md.backup_20260705_234153 | 3536 | 2026-07-05 23:41:53 |
| AI_CHARACTERS/OLGA/06_prompts/OLGA_PROMPT_RUN_LOG.jsonl | 12865 | 2026-07-18 06:28:08 |
| AI_CHARACTERS/OLGA/06_prompts/OLGA_PROMPT_RUN_LOG.jsonl.backup_20260705_234153 | 4930 | 2026-07-05 23:41:53 |
| AI_CHARACTERS/OLGA/06_prompts/OLGA_WORKING_SCENE_PROMPTS.md | 15437 | 2026-07-10 15:25:24 |
| AI_CHARACTERS/OLGA/06_prompts/OLGA_WORKING_SCENE_PROMPTS.md.backup_20260705_234153 | 11582 | 2026-07-05 23:41:53 |
| AI_CHARACTERS/OLGA/06_prompts/OLGA_WORKING_SCENE_PROMPTS_V2.md | 17552 | 2026-07-17 14:07:52 |
| AI_CHARACTERS/OLGA/07_generated/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/.gitkeep | 0 | 2026-07-04 16:04:15 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/01_evening_embankment/.gitkeep | 0 | 2026-07-04 16:04:16 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/01_evening_embankment/OLGA_test01_evening_embankment_v1_APPROVED.png | 2161552 | 2026-07-05 13:32:22 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/02_sports_yoga/.gitkeep | 0 | 2026-07-04 16:04:16 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/02_sports_yoga/OLGA_test02_sports_yoga_v1_APPROVED.png | 1700014 | 2026-07-04 22:26:20 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/03_portrait_expression/.gitkeep | 0 | 2026-07-04 16:04:16 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/03_portrait_expression/OLGA_test03_portrait_expression_v1_APPROVED.png | 2177503 | 2026-07-04 22:00:21 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/04_outdoor_walk_with_andrey_junior/OLGA_test04_outdoor_walk_with_andrey_junior_v1_APPROVED.png | 2334617 | 2026-07-05 12:40:15 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/05_business_interior/OLGA_test05_business_interior_v1_APPROVED.png | 1791762 | 2026-07-05 22:25:54 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/06_indoor_lounge_conversation_with_andrey_junior/OLGA_test06_indoor_lounge_conversation_with_andrey_junior_v1_APPROVED.png | 2063547 | 2026-07-05 21:43:27 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/07_pool_wellness_solo/.gitkeep | 0 | 2026-07-10 12:32:22 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/07_pool_wellness_solo/OLGA_test07_pool_wellness_solo_v1_APPROVED.png | 1921754 | 2026-07-10 01:39:03 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/08_dalle_evening_embankment/.gitkeep | 0 | 2026-07-10 15:23:41 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/08_dalle_evening_embankment/OLGA_test08_dalle_evening_embankment_v1_APPROVED.png | 1927004 | 2026-07-09 13:32:08 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/09_formal_elegant/OLGA_test09_formal_elegant_v4_APPROVED.png | 3164983 | 2026-07-10 21:11:44 |
| AI_CHARACTERS/OLGA/07_generated/canon_tests/10_neutral_height_scale_check/OLGA_test10_neutral_height_scale_check_v1_APPROVED.png | 1669083 | 2026-07-18 06:28:08 |
| AI_CHARACTERS/OLGA/07_generated/drafts/.gitkeep | 0 | 2026-07-04 16:04:16 |
| AI_CHARACTERS/OLGA/07_generated/rejected/.gitkeep | 0 | 2026-07-04 16:04:16 |
| AI_CHARACTERS/OLGA/08_masks/.gitkeep | 0 | 2026-07-04 16:04:16 |
| AI_CHARACTERS/OLGA/08_rejected/.gitkeep | 0 | 2026-07-04 16:04:16 |
| AI_CHARACTERS/OLGA/08_rejected/OLGA_business_interior_raw_1_unlabeled_REJECTED.png | 1791762 | 2026-07-05 22:25:13 |
| AI_CHARACTERS/OLGA/09_blender/.gitkeep | 0 | 2026-07-04 16:04:16 |
| AI_CHARACTERS/OLGA/09_exports/.gitkeep | 0 | 2026-07-04 16:04:16 |
| AI_CHARACTERS/OLGA/10_notes/.gitkeep | 0 | 2026-07-04 16:04:16 |
| AI_CHARACTERS/OLGA/10_notes/OLGA_CANON_INDEX.md | 2602 | 2026-07-11 08:25:21 |
| AI_CHARACTERS/OLGA/10_notes/OLGA_CANON_INDEX.md.backup_20260705_162431 | 987 | 2026-07-05 16:24:31 |
| AI_CHARACTERS/OLGA/10_notes/OLGA_CANON_INDEX.md.backup_20260705_234259 | 1911 | 2026-07-05 23:42:59 |
| AI_CHARACTERS/OLGA/10_notes/OLGA_IDENTITY_DRAFT.md | 2379 | 2026-07-05 16:25:50 |
| AI_CHARACTERS/OLGA/10_notes/OLGA_IDENTITY_DRAFT.md.backup_20260705_162431 | 2358 | 2026-07-05 16:24:31 |
| AI_CHARACTERS/OLGA/10_notes/OLGA_REFERENCE_PRESETS.json | 12992 | 2026-07-18 06:28:08 |
| AI_CHARACTERS/OLGA/10_notes/OLGA_REFERENCE_PRESETS.json.backup_20260705_162431 | 2127 | 2026-07-05 16:24:31 |
| AI_CHARACTERS/OLGA/10_notes/OLGA_REFERENCE_PRESETS.json.backup_20260705_234259 | 5317 | 2026-07-05 23:42:59 |
| AI_CHARACTERS/OLGA/10_notes/OLGA_REFERENCE_PRESETS.json.backup_20260709_092657 | 6792 | 2026-07-09 09:26:57 |
| AI_CHARACTERS/OLGA/10_notes/OLGA_TEST_RESULTS.md | 5014 | 2026-07-18 06:28:08 |
| AI_CHARACTERS/OLGA/10_notes/OLGA_TEST_RESULTS.md.backup_20260705_162431 | 1146 | 2026-07-05 16:24:31 |
| AI_CHARACTERS/OLGA/10_notes/OLGA_TEST_RESULTS.md.backup_20260705_234259 | 1360 | 2026-07-05 23:42:59 |
| AI_CHARACTERS/SERGEY/01_refs_raw/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/02_best_refs/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/03_face_sheet/expressions/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/04_body_sheet/candidates/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/05_outfits/candidates/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/05_outfits/casual/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/05_outfits/evening_dress/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/05_outfits/formal/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/05_outfits/scene_outfits/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/05_outfits/sports_look/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/06_prompts/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/06_prompts/SERGEY_CANON_GENERATION_PROMPTS.txt | 4474 | 2026-07-09 10:15:21 |
| AI_CHARACTERS/SERGEY/07_generated/canon_tests/01_evening_embankment/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/07_generated/canon_tests/02_sports_yoga/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/07_generated/canon_tests/03_portrait_expression/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/07_generated/drafts/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/07_generated/rejected/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/08_masks/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/09_blender/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/10_notes/.gitkeep | 0 | 2026-06-30 20:37:53 |
| AI_CHARACTERS/SERGEY/10_notes/SERGEY_REFERENCE_PRESETS.json | 2416 | 2026-07-09 09:26:57 |
| configs/visual_canon/character_bootstrap.schema.json | 2438 | 2026-07-19 08:50:49 |
| configs/visual_canon/character_manifest.schema.json | 7521 | 2026-07-12 18:22:17 |
| configs/visual_canon/deployment_request.schema.json | 7648 | 2026-07-14 08:57:39 |
| configs/visual_canon/pipeline_policy.json | 6807 | 2026-07-14 00:27:13 |
| configs/visual_canon/prompt_record.schema.json | 7040 | 2026-07-12 18:21:41 |
| docs/GITHUB_REFERENCE_PACK_WORKFLOW.md | 8871 | 2026-07-12 18:26:56 |
| docs/NCC_DEPLOY_CHECKLIST.md | 8924 | 2026-07-14 06:16:13 |
| docs/NCC_FOLDER_MAP.md | 4785 | 2026-07-12 18:27:22 |
| docs/NCC_VISUAL_CANON_WORKFLOW.md | 21758 | 2026-07-19 14:11:00 |
| docs/PROJECT_DOCUMENTATION_INDEX.md | 19699 | 2026-07-19 14:10:50 |
| docs/VOYAGE_INTEGRATION_WORKFLOW.md | 7250 | 2026-07-12 18:27:37 |
| docs/VOYAGE_SQLITE_MEMORY_WORKFLOW.md | 5250 | 2026-07-12 18:27:46 |
| INVENTORY.md | 100467 | 2026-07-20 21:39:16 |
| INVENTORY.md.backup_20260703_125505 | 47598 | 2026-07-03 12:55:05 |
| INVENTORY.md.backup_20260703_160011 | 53201 | 2026-07-03 16:00:11 |
| INVENTORY.md.backup_20260704_151411 | 58158 | 2026-07-04 15:14:11 |
| INVENTORY.md.backup_20260704_160831 | 63538 | 2026-07-04 16:08:31 |
| INVENTORY.md.backup_20260705_163018 | 65818 | 2026-07-05 16:30:18 |
| INVENTORY.md.backup_20260709_101916 | 78346 | 2026-07-09 10:19:16 |
| INVENTORY.md.backup_20260710_123336 | 79514 | 2026-07-10 12:33:36 |
| INVENTORY.md.backup_20260710_152700 | 82201 | 2026-07-10 15:27:15 |
| INVENTORY.md.backup_20260711_082946 | 82201 | 2026-07-10 15:26:47 |
| INVENTORY.md.backup_20260712_183037 | 82945 | 2026-07-12 18:30:37 |
| INVENTORY.md.backup_20260719_141209 | 95899 | 2026-07-19 14:12:09 |
| PHASE_1_CURRENT_LAPTOP_CLOUD_PIPELINE.md | 9830 | 2026-07-01 09:37:30 |
| PHASE_2_LOCAL_AI_WORKSTATION_PIPELINE.md | 11411 | 2026-07-01 09:37:30 |
| README.md | 1642 | 2026-07-12 18:28:43 |
| repo_audit.txt | 2384 | 2026-07-09 09:27:48 |
| ROADMAP.md | 7662 | 2026-07-12 18:29:00 |
| tests/visual_canon/__pycache__/deploy_test_support.cpython-314.pyc | 13896 | 2026-07-14 09:02:40 |
| tests/visual_canon/__pycache__/test_bootstrap_character.cpython-314.pyc | 40746 | 2026-07-19 08:57:53 |
| tests/visual_canon/__pycache__/test_cline_reference_import_skill.cpython-314.pyc | 33199 | 2026-07-19 14:09:01 |
| tests/visual_canon/__pycache__/test_deploy_visual_canon_apply.cpython-314.pyc | 8403 | 2026-07-14 09:01:37 |
| tests/visual_canon/__pycache__/test_deploy_visual_canon_authority.cpython-314.pyc | 20813 | 2026-07-14 23:26:58 |
| tests/visual_canon/__pycache__/test_deploy_visual_canon_cli.cpython-314.pyc | 10637 | 2026-07-14 09:01:37 |
| tests/visual_canon/__pycache__/test_deploy_visual_canon_concurrency.cpython-314.pyc | 14200 | 2026-07-14 09:01:37 |
| tests/visual_canon/__pycache__/test_deploy_visual_canon_dry_run.cpython-314.pyc | 8778 | 2026-07-14 23:26:58 |
| tests/visual_canon/__pycache__/test_deploy_visual_canon_rollback.cpython-314.pyc | 11555 | 2026-07-14 09:01:37 |
| tests/visual_canon/__pycache__/test_validator_cli.cpython-314.pyc | 8451 | 2026-07-14 06:20:04 |
| tests/visual_canon/__pycache__/test_validator_discovery.cpython-314.pyc | 20157 | 2026-07-14 06:20:04 |
| tests/visual_canon/__pycache__/test_validator_legacy_compatibility.cpython-314.pyc | 5784 | 2026-07-14 06:20:04 |
| tests/visual_canon/__pycache__/test_validator_prompt_records.cpython-314.pyc | 11314 | 2026-07-14 06:20:04 |
| tests/visual_canon/deploy_test_support.py | 9025 | 2026-07-14 09:02:34 |
| tests/visual_canon/fixtures/invalid_duplicate_id/prompt_run_log.jsonl | 1079 | 2026-07-12 21:54:03 |
| tests/visual_canon/fixtures/invalid_empty_prompt/prompt_run_log.jsonl | 599 | 2026-07-12 21:54:18 |
| tests/visual_canon/fixtures/invalid_jsonl/prompt_run_log.jsonl | 110 | 2026-07-12 21:53:59 |
| tests/visual_canon/fixtures/invalid_local_only_leak/prompt_run_log.jsonl | 522 | 2026-07-12 21:54:12 |
| tests/visual_canon/fixtures/invalid_missing_reference/prompt_run_log.jsonl | 586 | 2026-07-12 21:54:07 |
| tests/visual_canon/fixtures/invalid_mojibake/prompt_run_log.jsonl | 606 | 2026-07-12 21:56:59 |
| tests/visual_canon/fixtures/invalid_multiple_main/prompt_run_log.jsonl | 1156 | 2026-07-12 21:54:16 |
| tests/visual_canon/fixtures/invalid_selected_without_approval/prompt_run_log.jsonl | 579 | 2026-07-12 21:54:10 |
| tests/visual_canon/fixtures/invalid_variant_in_id/prompt_run_log.jsonl | 612 | 2026-07-12 21:54:05 |
| tests/visual_canon/fixtures/valid_legacy/prompt_run_log.jsonl | 392 | 2026-07-12 21:57:22 |
| tests/visual_canon/fixtures/valid_strict/prompt_run_log.jsonl | 646 | 2026-07-12 21:53:57 |
| tests/visual_canon/test_bootstrap_character.py | 30251 | 2026-07-19 08:57:42 |
| tests/visual_canon/test_cline_reference_import_skill.py | 21771 | 2026-07-19 14:08:53 |
| tests/visual_canon/test_deploy_visual_canon_apply.py | 3210 | 2026-07-14 08:59:52 |
| tests/visual_canon/test_deploy_visual_canon_authority.py | 11613 | 2026-07-14 23:22:57 |
| tests/visual_canon/test_deploy_visual_canon_cli.py | 4987 | 2026-07-14 08:59:18 |
| tests/visual_canon/test_deploy_visual_canon_concurrency.py | 5592 | 2026-07-14 09:00:39 |
| tests/visual_canon/test_deploy_visual_canon_dry_run.py | 3448 | 2026-07-14 23:26:25 |
| tests/visual_canon/test_deploy_visual_canon_rollback.py | 4810 | 2026-07-14 09:00:15 |
| tests/visual_canon/test_validator_cli.py | 4247 | 2026-07-13 10:46:16 |
| tests/visual_canon/test_validator_discovery.py | 11681 | 2026-07-12 23:00:14 |
| tests/visual_canon/test_validator_legacy_compatibility.py | 3480 | 2026-07-12 22:59:59 |
| tests/visual_canon/test_validator_prompt_records.py | 7043 | 2026-07-12 22:45:31 |
| tools/__pycache__/bootstrap_character.cpython-314.pyc | 54865 | 2026-07-19 09:28:32 |
| tools/__pycache__/deploy_visual_canon_result.cpython-314.pyc | 74220 | 2026-07-17 11:22:24 |
| tools/__pycache__/validate_visual_canon_pipeline.cpython-314.pyc | 53195 | 2026-07-12 22:59:15 |
| tools/bootstrap_character.py | 42313 | 2026-07-19 08:56:26 |
| tools/build_scene_reference_pack.ps1 | 1037 | 2026-07-01 11:04:26 |
| tools/build_scene_reference_pack.py | 16889 | 2026-07-01 17:18:12 |
| tools/deploy_visual_canon_result.py | 45384 | 2026-07-14 08:58:35 |
| tools/generate_inventory.py | 4231 | 2026-07-03 12:55:34 |
| tools/validate_visual_canon_pipeline.py | 33204 | 2026-07-12 22:58:07 |
| tools/voyage_memory_export.py | 5803 | 2026-07-03 01:36:48 |
| tools/voyage_memory_init.py | 19032 | 2026-07-03 01:36:25 |
| tools/voyage_memory_record.py | 17623 | 2026-07-03 01:54:56 |
| tools/voyage_memory_status.py | 2099 | 2026-07-03 01:38:25 |
| UNIFIED_CANON_TESTS_TEMPLATE.md | 5156 | 2026-07-09 17:07:51 |
