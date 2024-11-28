# Задача 2. Создание архива каталога.
# Напишите скрипт, который создает архив каталога в формате .zip.
# Скрипт должен принимать путь к исходному каталогу и путь к целевому архиву.
# Архив должен включать все файлы и подпапки исходного каталога.

from pathlib import Path
import os
import zipfile


def zip_dir(path: Path, output_zip: Path) -> None:
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in path.rglob('*'):
            zf.write(file, os.path.relpath(file, path))


if __name__ == '__main__':
    source = 'your_dir'
    output = 'your_zip_file.zip'
    zip_dir(source, output)
