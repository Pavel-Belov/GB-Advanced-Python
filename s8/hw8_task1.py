# Задание 1. Работа с основными данными.
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию. Для каждого объекта
# укажите файл это или директория. Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет
# для работы с файлами разных форматов.

import csv
import json
import pickle
from pathlib import Path


def directories_listing(dir_path: Path) -> None:
    dir_name = dir_path.name
    data = []
    for obj in dir_path.rglob('*'):
        dir_size = 0
        if obj.is_dir():
            for file in obj.iterdir():
                dir_size += file.stat().st_size

        data.append({
            'name': obj.name,
            'type': 'dir' if obj.is_dir() else 'file',
            'parent': obj.parent.as_posix(),
            'size': obj.stat().st_size if obj.is_file() else dir_size
        })

    with (
        open(f'{dir_name}.json', 'w', encoding='utf-8') as json_file,
        open(f'{dir_name}.csv', 'w', newline='', encoding='utf-8') as csv_file,
        open(f'{dir_name}.pickle', 'wb') as pickle_file,
    ):
        json.dump(data, json_file, indent=4, ensure_ascii=False)

        csv_write = csv.DictWriter(csv_file, fieldnames=['name', 'type', 'parent', 'size'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(data)

        pickle.dump(data, pickle_file)


if __name__ == '__main__':
    directories_listing(Path.cwd())
