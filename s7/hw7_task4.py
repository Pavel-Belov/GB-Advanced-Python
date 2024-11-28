# Задача 4. Поиск файлов по расширению.
# Напишите функцию, которая находит и перечисляет все файлы с заданным
# расширением в указанном каталоге и всех его подкаталогах.
# Функция должна принимать путь к каталогу и расширение файла.

from pathlib import Path


def search_files_by_extensions(path: Path, ext: str) -> None:
    for file in path.rglob('*'):
        if file.suffix == ext:
            print(file.name)


if __name__ == '__main__':
    search_files_by_extensions(Path.cwd() / 'new', '.txt')
