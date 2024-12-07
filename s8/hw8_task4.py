# Задача 4. Агрегирование данных из CSV файла.
# Напишите скрипт, который считывает данные из CSV файла, содержащего информацию
# о продажах (название продукта, количество, цена за единицу), и подсчитывает
# общую выручку для каждого продукта. Итог должен быть сохранён в новом CSV файле.
# Пример: Из файла sales.csv нужно создать файл total_sales.csv,
# где для каждого продукта будет указана общая выручка.

import csv
from pathlib import Path


def scv_update(input_file: Path, output_file: Path) -> None:
    total_sales = {}
    with open(input_file, 'r', newline='', encoding='utf-8') as file_read:
        data = csv.DictReader(file_read)

        for row in data:
            product = row['product']
            total = int(row['quantity']) * float(row['price'])
            if product not in total_sales:
                total_sales[product] = total
            else:
                total_sales[product] += total

    with open(output_file, 'w', newline='') as f:
        field_names = ['product', 'total_sales']
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        for product, total in total_sales.items():
            writer.writerow({'product': product, 'total_sales': total})


if __name__ == '__main__':
    scv_update('sales.csv', 'total_sales.csv')
