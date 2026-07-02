# SCENE_REQUEST_RULES

## Scene request states

* **EXAMPLE**
* **REQUESTED**
* **REFERENCE_PACK_READY**
* **GENERATED_DRAFT**
* **APPROVED_AS_TEST**
* **APPROVED_AS_CANON**
* **REJECTED**
* **PRIVATE_LOCAL_ONLY**

## Rule: example is not a task

Если пользователь приводит сцену как пример работы инструмента (например, для иллюстрации формата команды), не запускать генерацию и не создавать canon test на основе этого примера.

## Rule: generation requires explicit request

Генерация начинается только если пользователь явно говорит что-то вроде:

* "создай изображение";
* "сгенерируй сцену";
* "делаем эту сцену";
* "запускаем генерацию".

## Rule: GitHub-first refs

Для scene prompt можно использовать только tracked refs, если нужны GitHub raw links (см. [docs/GITHUB_REFERENCE_PACK_WORKFLOW.md](../docs/GITHUB_REFERENCE_PACK_WORKFLOW.md)).

## Rule: text canon can be embedded

Текстовые canon-данные можно вставлять в prompt напрямую, чтобы не загружать txt-файлы вручную.

## Rule: sensitive/private scenes

* только adult-персонажи;
* neutral base canon хранится отдельно от private/adult вариантов;
* private outputs хранятся вне public repo;
* нет автоматического коммита private outputs.

## Текущий пример-исключение

Сцена "Кира и Андрей в сауне разговаривают, укрытые по пояс полотенцем" была использована как EXAMPLE / TOOL TEST IDEA при обсуждении GitHub-first reference tool. Она не REQUESTED и не должна генерироваться, пока пользователь явно не попросит.
