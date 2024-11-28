# Задача 3. Удаление старых файлов.
# Напишите скрипт, который удаляет файлы в указанном каталоге,
# которые не изменялись более заданного количества дней.
# Скрипт должен принимать путь к каталогу и количество дней.

import os
from time import time
from pathlib import Path


def del_old_files(path: Path, days_old: int) -> None:
    cutoff = time() - (days_old * 24 * 60 * 60)

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_mod_time = os.path.getmtime(file_path)
            if file_mod_time < cutoff:
                os.remove(file_path)
                print(f"Удален файл: {file_path}")


if __name__ == '__main__':
    del_old_files('your_dir', 10)
