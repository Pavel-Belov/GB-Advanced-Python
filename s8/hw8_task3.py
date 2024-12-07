# Задача 3. Агрегирование данных из CSV файла.
# Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV файл.
# JSON файл содержит данные о продуктах (название, цена, количество на складе).
# В CSV файле каждая строка должна соответствовать одному продукту.

import json
import csv
from pathlib import Path


def json_to_csv(json_file: Path, csv_file: Path) -> None:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(csv_file, 'w', newline='') as f:
        field_names = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=field_names, dialect='excel-tab')
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    json_to_csv('products.json', 'products.csv')
