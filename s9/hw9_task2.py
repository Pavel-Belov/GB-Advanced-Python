# Задача 2. Замедление кода.
# В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
# Типичный пример — функция, которая постоянно проверяет, изменились ли данные
# на веб-странице или её код.
# Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.

from time import sleep
from typing import Callable


def slowdown(sleep_time: float):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            print(f'Выполнение функции {func.__name__} задержится на {sleep_time} секунд')
            sleep(sleep_time)
            print('Время вышло, запускаем код функции')
            result = func(*args, **kwargs)
            return result

        return wrapper

    return deco


@slowdown(2.5)
def test():
    print('<Тут что-то происходит...>')


if __name__ == '__main__':
    test()
