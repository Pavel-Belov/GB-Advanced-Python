# Задание 1. Функцию группового переименования файлов.
# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени.
# Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# 6. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from os import chdir
from pathlib import Path


def batch_rename_files(
        path: Path,
        end_name: str,
        num_digits: int,
        source_ext: str,
        final_ext: str,
        name_range: list[int]
) -> None:
    chdir(path)
    if not path.is_dir():
        raise FileNotFoundError(f'Каталог {path} не найден.')

    files_list = [file for file in path.iterdir() if file.suffix == f'.{source_ext}']

    if not files_list:
        print(f'Файлы с расширением {source_ext} не найдены.')

    for index, file in enumerate(files_list, start=1):
        source_name = file.stem

        if name_range:
            start, end = name_range
            final_name = source_name[start - 1:end]
        else:
            final_name = source_name

        if final_name:
            final_name += end_name

        final_name += f'{index:0{num_digits}}'

        if final_ext:
            file.rename(f'{final_name}.{final_ext}')
        else:
            file.rename(f'{final_name}.{file.suffix}')


if __name__ == '__main__':
    batch_rename_files(
        Path.cwd(),
        '1_hw7_',
        10,
        'doc',
        'txt',
        [1, 4]
    )
