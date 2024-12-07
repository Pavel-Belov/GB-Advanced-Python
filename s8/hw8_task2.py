# Задача 2. Объединение данных из нескольких JSON файлов.
# Напишите скрипт, который объединяет данные из нескольких JSON файлов в один.
# Каждый файл содержит список словарей, описывающих сотрудников компании
# (имя, фамилия, возраст, должность). Итоговый JSON файл должен содержать объединённые
# списки сотрудников из всех файлов.
# Пример: У вас есть три файла employees1.json, employees2.json, employees3.json.
# Нужно объединить их в один файл all_employees.json.

import json
from pathlib import Path


def union_to_json(files: list[Path]) -> None:
    data = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as rf:
            data.append(json.load(rf))

    with open('union_employees.json', 'w', encoding='utf-8') as wf:
        json.dump(data, wf, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    union_to_json(['employees1.json', 'employees2.json', 'employees3.json'])
