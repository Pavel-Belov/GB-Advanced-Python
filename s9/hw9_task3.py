# Задача 3. Счётчик.
# Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.
# Для решения задачи нельзя использовать операторы global и nonlocal.
# Пример: Из файла products.json нужно создать products.csv.
import csv
import json
from pathlib import Path
from typing import Callable


def deco_counter(num: int):
    def deco(func: Callable):
        counter = []

        def wrapper(*args, **kwargs):
            for count in range(1, num + 1):
                print(f'Запустили функцию {func.__name__} {count} раз')
                res = func(*args, **kwargs)
                counter.append(res)
            return counter

        return wrapper

    return deco


@deco_counter(5)
def json_to_csv(input_file: Path, output_file: Path) -> None:
    with (
        open(input_file, 'r', encoding='utf-8') as json_file,
        open(output_file, 'w', newline='', encoding='utf-8') as csv_file
    ):
        data = json.load(json_file)
        field_names = data[0].keys()
        csv_write = csv.DictWriter(csv_file, fieldnames=field_names, dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
    json_to_csv(Path('products.json'), Path('products.csv'))
