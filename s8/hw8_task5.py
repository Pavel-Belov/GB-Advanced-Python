# Задача 5. Конвертация CSV в JSON с изменением структуры данных.
# Напишите скрипт, который считывает данные из CSV файла и сохраняет их в JSON файл
# с другой структурой. CSV файл содержит данные о книгах (название, автор, год издания).
# В JSON файле данные должны быть сгруппированы по авторам,
# а книги каждого автора должны быть записаны как список.
# Пример: Из файла books.csv нужно создать файл books_by_author.json,
# где книги сгруппированы по авторам.

import csv
import json
from pathlib import Path


def csv_to_json(csv_file: Path, json_file: Path) -> None:
    authors = {}
    with open(csv_file, 'r', newline='', encoding='utf-8') as csv_f:
        data = csv.DictReader(csv_f)

        for row in data:
            author = row['author']
            book = {
                'name': row['name'],
                'year': row['year']
            }

            if author not in authors:
                authors[author] = [book]
            else:
                authors[author].append(book)

    with open(json_file, 'w', encoding='utf-8') as json_f:
        json.dump(authors, json_f, indent=4)


if __name__ == '__main__':
    csv_to_json('books.csv', 'books_by_author.json')
